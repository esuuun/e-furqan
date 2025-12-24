import React, { useState, useEffect, useMemo, useRef } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import SurahSelectorLocal from "../components/qtahfidz/SurahSelectorLocal";
import AyatSelectorDropdown from "../components/qtahfidz/AyatSelectorDropdown";
import quranData from "../data/quran-data";

const QMushaf = () => {
  const [cardsData, setCardsData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedSurah, setSelectedSurah] = useState("");
  const [selectedAyat, setSelectedAyat] = useState("all");

  const cardRefs = useRef({});

  useEffect(() => {
    fetch("/quran-cards-data.json")
      .then((res) => res.json())
      .then((data) => {
        setCardsData(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error loading data:", err);
        setLoading(false);
      });
  }, []);

  // We don't need distinctSurat anymore for the dropdown,
  // but we might want to filter quranData to only show surahs that exist in cardsData?
  // For now, let's show all surahs from quranData, but if selected surah has no cards, it will just show empty.
  // Or better, we can filter quranData.

  const availableSurahIds = useMemo(() => {
    return new Set(cardsData.map((d) => d.surat));
  }, [cardsData]);

  const filteredQuranData = useMemo(() => {
    // If cardsData is loaded, filter quranData to only include surahs present in cardsData
    // If cardsData is empty (loading), maybe show all or none.
    if (cardsData.length === 0) return quranData;
    return quranData.filter((s) => availableSurahIds.has(s.id));
  }, [cardsData, availableSurahIds]);

  const distinctAyat = useMemo(() => {
    if (!selectedSurah) return [];
    return [
      ...new Set(
        cardsData
          .filter((d) => String(d.surat) === String(selectedSurah))
          .map((d) => d.ayat)
      ),
    ].sort((a, b) => a - b);
  }, [cardsData, selectedSurah]);

  const filteredCards = useMemo(() => {
    if (!selectedSurah) return [];
    let filtered = cardsData.filter(
      (d) => String(d.surat) === String(selectedSurah)
    );
    if (selectedAyat !== "all") {
      filtered = filtered.filter(
        (d) => String(d.ayat) === String(selectedAyat)
      );
    }
    return filtered;
  }, [cardsData, selectedSurah, selectedAyat]);

  const handleSurahChange = (id) => {
    setSelectedSurah(id);
    setSelectedAyat("all");
  };

  const handleAyatChange = (val) => {
    setSelectedAyat(val);
  };

  const scrollToCard = (index) => {
    const el = cardRefs.current[index];
    if (el) {
      el.scrollIntoView({ behavior: "smooth", block: "center" });
      // Optional: Add a temporary highlight class
      el.classList.add("ring-2", "ring-yellow-400", "ring-offset-2");
      setTimeout(() => {
        el.classList.remove("ring-2", "ring-yellow-400", "ring-offset-2");
      }, 1500);
    }
  };

  // Helper to safely get value
  const getVal = (item, key) => (item[key] ? item[key] : "-");

  // Fields configuration based on cards.html logic
  const fields = [
    { key: "akhiran", label: "Akhiran" },
    { key: "awalan", label: "Awalan" },
    { key: "kt_kar", label: "Kata/Akar" },
    { key: "irab", label: "I'rab / Pola" },
    { key: "teori", label: "Teori" },
    { key: "bentuk_kata", label: "Bentuk Kata" },
    { key: "ilal", label: "I'lal" },
    { key: "arti", label: "Arti" },
    { key: "terjemah", label: "Terjemah", fullWidth: true },
  ];

  return (
    <div className="min-h-screen flex flex-col bg-gray-50 dark:bg-gray-900 font-sans">
      <Navbar />

      {/* Hero Section (Adapted from original) */}
      <div className="relative bg-gradient-to-br from-gray-50 via-white to-gray-100 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900 pt-32 pb-12">
        <div className="container mx-auto px-6 relative z-10 text-center">
          <div className="inline-block px-4 py-1.5 mb-6 bg-yellow-100 dark:bg-yellow-900/50 text-yellow-800 dark:text-yellow-200 rounded-full text-sm font-semibold tracking-wide">
            📖 qMushaf Digital
          </div>
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white leading-tight mb-6">
            Analisis Kata per Kata
          </h1>
          <p className="text-lg text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
            Pelajari struktur bahasa Al-Qur'an dengan detail morfologi dan
            sintaksis yang lengkap.
          </p>
        </div>
      </div>

      <div className="container mx-auto px-4 py-8 flex-grow">
        {/* Controls */}
        <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 p-6 mb-8">
          <div className="flex flex-col md:flex-row gap-6 items-center justify-between">
            <div className="flex flex-col md:flex-row gap-4 w-full md:w-auto">
              <div className="w-full md:w-72">
                <SurahSelectorLocal
                  surahs={filteredQuranData}
                  selectedSurahId={selectedSurah}
                  onSelectSurah={handleSurahChange}
                />
              </div>

              <div className="w-full md:w-48">
                <AyatSelectorDropdown
                  availableAyats={distinctAyat}
                  selectedAyat={selectedAyat}
                  onSelectAyat={handleAyatChange}
                  disabled={!selectedSurah || loading}
                />
              </div>
            </div>

            <div className="text-yellow-700 dark:text-yellow-300 font-semibold bg-yellow-50 dark:bg-yellow-900/20 px-4 py-2 rounded-lg">
              {loading ? "Memuat Data..." : `${filteredCards.length} Kartu`}
            </div>
          </div>
        </div>

        {/* Content */}
        {loading ? (
          <div className="flex justify-center py-20">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-yellow-500"></div>
          </div>
        ) : !selectedSurah ? (
          <div className="text-center py-20 text-gray-500 dark:text-gray-400">
            Silakan pilih surat untuk memulai.
          </div>
        ) : (
          <>
            {/* Full Verse Display */}
            {selectedAyat !== "all" && filteredCards.length > 0 && (
              <div className="bg-white dark:bg-gray-800 rounded-2xl p-8 mb-10 border border-gray-200 dark:border-gray-700 shadow-lg shadow-gray-200/50 dark:shadow-black/50 text-center">
                <div
                  className="font-amiri text-4xl md:text-5xl text-gray-800 dark:text-gray-100 leading-loose mb-8 flex flex-wrap justify-center gap-x-3 dir-rtl"
                  dir="rtl"
                >
                  {filteredCards.map((item, idx) => (
                    <span
                      key={idx}
                      onClick={() => scrollToCard(idx)}
                      className="cursor-pointer hover:text-yellow-600 dark:hover:text-yellow-400 hover:bg-yellow-50 dark:hover:bg-yellow-900/30 rounded px-2 transition-all duration-200"
                      title="Lihat detail kata"
                    >
                      {item.lafdz}
                    </span>
                  ))}
                </div>
                <div className="text-xl text-gray-600 dark:text-gray-300 font-medium italic max-w-4xl mx-auto leading-relaxed">
                  {filteredCards
                    .map((item) => item.terjemah)
                    .filter((t) => t && t !== "-")
                    .join(" ")
                    .replace(/\s+/g, " ")
                    .trim()}
                </div>
              </div>
            )}

            {/* Cards Grid */}
            <div
              className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6"
              dir="rtl"
            >
              {filteredCards.map((item, index) => (
                <div
                  key={index}
                  ref={(el) => (cardRefs.current[index] = el)}
                  className="flex flex-col gap-4 dir-ltr transition-all duration-300"
                  dir="ltr"
                >
                  {/* Verse Header (Arabic Word) */}
                  <div className="bg-gradient-to-br from-gray-50 to-white dark:from-gray-800 dark:to-gray-700 border border-gray-200 dark:border-gray-600 rounded-xl p-6 text-center shadow-sm">
                    <div
                      className="font-amiri text-5xl text-gray-900 dark:text-white drop-shadow-sm"
                      dir="rtl"
                    >
                      {getVal(item, "lafdz")}
                    </div>
                  </div>

                  {/* Card Details */}
                  <div className="bg-white dark:bg-gray-800 rounded-xl shadow-md border border-gray-100 dark:border-gray-700 overflow-hidden hover:shadow-xl transition-shadow duration-300 flex flex-col h-full">
                    <div className="bg-gray-50 dark:bg-gray-700 px-5 py-3 flex justify-between items-center border-b border-gray-100 dark:border-gray-600">
                      <span className="text-xs font-bold text-gray-500 dark:text-gray-300 uppercase tracking-wider">
                        Surat: {getVal(item, "surat")}
                      </span>
                      <span className="text-xs font-bold text-gray-500 dark:text-gray-300 uppercase tracking-wider">
                        Ayat: {getVal(item, "ayat")}
                      </span>
                    </div>

                    <div className="p-5 grid grid-cols-2 gap-4 text-sm flex-grow">
                      {fields.map((f) => {
                        const val = getVal(item, f.key);
                        if (val === "-" && f.key !== "terjemah") return null;

                        return (
                          <div
                            key={f.key}
                            className={`flex flex-col border-b border-gray-100 dark:border-gray-700 pb-2 last:border-0 ${
                              f.fullWidth
                                ? "col-span-2 text-center mt-2 pt-2 border-t"
                                : ""
                            }`}
                          >
                            <div className="text-[10px] font-bold text-yellow-600 dark:text-yellow-400 uppercase mb-1 tracking-wide">
                              {f.label}
                            </div>
                            <div
                              className={`font-medium text-gray-700 dark:text-gray-300 ${
                                f.key === "terjemah"
                                  ? "text-base italic text-gray-900 dark:text-gray-100"
                                  : ""
                              }`}
                            >
                              {val}
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </>
        )}
      </div>
      <Footer />
    </div>
  );
};

export default QMushaf;
