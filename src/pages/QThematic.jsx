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
  "id-ID": { code: "id", name: "Bahasa Indonesia" },
  "ms-MY": { code: "ms", name: "Bahasa Melayu" },
  "en-US": { code: "en", name: "English" },
  "ur-PK": { code: "ur", name: "Urdu" },
  "bn-BD": { code: "bn", name: "Bangla" },
  "hi-IN": { code: "hi", name: "Hindi" },
  "ru-RU": { code: "ru", name: "Русский" },
  "zh-CN": { code: "zh", name: "中文" },
  "fr-FR": { code: "fr", name: "Français" },
  "es-ES": { code: "es", name: "Español" },
  "pt-PT": { code: "pt", name: "Português" },
  "it-IT": { code: "it", name: "Italiano" },
  "tr-TR": { code: "tr", name: "Türkçe" },
  "de-DE": { code: "de", name: "Deutsch" },
  "ko-KR": { code: "ko", name: "한국어" },
  "ja-JP": { code: "ja", name: "日本語" },
  "th-TH": { code: "th", name: "ภาษาไทย" },
  "ar-SA": { code: "ar", name: "العربية" },
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

// UI Dictionary for multiple languages
const UI_STRINGS = {
  id: {
    thematicBadge: "Al-Qur'an Tematis",
    thematicTitle1: "Al-Qur'an",
    thematicTitle2: "Tematis",
    thematicDesc: "Eksplorasi kandungan ayat Al-Qur'an berdasarkan tema kehidupan, dengan audio TTS multi-bahasa dan asisten AI anti-halusinasi.",
    chooseTema: "1. Pilih Tema",
    choosePokok: "2. Pilih Pokok Bahasan",
    chooseSub: "3. Pilih Sub Bahasan",
    optTema: "-- Pilih Tema --",
    optPokok: "-- Pilih Pokok Bahasan --",
    optSub: "-- Pilih Sub Bahasan --",
    selectedSubLabel: "Sub Bahasan Terpilih",
    thematicGroupsCount: (n) => `${n} Kelompok Uraian`,
    shareWA: "Kirim WA",
    flipCardTip: "Klik pada kartu untuk membalik dan melihat teks Arab",
    loadingDb: "Memuat database Al-Quran Tematis...",
    selectPrompt: "Silakan pilih Tema, Pokok Bahasan, dan Sub Bahasan di atas untuk melihat ayat-ayat tematik.",
    loadingTrans: (name) => `Memuat terjemahan ${name}...`,
    versesCount: (n) => `${n} Ayat`,
    noVerses: "Tidak ada ayat untuk kelompok uraian ini.",
    viewArab: "Lihat Arab",
    viewTrans: "Lihat Terjemah",
    listen: "Dengarkan",
    stop: "Hentikan",
    askAi: "Tanya AI",
    mushafPerKata: "Mushaf Per Kata",
    copiedVerse: "Ayat berhasil disalin!",
    prevSub: "Sub Bahasan Sebelum",
    nextSub: "Sub Bahasan Berikutnya",
    // Tanya AI Modal
    aiModalTitle: "Tanya AI Al-Qur'an",
    aiModalSubtitle: "Zero Hallucination — berlandaskan nash ayat & tafsir mu'tabar.",
    aiSelectMode: "Pilih Jenis Kajian:",
    aiTabTadabbur: "Tadabbur Tematis",
    aiTabAsbab: "Asbabun Nuzul Shahih",
    aiTabMufradat: "Makna Kosakata",
    aiTabCustom: "Ajukan Pertanyaan",
    aiInputPlaceholder: "Tuliskan pertanyaan spesifik Anda tentang ayat ini...",
    aiPromptLabel: "Format Prompt Anti-Halusinasi:",
    aiCopyPrompt: "Salin Prompt",
    aiPromptCopied: "Prompt berhasil disalin!",
  },
  en: {
    thematicBadge: "Thematic Quran",
    thematicTitle1: "Thematic",
    thematicTitle2: "Quran",
    thematicDesc: "Explore Quranic verses classified by life themes, with multi-lingual audio and a zero-hallucination AI assistant.",
    chooseTema: "1. Select Theme",
    choosePokok: "2. Select Main Subject",
    chooseSub: "3. Select Sub-topic",
    optTema: "-- Select Theme --",
    optPokok: "-- Select Main Subject --",
    optSub: "-- Select Sub-topic --",
    selectedSubLabel: "Selected Sub-topic",
    thematicGroupsCount: (n) => `${n} Thematic Groups`,
    shareWA: "Share WA",
    flipCardTip: "Click card to flip and view Arabic text",
    loadingDb: "Loading Thematic Quran database...",
    selectPrompt: "Please select Theme, Main Subject, and Sub-topic above to view thematic verses.",
    loadingTrans: (name) => `Loading ${name} translation...`,
    versesCount: (n) => `${n} Verses`,
    noVerses: "No verses available for this topic.",
    viewArab: "View Arabic",
    viewTrans: "View Translation",
    listen: "Listen",
    stop: "Stop",
    askAi: "Ask AI",
    mushafPerKata: "Word by Word",
    copiedVerse: "Verse copied to clipboard!",
    prevSub: "Previous Sub-topic",
    nextSub: "Next Sub-topic",
    // Tanya AI Modal
    aiModalTitle: "Ask Quran AI",
    aiModalSubtitle: "Zero Hallucination — grounded in authentic verses & recognized classical Tafsir.",
    aiSelectMode: "Select Study Mode:",
    aiTabTadabbur: "Thematic Reflection",
    aiTabAsbab: "Authentic Asbabun Nuzul",
    aiTabMufradat: "Vocabulary & Mufradat",
    aiTabCustom: "Ask Custom Question",
    aiInputPlaceholder: "Type your specific question about this verse...",
    aiPromptLabel: "Anti-Hallucination Prompt Format:",
    aiCopyPrompt: "Copy Prompt",
    aiPromptCopied: "Prompt copied successfully!",
  },
  es: {
    thematicBadge: "Corán Temático",
    thematicTitle1: "Corán",
    thematicTitle2: "Temático",
    thematicDesc: "Explore los versículos del Corán clasificados por temas de la vida, con audio multilingüe y asistente de IA sin alucinaciones.",
    chooseTema: "1. Seleccionar Tema",
    choosePokok: "2. Seleccionar Tema Principal",
    chooseSub: "3. Seleccionar Subtema",
    optTema: "-- Seleccionar Tema --",
    optPokok: "-- Seleccionar Tema Principal --",
    optSub: "-- Seleccionar Subtema --",
    selectedSubLabel: "Subtema Seleccionado",
    thematicGroupsCount: (n) => `${n} Grupos Temáticos`,
    shareWA: "Compartir WA",
    flipCardTip: "Haga clic en la tarjeta para voltear y ver el texto en árabe",
    loadingDb: "Cargando base de datos del Corán Temático...",
    selectPrompt: "Seleccione Tema, Asunto y Subtema arriba para ver los versículos temáticos.",
    loadingTrans: (name) => `Cargando traducción al ${name}...`,
    versesCount: (n) => `${n} Versículos`,
    noVerses: "No hay versículos disponibles para este grupo.",
    viewArab: "Ver Árabe",
    viewTrans: "Ver Traducción",
    listen: "Escuchar",
    stop: "Detener",
    askAi: "Preguntar a IA",
    mushafPerKata: "Palabra por Palabra",
    copiedVerse: "¡Versículo copiado al portapapeles!",
    prevSub: "Subtema Anterior",
    nextSub: "Siguiente Subtema",
    // Tanya AI Modal
    aiModalTitle: "Preguntar a la IA del Corán",
    aiModalSubtitle: "Cero Alucinaciones — fundamentado en versículos auténticos y exégesis reconocida.",
    aiSelectMode: "Seleccionar Tipo de Estudio:",
    aiTabTadabbur: "Reflexión Temática",
    aiTabAsbab: "Asbab al-Nuzul Auténtico",
    aiTabMufradat: "Significado del Vocabulario",
    aiTabCustom: "Hacer Pregunta",
    aiInputPlaceholder: "Escriba su pregunta específica sobre este versículo...",
    aiPromptLabel: "Formato de Prompt Anti-Alucinación:",
    aiCopyPrompt: "Copiar Prompt",
    aiPromptCopied: "¡Prompt copiado con éxito!",
  },
  ar: {
    thematicBadge: "القرآن الموضوعي",
    thematicTitle1: "القرآن",
    thematicTitle2: "الموضوعي",
    thematicDesc: "استكشف آيات القرآن الكريم مصنفة حسب موضوعات الحياة، مع تلاوة صوتية ومساعد ذكاء اصطناعي موثوق.",
    chooseTema: "١. اختر الموضوع",
    choosePokok: "٢. اختر المحور الأساسي",
    chooseSub: "٣. اختر المحور الفرعي",
    optTema: "-- اختر الموضوع --",
    optPokok: "-- اختر المحور الأساسي --",
    optSub: "-- اختر المحور الفرعي --",
    selectedSubLabel: "المحور الفرعي المختار",
    thematicGroupsCount: (n) => `${n} مجموعات موضوعية`,
    shareWA: "مشاركة واتساب",
    flipCardTip: "اضغط على البطاقة للقلب ومشاهدة النص القرآني",
    loadingDb: "جاري تحميل قاعدة بيانات القرآن الموضوعي...",
    selectPrompt: "يرجى اختيار الموضوع والمحور الأساسي والفرعي أعلاه لعرض الآيات.",
    loadingTrans: (name) => `جاري تحميل ${name}...`,
    versesCount: (n) => `${n} آيات`,
    noVerses: "لا توجد آيات لهذا الموضوع حالياً.",
    viewArab: "عرض النص العربي",
    viewTrans: "عرض الترجمة",
    listen: "استماع",
    stop: "إيقاف",
    askAi: "سؤال الذكاء الاصطناعي",
    mushafPerKata: "مصحف كلمة بكلمة",
    copiedVerse: "تم نسخ الآية بنجاح!",
    prevSub: "المحور السابق",
    nextSub: "المحور التالي",
    // Tanya AI Modal
    aiModalTitle: "سؤال الذكاء الاصطناعي القرآني",
    aiModalSubtitle: "خالٍ من الهلوسة — مستند إلى نصوص الآيات وتفاسير أهل العلم المعتبرة.",
    aiSelectMode: "اختر نوع الدراسة:",
    aiTabTadabbur: "التدبر الموضوعي",
    aiTabAsbab: "أسباب النزول الصحيحة",
    aiTabMufradat: "معاني المفردات",
    aiTabCustom: "طرح سؤال مخصص",
    aiInputPlaceholder: "اكتب سؤالك الخاص حول هذه الآية الكريمة...",
    aiPromptLabel: "صيغة السؤال الموجه للذكاء الاصطناعي:",
    aiCopyPrompt: "نسخ السؤال",
    aiPromptCopied: "تم نسخ النص بنجاح!",
  },
  ms: {
    thematicBadge: "Al-Quran Tematik",
    thematicTitle1: "Al-Qur'an",
    thematicTitle2: "Tematik",
    thematicDesc: "Eksplorasi kandungan ayat Al-Quran berdasarkan tema kehidupan, dengan audio TTS pelbagai bahasa dan pembantu AI bebas halusinasi.",
    chooseTema: "1. Pilih Tema",
    choosePokok: "2. Pilih Pokok Bahasan",
    chooseSub: "3. Pilih Sub Bahasan",
    optTema: "-- Pilih Tema --",
    optPokok: "-- Pilih Pokok Bahasan --",
    optSub: "-- Pilih Sub Bahasan --",
    selectedSubLabel: "Sub Bahasan Terpilih",
    thematicGroupsCount: (n) => `${n} Kumpulan Huraian`,
    shareWA: "Kirim WA",
    flipCardTip: "Klik pada kad untuk membalik dan melihat teks Arab",
    loadingDb: "Memuatkan pangkalan data Al-Quran Tematik...",
    selectPrompt: "Sila pilih Tema, Pokok Bahasan, dan Sub Bahasan di atas untuk melihat ayat-ayat tematik.",
    loadingTrans: (name) => `Memuatkan terjemahan ${name}...`,
    versesCount: (n) => `${n} Ayat`,
    noVerses: "Tiada ayat untuk kumpulan huraian ini.",
    viewArab: "Lihat Arab",
    viewTrans: "Lihat Terjemahan",
    listen: "Dengarkan",
    stop: "Hentikan",
    askAi: "Tanya AI",
    mushafPerKata: "Mushaf Per Kata",
    copiedVerse: "Ayat berjaya disalin!",
    prevSub: "Sub Bahasan Sebelum",
    nextSub: "Sub Bahasan Berikutnya",
    // Tanya AI Modal
    aiModalTitle: "Tanya AI Al-Qur'an",
    aiModalSubtitle: "Zero Hallucination — berlandaskan nash ayat & tafsir mu'tabar.",
    aiSelectMode: "Pilih Jenis Kajian:",
    aiTabTadabbur: "Tadabbur Tematik",
    aiTabAsbab: "Asbabun Nuzul Sahih",
    aiTabMufradat: "Makna Kosakata",
    aiTabCustom: "Ajukan Soalan",
    aiInputPlaceholder: "Tuliskan soalan khusus anda mengenai ayat ini...",
    aiPromptLabel: "Format Prompt Anti-Halusinasi:",
    aiCopyPrompt: "Salin Prompt",
    aiPromptCopied: "Prompt berjaya disalin!",
  },
  fr: {
    thematicBadge: "Coran Thématique",
    thematicTitle1: "Coran",
    thematicTitle2: "Thématique",
    thematicDesc: "Explorez les versets du Coran classés par thèmes de vie, avec audio multilingue et assistant IA sans hallucination.",
    chooseTema: "1. Choisir le thème",
    choosePokok: "2. Choisir le sujet principal",
    chooseSub: "3. Choisir le sous-thème",
    optTema: "-- Choisir le thème --",
    optPokok: "-- Choisir le sujet principal --",
    optSub: "-- Choisir le sous-thème --",
    selectedSubLabel: "Sous-thème sélectionné",
    thematicGroupsCount: (n) => `${n} Groupes thématiques`,
    shareWA: "Partager sur WA",
    flipCardTip: "Cliquez sur la carte pour retourner et voir le texte arabe",
    loadingDb: "Chargement de la base de données...",
    selectPrompt: "Veuillez sélectionner un thème, sujet et sous-thème ci-dessus.",
    loadingTrans: (name) => `Chargement de la traduction en ${name}...`,
    versesCount: (n) => `${n} Versets`,
    noVerses: "Aucun verset disponible pour ce thème.",
    viewArab: "Voir en Arabe",
    viewTrans: "Voir la traduction",
    listen: "Écouter",
    stop: "Arrêter",
    askAi: "Demander à l'IA",
    mushafPerKata: "Mot à Mot",
    copiedVerse: "Verset copié !",
    prevSub: "Sous-thème précédent",
    nextSub: "Sous-thème suivant",
    // Tanya AI Modal
    aiModalTitle: "Demander à l'IA du Coran",
    aiModalSubtitle: "Zéro Hallucination — fondé sur les versets authentiques et le Tafsir reconnu.",
    aiSelectMode: "Choisir le mode d'étude :",
    aiTabTadabbur: "Réflexion Thématique",
    aiTabAsbab: "Asbab an-Nuzul Authentique",
    aiTabMufradat: "Vocabulaire et Mufradat",
    aiTabCustom: "Poser une question",
    aiInputPlaceholder: "Écrivez votre question spécifique sur ce verset...",
    aiPromptLabel: "Format du prompt anti-hallucination :",
    aiCopyPrompt: "Copier le prompt",
    aiPromptCopied: "Prompt copié avec succès !",
  }
};

// Module-level cache: "edition:surah:ayat" -> text
const translationCache = {};

// Local storage persistent cache for translated thematic titles (Tema, Pokok, Sub, Uraian)
const TITLE_CACHE_STORAGE_KEY = "thematic_title_translations_v2";
const getSavedTitleCache = () => {
  try {
    const raw = localStorage.getItem(TITLE_CACHE_STORAGE_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch (e) {
    return {};
  }
};
const dynamicTitleCache = getSavedTitleCache();
const saveTitleCache = () => {
  try {
    localStorage.setItem(TITLE_CACHE_STORAGE_KEY, JSON.stringify(dynamicTitleCache));
  } catch (e) {}
};

async function translateTextFree(text, targetLangCode) {
  if (!text || targetLangCode === "id" || targetLangCode === "id-ID") return text;
  const lang = targetLangCode.split("-")[0];
  const cacheKey = `${lang}:${text.trim()}`;
  if (dynamicTitleCache[cacheKey]) return dynamicTitleCache[cacheKey];

  // Separate numbering prefix (e.g., "14.1.1.1. " or "1. ")
  const prefixMatch = text.match(/^([\d.]+\s*)(.*)$/);
  const prefix = prefixMatch ? prefixMatch[1] : "";
  const queryText = prefixMatch ? prefixMatch[2].trim() : text.trim();
  if (!queryText) return text;

  let translated = null;

  // Google Translate official dict-chrome-ex client endpoint (free, robust, reliable)
  try {
    const url = `https://translate.googleapis.com/translate_a/single?client=dict-chrome-ex&sl=id&tl=${lang}&dt=t&q=${encodeURIComponent(queryText)}`;
    const res = await fetch(url);
    const textResp = await res.text();
    if (textResp && textResp.startsWith("[")) {
      const data = JSON.parse(textResp);
      if (data && data[0] && Array.isArray(data[0])) {
        translated = data[0].map((item) => item[0]).join("");
      }
    }
  } catch (e) {
    // silently catch
  }

  // Fallback to MyMemory if Google fails
  if (!translated) {
    try {
      const mmUrl = `https://api.mymemory.translated.net/get?q=${encodeURIComponent(queryText)}&langpair=id|${lang}`;
      const res = await fetch(mmUrl);
      const data = await res.json();
      if (data?.responseData?.translatedText && !data.responseData.translatedText.toLowerCase().includes("quota")) {
        let mmText = data.responseData.translatedText;
        mmText = mmText.replace(/&#39;/g, "'").replace(/&quot;/g, '"').replace(/&amp;/g, "&");
        translated = mmText;
      }
    } catch (err) {}
  }

  if (translated) {
    const finalResult = prefix + translated;
    dynamicTitleCache[cacheKey] = finalResult;
    saveTitleCache();
    return finalResult;
  }

  return text;
}

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
  const currentUtteranceRef = useRef(null);
  const [flippedCards, setFlippedCards] = useState({});
  const [isAiModalOpen, setIsAiModalOpen] = useState(false);
  const [aiModalVerse, setAiModalVerse] = useState(null);
  const [aiMode, setAiMode] = useState("tadabbur");
  const [aiCustomQuestion, setAiCustomQuestion] = useState("");
  const [selectedLang, setSelectedLang] = useState(getInitialLanguage);
  const [ayahTranslations, setAyahTranslations] = useState({});
  const [isTranslating, setIsTranslating] = useState(false);
  const [translatedTitles, setTranslatedTitles] = useState({});
  const [toastMessage, setToastMessage] = useState(null);

  const showToast = (msg) => { setToastMessage(msg); setTimeout(() => setToastMessage(null), 3000); };

  const currentLangCode = selectedLang.split("-")[0];
  const t = useCallback((key) => {
    return UI_STRINGS[currentLangCode]?.[key] || UI_STRINGS.en?.[key] || UI_STRINGS.id?.[key] || key;
  }, [currentLangCode]);

  const getDisplayTitle = useCallback((title) => {
    if (!title || currentLangCode === "id") return title;
    return translatedTitles[title] || dynamicTitleCache[`${currentLangCode}:${title.trim()}`] || title;
  }, [currentLangCode, translatedTitles]);

  const stopTTS = useCallback(() => {
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    setPlayingKey(null);
  }, []);

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

  const temaOptions = naturalSort(Object.keys(quranData));
  const pokokOptions = selectedTema && quranData[selectedTema] ? naturalSort(Object.keys(quranData[selectedTema])) : [];
  const subOptions = selectedTema && selectedPokok && quranData[selectedTema]?.[selectedPokok]
    ? naturalSort(Object.keys(quranData[selectedTema][selectedPokok])) : [];
  const currentSubData = selectedTema && selectedPokok && selectedSub
    ? quranData[selectedTema]?.[selectedPokok]?.[selectedSub] : null;
  const displayUraianKeys = currentSubData ? naturalSort(Object.keys(currentSubData)) : [];

  // Translate thematic hierarchy titles when non-ID language selected
  useEffect(() => {
    if (currentLangCode === "id") {
      setTranslatedTitles({});
      return;
    }

    const titlesToTranslate = new Set();
    temaOptions.forEach((t) => titlesToTranslate.add(t));
    pokokOptions.forEach((p) => titlesToTranslate.add(p));
    subOptions.forEach((s) => titlesToTranslate.add(s));
    displayUraianKeys.forEach((u) => titlesToTranslate.add(u));
    if (selectedSub) titlesToTranslate.add(selectedSub);

    const list = Array.from(titlesToTranslate).filter(Boolean);
    if (list.length === 0) return;

    let isCancelled = false;

    const runTranslation = async () => {
      const updates = {};
      for (const item of list) {
        if (isCancelled) break;
        const trans = await translateTextFree(item, currentLangCode);
        if (trans && trans !== item) {
          updates[item] = trans;
        }
      }
      if (!isCancelled && Object.keys(updates).length > 0) {
        setTranslatedTitles((prev) => ({ ...prev, ...updates }));
      }
    };

    runTranslation();

    return () => {
      isCancelled = true;
    };
  }, [currentLangCode, selectedTema, selectedPokok, selectedSub, temaOptions.length, pokokOptions.length, subOptions.length, displayUraianKeys.length]);

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
    const text = `*${t("thematicBadge").toUpperCase()} - e-Furqan*\n\n*${t("chooseTema")}:* ${getDisplayTitle(selectedTema)}\n*${t("choosePokok")}:* ${getDisplayTitle(selectedPokok)}\n*${t("chooseSub")}:* ${getDisplayTitle(selectedSub)}\n*Total:* ${t("thematicGroupsCount")(displayUraianKeys.length)}\n\n${link}`;
    window.location.href = `https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`;
  };

  const getVerseActiveTranslation = (v) => {
    if (!v) return "";
    if (selectedLang === "ar-SA") return v.arab;
    const vKey = `${v.surah_num}:${v.ayat_num}`;
    return ayahTranslations[vKey] || v.indo;
  };

  const generateAiPrompt = () => {
    if (!aiModalVerse) return "";
    const { surah_num: s, ayat_num: a, surah_name: sName, arab, indo } = aiModalVerse;
    const langName = LANG_CONFIG[selectedLang]?.name || "Bahasa Indonesia";
    const activeTranslation = getVerseActiveTranslation(aiModalVerse);
    const langCode = currentLangCode;

    if (langCode === "id") {
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
    } else if (langCode === "es") {
      let modeInstruction = "";
      if (aiMode === "tadabbur") modeInstruction = "ENFOQUE DEL ESTUDIO: Reflexión Temática y Lecciones de Vida\nExplique la sabiduría, reflexión espiritual (tadabbur) y lecciones prácticas de este versículo.";
      else if (aiMode === "asbab") modeInstruction = "ENFOQUE DEL ESTUDIO: Asbab al-Nuzul Auténtico (Causas de la Revelación)\nMencione la causa de la revelación de este versículo ÚNICAMENTE si proviene de narraciones auténticas (sahih/hasan).";
      else if (aiMode === "mufradat") modeInstruction = "ENFOQUE DEL ESTUDIO: Análisis Lingüístico y Vocabulario (Mufradat)\nAnalice el vocabulario clave morfológicamente y explique la elocuencia retórica coránica (balaghah).";
      else if (aiMode === "custom") modeInstruction = `PREGUNTA DEL USUARIO:\n"${aiCustomQuestion}"\nResponda la pregunta anterior basándose estrictamente en las pruebas del versículo y la exégesis autorizada.`;

      return `[SISTEMA CORÁNICO DE INTEGRIDAD ACADÉMICA - PROTOCOLO CERO ALUCINACIONES]
Usted es un asistente académico confiable del Sagrado Corán, libre de alucinaciones.

DATOS OFICIALES DE REFERENCIA:
- Sura y Versículo: Sura ${sName} [${s}] : Versículo ${a}
- Texto Árabe Original: ${arab}
- Traducción Oficial (${langName}): "${activeTranslation}"

REGLAS ESTRICTAS:
1. Todas las respuestas DEBEN basarse rigurosamente en el texto del versículo, hadices auténticos (sahih) y exégesis clásicas reconocidas (Ibn Kazir, At-Tabari, Al-Qurtubi, etc.).
2. QUEDA ESTRICTAMENTE PROHIBIDO inventar narraciones, causas ficticias de revelación o cadenas de transmisión falsas.
3. Si no existe una narración auténtica registrada, declare: "No existe una narración auténtica registrada, y Alá sabe más (Allahu a'lam)".
4. REQUISITO DE IDIOMA: Responda absolutamente TODO en idioma Español (${langName}).

${modeInstruction}`;
    } else if (langCode === "ar") {
      let modeInstruction = "";
      if (aiMode === "tadabbur") modeInstruction = "محور الدراسة: التدبر الموضوعي والدروس المستفادة\nاشرح الحكم والتدبرات والدروس العملية المستخلصة من هذه الآية الكريمة.";
      else if (aiMode === "asbab") modeInstruction = "محور الدراسة: أسباب النزول الصحيحة\nاذكر سبب نزول هذه الآية الكريمة فقط إذا ثبت بروايات صحيحة أو حسنة.";
      else if (aiMode === "mufradat") modeInstruction = "محور الدراسة: التحليل اللغوي والمفردات\nحلل المفردات الرئيسية صرفياً ولغوياً وبيّن اللطائف البلاغية.";
      else if (aiMode === "custom") modeInstruction = `سؤال المستخدم:\n"${aiCustomQuestion}"\nأجب عن السؤال بناءً على نص الآية وأقوال المفسرين المعتمدين.`;

      return `[نظام القرآن الكريم الأكاديمي - بروتوكول منع الهلوسة]
أنت مساعد قرآني موثوق وخالٍ تماماً من الهلوسة.

بيانات المرجع المعتمدة:
- السورة والآية: سورة ${sName} [${s}] : الآية ${a}
- النص القرآني الكريم: ${arab}

قواعد صارمة:
1. يجب أن تستند جميع الإجابات حصراً إلى نص الآية، والأحاديث الصحيحة المعتمدة، وتفاسير أهل العلم المعتبرة (ابن كثير، الطبري، القرطبي، إلخ).
2. يمنع منعاً باتاً اختلاق الروايات أو أسباب النزول أو الأسانيد الواهية.
3. إذا لم يرد سبب نزول صحيح، قل بوضوح: "لم يثبت في ذلك رواية صحيحة، والله أعلم".
4. شرط اللغة: أجب كاملاً باللغة العربية الفصحى.

${modeInstruction}`;
    } else if (langCode === "ms") {
      let modeInstruction = "";
      if (aiMode === "tadabbur") modeInstruction = "FOKUS KAJIAN: Tadabbur Tematik & Pengajaran Hidup\nJelaskan hikmah, tadabbur, dan pengajaran praktikal daripada ayat ini.";
      else if (aiMode === "asbab") modeInstruction = "FOKUS KAJIAN: Asbabun Nuzul Sahih\nSebutkan sebab turunnya ayat ini HANYA jika bersumber daripada riwayat sahih/hasan.";
      else if (aiMode === "mufradat") modeInstruction = "FOKUS KAJIAN: Analisis Tatabahasa & Kosa Kata\nTerangkan kosa kata kunci secara morfologi dan keindahan balaghah al-Quran.";
      else if (aiMode === "custom") modeInstruction = `SOALAN PENGGUNA:\n"${aiCustomQuestion}"\nJawab soalan di atas berdasarkan dalil nas ayat dan tafsir muktabar.`;

      return `[SISTEM AL-QURAN BERINTEGRITI ILMIAH - PROTOKOL ZERO HALLUCINATION]
Anda ialah pembantu Al-Quran berwibawa yang bebas daripada halusinasi.

DATA RUJUKAN RASMI:
- Surah & Ayat: Surah ${sName} [${s}] : Ayat ${a}
- Teks Arab Asal: ${arab}
- Terjemahan Rasmi: "${activeTranslation}"

PERATURAN KETAT:
1. Semua jawapan WAJIB bersumber daripada nas ayat, hadis sahih muktabar, dan tafsir muktabar (Ibnu Kathir, At-Tabari, Al-Qurtubi, dsb).
2. DILARANG mereka-reka riwayat, asbabun nuzul palsu, atau sanad rekaan.
3. Jika tiada riwayat sahih, nyatakan: "Tiada riwayat sahih direkodkan, Wallahu a'lam".
4. SYARAT BAHASA: Berikan keseluruhan jawapan dan huraian dalam Bahasa Melayu.

${modeInstruction}`;
    } else {
      // English / International Standard
      let modeInstruction = "";
      if (aiMode === "tadabbur") modeInstruction = "FOCUS OF STUDY: Thematic Reflection & Practical Lessons\nExplain the wisdom, spiritual contemplation (tadabbur), and practical life lessons of this verse.";
      else if (aiMode === "asbab") modeInstruction = "FOCUS OF STUDY: Authentic Asbab al-Nuzul (Occasions of Revelation)\nState the occasion of revelation ONLY if verified by authentic (sahih/hasan) narrations.";
      else if (aiMode === "mufradat") modeInstruction = "FOCUS OF STUDY: Linguistic & Vocabulary Analysis (Mufradat)\nBreak down key vocabulary morphologically and explain Quranic rhetorical beauty (balaghah).";
      else if (aiMode === "custom") modeInstruction = `USER QUESTION:\n"${aiCustomQuestion}"\nAnswer the question strictly based on Quranic evidence and recognized classical Tafsir.`;

      return `[ACADEMIC QURANIC SYSTEM - ZERO HALLUCINATION PROTOCOL]
You are a trusted Quranic scholarly assistant with zero hallucination.

OFFICIAL REFERENCE DATA:
- Surah & Ayah: Surah ${sName} [${s}] : Ayah ${a}
- Original Arabic Text: ${arab}
- Official Translation (${langName}): "${activeTranslation}"

STRICT RULES:
1. All answers MUST be strictly derived from authentic Quranic text, Sahih Hadiths, and recognized classical exegesis (Ibn Kathir, At-Tabari, Al-Qurtubi, etc.).
2. STRICTLY FORBIDDEN to fabricate narrations, unverified causes of revelation, or false chains of transmission.
3. If no authentic narration exists, explicitly state: "No authentic narration is recorded, Allah knows best."
4. LANGUAGE REQUIREMENT: Deliver the entire analysis and response strictly in ${langName} (${selectedLang}).

${modeInstruction}`;
    }
  };

  const openAiPlatform = (platform) => {
    const prompt = generateAiPrompt();
    if (platform === "gemini") {
      navigator.clipboard.writeText(prompt).catch(() => {});
      showToast(`${t("aiPromptCopied")} Opening Gemini...`);
      setTimeout(() => window.open("https://gemini.google.com/app", "_blank"), 400);
    } else if (platform === "chatgpt") {
      window.open(`https://chatgpt.com/?q=${encodeURIComponent(prompt)}`, "_blank");
    } else if (platform === "claude") {
      navigator.clipboard.writeText(prompt).catch(() => {});
      showToast(`${t("aiPromptCopied")} Opening Claude...`);
      setTimeout(() => window.open("https://claude.ai/new", "_blank"), 400);
    }
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
                <BookOpen className="w-3.5 h-3.5" /><span>{t("thematicBadge")}</span>
              </div>
              <h1 className="text-2xl md:text-3xl font-bold tracking-tight text-slate-900 dark:text-white">
                {t("thematicTitle1")} <span className="text-yellow-500">{t("thematicTitle2")}</span>
              </h1>
              <p className="text-sm text-slate-500 dark:text-slate-400 mt-1 max-w-xl">
                {t("thematicDesc")}
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
              <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-1.5">{t("chooseTema")}</label>
              <div className="relative">
                <select value={selectedTema} onChange={handleTemaChange} className="w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-100 text-xs sm:text-sm rounded-xl py-2.5 px-3 pr-8 appearance-none focus:outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer">
                  <option value="">{t("optTema")}</option>
                  {temaOptions.map((opt) => <option key={opt} value={opt}>{getDisplayTitle(opt)}</option>)}
                </select>
                <ChevronDown className="w-4 h-4 text-slate-400 absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none" />
              </div>
            </div>
            <div>
              <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-1.5">{t("choosePokok")}</label>
              <div className="relative">
                <select value={selectedPokok} onChange={handlePokokChange} disabled={!selectedTema} className="w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-100 text-xs sm:text-sm rounded-xl py-2.5 px-3 pr-8 appearance-none focus:outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed">
                  <option value="">{t("optPokok")}</option>
                  {pokokOptions.map((opt) => <option key={opt} value={opt}>{getDisplayTitle(opt)}</option>)}
                </select>
                <ChevronDown className="w-4 h-4 text-slate-400 absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none" />
              </div>
            </div>
            <div>
              <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-1.5">{t("chooseSub")}</label>
              <div className="relative">
                <select value={selectedSub} onChange={handleSubChange} disabled={!selectedPokok} className="w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-100 text-xs sm:text-sm rounded-xl py-2.5 px-3 pr-8 appearance-none focus:outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed">
                  <option value="">{t("optSub")}</option>
                  {subOptions.map((opt) => <option key={opt} value={opt}>{getDisplayTitle(opt)}</option>)}
                </select>
                <ChevronDown className="w-4 h-4 text-slate-400 absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none" />
              </div>
            </div>
          </div>
        </div>

        {selectedSub && (
          <div className="bg-white dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/80 rounded-2xl p-5 mb-8 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 shadow-sm">
            <div>
              <div className="text-xs font-semibold text-slate-400 uppercase tracking-wider">{t("selectedSubLabel")}</div>
              <h2 className="text-xl font-bold text-slate-900 dark:text-white mt-0.5">{getDisplayTitle(selectedSub)}</h2>
              <div className="text-xs font-semibold text-yellow-600 dark:text-yellow-400 mt-1">{t("thematicGroupsCount")(displayUraianKeys.length)}</div>
            </div>
            <button
              onClick={shareSubToWhatsApp}
              className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-700 text-white transition shadow-sm shrink-0"
              title="WhatsApp"
            >
              <MessageCircle className="w-4 h-4" />
              <span>{t("shareWA")}</span>
            </button>
          </div>
        )}

        {selectedSub && (
          <div className="flex justify-center mb-8">
            <span className="inline-flex items-center gap-1.5 px-4 py-1.5 rounded-full text-xs font-medium bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700 text-center">
              <RotateCw className="w-3.5 h-3.5 text-yellow-500 shrink-0" /><span>{t("flipCardTip")}</span>
            </span>
          </div>
        )}

        {isLoading && (
          <div className="py-16 text-center">
            <div className="w-10 h-10 border-4 border-yellow-500/20 border-t-yellow-500 rounded-full animate-spin mx-auto mb-3" />
            <p className="text-sm text-slate-500 dark:text-slate-400">{t("loadingDb")}</p>
          </div>
        )}

        {!isLoading && !selectedSub && (
          <div className="py-16 text-center">
            <BookOpen className="w-12 h-12 text-yellow-500/40 mx-auto mb-4" />
            <p className="text-slate-500 dark:text-slate-400 text-sm">{t("selectPrompt")}</p>
          </div>
        )}

        {!isLoading && selectedSub && isTranslating && (
          <div className="flex justify-center mb-4">
            <span className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full text-xs font-medium bg-yellow-500/10 text-yellow-600 dark:text-yellow-400 border border-yellow-500/20">
              <span className="w-3 h-3 border-2 border-yellow-500/30 border-t-yellow-500 rounded-full animate-spin" />
              {t("loadingTrans")(LANG_CONFIG[selectedLang]?.name || "")}
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
                <div className="flex items-center gap-2.5 flex-1 pr-2">
                  <h3 className="text-base font-bold text-slate-900 dark:text-white">{getDisplayTitle(uraianTitle)}</h3>
                  <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-yellow-500/15 text-yellow-600 dark:text-yellow-400 border border-yellow-500/30 shrink-0">{t("versesCount")(verses.length)}</span>
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
                    <p className="text-sm text-slate-500 dark:text-slate-400 text-center py-4">{t("noVerses")}</p>
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
                      <div key={vIdx} className="pt-3 first:pt-0">
                        {/* Verse label row + native audio player with dedicated responsive spacing */}
                        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 sm:gap-4 mb-3.5">
                          <div className="flex items-center gap-2 text-sm font-semibold text-yellow-600 dark:text-yellow-400">
                            <span className="w-2 h-2 rounded-full bg-yellow-500 inline-block shrink-0" />
                            <span>{v.surah_name} [{v.surah_num}]: {v.ayat_num}</span>
                          </div>
                          {/* Native HTML5 audio — murottal Alafasy with ample margin on mobile */}
                          <div className="w-full sm:w-auto flex justify-start sm:justify-end my-1 sm:my-0">
                            <audio
                              controls
                              src={`https://everyayah.com/data/Alafasy_128kbps/${String(v.surah_num).padStart(3,"0")}${String(v.ayat_num).padStart(3,"0")}.mp3`}
                              className="h-9 sm:h-8 w-full sm:w-[260px] max-w-full rounded-lg shadow-sm focus:outline-none"
                              preload="none"
                            />
                          </div>
                        </div>

                        {/* Flip card with guaranteed top margin */}
                        <div onClick={() => toggleCardFlip(cardKey)} className="cursor-pointer mt-1" style={{ perspective: "1000px" }}>
                          <div style={{ position: "relative", transition: "transform 0.7s cubic-bezier(0.34,1.56,0.64,1)", transformStyle: "preserve-3d", transform: isFlipped ? "rotateY(180deg)" : "rotateY(0deg)", minHeight: "180px" }}>
                            <div style={{ backfaceVisibility: "hidden", WebkitBackfaceVisibility: "hidden" }} className="absolute inset-0 flex flex-col justify-center bg-gradient-to-br from-slate-900 to-slate-800 border border-slate-700 rounded-2xl p-5 sm:p-7">
                              <div className="absolute top-3 right-3 text-xs text-slate-500 flex items-center gap-1">
                                <RotateCw className="w-3 h-3 text-yellow-500" /><span className="hidden sm:inline">{t("viewArab")}</span>
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
                                  <Volume2 className="w-3.5 h-3.5" /><span>{isPlaying ? t("stop") : t("listen")}</span>
                                </button>
                                <button onClick={() => { setAiModalVerse(v); setIsAiModalOpen(true); }} className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-purple-500/15 hover:bg-purple-500/25 text-purple-400 border border-purple-500/30 transition">
                                  <Sparkles className="w-3.5 h-3.5" /><span>{t("askAi")}</span>
                                </button>
                                <Link to={`/qmushaf?surah=${v.surah_num}&ayah=${v.ayat_num}`} className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-sky-500/15 hover:bg-sky-500/25 text-sky-400 border border-sky-500/30 transition" onClick={(e) => e.stopPropagation()}>
                                  <BookOpen className="w-3.5 h-3.5" /><span>{t("mushafPerKata")}</span>
                                </Link>
                                <button onClick={() => { navigator.clipboard.writeText(`QS. ${v.surah_name} [${v.surah_num}:${v.ayat_num}]\n\n${v.arab}\n\n"${displayText}"`); showToast(t("copiedVerse")); }} className="p-1.5 rounded-xl bg-slate-700 hover:bg-slate-600 text-slate-300 hover:text-white transition" title="Salin">
                                  <Copy className="w-3.5 h-3.5" />
                                </button>
                              </div>
                            </div>
                            <div style={{ backfaceVisibility: "hidden", WebkitBackfaceVisibility: "hidden", transform: "rotateY(180deg)", position: "absolute", inset: 0 }} className="flex flex-col items-center justify-center bg-gradient-to-br from-slate-900 to-slate-800 border border-yellow-500/40 rounded-2xl p-5 sm:p-7">
                              <div className="absolute top-3 right-3 text-xs text-slate-500 flex items-center gap-1">
                                <RotateCw className="w-3 h-3 text-yellow-500" /><span className="hidden sm:inline">{t("viewTrans")}</span>
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
              <ChevronLeft className="w-4 h-4" /><span>{t("prevSub")}</span>
            </button>
            <button onClick={() => { const idx = subOptions.indexOf(selectedSub); if (idx < subOptions.length - 1) { setSelectedSub(subOptions[idx + 1]); setFlippedCards({}); stopTTS(); } }} disabled={subOptions.indexOf(selectedSub) >= subOptions.length - 1} className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-bold bg-yellow-500 hover:bg-yellow-400 text-slate-900 disabled:opacity-40 disabled:cursor-not-allowed transition shadow-sm">
              <span>{t("nextSub")}</span><ChevronRight className="w-4 h-4" />
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
                <h3 className="text-base font-bold text-slate-900 dark:text-white">{t("aiModalTitle")}</h3>
                <p className="text-xs text-slate-500 dark:text-slate-400">{t("aiModalSubtitle")}</p>
              </div>
            </div>
            <div className="bg-slate-50 dark:bg-slate-800/60 p-3 rounded-xl border border-slate-200 dark:border-slate-700 mb-4">
              <div className="text-xs font-bold text-yellow-600 dark:text-yellow-400 mb-1">QS. {aiModalVerse.surah_name} [{aiModalVerse.surah_num}:{aiModalVerse.ayat_num}]</div>
              <div className="text-xs text-slate-600 dark:text-slate-300 italic line-clamp-3">"{getVerseActiveTranslation(aiModalVerse)}"</div>
            </div>
            <p className="text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider mb-2">{t("aiSelectMode")}</p>
            <div className="flex flex-wrap items-center gap-1.5 mb-4">
              {[
                { id: "tadabbur", label: t("aiTabTadabbur") },
                { id: "asbab", label: t("aiTabAsbab") },
                { id: "mufradat", label: t("aiTabMufradat") },
                { id: "custom", label: t("aiTabCustom") }
              ].map((tab) => (
                <button key={tab.id} onClick={() => setAiMode(tab.id)} className={`px-3 py-1 rounded-full text-xs font-semibold transition ${aiMode === tab.id ? "bg-purple-600 text-white" : "bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700"}`}>{tab.label}</button>
              ))}
            </div>
            {aiMode === "custom" && (
              <div className="mb-4">
                <input type="text" value={aiCustomQuestion} onChange={(e) => setAiCustomQuestion(e.target.value)} placeholder={t("aiInputPlaceholder")} className="w-full bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl p-2.5 text-xs text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-purple-500/50" />
              </div>
            )}
            <div className="mb-4">
              <label className="block text-xs font-semibold text-slate-500 dark:text-slate-400 mb-1">{t("aiPromptLabel")}</label>
              <textarea readOnly value={generateAiPrompt()} rows={6} className="w-full bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 rounded-xl p-3 text-xs font-mono text-slate-700 dark:text-slate-300 focus:outline-none resize-none" />
            </div>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
              <button onClick={() => { navigator.clipboard.writeText(generateAiPrompt()); showToast(t("aiPromptCopied")); }} className="inline-flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl text-xs font-bold bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 transition"><Copy className="w-3.5 h-3.5" /><span>{t("aiCopyPrompt")}</span></button>
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
