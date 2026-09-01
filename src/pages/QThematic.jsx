import React, { useState, useEffect, useRef, useCallback } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import { 
  Sparkles, 
  BookOpen, 
  Volume2, 
  Square, 
  Play, 
  ChevronLeft, 
  ChevronRight, 
  ChevronDown, 
  ChevronUp, 
  Bot, 
  Globe, 
  Info, 
  Layers,
  HelpCircle,
  Loader2
} from "lucide-react";

// ─── COMPLETE 39 LANGUAGES CONFIGURATION ─────────────────────────────
const LANG_CONFIG = {
  'id-ID': { code: 'id', edition: 'id.indonesian', name: 'Bahasa Indonesia', translator: 'Kemenag RI' },
  'ms-MY': { code: 'ms', edition: 'ms.basmeih', name: 'Bahasa Melayu', translator: 'Basmeih' },
  'en-US': { code: 'en', edition: 'en.sahih', name: 'English', translator: 'Saheeh International' },
  'ur-PK': { code: 'ur', edition: 'ur.jalandhry', name: 'اردو (Urdu)', translator: 'Jalandhry' },
  'bn-BD': { code: 'bn', edition: 'bn.bengali', name: 'বাংলা (Bangla)', translator: 'Muhiuddin Khan' },
  'hi-IN': { code: 'hi', edition: 'hi.hindi', name: 'हिन्दी (Hindi)', translator: 'Farooq & Nadwi' },
  'ru-RU': { code: 'ru', edition: 'ru.kuliev', name: 'Русский (Russian)', translator: 'Elmir Kuliev' },
  'zh-CN': { code: 'zh', edition: 'zh.jian', name: '中文 (Chinese)', translator: 'Ma Jian' },
  'fr-FR': { code: 'fr', edition: 'fr.hamidullah', name: 'Français (French)', translator: 'Hamidullah' },
  'es-ES': { code: 'es', edition: 'es.cortes', name: 'Español (Spanish)', translator: 'Julio Cortés' },
  'pt-PT': { code: 'pt', edition: 'pt.elhayek', name: 'Português (Portuguese)', translator: 'El-Hayek' },
  'it-IT': { code: 'it', edition: 'it.piccardo', name: 'Italiano (Italian)', translator: 'Piccardo' },
  'tr-TR': { code: 'tr', edition: 'tr.diyanet', name: 'Türkçe (Turkish)', translator: 'Diyanet' },
  'de-DE': { code: 'de', edition: 'de.bubenheim', name: 'Deutsch (German)', translator: 'Bubenheim & Elyas' },
  'ko-KR': { code: 'ko', edition: 'ko.korean', name: '한국어 (Korean)', translator: 'Hamid Choi' },
  'ja-JP': { code: 'ja', edition: 'ja.japanese', name: '日本語 (Japanese)', translator: 'Ryoichi Mita' },
  'th-TH': { code: 'th', edition: 'th.thai', name: 'ภาษาไทย (Thai)', translator: 'King Fahad Complex' },
  'ha-NG': { code: 'ha', edition: 'ha.gumi', name: 'Hausa', translator: 'Abubakar Gumi' },
  'sw-TZ': { code: 'sw', edition: 'sw.barwani', name: 'Kiswahili (Swahili)', translator: 'Ali Muhsin Al-Barwani' },
  'bs-BA': { code: 'bs', edition: 'bs.korkut', name: 'Bosanski (Bosnian)', translator: 'Besim Korkut' },
  'sq-AL': { code: 'sq', edition: 'sq.ahmeti', name: 'Shqip (Albanian)', translator: 'Sherif Ahmeti' },
  'ber-DZ': { code: 'ber', edition: 'ber.mensur', name: 'ⵜⴰⵎⴰⵣⵉⵖⵜ (Amazigh)', translator: 'At Mansour' },
  'am-ET': { code: 'am', edition: 'am.sadiq', name: 'አማርኛ (Amharic)', translator: 'Sadiq & Sani' },
  'az-AZ': { code: 'az', edition: 'az.mammadaliyev', name: 'Azərbaycan (Azerbaijani)', translator: 'Mammadaliyev' },
  'bg-BG': { code: 'bg', edition: 'bg.theophanov', name: 'Български (Bulgarian)', translator: 'Theophanov' },
  'cs-CZ': { code: 'cs', edition: 'cs.hrbek', name: 'Čeština (Czech)', translator: 'Ivan Hrbek' },
  'dv-MV': { code: 'dv', edition: 'dv.divehi', name: 'ދިވެހި (Dhivehi)', translator: 'President Office' },
  'nl-NL': { code: 'nl', edition: 'nl.siregar', name: 'Nederlands (Dutch)', translator: 'Siregar' },
  'no-NO': { code: 'no', edition: 'no.berg', name: 'Norsk (Norwegian)', translator: 'Einar Berg' },
  'pl-PL': { code: 'pl', edition: 'pl.bielawskiego', name: 'Polski (Polish)', translator: 'Bielawski' },
  'ro-RO': { code: 'ro', edition: 'ro.grigore', name: 'Română (Romanian)', translator: 'Grigore' },
  'sv-SE': { code: 'sv', edition: 'sv.bernstrom', name: 'Svenska (Swedish)', translator: 'Bernström' },
  'tg-TJ': { code: 'tg', edition: 'tg.ayati', name: 'Тоҷикӣ (Tajik)', translator: 'Ayati' },
  'ta-IN': { code: 'ta', edition: 'ta.tamil', name: 'தமிழ் (Tamil)', translator: 'Jan Trust' },
  'tt-RU': { code: 'tt', edition: 'tt.nugman', name: 'Татарча (Tatar)', translator: 'Nugman' },
  'ug-CN': { code: 'ug', edition: 'ug.saleh', name: 'ئۇيغۇرޗە (Uyghur)', translator: 'Muhammad Saleh' },
  'uz-UZ': { code: 'uz', edition: 'uz.sodik', name: 'O‘zbekcha (Uzbek)', translator: 'Sodiq' },
  'ar-SA': { code: 'ar', edition: 'ar.muyassar', name: 'العربية (Arabic)', translator: 'Tafsir Al-Muyassar' },
  'ku-IQ': { code: 'ckb', edition: 'ku.asan', name: 'کوردی (Kurdish)', translator: 'Burhan Amin' }
};

// Global translation cache for labels/headers
const globalTranslationCache = {};

// Free Google Translate API helper for labels/headers and fallback translations
const translateTextFree = async (text, targetLangCode) => {
  if (!text || targetLangCode === 'id') return text;
  const cacheKey = `${targetLangCode}:${text}`;
  if (globalTranslationCache[cacheKey]) return globalTranslationCache[cacheKey];

  try {
    let queryText = text;
    queryText = queryText.replace(/^(\d+(?:\.\d+)*)\.([^\s\d])/g, '$1. $2');
    queryText = queryText.replace(/\(Bakhil\)/gi, '(Al-Bakhil)');

    const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=id&tl=${encodeURIComponent(targetLangCode)}&dt=t&q=${encodeURIComponent(queryText)}`;
    const res = await fetch(url);
    const data = await res.json();
    let translated = data[0].map((item) => item[0]).join('');

    translated = translated
      .replace(/\bKakhil\b/gi, (match) => match === 'KAKHIL' ? 'BAKHIL' : (match === 'Kakhil' ? 'Bakhil' : 'bakhil'))
      .replace(/\(Kakhil\)/gi, (match) => match === '(KAKHIL)' ? '(BAKHIL)' : (match === '(Kakhil)' ? '(Bakhil)' : '(bakhil)'))
      .replace(/الكخيل/g, 'البخيل')
      .replace(/کاخیل/g, 'البخيل');

    globalTranslationCache[cacheKey] = translated;
    return translated;
  } catch (e) {
    console.error("Translation error:", e);
    return text;
  }
};

// Natural Compare Helper for sorting numeric titles correctly
const naturalCompare = (a, b) => {
  return (a || "").toString().localeCompare((b || "").toString(), undefined, {
    numeric: true,
    sensitivity: "base"
  });
};

const naturalSort = (arr) => [...arr].sort(naturalCompare);

// Helper to split text into chunks for TTS limits
const splitTextIntoChunks = (text, maxLen = 120) => {
  if (!text) return [];
  if (text.length <= maxLen) return [text];

  const regex = /([^.?!,;:\n\u06d4\u0964]+[.?!,;:\n\u06d4\u0964]+|[^.?!,;:\n\u06d4\u0964]+$)/g;
  const parts = text.match(regex) || [text];
  const chunks = [];
  let current = "";

  for (let part of parts) {
    part = part.trim();
    if (!part) continue;
    if ((current + " " + part).trim().length <= maxLen) {
      current = (current ? current + " " + part : part).trim();
    } else {
      if (current) chunks.push(current);
      if (part.length > maxLen) {
        const words = part.split(/\s+/);
        current = "";
        for (let w of words) {
          if ((current + " " + w).trim().length <= maxLen) {
            current = (current ? current + " " + w : w).trim();
          } else {
            if (current) chunks.push(current);
            current = w;
          }
        }
      } else {
        current = part;
      }
    }
  }
  if (current) chunks.push(current);
  return chunks;
};

// ─── VERSE CARD COMPONENT ─────────────────────────────────────────────
const VerseCard = ({ 
  verse, 
  uraianTitle, 
  selectedLang, 
  translatedText, 
  isLoadingTranslation,
  isPlaying, 
  onPlayTTS, 
  onStopTTS,
  uiLabels
}) => {
  const [isFlipped, setIsFlipped] = useState(false);
  const cfg = LANG_CONFIG[selectedLang] || LANG_CONFIG['id-ID'];

  // Determine text to show: If non-Indonesian, show translatedText or loading text
  let displayText = verse.indo;
  if (selectedLang !== 'id-ID') {
    if (translatedText) {
      displayText = translatedText;
    } else if (isLoadingTranslation) {
      displayText = uiLabels.loadingText || "Memuat terjemahan...";
    }
  }

  const handleTanyaAI = (e) => {
    e.stopPropagation();
    onStopTTS();
    const prompt = `Jelaskan singkat QS. ${verse.surah_num}:${verse.ayat_num} terkait "${uraianTitle}": "${displayText}"`;
    window.open(`https://chatgpt.com/?q=${encodeURIComponent(prompt)}`, "_blank");
  };

  const handlePlayTTSClick = (e) => {
    e.stopPropagation();
    if (isPlaying) {
      onStopTTS();
    } else {
      onPlayTTS(displayText, verse.surah_num, verse.ayat_num);
    }
  };

  return (
    <div className="verse-item-wrapper mb-8">
      {/* Header bar: Surah title + Audio element if present */}
      <div className="flex flex-wrap items-center justify-between gap-3 mb-3 px-1">
        <div className="text-sm font-bold text-yellow-600 dark:text-yellow-400 bg-yellow-50 dark:bg-yellow-950/40 px-3 py-1 rounded-full border border-yellow-200/60 dark:border-yellow-900/40">
          {verse.surah_name} [{verse.surah_num}]: {verse.ayat_num}
        </div>

        {verse.audio && (
          <audio controls className="h-8 max-w-xs rounded-full shadow-xs">
            <source src={verse.audio} type="audio/mpeg" />
          </audio>
        )}
      </div>

      {/* 3D Flip Card */}
      <div 
        className="word-scene cursor-pointer group"
        onClick={() => setIsFlipped(!isFlipped)}
      >
        <div className={`word-card relative min-h-[220px] ${isFlipped ? "is-flipped" : ""}`}>
          
          {/* FRONT FACE: Translation & Action Buttons */}
          <div className="word-card-face word-card-front absolute inset-0 p-6 flex flex-col justify-between rounded-2xl bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 shadow-sm hover:border-yellow-500 dark:hover:border-yellow-500 hover:shadow-md transition duration-300">
            <div className="text-base sm:text-lg text-gray-800 dark:text-gray-200 leading-relaxed font-medium">
              {isLoadingTranslation && selectedLang !== 'id-ID' && !translatedText ? (
                <div className="flex items-center gap-2 text-yellow-600 dark:text-yellow-400 animate-pulse font-semibold">
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span>{uiLabels.loadingText || "Memuat terjemahan..."}</span>
                </div>
              ) : (
                displayText
              )}
            </div>

            <div className="flex flex-wrap items-center justify-center gap-3 pt-4 border-t border-gray-100 dark:border-gray-800 mt-4">
              {/* TTS Button */}
              <button
                onClick={handlePlayTTSClick}
                className={`px-4 py-2 rounded-full border text-xs font-bold uppercase tracking-wider transition duration-300 flex items-center gap-2 cursor-pointer ${
                  isPlaying 
                    ? "border-red-500 text-red-500 hover:bg-red-500 hover:text-white"
                    : "border-yellow-500 text-yellow-600 dark:text-yellow-400 hover:bg-yellow-500 hover:text-white dark:hover:text-gray-900"
                }`}
                title={isPlaying ? uiLabels.stopText : uiLabels.playText}
              >
                {isPlaying ? (
                  <>
                    <Square className="w-3.5 h-3.5 animate-pulse" />
                    <span>{uiLabels.stopText || "Hentikan"}</span>
                  </>
                ) : (
                  <>
                    <Volume2 className="w-3.5 h-3.5" />
                    <span>{uiLabels.playText || "Dengarkan"}</span>
                  </>
                )}
              </button>

              {/* Tanya AI Button */}
              <button
                onClick={handleTanyaAI}
                className="px-4 py-2 rounded-full border border-purple-500/50 text-purple-600 dark:text-purple-400 bg-purple-50/50 dark:bg-purple-950/20 hover:bg-purple-500 hover:text-white text-xs font-bold uppercase tracking-wider transition duration-300 flex items-center gap-2 cursor-pointer"
                title="Tanya AI tentang ayat ini"
              >
                <Bot className="w-3.5 h-3.5" />
                <span>{uiLabels.aiText || "Tanya AI"}</span>
              </button>
            </div>
          </div>

          {/* BACK FACE: Uthmani Arabic Text */}
          <div className="word-card-face word-card-back absolute inset-0 p-6 flex items-center justify-center rounded-2xl bg-slate-50 dark:bg-zinc-950/60 border border-gray-200 dark:border-gray-800 shadow-sm hover:border-yellow-500 dark:hover:border-yellow-500 transition duration-300">
            <div className="font-arabic text-2xl sm:text-3xl text-gray-900 dark:text-white leading-loose text-center direction-rtl select-none">
              {verse.arab}
            </div>
          </div>

        </div>
      </div>
    </div>
  );
};

// ─── MAIN COMPONENT ──────────────────────────────────────────────────
const QThematic = () => {
  const [quranData, setQuranData] = useState({});
  const [isLoading, setIsLoading] = useState(true);

  // Selector state
  const [selectedTema, setSelectedTema] = useState("");
  const [selectedPokok, setSelectedPokok] = useState("");
  const [selectedSub, setSelectedSub] = useState("");
  const [selectedUraian, setSelectedUraian] = useState("");

  // Collapsed groups state
  const [collapsedGroups, setCollapsedGroups] = useState(new Set());
  const [allCollapsedMode, setAllCollapsedMode] = useState(true);

  // Multi-language state
  const [selectedLang, setSelectedLang] = useState("id-ID");
  const [ayahTranslations, setAyahTranslations] = useState({});
  const [isFetchingTranslations, setIsFetchingTranslations] = useState(false);

  // Dynamic UI Translation State
  const [uiLabels, setUiLabels] = useState({
    langLabel: 'Bahasa Terjemahan & Suara:',
    heroBadge: 'qThematic — Al-Qur’an Tematis',
    heroTitle1: 'Kandungan Al-Qur\'an',
    heroTitle2: 'Berdasarkan Tema & Pembahasan',
    heroDesc: 'Eksplorasi kandungan Al-Qur\'an secara tematis terstruktur, didukung multi-bahasa internasional, fitur pelafalan audio murottal & suara terjemahan (audible), serta pendalaman makna interaktif berbasis AI (AI explorable).',
    labels: ['1. Tema Utama', '2. Pokok Bahasan', '3. Sub Bahasan', '4. Kelompok Uraian'],
    placeholders: ['Pilih Tema', 'Pilih Pokok Bahasan', 'Pilih Sub Pokok Bahasan', 'Semua Kelompok Uraian'],
    hint: 'Ketuk kartu untuk melihat teks Arab ayat',
    prevBtn: 'Sub Tema Sebelumnya',
    nextBtn: 'Sub Tema Selanjutnya',
    showVerses: 'Buka Semua',
    hideVerses: 'Tutup Semua',
    playText: 'Dengarkan',
    stopText: 'Hentikan',
    aiText: 'Tanya AI',
    loadingText: 'Memuat terjemahan...',
    emptySelect: 'Silakan pilih kategori di atas untuk melihat ayat.'
  });

  const [subTitleTranslation, setSubTitleTranslation] = useState("");
  const [groupTitleTranslations, setGroupTitleTranslations] = useState({});
  const [optionTranslations, setOptionTranslations] = useState({});

  // Audio / TTS state
  const [playingKey, setPlayingKey] = useState(null);
  const currentAudioRef = useRef(null);
  const currentUtteranceRef = useRef(null);

  const cfg = LANG_CONFIG[selectedLang] || LANG_CONFIG['id-ID'];

  // Stop TTS Audio
  const stopTTS = useCallback(() => {
    if (window.speechSynthesis) {
      window.speechSynthesis.cancel();
    }
    if (currentAudioRef.current) {
      currentAudioRef.current.pause();
      currentAudioRef.current.currentTime = 0;
      currentAudioRef.current = null;
    }
    setPlayingKey(null);
  }, []);

  // Clean up audio on unmount or tab change
  useEffect(() => {
    stopTTS();
    return () => stopTTS();
  }, [selectedTema, selectedPokok, selectedSub, selectedUraian, selectedLang, stopTTS]);

  // Load Data on Mount
  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      try {
        const res = await fetch("/quran-thematic-new.json");
        const data = await res.json();
        setQuranData(data);

        // Auto selection of first available options if any
        const temaKeys = naturalSort(Object.keys(data));
        if (temaKeys.length > 0) {
          const firstTema = temaKeys[0];
          setSelectedTema(firstTema);
          
          const pokokKeys = naturalSort(Object.keys(data[firstTema] || {}));
          if (pokokKeys.length > 0) {
            const firstPokok = pokokKeys[0];
            setSelectedPokok(firstPokok);

            const subKeys = naturalSort(Object.keys(data[firstTema][firstPokok] || {}));
            if (subKeys.length > 0) {
              const firstSub = subKeys[0];
              setSelectedSub(firstSub);
            }
          }
        }
      } catch (error) {
        console.error("Error loading quran-thematic-new.json:", error);
      }
      setIsLoading(false);
    };

    fetchData();
  }, []);

  // Dynamic UI Labels & Static Strings Translation Effect
  useEffect(() => {
    const targetLangCode = cfg.code || 'id';

    if (selectedLang === 'id-ID') {
      setUiLabels({
        langLabel: 'Bahasa Terjemahan & Suara:',
        heroBadge: 'qThematic — Al-Qur’an Tematis',
        heroTitle1: 'Kandungan Al-Qur\'an',
        heroTitle2: 'Berdasarkan Tema & Pembahasan',
        heroDesc: 'Eksplorasi kandungan Al-Qur\'an secara tematis terstruktur, didukung multi-bahasa internasional, fitur pelafalan audio murottal & suara terjemahan (audible), serta pendalaman makna interaktif berbasis AI (AI explorable).',
        labels: ['1. Tema Utama', '2. Pokok Bahasan', '3. Sub Bahasan', '4. Kelompok Uraian'],
        placeholders: ['Pilih Tema', 'Pilih Pokok Bahasan', 'Pilih Sub Pokok Bahasan', 'Semua Kelompok Uraian'],
        hint: 'Ketuk kartu untuk melihat teks Arab ayat',
        prevBtn: 'Sub Tema Sebelumnya',
        nextBtn: 'Sub Tema Selanjutnya',
        showVerses: 'Buka Semua',
        hideVerses: 'Tutup Semua',
        playText: 'Dengarkan',
        stopText: 'Hentikan',
        aiText: 'Tanya AI',
        loadingText: 'Memuat terjemahan...',
        emptySelect: 'Silakan pilih kategori di atas untuk melihat ayat.'
      });
      return;
    }

    const translateStaticUI = async () => {
      const [
        langLabel,
        heroBadge,
        heroTitle1,
        heroTitle2,
        heroDesc,
        lbl1, lbl2, lbl3, lbl4,
        pl1, pl2, pl3, pl4,
        hint, prevBtn, nextBtn, showVerses, hideVerses, playText, stopText, aiText, loadingText, emptySelect
      ] = await Promise.all([
        translateTextFree('Bahasa Terjemahan & Suara:', targetLangCode),
        translateTextFree('qThematic — Al-Qur’an Tematis', targetLangCode),
        translateTextFree('Kandungan Al-Qur\'an', targetLangCode),
        translateTextFree('Berdasarkan Tema & Pembahasan', targetLangCode),
        translateTextFree('Eksplorasi kandungan Al-Qur\'an secara tematis terstruktur, didukung multi-bahasa internasional, fitur pelafalan audio murottal & suara terjemahan (audible), serta pendalaman makna interaktif berbasis AI (AI explorable).', targetLangCode),
        translateTextFree('1. Tema Utama', targetLangCode),
        translateTextFree('2. Pokok Bahasan', targetLangCode),
        translateTextFree('3. Sub Bahasan', targetLangCode),
        translateTextFree('4. Kelompok Uraian', targetLangCode),
        translateTextFree('Pilih Tema', targetLangCode),
        translateTextFree('Pilih Pokok Bahasan', targetLangCode),
        translateTextFree('Pilih Sub Pokok Bahasan', targetLangCode),
        translateTextFree('Semua Kelompok Uraian', targetLangCode),
        translateTextFree('Ketuk kartu untuk melihat teks Arab ayat', targetLangCode),
        translateTextFree('Sub Tema Sebelumnya', targetLangCode),
        translateTextFree('Sub Tema Selanjutnya', targetLangCode),
        translateTextFree('Buka Semua', targetLangCode),
        translateTextFree('Tutup Semua', targetLangCode),
        translateTextFree('Dengarkan', targetLangCode),
        translateTextFree('Hentikan', targetLangCode),
        translateTextFree('Tanya AI', targetLangCode),
        translateTextFree('Memuat terjemahan...', targetLangCode),
        translateTextFree('Silakan pilih kategori di atas untuk melihat ayat.', targetLangCode)
      ]);

      setUiLabels({
        langLabel,
        heroBadge,
        heroTitle1,
        heroTitle2,
        heroDesc,
        labels: [lbl1, lbl2, lbl3, lbl4],
        placeholders: [pl1, pl2, pl3, pl4],
        hint,
        prevBtn,
        nextBtn,
        showVerses,
        hideVerses,
        playText,
        stopText,
        aiText,
        loadingText,
        emptySelect
      });
    };

    translateStaticUI();
  }, [selectedLang, cfg.code]);

  // Cascading dropdown handlers
  const handleTemaChange = (e) => {
    const tema = e.target.value;
    setSelectedTema(tema);
    setSelectedPokok("");
    setSelectedSub("");
    setSelectedUraian("");
    stopTTS();

    if (tema && quranData[tema]) {
      const pokoks = naturalSort(Object.keys(quranData[tema]));
      if (pokoks.length > 0) {
        const firstPokok = pokoks[0];
        setSelectedPokok(firstPokok);
        const subs = naturalSort(Object.keys(quranData[tema][firstPokok] || {}));
        if (subs.length > 0) {
          setSelectedSub(subs[0]);
        }
      }
    }
  };

  const handlePokokChange = (e) => {
    const pokok = e.target.value;
    setSelectedPokok(pokok);
    setSelectedSub("");
    setSelectedUraian("");
    stopTTS();

    if (selectedTema && pokok && quranData[selectedTema]?.[pokok]) {
      const subs = naturalSort(Object.keys(quranData[selectedTema][pokok]));
      if (subs.length > 0) {
        setSelectedSub(subs[0]);
      }
    }
  };

  const handleSubChange = (e) => {
    const sub = e.target.value;
    setSelectedSub(sub);
    setSelectedUraian("");
    stopTTS();
  };

  const handleUraianChange = (e) => {
    setSelectedUraian(e.target.value);
    stopTTS();
  };

  // Group Accordion Toggle
  const toggleGroupCollapse = (groupIdx) => {
    setCollapsedGroups((prev) => {
      const next = new Set(prev);
      if (next.has(groupIdx)) {
        next.delete(groupIdx);
      } else {
        next.add(groupIdx);
      }
      return next;
    });
  };

  const toggleAllGroups = () => {
    if (allCollapsedMode) {
      setCollapsedGroups(new Set());
      setAllCollapsedMode(false);
    } else {
      if (selectedTema && selectedPokok && selectedSub) {
        const subData = quranData[selectedTema]?.[selectedPokok]?.[selectedSub] || {};
        const groupKeys = naturalSort(Object.keys(subData));
        setCollapsedGroups(new Set(groupKeys.map((_, i) => i)));
      }
      setAllCollapsedMode(true);
    }
  };

  // TTS Play Logic (Web Speech API / Online TTS Queue)
  const handlePlayTTS = (text, surah, ayat) => {
    stopTTS();
    const key = `${surah}:${ayat}`;
    setPlayingKey(key);

    const langCode = cfg.code || 'id';

    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      const chunks = splitTextIntoChunks(text);
      let currentChunkIdx = 0;

      const speakChunk = () => {
        if (currentChunkIdx >= chunks.length) {
          setPlayingKey(null);
          return;
        }

        const msg = new SpeechSynthesisUtterance(chunks[currentChunkIdx]);
        msg.lang = selectedLang;
        msg.rate = 0.9;
        
        msg.onend = () => {
          currentChunkIdx++;
          speakChunk();
        };

        msg.onerror = (e) => {
          console.warn("Speech synthesis chunk error:", e);
          setPlayingKey(null);
        };

        currentUtteranceRef.current = msg;
        window.speechSynthesis.speak(msg);
      };

      speakChunk();
    } else {
      // Fallback Google Translate TTS
      const url = `https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=${encodeURIComponent(langCode)}&q=${encodeURIComponent(text.slice(0, 100))}`;
      const audio = new Audio(url);
      currentAudioRef.current = audio;
      audio.onended = () => setPlayingKey(null);
      audio.onerror = () => setPlayingKey(null);
      audio.play().catch(() => setPlayingKey(null));
    }
  };

  // Derived Options lists
  const temaOptions = naturalSort(Object.keys(quranData));
  const pokokOptions = selectedTema && quranData[selectedTema] ? naturalSort(Object.keys(quranData[selectedTema])) : [];
  const subOptions = selectedTema && selectedPokok && quranData[selectedTema]?.[selectedPokok] ? naturalSort(Object.keys(quranData[selectedTema][selectedPokok])) : [];
  const uraianOptions = selectedTema && selectedPokok && selectedSub && quranData[selectedTema]?.[selectedPokok]?.[selectedSub] ? naturalSort(Object.keys(quranData[selectedTema][selectedPokok][selectedSub])) : [];

  // Derived Groups to display
  const currentSubData = (selectedTema && selectedPokok && selectedSub) ? quranData[selectedTema]?.[selectedPokok]?.[selectedSub] : null;
  
  let displayUraianKeys = [];
  if (currentSubData) {
    if (selectedUraian) {
      displayUraianKeys = [selectedUraian];
    } else {
      displayUraianKeys = naturalSort(Object.keys(currentSubData));
    }
  }

  // Fetch Non-Indonesian Verse Translations dynamically in PARALLEL with API + Fallback
  useEffect(() => {
    if (selectedLang === 'id-ID' || !selectedTema || !selectedPokok || !selectedSub) {
      setIsFetchingTranslations(false);
      return;
    }

    const edition = cfg.edition;
    const targetLangCode = cfg.code || 'en';

    const subData = quranData[selectedTema]?.[selectedPokok]?.[selectedSub] || {};
    const groupKeys = naturalSort(Object.keys(subData));
    
    let versesToFetch = [];
    groupKeys.forEach((uraianTitle) => {
      const group = subData[uraianTitle];
      if (group && group.verses) {
        group.verses.forEach((v) => {
          versesToFetch.push(v);
        });
      }
    });

    if (versesToFetch.length === 0) return;

    setIsFetchingTranslations(true);

    const fetchAllParallel = async () => {
      const results = {};
      await Promise.all(
        versesToFetch.map(async (v) => {
          const cacheKey = `${edition}:${v.surah_num}:${v.ayat_num}`;

          if (ayahTranslations[cacheKey]) {
            results[cacheKey] = ayahTranslations[cacheKey];
            return;
          }

          try {
            // 1. Try Al-Quran Cloud API
            const res = await fetch(`https://api.alquran.cloud/v1/ayah/${v.surah_num}:${v.ayat_num}/${edition}`);
            const json = await res.json();
            if (json && json.data && json.data.text) {
              results[cacheKey] = json.data.text;
              return;
            }
          } catch (e) {
            console.warn("Al-Quran Cloud API failed, trying Google Translate fallback...", e);
          }

          // 2. Fallback Google Translate API
          try {
            const fallbackText = await translateTextFree(v.indo, targetLangCode);
            if (fallbackText) {
              results[cacheKey] = fallbackText;
            }
          } catch (err) {
            console.error("Fallback translation failed:", err);
          }
        })
      );

      setAyahTranslations((prev) => ({
        ...prev,
        ...results
      }));
      setIsFetchingTranslations(false);
    };

    fetchAllParallel();
  }, [selectedLang, selectedTema, selectedPokok, selectedSub, quranData, cfg.edition, cfg.code]);

  // Translate Group Titles, Sub Header Titles & Options dynamically
  useEffect(() => {
    if (selectedLang === 'id-ID' || !selectedSub) {
      setSubTitleTranslation("");
      setGroupTitleTranslations({});
      setOptionTranslations({});
      return;
    }

    const targetLangCode = cfg.code;
    if (!targetLangCode) return;

    const translateHeaders = async () => {
      // 1. Translate Sub Title
      const subTrans = await translateTextFree(selectedSub, targetLangCode);
      setSubTitleTranslation(subTrans);

      // 2. Translate Group Titles
      if (displayUraianKeys.length > 0) {
        const groupTrans = {};
        await Promise.all(
          displayUraianKeys.map(async (key) => {
            const trans = await translateTextFree(key, targetLangCode);
            groupTrans[key] = trans;
          })
        );
        setGroupTitleTranslations(groupTrans);
      }

      // 3. Translate Dropdown Options
      const optionTrans = {};
      const allSelectOptions = [...temaOptions, ...pokokOptions, ...subOptions, ...uraianOptions];
      await Promise.all(
        allSelectOptions.map(async (opt) => {
          if (!optionTranslations[opt]) {
            const trans = await translateTextFree(opt, targetLangCode);
            optionTrans[opt] = trans;
          }
        })
      );
      setOptionTranslations((prev) => ({ ...prev, ...optionTrans }));
    };

    translateHeaders();
  }, [selectedLang, selectedSub, displayUraianKeys.join(","), cfg.code]);

  // Navigation across Sub-Themes
  const handlePrevSub = () => {
    if (!subOptions || subOptions.length === 0) return;
    const curIndex = subOptions.indexOf(selectedSub);
    if (curIndex > 0) {
      setSelectedSub(subOptions[curIndex - 1]);
      setSelectedUraian("");
      stopTTS();
    }
  };

  const handleNextSub = () => {
    if (!subOptions || subOptions.length === 0) return;
    const curIndex = subOptions.indexOf(selectedSub);
    if (curIndex < subOptions.length - 1) {
      setSelectedSub(subOptions[curIndex + 1]);
      setSelectedUraian("");
      stopTTS();
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-white dark:bg-gray-900 font-sans text-gray-800 dark:text-gray-200">
      <Navbar />

      {/* Styled 3D Flip Card animations */}
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
            <span>{uiLabels.heroBadge}</span>
          </div>

          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white leading-tight mb-6">
            {uiLabels.heroTitle1} <br />
            <span className="text-transparent bg-clip-text bg-linear-to-r from-yellow-500 to-yellow-600">
              {uiLabels.heroTitle2}
            </span>
          </h1>

          <p className="text-base sm:text-lg text-gray-600 dark:text-gray-300 mb-8 max-w-3xl mx-auto leading-relaxed">
            {uiLabels.heroDesc}
          </p>

          {/* Multi-Language Selector Dropdown with all 39 Languages */}
          <div className="mb-8 flex flex-wrap justify-center items-center gap-2">
            <Globe className="w-4 h-4 text-yellow-500" />
            <span className="text-xs font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
              {uiLabels.langLabel}
            </span>
            <select
              value={selectedLang}
              onChange={(e) => setSelectedLang(e.target.value)}
              className="px-3.5 py-2 rounded-full border border-yellow-500/50 bg-white dark:bg-gray-900 text-xs font-bold text-gray-800 dark:text-gray-200 outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer shadow-xs max-w-xs"
            >
              {Object.keys(LANG_CONFIG).map((langKey) => (
                <option key={langKey} value={langKey}>
                  {LANG_CONFIG[langKey].name} ({LANG_CONFIG[langKey].translator})
                </option>
              ))}
            </select>
          </div>

          {/* 4 Cascading Selectors Grid */}
          <div className="bg-white dark:bg-gray-900 p-6 rounded-2xl shadow-xs border border-gray-200 dark:border-gray-800 max-w-4xl mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            
            {/* 1. Tema Utama */}
            <div className="flex flex-col items-start gap-1">
              <label className="text-[11px] font-bold text-gray-400 dark:text-gray-500 uppercase tracking-wider">
                {uiLabels.labels[0]}
              </label>
              <select
                value={selectedTema}
                onChange={handleTemaChange}
                className="w-full px-3.5 py-2.5 rounded-xl border border-gray-250 dark:border-gray-800 bg-white dark:bg-gray-900 text-gray-800 dark:text-gray-200 text-sm font-semibold outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer"
              >
                <option value="">{uiLabels.placeholders[0]}</option>
                {temaOptions.map((opt) => (
                  <option key={opt} value={opt}>
                    {optionTranslations[opt] || opt}
                  </option>
                ))}
              </select>
            </div>

            {/* 2. Pokok Bahasan */}
            <div className="flex flex-col items-start gap-1">
              <label className="text-[11px] font-bold text-gray-400 dark:text-gray-500 uppercase tracking-wider">
                {uiLabels.labels[1]}
              </label>
              <select
                value={selectedPokok}
                onChange={handlePokokChange}
                disabled={!selectedTema}
                className="w-full px-3.5 py-2.5 rounded-xl border border-gray-250 dark:border-gray-800 bg-white dark:bg-gray-900 text-gray-800 dark:text-gray-200 text-sm font-semibold outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed"
              >
                <option value="">{uiLabels.placeholders[1]}</option>
                {pokokOptions.map((opt) => (
                  <option key={opt} value={opt}>
                    {optionTranslations[opt] || opt}
                  </option>
                ))}
              </select>
            </div>

            {/* 3. Sub Bahasan */}
            <div className="flex flex-col items-start gap-1">
              <label className="text-[11px] font-bold text-gray-400 dark:text-gray-500 uppercase tracking-wider">
                {uiLabels.labels[2]}
              </label>
              <select
                value={selectedSub}
                onChange={handleSubChange}
                disabled={!selectedPokok}
                className="w-full px-3.5 py-2.5 rounded-xl border border-gray-250 dark:border-gray-800 bg-white dark:bg-gray-900 text-gray-800 dark:text-gray-200 text-sm font-semibold outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed"
              >
                <option value="">{uiLabels.placeholders[2]}</option>
                {subOptions.map((opt) => (
                  <option key={opt} value={opt}>
                    {optionTranslations[opt] || opt}
                  </option>
                ))}
              </select>
            </div>

            {/* 4. Kelompok Uraian */}
            <div className="flex flex-col items-start gap-1">
              <label className="text-[11px] font-bold text-gray-400 dark:text-gray-500 uppercase tracking-wider">
                {uiLabels.labels[3]}
              </label>
              <select
                value={selectedUraian}
                onChange={handleUraianChange}
                disabled={!selectedSub}
                className="w-full px-3.5 py-2.5 rounded-xl border border-gray-250 dark:border-gray-800 bg-white dark:bg-gray-900 text-gray-800 dark:text-gray-200 text-sm font-semibold outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed"
              >
                <option value="">{uiLabels.placeholders[3]}</option>
                {uraianOptions.map((opt) => (
                  <option key={opt} value={opt}>
                    {optionTranslations[opt] || opt}
                  </option>
                ))}
              </select>
            </div>

          </div>
        </div>
      </div>

      {/* Main Content Display Area */}
      <main className="grow container mx-auto px-6 py-12">
        {isLoading ? (
          <div className="flex flex-col items-center justify-center py-24 gap-4">
            <div className="animate-spin rounded-full h-10 w-10 border-b-2 border-yellow-500" />
            <p className="text-sm font-semibold text-gray-400 dark:text-gray-500 uppercase tracking-wider animate-pulse">
              Memuat database tematis Al-Qur'an...
            </p>
          </div>
        ) : !selectedSub ? (
          <div className="max-w-md mx-auto text-center py-20 bg-gray-50 dark:bg-gray-800/40 rounded-3xl border border-gray-100 dark:border-gray-800 p-8">
            <HelpCircle className="w-12 h-12 text-yellow-500 mx-auto mb-4 opacity-70" />
            <p className="text-sm font-semibold text-gray-600 dark:text-gray-400">
              {uiLabels.emptySelect}
            </p>
          </div>
        ) : (
          <div className="max-w-4xl mx-auto flex flex-col items-center">
            
            {/* Sub-Header Banner Card */}
            <div className="w-full bg-linear-to-r from-yellow-500/10 via-white to-gray-50 dark:from-yellow-900/20 dark:via-gray-900 dark:to-gray-950 p-6 sm:p-8 rounded-3xl border border-yellow-200/50 dark:border-yellow-900/30 flex flex-col sm:flex-row items-center justify-between gap-6 mb-10 shadow-xs">
              <div className="text-center sm:text-left">
                <h2 className="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-white mb-2">
                  {subTitleTranslation || selectedSub}
                </h2>
                <p className="text-xs sm:text-sm font-semibold text-yellow-600 dark:text-yellow-400">
                  {displayUraianKeys.length} Group Cards
                </p>
              </div>

              <div className="flex items-center gap-3">
                {/* Expand / Collapse All Toggle Button */}
                <button
                  onClick={toggleAllGroups}
                  className="px-5 py-2.5 rounded-full border border-yellow-500 hover:bg-yellow-500 hover:text-white dark:hover:text-gray-900 text-yellow-600 dark:text-yellow-400 text-xs font-bold uppercase tracking-wider transition duration-300 flex items-center gap-2 cursor-pointer shadow-xs whitespace-nowrap"
                >
                  <Layers className="w-4 h-4" />
                  <span>{allCollapsedMode ? uiLabels.showVerses : uiLabels.hideVerses}</span>
                </button>
              </div>
            </div>

            {/* Hint Indicator */}
            <div className="inline-flex items-center gap-2 px-4 py-2 mb-10 bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 rounded-full text-xs font-semibold tracking-wide border border-gray-200 dark:border-gray-700">
              <Info className="w-4 h-4 text-yellow-500" />
              <span>{uiLabels.hint}</span>
            </div>

            {/* List of Uraian Group Cards */}
            <div className="w-full space-y-10 mb-12">
              {displayUraianKeys.map((uraianTitle, groupIdx) => {
                const groupData = currentSubData[uraianTitle];
                const isGroupCollapsed = collapsedGroups.has(groupIdx);
                const verseCount = groupData?.verses ? groupData.verses.length : 0;
                const translatedGroupTitle = groupTitleTranslations[uraianTitle] || uraianTitle;

                return (
                  <div
                    key={uraianTitle}
                    className="uraian-group-card bg-white dark:bg-gray-900 rounded-3xl border border-gray-200 dark:border-gray-800 overflow-hidden shadow-xs hover:border-yellow-500/50 transition duration-300"
                  >
                    {/* Header Banner */}
                    <div
                      onClick={() => toggleGroupCollapse(groupIdx)}
                      className="p-6 bg-gray-50/60 dark:bg-gray-800/40 border-b border-gray-100 dark:border-gray-800 flex items-center justify-between cursor-pointer select-none gap-4"
                      title="Klik untuk Buka / Tutup Kelompok Ini"
                    >
                      <div className="flex flex-wrap items-center gap-3">
                        <h3 className="text-lg font-bold text-gray-900 dark:text-white">
                          {translatedGroupTitle}
                        </h3>
                        <span className="inline-flex items-center gap-1.5 px-3 py-1 bg-yellow-100 dark:bg-yellow-950/40 text-yellow-800 dark:text-yellow-300 rounded-full text-xs font-semibold border border-yellow-200/50 dark:border-yellow-900/30">
                          <BookOpen className="w-3.5 h-3.5 text-yellow-500" />
                          {verseCount} Verses
                        </span>
                      </div>

                      <div className="text-gray-400 group-hover:text-yellow-500 transition duration-300">
                        {isGroupCollapsed ? (
                          <ChevronDown className="w-5 h-5" />
                        ) : (
                          <ChevronUp className="w-5 h-5" />
                        )}
                      </div>
                    </div>

                    {/* Group Body: Verses */}
                    {!isGroupCollapsed && (
                      <div className="p-6 sm:p-8">
                        {groupData.is_lihat_juga ? (
                          <div className="p-4 rounded-xl bg-blue-50 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-900/40 text-blue-700 dark:text-blue-300 text-sm font-semibold flex items-center gap-2">
                            <Info className="w-4 h-4 shrink-0" />
                            <span>Lihat juga bahasan terkait pada referensi utama.</span>
                          </div>
                        ) : !groupData.verses || groupData.verses.length === 0 ? (
                          <div className="text-center py-6 text-sm font-medium text-gray-400">
                            Tidak ada ayat untuk kelompok uraian ini.
                          </div>
                        ) : (
                          <div className="space-y-6">
                            {groupData.verses.map((verse, vIdx) => {
                              const cacheKey = `${cfg.edition}:${verse.surah_num}:${verse.ayat_num}`;
                              const translatedText = ayahTranslations[cacheKey];
                              const playKey = `${verse.surah_num}:${verse.ayat_num}`;

                              return (
                                <VerseCard
                                  key={`${verse.surah_num}-${verse.ayat_num}-${vIdx}`}
                                  verse={verse}
                                  uraianTitle={translatedGroupTitle}
                                  selectedLang={selectedLang}
                                  translatedText={translatedText}
                                  isLoadingTranslation={isFetchingTranslations && selectedLang !== 'id-ID' && !translatedText}
                                  isPlaying={playingKey === playKey}
                                  onPlayTTS={(txt, s, a) => handlePlayTTS(txt, s, a)}
                                  onStopTTS={stopTTS}
                                  uiLabels={uiLabels}
                                />
                              );
                            })}
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>

            {/* Bottom Sub-Theme Navigation Controls */}
            <div className="flex justify-center items-center gap-6 pt-6 border-t border-gray-100 dark:border-gray-800 w-full">
              <button
                onClick={handlePrevSub}
                disabled={!subOptions || subOptions.indexOf(selectedSub) <= 0}
                className="px-5 py-2.5 rounded-full border border-gray-250 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-700 dark:text-gray-300 disabled:opacity-30 disabled:cursor-not-allowed text-xs font-bold uppercase tracking-wider transition duration-300 flex items-center cursor-pointer gap-1.5"
              >
                <ChevronLeft className="w-3.5 h-3.5" />
                <span>{uiLabels.prevBtn}</span>
              </button>

              <button
                onClick={handleNextSub}
                disabled={!subOptions || subOptions.indexOf(selectedSub) >= subOptions.length - 1}
                className="px-5 py-2.5 rounded-full border border-gray-250 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-700 dark:text-gray-300 disabled:opacity-30 disabled:cursor-not-allowed text-xs font-bold uppercase tracking-wider transition duration-300 flex items-center cursor-pointer gap-1.5"
              >
                <span>{uiLabels.nextBtn}</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </button>
            </div>

          </div>
        )}
      </main>

      <Footer />
    </div>
  );
};

export default QThematic;
