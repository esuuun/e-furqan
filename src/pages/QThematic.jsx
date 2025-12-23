import React, { useState } from "react";
import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import courseData from "../data/thematicData";

const features = [
  {
    title: "Tafsir Tematis",
    description:
      "Ayat terarah, makna lebih mudah. Pelajari Al-Qur'an berdasarkan tema kehidupan sehari-hari.",
    icon: "📖",
  },
  {
    title: "Multi Language",
    description:
      "Satu ilmu, banyak bahasa. Tersedia dalam berbagai bahasa untuk menjangkau lebih banyak umat.",
    icon: "🌐",
  },
  {
    title: "Kuis & Latihan",
    description:
      "Belajar seru, hafal makin cepat. Uji pemahaman Anda dengan kuis interaktif.",
    icon: "📝",
  },
  {
    title: "Glosarium & Tooltip",
    description:
      "Istilah jelas, paham seketika. Penjelasan kata-kata sulit langsung di layar.",
    icon: "💡",
  },
  {
    title: "Pencarian Cepat",
    description:
      "Temukan topik hanya sekejap. Mesin pencari canggih untuk menemukan ayat yang Anda cari.",
    icon: "🔍",
  },
  {
    title: "Akses Gratis",
    description:
      "Ilmu Qur’an untuk semua. Tanpa biaya berlangganan, akses ilmu tanpa batas.",
    icon: "🎁",
  },
  {
    title: "PDF Ayat & Terjemahan",
    description:
      "Baca ayat sesuai topik. Unduh materi dalam format PDF untuk dipelajari secara offline.",
    icon: "📄",
  },
  {
    title: "Daftar Referensi",
    description:
      "Sumber terpercaya, isi teruji. Materi disusun berdasarkan referensi yang valid dan otentik.",
    icon: "📚",
  },
];

const QThematic = () => {
  const [visibleCount, setVisibleCount] = useState(6);
  const [searchQuery, setSearchQuery] = useState("");

  const handleLoadMore = () => {
    setVisibleCount((prev) => prev + 6);
  };

  const filteredData = courseData.filter((theme) => {
    const query = searchQuery.toLowerCase();
    if (!query) return true;

    // Check theme level
    if ((theme.title || "").toLowerCase().includes(query)) return true;
    if ((theme.description || "").toLowerCase().includes(query)) return true;

    // Check subjects and topics level
    return theme.subjects?.some(
      (subject) =>
        (subject.title || "").toLowerCase().includes(query) ||
        subject.topics?.some(
          (topic) =>
            (topic.title || "").toLowerCase().includes(query) ||
            (topic.content || "").toLowerCase().includes(query)
        )
    );
  });

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
    return images[index % images.length];
  };

  return (
    <div className="min-h-screen flex flex-col bg-white font-sans">
      <Navbar />

      {/* Hero Section */}
      <div className="relative bg-linear-to-br from-emerald-50 via-white to-teal-50 pt-32 pb-20 overflow-hidden">
        {/* Background decoration */}
        <div className="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-emerald-100 rounded-full blur-3xl opacity-50"></div>
        <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-80 h-80 bg-teal-100 rounded-full blur-3xl opacity-50"></div>

        <div className="container mx-auto px-6 relative z-10 text-center">
          <div className="inline-block px-4 py-1.5 mb-6 bg-emerald-100 text-emerald-700 rounded-full text-sm font-semibold tracking-wide">
            ✨ qThematic
          </div>
          <h1 className="text-4xl md:text-6xl font-bold text-gray-900 leading-tight mb-6">
            Belajar Kandungan Al-Qur’an <br />
            <span className="text-transparent bg-clip-text bg-linear-to-r from-emerald-600 to-teal-600">
              Secara Tematis
            </span>
          </h1>
          <p className="text-lg text-gray-600 mb-8 leading-relaxed max-w-2xl mx-auto">
            Ayat demi ayat dibahas menurut tema kehidupan, memudahkan Anda
            memahami pesan Al-Qur'an secara utuh dan mendalam.
          </p>
        </div>
      </div>

      {/* Stats Section */}
      <section className="py-12 bg-white border-b border-gray-100">
        <div className="container mx-auto px-6">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            <div>
              <p className="text-4xl font-bold text-emerald-600 mb-2">
                {courseData.length}
              </p>
              <p className="text-gray-500 font-medium">Tema Utama</p>
            </div>
            <div>
              <p className="text-4xl font-bold text-emerald-600 mb-2">
                {courseData.reduce(
                  (acc, theme) => acc + theme.subjects.length,
                  0
                )}
              </p>
              <p className="text-gray-500 font-medium">Subtema</p>
            </div>
            <div>
              <p className="text-4xl font-bold text-emerald-600 mb-2">6236</p>
              <p className="text-gray-500 font-medium">Ayat Terpilih</p>
            </div>
            <div>
              <p className="text-4xl font-bold text-emerald-600 mb-2">100%</p>
              <p className="text-gray-500 font-medium">Valid & Shahih</p>
            </div>
          </div>
        </div>
      </section>

      {/* Course List Section */}
      <section id="tema" className="bg-gray-50 py-24">
        <div className="container mx-auto px-6">
          <div className="flex flex-col md:flex-row justify-between items-end mb-12 gap-4">
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-2">
                Daftar Tema
              </h2>
              <p className="text-gray-500">
                Jelajahi berbagai tema menarik dari Al-Qur'an
              </p>
            </div>

            <div className="relative w-full md:w-72">
              <input
                type="text"
                placeholder="Cari tema..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full px-4 py-2 pl-10 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
              />
              <svg
                className="w-5 h-5 absolute left-3 top-2.5 text-gray-400"
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

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {filteredData.slice(0, visibleCount).map((theme, index) => (
              <Link
                to={`/qthematic/${theme.id}${
                  searchQuery
                    ? `?search=${encodeURIComponent(searchQuery)}`
                    : ""
                }`}
                key={theme.id}
                className="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 border border-gray-100 group cursor-pointer block"
              >
                <div className="h-48 overflow-hidden relative">
                  <div className="absolute inset-0 bg-black/20 group-hover:bg-black/10 transition-colors z-10"></div>
                  <img
                    src={getThemeImage(index)}
                    alt={theme.title}
                    className="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500"
                  />
                  <div className="absolute top-4 right-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-xs font-bold text-emerald-600 z-20 shadow-sm">
                    {theme.subjects.length} Subtema
                  </div>
                </div>
                <div className="p-6">
                  <h3 className="text-xl font-bold text-gray-900 mb-2 group-hover:text-emerald-600 transition-colors">
                    {theme.title}
                  </h3>
                  <p className="text-gray-500 text-sm leading-relaxed mb-4">
                    {theme.description}
                  </p>
                  <div className="flex items-center text-emerald-600 font-medium text-sm group-hover:translate-x-2 transition-transform">
                    Pelajari Tema
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
                        d="M9 5l7 7-7 7"
                      ></path>
                    </svg>
                  </div>
                </div>
              </Link>
            ))}
          </div>

          {visibleCount < filteredData.length && (
            <div className="mt-12 text-center">
              <button
                onClick={handleLoadMore}
                className="px-8 py-3 bg-white border border-gray-300 text-gray-700 rounded-full font-semibold hover:bg-gray-50 transition"
              >
                Muat Lebih Banyak
              </button>
            </div>
          )}
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-emerald-600 relative overflow-hidden">
        <div className="absolute top-0 left-0 w-full h-full overflow-hidden">
          <div className="absolute w-64 h-64 bg-white opacity-10 rounded-full -top-10 -left-10"></div>
          <div className="absolute w-96 h-96 bg-white opacity-10 rounded-full bottom-0 right-0"></div>
        </div>
        <div className="container mx-auto px-6 text-center relative z-10">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">
            Mulai Belajar Tafsir Tematis Sekarang
          </h2>
          <p className="text-emerald-100 text-lg mb-10 max-w-2xl mx-auto">
            Dapatkan pemahaman yang lebih dalam tentang Al-Qur'an dengan metode
            yang terstruktur dan mudah dipahami.
          </p>
          <a href="#tema">
            <button className="bg-white text-emerald-600 px-8 py-4 rounded-full font-bold text-lg hover:bg-gray-100 transition shadow-xl">
              Akses Materi Gratis
            </button>
          </a>
        </div>
      </section>

      <Footer />
    </div>
  );
};

export default QThematic;
