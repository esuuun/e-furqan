import React, { useState, useEffect, useMemo, useRef } from "react";
import { useSearchParams, Link } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import {
  BookOpen,
  Volume2,
  ChevronLeft,
  ChevronRight,
  ChevronDown,
  Layers,
  Copy,
  ExternalLink,
  RotateCw,
  Check,
  MessageCircle
} from "lucide-react";

// ─── COMPLETE 114 SURAH NAMES LIST ───────────────────────────────────────
const SURAH_NAMES = [
  "Al-Fatihah", "Al-Baqarah", "Ali 'Imran", "An-Nisa'", "Al-Ma'idah", "Al-An'am", "Al-A'raf", "Al-Anfal", "At-Taubah", "Yunus",
  "Hud", "Yusuf", "Ar-Ra'd", "Ibrahim", "Al-Hijr", "An-Nahl", "Al-Isra'", "Al-Kahf", "Maryam", "Taha",
  "Al-Anbiya'", "Al-Hajj", "Al-Mu'minun", "An-Nur", "Al-Furqan", "Asy-Syu'ara'", "An-Naml", "Al-Qasas", "Al-'Ankabut", "Ar-Rum",
  "Luqman", "As-Sajdah", "Al-Ahzab", "Saba'", "Fatir", "Yasin", "As-Saffat", "Sad", "Az-Zumar", "Ghafir",
  "Fussilat", "Asy-Syura", "Az-Zukhruf", "Ad-Dukhan", "Al-Jasiyah", "Al-Ahqaf", "Muhammad", "Al-Fath", "Al-Hujurat", "Qaf",
  "Az-Zariyat", "At-Tur", "An-Najm", "Al-Qamar", "Ar-Rahman", "Al-Waqi'ah", "Al-Hadid", "Al-Mujadilah", "Al-Hasyr", "Al-Mumtahanah",
  "As-Saff", "Al-Jumu'ah", "Al-Munafiqun", "At-Tagabun", "At-Talaq", "At-Tahrim", "Al-Mulk", "Al-Qalam", "Al-Haqqah", "Al-Ma'arij",
  "Nuh", "Al-Jinn", "Al-Muzzammil", "Al-Muddassir", "Al-Qiyamah", "Al-Insan", "Al-Mursalat", "An-Naba'", "An-Nazi'at", "'Abasa",
  "At-Takwir", "Al-Infitar", "Al-Mutaffifin", "Al-Insyiqaq", "Al-Buruj", "At-Tariq", "Al-A'la", "Al-Gasyiyah", "Al-Fajr", "Al-Balad",
  "Asy-Syams", "Al-Lail", "Ad-Duha", "Al-Insyirah", "At-Tin", "Al-'Alaq", "Al-Qadr", "Al-Bayyinah", "Az-Zalzalah", "Al-'Adiyat",
  "Al-Qari'ah", "At-Takasur", "Al-'Asr", "Al-Humazah", "Al-Fil", "Quraisy", "Al-Ma'un", "Al-Kausar", "Al-Kafirun", "An-Nasr",
  "Al-Lahab", "Al-Ikhlas", "Al-Falaq", "An-Nas"
];

// ─── TEXT FORMATTER (SIMAQ STYLE) ─────────────────────────────────────────
const renderMixedText = (text, forceColor = null) => {
  if (text == null || text === "") return "";
  const textStr = String(text);
  const arabicRegex = /([\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+(?:[\s]+[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+)*)/g;
  const shouldHighlight = textStr.includes("-");

  let wordCount = 0;
  const colors = ["#fde047", "#f87171"]; // yellow and red

  return textStr.split(arabicRegex).map((part, index) => {
    // If it's an Arabic part
    if (part.match(/[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]/)) {
      const color = forceColor ? forceColor : (shouldHighlight ? colors[wordCount % colors.length] : undefined);
      if (shouldHighlight && !forceColor) wordCount++;
      return (
        <span
          key={index}
          className="font-arabic"
          dir="rtl"
          style={{ ...(color ? { color } : {}), fontSize: shouldHighlight ? "1.1rem" : undefined }}
        >
          {part}
        </span>
      );
    }

    // For non-Arabic parts, highlight hyphens and apply colors to split parts
    if (shouldHighlight) {
      return (
        <span key={index}>
          {part.split(/(-)/).map((subPart, subIndex) => {
            if (subPart === "-") {
              return (
                <span
                  key={subIndex}
                  style={{ color: forceColor ? forceColor : "rgba(255,255,255,0.4)", margin: "0 4px" }}
                >
                  -
                </span>
              );
            } else if (subPart.trim().length > 0) {
              const color = forceColor ? forceColor : colors[wordCount % colors.length];
              if (!forceColor) wordCount++;
              return (
                <span key={subIndex} style={{ color }}>
                  {subPart}
                </span>
              );
            } else {
              return <span key={subIndex}>{subPart}</span>;
            }
          })}
        </span>
      );
    }

    return (
      <span key={index} style={forceColor ? { color: forceColor } : {}}>
        {part}
      </span>
    );
  });
};

// ─── MUTTASHIL TITLE HELPER ───────────────────────────────────────────────
const getMuttashilTitle = (text) => {
  if (!text) return "Huruf Awalan / Akhiran";
  const trimmed = text.trim();
  const startsWithDots = trimmed.startsWith("..");
  const endsWithDots = trimmed.endsWith("..");

  if (startsWithDots && endsWithDots) {
    return "Huruf Awalan & Akhiran (Dhamir & Harf)";
  } else if (startsWithDots) {
    return "Huruf Akhiran (Dhamir Muttashil)";
  } else if (endsWithDots) {
    return "Huruf Awalan (Harf Muttashil)";
  }
  return "Huruf Awalan / Akhiran";
};

// ─── AUDIO CLEANER FOR TTS FALLBACK ──────────────────────────────────────
const cleanArabicForTTS = (text) => {
  if (!text) return "";
  return text
    .replace(/\u0671/g, "\u0627") // Alif Wasla -> Alif
    .replace(/\u0670/g, "\u0627") // Dagger Alif -> Alif
    .replace(/\u06E1/g, "\u0652") // Small sukoon -> standard sukoon
    .replace(/[\u06D6-\u06DC\u06DF-\u06E0\u06E2-\u06ED]/g, "") // Waqf marks
    .trim();
};

let currentWordAudio = null;

const stopAllAudio = () => {
  const mainAudio = document.getElementById("main-ayah-audio");
  if (mainAudio && !mainAudio.paused) {
    mainAudio.pause();
  }
  if (currentWordAudio) {
    currentWordAudio.pause();
    currentWordAudio.currentTime = 0;
  }
  if (window.speechSynthesis) {
    window.speechSynthesis.cancel();
  }
};

const playAudioTTS = (text, lang = "ar") => {
  if (!text) return;
  const ttsText = lang === "ar" ? cleanArabicForTTS(text) : text;
  const urls = [
    `https://translate.google.com/translate_tts?ie=UTF-8&q=${encodeURIComponent(ttsText)}&tl=${lang}&client=tw-ob`,
    `https://translate.googleapis.com/translate_tts?ie=UTF-8&q=${encodeURIComponent(ttsText)}&tl=${lang}&client=gtx`
  ];

  const tryPlay = (index) => {
    if (index >= urls.length) {
      if (window.speechSynthesis) {
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = lang === "ar" ? "ar-SA" : "id-ID";
        utterance.rate = 0.85;
        window.speechSynthesis.speak(utterance);
      }
      return;
    }

    const audio = new Audio(urls[index]);
    currentWordAudio = audio;
    audio.play().catch(() => {
      tryPlay(index + 1);
    });
  };

  tryPlay(0);
};

const playQuranWord = (suratId, ayatId, wordIndex, fallbackText) => {
  stopAllAudio();

  if (!suratId || !ayatId || !wordIndex) {
    playAudioTTS(fallbackText, "ar");
    return;
  }

  const surahStr = String(suratId).padStart(3, "0");
  const ayahStr = String(ayatId).padStart(3, "0");
  const wordStr = String(wordIndex).padStart(3, "0");
  const url = `https://verses.quran.com/wbw/${surahStr}_${ayahStr}_${wordStr}.mp3`;

  const audio = new Audio(url);
  currentWordAudio = audio;
  audio.play().catch((e) => {
    console.warn("Quran CDN failed, falling back to TTS:", e);
    playAudioTTS(fallbackText, "ar");
  });
};

// ─── TRANSLATION CACHE & FETCHER ──────────────────────────────────────────
const translationCache = new Map();

const fetchTranslation = async (text, lang) => {
  if (lang === "id" || !text) return text;
  const clean = String(text).replace(/\s*\[.*?\]\s*/g, " ").trim();
  if (!clean) return "";

  const cacheKey = `${lang}_${clean}`;
  if (translationCache.has(cacheKey)) {
    return translationCache.get(cacheKey);
  }

  try {
    const response = await fetch(
      `https://translate.googleapis.com/translate_a/single?client=gtx&sl=id&tl=${lang}&dt=t&q=${encodeURIComponent(clean)}`
    );
    const data = await response.json();
    const translatedText = data[0].map((item) => item[0]).join("");
    translationCache.set(cacheKey, translatedText);
    return translatedText;
  } catch (error) {
    console.error("Translation error:", error);
    return text;
  }
};

const TranslatedText = ({ text, lang }) => {
  const [translated, setTranslated] = useState(lang === "id" ? text : "...");

  useEffect(() => {
    if (lang === "id") {
      setTranslated(text);
      return;
    }
    let isMounted = true;
    setTranslated("...");
    fetchTranslation(text, lang).then((res) => {
      if (isMounted) setTranslated(res);
    });
    return () => {
      isMounted = false;
    };
  }, [text, lang]);

  return <span>{translated}</span>;
};

// ─── IN-MEMORY SURAH DATA CACHE ──────────────────────────────────────────
const surahCache = new Map();

// ─── MAIN QMUSHAF COMPONENT ───────────────────────────────────────────────
const QMushaf = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const [metadata, setMetadata] = useState(null);

  // Initialize selectedSurah and selectedAyah directly from URL searchParams to prevent race conditions on mount
  const [selectedSurah, setSelectedSurah] = useState(() => {
    const params = new URLSearchParams(window.location.search);
    const s = params.get("surah") || params.get("surat");
    return s && parseInt(s) >= 1 && parseInt(s) <= 114 ? String(parseInt(s)) : "1";
  });
  const [selectedAyah, setSelectedAyah] = useState(() => {
    const params = new URLSearchParams(window.location.search);
    const a = params.get("ayah") || params.get("ayat");
    return a && parseInt(a) >= 1 ? String(parseInt(a)) : "1";
  });

  const [isAyahFlipped, setIsAyahFlipped] = useState(false);
  const [surahData, setSurahData] = useState(() => {
    const params = new URLSearchParams(window.location.search);
    const s = params.get("surah") || params.get("surat") || "1";
    return surahCache.get(s) || null;
  });
  const [loadingSurah, setLoadingSurah] = useState(!surahCache.has(
    new URLSearchParams(window.location.search).get("surah") || new URLSearchParams(window.location.search).get("surat") || "1"
  ));
  const [kamusLookup, setKamusLookup] = useState(null);

  // Column visibility (NO Bentuk Kata as requested by user)
  const [visibleColumns, setVisibleColumns] = useState({
    kataAkar: true,
    terjemah: true
  });
  const [terjemahLang, setTerjemahLang] = useState("id"); // 'id' | 'en'

  // Tooltip / active states for flip cards
  const [activeLafdzIndex, setActiveLafdzIndex] = useState(null);
  const [activeAkarIndex, setActiveAkarIndex] = useState(null);
  const [toastMessage, setToastMessage] = useState(null);

  // Audio player ref
  const mainAudioRef = useRef(null);

  const showToast = (msg) => {
    setToastMessage(msg);
    setTimeout(() => setToastMessage(null), 3000);
  };

  const handleToggleColumn = (colId) => {
    setVisibleColumns((prev) => ({ ...prev, [colId]: !prev[colId] }));
  };

  // ─── FETCH METADATA & KAMUS LOOKUP ────────────────────────────────────
  useEffect(() => {
    fetch("/mushaf_data/metadata.json")
      .then((res) => res.json())
      .then((data) => setMetadata(data))
      .catch((err) => console.error("Error fetching mushaf metadata:", err));

    fetch("/mushaf_data/kamus_lookup.json")
      .then((res) => res.json())
      .then((data) => setKamusLookup(data))
      .catch((err) => console.warn("Kamus lookup not loaded:", err));
  }, []);

  // ─── SYNC WITH URL SEARCH PARAMS ──────────────────────────────────────
  useEffect(() => {
    const sParam = searchParams.get("surah") || searchParams.get("surat");
    const aParam = searchParams.get("ayah") || searchParams.get("ayat");

    if (sParam && parseInt(sParam) >= 1 && parseInt(sParam) <= 114) {
      const sStr = String(parseInt(sParam));
      setSelectedSurah((prev) => (prev !== sStr ? sStr : prev));
    }
    if (aParam && parseInt(aParam) >= 1) {
      const aStr = String(parseInt(aParam));
      setSelectedAyah((prev) => (prev !== aStr ? aStr : prev));
    }
  }, [searchParams]);

  // ─── FETCH SURAH DATA (WITH CACHE & RACE-CONDITION PREVENTION) ────────
  useEffect(() => {
    if (!selectedSurah) return;
    let isCancelled = false;

    setIsAyahFlipped(false);
    setActiveLafdzIndex(null);
    setActiveAkarIndex(null);

    // If already in memory cache, load synchronously
    if (surahCache.has(selectedSurah)) {
      const data = surahCache.get(selectedSurah);
      setSurahData(data);
      setLoadingSurah(false);

      const ayahs = Object.keys(data).sort((a, b) => parseInt(a) - parseInt(b));
      if (ayahs.length > 0 && !ayahs.includes(selectedAyah)) {
        setSelectedAyah(ayahs[0]);
      }
      return;
    }

    // Otherwise fetch from server
    setLoadingSurah(true);

    fetch(`/mushaf_data/surah_${selectedSurah}.json`)
      .then((res) => {
        if (!res.ok) throw new Error(`Gagal mengambil data Surat ${selectedSurah}`);
        return res.json();
      })
      .then((data) => {
        if (isCancelled) return;
        surahCache.set(selectedSurah, data);
        setSurahData(data);
        setLoadingSurah(false);

        // Auto-select valid ayah if current selectedAyah is out of range
        const ayahs = Object.keys(data).sort((a, b) => parseInt(a) - parseInt(b));
        if (ayahs.length > 0 && !ayahs.includes(selectedAyah)) {
          setSelectedAyah(ayahs[0]);
        }
      })
      .catch((err) => {
        if (isCancelled) return;
        console.error("Error fetching surah data:", err);
        setLoadingSurah(false);
        showToast(`Gagal memuat data Surat ${selectedSurah}. Periksa koneksi internet.`);
      });

    return () => {
      isCancelled = true;
    };
  }, [selectedSurah]);

  // ─── COMPUTED AYAH LIST & NAVIGATION ──────────────────────────────────
  const availableSurahs = useMemo(() => {
    if (metadata) {
      return Object.keys(metadata).sort((a, b) => parseInt(a) - parseInt(b));
    }
    return Array.from({ length: 114 }, (_, i) => String(i + 1));
  }, [metadata]);

  const availableAyahs = useMemo(() => {
    if (surahData) {
      return Object.keys(surahData).sort((a, b) => parseInt(a) - parseInt(b));
    }
    if (metadata && metadata[selectedSurah]) {
      return metadata[selectedSurah].map((a) => String(a));
    }
    return [];
  }, [surahData, metadata, selectedSurah]);

  const currentAyahWords = (surahData && selectedAyah && surahData[selectedAyah]) || [];

  const currentAyahIndex = availableAyahs.indexOf(selectedAyah);
  const isFirstAyah = currentAyahIndex <= 0;
  const isLastAyah = currentAyahIndex >= availableAyahs.length - 1 || currentAyahIndex === -1;

  const handleSelectSurah = (sId) => {
    if (sId !== selectedSurah) {
      setSelectedSurah(sId);
      setSelectedAyah("1");
      setSearchParams({ surah: sId, ayah: "1" });
    }
  };

  const handleSelectAyah = (aId) => {
    setSelectedAyah(aId);
    setIsAyahFlipped(false);
    setActiveLafdzIndex(null);
    setActiveAkarIndex(null);
    setSearchParams({ surah: selectedSurah, ayah: aId });
  };

  const handlePrevAyah = () => {
    if (!isFirstAyah) {
      const prev = availableAyahs[currentAyahIndex - 1];
      handleSelectAyah(prev);
    }
  };

  const handleNextAyah = () => {
    if (!isLastAyah) {
      const next = availableAyahs[currentAyahIndex + 1];
      handleSelectAyah(next);
    }
  };

  // ─── AUDIO URL ────────────────────────────────────────────────────────
  const currentAyahAudioUrl = useMemo(() => {
    if (!selectedSurah || !selectedAyah) return "";
    const s3 = String(selectedSurah).padStart(3, "0");
    const a3 = String(selectedAyah).padStart(3, "0");
    return `https://everyayah.com/data/Alafasy_128kbps/${s3}${a3}.mp3`;
  }, [selectedSurah, selectedAyah]);

  // ─── KAMUS DEEP LINK HELPER ───────────────────────────────────────────
  const getKamusLinkForWord = (word) => {
    if (!word) return "/qkamus";
    const lookup = kamusLookup || {};
    const kataAkar = String(word["Kata/Akar"] || "").replace(/[\u064B-\u065F\u06E1\u06D6-\u06ED]/g, "").trim();
    const kataAkarNoSpace = kataAkar.replace(/\s+/g, "");
    const lafdz = String(word["Lafdz"] || "").replace(/[\u064B-\u065F\u06E1\u06D6-\u06ED]/g, "").trim();

    // 1. Check Musytaq (by root)
    const musytaqMap = lookup.musytaq_roots || {};
    const mEntry = musytaqMap[kataAkar] || musytaqMap[kataAkarNoSpace];
    if (mEntry) {
      const akarId = mEntry.id || mEntry;
      return `/qkamus?dict=musytaq&akar=${akarId}`;
    }

    // 2. Check Jamid Mabny
    const jamidMap = lookup.jamid_words || {};
    const jEntry = jamidMap[kataAkar] || jamidMap[lafdz];
    if (jEntry) {
      const no = jEntry.no || jEntry;
      return `/qkamus?dict=jamid&no=${encodeURIComponent(no)}`;
    }

    // 3. Check Harf Amil
    const harfAmilMap = lookup.harf_amil_words || {};
    const haEntry = harfAmilMap[kataAkar] || harfAmilMap[lafdz];
    if (haEntry) {
      const no = haEntry.no || haEntry;
      return `/qkamus?dict=harf_amil&no=${encodeURIComponent(no)}`;
    }

    // 4. Check Harf Ghair Amil
    const harfMap = lookup.harf_words || {};
    const hEntry = harfMap[kataAkar] || harfMap[lafdz];
    if (hEntry) {
      const no = hEntry.no || hEntry;
      return `/qkamus?dict=harf&no=${encodeURIComponent(no)}`;
    }

    return `/qkamus`;
  };

  // ─── FULL AYAH TEXT & TRANSLATION ─────────────────────────────────────
  const fullAyahArabic = useMemo(() => {
    return currentAyahWords.map((w) => w["Lafdz"]).join(" ");
  }, [currentAyahWords]);

  const fullAyahTranslation = useMemo(() => {
    return currentAyahWords
      .map((w) => String(w["Terjemah"] || "").replace(/\s*\[.*?\]\s*/g, " ").trim())
      .filter((t) => t.length > 0)
      .join(" ")
      .replace(/\s+([,;.])/g, "$1")
      .replace(/\s+/g, " ");
  }, [currentAyahWords]);

  // WhatsApp share
  const shareAyahToWhatsApp = () => {
    const surahIdx = parseInt(selectedSurah) - 1;
    const surahName = SURAH_NAMES[surahIdx] || `Surat ${selectedSurah}`;
    const link = `${window.location.origin}/qmushaf?surah=${selectedSurah}&ayah=${selectedAyah}`;

    const text =
      `*MUSHAF PER KATA — SIMAQ*\n\n` +
      `*QS. ${surahName} [${selectedSurah}:${selectedAyah}]*\n\n` +
      `${fullAyahArabic}\n\n` +
      `*Terjemahan:*\n"${fullAyahTranslation}"\n\n` +
      `Pelajari analisis morfologi & gramatika kata per kata:\n${link}`;

    const waUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`;
    window.location.href = waUrl;
  };

  const surahIdx = parseInt(selectedSurah) - 1;
  const currentSurahName = SURAH_NAMES[surahIdx] || `Surat ${selectedSurah}`;

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-100 transition-colors duration-200">
      <Navbar />

      {/* Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 left-1/2 transform -translate-x-1/2 z-50 bg-slate-900/90 dark:bg-slate-800/95 border border-yellow-500/40 text-yellow-400 px-5 py-2.5 rounded-full shadow-xl text-sm font-medium flex items-center gap-2 backdrop-blur-md">
          <Check className="w-4 h-4 text-emerald-400" />
          <span>{toastMessage}</span>
        </div>
      )}

      {/* Header Banner */}
      <header className="pt-24 pb-8 border-b border-slate-200 dark:border-slate-800 bg-white/50 dark:bg-slate-900/50 backdrop-blur-sm">
        <div className="container mx-auto px-4 max-w-6xl">
          <div className="flex flex-col md:flex-row items-center justify-between gap-4">
            <div>
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold uppercase tracking-wider bg-yellow-500/10 text-yellow-600 dark:text-yellow-400 border border-yellow-500/20 mb-2">
                <BookOpen className="w-3.5 h-3.5" />
                <span>Word-by-Word & Analisis Morfologi</span>
              </div>
              <h1 className="text-2xl md:text-3xl font-bold tracking-tight text-slate-900 dark:text-white">
                Mushaf <span className="text-yellow-500">Per Kata</span>
              </h1>
              <p className="text-sm text-slate-500 dark:text-slate-400 mt-1 max-w-xl">
                Eksplorasi setiap lafaz Al-Qur'an 114 Surah: Akar Kata, Harf/Dhamir Muttashil (Huruf Awalan & Akhiran), Terjemah Multi-Bahasa, dan Audio Kata per Kata.
              </p>
            </div>

            {/* Link to Kamus */}
            <Link
              to="/qkamus"
              className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-semibold bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 transition shadow-sm"
            >
              <ExternalLink className="w-3.5 h-3.5 text-yellow-500" />
              <span>Buka Portal Kamus Al-Qur'an</span>
            </Link>
          </div>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="container mx-auto px-4 py-8 max-w-6xl">
        {/* Controls Container (Pilih Surat, Pilih Ayat, Tampilkan Kolom) */}
        <section className="bg-white dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/80 rounded-2xl p-4 md:p-6 mb-8 shadow-sm">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
            {/* 1. Pilih Surat */}
            <div className="selector-section">
              <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-2 flex items-center gap-1.5">
                <BookOpen className="w-4 h-4 text-yellow-500" />
                <span>Pilih Surat</span>
              </label>
              <div className="relative">
                <select
                  value={selectedSurah}
                  onChange={(e) => handleSelectSurah(e.target.value)}
                  className="w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-100 text-sm rounded-xl py-2.5 px-3.5 pr-9 appearance-none focus:outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer shadow-xs"
                >
                  {availableSurahs.map((sId) => {
                    const idx = parseInt(sId) - 1;
                    const name = SURAH_NAMES[idx] || `Surat ${sId}`;
                    return (
                      <option key={sId} value={sId}>
                        {sId}. {name}
                      </option>
                    );
                  })}
                </select>
                <ChevronDown className="w-4 h-4 text-slate-400 absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none" />
              </div>
            </div>

            {/* 2. Pilih Ayat */}
            <div className="selector-section">
              <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-2 flex items-center justify-between">
                <span className="flex items-center gap-1.5">
                  <RotateCw className="w-4 h-4 text-yellow-500" />
                  Pilih Ayat
                </span>
                <span className="text-[11px] font-normal text-slate-400">({availableAyahs.length} Ayat)</span>
              </label>
              <div className="flex items-center gap-2">
                <button
                  onClick={handlePrevAyah}
                  disabled={isFirstAyah}
                  className="p-2.5 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed transition"
                  title="Ayat Sebelumnya"
                >
                  <ChevronLeft className="w-4 h-4" />
                </button>
                <div className="relative flex-1">
                  <select
                    value={selectedAyah}
                    onChange={(e) => handleSelectAyah(e.target.value)}
                    className="w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-100 text-sm rounded-xl py-2.5 px-3.5 pr-9 appearance-none focus:outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer shadow-xs"
                  >
                    {availableAyahs.map((aId) => (
                      <option key={aId} value={aId}>
                        Ayat {aId}
                      </option>
                    ))}
                  </select>
                  <ChevronDown className="w-4 h-4 text-slate-400 absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none" />
                </div>
                <button
                  onClick={handleNextAyah}
                  disabled={isLastAyah}
                  className="p-2.5 rounded-xl bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed transition"
                  title="Ayat Selanjutnya"
                >
                  <ChevronRight className="w-4 h-4" />
                </button>
              </div>
            </div>

            {/* 3. Tampilkan Kolom (NO Bentuk Kata!) */}
            <div className="selector-section">
              <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-2 flex items-center gap-1.5">
                <Layers className="w-4 h-4 text-yellow-500" />
                <span>Tampilkan Kolom</span>
              </label>
              <div className="flex items-center gap-3 bg-slate-50 dark:bg-slate-900 p-2 rounded-xl border border-slate-200 dark:border-slate-700">
                <label className="flex items-center gap-2 cursor-pointer text-xs font-semibold text-slate-700 dark:text-slate-200 select-none">
                  <input
                    type="checkbox"
                    checked={visibleColumns.kataAkar}
                    onChange={() => handleToggleColumn("kataAkar")}
                    className="w-4 h-4 rounded text-yellow-500 accent-yellow-500 focus:ring-0 cursor-pointer"
                  />
                  <span>Kata/Akar</span>
                </label>
                <label className="flex items-center gap-2 cursor-pointer text-xs font-semibold text-slate-700 dark:text-slate-200 select-none ml-2">
                  <input
                    type="checkbox"
                    checked={visibleColumns.terjemah}
                    onChange={() => handleToggleColumn("terjemah")}
                    className="w-4 h-4 rounded text-yellow-500 accent-yellow-500 focus:ring-0 cursor-pointer"
                  />
                  <span>Terjemah</span>
                </label>
              </div>
            </div>
          </div>
        </section>

        {/* LOADING STATEMENT */}
        {loadingSurah && (
          <div className="bg-white dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/80 rounded-2xl p-8 md:p-12 text-center shadow-sm my-6 animate-fade-in">
            <div className="relative w-16 h-16 mx-auto mb-4">
              <div className="w-16 h-16 border-4 border-yellow-500/20 border-t-yellow-500 rounded-full animate-spin" />
              <BookOpen className="w-6 h-6 text-yellow-500 absolute inset-0 m-auto" />
            </div>
            <h3 className="text-lg md:text-xl font-bold text-slate-900 dark:text-white mb-2">
              Memuat Data Mushaf Per Kata...
            </h3>
            <p className="text-sm text-slate-500 dark:text-slate-400 max-w-md mx-auto leading-relaxed">
              Sedang memuat analisis morfologi kata, akar kata, dan harf/dhamir muttashil untuk{" "}
              <span className="font-semibold text-yellow-600 dark:text-yellow-400">
                Surat {selectedSurah} ({currentSurahName}), Ayat {selectedAyah}
              </span>
              . Mohon tunggu sebentar...
            </p>
            <div className="mt-5 inline-flex items-center gap-2 px-3 py-1.5 rounded-full text-xs font-medium bg-yellow-500/10 text-yellow-600 dark:text-yellow-400 border border-yellow-500/20">
              <span className="w-2 h-2 rounded-full bg-yellow-500 animate-pulse" />
              <span>Memproses 114 Surah Word-by-Word</span>
            </div>
          </div>
        )}

        {/* EMPTY STATE / FALLBACK WHEN AYAH WORDS NOT FOUND */}
        {!loadingSurah && currentAyahWords.length === 0 && (
          <div className="bg-white dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/80 rounded-2xl p-8 md:p-10 text-center shadow-sm my-6 animate-fade-in">
            <BookOpen className="w-12 h-12 text-slate-400 mx-auto mb-3 opacity-40" />
            <h3 className="text-base md:text-lg font-bold text-slate-900 dark:text-white mb-1.5">
              Data Ayat {selectedAyah} Belum Tersedia
            </h3>
            <p className="text-xs md:text-sm text-slate-500 dark:text-slate-400 max-w-md mx-auto mb-5 leading-relaxed">
              Ayat {selectedAyah} tidak ditemukan pada Surat {selectedSurah} ({currentSurahName}). Silakan pilih nomor ayat yang tersedia dalam daftar di atas.
            </p>
            <div className="flex flex-wrap items-center justify-center gap-3">
              <button
                onClick={() => handleSelectAyah("1")}
                className="px-4 py-2 rounded-xl text-xs font-bold bg-yellow-500 text-slate-900 hover:bg-yellow-400 transition shadow-sm"
              >
                Tampilkan Ayat 1
              </button>
              <button
                onClick={() => {
                  surahCache.delete(selectedSurah);
                  setSelectedSurah((prev) => prev);
                }}
                className="px-4 py-2 rounded-xl text-xs font-semibold bg-slate-100 dark:bg-slate-700 text-slate-700 dark:text-slate-200 hover:bg-slate-200 dark:hover:bg-slate-600 transition"
              >
                Muat Ulang Data Surat
              </button>
            </div>
          </div>
        )}

        {/* AYAH HEADER, AUDIO & FLIP CARD */}
        {!loadingSurah && currentAyahWords.length > 0 && (
          <div>
            {/* Header Ayat & Action Controls */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-5">
              <div className="flex flex-col sm:flex-row sm:items-center gap-3">
                <h2 className="text-xl md:text-2xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
                  <span className="text-yellow-500">
                    Surat {selectedSurah} ({currentSurahName}), Ayat {selectedAyah}
                  </span>
                </h2>
              </div>

              <div className="flex items-center gap-2.5 flex-wrap">
                {/* Native HTML5 Audio Murottal (Alafasy) */}
                <audio
                  id="main-ayah-audio"
                  ref={mainAudioRef}
                  controls
                  src={currentAyahAudioUrl}
                  className="h-8 max-w-[220px] sm:max-w-xs"
                  preload="none"
                />

                {/* WhatsApp Share */}
                <button
                  onClick={shareAyahToWhatsApp}
                  className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-emerald-600 hover:bg-emerald-700 text-white transition shadow-sm"
                  title="Bagikan Ayat ke WhatsApp"
                >
                  <MessageCircle className="w-3.5 h-3.5" />
                  <span>Kirim WA</span>
                </button>

                {/* Copy Link */}
                <button
                  onClick={() => {
                    const url = `${window.location.origin}/qmushaf?surah=${selectedSurah}&ayah=${selectedAyah}`;
                    navigator.clipboard.writeText(url).then(() => {
                      showToast("Link ayat berhasil disalin!");
                    });
                  }}
                  className="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition"
                  title="Salin Link Ayat"
                >
                  <Copy className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>

            {/* 3D Flip Card Ayat Utama */}
            <div
              onClick={() => setIsAyahFlipped(!isAyahFlipped)}
              className="cursor-pointer mb-8"
              style={{ perspective: "1000px" }}
              title="Klik untuk membalik dan melihat terjemahan ayat"
            >
              <div
                style={{
                  position: "relative",
                  transition: "transform 0.7s cubic-bezier(0.34, 1.56, 0.64, 1)",
                  transformStyle: "preserve-3d",
                  transform: isAyahFlipped ? "rotateX(180deg)" : "rotateX(0deg)",
                  minHeight: "150px"
                }}
              >
                {/* Front: Arabic Text */}
                <div
                  style={{ backfaceVisibility: "hidden", WebkitBackfaceVisibility: "hidden" }}
                  className="bg-gradient-to-br from-slate-900 to-slate-800 border border-slate-700 rounded-2xl p-6 sm:p-8 shadow-md flex flex-col justify-center relative"
                >
                  <div className="absolute top-3 right-3 text-xs text-slate-400 flex items-center gap-1">
                    <RotateCw className="w-3.5 h-3.5 text-yellow-500" />
                    <span className="hidden sm:inline">Klik untuk Terjemahan</span>
                  </div>
                  <p
                    className="text-2xl md:text-3xl font-arabic text-center leading-loose text-slate-100"
                    dir="rtl"
                  >
                    {fullAyahArabic}
                  </p>
                </div>

                {/* Back: Translation */}
                <div
                  style={{
                    backfaceVisibility: "hidden",
                    WebkitBackfaceVisibility: "hidden",
                    transform: "rotateX(180deg)",
                    position: "absolute",
                    inset: 0
                  }}
                  className="bg-gradient-to-br from-slate-900 to-slate-800 border border-yellow-500/40 rounded-2xl p-6 sm:p-8 shadow-md flex flex-col items-center justify-center text-center"
                >
                  <div className="absolute top-3 right-3 text-xs text-slate-400 flex items-center gap-1">
                    <RotateCw className="w-3.5 h-3.5 text-yellow-500" />
                    <span className="hidden sm:inline">Lihat Teks Arab</span>
                  </div>
                  <div className="text-xs uppercase tracking-wider font-semibold text-yellow-500 mb-2">
                    {terjemahLang === "en" ? "English Translation" : "Terjemahan Kementerian Agama RI"}
                  </div>
                  <p className="text-base md:text-lg text-yellow-300 font-medium leading-relaxed max-w-3xl italic">
                    "<TranslatedText text={fullAyahTranslation} lang={terjemahLang} />"
                  </p>
                </div>
              </div>
            </div>

            {/* Word-by-Word Table (NO Bentuk Kata, Lafdz Flips for Huruf Awalan/Akhiran, Kata/Akar with Kamus Button) */}
            <div className="bg-white dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/80 rounded-2xl overflow-hidden shadow-sm">
              <div className="overflow-x-auto">
                <table className="w-full text-sm border-collapse" dir="rtl">
                  <thead>
                    <tr className="bg-slate-100 dark:bg-slate-900 text-xs font-bold text-slate-700 dark:text-slate-200 border-b border-slate-200 dark:border-slate-700">
                      {/* 1. Lafdz */}
                      <th className="py-3.5 px-4 text-center" style={{ width: "35%" }}>
                        Lafdz
                      </th>

                      {/* 2. Kata / Akar */}
                      {visibleColumns.kataAkar && (
                        <th className="py-3.5 px-4 text-center text-yellow-600 dark:text-yellow-400 bg-yellow-500/5" style={{ width: "35%" }}>
                          Kata / Akar
                        </th>
                      )}

                      {/* 3. Terjemah with Language Selector */}
                      {visibleColumns.terjemah && (
                        <th className="py-3.5 px-4 text-left" dir="ltr" style={{ width: "30%" }}>
                          <div className="flex items-center justify-between gap-2">
                            <span>Terjemah</span>
                            <div className="inline-flex items-center gap-1 border border-yellow-500/40 rounded-lg p-0.5 bg-yellow-500/10">
                              <button
                                onClick={() => setTerjemahLang("id")}
                                className={`px-2 py-0.5 rounded text-[11px] font-bold transition ${
                                  terjemahLang === "id"
                                    ? "bg-yellow-500 text-slate-900 shadow-xs"
                                    : "text-yellow-600 dark:text-yellow-400 hover:text-yellow-500"
                                }`}
                              >
                                ID
                              </button>
                              <button
                                onClick={() => setTerjemahLang("en")}
                                className={`px-2 py-0.5 rounded text-[11px] font-bold transition ${
                                  terjemahLang === "en"
                                    ? "bg-yellow-500 text-slate-900 shadow-xs"
                                    : "text-yellow-600 dark:text-yellow-400 hover:text-yellow-500"
                                }`}
                              >
                                EN
                              </button>
                            </div>
                          </div>
                        </th>
                      )}
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100 dark:divide-slate-700/60">
                    {currentAyahWords.map((word, idx) => {
                      const lafdz = word["Lafdz"] || "";
                      const terjemah = word["Terjemah"] || "";
                      const kataAkar = word["Kata/Akar"] || "";
                      const arti = word["Arti "] || word["Arti"] || "";
                      const muttashil = (word["Dhamir Muttashil / Harf Muttashil"] || "").trim();

                      const isLafdzFlipped = activeLafdzIndex === idx;
                      const isAkarFlipped = activeAkarIndex === idx;

                      return (
                        <tr
                          key={idx}
                          className="hover:bg-yellow-500/5 dark:hover:bg-yellow-500/5 transition"
                        >
                          {/* 1. Lafadz — Click to flip and reveal Huruf Awalan & Akhiran */}
                          <td
                            className="p-2 text-center align-middle cursor-pointer select-none"
                            onClick={() => {
                              if (muttashil) {
                                setActiveLafdzIndex(isLafdzFlipped ? null : idx);
                              }
                            }}
                            title={muttashil ? "Klik untuk melihat Huruf Awalan & Akhiran (Dhamir/Harf Muttashil)" : "Kata tunggal tanpa awalan/akhiran"}
                          >
                            <div className={`flip-container ${isLafdzFlipped ? "flipped" : ""}`}>
                              <div className="flip-inner">
                                {/* Front: Arabic Lafdz */}
                                <div className="flip-front">
                                  <div className="flex items-center justify-center gap-1.5">
                                    <span className="text-2xl md:text-3xl font-bold font-arabic text-slate-900 dark:text-white">
                                      {lafdz}
                                    </span>
                                    {muttashil ? (
                                      <span
                                        className="w-2 h-2 rounded-full bg-yellow-500"
                                        title="Memiliki huruf awalan/akhiran (klik untuk melihat)"
                                      />
                                    ) : (
                                      <span className="opacity-30 text-xs">&bull;</span>
                                    )}
                                  </div>
                                </div>

                                {/* Back: Huruf Awalan & Akhiran */}
                                <div className="flip-back bg-slate-800 text-white rounded-xl p-2.5 shadow-inner">
                                  <div className="text-[10px] font-bold uppercase tracking-wider text-yellow-400 mb-1" dir="ltr">
                                    {getMuttashilTitle(muttashil)}
                                  </div>
                                  <div className="text-base font-arabic font-bold text-white">
                                    {renderMixedText(muttashil, "white")}
                                  </div>
                                </div>
                              </div>
                            </div>
                          </td>

                          {/* 2. Kata / Akar — Click to flip to see Arti, and includes Button to Kamus */}
                          {visibleColumns.kataAkar && (
                            <td
                              className="p-2 text-center align-middle bg-yellow-500/[0.03] select-none"
                              onClick={() => {
                                if (arti) {
                                  setActiveAkarIndex(isAkarFlipped ? null : idx);
                                }
                              }}
                              title={arti ? "Klik kartu untuk melihat arti akar kata" : ""}
                            >
                              <div className={`flip-container cursor-pointer ${isAkarFlipped ? "flipped" : ""}`}>
                                <div className="flip-inner">
                                  {/* Front: Kata / Akar */}
                                  <div className="flip-front">
                                    <div className="font-arabic text-xl font-bold text-yellow-600 dark:text-yellow-400">
                                      {renderMixedText(kataAkar || "-", "#fde047")}
                                    </div>
                                  </div>

                                  {/* Back: Arti Akar */}
                                  <div className="flip-back bg-yellow-500/10 text-yellow-600 dark:text-yellow-400 rounded-xl p-2 border border-yellow-500/20" dir="ltr">
                                    <div className="text-xs font-semibold leading-relaxed">
                                      {renderMixedText(arti || "-", "#fde047")}
                                    </div>
                                  </div>
                                </div>
                              </div>

                              {/* Button ke Kamus */}
                              <div className="flex justify-center mt-1">
                                <Link
                                  to={getKamusLinkForWord(word)}
                                  onClick={(e) => e.stopPropagation()}
                                  className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs font-semibold bg-yellow-500/15 hover:bg-yellow-500/25 text-yellow-600 dark:text-yellow-400 border border-yellow-500/30 transition shadow-xs"
                                  title="Buka Analisis Kata ini di Kamus Al-Qur'an"
                                >
                                  <BookOpen className="w-3 h-3" />
                                  <span>Kamus</span>
                                  <ExternalLink className="w-2.5 h-2.5 opacity-70" />
                                </Link>
                              </div>
                            </td>
                          )}

                          {/* 3. Terjemah with Live Translation & Audio Playback Button */}
                          {visibleColumns.terjemah && (
                            <td className="py-3 px-4 text-left align-middle" dir="ltr">
                              <div className="flex items-center justify-between gap-3">
                                <span className="text-xs sm:text-sm font-medium text-slate-800 dark:text-slate-200">
                                  <TranslatedText
                                    text={String(terjemah || "").replace(/\s*\[.*?\]\s*/g, " ").trim()}
                                    lang={terjemahLang}
                                  />
                                </span>
                                <button
                                  onClick={(e) => {
                                    e.stopPropagation();
                                    playQuranWord(word["SURAT_ID"], word["AYAT_ID"], idx + 1, lafdz);
                                  }}
                                  className="p-1.5 rounded-lg text-yellow-600 dark:text-yellow-400 hover:bg-yellow-500/10 transition shrink-0"
                                  title="Putar Audio Lafadz"
                                >
                                  <Volume2 className="w-4 h-4" />
                                </button>
                              </div>
                            </td>
                          )}
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            </div>

            {/* Bottom Stepper Buttons */}
            <div className="flex items-center justify-center gap-3 mt-8">
              <button
                onClick={handlePrevAyah}
                disabled={isFirstAyah}
                className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-semibold bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-slate-700 dark:text-slate-200 transition"
              >
                <ChevronLeft className="w-4 h-4" />
                <span>Ayat Sebelumnya</span>
              </button>

              <button
                onClick={handleNextAyah}
                disabled={isLastAyah}
                className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-semibold bg-yellow-500 hover:bg-yellow-400 text-slate-900 font-bold disabled:opacity-40 disabled:cursor-not-allowed transition shadow-sm"
              >
                <span>Ayat Selanjutnya</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        )}
      </main>

      <Footer />
    </div>
  );
};

export default QMushaf;
