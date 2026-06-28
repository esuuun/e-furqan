import React, { useState, useEffect, useRef } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import { 
  Volume2, 
  Square, 
  Play, 
  ChevronLeft, 
  ChevronRight, 
  Sparkles 
} from "lucide-react";

// ─── FLASHCARD COMPONENT ─────────────────────────────────────────────
const Flashcard = ({ word, surahId, ayatNumber, playAudioGlobal, rootWord }) => {
  const [isFlipped, setIsFlipped] = useState(false);

  // Reset flipped state if word changes
  useEffect(() => {
    setIsFlipped(false);
  }, [word]);

  // If the word is the "end" marker (verse number), render a decorative medallion
  if (word.char_type_name === "end") {
    return (
      <div className="word-scene w-28 h-28 flex items-center justify-center">
        <div className="word-card w-full h-full">
          <div className="word-card-face word-card-front flex items-center justify-center border-2 border-dashed border-gray-200 dark:border-gray-800 bg-gray-50/50 dark:bg-zinc-900/30 rounded-2xl shadow-xs">
            <span className="font-arabic text-xl font-bold text-yellow-600 dark:text-yellow-400 select-none">
              {word.text_uthmani}
            </span>
          </div>
        </div>
      </div>
    );
  }

  const handleCardClick = () => {
    setIsFlipped(!isFlipped);
    if (word.char_type_name === "word") {
      // Reconstruct audio URL manually to fix API offset bugs
      const paddedSurah = String(surahId).padStart(3, "0");
      const paddedAyat = String(ayatNumber).padStart(3, "0");
      const paddedPos = String(word.position).padStart(3, "0");
      const constructedAudioUrl = `https://verses.quran.com/wbw/${paddedSurah}_${paddedAyat}_${paddedPos}.mp3`;
      
      playAudioGlobal(constructedAudioUrl, false);
    }
  };

  return (
    <div className="word-scene w-32 h-32 sm:w-36 sm:h-36 cursor-pointer group" onClick={handleCardClick}>
      <div className={`word-card w-full h-full relative ${isFlipped ? "is-flipped" : ""}`}>
        {/* FRONT FACE */}
        <div className="word-card-face word-card-front absolute w-full h-full p-4 flex flex-col justify-center items-center rounded-2xl bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 shadow-sm hover:border-yellow-500 dark:hover:border-yellow-500 hover:shadow-md hover:shadow-yellow-500/5 transition duration-300">
          <div className="absolute top-2.5 left-2.5 opacity-45 group-hover:opacity-100 group-hover:text-yellow-600 dark:group-hover:text-yellow-400 transition duration-300">
            <Volume2 className="w-3.5 h-3.5" />
          </div>
          <div className="font-arabic text-2xl font-bold text-gray-900 dark:text-white leading-relaxed select-none">
            {word.text_uthmani}
          </div>
        </div>

        {/* BACK FACE */}
        <div dir="ltr" className="word-card-face word-card-back absolute w-full h-full p-4 flex flex-col justify-center items-center rounded-2xl bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 shadow-sm hover:border-yellow-500 dark:hover:border-yellow-500 hover:shadow-md hover:shadow-yellow-500/5 transition duration-300">
          <div className="text-xs sm:text-sm font-semibold text-gray-700 dark:text-gray-300 leading-snug line-clamp-3 text-center">
            {word.translation?.text || ""}
          </div>
          {rootWord && (
            <div dir="rtl" className="mt-2 text-[10px] sm:text-xs font-bold text-yellow-600 dark:text-yellow-400 bg-yellow-50 dark:bg-yellow-950/30 px-2 py-0.5 rounded-md font-arabic select-none">
              {rootWord}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

// ─── MAIN COMPONENT ──────────────────────────────────────────────────
const QTahfidz = () => {
  const [surahs, setSurahs] = useState([]);
  const [currentSurahId, setCurrentSurahId] = useState(1);
  const [ayatData, setAyatData] = useState([]);
  const [currentAyatIndex, setCurrentAyatIndex] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  const [rootDictionary, setRootDictionary] = useState({});
  const [isPlayingVerse, setIsPlayingVerse] = useState(false);

  const currentAudioRef = useRef(null);

  // Stop currently playing audio
  const stopAudio = () => {
    if (currentAudioRef.current) {
      currentAudioRef.current.pause();
      currentAudioRef.current.currentTime = 0;
    }
    setIsPlayingVerse(false);
  };

  // Play audio globally
  const playAudioGlobal = (url, isVerse) => {
    stopAudio();
    const audio = new Audio(url);
    currentAudioRef.current = audio;
    if (isVerse) {
      setIsPlayingVerse(true);
    }
    audio.play().catch((e) => {
      console.warn("Audio Context error:", e);
      if (isVerse) setIsPlayingVerse(false);
    });
    audio.onended = () => {
      if (isVerse) setIsPlayingVerse(false);
    };
  };

  // Cleanup audio on index change or unmount
  useEffect(() => {
    stopAudio();
    return () => stopAudio();
  }, [currentAyatIndex, currentSurahId]);

  // Fetch Surah list & roots database on mount
  useEffect(() => {
    const fetchAllSurahs = async () => {
      try {
        const res = await fetch("https://api.quran.com/api/v4/chapters?language=id");
        const data = await res.json();
        setSurahs(data.chapters || []);
      } catch (error) {
        console.error("Error fetching chapters:", error);
      }
    };

    const fetchRoots = async () => {
      try {
        const res = await fetch("/roots.json");
        const data = await res.json();
        setRootDictionary(data || {});
      } catch (error) {
        console.error("Error fetching roots:", error);
      }
    };

    fetchAllSurahs();
    fetchRoots();
  }, []);

  // Fetch all verses of selected Surah
  useEffect(() => {
    const fetchSurah = async () => {
      setIsLoading(true);
      try {
        let allVerses = [];
        let currentPage = 1;
        let totalPages = 1;

        do {
          const res = await fetch(
            `https://api.quran.com/api/v4/verses/by_chapter/${currentSurahId}?language=id&words=true&word_fields=text_uthmani&word_translation_language=id&audio=7&per_page=100&page=${currentPage}`
          );
          const data = await res.json();
          allVerses = [...allVerses, ...(data.verses || [])];
          totalPages = data.pagination?.total_pages || 1;
          currentPage++;
        } while (currentPage <= totalPages);

        const formattedData = allVerses.map((verse) => ({
          ayatNumber: verse.verse_number,
          fullText: verse.words.map((w) => w.text_uthmani).join(" "),
          words: verse.words || [],
          audioUrl: verse.audio?.url ? `https://verses.quran.com/${verse.audio.url}` : null,
        }));

        setAyatData(formattedData);
        setCurrentAyatIndex(0);
      } catch (error) {
        console.error("Error fetching verses:", error);
      }
      setIsLoading(false);
    };

    fetchSurah();
  }, [currentSurahId]);

  const handleNext = () => {
    setCurrentAyatIndex((prev) => (prev < ayatData.length - 1 ? prev + 1 : prev));
  };

  const handlePrev = () => {
    setCurrentAyatIndex((prev) => (prev > 0 ? prev - 1 : prev));
  };

  const currentAyat = ayatData[currentAyatIndex];

  return (
    <div className="min-h-screen flex flex-col bg-white dark:bg-gray-900 font-sans text-gray-800 dark:text-gray-200">
      <Navbar />

      {/* Styled Animations and 3D Flip Card classes */}
      <style>{`
        .word-scene {
          perspective: 1000px;
        }
        .word-card {
          transition: transform 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
          transform-style: preserve-3d;
        }
        .word-card.is-flipped {
          transform: rotateY(180deg);
        }
        .word-card-face {
          backface-visibility: hidden;
          -webkit-backface-visibility: hidden;
        }
        .word-card-back {
          transform: rotateY(180deg);
        }
      `}</style>

      {/* Hero Banner Section */}
      <div className="relative bg-linear-to-br from-gray-50 via-white to-gray-100 dark:from-gray-900 dark:via-gray-900 dark:to-gray-950 pt-32 pb-16 overflow-hidden border-b border-gray-100 dark:border-gray-800">
        <div className="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-yellow-100 dark:bg-yellow-900/10 rounded-full blur-3xl opacity-50" />
        <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-80 h-80 bg-yellow-50 dark:bg-yellow-900/5 rounded-full blur-3xl opacity-50" />

        <div className="container mx-auto px-6 relative z-10 text-center">
          <div className="inline-flex items-center px-4 py-1.5 mb-6 bg-yellow-100 dark:bg-yellow-950/40 text-yellow-800 dark:text-yellow-300 rounded-full text-sm font-semibold tracking-wide gap-2 border border-yellow-200/50 dark:border-yellow-900/30">
            <Sparkles className="w-4 h-4 text-yellow-500" />
            <span>qTahfidz — Flip Card Memory Game</span>
          </div>

          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white leading-tight mb-6">
            Hafalan Al-Qur'an <br />
            <span className="text-transparent bg-clip-text bg-linear-to-r from-yellow-500 to-yellow-600">
              Per Kata Secara Mandiri
            </span>
          </h1>

          <p className="text-base text-gray-600 dark:text-gray-400 mb-8 max-w-2xl mx-auto leading-relaxed">
            Metode interaktif menghafal dan memahami arti kosakata per lafadz. Pilih surah dan ayat di bawah, lalu ketuk kartu untuk membalik dan mendengarkan lafalnya.
          </p>

          {/* Selectors */}
          <div className="bg-white dark:bg-gray-900 p-6 rounded-2xl shadow-xs border border-gray-200 dark:border-gray-800 max-w-3xl mx-auto flex flex-col sm:flex-row justify-center items-center gap-4">
            <div className="w-full sm:w-1/2 flex flex-col items-start gap-1">
              <label className="text-[11px] font-bold text-gray-400 dark:text-gray-500 uppercase tracking-wider">Pilih Surah</label>
              <select
                className="w-full px-4 py-2.5 rounded-xl border border-gray-250 dark:border-gray-800 bg-white dark:bg-gray-900 text-gray-800 dark:text-gray-200 outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer"
                value={currentSurahId}
                onChange={(e) => setCurrentSurahId(Number(e.target.value))}
              >
                {surahs.map((surah) => (
                  <option key={surah.id} value={surah.id}>
                    Surah {surah.id} - {surah.name_simple}
                  </option>
                ))}
              </select>
            </div>

            <div className="w-full sm:w-1/2 flex flex-col items-start gap-1">
              <label className="text-[11px] font-bold text-gray-400 dark:text-gray-500 uppercase tracking-wider">Pilih Ayat</label>
              {!isLoading && ayatData.length > 0 ? (
                <select
                  className="w-full px-4 py-2.5 rounded-xl border border-gray-250 dark:border-gray-800 bg-white dark:bg-gray-900 text-gray-800 dark:text-gray-200 outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer"
                  value={currentAyatIndex}
                  onChange={(e) => setCurrentAyatIndex(Number(e.target.value))}
                >
                  {ayatData.map((ayat, idx) => (
                    <option key={ayat.ayatNumber} value={idx}>
                      Ayat {ayat.ayatNumber}
                    </option>
                  ))}
                </select>
              ) : (
                <div className="w-full px-4 py-2.5 rounded-xl border border-gray-200 dark:border-gray-800 bg-gray-50 dark:bg-gray-800 text-gray-400 text-left text-sm select-none">
                  Memuat ayat...
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Main Content Area */}
      <main className="grow container mx-auto px-6 py-12">
        {isLoading ? (
          <div className="flex flex-col items-center justify-center py-24 gap-4">
            <div className="animate-spin rounded-full h-10 w-10 border-b-2 border-yellow-500" />
            <p className="text-sm font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider animate-pulse">
              Memuat data ayat...
            </p>
          </div>
        ) : (
          currentAyat && (
            <div className="max-w-4xl mx-auto flex flex-col items-center">
              {/* Entire Verse Player Card */}
              <div className="w-full bg-slate-50/50 dark:bg-zinc-950/30 rounded-3xl p-6 sm:p-8 border border-gray-200/60 dark:border-gray-800/60 flex flex-col items-center mb-10 gap-6">
                <div dir="rtl" className="font-arabic text-3xl sm:text-4xl text-gray-900 dark:text-white leading-loose text-center select-none">
                  {currentAyat.fullText}
                </div>

                {currentAyat.audioUrl && (
                  <div>
                    {isPlayingVerse ? (
                      <button
                        onClick={stopAudio}
                        className="px-6 py-2.5 rounded-full border border-red-500 text-red-500 hover:bg-red-500 hover:text-white text-xs font-bold uppercase tracking-wider transition duration-300 flex items-center gap-1.5 cursor-pointer shadow-xs"
                      >
                        <Square className="w-3.5 h-3.5 animate-pulse" />
                        Hentikan Audio
                      </button>
                    ) : (
                      <button
                        onClick={() => playAudioGlobal(currentAyat.audioUrl, true)}
                        className="px-6 py-2.5 rounded-full border border-yellow-500 hover:bg-yellow-500 hover:text-white dark:hover:text-gray-900 text-yellow-600 dark:text-yellow-400 text-xs font-bold uppercase tracking-wider transition duration-300 flex items-center gap-1.5 cursor-pointer shadow-xs"
                      >
                        <Play className="w-3.5 h-3.5 fill-current" />
                        Putar Ayat Lengkap
                      </button>
                    )}
                  </div>
                )}
              </div>

              {/* Grid of Word Flashcards */}
              <div 
                key={`${currentSurahId}-${currentAyatIndex}`} 
                dir="rtl"
                className="words-grid flex flex-wrap gap-4 sm:gap-6 justify-center w-full mb-12"
              >
                {currentAyat.words.map((word) => (
                  <Flashcard
                    key={word.id}
                    word={word}
                    surahId={currentSurahId}
                    ayatNumber={currentAyat.ayatNumber}
                    playAudioGlobal={playAudioGlobal}
                    rootWord={rootDictionary[`${currentSurahId}_${currentAyat.ayatNumber}_${word.position}`]}
                  />
                ))}
              </div>

              {/* Navigation Controls */}
              <div className="flex justify-center items-center gap-6 pt-6 border-t border-gray-100 dark:border-gray-800 w-full">
                <button
                  onClick={handlePrev}
                  disabled={currentAyatIndex === 0}
                  className="px-5 py-2.5 rounded-full border border-gray-250 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-700 dark:text-gray-300 disabled:opacity-30 disabled:cursor-not-allowed text-xs font-bold uppercase tracking-wider transition duration-300 flex items-center cursor-pointer gap-1.5"
                >
                  <ChevronLeft className="w-3.5 h-3.5" />
                  Sebelumnya
                </button>

                <span className="text-sm font-bold text-gray-500 dark:text-gray-400 tracking-wide select-none">
                  Ayat {currentAyat.ayatNumber} / {ayatData.length}
                </span>

                <button
                  onClick={handleNext}
                  disabled={currentAyatIndex === ayatData.length - 1}
                  className="px-5 py-2.5 rounded-full border border-gray-250 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-700 dark:text-gray-300 disabled:opacity-30 disabled:cursor-not-allowed text-xs font-bold uppercase tracking-wider transition duration-300 flex items-center cursor-pointer gap-1.5"
                >
                  Selanjutnya
                  <ChevronRight className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
          )
        )}
      </main>

      <Footer />
    </div>
  );
};

export default QTahfidz;
