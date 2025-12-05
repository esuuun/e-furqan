import React, { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import SurahSelector from "../components/qtahfidz/SurahSelector";
import AyatSelector from "../components/qtahfidz/AyatSelector";
import AyatCard from "../components/qtahfidz/AyatCard";

const QTahfidz = () => {
  const [selectedSurah, setSelectedSurah] = useState(89); // Default Al-Fajr
  const [selectedAyat, setSelectedAyat] = useState(null);
  const [surahData, setSurahData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (selectedSurah) {
      fetch(`https://quran-api.santrikoding.com/api/surah/${selectedSurah}`)
        .then((res) => res.json())
        .then((data) => {
          if (data.status) {
            setSurahData(data);
            setSelectedAyat(null); // Reset ayat selection when surah changes
          }
        })
        .catch((err) => console.error(err))
        .finally(() => setLoading(false));
    }
  }, [selectedSurah]);

  const handleSelectSurah = (id) => {
    if (id !== selectedSurah) {
      setLoading(true);
      setSelectedSurah(id);
    }
  };

  const filteredVerses = surahData
    ? selectedAyat
      ? surahData.ayat.filter((_, index) => index + 1 === selectedAyat)
      : surahData.ayat
    : [];

  return (
    <div className="min-h-screen flex flex-col bg-white font-sans">
      <Navbar />

      {/* Hero Section */}
      <div className="relative bg-linear-to-br from-emerald-50 via-white to-teal-50 pt-32 pb-16">
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          <div className="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-emerald-100 rounded-full blur-3xl opacity-50"></div>
          <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-80 h-80 bg-teal-100 rounded-full blur-3xl opacity-50"></div>
        </div>

        <div className="container mx-auto px-6 relative z-10 text-center">
          <div className="inline-block px-4 py-1.5 mb-6 bg-emerald-100 text-emerald-700 rounded-full text-sm font-semibold tracking-wide">
            ✨ QTahfidz Interaktif
          </div>
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 leading-tight mb-6">
            Hafalan Al-Qur'an <br />
            <span className="text-transparent bg-clip-text bg-linear-to-r from-emerald-600 to-teal-600">
              Lebih Mudah & Menyenangkan
            </span>
          </h1>
          <p className="text-lg text-gray-600 mb-8 leading-relaxed max-w-2xl mx-auto">
            Metode interaktif menyusun ayat untuk memperkuat hafalan Anda.
            Dengarkan, susun, dan cek hafalanmu.
          </p>

          {/* Controls */}
          <div className="bg-white p-4 rounded-2xl shadow-xl border border-gray-100 max-w-3xl mx-auto flex flex-col md:flex-row gap-4">
            <div className="flex-1">
              <SurahSelector
                selectedSurah={selectedSurah}
                onSelectSurah={handleSelectSurah}
              />
            </div>
            <div className="w-full md:w-48">
              <AyatSelector
                totalAyat={surahData ? surahData.jumlah_ayat : 0}
                selectedAyat={selectedAyat}
                onSelectAyat={setSelectedAyat}
                disabled={!surahData}
              />
            </div>
          </div>
        </div>
      </div>

      {/* Content Section */}
      <main className="grow container mx-auto px-6 py-12">
        {loading ? (
          <div className="text-center py-20">
            <div className="inline-block animate-spin rounded-full h-8 w-8 border-4 border-emerald-500 border-t-transparent"></div>
            <p className="mt-4 text-gray-500">Memuat data surah...</p>
          </div>
        ) : surahData ? (
          <div className="max-w-4xl mx-auto">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold text-gray-900 mb-2">
                Surah {surahData.nama_latin} ({surahData.nama})
              </h2>
              <p className="text-gray-500">
                {surahData.arti} • {surahData.jumlah_ayat} Ayat •{" "}
                {surahData.tempat_turun}
              </p>
            </div>

            <div
              className={`grid gap-8 ${
                selectedAyat ? "grid-cols-1" : "grid-cols-1"
              }`}
            >
              {filteredVerses.map((verse, index) => {
                // Calculate actual verse number
                const verseNumber = selectedAyat ? selectedAyat : index + 1;
                return (
                  <AyatCard
                    key={`${surahData.nomor}-${verseNumber}`}
                    surahNumber={surahData.nomor}
                    ayatNumber={verseNumber}
                    ayatText={verse.ar}
                    surahName={surahData.nama_latin}
                  />
                );
              })}
            </div>
          </div>
        ) : (
          <div className="text-center py-20 text-gray-500">
            Silakan pilih surah untuk memulai.
          </div>
        )}
      </main>

      <Footer />
    </div>
  );
};

export default QTahfidz;
