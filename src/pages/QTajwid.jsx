import React, { useState, useEffect, useRef, useCallback } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

// ─── DATASET: 6 LEVELS OF METODE TILAWATI ──────────────────────────
const LEVELS_DATA = [
  {
    id: 1,
    title: "Level 1: Harakat Fathah",
    desc: "Hijaiyah Tunggal Fathah",
    subtitle: "Membaca huruf Hijaiyah tunggal berharakat Fathah (a)",
    pdfPath: "/qtajwid/belajar membaca/Tilawati_1.pdf",
    data: [
      { a: "اَ", l: "a" }, { a: "بَ", l: "ba" }, { a: "تَ", l: "ta" }, { a: "ثَ", l: "tsa" },
      { a: "جَ", l: "ja" }, { a: "حَ", l: "ha" }, { a: "خَ", l: "kha" }, { a: "دَ", l: "da" },
      { a: "ذَ", l: "dza" }, { a: "رَ", l: "ra" }, { a: "زَ", l: "za" }, { a: "سَ", l: "sa" },
      { a: "شَ", l: "sya" }, { a: "صَ", l: "sha" }, { a: "ضَ", l: "dha" }, { a: "طَ", l: "tha" },
      { a: "ظَ", l: "zha" }, { a: "عَ", l: "'a" }, { a: "غَ", l: "gha" }, { a: "فَ", l: "fa" },
      { a: "قَ", l: "qa" }, { a: "كَ", l: "ka" }, { a: "لَ", l: "la" }, { a: "مَ", l: "ma" },
      { a: "نَ", l: "na" }, { a: "وَ", l: "wa" }, { a: "هَ", l: "ha" }, { a: "يَ", l: "ya" }
    ]
  },
  {
    id: 2,
    title: "Level 2: Kasrah, Dhommah & Tanwin",
    desc: "Harakat i, u, dan Tanwin",
    subtitle: "Belajar membaca harakat Kasrah (i), Dhommah (u), dan Tanwin (an, in, un)",
    pdfPath: "/qtajwid/belajar membaca/Tilawati_2.pdf",
    data: [
      { a: "بِ", l: "bi" }, { a: "بُ", l: "bu" }, { a: "تِ", l: "ti" }, { a: "تُ", l: "tu" },
      { a: "ثِ", l: "tsi" }, { a: "ثُ", l: "tsu" }, { a: "جِ", l: "ji" }, { a: "جُ", l: "ju" },
      { a: "حِ", l: "hi" }, { a: "حُ", l: "hu" }, { a: "خِ", l: "khi" }, { a: "خُ", l: "khu" },
      { a: "دِ", l: "di" }, { a: "دُ", l: "du" }, { a: "رِ", l: "ri" }, { a: "رُ", l: "ru" },
      { a: "زِ", l: "zi" }, { a: "زُ", l: "zu" }, { a: "سِ", l: "si" }, { a: "سُ", l: "su" },
      { a: "شِ", l: "syi" }, { a: "شُ", l: "syu" }, { a: "صِ", l: "shi" }, { a: "صُ", l: "shu" },
      { a: "طِ", l: "thi" }, { a: "طُ", l: "thu" }, { a: "عِ", l: "'i" }, { a: "عُ", l: "'u" },
      { a: "فِ", l: "fi" }, { a: "فُ", l: "fu" }, { a: "قِ", l: "qi" }, { a: "قُ", l: "qu" },
      { a: "كِ", l: "ki" }, { a: "كُ", l: "ku" }, { a: "لِ", l: "li" }, { a: "لُ", l: "lu" },
      { a: "مِ", l: "mi" }, { a: "مُ", l: "mu" }, { a: "نِ", l: "ni" }, { a: "نُ", l: "nu" },
      { a: "وِ", l: "wi" }, { a: "وُ", l: "wu" }, { a: "يِ", l: "yi" }, { a: "يُ", l: "yu" },
      { a: "بً", l: "ban" }, { a: "بٍ", l: "bin" }, { a: "بٌ", l: "bun" },
      { a: "تً", l: "tan" }, { a: "تٍ", l: "tin" }, { a: "تٌ", l: "tun" },
      { a: "دً", l: "dan" }, { a: "دٍ", l: "din" }, { a: "دٌ", l: "dun" },
      { a: "رً", l: "ran" }, { a: "رٍ", l: "rin" }, { a: "رٌ", l: "run" },
      { a: "سً", l: "san" }, { a: "سٍ", l: "sin" }, { a: "سٌ", l: "sun" }
    ]
  },
  {
    id: 3,
    title: "Level 3: Huruf Sukun, Au & Ai",
    desc: "Sukun (Mati) & Mad Layyin",
    subtitle: "Membaca huruf bersukun (mati) serta mad layyin (au dan ai)",
    pdfPath: "/qtajwid/belajar membaca/Tilawati_3.pdf",
    data: [
      { a: "مَلْ", l: "mal" }, { a: "سَلْ", l: "sal" }, { a: "قُلْ", l: "qul" }, { a: "بَلْ", l: "bal" },
      { a: "تَمْ", l: "tam" }, { a: "كَمْ", l: "kam" }, { a: "هُمْ", l: "hum" }, { a: "كُمْ", l: "kum" },
      { a: "مَسْ", l: "mas" }, { a: "بِسْ", l: "bis" }, { a: "يَشْ", l: "yash" }, { a: "مُشْ", l: "mush" },
      { a: "مَرْ", l: "mar" }, { a: "بَرْ", l: "bar" }, { a: "تَرْ", l: "tar" }, { a: "يَرْ", l: "yar" },
      { a: "يَأْ", l: "ya'" }, { a: "مُتْ", l: "mut" }, { a: "يَعْ", l: "ya'" }, { a: "بَعْ", l: "ba'" },
      { a: "يَوْ", l: "yau" }, { a: "قَوْ", l: "qau" }, { a: "سَوْ", l: "sau" }, { a: "لَوْ", l: "lau" },
      { a: "حَوْ", l: "hau" }, { a: "خَوْ", l: "khau" }, { a: "نَوْ", l: "nau" }, { a: "مَوْ", l: "mau" },
      { a: "أَيْ", l: "ai" }, { a: "بَيْ", l: "bai" }, { a: "خَيْ", l: "khai" }, { a: "شَيْ", l: "syai" },
      { a: "لَيْ", l: "lai" }, { a: "كَيْ", l: "kai" }, { a: "غَيْ", l: "ghai" }, { a: "عَيْ", l: "'ai" }
    ]
  },
  {
    id: 4,
    title: "Level 4: Tasydid & Ghunnah",
    desc: "Penekanan & Dengung",
    subtitle: "Membaca huruf bertasydid (dobel) dan ghunnah (dengung)",
    pdfPath: "/qtajwid/belajar membaca/Tilawati_4.pdf",
    data: [
      { a: "سَبَّ", l: "sabba" }, { a: "حَقَّ", l: "haqqa" }, { a: "مَسَّ", l: "massa" }, { a: "شَدَّ", l: "syadda" },
      { a: "رَبَّ", l: "rabba" }, { a: "ظَنَّ", l: "zhanna" }, { a: "دَقَّ", l: "daqqa" }, { a: "عَضَّ", l: "'adhdha" },
      { a: "إِنَّ", l: "inna" }, { a: "أَنَّ", l: "anna" }, { a: "ثُمَّ", l: "tsumma" }, { a: "عَمَّ", l: "'amma" },
      { a: "لَمَّا", l: "lamma" }, { a: "كَأَنَّ", l: "ka-anna" }, { a: "مِنَّا", l: "minna" },
      { a: "رَبِّ", l: "rabbi" }, { a: "يُحِبُّ", l: "yuhibbu" }, { a: "يَظُنُّ", l: "yazhunnu" }, { a: "حَقُّ", l: "haqqu" },
      { a: "قَدَّمَ", l: "qaddama" }, { a: "سَبَّحَ", l: "sabbaha" }, { a: "كَذَّبَ", l: "kadzdzaba" }
    ]
  },
  {
    id: 5,
    title: "Level 5: Tajwid Dasar",
    desc: "Qalqalah, Idgham, Iqlab, Ikhfa, Idzhar",
    subtitle: "Membaca hukum tajwid praktis: Idgham, Qalqalah, Iqlab, Ikhfa, dan Idzhar",
    pdfPath: "/qtajwid/belajar membaca/Tilawati_5.pdf",
    data: [
      { a: "مِنْ وَ", l: "miw wa" }, { a: "مِنْ يَّ", l: "miy ya" },
      { a: "أَبْ", l: "ab" }, { a: "تَجْ", l: "taj" }, { a: "يَدْ", l: "yad" },
      { a: "مِنْ بَ", l: "mim ba" }, { a: "عٌ بَ", l: "um ba" },
      { a: "هُمْ بِ", l: "hum bi" }, { a: "هُمْ مَ", l: "hum ma" },
      { a: "مِنْ رَ", l: "mir ra" }, { a: "لٌ لِ", l: "lul li" },
      { a: "مِنْ خَ", l: "min kha" }, { a: "مِنْ عَ", l: "min 'a" },
      { a: "الۤمّۤ", l: "alif laam miim" }, { a: "يٰسۤ", l: "yaa siin" },
      { a: "نۤ", l: "nuun" }, { a: "قۤ", l: "qaaf" }
    ]
  },
  {
    id: 6,
    title: "Level 6: Ghorib & Surat Pendek",
    desc: "Level Akhir & Ghorib",
    subtitle: "Membaca bacaan-bacaan ghorib (khusus) dan potongan surat pendek",
    pdfPath: "/qtajwid/belajar membaca/Tilawati_6.pdf",
    data: [
      { a: "مَجْرٰىهَا", l: "majreeha" }, { a: "لَا تَأْمَنَّا", l: "laa ta'manna" },
      { a: "ءَاَعْجَمِيٌّ", l: "a-a'jamiyyun" }, { a: "بِئْسَ الِاسْمُ", l: "bi'sal-lismu" },
      { a: "بَلْۜ رَانَ", l: "bal raana" }, { a: "مَنْۜ رَاقٍ", l: "man raaq" },
      { a: "عِوَجًاۜ", l: "'iwajaa" }, { a: "اَنَا", l: "ana" }, { a: "لٰكِنَّا", l: "laakinna" },
      { a: "قُلْ هُوَ", l: "qul huwa" }, { a: "اللّٰهُ اَحَدٌ", l: "allahu ahad" },
      { a: "اللّٰهُ الصَّمَدُ", l: "allahu sh-shamad" }, { a: "مِنْ شَرِّ", l: "min syarri" },
      { a: "مَا خَلَقَ", l: "maa khalaq" }
    ]
  }
];

// Helper to shuffle arrays
const shuffle = (array) => {
  return [...array].sort(() => Math.random() - 0.5);
};

// ─── MAIN COMPONENT ──────────────────────────────────────────────────
const QTajwid = () => {
  const [selectedLevel, setSelectedLevel] = useState(null);
  const [activeGame, setActiveGame] = useState(null); // null | "tebak" | "balon" | "susun"
  const [audioEnabled, setAudioEnabled] = useState(true);

  // Sound Engine using Web Audio API (Oscillators)
  const playPopSound = useCallback(() => {
    if (!audioEnabled) return;
    try {
      const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.type = "sine";
      osc.frequency.setValueAtTime(800, audioCtx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(100, audioCtx.currentTime + 0.1);
      gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
      osc.start(audioCtx.currentTime);
      osc.stop(audioCtx.currentTime + 0.1);
    } catch (e) {
      console.warn("Audio Context blocked or unsupported:", e);
    }
  }, [audioEnabled]);

  const playCorrectSound = useCallback(() => {
    if (!audioEnabled) return;
    try {
      const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.type = "triangle";
      osc.frequency.setValueAtTime(523.25, audioCtx.currentTime); // C5
      osc.frequency.setValueAtTime(659.25, audioCtx.currentTime + 0.08); // E5
      osc.frequency.setValueAtTime(783.99, audioCtx.currentTime + 0.16); // G5
      gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.35);
      osc.start(audioCtx.currentTime);
      osc.stop(audioCtx.currentTime + 0.35);
    } catch (e) {
      console.warn("Audio Context blocked or unsupported:", e);
    }
  }, [audioEnabled]);

  const playWrongSound = useCallback(() => {
    if (!audioEnabled) return;
    try {
      const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.type = "sawtooth";
      osc.frequency.setValueAtTime(130.81, audioCtx.currentTime); // C3
      gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.3);
      osc.start(audioCtx.currentTime);
      osc.stop(audioCtx.currentTime + 0.3);
    } catch (e) {
      console.warn("Audio Context blocked or unsupported:", e);
    }
  }, [audioEnabled]);

  // TTS Readout Engine
  const speakReading = useCallback((text) => {
    if (!audioEnabled) return;
    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
      const cleanText = text.replace("(pendek)", "").trim();
      const msg = new SpeechSynthesisUtterance(cleanText);
      msg.lang = "id-ID";
      msg.rate = 0.8;
      window.speechSynthesis.speak(msg);
    }
  }, [audioEnabled]);

  // Back to level detail dashboard
  const handleBackToDashboard = () => {
    setSelectedLevel(null);
    setActiveGame(null);
  };

  // Back to game selection
  const handleBackToGameMenu = () => {
    setActiveGame(null);
  };

  return (
    <div className="min-h-screen flex flex-col bg-white dark:bg-gray-900 font-sans text-gray-800 dark:text-gray-200">
      <Navbar />

      {/* Styled Animations for Balon Game */}
      <style>{`
        @keyframes floatUp {
          0% { transform: translateY(420px) rotate(-3deg); }
          50% { transform: translateY(150px) rotate(3deg); }
          100% { transform: translateY(-100px) rotate(-3deg); }
        }
        @keyframes wrongShake {
          0%, 100% { transform: translateX(0); }
          25% { transform: translateX(-8px); }
          75% { transform: translateX(8px); }
        }
        .float-balloon {
          animation: floatUp 7s linear infinite;
        }
        .shake-element {
          animation: wrongShake 0.3s ease-in-out;
        }
      `}</style>

      {/* Hero Banner Section */}
      <div className="relative bg-linear-to-br from-gray-50 via-white to-gray-100 dark:from-gray-900 dark:via-gray-900 dark:to-gray-950 pt-32 pb-16 overflow-hidden border-b border-gray-100 dark:border-gray-800">
        <div className="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-yellow-100 dark:bg-yellow-900/10 rounded-full blur-3xl opacity-50" />
        <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-80 h-80 bg-yellow-50 dark:bg-yellow-900/5 rounded-full blur-3xl opacity-50" />

        <div className="container mx-auto px-6 relative z-10 text-center">
          <div className="inline-flex items-center px-4 py-1.5 mb-6 bg-yellow-100 dark:bg-yellow-950/40 text-yellow-800 dark:text-yellow-300 rounded-full text-sm font-semibold tracking-wide gap-2 border border-yellow-200/50 dark:border-yellow-900/30">
            <svg className="w-4 h-4 text-yellow-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
            </svg>
            <span>qTajwid — Belajar Membaca</span>
          </div>

          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white leading-tight mb-6">
            Kuasai Bacaan Al-Qur'an <br />
            <span className="text-transparent bg-clip-text bg-linear-to-r from-yellow-500 to-yellow-600">
              Secara Praktis & Mandiri
            </span>
          </h1>

          <p className="text-base text-gray-600 dark:text-gray-400 mb-2 max-w-2xl mx-auto leading-relaxed">
            Metode interaktif Tilawati yang terbagi menjadi 6 level belajar. Latih kemampuan pelafalan Anda secara menyenangkan melalui berbagai game interaktif.
          </p>
        </div>
      </div>

      {/* Main Content Area */}
      <main className="grow container mx-auto px-6 py-12">
        {!selectedLevel ? (
          /* LEVEL CARD DASHBOARD */
          <div>
            <div className="text-center mb-10">
              <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-2">Pilih Level Belajar</h2>
              <p className="text-sm text-gray-500 dark:text-gray-400">Mulailah dari level dasar dan tingkatkan kemampuan Anda secara bertahap</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-5xl mx-auto">
              {LEVELS_DATA.map((lvl) => (
                <button
                  key={lvl.id}
                  onClick={() => setSelectedLevel(lvl)}
                  className="p-6 rounded-2xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 text-left hover:border-yellow-450 hover:shadow-lg hover:shadow-yellow-500/5 transition duration-350 cursor-pointer flex flex-col group relative overflow-hidden"
                >
                  <div className="absolute top-0 right-0 w-24 h-24 bg-yellow-500/5 rounded-bl-full translate-x-4 -translate-y-4 group-hover:bg-yellow-500/10 transition duration-300" />
                  
                  <div className="flex justify-between items-center w-full mb-4">
                    <span className="text-xs font-bold uppercase tracking-wider text-yellow-600 dark:text-yellow-400 bg-yellow-50 dark:bg-yellow-950/30 px-3 py-1 rounded-lg">
                      Level {lvl.id}
                    </span>
                    <span className="text-[11px] font-semibold text-gray-400 dark:text-gray-500">
                      {lvl.data.length} Huruf
                    </span>
                  </div>

                  <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-2 group-hover:text-yellow-600 dark:group-hover:text-yellow-400 transition-colors">
                    {lvl.desc}
                  </h3>
                  
                  <p className="text-xs text-gray-500 dark:text-gray-400 leading-relaxed mb-4">
                    {lvl.subtitle}
                  </p>

                  <div className="mt-auto pt-4 flex items-center justify-between border-t border-gray-150 dark:border-gray-800 w-full text-xs font-bold text-yellow-600 dark:text-yellow-400">
                    <span>Mulai Latihan</span>
                    <span className="transform group-hover:translate-x-1 transition-transform">→</span>
                  </div>
                </button>
              ))}
            </div>
          </div>
        ) : (
          /* LEVEL DETAIL INTERFACE */
          <div className="max-w-4xl mx-auto">
            {/* Level Detail Top Navigation Header */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-gray-100 dark:border-gray-800 pb-5 mb-8">
              <div className="flex items-center gap-3">
                <button
                  onClick={handleBackToDashboard}
                  className="p-2.5 rounded-xl bg-gray-50 dark:bg-gray-800 hover:bg-yellow-500 dark:hover:bg-yellow-600 hover:text-white text-gray-600 dark:text-gray-400 transition cursor-pointer"
                  title="Kembali ke Dashboard"
                >
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                  </svg>
                </button>
                <div>
                  <span className="text-xs font-bold uppercase tracking-wider text-yellow-600 dark:text-yellow-400">Level {selectedLevel.id}</span>
                  <h2 className="text-xl font-bold text-gray-900 dark:text-white leading-tight">{selectedLevel.title.split(": ")[1]}</h2>
                </div>
              </div>

              {/* Sound Controls */}
              <div className="flex items-center gap-3 self-start">
                <button
                  onClick={() => setAudioEnabled(!audioEnabled)}
                  className={`p-2.5 rounded-xl border border-gray-200 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-gray-800 transition cursor-pointer flex items-center justify-center ${
                    audioEnabled ? "text-yellow-600 dark:text-yellow-400" : "text-gray-400 dark:text-gray-500"
                  }`}
                  title={audioEnabled ? "Matikan Suara" : "Aktifkan Suara"}
                >
                  {audioEnabled ? (
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.536 8.464a5 5 0 010 7.072M18.364 5.636a9 9 0 010 12.728M12 18.75V5.25L7.75 9.5H4.5v5h3.25L12 18.75z" />
                    </svg>
                  ) : (
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2" />
                    </svg>
                  )}
                </button>
              </div>
            </div>

            {/* GAME CONTENTS */}
            <div>
              {!activeGame ? (
                /* GAME SELECTION MENU */
                <div>
                  <div className="text-center mb-6">
                    <h3 className="text-lg font-bold text-gray-800 dark:text-white">Pilih Permainan Latihan</h3>
                    <p className="text-xs text-gray-500 dark:text-gray-400">Mainkan game di bawah untuk mengasah daya ingat dan kefasihan membaca</p>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl mx-auto">
                    {/* Game 1 Card */}
                    <button
                      onClick={() => setActiveGame("tebak")}
                      className="p-5 rounded-2xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 hover:border-yellow-450 hover:shadow-md text-left transition duration-300 flex flex-col items-start cursor-pointer group"
                    >
                      <div className="w-10 h-10 rounded-xl bg-yellow-50 dark:bg-yellow-950/30 text-yellow-600 dark:text-yellow-400 flex items-center justify-center mb-4 group-hover:bg-yellow-500 group-hover:text-white transition">
                        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                      </div>
                      <h4 className="text-sm font-bold text-gray-900 dark:text-white mb-2">Tebak Bacaan</h4>
                      <p className="text-[11px] text-gray-500 dark:text-gray-400 leading-relaxed mb-4">
                        Cari ejaan latin yang tepat berdasarkan aksara Arab yang ditampilkan pada layar.
                      </p>
                      <span className="text-[11px] font-bold text-yellow-600 dark:text-yellow-400 group-hover:translate-x-1 transition-transform">
                        Mulai Main →
                      </span>
                    </button>

                    {/* Game 2 Card */}
                    <button
                      onClick={() => setActiveGame("balon")}
                      className="p-5 rounded-2xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 hover:border-yellow-450 hover:shadow-md text-left transition duration-300 flex flex-col items-start cursor-pointer group"
                    >
                      <div className="w-10 h-10 rounded-xl bg-yellow-50 dark:bg-yellow-950/30 text-yellow-600 dark:text-yellow-400 flex items-center justify-center mb-4 group-hover:bg-yellow-500 group-hover:text-white transition">
                        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19.428 15.428a2 2 0 00-1.022-.547l-2.384-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
                        </svg>
                      </div>
                      <h4 className="text-sm font-bold text-gray-900 dark:text-white mb-2">Letuskan Balon</h4>
                      <p className="text-[11px] text-gray-500 dark:text-gray-400 leading-relaxed mb-4">
                        Dengarkan panduan audio pelafalan, lalu cari dan letuskan balon aksara Arab yang sesuai.
                      </p>
                      <span className="text-[11px] font-bold text-yellow-600 dark:text-yellow-400 group-hover:translate-x-1 transition-transform">
                        Mulai Main →
                      </span>
                    </button>

                    {/* Game 3 Card */}
                    <button
                      onClick={() => setActiveGame("susun")}
                      className="p-5 rounded-2xl border border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 hover:border-yellow-450 hover:shadow-md text-left transition duration-300 flex flex-col items-start cursor-pointer group"
                    >
                      <div className="w-10 h-10 rounded-xl bg-yellow-50 dark:bg-yellow-950/30 text-yellow-600 dark:text-yellow-400 flex items-center justify-center mb-4 group-hover:bg-yellow-500 group-hover:text-white transition">
                        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
                        </svg>
                      </div>
                      <h4 className="text-sm font-bold text-gray-900 dark:text-white mb-2">Susun Bacaan</h4>
                      <p className="text-[11px] text-gray-500 dark:text-gray-400 leading-relaxed mb-4">
                        Rangkai kepingan-kepingan aksara Arab acak menjadi kalimat utuh sesuai ejaan yang diberikan.
                      </p>
                      <span className="text-[11px] font-bold text-yellow-600 dark:text-yellow-400 group-hover:translate-x-1 transition-transform">
                        Mulai Main →
                      </span>
                    </button>
                  </div>
                </div>
              ) : (
                /* RENDER ACTIVE GAME SCREEN */
                <div>
                  <button
                    onClick={handleBackToGameMenu}
                    className="inline-flex items-center text-xs font-bold text-gray-500 hover:text-yellow-600 dark:hover:text-yellow-400 mb-6 transition cursor-pointer"
                  >
                    <svg className="w-4 h-4 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                    </svg>
                    Kembali ke Menu Game
                  </button>

                  {activeGame === "tebak" && (
                    <TebakBacaanGame
                      dataset={selectedLevel.data}
                      speak={speakReading}
                      playCorrect={playCorrectSound}
                      playWrong={playWrongSound}
                    />
                  )}

                  {activeGame === "balon" && (
                    <LetuskanBalonGame
                      dataset={selectedLevel.data}
                      speak={speakReading}
                      playPop={playPopSound}
                      playCorrect={playCorrectSound}
                      playWrong={playWrongSound}
                    />
                  )}

                  {activeGame === "susun" && (
                    <SusunBacaanGame
                      dataset={selectedLevel.data}
                      speak={speakReading}
                      playPop={playPopSound}
                      playCorrect={playCorrectSound}
                      playWrong={playWrongSound}
                    />
                  )}
                </div>
              )}
            </div>
          </div>
        )}
      </main>

      <Footer />
    </div>
  );
};

// ─── SUB-GAME 1: TEBAK BACAAN ────────────────────────────────────────
const TebakBacaanGame = ({ dataset, speak, playCorrect, playWrong }) => {
  const [score, setScore] = useState(0);
  const [currentQuestion, setCurrentQuestion] = useState(null);
  const [options, setOptions] = useState([]);
  const [selectedOpt, setSelectedOpt] = useState(null);
  const [status, setStatus] = useState(""); // "correct" | "wrong" | ""

  const generateQuestion = useCallback(() => {
    setSelectedOpt(null);
    setStatus("");

    // Select a correct item
    const pool = [...dataset];
    const correctItem = pool[Math.floor(Math.random() * pool.length)];

    // Select three wrong distractors
    const rest = pool.filter((x) => x.l !== correctItem.l);
    const distractors = shuffle(rest).slice(0, 3);

    // Merge & Shuffle Options
    const allOpts = shuffle([correctItem, ...distractors]);

    setCurrentQuestion(correctItem);
    setOptions(allOpts);
  }, [dataset]);

  useEffect(() => {
    generateQuestion();
  }, [generateQuestion]);

  const handleChoice = (opt) => {
    if (selectedOpt) return; // Prevent double choosing
    setSelectedOpt(opt);

    if (opt.l === currentQuestion.l) {
      setStatus("correct");
      playCorrect();
      speak(opt.l);
      setScore((s) => s + 10);
      setTimeout(() => {
        generateQuestion();
      }, 1300);
    } else {
      setStatus("wrong");
      playWrong();
      // Reset status and choice shortly after to shake and allow retry
      setTimeout(() => {
        setSelectedOpt(null);
        setStatus("");
      }, 600);
    }
  };

  if (!currentQuestion) return null;

  return (
    <div className="bg-white dark:bg-gray-900 p-6 sm:p-8 rounded-2xl border border-gray-200 dark:border-gray-800 shadow-xs max-w-xl mx-auto">
      {/* Game Dashboard Header */}
      <div className="flex justify-between items-center mb-6 text-xs font-bold text-gray-500">
        <span>Tebak Ejaan Latin</span>
        <span className="text-yellow-600 dark:text-yellow-400">Skor: {score}</span>
      </div>

      <div className="text-center py-6 mb-8 bg-gray-50 dark:bg-gray-900 rounded-xl relative overflow-hidden">
        <span className="absolute top-2 left-4 text-[10px] text-gray-400 dark:text-gray-500 font-bold uppercase tracking-wider">Lafalkan & Tebak</span>
        <div className="text-7xl font-arabic font-bold text-gray-800 dark:text-white leading-relaxed select-none">
          {currentQuestion.a}
        </div>
      </div>

      <div className="grid grid-cols-2 gap-4">
        {options.map((opt, i) => {
          let btnClass = "border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 hover:border-yellow-400 text-gray-800 dark:text-gray-300";
          let isShake = false;

          if (selectedOpt?.l === opt.l) {
            if (status === "correct") {
              btnClass = "border-emerald-500 bg-emerald-50 dark:bg-emerald-950/20 text-emerald-700 dark:text-emerald-300";
            } else if (status === "wrong") {
              btnClass = "border-red-500 bg-red-50 dark:bg-red-950/20 text-red-700 dark:text-red-300";
              isShake = true;
            }
          } else if (selectedOpt && opt.l === currentQuestion.l && status === "wrong") {
            // Highlight the correct one silently if user guessed wrong
            btnClass = "border-emerald-500/50 bg-emerald-50/30 dark:bg-emerald-950/10 text-emerald-600 dark:text-emerald-400";
          }

          return (
            <button
              key={i}
              onClick={() => handleChoice(opt)}
              disabled={selectedOpt !== null && status === "correct"}
              className={`p-4 rounded-xl border-2 text-base font-semibold transition cursor-pointer text-center select-none ${btnClass} ${
                isShake ? "shake-element" : ""
              }`}
            >
              {opt.l}
            </button>
          );
        })}
      </div>
    </div>
  );
};

// ─── SUB-GAME 2: LETUSKAN BALON ──────────────────────────────────────
const LetuskanBalonGame = ({ dataset, speak, playPop, playCorrect, playWrong }) => {
  const [score, setScore] = useState(0);
  const [targetItem, setTargetItem] = useState(null);
  const [balloons, setBalloons] = useState([]);
  const [wrongBalloonId, setWrongBalloonId] = useState(null);

  const colors = [
    "from-blue-400 to-blue-600 dark:from-blue-500 dark:to-blue-700 border-blue-300 dark:border-blue-800",
    "from-emerald-400 to-emerald-600 dark:from-emerald-500 dark:to-emerald-750 border-emerald-300 dark:border-emerald-800",
    "from-amber-400 to-amber-600 dark:from-amber-500 dark:to-amber-700 border-amber-300 dark:border-amber-800",
    "from-rose-400 to-rose-600 dark:from-rose-500 dark:to-rose-700 border-rose-300 dark:border-rose-800",
    "from-purple-400 to-purple-600 dark:from-purple-500 dark:to-purple-700 border-purple-300 dark:border-purple-800"
  ];

  const generateWave = useCallback(() => {
    setWrongBalloonId(null);

    // Pick 1 correct and 3 distractors
    const pool = shuffle([...dataset]);
    const waveItems = pool.slice(0, 4);
    const correct = waveItems[0];

    // Map to balloon state with random offsets
    const mappedBalloons = waveItems.map((item, index) => {
      // Differentiate positions to prevent overlaying
      const left = 10 + index * 22 + Math.floor(Math.random() * 8);
      const delay = Math.random() * 1.5;
      const duration = 5.5 + Math.random() * 2;
      const color = colors[index % colors.length];

      return {
        id: index,
        item,
        left,
        delay,
        duration,
        color,
        popped: false
      };
    });

    setTargetItem(correct);
    setBalloons(shuffle(mappedBalloons));

    // Auto-cue vocal targets
    setTimeout(() => {
      speak(correct.l);
    }, 250);
  }, [dataset, speak]);

  useEffect(() => {
    generateWave();
  }, [generateWave]);

  const handleBalloonClick = (balloon) => {
    if (balloon.popped) return;

    if (balloon.item.l === targetItem.l) {
      // Pop Animation & Score Up
      playPop();
      setTimeout(() => {
        playCorrect();
      }, 100);

      setBalloons((prev) =>
        prev.map((b) => (b.id === balloon.id ? { ...b, popped: true } : b))
      );
      setScore((s) => s + 10);

      setTimeout(() => {
        generateWave();
      }, 1100);
    } else {
      playWrong();
      setWrongBalloonId(balloon.id);
      setTimeout(() => {
        setWrongBalloonId(null);
      }, 400);
    }
  };

  if (!targetItem) return null;

  return (
    <div className="bg-white dark:bg-gray-900 p-6 rounded-2xl border border-gray-200 dark:border-gray-800 shadow-xs max-w-xl mx-auto">
      {/* Game Dashboard Header */}
      <div className="flex justify-between items-center mb-4 text-xs font-bold text-gray-500">
        <span>Letuskan Aksara Yang Benar</span>
        <span className="text-yellow-600 dark:text-yellow-400">Skor: {score}</span>
      </div>

      <div className="flex justify-between items-center bg-gray-50 dark:bg-gray-900 px-4 py-3 rounded-xl mb-4 border border-gray-200 dark:border-gray-800">
        <p className="text-xs font-semibold text-gray-600 dark:text-gray-400">
          Cari & letuskan balon: <span className="font-bold text-yellow-600 dark:text-yellow-400 text-sm ml-1 uppercase">{targetItem.l}</span>
        </p>

        {/* Replay target vocal button */}
        <button
          onClick={() => speak(targetItem.l)}
          className="p-1.5 rounded-lg bg-white dark:bg-gray-900 hover:bg-yellow-50 dark:hover:bg-yellow-950/20 text-yellow-600 hover:scale-105 transition cursor-pointer"
          title="Ulangi Suara"
        >
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M15.536 8.464a5 5 0 010 7.072M18.364 5.636a9 9 0 010 12.728M12 18.75V5.25L7.75 9.5H4.5v5h3.25L12 18.75z" />
          </svg>
        </button>
      </div>

      {/* Floating Zone Container */}
      <div className="relative w-full h-[400px] bg-slate-50/50 dark:bg-zinc-950 border border-dashed border-gray-200 dark:border-gray-800 rounded-2xl overflow-hidden">
        {balloons.map((b) => {
          if (b.popped) {
            // Popped rendering: scale down & fade animation
            return (
              <div
                key={b.id}
                style={{ left: `${b.left}%` }}
                className="absolute bottom-1/3 transform -translate-x-1/2 flex items-center justify-center w-16 h-16 rounded-full border bg-emerald-500 text-white font-bold text-lg scale-0 opacity-0 transition-all duration-300 select-none"
              >
                Pop!
              </div>
            );
          }

          const balloonStyle = {
            left: `${b.left}%`,
            animationPlayState: wrongBalloonId === b.id ? "paused" : "running"
          };

          return (
            <button
              key={b.id}
              onClick={() => handleBalloonClick(b)}
              style={balloonStyle}
              className={`absolute w-16 h-16 rounded-full shadow-md hover:scale-105 active:scale-95 transition-transform duration-100 flex items-center justify-center font-arabic text-2xl text-white font-bold select-none cursor-pointer bg-gradient-to-br border border-white/20 float-balloon ${
                b.color
              } ${wrongBalloonId === b.id ? "shake-element !bg-red-500 !border-red-600" : ""}`}
            >
              {b.item.a}
            </button>
          );
        })}
      </div>
    </div>
  );
};

// ─── SUB-GAME 3: SUSUN BACAAN ────────────────────────────────────────
const SusunBacaanGame = ({ dataset, speak, playPop, playCorrect, playWrong }) => {
  const [score, setScore] = useState(0);
  const [targetSequence, setTargetSequence] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [assembledPieces, setAssembledPieces] = useState([]);
  const [scrambledPool, setScrambledPool] = useState([]);
  const [wrongPieceId, setWrongPieceId] = useState(null);
  const [isSuccess, setIsSuccess] = useState(false);

  const initGameRound = useCallback(() => {
    setCurrentIndex(0);
    setAssembledPieces([]);
    setWrongPieceId(null);
    setIsSuccess(false);

    // Pick 3 random distinct items from dataset
    const shuffledItems = shuffle([...dataset]);
    const sequence = shuffledItems.slice(0, 3);
    setTargetSequence(sequence);

    // Prepare pool of pieces: correct 3 + 2 random distractors
    const remaining = shuffledItems.slice(3, 5);
    const pool = shuffle([...sequence, ...remaining]);
    setScrambledPool(pool.map((item, idx) => ({ id: idx, ...item })));

    // Synthesize phonetic cue phrase
    setTimeout(() => {
      const phrase = sequence.map((x) => x.l).join(" ");
      speak(phrase);
    }, 300);
  }, [dataset, speak]);

  useEffect(() => {
    initGameRound();
  }, [initGameRound]);

  const handlePieceClick = (piece) => {
    if (isSuccess) return;

    const expectedTarget = targetSequence[currentIndex];

    if (piece.l === expectedTarget.l) {
      playPop();
      setAssembledPieces((prev) => [...prev, piece]);
      setCurrentIndex((prev) => prev + 1);

      // Verify if sequence is completed
      if (currentIndex + 1 === targetSequence.length) {
        setIsSuccess(true);
        setScore((s) => s + 20);
        setTimeout(() => {
          playCorrect();
        }, 150);

        setTimeout(() => {
          initGameRound();
        }, 1500);
      }
    } else {
      playWrong();
      setWrongPieceId(piece.id);
      setTimeout(() => {
        setWrongPieceId(null);
      }, 500);
    }
  };

  const handleReset = () => {
    setCurrentIndex(0);
    setAssembledPieces([]);
    setIsSuccess(false);
  };

  return (
    <div className="bg-white dark:bg-gray-900 p-6 sm:p-8 rounded-2xl border border-gray-200 dark:border-gray-800 shadow-xs max-w-xl mx-auto">
      {/* Game Dashboard Header */}
      <div className="flex justify-between items-center mb-6 text-xs font-bold text-gray-500">
        <span>Rangkai Huruf/Kalimat</span>
        <span className="text-yellow-600 dark:text-yellow-400">Skor: {score}</span>
      </div>

      <div className="text-center mb-6 bg-gray-50 dark:bg-gray-900 py-3 px-4 rounded-xl border border-gray-200 dark:border-gray-800">
        <p className="text-xs text-gray-500 mb-1">Susun kalimat sesuai lafal ejaan berikut:</p>
        <div className="text-lg font-bold text-yellow-600 dark:text-yellow-400 uppercase tracking-wide">
          {targetSequence.map((x) => x.l).join(" - ")}
        </div>
      </div>

      {/* RTL Drop Zone */}
      <div className="bg-slate-50 dark:bg-zinc-950 border-2 border-dashed border-gray-200 dark:border-gray-800 rounded-xl p-4 min-h-[72px] mb-6 flex flex-row-reverse justify-center items-center gap-3.5 flex-wrap transition duration-300">
        {assembledPieces.length === 0 && (
          <span className="text-xs text-gray-400 select-none">Klik kepingan huruf di bawah untuk menyusun</span>
        )}
        {assembledPieces.map((piece, idx) => (
          <div
            key={idx}
            className="px-4 py-2 bg-yellow-500 text-white rounded-lg font-arabic text-2xl font-bold select-none animate-pulse"
          >
            {piece.a}
          </div>
        ))}
      </div>

      {/* Shuffled Pieces Pool */}
      <div className="flex justify-center gap-3 flex-wrap p-4 bg-gray-50 dark:bg-gray-900 rounded-xl mb-6 min-h-[72px] items-center">
        {scrambledPool
          .filter((p) => !assembledPieces.some((ap) => ap.l === p.l))
          .map((piece) => (
            <button
              key={piece.id}
              disabled={isSuccess}
              onClick={() => handlePieceClick(piece)}
              className={`px-4 py-2.5 rounded-lg border-2 border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 font-arabic text-2xl font-bold hover:border-yellow-450 hover:scale-105 active:scale-95 transition cursor-pointer select-none ${
                wrongPieceId === piece.id ? "shake-element border-red-500 bg-red-50 dark:bg-red-950/20 text-red-700 dark:text-red-300" : ""
              }`}
            >
              {piece.a}
            </button>
          ))}
      </div>

      {/* Success alert message banner */}
      {isSuccess && (
        <div className="p-3 bg-emerald-50 dark:bg-emerald-950/20 border border-emerald-200 dark:border-emerald-900 rounded-xl text-center text-xs font-bold text-emerald-700 dark:text-emerald-400 mb-6 transition">
          Masha Allah, Benar!
        </div>
      )}

      {/* Reset Controls */}
      <div className="flex justify-center gap-3">
        <button
          onClick={handleReset}
          disabled={isSuccess}
          className="px-5 py-2 border border-gray-200 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-500 dark:text-gray-400 rounded-xl text-xs font-bold transition cursor-pointer disabled:opacity-50"
        >
          Reset Susunan
        </button>
      </div>
    </div>
  );
};

export default QTajwid;
