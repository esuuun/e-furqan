import React, { useState, useEffect, useCallback } from "react";
import { useParams, Link, useLocation } from "react-router-dom";
import { Document, Page, pdfjs } from "react-pdf";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import courseData from "../data/thematicData";

// Configure PDF worker
import "react-pdf/dist/Page/AnnotationLayer.css";
import "react-pdf/dist/Page/TextLayer.css";

pdfjs.GlobalWorkerOptions.workerSrc = new URL(
  "pdfjs-dist/build/pdf.worker.min.mjs",
  import.meta.url,
).toString();

const LessonDetail = () => {
  const { themeSlug, lessonSlug } = useParams();
  const [activeTab, setActiveTab] = useState("quiz");

  // Quiz State
  const [quizAnswers, setQuizAnswers] = useState({});
  const [quizSubmitted, setQuizSubmitted] = useState(false);
  const [quizScore, setQuizScore] = useState(0);

  // PDF State
  const [numPages, setNumPages] = useState(null);
  const [pageNumber, setPageNumber] = useState(1);

  const theme = courseData.find((t) => t.id === themeSlug);

  // Flatten topics to find current, next, prev
  const allTopics = theme
    ? theme.subjects.flatMap((subject) => subject.topics)
    : [];

  const currentTopicIndex = allTopics.findIndex(
    (t) => String(t.id) === lessonSlug,
  );
  const lesson = allTopics[currentTopicIndex];

  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const highlightTerm = searchParams.get("highlight");

  // Helper to construct normalized regex for highlight matches (q/k interchangeability)
  const getHighlightRegex = useCallback((term, flags = "gi") => {
    if (!term) return null;
    let pattern = term.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
    pattern = pattern.replace(/q/gi, '[qk]').replace(/k/gi, '[qk]');
    return new RegExp(`(${pattern})`, flags);
  }, []);

  // PDF Text highlighting renderer - must return a string (HTML) since react-pdf uses innerHTML
  const textRenderer = useCallback(
    ({ str }) => {
      if (!highlightTerm) return str;

      // Escape HTML entities to prevent XSS
      const escapeHtml = (s) =>
        s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

      const escapedStr = escapeHtml(str);

      // Build pattern with q/k interchangeability for Indonesian/Arabic transliteration
      let pattern = highlightTerm.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
      pattern = pattern.replace(/q/gi, '[qk]').replace(/k/gi, '[qk]');
      const regex = new RegExp(`(${pattern})`, 'gi');

      const result = escapedStr.replace(regex, '<mark>$1</mark>');
      // If no match, return original str (not escaped, to preserve original content)
      return result !== escapedStr ? result : str;
    },
    [highlightTerm]
  );

  // Helper to find the first page containing the term
  const findFirstPageWithTerm = useCallback(async (pdf, term) => {
    try {
      const regex = getHighlightRegex(term, "i");
      if (!regex) return 1;

      for (let i = 1; i <= pdf.numPages; i++) {
        const page = await pdf.getPage(i);
        const textContent = await page.getTextContent();
        const itemsStr = textContent.items.map(item => item.str);
        const textWithSpaces = itemsStr.join(" ");
        const textWithoutSpaces = itemsStr.join("");

        if (regex.test(textWithSpaces) || regex.test(textWithoutSpaces)) {
          return i;
        }
      }
    } catch (error) {
      console.error("Error searching PDF text:", error);
    }
    return 1;
  }, [getHighlightRegex]);

  // Redirect to pdf tab if highlight search is present
  useEffect(() => {
    if (highlightTerm) {
      setActiveTab("pdf");
    }
  }, [lesson, highlightTerm]);


  // --- PDF Logic ---
  function onDocumentLoadSuccess(pdf) {
    setNumPages(pdf.numPages);
    if (highlightTerm) {
      findFirstPageWithTerm(pdf, highlightTerm)
        .then((pageIndex) => {
          setPageNumber(pageIndex);
        })
        .catch(() => {
          setPageNumber(1);
        });
    } else {
      setPageNumber(1);
    }
  }

  function changePage(offset) {
    setPageNumber((prevPageNumber) => prevPageNumber + offset);
  }

  function previousPage() {
    changePage(-1);
  }

  function nextPage() {
    changePage(1);
  }

  // --- Quiz Logic ---
  const handleAnswerSelect = (questionIndex, optionIndex) => {
    if (quizSubmitted) return;
    setQuizAnswers((prev) => ({
      ...prev,
      [questionIndex]: optionIndex,
    }));
  };

  const submitQuiz = () => {
    if (!lesson.quiz) return;
    let correct = 0;
    lesson.quiz.forEach((q, index) => {
      // Data uses 1-based index for 'correct' (or fallback to 0-based 'answer')
      const correctIndex = q.correct !== undefined ? q.correct - 1 : q.answer;
      if (quizAnswers[index] === correctIndex) {
        correct++;
      }
    });
    setQuizScore(correct);
    setQuizSubmitted(true);
  };

  const resetQuiz = () => {
    setQuizAnswers({});
    setQuizSubmitted(false);
    setQuizScore(0);
  };

  if (!theme || !lesson) {
    return (
      <div className="min-h-screen flex flex-col bg-white dark:bg-gray-900 font-sans">
        <Navbar />
        <div className="grow flex items-center justify-center">
          <div className="text-center">
            <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">
              Pelajaran Tidak Ditemukan
            </h1>
            <Link
              to={`/qthematic/${themeSlug}`}
              className="text-emerald-600 dark:text-emerald-400 hover:underline"
            >
              Kembali ke Detail Tema
            </Link>
          </div>
        </div>
        <Footer />
      </div>
    );
  }

  const prevLesson =
    currentTopicIndex > 0 ? allTopics[currentTopicIndex - 1] : null;
  const nextLesson =
    currentTopicIndex < allTopics.length - 1
      ? allTopics[currentTopicIndex + 1]
      : null;

  return (
    <div className="min-h-screen flex flex-col bg-white dark:bg-gray-900 font-sans">
      <Navbar />

      <main className="grow container mx-auto px-6 pt-24 pb-8 relative">
        <Link
          to={`/qthematic/${themeSlug}`}
          className="inline-flex items-center text-gray-500 dark:text-gray-400 hover:text-yellow-600 dark:hover:text-yellow-400 mb-6 transition-colors font-medium"
        >
          <svg
            className="w-5 h-5 mr-2"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M10 19l-7-7m0 0l7-7m-7 7h18"
            ></path>
          </svg>
          Kembali ke Materi Tema
        </Link>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Main Content */}
          <div className="lg:col-span-2">
            {/* Header */}
            <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-6 gap-4 bg-white dark:bg-gray-800 p-4 rounded-xl border border-gray-100 dark:border-gray-700 shadow-sm sticky top-20 z-30">
              <div>
                <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
                  {lesson.title}
                </h1>
                <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
                  Interactive Learning Module
                </p>
              </div>
            </div>

            {/* Tabs */}
            <div className="flex gap-2 mb-6 overflow-x-auto pb-2 mt-8">
              <button
                onClick={() => setActiveTab("pdf")}
                className={`px-6 py-3 rounded-lg font-medium transition-all whitespace-nowrap flex items-center gap-2 ${
                  activeTab === "pdf"
                    ? "bg-yellow-500 dark:bg-yellow-600 text-white shadow-lg shadow-yellow-500/20"
                    : "bg-white dark:bg-gray-800 text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 border border-gray-200 dark:border-gray-700"
                }`}
              >
                <svg
                  className="w-5 h-5"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"
                  />
                </svg>
                PDF Asli
              </button>
              <button
                onClick={() => setActiveTab("quiz")}
                className={`px-6 py-3 rounded-lg font-medium transition-all whitespace-nowrap flex items-center gap-2 ${
                  activeTab === "quiz"
                    ? "bg-yellow-500 dark:bg-yellow-600 text-white shadow-lg shadow-yellow-500/20"
                    : "bg-white dark:bg-gray-800 text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 border border-gray-200 dark:border-gray-700"
                }`}
              >
                <svg
                  className="w-5 h-5"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
                Quiz Interaktif
              </button>
            </div>

            {/* Content Area */}
            <div className="bg-white dark:bg-gray-800 rounded-2xl p-8 shadow-lg border border-gray-200 dark:border-gray-700 mb-8 min-h-[500px]">


              {activeTab === "pdf" && (
                <div className="flex flex-col items-center bg-gray-100 dark:bg-gray-700 rounded-xl p-6 min-h-[600px]">
                  {lesson.file ? (
                    <div className="w-full max-w-4xl flex flex-col items-center">
                      {/* PDF Controls */}
                      <div className="bg-white dark:bg-gray-800 rounded-full shadow-md px-8 py-3 mb-8 flex items-center justify-between gap-6 sticky top-4 z-10">
                        <button
                          type="button"
                          disabled={pageNumber <= 1}
                          onClick={previousPage}
                          className="flex items-center px-5 py-2 bg-blue-600 dark:bg-blue-700 text-white rounded-full text-sm font-bold hover:bg-blue-700 dark:hover:bg-blue-600 disabled:bg-gray-300 dark:disabled:bg-gray-600 disabled:cursor-not-allowed transition-all shadow-sm"
                        >
                          <svg
                            className="w-4 h-4 mr-2"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                          >
                            <path
                              strokeLinecap="round"
                              strokeLinejoin="round"
                              strokeWidth="2"
                              d="M15 19l-7-7 7-7"
                            />
                          </svg>
                          Prev
                        </button>

                        <span className="text-gray-700 dark:text-gray-300 font-bold text-lg min-w-[100px] text-center">
                          Page {pageNumber} / {numPages || "--"}
                        </span>

                        <button
                          type="button"
                          disabled={pageNumber >= numPages}
                          onClick={nextPage}
                          className="flex items-center px-5 py-2 bg-blue-600 dark:bg-blue-700 text-white rounded-full text-sm font-bold hover:bg-blue-700 dark:hover:bg-blue-600 disabled:bg-gray-300 dark:disabled:bg-gray-600 disabled:cursor-not-allowed transition-all shadow-sm"
                        >
                          Next
                          <svg
                            className="w-4 h-4 ml-2"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                          >
                            <path
                              strokeLinecap="round"
                              strokeLinejoin="round"
                              strokeWidth="2"
                              d="M9 5l7 7-7 7"
                            />
                          </svg>
                        </button>
                      </div>

                      {/* PDF Document */}
                      <div className="shadow-2xl rounded-lg overflow-hidden bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700">
                        <Document
                          file={`/pdf/${lesson.file}`}
                          onLoadSuccess={onDocumentLoadSuccess}
                          loading={
                            <div className="flex flex-col items-center justify-center h-96 w-[600px]">
                              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-yellow-500 mb-4"></div>
                              <p className="text-gray-500 dark:text-gray-400">
                                Memuat dokumen PDF...
                              </p>
                            </div>
                          }
                          error={
                            <div className="text-red-500 dark:text-red-400 p-12 text-center bg-red-50 dark:bg-red-900/20">
                              <p className="font-bold text-lg mb-2">
                                Gagal memuat PDF
                              </p>
                              <p className="text-sm">
                                Pastikan file PDF tersedia di folder public/pdf/
                              </p>
                            </div>
                          }
                        >
                          <Page
                            pageNumber={pageNumber}
                            renderTextLayer={true}
                            customTextRenderer={textRenderer}
                            renderAnnotationLayer={false}
                            width={Math.min(window.innerWidth * 0.8, 800)}
                            className="max-w-full"
                          />
                        </Document>
                      </div>
                    </div>
                  ) : (
                    <div className="flex items-center justify-center h-full text-gray-500 dark:text-gray-400">
                      PDF tidak tersedia untuk materi ini.
                    </div>
                  )}
                </div>
              )}

              {activeTab === "quiz" && (
                <div className="max-w-2xl mx-auto">
                  <div className="text-center mb-8">
                    <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-2">
                      Uji Pemahaman Materi
                    </h3>
                    <p className="text-gray-500 dark:text-gray-400">
                      Jawab pertanyaan berikut untuk menguji pemahaman Anda.
                    </p>
                    {quizSubmitted && (
                      <div className="mt-4 inline-block px-6 py-2 bg-yellow-100 dark:bg-yellow-900/50 text-yellow-800 dark:text-yellow-200 rounded-full font-bold text-lg">
                        Skor Anda: {quizScore} / {lesson.quiz?.length || 0}
                      </div>
                    )}
                  </div>

                  {lesson.quiz && lesson.quiz.length > 0 ? (
                    <div className="space-y-8">
                      {lesson.quiz.map((q, qIndex) => (
                        <div
                          key={qIndex}
                          className="bg-gray-50 dark:bg-gray-800 p-6 rounded-xl border border-gray-200 dark:border-gray-700"
                        >
                          <p className="font-semibold text-gray-900 dark:text-white mb-4 text-lg">
                            {qIndex + 1}. {q.question}
                          </p>
                          <div className="space-y-3">
                            {q.options.map((option, oIndex) => {
                              // Data uses 1-based index for 'correct' (or fallback to 0-based 'answer')
                              const correctIndex = q.correct !== undefined ? q.correct - 1 : q.answer;

                              let optionClass =
                                "w-full text-left p-4 rounded-lg border transition-all ";
                              if (quizSubmitted) {
                                if (oIndex === correctIndex) {
                                  optionClass +=
                                    "bg-yellow-100 dark:bg-yellow-900/50 border-yellow-500 dark:border-yellow-500 text-yellow-800 dark:text-yellow-200 font-medium";
                                } else if (
                                  quizAnswers[qIndex] === oIndex &&
                                  oIndex !== correctIndex
                                ) {
                                  optionClass +=
                                    "bg-red-100 dark:bg-red-900/50 border-red-500 dark:border-red-500 text-red-700 dark:text-red-300";
                                } else {
                                  optionClass +=
                                    "bg-white dark:bg-gray-700 border-gray-200 dark:border-gray-600 opacity-50";
                                }
                              } else {
                                if (quizAnswers[qIndex] === oIndex) {
                                  optionClass +=
                                    "bg-yellow-50 dark:bg-yellow-900/20 border-yellow-500 dark:border-yellow-500 text-yellow-800 dark:text-yellow-200 shadow-sm ring-1 ring-yellow-500";
                                } else {
                                  optionClass +=
                                    "bg-white dark:bg-gray-700 border-gray-200 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-600 hover:border-gray-300 dark:hover:border-gray-500";
                                }
                              }

                              return (
                                <button
                                  key={oIndex}
                                  onClick={() =>
                                    handleAnswerSelect(qIndex, oIndex)
                                  }
                                  disabled={quizSubmitted}
                                  className={optionClass}
                                >
                                  <div className="flex items-center">
                                    <div
                                      className={`w-6 h-6 rounded-full border flex items-center justify-center mr-3 ${
                                        quizSubmitted && oIndex === correctIndex
                                          ? "bg-yellow-500 dark:bg-yellow-600 border-yellow-500 dark:border-yellow-600 text-white"
                                          : quizAnswers[qIndex] === oIndex
                                            ? quizSubmitted &&
                                              oIndex !== correctIndex
                                              ? "bg-red-500 dark:bg-red-600 border-red-500 dark:border-red-600 text-white"
                                              : "bg-yellow-500 dark:bg-yellow-600 border-yellow-500 dark:border-yellow-600 text-white"
                                            : "border-gray-300 dark:border-gray-500"
                                      }`}
                                    >
                                      {String.fromCharCode(65 + oIndex)}
                                    </div>
                                    <span className="text-gray-700 dark:text-gray-300">
                                      {option}
                                    </span>
                                  </div>
                                </button>
                              );
                            })}
                          </div>

                          {quizSubmitted && q.explanation && (
                            <div className="mt-6 p-5 bg-yellow-50 dark:bg-yellow-900/20 rounded-xl border border-yellow-200 dark:border-yellow-800 shadow-sm">
                              <h4 className="text-yellow-800 dark:text-yellow-200 font-bold mb-2 flex items-center">
                                <svg
                                  className="w-5 h-5 mr-2 text-yellow-600 dark:text-yellow-400"
                                  fill="none"
                                  stroke="currentColor"
                                  viewBox="0 0 24 24"
                                >
                                  <path
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    strokeWidth="2"
                                    d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                                  />
                                </svg>
                                Penjelasan:
                              </h4>
                              <p className="text-gray-700 dark:text-gray-300 leading-relaxed">
                                {q.explanation}
                              </p>
                            </div>
                          )}
                        </div>
                      ))}

                      <div className="flex justify-center pt-6">
                        {!quizSubmitted ? (
                          <button
                            onClick={submitQuiz}
                            disabled={
                              Object.keys(quizAnswers).length !==
                              lesson.quiz.length
                            }
                            className="px-8 py-3 bg-yellow-500 dark:bg-yellow-600 text-white rounded-full font-bold hover:bg-yellow-600 dark:hover:bg-yellow-500 disabled:opacity-50 disabled:cursor-not-allowed shadow-lg shadow-yellow-500/20 transition-all"
                          >
                            Cek Jawaban
                          </button>
                        ) : (
                          <button
                            onClick={resetQuiz}
                            className="px-8 py-3 bg-white dark:bg-gray-800 border-2 border-yellow-500 dark:border-yellow-600 text-yellow-600 dark:text-yellow-400 rounded-full font-bold hover:bg-yellow-50 dark:hover:bg-yellow-900/20 transition-all"
                          >
                            Ulangi Quiz
                          </button>
                        )}
                      </div>
                    </div>
                  ) : (
                    <div className="text-center py-12 text-gray-500 dark:text-gray-400">
                      Belum ada quiz untuk materi ini.
                    </div>
                  )}
                </div>
              )}
            </div>

            {/* Navigation Buttons */}
            <div className="flex justify-between mt-12 pt-8 border-t border-gray-100 dark:border-gray-700">
              {prevLesson ? (
                <Link
                  to={`/qthematic/${themeSlug}/${prevLesson.id}`}
                  className="flex items-center px-6 py-3 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-full text-gray-700 dark:text-gray-300 font-semibold hover:bg-gray-50 dark:hover:bg-gray-700 hover:border-gray-300 dark:hover:border-gray-600 transition-all"
                >
                  <svg
                    className="w-5 h-5 mr-2"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M15 19l-7-7 7-7"
                    />
                  </svg>
                  Sebelumnya
                </Link>
              ) : (
                <div></div>
              )}

              {nextLesson ? (
                <Link
                  to={`/qthematic/${themeSlug}/${nextLesson.id}`}
                  className="flex items-center px-6 py-3 bg-yellow-500 dark:bg-yellow-600 text-white rounded-full font-semibold hover:bg-yellow-600 dark:hover:bg-yellow-500 shadow-lg shadow-yellow-500/20 transition-all"
                >
                  Selanjutnya
                  <svg
                    className="w-5 h-5 ml-2"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M9 5l7 7-7 7"
                    />
                  </svg>
                </Link>
              ) : (
                <Link
                  to={`/qthematic/${themeSlug}`}
                  className="flex items-center px-6 py-3 bg-yellow-500 dark:bg-yellow-600 text-white rounded-full font-semibold hover:bg-yellow-600 dark:hover:bg-yellow-500 shadow-lg shadow-yellow-500/20 transition-all"
                >
                  Selesai
                  <svg
                    className="w-5 h-5 ml-2"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M5 13l4 4L19 7"
                    />
                  </svg>
                </Link>
              )}
            </div>
          </div>

          {/* Sidebar */}
          <div className="lg:col-span-1">
            <div className="bg-gray-50 dark:bg-gray-800 rounded-2xl p-6 border border-gray-100 dark:border-gray-700 sticky top-24 max-h-[calc(100vh-8rem)] overflow-y-auto">
              <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-4">
                Daftar Materi
              </h3>
              <div className="space-y-6">
                {theme.subjects.map((subject) => (
                  <div key={subject.id}>
                    <h4 className="text-sm font-bold text-yellow-800 dark:text-yellow-200 uppercase tracking-wider mb-2">
                      {subject.title}
                    </h4>
                    <div className="space-y-2">
                      {subject.topics.map((topic, index) => (
                        <Link
                          key={topic.id}
                          to={`/qthematic/${themeSlug}/${topic.id}`}
                          className={`block p-3 rounded-lg transition-colors ${
                            String(topic.id) === lessonSlug
                              ? "bg-yellow-100 dark:bg-yellow-900/50 text-yellow-800 dark:text-yellow-200 font-medium"
                              : "hover:bg-white dark:hover:bg-gray-700 hover:shadow-sm text-gray-600 dark:text-gray-300"
                          }`}
                        >
                          <div className="flex items-start">
                            <span className="text-sm">{topic.title}</span>
                          </div>
                        </Link>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default LessonDetail;
