import React from "react";
import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import ServiceCard from "../components/ServiceCard";
import Footer from "../components/Footer";

const services = [
  {
    title: "qThematic",
    description:
      "Belajar kandungan Al-Qur’an secara tematis — ayat demi ayat dibahas menurut tema kehidupan.",
    link: "/qthematic",
    icon: (
      <svg
        className="w-7 h-7"
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
    ),
  },
  {
    title: "qTajwid",
    description:
      "Pelajari tajwid interaktif dengan contoh suara, warna, dan latihan real-time.",
    link: "https://qtajwid.e-furqan.com/",
    icon: (
      <svg
        className="w-7 h-7"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"
        ></path>
      </svg>
    ),
  },
  {
    title: "qTahfidz",
    description:
      "Latihan hafalan ayat demi ayat dengan sistem audio, drag-and-drop, dan penilaian otomatis.",
    link: "/qtahfidz",
    icon: (
      <svg
        className="w-7 h-7"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 3-2 3-2 1.343 2 3 2zm0 0v-8"
        ></path>
      </svg>
    ),
  },
  {
    title: "qNahwu",
    description:
      "Kuasai struktur bahasa Arab Al-Qur’an dengan pendekatan nahwu dan shorof yang mudah.",
    link: "/qnahwu",
    icon: (
      <svg
        className="w-7 h-7"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129"
        ></path>
      </svg>
    ),
  },
  // {
  //   title: "qGames",
  //   description:
  //     "Main sambil belajar lewat game akar kata, wazan, dan i‘rab interaktif khas Al-Qur’an.",
  //   link: "https://qgames.e-furqan.com/home/",
  //   icon: (
  //     <svg
  //       className="w-7 h-7"
  //       fill="none"
  //       stroke="currentColor"
  //       viewBox="0 0 24 24"
  //     >
  //       <path
  //         strokeLinecap="round"
  //         strokeLinejoin="round"
  //         strokeWidth="2"
  //         d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"
  //       ></path>
  //       <path
  //         strokeLinecap="round"
  //         strokeLinejoin="round"
  //         strokeWidth="2"
  //         d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
  //       ></path>
  //     </svg>
  //   ),
  // },
  {
    title: "qMushaf",
    description:
      "Jelajahi mushaf digital interaktif dengan analisis morfologi dan pencarian cepat setiap lafadz.",
    link: "/qmushaf",
    icon: (
      <svg
        className="w-7 h-7"
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
    ),
  },
  // {
  //   title: "qData",
  //   description:
  //     "Temukan keindahan data Al-Qur’an melalui infografis, statistik ayat, dan visualisasi ilmiah",
  //   link: "https://qdata.e-furqan.com/",
  //   icon: (
  //     <svg
  //       className="w-7 h-7"
  //       fill="none"
  //       stroke="currentColor"
  //       viewBox="0 0 24 24"
  //     >
  //       <path
  //         strokeLinecap="round"
  //         strokeLinejoin="round"
  //         strokeWidth="2"
  //         d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
  //       ></path>
  //     </svg>
  //   ),
  // },
  // {
  //   title: "qVideo",
  //   description:
  //     "Nikmati kisah Qur’ani dalam video ilustrasi kontemplatif (VIK) yang menggugah hati.",
  //   link: "https://qvideo.e-furqan.com/",
  //   icon: (
  //     <svg
  //       className="w-7 h-7"
  //       fill="none"
  //       stroke="currentColor"
  //       viewBox="0 0 24 24"
  //     >
  //       <path
  //         strokeLinecap="round"
  //         strokeLinejoin="round"
  //         strokeWidth="2"
  //         d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"
  //       ></path>
  //     </svg>
  //   ),
  // },
  // {
  //   title: "qSains",
  //   description:
  //     "Menjelajahi hubungan antara ayat-ayat Al-Qur’an dan keajaiban ilmu pengetahuan modern.",
  //   link: "https://qsains.e-furqan.com/",
  //   icon: (
  //     <svg
  //       className="w-7 h-7"
  //       fill="none"
  //       stroke="currentColor"
  //       viewBox="0 0 24 24"
  //     >
  //       <path
  //         strokeLinecap="round"
  //         strokeLinejoin="round"
  //         strokeWidth="2"
  //         d="M19.428 15.428a2 2 0 00-1.022-.547l-2.384-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"
  //       ></path>
  //     </svg>
  //   ),
  // },
];

const Home = () => {
  return (
    <div className="min-h-screen flex flex-col bg-white font-sans">
      <Navbar />
      <Hero />

      {/* Stats Section */}
      {/* <section className="py-12 bg-white border-b border-gray-100">
        <div className="container mx-auto px-6">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            <div>
              <p className="text-4xl font-bold text-emerald-600 mb-2">9+</p>
              <p className="text-gray-500 font-medium">Modul Pembelajaran</p>
            </div>
            <div>
              <p className="text-4xl font-bold text-emerald-600 mb-2">10k+</p>
              <p className="text-gray-500 font-medium">Pengguna Aktif</p>
            </div>
            <div>
              <p className="text-4xl font-bold text-emerald-600 mb-2">100%</p>
              <p className="text-gray-500 font-medium">Gratis Diakses</p>
            </div>
            <div>
              <p className="text-4xl font-bold text-emerald-600 mb-2">24/7</p>
              <p className="text-gray-500 font-medium">Akses Kapan Saja</p>
            </div>
          </div>
        </div>
      </section> */}

      {/* Services Section */}
      <main className="grow container mx-auto px-6 py-24" id="services">
        <div className="text-center mb-16">
          <span className="text-emerald-600 font-semibold tracking-wider uppercase text-sm">
            Layanan Kami
          </span>
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mt-3 mb-4">
            Eksplorasi Dunia Al-Qur'an
          </h2>
          <p className="text-gray-500 max-w-2xl mx-auto text-lg">
            Pilih modul pembelajaran yang sesuai dengan kebutuhan Anda, mulai
            dari tajwid hingga sains.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {services.map((service, index) => (
            <ServiceCard
              key={index}
              title={service.title}
              description={service.description}
              link={service.link}
              icon={service.icon}
            />
          ))}
        </div>
      </main>

      {/* Features Section */}
      <section className="py-24 bg-gray-50" id="features">
        <div className="container mx-auto px-6">
          <div className="flex flex-col md:flex-row items-center gap-16">
            <div className="md:w-1/2">
              <div className="relative">
                <div className="absolute -top-4 -left-4 w-24 h-24 bg-emerald-200 rounded-full opacity-50 blur-xl"></div>
                <img
                  src="https://images.unsplash.com/photo-1609599006353-e629aaabfeae?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
                  alt="Belajar Quran"
                  className="rounded-2xl shadow-2xl relative z-10 w-full object-cover h-[400px]"
                />
                <div className="absolute -bottom-6 -right-6 w-48 h-48 bg-teal-100 rounded-full opacity-50 blur-xl"></div>
              </div>
            </div>
            <div className="md:w-1/2">
              <span className="text-emerald-600 font-semibold tracking-wider uppercase text-sm">
                Kenapa e-Furqan?
              </span>
              <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mt-3 mb-6">
                Metode Belajar Modern & Interaktif
              </h2>
              <div className="space-y-6">
                <div className="flex gap-4">
                  <div className="w-12 h-12 bg-white rounded-xl shadow-md flex items-center justify-center text-emerald-600 shrink-0">
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
                        d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"
                      ></path>
                    </svg>
                  </div>
                  <div>
                    <h3 className="text-xl font-bold text-gray-900 mb-2">
                      Mudah Dipahami
                    </h3>
                    <p className="text-gray-500">
                      Materi disusun secara sistematis agar mudah dipahami oleh
                      pemula sekalipun.
                    </p>
                  </div>
                </div>
                <div className="flex gap-4">
                  <div className="w-12 h-12 bg-white rounded-xl shadow-md flex items-center justify-center text-emerald-600 shrink-0">
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
                        d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"
                      ></path>
                    </svg>
                  </div>
                  <div>
                    <h3 className="text-xl font-bold text-gray-900 mb-2">
                      Akses Multi-Platform
                    </h3>
                    <p className="text-gray-500">
                      Bisa diakses melalui laptop, tablet, maupun smartphone
                      Anda.
                    </p>
                  </div>
                </div>
                <div className="flex gap-4">
                  <div className="w-12 h-12 bg-white rounded-xl shadow-md flex items-center justify-center text-emerald-600 shrink-0">
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
                        d="M19.428 15.428a2 2 0 00-1.022-.547l-2.384-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"
                      ></path>
                    </svg>
                  </div>
                  <div>
                    <h3 className="text-xl font-bold text-gray-900 mb-2">
                      Terintegrasi Sains
                    </h3>
                    <p className="text-gray-500">
                      Menghubungkan ayat-ayat Al-Qur'an dengan penemuan ilmiah
                      modern.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
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
            Siap Memperdalam Ilmu Al-Qur'an?
          </h2>
          <p className="text-emerald-100 text-lg mb-10 max-w-2xl mx-auto">
            Bergabunglah dengan ribuan pengguna lainnya dan rasakan kemudahan
            belajar Al-Qur'an dengan teknologi modern.
          </p>
          <button className="bg-white text-emerald-600 px-8 py-4 rounded-full font-bold text-lg hover:bg-gray-100 transition shadow-xl">
            Mulai Sekarang - Gratis
          </button>
        </div>
      </section>

      <Footer />
    </div>
  );
};

export default Home;
