import React from "react";
import { useParams, Link } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

const themeData = {
  "sifat-allah": {
    title: "Sifat Allah",
    description:
      "Mengenal Asmaul Husna dan sifat-sifat keagungan Allah SWT. Pelajari bagaimana memahami kebesaran Allah melalui ayat-ayat pilihan.",
    image:
      "https://images.unsplash.com/photo-1584286595398-a59f21d313f5?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    lessons: [
      {
        title: "Sifat Allah Bagian 1",
        duration: "10 min",
        id: "sifat-allah-bagian-1",
      },
      {
        title: "Sifat Allah Bagian 2",
        duration: "12 min",
        id: "sifat-allah-bagian-2",
      },
      {
        title: "Sifat Allah Bagian 3",
        duration: "15 min",
        id: "sifat-allah-bagian-3",
      },
      {
        title: "Sifat Allah Bagian 4",
        duration: "11 min",
        id: "sifat-allah-bagian-4",
      },
      {
        title: "Sifat Allah Bagian 5",
        duration: "14 min",
        id: "sifat-allah-bagian-5",
      },
      {
        title: "Sifat Allah Bagian 6",
        duration: "13 min",
        id: "sifat-allah-bagian-6",
      },
      {
        title: "Sifat Allah Bagian 7",
        duration: "16 min",
        id: "sifat-allah-bagian-7",
      },
    ],
  },
};

const ThemeDetail = () => {
  const { slug } = useParams();
  const theme = themeData[slug];

  if (!theme) {
    return (
      <div className="min-h-screen flex flex-col bg-white font-sans">
        <Navbar />
        <div className="grow flex items-center justify-center">
          <div className="text-center">
            <h1 className="text-4xl font-bold text-gray-900 mb-4">
              Tema Tidak Ditemukan
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

      {/* Hero Section */}
      <div className="relative bg-emerald-900 py-24 overflow-hidden">
        <div className="absolute inset-0 opacity-20">
          <img
            src={theme.image}
            alt={theme.title}
            className="w-full h-full object-cover"
          />
        </div>
        <div className="absolute inset-0 bg-linear-to-t from-emerald-900 via-emerald-900/80 to-transparent"></div>

        <div className="container mx-auto px-6 relative z-10">
          <Link
            to="/qthematic"
            className="inline-flex items-center text-emerald-200 hover:text-white mb-6 transition-colors"
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
            Kembali ke Daftar Tema
          </Link>
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-4">
            {theme.title}
          </h1>
          <p className="text-xl text-emerald-100 max-w-2xl leading-relaxed">
            {theme.description}
          </p>

          <div className="mt-8 flex flex-wrap gap-4">
            <div className="flex items-center text-emerald-200 bg-emerald-800/50 px-4 py-2 rounded-full backdrop-blur-sm">
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
                  d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"
                ></path>
              </svg>
              {theme.lessons.length} Pelajaran
            </div>
            <div className="flex items-center text-emerald-200 bg-emerald-800/50 px-4 py-2 rounded-full backdrop-blur-sm">
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
                  d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                ></path>
              </svg>
              ~90 Menit Total
            </div>
          </div>
        </div>
      </div>

      {/* Lessons List */}
      <main className="grow container mx-auto px-6 py-16">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-2xl font-bold text-gray-900 mb-8">
            Daftar Pelajaran
          </h2>
          <div className="space-y-4">
            {theme.lessons.map((lesson, index) => (
              <Link
                to={`/qthematic/${slug}/${lesson.id}`}
                key={index}
                className="group flex items-center p-4 bg-white border border-gray-100 rounded-xl hover:shadow-md hover:border-emerald-200 transition-all duration-300 cursor-pointer"
              >
                <div className="shrink-0 w-12 h-12 bg-emerald-50 text-emerald-600 rounded-full flex items-center justify-center font-bold text-lg group-hover:bg-emerald-600 group-hover:text-white transition-colors">
                  {index + 1}
                </div>
                <div className="ml-6 grow">
                  <h3 className="text-lg font-semibold text-gray-900 group-hover:text-emerald-600 transition-colors">
                    {lesson.title}
                  </h3>
                  <p className="text-sm text-gray-500">Materi Pembelajaran</p>
                </div>
                <div className="shrink-0">
                  <button className="w-10 h-10 rounded-full border border-gray-200 flex items-center justify-center text-gray-400 group-hover:border-emerald-600 group-hover:text-emerald-600 transition-all">
                    <svg
                      className="w-5 h-5 ml-0.5"
                      fill="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path d="M8 5v14l11-7z" />
                    </svg>
                  </button>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </main>

      <Footer />
    </div>
  );
};

export default ThemeDetail;
