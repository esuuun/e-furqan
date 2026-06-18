import React, { useState, useCallback, useEffect, useRef } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import {
  hijaiyahSounds,
  wordList,
  madPanjangWords,
  tanwinData,
  sukunData,
  tasydidData,
  qalqalahWords,
  ghunnahData,
  alifLamQuiz,
  waqafQuiz,
  waqafPracticeData,
  muqattaahData,
  muqattaahPractice,
  level3Data,
  JILID_META,
  CARD_META,
  LEVELS
} from "../data/tilawatiData";

// ─── UTILS & HELPERS ───────────────────────────────────────────────
function shuffle(arr) {
  return [...arr].sort(() => Math.random() - 0.5);
}

const normalizeArabic = (text) => {
  if (!text) return "";
  // Remove all harakat/tashkeel
  let normalized = text.replace(/[\u064B-\u0652]/g, "");
  // Normalize Alif forms (أ, إ, آ) to plain Alif (ا)
  normalized = normalized.replace(/[أإآ]/g, "ا");
  return normalized.trim();
};

const QURANCDN_BASE = "https://audio.qurancdn.com/";

// Exact word-by-word Quranic audio — verified standalone with FULL harakat match (no wa/fa prefix)
// Verified via quran.com API text_uthmani exact comparison
const QURAN_WORDS_AUDIO = {
  "أَمِنَ": "wbw/002_283_011.mp3",   // Surah 2:283 — exact match ✓
  "عَلِمَ": "wbw/002_060_015.mp3",   // Surah 2:60 — exact match ✓ (was 002_032, wrong)
  "كَفَرَ": "wbw/002_102_009.mp3",   // Surah 2:102 — exact match ✓
  "عَمِلَ": "wbw/006_054_016.mp3",   // Surah 6:54 — exact match ✓ (was 003_195 = noun عَمَلَ "amala")
  "جَعَلَ": "wbw/002_022_002.mp3",   // Surah 2:22 — exact match ✓
  "رَحِمَ": "wbw/012_053_010.mp3",   // Surah 12:53 — exact match ✓ (was 011_043)
  "كُتِبَ": "wbw/002_178_004.mp3",   // Surah 2:178 — exact match ✓
  "ظَلَمَ": "wbw/002_231_019.mp3",   // Surah 2:231 — exact match ✓
  "نَزَلَ": "wbw/026_193_001.mp3",   // Surah 26:193 — exact match ✓ (was 002_176)
  "كَذَبَ": "wbw/039_032_004.mp3",   // Surah 39:32 — exact match ✓ (was 003_184)
  "ذُكِرَ": "wbw/006_118_003.mp3",   // Surah 6:118 — exact match ✓
  // هُدِيَ and عَبَدَ don't appear standalone in Quran — best available approximation:
  "هُدِيَ": "wbw/002_002_006.mp3",   // closest: هُدًى Surah 2:2
  "عَبَدَ": "wbw/019_030_003.mp3",   // closest: Surah 19:30
};

const playQuranCdnAudio = (path) => {
  return new Promise((resolve, reject) => {
    const audio = new Audio(`${QURANCDN_BASE}${path}`);
    audio.referrerPolicy = "no-referrer";
    audio.play().then(resolve).catch(reject);
  });
};

const speakArabic = (text) => {
  if (!text) return;
  const cleanText = text.trim();
  
  // Fallback: use browser SpeechSynthesis with Arabic locale
  if ('speechSynthesis' in window) {
    try {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(cleanText);
      utterance.lang = 'ar-SA';
      utterance.rate = 0.65;
      
      const voices = window.speechSynthesis.getVoices();
      let arabicVoice = voices.find(v => v.lang === 'ar-SA' || v.lang === 'ar_SA');
      if (!arabicVoice) {
        arabicVoice = voices.find(v => v.lang.startsWith('ar') || v.lang.toLowerCase().includes('arabic'));
      }
      if (arabicVoice) utterance.voice = arabicVoice;
      
      window.speechSynthesis.speak(utterance);
    } catch (e) {
      console.error("Browser speechSynthesis failed:", e);
    }
  }
};

// Normalize Arabic for fuzzy audio key lookup: strip harakat but keep base letters + alif normalization
const stripHarakat = (text) => text
  .replace(/[\u064B-\u0652\u0670]/g, '') // remove all harakat/diacritics/superscript alif
  .replace(/[\u0623\u0625\u0622\u0671]/g, '\u0627') // أ إ آ ٱ → ا
  .replace(/\u0649/g, '\u064A'); // ى → ي

// Find Quran CDN audio path for a word (exact match first, then stripped match)
const getQuranAudioPath = (text) => {
  if (!text) return null;
  const clean = text.trim();
  // 1. Exact match
  if (QURAN_WORDS_AUDIO[clean]) return QURAN_WORDS_AUDIO[clean];
  // 2. Harakat-stripped fallback (handles encoding variations)
  const stripped = stripHarakat(clean);
  for (const [key, val] of Object.entries(QURAN_WORDS_AUDIO)) {
    if (stripHarakat(key) === stripped) return val;
  }
  return null;
};

const playSound = (text) => {
  if (!text) return;
  const cleanText = text.trim();
  
  // 0. Play high-quality native Qari recitation from audio.qurancdn.com if mapped
  const quranPath = getQuranAudioPath(cleanText);
  if (quranPath) {
    playQuranCdnAudio(quranPath).catch((err) => {
      console.warn("QuranCDN audio failed, falling back to local MP3 / TTS:", err);
      playLocalOrTts(cleanText);
    });
    return;
  }
  
  playLocalOrTts(cleanText);
};

const normalizeArabicText = (text) => {
  if (!text) return "";
  let norm = text.trim().normalize("NFC");
  
  // 1. Remove leading Alif Fathah (اَ) if string length is > 2 characters
  if (norm.length > 2 && norm.startsWith("\u0627\u064E")) {
    norm = norm.substring(2);
  }
  
  // 2. Remove trailing Alif (ا) only if it is preceded by Fathatayn (ً)
  if (norm.endsWith("\u0627") && norm.charAt(norm.length - 2) === "\u064B") {
    norm = norm.substring(0, norm.length - 1);
  }
  return norm;
};

const playLocalOrTts = (cleanText) => {
  // 1. Search for exact match first
  let matchedItem = hijaiyahSounds.find(h => h.text === cleanText);
  if (!matchedItem) {
    const lists = [...sukunData, ...tanwinData, ...tasydidData];
    matchedItem = lists.find(item => item.text === cleanText);
  }

  // 2. If no exact match, use normalized match
  if (!matchedItem) {
    const normalizedQuery = normalizeArabicText(cleanText);
    
    // Check hijaiyahSounds first with normalized comparison
    matchedItem = hijaiyahSounds.find(h => normalizeArabicText(h.text) === normalizedQuery);
    
    // Check sukun/tanwin/tasydid with normalized comparison
    if (!matchedItem) {
      const lists = [...sukunData, ...tanwinData, ...tasydidData];
      matchedItem = lists.find(item => normalizeArabicText(item.text) === normalizedQuery);
    }
  }

  // 3. Play audio if matched and has a sound file, else fallback to browser TTS
  if (matchedItem?.sound) {
    const audio = new Audio(`/qtajwid/audio/${matchedItem.sound}.mp3`);
    audio.play().catch((err) => {
      console.warn(`Local audio play failed for ${matchedItem.sound}.mp3, falling back to TTS:`, err);
      speakArabic(cleanText);
    });
  } else {
    speakArabic(cleanText);
  }
};

// Play audio directly for a wordList item using its stored quranAudio URL
const playWordAudio = (item) => {
  if (!item) return;
  const wordText = item.word || item.text || '';
  if (item.quranAudio) {
    playQuranCdnAudio(item.quranAudio)
      .catch(() => speakArabic(wordText));
    return;
  }
  // Fallback for words without quranAudio
  playLocalOrTts(wordText);
};

const getGameIcon = (id, className = "w-4 h-4") => {
  switch (id) {
    case 'tilawati':
      return (
        <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
        </svg>
      );
    case 'course':
      return (
        <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
        </svg>
      );
    case 'susunKata':
      return (
        <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
        </svg>
      );
    case 'tebakSuara':
      return (
        <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.536 8.464a5 5 0 010 7.072M18.364 5.636a9 9 0 010 12.728M12 18.75V5.25L7.75 9.5H4.5v5h3.25L12 18.75z" />
        </svg>
      );
    case 'cekUcapan':
      return (
        <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" />
        </svg>
      );
    case 'tajwidRules':
      return (
        <svg className={className} fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
        </svg>
      );
    default:
      return null;
  }
};

// ─── COMPONENT: JILID & LEVEL COURSE ──────────────────────────────
function JilidCourse() {
  const [currentJilid, setCurrentJilid] = useState(null); // null means Jilid grid
  const [currentLevel, setCurrentLevel] = useState(null); // null or level ID (e.g. '1A')
  const [gameMode, setGameMode] = useState("study"); // "study" | "quiz"

  // Quiz Play States
  const [questions, setQuestions] = useState([]);
  const [qIndex, setQIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [lives, setLives] = useState(3);
  const [chosenAnswer, setChosenAnswer] = useState(null);
  const [isAnswered, setIsAnswered] = useState(false);
  const [quizFinished, setQuizFinished] = useState(false);

  // Load progress
  const [progress, setProgress] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem("qtajwid_progress") || "{}");
    } catch {
      return {};
    }
  });

  const saveLevelProgress = (lvlId) => {
    const nextProgress = { ...progress, [lvlId]: true };
    setProgress(nextProgress);
    localStorage.setItem("qtajwid_progress", JSON.stringify(nextProgress));
  };

  const startLevelQuiz = (lvlId) => {
    const lvl = LEVELS[lvlId];
    if (!lvl) return;
    const shuffledQs = shuffle(lvl.questions).slice(0, 10);
    setQuestions(shuffledQs);
    setQIndex(0);
    setScore(0);
    setLives(3);
    setChosenAnswer(null);
    setIsAnswered(false);
    setQuizFinished(false);
    setGameMode("quiz");

    // Auto play first question sound — use playLocalOrTts directly for letters
    setTimeout(() => {
      playLocalOrTts(shuffledQs[0].arabic);
    }, 300);
  };

  const handleChoose = (opt, q) => {
    if (isAnswered) return;
    setChosenAnswer(opt);
    setIsAnswered(true);

    if (opt === q.answer) {
      setScore(s => s + 1);
    } else {
      setLives(l => l - 1);
    }
  };

  const handleNextQuestion = () => {
    if (lives - 1 <= 0 && chosenAnswer !== questions[qIndex].answer) {
      setQuizFinished(true);
      return;
    }

    if (qIndex + 1 >= questions.length) {
      setQuizFinished(true);
      if (score >= questions.length * 0.7 || (score + 1 >= questions.length * 0.7 && chosenAnswer === questions[qIndex].answer)) {
        saveLevelProgress(currentLevel);
      }
    } else {
      const nextIdx = qIndex + 1;
      setQIndex(nextIdx);
      setChosenAnswer(null);
      setIsAnswered(false);
      // Play next letter sound immediately (no timeout to stay in gesture context)
      playLocalOrTts(questions[nextIdx].arabic);
    }
  };

  // Render main Jilid card grid selection
  if (currentJilid === null) {
    return (
      <div>
        <p className="text-center text-gray-500 dark:text-gray-400 text-sm mb-8">
          Pilih tingkat Jilid metode Tilawati di bawah untuk memulai pembelajaran interaktif.
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {Object.entries(JILID_META).map(([id, meta]) => {
            const completedCount = meta.levels.filter(lvl => progress[lvl]).length;
            const progressPercent = Math.round((completedCount / 3) * 100);

            return (
              <button
                key={id}
                onClick={() => setCurrentJilid(id)}
                className="p-6 rounded-2xl border-2 border-gray-100 dark:border-gray-800 bg-white dark:bg-gray-900 text-left hover:border-yellow-400 hover:shadow-md transition duration-200 cursor-pointer flex flex-col group"
              >
                <div className="flex justify-between items-start w-full mb-4">
                  <span className="text-3xl font-arabic text-yellow-600 dark:text-yellow-400 bg-yellow-50 dark:bg-yellow-950/20 px-3 py-1 rounded-xl">
                    {meta.arabic}
                  </span>
                  <span className="text-xs font-semibold px-2 py-1 rounded-md bg-gray-100 dark:bg-gray-800 text-gray-500">
                    Jilid {id}
                  </span>
                </div>
                <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-1 group-hover:text-yellow-600 dark:group-hover:text-yellow-400 transition">
                  {meta.title}
                </h3>
                <p className="text-xs text-gray-400 dark:text-gray-500 mb-5 flex-1">
                  {meta.desc}
                </p>
                <div className="w-full">
                  <div className="flex justify-between text-xs text-gray-500 mb-1.5">
                    <span>Progres Belajar</span>
                    <span className="font-semibold">{completedCount}/3 Level</span>
                  </div>
                  <div className="w-full bg-gray-100 dark:bg-gray-800 h-2 rounded-full overflow-hidden">
                    <div
                      className="bg-yellow-500 h-full rounded-full transition-all duration-500"
                      style={{ width: `${progressPercent}%` }}
                    />
                  </div>
                </div>
              </button>
            );
          })}
        </div>
      </div>
    );
  }

  // Render specific levels inside chosen Jilid
  if (currentLevel === null) {
    const meta = JILID_META[currentJilid];
    return (
      <div>
        <div className="flex items-center gap-3 mb-6">
          <button
            onClick={() => setCurrentJilid(null)}
            className="p-2 rounded-lg bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-400 hover:bg-yellow-500 hover:text-white transition cursor-pointer"
          >
            ← Kembali
          </button>
          <div>
            <span className="text-xs font-semibold uppercase tracking-wider text-yellow-600">Jilid {currentJilid}</span>
            <h2 className="text-xl font-bold text-gray-900 dark:text-white">{meta.title}</h2>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          {meta.levels.map(lvlId => {
            const cm = CARD_META[lvlId];
            const isCompleted = progress[lvlId];
            return (
              <button
                key={lvlId}
                onClick={() => {
                  setCurrentLevel(lvlId);
                  setGameMode("study");
                }}
                className={`p-6 rounded-2xl border-2 hover:shadow-md transition text-left cursor-pointer flex flex-col items-start bg-white dark:bg-gray-900 ${
                  isCompleted ? "border-emerald-200 dark:border-emerald-900" : "border-gray-100 dark:border-gray-800"
                }`}
              >
                <div className="flex justify-between items-center w-full mb-3">
                  <span className="text-xs font-bold px-2 py-0.5 rounded bg-yellow-100 dark:bg-yellow-950/40 text-yellow-800 dark:text-yellow-300">
                    {lvlId}
                  </span>
                  {isCompleted && (
                    <span className="text-xs font-bold text-emerald-600 dark:text-emerald-400 flex items-center gap-1">
                      ✓ Selesai
                    </span>
                  )}
                </div>
                <span className="text-4xl font-arabic text-gray-800 dark:text-white mb-2 self-center py-2">
                  {cm.arabic}
                </span>
                <span className="text-base font-bold text-gray-900 dark:text-white w-full text-center">
                  {cm.name}
                </span>
                <span className="text-xs text-gray-500 dark:text-gray-400 w-full text-center mt-1">
                  {cm.sub}
                </span>
              </button>
            );
          })}
        </div>
      </div>
    );
  }

  // Render specific selected Level's Play Panel (study / quiz mode)
  const cm = CARD_META[currentLevel];
  const lvlData = LEVELS[currentLevel];

  return (
    <div>
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-gray-100 dark:border-gray-800 pb-4 mb-6">
        <div className="flex items-center gap-3">
          <button
            onClick={() => {
              setCurrentLevel(null);
              setGameMode("study");
            }}
            className="p-2 rounded-lg bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-400 hover:bg-yellow-500 hover:text-white transition cursor-pointer"
          >
            ← Kembali
          </button>
          <div>
            <span className="text-xs text-gray-400">Level {currentLevel} • {cm.sub}</span>
            <h2 className="text-xl font-bold text-gray-900 dark:text-white">{cm.name}</h2>
          </div>
        </div>

        {/* Study / Quiz selector toggles */}
        <div className="flex bg-gray-100 dark:bg-gray-800 p-1 rounded-xl self-start">
          <button
            onClick={() => setGameMode("study")}
            className={`px-4 py-1.5 rounded-lg text-sm font-semibold transition cursor-pointer ${
              gameMode === "study" ? "bg-white dark:bg-gray-700 text-gray-900 dark:text-white shadow-xs" : "text-gray-500"
            }`}
          >
            Mode Belajar
          </button>
          <button
            onClick={() => startLevelQuiz(currentLevel)}
            className={`px-4 py-1.5 rounded-lg text-sm font-semibold transition cursor-pointer ${
              gameMode === "quiz" ? "bg-white dark:bg-gray-700 text-gray-900 dark:text-white shadow-xs" : "text-gray-500"
            }`}
          >
            Mode Kuis
          </button>
        </div>
      </div>

      {/* ── MODE: STUDY (CLICK & HEAR) ── */}
      {gameMode === "study" && (
        <div className="text-center">
          <p className="text-sm text-gray-500 mb-6 font-sans">
            Klik pada kartu huruf/kata di bawah untuk mendengarkan lafal pengucapan yang benar.
          </p>
          <div className="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-5 gap-4">
            {lvlData.questions.map((item, idx) => (
              <button
                key={idx}
                onClick={() => playLocalOrTts(item.arabic)}
                className="p-6 rounded-2xl bg-gray-50 dark:bg-gray-900 hover:bg-yellow-50 dark:hover:bg-yellow-950/20 border border-gray-100 dark:border-gray-800 hover:border-yellow-400 dark:hover:border-yellow-600 transition flex flex-col items-center justify-center gap-3 cursor-pointer group active:scale-95"
              >
                <span className="text-4xl font-arabic font-bold text-gray-800 dark:text-white group-hover:text-yellow-600 dark:group-hover:text-yellow-400 transition">
                  {item.arabic}
                </span>
                <span className="text-xs font-mono text-gray-400 dark:text-gray-500 uppercase">
                  {item.latin}
                </span>
                <span className="p-1 rounded bg-white dark:bg-gray-850 border border-gray-150 dark:border-gray-700 group-hover:bg-yellow-500 group-hover:text-white transition">
                  <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.536 8.464a5 5 0 010 7.072M18.364 5.636a9 9 0 010 12.728M12 18.75V5.25L7.75 9.5H4.5v5h3.25L12 18.75z" />
                  </svg>
                </span>
              </button>
            ))}
          </div>
        </div>
      )}

      {/* ── MODE: QUIZ ── */}
      {gameMode === "quiz" && (
        <div>
          {quizFinished ? (
            <div className="text-center py-8">
              <div className="text-6xl font-bold mb-3 text-yellow-600 dark:text-yellow-400">
                {Math.round((score / questions.length) * 100)}%
              </div>
              <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-2">
                {score >= questions.length * 0.7 ? "Masha Allah, Hebat!" : "Tetap Semangat!"}
              </h3>
              <p className="text-sm text-gray-500 mb-6">
                Skor Anda: {score} dari {questions.length} benar
              </p>
              <div className="flex gap-3 justify-center">
                <button
                  onClick={() => startLevelQuiz(currentLevel)}
                  className="px-6 py-2.5 rounded-full font-bold text-white bg-yellow-500 hover:bg-yellow-450 transition cursor-pointer"
                >
                  Ulangi Kuis
                </button>
                <button
                  onClick={() => {
                    setCurrentLevel(null);
                    setGameMode("study");
                  }}
                  className="px-6 py-2.5 rounded-full font-semibold border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-800 transition cursor-pointer"
                >
                  Pilih Level Lain
                </button>
              </div>
            </div>
          ) : (
            <div>
              {/* Score bar & Hearts */}
              <div className="flex justify-between items-center text-sm text-gray-500 mb-4">
                <span>Pertanyaan {qIndex + 1}/{questions.length}</span>
                <div className="flex items-center gap-1.5">
                  <span className="flex gap-1">
                    {Array.from({ length: 3 }).map((_, i) => (
                      <span key={i}>
                        <svg className={`w-5 h-5 ${i < lives ? "text-red-500 fill-current" : "text-gray-300 dark:text-gray-700 fill-none"}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                        </svg>
                      </span>
                    ))}
                  </span>
                  <span className="font-semibold text-emerald-600 ml-2">{score} Benar</span>
                </div>
              </div>
              <div className="w-full bg-gray-100 dark:bg-gray-800 h-1.5 rounded-full mb-6 overflow-hidden">
                <div
                  className="bg-yellow-500 h-full rounded-full transition-all duration-300"
                  style={{ width: `${(qIndex / questions.length) * 100}%` }}
                />
              </div>

              {/* Quiz Main Card */}
              <div className="text-center mb-8">
                <p className="text-xs uppercase tracking-wider text-gray-400 font-semibold mb-2">Dengarkan audio dan pilih aksara yang tepat</p>
                <div className="flex justify-center items-center gap-3">
                  <button
                    onClick={() => playLocalOrTts(questions[qIndex].arabic)}
                    className="p-5 bg-yellow-500 hover:bg-yellow-450 text-white rounded-full transition shadow-md active:scale-95 cursor-pointer flex items-center justify-center animate-pulse"
                    title="Putar Ulang Suara"
                  >
                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.536 8.464a5 5 0 010 7.072M18.364 5.636a9 9 0 010 12.728M12 18.75V5.25L7.75 9.5H4.5v5h3.25L12 18.75z" />
                    </svg>
                  </button>
                </div>
              </div>

              {/* Choices Option Grid */}
              <div className="grid grid-cols-2 md:grid-cols-3 gap-3.5 mb-6">
                {questions[qIndex].options.map(opt => {
                  let cls = "border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 text-gray-700 dark:text-gray-300 hover:border-yellow-400 cursor-pointer";
                  if (isAnswered) {
                    if (opt === questions[qIndex].answer) {
                      cls = "border-emerald-400 bg-emerald-50 dark:bg-emerald-950/20 text-emerald-700 dark:text-emerald-300";
                    } else if (opt === chosenAnswer) {
                      cls = "border-red-400 bg-red-50 dark:bg-red-950/20 text-red-700 dark:text-red-300";
                    } else {
                      cls = "border-gray-100 dark:border-gray-850 bg-gray-50/50 dark:bg-gray-900/50 text-gray-400 dark:text-gray-600";
                    }
                  }

                  return (
                    <button
                      key={opt}
                      onClick={() => handleChoose(opt, questions[qIndex])}
                      disabled={isAnswered}
                      className={`p-5 rounded-2xl border-2 text-2xl font-arabic transition-all flex items-center justify-center font-bold ${cls}`}
                    >
                      {opt}
                    </button>
                  );
                })}
              </div>

              {isAnswered && (
                <button
                  onClick={handleNextQuestion}
                  className="w-full py-3 bg-yellow-500 hover:bg-yellow-400 text-white font-bold rounded-xl transition cursor-pointer text-sm shadow-md"
                >
                  {qIndex + 1 >= questions.length ? "Selesai" : "Soal Berikutnya →"}
                </button>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

// ─── COMPONENT: SUSUN KATA GAME ──────────────────────────────────
function SusunKataGame() {
  const [wordIndex, setWordIndex] = useState(0);
  const [shuffledPieces, setShuffledPieces] = useState([]);
  const [assembledPieces, setAssembledPieces] = useState([]);
  const [feedback, setFeedback] = useState(null); // null or { type: 'correct'|'wrong', text: string }
  const [isDone, setIsDone] = useState(false);

  const currentWord = wordList[wordIndex];

  const initWord = useCallback((idx) => {
    const word = wordList[idx];
    setAssembledPieces([]);
    setFeedback(null);
    setIsDone(false);
    const shuffled = [...word.pieces].sort(() => Math.random() - 0.5);
    setShuffledPieces(shuffled);
  }, []);

  useEffect(() => {
    initWord(wordIndex);
  }, [wordIndex, initWord]);

  const handleAssemble = (piece) => {
    if (isDone) return;
    const newAssembled = [...assembledPieces, piece];
    setAssembledPieces(newAssembled);
    setShuffledPieces(shuffledPieces.filter(p => p.value !== piece.value));

    if (newAssembled.length === currentWord.pieces.length) {
      const isCorrect = newAssembled.every((p, idx) => p.value === currentWord.pieces[idx].value);
      if (isCorrect) {
        setFeedback({ type: 'correct', text: 'Masha Allah, Benar!' });
        setIsDone(true);
        playWordAudio(currentWord); // use direct quranAudio URL
      } else {
        setFeedback({ type: 'wrong', text: 'Belum tepat. Silakan coba susun kembali.' });
      }
    }
  };

  const handleRemove = (piece) => {
    if (isDone) return;
    setShuffledPieces([...shuffledPieces, piece]);
    setAssembledPieces(assembledPieces.filter(p => p.value !== piece.value));
    setFeedback(null);
  };

  const handleReset = () => {
    initWord(wordIndex);
  };

  const handleNext = () => {
    const nextIdx = (wordIndex + 1) % wordList.length;
    setWordIndex(nextIdx);
  };

  return (
    <div className="max-w-2xl mx-auto py-4">
      <div className="flex justify-between items-center text-xs text-gray-400 font-semibold mb-6">
        <span>KOSA KATA ARAB</span>
        <span>KATA {wordIndex + 1} DARI {wordList.length}</span>
      </div>

      <div className="text-center mb-8">
        <h3 className="text-4xl font-arabic font-bold text-yellow-600 mb-2">{currentWord.word}</h3>
        <p className="text-sm text-gray-500 italic dark:text-gray-400">Artinya: {currentWord.meaning}</p>
        <button
          onClick={() => playWordAudio(currentWord)}
          className="mt-3.5 p-2.5 rounded-lg bg-yellow-50 dark:bg-yellow-950/20 text-yellow-600 hover:bg-yellow-500 hover:text-white transition cursor-pointer inline-flex items-center gap-1.5 text-xs font-semibold"
        >
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.536 8.464a5 5 0 010 7.072M18.364 5.636a9 9 0 010 12.728M12 18.75V5.25L7.75 9.5H4.5v5h3.25L12 18.75z" />
          </svg>
          Dengarkan Suara
        </button>
      </div>

      {/* Target Assembly Zones (RTL layout) */}
      <div className="bg-gray-50 dark:bg-gray-900 border-2 border-dashed border-gray-200 dark:border-gray-800 rounded-2xl p-6 min-h-24 mb-6 flex flex-row-reverse justify-center items-center gap-3.5 flex-wrap">
        {currentWord.pieces.map((piece, index) => {
          const placed = assembledPieces[index];
          return (
            <button
              key={index}
              disabled={isDone || !placed}
              onClick={() => placed && handleRemove(placed)}
              className={`w-14 h-14 rounded-xl font-arabic text-3xl font-bold flex items-center justify-center border-2 transition active:scale-95 ${
                placed
                  ? "border-yellow-400 bg-yellow-50/50 dark:bg-yellow-950/20 text-gray-800 dark:text-white cursor-pointer hover:border-red-400"
                  : "border-gray-200 dark:border-gray-800 bg-white/20 text-transparent pointer-events-none"
              }`}
            >
              {placed ? placed.text : ""}
            </button>
          );
        })}
      </div>

      {/* Scrambled Pieces Pool */}
      <div className="flex justify-center gap-3.5 flex-wrap p-5 bg-gray-50 dark:bg-gray-900 rounded-2xl mb-8 min-h-20 items-center">
        {shuffledPieces.map(piece => (
          <button
            key={piece.value}
            disabled={isDone}
            onClick={() => handleAssemble(piece)}
            className="w-14 h-14 rounded-xl font-arabic text-3xl font-bold flex items-center justify-center border-2 border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 text-gray-800 dark:text-white shadow-xs cursor-pointer hover:border-yellow-400 hover:scale-105 active:scale-95 transition"
          >
            {piece.text}
          </button>
        ))}
      </div>

      {/* Feedback Panel */}
      {feedback && (
        <div className={`p-4 rounded-xl text-center text-sm font-semibold mb-6 border ${
          feedback.type === 'correct' ? 'bg-emerald-50 dark:bg-emerald-950/10 border-emerald-200 dark:border-emerald-800 text-emerald-700 dark:text-emerald-400' : 'bg-red-50 dark:bg-red-950/10 border-red-200 dark:border-red-800 text-red-700 dark:text-red-400'
        }`}>
          {feedback.text}
        </div>
      )}

      {/* Control Buttons */}
      <div className="flex gap-3.5 justify-center">
        <button
          onClick={handleReset}
          className="px-6 py-2 bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700 rounded-xl text-sm font-semibold transition cursor-pointer"
        >
          Reset
        </button>
        <button
          onClick={handleNext}
          className="px-6 py-2 bg-yellow-500 hover:bg-yellow-400 text-white rounded-xl text-sm font-bold transition cursor-pointer shadow-md"
        >
          Kata Berikutnya
        </button>
      </div>
    </div>
  );
}

// ─── COMPONENT: TEBAK SUARA GAME ─────────────────────────────────
function TebakSuaraGame() {
  const [target, setTarget] = useState(null);
  const [options, setOptions] = useState([]);
  const [chosen, setChosen] = useState(null);
  const [isCorrect, setIsCorrect] = useState(null);
  const [score, setScore] = useState(0);

  const generateQuestion = useCallback(() => {
    setChosen(null);
    setIsCorrect(null);
    const isLetter = Math.random() > 0.5;
    const pool = isLetter ? hijaiyahSounds : wordList;
    const item = pool[Math.floor(Math.random() * pool.length)];
    const itemText = isLetter ? item.text : item.word;

    const incorrect = pool
      .filter(p => (isLetter ? p.text : p.word) !== itemText)
      .map(p => (isLetter ? p.text : p.word))
      .sort(() => Math.random() - 0.5)
      .slice(0, 3);

    const opts = [itemText, ...incorrect].sort(() => Math.random() - 0.5);
    setTarget(item);
    setOptions(opts);
    
    // Play directly using the correct method for this item type
    if (isLetter) {
      playLocalOrTts(itemText);
    } else {
      playWordAudio(item);
    }
  }, []);

  useEffect(() => {
    generateQuestion();
  }, [generateQuestion]);

  const handleChoose = (opt) => {
    if (chosen) return;
    setChosen(opt);
    const correct = opt === (target.text || target.word);
    setIsCorrect(correct);
    if (correct) {
      setScore(s => s + 1);
    }
  };

  return (
    <div className="max-w-xl mx-auto text-center py-6">
      <div className="flex justify-between items-center text-xs text-gray-400 mb-6 font-semibold">
        <span>TEBAK SUARA</span>
        <span className="text-emerald-600">Skor: {score} Benar</span>
      </div>

      <div className="mb-8 p-6 bg-gray-50 dark:bg-gray-900 rounded-3xl border border-gray-100 dark:border-gray-800">
        <p className="text-sm text-gray-500 mb-4 font-sans">Dengarkan audio dan pilihlah aksara Arab yang sesuai</p>
        <button
          onClick={() => {
            if (!target) return;
            if (target.quranAudio) playWordAudio(target);
            else playLocalOrTts(target.text || target.word);
          }}
          className="p-5 bg-yellow-500 hover:bg-yellow-450 text-white rounded-full transition shadow-md active:scale-95 cursor-pointer animate-pulse"
        >
          <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.536 8.464a5 5 0 010 7.072M18.364 5.636a9 9 0 010 12.728M12 18.75V5.25L7.75 9.5H4.5v5h3.25L12 18.75z" />
          </svg>
        </button>
      </div>

      <div className="grid grid-cols-2 gap-4 mb-8">
        {options.map(opt => {
          let cls = "border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-800 text-gray-800 dark:text-gray-200 hover:border-yellow-400 hover:scale-[1.02] cursor-pointer";
          const correctText = target ? (target.text || target.word) : "";

          if (chosen) {
            if (opt === correctText) {
              cls = "border-emerald-400 bg-emerald-50 dark:bg-emerald-950/20 text-emerald-700 dark:text-emerald-300";
            } else if (opt === chosen) {
              cls = "border-red-400 bg-red-50 dark:bg-red-950/20 text-red-700 dark:text-red-300";
            } else {
              cls = "border-gray-100 dark:border-gray-850 bg-gray-50/50 dark:bg-gray-900/50 text-gray-400 dark:text-gray-600";
            }
          }

          return (
            <button
              key={opt}
              disabled={!!chosen}
              onClick={() => handleChoose(opt)}
              className={`p-6 rounded-2xl border-2 font-arabic text-3xl font-bold flex items-center justify-center transition duration-150 ${cls}`}
            >
              {opt}
            </button>
          );
        })}
      </div>

      {chosen && (
        <button
          onClick={generateQuestion}
          className="w-full py-3 bg-yellow-500 hover:bg-yellow-400 text-white font-bold rounded-xl transition cursor-pointer text-sm shadow-md"
        >
          Soal Berikutnya →
        </button>
      )}
    </div>
  );
}

// ─── COMPONENT: CEK UCAPAN GAME ──────────────────────────────────
function CekUcapanGame() {
  const [target, setTarget] = useState(null);
  const [isListening, setIsListening] = useState(false);
  const [statusMessage, setStatusMessage] = useState("Klik tombol mikrofon untuk mulai berbicara");
  const [transcript, setTranscript] = useState("");
  const [isCorrect, setIsCorrect] = useState(null);
  const [supported, setSupported] = useState(true);

  const recognitionRef = useRef(null);

  useEffect(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      setSupported(false);
      setStatusMessage("Browser Anda tidak mendukung fitur Speech Recognition. Silakan gunakan Google Chrome atau Edge.");
    } else {
      const rec = new SpeechRecognition();
      rec.lang = 'ar-SA';
      rec.interimResults = false;
      rec.maxAlternatives = 1;

      rec.onstart = () => {
        setIsListening(true);
        setStatusMessage("Mendengarkan... Ucapkan aksara di layar");
      };

      rec.onend = () => {
        setIsListening(false);
      };

      rec.onresult = (event) => {
        const result = event.results[0][0].transcript;
        setTranscript(result);
        
        const targetText = target.text || target.word;
        const normalizedTranscript = normalizeArabic(result);
        const normalizedTarget = normalizeArabic(targetText);

        if (normalizedTranscript === normalizedTarget) {
          setIsCorrect(true);
          setStatusMessage("✓ Bagus! Pelafalan Anda benar.");
        } else {
          setIsCorrect(false);
          setStatusMessage(`✗ Pelafalan belum tepat. Terdengar: "${result}". Coba lagi.`);
        }
      };

      rec.onerror = (event) => {
        setIsListening(false);
        if (event.error === 'no-speech') {
          setStatusMessage("Tidak ada suara terdeteksi. Silakan coba lagi.");
        } else if (event.error === 'not-allowed') {
          setStatusMessage("Izin mikrofon ditolak. Harap izinkan mikrofon di pengaturan browser.");
        } else {
          setStatusMessage(`Error: ${event.error}`);
        }
      };

      recognitionRef.current = rec;
    }
  }, [target]);

  const generateTarget = useCallback(() => {
    setTranscript("");
    setIsCorrect(null);
    setStatusMessage("Klik tombol mikrofon untuk mulai berbicara");
    const isLetter = Math.random() > 0.5;
    const pool = isLetter ? hijaiyahSounds : wordList;
    const item = pool[Math.floor(Math.random() * pool.length)];
    setTarget(item);
  }, []);

  useEffect(() => {
    generateTarget();
  }, [generateTarget]);

  const handleStartListening = () => {
    if (!supported || isListening) return;
    try {
      recognitionRef.current.start();
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <div className="max-w-xl mx-auto text-center py-6">
      <div className="flex justify-between items-center text-xs text-gray-400 mb-6 font-semibold">
        <span>CEK UCAPAN (MICROPHONE)</span>
      </div>

      {!supported && (
        <div className="p-4 bg-yellow-50 dark:bg-yellow-950/20 border border-yellow-200 dark:border-yellow-800 text-yellow-800 dark:text-yellow-300 rounded-xl text-sm font-semibold mb-6">
          {statusMessage}
        </div>
      )}

      {target && (
        <div className="mb-6 p-8 bg-gray-50 dark:bg-gray-900 rounded-3xl border border-gray-100 dark:border-gray-800 relative group">
          <span className="text-7xl font-arabic font-bold text-gray-800 dark:text-white block py-4">
            {target.text || target.word}
          </span>
          <p className="text-xs text-gray-400 mt-2">Dengarkan contoh:</p>
          <button
            onClick={() => playSound(target.text || target.word)}
            className="mt-2 p-2 rounded-full bg-white dark:bg-gray-800 hover:bg-yellow-500 hover:text-white transition shadow-sm cursor-pointer inline-flex items-center justify-center"
            title="Dengarkan Contoh"
          >
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.536 8.464a5 5 0 010 7.072M18.364 5.636a9 9 0 010 12.728M12 18.75V5.25L7.75 9.5H4.5v5h3.25L12 18.75z" />
            </svg>
          </button>
        </div>
      )}

      {/* Mic Trigger */}
      <div className="flex justify-center mb-6">
        <button
          onClick={handleStartListening}
          disabled={!supported || isListening}
          className={`p-6 rounded-full shadow-lg transition active:scale-95 cursor-pointer flex items-center justify-center ${
            isListening
              ? "bg-red-500 text-white animate-pulse"
              : "bg-yellow-500 hover:bg-yellow-400 text-white"
          }`}
        >
          <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" />
          </svg>
        </button>
      </div>

      <div className={`p-4 rounded-xl text-center text-sm font-semibold mb-6 border ${
        isCorrect === true
          ? "bg-emerald-50 dark:bg-emerald-950/10 border-emerald-200 dark:border-emerald-800 text-emerald-700 dark:text-emerald-400"
          : isCorrect === false
          ? "bg-red-50 dark:bg-red-950/10 border-red-200 dark:border-red-800 text-red-700 dark:text-red-400"
          : "bg-gray-50 dark:bg-gray-850 border-gray-150 dark:border-gray-800 text-gray-500 dark:text-gray-400"
      }`}>
        {statusMessage}
      </div>

      <div className="flex gap-3 justify-center">
        <button
          onClick={generateTarget}
          className="px-6 py-2.5 bg-yellow-500 hover:bg-yellow-400 text-white rounded-xl text-sm font-bold transition cursor-pointer shadow-md"
        >
          Huruf Berikutnya
        </button>
      </div>
    </div>
  );
}

// ─── COMPONENT: TAJWID RULE MULTIPLE CHOICE ─────────────────────
function TajwidQuiz({ questions, accentBg = "bg-yellow-500" }) {
  const [qs] = useState(() => shuffle(questions).slice(0, 8));
  const [cur, setCur] = useState(0);
  const [chosen, setChosen] = useState(null);
  const [score, setScore] = useState(0);
  const [done, setDone] = useState(false);
  const [history, setHistory] = useState([]);

  const q = qs[cur];

  useEffect(() => {
    if (q) {
      // Small delay to let the component render, but keep within user-gesture window
      const t = setTimeout(() => {
        playSound(q.example || q.word);
      }, 100);
      return () => clearTimeout(t);
    }
  }, [cur]); // only re-run when cur changes, not when q changes (avoids double-play)

  const handleChoose = (opt) => {
    if (chosen) return;
    const correct = opt === q.answer;
    setChosen(opt);
    if (correct) setScore((s) => s + 1);
    setHistory((h) => [...h, { ex: q.example || q.word || q.sign, answer: q.answer, chosen: opt, correct }]);
  };

  const next = () => {
    if (cur + 1 >= qs.length) setDone(true);
    else { setCur((c) => c + 1); setChosen(null); }
  };

  const restart = () => { setCur(0); setChosen(null); setScore(0); setDone(false); setHistory([]); };

  if (done) {
    const pct = Math.round((score / qs.length) * 100);
    return (
      <div className="text-center py-6">
        <div className={`text-6xl font-bold mb-3 ${pct >= 80 ? "text-emerald-600 dark:text-emerald-400" : pct >= 60 ? "text-yellow-600 dark:text-yellow-400" : "text-red-500"}`}>
          {pct}%
        </div>
        <p className="text-gray-900 dark:text-white font-bold text-lg mb-1 font-sans">
          {pct >= 80 ? "Luar Biasa!" : pct >= 60 ? "Bagus!" : "Terus Berlatih!"}
        </p>
        <p className="text-gray-500 dark:text-gray-400 mb-6">{score} dari {qs.length} benar</p>
        <div className="space-y-2 mb-6 text-left max-h-40 overflow-y-auto">
          {history.map((h, i) => (
            <div key={i} className={`flex items-center gap-3 p-3 rounded-xl text-sm border ${h.correct ? "bg-emerald-50 dark:bg-emerald-950/15 border-emerald-200 dark:border-emerald-800" : "bg-red-50 dark:bg-red-950/15 border-red-200 dark:border-red-800"}`}>
              <span>{h.correct ? <span className="text-emerald-500 font-bold">✓</span> : <span className="text-red-500 font-bold">✗</span>}</span>
              <span className="font-arabic text-xl text-gray-800 dark:text-gray-200">{h.ex}</span>
              <span className="text-gray-500 dark:text-gray-400 text-xs">→ {h.answer}</span>
            </div>
          ))}
        </div>
        <button onClick={restart} className={`px-8 py-3 rounded-xl font-semibold text-white transition ${accentBg} hover:opacity-90 cursor-pointer`}>
          Ulangi
        </button>
      </div>
    );
  }

  const allOptions = q.options || shuffle([q.answer, ...(q.incorrectAnswers || [])]).slice(0, 4);

  return (
    <div>
      <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-3">
        <span>Soal {cur + 1}/{qs.length}</span>
        <span className="text-emerald-600 dark:text-emerald-400 font-semibold">{score} benar</span>
      </div>
      <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-1.5 mb-6">
        <div className={`h-1.5 rounded-full transition-all ${accentBg}`} style={{ width: `${(cur / qs.length) * 100}%` }} />
      </div>

      <div className="text-center mb-6">
        <div className="flex justify-center items-center gap-3">
          <div className="text-6xl font-arabic text-gray-900 dark:text-white bg-gray-50 dark:bg-gray-850 rounded-xl py-5 px-8 border border-gray-100 dark:border-gray-800 shadow-xs">
            {q.example || q.word || q.sign}
          </div>
          {(!q.sign || q.sign === '۝') && (
            <button
              onClick={() => playSound(q.example || q.word)}
              className="p-4 bg-yellow-500 hover:bg-yellow-450 text-white rounded-full transition shadow-md flex items-center justify-center active:scale-95 cursor-pointer"
              title="Dengarkan Suara"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
              </svg>
            </button>
          )}
        </div>
        {q.romanization && <p className="text-gray-400 font-mono text-sm mt-2 mb-2">/{q.romanization}/</p>}
        <p className="text-gray-700 dark:text-gray-200 font-semibold mt-3">{q.question || q.name || `Apa arti tanda "${q.sign}"?`}</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-4">
        {allOptions.map((opt) => {
          let cls = "border-gray-200 dark:border-gray-850 bg-white dark:bg-gray-900 text-gray-700 dark:text-gray-300 hover:border-yellow-400 hover:bg-yellow-50 dark:hover:bg-yellow-950/10 cursor-pointer";
          if (chosen) {
            if (opt === q.answer) cls = "border-emerald-400 bg-emerald-50 dark:bg-emerald-950/20 text-emerald-700 dark:text-emerald-300";
            else if (opt === chosen) cls = "border-red-400 bg-red-50 dark:bg-red-950/20 text-red-700 dark:text-red-300";
            else cls = "border-gray-100 dark:border-gray-850 bg-gray-50 dark:bg-gray-950 text-gray-400 dark:text-gray-600";
          }
          return (
            <button
              key={opt}
              onClick={() => handleChoose(opt)}
              disabled={!!chosen}
              className={`p-4 rounded-xl border-2 text-left font-medium text-sm transition-all disabled:cursor-default ${cls}`}
            >
              {opt}
            </button>
          );
        })}
      </div>

      {chosen && q.explanation && (
        <div className="bg-blue-50 dark:bg-blue-950/10 border border-blue-200 dark:border-blue-800 rounded-xl p-4 mb-4 text-sm text-gray-600 dark:text-gray-300">
          <span className="flex items-start gap-2 font-sans">
            <svg className="w-5 h-5 text-blue-500 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>{q.explanation}</span>
          </span>
        </div>
      )}

      {chosen && (
        <button onClick={next} className={`w-full py-3 rounded-xl font-semibold text-white transition ${accentBg} hover:opacity-90 cursor-pointer`}>
          {cur + 1 >= qs.length ? "Lihat Hasil" : "Soal Berikutnya →"}
        </button>
      )}
    </div>
  );
}

// ─── COMPONENT: QALQALAH GAME ────────────────────────────────────
function QalqalahGame() {
  const [qs] = useState(() => shuffle(qalqalahWords));
  const [cur, setCur] = useState(0);
  const [result, setResult] = useState(null);
  const [score, setScore] = useState(0);
  const [done, setDone] = useState(false);

  const q = qs[cur];

  useEffect(() => {
    if (q) {
      const t = setTimeout(() => {
        playSound(q.arabicText);
      }, 300);
      return () => clearTimeout(t);
    }
  }, [cur, q]);

  const handleClick = (part) => {
    if (result) return;
    if (part.isQalqalah) { setResult("correct"); setScore((s) => s + 1); }
    else setResult("wrong");
  };

  const next = () => {
    if (cur + 1 >= qs.length) setDone(true);
    else { setCur((c) => c + 1); setResult(null); }
  };

  const restart = () => { setCur(0); setResult(null); setScore(0); setDone(false); };

  if (done) {
    return (
      <div className="text-center py-6">
        <div className={`text-6xl font-bold mb-3 ${score >= qs.length * 0.8 ? "text-emerald-600" : "text-yellow-600"}`}>
          {Math.round((score / qs.length) * 100)}%
        </div>
        <p className="text-gray-900 dark:text-white font-bold mb-4">{score} dari {qs.length} benar</p>
        <div className="inline-flex gap-2 bg-gray-100 dark:bg-gray-800 rounded-xl p-3 mb-6 text-sm text-gray-600 dark:text-gray-300">
          Huruf Qalqalah: <span className="font-arabic text-lg font-bold text-yellow-600 dark:text-yellow-400">ق ط ب ج د</span>
        </div>
        <div><button onClick={restart} className="px-8 py-3 rounded-xl font-semibold text-white bg-yellow-500 hover:bg-yellow-450 transition cursor-pointer">Ulangi</button></div>
      </div>
    );
  }

  return (
    <div>
      <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-3">
        <span>Soal {cur + 1}/{qs.length}</span>
        <span className="text-emerald-600 dark:text-emerald-400 font-semibold">{score} benar</span>
      </div>
      <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-1.5 mb-6">
        <div className="h-1.5 rounded-full bg-yellow-500 transition-all" style={{ width: `${(cur / qs.length) * 100}%` }} />
      </div>

      <p className="text-center text-gray-600 dark:text-gray-400 text-sm mb-5">
        Klik suku kata yang mengandung huruf <span className="font-bold text-gray-900 dark:text-white">Qalqalah</span> (ق ط ب ج د dalam keadaan sukun)
      </p>

      <div className="flex gap-3 justify-center mb-3 flex-wrap items-center">
        <div className="flex items-center gap-3 bg-gray-50 dark:bg-gray-850 p-4 rounded-3xl border border-gray-100 dark:border-gray-800 shadow-xs">
          {q.parts.map((part, i) => (
            <button
              key={i}
              onClick={() => handleClick(part)}
              disabled={!!result}
              className={`font-arabic text-5xl px-5 py-4 rounded-2xl border-2 transition-all disabled:cursor-default cursor-pointer ${
                result && part.isQalqalah ? "border-emerald-400 bg-emerald-50 dark:bg-emerald-950/20 text-emerald-700 dark:text-emerald-300" :
                "border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 text-gray-900 dark:text-white hover:border-yellow-400 hover:bg-yellow-50 dark:hover:bg-yellow-950/10"
              }`}
            >
              {part.text}
            </button>
          ))}
          <button
            onClick={() => playSound(q.arabicText)}
            className="p-4 bg-yellow-500 hover:bg-yellow-400 text-white rounded-full transition shadow-md flex items-center justify-center active:scale-95 cursor-pointer"
            title="Dengarkan Kata"
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
            </svg>
          </button>
        </div>
      </div>

      <p className="text-center text-gray-500 dark:text-gray-400 text-sm mb-5 font-sans">Arti: <span className="text-gray-700 dark:text-gray-300">{q.meaning}</span></p>

      {result && (
        <>
          <div className={`p-3 rounded-xl text-center text-sm mb-4 border ${result === "correct" ? "bg-emerald-50 dark:bg-emerald-950/10 border-emerald-200 dark:border-emerald-800 text-emerald-700 dark:text-emerald-300" : "bg-red-50 dark:bg-red-950/10 border-red-200 dark:border-red-800 text-red-700 dark:text-red-300"}`}>
            {result === "correct" ? (
              <span className="flex items-center justify-center gap-1.5 font-sans">
                <span className="text-emerald-500 font-bold">✓</span> Benar! Itu adalah huruf Qalqalah.
              </span>
            ) : (
              <span className="flex items-center justify-center gap-1.5 font-sans">
                <span className="text-red-500 font-bold">✗</span> Bukan. Cari huruf dari ق ط ب ج د yang berharakat sukun.
              </span>
            )}
          </div>
          <button onClick={next} className="w-full py-3 rounded-xl font-semibold text-white bg-yellow-500 hover:bg-yellow-400 transition cursor-pointer">
            {cur + 1 >= qs.length ? "Lihat Hasil" : "Soal Berikutnya →"}
          </button>
        </>
      )}
    </div>
  );
}

// ─── COMPONENT: ALIF LAM GAME ────────────────────────────────────
function AlifLamGame() {
  const [qs] = useState(() => shuffle(alifLamQuiz));
  const [cur, setCur] = useState(0);
  const [chosen, setChosen] = useState(null);
  const [score, setScore] = useState(0);
  const [done, setDone] = useState(false);

  const q = qs[cur];

  useEffect(() => {
    if (q) {
      const t = setTimeout(() => {
        playSound(q.example);
      }, 300);
      return () => clearTimeout(t);
    }
  }, [cur, q]);

  const handleChoose = (a) => {
    if (chosen) return;
    setChosen(a);
    if (a === q.answer) setScore((s) => s + 1);
  };
  const next = () => {
    if (cur + 1 >= qs.length) setDone(true);
    else { setCur((c) => c + 1); setChosen(null); }
  };
  const restart = () => { setCur(0); setChosen(null); setScore(0); setDone(false); };

  if (done) {
    return (
      <div className="text-center py-6">
        <div className={`text-6xl font-bold mb-3 ${score >= qs.length * 0.8 ? "text-emerald-600" : "text-yellow-600"}`}>
          {Math.round((score / qs.length) * 100)}%
        </div>
        <p className="text-gray-900 dark:text-white font-bold mb-6">{score} dari {qs.length} benar</p>
        <button onClick={restart} className="px-8 py-3 rounded-xl font-semibold text-white bg-yellow-500 hover:bg-yellow-400 transition cursor-pointer">Ulangi</button>
      </div>
    );
  }

  return (
    <div>
      <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-3">
        <span>Soal {cur + 1}/{qs.length}</span>
        <span className="text-emerald-600 font-semibold">{score} benar</span>
      </div>
      <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-1.5 mb-6">
        <div className="h-1.5 rounded-full bg-yellow-500 transition-all" style={{ width: `${(cur / qs.length) * 100}%` }} />
      </div>
      <div className="text-center mb-6">
        <div className="flex justify-center items-center gap-3">
          <div className="text-7xl font-arabic text-gray-900 dark:text-white bg-gray-50 dark:bg-gray-850 rounded-xl py-5 px-8 border border-gray-100 dark:border-gray-800 shadow-xs">{q.example}</div>
          <button
            onClick={() => playSound(q.example)}
            className="p-4 bg-yellow-500 hover:bg-yellow-400 text-white rounded-full transition shadow-md flex items-center justify-center active:scale-95 cursor-pointer"
            title="Dengarkan Suara"
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" />
            </svg>
          </button>
        </div>
        <p className="text-gray-400 font-mono text-sm mt-2 mb-1">/{q.pronunciation}/</p>
      </div>

      <div className="grid grid-cols-2 gap-4 mb-4">
        {["Syamsiyah", "Qamariyah"].map((opt) => {
          let cls = "border-gray-200 dark:border-gray-850 bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:border-yellow-400 cursor-pointer";
          if (chosen) {
            if (opt === q.answer) cls = "border-emerald-400 bg-emerald-50 dark:bg-emerald-950/20 text-emerald-700 dark:text-emerald-300";
            else if (opt === chosen) cls = "border-red-400 bg-red-50 dark:bg-red-950/20 text-red-700 dark:text-red-300";
            else cls = "border-gray-100 dark:border-gray-850 text-gray-400 dark:text-gray-600";
          }
          return (
            <button key={opt} onClick={() => handleChoose(opt)} disabled={!!chosen}
              className={`p-5 rounded-2xl border-2 font-bold text-lg transition-all disabled:cursor-default ${cls}`}>
              {opt === "Syamsiyah" ? (
                <span className="flex items-center justify-center gap-2">
                  <svg className="w-5 h-5 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364-6.364l-.707.707M6.343 17.657l-.707.707m0-12.728l.707.707m12.728 12.728l.707-.707M12 8a4 4 0 100 8 4 4 0 000-8z" />
                  </svg>
                  {opt}
                </span>
              ) : (
                <span className="flex items-center justify-center gap-2">
                  <svg className="w-5 h-5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
                  </svg>
                  {opt}
                </span>
              )}
            </button>
          );
        })}
      </div>

      {chosen && (
        <div className={`p-4 rounded-xl text-sm mb-4 border ${chosen === q.answer ? "bg-emerald-50 dark:bg-emerald-950/10 border-emerald-200 dark:border-emerald-800 text-emerald-700 dark:text-emerald-300" : "bg-red-50 dark:bg-red-950/10 border-red-200 dark:border-red-800 text-red-700 dark:text-red-300"}`}>
          {chosen === q.answer ? (
            <span className="font-semibold text-emerald-600 dark:text-emerald-400">✓ Benar! </span>
          ) : (
            <span className="font-semibold text-red-600 dark:text-red-400">Jawaban benar: {q.answer}. </span>
          )}
          <span className="text-gray-600 dark:text-gray-300 font-sans ml-1">
            Harakat tasydid setelah Alif Lam menunjukkan hukum Alif Lam Syamsiyah (lebur), sedangkan sukun menunjukkan hukum Qamariyah (jelas).
          </span>
        </div>
      )}

      {chosen && (
        <button onClick={next} className="w-full py-3 rounded-xl font-semibold text-white bg-yellow-500 hover:bg-yellow-400 transition cursor-pointer">
          {cur + 1 >= qs.length ? "Lihat Hasil" : "Soal Berikutnya →"}
        </button>
      )}
    </div>
  );
}

// ─── COMPONENT: ARENA TAJWID (RULE SELECTOR PANEL) ───────────────
function ArenaTajwid() {
  const [activeRule, setActiveRule] = useState(null); // null means rule selector grid

  const RULES = [
    { id: "nunSukun", title: "Nun Sukun & Tanwin", desc: "Izhar • Idgham • Iqlab • Ikhfa", component: <TajwidQuiz questions={level3Data.nunSukunQuiz} /> },
    { id: "qalqalah", title: "Qalqalah", desc: "Ketuk suku kata memantul (ق ط ب ج د)", component: <QalqalahGame /> },
    { id: "alifLam", title: "Alif Lam (ال)", desc: "Bedakan Syamsiyah dan Qamariyah", component: <AlifLamGame /> },
    { id: "waqaf", title: "Tanda Waqaf", desc: "Pahami rambu-rambu berhenti & lanjut", component: <TajwidQuiz questions={waqafQuiz} /> },
    { id: "mad", title: "Hukum Mad", desc: "Aturan memanjangkan ketukan lafal", component: <TajwidQuiz questions={level3Data.madTambahanQuiz} /> }
  ];

  if (activeRule !== null) {
    const rule = RULES.find(r => r.id === activeRule);
    return (
      <div>
        <div className="flex items-center gap-3 border-b border-gray-150 dark:border-gray-800 pb-4 mb-6">
          <button
            onClick={() => setActiveRule(null)}
            className="px-3 py-1.5 rounded-lg bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-yellow-500 hover:text-white transition cursor-pointer text-xs font-semibold"
          >
            ← Kembali
          </button>
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">{rule.title}</h2>
        </div>
        {rule.component}
      </div>
    );
  }

  return (
    <div>
      <p className="text-center text-gray-500 dark:text-gray-400 text-sm mb-8">
        Pilih hukum tajwid lanjutan di bawah untuk menguji pemahaman teori Al-Qur'an Anda.
      </p>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {RULES.map(rule => (
          <button
            key={rule.id}
            onClick={() => setActiveRule(rule.id)}
            className="p-6 rounded-2xl border-2 border-gray-100 dark:border-gray-800 bg-white dark:bg-gray-900 text-left hover:border-yellow-450 hover:shadow-md transition duration-200 cursor-pointer flex flex-col items-start"
          >
            <span className="text-xs font-bold text-yellow-600 bg-yellow-50 dark:bg-yellow-950/20 px-2.5 py-1 rounded-md mb-4 uppercase tracking-wider">
              {rule.id}
            </span>
            <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-2">{rule.title}</h3>
            <p className="text-xs text-gray-500 dark:text-gray-400">{rule.desc}</p>
          </button>
        ))}
      </div>
    </div>
  );
}

// ─── MAIN PAGE COMPONENT ──────────────────────────────────────────
const QTajwid = () => {
  const [activeTab, setActiveTab] = useState("tilawati"); // "tilawati" | "course" | "susunKata" | "tebakSuara" | "cekUcapan" | "tajwidRules"
  const [remountKey, setRemountKey] = useState(0);

  useEffect(() => {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.getVoices();
      if (window.speechSynthesis.onvoiceschanged !== undefined) {
        window.speechSynthesis.onvoiceschanged = () => {
          window.speechSynthesis.getVoices();
        };
      }
    }
  }, []);

  const handleTabSelect = (tabId) => {
    if (activeTab === tabId) {
      setRemountKey(k => k + 1); // trigger restart
    } else {
      setActiveTab(tabId);
    }
  };

  const getTabTitle = () => {
    switch (activeTab) {
      case "tilawati": return "Kitab Tilawati";
      case "course": return "Belajar Jilid (Interactive)";
      case "susunKata": return "Susun Kata";
      case "tebakSuara": return "Tebak Suara";
      case "cekUcapan": return "Cek Ucapan (Mic)";
      case "tajwidRules": return "Kuis Hukum Tajwid";
      default: return "Tajwid Game";
    }
  };

  const renderActiveTabContent = () => {
    switch (activeTab) {
      case "tilawati":
        return (
          <div className="bg-white dark:bg-gray-900 rounded-2xl shadow-xs border border-gray-100 dark:border-gray-800 overflow-hidden">
            <div className="flex items-center justify-between px-6 py-4 border-b border-gray-100 dark:border-gray-800">
              <div className="flex items-center gap-3">
                {getGameIcon("tilawati", "w-6 h-6 text-yellow-600 dark:text-yellow-400")}
                <div>
                  <h2 className="text-xl font-bold text-gray-900 dark:text-white">Kitab Tilawati</h2>
                  <p className="text-sm text-gray-500 dark:text-gray-400">Panduan belajar tajwid metode Tilawati</p>
                </div>
              </div>
              <a
                href="/qtajwid/Tilawati.pdf"
                download
                className="flex items-center gap-2 px-4 py-2 rounded-lg bg-yellow-50 dark:bg-yellow-950/20 text-yellow-700 dark:text-yellow-400 border border-yellow-200 dark:border-yellow-900 text-sm font-semibold hover:bg-yellow-100 dark:hover:bg-yellow-500 dark:hover:text-white transition"
              >
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
                Download PDF
              </a>
            </div>
            <div style={{ height: "75vh" }}>
              <iframe
                src="/qtajwid/Tilawati.pdf"
                title="Kitab Tilawati"
                className="w-full h-full"
                style={{ border: "none" }}
              />
            </div>
          </div>
        );
      case "course":
        return <JilidCourse key={remountKey} />;
      case "susunKata":
        return <SusunKataGame key={remountKey} />;
      case "tebakSuara":
        return <TebakSuaraGame key={remountKey} />;
      case "cekUcapan":
        return <CekUcapanGame key={remountKey} />;
      case "tajwidRules":
        return <ArenaTajwid key={remountKey} />;
      default:
        return null;
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-white dark:bg-gray-900 font-sans text-gray-800 dark:text-gray-250">
      <Navbar />

      {/* Hero Banner Section */}
      <div className="relative bg-linear-to-br from-gray-50 via-white to-gray-100 dark:from-gray-900 dark:via-gray-900 dark:to-gray-900 pt-32 pb-20 overflow-hidden border-b border-gray-100 dark:border-gray-900">
        <div className="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-yellow-100 dark:bg-yellow-900/20 rounded-full blur-3xl opacity-50" />
        <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-80 h-80 bg-yellow-50 dark:bg-yellow-900/10 rounded-full blur-3xl opacity-50" />

        <div className="container mx-auto px-6 relative z-10 text-center">
          <div className="inline-flex items-center px-4 py-1.5 mb-6 bg-yellow-100 dark:bg-yellow-900/20 text-yellow-800 dark:text-yellow-200 rounded-full text-sm font-semibold tracking-wide gap-1.5">
            <svg className="w-4 h-4 text-yellow-500 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L11 3z" />
            </svg>
            <span>qTajwid — Metode Tilawati</span>
          </div>
          <h1 className="text-4xl md:text-6xl font-bold text-gray-900 dark:text-white leading-tight mb-6">
            Belajar Tajwid Al-Qur'an <br />
            <span className="text-transparent bg-clip-text bg-linear-to-r from-yellow-500 to-yellow-600">
              Secara Interaktif
            </span>
          </h1>
          <p className="text-lg text-gray-600 dark:text-gray-400 mb-8 leading-relaxed max-w-2xl mx-auto font-sans">
            Rangkaian game interaktif modern metode Tilawati. Klik, susun kata, tebak suara, hingga uji ucapan pelafalan makhraj Anda langsung di browser.
          </p>
          <div className="flex gap-3.5 justify-center flex-wrap">
            <button
              onClick={() => handleTabSelect("course")}
              className="px-6 py-3 bg-yellow-500 hover:bg-yellow-400 text-white font-bold rounded-full transition shadow-lg shadow-yellow-500/20 flex items-center gap-2 cursor-pointer"
            >
              {getGameIcon("course", "w-5 h-5")}
              <span>Mulai Belajar Jilid</span>
            </button>
            <button
              onClick={() => handleTabSelect("tilawati")}
              className="px-6 py-3 bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 text-gray-700 dark:text-gray-300 font-semibold rounded-full hover:bg-gray-50 dark:hover:bg-gray-800 transition flex items-center gap-2 cursor-pointer"
            >
              {getGameIcon("tilawati", "w-5 h-5 text-gray-400")}
              <span>Buka Kitab PDF</span>
            </button>
          </div>
        </div>
      </div>

      {/* Main Game Page Content */}
      <section className="bg-gray-50/50 dark:bg-gray-900 py-16 flex-1">
        <div className="container mx-auto px-6">
          
          {/* Navigation Tab Menu */}
          <div className="flex flex-wrap gap-2.5 mb-10">
            {[
              { id: "tilawati", title: "Kitab PDF" },
              { id: "course", title: "Interactive Course" },
              { id: "susunKata", title: "Game Susun Kata" },
              { id: "tebakSuara", title: "Game Tebak Suara" },
              { id: "cekUcapan", title: "Cek Ucapan (Mic)" },
              { id: "tajwidRules", title: "Kuis Tajwid" }
            ].map(t => (
              <button
                key={t.id}
                onClick={() => handleTabSelect(t.id)}
                className={`flex items-center gap-2.5 px-5 py-2.5 rounded-full font-semibold text-sm transition-all border cursor-pointer ${
                  activeTab === t.id
                    ? "bg-yellow-500 border-yellow-500 text-white shadow-md shadow-yellow-500/20"
                    : "bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-800 text-gray-600 dark:text-gray-400 hover:border-yellow-400"
                }`}
              >
                {getGameIcon(t.id)}
                <span>{t.title}</span>
              </button>
            ))}
          </div>

          {/* Active Game / Content Panel */}
          <div className="bg-white dark:bg-gray-900 rounded-3xl p-6 md:p-10 border border-gray-150 dark:border-gray-850 shadow-xs min-h-96">
            {renderActiveTabContent()}
          </div>
        </div>
      </section>

      {/* CTA Footer Section */}
      <section className="py-20 bg-yellow-500 relative overflow-hidden">
        <div className="absolute top-0 left-0 w-full h-full overflow-hidden">
          <div className="absolute w-64 h-64 bg-white opacity-10 rounded-full -top-10 -left-10" />
          <div className="absolute w-96 h-96 bg-white opacity-10 rounded-full bottom-0 right-0" />
        </div>
        <div className="container mx-auto px-6 text-center relative z-10">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">
            Ingin Mengasah Bacaan Al-Qur'an Anda?
          </h2>
          <p className="text-white/90 text-lg mb-10 max-w-2xl mx-auto">
            Pelajari tajwid Al-Qur'an secara tartil menggunakan modul-modul game interaktif menyenangkan dan dapatkan nilai sempurna!
          </p>
          <button
            onClick={() => {
              setActiveTab("course");
              document.querySelector("section.py-16")?.scrollIntoView({ behavior: "smooth" });
            }}
            className="bg-white text-yellow-600 px-8 py-4 rounded-full font-bold text-lg hover:bg-gray-100 transition shadow-xl cursor-pointer"
          >
            Mulai Belajar Sekarang
          </button>
        </div>
      </section>

      <Footer />
    </div>
  );
};

export default QTajwid;
