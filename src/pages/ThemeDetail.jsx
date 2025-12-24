import React from "react";
import { useParams, Link, useLocation } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import courseData from "../data/thematicData";

const ThemeDetail = () => {
  const { slug } = useParams();
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const [searchQuery, setSearchQuery] = React.useState(
    searchParams.get("search") || ""
  );
  const theme = courseData.find((t) => t.id === slug);
  const themeIndex = courseData.findIndex((t) => t.id === slug);

  const getThemeImage = (index) => {
    const images = [
      "https://bimamedia-cms.ap-south-1.linodeobjects.com/sarungbhs.co.id/2025/01/29/l-ilustrasi-99-asmaul-husna-116920250129135332.jpeg",
      "golonganManusia.png",
      "malaikatKitabRasul.png",
      "takdirHariAkhir.png",
      "nabiMuhammad.png",
      "kisahAlquran.png",
      "taqwaJihadIbadah.png",
      "akhlakTerpuji.png",
      "akhlakTercela.png",
      "hukumKeluarga.png",
      "hukumMuamalat.png",
      "hukumPidana.png",
      "hukumPemerintahan.png",
      "hukumMakananPakaian.png",
      "manusia.png",
      "alam.png",
      "jinIblis.png",
    ];
    const image = images[index % images.length];
    return image.startsWith("http") ? image : `/${image}`;
  };

  if (!theme) {
    return (
      <div className="min-h-screen flex flex-col bg-white dark:bg-gray-900 font-sans">
        <Navbar />
        <div className="grow flex items-center justify-center">
          <div className="text-center">
            <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">
              Tema Tidak Ditemukan
            </h1>
            <Link to="/qthematic" className="text-yellow-600 dark:text-yellow-400 hover:underline">
              Kembali ke Daftar Tema
            </Link>
          </div>
        </div>
        <Footer />
      </div>
    );
  }

  const totalTopics = theme.subjects.reduce(
    (acc, subject) => acc + subject.topics.length,
    0
  );

  return (
    <div className="min-h-screen flex flex-col bg-white dark:bg-gray-900 font-sans">
      <Navbar />

      {/* Hero Section */}
      <div className="relative bg-gray-900 dark:bg-black py-24 overflow-hidden">
        <div className="absolute inset-0 opacity-20">
          <img
            src={getThemeImage(themeIndex)}
            alt={theme.title}
            className="w-full h-full object-cover"
          />
        </div>
        <div className="absolute inset-0 bg-linear-to-t from-gray-900 via-gray-900/80 to-transparent dark:from-black dark:via-black/80"></div>

        <div className="container mx-auto px-6 relative z-10">
          <Link
            to="/qthematic"
            className="inline-flex items-center text-gray-300 hover:text-white mb-6 transition-colors"
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
          <p className="text-xl text-gray-300 max-w-2xl leading-relaxed">
            {theme.description}
          </p>

          <div className="mt-8 flex flex-wrap gap-4">
            <div className="flex items-center text-yellow-200 bg-gray-800/50 px-4 py-2 rounded-full backdrop-blur-sm">
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
              {totalTopics} Pelajaran
            </div>
          </div>

          <div className="mt-8 relative max-w-xl">
            <input
              type="text"
              placeholder="Cari dalam tema ini..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full px-5 py-3 pl-12 rounded-xl bg-white/10 backdrop-blur-md border border-yellow-400/30 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:bg-white/20 transition-all"
            />
            <svg
              className="w-5 h-5 absolute left-4 top-3.5 text-gray-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
              ></path>
            </svg>
          </div>
        </div>
      </div>

      {/* Lessons List */}
      <main className="grow container mx-auto px-6 py-16">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-8">
            Daftar Pelajaran
          </h2>
          <div className="space-y-8">
            {theme.subjects.map((subject, sIndex) => {
              const filteredTopics = subject.topics.filter((topic) => {
                if (!searchQuery) return true;
                const query = searchQuery.toLowerCase();
                return (
                  (topic.title || "").toLowerCase().includes(query) ||
                  (topic.content || "").toLowerCase().includes(query)
                );
              });

              if (filteredTopics.length === 0) return null;

              return (
                <div key={subject.id}>
                  <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-4 border-b border-yellow-200 dark:border-yellow-800 pb-2">
                    {subject.title}
                  </h3>
                  <div className="space-y-4">
                    {filteredTopics.map((topic, tIndex) => (
                      <Link
                        to={`/qthematic/${slug}/${topic.id}${
                          searchQuery
                            ? `?highlight=${encodeURIComponent(searchQuery)}`
                            : ""
                        }`}
                        key={topic.id}
                        className="group flex items-center p-4 bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 rounded-xl hover:shadow-md hover:border-yellow-200 dark:hover:border-yellow-700 transition-all duration-300 cursor-pointer"
                      >
                        <div className="shrink-0 w-12 h-12 bg-yellow-50 dark:bg-yellow-900/20 text-yellow-600 dark:text-yellow-400 rounded-full flex items-center justify-center font-bold text-lg group-hover:bg-yellow-500 group-hover:text-white transition-colors">
                          {tIndex + 1}
                        </div>
                        <div className="ml-6 grow">
                          <h3 className="text-lg font-semibold text-gray-900 dark:text-white group-hover:text-yellow-600 dark:group-hover:text-yellow-400 transition-colors">
                            {topic.title}
                          </h3>
                          <p className="text-sm text-gray-500 dark:text-gray-400">
                            Materi Pembelajaran
                          </p>
                        </div>
                        <div className="shrink-0">
                          <button className="w-10 h-10 rounded-full border border-gray-200 dark:border-gray-600 flex items-center justify-center text-gray-400 dark:text-gray-500 group-hover:border-yellow-500 group-hover:text-yellow-600 dark:group-hover:text-yellow-400 transition-all">
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
              );
            })}
          </div>

          <div className="mt-12 pt-8 border-t border-gray-100 dark:border-gray-800">
            <Link
              to="/qthematic"
              className="inline-flex items-center text-gray-600 dark:text-gray-300 hover:text-emerald-600 dark:hover:text-emerald-400 font-medium transition-colors"
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
          </div>
        </div>
      </main>

      <Footer />
    </div>
  );
};

export default ThemeDetail;
