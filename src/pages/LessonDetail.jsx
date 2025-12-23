import React, { useState, useEffect, useRef, useMemo } from "react";
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
  import.meta.url
).toString();

const LessonDetail = () => {
  const { themeSlug, lessonSlug } = useParams();
  const [activeTab, setActiveTab] = useState("materi");

  // Audio State
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [isPaused, setIsPaused] = useState(false);
  const [speechRate, setSpeechRate] = useState(1);
  const [audioSections, setAudioSections] = useState([]);
  const [showAudioPanel, setShowAudioPanel] = useState(false);
  const [currentSectionIndex, setCurrentSectionIndex] = useState(-1);
  const [pendingSectionIndex, setPendingSectionIndex] = useState(-1);

  // Quiz State
  const [quizAnswers, setQuizAnswers] = useState({});
  const [quizSubmitted, setQuizSubmitted] = useState(false);
  const [quizScore, setQuizScore] = useState(0);

  // PDF State
  const [numPages, setNumPages] = useState(null);
  const [pageNumber, setPageNumber] = useState(1);

  const contentRef = useRef(null);
  const speechRef = useRef(null); // To store the current utterance
  const synth = window.speechSynthesis;
  const audioSegmentsRef = useRef([]);
  const currentSegmentIndexRef = useRef(0);
  const isPlayingRef = useRef(false); // Track playback state safely

  const theme = courseData.find((t) => t.id === themeSlug);

  // Flatten topics to find current, next, prev
  const allTopics = theme
    ? theme.subjects.flatMap((subject) => subject.topics)
    : [];

  const currentTopicIndex = allTopics.findIndex(
    (t) => String(t.id) === lessonSlug
  );
  const lesson = allTopics[currentTopicIndex];

  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const highlightTerm = searchParams.get("highlight");

  // Pre-process content to ensure IDs are stable and apply highlighting
  const processedContent = useMemo(() => {
    if (!lesson?.content) return "";

    const div = document.createElement("div");
    div.innerHTML = lesson.content;

    // 1. ID Injection
    let sectionCount = 0;
    const processNode = (node) => {
      if (node.tagName === "H2" || node.tagName === "H3") {
        // Always assign a consistent ID based on order if not present
        if (!node.id) {
          node.id = `section-${sectionCount}`;
          sectionCount++;
        }
      }
      if (node.children) {
        Array.from(node.children).forEach(processNode);
      }
    };
    Array.from(div.children).forEach(processNode);

    // 2. Highlighting
    if (highlightTerm) {
      const term = highlightTerm.toLowerCase();
      // Escape special regex characters
      const escapedTerm = term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

      const highlightText = (node) => {
        if (node.nodeType === 3) {
          // Text node
          const text = node.nodeValue;
          if (text.toLowerCase().includes(term)) {
            const regex = new RegExp(`(${escapedTerm})`, "gi");
            const parts = text.split(regex);
            const fragment = document.createDocumentFragment();

            parts.forEach((part) => {
              if (part.toLowerCase() === term) {
                const mark = document.createElement("span");
                mark.className =
                  "bg-yellow-300 text-gray-900 font-medium px-1 rounded-sm";
                mark.textContent = part;
                fragment.appendChild(mark);
              } else {
                fragment.appendChild(document.createTextNode(part));
              }
            });

            node.parentNode.replaceChild(fragment, node);
          }
        } else if (
          node.nodeType === 1 &&
          node.tagName !== "SCRIPT" &&
          node.tagName !== "STYLE"
        ) {
          // Element node, recurse
          Array.from(node.childNodes).forEach(highlightText);
        }
      };
      Array.from(div.childNodes).forEach(highlightText);
    }

    return div.innerHTML;
  }, [lesson, highlightTerm]);

  // --- Audio Logic ---

  // Parse content for audio sections
  useEffect(() => {
    if (activeTab === "materi" && contentRef.current && lesson) {
      // Small timeout to ensure DOM is ready
      setTimeout(() => {
        const sections = parseContentForAudio(contentRef.current);
        setAudioSections(sections);
      }, 100);
    }
  }, [lesson, activeTab]);

  // Handle pending audio section (when switching from another tab)
  useEffect(() => {
    if (
      pendingSectionIndex !== -1 &&
      audioSections.length > 0 &&
      activeTab === "materi" &&
      contentRef.current
    ) {
      // Add extra delay to ensure DOM is fully updated after tab switch
      setTimeout(() => {
        const index = pendingSectionIndex;

        // Stop current
        synth.cancel();

        // Build segments from this section onwards
        let segments = [];
        for (let i = index; i < audioSections.length; i++) {
          segments = segments.concat(audioSections[i].segments);
        }

        audioSegmentsRef.current = segments;
        currentSegmentIndexRef.current = 0;
        setCurrentSectionIndex(index);

        // Highlight section title
        const section = audioSections[index];

        // Try to find element by ID first (more reliable if re-rendered)
        let element = section.id ? document.getElementById(section.id) : null;

        if (!element && section.element) {
          element = section.element;
        }

        if (element) {
          element.scrollIntoView({ behavior: "smooth", block: "start" });
          // Add temporary highlight class or style
          const originalColor = element.style.color;
          element.style.transition = "color 0.5s";
          element.style.color = "#059669"; // Emerald-600
          setTimeout(() => {
            element.style.color = originalColor;
          }, 1500);
        }

        setIsSpeaking(true);
        setIsPaused(false);
        playNextSegment();

        // Reset pending
        setPendingSectionIndex(-1);
      }, 300);
    }
  }, [audioSections, pendingSectionIndex, activeTab]);

  // Stop audio on unmount or lesson change
  useEffect(() => {
    return () => {
      stopSpeaking();
    };
  }, [lessonSlug]);

  // Ensure audio stops when navigating away (component unmount)
  useEffect(() => {
    return () => {
      window.speechSynthesis.cancel();
      isPlayingRef.current = false;
    };
  }, []);

  const parseContentForAudio = (root) => {
    const sections = [];
    let currentSection = {
      title: "Pembukaan",
      segments: [],
      id: "section-intro",
      element: root.firstElementChild,
    };

    const addSegment = (text, lang) => {
      if (!text || text.trim().length === 0) return;
      if (lang === "id-ID") {
        // Split by punctuation for better pacing
        const chunks = text.match(/[^.!?]+[.!?]+|[^.!?]+$/g) || [text];
        chunks.forEach((c) => {
          if (c.trim())
            currentSection.segments.push({ text: c.trim(), lang: "id-ID" });
        });
      } else {
        currentSection.segments.push({ text: text.trim(), lang: "ar-SA" });
      }
    };

    const processNode = (node) => {
      if (node.style && node.style.display === "none") return;
      if (node.classList && node.classList.contains("toc-list")) return;

      if (node.tagName === "H2" || node.tagName === "H3") {
        if (currentSection.segments.length > 0) sections.push(currentSection);

        // ID should already be there from processedContent
        const sectionId = node.id || `section-${sections.length}`;

        currentSection = {
          title: node.innerText,
          segments: [],
          id: sectionId,
          element: node,
        };
      } else if (node.classList && node.classList.contains("quran-quote")) {
        const arabic = node.querySelector(".arabic");
        if (arabic) addSegment(arabic.innerText, "ar-SA");
        const trans = node.querySelector(".translation");
        if (trans) addSegment(trans.innerText, "id-ID");
      } else if (node.tagName === "DIV" || node.tagName === "SECTION") {
        Array.from(node.children).forEach(processNode);
      } else if (
        node.tagName === "P" ||
        node.tagName === "LI" ||
        node.tagName === "STRONG"
      ) {
        if (!node.closest(".quran-quote")) {
          if (
            !node.classList.contains("arabic") &&
            !node.classList.contains("translation") &&
            !node.classList.contains("source")
          ) {
            addSegment(node.innerText, "id-ID");
          }
        }
      } else if (node.tagName === "UL" || node.tagName === "OL") {
        Array.from(node.children).forEach(processNode);
      }
    };

    Array.from(root.children).forEach(processNode);
    if (currentSection.segments.length > 0) sections.push(currentSection);
    return sections;
  };

  const getVoices = () => {
    return synth.getVoices();
  };

  const playNextSegment = () => {
    if (!isPlayingRef.current) return;

    if (currentSegmentIndexRef.current >= audioSegmentsRef.current.length) {
      setIsSpeaking(false);
      setIsPaused(false);
      isPlayingRef.current = false;
      return;
    }

    const seg = audioSegmentsRef.current[currentSegmentIndexRef.current];
    const utterance = new SpeechSynthesisUtterance(seg.text);
    const voices = getVoices();

    let selectedVoice = null;
    if (seg.lang === "ar-SA") {
      selectedVoice = voices.find((v) => v.lang.includes("ar"));
    } else {
      selectedVoice =
        voices.find((v) => v.lang === "id-ID") ||
        voices.find(
          (v) => v.lang.replace("_", "-").toLowerCase() === "id-id"
        ) ||
        voices.find((v) => v.name.toLowerCase().includes("indonesia")) ||
        voices.find((v) => v.lang.includes("id"));
    }

    if (selectedVoice) utterance.voice = selectedVoice;
    utterance.lang = seg.lang || "id-ID";
    utterance.rate = speechRate;

    utterance.onend = () => {
      if (isPlayingRef.current) {
        currentSegmentIndexRef.current++;
        playNextSegment();
      }
    };

    utterance.onerror = (e) => {
      console.error("Audio error", e);
      if (
        e.error !== "interrupted" &&
        e.error !== "canceled" &&
        isPlayingRef.current
      ) {
        currentSegmentIndexRef.current++;
        playNextSegment();
      }
    };

    speechRef.current = utterance;
    synth.speak(utterance);
  };

  const playSection = (index) => {
    setShowAudioPanel(false);

    if (activeTab !== "materi") {
      setActiveTab("materi");
      setPendingSectionIndex(index);
      return;
    }

    // Stop current
    synth.cancel();

    // Build segments from this section onwards
    let segments = [];
    for (let i = index; i < audioSections.length; i++) {
      segments = segments.concat(audioSections[i].segments);
    }

    audioSegmentsRef.current = segments;
    currentSegmentIndexRef.current = 0;
    setCurrentSectionIndex(index);

    // Highlight section title
    const section = audioSections[index];

    // Try to find element by ID first (more reliable if re-rendered)
    let element = section.id ? document.getElementById(section.id) : null;

    if (!element && section.element) {
      element = section.element;
    }

    if (element) {
      element.scrollIntoView({ behavior: "smooth", block: "start" });
      // Add temporary highlight class or style
      const originalColor = element.style.color;
      element.style.transition = "color 0.5s";
      element.style.color = "#059669"; // Emerald-600
      setTimeout(() => {
        element.style.color = originalColor;
      }, 1500);
    }

    setIsSpeaking(true);
    setIsPaused(false);
    isPlayingRef.current = true;
    playNextSegment();
  };

  const toggleSpeech = () => {
    if (isSpeaking) {
      if (isPaused) {
        synth.resume();
        setIsPaused(false);
      } else {
        synth.pause();
        setIsPaused(true);
      }
    } else {
      // Start from beginning if nothing playing
      if (audioSections.length > 0) {
        playSection(0);
      }
    }
  };

  const stopSpeaking = () => {
    isPlayingRef.current = false;
    synth.cancel();
    setIsSpeaking(false);
    setIsPaused(false);
    currentSegmentIndexRef.current = 0;
  };

  const toggleSpeed = () => {
    const newRate = speechRate === 1 ? 1.5 : speechRate === 1.5 ? 2 : 1;
    setSpeechRate(newRate);
    // If playing, we need to restart current segment with new rate
    if (isSpeaking && !isPaused) {
      synth.cancel();
      playNextSegment();
    }
  };

  // --- PDF Logic ---
  function onDocumentLoadSuccess({ numPages }) {
    setNumPages(numPages);
    setPageNumber(1);
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
      // Data uses 1-based index for 'correct'
      const correctIndex = q.correct - 1;
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
      <div className="min-h-screen flex flex-col bg-white font-sans">
        <Navbar />
        <div className="grow flex items-center justify-center">
          <div className="text-center">
            <h1 className="text-4xl font-bold text-gray-900 mb-4">
              Pelajaran Tidak Ditemukan
            </h1>
            <Link
              to={`/qthematic/${themeSlug}`}
              className="text-emerald-600 hover:underline"
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
    <div className="min-h-screen flex flex-col bg-white font-sans">
      <Navbar />

      <main className="grow container mx-auto px-6 pt-24 pb-8 relative">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Main Content */}
          <div className="lg:col-span-2">
            {/* Header & Audio Controls */}
            <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-6 gap-4 bg-white p-4 rounded-xl border border-gray-100 shadow-sm sticky top-20 z-30">
              <div>
                <h1 className="text-2xl font-bold text-gray-900">
                  {lesson.title}
                </h1>
                <p className="text-sm text-gray-500 mt-1">
                  Interactive Learning Module
                </p>
              </div>
              <div className="flex items-center gap-2">
                <button
                  onClick={() => setShowAudioPanel(true)}
                  className="px-4 py-2 bg-emerald-50 text-emerald-700 rounded-lg hover:bg-emerald-100 transition-colors text-sm font-medium flex items-center gap-2"
                >
                  <svg
                    className="w-4 h-4"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M4 6h16M4 12h16M4 18h16"
                    />
                  </svg>
                  Daftar Audio
                </button>
                <div className="h-8 w-px bg-gray-200 mx-2"></div>
                <button
                  onClick={toggleSpeech}
                  className={`w-10 h-10 rounded-full flex items-center justify-center transition-colors ${
                    isSpeaking && !isPaused
                      ? "bg-emerald-100 text-emerald-600"
                      : "bg-gray-100 text-gray-600 hover:bg-gray-200"
                  }`}
                  title={isSpeaking && !isPaused ? "Jeda" : "Putar"}
                >
                  {isSpeaking && !isPaused ? (
                    <svg
                      className="w-4 h-4"
                      fill="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path d="M6 4h4v16H6V4zm8 0h4v16h-4V4z" />
                    </svg>
                  ) : (
                    <svg
                      className="w-4 h-4 ml-0.5"
                      fill="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path d="M8 5v14l11-7z" />
                    </svg>
                  )}
                </button>
                <button
                  onClick={stopSpeaking}
                  className="w-10 h-10 rounded-full bg-gray-100 text-gray-600 hover:bg-gray-200 flex items-center justify-center transition-colors"
                  title="Berhenti"
                >
                  <svg
                    className="w-4 h-4"
                    fill="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path d="M6 6h12v12H6z" />
                  </svg>
                </button>
                <button
                  onClick={toggleSpeed}
                  className="w-10 h-10 rounded-full bg-gray-100 text-gray-600 hover:bg-gray-200 flex items-center justify-center text-xs font-bold transition-colors"
                  title="Kecepatan"
                >
                  {speechRate}x
                </button>
              </div>
            </div>

            {/* Tabs */}
            <div className="flex gap-2 mb-6 overflow-x-auto pb-2 mt-8">
              <button
                onClick={() => setActiveTab("materi")}
                className={`px-6 py-3 rounded-lg font-medium transition-all whitespace-nowrap flex items-center gap-2 ${
                  activeTab === "materi"
                    ? "bg-emerald-600 text-white shadow-lg shadow-emerald-600/20"
                    : "bg-white text-gray-600 hover:bg-gray-50 border border-gray-200"
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
                    d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
                  />
                </svg>
                Materi Pelajaran
              </button>
              <button
                onClick={() => setActiveTab("pdf")}
                className={`px-6 py-3 rounded-lg font-medium transition-all whitespace-nowrap flex items-center gap-2 ${
                  activeTab === "pdf"
                    ? "bg-emerald-600 text-white shadow-lg shadow-emerald-600/20"
                    : "bg-white text-gray-600 hover:bg-gray-50 border border-gray-200"
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
                    ? "bg-emerald-600 text-white shadow-lg shadow-emerald-600/20"
                    : "bg-white text-gray-600 hover:bg-gray-50 border border-gray-200"
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
            <div className="bg-white rounded-2xl p-8 shadow-lg border border-gray-200 mb-8 min-h-[500px]">
              {activeTab === "materi" && (
                <div
                  ref={contentRef}
                  className="lesson-content"
                  dangerouslySetInnerHTML={{ __html: processedContent }}
                />
              )}

              {activeTab === "pdf" && (
                <div className="flex flex-col items-center bg-gray-100 rounded-xl p-6 min-h-[600px]">
                  {lesson.file ? (
                    <div className="w-full max-w-4xl flex flex-col items-center">
                      {/* PDF Controls */}
                      <div className="bg-white rounded-full shadow-md px-8 py-3 mb-8 flex items-center justify-between gap-6 sticky top-4 z-10">
                        <button
                          type="button"
                          disabled={pageNumber <= 1}
                          onClick={previousPage}
                          className="flex items-center px-5 py-2 bg-blue-600 text-white rounded-full text-sm font-bold hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-all shadow-sm"
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

                        <span className="text-gray-700 font-bold text-lg min-w-[100px] text-center">
                          Page {pageNumber} / {numPages || "--"}
                        </span>

                        <button
                          type="button"
                          disabled={pageNumber >= numPages}
                          onClick={nextPage}
                          className="flex items-center px-5 py-2 bg-blue-600 text-white rounded-full text-sm font-bold hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-all shadow-sm"
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
                      <div className="shadow-2xl rounded-lg overflow-hidden bg-white border border-gray-200">
                        <Document
                          file={`/pdf/${lesson.file}`}
                          onLoadSuccess={onDocumentLoadSuccess}
                          loading={
                            <div className="flex flex-col items-center justify-center h-96 w-[600px]">
                              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-emerald-600 mb-4"></div>
                              <p className="text-gray-500">
                                Memuat dokumen PDF...
                              </p>
                            </div>
                          }
                          error={
                            <div className="text-red-500 p-12 text-center bg-red-50">
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
                            renderTextLayer={false}
                            renderAnnotationLayer={false}
                            width={Math.min(window.innerWidth * 0.8, 800)}
                            className="max-w-full"
                          />
                        </Document>
                      </div>
                    </div>
                  ) : (
                    <div className="flex items-center justify-center h-full text-gray-500">
                      PDF tidak tersedia untuk materi ini.
                    </div>
                  )}
                </div>
              )}

              {activeTab === "quiz" && (
                <div className="max-w-2xl mx-auto">
                  <div className="text-center mb-8">
                    <h3 className="text-2xl font-bold text-gray-900 mb-2">
                      Uji Pemahaman Materi
                    </h3>
                    <p className="text-gray-500">
                      Jawab pertanyaan berikut untuk menguji pemahaman Anda.
                    </p>
                    {quizSubmitted && (
                      <div className="mt-4 inline-block px-6 py-2 bg-emerald-100 text-emerald-700 rounded-full font-bold text-lg">
                        Skor Anda: {quizScore} / {lesson.quiz?.length || 0}
                      </div>
                    )}
                  </div>

                  {lesson.quiz && lesson.quiz.length > 0 ? (
                    <div className="space-y-8">
                      {lesson.quiz.map((q, qIndex) => (
                        <div
                          key={qIndex}
                          className="bg-gray-50 p-6 rounded-xl border border-gray-200"
                        >
                          <p className="font-semibold text-gray-900 mb-4 text-lg">
                            {qIndex + 1}. {q.question}
                          </p>
                          <div className="space-y-3">
                            {q.options.map((option, oIndex) => {
                              // Data uses 1-based index for 'correct'
                              const correctIndex = q.correct - 1;

                              let optionClass =
                                "w-full text-left p-4 rounded-lg border transition-all ";
                              if (quizSubmitted) {
                                if (oIndex === correctIndex) {
                                  optionClass +=
                                    "bg-emerald-100 border-emerald-500 text-emerald-700 font-medium";
                                } else if (
                                  quizAnswers[qIndex] === oIndex &&
                                  oIndex !== correctIndex
                                ) {
                                  optionClass +=
                                    "bg-red-100 border-red-500 text-red-700";
                                } else {
                                  optionClass +=
                                    "bg-white border-gray-200 opacity-50";
                                }
                              } else {
                                if (quizAnswers[qIndex] === oIndex) {
                                  optionClass +=
                                    "bg-emerald-50 border-emerald-500 text-emerald-700 shadow-sm ring-1 ring-emerald-500";
                                } else {
                                  optionClass +=
                                    "bg-white border-gray-200 hover:bg-gray-50 hover:border-gray-300";
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
                                          ? "bg-emerald-500 border-emerald-500 text-white"
                                          : quizAnswers[qIndex] === oIndex
                                          ? quizSubmitted &&
                                            oIndex !== correctIndex
                                            ? "bg-red-500 border-red-500 text-white"
                                            : "bg-emerald-500 border-emerald-500 text-white"
                                          : "border-gray-300"
                                      }`}
                                    >
                                      {String.fromCharCode(65 + oIndex)}
                                    </div>
                                    {option}
                                  </div>
                                </button>
                              );
                            })}
                          </div>

                          {quizSubmitted && q.explanation && (
                            <div className="mt-6 p-5 bg-slate-800 rounded-xl border-l-4 border-yellow-400 shadow-md">
                              <h4 className="text-yellow-400 font-bold mb-2 flex items-center">
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
                                    d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                                  />
                                </svg>
                                Penjelasan:
                              </h4>
                              <p className="text-slate-200 leading-relaxed">
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
                            className="px-8 py-3 bg-emerald-600 text-white rounded-full font-bold hover:bg-emerald-700 disabled:opacity-50 disabled:cursor-not-allowed shadow-lg shadow-emerald-600/20 transition-all"
                          >
                            Cek Jawaban
                          </button>
                        ) : (
                          <button
                            onClick={resetQuiz}
                            className="px-8 py-3 bg-white border-2 border-emerald-600 text-emerald-600 rounded-full font-bold hover:bg-emerald-50 transition-all"
                          >
                            Ulangi Quiz
                          </button>
                        )}
                      </div>
                    </div>
                  ) : (
                    <div className="text-center py-12 text-gray-500">
                      Belum ada quiz untuk materi ini.
                    </div>
                  )}
                </div>
              )}
            </div>

            {/* Navigation Buttons */}
            <div className="flex justify-between mt-12 pt-8 border-t border-gray-100">
              {prevLesson ? (
                <Link
                  to={`/qthematic/${themeSlug}/${prevLesson.id}`}
                  className="flex items-center px-6 py-3 bg-white border border-gray-200 rounded-full text-gray-700 font-semibold hover:bg-gray-50 hover:border-gray-300 transition-all"
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
                  className="flex items-center px-6 py-3 bg-emerald-600 text-white rounded-full font-semibold hover:bg-emerald-700 shadow-lg shadow-emerald-600/20 transition-all"
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
                  className="flex items-center px-6 py-3 bg-emerald-600 text-white rounded-full font-semibold hover:bg-emerald-700 shadow-lg shadow-emerald-600/20 transition-all"
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
            <div className="bg-gray-50 rounded-2xl p-6 border border-gray-100 sticky top-24 max-h-[calc(100vh-8rem)] overflow-y-auto">
              <h3 className="text-lg font-bold text-gray-900 mb-4">
                Daftar Materi
              </h3>
              <div className="space-y-6">
                {theme.subjects.map((subject) => (
                  <div key={subject.id}>
                    <h4 className="text-sm font-bold text-emerald-700 uppercase tracking-wider mb-2">
                      {subject.title}
                    </h4>
                    <div className="space-y-2">
                      {subject.topics.map((topic, index) => (
                        <Link
                          key={topic.id}
                          to={`/qthematic/${themeSlug}/${topic.id}`}
                          className={`block p-3 rounded-lg transition-colors ${
                            String(topic.id) === lessonSlug
                              ? "bg-emerald-100 text-emerald-700 font-medium"
                              : "hover:bg-white hover:shadow-sm text-gray-600"
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

        {/* Audio Panel Overlay */}
        {showAudioPanel && (
          <div className="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4 backdrop-blur-sm">
            <div className="bg-white rounded-2xl shadow-2xl w-full max-w-md max-h-[80vh] flex flex-col">
              <div className="p-6 border-b border-gray-100 flex justify-between items-center">
                <h3 className="text-xl font-bold text-gray-900">
                  Daftar Bagian Audio
                </h3>
                <button
                  onClick={() => setShowAudioPanel(false)}
                  className="text-gray-400 hover:text-gray-600"
                >
                  <svg
                    className="w-6 h-6"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M6 18L18 6M6 6l12 12"
                    />
                  </svg>
                </button>
              </div>
              <div className="overflow-y-auto p-4 space-y-2">
                {audioSections.map((section, index) => (
                  <button
                    key={index}
                    onClick={() => playSection(index)}
                    className={`w-full text-left p-4 rounded-xl transition-all ${
                      currentSectionIndex === index && isSpeaking
                        ? "bg-emerald-100 text-emerald-700 font-bold border border-emerald-200"
                        : "bg-gray-50 text-gray-700 hover:bg-gray-100 border border-transparent"
                    }`}
                  >
                    {section.title}
                  </button>
                ))}
                {audioSections.length === 0 && (
                  <p className="text-center text-gray-500 py-8">
                    Tidak ada bagian audio yang terdeteksi.
                  </p>
                )}
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
};

export default LessonDetail;
