import React from "react";
import previewQuiz from "/preview-quiz.png";

const Hero = () => {
  return (
    <div className="relative bg-linear-to-br from-emerald-50 via-white to-teal-50 pt-32 pb-20 overflow-hidden">
      {/* Background decoration */}
      <div className="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-emerald-100 rounded-full blur-3xl opacity-50"></div>
      <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-80 h-80 bg-teal-100 rounded-full blur-3xl opacity-50"></div>

      <div className="container mx-auto px-6 relative z-10">
        <div className="flex flex-col lg:flex-row items-center gap-12">
          <div className="lg:w-1/2 text-center lg:text-left">
            <div className="inline-block px-4 py-1.5 mb-6 bg-emerald-100 text-emerald-700 rounded-full text-sm font-semibold tracking-wide">
              ✨ Platform Pembelajaran Al-Qur'an
            </div>
            <h1 className="text-4xl md:text-6xl font-bold text-gray-900 leading-tight mb-6">
              Gerbang Pembelajaran <br />
              <span className="text-transparent bg-clip-text bg-linear-to-r from-emerald-600 to-teal-500">
                Al-Qur’an Interaktif
              </span>{" "}
              Dunia
            </h1>
            <p className="text-lg text-gray-600 mb-8 leading-relaxed max-w-2xl mx-auto lg:mx-0">
              Satu platform dengan sembilan pintu ilmu: Tajwid, Tahfidz, Nahwu,
              Shorof, Mushaf, Data, Video, Sains, dan Tematis. Belajar Al-Qur'an
              kini lebih mudah dan menyenangkan.
            </p>
            {/* <div className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
              <button className="px-8 py-4 bg-emerald-600 text-white rounded-full font-semibold hover:bg-emerald-700 transition shadow-lg shadow-emerald-600/30 transform hover:-translate-y-1">
                Mulai Belajar Gratis
              </button>
            </div> */}
            {/* <div className="mt-10 flex items-center justify-center lg:justify-start gap-4 text-sm text-gray-500">
              <div className="flex -space-x-2">
                {[1, 2, 3, 4].map((i) => (
                  <div
                    key={i}
                    className="w-8 h-8 rounded-full bg-gray-200 border-2 border-white"
                  ></div>
                ))}
              </div>
              <p>Dipercaya oleh 10,000+ Pengguna</p>
            </div> */}
          </div>

          <div className="lg:w-1/2 relative">
            <div className="relative rounded-2xl overflow-hidden shadow-2xl border-4 border-white bg-white p-2">
              <div className="aspect-video bg-gray-100 rounded-xl flex items-center justify-center overflow-hidden">
                <img
                  src={previewQuiz}
                  alt="Preview Aplikasi e-Furqan"
                  className="w-full h-full object-cover"
                />
              </div>
            </div>
            {/* Floating Cards */}
            <div className="absolute -bottom-6 -left-6 bg-white p-4 rounded-xl shadow-xl border border-gray-100 hidden md:block">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center text-green-600">
                  ✓
                </div>
                <div>
                  <p className="text-xs text-gray-500">Progress Hafalan</p>
                  <p className="font-bold text-gray-800">Juz 30 Selesai</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Hero;
