import React, { useState, useEffect, useMemo, useRef } from "react";
import { useSearchParams, Link } from "react-router-dom";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import {
  BookMarked,
  BookOpen,
  PenTool,
  Sprout,
  Home,
  Globe,
  Search,
  Sparkles,
  Volume2,
  Copy,
  Share2,
  ExternalLink,
  ChevronDown,
  Check,
  ArrowRight,
  Layers,
  HelpCircle,
  X,
  MessageCircle,
  FileText,
  Play,
  Pause,
  Info
} from "lucide-react";

// ─── 39 LANGUAGES SELECTOR LIST WITH REGIONS ─────────────────────────────
const KAMUS_LANGUAGES = [
  // 🌏 Asia Tenggara & Asia Timur
  { code: "id", name: "Bahasa Indonesia", region: "🌏 Asia Tenggara & Asia Timur" },
  { code: "ms", name: "Bahasa Melayu", region: "🌏 Asia Tenggara & Asia Timur" },
  { code: "th", name: "ภาษาไทย (Thai)", region: "🌏 Asia Tenggara & Asia Timur" },
  { code: "zh", name: "中文 (Chinese)", region: "🌏 Asia Tenggara & Asia Timur" },
  { code: "ja", name: "日本語 (Japanese)", region: "🌏 Asia Tenggara & Asia Timur" },
  { code: "ko", name: "한국어 (Korean)", region: "🌏 Asia Tenggara & Asia Timur" },
  { code: "ug", name: "ئۇيغۇرچە (Uyghur)", region: "🌏 Asia Tenggara & Asia Timur" },

  // 🕌 Timur Tengah, Asia Tengah & Kaukasus
  { code: "fa", name: "فارسی (Persian)", region: "🕌 Timur Tengah, Asia Tengah & Kaukasus" },
  { code: "ku", name: "کوردی (Kurdish)", region: "🕌 Timur Tengah, Asia Tengah & Kaukasus" },
  { code: "ur", name: "اردو (Urdu)", region: "🕌 Timur Tengah, Asia Tengah & Kaukasus" },
  { code: "tr", name: "Türkçe (Turkish)", region: "🕌 Timur Tengah, Asia Tengah & Kaukasus" },
  { code: "az", name: "Azərbaycan (Azerbaijani)", region: "🕌 Timur Tengah, Asia Tengah & Kaukasus" },
  { code: "uz", name: "O'zbekcha (Uzbek)", region: "🕌 Timur Tengah, Asia Tengah & Kaukasus" },
  { code: "tg", name: "Тоҷикӣ (Tajik)", region: "🕌 Timur Tengah, Asia Tengah & Kaukasus" },
  { code: "tt", name: "Татарча (Tatar)", region: "🕌 Timur Tengah, Asia Tengah & Kaukasus" },

  // 🪷 Asia Selatan & Samudra Hindia
  { code: "hi", name: "हिन्दी (Hindi)", region: "🪷 Asia Selatan & Samudra Hindia" },
  { code: "bn", name: "বাংলা (Bangla)", region: "🪷 Asia Selatan & Samudra Hindia" },
  { code: "ta", name: "தமிழ் (Tamil)", region: "🪷 Asia Selatan & Samudra Hindia" },
  { code: "dv", name: "ދިވެހި (Dhivehi)", region: "🪷 Asia Selatan & Samudra Hindia" },

  // 🌍 Afrika
  { code: "ha", name: "Hausa", region: "🌍 Afrika" },
  { code: "sw", name: "Kiswahili (Swahili)", region: "🌍 Afrika" },
  { code: "am", name: "አማርኛ (Amharic)", region: "🌍 Afrika" },
  { code: "ber", name: "Tamaziɣt (Amazigh)", region: "🌍 Afrika" },

  // 🏛️ Eropa Barat, Utara, Tengah & Timur
  { code: "en", name: "English", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" },
  { code: "fr", name: "Français (French)", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" },
  { code: "de", name: "Deutsch (German)", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" },
  { code: "es", name: "Español (Spanish)", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" },
  { code: "pt", name: "Português (Portuguese)", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" },
  { code: "nl", name: "Nederlands (Dutch)", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" },
  { code: "it", name: "Italiano (Italian)", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" },
  { code: "ru", name: "Русский (Russian)", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" },
  { code: "bs", name: "Bosanski (Bosnian)", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" },
  { code: "sq", name: "Shqip (Albanian)", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" },
  { code: "bg", name: "Български (Bulgarian)", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" },
  { code: "cs", name: "Čeština (Czech)", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" },
  { code: "no", name: "Norsk (Norwegian)", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" },
  { code: "pl", name: "Polski (Polish)", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" },
  { code: "ro", name: "Română (Romanian)", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" },
  { code: "sv", name: "Svenska (Swedish)", region: "🏛️ Eropa Barat, Utara, Tengah & Timur" }
];

// Translation source mapping across languages
const TRANSLATION_SOURCES = {
  id: "Kementerian Agama RI (Kemenag)",
  en: "Saheeh International",
  ms: "Basmeih (Jabatan Perdana Menteri Malaysia)",
  fr: "Muhammad Hamidullah",
  de: "Frank Bubenheim & Nadeem Elyas",
  ur: "مولانا فتح محمد جالندھری",
  hi: "डॉ. सुहैल फ़ारूक़ ख़ान व डॉ. सैफ़ुर्रहमान नदवी",
  bn: "মুহিউদ্দীন খান",
  ru: "Эльмир Кулиев",
  zh: "马仲刚 (Muhammad Makin)",
  es: "Raúl González Bórnez",
  tr: "Diyanet İşleri Başkanlığı",
  pt: "Prof. Samir El-Hayek",
  ha: "Abubakar Mahmoud Gumi",
  sw: "Ali Muhsin Al-Barwani",
  fa: "مهدی الهی قمشه‌ای",
  ja: "日本ムスリム協会 (中田考)",
  ko: "최영길 (Hamed Choi)",
  nl: "Sofian S. Siregar",
  it: "Hamza Roberto Piccardo",
  bs: "Besim Korkut",
  sq: "Hasan Efendi Nahi",
  th: "สมาคมนักเรียนเก่าอาหรับ (King Fahd Complex)",
  ber: "Ramdane At Mansour",
  am: "ሳዲቅ እና ሙሐመድ ሳኒ ሐቢብ",
  az: "Vasim Məmmədəliyev & Ziya Bünyadov",
  bg: "Цветан Теофанов",
  cs: "Ivan Hrbek",
  dv: "Office of the President of Maldives",
  no: "Einar Berg",
  pl: "Józef Bielawski",
  ro: "George Grigore",
  sv: "Knut Bernström",
  tg: "Абдулҳамид Оятӣ",
  ta: "ஜான் டிரஸ்ட் அறக்கட்டளை",
  tt: "Якуб Ибн Нугман",
  ug: "مۇھەممەد سالىھ",
  uz: "Muhammad Sodiq Muhammad Yusuf",
  ku: "بورهان موحەممەد ئەمین"
};

// TTS SpeechSynthesis voice mapping
const TTS_LANG_MAP = {
  id: "id-ID",
  en: "en-US",
  ms: "ms-MY",
  fr: "fr-FR",
  de: "de-DE",
  ur: "ur-PK",
  hi: "hi-IN",
  bn: "bn-BD",
  ru: "ru-RU",
  zh: "zh-CN",
  es: "es-ES",
  tr: "tr-TR",
  pt: "pt-BR",
  ha: "ha-NG",
  sw: "sw-TZ",
  fa: "fa-IR",
  ja: "ja-JP",
  ko: "ko-KR",
  nl: "nl-NL",
  it: "it-IT",
  bs: "bs-BA",
  sq: "sq-AL",
  th: "th-TH",
  az: "az-AZ",
  bg: "bg-BG",
  cs: "cs-CZ",
  no: "nb-NO",
  pl: "pl-PL",
  ro: "ro-RO",
  sv: "sv-SE",
  ar: "ar-SA"
};

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

// ─── ARABIC NORMALIZER & EXPANSIONS (FROM SIMAQ SPEC) ────────────────────
const cleanArabicForHighlight = (text) => {
  if (!text) return "";
  let t = String(text).replace(/[\.\d\(\)\[\]_\-ـ\s]/g, "");
  t = t.replace(/[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u08D0-\u08FF\u06DF\u06E0\u06E2\u06E5\u06E6]/g, "");
  t = t.replace(/[إأآٱ]/g, "ا");
  t = t.replace(/[ىيئ]/g, "ي");
  t = t.replace(/[ؤ]/g, "و").replace(/[ء]/g, "");
  t = t.replace(/ة/g, "ه");
  return t;
};

const ARABIC_SPECIAL_EXPANSIONS = {
  "مِنْ": ["من", "ومن", "فمن", "لمن", "بمن", "عمن", "ممن"],
  "فِي": ["في", "وفي", "ففي", "لفي", "وفيه", "فيهم", "فيها", "فينا", "فيكم", "فيك", "فيكما", "فيهما"],
  "عَلَىٰ": ["علي", "وعلي", "فعلي", "لعلي", "عليه", "عليهم", "عليها", "علينا", "عليكم", "عليك", "عليهما"],
  "إِلَىٰ": ["الي", "والي", "فالي", "اليه", "اليهم", "اليها", "الينا", "اليكم", "اليك", "اليهما"],
  "عَنْ": ["عن", "وعن", "فعن", "عنه", "عنهم", "عنها", "عنا", "عنكم", "عنك", "عنهما"],
  "مِمَّا": ["مما", "ومما", "فمما"],
  "عَمَّا 1": ["عما", "وعما", "فعما"],
  "عَمَّا 2": ["عما", "وعما", "فعما"],
  "عَمَّ": ["عم", "وعم", "فعم"],
  "مِمَّن": ["ممن", "وممن", "فممن"],
  "مِمَّ": ["مم", "ومم", "فمم"],
  "فِيمَا": ["فيما", "وفيما", "ففيما"],
  "فِيمَ": ["فيم", "وفيم", "ففيم"],
  "حَتَّىٰ 3": ["حتي", "وحتي", "فحتي"],
  "حَتَّىٰ 1": ["حتي", "وحتي", "فحتي"],
  "حَتَّىٰ": ["حتي", "وحتي", "فحتي"],
  "رُّبَمَا": ["ربما", "ورbما", "فربما"],
  "أَنْ 1": ["ان", "وان", "فان", "بان", "لان", "ابان", "فبان"],
  "أَنْ": ["ان", "وان", "فان", "بان", "لان"],
  "لَنْ": ["لن", "ولن", "فلن"],
  "كَيْ": ["كي", "وكي", "فكي", "لكي", "ولكي", "فلكي"],
  "كَيۡلَا": ["كيلا", "لكيلا", "ولكيلا", "فلكيلا"],
  "إِنْ 1": ["ان", "وان", "فان", "ولئن", "لئن", "افان"],
  "إِنْ": ["ان", "وان", "فان", "ولئن", "لئن"],
  "لاَ 2": ["لا", "ولا", "فلا"],
  "لاَ": ["لا", "ولا", "فلا"],
  "لَمۡ": ["لم", "ولم", "فلم", "الم", "افلم", "اولم"],
  "لَّمَّا 2": ["لما", "ولما", "فلما"],
  "لَّمَّا": ["لما", "ولما", "فلما"],
  "إِلَّا 1": ["الا", "والا", "فالا"],
  "إِلَّا 2": ["الا", "والا", "فالا"],
  "إِلَّا": ["الا", "والا", "فالا"],
  "إِلَّمۡ": ["الم", "فالم", "والا", "فان لم", "فالم"],
  "ثُمَّ": ["ثم", "وثم", "فثم"],
  "أَوْ": ["او", "واو", "فاو"],
  "بَلْ": ["بل", "وبل", "فبل"],
  "أَمْ": ["ام", "وام", "فام"],
  "لَٰكِنْ": ["لكن", "ولكن", "فلكن"],
  "إِمَّا 2": ["اما", "واما", "فاما"],
  "إِمَّا": ["اما", "واما", "فاما"],
  "أَمَّن 1": ["امن", "وامن", "فامن"],
  "أَمَّن 2": ["امن", "وامن", "فامن"],
  "أَمَّا": ["اما", "واما", "فاما"],
  "أَمَّاذَا": ["اماذا", "واماذا", "فاماذا"],
  "لَكِنْ أنا": ["لكنا", "ولكنا", "لكن انا", "ولكن انا", "لكن"],
  "إِنَّ": ["ان", "وان", "فان", "لان", "وانك", "وانكم", "واني", "وانا", "وانه", "وانهم", "وانهن", "وانها", "واننا"],
  "أَنَّ": ["ان", "وان", "فان", "بان", "لان", "وانك", "وانكم", "واني", "وانا", "وانه", "وانهم", "وانهن", "وانها", "واننا", "بانه", "بانهم", "بانكم"],
  "إِنَّمَا 1": ["انما", "وانما", "فانما"],
  "إِنَّمَا 2": ["انما", "وانما", "فانما"],
  "لَعَلَّ": ["لعل", "ولعل", "فلعل", "لعله", "لعلهم", "لعلكم", "لعلي", "لعلنا", "لعلها"],
  "لَكِنَّ": ["لكن", "ولكن", "فلكن", "ولكنه", "ولكنهم", "ولكنكم", "ولكني", "ولكننا", "ولكنها", "ولكنهن"],
  "كَأَنَّ": ["كان", "وكان", "فكان", "كانه", "كانهم", "كانك", "كانكم", "كانها", "كاني", "كاننا"],
  "لَيْتَ": ["ليت", "وليت", "فليت", "ياليت", "يا ليت", "ياليتني", "ياليتها", "ياليتنا", "ياليتهم"],
  "أَنَّمَا 1": ["انما", "وانما", "فانما", "بانما"],
  "أَنَّمَا 2": ["انما", "وانما", "فانما", "بانما"],
  "كَأَنَّمَا": ["كانما", "وكانما", "فكانما"],
  "أَلَّا 3": ["الا", "والا", "فالا", "ان لا", "وان لا"],
  "أَلَّا 4": ["الا", "والا", "فالا", "ان لا", "وان لا"],
  "أَلَّن": ["الن", "والن", "فلن", "ان لن", "وان لن"],
  "وَيۡكَأَنَّ": ["ويكان", "فويكان", "ويكانه"],
  "أَلَّو": ["الو", "لو", "ان", "وان لو"],
  "1b": ["ه", "هو", "هي", "له", "به", "منه", "عنه", "فيه", "عليه", "اليه", "كتابه", "ربه", "عنده", "دونه", "بيده", "قلبه", "اهله", "نفسه", "امره", "اسمه"],
  "2b": ["هما", "لهما", "بهما", "عنهما", "منهما", "فيهما", "عليهما", "اليهما", "بينهما"],
  "3b": ["هم", "همو", "لهم", "بهم", "عنهم", "منهم", "عليهم", "اليهم", "فيهم", "انفسهم", "قلوبهم", "اموالهم", "ديارهم", "اعمالهم", "ابصارهم"],
  "4b": ["ها", "لها", "بها", "عنها", "منها", "فيها", "عليها", "اليها", "نفسها", "عينها", "اثرها"],
  "5b": ["هن", "لهن", "بهن", "عنهن", "منهن", "فيهن", "عليهن", "اليهن", "انفسهن", "بيوتهن"],
  "6b": ["ك", "لك", "بك", "عنك", "منك", "فيك", "عليك", "اليك", "ربك", "نفسك", "يدك", "صدرك"],
  "7b": ["كما", "لكما", "بكما", "عنكما", "منكما", "فيكما", "عليكما", "اليكما", "ربكما"],
  "8b": ["كم", "كمو", "لكم", "بكم", "عنكم", "منكم", "فيكم", "عليكم", "اليكم", "انفسكم", "دينكم", "ربكم", "اموالكم"],
  "9b": ["ك", "لك", "بك", "عنك", "منك", "فيك", "عليك", "اليك"],
  "10b": ["كن", "لكن", "بكن", "عنكن", "منكن", "فيكن", "عليكن", "اليكن"],
  "11b": ["ي", "ني", "لي", "بي", "عني", "مني", "في", "علي", "الي", "ربي", "صدري", "امري", "ديني", "قومي", "نفسي"],
  "12b": ["نا", "لنا", "بنا", "عنا", "منا", "فينا", "علينا", "الينا", "ربنا", "انفسنا", "ديننا", "الهنا"],
  "11a": ["انا", "انني", "وانا", "فانا"],
  "1a": ["هو", "وهو", "فهو", "لهو"],
  "4a": ["هي", "وهي", "فهي", "لهي"],
  "3a": ["هم", "وهم", "فهم", "لهم"],
  "5a": ["هن", "وهن", "فهن"],
  "6a": ["انت", "وانت", "فانت"],
  "8a": ["انتم", "وانتم", "فانتم"],
  "12a": ["نحن", "ونحن", "فنحن"],
  "اللاَّتِي": ["اللاتي", "التي", "والاتي", "والتي"],
  "اللائِي": ["اللائي", "اللاي", "الاي", "الي", "اللاءي", "والائي", "والي"],
  "اللَّذَانِ": ["اللذان", "اللذين", "الذان", "الذين", "والذان", "والذين"],
  "الَّذِينَ": ["الذين", "والذين", "فالذين", "للذين"],
  "الَّذِي": ["الذي", "والذي", "فالذي", "للذي", "كالذي"],
  "الَّتِي": ["التي", "والتي", "فالتي", "للتي"],
  "أَيّ 2": ["اي", "بايك", "ايكم", "ايهم", "فايهم", "وايهم"],
  "أَيّ": ["اي", "بايك", "ايكم", "ايهم", "فايهم", "وايهم"],
  "ذَا": ["ذا", "هذا", "ذلك", "كذلك", "فذلك", "وكذلك", "فذلكم", "ذلكم"],
  "أُولاَءِ": ["اولاء", "هولاء", "اوليك", "اولىك", "فاوليك", "واوليك", "هاولاء"],
  "هَٰذَٰنِ": ["هذان", "فذانك", "ذانك", "هذين", "ذينك"],
  "تَانِ": ["تان", "تانك", "هاتين", "هتين"],
  "هَٰذَا": ["هذا", "فهذا", "وهذا", "بهذا", "لهذا"],
  "ذَٰلِكَ": ["ذلك", "فذلك", "وذلك", "كذلك", "بذلك", "لذلك", "ذلكم"],
  "تِلْكَ": ["تلك", "فتلك", "وتلك", "كتلك"],
  "هَٰؤُلَاءِ": ["هولاء", "هاولاء", "فهولاء", "وهولاء"],
  "سُبْحَانَ": ["سبحان", "فسبحان", "سبحانه", "سبحانك", "سبحن"],
  "أُمُ": ["هاوم", "هاؤم", "هاام", "هاوءم"],
  "لَيْسَ": ["ليس", "لست", "لسنا", "ليسوا", "ليست", "لستم", "لستن", "وليس", "فليس"],
  "نِعْمَ": ["نعم", "فنعما", "نعما", "ولنعم"],
  "بِئْسَ": ["بئس", "فبئس", "ولبئس", "بئسما"],
  "عَسَى": ["عسى", "فعسى", "وعسى"],
  "سَاءَ": ["ساء", "وساء", "فساء"],
  "تَبَارَكَ": ["تبارك", "فتبارك"]
};

// Robust Occurrence Data Getters
const getOccSurat = (occ) => occ?.SURAT ?? occ?.surat ?? occ?.Surat ?? 1;
const getOccAyat = (occ) => occ?.AYAT ?? occ?.ayat ?? occ?.Ayat ?? 1;
const getOccSuratNama = (occ) => {
  if (occ?.SuratNama && occ.SuratNama.trim() && !occ.SuratNama.startsWith("Surat ")) {
    return occ.SuratNama.trim();
  }
  if (occ?.NAMA_SURAT && occ.NAMA_SURAT.trim()) return occ.NAMA_SURAT.trim();
  if (occ?.nama_surat && occ.nama_surat.trim()) return occ.nama_surat.trim();
  if (occ?.surat_nama && occ.surat_nama.trim()) return occ.surat_nama.trim();
  const sNum = parseInt(getOccSurat(occ), 10);
  if (sNum >= 1 && sNum <= 114) {
    return SURAH_NAMES[sNum - 1];
  }
  return `Surat ${sNum}`;
};
const getOccTeksArab = (occ) => {
  return occ?.TeksArab || occ?.Teks_Arab || occ?.teks_arab || occ?.Lafdz || "";
};
const getOccRawArti = (occ, lang = "id") => {
  if (!occ) return "";
  const lUpper = (lang || "id").toUpperCase();
  return (
    occ[`TeksArti${lUpper}`] ||
    occ[`teksArti${lUpper}`] ||
    occ.TeksArti ||
    occ.Teks_Arti ||
    occ.teks_arti ||
    occ.Terjemah ||
    occ.TeksArtiID ||
    ""
  );
};

const QKamus = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const [activeDict, setActiveDict] = useState("portal"); // 'portal' | 'jamid' | 'harf' | 'harf_amil' | 'musytaq'
  const [selectedLang, setSelectedLang] = useState(() => {
    return localStorage.getItem("kamus_lang") || "id";
  });

  // Dataset caches
  const [dataSets, setDataSets] = useState({
    jamid: null,
    harf: null,
    harf_amil: null,
    musytaq: null
  });
  const [translationsCache, setTranslationsCache] = useState({});
  const [loadingDict, setLoadingDict] = useState(false);
  const [toastMessage, setToastMessage] = useState(null);

  // Standard Dictionary selection state (Jamid, Harf, Harf Amil)
  const [selectedBentuk, setSelectedBentuk] = useState("");
  const [selectedNoKata, setSelectedNoKata] = useState("");
  const [ayatFilterQuery, setAyatFilterQuery] = useState("");

  // Musytaq state
  const [musytaqLevel, setMusytaqLevel] = useState("1");
  const [musytaqSelectedAkarId, setMusytaqSelectedAkarId] = useState("");
  const [musytaqCategory, setMusytaqCategory] = useState("all"); // 'all' | 'madhi' | 'mudhari' | 'amr' | 'masdar' | 'isim'
  const [musytaqFilterQuery, setMusytaqFilterQuery] = useState("");

  // Audio Tilawah state
  const [playingAudioKey, setPlayingAudioKey] = useState(null); // `${surat}:${ayat}`
  const audioRef = useRef(null);

  // AI Assistant Modal State
  const [aiModalOpen, setAiModalOpen] = useState(false);
  const [aiTopic, setAiTopic] = useState("nahwu"); // 'nahwu' | 'tafsir' | 'balaghah'
  const [aiContext, setAiContext] = useState({
    surat: 1,
    ayat: 1,
    suratNama: "",
    kata: "",
    noKata: "",
    bentuk: "",
    teksArab: "",
    teksArti: ""
  });

  const showToast = (msg) => {
    setToastMessage(msg);
    setTimeout(() => setToastMessage(null), 3000);
  };

  // Group languages by region for <optgroup>
  const groupedLanguages = useMemo(() => {
    const groups = {};
    KAMUS_LANGUAGES.forEach((l) => {
      if (!groups[l.region]) groups[l.region] = [];
      groups[l.region].push(l);
    });
    return groups;
  }, []);

  // ─── LOAD DATASET FOR ACTIVE DICTIONARY ────────────────────────────────
  useEffect(() => {
    if (activeDict === "portal") return;

    if (!dataSets[activeDict]) {
      setLoadingDict(true);
      const filenameMap = {
        jamid: "dhamir_data.json",
        harf: "harf_data.json",
        harf_amil: "harf_amil_data.json",
        musytaq: "musytaq_data.json"
      };

      fetch(`/kamus_data/${filenameMap[activeDict]}`)
        .then((res) => {
          if (!res.ok) throw new Error("Gagal mengambil data kamus");
          return res.json();
        })
        .then((data) => {
          setDataSets((prev) => ({ ...prev, [activeDict]: data }));
          setLoadingDict(false);
        })
        .catch((err) => {
          console.error("Error loading dictionary:", err);
          setLoadingDict(false);
          showToast("Gagal memuat data kamus.");
        });
    }
  }, [activeDict, dataSets]);

  // ─── LOAD TRANSLATION IF NON-ID SELECTED ──────────────────────────────
  useEffect(() => {
    if (selectedLang === "id") return;
    if (!translationsCache[selectedLang]) {
      fetch(`/kamus_data/translations/${selectedLang}_translations.json`)
        .then((res) => (res.ok ? res.json() : null))
        .then((data) => {
          if (data) {
            setTranslationsCache((prev) => ({ ...prev, [selectedLang]: data }));
          }
        })
        .catch((err) => console.warn("Failed to load translation json:", err));
    }
  }, [selectedLang, translationsCache]);

  // ─── HANDLE URL QUERY PARAMS (DEEP LINKING) ───────────────────────────
  useEffect(() => {
    const dictParam = searchParams.get("dict") || searchParams.get("kamus");
    const langParam = searchParams.get("lang");
    const noParam = searchParams.get("no") || searchParams.get("kata");
    const akarParam = searchParams.get("akar") || searchParams.get("root");

    if (langParam && KAMUS_LANGUAGES.some((l) => l.code === langParam)) {
      setSelectedLang(langParam);
    }

    if (dictParam) {
      let d = dictParam.toLowerCase().trim();
      if (d === "dhamir") d = "jamid";
      if (d === "ghair_amil" || d === "ghairamil") d = "harf";
      if (d === "amil") d = "harf_amil";
      if (d === "tasrif") d = "musytaq";

      if (["jamid", "harf", "harf_amil", "musytaq", "portal"].includes(d)) {
        setActiveDict(d);
      }
    } else if (akarParam) {
      setActiveDict("musytaq");
    } else if (noParam) {
      setActiveDict("jamid");
    }
  }, [searchParams]);

  // ─── STANDARD DICTIONARY COMPUTED VALUES ──────────────────────────────
  const currentDataset = dataSets[activeDict] || [];

  // Distinct "Bentuk Kata" list
  const bentukKataList = useMemo(() => {
    if (!Array.isArray(currentDataset)) return [];
    const set = new Set();
    currentDataset.forEach((item) => {
      const b = item["Bentuk Kata"] || item.bentuk_kata;
      if (b && typeof b === "string" && b.trim()) {
        set.add(b.trim());
      }
    });
    return Array.from(set);
  }, [currentDataset]);

  // Auto-select first Bentuk Kata or match URL parameter
  useEffect(() => {
    if (["jamid", "harf", "harf_amil"].includes(activeDict) && bentukKataList.length > 0) {
      const bParam = searchParams.get("b") || searchParams.get("bentuk");
      if (bParam) {
        const matched = bentukKataList.find(
          (b) => b.toLowerCase().includes(bParam.toLowerCase()) || b.startsWith(bParam)
        );
        if (matched) {
          setSelectedBentuk(matched);
          return;
        }
      }
      if (!selectedBentuk || !bentukKataList.includes(selectedBentuk)) {
        setSelectedBentuk(bentukKataList[0]);
      }
    }
  }, [activeDict, bentukKataList, searchParams]);

  // Distinct "No Kata" for selected Bentuk Kata
  const noKataList = useMemo(() => {
    if (!selectedBentuk || !Array.isArray(currentDataset)) return [];
    const map = new Map();
    currentDataset.forEach((item) => {
      const b = item["Bentuk Kata"] || item.bentuk_kata;
      const no = item["No kata"] || item.no_kata || item["No Kata"];
      if (b && b.trim() === selectedBentuk && no) {
        const noStr = String(no).trim();
        if (!map.has(noStr)) {
          map.set(noStr, {
            no: noStr,
            kata: item["Kata"] || item.kata,
            arti: item["Arti kata"] || item.arti_kata || item["Arti"],
            latin: item["Latin"] || item.latin || item["Nama"] || ""
          });
        }
      }
    });
    return Array.from(map.values()).sort((a, b) => a.no.localeCompare(b.no, "id", { numeric: true }));
  }, [currentDataset, selectedBentuk]);

  // Auto-select first No Kata or match URL parameter
  useEffect(() => {
    if (noKataList.length > 0) {
      const noParam = searchParams.get("no") || searchParams.get("kata");
      if (noParam) {
        const matched = noKataList.find((n) => n.no.toLowerCase() === noParam.toLowerCase().trim());
        if (matched) {
          setSelectedNoKata(matched.no);
          return;
        }
      }
      if (!selectedNoKata || !noKataList.some((n) => n.no === selectedNoKata)) {
        setSelectedNoKata(noKataList[0].no);
      }
    }
  }, [noKataList, searchParams]);

  // Current spotlight item
  const currentSpotlight = useMemo(() => {
    if (!selectedNoKata || !Array.isArray(currentDataset)) return null;
    const match = currentDataset.find((item) => {
      const b = item["Bentuk Kata"] || item.bentuk_kata;
      const no = item["No kata"] || item.no_kata || item["No Kata"];
      return b && b.trim() === selectedBentuk && String(no).trim() === selectedNoKata;
    });
    return match || null;
  }, [currentDataset, selectedBentuk, selectedNoKata]);

  // References (all ayat occurrences for this word)
  const currentReferences = useMemo(() => {
    if (!selectedNoKata || !Array.isArray(currentDataset)) return [];
    const occurrences = currentDataset.filter((item) => {
      const b = item["Bentuk Kata"] || item.bentuk_kata;
      const no = item["No kata"] || item.no_kata || item["No Kata"];
      return b && b.trim() === selectedBentuk && String(no).trim() === selectedNoKata;
    });

    if (!ayatFilterQuery.trim()) return occurrences;
    const q = ayatFilterQuery.toLowerCase().trim();
    return occurrences.filter((occ) => {
      const surat = String(getOccSurat(occ));
      const ayat = String(getOccAyat(occ));
      const namaSurat = getOccSuratNama(occ).toLowerCase();
      const rawArti = getOccRawArti(occ, selectedLang).toLowerCase();
      return surat.includes(q) || ayat.includes(q) || namaSurat.includes(q) || rawArti.includes(q);
    });
  }, [currentDataset, selectedBentuk, selectedNoKata, ayatFilterQuery, selectedLang]);

  // ─── MUSYTAQ COMPUTED VALUES ─────────────────────────────────────────
  const musytaqDataset = dataSets.musytaq || [];

  // Group Musytaq by Root (No Akar & Akar)
  const musytaqRoots = useMemo(() => {
    if (activeDict !== "musytaq" || !Array.isArray(musytaqDataset)) return [];
    const map = new Map();
    musytaqDataset.forEach((item) => {
      const noAkar = item["No Akar"] || item.no_akar || item.id;
      const akar = item["Akar"] || item.akar || item["Kata/Akar"];
      if (noAkar != null && akar) {
        const id = String(noAkar).trim();
        if (!map.has(id)) {
          map.set(id, {
            id,
            akar: String(akar).trim(),
            masdar: item["Masdar"] || item.masdar || "",
            arti: item["Arti Akar"] || item.arti_akar || item["Arti"] || "",
            frek: item["Frek Akar"] || item.frek_akar || item["Frek"] || "-"
          });
        }
      }
    });
    return Array.from(map.values()).sort((a, b) => parseInt(a.id) - parseInt(b.id));
  }, [activeDict, musytaqDataset]);

  // Auto-select first root or match URL parameter
  useEffect(() => {
    if (activeDict === "musytaq" && musytaqRoots.length > 0) {
      const akarParam = searchParams.get("akar") || searchParams.get("root");
      if (akarParam) {
        const matched = musytaqRoots.find(
          (r) => r.id === akarParam.trim() || r.akar.replace(/\s+/g, "") === akarParam.replace(/\s+/g, "")
        );
        if (matched) {
          setMusytaqSelectedAkarId(matched.id);
          return;
        }
      }
      if (!musytaqSelectedAkarId || !musytaqRoots.some((r) => r.id === musytaqSelectedAkarId)) {
        setMusytaqSelectedAkarId(musytaqRoots[0].id);
      }
    }
  }, [activeDict, musytaqRoots, searchParams]);

  const currentMusytaqRoot = useMemo(() => {
    if (!musytaqSelectedAkarId) return null;
    return musytaqRoots.find((r) => r.id === musytaqSelectedAkarId) || null;
  }, [musytaqRoots, musytaqSelectedAkarId]);

  // All tasrif rows for selected root
  const currentMusytaqTasrifRows = useMemo(() => {
    if (!musytaqSelectedAkarId || !Array.isArray(musytaqDataset)) return [];
    return musytaqDataset.filter((item) => {
      const no = String(item["No Akar"] || item.no_akar || item.id || "").trim();
      return no === musytaqSelectedAkarId;
    });
  }, [musytaqDataset, musytaqSelectedAkarId]);

  // Counts for Musytaq Category Chips
  const categoryCounts = useMemo(() => {
    const counts = { all: currentMusytaqTasrifRows.length, madhi: 0, mudhari: 0, amr: 0, masdar: 0, isim: 0 };
    currentMusytaqTasrifRows.forEach((row) => {
      const bentuk = String(row["Bentuk Kata"] || row.bentuk_kata || "").toLowerCase();
      if (bentuk.includes("madhi")) counts.madhi++;
      else if (bentuk.includes("mudhari")) counts.mudhari++;
      else if (bentuk.includes("amr")) counts.amr++;
      else if (bentuk.includes("masdar") || bentuk.includes("mashdar")) counts.masdar++;
      else if (bentuk.includes("fa'il") || bentuk.includes("maf'ul") || bentuk.includes("sifat") || bentuk.includes("isim")) counts.isim++;
    });
    return counts;
  }, [currentMusytaqTasrifRows]);

  // Filter tasrif rows by category & search query
  const filteredTasrifList = useMemo(() => {
    let rows = currentMusytaqTasrifRows;

    // Filter by category chip
    if (musytaqCategory && musytaqCategory !== "all") {
      rows = rows.filter((row) => {
        const bentuk = String(row["Bentuk Kata"] || row.bentuk_kata || "").toLowerCase();
        if (musytaqCategory === "madhi") return bentuk.includes("madhi");
        if (musytaqCategory === "mudhari") return bentuk.includes("mudhari");
        if (musytaqCategory === "amr") return bentuk.includes("amr");
        if (musytaqCategory === "masdar") return bentuk.includes("masdar") || bentuk.includes("mashdar");
        if (musytaqCategory === "isim") return bentuk.includes("fa'il") || bentuk.includes("maf'ul") || bentuk.includes("sifat") || bentuk.includes("isim");
        return true;
      });
    }

    // Filter by search query
    if (musytaqFilterQuery.trim()) {
      const q = musytaqFilterQuery.toLowerCase().trim();
      rows = rows.filter((row) => {
        const lafdz = String(row["Lafdz"] || row.lafdz || row["Kata"] || "").toLowerCase();
        const arti = String(row["Terjemah"] || row.terjemah || row["Arti"] || "").toLowerCase();
        const wazan = String(row["Teori/i'rab/Wazan/I'lal"] || row.wazan || "").toLowerCase();
        return lafdz.includes(q) || arti.includes(q) || wazan.includes(q);
      });
    }

    return rows;
  }, [currentMusytaqTasrifRows, musytaqCategory, musytaqFilterQuery]);

  // ─── AUDIO PLAYBACK ──────────────────────────────────────────────────
  const playArabicAudio = (text) => {
    if (!text) return;
    if (window.speechSynthesis) {
      window.speechSynthesis.cancel();
      const cleaned = String(text)
        .replace(/\u0671/g, "\u0627")
        .replace(/\u0670/g, "\u0627")
        .replace(/\u06E1/g, "\u0652")
        .replace(/[\u06D6-\u06DC\u06DF-\u06E0\u06E2-\u06ED]/g, "")
        .trim();
      const utter = new SpeechSynthesisUtterance(cleaned);
      utter.lang = "ar-SA";
      utter.rate = 0.85;
      window.speechSynthesis.speak(utter);
    }
  };

  const playTranslationTts = (text) => {
    if (!text) return;
    if (window.speechSynthesis) {
      window.speechSynthesis.cancel();
      const utter = new SpeechSynthesisUtterance(text);
      utter.lang = TTS_LANG_MAP[selectedLang] || "id-ID";
      utter.rate = 0.95;
      window.speechSynthesis.speak(utter);
      showToast(`Membacakan terjemahan (${selectedLang.toUpperCase()})`);
    } else {
      showToast("Text-to-speech tidak didukung di browser ini.");
    }
  };

  const toggleVerseAudio = (surat, ayat) => {
    if (!surat || !ayat) return;
    const key = `${surat}:${ayat}`;

    if (playingAudioKey === key) {
      if (audioRef.current) audioRef.current.pause();
      setPlayingAudioKey(null);
      return;
    }

    const s3 = String(surat).padStart(3, "0");
    const a3 = String(ayat).padStart(3, "0");
    const url = `https://everyayah.com/data/Alafasy_128kbps/${s3}${a3}.mp3`;

    if (audioRef.current) {
      audioRef.current.pause();
      audioRef.current.src = url;
      audioRef.current
        .play()
        .then(() => setPlayingAudioKey(key))
        .catch((err) => {
          console.warn("Audio play error:", err);
          showToast("Gagal memutar audio tilawah.");
          setPlayingAudioKey(null);
        });
    }
  };

  // Helper to get translated text for an ayat
  const getVerseTranslation = (surat, ayat, fallbackText = "") => {
    if (selectedLang !== "id") {
      const key = `${surat}:${ayat}`;
      const cached = translationsCache[selectedLang];
      if (cached && cached[key]) {
        return cached[key];
      }
    }
    return fallbackText || "";
  };

  // ─── HIGHLIGHT ARABIC TARGET WORD (ACCORDING TO SIMAQ SPEC) ───────────
  const renderHighlightedArabic = (fullArabText, targetKata) => {
    if (!fullArabText || !targetKata) return fullArabText || "";

    const tokens = new Set();
    const cleanK = cleanArabicForHighlight(targetKata);

    // 1. Check special expansion by targetKata
    Object.keys(ARABIC_SPECIAL_EXPANSIONS).forEach((expK) => {
      if (targetKata.includes(expK) || expK === targetKata || cleanArabicForHighlight(expK) === cleanK) {
        ARABIC_SPECIAL_EXPANSIONS[expK].forEach((x) => tokens.add(cleanArabicForHighlight(x)));
      }
    });

    // 2. Add individual parts separated by slash or space
    const parts = targetKata.split(/[/,\s]+/);
    parts.forEach((p) => {
      const cl = cleanArabicForHighlight(p);
      if (cl && cl.length >= 1) tokens.add(cl);
    });

    const tokenList = Array.from(tokens).filter(Boolean);
    if (tokenList.length === 0) return fullArabText;

    const words = String(fullArabText).split(/\s+/);
    return words.map((w, idx) => {
      const cleanW = cleanArabicForHighlight(w);
      let isMatch = false;

      for (let i = 0; i < tokenList.length; i++) {
        const tok = tokenList[i];
        if (cleanW === tok || (tok.length >= 2 && (cleanW.endsWith(tok) || cleanW.startsWith(tok) || cleanW.includes(tok)))) {
          isMatch = true;
          break;
        }
      }

      return (
        <React.Fragment key={idx}>
          {isMatch ? (
            <span className="text-red-500 dark:text-red-400 font-extrabold bg-red-500/15 border border-red-500/35 px-1.5 py-0.5 rounded shadow-[0_0_12px_rgba(239,68,68,0.35)] inline transition">
              {w}
            </span>
          ) : (
            <span>{w}</span>
          )}{" "}
        </React.Fragment>
      );
    });
  };

  // ─── AI ASSISTANT MODAL TRIGGER ──────────────────────────────────────
  const handleOpenAiModal = (occ, kata, noKata, bentuk) => {
    const surat = getOccSurat(occ);
    const ayat = getOccAyat(occ);
    const namaSurat = getOccSuratNama(occ);
    const teksArab = getOccTeksArab(occ);
    const rawArti = getOccRawArti(occ, selectedLang);
    const teksArti = getVerseTranslation(surat, ayat, rawArti);

    setAiContext({
      surat,
      ayat,
      suratNama: namaSurat,
      kata,
      noKata,
      bentuk,
      teksArab,
      teksArti
    });
    setAiTopic("nahwu");
    setAiModalOpen(true);
  };

  const handleOpenMusytaqAiModal = () => {
    if (!currentMusytaqRoot) return;
    setAiContext({
      surat: 1,
      ayat: 1,
      suratNama: `Akar ${currentMusytaqRoot.akar}`,
      kata: currentMusytaqRoot.akar,
      noKata: currentMusytaqRoot.id,
      bentuk: `Kamus Musytaq (Akar: ${currentMusytaqRoot.akar}, Masdar: ${currentMusytaqRoot.masdar})`,
      teksArab: `${currentMusytaqRoot.akar} (${currentMusytaqRoot.masdar})`,
      teksArti: `Arti Akar: ${currentMusytaqRoot.arti} | Total ${currentMusytaqTasrifRows.length} variasi tasrif di Al-Qur'an`
    });
    setAiTopic("nahwu");
    setAiModalOpen(true);
  };

  // Build AI Prompt
  const generatedAiPrompt = useMemo(() => {
    const { surat, ayat, suratNama, kata, noKata, bentuk, teksArab, teksArti } = aiContext;

    if (aiTopic === "nahwu") {
      return `Tolong jelaskan analisis kaidah tata bahasa Arab (Nahwu/Shorof) dan I'rob secara mendalam mengenai kata "${kata}" (${noKata}, ${bentuk}) pada ${suratNama} [${surat}:${ayat}]:\n\nTeks Arab: "${teksArab}"\nTerjemahan: "${teksArti}"\n\nMohon sertakan:\n1. Kedudukan i'rob kata "${kata}" dalam kalimat tersebut (Marfu'/Manshub/Majrur).\n2. Jenis kata dan status morfemnya (Dhamir, Isim Mawshul, Harf, Wazan Sharaf, dsb).\n3. Penjelasan kaidah nahwu bahasa Al-Qur'an terkait secara sistematis.`;
    } else if (aiTopic === "tafsir") {
      return `Tolong berikan penjelasan tafsir ringkas dan kontekstual mengenai ${suratNama} [${surat}:${ayat}]:\n\nTeks Arab: "${teksArab}"\nTerjemahan: "${teksArti}"\n\nFokus pada kata "${kata}": Apa hikmah, asbabun nuzul (jika ada), dan pelajaran utama yang dapat dipetik oleh seorang muslim dari ayat ini?`;
    } else {
      return `Tolong jelaskan keindahan balaghah (sastra dan uslub Al-Qur'an) terkait pemilihan kata "${kata}" pada ${suratNama} [${surat}:${ayat}]:\n\nTeks Arab: "${teksArab}"\nTerjemahan: "${teksArti}"\n\nMengapa kata/lafadz ini yang dipilih pada konteks ayat tersebut dan apa rahasia keindahan serta ketelitian maknanya?`;
    }
  }, [aiContext, aiTopic]);

  // ─── WHATSAPP SHARING LOGIC ──────────────────────────────────────────
  const shareWordToWhatsApp = () => {
    if (!currentSpotlight) return;
    const kata = currentSpotlight["Kata"] || currentSpotlight.kata || "";
    const latin = currentSpotlight["Latin"] || currentSpotlight.latin || "";
    const arti = currentSpotlight["Arti kata"] || currentSpotlight.arti_kata || currentSpotlight["Arti"] || "";
    const bentuk = currentSpotlight["Bentuk Kata"] || currentSpotlight.bentuk_kata || "";
    const no = currentSpotlight["No kata"] || currentSpotlight.no_kata || "";
    const frek = currentSpotlight["Frek kata"] || currentSpotlight.frek_kata || "-";

    const link = `${window.location.origin}/qkamus?dict=${activeDict}&no=${encodeURIComponent(no)}&lang=${selectedLang}`;
    const text = `*KAMUS AL-QUR'AN — SIMAQ*\n\n` +
      `*Kata:* ${kata} (${latin})\n` +
      `*Nomor Kata:* ${no}\n` +
      `*Kategori:* ${bentuk}\n` +
      `*Arti:* ${arti}\n` +
      `*Frekuensi di Al-Qur'an:* ${frek}x\n\n` +
      `Pelajari lebih lengkap & dengarkan audio:\n${link}`;

    const waUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`;
    window.open(waUrl, "_blank", "noopener,noreferrer");
  };

  const shareAyatToWhatsApp = (occ) => {
    if (!occ) return;
    const surat = getOccSurat(occ);
    const ayat = getOccAyat(occ);
    const namaSurat = getOccSuratNama(occ);
    const arab = getOccTeksArab(occ);
    const rawArti = getOccRawArti(occ, selectedLang);
    const arti = getVerseTranslation(surat, ayat, rawArti);

    const link = `${window.location.origin}/qmushaf?surah=${surat}&ayah=${ayat}`;
    const text = `*RUJUKAN AYAT AL-QUR'AN — SIMAQ*\n\n` +
      `*QS. ${namaSurat} [${surat}:${ayat}]*\n\n` +
      `${arab}\n\n` +
      `*Terjemahan:*\n"${arti}"\n\n` +
      `Buka Mushaf Word-by-Word:\n${link}`;

    const waUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`;
    window.open(waUrl, "_blank", "noopener,noreferrer");
  };

  const shareMusytaqToWhatsApp = () => {
    if (!currentMusytaqRoot) return;
    const link = `${window.location.origin}/qkamus?dict=musytaq&akar=${encodeURIComponent(currentMusytaqRoot.id)}&lang=${selectedLang}`;
    const text = `*KAMUS MUSYTAQ AL-QUR'AN — SIMAQ*\n\n` +
      `*Akar Kata:* ${currentMusytaqRoot.akar} (${currentMusytaqRoot.masdar})\n` +
      `*Arti Akar:* ${currentMusytaqRoot.arti}\n` +
      `*Frekuensi Kemunculan:* ${currentMusytaqRoot.frek}x\n` +
      `*Total Variasi Tasrif:* ${currentMusytaqTasrifRows.length} Bentuk\n\n` +
      `Eksplorasi seluruh pola tasrif Al-Qur'an:\n${link}`;

    const waUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`;
    window.open(waUrl, "_blank", "noopener,noreferrer");
  };

  const shareTasrifRowToWhatsApp = (row) => {
    if (!row) return;
    const lafdz = row["Lafdz"] || row.lafdz || row["Kata"] || "";
    const wazan = row["Teori/i'rab/Wazan/I'lal"] || row.wazan || "";
    const bentuk = row["Bentuk Kata"] || row.bentuk_kata || "";
    const arti = row["Terjemah"] || row.terjemah || row["Arti"] || "";
    const frek = row["Frek"] || row.frek || "-";
    const link = `${window.location.origin}/qkamus?dict=musytaq&akar=${encodeURIComponent(musytaqSelectedAkarId)}&lang=${selectedLang}`;

    const text = `*TASRIF MUSYTAQ AL-QUR'AN — SIMAQ*\n\n` +
      `*Akar Kata:* ${currentMusytaqRoot?.akar || ""} (${currentMusytaqRoot?.masdar || ""})\n` +
      `*Bentuk:* ${lafdz}\n` +
      `*Wazan:* ${wazan}\n` +
      `*Kategori:* ${bentuk}\n` +
      `*Arti:* ${arti}\n` +
      `*Frekuensi di Al-Qur'an:* ${frek}x\n\n` +
      `Eksplorasi seluruh pola tasrif:\n${link}`;

    const waUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`;
    window.open(waUrl, "_blank", "noopener,noreferrer");
  };

  // ─── COPY LINK ───────────────────────────────────────────────────────
  const copyDeepLink = (dictType, keyVal) => {
    let url = `${window.location.origin}/qkamus?dict=${dictType}`;
    if (dictType === "musytaq") {
      url += `&akar=${encodeURIComponent(keyVal || musytaqSelectedAkarId)}`;
    } else {
      url += `&no=${encodeURIComponent(keyVal || selectedNoKata)}`;
    }
    url += `&lang=${selectedLang}`;

    navigator.clipboard.writeText(url).then(() => {
      showToast("Link berhasil disalin ke clipboard! 📋");
    });
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-100 transition-colors duration-200">
      <Navbar />

      {/* Hidden audio element for Murottal */}
      <audio
        ref={audioRef}
        onEnded={() => setPlayingAudioKey(null)}
        onError={() => {
          showToast("Gagal memutar audio ayat. Periksa koneksi internet.");
          setPlayingAudioKey(null);
        }}
        className="hidden"
      />

      {/* Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 left-1/2 transform -translate-x-1/2 z-50 bg-slate-900/90 dark:bg-slate-800/95 border border-yellow-500/40 text-yellow-400 px-5 py-2.5 rounded-full shadow-xl text-sm font-medium flex items-center gap-2 backdrop-blur-md animate-fade-in">
          <Check className="w-4 h-4 text-emerald-400" />
          <span>{toastMessage}</span>
        </div>
      )}

      {/* Header Banner */}
      <header className="pt-24 pb-6 border-b border-slate-200 dark:border-slate-800 bg-white/50 dark:bg-slate-900/50 backdrop-blur-sm">
        <div className="container mx-auto px-4 max-w-6xl">
          <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-5">
            <div>
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold uppercase tracking-wider bg-yellow-500/10 text-yellow-600 dark:text-yellow-400 border border-yellow-500/20 mb-2">
                <BookMarked className="w-3.5 h-3.5" />
                <span>Leksikon & Gramatika Al-Qur'an</span>
              </div>
              <h1 className="text-2xl md:text-3xl font-bold tracking-tight text-slate-900 dark:text-white">
                Kamus <span className="text-yellow-500">Al-Qur'an</span>
              </h1>
              <p className="text-sm text-slate-500 dark:text-slate-400 mt-1 max-w-xl leading-relaxed">
                Koleksi komprehensif kosakata gramatika: Jamid Mabny, Harf Ghair 'Amil, Harf 'Amil, dan Musytaq 80 akar kata dengan audio tilawah dan 39 bahasa dunia.
              </p>
            </div>

            {/* Language Selector Box */}
            <div className="flex flex-col items-start lg:items-end gap-1.5 w-full lg:w-auto">
              <div className="flex items-center gap-2 bg-slate-100 dark:bg-slate-800 p-2 rounded-xl border border-slate-200 dark:border-slate-700 w-full sm:w-auto shadow-sm">
                <Globe className="w-4 h-4 text-yellow-500 shrink-0 ml-1" />
                <div className="flex flex-col sm:flex-row sm:items-center gap-1">
                  <span className="text-[11px] font-medium text-slate-500 dark:text-slate-400 shrink-0">
                    Bahasa Terjemahan & Suara:
                  </span>
                  <select
                    value={selectedLang}
                    onChange={(e) => {
                      setSelectedLang(e.target.value);
                      localStorage.setItem("kamus_lang", e.target.value);
                      showToast(`Bahasa diubah ke ${e.target.value.toUpperCase()}`);
                    }}
                    className="bg-transparent text-xs font-bold text-slate-800 dark:text-slate-100 py-1 px-2 focus:outline-none cursor-pointer rounded"
                    title="Pilih Bahasa Terjemahan & Suara"
                  >
                    {Object.entries(groupedLanguages).map(([region, langs]) => (
                      <optgroup key={region} label={region} className="bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-200 font-bold">
                        {langs.map((l) => (
                          <option key={l.code} value={l.code} className="bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-200 font-normal">
                            {l.code.toUpperCase()} — {l.name}
                          </option>
                        ))}
                      </optgroup>
                    ))}
                  </select>
                </div>
              </div>

              {/* Translation Source Badge */}
              <div className="inline-flex items-center gap-1.5 text-[11px] text-slate-500 dark:text-slate-400 px-2 py-0.5 rounded-md bg-slate-100/80 dark:bg-slate-800/80 border border-slate-200/60 dark:border-slate-700/60">
                <Info className="w-3.5 h-3.5 text-yellow-500 shrink-0" />
                <span>
                  Terjemahan: <strong className="text-slate-700 dark:text-slate-200">{TRANSLATION_SOURCES[selectedLang] || "Kementerian Agama RI (Kemenag)"}</strong>
                </span>
              </div>
            </div>
          </div>

          {/* Tab Switcher Bar (Visible when in a dictionary) */}
          {activeDict !== "portal" && (
            <div className="flex items-center gap-2 overflow-x-auto py-3 mt-6 border-t border-slate-200 dark:border-slate-800 no-scrollbar">
              <button
                onClick={() => setActiveDict("portal")}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition bg-slate-200/70 dark:bg-slate-800 hover:bg-slate-300 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 shrink-0"
              >
                <Home className="w-3.5 h-3.5" />
                <span>Menu Utama</span>
              </button>
              <button
                onClick={() => setActiveDict("jamid")}
                className={`inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs font-semibold transition shrink-0 ${
                  activeDict === "jamid"
                    ? "bg-yellow-500 text-slate-900 font-bold shadow-sm"
                    : "bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700"
                }`}
              >
                <BookMarked className="w-3.5 h-3.5" />
                <span>Kamus Jamid Mabny</span>
              </button>
              <button
                onClick={() => setActiveDict("harf")}
                className={`inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs font-semibold transition shrink-0 ${
                  activeDict === "harf"
                    ? "bg-yellow-500 text-slate-900 font-bold shadow-sm"
                    : "bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700"
                }`}
              >
                <BookOpen className="w-3.5 h-3.5" />
                <span>Kamus Harf Ghair 'Amil</span>
              </button>
              <button
                onClick={() => setActiveDict("harf_amil")}
                className={`inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs font-semibold transition shrink-0 ${
                  activeDict === "harf_amil"
                    ? "bg-yellow-500 text-slate-900 font-bold shadow-sm"
                    : "bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700"
                }`}
              >
                <PenTool className="w-3.5 h-3.5" />
                <span>Kamus Harf 'Amil</span>
              </button>
              <button
                onClick={() => setActiveDict("musytaq")}
                className={`inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg text-xs font-semibold transition shrink-0 ${
                  activeDict === "musytaq"
                    ? "bg-yellow-500 text-slate-900 font-bold shadow-sm"
                    : "bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700"
                }`}
              >
                <Sprout className="w-3.5 h-3.5" />
                <span>Kamus Musytaq (80 Akar)</span>
              </button>
            </div>
          )}
        </div>
      </header>

      {/* Main Content Area */}
      <main className="container mx-auto px-4 py-8 max-w-6xl">
        {/* VIEW 1: PORTAL / HUB 4 CARDS */}
        {activeDict === "portal" && (
          <section className="py-4">
            <div className="text-center mb-8">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 mb-2">
                <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                <span>Eksplorasi Linguistik Al-Qur'an Interaktif</span>
              </div>
              <h2 className="text-2xl md:text-3xl font-bold text-slate-900 dark:text-white">
                Pilih Kamus untuk Memulai Eksplorasi
              </h2>
              <p className="text-sm text-slate-500 dark:text-slate-400 mt-2 max-w-2xl mx-auto leading-relaxed">
                Koleksi komprehensif kamus kata gramatika, partikel harf, dan morfologi tasrif Al-Qur'an dengan terjemahan 39 bahasa serta audio tilawah.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
              {/* Card 1: Jamid Mabny */}
              <div
                onClick={() => setActiveDict("jamid")}
                className="group relative bg-white dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700/80 hover:border-yellow-500/50 dark:hover:border-yellow-500/50 rounded-2xl p-5 cursor-pointer transition-all duration-300 hover:shadow-lg hover:-translate-y-1 flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between mb-4">
                    <div className="w-12 h-12 rounded-xl bg-yellow-500/10 text-yellow-500 flex items-center justify-center border border-yellow-500/20 group-hover:bg-yellow-500 group-hover:text-slate-900 transition">
                      <BookMarked className="w-6 h-6" />
                    </div>
                    <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300">
                      7 Bentuk Kata
                    </span>
                  </div>
                  <h3 className="text-lg font-bold text-slate-900 dark:text-white group-hover:text-yellow-500 transition">
                    Kamus Jamid Mabny
                  </h3>
                  <p className="text-xs text-slate-500 dark:text-slate-400 mt-2 leading-relaxed">
                    Kamus interaktif kata ganti (Dhamir), kata sambung (Isim Mawshul), kata tanya (Istifham), syarat, isyarat, isim fi'il, dan fi'il jamid dengan 299 ayat syahid.
                  </p>
                </div>
                <div className="mt-6 pt-4 border-t border-slate-100 dark:border-slate-700/60 flex items-center justify-between text-xs font-semibold text-yellow-600 dark:text-yellow-400">
                  <span className="text-slate-400 font-normal">299 Ayat Syahid</span>
                  <div className="flex items-center gap-1">
                    <span>Buka Kamus</span>
                    <ArrowRight className="w-4 h-4 transform group-hover:translate-x-1 transition" />
                  </div>
                </div>
              </div>

              {/* Card 2: Harf Ghair 'Amil */}
              <div
                onClick={() => setActiveDict("harf")}
                className="group relative bg-white dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700/80 hover:border-yellow-500/50 dark:hover:border-yellow-500/50 rounded-2xl p-5 cursor-pointer transition-all duration-300 hover:shadow-lg hover:-translate-y-1 flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between mb-4">
                    <div className="w-12 h-12 rounded-xl bg-yellow-500/10 text-yellow-500 flex items-center justify-center border border-yellow-500/20 group-hover:bg-yellow-500 group-hover:text-slate-900 transition">
                      <BookOpen className="w-6 h-6" />
                    </div>
                    <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300">
                      17 Bentuk Harf
                    </span>
                  </div>
                  <h3 className="text-lg font-bold text-slate-900 dark:text-white group-hover:text-yellow-500 transition">
                    Kamus Harf Ghair 'Amil
                  </h3>
                  <p className="text-xs text-slate-500 dark:text-slate-400 mt-2 leading-relaxed">
                    Partikel huruf Al-Qur'an yang tidak beramal (tidak mengubah harakat i'rab kata setelahnya), mencakup huruf nafy, istifham, jawab, dan tanbih.
                  </p>
                </div>
                <div className="mt-6 pt-4 border-t border-slate-100 dark:border-slate-700/60 flex items-center justify-between text-xs font-semibold text-yellow-600 dark:text-yellow-400">
                  <span className="text-slate-400 font-normal">187 Ayat Syahid</span>
                  <div className="flex items-center gap-1">
                    <span>Buka Kamus</span>
                    <ArrowRight className="w-4 h-4 transform group-hover:translate-x-1 transition" />
                  </div>
                </div>
              </div>

              {/* Card 3: Harf 'Amil */}
              <div
                onClick={() => setActiveDict("harf_amil")}
                className="group relative bg-white dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700/80 hover:border-yellow-500/50 dark:hover:border-yellow-500/50 rounded-2xl p-5 cursor-pointer transition-all duration-300 hover:shadow-lg hover:-translate-y-1 flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between mb-4">
                    <div className="w-12 h-12 rounded-xl bg-yellow-500/10 text-yellow-500 flex items-center justify-center border border-yellow-500/20 group-hover:bg-yellow-500 group-hover:text-slate-900 transition">
                      <PenTool className="w-6 h-6" />
                    </div>
                    <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300">
                      6 Kategori Harf
                    </span>
                  </div>
                  <h3 className="text-lg font-bold text-slate-900 dark:text-white group-hover:text-yellow-500 transition">
                    Kamus Harf 'Amil
                  </h3>
                  <p className="text-xs text-slate-500 dark:text-slate-400 mt-2 leading-relaxed">
                    Partikel huruf operatif yang aktif memengaruhi dan menentukan i'rab kata setelahnya (jar, nashab, jazam), lengkap kaidah nahwu & contoh ayat.
                  </p>
                </div>
                <div className="mt-6 pt-4 border-t border-slate-100 dark:border-slate-700/60 flex items-center justify-between text-xs font-semibold text-yellow-600 dark:text-yellow-400">
                  <span className="text-slate-400 font-normal">213 Ayat Syahid</span>
                  <div className="flex items-center gap-1">
                    <span>Buka Kamus</span>
                    <ArrowRight className="w-4 h-4 transform group-hover:translate-x-1 transition" />
                  </div>
                </div>
              </div>

              {/* Card 4: Musytaq */}
              <div
                onClick={() => setActiveDict("musytaq")}
                className="group relative bg-white dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700/80 hover:border-yellow-500/50 dark:hover:border-yellow-500/50 rounded-2xl p-5 cursor-pointer transition-all duration-300 hover:shadow-lg hover:-translate-y-1 flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between mb-4">
                    <div className="w-12 h-12 rounded-xl bg-yellow-500/10 text-yellow-500 flex items-center justify-center border border-yellow-500/20 group-hover:bg-yellow-500 group-hover:text-slate-900 transition">
                      <Sprout className="w-6 h-6" />
                    </div>
                    <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300">
                      80 Akar Kata
                    </span>
                  </div>
                  <h3 className="text-lg font-bold text-slate-900 dark:text-white group-hover:text-yellow-500 transition">
                    Kamus Musytaq
                  </h3>
                  <p className="text-xs text-slate-500 dark:text-slate-400 mt-2 leading-relaxed">
                    Eksplorasi morfologi, wazan sharaf, bentuk asal, dan kaidah I'lal dari 80 akar kata Al-Qur'an dalam 3.012 tasrif terstruktur per baris.
                  </p>
                </div>
                <div className="mt-6 pt-4 border-t border-slate-100 dark:border-slate-700/60 flex items-center justify-between text-xs font-semibold text-yellow-600 dark:text-yellow-400">
                  <span className="text-slate-400 font-normal">3.012 Tasrif</span>
                  <div className="flex items-center gap-1">
                    <span>Buka Kamus</span>
                    <ArrowRight className="w-4 h-4 transform group-hover:translate-x-1 transition" />
                  </div>
                </div>
              </div>
            </div>
          </section>
        )}

        {/* LOADING INDICATOR */}
        {loadingDict && (
          <div className="py-16 text-center">
            <div className="w-10 h-10 border-4 border-yellow-500/20 border-t-yellow-500 rounded-full animate-spin mx-auto mb-3" />
            <p className="text-sm text-slate-500 dark:text-slate-400">Memuat data kamus...</p>
          </div>
        )}

        {/* VIEW 2: STANDARD DICTIONARIES (Jamid, Harf Ghair Amil, Harf Amil) */}
        {!loadingDict && ["jamid", "harf", "harf_amil"].includes(activeDict) && (
          <div>
            {/* Filter Dropdowns Card */}
            <div className="bg-white dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/80 rounded-2xl p-4 md:p-6 mb-6 shadow-sm">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {/* Select 1: Bentuk Kata */}
                <div>
                  <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-1.5">
                    1. Pilih Bentuk Kata
                  </label>
                  <div className="relative">
                    <select
                      value={selectedBentuk}
                      onChange={(e) => setSelectedBentuk(e.target.value)}
                      className="w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-100 text-sm rounded-xl py-2.5 px-3.5 pr-9 appearance-none focus:outline-none focus:ring-2 focus:ring-yellow-500/50"
                    >
                      {bentukKataList.map((b) => (
                        <option key={b} value={b}>
                          {b}
                        </option>
                      ))}
                    </select>
                    <ChevronDown className="w-4 h-4 text-slate-400 absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none" />
                  </div>
                </div>

                {/* Select 2: Nomor Kata */}
                <div>
                  <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-1.5">
                    2. Pilih Nomor Kata & Lafadz
                  </label>
                  <div className="relative">
                    <select
                      value={selectedNoKata}
                      onChange={(e) => setSelectedNoKata(e.target.value)}
                      className="w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-100 text-sm rounded-xl py-2.5 px-3.5 pr-9 appearance-none focus:outline-none focus:ring-2 focus:ring-yellow-500/50"
                    >
                      {noKataList.map((n) => (
                        <option key={n.no} value={n.no}>
                          No. {n.no}: {n.kata} {n.latin ? `(${n.latin})` : ""} — {n.arti}
                        </option>
                      ))}
                    </select>
                    <ChevronDown className="w-4 h-4 text-slate-400 absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none" />
                  </div>
                </div>
              </div>
            </div>

            {/* Spotlight Card */}
            {currentSpotlight && (
              <div className="bg-white dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/80 rounded-2xl p-6 mb-8 shadow-sm">
                <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 border-b border-slate-100 dark:border-slate-700/60 pb-5">
                  <div className="flex flex-wrap items-center gap-2">
                    <span className="px-2.5 py-1 rounded-lg text-xs font-bold bg-yellow-500/15 text-yellow-600 dark:text-yellow-400 border border-yellow-500/30">
                      {currentSpotlight["Bentuk Kata"] || currentSpotlight.bentuk_kata}
                    </span>
                    <span className="px-2.5 py-1 rounded-lg text-xs font-semibold bg-slate-100 dark:bg-slate-700 text-slate-700 dark:text-slate-200">
                      No. Kata: {currentSpotlight["No kata"] || currentSpotlight.no_kata}
                    </span>
                    {(currentSpotlight["Jenis"] || currentSpotlight.jenis) && (
                      <span className="px-2.5 py-1 rounded-lg text-xs font-semibold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20">
                        {currentSpotlight["Jenis"] || currentSpotlight.jenis}
                      </span>
                    )}
                  </div>

                  {/* Actions */}
                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => copyDeepLink(activeDict, selectedNoKata)}
                      className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-slate-100 dark:bg-slate-700 hover:bg-slate-200 dark:hover:bg-slate-600 text-slate-700 dark:text-slate-200 transition"
                      title="Salin Link Kata"
                    >
                      <Copy className="w-3.5 h-3.5" />
                      <span>Salin Link</span>
                    </button>
                    <button
                      onClick={shareWordToWhatsApp}
                      className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-emerald-600 hover:bg-emerald-700 text-white transition shadow-sm"
                      title="Bagikan ke WhatsApp"
                    >
                      <MessageCircle className="w-3.5 h-3.5" />
                      <span>Kirim WA</span>
                    </button>
                  </div>
                </div>

                {/* Spotlight Body */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6 pt-6 items-center">
                  {/* Arabic Word Display */}
                  <div className="md:col-span-1 text-center md:text-left">
                    <div className="flex items-center justify-center md:justify-start gap-3 mb-2">
                      <div className="text-4xl md:text-5xl font-bold font-arabic text-yellow-500">
                        {currentSpotlight["Kata"] || currentSpotlight.kata}
                      </div>
                      <button
                        onClick={() => playArabicAudio(currentSpotlight["Kata"] || currentSpotlight.kata)}
                        className="p-2 rounded-full bg-slate-100 dark:bg-slate-700/80 hover:bg-yellow-500/20 text-slate-600 dark:text-slate-300 hover:text-yellow-500 transition"
                        title="Dengarkan Pelafalan Arab"
                      >
                        <Volume2 className="w-4 h-4" />
                      </button>
                    </div>
                    {(currentSpotlight["Latin"] || currentSpotlight.latin) && (
                      <div className="inline-block px-2.5 py-0.5 rounded-md text-xs font-semibold bg-slate-100 dark:bg-slate-700/60 text-slate-600 dark:text-slate-300 tracking-wider">
                        {currentSpotlight["Latin"] || currentSpotlight.latin}
                      </div>
                    )}
                    <div className="text-lg font-bold text-slate-900 dark:text-white mt-2">
                      {currentSpotlight["Arti kata"] || currentSpotlight.arti_kata || currentSpotlight["Arti"]}
                    </div>
                    {(currentSpotlight["Keterangan"] || currentSpotlight.keterangan) && (
                      <div className="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">
                        {currentSpotlight["Keterangan"] || currentSpotlight.keterangan}
                      </div>
                    )}
                  </div>

                  {/* Metrics */}
                  <div className="md:col-span-2 grid grid-cols-2 gap-4">
                    <div className="bg-slate-50 dark:bg-slate-900/70 border border-slate-200/80 dark:border-slate-700/60 rounded-xl p-4">
                      <div className="text-xs text-slate-500 dark:text-slate-400 font-medium">
                        Frekuensi dalam Al-Qur'an
                      </div>
                      <div className="text-2xl font-bold text-yellow-500 mt-1">
                        {currentSpotlight["Frek kata"] || currentSpotlight.frek_kata || "-"} ×
                      </div>
                      <div className="text-[11px] text-slate-400 mt-1">Frekuensi Kemunculan</div>
                    </div>
                    <div className="bg-slate-50 dark:bg-slate-900/70 border border-slate-200/80 dark:border-slate-700/60 rounded-xl p-4">
                      <div className="text-xs text-slate-500 dark:text-slate-400 font-medium">
                        Total Referensi Ayat
                      </div>
                      <div className="text-2xl font-bold text-emerald-500 mt-1">
                        {currentReferences.length} Ayat
                      </div>
                      <div className="text-[11px] text-slate-400 mt-1">Tersedia dalam Dataset</div>
                    </div>
                  </div>
                </div>
              </div>
            )}

            {/* References Section */}
            <div className="mt-8">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-4">
                <h3 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
                  <FileText className="w-4 h-4 text-yellow-500" />
                  <span>Daftar Surat & Ayat yang Keluar ({currentReferences.length})</span>
                </h3>

                {/* Filter Search inside references */}
                <div className="relative w-full sm:w-72">
                  <input
                    type="text"
                    value={ayatFilterQuery}
                    onChange={(e) => setAyatFilterQuery(e.target.value)}
                    placeholder="Cari nama surat / ayat..."
                    className="w-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-xs rounded-xl py-2 pl-8 pr-3 text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-yellow-500/40"
                  />
                  <Search className="w-3.5 h-3.5 text-slate-400 absolute left-2.5 top-1/2 -translate-y-1/2" />
                </div>
              </div>

              {/* Grid of References */}
              {currentReferences.length === 0 ? (
                <div className="py-12 text-center bg-white dark:bg-slate-800/60 rounded-2xl border border-slate-200 dark:border-slate-700">
                  <BookOpen className="w-8 h-8 text-slate-400 mx-auto mb-2 opacity-50" />
                  <p className="text-sm text-slate-500 dark:text-slate-400">
                    Tidak ada surat atau ayat yang cocok dengan kata pencarian tersebut.
                  </p>
                </div>
              ) : (
                <div className="flex flex-col gap-4">
                  {currentReferences.map((occ, idx) => {
                    const surat = getOccSurat(occ);
                    const ayat = getOccAyat(occ);
                    const namaSurat = getOccSuratNama(occ);
                    const teksArab = getOccTeksArab(occ);
                    const rawArti = getOccRawArti(occ, selectedLang);
                    const translatedArti = getVerseTranslation(surat, ayat, rawArti);
                    const isAudioPlaying = playingAudioKey === `${surat}:${ayat}`;

                    return (
                      <div
                        key={idx}
                        className="bg-white dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/80 rounded-2xl p-5 shadow-sm hover:border-yellow-500/40 transition flex flex-col justify-between"
                      >
                        {/* Card Top Row */}
                        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 dark:border-slate-700/60 pb-3">
                          <div className="flex items-center gap-3">
                            <div className="w-8 h-8 rounded-full bg-yellow-500/15 text-yellow-600 dark:text-yellow-400 font-bold text-xs flex items-center justify-center border border-yellow-500/30 shrink-0">
                              {idx + 1}
                            </div>
                            <div>
                              <div className="text-sm font-bold text-slate-900 dark:text-white">
                                QS. {namaSurat} [{surat}:{ayat}]
                              </div>
                              <div className="text-[11px] text-slate-500 dark:text-slate-400">
                                Surat ke-{surat} • Ayat ke-{ayat}
                              </div>
                            </div>
                          </div>

                          {/* Action Buttons */}
                          <div className="flex items-center gap-2 self-end sm:self-auto">
                            {/* Audio Tilawah Button */}
                            <button
                              onClick={() => toggleVerseAudio(surat, ayat)}
                              className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition ${
                                isAudioPlaying
                                  ? "bg-yellow-500 text-slate-900 font-bold shadow-sm"
                                  : "bg-slate-100 dark:bg-slate-700/80 text-slate-700 dark:text-slate-200 hover:bg-slate-200 dark:hover:bg-slate-600"
                              }`}
                              title={isAudioPlaying ? "Jeda Tilawah" : "Putar Tilawah (Mishary Alafasy)"}
                            >
                              {isAudioPlaying ? <Pause className="w-3.5 h-3.5" /> : <Play className="w-3.5 h-3.5" />}
                              <span>{isAudioPlaying ? "Jeda" : "Tilawah"}</span>
                            </button>

                            {/* Tanya AI Button */}
                            <button
                              onClick={() => handleOpenAiModal(occ, currentSpotlight?.["Kata"] || currentSpotlight?.kata || "", selectedNoKata, selectedBentuk)}
                              className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-purple-500/10 text-purple-600 dark:text-purple-400 hover:bg-purple-500/20 border border-purple-500/20 transition"
                              title="Tanya AI Analisis Nahwu & Tafsir"
                            >
                              <Sparkles className="w-3.5 h-3.5 text-purple-500" />
                              <span>Tanya AI</span>
                            </button>

                            {/* Share to WA */}
                            <button
                              onClick={() => shareAyatToWhatsApp(occ)}
                              className="p-1.5 rounded-lg bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 hover:bg-emerald-500/20 transition"
                              title="Bagikan ke WhatsApp"
                            >
                              <MessageCircle className="w-3.5 h-3.5" />
                            </button>
                          </div>
                        </div>

                        {/* Arabic Text with Word Highlight */}
                        <div className="py-4">
                          <p
                            className="text-2xl md:text-3xl leading-loose text-right font-arabic text-slate-900 dark:text-slate-100"
                            dir="rtl"
                          >
                            {renderHighlightedArabic(teksArab, currentSpotlight?.["Kata"] || currentSpotlight?.kata || "")}
                          </p>
                        </div>

                        {/* Translation Box with TTS Button */}
                        <div className="bg-slate-50 dark:bg-slate-900/60 border border-slate-200/80 dark:border-slate-700/60 rounded-xl p-3.5 mb-3 flex items-start justify-between gap-3">
                          <blockquote className="text-xs md:text-sm text-slate-700 dark:text-slate-300 leading-relaxed italic">
                            "{translatedArti}"
                          </blockquote>
                          <button
                            onClick={() => playTranslationTts(translatedArti)}
                            className="p-1.5 rounded-lg text-slate-400 hover:text-yellow-500 hover:bg-yellow-500/10 transition shrink-0"
                            title="Dengarkan Arti / Terjemahan"
                          >
                            <Volume2 className="w-4 h-4" />
                          </button>
                        </div>

                        {/* Card Footer Link */}
                        <div className="pt-2 border-t border-slate-100 dark:border-slate-700/60 flex items-center justify-end">
                          <Link
                            to={`/qmushaf?surah=${surat}&ayah=${ayat}`}
                            className="text-xs font-semibold text-yellow-600 dark:text-yellow-400 hover:underline inline-flex items-center gap-1"
                          >
                            <span>Lihat di Mushaf Per Kata</span>
                            <ExternalLink className="w-3 h-3" />
                          </Link>
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          </div>
        )}

        {/* VIEW 3: MUSYTAQ (80 AKAR KATA) */}
        {!loadingDict && activeDict === "musytaq" && (
          <div>
            {/* Filter Dropdowns Card */}
            <div className="bg-white dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/80 rounded-2xl p-4 md:p-6 mb-6 shadow-sm">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {/* Select 1: Level */}
                <div>
                  <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-1.5">
                    1. Pilih Level
                  </label>
                  <div className="relative">
                    <select
                      value={musytaqLevel}
                      onChange={(e) => setMusytaqLevel(e.target.value)}
                      className="w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-100 text-sm rounded-xl py-2.5 px-3.5 pr-9 appearance-none focus:outline-none focus:ring-2 focus:ring-yellow-500/50"
                    >
                      <option value="1">Level 1 (80 Akar Kata Terpopuler)</option>
                    </select>
                    <ChevronDown className="w-4 h-4 text-slate-400 absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none" />
                  </div>
                </div>

                {/* Select 2: Nomor Akar & Akar */}
                <div>
                  <label className="block text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-1.5">
                    2. Pilih Nomor Akar & Akar Kata
                  </label>
                  <div className="relative">
                    <select
                      value={musytaqSelectedAkarId}
                      onChange={(e) => setMusytaqSelectedAkarId(e.target.value)}
                      className="w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-100 text-sm rounded-xl py-2.5 px-3.5 pr-9 appearance-none focus:outline-none focus:ring-2 focus:ring-yellow-500/50"
                    >
                      {musytaqRoots.map((r) => (
                        <option key={r.id} value={r.id}>
                          {r.id}. {r.akar} {r.masdar ? `(${r.masdar})` : ""} — {r.arti}
                        </option>
                      ))}
                    </select>
                    <ChevronDown className="w-4 h-4 text-slate-400 absolute right-3 top-1/2 -translate-y-1/2 pointer-events-none" />
                  </div>
                </div>
              </div>
            </div>

            {/* Musytaq Spotlight Hero */}
            {currentMusytaqRoot && (
              <div className="bg-white dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/80 rounded-2xl p-6 mb-8 shadow-sm">
                <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 border-b border-slate-100 dark:border-slate-700/60 pb-5">
                  <div className="flex items-center gap-2">
                    <span className="px-2.5 py-1 rounded-lg text-xs font-bold bg-yellow-500/15 text-yellow-600 dark:text-yellow-400 border border-yellow-500/30">
                      Level {musytaqLevel}
                    </span>
                    <span className="px-2.5 py-1 rounded-lg text-xs font-semibold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20">
                      No. {currentMusytaqRoot.id} ({currentMusytaqRoot.akar})
                    </span>
                  </div>

                  {/* Actions */}
                  <div className="flex items-center gap-2">
                    {/* Tanya AI */}
                    <button
                      onClick={handleOpenMusytaqAiModal}
                      className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-purple-500/10 text-purple-600 dark:text-purple-400 hover:bg-purple-500/20 border border-purple-500/20 transition"
                      title="Tanya AI Seputar Akar Kata Ini"
                    >
                      <Sparkles className="w-3.5 h-3.5 text-purple-500" />
                      <span>Tanya AI</span>
                    </button>
                    <button
                      onClick={() => copyDeepLink("musytaq", currentMusytaqRoot.id)}
                      className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-slate-100 dark:bg-slate-700 hover:bg-slate-200 dark:hover:bg-slate-600 text-slate-700 dark:text-slate-200 transition"
                      title="Salin Link Akar"
                    >
                      <Copy className="w-3.5 h-3.5" />
                      <span>Salin Link</span>
                    </button>
                    <button
                      onClick={shareMusytaqToWhatsApp}
                      className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-emerald-600 hover:bg-emerald-700 text-white transition shadow-sm"
                      title="Bagikan ke WhatsApp"
                    >
                      <MessageCircle className="w-3.5 h-3.5" />
                      <span>Kirim WA</span>
                    </button>
                  </div>
                </div>

                {/* Metrics 3 Columns */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-5">
                  <div className="bg-slate-50 dark:bg-slate-900/70 border border-slate-200/80 dark:border-slate-700/60 rounded-xl p-4">
                    <div className="text-xs text-slate-500 dark:text-slate-400 font-medium">
                      Akar & Bentuk Dasar (Masdar)
                    </div>
                    <div className="text-xl font-bold font-arabic text-yellow-500 mt-1">
                      {currentMusytaqRoot.akar} {currentMusytaqRoot.masdar ? `(${currentMusytaqRoot.masdar})` : ""}
                    </div>
                    <div className="text-xs text-slate-500 dark:text-slate-400 mt-1">
                      Arti: {currentMusytaqRoot.arti}
                    </div>
                  </div>

                  <div className="bg-slate-50 dark:bg-slate-900/70 border border-slate-200/80 dark:border-slate-700/60 rounded-xl p-4">
                    <div className="text-xs text-slate-500 dark:text-slate-400 font-medium">
                      Frekuensi Kemunculan Akar
                    </div>
                    <div className="text-2xl font-bold text-yellow-500 mt-1">
                      {currentMusytaqRoot.frek} ×
                    </div>
                    <div className="text-xs text-slate-500 dark:text-slate-400 mt-1">
                      Frekuensi dalam Al-Qur'an
                    </div>
                  </div>

                  <div className="bg-slate-50 dark:bg-slate-900/70 border border-slate-200/80 dark:border-slate-700/60 rounded-xl p-4">
                    <div className="text-xs text-slate-500 dark:text-slate-400 font-medium">
                      Total Variasi Tasrif
                    </div>
                    <div className="text-2xl font-bold text-emerald-500 mt-1">
                      {currentMusytaqTasrifRows.length} Bentuk
                    </div>
                    <div className="text-xs text-slate-500 dark:text-slate-400 mt-1">
                      Tersedia untuk akar ini
                    </div>
                  </div>
                </div>
              </div>
            )}

            {/* Interactive Tasrif Browser Section */}
            <div className="mt-8">
              <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-4">
                <h3 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
                  <Sprout className="w-4 h-4 text-yellow-500" />
                  <span>Daftar Lengkap Seluruh Bentuk Tasrif Akar: {currentMusytaqRoot?.akar}</span>
                </h3>

                {/* Search input in tasrif */}
                <div className="relative w-full md:w-72">
                  <input
                    type="text"
                    value={musytaqFilterQuery}
                    onChange={(e) => setMusytaqFilterQuery(e.target.value)}
                    placeholder="Cari lafaz / arti / wazan..."
                    className="w-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-xs rounded-xl py-2 pl-8 pr-3 text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-yellow-500/40"
                  />
                  <Search className="w-3.5 h-3.5 text-slate-400 absolute left-2.5 top-1/2 -translate-y-1/2" />
                </div>
              </div>

              {/* Category Filter Chips */}
              <div className="flex items-center gap-2 overflow-x-auto pb-3 mb-4 no-scrollbar">
                {[
                  { id: "all", label: `Semua (${categoryCounts.all})` },
                  { id: "madhi", label: `Fi'il Madhi (${categoryCounts.madhi})` },
                  { id: "mudhari", label: `Fi'il Mudhari' (${categoryCounts.mudhari})` },
                  { id: "amr", label: `Fi'il Amr (${categoryCounts.amr})` },
                  { id: "masdar", label: `Masdar (${categoryCounts.masdar})` },
                  { id: "isim", label: `Isim Fa'il / Sifat (${categoryCounts.isim})` }
                ].map((chip) => (
                  <button
                    key={chip.id}
                    onClick={() => setMusytaqCategory(chip.id)}
                    className={`px-3 py-1.5 rounded-full text-xs font-semibold transition shrink-0 ${
                      musytaqCategory === chip.id
                        ? "bg-yellow-500 text-slate-900 font-bold shadow-sm"
                        : "bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700"
                    }`}
                  >
                    {chip.label}
                  </button>
                ))}
              </div>

              {/* Tasrif Grid */}
              {filteredTasrifList.length === 0 ? (
                <div className="py-12 text-center bg-white dark:bg-slate-800/60 rounded-2xl border border-slate-200 dark:border-slate-700">
                  <Search className="w-8 h-8 text-slate-400 mx-auto mb-2 opacity-50" />
                  <p className="text-sm text-slate-500 dark:text-slate-400">
                    Tidak ada bentuk tasrif yang cocok dengan kata pencarian tersebut.
                  </p>
                </div>
              ) : (
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                  {filteredTasrifList.map((row, idx) => {
                    const lafdz = row["Lafdz"] || row.lafdz || row["Kata"] || "-";
                    const arti = row["Terjemah"] || row.terjemah || row["Arti"] || "-";
                    const bentuk = row["Bentuk Kata"] || row.bentuk_kata || "-";
                    const wazan = row["Teori/i'rab/Wazan/I'lal"] || row.wazan || "-";
                    const asal = row["Asal"] || row.asal || "";
                    const ilal = row["I'lal"] || row.ilal || "";

                    let badgeColor = "bg-purple-500/10 text-purple-600 dark:text-purple-400 border-purple-500/20";
                    if (bentuk.toLowerCase().includes("mudhari")) {
                      badgeColor = "bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border-emerald-500/20";
                    } else if (bentuk.toLowerCase().includes("amr")) {
                      badgeColor = "bg-amber-500/10 text-amber-600 dark:text-amber-400 border-amber-500/20";
                    } else if (bentuk.toLowerCase().includes("masdar")) {
                      badgeColor = "bg-cyan-500/10 text-cyan-600 dark:text-cyan-400 border-cyan-500/20";
                    } else if (bentuk.toLowerCase().includes("isim") || bentuk.toLowerCase().includes("fa'il")) {
                      badgeColor = "bg-yellow-500/10 text-yellow-600 dark:text-yellow-400 border-yellow-500/20";
                    }

                    return (
                      <div
                        key={idx}
                        className="bg-white dark:bg-slate-800/90 border border-slate-200 dark:border-slate-700/80 rounded-2xl p-4 flex flex-col justify-between shadow-sm hover:border-yellow-500/40 transition"
                      >
                        <div>
                          <div className="flex items-center justify-between mb-2">
                            <span className={`text-[11px] font-semibold px-2 py-0.5 rounded-md border ${badgeColor}`}>
                              {bentuk}
                            </span>
                            <div className="flex items-center gap-1">
                              <button
                                onClick={() => shareTasrifRowToWhatsApp(row)}
                                className="p-1 rounded-md text-slate-400 hover:text-emerald-500 transition"
                                title="Bagikan ke WhatsApp"
                              >
                                <MessageCircle className="w-3.5 h-3.5" />
                              </button>
                              <button
                                onClick={() => playArabicAudio(lafdz)}
                                className="p-1 rounded-md text-slate-400 hover:text-yellow-500 transition"
                                title="Dengarkan Lafadz"
                              >
                                <Volume2 className="w-3.5 h-3.5" />
                              </button>
                            </div>
                          </div>

                          <div className="text-2xl font-bold font-arabic text-right text-yellow-500 my-2" dir="rtl">
                            {lafdz}
                          </div>

                          <div className="text-xs font-semibold text-slate-800 dark:text-slate-100">
                            {arti}
                          </div>

                          {wazan && (
                            <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-1 font-mono">
                              Wazan: <span className="font-arabic font-bold text-slate-700 dark:text-slate-300">{wazan}</span>
                            </div>
                          )}

                          {asal && (
                            <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5 font-mono">
                              Asal: <span className="font-arabic text-slate-700 dark:text-slate-300">{asal}</span>
                            </div>
                          )}

                          {ilal && (
                            <div className="text-[10px] text-rose-500/90 dark:text-rose-400/90 mt-1 bg-rose-500/5 p-1 rounded">
                              I'lal: {ilal}
                            </div>
                          )}
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          </div>
        )}
      </main>

      {/* ─── AI ASSISTANT MODAL DIALOG ─────────────────────────────────── */}
      {aiModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm animate-fade-in">
          <div className="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl w-full max-w-xl shadow-2xl overflow-hidden animate-scale-up">
            {/* Modal Header */}
            <div className="p-5 border-b border-slate-100 dark:border-slate-700 flex items-center justify-between bg-slate-50/50 dark:bg-slate-900/50">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-purple-500/10 text-purple-600 dark:text-purple-400 flex items-center justify-center border border-purple-500/20">
                  <Sparkles className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-base font-bold text-slate-900 dark:text-white">
                    Tanya Asisten AI Al-Qur'an
                  </h3>
                  <p className="text-xs text-slate-500 dark:text-slate-400">
                    Analisis Nahwu, I'rab & Tafsir Kata Terpilih
                  </p>
                </div>
              </div>
              <button
                onClick={() => setAiModalOpen(false)}
                className="p-1.5 rounded-lg text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-700 transition"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Modal Body */}
            <div className="p-5 space-y-4 max-h-[70vh] overflow-y-auto">
              {/* Verse Preview */}
              <div className="bg-slate-50 dark:bg-slate-900/80 border border-slate-200 dark:border-slate-700 rounded-xl p-3.5 space-y-2">
                <div className="text-lg font-arabic font-bold text-right text-yellow-500" dir="rtl">
                  {aiContext.teksArab}
                </div>
                <div className="text-xs text-slate-600 dark:text-slate-300 italic">
                  "{aiContext.teksArti}"
                </div>
              </div>

              {/* Topic Selection Chips */}
              <div>
                <label className="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-2">
                  Pilih Topik Analisis AI:
                </label>
                <div className="flex flex-wrap gap-2">
                  {[
                    { id: "nahwu", label: "🔍 Kaidah Nahwu & I'rab" },
                    { id: "tafsir", label: "📖 Tafsir & Makna Ayat" },
                    { id: "balaghah", label: "✨ Keindahan Balaghah" }
                  ].map((t) => (
                    <button
                      key={t.id}
                      onClick={() => setAiTopic(t.id)}
                      className={`px-3 py-1.5 rounded-xl text-xs font-semibold transition ${
                        aiTopic === t.id
                          ? "bg-purple-600 text-white shadow-sm font-bold"
                          : "bg-slate-100 dark:bg-slate-700/70 text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-600"
                      }`}
                    >
                      {t.label}
                    </button>
                  ))}
                </div>
              </div>

              {/* Generated Prompt Preview Textarea */}
              <div>
                <label className="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1.5">
                  Prompt Tanya AI (Siap Digunakan):
                </label>
                <textarea
                  value={generatedAiPrompt}
                  readOnly
                  rows={5}
                  className="w-full bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 text-xs rounded-xl p-3 text-slate-800 dark:text-slate-200 font-mono leading-relaxed focus:outline-none"
                />
              </div>
            </div>

            {/* Modal Footer */}
            <div className="p-4 border-t border-slate-100 dark:border-slate-700 bg-slate-50/50 dark:bg-slate-900/50 flex flex-wrap items-center justify-end gap-2">
              <button
                onClick={() => {
                  window.open(`https://gemini.google.com/app?prompt=${encodeURIComponent(generatedAiPrompt)}`, "_blank");
                }}
                className="inline-flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-bold bg-blue-600 hover:bg-blue-700 text-white transition shadow-sm"
              >
                <Sparkles className="w-3.5 h-3.5" />
                <span>Google Gemini</span>
              </button>

              <button
                onClick={() => {
                  window.open(`https://chatgpt.com/?q=${encodeURIComponent(generatedAiPrompt)}`, "_blank");
                }}
                className="inline-flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-700 text-white transition shadow-sm"
              >
                <MessageCircle className="w-3.5 h-3.5" />
                <span>ChatGPT</span>
              </button>

              <button
                onClick={() => {
                  navigator.clipboard.writeText(generatedAiPrompt).then(() => {
                    showToast("Prompt AI berhasil disalin ke clipboard! 📋");
                  });
                }}
                className="inline-flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-semibold bg-slate-200 dark:bg-slate-700 text-slate-800 dark:text-slate-200 hover:bg-slate-300 dark:hover:bg-slate-600 transition"
              >
                <Copy className="w-3.5 h-3.5" />
                <span>Salin Prompt</span>
              </button>
            </div>
          </div>
        </div>
      )}

      <Footer />
    </div>
  );
};

export default QKamus;
