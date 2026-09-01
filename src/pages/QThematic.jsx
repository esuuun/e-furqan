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

// ─── LANGUAGE CONFIGURATION ──────────────────────────────────────────
const LANG_CONFIG = {
  'id-ID': {
    code: 'id',
    edition: 'id.indonesian',
    label: 'Bahasa Terjemahan & Suara:',
    heroBadge: 'qThematic — Al-Qur’an Tematis',
    heroTitle1: 'Kandungan Al-Qur\'an',
    heroTitle2: 'Berdasarkan Tema & Pembahasan',
    heroDesc: 'Eksplorasi kandungan Al-Qur\'an secara tematis terstruktur, didukung multi-bahasa internasional, fitur pelafalan audio murottal & suara terjemahan (audible), serta pendalaman makna interaktif berbasis AI (AI explorable).',
    labels: ['1. Tema Utama', '2. Pokok Bahasan', '3. Sub Bahasan', '4. Kelompok Uraian'],
    placeholders: ['Pilih Tema', 'Pilih Pokok Bahasan', 'Pilih Sub Pokok Bahasan', 'Semua Kelompok Uraian'],
    translatorLabel: 'Terjemahan:',
    translator: 'Kementerian Agama Republik Indonesia (Kemenag RI)',
    hint: 'Ketuk kartu untuk melihat teks Arab ayat',
    prevBtn: 'Sub Tema Sebelumnya',
    nextBtn: 'Sub Tema Selanjutnya',
    subMeta: count => `Menampilkan ${count} Kelompok Uraian Flash Card`,
    groupMeta: count => `${count} Ayat Al-Qur'an`,
    hideVerses: 'Tutup Semua',
    showVerses: 'Buka Semua',
    playText: 'Dengarkan',
    stopText: 'Hentikan',
    aiText: 'Tanya AI',
    copyText: 'Salin Teks',
    copiedText: 'Tersalin!',
    copyTitle: 'Salin Teks Terjemahan',
    loadingText: 'Memuat terjemahan...',
    errorText: 'Gagal memuat terjemahan',
    connErrorText: 'Koneksi bermasalah',
    emptySelect: 'Silakan pilih kategori di atas untuk melihat ayat.',
    cssClass: '',
    aiPrompt: (surah, ayat, uraian, text) => `Jelaskan singkat QS. ${surah}:${ayat} terkait "${uraian}": "${text}"`
  },
  'en-US': {
    code: 'en',
    edition: 'en.sahih',
    label: 'Translation & Voice Language:',
    heroBadge: 'qThematic — Thematic Qur\'an',
    heroTitle1: 'Qur\'anic Insights',
    heroTitle2: 'By Topic & Thematic Study',
    heroDesc: 'Explore the Qur\'an through structured thematic topics, multi-language translations, audible recitations & voice reading, and interactive AI-driven verse exploration.',
    labels: ['1. Main Theme', '2. Main Topic', '3. Sub Topic', '4. Category Group'],
    placeholders: ['Select Theme', 'Select Topic', 'Select Sub-Topic', 'All Category Groups'],
    translatorLabel: 'Translation:',
    translator: 'Saheeh International',
    hint: 'Tap card to view Arabic text',
    prevBtn: 'Previous Sub-topic',
    nextBtn: 'Next Sub-topic',
    subMeta: count => `Showing ${count} Flashcard Groups`,
    groupMeta: count => `${count} Qur'anic Verses`,
    hideVerses: 'Collapse All',
    showVerses: 'Expand All',
    playText: 'Listen',
    stopText: 'Stop',
    aiText: 'Ask AI',
    copyText: 'Copy Text',
    copiedText: 'Copied!',
    copyTitle: 'Copy Translation Text',
    loadingText: 'Loading translation...',
    errorText: 'Failed to load translation',
    connErrorText: 'Connection error',
    emptySelect: 'Please select a category above to view verses.',
    cssClass: '',
    aiPrompt: (surah, ayat, uraian, text) => `Briefly explain Qur'an ${surah}:${ayat} regarding topic "${uraian}": "${text}"`
  },
  'ar-SA': {
    code: 'ar',
    edition: 'ar.muyassar',
    label: 'لغة الترجمة والصوت:',
    heroBadge: 'qThematic — القرآن الموضوعي',
    heroTitle1: 'موضوعات القرآن الكريم',
    heroTitle2: 'دراسة وتفسير موضوعي',
    heroDesc: 'استكشف معاني القرآن الكريم بشكل موضوعي ومنظم، مع دعم لغات متعددة وتلاوات صوتية واستكشاف تفاعلي بواسطة الذكاء الاصطناعي.',
    labels: ['١. المحور الرئيسي', '٢. الموضوع العام', '٣. الموضوع الفرعي', '٤. مجموعة العناصر'],
    placeholders: ['اختر المحور', 'اختر الموضوع', 'اختر الموضوع الفرعي', 'جميع المجموعات'],
    translatorLabel: 'التفسير:',
    translator: 'Tafsir Al-Muyassar',
    hint: 'انقر على البطاقة لقلبها ومشاهدة النص القرآني',
    prevBtn: 'الموضوع الفرعي السابق',
    nextBtn: 'الموضوع الفرعي التالي',
    subMeta: count => `عرض ${count} من مجموعات البطاقات`,
    groupMeta: count => `${count} آيات من القرآن الكريم`,
    hideVerses: 'إخفاء الآيات',
    showVerses: 'إظهار الآيات',
    playText: 'استماع',
    stopText: 'إيقاف',
    aiText: 'اسأل الذكاء الاصطناعي',
    copyText: 'نسخ النص',
    copiedText: 'تم النسخ!',
    copyTitle: 'نسخ نص الترجمة والتفسير',
    loadingText: 'جارٍ التحميل...',
    errorText: 'فشل في جلب التفسير',
    connErrorText: 'خطأ في الاتصال',
    emptySelect: 'يرجى اختيار الفئة أعلاه لعرض الآيات.',
    cssClass: 'lang-ar',
    aiPrompt: (surah, ayat, uraian, text) => `اشرح بإيجاز سورة ${surah}:${ayat} المتعلقة بموضوع "${uraian}": "${text}"`
  },
  'fr-FR': {
    code: 'fr',
    edition: 'fr.hamidullah',
    label: 'Langue de traduction & voix:',
    heroBadge: 'qThematic — Coran Thématique',
    heroTitle1: 'Enseignements du Coran',
    heroTitle2: 'Par Thème & Étude Thématique',
    heroDesc: 'Explorez le Coran par thèmes structurés, traductions multilingues, récitations audio et exploration interactive assistée par l\'IA.',
    labels: ['1. Thème Principal', '2. Sujet Principal', '3. Sous-Sujet', '4. Groupe de Catégorie'],
    placeholders: ['Sélectionner le Thème', 'Sélectionner le Sujet', 'Sélectionner le Sous-Sujet', 'Tous les Groupes'],
    translatorLabel: 'Traduction:',
    translator: 'Muhammad Hamidullah',
    hint: 'Appuyez sur la carte pour voir le texte arabe',
    prevBtn: 'Sous-thème précédent',
    nextBtn: 'Sous-thème suivant',
    subMeta: count => `Affichage de ${count} groupes de cartes`,
    groupMeta: count => `${count} versets du Coran`,
    hideVerses: 'Tout réduire',
    showVerses: 'Tout développer',
    playText: 'Écouter',
    stopText: 'Arrêter',
    aiText: 'Demander à l\'IA',
    copyText: 'Copier',
    copiedText: 'Copié!',
    copyTitle: 'Copier la traduction',
    loadingText: 'Chargement...',
    errorText: 'Échec du chargement',
    connErrorText: 'Erreur de connexion',
    emptySelect: 'Veuillez sélectionner une catégorie ci-dessus.',
    cssClass: '',
    aiPrompt: (surah, ayat, uraian, text) => `Expliquez brièvement le Coran ${surah}:${ayat} sur le thème "${uraian}": "${text}"`
  },
  'de-DE': {
    code: 'de',
    edition: 'de.bubenheim',
    label: 'Übersetzung & Sprachausgabe:',
    heroBadge: 'qThematic — Thematischer Koran',
    heroTitle1: 'Erkenntnisse des Korans',
    heroTitle2: 'Nach Themen & Studien',
    heroDesc: 'Entdecken Sie den Koran durch strukturierte Themen, mehrsprachige Übersetzungen, Audio-Rezitationen und interaktive KI-gestützte Verserkundung.',
    labels: ['1. Hauptthema', '2. Hauptthema-Bereich', '3. Unterthema', '4. Kategoriegruppe'],
    placeholders: ['Thema wählen', 'Bereich wählen', 'Unterthema wählen', 'Alle Gruppen'],
    translatorLabel: 'Übersetzung:',
    translator: 'A. S. F. Bubenheim & N. Elyas',
    hint: 'Tippe auf die Karte, um den arabischen Text zu sehen',
    prevBtn: 'Vorheriges Unterthema',
    nextBtn: 'Nächstes Unterthema',
    subMeta: count => `${count} Karteikartengruppen werden angezeigt`,
    groupMeta: count => `${count} Koran-Verse`,
    hideVerses: 'Alle einklappen',
    showVerses: 'Alle ausklappen',
    playText: 'Anhören',
    stopText: 'Stopp',
    aiText: 'KI fragen',
    copyText: 'Kopieren',
    copiedText: 'Kopiert!',
    copyTitle: 'Übersetzung kopieren',
    loadingText: 'Wird geladen...',
    errorText: 'Laden fehlgeschlagen',
    connErrorText: 'Verbindungsfehler',
    emptySelect: 'Bitte wähle oben eine Kategorie aus.',
    cssClass: '',
    aiPrompt: (surah, ayat, uraian, text) => `Erkläre kurz Koran ${surah}:${ayat} zum Thema "${uraian}": "${text}"`
  },
  'es-ES': {
    code: 'es',
    edition: 'es.bornez',
    label: 'Idioma de traducción y voz:',
    heroBadge: 'qThematic — Corán Temático',
    heroTitle1: 'Enseñanzas del Corán',
    heroTitle2: 'Por Tema y Estudio Temático',
    heroDesc: 'Explore el Corán a través de temas estructurados, traducciones multilingües, recitaciones en audio y exploración interactiva con Inteligencia Artificial.',
    labels: ['1. Tema Principal', '2. Tema General', '3. Subtema', '4. Grupo de Categoría'],
    placeholders: ['Seleccionar Tema', 'Seleccionar Tema General', 'Seleccionar Subtema', 'Todos los Grupos'],
    translatorLabel: 'Traducción:',
    translator: 'Raúl González Bornez',
    hint: 'Toca la tarjeta para ver el texto en árabe',
    prevBtn: 'Subtema anterior',
    nextBtn: 'Subtema siguiente',
    subMeta: count => `Mostrando ${count} grupos de tarjetas`,
    groupMeta: count => `${count} versículos del Corán`,
    hideVerses: 'Contraer todo',
    showVerses: 'Expandir todo',
    playText: 'Escuchar',
    stopText: 'Detener',
    aiText: 'Preguntar a la IA',
    copyText: 'Copiar',
    copiedText: '¡Copiado!',
    copyTitle: 'Copiar traducción',
    loadingText: 'Cargando traducción...',
    errorText: 'Error al cargar la traducción',
    connErrorText: 'Error de conexión',
    emptySelect: 'Selecciona una categoría arriba para ver los versículos.',
    cssClass: '',
    aiPrompt: (surah, ayat, uraian, text) => `Explica brevemente el Corán ${surah}:${ayat} sobre el tema "${uraian}": "${text}"`
  },
  'tr-TR': {
    code: 'tr',
    edition: 'tr.diyanet',
    label: 'Çeviri ve Ses Dili:',
    heroBadge: 'qThematic — Konulu Kur\'an',
    heroTitle1: 'Kur\'an-ı Kerim Konuları',
    heroTitle2: 'Konulu Çalışma ve Tefsir',
    heroDesc: 'Yapılandırılmış konular, çok dilli çeviriler, sesli tilavetler ve yapay zeka destekli etkileşimli ayet incelemesi ile Kur\'an-ı Kerim\'i keşfedin.',
    labels: ['1. Ana Tema', '2. Ana Konu', '3. Alt Konu', '4. Kategori Grubu'],
    placeholders: ['Tema Seçin', 'Konu Seçin', 'Alt Konu Seçin', 'Tüm Gruplar'],
    translatorLabel: 'Çeviri:',
    translator: 'Diyanet İşleri Başkanlığı',
    hint: 'Arapça metni görmek için karta dokunun',
    prevBtn: 'Önceki Alt Konu',
    nextBtn: 'Sonraki Alt Konu',
    subMeta: count => `${count} bilgi kartı grubu gösteriliyor`,
    groupMeta: count => `${count} Kur'an Ayeti`,
    hideVerses: 'Tümünü Daralt',
    showVerses: 'Tümünü Genişlet',
    playText: 'Dinle',
    stopText: 'Durdur',
    aiText: 'Yapay Zekaya Sor',
    copyText: 'Kopyala',
    copiedText: 'Kopyalandı!',
    copyTitle: 'Metni Kopyala',
    loadingText: 'Çeviri yükleniyor...',
    errorText: 'Çeviri yüklenemedi',
    connErrorText: 'Bağlantı hatası',
    emptySelect: 'Ayetleri görmek için yukarıdan bir kategori seçin.',
    cssClass: '',
    aiPrompt: (surah, ayat, uraian, text) => `Kur'an ${surah}:${ayat} ayetini "${uraian}" konusu bağlamında kısaca açıklayın: "${text}"`
  },
  'ru-RU': {
    code: 'ru',
    edition: 'ru.kuliev',
    label: 'Язык перевода и озвучки:',
    heroBadge: 'qThematic — Тематический Коран',
    heroTitle1: 'Смыслы Корана',
    heroTitle2: 'По Темам и Исследованиям',
    heroDesc: 'Изучайте Коран по структурированным темам с многоязычным переводом, аудиозаписями и интерактивным исследованием аятов с помощью ИИ.',
    labels: ['1. Главная Тема', '2. Основной Раздел', '3. Подраздел', '4. Группа Категорий'],
    placeholders: ['Выберите Тему', 'Выберите Раздел', 'Выберите Подраздел', 'Все Группы'],
    translatorLabel: 'Перевод:',
    translator: 'Эльмир Кулиев (Elmir Kuliev)',
    hint: 'Нажмите на карточку, чтобы увидеть арабский текст',
    prevBtn: 'Предыдущая подтема',
    nextBtn: 'Следующая подтема',
    subMeta: count => `Отображается ${count} групп карточек`,
    groupMeta: count => `${count} аятов Корана`,
    hideVerses: 'Свернуть все',
    showVerses: 'Развернуть все',
    playText: 'Слушать',
    stopText: 'Стоп',
    aiText: 'Спросить ИИ',
    copyText: 'Копировать',
    copiedText: 'Скопировано!',
    copyTitle: 'Копировать текст',
    loadingText: 'Загрузка перевода...',
    errorText: 'Не удалось загрузить',
    connErrorText: 'Ошибка соединения',
    emptySelect: 'Выберите категорию выше для просмотра аятов.',
    cssClass: '',
    aiPrompt: (surah, ayat, uraian, text) => `Кратко объясните Коран ${surah}:${ayat} по теме "${uraian}": "${text}"`
  },
  'zh-CN': {
    code: 'zh',
    edition: 'zh.jian',
    label: '翻译与语音语言：',
    heroBadge: 'qThematic — 主题古兰经',
    heroTitle1: '古兰经要义',
    heroTitle2: '按主题与专题研读',
    heroDesc: '通过结构化主题、多语言翻译、音频朗读以及人工智能交互式经文探索，深入领会古兰经的奥义。',
    labels: ['1. 主主题', '2. 核心主题', '3. 子主题', '4. 分类分组'],
    placeholders: ['选择主题', '选择核心主题', '选择子主题', '所有分组'],
    translatorLabel: '翻译：',
    translator: '马坚 (Ma Jian)',
    hint: '点击卡片查看阿拉伯语原文',
    prevBtn: '上一子主题',
    nextBtn: '下一子主题',
    subMeta: count => `显示 ${count} 个卡片组`,
    groupMeta: count => `${count} 节古兰经文`,
    hideVerses: '折叠全部',
    showVerses: '展开全部',
    playText: '朗读',
    stopText: '停止',
    aiText: '询问 AI',
    copyText: '复制',
    copiedText: '已复制！',
    copyTitle: '复制译文',
    loadingText: '加载翻译中...',
    errorText: '加载失败',
    connErrorText: '连接错误',
    emptySelect: '请在上方选择分类以查看经文。',
    cssClass: '',
    aiPrompt: (surah, ayat, uraian, text) => `简要解释古兰经 ${surah}:${ayat} 关于主题 "${uraian}" 的内容："${text}"`
  },
  'ja-JP': {
    code: 'ja',
    edition: 'ja.japanese',
    label: '翻訳と音声の言語：',
    heroBadge: 'qThematic — テーマ別クルアーン',
    heroTitle1: 'クルアーンの教え',
    heroTitle2: 'テーマ別・分野別研究',
    heroDesc: '体系的なテーマ分類、多言語翻訳、音声朗読、そしてAIを活用した対話型の聖句探求を通じて、クルアーンの教えを深めましょう。',
    labels: ['1. メインテーマ', '2. 主要トピック', '3. サブトピック', '4. カテゴリーグループ'],
    placeholders: ['テーマを選択', 'トピックを選択', 'サブトピックを選択', 'すべてのグループ'],
    translatorLabel: '翻訳：',
    translator: '日本ムスリム協会',
    hint: 'カードをタップしてアラビア語原文を表示',
    prevBtn: '前のサブトピック',
    nextBtn: '次のサブトピック',
    subMeta: count => `${count} 個のカードグループを表示中`,
    groupMeta: count => `${count} 節のクルアーン聖句`,
    hideVerses: 'すべて折りたたむ',
    showVerses: 'すべて展開',
    playText: '再生',
    stopText: '停止',
    aiText: 'AIに質問',
    copyText: 'コピー',
    copiedText: 'コピーしました！',
    copyTitle: '翻訳文をコピー',
    loadingText: '翻訳を読み込み中...',
    errorText: '読み込み失敗',
    connErrorText: '接続エラー',
    emptySelect: '上記からカテゴリーを選択してください。',
    cssClass: '',
    aiPrompt: (surah, ayat, uraian, text) => `クルアーン第${surah}章${ayat}節の「${uraian}」に関する内容を簡単に解説してください：「${text}」`
  }
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
  onStopTTS 
}) => {
  const [isFlipped, setIsFlipped] = useState(false);
  const cfg = LANG_CONFIG[selectedLang] || LANG_CONFIG['id-ID'];

  // Determine text to show: If non-Indonesian, show translatedText or loading text
  let displayText = verse.indo;
  if (selectedLang !== 'id-ID') {
    if (translatedText) {
      displayText = translatedText;
    } else if (isLoadingTranslation) {
      displayText = cfg.loadingText || "Memuat terjemahan...";
    }
  }

  const handleTanyaAI = (e) => {
    e.stopPropagation();
    onStopTTS();
    const prompt = cfg.aiPrompt
      ? cfg.aiPrompt(verse.surah_num, verse.ayat_num, uraianTitle, displayText)
      : `Jelaskan singkat QS. ${verse.surah_num}:${verse.ayat_num} terkait "${uraianTitle}": "${displayText}"`;
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
                  <span>{cfg.loadingText}</span>
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
                title={isPlaying ? cfg.stopText : cfg.playText}
              >
                {isPlaying ? (
                  <>
                    <Square className="w-3.5 h-3.5 animate-pulse" />
                    <span>{cfg.stopText}</span>
                  </>
                ) : (
                  <>
                    <Volume2 className="w-3.5 h-3.5" />
                    <span>{cfg.playText}</span>
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
                <span>{cfg.aiText}</span>
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

  // Translated headers & options state
  const [subTitleTranslation, setSubTitleTranslation] = useState("");
  const [groupTitleTranslations, setGroupTitleTranslations] = useState({});
  const [optionTranslations, setOptionTranslations] = useState({});

  // Audio / TTS state
  const [playingKey, setPlayingKey] = useState(null); // `${surah}:${ayat}`
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
      setCollapsedGroups(new Set()); // Expand all
      setAllCollapsedMode(false);
    } else {
      // Collapse all
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

          // Check if already fetched
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

          // 2. Fallback Google Translate API if Cloud API fails or is unavailable
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
            <span>{cfg.heroBadge || 'qThematic — Al-Qur’an Tematis'}</span>
          </div>

          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white leading-tight mb-6">
            {cfg.heroTitle1 || "Kandungan Al-Qur'an"} <br />
            <span className="text-transparent bg-clip-text bg-linear-to-r from-yellow-500 to-yellow-600">
              {cfg.heroTitle2 || "Berdasarkan Tema & Pembahasan"}
            </span>
          </h1>

          <p className="text-base sm:text-lg text-gray-600 dark:text-gray-300 mb-8 max-w-3xl mx-auto leading-relaxed">
            {cfg.heroDesc}
          </p>

          {/* Multi-Language Selector Dropdown */}
          <div className="mb-8 flex flex-wrap justify-center items-center gap-2">
            <Globe className="w-4 h-4 text-yellow-500" />
            <span className="text-xs font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wider">
              {cfg.label}
            </span>
            <select
              value={selectedLang}
              onChange={(e) => setSelectedLang(e.target.value)}
              className="px-3.5 py-2 rounded-full border border-yellow-500/50 bg-white dark:bg-gray-900 text-xs font-bold text-gray-800 dark:text-gray-200 outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer shadow-xs"
            >
              <option value="id-ID">Bahasa Indonesia</option>
              <option value="en-US">English (Saheeh Intl)</option>
              <option value="ar-SA">العربية (الميسر)</option>
              <option value="fr-FR">Français (Hamidullah)</option>
              <option value="de-DE">Deutsch (Bubenheim)</option>
              <option value="es-ES">Español (Bornez)</option>
              <option value="tr-TR">Türkçe (Diyanet)</option>
              <option value="ru-RU">Русский (Кулиев)</option>
              <option value="zh-CN">中文 (马坚)</option>
              <option value="ja-JP">日本語</option>
            </select>
          </div>

          {/* 4 Cascading Selectors Grid */}
          <div className="bg-white dark:bg-gray-900 p-6 rounded-2xl shadow-xs border border-gray-200 dark:border-gray-800 max-w-4xl mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            
            {/* 1. Tema Utama */}
            <div className="flex flex-col items-start gap-1">
              <label className="text-[11px] font-bold text-gray-400 dark:text-gray-500 uppercase tracking-wider">
                {cfg.labels?.[0] || "1. Tema Utama"}
              </label>
              <select
                value={selectedTema}
                onChange={handleTemaChange}
                className="w-full px-3.5 py-2.5 rounded-xl border border-gray-250 dark:border-gray-800 bg-white dark:bg-gray-900 text-gray-800 dark:text-gray-200 text-sm font-semibold outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer"
              >
                <option value="">{cfg.placeholders?.[0] || "Pilih Tema"}</option>
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
                {cfg.labels?.[1] || "2. Pokok Bahasan"}
              </label>
              <select
                value={selectedPokok}
                onChange={handlePokokChange}
                disabled={!selectedTema}
                className="w-full px-3.5 py-2.5 rounded-xl border border-gray-250 dark:border-gray-800 bg-white dark:bg-gray-900 text-gray-800 dark:text-gray-200 text-sm font-semibold outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed"
              >
                <option value="">{cfg.placeholders?.[1] || "Pilih Pokok Bahasan"}</option>
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
                {cfg.labels?.[2] || "3. Sub Bahasan"}
              </label>
              <select
                value={selectedSub}
                onChange={handleSubChange}
                disabled={!selectedPokok}
                className="w-full px-3.5 py-2.5 rounded-xl border border-gray-250 dark:border-gray-800 bg-white dark:bg-gray-900 text-gray-800 dark:text-gray-200 text-sm font-semibold outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed"
              >
                <option value="">{cfg.placeholders?.[2] || "Pilih Sub Pokok Bahasan"}</option>
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
                {cfg.labels?.[3] || "4. Kelompok Uraian"}
              </label>
              <select
                value={selectedUraian}
                onChange={handleUraianChange}
                disabled={!selectedSub}
                className="w-full px-3.5 py-2.5 rounded-xl border border-gray-250 dark:border-gray-800 bg-white dark:bg-gray-900 text-gray-800 dark:text-gray-200 text-sm font-semibold outline-none focus:ring-2 focus:ring-yellow-500/50 cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed"
              >
                <option value="">{cfg.placeholders?.[3] || "Semua Kelompok Uraian"}</option>
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
              {cfg.emptySelect}
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
                  {cfg.subMeta(displayUraianKeys.length)}
                </p>
              </div>

              <div className="flex items-center gap-3">
                {/* Expand / Collapse All Toggle Button */}
                <button
                  onClick={toggleAllGroups}
                  className="px-5 py-2.5 rounded-full border border-yellow-500 hover:bg-yellow-500 hover:text-white dark:hover:text-gray-900 text-yellow-600 dark:text-yellow-400 text-xs font-bold uppercase tracking-wider transition duration-300 flex items-center gap-2 cursor-pointer shadow-xs whitespace-nowrap"
                >
                  <Layers className="w-4 h-4" />
                  <span>{allCollapsedMode ? cfg.showVerses : cfg.hideVerses}</span>
                </button>
              </div>
            </div>

            {/* Hint Indicator */}
            <div className="inline-flex items-center gap-2 px-4 py-2 mb-10 bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 rounded-full text-xs font-semibold tracking-wide border border-gray-200 dark:border-gray-700">
              <Info className="w-4 h-4 text-yellow-500" />
              <span>{cfg.hint}</span>
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
                          {cfg.groupMeta(verseCount)}
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
                <span>{cfg.prevBtn}</span>
              </button>

              <button
                onClick={handleNextSub}
                disabled={!subOptions || subOptions.indexOf(selectedSub) >= subOptions.length - 1}
                className="px-5 py-2.5 rounded-full border border-gray-250 dark:border-gray-800 hover:bg-gray-50 dark:hover:bg-gray-800 text-gray-700 dark:text-gray-300 disabled:opacity-30 disabled:cursor-not-allowed text-xs font-bold uppercase tracking-wider transition duration-300 flex items-center cursor-pointer gap-1.5"
              >
                <span>{cfg.nextBtn}</span>
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
