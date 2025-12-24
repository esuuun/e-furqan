import React, { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import SurahSelectorLocal from "../components/qtahfidz/SurahSelectorLocal";
import AyatGridSelector from "../components/qtahfidz/AyatGridSelector";
import DraggableAyatCard from "../components/qtahfidz/DraggableAyatCard";
import quranData from "../data/quran-data";

const QTahfidz = () => {
  const [selectedSurahId, setSelectedSurahId] = useState(62); // Default Al-Jumu'ah
  const [selectedAyahs, setSelectedAyahs] = useState([]);
  const [gameStarted, setGameStarted] = useState(false);

  // Get current Surah data
  const currentSurah = quranData.find((s) => s.id === selectedSurahId);

  // Reset selection when Surah changes
  const handleSurahChange = (id) => {
    setSelectedSurahId(id);
    setSelectedAyahs([]);
    setGameStarted(false);
  };

  // Handle Start Game
  const handleStartGame = () => {
    if (selectedAyahs.length > 0) {
      setGameStarted(true);
      // Scroll to game area
      setTimeout(() => {
        document
          .getElementById("game-area")
          ?.scrollIntoView({ behavior: "smooth" });
      }, 100);
    }
  };

  // Handle Reset
  const handleReset = () => {
    setGameStarted(false);
    setSelectedAyahs([]);
  };

  // Helper to process verses (split long ones)
  const getProcessedVerses = () => {
    if (!currentSurah) return [];

    const versesToRender = [];

    selectedAyahs.forEach((ayahNum) => {
      const verse = currentSurah.verses.find((v) => v.id === ayahNum);
      if (!verse) return;

      const cleanText = verse.text.replace(/[\u200B-\u200D\uFEFF]/g, "").trim();
      const words = cleanText.split(/\s+/).filter((w) => w.length > 0);

      if (words.length <= 15) {
        versesToRender.push(verse);
      } else {
        const chunkSize = 12;
        let chunkIndex = 1;
        for (let i = 0; i < words.length; i += chunkSize) {
          const chunkText = words.slice(i, i + chunkSize).join(" ");
          versesToRender.push({
            id: `${verse.id}.${chunkIndex}`,
            text: chunkText,
            originalId: verse.id,
          });
          chunkIndex++;
        }
      }
    });

    return versesToRender;
  };

  const processedVerses = gameStarted ? getProcessedVerses() : [];

  return (
    <div className="min-h-screen flex flex-col bg-white dark:bg-gray-900 font-sans">
      <Navbar />

      {/* Hero Section */}
      <div className="relative bg-linear-to-br from-gray-50 via-white to-gray-100 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900 pt-32 pb-16">
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          <div className="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-yellow-100 dark:bg-yellow-900/20 rounded-full blur-3xl opacity-50"></div>
          <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-80 h-80 bg-yellow-50 dark:bg-yellow-900/10 rounded-full blur-3xl opacity-50"></div>
        </div>

        <div className="container mx-auto px-6 relative z-10 text-center">
          <div className="inline-block px-4 py-1.5 mb-6 bg-yellow-100 dark:bg-yellow-900/50 text-yellow-800 dark:text-yellow-200 rounded-full text-sm font-semibold tracking-wide">
            ✨ QTahfidz Interaktif
          </div>
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white leading-tight mb-6">
            Hafalan Al-Qur'an <br />
            <span className="text-transparent bg-clip-text bg-linear-to-r from-yellow-500 to-yellow-600">
              Lebih Mudah & Menyenangkan
            </span>
          </h1>
          <p className="text-lg text-gray-600 dark:text-gray-300 mb-8 leading-relaxed max-w-2xl mx-auto">
            Pilih surah dan ayat, lalu susun potongan ayat untuk menguji
            hafalanmu.
          </p>

          {/* Controls */}
          <div className="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-xl border border-gray-100 dark:border-gray-700 max-w-4xl mx-auto">
            <div className="grid md:grid-cols-3 gap-6">
              <div className="md:col-span-1">
                <SurahSelectorLocal
                  surahs={quranData}
                  selectedSurahId={selectedSurahId}
                  onSelectSurah={handleSurahChange}
                />
              </div>
              <div className="md:col-span-2">
                {currentSurah && (
                  <AyatGridSelector
                    surah={currentSurah}
                    selectedAyahs={selectedAyahs}
                    onSelectionChange={setSelectedAyahs}
                  />
                )}
              </div>
            </div>

            {/* Action Buttons */}
            <div className="mt-8 flex justify-center gap-4 border-t border-gray-100 dark:border-gray-700 pt-6">
              <button
                onClick={handleStartGame}
                disabled={selectedAyahs.length === 0}
                className={`px-8 py-3 rounded-xl font-semibold shadow-lg transition-all transform hover:-translate-y-0.5 ${
                  selectedAyahs.length > 0
                    ? "bg-yellow-500 text-white hover:bg-yellow-600 hover:shadow-yellow-500/30"
                    : "bg-gray-200 dark:bg-gray-700 text-gray-400 dark:text-gray-500 cursor-not-allowed"
                }`}
              >
                Mulai Hafalan ({selectedAyahs.length} Ayat)
              </button>
              {gameStarted && (
                <button
                  onClick={handleReset}
                  className="px-8 py-3 rounded-xl font-semibold bg-white dark:bg-gray-700 text-gray-700 dark:text-gray-200 border border-gray-200 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-600 hover:border-gray-300 dark:hover:border-gray-500 transition-all"
                >
                  Reset
                </button>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Game Area */}
      {gameStarted && currentSurah && (
        <main
          id="game-area"
          className="grow container mx-auto px-6 py-12 bg-gray-50 dark:bg-gray-900"
        >
          <div className="max-w-4xl mx-auto space-y-8">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-2">
                {currentSurah.transliteration} ({currentSurah.name})
              </h2>
            </div>

            <div className="space-y-8">
              {processedVerses.map((verse) => (
                <DraggableAyatCard
                  key={`${selectedSurahId}-${verse.id}`}
                  verse={verse}
                  surahName={currentSurah.transliteration}
                  surahId={selectedSurahId}
                />
              ))}
            </div>
          </div>
        </main>
      )}

      <Footer />
    </div>
  );
};

export default QTahfidz;
