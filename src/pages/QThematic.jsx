import React, { useState, useEffect, useRef, useCallback } from "react";
import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import {
  Sparkles, BookOpen, Volume2, ChevronLeft, ChevronRight,
  ChevronDown, ChevronUp, Languages, MessageCircle, Copy,
  ExternalLink, RotateCw, X, Check,
} from "lucide-react";

const LANG_CONFIG = {
  "id-ID": { name: "Bahasa Indonesia" },
  "ms-MY": { name: "Bahasa Melayu" },
  "en-US": { name: "English" },
  "ur-PK": { name: "Urdu" },
  "bn-BD": { name: "Bangla" },
  "hi-IN": { name: "Hindi" },
  "ru-RU": { name: "Русский" },
  "zh-CN": { name: "中文" },
  "fr-FR": { name: "Français" },
  "es-ES": { name: "Español" },
  "pt-PT": { name: "Português" },
  "it-IT": { name: "Italiano" },
  "tr-TR": { name: "Türkçe" },
  "de-DE": { name: "Deutsch" },
  "ko-KR": { name: "한국어" },
  "ja-JP": { name: "日本語" },
  "th-TH": { name: "ภาษาไทย" },
  "ar-SA": { name: "العربية" },
};

// Edition codes for api.alquran.cloud/v1/ayah/{s}:{a}/{edition}
const LANG_EDITIONS = {
  "id-ID": null,          // pakai v.indo langsung
  "ar-SA": null,          // pakai v.arab langsung
  "ms-MY": "ms.basmeih",
  "en-US": "en.sahih",
  "ur-PK": "ur.jalandhry",
  "bn-BD": "bn.bengali",
  "hi-IN": "hi.hindi",
  "ru-RU": "ru.kuliev",
  "zh-CN": "zh.jian",
  "fr-FR": "fr.hamidullah",
  "es-ES": "es.cortes",
  "pt-PT": "pt.elhayek",
  "it-IT": "it.piccardo",
  "tr-TR": "tr.diyanet",
  "de-DE": "de.aburida",
  "ko-KR": "ko.korean",
  "ja-JP": "ja.japanese",
  "th-TH": "th.thai",
};

// Module-level cache: "edition:surah:ayat" -> text
const translationCache = {};

const getInitialLanguage = () => {
  try { const s = localStorage.getItem("active_lang"); if (s && LANG_CONFIG[s]) return s; } catch (e) {}
  return "id-ID";
};
const naturalCompare = (a, b) => (a||"").toString().localeCompare((b||"").toString(), undefined, { numeric: true, sensitivity: "base" });
const naturalSort = (arr) => [...arr].sort(naturalCompare);

const QThematic = () => {
  const [quranData, setQuranData] = useState({});
  const [isLoading, setIsLoading] = useState(true);
  const [selectedTema, setSelectedTema] = useState("");
  const [selectedPokok, setSelectedPokok] = useState("");
  const [selectedSub, setSelectedSub] = useState("");
  const [collapsedGroups, setCollapsedGroups] = useState(new Set());
  const [fontScale, setFontScale] = useState(0);
  const [playingKey, setPlayingKey] = useState(null);   // TTS key
  const [murottalKey, setMurottalKey] = useState(null); // murottal audio key
  const currentUtteranceRef = useRef(null);
  const currentAudioRef = useRef(null);
  const [flippedCards, setFlippedCards] = useState({});
  const [isAiModalOpen, setIsAiModalOpen] = useState(false);
  const [aiModalVerse, setAiModalVerse] = useState(null);
  const [aiMode, setAiMode] = useState("tadabbur");
  const [aiCustomQuestion, setAiCustomQuestion] = useState("");
  const [selectedLang, setSelectedLang] = useState(getInitialLanguage);
  const [ayahTranslations, setAyahTranslations] = useState({});
  const [isTranslating, setIsTranslating] = useState(false);
  const [toastMessage, setToastMessage] = useState(null);

  const showToast = (msg) => { setToastMessage(msg); setTimeout(() => setToastMessage(null), 3000); };

  const stopTTS = useCallback(() => {
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    setPlayingKey(null);
  }, []);

  const stopMurottal = useCallback(() => {
    if (currentAudioRef.current) {
      currentAudioRef.current.pause();
      currentAudioRef.current.src = "";
      currentAudioRef.current = null;
    }
    setMurottalKey(null);
  }, []);

  const handlePlayMurottal = (surah, ayat) => {
    const key = `murottal-${surah}:${ayat}`;
    if (murottalKey === key) { stopMurottal(); return; }
    stopTTS();
    stopMurottal();
    const surahPadded = String(surah).padStart(3, "0");
    const ayatPadded = String(ayat).padStart(3, "0");
    const url = `https://everyayah.com/data/Alafasy_128kbps/${surahPadded}${ayatPadded}.mp3`;
    const audio = new Audio(url);
    audio.onplay = () => setMurottalKey(key);
    audio.onended = () => setMurottalKey(null);
    audio.onerror = () => { setMurottalKey(null); showToast("Audio murottal tidak tersedia."); };
    currentAudioRef.current = audio;
    audio.play().catch(() => { setMurottalKey(null); showToast("Gagal memutar audio murottal."); });
    setMurottalKey(key);
  };

  useEffect(() => {
    fetch("/quran-thematic-new.json")
      .then((res) => { if (!res.ok) throw new Error("Gagal memuat"); return res.json(); })
      .then((data) => {
        setQuranData(data);
        setIsLoading(false);
        const temas = naturalSort(Object.keys(data));
        if (temas.length > 0) {
          const firstTema = temas[0];
          setSelectedTema(firstTema);
          const pokoks = naturalSort(Object.keys(data[firstTema] || {}));
          if (pokoks.length > 0) {
            setSelectedPokok(pokoks[0]);
            const subs = naturalSort(Object.keys(data[firstTema][pokoks[0]] || {}));
            if (subs.length > 0) setSelectedSub(subs[0]);
          }
        }
      })
      .catch((err) => { console.error("Error loading thematic database:", err); setIsLoading(false); });
  }, []);

  // Fetch translations when language or displayed sub bahasan changes
  useEffect(() => {
    if (!currentSubData) return;
    const edition = LANG_EDITIONS[selectedLang];

    // For Indonesian or Arabic, use embedded data directly
    if (!edition) {
      setAyahTranslations({});
      setIsTranslating(false);
      return;
    }

    // Collect all visible verses
    const allVerses = displayUraianKeys.flatMap((key) => currentSubData[key]?.verses || []);
    if (allVerses.length === 0) return;

    // Check which need fetching
    const toFetch = allVerses.filter((v) => !translationCache[`${edition}:${v.surah_num}:${v.ayat_num}`]);

    const buildState = () => {
      const newT = {};
      allVerses.forEach((v) => {
        const cached = translationCache[`${edition}:${v.surah_num}:${v.ayat_num}`];
        if (cached) newT[`${v.surah_num}:${v.ayat_num}`] = cached;
      });
      setAyahTranslations(newT);
    };

    if (toFetch.length === 0) { buildState(); return; }

    setIsTranslating(true);
    let cancelled = false;

    const fetchOne = async (v) => {
      const cacheKey = `${edition}:${v.surah_num}:${v.ayat_num}`;
      if (translationCache[cacheKey]) return;
      try {
        const res = await fetch(`https://api.alquran.cloud/v1/ayah/${v.surah_num}:${v.ayat_num}/${edition}`);
        const json = await res.json();
        if (json.code === 200 && json.data?.text) {
          translationCache[cacheKey] = json.data.text;
        }
      } catch (_) {}
    };

    // Fetch in batches of 8 to avoid rate limiting
    const runBatched = async () => {
      const batchSize = 8;
      for (let i = 0; i < toFetch.length; i += batchSize) {
        if (cancelled) return;
        await Promise.all(toFetch.slice(i, i + batchSize).map(fetchOne));
      }
      if (!cancelled) { buildState(); setIsTranslating(false); }
    };

    runBatched();
    return () => { cancelled = true; };
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [selectedLang, selectedSub, selectedPokok, selectedTema]);

  const temaOptions = naturalSort(Object.keys(quranData));
  const pokokOptions = selectedTema && quranData[selectedTema] ? naturalSort(Object.keys(quranData[selectedTema])) : [];
  const subOptions = selectedTema && selectedPokok && quranData[selectedTema]?.[selectedPokok]
    ? naturalSort(Object.keys(quranData[selectedTema][selectedPokok])) : [];
  const currentSubData = selectedTema && selectedPokok && selectedSub
    ? quranData[selectedTema]?.[selectedPokok]?.[selectedSub] : null;
  const displayUraianKeys = currentSubData ? naturalSort(Object.keys(currentSubData)) : [];

  const handleTemaChange = (e) => {
    const t = e.target.value;
    setSelectedTema(t); setSelectedPokok(""); setSelectedSub(""); setFlippedCards({}); stopTTS();
    if (t && quranData[t]) {
      const pList = naturalSort(Object.keys(quranData[t]));
      if (pList.length > 0) {
        setSelectedPokok(pList[0]);
        const sList = naturalSort(Object.keys(quranData[t][pList[0]] || {}));
        if (sList.length > 0) setSelectedSub(sList[0]);
      }
    }
  };
  const handlePokokChange = (e) => {
    const p = e.target.value;
    setSelectedPokok(p); setSelectedSub(""); setFlippedCards({}); stopTTS();
    if (selectedTema && p && quranData[selectedTema]?.[p]) {
      const sList = naturalSort(Object.keys(quranData[selectedTema][p]));
      if (sList.length > 0) setSelectedSub(sList[0]);
    }
  };
  const handleSubChange = (e) => { setSelectedSub(e.target.value); setFlippedCards({}); stopTTS(); };

  const toggleCardFlip = (cardKey) => setFlippedCards((prev) => ({ ...prev, [cardKey]: !prev[cardKey] }));

  const handlePlayTTS = (text, surah, ayat) => {
    const key = `${surah}:${ayat}`;
    if (playingKey === key) { stopTTS(); return; }
    stopTTS();
    setPlayingKey(key);
    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
      const utter = new SpeechSynthesisUtterance(text);
      utter.lang = selectedLang; utter.rate = 0.9;
      utter.onend = () => setPlayingKey(null); utter.onerror = () => setPlayingKey(null);
      currentUtteranceRef.current = utter;
      window.speechSynthesis.speak(utter);
    } else { setPlayingKey(null); }
  };

  const shareSubToWhatsApp = () => {
    if (!selectedSub) return;
    const link = `${window.location.origin}/qthematic`;
    const text = `*AL-QURAN TEMATIS - e-Furqan*\n\n*Tema:* ${selectedTema}\n*Pokok Bahasan:* ${selectedPokok}\n*Sub Bahasan:* ${selectedSub}\n*Total Kelompok Uraian:* ${displayUraianKeys.length} Topik\n\nEksplorasi ayat tematis:\n${link}`;
    window.location.href = `https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`;
  };
  const shareUraianToWhatsApp = (uraianTitle, verses) => {
    if (!uraianTitle || !verses || verses.length === 0) return;
    const link = `${window.location.origin}/qthematic`;
    const verseList = verses.slice(0, 6).map((v) => `• QS. ${v.surah_name} [${v.surah_num}:${v.ayat_num}]`).join("\n");
    const more = verses.length > 6 ? `\n...dan ${verses.length - 6} ayat lainnya` : "";
    const text = `*AL-QURAN TEMATIS - e-Furqan*\n\n*Tema:* ${selectedTema}\n*Kelompok Uraian:* ${uraianTitle}\n*Daftar Ayat (${verses.length}):*\n${verseList}${more}\n\n${link}`;
    window.location.href = `https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`;
  };
  const shareVerseToWhatsApp = (v) => {
    if (!v) return;
    const link = `${window.location.origin}/qmushaf?surah=${v.surah_num}&ayah=${v.ayat_num}`;
    const text = `*AYAT TEMATIS - e-Furqan*\n\n*QS. ${v.surah_name} [${v.surah_num}:${v.ayat_num}]*\n\n${v.arab}\n\n*Terjemahan:*\n"${v.indo}"\n\nBuka selengkapnya:\n${link}`;
    window.location.href = `https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`;
  };

  const generateAiPrompt = () => {
    if (!aiModalVerse) return "";
    const { surah_num: s, ayat_num: a, surah_name: sName, arab, indo } = aiModalVerse;
    let modeInstruction = "";
    if (aiMode === "tadabbur") modeInstruction = "FOKUS KAJIAN: Tadabbur Tematis & Pelajaran Hidup\nJelaskan hikmah, tadabbur, dan pelajaran praktis dari ayat ini.";
    else if (aiMode === "asbab") modeInstruction = "FOKUS KAJIAN: Asbabun Nuzul Shahih\nSebutkan sebab turunnya ayat ini HANYA jika bersumber dari riwayat shahih/hasan.";
    else if (aiMode === "mufradat") modeInstruction = "FOKUS KAJIAN: Analisis Kebahasaan & Mufradat\nBedah kosakata kunci secara morfologis dan terangkan keindahan balaghah.";
    else if (aiMode === "custom") modeInstruction = `PERTANYAAN PENGGUNA:\n"${aiCustomQuestion}"\nJawab pertanyaan di atas berdasarkan dalil nash ayat dan tafsir mu'tabar.`;
    return `[SISTEM AL-QURAN BERINTEGRITAS ILMIAH - PROTOKOL ZERO HALLUCINATION]
Anda adalah asisten Al-Quran terpercaya bebas halusinasi.

DATA RUJUKAN RESMI:
- Surat & Ayat: QS. ${sName} [${s}] : Ayat ${a}
- Teks Arab Asli: ${arab}
- Terjemahan Resmi Kemenag RI: "${indo}"

ATURAN KETAT:
1. Seluruh jawaban WAJIB bersumber dari nash ayat, hadits shahih mu'tabar, dan tafsir mu'tabar (Ibnu Katsir, At-Thabari, Al-Qurthubi, Kemenag RI).
2. DILARANG mengarang riwayat, asbabun nuzul fiktif, atau sanad palsu.
3. Jika tidak ada riwayat shahih, nyatakan: "Tidak terdapat riwayat shahih, Wallahu a'lam".

${modeInstruction}`;
  };

  const openAiPlatform = (platform) => {
    const prompt = generateAiPrompt();
    if (platform === "gemini") { navigator.clipboard.writeText(prompt).catch(() => {}); showToast("Prompt disalin! Membuka Google Gemini..."); setTimeout(() => window.open("https://gemini.google.com/app", "_blank"), 400); }
    else if (platform === "chatgpt") { window.open(`https://chatgpt.com/?q=${encodeURIComponent(prompt)}`, "_blank"); }
    else if (platform === "claude") { navigator.clipboard.writeText(prompt).catch(() => {}); showToast("Prompt disalin! Membuka Claude..."); setTimeout(() => window.open("https://claude.ai/new", "_blank"), 400); }
  };

  const arabicFontClass = fontScale === -1 ? "text-xl sm:text-2xl" : fontScale === 1 ? "text-3xl sm:text-4xl" : fontScale === 2 ? "text-4xl sm:text-5xl" : "text-2xl sm:text-3xl";

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-100 transition-colors duration-200">
      <Navbar />

      {toastMessage && (
        <div className="fixed bottom-6 left-1/2 transform -translate-x-1/2 z-50 bg-slate-900/90 dark:bg-slate-800/95 border border-yellow-500/40 text-yellow-400 px-5 py-2.5 rounded-full shadow-xl text-sm font-medium flex items-center gap-2 backdrop-blur-md">
          <Check className="w-4 h-4 text-emerald-400" /><span>{toastMessage}</span>
        </div>
      )}

      <header className="pt-24 pb-8 border-b border-slate-200 dark:border-slate-800 bg-white/50 dark:bg-slate-900/50 backdrop-blur-sm">
        <div className="container mx-auto px-4 max-w-6xl">
          <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
            <div>
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold uppercase tracking-wider bg-yellow-500/10 text-yellow-600 dark:text-yellow-400 border border-yellow-500/20 mb-2">
                <BookOpen className="w-3.5 h-3.5" /><span>Al-Qur'an Tematis</span>
              </div>
              <h1 className="text-2xl md:text-3xl font-bold tracking-tight text-slate-900 dark:text-white">
                Al-Qur'an <span className="text-yellow-500">Tematis</span>
              </h1>
              <p className="text-sm text-slate-500 dark:text-slate-400 mt-1 max-w-xl">
                Eksplorasi kandungan ayat Al-Qur'an berdasarkan tema kehidupan, dengan audio TTS multi-bahasa dan asisten AI anti-halusinasi.
              </p>
            </div>
            <div className="flex flex-wrap items-center gap-2.5">
              <div className="flex items-center bg-slate-100 dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 p-1 gap-0.5">
                <button onClick={() => setFontScale((p) => Math.max(-1, p - 1))} className="px-2.5 py-1 text-xs font-bold text-slate-600 dark:text-slate-300 hover:text-yellow-500 transition">A-</button>
                <button onClick={() => setFontScale(0)} className="px-2 py-1 text-xs font-bold text-slate-600 dark:text-slate-300 hover:text-yellow-500 transition">A</button>
                <button onClick={() => setFontScale((p) => Math.min(2, p + 1))} className="px-2.5 py-1 text-xs font-bold text-slate-600 dark:text-slate-300 hover:text-yellow-500 transition">A+</button>
              </div>
              <div className="flex items-center gap-2 bg-slate-100 dark:bg-slate-800 p-1.5 rounded-xl border border-slate-200 dark:border-slate-700">
                <Languages className="w-4 h-4 text-yellow-500 ml-1.5 shrink-0" />
                <select
                  value={selectedLang}
                  onChange={(e) => { setSelectedLang(e.target.value); localStorage.setItem("active_lang", e.target.value); stopTTS(); }}
                  className="bg-transparent text-xs font-semibold text-slate-700 dark:text-slate-200 py-1 px-2 focus:outline-none cursor-pointer max-w-[175px]"
                >
                  {Object.entries(LANG_CONFIG).map(([lKey, lCfg]) => (
                    <option key={lKey} value={lKey} className="bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-200">{lCfg.name}</option>
                  ))}
                </select>
              </div>
            </div>
          </div>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8 max-w-6xl grow">
        <div className="bg-white dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/80 rounded-2xl p-4 md:p-6 mb-8 shadow-sm">
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div>
              <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-1.5">1. Pilih Tema</label>
              <div className="relative">
                <select value={selectedTema} onChange={handleTemaChange} className="w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-100 text-xs sm:text-sm rounded-xl py-2.5 px-3 pr-8 appearance-none focus:outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer">
                  <option value="">-- Pilih Tema --</option>
                  {temaOptions.map((opt) => <option key={opt} value={opt}>{opt}</option>)}
                </select>
                <ChevronDown className="w-4 h-4 text-slate-400 absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none" />
              </div>
            </div>
            <div>
              <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-1.5">2. Pilih Pokok Bahasan</label>
              <div className="relative">
                <select value={selectedPokok} onChange={handlePokokChange} disabled={!selectedTema} className="w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-100 text-xs sm:text-sm rounded-xl py-2.5 px-3 pr-8 appearance-none focus:outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed">
                  <option value="">-- Pilih Pokok Bahasan --</option>
                  {pokokOptions.map((opt) => <option key={opt} value={opt}>{opt}</option>)}
                </select>
                <ChevronDown className="w-4 h-4 text-slate-400 absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none" />
              </div>
            </div>
            <div>
              <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-1.5">3. Pilih Sub Bahasan</label>
              <div className="relative">
                <select value={selectedSub} onChange={handleSubChange} disabled={!selectedPokok} className="w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-100 text-xs sm:text-sm rounded-xl py-2.5 px-3 pr-8 appearance-none focus:outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed">
                  <option value="">-- Pilih Sub Bahasan --</option>
                  {subOptions.map((opt) => <option key={opt} value={opt}>{opt}</option>)}
                </select>
                <ChevronDown className="w-4 h-4 text-slate-400 absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none" />
              </div>
            </div>
          </div>
        </div>

        {selectedSub && (
          <div className="bg-white dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/80 rounded-2xl p-5 mb-8 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 shadow-sm">
            <div>
              <div className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Sub Bahasan Terpilih</div>
              <h2 className="text-xl font-bold text-slate-900 dark:text-white mt-0.5">{selectedSub}</h2>
              <div className="text-xs font-semibold text-yellow-600 dark:text-yellow-400 mt-1">{displayUraianKeys.length} Kelompok Uraian</div>
            </div>
            <button
              onClick={shareSubToWhatsApp}
              className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-700 text-white transition shadow-sm shrink-0"
              title="Bagikan Sub Bahasan ke WhatsApp"
            >
              <MessageCircle className="w-4 h-4" />
              <span>Kirim WA</span>
            </button>
          </div>
        )}

        {selectedSub && (
          <div className="flex justify-center mb-8">
            <span className="inline-flex items-center gap-1.5 px-4 py-1.5 rounded-full text-xs font-medium bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
              <RotateCw className="w-3.5 h-3.5 text-yellow-500" /><span>Klik pada kartu untuk membalik dan melihat teks Arab</span>
            </span>
          </div>
        )}

        {isLoading && (
          <div className="py-16 text-center">
            <div className="w-10 h-10 border-4 border-yellow-500/20 border-t-yellow-500 rounded-full animate-spin mx-auto mb-3" />
            <p className="text-sm text-slate-500 dark:text-slate-400">Memuat database Al-Quran Tematis...</p>
          </div>
        )}

        {!isLoading && !selectedSub && (
          <div className="py-16 text-center">
            <BookOpen className="w-12 h-12 text-yellow-500/40 mx-auto mb-4" />
            <p className="text-slate-500 dark:text-slate-400 text-sm">Silakan pilih Tema, Pokok Bahasan, dan Sub Bahasan di atas untuk melihat ayat-ayat tematik.</p>
          </div>
        )}

        {!isLoading && selectedSub && isTranslating && (
          <div className="flex justify-center mb-4">
            <span className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full text-xs font-medium bg-yellow-500/10 text-yellow-600 dark:text-yellow-400 border border-yellow-500/20">
              <span className="w-3 h-3 border-2 border-yellow-500/30 border-t-yellow-500 rounded-full animate-spin" />
              Memuat terjemahan {LANG_CONFIG[selectedLang]?.name}...
            </span>
          </div>
        )}

        {!isLoading && selectedSub && displayUraianKeys.map((uraianTitle, gIdx) => {
          const group = currentSubData[uraianTitle];
          const verses = group?.verses || [];
          const isCollapsed = collapsedGroups.has(gIdx);
          return (
            <div key={uraianTitle} className="bg-white dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/80 rounded-2xl mb-8 overflow-hidden shadow-sm hover:border-yellow-500/30 transition-colors">
              <div
                onClick={() => setCollapsedGroups((prev) => { const next = new Set(prev); if (next.has(gIdx)) next.delete(gIdx); else next.add(gIdx); return next; })}
                className="p-4 sm:p-5 bg-slate-50 dark:bg-slate-800 border-b border-slate-100 dark:border-slate-700/60 flex items-center justify-between cursor-pointer select-none"
              >
                <div className="flex items-center gap-2.5 flex-1">
                  <h3 className="text-base font-bold text-slate-900 dark:text-white">{uraianTitle}</h3>
                  <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-yellow-500/15 text-yellow-600 dark:text-yellow-400 border border-yellow-500/30">{verses.length} Ayat</span>
                </div>
                <div className="flex items-center gap-2">
                  <button onClick={(e) => { e.stopPropagation(); setCollapsedGroups((prev) => { const next = new Set(prev); if (next.has(gIdx)) next.delete(gIdx); else next.add(gIdx); return next; }); }} className="p-1 rounded-lg hover:bg-slate-200 dark:hover:bg-slate-700 transition text-slate-400">
                    {isCollapsed ? <ChevronDown className="w-4 h-4" /> : <ChevronUp className="w-4 h-4" />}
                  </button>
                </div>
              </div>
              {!isCollapsed && (
                <div className="p-4 sm:p-5 space-y-8">
                  {verses.length === 0 ? (
                    <p className="text-sm text-slate-500 dark:text-slate-400 text-center py-4">Tidak ada ayat untuk kelompok uraian ini.</p>
                  ) : verses.map((v, vIdx) => {
                    const cardKey = `g${gIdx}-v${vIdx}`;
                    const isFlipped = !!flippedCards[cardKey];
                    const playKey = `${v.surah_num}:${v.ayat_num}`;
                    const isPlaying = playingKey === playKey;

                    const vKey = `${v.surah_num}:${v.ayat_num}`;
                    // Compute display text based on selected language
                    let displayText = v.indo;
                    let isTextLoading = false;
                    if (selectedLang === "ar-SA") {
                      displayText = v.arab;
                    } else if (selectedLang !== "id-ID") {
                      if (ayahTranslations[vKey]) {
                        displayText = ayahTranslations[vKey];
                      } else if (isTranslating) {
                        isTextLoading = true;
                        displayText = "...";
                      } else {
                        displayText = v.indo; // fallback
                      }
                    }

                    return (
                      <div key={vIdx} className="space-y-4">
                        {/* Verse label row + native audio player */}
                        <div className="flex items-center justify-between gap-3 flex-wrap">
                          <div className="flex items-center gap-2 text-sm font-semibold text-yellow-600 dark:text-yellow-400">
                            <span className="w-2 h-2 rounded-full bg-yellow-500 inline-block" />
                            {v.surah_name} [{v.surah_num}]: {v.ayat_num}
                          </div>
                          {/* Native HTML5 audio — murottal Alafasy */}
                          <audio
                            controls
                            src={`https://everyayah.com/data/Alafasy_128kbps/${String(v.surah_num).padStart(3,"0")}${String(v.ayat_num).padStart(3,"0")}.mp3`}
                            className="h-8 max-w-[240px] sm:max-w-xs"
                            preload="none"
                          />
                        </div>
                        {/* Flip card */}
                        <div onClick={() => toggleCardFlip(cardKey)} className="cursor-pointer" style={{ perspective: "1000px" }}>
                          <div style={{ position: "relative", transition: "transform 0.7s cubic-bezier(0.34,1.56,0.64,1)", transformStyle: "preserve-3d", transform: isFlipped ? "rotateY(180deg)" : "rotateY(0deg)", minHeight: "180px" }}>
                            <div style={{ backfaceVisibility: "hidden", WebkitBackfaceVisibility: "hidden" }} className="absolute inset-0 flex flex-col justify-center bg-gradient-to-br from-slate-900 to-slate-800 border border-slate-700 rounded-2xl p-5 sm:p-7">
                              <div className="absolute top-3 right-3 text-xs text-slate-500 flex items-center gap-1">
                                <RotateCw className="w-3 h-3 text-yellow-500" /><span className="hidden sm:inline">Lihat Arab</span>
                              </div>
                              {isTextLoading ? (
                                <div className="flex items-center justify-center py-6">
                                  <div className="w-6 h-6 border-2 border-yellow-500/20 border-t-yellow-500 rounded-full animate-spin" />
                                </div>
                              ) : (
                                <p className={`text-sm sm:text-base leading-relaxed text-slate-100 italic text-center mb-5 ${selectedLang === "ar-SA" ? "font-arabic text-xl leading-loose" : ""}`} dir={selectedLang === "ar-SA" ? "rtl" : "ltr"}>
                                  "{displayText}"
                                </p>
                              )}
                              <div className="flex flex-wrap items-center justify-center gap-2" onClick={(e) => e.stopPropagation()}>
                                {/* TTS: baca terjemahan sesuai bahasa dipilih */}
                                <button
                                  onClick={() => handlePlayTTS(displayText, v.surah_num, v.ayat_num)}
                                  className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold transition ${
                                    isPlaying ? "bg-red-500 text-white" : "bg-yellow-500/15 hover:bg-yellow-500/25 text-yellow-400 border border-yellow-500/30"
                                  }`}
                                >
                                  <Volume2 className="w-3.5 h-3.5" /><span>{isPlaying ? "Hentikan" : "Dengarkan"}</span>
                                </button>
                                <button onClick={() => { setAiModalVerse(v); setIsAiModalOpen(true); }} className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-purple-500/15 hover:bg-purple-500/25 text-purple-400 border border-purple-500/30 transition">
                                  <Sparkles className="w-3.5 h-3.5" /><span>Tanya AI</span>
                                </button>
                                <Link to={`/qmushaf?surah=${v.surah_num}&ayah=${v.ayat_num}`} className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-sky-500/15 hover:bg-sky-500/25 text-sky-400 border border-sky-500/30 transition" onClick={(e) => e.stopPropagation()}>
                                  <BookOpen className="w-3.5 h-3.5" /><span>Mushaf Per Kata</span>
                                </Link>
                                <button onClick={() => { navigator.clipboard.writeText(`QS. ${v.surah_name} [${v.surah_num}:${v.ayat_num}]\n\n${v.arab}\n\n"${v.indo}"`); showToast("Ayat berhasil disalin!"); }} className="p-1.5 rounded-xl bg-slate-700 hover:bg-slate-600 text-slate-300 hover:text-white transition" title="Salin">
                                  <Copy className="w-3.5 h-3.5" />
                                </button>
                              </div>
                            </div>
                            <div style={{ backfaceVisibility: "hidden", WebkitBackfaceVisibility: "hidden", transform: "rotateY(180deg)", position: "absolute", inset: 0 }} className="flex flex-col items-center justify-center bg-gradient-to-br from-slate-900 to-slate-800 border border-yellow-500/40 rounded-2xl p-5 sm:p-7">
                              <div className="absolute top-3 right-3 text-xs text-slate-500 flex items-center gap-1">
                                <RotateCw className="w-3 h-3 text-yellow-500" /><span className="hidden sm:inline">Lihat Terjemah</span>
                              </div>
                              <p className={`${arabicFontClass} font-arabic leading-loose text-right text-slate-100 w-full`} dir="rtl">{v.arab}</p>
                            </div>
                          </div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          );
        })}

        {!isLoading && selectedSub && subOptions.length > 1 && (
          <div className="flex items-center justify-center gap-4 mt-8">
            <button onClick={() => { const idx = subOptions.indexOf(selectedSub); if (idx > 0) { setSelectedSub(subOptions[idx - 1]); setFlippedCards({}); stopTTS(); } }} disabled={subOptions.indexOf(selectedSub) <= 0} className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-bold bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed transition shadow-sm">
              <ChevronLeft className="w-4 h-4" /><span>Sub Bahasan Sebelum</span>
            </button>
            <button onClick={() => { const idx = subOptions.indexOf(selectedSub); if (idx < subOptions.length - 1) { setSelectedSub(subOptions[idx + 1]); setFlippedCards({}); stopTTS(); } }} disabled={subOptions.indexOf(selectedSub) >= subOptions.length - 1} className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-bold bg-yellow-500 hover:bg-yellow-400 text-slate-900 disabled:opacity-40 disabled:cursor-not-allowed transition shadow-sm">
              <span>Sub Bahasan Berikutnya</span><ChevronRight className="w-4 h-4" />
            </button>
          </div>
        )}
      </main>

      {isAiModalOpen && aiModalVerse && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm" onClick={(e) => { if (e.target === e.currentTarget) setIsAiModalOpen(false); }}>
          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-2xl max-w-xl w-full p-6 shadow-2xl relative max-h-[90vh] overflow-y-auto">
            <button onClick={() => setIsAiModalOpen(false)} className="absolute top-4 right-4 p-1.5 rounded-lg text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 bg-slate-100 dark:bg-slate-800 transition"><X className="w-4 h-4" /></button>
            <div className="flex items-center gap-2.5 mb-3">
              <div className="p-2 rounded-xl bg-purple-500/10 text-purple-600 dark:text-purple-400 border border-purple-500/20"><Sparkles className="w-5 h-5" /></div>
              <div>
                <h3 className="text-base font-bold text-slate-900 dark:text-white">Tanya AI Al-Qur'an</h3>
                <p className="text-xs text-slate-500 dark:text-slate-400">Zero Hallucination — berlandaskan nash ayat & tafsir mu'tabar.</p>
              </div>
            </div>
            <div className="bg-slate-50 dark:bg-slate-800/60 p-3 rounded-xl border border-slate-200 dark:border-slate-700 mb-4">
              <div className="text-xs font-bold text-yellow-600 dark:text-yellow-400 mb-1">QS. {aiModalVerse.surah_name} [{aiModalVerse.surah_num}:{aiModalVerse.ayat_num}]</div>
              <div className="text-xs text-slate-600 dark:text-slate-300 italic line-clamp-3">"{aiModalVerse.indo}"</div>
            </div>
            <p className="text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider mb-2">Pilih Jenis Kajian:</p>
            <div className="flex flex-wrap items-center gap-1.5 mb-4">
              {[{id:"tadabbur",label:"Tadabbur Tematis"},{id:"asbab",label:"Asbabun Nuzul Shahih"},{id:"mufradat",label:"Makna Kosakata"},{id:"custom",label:"Ajukan Pertanyaan"}].map((tab) => (
                <button key={tab.id} onClick={() => setAiMode(tab.id)} className={`px-3 py-1 rounded-full text-xs font-semibold transition ${aiMode === tab.id ? "bg-purple-600 text-white" : "bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700"}`}>{tab.label}</button>
              ))}
            </div>
            {aiMode === "custom" && (
              <div className="mb-4">
                <input type="text" value={aiCustomQuestion} onChange={(e) => setAiCustomQuestion(e.target.value)} placeholder="Tuliskan pertanyaan spesifik Anda tentang ayat ini..." className="w-full bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl p-2.5 text-xs text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-purple-500/50" />
              </div>
            )}
            <div className="mb-4">
              <label className="block text-xs font-semibold text-slate-500 dark:text-slate-400 mb-1">Format Prompt Anti-Halusinasi:</label>
              <textarea readOnly value={generateAiPrompt()} rows={5} className="w-full bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 rounded-xl p-3 text-xs font-mono text-slate-700 dark:text-slate-300 focus:outline-none resize-none" />
            </div>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
              <button onClick={() => { navigator.clipboard.writeText(generateAiPrompt()); showToast("Prompt berhasil disalin!"); }} className="inline-flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl text-xs font-bold bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 transition"><Copy className="w-3.5 h-3.5" /><span>Salin Prompt</span></button>
              <button onClick={() => openAiPlatform("chatgpt")} className="inline-flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-700 text-white transition"><ExternalLink className="w-3.5 h-3.5" /><span>ChatGPT</span></button>
              <button onClick={() => openAiPlatform("gemini")} className="inline-flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl text-xs font-bold bg-blue-600 hover:bg-blue-700 text-white transition"><ExternalLink className="w-3.5 h-3.5" /><span>Gemini</span></button>
              <button onClick={() => openAiPlatform("claude")} className="inline-flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl text-xs font-bold bg-amber-600 hover:bg-amber-700 text-white transition"><ExternalLink className="w-3.5 h-3.5" /><span>Claude</span></button>
            </div>
          </div>
        </div>
      )}

      <Footer />
    </div>
  );
};

export default QThematic;
