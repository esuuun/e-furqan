import React, { useState } from "react";
import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

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

const themes = [
  {
    title: "Sifat Allah",
    externalUrl: "https://qthematic.e-furqan.com/courses/al-quran-tematis-2-2/",
    description: "Mengenal Asmaul Husna dan sifat-sifat keagungan Allah SWT.",
    count: "100+ Ayat",
    image:
      "https://bimamedia-cms.ap-south-1.linodeobjects.com/sarungbhs.co.id/2025/01/29/l-ilustrasi-99-asmaul-husna-116920250129135332.jpeg",
  },
  {
    title: "Golongan Manusia",
    externalUrl: "https://qthematic.e-furqan.com/courses/al-quran-tematis-2-3/",
    description:
      "Karakteristik orang mukmin, kafir, dan munafik dalam Al-Qur'an.",
    count: "150+ Ayat",
    image: "golonganManusia.png",
  },
  {
    title: "Malaikat, Kitab, dan Rasul",
    externalUrl: "https://qthematic.e-furqan.com/courses/al-quran-tematis-2-4/",
    description:
      "Keimanan kepada malaikat, kitab-kitab samawi, dan para utusan Allah.",
    count: "120+ Ayat",
    image: "malaikatKitabRasul.png",
  },
  {
    title: "Taqdir dan Hari Akhir",
    externalUrl:
      "https://qthematic.e-furqan.com/courses/taqdir-dan-hari-akhir/",
    description: "Ketetapan Allah dan peristiwa dahsyat di hari kiamat.",
    count: "200+ Ayat",
    image: "takdirHariAkhir.png",
  },
  {
    title: "Nabi Muhammad ﷺ",
    externalUrl: "https://qthematic.e-furqan.com/courses/nabi-muhammad-saw/",
    description: "Riwayat hidup, dakwah, dan kemuliaan akhlak Rasulullah ﷺ.",
    count: "300+ Ayat",
    image: "nabiMuhammad.png",
  },
  {
    title: "Kisah Dalam Al-Quran",
    externalUrl: "https://qthematic.e-furqan.com/courses/kisah-dalam-al-quran/",
    description: "Pelajaran dari umat terdahulu dan kisah-kisah penuh hikmah.",
    count: "250+ Ayat",
    image: "kisahAlquran.png",
  },
  {
    title: "Taqwa, Jihad, dan Ibadah",
    externalUrl:
      "https://qthematic.e-furqan.com/courses/taqwa-jihad-dan-ibadah/",
    description:
      "Perintah bertakwa, berjuang di jalan Allah, dan tata cara ibadah.",
    count: "180+ Ayat",
    image: "taqwaJihadIbadah.png",
  },
  {
    title: "Akhlak Terpuji",
    externalUrl: "https://qthematic.e-furqan.com/courses/akhlak-terpuji-2/",
    description: "Sifat-sifat mulia seperti sabar, jujur, dan amanah.",
    count: "140+ Ayat",
    image: "akhlakTerpuji.png",
  },
  {
    title: "Akhlak Tercela",
    externalUrl: "https://qthematic.e-furqan.com/courses/akhlah-tercela/",
    description: "Larangan sifat sombong, dengki, dan perilaku buruk lainnya.",
    count: "130+ Ayat",
    image: "akhlakTercela.png",
  },
  {
    title: "Hukum Keluarga",
    externalUrl: "https://qthematic.e-furqan.com/courses/hukum-keluarga/",
    description: "Pernikahan, perceraian, waris, dan hak-hak anggota keluarga.",
    count: "90+ Ayat",
    image: "hukumKeluarga.png",
  },
  {
    title: "Hukum Muamalat",
    externalUrl: "https://qthematic.e-furqan.com/courses/hukum-muamalat/",
    description: "Prinsip ekonomi Islam, jual beli, hutang piutang, dan riba.",
    count: "110+ Ayat",
    image: "hukumMuamalat.png",
  },
  {
    title: "Hukum Pidana",
    externalUrl: "https://qthematic.e-furqan.com/courses/hukum-pidana/",
    description: "Qishash, hudud, dan keadilan hukum dalam Islam.",
    count: "60+ Ayat",
    image: "hukumPidana.png",
  },
  {
    title: "Hukum Pemerintahan",
    externalUrl: "https://qthematic.e-furqan.com/courses/hukum-pemerintahan/",
    description: "Kepemimpinan, musyawarah, dan keadilan sosial.",
    count: "50+ Ayat",
    image: "hukumPemerintahan.png",
  },
  {
    title: "Hukum Makanan dan Pakaian",
    externalUrl:
      "https://qthematic.e-furqan.com/courses/hukum-makanan-pakaian/",
    description: "Halal haram makanan dan adab berpakaian.",
    count: "40+ Ayat",
    image: "hukumMakananPakaian.png",
  },
  {
    title: "Manusia",
    externalUrl: "https://qthematic.e-furqan.com/courses/15-manusia/",
    description: "Penciptaan manusia, tujuan hidup, dan potensi diri.",
    count: "160+ Ayat",
    image: "manusia.png",
  },
  {
    title: "Alam",
    externalUrl: "https://qthematic.e-furqan.com/courses/16-alam/",
    description: "Fenomena alam semesta sebagai tanda kekuasaan Allah.",
    count: "170+ Ayat",
    image: "alam.png",
  },
  {
    title: "Jin dan Iblis",
    externalUrl: "https://qthematic.e-furqan.com/courses/17-jin-dan-iblis/",
    description: "Hakikat jin, tipu daya iblis, dan cara berlindung darinya.",
    count: "30+ Ayat",
    image: "jinIblis.png",
  },
];

const QThematic = () => {
  const [visibleCount, setVisibleCount] = useState(6);

  const handleLoadMore = () => {
    setVisibleCount((prev) => prev + 6);
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
          {/* <div className="flex justify-center gap-4">
            <button className="px-8 py-4 bg-emerald-600 text-white rounded-full font-semibold hover:bg-emerald-700 transition shadow-lg shadow-emerald-600/30 transform hover:-translate-y-1">
              Mulai Belajar
            </button>
            <button className="px-8 py-4 bg-white text-gray-700 border border-gray-200 rounded-full font-semibold hover:bg-gray-50 transition hover:border-gray-300">
              Lihat Demo
            </button>
          </div> */}
        </div>
      </div>

      {/* Stats Section */}
      <section className="py-12 bg-white border-b border-gray-100">
        <div className="container mx-auto px-6">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            <div>
              <p className="text-4xl font-bold text-emerald-600 mb-2">17</p>
              <p className="text-gray-500 font-medium">Tema Utama</p>
            </div>
            <div>
              <p className="text-4xl font-bold text-emerald-600 mb-2">110</p>
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
            {/* <div>
              <p className="text-4xl font-bold text-emerald-600 mb-2">PDF</p>
              <p className="text-gray-500 font-medium">Unduh Materi</p>
            </div> */}
          </div>
        </div>
      </section>

      {/* Features Grid */}
      {/* <main className="grow container mx-auto px-6 py-24">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
            Fitur Unggulan
          </h2>
          <p className="text-gray-500 max-w-2xl mx-auto text-lg">
            Platform komprehensif untuk mendalami Al-Qur'an dengan metode yang
            modern dan mudah dipahami.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {features.map((feature, index) => (
            <div
              key={index}
              className="group bg-white p-6 rounded-2xl border border-gray-100 hover:shadow-xl transition-all duration-300 hover:-translate-y-1 relative overflow-hidden"
            >
              <div className="absolute top-0 right-0 w-20 h-20 bg-emerald-50 rounded-bl-full -mr-6 -mt-6 transition-transform group-hover:scale-110"></div>
              <div className="relative z-10">
                <div className="w-12 h-12 bg-emerald-100 rounded-xl flex items-center justify-center text-2xl mb-4 group-hover:bg-emerald-600 group-hover:text-white transition-colors duration-300">
                  {feature.icon}
                </div>
                <h3 className="text-xl font-bold text-gray-900 mb-2 group-hover:text-emerald-600 transition-colors">
                  {feature.title}
                </h3>
                <p className="text-gray-500 text-sm leading-relaxed">
                  {feature.description}
                </p>
              </div>
            </div>
          ))}
        </div>
      </main> */}

      {/* Course List Section */}
      <section id="tema" className="bg-gray-50 py-24">
        <div className="container mx-auto px-6">
          <div className="flex justify-between items-end mb-12">
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-2">
                Daftar Tema
              </h2>
              <p className="text-gray-500">
                Jelajahi berbagai tema menarik dari Al-Qur'an
              </p>
            </div>
            <button className="text-emerald-600 font-semibold hover:text-emerald-700">
              Lihat Semua Tema →
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {themes.slice(0, visibleCount).map((theme, index) => (
              <a
                href={theme.externalUrl}
                target="_blank"
                rel="noopener noreferrer"
                key={index}
                className="bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 border border-gray-100 group cursor-pointer block"
              >
                <div className="h-48 overflow-hidden relative">
                  <div className="absolute inset-0 bg-black/20 group-hover:bg-black/10 transition-colors z-10"></div>
                  <img
                    src={theme.image}
                    alt={theme.title}
                    className="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500"
                  />
                  <div className="absolute top-4 right-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-xs font-bold text-emerald-600 z-20 shadow-sm">
                    {theme.count}
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
              </a>
            ))}
          </div>

          {visibleCount < themes.length && (
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
