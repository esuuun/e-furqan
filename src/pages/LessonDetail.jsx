import React from "react";
import { useParams, Link } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

const lessonData = {
  "sifat-allah-bagian-1": {
    title: "Sifat Allah Bagian 1",
    contentUrl:
      "https://qthematic.e-furqan.com/courses/al-quran-tematis-2-2/lessons/sifat-allah-bagian-1/",
    themeSlug: "sifat-allah",
    themeTitle: "Sifat Allah",
    nextLesson: "sifat-allah-bagian-2",
  },
  "sifat-allah-bagian-2": {
    title: "Sifat Allah Bagian 2",
    contentUrl:
      "https://qthematic.e-furqan.com/courses/al-quran-tematis-2-2/lessons/sifat-allah-bagian-2/",
    themeSlug: "sifat-allah",
    themeTitle: "Sifat Allah",
    prevLesson: "sifat-allah-bagian-1",
    nextLesson: "sifat-allah-bagian-3",
  },
  "sifat-allah-bagian-3": {
    title: "Sifat Allah Bagian 3",
    contentUrl:
      "https://qthematic.e-furqan.com/courses/al-quran-tematis-2-2/lessons/sifat-allah-bagian-3/",
    themeSlug: "sifat-allah",
    themeTitle: "Sifat Allah",
    prevLesson: "sifat-allah-bagian-2",
    nextLesson: "sifat-allah-bagian-4",
  },
  "sifat-allah-bagian-4": {
    title: "Sifat Allah Bagian 4",
    contentUrl:
      "https://qthematic.e-furqan.com/courses/al-quran-tematis-2-2/lessons/sifat-allah-bagian-4/",
    themeSlug: "sifat-allah",
    themeTitle: "Sifat Allah",
    prevLesson: "sifat-allah-bagian-3",
    nextLesson: "sifat-allah-bagian-5",
  },
  "sifat-allah-bagian-5": {
    title: "Sifat Allah Bagian 5",
    contentUrl:
      "https://qthematic.e-furqan.com/courses/al-quran-tematis-2-2/lessons/sifat-allah-bagian-5/",
    themeSlug: "sifat-allah",
    themeTitle: "Sifat Allah",
    prevLesson: "sifat-allah-bagian-4",
    nextLesson: "sifat-allah-bagian-6",
  },
  "sifat-allah-bagian-6": {
    title: "Sifat Allah Bagian 6",
    contentUrl:
      "https://qthematic.e-furqan.com/courses/al-quran-tematis-2-2/lessons/sifat-allah-bagian-6/",
    themeSlug: "sifat-allah",
    themeTitle: "Sifat Allah",
    prevLesson: "sifat-allah-bagian-5",
    nextLesson: "sifat-allah-bagian-7",
  },
  "sifat-allah-bagian-7": {
    title: "Sifat Allah Bagian 7",
    contentUrl:
      "https://qthematic.e-furqan.com/courses/al-quran-tematis-2-2/lessons/sifat-allah-bagian-7/",
    themeSlug: "sifat-allah",
    themeTitle: "Sifat Allah",
    prevLesson: "sifat-allah-bagian-6",
  },
};

const LessonDetail = () => {
  const { lessonSlug } = useParams();
  const lesson = lessonData[lessonSlug];

  if (!lesson) {
    return (
      <div className="min-h-screen flex flex-col bg-white font-sans">
        <Navbar />
        <div className="grow flex items-center justify-center">
          <div className="text-center">
            <h1 className="text-4xl font-bold text-gray-900 mb-4">
              Pelajaran Tidak Ditemukan
            </h1>
            <Link to="/qthematic" className="text-emerald-600 hover:underline">
              Kembali ke Daftar Tema
            </Link>
          </div>
        </div>
        <Footer />
      </div>
    );
  }

  return (
    <div className="min-h-screen flex flex-col bg-white font-sans">
      <Navbar />

      <main className="grow container mx-auto px-6 py-12">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
          {/* Main Content */}
          <div className="lg:col-span-2">
            <h1 className="text-3xl font-bold text-gray-900 mb-6">
              {lesson.title}
            </h1>

            <div className="bg-white rounded-2xl overflow-hidden shadow-lg border border-gray-200 mb-8">
              <div className="aspect-4/3 w-full relative">
                <iframe
                  className="absolute inset-0 w-full h-full"
                  src={lesson.contentUrl}
                  title={lesson.title}
                  frameBorder="0"
                ></iframe>
              </div>
              <div className="p-4 bg-gray-50 border-t border-gray-200 text-center">
                <a
                  href={lesson.contentUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-emerald-600 hover:text-emerald-700 font-medium text-sm inline-flex items-center"
                >
                  Buka materi di tab baru
                  <svg
                    className="w-4 h-4 ml-1"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
                    ></path>
                  </svg>
                </a>
              </div>
            </div>

            {/* Navigation Buttons */}
            <div className="flex justify-between mt-12 pt-8 border-t border-gray-100">
              {lesson.prevLesson ? (
                <Link
                  to={`/qthematic/${lesson.themeSlug}/${lesson.prevLesson}`}
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
                    ></path>
                  </svg>
                  Sebelumnya
                </Link>
              ) : (
                <div></div>
              )}

              {lesson.nextLesson ? (
                <Link
                  to={`/qthematic/${lesson.themeSlug}/${lesson.nextLesson}`}
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
                    ></path>
                  </svg>
                </Link>
              ) : (
                <Link
                  to={`/qthematic/${lesson.themeSlug}`}
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
                    ></path>
                  </svg>
                </Link>
              )}
            </div>
          </div>

          {/* Sidebar */}
          <div className="lg:col-span-1">
            <div className="bg-gray-50 rounded-2xl p-6 border border-gray-100 sticky top-24">
              <h3 className="text-lg font-bold text-gray-900 mb-4">
                Daftar Materi
              </h3>
              <div className="space-y-3">
                {Object.entries(lessonData)
                  .filter(([, data]) => data.themeSlug === lesson.themeSlug)
                  .map(([slug, data], index) => (
                    <Link
                      key={slug}
                      to={`/qthematic/${data.themeSlug}/${slug}`}
                      className={`block p-3 rounded-lg transition-colors ${
                        slug === lessonSlug
                          ? "bg-emerald-100 text-emerald-700 font-medium"
                          : "hover:bg-white hover:shadow-sm text-gray-600"
                      }`}
                    >
                      <div className="flex items-start">
                        <span className="inline-block w-6 text-sm opacity-70 mt-0.5">
                          {index + 1}.
                        </span>
                        <span className="text-sm">{data.title}</span>
                      </div>
                    </Link>
                  ))}
              </div>
            </div>
          </div>
        </div>
      </main>

      <Footer />
    </div>
  );
};

export default LessonDetail;
