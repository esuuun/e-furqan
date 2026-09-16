/**
 * Aplikasi Eksplorasi Dhamir & Harf Al-Qur'an (16 Bahasa Dunia)
 * Logika Dropdown Bentuk Kata, Nomor Kata, Audio Tilawah Arab, Audio Terjemahan Multibahasa, & Transliterasi Latin
 */

(function () {
  'use strict';

  // State Management
  const state = {
    activeDict: localStorage.getItem('dhamir_active_dict') || 'jamid', // 'jamid' | 'harf' | 'harf_amil' | 'musytaq'
    selectedMusytaqLevel: 1,
    selectedMusytaqAkarNo: 1,
    selectedMusytaqTasrifIndex: 0,
    musytaqCategoryFilter: 'madhi',
    musytaqSearchQuery: '',
    lang: ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa', 'ja', 'ko', 'nl', 'it', 'bs', 'sq', 'th', 'ber', 'am', 'az', 'bg', 'cs', 'dv', 'no', 'pl', 'ro', 'sv', 'tg', 'ta', 'tt', 'ug', 'uz', 'ku'].includes(localStorage.getItem('dhamir_lang')) ? localStorage.getItem('dhamir_lang') : 'id',
    selectedBentuk: '',
    selectedNoKata: '',
    currentAyatIndex: 0,
    searchQuery: '',
    theme: localStorage.getItem('dhamir_theme') || 'dark'
  };

  const I18N = {
    hi: {
      pageTitle: "जामिद मबनी शब्दकोश | संवादात्मक क़ुरआनी शब्द और आयत संदर्भ",
      brandTitle: "जामिद मबनी <span>शब्दकोश</span>",
      brandSubtitle: "शब्द रूपों और शब्द संख्याओं के लिए संवादात्मक शब्दकोश",
      themeToggleTitle: "डार्क / लाइट थीम बदलें",
      labelLangSelect: "अनुवाद और आवाज़ की भाषा:",
      translationSourceHtml: "अनुवाद: <strong>डॉ. सुहैल फ़ारूक़ ख़ान व डॉ. सैफ़ुर्रहमान नदवी</strong>",
      optgroupEastAsia: "🌏 दक्षिण-पूर्व और पूर्वी एशिया",
      optgroupMidEast: "🕌 मध्य पूर्व, मध्य एशिया और काकेशस",
      optgroupSouthAsia: "🪷 दक्षिण एशिया और हिंद महासागर",
      optgroupAfrica: "🌍 अफ्रीका",
      optgroupEurope: "🏛️ पश्चिमी, उत्तरी, मध्य और पूर्वी यूरोप",
      tabBadgeJamid: "7 शब्द रूप",
      tabBadgeHarf: "17 हर्फ़ रूप",
      
      // Control Card
      step1Label: "१. शब्द का रूप चुनें",
      step1Placeholder: "शब्द का रूप चुनें",
      step1OptionDhamir: "१. सर्वनाम (Dhamir - Pronouns)",
      step1OptionMawshul: "२. संबंधवाचक सर्वनाम (Mawshul - Relative Pronouns)",
      step1OptionIstifham: "३. प्रश्नवाचक शब्द (Istifham - Interrogatives)",
      step1OptionSyarath: "४. शर्तवाचक शब्द (Syarath - Conditionals)",
      step1OptionIsyarah: "५. संकेतवाचक सर्वनाम (Isyarah - Demonstratives)",
      step1OptionIsimFiil: "६. क्रियार्थक संज्ञा (Isim Fi'il - Verbal Nouns)",
      step1OptionFiilJamid: "७. रूढ़ क्रियाएं (Fi'il Jamid - Inflexible Verbs)",
      step2Label: "२. शब्द संख्या चुनें",
      step2Placeholder: "शब्द संख्या चुनें",
      welcomeTitle: "कृपया शब्द का रूप और संख्या चुनें",
      welcomeSubtitle: "अरबी शब्द, अर्थ, क़ुरआन में आवृत्ति (फ्रीक्वेंसी) और आयत संदर्भ देखने के लिए ऊपर दिए गए मेनू से शब्द रूप चुनें।",
      
      // Spotlight Card
      wordFormBadge: "शब्द रूप",
      wordNoBadgePrefix: "शब्द संख्या:",
      arabicVoiceBtn: "अरबी आवाज़",
      arabicVoiceTooltip: "अरबी उच्चारण सुनें (TTS)",
      meaningVoiceBtn: "अर्थ की आवाज़",
      meaningVoiceTooltip: "हिन्दी अर्थ / अनुवाद सुनें (TTS)",
      copyArabicTooltip: "अरबी शब्द कॉपी करें",
      copyInfoBtn: "जानकारी कॉपी करें",
      copyInfoTooltip: "सम्पूर्ण सारांश कॉपी करें",
      freqLabel: "क़ुरआन मजीद में आवृत्ति (फ़्रीक्वेंसी)",
      freqSub: "आगमन की संख्या",
      freqMuttashilVal: "मुत्तसिल (संयुक्त)",
      freqMuttashilSub: "संयुक्त रूप (प्रत्यय / Affix)",
      totalAyatLabel: "कुल संदर्भ आयतें",
      totalAyatSub: "डेटासेट में उपलब्ध",
      sampleAyatSuffix: "उदाहरण आयतें",
      transliterationPrefix: "उच्चारण (Transliteration):",
      meaningPrefix: "अर्थ:",
      
      // References Section
      referencesTitlePrefix: "क़ुरआनी संदर्भ आयतें:",
      ayatCountBadgePattern: (cur, total) => `आयत ${cur} / ${total}`,
      ayatCountZero: "० आयतें",
      searchPlaceholder: "सूरह का नाम / आयत संख्या खोजें...",
      exportCsvBtn: "CSV निर्यात करें",
      exportCsvTooltip: "इस शब्द के सभी आयत संदर्भ CSV फ़ाइल में डाउनलोड करें",
      
      // Ayat Card
      surahPrefix: "सूरह",
      surahPositionTag: (cur, surahNo, ayatNo) => `सूरह #${surahNo} • आयत #${ayatNo}`,
      playTranslationBtn: "अनुवाद सुनें",
      stopTranslationBtn: "आवाज़ बंद करें",
      playTilawahBtn: "तिलावत सुनें",
      pauseTilawahBtn: "तिलावत रोकें",
      askAiBtn: "AI से पूछें",
      askAiTooltip: "इस आयत के व्याकरण और व्याख्या के लिए AI से पूछें",
      aiModalTitle: "क़ुरआनी AI सहायक",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `अध्ययन: सूरह ${suratNama}:${ayat} • शब्द "${kata}" (${noKata})`,
      aiTopicLabel: "AI विश्लेषण का विषय चुनें:",
      aiPromptPreviewLabel: "तैयार AI प्रॉम्प्ट:",
      aiTopicNahwu: "🔍 नहव (व्याकरण) व ए'राब",
      aiTopicTafsir: "📖 तफ़सीर और आयत का अर्थ",
      aiTopicBalaghah: "✨ क़ुरआनी बलाग़त (अलंकार)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "प्रॉम्प्ट कॉपी करें",
      toastPromptCopied: "AI प्रॉम्प्ट क्लिपबोर्ड पर कॉपी हो गया!",
      ayahPill: (n) => `आयत ${n}`,
      flipToArabicBtn: "अरबी पाठ देखें",
      flipToTranslationBtn: "अनुवाद देखें",
      translationBoxHeader: "आयत का अनुवाद (हिन्दी - डॉ. सुहैल फ़ारूक़ ख़ान व डॉ. सैफ़ुर्रहमान नदवी)",
      latinBoxHeader: "रोमन उच्चारण (TRANSLITERATION)",
      copyLatinBtn: "उच्चारण कॉपी करें",
      arabicBoxHeader: "النص القرآني • सम्पूर्ण अरबी आयत",
      latinBackHeader: "रोमन उच्चारण:",
      copyBtn: "कॉपी करें",
      prevBtn: "पिछला",
      nextBtn: "अगला",
      emptyStateText: "आपकी खोज के अनुसार कोई सूरह या आयत नहीं मिली।",
      
      // Toasts & Speech
      toastLangChanged: "भाषा सफलतापूर्वक हिन्दी में बदल दी गई 🇮🇳",
      toastTilawahPaused: "तिलावत रोक दी गई।",
      toastTilawahPlaying: (s, a) => `सूरह ${s}:${a} की अरबी तिलावत जारी है (मिशारी अल-अफ़ासी)`,
      toastTilawahEnded: "तिलावत समाप्त हुई।",
      toastAudioFailed: "ऑडियो लोड करने में त्रुटि। कृपया इंटरनेट कनेक्शन जांचें।",
      toastTranslationStopped: "अनुवाद की आवाज़ बंद कर दी गई।",
      toastTtsNotSupported: "यह ब्राउज़र टेक्स्ट-टू-स्पीच का समर्थन नहीं करता।",
      toastTranslationNotAvail: "अनुवाद उपलब्ध नहीं है।",
      toastSpeakingMeaning: (suratNama, ayat) => `सूरह ${suratNama}:${ayat} का हिन्दी अनुवाद सुनाया जा रहा है`,
      toastSpeakingArabic: (word) => `अरबी शब्द का उच्चारण: ${word}`,
      toastSpeakingWordMeaning: (arti) => `अर्थ सुनाया जा रहा है: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `सूरह ${suratNama}:${ayat} का रोमन उच्चारण सुनाया जा रहा है`,
      toastArabicCopied: (word) => `अरबी शब्द "${word}" कॉपी हो गया!`,
      toastLatinCopied: "रोमन उच्चारण कॉपी हो गया!",
      toastSummaryCopied: "सारांश सफलतापूर्वक कॉपी हो गया!",
      toastCsvExported: (nk) => `शब्द ${nk} का डेटा CSV में निर्यात हो गया!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_hi || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_hi || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'संबंधवाचक सर्वनाम' : 'सर्वनाम';
        return `${prefix} ${cleanWord}, ${latin}अर्थ ${arti}। ${desc ? 'विवरण: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    id: {
      pageTitle: "Kamus Jamid Mabny | Kamus & Rujukan Ayat Interaktif Al-Qur'an",
      brandTitle: "Kamus <span>Jamid Mabny</span>",
      brandSubtitle: "Kamus Interaktif Bentuk Kata & Nomor Kata",
      themeToggleTitle: "Ubah Tema Gelap / Terang",
      labelLangSelect: "Bahasa Terjemahan & Suara:",
      translationSourceHtml: "Terjemahan: <strong>Kementerian Agama RI (Kemenag)</strong>",
      optgroupEastAsia: "🌏 Asia Tenggara & Asia Timur",
      optgroupMidEast: "🕌 Timur Tengah, Asia Tengah & Kaukasus",
      optgroupSouthAsia: "🪷 Asia Selatan & Samudra Hindia",
      optgroupAfrica: "🌍 Afrika",
      optgroupEurope: "🏛️ Eropa Barat, Utara, Tengah & Timur",
      tabBadgeJamid: "7 Bentuk Kata",
      tabBadgeHarf: "17 Bentuk Harf",
      
      // Control Card
      step1Label: "Pilih Bentuk Kata",
      step1Placeholder: "Pilih Bentuk Kata",
      step1OptionDhamir: "1. Dhamir (Kata Ganti)",
      step1OptionMawshul: "2. Mawshul (Kata Sambung)",
      step1OptionIstifham: "3. Istifham (Kata Tanya)",
      step1OptionSyarath: "4. Syarath (Kata Syarat / Pengandaian)",
      step1OptionIsyarah: "5. Isyarah (Kata Tunjuk)",
      step1OptionIsimFiil: "6. Isim Fi'il (Kata Benda Makna Kerja)",
      step1OptionFiilJamid: "7. Fi'il Jamid (Kata Kerja Statis / Kaku)",
      step2Label: "Pilih Nomor Kata",
      step2Placeholder: "Pilih Nomor Kata",
      welcomeTitle: "Silakan Pilih Bentuk Kata & Nomor Kata",
      welcomeSubtitle: "Pilih Bentuk Kata (Dhamir / Mawshul) pada menu di atas untuk menampilkan telaah lafaz Arab, arti kata, frekuensi, dan daftar rujukan ayat Al-Qur'an.",
      
      // Spotlight Card
      wordFormBadge: "Bentuk Kata",
      wordNoBadgePrefix: "No. Kata:",
      arabicVoiceBtn: "Suara Arab",
      arabicVoiceTooltip: "Dengarkan Pelafalan Arab (TTS Arab)",
      meaningVoiceBtn: "Suara Arti",
      meaningVoiceTooltip: "Dengarkan Arti / Terjemahan (Bahasa Indonesia)",
      copyArabicTooltip: "Salin Lafaz Arab",
      copyInfoBtn: "Salin Info",
      copyInfoTooltip: "Salin Ringkasan Lengkap",
      freqLabel: "Frekuensi dalam Al-Qur'an",
      freqSub: "Frekuensi Kemunculan",
      freqMuttashilVal: "Muttashil",
      freqMuttashilSub: "Bentuk Sambung (Imbuhan)",
      totalAyatLabel: "Total Referensi Ayat",
      totalAyatSub: "Tersedia dalam Dataset",
      sampleAyatSuffix: "Contoh Ayat",
      transliterationPrefix: "Transliterasi:",
      meaningPrefix: "Makna:",
      
      // References Section
      referencesTitlePrefix: "Rujukan Ayat untuk",
      ayatCountBadgePattern: (cur, total) => `Contoh ${cur} dari ${total} Ayat`,
      ayatCountZero: "0 Ayat",
      searchPlaceholder: "Cari nama surat / ayat...",
      exportCsvBtn: "Ekspor CSV",
      exportCsvTooltip: "Ekspor daftar ayat kata ini ke CSV",
      
      // Ayat Card
      surahPrefix: "QS.",
      surahPositionTag: (cur, surahNo, ayatNo) => `Surat ke-${surahNo} • Ayat ke-${ayatNo}`,
      playTranslationBtn: "Putar Terjemahan",
      stopTranslationBtn: "Hentikan Suara",
      playTilawahBtn: "Putar Tilawah",
      pauseTilawahBtn: "Jeda Tilawah",
      askAiBtn: "Tanya AI",
      askAiTooltip: "Tanya AI tentang analisis tata bahasa & tafsir ayat ini",
      aiModalTitle: "Tanya Asisten AI Al-Qur'an",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Kajian QS. ${suratNama}:${ayat} • Kata "${kata}" (${noKata})`,
      aiTopicLabel: "Pilih Topik Analisis AI:",
      aiPromptPreviewLabel: "Prompt Tanya AI (Siap Digunakan):",
      aiTopicNahwu: "🔍 Kaidah Nahwu & I'rab",
      aiTopicTafsir: "📖 Tafsir & Makna Ayat",
      aiTopicBalaghah: "✨ Keindahan Balaghah",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Salin Prompt",
      toastPromptCopied: "Prompt Tanya AI berhasil disalin!",
      ayahPill: (n) => `Ayat ${n}`,
      flipToArabicBtn: "Lihat Teks Arab",
      flipToTranslationBtn: "Lihat Terjemahan",
      translationBoxHeader: "ARTI / TERJEMAHAN AYAT (BAHASA INDONESIA)",
      latinBoxHeader: "BACAAN LATIN (TRANSLITERASI KEMENAG)",
      copyLatinBtn: "Salin Latin",
      arabicBoxHeader: "النص القرآني • TEKS ARAB AYAT LENGKAP",
      latinBackHeader: "BACAAN LATIN:",
      copyBtn: "Salin",
      prevBtn: "Sebelumnya",
      nextBtn: "Selanjutnya",
      emptyStateText: "Tidak ada surat atau ayat yang cocok dengan kata pencarian tersebut.",
      
      // Toasts & Speech
      toastLangChanged: "Bahasa berhasil diubah ke Bahasa Indonesia 🇮🇩",
      toastTilawahPaused: "Tilawah dijeda.",
      toastTilawahPlaying: (s, a) => `Memutar tilawah QS. ${s}:${a} (Mishary Alafasy)`,
      toastTilawahEnded: "Tilawah selesai.",
      toastAudioFailed: "Gagal memuat audio ayat. Pastikan koneksi internet aktif.",
      toastTranslationStopped: "Audio terjemahan dihentikan.",
      toastTtsNotSupported: "Fitur suara tidak didukung di browser ini.",
      toastTranslationNotAvail: "Teks terjemahan tidak tersedia.",
      toastSpeakingMeaning: (suratNama, ayat) => `Membacakan arti QS. ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Melafalkan lafaz Arab: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Membacakan arti: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Melafalkan teks Latin QS. ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Lafaz "${word}" disalin!`,
      toastLatinCopied: "Teks Latin berhasil disalin!",
      toastSummaryCopied: "Ringkasan data berhasil disalin!",
      toastCsvExported: (nk) => `Berhasil mengekspor data ${nk} ke CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Isim Mawshul' : 'Dhamir';
        return `${prefix} ${cleanWord}, ${latin}artinya ${arti}. ${desc ? 'Makna: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    en: {
      pageTitle: "Jamid Mabny Dictionary | Interactive Quranic Word & Verse References",
      brandTitle: "<span>Jamid Mabny</span> Dictionary",
      brandSubtitle: "Interactive Dictionary for Word Forms & Word Numbers",
      themeToggleTitle: "Toggle Dark / Light Theme",
      labelLangSelect: "Translation & Voice Language:",
      translationSourceHtml: "Translation: <strong>Sahih International</strong>",
      optgroupEastAsia: "🌏 Southeast & East Asia",
      optgroupMidEast: "🕌 Middle East, Central Asia & Caucasus",
      optgroupSouthAsia: "🪷 South Asia & Indian Ocean",
      optgroupAfrica: "🌍 Africa",
      optgroupEurope: "🏛️ West, North, Central & East Europe",
      tabBadgeJamid: "7 Word Forms",
      tabBadgeHarf: "17 Harf Forms",
      
      // Control Card
      step1Label: "Select Word Form",
      step1Placeholder: "Select Word Form",
      step1OptionDhamir: "1. Pronouns (Dhamir)",
      step1OptionMawshul: "2. Relative Pronouns (Mawshul)",
      step1OptionIstifham: "3. Interrogatives (Istifham - Question Words)",
      step1OptionSyarath: "4. Conditionals (Syarath - Conditional Words)",
      step1OptionIsyarah: "5. Demonstratives (Isyarah - Pointing Words)",
      step1OptionIsimFiil: "6. Verbal Nouns (Isim Fi'il)",
      step1OptionFiilJamid: "7. Inflexible Verbs (Fi'il Jamid)",
      step2Label: "Select Word Number",
      step2Placeholder: "Select Word Number",
      welcomeTitle: "Please Select a Word Form & Word Number",
      welcomeSubtitle: "Select a Word Form (Dhamir / Mawshul) from the menu above to explore Arabic text, meanings, frequency, and Quranic verse references.",
      
      // Spotlight Card
      wordFormBadge: "Word Form",
      wordNoBadgePrefix: "Word No:",
      arabicVoiceBtn: "Arabic Audio",
      arabicVoiceTooltip: "Listen to Arabic Pronunciation (Arabic TTS)",
      meaningVoiceBtn: "Meaning Audio",
      meaningVoiceTooltip: "Listen to Meaning / Translation (English TTS)",
      copyArabicTooltip: "Copy Arabic Text",
      copyInfoBtn: "Copy Info",
      copyInfoTooltip: "Copy Full Summary",
      freqLabel: "Frequency in the Qur'an",
      freqSub: "Occurrence Frequency",
      freqMuttashilVal: "Attached",
      freqMuttashilSub: "Attached Suffix/Prefix Form",
      totalAyatLabel: "Total Verse References",
      totalAyatSub: "Available in Dataset",
      sampleAyatSuffix: "Sample Verses",
      transliterationPrefix: "Transliteration:",
      meaningPrefix: "Meaning:",
      
      // References Section
      referencesTitlePrefix: "Verse References for",
      ayatCountBadgePattern: (cur, total) => `Sample ${cur} of ${total} Verses`,
      ayatCountZero: "0 Verses",
      searchPlaceholder: "Search surah name / verse...",
      exportCsvBtn: "Export CSV",
      exportCsvTooltip: "Export verse references of this word to CSV",
      
      // Ayat Card
      surahPrefix: "Surah",
      surahPositionTag: (cur, surahNo, ayatNo) => `Surah #${surahNo} • Ayah #${ayatNo}`,
      playTranslationBtn: "Play Translation",
      stopTranslationBtn: "Stop Audio",
      playTilawahBtn: "Play Tilawah",
      pauseTilawahBtn: "Pause Tilawah",
      askAiBtn: "Ask AI",
      askAiTooltip: "Ask AI about grammar analysis & tafsir for this verse",
      aiModalTitle: "Quranic AI Assistant",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Study for Surah ${suratNama}:${ayat} • Word "${kata}" (${noKata})`,
      aiTopicLabel: "Select AI Analysis Topic:",
      aiPromptPreviewLabel: "Ready-to-Use AI Prompt:",
      aiTopicNahwu: "🔍 Nahwu Rules & I'rab",
      aiTopicTafsir: "📖 Tafsir & Meaning",
      aiTopicBalaghah: "✨ Quranic Rhetoric",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Copy Prompt",
      toastPromptCopied: "AI Prompt copied to clipboard!",
      ayahPill: (n) => `Ayah ${n}`,
      flipToArabicBtn: "View Arabic Text",
      flipToTranslationBtn: "View Translation",
      translationBoxHeader: "VERSE MEANING / TRANSLATION (ENGLISH - SAHIH INT.)",
      latinBoxHeader: "LATIN TRANSLITERATION",
      copyLatinBtn: "Copy Latin",
      arabicBoxHeader: "النص القرآني • FULL ARABIC TEXT",
      latinBackHeader: "LATIN READING:",
      copyBtn: "Copy",
      prevBtn: "Previous",
      nextBtn: "Next",
      emptyStateText: "No surahs or verses found matching your search term.",
      
      // Toasts & Speech
      toastLangChanged: "Language switched to English 🇬🇧",
      toastTilawahPaused: "Tilawah paused.",
      toastTilawahPlaying: (s, a) => `Playing tilawah Surah ${s}:${a} (Mishary Alafasy)`,
      toastTilawahEnded: "Tilawah finished.",
      toastAudioFailed: "Failed to load audio. Please check your internet connection.",
      toastTranslationStopped: "Translation speech stopped.",
      toastTtsNotSupported: "Text-to-speech is not supported in this browser.",
      toastTranslationNotAvail: "Translation text not available.",
      toastSpeakingMeaning: (suratNama, ayat) => `Reading translation of Surah ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Pronouncing Arabic: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Reading meaning: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Pronouncing Latin text of Surah ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Arabic text "${word}" copied!`,
      toastLatinCopied: "Latin text copied!",
      toastSummaryCopied: "Data summary copied successfully!",
      toastCsvExported: (nk) => `Successfully exported data ${nk} to CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_en || group.arti;
        const desc = (group.grammar && (group.grammar.desc_en || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Relative Pronoun' : 'Pronoun';
        return `${prefix} ${cleanWord}, ${latin}means ${arti}. ${desc ? 'Details: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    ms: {
      pageTitle: "Kamus Jamid Mabny | Kamus & Rujukan Ayat Interaktif Al-Qur'an",
      brandTitle: "Kamus <span>Jamid Mabny</span>",
      brandSubtitle: "Kamus Interaktif Bentuk Kata & Nombor Kata",
      themeToggleTitle: "Tukar Tema Gelap / Terang",
      labelLangSelect: "Bahasa Terjemahan & Suara:",
      translationSourceHtml: "Terjemahan: <strong>Syeikh Abdullah Muhammad Basmeih (JAKIM)</strong>",
      optgroupEastAsia: "🌏 Asia Tenggara & Asia Timur",
      optgroupMidEast: "🕌 Timur Tengah, Asia Tengah & Caucasus",
      optgroupSouthAsia: "🪷 Asia Selatan & Lautan Hindi",
      optgroupAfrica: "🌍 Afrika",
      optgroupEurope: "🏛️ Eropah Barat, Utara, Tengah & Timur",
      tabBadgeJamid: "7 Bentuk Kata",
      tabBadgeHarf: "17 Bentuk Harf",
      
      // Control Card
      step1Label: "Pilih Bentuk Kata",
      step1Placeholder: "Pilih Bentuk Kata",
      step1OptionDhamir: "1. Dhamir (Kata Ganti Nama)",
      step1OptionMawshul: "2. Mawshul (Kata Hubung)",
      step1OptionIstifham: "3. Istifham (Kata Tanya)",
      step1OptionSyarath: "4. Syarat (Kata Syarat)",
      step1OptionIsyarah: "5. Isyarat (Kata Tunjuk)",
      step1OptionIsimFiil: "6. Isim Fi'il (Kata Nama Makna Perbuatan)",
      step1OptionFiilJamid: "7. Fi'il Jamid (Kata Kerja Kaku)",
      step2Label: "Pilih Nombor Kata",
      step2Placeholder: "Pilih Nombor Kata",
      welcomeTitle: "Sila Pilih Bentuk Kata & Nombor Kata",
      welcomeSubtitle: "Pilih Bentuk Kata (Dhamir / Mawshul) pada menu di atas untuk memaparkan lafaz Arab, makna kata, frekuensi, dan senarai rujukan ayat Al-Qur'an.",
      
      // Spotlight Card
      wordFormBadge: "Bentuk Kata",
      wordNoBadgePrefix: "No. Kata:",
      arabicVoiceBtn: "Suara Arab",
      arabicVoiceTooltip: "Dengar Sebutan Arab (TTS Arab)",
      meaningVoiceBtn: "Suara Maksud",
      meaningVoiceTooltip: "Dengar Maksud / Terjemahan (Bahasa Melayu)",
      copyArabicTooltip: "Salin Lafaz Arab",
      copyInfoBtn: "Salin Maklumat",
      copyInfoTooltip: "Salin Ringkasan Penuh",
      freqLabel: "Frekuensi dalam Al-Qur'an",
      freqSub: "Kekerapan Kemunculan",
      freqMuttashilVal: "Muttashil",
      freqMuttashilSub: "Bentuk Bersambung (Imbuhan)",
      totalAyatLabel: "Jumlah Rujukan Ayat",
      totalAyatSub: "Tersedia dalam Dataset",
      sampleAyatSuffix: "Contoh Ayat",
      transliterationPrefix: "Transliterasi:",
      meaningPrefix: "Makna:",
      
      // References Section
      referencesTitlePrefix: "Rujukan Ayat untuk",
      ayatCountBadgePattern: (cur, total) => `Contoh ${cur} daripada ${total} Ayat`,
      ayatCountZero: "0 Ayat",
      searchPlaceholder: "Cari nama surah / ayat...",
      exportCsvBtn: "Eksport CSV",
      exportCsvTooltip: "Eksport senarai rujukan ayat kata ini ke CSV",
      
      // Ayat Card
      surahPrefix: "Surah",
      surahPositionTag: (cur, surahNo, ayatNo) => `Surah ke-${surahNo} • Ayat ke-${ayatNo}`,
      playTranslationBtn: "Mainkan Maksud",
      stopTranslationBtn: "Hentikan Suara",
      playTilawahBtn: "Mainkan Tilawah",
      pauseTilawahBtn: "Jeda Tilawah",
      askAiBtn: "Tanya AI",
      askAiTooltip: "Tanya AI tentang analisis tatabahasa & tafsir ayat ini",
      aiModalTitle: "Tanya Pembantu AI Al-Qur'an",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Kajian Surah ${suratNama}:${ayat} • Kata "${kata}" (${noKata})`,
      aiTopicLabel: "Pilih Topik Analisis AI:",
      aiPromptPreviewLabel: "Prompt Tanya AI (Sedia Digunakan):",
      aiTopicNahwu: "🔍 Kaedah Nahwu & I'rab",
      aiTopicTafsir: "📖 Tafsir & Makna Ayat",
      aiTopicBalaghah: "✨ Keindahan Balaghah",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Salin Prompt",
      toastPromptCopied: "Prompt Tanya AI berjaya disalin!",
      ayahPill: (n) => `Ayat ${n}`,
      flipToArabicBtn: "Lihat Teks Arab",
      flipToTranslationBtn: "Lihat Terjemahan",
      translationBoxHeader: "MAKSUD / TERJEMAHAN AYAT (BAHASA MELAYU)",
      latinBoxHeader: "BACAAN LATIN",
      copyLatinBtn: "Salin Latin",
      arabicBoxHeader: "النص القرآني • TEKS ARAB AYAT PENUH",
      latinBackHeader: "BACAAN LATIN:",
      copyBtn: "Salin",
      prevBtn: "Sebelumnya",
      nextBtn: "Seterusnya",
      emptyStateText: "Tiada surah atau ayat yang sepadan dengan carian tersebut.",
      
      // Toasts & Speech
      toastLangChanged: "Bahasa berjaya ditukar ke Bahasa Melayu 🇲🇾",
      toastTilawahPaused: "Tilawah dijeda.",
      toastTilawahPlaying: (s, a) => `Memainkan tilawah Surah ${s}:${a} (Mishary Alafasy)`,
      toastTilawahEnded: "Tilawah selesai.",
      toastAudioFailed: "Gagal memuatkan audio ayat. Sila pastikan sambungan internet aktif.",
      toastTranslationStopped: "Audio terjemahan dihentikan.",
      toastTtsNotSupported: "Ciri suara teks tidak disokong pada pelayar ini.",
      toastTranslationNotAvail: "Teks terjemahan tidak tersedia.",
      toastSpeakingMeaning: (suratNama, ayat) => `Membacakan maksud Surah ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Melafazkan lafaz Arab: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Membacakan maksud: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Melafazkan teks Latin Surah ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Lafaz "${word}" disalin!`,
      toastLatinCopied: "Teks Latin berjaya disalin!",
      toastSummaryCopied: "Ringkasan data berjaya disalin!",
      toastCsvExported: (nk) => `Berjaya mengeksport data ${nk} ke CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ms || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ms || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Isim Mawshul' : 'Dhamir';
        return `${prefix} ${cleanWord}, ${latin}bermaksud ${arti}. ${desc ? 'Makna: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    fr: {
      pageTitle: "Dictionnaire Jamid Mabny | Dictionnaire & Références des Versets du Coran",
      brandTitle: "Dictionnaire <span>Jamid Mabny</span>",
      brandSubtitle: "Dictionnaire Interactif des Formes de Mots & Numéros de Mots",
      themeToggleTitle: "Changer de Thème Sombre / Clair",
      labelLangSelect: "Langue de Traduction & Voix :",
      translationSourceHtml: "Traduction : <strong>Muhammad Hamidullah (Le Saint Coran)</strong>",
      optgroupEastAsia: "🌏 Asie du Sud-Est & Asie de l'Est",
      optgroupMidEast: "🕌 Moyen-Orient, Asie Centrale & Caucase",
      optgroupSouthAsia: "🪷 Asie du Sud & Océan Indien",
      optgroupAfrica: "🌍 Afrique",
      optgroupEurope: "🏛️ Europe de l'Ouest, Nord, Centre & Est",
      tabBadgeJamid: "7 Formes de Mots",
      tabBadgeHarf: "17 Formes de Harf",
      
      // Control Card
      step1Label: "Choisir la Forme du Mot",
      step1Placeholder: "Choisir la Forme du Mot",
      step1OptionDhamir: "1. Pronoms (Dhamir)",
      step1OptionMawshul: "2. Pronoms Relatifs (Mawshul)",
      step1OptionIstifham: "3. Interrogatifs (Istifham - Mots Interrogatifs)",
      step1OptionSyarath: "4. Conditionnels (Syarath - Mots Conditionnels)",
      step1OptionIsyarah: "5. Démonstratifs (Isyarah - Pronoms Démonstratifs)",
      step1OptionIsimFiil: "6. Noms Verbaux (Isim Fi'il)",
      step1OptionFiilJamid: "7. Verbes Inflexibles (Fi'il Jamid)",
      step2Label: "Choisir le Numéro du Mot",
      step2Placeholder: "Choisir le Numéro du Mot",
      welcomeTitle: "Veuillez Sélectionner une Forme et un Numéro de Mot",
      welcomeSubtitle: "Sélectionnez une Forme de Mot (Dhamir / Mawshul) dans le menu ci-dessus pour explorer le texte arabe, les significations, la fréquence et les références de versets du Coran.",
      
      // Spotlight Card
      wordFormBadge: "Forme du Mot",
      wordNoBadgePrefix: "N° Mot :",
      arabicVoiceBtn: "Audio Arabe",
      arabicVoiceTooltip: "Écouter la Prononciation Arabe (TTS Arabe)",
      meaningVoiceBtn: "Audio Sens",
      meaningVoiceTooltip: "Écouter la Traduction / Sens (Français TTS)",
      copyArabicTooltip: "Copier le Texte Arabe",
      copyInfoBtn: "Copier Info",
      copyInfoTooltip: "Copier le Résumé Complet",
      freqLabel: "Fréquence dans le Coran",
      freqSub: "Fréquence d'Apparition",
      freqMuttashilVal: "Attaché",
      freqMuttashilSub: "Forme Attachée (Suffixe / Préfixe)",
      totalAyatLabel: "Total Références de Versets",
      totalAyatSub: "Disponible dans le Dataset",
      sampleAyatSuffix: "Exemples de Versets",
      transliterationPrefix: "Translittération :",
      meaningPrefix: "Signification :",
      
      // References Section
      referencesTitlePrefix: "Références de Versets pour",
      ayatCountBadgePattern: (cur, total) => `Exemple ${cur} sur ${total} Versets`,
      ayatCountZero: "0 Verset",
      searchPlaceholder: "Rechercher une sourate / un verset...",
      exportCsvBtn: "Exporter CSV",
      exportCsvTooltip: "Exporter les références de versets de ce mot en CSV",
      
      // Ayat Card
      surahPrefix: "Sourate",
      surahPositionTag: (cur, surahNo, ayatNo) => `Sourate n°${surahNo} • Verset n°${ayatNo}`,
      playTranslationBtn: "Écouter Traduction",
      stopTranslationBtn: "Arrêter la Voix",
      playTilawahBtn: "Écouter Tilawah",
      pauseTilawahBtn: "Mettre en Pause",
      askAiBtn: "Demander à l'IA",
      askAiTooltip: "Demander à l'IA une analyse grammaticale et le tafsir de ce verset",
      aiModalTitle: "Assistant IA du Coran",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Étude de Sourate ${suratNama}:${ayat} • Mot "${kata}" (${noKata})`,
      aiTopicLabel: "Sélectionnez le Thème d'Analyse IA :",
      aiPromptPreviewLabel: "Prompt pour IA (Prêt à l'Emploi) :",
      aiTopicNahwu: "🔍 Règles de Nahwu & I'rab",
      aiTopicTafsir: "📖 Tafsir & Sens du Verset",
      aiTopicBalaghah: "✨ Éloquence & Balaghah",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Copier le Prompt",
      toastPromptCopied: "Prompt pour l'IA copié dans le presse-papiers !",
      ayahPill: (n) => `Verset ${n}`,
      flipToArabicBtn: "Voir le Texte Arabe",
      flipToTranslationBtn: "Voir la Traduction",
      translationBoxHeader: "SENS / TRADUCTION DU VERSET (FRANÇAIS - MUHAMMAD HAMIDULLAH)",
      latinBoxHeader: "LECTURE EN TRANSLITTÉRATION",
      copyLatinBtn: "Copier Latin",
      arabicBoxHeader: "النص القرآني • TEXTE ARABE COMPLET",
      latinBackHeader: "LECTURE LATINE :",
      copyBtn: "Copier",
      prevBtn: "Précédent",
      nextBtn: "Suivant",
      emptyStateText: "Aucune sourate ou verset ne correspond à votre recherche.",
      
      // Toasts & Speech
      toastLangChanged: "Langue changée en Français 🇫🇷",
      toastTilawahPaused: "Tilawah en pause.",
      toastTilawahPlaying: (s, a) => `Lecture de la tilawah Sourate ${s}:${a} (Mishary Alafasy)`,
      toastTilawahEnded: "Tilawah terminée.",
      toastAudioFailed: "Échec du chargement de l'audio. Veuillez vérifier votre connexion internet.",
      toastTranslationStopped: "Lecture audio de la traduction arrêtée.",
      toastTtsNotSupported: "La synthèse vocale n'est pas supportée par ce navigateur.",
      toastTranslationNotAvail: "Texte de traduction non disponible.",
      toastSpeakingMeaning: (suratNama, ayat) => `Lecture de la traduction de Sourate ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Prononciation arabe : ${word}`,
      toastSpeakingWordMeaning: (arti) => `Lecture de la signification : ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Lecture de la translittération Sourate ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Texte arabe "${word}" copié !`,
      toastLatinCopied: "Texte en translittération copié !",
      toastSummaryCopied: "Résumé copié avec succès !",
      toastCsvExported: (nk) => `Données de ${nk} exportées avec succès en CSV !`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_fr || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_fr || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Pronom relatif' : 'Pronom';
        return `${prefix} ${cleanWord}, ${latin}signifie ${arti}. ${desc ? 'Sens : ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    de: {
      pageTitle: "Jamid Mabny Wörterbuch | Interaktives Lexikon & Versreferenzen des Korans",
      brandTitle: "<span>Jamid Mabny</span> Wörterbuch",
      brandSubtitle: "Interaktives Wörterbuch für Wortformen & Wortnummern",
      themeToggleTitle: "Dunkles / Helles Design umschalten",
      labelLangSelect: "Übersetzungs- & Sprachausgabe:",
      translationSourceHtml: "Übersetzung: <strong>Frank Bubenheim & Nadeem Elyas (König-Fahd-Komplex)</strong>",
      optgroupEastAsia: "🌏 Südost- & Ostasien",
      optgroupMidEast: "🕌 Naher Osten, Zentralasien & Kaukasus",
      optgroupSouthAsia: "🪷 Südasien & Indischer Ozean",
      optgroupAfrica: "🌍 Afrika",
      optgroupEurope: "🏛️ West-, Nord-, Mittel- & Osteuropa",
      tabBadgeJamid: "7 Wortformen",
      tabBadgeHarf: "17 Harf-Formen",
      
      // Control Card
      step1Label: "Wortform auswählen",
      step1Placeholder: "Wortform auswählen",
      step1OptionDhamir: "1. Pronomen (Dhamir)",
      step1OptionMawshul: "2. Relativpronomen (Mawshul)",
      step1OptionIstifham: "3. Fragewörter (Istifham - Interrogativpronomen)",
      step1OptionSyarath: "4. Konditionale (Syarath - Bedingungswörter)",
      step1OptionIsyarah: "5. Demonstrativpronomen (Isyarah - Hinweiswörter)",
      step1OptionIsimFiil: "6. Verbalnomina (Isim Fi'il)",
      step1OptionFiilJamid: "7. Erstarrte Verben (Fi'il Jamid)",
      step2Label: "Wortnummer auswählen",
      step2Placeholder: "Wortnummer auswählen",
      welcomeTitle: "Bitte wählen Sie eine Wortform & Wortnummer",
      welcomeSubtitle: "Wählen Sie eine Wortform (Dhamir / Mawshul) aus dem obigen Menü, um den arabischen Wortlaut, die Bedeutung, die Häufigkeit und die Versreferenzen des Korans anzuzeigen.",
      
      // Spotlight Card
      wordFormBadge: "Wortform",
      wordNoBadgePrefix: "Wort-Nr.:",
      arabicVoiceBtn: "Arabische Stimme",
      arabicVoiceTooltip: "Arabische Aussprache anhören (Arabisch TTS)",
      meaningVoiceBtn: "Bedeutung anhören",
      meaningVoiceTooltip: "Bedeutung / Übersetzung anhören (Deutsche Sprachausgabe)",
      copyArabicTooltip: "Arabischen Wortlaut kopieren",
      copyInfoBtn: "Info kopieren",
      copyInfoTooltip: "Vollständige Zusammenfassung kopieren",
      freqLabel: "Häufigkeit im Koran",
      freqSub: "Vorkommenshäufigkeit",
      freqMuttashilVal: "Verbunden",
      freqMuttashilSub: "Verbundene Form (Affix / Suffix)",
      totalAyatLabel: "Gesamte Versreferenzen",
      totalAyatSub: "Im Datensatz verfügbar",
      sampleAyatSuffix: "Beispielverse",
      transliterationPrefix: "Transliteration:",
      meaningPrefix: "Bedeutung:",
      
      // References Section
      referencesTitlePrefix: "Versreferenzen für",
      ayatCountBadgePattern: (cur, total) => `Beispiel ${cur} von ${total} Versen`,
      ayatCountZero: "0 Verse",
      searchPlaceholder: "Suraname / Vers suchen...",
      exportCsvBtn: "CSV exportieren",
      exportCsvTooltip: "Versreferenzen dieses Wortes als CSV exportieren",
      
      // Ayat Card
      surahPrefix: "Sure",
      surahPositionTag: (cur, surahNo, ayatNo) => `Sure #${surahNo} • Vers #${ayatNo}`,
      playTranslationBtn: "Übersetzung abspielen",
      stopTranslationBtn: "Sprachausgabe stoppen",
      playTilawahBtn: "Tilawah abspielen",
      pauseTilawahBtn: "Tilawah pausieren",
      askAiBtn: "KI fragen",
      askAiTooltip: "KI nach Grammatikanalyse und Tafsir für diesen Vers fragen",
      aiModalTitle: "Koran-KI-Assistent",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Analyse zu Sure ${suratNama}:${ayat} • Wort "${kata}" (${noKata})`,
      aiTopicLabel: "Thema der KI-Analyse wählen:",
      aiPromptPreviewLabel: "KI-Prompt (Sofort verwendbar):",
      aiTopicNahwu: "🔍 Nahwu-Regeln & I'rab",
      aiTopicTafsir: "📖 Tafsir & Versbedeutung",
      aiTopicBalaghah: "✨ Koranische Rhetorik (Balagha)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Prompt kopieren",
      toastPromptCopied: "KI-Prompt in die Zwischenablage kopiert!",
      ayahPill: (n) => `Vers ${n}`,
      flipToArabicBtn: "Arabischen Text anzeigen",
      flipToTranslationBtn: "Übersetzung anzeigen",
      translationBoxHeader: "BEDEUTUNG / ÜBERSETZUNG DES VERSES (DEUTSCH - BUBENHEIM & ELYAS)",
      latinBoxHeader: "LATEINISCHE TRANSLITERATION",
      copyLatinBtn: "Transliteration kopieren",
      arabicBoxHeader: "النص القرآني • VOLLSTÄNDIGER ARABISCHER TEXT",
      latinBackHeader: "LATEINISCHE LESUNG:",
      copyBtn: "Kopieren",
      prevBtn: "Zurück",
      nextBtn: "Weiter",
      emptyStateText: "Keine Suren oder Verse entsprechen Ihrem Suchbegriff.",
      
      // Toasts & Speech
      toastLangChanged: "Sprache erfolgreich auf Deutsch umgestellt 🇩🇪",
      toastTilawahPaused: "Tilawah pausiert.",
      toastTilawahPlaying: (s, a) => `Spiele Tilawah Sure ${s}:${a} ab (Mishary Alafasy)`,
      toastTilawahEnded: "Tilawah beendet.",
      toastAudioFailed: "Audio konnte nicht geladen werden. Bitte Internetverbindung prüfen.",
      toastTranslationStopped: "Übersetzungsausgabe beendet.",
      toastTtsNotSupported: "Sprachsynthese wird von diesem Browser nicht unterstützt.",
      toastTranslationNotAvail: "Übersetzungstext nicht verfügbar.",
      toastSpeakingMeaning: (suratNama, ayat) => `Lese Übersetzung von Sure ${suratNama}:${ayat} vor`,
      toastSpeakingArabic: (word) => `Spreche arabischen Wortlaut: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Lese Bedeutung vor: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Lese Transliteration von Sure ${suratNama}:${ayat} vor`,
      toastArabicCopied: (word) => `Arabischer Text "${word}" kopiert!`,
      toastLatinCopied: "Transliterationstext kopiert!",
      toastSummaryCopied: "Zusammenfassung erfolgreich kopiert!",
      toastCsvExported: (nk) => `Daten für ${nk} erfolgreich als CSV exportiert!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_de || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_de || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Relativpronomen' : 'Pronomen';
        return `${prefix} ${cleanWord}, ${latin}bedeutet ${arti}. ${desc ? 'Bedeutung: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    ur: {
      pageTitle: "جامد مبنی لغت | انٹرایکٹو قرآنی الفاظ اور حوالہ جات",
      brandTitle: "جامد مبنی <span>لغت</span>",
      brandSubtitle: "انٹرایکٹو ڈکشنری برائے اشکال الفاظ و اعداد الفاظ",
      themeToggleTitle: "ڈارک / لائٹ موڈ تبدیل کریں",
      labelLangSelect: "ترجمہ اور آواز کی زبان:",
      translationSourceHtml: "ترجمہ: <strong>مولانا فتح محمد جالندھری (Fateh Jalandhry)</strong>",
      optgroupEastAsia: "🌏 جنوب مشرقی اور مشرقی ایشیا",
      optgroupMidEast: "🕌 مشرق وسطیٰ، وسطی ایشیا اور قفقاز",
      optgroupSouthAsia: "🪷 جنوبی ایشیا اور بحر ہند",
      optgroupAfrica: "🌍 افریقہ",
      optgroupEurope: "🏛️ مغربی، شمالی، وسطی اور مشرقی یورپ",
      tabBadgeJamid: "7 کلمے کی اقسام",
      tabBadgeHarf: "17 غیر عامل حروف",
      
      // Control Card
      step1Label: "۱. لفظ کی شکل منتخب کریں",
      step1Placeholder: "لفظ کی شکل منتخب کریں",
      step1OptionDhamir: "۱. ضمائر (Dhamir - Pronouns)",
      step1OptionMawshul: "۲. اسم موصول (Mawshul - Relative Pronouns)",
      step1OptionIstifham: "۳. حروف و اسمائے استفہام (Istifham)",
      step1OptionSyarath: "۴. حروف و اسمائے شرط (Syarath)",
      step1OptionIsyarah: "۵. اسمائے اشارہ (Isyarah)",
      step1OptionIsimFiil: "۶. اسم فعل (Isim Fi'il)",
      step1OptionFiilJamid: "۷. افعال جامد (Fi'il Jamid)",
      step2Label: "۲. لفظ کا نمبر منتخب کریں",
      step2Placeholder: "لفظ کا نمبر منتخب کریں",
      welcomeTitle: "براہ کرم لفظ کی شکل اور نمبر منتخب کریں",
      welcomeSubtitle: "اوپر والے مینو سے لفظ کی شکل (ضمیر / اسم موصول) منتخب کریں تاکہ عربی الفاظ، معانی، تکرار (فریکوئنسی) اور قرآنی آیات کے حوالہ جات دیکھے جا سکیں۔",
      
      // Spotlight Card
      wordFormBadge: "لفظ کی شکل",
      wordNoBadgePrefix: "لفظ نمبر:",
      arabicVoiceBtn: "عربی آواز",
      arabicVoiceTooltip: "عربی تلفظ سنیں (عربی TTS)",
      meaningVoiceBtn: "معنی کی آواز",
      meaningVoiceTooltip: "معنی / ترجمہ سنیں (اردو آواز)",
      copyArabicTooltip: "عربی لفظ کاپی کریں",
      copyInfoBtn: "معلومات کاپی کریں",
      copyInfoTooltip: "مکمل خلاصہ کاپی کریں",
      freqLabel: "قرآن مجید میں تکرار (فریکوئنسی)",
      freqSub: "ظہور کی تعداد",
      freqMuttashilVal: "متصل",
      freqMuttashilSub: "جڑی ہوئی شکل (لاحقہ / Affix)",
      totalAyatLabel: "کل حوالہ جاتی آیات",
      totalAyatSub: "ڈیٹا سیٹ میں دستیاب",
      sampleAyatSuffix: "مثالی آیات",
      transliterationPrefix: "تلفظ (Transliteration):",
      meaningPrefix: "معنی:",
      
      // References Section
      referencesTitlePrefix: "قرآنی حوالہ جات برائے",
      ayatCountBadgePattern: (cur, total) => `آیت ${cur} از ${total} آیات`,
      ayatCountZero: "۰ آیات",
      searchPlaceholder: "سورہ کا نام / آیت نمبر تلاش کریں...",
      exportCsvBtn: "CSV برآمد کریں",
      exportCsvTooltip: "اس لفظ کے تمام قرآنی حوالہ جات بطور CSV ڈاؤن لوڈ کریں",
      
      // Ayat Card
      surahPrefix: "سورۃ",
      surahPositionTag: (cur, surahNo, ayatNo) => `سورۃ #${surahNo} • آیت #${ayatNo}`,
      playTranslationBtn: "ترجمہ سنیں",
      stopTranslationBtn: "آواز بند کریں",
      playTilawahBtn: "تلاوت سنیں",
      pauseTilawahBtn: "تلاوت روکیں",
      askAiBtn: "AI سے پوچھیں",
      askAiTooltip: "اس آیت کی نحوی، تفسیری اور بلاغی تحلیل کے لیے AI سے استفسار کریں",
      aiModalTitle: "قرآنی AI معاون",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `تحلیل برائے سورۃ ${suratNama}:${ayat} • لفظ "${kata}" (${noKata})`,
      aiTopicLabel: "AI تجزیہ کا موضوع منتخب کریں:",
      aiPromptPreviewLabel: "تیار شدہ AI پرامپٹ:",
      aiTopicNahwu: "🔍 نحو کے قواعد و اعراب",
      aiTopicTafsir: "📖 تفسیر و مفہوم آیت",
      aiTopicBalaghah: "✨ قرآنی بلاغت و اسلوب",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "پرامپٹ کاپی کریں",
      toastPromptCopied: "AI پرامپٹ کلپ بورڈ پر کاپی ہو گیا!",
      ayahPill: (n) => `آیت ${n}`,
      flipToArabicBtn: "عربی متن دیکھیں",
      flipToTranslationBtn: "ترجمہ دیکھیں",
      translationBoxHeader: "آیت کا ترجمہ (اردو - مولانا فتح محمد جالندھری)",
      latinBoxHeader: "لاطینی تلفظ (TRANSLITERATION)",
      copyLatinBtn: "تلفظ کاپی کریں",
      arabicBoxHeader: "النص القرآني • مکمل عربی متن",
      latinBackHeader: "لاطینی تلفظ:",
      copyBtn: "کاپی کریں",
      prevBtn: "پچھلا",
      nextBtn: "اگلا",
      emptyStateText: "آپ کی تلاش کے مطابق کوئی سورۃ یا آیت نہیں ملی۔",
      
      // Toasts & Speech
      toastLangChanged: "زبان کامیابی کے ساتھ اردو میں تبدیل کر دی گئی 🇵🇰",
      toastTilawahPaused: "تلاوت روک دی گئی۔",
      toastTilawahPlaying: (s, a) => `سورۃ ${s}:${a} کی تلاوت جاری ہے (مشاری العفاسی)`,
      toastTilawahEnded: "تلاوت مکمل ہو گئی۔",
      toastAudioFailed: "آڈیو لوڈ کرنے میں ناکامی۔ براہ کرم انٹرنیٹ چیک کریں۔",
      toastTranslationStopped: "ترجمے کی آواز بند کر دی گئی۔",
      toastTtsNotSupported: "آپ کا براؤزر ٹیکسٹ ٹو اسپیچ کو سپورٹ نہیں کرتا۔",
      toastTranslationNotAvail: "ترجمہ کا متن دستیاب نہیں ہے۔",
      toastSpeakingMeaning: (suratNama, ayat) => `سورۃ ${suratNama}:${ayat} کا ترجمہ سنایا جا رہا ہے`,
      toastSpeakingArabic: (word) => `عربی لفظ سنایا جا رہا ہے: ${word}`,
      toastSpeakingWordMeaning: (arti) => `معنی سنایا جا رہا ہے: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `سورۃ ${suratNama}:${ayat} کا لاطینی تلفظ سنایا جا رہا ہے`,
      toastArabicCopied: (word) => `عربی متن "${word}" کاپی ہو گیا!`,
      toastLatinCopied: "لاطینی تلفظ کاپی ہو گیا!",
      toastSummaryCopied: "خلاصہ کامیابی کے ساتھ کاپی ہو گیا!",
      toastCsvExported: (nk) => `لفظ ${nk} کا ڈیٹا کامیابی سے CSV میں محفوظ ہو گیا!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ur || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ur || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'اسم موصول' : 'ضمیر';
        return `${prefix} ${cleanWord}، ${latin}معنی ${arti}۔ ${desc ? 'وضاحت: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    bn: {
      pageTitle: "জামেদ মাবনি অভিধান | ইন্টারেক্টিভ কুরআনিক শব্দ ও আয়াত রেফারেন্স",
      brandTitle: "জামেদ মাবনি <span>অভিধান</span>",
      brandSubtitle: "শব্দরূপ ও শব্দ নম্বরের ইন্টারেক্টিভ অভিধান",
      themeToggleTitle: "ডার্ক / লাইট থিম পরিবর্তন করুন",
      labelLangSelect: "অনুবাদ ও ভয়েস ভাষা:",
      translationSourceHtml: "অনুবাদ: <strong>মাওলানা মুহিউদ্দীন খান (Muhiuddin Khan)</strong>",
      optgroupEastAsia: "🌏 দক্ষিণ-পূর্ব ও পূর্ব এশিয়া",
      optgroupMidEast: "🕌 মধ্যপ্রাচ্য, মধ্য এশিয়া ও ককেশাস",
      optgroupSouthAsia: "🪷 দক্ষিণ এশিয়া ও ভারত মহাসাগর",
      optgroupAfrica: "🌍 আফ্রিকা",
      optgroupEurope: "🏛️ পশ্চিম, উত্তর, মধ্য ও পূর্ব ইউরোপ",
      tabBadgeJamid: "৭টি শব্দের রূপ",
      tabBadgeHarf: "১৭টি হরফের রূপ",
      
      // Control Card
      step1Label: "১. শব্দের রূপ নির্বাচন করুন",
      step1Placeholder: "শব্দের রূপ নির্বাচন করুন",
      step1OptionDhamir: "১. সর্বনাম (Dhamir - Pronouns)",
      step1OptionMawshul: "২. সম্বন্ধবাচক সর্বনাম (Mawshul - Relative Pronouns)",
      step1OptionIstifham: "৩. প্রশ্নবোধক শব্দ (Istifham - Interrogatives)",
      step1OptionSyarath: "৪. শর্তমূলক শব্দ (Syarath - Conditionals)",
      step1OptionIsyarah: "৫. নির্দেশক সর্বনাম (Isyarah - Demonstratives)",
      step1OptionIsimFiil: "৬. ক্রিয়াভিত্তিক বিশেষ্য (Isim Fi'il - Verbal Nouns)",
      step1OptionFiilJamid: "৭. অপরিবর্তনীয় ক্রিয়া (Fi'il Jamid - Inflexible Verbs)",
      step2Label: "২. শব্দ নম্বর নির্বাচন করুন",
      step2Placeholder: "শব্দ নম্বর নির্বাচন করুন",
      welcomeTitle: "অনুগ্রহ করে শব্দের রূপ ও নম্বর নির্বাচন করুন",
      welcomeSubtitle: "আরবি শব্দ, অর্থ, কুরআনে পুনরাবৃত্তি (ফ্রিকোয়েন্সি) ও আয়াত রেফারেন্স দেখতে উপরের মেনু থেকে শব্দরূপ নির্বাচন করুন।",
      
      // Spotlight Card
      wordFormBadge: "শব্দরূপ",
      wordNoBadgePrefix: "শব্দ নং:",
      arabicVoiceBtn: "আরবি ভয়েস",
      arabicVoiceTooltip: "আরবি উচ্চারণ শুনুন (TTS)",
      meaningVoiceBtn: "অর্থের ভয়েস",
      meaningVoiceTooltip: "বাংলা অর্থ / অনুবাদ শুনুন (বাংলা TTS)",
      copyArabicTooltip: "আরবি শব্দ কপি করুন",
      copyInfoBtn: "তথ্য কপি করুন",
      copyInfoTooltip: "সম্পূর্ণ সারাংশ কপি করুন",
      freqLabel: "পবিত্র কুরআনে পুনরাবৃত্তি (ফ্রিকোয়েন্সি)",
      freqSub: "উপস্থিতির সংখ্যা",
      freqMuttashilVal: "সংযুক্ত (Muttashil)",
      freqMuttashilSub: "সংযুক্ত রূপ (প্রত্যয় / Affix)",
      totalAyatLabel: "মোট রেফারেন্স আয়াত",
      totalAyatSub: "ডেটাবেজে উপলব্ধ",
      sampleAyatSuffix: "উদাহরণ আয়াত",
      transliterationPrefix: "উচ্চারণ (Transliteration):",
      meaningPrefix: "অর্থ:",
      
      // References Section
      referencesTitlePrefix: "কুরআনিক রেফারেন্স আয়াতসমূহ:",
      ayatCountBadgePattern: (cur, total) => `আয়াত ${cur} / ${total}`,
      ayatCountZero: "০ আয়াত",
      searchPlaceholder: "সূরার নাম / আয়াত নম্বর খুঁজুন...",
      exportCsvBtn: "CSV ডাউনলোড",
      exportCsvTooltip: "এই শব্দের সকল রেফারেন্স আয়াত CSV ফাইলে ডাউনলোড করুন",
      
      // Ayat Card
      surahPrefix: "সূরা",
      surahPositionTag: (cur, surahNo, ayatNo) => `সূরা #${surahNo} • আয়াত #${ayatNo}`,
      playTranslationBtn: "অনুবাদ শুনুন",
      stopTranslationBtn: "ভয়েস বন্ধ করুন",
      playTilawahBtn: "তিলাওয়াত শুনুন",
      pauseTilawahBtn: "তিলাওয়াত থামান",
      askAiBtn: "AI জিজ্ঞাসা করুন",
      askAiTooltip: "এই আয়াতের ব্যাকরণ ও তাফসির সম্পর্কে AI কে জিজ্ঞাসা করুন",
      aiModalTitle: "কুরআনিক AI সহকারী",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `পর্যালোচনা: সূরা ${suratNama}:${ayat} • শব্দ "${kata}" (${noKata})`,
      aiTopicLabel: "AI বিশ্লেষণের বিষয় নির্বাচন করুন:",
      aiPromptPreviewLabel: "প্রস্তুতকৃত AI প্রম্পট:",
      aiTopicNahwu: "🔍 নাহব (ব্যাকরণ) ও ই'রাব",
      aiTopicTafsir: "📖 তাফসির ও আয়াতের মর্মার্থ",
      aiTopicBalaghah: "✨ অলঙ্কারশাস্ত্র (বালাগাত)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "প্রম্পট কপি করুন",
      toastPromptCopied: "AI প্রম্পট ক্লিপবোর্ডে কপি হয়েছে!",
      ayahPill: (n) => `আয়াত ${n}`,
      flipToArabicBtn: "আরবি পাঠ দেখুন",
      flipToTranslationBtn: "অনুবাদ দেখুন",
      translationBoxHeader: "আয়াতের অর্থ / অনুবাদ (বাংলা - মাওলানা মুহিউদ্দীন খান)",
      latinBoxHeader: "রোমান উচ্চারণ (TRANSLITERATION)",
      copyLatinBtn: "উচ্চারণ কপি করুন",
      arabicBoxHeader: "النص القرآني • সম্পূর্ণ আরবি আয়াত",
      latinBackHeader: "রোমান উচ্চারণ:",
      copyBtn: "কপি করুন",
      prevBtn: "পূর্ববর্তী",
      nextBtn: "পরবর্তী",
      emptyStateText: "আপনার অনুসন্ধানের সাথে মিলে এমন কোনো সূরা বা আয়াত পাওয়া যায়নি।",
      
      // Toasts & Speech
      toastLangChanged: "ভাষা সফলভাবে বাংলায় পরিবর্তিত হয়েছে 🇧🇩",
      toastTilawahPaused: "তিলাওয়াত স্থগিত করা হয়েছে।",
      toastTilawahPlaying: (s, a) => `সূরা ${s}:${a}-এর তিলাওয়াত চলছে (মিশারী রাশিদ আল-আফাসী)`,
      toastTilawahEnded: "তিলাওয়াত সমাপ্ত হয়েছে।",
      toastAudioFailed: "অডিও লোড করতে ব্যর্থ হয়েছে। ইন্টারনেট সংযোগ পরীক্ষা করুন।",
      toastTranslationStopped: "অনুবাদ ভয়েস বন্ধ করা হয়েছে।",
      toastTtsNotSupported: "আপনার ব্রাউজারে টেক্সট-টু-স্পিচ সমর্থিত নয়।",
      toastTranslationNotAvail: "অনুবাদ পাঠ্য উপলব্ধ নেই।",
      toastSpeakingMeaning: (suratNama, ayat) => `সূরা ${suratNama}:${ayat}-এর বাংলা অনুবাদ শোনানো হচ্ছে`,
      toastSpeakingArabic: (word) => `আরবি উচ্চারণ: ${word}`,
      toastSpeakingWordMeaning: (arti) => `অর্থ শোনানো হচ্ছে: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `সূরা ${suratNama}:${ayat}-এর রোমান উচ্চারণ শোনানো হচ্ছে`,
      toastArabicCopied: (word) => `আরবি শব্দ "${word}" কপি করা হয়েছে!`,
      toastLatinCopied: "রোমান উচ্চারণ কপি করা হয়েছে!",
      toastSummaryCopied: "সারাংশ সফলভাবে কপি করা হয়েছে!",
      toastCsvExported: (nk) => `শব্দ ${nk}-এর ডেটা সফলভাবে CSV-তে এক্সপোর্ট করা হয়েছে!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_bn || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_bn || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'সম্বন্ধবাচক সর্বনাম' : 'সর্বনাম';
        return `${prefix} ${cleanWord}, ${latin}অর্থ ${arti}। ${desc ? 'বিবরণ: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    ru: {
      pageTitle: "Словарь Джамид Мабни | Интерактивный словарь и коранические ссылки на аяты",
      brandTitle: "Словарь <span>Джамид Мабни</span>",
      brandSubtitle: "Интерактивный словарь грамматических форм и номеров слов",
      themeToggleTitle: "Переключить тёмную / светлую тему",
      labelLangSelect: "Язык перевода и озвучивания:",
      translationSourceHtml: "Перевод: <strong>Эльмир Кулиев (Elmir Kuliev)</strong>",
      optgroupEastAsia: "🌏 Юго-Восточная и Восточная Азия",
      optgroupMidEast: "🕌 Ближний Восток, Центральная Азия и Кавказ",
      optgroupSouthAsia: "🪷 Южная Азия и Индийский океан",
      optgroupAfrica: "🌍 Африка",
      optgroupEurope: "🏛️ Западная, Северная, Центральная и Восточная Европа",
      tabBadgeJamid: "7 форм слов",
      tabBadgeHarf: "17 форм частиц",
      
      // Control Card
      step1Label: "1. Выберите форму слова",
      step1Placeholder: "Выберите форму слова",
      step1OptionDhamir: "1. Местоимения (Дамир / Dhamir)",
      step1OptionMawshul: "2. Относительные местоимения (Маусуль / Mawshul)",
      step1OptionIstifham: "3. Вопросительные слова (Истифхам / Istifham)",
      step1OptionSyarath: "4. Условные частицы (Шарат / Syarath)",
      step1OptionIsyarah: "5. Указательные местоимения (Ишара / Isyarah)",
      step1OptionIsimFiil: "6. Именные глаголы (Исм Фииль / Isim Fi'il)",
      step1OptionFiilJamid: "7. Неизменяемые глаголы (Фииль Джамид / Fi'il Jamid)",
      step2Label: "2. Выберите номер слова",
      step2Placeholder: "Выберите номер слова",
      welcomeTitle: "Пожалуйста, выберите форму и номер слова",
      welcomeSubtitle: "Выберите форму слова (Дамир, Маусуль и др.) в меню выше, чтобы просмотреть арабский текст, значение, частоту упоминания в Коране и список аятов.",
      
      // Spotlight Card
      wordFormBadge: "Форма слова",
      wordNoBadgePrefix: "№ слова:",
      arabicVoiceBtn: "Озвучить арабский",
      arabicVoiceTooltip: "Слушать арабское произношение (TTS)",
      meaningVoiceBtn: "Озвучить значение",
      meaningVoiceTooltip: "Слушать русский перевод / значение (TTS)",
      copyArabicTooltip: "Копировать арабский текст",
      copyInfoBtn: "Копировать инфо",
      copyInfoTooltip: "Копировать полную сводку",
      freqLabel: "Частота в Священном Коране",
      freqSub: "Количество упоминаний",
      freqMuttashilVal: "Муттасыль (Слитное)",
      freqMuttashilSub: "Слитная форма (Аффикс)",
      totalAyatLabel: "Всего ссылок на аяты",
      totalAyatSub: "Доступно в базе данных",
      sampleAyatSuffix: "Примеров аятов",
      transliterationPrefix: "Транслитерация:",
      meaningPrefix: "Значение:",
      
      // References Section
      referencesTitlePrefix: "Коранические аяты для",
      ayatCountBadgePattern: (cur, total) => `Пример ${cur} из ${total} аятов`,
      ayatCountZero: "0 аятов",
      searchPlaceholder: "Поиск суры / номера аята...",
      exportCsvBtn: "Экспорт CSV",
      exportCsvTooltip: "Скачать все аяты этого слова в CSV",
      
      // Ayat Card
      surahPrefix: "Сура",
      surahPositionTag: (cur, surahNo, ayatNo) => `Сура №${surahNo} • Аят №${ayatNo}`,
      playTranslationBtn: "Слушать перевод",
      stopTranslationBtn: "Остановить звук",
      playTilawahBtn: "Слушать чтение (Тиляват)",
      pauseTilawahBtn: "Пауза чтения",
      askAiBtn: "Спросить ИИ",
      askAiTooltip: "Спросить ИИ о грамматике и тафсире этого аята",
      aiModalTitle: "Коранический ИИ-помощник",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Исследование: Сура ${suratNama}:${ayat} • Слово "${kata}" (${noKata})`,
      aiTopicLabel: "Выберите тему анализа ИИ:",
      aiPromptPreviewLabel: "Готовый ИИ-промпт (для копирования):",
      aiTopicNahwu: "🔍 Грамматика Нахву и И'раб",
      aiTopicTafsir: "📖 Тафсир и значение аята",
      aiTopicBalaghah: "✨ Риторика и красота Баляги",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Скопировать промпт",
      toastPromptCopied: "Промпт для ИИ скопирован в буфер обмена!",
      ayahPill: (n) => `Аят ${n}`,
      flipToArabicBtn: "Показать арабский текст",
      flipToTranslationBtn: "Показать перевод",
      translationBoxHeader: "ПЕРЕВОД АЯТА (РУССКИЙ - ЭЛЬМИР КУЛИЕВ)",
      latinBoxHeader: "ТРАНСЛИТЕРАЦИЯ (КЕМЕНАГ / РОМАНИЗАЦИЯ)",
      copyLatinBtn: "Копировать латиницу",
      arabicBoxHeader: "النص القرآني • ПОЛНЫЙ АРАБСКИЙ ТЕКСТ АЯТА",
      latinBackHeader: "ТРАНСЛИТЕРАЦИЯ:",
      copyBtn: "Копировать",
      prevBtn: "Предыдущий",
      nextBtn: "Следующий",
      emptyStateText: "Ничего не найдено по вашему поисковому запросу.",
      
      // Toasts & Speech
      toastLangChanged: "Язык успешно изменён на русский 🇷🇺",
      toastTilawahPaused: "Чтение приостановлено.",
      toastTilawahPlaying: (s, a) => `Воспроизведение чтения Суры ${s}:${a} (Мишари Рашид аль-Афаси)`,
      toastTilawahEnded: "Чтение завершено.",
      toastAudioFailed: "Не удалось загрузить аудио аята. Проверьте интернет-соединение.",
      toastTranslationStopped: "Озвучивание перевода остановлено.",
      toastTtsNotSupported: "Синтез речи (TTS) не поддерживается в этом браузере.",
      toastTranslationNotAvail: "Текст перевода недоступен.",
      toastSpeakingMeaning: (suratNama, ayat) => `Озвучивание перевода: Сура ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Произношение арабского слова: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Озвучивание значения: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Озвучивание латинской транслитерации Суры ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Арабское слово "${word}" скопировано!`,
      toastLatinCopied: "Транслитерация скопирована!",
      toastSummaryCopied: "Сводка успешно скопирована!",
      toastCsvExported: (nk) => `Данные слова ${nk} экспортированы в CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ru || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ru || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Относительное местоимение' : 'Местоимение';
        return `${prefix} ${cleanWord}, ${latin}значение ${arti}. ${desc ? 'Описание: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    zh: {
      pageTitle: "贾米德·马布尼词典 | 古兰经互动词汇与经文参考",
      brandTitle: "贾米德·马布尼 <span>词典</span>",
      brandSubtitle: "词形与词号古兰经交互式词典",
      themeToggleTitle: "切换深色 / 浅色主题",
      labelLangSelect: "翻译与语音语言:",
      translationSourceHtml: "译文: <strong>马坚 (Muhammad Makin)</strong>",
      optgroupEastAsia: "🌏 东南亚与东亚",
      optgroupMidEast: "🕌 中东、中亚与高加索",
      optgroupSouthAsia: "🪷 南亚与印度洋",
      optgroupAfrica: "🌍 非洲",
      optgroupEurope: "🏛️ 西欧、北欧、中欧与东欧",
      tabBadgeJamid: "7种词形",
      tabBadgeHarf: "17种虚词形态",
      
      // Control Card
      step1Label: "1. 请选择词形类别",
      step1Placeholder: "请选择词形类别",
      step1OptionDhamir: "1. 人称代词 (代名词 / Dhamir)",
      step1OptionMawshul: "2. 关系代词 (接续词 / Mawshul)",
      step1OptionIstifham: "3. 疑问词 (疑问代词 / Istifham)",
      step1OptionSyarath: "4. 条件虚词 (条件代词 / Syarath)",
      step1OptionIsyarah: "5. 指示代词 (指示名词 / Isyarah)",
      step1OptionIsimFiil: "6. 动名词 (含动词义名词 / Isim Fi'il)",
      step1OptionFiilJamid: "7. 固态动词 (不规则静态动词 / Fi'il Jamid)",
      step2Label: "2. 请选择词号",
      step2Placeholder: "请选择词号",
      welcomeTitle: "请选择词形与词号",
      welcomeSubtitle: "请在上方菜单中选择词形（代词、关系代词等），以查看阿拉伯语原文、含义、古兰经中出现频次及经文参考列表。",
      
      // Spotlight Card
      wordFormBadge: "词形类别",
      wordNoBadgePrefix: "词号:",
      arabicVoiceBtn: "阿拉伯语发音",
      arabicVoiceTooltip: "收听阿拉伯语音频 (TTS)",
      meaningVoiceBtn: "词义朗读",
      meaningVoiceTooltip: "收听中文翻译与释义 (TTS)",
      copyArabicTooltip: "复制阿拉伯语单词",
      copyInfoBtn: "复制信息",
      copyInfoTooltip: "复制完整摘要",
      freqLabel: "古兰经中出现频次",
      freqSub: "经文出现次数",
      freqMuttashilVal: "接尾代词 (Muttashil)",
      freqMuttashilSub: "附着词缀形式",
      totalAyatLabel: "参考经文总数",
      totalAyatSub: "数据库中收录",
      sampleAyatSuffix: "条示例经文",
      transliterationPrefix: "罗马拼音:",
      meaningPrefix: "释义:",
      
      // References Section
      referencesTitlePrefix: "古兰经经文参考 —",
      ayatCountBadgePattern: (cur, total) => `示例 ${cur} / 共 ${total} 节经文`,
      ayatCountZero: "0 节经文",
      searchPlaceholder: "搜索苏拉名称 / 节数...",
      exportCsvBtn: "导出 CSV",
      exportCsvTooltip: "下载该词的所有参考经文 CSV 文件",
      
      // Ayat Card
      surahPrefix: "苏拉",
      surahPositionTag: (cur, surahNo, ayatNo) => `第 ${surahNo} 章 • 第 ${ayatNo} 节`,
      playTranslationBtn: "朗读译文",
      stopTranslationBtn: "停止播放",
      playTilawahBtn: "诵读音频",
      pauseTilawahBtn: "暂停诵读",
      askAiBtn: "向 AI 提问",
      askAiTooltip: "向 AI 询问本节经文的语法与经注 (Tafsir)",
      aiModalTitle: "古兰经 AI 学习助手",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `研读: 苏拉 ${suratNama}:${ayat} • 词汇 "${kata}" (${noKata})`,
      aiTopicLabel: "选择 AI 分析主题:",
      aiPromptPreviewLabel: "生成的 AI 提示词 (可直接复制):",
      aiTopicNahwu: "🔍 语法 (Nahwu) 与语法分析 (I'rab)",
      aiTopicTafsir: "📖 经注 (Tafsir) 与经文内涵",
      aiTopicBalaghah: "✨ 修辞学 (Balaghah) 鉴赏",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "复制提示词",
      toastPromptCopied: "AI 提示词已成功复制到剪贴板！",
      ayahPill: (n) => `第 ${n} 节`,
      flipToArabicBtn: "查看阿拉伯语原文",
      flipToTranslationBtn: "查看中文译文",
      translationBoxHeader: "经文译文 (中文 - 马坚 译本)",
      latinBoxHeader: "罗马拼音转写 (TRANSLITERATION)",
      copyLatinBtn: "复制拼音",
      arabicBoxHeader: "النص القرآني • 古兰经完整阿拉伯语经文",
      latinBackHeader: "罗马拼音:",
      copyBtn: "复制",
      prevBtn: "上一节",
      nextBtn: "下一节",
      emptyStateText: "未找到与您的搜索条件匹配的苏拉或经文。",
      
      // Toasts & Speech
      toastLangChanged: "语言已成功切换为中文 🇨🇳",
      toastTilawahPaused: "诵读已暂停。",
      toastTilawahPlaying: (s, a) => `正在播放苏拉 ${s}:${a} 阿拉伯语诵读 (米沙里·拉希德)`,
      toastTilawahEnded: "诵读播放完毕。",
      toastAudioFailed: "音频加载失败，请检查网络连接。",
      toastTranslationStopped: "译文朗读已停止。",
      toastTtsNotSupported: "当前浏览器不支持语音合成 (TTS)。",
      toastTranslationNotAvail: "未找到译文内容。",
      toastSpeakingMeaning: (suratNama, ayat) => `正在朗读苏拉 ${suratNama}:${ayat} 中文译文`,
      toastSpeakingArabic: (word) => `阿拉伯语词汇发音: ${word}`,
      toastSpeakingWordMeaning: (arti) => `正在朗读词义: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `正在朗读苏拉 ${suratNama}:${ayat} 罗马拼音`,
      toastArabicCopied: (word) => `阿拉伯语词汇 "${word}" 已复制！`,
      toastLatinCopied: "拼音转写已复制！",
      toastSummaryCopied: "详细摘要已成功复制！",
      toastCsvExported: (nk) => `词号 ${nk} 的数据已成功导出为 CSV！`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_zh || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_zh || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? '关系代词' : '人称代词';
        return `${prefix} ${cleanWord}, ${latin}含义 ${arti}。${desc ? '语法解析: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }
,
    es: {
      pageTitle: "Diccionario Jamid Mabny | Léxico Interactivo y Referencias de Versículos del Corán",
      brandTitle: "Diccionario <span>Jamid Mabny</span>",
      brandSubtitle: "Diccionario Interactivo de Formas y Números de Palabras",
      themeToggleTitle: "Cambiar Tema Oscuro / Claro",
      labelLangSelect: "Idioma de Traducción y Voz:",
      translationSourceHtml: "Traducción: <strong>Muhammad Isa García</strong>",
      optgroupEastAsia: "🌏 Sudeste Asiático y Asia Oriental",
      optgroupMidEast: "🕌 Medio Oriente, Asia Central y Cáucaso",
      optgroupSouthAsia: "🪷 Asia del Sur y Océano Índico",
      optgroupAfrica: "🌍 África",
      optgroupEurope: "🏛️ Europa Occidental, Norte, Central y Oriental",
      tabBadgeJamid: "7 Formas de Palabras",
      tabBadgeHarf: "17 Formas de Harf",
      
      // Control Card
      step1Label: "Seleccionar Forma de Palabra",
      step1Placeholder: "Seleccionar Forma de Palabra",
      step1OptionDhamir: "1. Pronombres (Dhamir)",
      step1OptionMawshul: "2. Pronombres Relativos (Mawshul)",
      step1OptionIstifham: "3. Interrogativos (Istifham)",
      step1OptionSyarath: "4. Condicionales (Syarath)",
      step1OptionIsyarah: "5. Demostrativos (Isyarah)",
      step1OptionIsimFiil: "6. Nombres Verbales (Isim Fi'il)",
      step1OptionFiilJamid: "7. Verbos Inflexibles (Fi'il Jamid)",
      step2Label: "Seleccionar Número de Palabra",
      step2Placeholder: "Seleccionar Número de Palabra",
      welcomeTitle: "Por favor seleccione una Forma y Número de Palabra",
      welcomeSubtitle: "Seleccione una forma de palabra del menú superior para ver la pronunciación árabe, significado, frecuencia y referencias completas del Corán.",
      
      // Spotlight Card
      wordFormBadge: "Forma de Palabra",
      wordNoBadgePrefix: "Palabra N°:",
      arabicVoiceBtn: "Audio Árabe",
      arabicVoiceTooltip: "Escuchar la pronunciación en árabe (TTS Árabe)",
      meaningVoiceBtn: "Audio Significado",
      meaningVoiceTooltip: "Escuchar el significado en español (TTS Español)",
      copyArabicTooltip: "Copiar texto árabe",
      copyInfoBtn: "Copiar Información",
      copyInfoTooltip: "Copiar resumen completo de la palabra",
      freqLabel: "Frecuencia en el Corán",
      freqSub: "Frecuencia de Aparición",
      freqMuttashilVal: "Unido / Sufijo",
      freqMuttashilSub: "Forma Sufija / Prefija (Muttashil)",
      totalAyatLabel: "Total de Referencias",
      totalAyatSub: "Disponibles en el Dataset",
      sampleAyatSuffix: "Ejemplos de Versículos",
      transliterationPrefix: "Pronunciación (Transliteración):",
      meaningPrefix: "Significado:",
      
      // References Section
      referencesTitlePrefix: "Referencias de Versículos para",
      ayatCountBadgePattern: (cur, total) => `Ejemplo ${cur} de ${total} Versículos`,
      ayatCountZero: "0 Versículos",
      searchPlaceholder: "Buscar por sura, número o significado...",
      exportCsvBtn: "Exportar CSV",
      exportCsvTooltip: "Exportar las referencias de esta palabra en archivo CSV",
      
      // Ayat Card
      surahPrefix: "Sura",
      surahPositionTag: (cur, surahNo, ayatNo) => `Sura N°${surahNo} • Versículo N°${ayatNo}`,
      playTranslationBtn: "Escuchar Traducción",
      stopTranslationBtn: "Detener Voz",
      playTilawahBtn: "Escuchar Recitación",
      pauseTilawahBtn: "Pausar Recitación",
      askAiBtn: "Consultar IA",
      askAiTooltip: "Consultar a la IA sobre la gramática (Nahwu/I'rab) y Tafsir de este versículo",
      aiModalTitle: "Asistente de IA del Corán",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Estudio de Sura ${suratNama}:${ayat} • Palabra "${kata}" (${noKata})`,
      aiTopicLabel: "Seleccione el Tema de Análisis con IA:",
      aiPromptPreviewLabel: "Prompt para IA (Listo para Usar):",
      aiTopicNahwu: "🔍 Reglas de Nahw, Sarf e I'rab",
      aiTopicTafsir: "📖 Tafsir y Contexto del Versículo",
      aiTopicBalaghah: "✨ Retórica y Balaghah",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Copiar Prompt",
      toastPromptCopied: "¡Prompt de IA copiado al portapapeles!",
      ayahPill: (n) => `Versículo ${n}`,
      flipToArabicBtn: "Ver Texto Árabe",
      flipToTranslationBtn: "Ver Traducción",
      translationBoxHeader: "SIGNIFICADO / TRADUCCIÓN DEL VERSÍCULO (ESPAÑOL - MUHAMMAD ISA GARCÍA)",
      latinBoxHeader: "LECTURA EN TRANSLITERACIÓN",
      copyLatinBtn: "Copiar Transliteración",
      arabicBoxHeader: "النص القرآني • TEXTO ÁRABE COMPLETO",
      latinBackHeader: "TRANSLITERACIÓN:",
      copyBtn: "Copiar",
      prevBtn: "Anterior",
      nextBtn: "Siguiente",
      emptyStateText: "No se encontraron suras o versículos que coincidan con su búsqueda.",
      
      // Toasts & Speech
      toastLangChanged: "Idioma cambiado a Español 🇪🇸",
      toastTilawahPaused: "Recitación pausada.",
      toastTilawahPlaying: (s, a) => `Reproduciendo recitación de Sura ${s}:${a} (Mishary Alafasy)`,
      toastTilawahEnded: "Recitación finalizada.",
      toastAudioFailed: "Error al cargar el audio. Compruebe su conexión a internet.",
      toastTranslationStopped: "Lectura de traducción detenida.",
      toastTtsNotSupported: "La síntesis de voz (TTS) no es compatible con este navegador.",
      toastTranslationNotAvail: "Texto de traducción no disponible.",
      toastSpeakingMeaning: (suratNama, ayat) => `Leyendo traducción de Sura ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Pronunciación en árabe: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Leyendo significado: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Leyendo transliteración de Sura ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `¡Texto árabe "${word}" copiado!`,
      toastLatinCopied: "¡Transliteración copiada!",
      toastSummaryCopied: "¡Resumen copiado exitosamente!",
      toastCsvExported: (nk) => `¡Datos de ${nk} exportados exitosamente en CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_es || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_es || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Pronombre relativo' : 'Pronombre';
        return `${prefix} ${cleanWord}, ${latin}significa ${arti}. ${desc ? 'Significado: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }
,
    tr: {
      pageTitle: "Câmid Mebnî Sözlüğü | İnteraktif Kur'an Kelime & Ayet Referansları",
      brandTitle: "Câmid Mebnî <span>Sözlüğü</span>",
      brandSubtitle: "Kelime Formları ve Numaraları İçin İnteraktif Sözlük",
      themeToggleTitle: "Koyu / Açık Temayı Değiştir",
      labelLangSelect: "Meal ve Ses Dili:",
      translationSourceHtml: "Meal: <strong>Türkiye Diyanet Vakfı</strong>",
      optgroupEastAsia: "🌏 Güneydoğu ve Doğu Asya",
      optgroupMidEast: "🕌 Orta Doğu, Orta Asya ve Kafkaslar",
      optgroupSouthAsia: "🪷 Güney Asya ve Hint Okyanusu",
      optgroupAfrica: "🌍 Afrika",
      optgroupEurope: "🏛️ Batı, Kuzey, Orta ve Doğu Avrupa",
      tabBadgeJamid: "7 Kelime Türü",
      tabBadgeHarf: "17 Harf Türü",
      
      // Control Card
      step1Label: "1. Kelime Formunu Seçiniz",
      step1Placeholder: "Kelime Formunu Seçiniz",
      step1OptionDhamir: "1. Zamirler (Dhamir - Şahıs Zamirleri)",
      step1OptionMawshul: "2. İsmi Mevsul (Mawshul - İlgi Zamirleri)",
      step1OptionIstifham: "3. Soru Edatları (İstifham - Soru İsimleri)",
      step1OptionSyarath: "4. Şart Edatları (Şart - Şart İsimleri)",
      step1OptionIsyarah: "5. İşaret İsimleri (İşaret Zamirleri / İsm-i İşâre)",
      step1OptionIsimFiil: "6. İsim Fiil (Fiil Anlamlı İsimler / İsm-i Fiil)",
      step1OptionFiilJamid: "7. Camid Fiiller (Çekimsiz / Donuk Fiiller)",
      step2Label: "2. Kelime Numarasını Seçiniz",
      step2Placeholder: "Kelime Numarasını Seçiniz",
      welcomeTitle: "Lütfen Kelime Formu ve Numarası Seçiniz",
      welcomeSubtitle: "Arapça lafız, anlam, Kur'an'daki geçiş sıklığı ve ayet referanslarını görüntülemek için yukarıdaki menüden bir kelime formu seçiniz.",
      
      // Spotlight Card
      wordFormBadge: "Kelime Formu",
      wordNoBadgePrefix: "Kelime No:",
      arabicVoiceBtn: "Arapça Ses",
      arabicVoiceTooltip: "Arapça Telaffuzu Dinle (Arapça TTS)",
      meaningVoiceBtn: "Meal Sesi",
      meaningVoiceTooltip: "Türkçe Anlamı / Meali Dinle (Türkçe TTS)",
      copyArabicTooltip: "Arapça Kelimeyi Kopyala",
      copyInfoBtn: "Bilgiyi Kopyala",
      copyInfoTooltip: "Tüm Özeti Kopyala",
      freqLabel: "Kur'an-ı Kerim'deki Frekansı",
      freqSub: "Toplam Geçiş Sayısı",
      freqMuttashilVal: "Muttasıl (Bitişik)",
      freqMuttashilSub: "Bitişik Form (Ek / Sonek)",
      totalAyatLabel: "Toplam Ayet Referansı",
      totalAyatSub: "Veri Setinde Mevcut",
      sampleAyatSuffix: "Örnek Ayetler",
      transliterationPrefix: "Okunuş (Transliterasyon):",
      meaningPrefix: "Anlam:",
      
      // References Section
      referencesTitlePrefix: "Kelime İçin Ayet Referansları:",
      ayatCountBadgePattern: (cur, total) => `Örnek ${cur} / ${total} Ayet`,
      ayatCountZero: "0 Ayet",
      searchPlaceholder: "Sure adı veya ayet no ile ara...",
      exportCsvBtn: "CSV İndir",
      exportCsvTooltip: "Bu kelimenin tüm ayet referanslarını CSV dosyası olarak indir",
      
      // Ayat Card
      surahPrefix: "Sure",
      surahPositionTag: (cur, surahNo, ayatNo) => `Sure No: ${surahNo} • Ayet No: ${ayatNo}`,
      playTranslationBtn: "Meali Dinle",
      stopTranslationBtn: "Sesi Durdur",
      playTilawahBtn: "Tilaveti Dinle",
      pauseTilawahBtn: "Tilaveti Duraklat",
      askAiBtn: "Yapay Zekaya Sor",
      askAiTooltip: "Bu ayetin Nahiv/İ'rab analizi ve tefsiri hakkında Yapay Zekaya danışın",
      aiModalTitle: "Kur'an Yapay Zeka Asistanı",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `İnceleme: ${suratNama} Suresi ${ayat}. Ayet • Kelime: "${kata}" (${noKata})`,
      aiTopicLabel: "Yapay Zeka Analiz Konusunu Seçiniz:",
      aiPromptPreviewLabel: "Hazır Yapay Zeka İstemi (Prompt):",
      aiTopicNahwu: "🔍 Nahiv, Sarf & İ'rab Kaideleri",
      aiTopicTafsir: "📖 Tefsir ve Ayetin Anlamı",
      aiTopicBalaghah: "✨ Kur'an Belâğatı & Edebî İncelikler",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "İstemi Kopyala",
      toastPromptCopied: "Yapay Zeka istemi panoya kopyalandı!",
      ayahPill: (n) => `Ayet ${n}`,
      flipToArabicBtn: "Arapça Metni Gör",
      flipToTranslationBtn: "Meali Gör",
      translationBoxHeader: "AYET MEALİ (TÜRKÇE - DİYANET İŞLERİ BAŞKANLIĞI)",
      latinBoxHeader: "LATİN HARFLERİYLE OKUNUŞ (TRANSLİTERASYON)",
      copyLatinBtn: "Okunuşu Kopyala",
      arabicBoxHeader: "النص القرآني • TAM ARAPÇA AYET METNİ",
      latinBackHeader: "OKUNUŞ:",
      copyBtn: "Kopyala",
      prevBtn: "Önceki",
      nextBtn: "Sonraki",
      emptyStateText: "Arama kriterinize uygun sure veya ayet bulunamadı.",
      
      // Toasts & Speech
      toastLangChanged: "Dil Türkçe olarak değiştirildi 🇹🇷",
      toastTilawahPaused: "Tilavet duraklatıldı.",
      toastTilawahPlaying: (s, a) => `${s} Suresi ${a}. Ayetin tilaveti çalınıyor (Mişâri Râşid el-Afâsî)`,
      toastTilawahEnded: "Tilavet tamamlandı.",
      toastAudioFailed: "Ses dosyası yüklenemedi. Lütfen internet bağlantınızı kontrol ediniz.",
      toastTranslationStopped: "Meal seslendirmesi durduruldu.",
      toastTtsNotSupported: "Tarayıcınız metin okuma (TTS) özelliğini desteklemiyor.",
      toastTranslationNotAvail: "Meal metni bulunamadı.",
      toastSpeakingMeaning: (suratNama, ayat) => `${suratNama} Suresi ${ayat}. Ayetin Türkçe meali seslendiriliyor`,
      toastSpeakingArabic: (word) => `Arapça kelime telaffuzu: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Anlam seslendiriliyor: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `${suratNama} Suresi ${ayat}. Ayetin Latin okunuşu seslendiriliyor`,
      toastArabicCopied: (word) => `Arapça kelime "${word}" kopyalandı!`,
      toastLatinCopied: "Okunuş metni kopyalandı!",
      toastSummaryCopied: "Özet başarıyla kopyalandı!",
      toastCsvExported: (nk) => `Kelime ${nk} verileri başarıyla CSV olarak indirildi!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_tr || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_tr || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'İsmi mevsul' : 'Zamir';
        return `${prefix} ${cleanWord}, ${latin}anlamı ${arti}. ${desc ? 'Açıklama: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },

    pt: {
      pageTitle: "Dicionário Jamid Mabny | Vocabulário Alcorânico e Referências Interativas",
      brandTitle: "Dicionário <span>Jamid Mabny</span>",
      brandSubtitle: "Dicionário Interativo de Formas e Números de Palavras",
      themeToggleTitle: "Alternar Tema Claro / Escuro",
      labelLangSelect: "Idioma da Tradução e Voz:",
      translationSourceHtml: "Tradução: <strong>Prof. Samir El-Hayek (Centro Islâmico)</strong>",
      optgroupEastAsia: "🌏 Sudeste Asiático e Leste da Ásia",
      optgroupMidEast: "🕌 Oriente Médio, Ásia Central e Cáucaso",
      optgroupSouthAsia: "🪷 Sul da Ásia e Oceano Índico",
      optgroupAfrica: "🌍 África",
      optgroupEurope: "🏛️ Europa Ocidental, Norte, Central e Oriental",
      tabBadgeJamid: "7 Formas de Palavras",
      tabBadgeHarf: "17 Formas de Harf",
      
      // Control Card
      step1Label: "1. Selecione a Forma da Palavra",
      step1Placeholder: "Selecione a Forma da Palavra",
      step1OptionDhamir: "1. Pronomes (Dhamir - Pronomes Pessoais)",
      step1OptionMawshul: "2. Pronomes Relativos (Mawshul)",
      step1OptionIstifham: "3. Interrogativos (Istifham)",
      step1OptionSyarath: "4. Condicionais (Syarath)",
      step1OptionIsyarah: "5. Demonstrativos (Isyarah)",
      step1OptionIsimFiil: "6. Nomes Verbais (Isim Fi'il)",
      step1OptionFiilJamid: "7. Verbos Inflexíveis (Fi'il Jamid)",
      step2Label: "2. Selecione o Número da Palavra",
      step2Placeholder: "Selecione o Número da Palavra",
      welcomeTitle: "Por favor, Selecione a Forma e o Número da Palavra",
      welcomeSubtitle: "Selecione a Forma da Palavra no menu acima para visualizar a palavra em árabe, significado, frequência no Alcorão e referências de versículos.",
      
      // Spotlight Card
      wordFormBadge: "Forma da Palavra",
      wordNoBadgePrefix: "Nº da Palavra:",
      arabicVoiceBtn: "Voz Árabe",
      arabicVoiceTooltip: "Ouvir Pronúncia em Árabe (TTS)",
      meaningVoiceBtn: "Voz do Significado",
      meaningVoiceTooltip: "Ouvir Significado em Português (TTS)",
      copyArabicTooltip: "Copiar Palavra em Árabe",
      copyInfoBtn: "Copiar Informações",
      copyInfoTooltip: "Copiar Resumo Completo",
      freqLabel: "Frequência no Alcorão Sagrado",
      freqSub: "Total de Ocorrências",
      freqMuttashilVal: "Muttashil (Ligado)",
      freqMuttashilSub: "Forma Ligada (Sufixo / Imbuhan)",
      totalAyatLabel: "Total de Versículos de Referência",
      totalAyatSub: "Disponíveis no Conjunto de Dados",
      sampleAyatSuffix: "Versículos de Exemplo",
      transliterationPrefix: "Transliteração:",
      meaningPrefix: "Significado:",
      
      // References Section
      referencesTitlePrefix: "Referências de Versículos para:",
      ayatCountBadgePattern: (cur, total) => `Exemplo ${cur} de ${total} Versículos`,
      ayatCountZero: "0 Versículos",
      searchPlaceholder: "Buscar por nome da surata ou número do versículo...",
      exportCsvBtn: "Exportar CSV",
      exportCsvTooltip: "Baixar todas as referências de versículos desta palavra em formato CSV",
      
      // Ayat Card
      surahPrefix: "Surata",
      surahPositionTag: (cur, surahNo, ayatNo) => `Surata nº ${surahNo} • Versículo nº ${ayatNo}`,
      playTranslationBtn: "Ouvir Tradução",
      stopTranslationBtn: "Parar Áudio",
      playTilawahBtn: "Ouvir Recitação",
      pauseTilawahBtn: "Pausar Recitação",
      askAiBtn: "Perguntar à IA",
      askAiTooltip: "Consultar IA sobre análise gramatical (Nahwu/I'rab) e Tafsir deste versículo",
      aiModalTitle: "Assistente de IA Alcorânica",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Estudo: Surata ${suratNama}:${ayat} • Palavra "${kata}" (${noKata})`,
      aiTopicLabel: "Selecione o Tópico de Análise da IA:",
      aiPromptPreviewLabel: "Prompt Pronto para IA:",
      aiTopicNahwu: "🔍 Regras de Gramática (Nahwu/Sarf) & I'rab",
      aiTopicTafsir: "📖 Tafsir e Significado do Versículo",
      aiTopicBalaghah: "✨ Eloquência e Balaghah Alcorânica",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Copiar Prompt",
      toastPromptCopied: "Prompt copiado para a área de transferência!",
      ayahPill: (n) => `Versículo ${n}`,
      flipToArabicBtn: "Ver Texto Árabe",
      flipToTranslationBtn: "Ver Tradução",
      translationBoxHeader: "TRADUÇÃO DO VERSÍCULO (PORTUGUÊS - PROF. SAMIR EL-HAYEK)",
      latinBoxHeader: "TRANSLITERAÇÃO EM CARACTERES LATINOS",
      copyLatinBtn: "Copiar Transliteração",
      arabicBoxHeader: "النص القرآني • TEXTO ÁRABE INTEGRAL DO VERSÍCULO",
      latinBackHeader: "TRANSLITERAÇÃO:",
      copyBtn: "Copiar",
      prevBtn: "Anterior",
      nextBtn: "Próximo",
      emptyStateText: "Nenhuma surata ou versículo encontrado para sua pesquisa.",
      
      // Toasts & Speech
      toastLangChanged: "Idioma alterado para Português 🇵🇹 🇧🇷",
      toastTilawahPaused: "Recitação pausada.",
      toastTilawahPlaying: (s, a) => `Reproduzindo recitação da Surata ${s}:${a} (Mishary Rashid Alafasy)`,
      toastTilawahEnded: "Recitação concluída.",
      toastAudioFailed: "Falha ao carregar arquivo de áudio. Verifique sua conexão com a internet.",
      toastTranslationStopped: "Reprodução da tradução interrompida.",
      toastTtsNotSupported: "Seu navegador não suporta síntese de voz (TTS).",
      toastTranslationNotAvail: "Texto de tradução não encontrado.",
      toastSpeakingMeaning: (suratNama, ayat) => `Reproduzindo tradução em português da Surata ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Pronúncia em árabe da palavra: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Reproduzindo significado: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Reproduzindo transliteração da Surata ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Palavra em árabe "${word}" copiada!`,
      toastLatinCopied: "Transliteração copiada!",
      toastSummaryCopied: "Resumo copiado com sucesso!",
      toastCsvExported: (nk) => `Dados da palavra ${nk} exportados para CSV com sucesso!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_pt || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_pt || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Pronome relativo' : 'Pronome';
        return `${prefix} ${cleanWord}, ${latin}significado ${arti}. ${desc ? 'Explicação: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }
,
    ha: {
      pageTitle: "Ƙamus ɗin Jamid Mabny | Ƙamus da Manazartar Ayoyin Al-Ƙur'ani Mai Girma",
      brandTitle: "Ƙamus ɗin <span>Jamid Mabny</span>",
      brandSubtitle: "Ƙamus Mai Ma'amala don Sigar Kalmomi da Lambobin Kalmomi",
      themeToggleTitle: "Sauya Haske / Duhu na Fuska",
      labelLangSelect: "Harshen Fassara da Murya:",
      translationSourceHtml: "Fassara: <strong>Sheikh Abubakar Mahmoud Gumi</strong>",
      optgroupEastAsia: "🌏 Kudu Maso Gabas da Gabashin Asiya",
      optgroupMidEast: "🕌 Gabas Ta Tsakiya, Tsakiyar Asiya da Caucasus",
      optgroupSouthAsia: "🪷 Kudancin Asiya da Tekun Indiya",
      optgroupAfrica: "🌍 Afirka",
      optgroupEurope: "🏛️ Yamma, Arewa, Tsakiya da Gabashin Turai",
      tabBadgeJamid: "Siffofin Kalmomi 7",
      tabBadgeHarf: "Siffofin Haruffa 17",
      
      // Control Card
      step1Label: "1. Zaɓi Sigar Kalma",
      step1Placeholder: "Zaɓi Sigar Kalma",
      step1OptionDhamir: "1. Wakilan Suna (Dhamir - Pronouns)",
      step1OptionMawshul: "2. Sunayen Sadarwa (Mawshul - Relative Pronouns)",
      step1OptionIstifham: "3. Kalmomin Tambaya (Istifham - Interrogatives)",
      step1OptionSyarath: "4. Kalmomin Sharaɗi (Syarath - Conditionals)",
      step1OptionIsyarah: "5. Sunayen Nuni (Isyarah - Demonstratives)",
      step1OptionIsimFiil: "6. Sunayen Aiki (Isim Fi'il - Verbal Nouns)",
      step1OptionFiilJamid: "7. Ayyuka Kafaffu (Fi'il Jamid - Inflexible Verbs)",
      step2Label: "2. Zaɓi Lambar Kalma",
      step2Placeholder: "Zaɓi Lambar Kalma",
      welcomeTitle: "Da fatan za a zaɓi Sigar Kalma da Lambar Kalma",
      welcomeSubtitle: "Zaɓi Sigar Kalma daga jerin da ke sama don ganin lafazin Larabci, ma'ana, adadin fitowa a Al-Ƙur'ani, da manazartar ayoyi.",
      
      // Spotlight Card
      wordFormBadge: "Sigar Kalma",
      wordNoBadgePrefix: "Lambar Kalma:",
      arabicVoiceBtn: "Muryar Larabci",
      arabicVoiceTooltip: "Saurari Lafazin Larabci (TTS)",
      meaningVoiceBtn: "Muryar Ma'ana",
      meaningVoiceTooltip: "Saurari Ma'ana / Fassarar Hausa (TTS)",
      copyArabicTooltip: "Kwafi Kalmar Larabci",
      copyInfoBtn: "Kwafi Bayani",
      copyInfoTooltip: "Kwafi Cikakken Taƙaitaccen Bayani",
      freqLabel: "Adadin Fitowa a Al-Ƙur'ani",
      freqSub: "Adadin Sau nawa ta Zo",
      freqMuttashilVal: "Muttashil (Mai Maƙalewa)",
      freqMuttashilSub: "Sigar Ƙari / Haɗawa (Sufiksi)",
      totalAyatLabel: "Jimillar Ayoyin Manazarta",
      totalAyatSub: "Akwai a Cikin Bayanai",
      sampleAyatSuffix: "Misalan Ayoyi",
      transliterationPrefix: "Karatun Haruffan Boko:",
      meaningPrefix: "Ma'ana:",
      
      // References Section
      referencesTitlePrefix: "Manazartar Ayoyi na:",
      ayatCountBadgePattern: (cur, total) => `Misalin Aya ${cur} cikin ${total} Ayoyi`,
      ayatCountZero: "Ayoyi 0",
      searchPlaceholder: "Bincika sunan surah / lambar aya...",
      exportCsvBtn: "Fitarwa zuwa CSV",
      exportCsvTooltip: "Sauke manazartar ayoyin wannan kalma a fayil ɗin CSV",
      
      // Ayat Card
      surahPrefix: "Surah",
      surahPositionTag: (cur, surahNo, ayatNo) => `Surah #${surahNo} • Aya #${ayatNo}`,
      playTranslationBtn: "Saurari Fassara",
      stopTranslationBtn: "Dakatar da Murya",
      playTilawahBtn: "Saurari Karatu",
      pauseTilawahBtn: "Dakata da Karatu",
      askAiBtn: "Tambayi AI",
      askAiTooltip: "Tambayi AI game da ƙa'idojin nahawu da tafsirin wannan aya",
      aiModalTitle: "Mataimakin AI na Al-Ƙur'ani",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Nazari: Surah ${suratNama}:${ayat} • Kalmar "${kata}" (${noKata})`,
      aiTopicLabel: "Zaɓi Fannin Nazarin AI:",
      aiPromptPreviewLabel: "Rubutun Tambayar AI (A Shirye):",
      aiTopicNahwu: "🔍 Ƙa'idojin Nahawu & I'rabi",
      aiTopicTafsir: "📖 Tafsiri & Ma'anar Aya",
      aiTopicBalaghah: "✨ Balagar Al-Ƙur'ani",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Kwafi Tambaya",
      toastPromptCopied: "An kwafi tambayar AI zuwa allon kwafi!",
      ayahPill: (n) => `Aya ${n}`,
      flipToArabicBtn: "Duba Larabci",
      flipToTranslationBtn: "Duba Fassara",
      translationBoxHeader: "FASSARAR AYA (HAUSA - SHEIKH ABUBAKAR GUMI)",
      latinBoxHeader: "RUBUTUN HARUFFAN BOKO (TRANSLITERATION)",
      copyLatinBtn: "Kwafi Haruffan Boko",
      arabicBoxHeader: "النص القرآني • CIKAKKEN NASSIN LARABCI",
      latinBackHeader: "KARATUN HARUFFAN BOKO:",
      copyBtn: "Kwafi",
      prevBtn: "Baya",
      nextBtn: "Gaba",
      emptyStateText: "Ba a sami surah ko ayar da ta dace da bincikenka ba.",
      
      // Toasts & Speech
      toastLangChanged: "An canza harshe zuwa Hausa 🇳🇬",
      toastTilawahPaused: "An dakatar da karatu.",
      toastTilawahPlaying: (s, a) => `Ana kunna karatun Surah ${s}:${a} (Mishary Alafasy)`,
      toastTilawahEnded: "An kammala karatu.",
      toastAudioFailed: "An sami matsalar kunna sauti. Da fatan a duba intanet ɗinku.",
      toastTranslationStopped: "An dakatar da karatun fassara.",
      toastTtsNotSupported: "Wannan burawza ba ta goyi bayan karanta rubutu da murya ba.",
      toastTranslationNotAvail: "Babu nassin fassara a yanzu.",
      toastSpeakingMeaning: (suratNama, ayat) => `Ana karanta fassarar Hausa ta Surah ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Lafazin Larabci: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Ana karanta ma'ana: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Ana karanta haruffan Boko na Surah ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `An kwafi nassin Larabci "${word}"!`,
      toastLatinCopied: "An kwafi rubutun Boko!",
      toastSummaryCopied: "An kwafi taƙaitaccen bayanin cikin nasara!",
      toastCsvExported: (nk) => `An yi nasarar fitar da bayanan ${nk} zuwa CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ha || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ha || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Sunan sadarwa' : 'Wakilin suna';
        return `${prefix} ${cleanWord}, ${latin}ma'ana ${arti}. ${desc ? 'Bayani: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }
,
    sw: {
      pageTitle: "Kamusi ya Jamid Mabny | Kamusi na Marejeleo ya Aya za Qur'ani Tukufu",
      brandTitle: "Kamusi ya <span>Jamid Mabny</span>",
      brandSubtitle: "Kamusi Shirikishi ya Aina za Maneno na Nambari za Maneno",
      themeToggleTitle: "Badilisha Mandhari ya Mwangaza / Giza",
      labelLangSelect: "Lugha ya Tafsiri na Sauti:",
      translationSourceHtml: "Tafsiri: <strong>Sheikh Ali Muhsin Al-Barwani</strong>",
      optgroupEastAsia: "🌏 Asia ya Kusini-Mashariki na Asia ya Mashariki",
      optgroupMidEast: "🕌 Mashariki ya Kati, Asia ya Kati na Caucasus",
      optgroupSouthAsia: "🪷 Asia ya Kusini na Bahari ya Hindi",
      optgroupAfrica: "🌍 Afrika",
      optgroupEurope: "🏛️ Ulaya ya Magharibi, Kaskazini, Kati na Mashariki",
      tabBadgeJamid: "Aina 7 za Maneno",
      tabBadgeHarf: "Aina 17 za Harf",
      
      // Control Card
      step1Label: "1. Chagua Aina ya Neno",
      step1Placeholder: "Chagua Aina ya Neno",
      step1OptionDhamir: "1. Viwakilishi vya Nafsi (Dhamir - Pronouns)",
      step1OptionMawshul: "2. Majina ya Kuunganisha (Mawshul - Relative Pronouns)",
      step1OptionIstifham: "3. Maneno ya Kuulizia (Istifham - Interrogatives)",
      step1OptionSyarath: "4. Maneno ya Sharti (Syarath - Conditionals)",
      step1OptionIsyarah: "5. Majina ya Kuonyeshea (Isyarah - Demonstratives)",
      step1OptionIsimFiil: "6. Majina ya Vitendo (Isim Fi'il - Verbal Nouns)",
      step1OptionFiilJamid: "7. Vitendo Visivyobadilika (Fi'il Jamid - Inflexible Verbs)",
      step2Label: "2. Chagua Nambari ya Neno",
      step2Placeholder: "Chagua Nambari ya Neno",
      welcomeTitle: "Tafadhali chagua Aina ya Neno na Nambari ya Neno",
      welcomeSubtitle: "Chagua Aina ya Neno kutoka kwenye orodha hapo juu ili kuona matamshi ya Kiarabu, maana, marudio ndani ya Qur'ani, na marejeleo ya aya.",
      
      // Spotlight Card
      wordFormBadge: "Aina ya Neno",
      wordNoBadgePrefix: "Nambari ya Neno:",
      arabicVoiceBtn: "Sauti ya Kiarabu",
      arabicVoiceTooltip: "Sikiliza Matamshi ya Kiarabu (TTS)",
      meaningVoiceBtn: "Sauti ya Maana",
      meaningVoiceTooltip: "Sikiliza Maana / Tafsiri ya Kiswahili (TTS)",
      copyArabicTooltip: "Nakili Neno la Kiarabu",
      copyInfoBtn: "Nakili Maelezo",
      copyInfoTooltip: "Nakili Muhtasari Kamili wa Neno",
      freqLabel: "Marudio Ndani ya Qur'ani",
      freqSub: "Jumla ya Mara Lilipotajwa",
      freqMuttashilVal: "Muttashil (Kiwakilishi Tegemezi)",
      freqMuttashilSub: "Muundo wa Kiambishi / Mnyambuliko",
      totalAyatLabel: "Jumla ya Aya za Marejeleo",
      totalAyatSub: "Zilizopo kwenye Data",
      sampleAyatSuffix: "Mifano ya Aya",
      transliterationPrefix: "Matamshi ya Herufi za Kilatini:",
      meaningPrefix: "Maana:",
      
      // References Section
      referencesTitlePrefix: "Marejeleo ya Aya kwa:",
      ayatCountBadgePattern: (cur, total) => `Mfano wa Aya ${cur} kati ya ${total} Aya`,
      ayatCountZero: "Aya 0",
      searchPlaceholder: "Tafuta jina la sura / nambari ya aya...",
      exportCsvBtn: "Hamisha kwenye CSV",
      exportCsvTooltip: "Pakua marejeleo ya aya za neno hili katika faili ya CSV",
      
      // Ayat Card
      surahPrefix: "Sura",
      surahPositionTag: (cur, surahNo, ayatNo) => `Sura #${surahNo} • Aya #${ayatNo}`,
      playTranslationBtn: "Sikiliza Tafsiri",
      stopTranslationBtn: "Simamisha Sauti",
      playTilawahBtn: "Sikiliza Kisomo",
      pauseTilawahBtn: "Sitisha Kisomo",
      askAiBtn: "Uliza AI",
      askAiTooltip: "Uliza AI kuhusu kanuni za nahau na tafsiri ya aya hii",
      aiModalTitle: "Msaidizi wa AI wa Qur'ani",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Uchambuzi: Sura ${suratNama}:${ayat} • Neno "${kata}" (${noKata})`,
      aiTopicLabel: "Chagua Eneo la Uchambuzi wa AI:",
      aiPromptPreviewLabel: "Maandishi ya Swali kwa AI (Tayari):",
      aiTopicNahwu: "🔍 Kanuni za Nahau & I'rabu",
      aiTopicTafsir: "📖 Tafsiri & Maana ya Aya",
      aiTopicBalaghah: "✨ Balagha ya Qur'ani",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Nakili Swali",
      toastPromptCopied: "Swali la AI limenakiliwa kwenye ubao wa kunakili!",
      ayahPill: (n) => `Aya ${n}`,
      flipToArabicBtn: "Angalia Kiarabu",
      flipToTranslationBtn: "Angalia Tafsiri",
      translationBoxHeader: "TAFSIRI YA AYA (KISWAHILI - SHEIKH ALI MUHSIN AL-BARWANI)",
      latinBoxHeader: "MATAMSHI YA KILATINI (TRANSLITERATION)",
      copyLatinBtn: "Nakili Kilatini",
      arabicBoxHeader: "النص القرآني • MAANDISHI KAMILI YA KIARABU",
      latinBackHeader: "MATAMSHI YA KILATINI:",
      copyBtn: "Nakili",
      prevBtn: "Nyuma",
      nextBtn: "Mbele",
      emptyStateText: "Hakuna sura au aya inayolingana na utafutaji wako.",
      
      // Toasts & Speech
      toastLangChanged: "Lugha imebadilishwa kuwa Kiswahili 🇹🇿🇰🇪",
      toastTilawahPaused: "Kisomo kimesitishwa.",
      toastTilawahPlaying: (s, a) => `Inacheza kisomo cha Sura ${s}:${a} (Mishary Alafasy)`,
      toastTilawahEnded: "Kisomo kimekamilika.",
      toastAudioFailed: "Hitilafu katika kucheza sauti. Tafadhali angalia mtandao wako.",
      toastTranslationStopped: "Usomaji wa tafsiri umesimamishwa.",
      toastTtsNotSupported: "Kivinjari hiki hakitumii usomaji wa sauti wa maandishi (TTS).",
      toastTranslationNotAvail: "Maandishi ya tafsiri hayapatikani kwa sasa.",
      toastSpeakingMeaning: (suratNama, ayat) => `Inasoma tafsiri ya Kiswahili ya Sura ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Matamshi ya Kiarabu: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Inasoma maana: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Inasoma matamshi ya Kilatini ya Sura ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Maandishi ya Kiarabu "${word}" yamenakiliwa!`,
      toastLatinCopied: "Matamshi ya Kilatini yamenakiliwa!",
      toastSummaryCopied: "Muhtasari umenakiliwa kikamilifu!",
      toastCsvExported: (nk) => `Data ya ${nk} imehamishwa kwa mafanikio kwenye CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_sw || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_sw || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Jina la kuunganisha' : 'Kiwakilishi cha nafsi';
        return `${prefix} ${cleanWord}, ${latin}maana yake ni ${arti}. ${desc ? 'Maelezo: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }
,
    fa: {
      pageTitle: "فرهنگ جامع جامد مبنی | لغت‌نامه و مراجع تعاملی آیات قرآن کریم",
      brandTitle: "فرهنگ <span>جامد مبنی</span>",
      brandSubtitle: "لغت‌نامه تعاملی انواع کلمات و شماره کلمات قرآن کریم",
      themeToggleTitle: "تغییر حالت روشن / تاریک",
      labelLangSelect: "زبان ترجمه و صوت:",
      translationSourceHtml: "ترجمه: <strong>آیت‌الله ناصر مکارم شیرازی</strong>",
      optgroupEastAsia: "🌏 جنوب شرقی و شرق آسیا",
      optgroupMidEast: "🕌 خاورمیانه، آسیای مرکزی و قفقاز",
      optgroupSouthAsia: "🪷 جنوب آسیا و اقیانوس هند",
      optgroupAfrica: "🌍 آفریقا",
      optgroupEurope: "🏛️ غرب، شمال، مرکز و شرق اروپا",
      tabBadgeJamid: "۷ شکل کلمه",
      tabBadgeHarf: "۱۷ شکل حرف",
      
      // Control Card
      step1Label: "۱. انتخاب نوع کلمه",
      step1Placeholder: "نوع کلمه را انتخاب کنید",
      step1OptionDhamir: "۱. ضمایر (Dhamir - Pronouns)",
      step1OptionMawshul: "۲. اسم‌های موصول (Mawshul - Relative Pronouns)",
      step1OptionIstifham: "۳. کلمات پرسشی (Istifham - Interrogatives)",
      step1OptionSyarath: "۴. ادوات شرط (Syarath - Conditionals)",
      step1OptionIsyarah: "۵. اسم‌های اشاره (Isyarah - Demonstratives)",
      step1OptionIsimFiil: "۶. اسم‌های فعل (Isim Fi'il - Verbal Nouns)",
      step1OptionFiilJamid: "۷. افعال جامد (Fi'il Jamid - Inflexible Verbs)",
      step2Label: "۲. انتخاب شماره کلمه",
      step2Placeholder: "شماره کلمه را انتخاب کنید",
      welcomeTitle: "لطفاً نوع کلمه و شماره کلمه را انتخاب نمایید",
      welcomeSubtitle: "نوع کلمه را از فهرست بالا انتخاب کنید تا تلفظ عربی، معنی، بسامد تکرار در قرآن و آیات مرجع نمایش داده شود.",
      
      // Spotlight Card
      wordFormBadge: "نوع کلمه",
      wordNoBadgePrefix: "شماره کلمه:",
      arabicVoiceBtn: "صوت عربی",
      arabicVoiceTooltip: "شنیدن تلفظ عربی (TTS)",
      meaningVoiceBtn: "صوت معنی",
      meaningVoiceTooltip: "شنیدن معنی / ترجمه فارسی (TTS)",
      copyArabicTooltip: "کپی کلمه عربی",
      copyInfoBtn: "کپی مشخصات",
      copyInfoTooltip: "کپی چکیده کامل مشخصات کلمه",
      freqLabel: "بسامد تکرار در قرآن",
      freqSub: "تعداد کل دفعات ذکر شده",
      freqMuttashilVal: "متصل (ضمایر پیوسته)",
      freqMuttashilSub: "ساختار پسوندی / ترکیبی",
      totalAyatLabel: "تعداد آیات مرجع",
      totalAyatSub: "موجود در پایگاه داده",
      sampleAyatSuffix: "نمونه آیات",
      transliterationPrefix: "آوانگاری لاتین:",
      meaningPrefix: "معنی:",
      
      // References Section
      referencesTitlePrefix: "آیات مرجع برای:",
      ayatCountBadgePattern: (cur, total) => `نمونه آیه ${cur} از ${total} آیه`,
      ayatCountZero: "۰ آیه",
      searchPlaceholder: "جستجوی نام سوره / شماره آیه...",
      exportCsvBtn: "خروجی CSV",
      exportCsvTooltip: "دانلود آیات مرجع این کلمه در قالب فایل CSV",
      
      // Ayat Card
      surahPrefix: "سوره",
      surahPositionTag: (cur, surahNo, ayatNo) => `سوره #${surahNo} • آیه #${ayatNo}`,
      playTranslationBtn: "پخش ترجمه",
      stopTranslationBtn: "توقف صوت",
      playTilawahBtn: "پخش تلاوت",
      pauseTilawahBtn: "توقف تلاوت",
      askAiBtn: "پرسش از هوش مصنوعی",
      askAiTooltip: "پرسش از هوش مصنوعی درباره نکات نحوی، صرفی و تفسیر این آیه",
      aiModalTitle: "دستیار هوش مصنوعی قرآن کریم",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `تحلیل: سوره ${suratNama}:${ayat} • کلمه «${kata}» (${noKata})`,
      aiTopicLabel: "انتخاب موضوع تحلیل هوش مصنوعی:",
      aiPromptPreviewLabel: "متن پرسش هوش مصنوعی (آماده ارسال):",
      aiTopicNahwu: "🔍 قواعد نحو، صرف و اعراب",
      aiTopicTafsir: "📖 تفسیر و پیام آیه",
      aiTopicBalaghah: "✨ بلاغت و اعجاز کلامی قرآن",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "کپی متن پرسش",
      toastPromptCopied: "متن پرسش هوش مصنوعی در حافظه کپی شد!",
      ayahPill: (n) => `آیه ${n}`,
      flipToArabicBtn: "مشاهده متن عربی",
      flipToTranslationBtn: "مشاهده ترجمه",
      translationBoxHeader: "ترجمه آیه (فارسی - آیت‌الله مکارم شیرازی)",
      latinBoxHeader: "آوانگاری لاتین (TRANSLITERATION)",
      copyLatinBtn: "کپی آوانگاری",
      arabicBoxHeader: "النص القرآني • متن کامل آیه به زبان عربی",
      latinBackHeader: "آوانگاری لاتین:",
      copyBtn: "کپی",
      prevBtn: "قبلی",
      nextBtn: "بعدی",
      emptyStateText: "هیچ سوره یا آیه‌ای مطابق با جستجوی شما یافت نشد.",
      
      // Toasts & Speech
      toastLangChanged: "زبان برنامه به فارسی تغییر یافت 🇮🇷",
      toastTilawahPaused: "تلاوت متوقف شد.",
      toastTilawahPlaying: (s, a) => `در حال پخش تلاوت سوره ${s}:${a} (استاد مشاری راشد العفاسی)`,
      toastTilawahEnded: "تلاوت به پایان رسید.",
      toastAudioFailed: "خطا در پخش صوت. لطفاً اتصال اینترنت خود را بررسی کنید.",
      toastTranslationStopped: "پخش صوت ترجمه متوقف شد.",
      toastTtsNotSupported: "مرورگر شما از سیستم تبدیل متن به گفتار (TTS) پشتیبانی نمی‌کند.",
      toastTranslationNotAvail: "متن ترجمه در دسترس نیست.",
      toastSpeakingMeaning: (suratNama, ayat) => `در حال خواندن ترجمه فارسی سوره ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `تلفظ عربی: ${word}`,
      toastSpeakingWordMeaning: (arti) => `در حال قرائت معنی: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `در حال قرائت آوانگاری سوره ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `متن عربی «${word}» کپی شد!`,
      toastLatinCopied: "آوانگاری لاتین کپی شد!",
      toastSummaryCopied: "چکیده مشخصات با موفقیت کپی شد!",
      toastCsvExported: (nk) => `اطلاعات کلمه ${nk} با موفقیت در قالب CSV ذخیره شد!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_fa || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_fa || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'اسم موصول' : 'ضمیر';
        return `${prefix} ${cleanWord}, ${latin}به معنی ${arti}. ${desc ? 'توضیحات: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }
,
    ja: {
      pageTitle: "ジャーミド・マブニー辞書 | クルアーン語形・節対話型リファレンス",
      brandTitle: "ジャーミド・マブニー <span>辞書</span>",
      brandSubtitle: "クルアーン語形と語番号の対話型辞典",
      themeToggleTitle: "ダーク / ライトテーマ切り替え",
      labelLangSelect: "翻訳言語と音声:",
      translationSourceHtml: "翻訳: <strong>日本ムスリム協会 / 三田了一 訳 (Ryoichi Mita)</strong>",
      optgroupEastAsia: "🌏 東南アジア・東アジア",
      optgroupMidEast: "🕌 中東・中央アジア・コーカサス",
      optgroupSouthAsia: "🪷 南アジア・インド洋",
      optgroupAfrica: "🌍 アフリカ",
      optgroupEurope: "🏛️ 西欧・北欧・中欧・東欧",
      tabBadgeJamid: "7つの語形",
      tabBadgeHarf: "17の助詞形態",
      
      // Control Card
      step1Label: "1. 語形を選択",
      step1Placeholder: "語形を選択してください",
      step1OptionDhamir: "1. 代名詞 (Dhamir - Pronouns)",
      step1OptionMawshul: "2. 関係代名詞 (Mawshul - Relative Pronouns)",
      step1OptionIstifham: "3. 疑問詞 (Istifham - Interrogatives)",
      step1OptionSyarath: "4. 条件詞 (Syarath - Conditionals)",
      step1OptionIsyarah: "5. 指示代名詞 (Isyarah - Demonstratives)",
      step1OptionIsimFiil: "6. 動詞性名詞 (Isim Fi'il - Verbal Nouns)",
      step1OptionFiilJamid: "7. 固着動詞 (Fi'il Jamid - Inflexible Verbs)",
      step2Label: "2. 語番号を選択",
      step2Placeholder: "語番号を選択してください",
      welcomeTitle: "語形と語番号を選択してください",
      welcomeSubtitle: "上のメニューから語形を選択すると、アラビア語表記、日本語訳、クルアーン内出現頻度、および参照節が表示されます。",
      
      // Spotlight Card
      wordFormBadge: "語形",
      wordNoBadgePrefix: "語番号:",
      arabicVoiceBtn: "アラビア語音声",
      arabicVoiceTooltip: "アラビア語の発音を聞く (TTS)",
      meaningVoiceBtn: "意味の音声",
      meaningVoiceTooltip: "日本語の意味・訳を聞く (TTS)",
      copyArabicTooltip: "アラビア語単語をコピー",
      copyInfoBtn: "情報をコピー",
      copyInfoTooltip: "単語の全詳細をコピー",
      freqLabel: "クルアーン内出現頻度",
      freqSub: "総出現回数",
      freqMuttashilVal: "接尾形（ムッタスィル）",
      freqMuttashilSub: "接尾辞・結合構造",
      totalAyatLabel: "参照節の総数",
      totalAyatSub: "データセット内収録数",
      sampleAyatSuffix: "例文・参照節",
      transliterationPrefix: "ローマ字転写:",
      meaningPrefix: "意味:",
      
      // References Section
      referencesTitlePrefix: "クルアーン参照節:",
      ayatCountBadgePattern: (cur, total) => `節 ${cur} / ${total}`,
      ayatCountZero: "0 節",
      searchPlaceholder: "章名または節番号で検索...",
      exportCsvBtn: "CSVエクスポート",
      exportCsvTooltip: "この単語の全参照節をCSV形式でダウンロード",
      
      // Ayat Card
      surahPrefix: "章 (スーラ)",
      surahPositionTag: (cur, surahNo, ayatNo) => `第${surahNo}章 • 第${ayatNo}節`,
      playTranslationBtn: "訳文を聞く",
      stopTranslationBtn: "音声を停止",
      playTilawahBtn: "朗誦を聞く",
      pauseTilawahBtn: "朗誦を一時停止",
      askAiBtn: "AIに質問",
      askAiTooltip: "この節の文法や注釈についてAIに質問する",
      aiModalTitle: "クルアーンAIアシスタント",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `分析: 第${suratNama}章:${ayat} • 単語「${kata}」(${noKata})`,
      aiTopicLabel: "AI分析トピックを選択:",
      aiPromptPreviewLabel: "作成されたAIプロンプト:",
      aiTopicNahwu: "🔍 ナフウ (文法・構文解析) と格変化 (イアラーブ)",
      aiTopicTafsir: "📖 タフスィール (節の注釈と教訓)",
      aiTopicBalaghah: "✨ バラーガ (クルアーンの修辞美と文体)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "プロンプトをコピー",
      toastPromptCopied: "AIプロンプトをクリップボードにコピーしました！",
      ayahPill: (n) => `第${n}節`,
      flipToArabicBtn: "アラビア語本文を見る",
      flipToTranslationBtn: "日本語訳を見る",
      translationBoxHeader: "節の日本語訳 (三田了一 訳 / 日本ムスリム協会)",
      latinBoxHeader: "ローマ字転写 (TRANSLITERATION)",
      copyLatinBtn: "転写をコピー",
      arabicBoxHeader: "النص القرآني • アラビア語全文",
      latinBackHeader: "ローマ字転写:",
      copyBtn: "コピー",
      prevBtn: "前へ",
      nextBtn: "次へ",
      emptyStateText: "検索条件に一致する章や節が見つかりませんでした。",
      
      // Toasts & Speech
      toastLangChanged: "言語を日本語に切り替えました 🇯🇵",
      toastTilawahPaused: "朗誦を一時停止しました。",
      toastTilawahPlaying: (s, a) => `第${s}章:${a}節の朗誦を再生中 (ミシャリー・ラシード・アル＝アファスィー)`,
      toastTilawahEnded: "朗誦が終了しました。",
      toastAudioFailed: "音声の再生に失敗しました。接続をご確認ください。",
      toastTranslationStopped: "訳文の読み上げを停止しました。",
      toastTtsNotSupported: "お使いのブラウザは音声合成 (TTS) に対応していません。",
      toastTranslationNotAvail: "翻訳テキストが利用できません。",
      toastSpeakingMeaning: (suratNama, ayat) => `第${suratNama}章:${ayat}節の日本語訳を読み上げ中`,
      toastSpeakingArabic: (word) => `アラビア語発音: ${word}`,
      toastSpeakingWordMeaning: (arti) => `意味を読み上げ中: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `第${suratNama}章:${ayat}節の転写を読み上げ中`,
      toastArabicCopied: (word) => `アラビア語「${word}」をコピーしました！`,
      toastLatinCopied: "ローマ字転写をコピーしました！",
      toastSummaryCopied: "単語の全詳細をコピーしました！",
      toastCsvExported: (nk) => `単語 ${nk} の参照節をCSVに出力しました！`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ja || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ja || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? '関係代名詞' : '代名詞';
        return `${prefix} ${cleanWord}、${latin}意味は「${arti}」。${desc ? '解説：' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    ko: {
      pageTitle: "자미드 맙니 사전 | 꾸란 단어 및 구절 대화형 참조",
      brandTitle: "자미드 맙니 <span>사전</span>",
      brandSubtitle: "꾸란 단어 형태 및 단어 번호 대화형 사전",
      themeToggleTitle: "다크 / 라이트 테마 전환",
      labelLangSelect: "번역 언어 및 음성:",
      translationSourceHtml: "번역: <strong>최영길 박사 번역 (파드 국왕 성원 출판)</strong>",
      optgroupEastAsia: "🌏 동남아시아 및 동아시아",
      optgroupMidEast: "🕌 중동, 중앙아시아 및 코카서스",
      optgroupSouthAsia: "🪷 남아시아 및 인도양",
      optgroupAfrica: "🌍 아프리카",
      optgroupEurope: "🏛️ 서유럽, 북유럽, 중유럽 및 동유럽",
      tabBadgeJamid: "7가지 어형",
      tabBadgeHarf: "17가지 불변사 형태",
      
      // Control Card
      step1Label: "1. 단어 형태 선택",
      step1Placeholder: "단어 형태를 선택하세요",
      step1OptionDhamir: "1. 대명사 (Dhamir - Pronouns)",
      step1OptionMawshul: "2. 관계대명사 (Mawshul - Relative Pronouns)",
      step1OptionIstifham: "3. 의문사 (Istifham - Interrogatives)",
      step1OptionSyarath: "4. 조건사 (Syarath - Conditionals)",
      step1OptionIsyarah: "5. 지시대명사 (Isyarah - Demonstratives)",
      step1OptionIsimFiil: "6. 동사성 명사 (Isim Fi'il - Verbal Nouns)",
      step1OptionFiilJamid: "7. 불변동사 (Fi'il Jamid - Inflexible Verbs)",
      step2Label: "2. 단어 번호 선택",
      step2Placeholder: "단어 번호를 선택하세요",
      welcomeTitle: "단어 형태와 번호를 선택해 주세요",
      welcomeSubtitle: "위 메뉴에서 단어 형태를 선택하면 아랍어 표기, 한국어 번역, 꾸란 내 빈도 및 참조 구절이 표시됩니다.",
      
      // Spotlight Card
      wordFormBadge: "단어 형태",
      wordNoBadgePrefix: "단어 번호:",
      arabicVoiceBtn: "아랍어 음성",
      arabicVoiceTooltip: "아랍어 발음 듣기 (TTS)",
      meaningVoiceBtn: "의미 음성",
      meaningVoiceTooltip: "한국어 의미 및 번역 듣기 (TTS)",
      copyArabicTooltip: "아랍어 단어 복사",
      copyInfoBtn: "정보 복사",
      copyInfoTooltip: "단어 전체 상세 정보 복사",
      freqLabel: "꾸란 내 출현 빈도",
      freqSub: "총 언급 횟수",
      freqMuttashilVal: "접미형 (뭇타실)",
      freqMuttashilSub: "접미 결합 구조",
      totalAyatLabel: "총 참조 구절 수",
      totalAyatSub: "데이터셋 수록 구절",
      sampleAyatSuffix: "예시 구절",
      transliterationPrefix: "로마자 전사:",
      meaningPrefix: "의미:",
      
      // References Section
      referencesTitlePrefix: "꾸란 참조 구절:",
      ayatCountBadgePattern: (cur, total) => `구절 ${cur} / ${total}`,
      ayatCountZero: "0 구절",
      searchPlaceholder: "장 이름 또는 구절 번호 검색...",
      exportCsvBtn: "CSV 내보내기",
      exportCsvTooltip: "이 단어의 모든 참조 구절을 CSV 파일로 다운로드",
      
      // Ayat Card
      surahPrefix: "장 (수라)",
      surahPositionTag: (cur, surahNo, ayatNo) => `제${surahNo}장 • 제${ayatNo}절`,
      playTranslationBtn: "번역 듣기",
      stopTranslationBtn: "음성 정지",
      playTilawahBtn: "낭송 듣기",
      pauseTilawahBtn: "낭송 일시정지",
      askAiBtn: "AI에게 질문",
      askAiTooltip: "이 구절의 문법 및 해석에 대해 AI에게 질문하기",
      aiModalTitle: "꾸란 AI 어시스턴트",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `분석: 제${suratNama}장:${ayat} • 단어 "${kata}" (${noKata})`,
      aiTopicLabel: "AI 분석 주제 선택:",
      aiPromptPreviewLabel: "생성된 AI 프롬프트:",
      aiTopicNahwu: "🔍 나흐우 (아랍어 문법) 및 격변화 (이라브)",
      aiTopicTafsir: "📖 타프시르 (구절의 주석 및 교훈)",
      aiTopicBalaghah: "✨ 발라가 (꾸란의 수사학적 아름다움)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "프롬프트 복사",
      toastPromptCopied: "AI 프롬프트가 클립보드에 복사되었습니다!",
      ayahPill: (n) => `제${n}절`,
      flipToArabicBtn: "아랍어 본문 보기",
      flipToTranslationBtn: "한국어 번역 보기",
      translationBoxHeader: "구절 한국어 번역 (최영길 박사 번역)",
      latinBoxHeader: "로마자 발음 전사 (TRANSLITERATION)",
      copyLatinBtn: "전사 복사",
      arabicBoxHeader: "النص القرآني • 아랍어 전문",
      latinBackHeader: "로마자 전사:",
      copyBtn: "복사",
      prevBtn: "이전",
      nextBtn: "다음",
      emptyStateText: "검색 조건과 일치하는 장 또는 구절을 찾을 수 없습니다.",
      
      // Toasts & Speech
      toastLangChanged: "언어가 한국어로 변경되었습니다 🇰🇷",
      toastTilawahPaused: "낭송이 일시정지되었습니다.",
      toastTilawahPlaying: (s, a) => `제${s}장:${a}절 낭송 재생 중 (미샤리 라시드 알아파시)`,
      toastTilawahEnded: "낭송이 종료되었습니다.",
      toastAudioFailed: "오디오 재생 오류. 인터넷 연결을 확인해 주세요.",
      toastTranslationStopped: "번역 음성 재생이 정지되었습니다.",
      toastTtsNotSupported: "사용 중인 브라우저가 텍스트 음성 변환 (TTS)을 지원하지 않습니다.",
      toastTranslationNotAvail: "번역 텍스트를 사용할 수 없습니다.",
      toastSpeakingMeaning: (suratNama, ayat) => `제${suratNama}장:${ayat}절 한국어 번역 낭독 중`,
      toastSpeakingArabic: (word) => `아랍어 발음: ${word}`,
      toastSpeakingWordMeaning: (arti) => `의미 낭독 중: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `제${suratNama}장:${ayat}절 로마자 전사 낭독 중`,
      toastArabicCopied: (word) => `아랍어 "${word}" 복사 완료!`,
      toastLatinCopied: "로마자 전사가 복사되었습니다!",
      toastSummaryCopied: "단어 상세 정보가 클립보드에 복사되었습니다!",
      toastCsvExported: (nk) => `단어 ${nk}의 참조 구절이 CSV로 저장되었습니다!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ko || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ko || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? '관계대명사' : '대명사';
        return `${prefix} ${cleanWord}, ${latin}의미는 ${arti}. ${desc ? '설명: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }
,
    nl: {
      pageTitle: "Woordenboek Jamid Mabny | Interactieve Koran Woorden & Versverwijzingen",
      brandTitle: "Woordenboek <span>Jamid Mabny</span>",
      brandSubtitle: "Interactief Woordenboek voor Vaste en Onveranderlijke Woorden",
      themeToggleTitle: "Donker / Licht Thema Schakelen",
      labelLangSelect: "Vertaling- en Spraaktaal:",
      translationSourceHtml: "Vertaling: <strong>Sofian S. Siregar</strong>",
      optgroupEastAsia: "🌏 Zuidoost- & Oost-Azië",
      optgroupMidEast: "🕌 Midden-Oosten, Centraal-Azië & Kaukasus",
      optgroupSouthAsia: "🪷 Zuid-Azië & Indische Oceaan",
      optgroupAfrica: "🌍 Afrika",
      optgroupEurope: "🏛️ West-, Noord-, Midden- & Oost-Europa",
      tabBadgeJamid: "7 Woordvormen",
      tabBadgeHarf: "17 Harf-vormen",
      
      // Control Card
      step1Label: "1. Selecteer Woordvorm",
      step1Placeholder: "Selecteer Woordvorm",
      step1OptionDhamir: "1. Voornaamwoorden (Dhamir - Persoonlijke & Bezittelijke Voornaamwoorden)",
      step1OptionMawshul: "2. Betrekkelijke Voornaamwoorden (Mawshul - Relatieve Voornaamwoorden)",
      step1OptionIstifham: "3. Vragende Voornaamwoorden (Istifham - Vraagelementen)",
      step1OptionSyarath: "4. Voorwaardelijke Nomina (Syarath - Conditionele Woorden)",
      step1OptionIsyarah: "5. Aanwijzende Voornaamwoorden (Isyarah - Demonstratieven)",
      step1OptionIsimFiil: "6. Verbale Zelfstandige Naamwoorden (Isim Fi'il - Verbale Nomina)",
      step1OptionFiilJamid: "7. Onvervoegbare Werkwoorden (Fi'il Jamid - Vaste Werkwoorden)",
      step2Label: "2. Selecteer Woordnummer",
      step2Placeholder: "Selecteer Woordnummer",
      welcomeTitle: "Kies een Woordvorm en Woordnummer",
      welcomeSubtitle: "Selecteer een woordvorm uit het bovenstaande menu om Arabische spelling, betekenis, frequentie in de Koran en versverwijzingen te bekijken.",
      
      // Spotlight Card
      wordFormBadge: "Woordvorm",
      wordNoBadgePrefix: "Woord Nr:",
      arabicVoiceBtn: "Arabische Stem",
      arabicVoiceTooltip: "Luister naar Arabische uitspraak (Arabische TTS)",
      meaningVoiceBtn: "Betekenisstem",
      meaningVoiceTooltip: "Luister naar Nederlandse betekenis (Nederlandse TTS)",
      copyArabicTooltip: "Kopieer Arabisch Woord",
      copyInfoBtn: "Kopieer Info",
      copyInfoTooltip: "Kopieer Alle Woorddetails",
      freqLabel: "Frequentie in de Koran",
      freqSub: "Totaal Aantal Vermeldingen",
      freqMuttashilVal: "Aangehechte Vorm (Muttashil)",
      freqMuttashilSub: "Als Aangehecht Voornaamwoord",
      totalAyatLabel: "Totaal Referentieverzen",
      totalAyatSub: "Voorbeeldverzen Beschikbaar",
      sampleAyatSuffix: "Verzen",
      transliterationPrefix: "Transliteratie:",
      meaningPrefix: "Betekenis:",
      
      // References Section
      referencesTitlePrefix: "Versverwijzingen in de Koran:",
      ayatCountBadgePattern: (cur, total) => `Vers ${cur} van ${total}`,
      ayatCountZero: "0 Verzen",
      searchPlaceholder: "Zoek op Soerah-naam of versnummer...",
      exportCsvBtn: "Exporteer CSV",
      exportCsvTooltip: "Download alle referentieverzen voor dit woord als CSV-bestand",
      
      // Ayat Card
      surahPrefix: "Soerah",
      surahPositionTag: (cur, surahNo, ayatNo) => `Soerah #${surahNo} • Vers #${ayatNo}`,
      playTranslationBtn: "Nederlandse Vertaling",
      stopTranslationBtn: "Stop Spraak",
      playTilawahBtn: "Koranrecitatie",
      pauseTilawahBtn: "Pauzeer Recitatie",
      askAiBtn: "Vraag AI",
      askAiTooltip: "Stel een vraag aan AI over de grammatica en betekenis van dit vers",
      aiModalTitle: "Koran AI Assistent",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Analyseer Soerah ${suratNama}:${ayat} • Woord "${kata}" (${noKata})`,
      aiTopicLabel: "Kies AI-analyseonderwerp:",
      aiPromptPreviewLabel: "Gegenereerde AI-prompt:",
      aiTopicNahwu: "🔍 Nahw (Arabische Grammatica & Syntaxis) en I'rab (Naamval)",
      aiTopicTafsir: "📖 Tafsir (Uitleg & Context van het Vers)",
      aiTopicBalaghah: "✨ Balaghah (Retoriek & Literaire Schoonheid van de Koran)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Kopieer Prompt",
      toastPromptCopied: "AI-prompt succesvol gekopieerd naar klembord!",
      ayahPill: (n) => `Vers ${n}`,
      flipToArabicBtn: "Bekijk Arabische Tekst",
      flipToTranslationBtn: "Bekijk Nederlandse Vertaling",
      translationBoxHeader: "Nederlandse Vertaling (Sofian S. Siregar)",
      latinBoxHeader: "Latijnse Transliteratie",
      copyLatinBtn: "Kopieer Transliteratie",
      arabicBoxHeader: "النص القرآني • Volledige Arabische Tekst",
      latinBackHeader: "Latijnse Transliteratie:",
      copyBtn: "Kopiëren",
      prevBtn: "Vorige",
      nextBtn: "Volgende",
      emptyStateText: "Geen Soerah of vers gevonden die overeenkomt met uw zoekopdracht.",
      
      // Toasts & Speech
      toastLangChanged: "Taal succesvol gewijzigd naar Nederlands 🇳🇱",
      toastTilawahPaused: "Koranrecitatie gepauzeerd.",
      toastTilawahPlaying: (s, a) => `Recitatie van Soerah ${s}:${a} wordt afgespeeld (Mishary Rashid Alafasy)`,
      toastTilawahEnded: "Recitatie voltooid.",
      toastAudioFailed: "Fout bij afspelen van audio. Controleer uw verbinding.",
      toastTranslationStopped: "Voorlezen van vertaling gestopt.",
      toastTtsNotSupported: "Uw browser ondersteunt geen spraaksynthese (TTS).",
      toastTranslationNotAvail: "Vertalingtekst niet beschikbaar.",
      toastSpeakingMeaning: (suratNama, ayat) => `Nederlandse vertaling van Soerah ${suratNama}:${ayat} voorlezen`,
      toastSpeakingArabic: (word) => `Arabische uitspraak: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Betekenis voorlezen: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Transliteratie van Soerah ${suratNama}:${ayat} voorlezen`,
      toastArabicCopied: (word) => `Arabisch woord "${word}" gekopieerd naar klembord!`,
      toastLatinCopied: "Latijnse transliteratie gekopieerd!",
      toastSummaryCopied: "Volledige woorddetails gekopieerd naar klembord!",
      toastCsvExported: (nk) => `Versverwijzingen voor woord ${nk} geëxporteerd naar CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_nl || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_nl || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Betrekkelijk voornaamwoord' : 'Voornaamwoord';
        return `${prefix} ${cleanWord}, ${latin}betekent ${arti}. ${desc ? 'Uitleg: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    it: {
      pageTitle: "Dizionario Jamid Mabny | Riferimenti Interattivi di Parole e Versetti Coranici",
      brandTitle: "Dizionario <span>Jamid Mabny</span>",
      brandSubtitle: "Dizionario Interattivo per Forme di Parole e Numeri Coranici",
      themeToggleTitle: "Cambia Tema Scuro / Chiaro",
      labelLangSelect: "Lingua di Traduzione e Voce:",
      translationSourceHtml: "Traduzione: <strong>Hamza Roberto Piccardo</strong>",
      optgroupEastAsia: "🌏 Sud-est asiatico & Asia orientale",
      optgroupMidEast: "🕌 Medio Oriente, Asia centrale & Caucaso",
      optgroupSouthAsia: "🪷 Asia meridionale & Oceano Indiano",
      optgroupAfrica: "🌍 Africa",
      optgroupEurope: "🏛️ Europa occidentale, settentrionale, centrale & orientale",
      tabBadgeJamid: "7 Forme di Parole",
      tabBadgeHarf: "17 Forme di Harf",
      
      // Control Card
      step1Label: "1. Seleziona Forma della Parola",
      step1Placeholder: "Seleziona Forma della Parola",
      step1OptionDhamir: "1. Pronomi (Dhamir - Pronomi Personali e Possessivi)",
      step1OptionMawshul: "2. Pronomi Relativi (Mawshul)",
      step1OptionIstifham: "3. Pronomi Interrogativi (Istifham)",
      step1OptionSyarath: "4. Sostantivi Condizionali (Syarath)",
      step1OptionIsyarah: "5. Pronomi Dimostrativi (Isyarah)",
      step1OptionIsimFiil: "6. Nomi Verbali (Isim Fi'il)",
      step1OptionFiilJamid: "7. Verbi Invariabili / Difettivi (Fi'il Jamid)",
      step2Label: "2. Seleziona Numero della Parola",
      step2Placeholder: "Seleziona Numero della Parola",
      welcomeTitle: "Seleziona una Forma di Parola e Numero",
      welcomeSubtitle: "Scegli una forma dal menu sopra per visualizzare la scrittura araba, il significato, la frequenza nel Corano e i versetti di riferimento.",
      
      // Spotlight Card
      wordFormBadge: "Forma della Parola",
      wordNoBadgePrefix: "Parola N°:",
      arabicVoiceBtn: "Voce Araba",
      arabicVoiceTooltip: "Ascolta la pronuncia araba (TTS Arabo)",
      meaningVoiceBtn: "Voce Traduzione",
      meaningVoiceTooltip: "Ascolta il significato in italiano (TTS Italiano)",
      copyArabicTooltip: "Copia Parola Araba",
      copyInfoBtn: "Copia Info",
      copyInfoTooltip: "Copia Tutti i Dettagli della Parola",
      freqLabel: "Frequenza nel Corano",
      freqSub: "Numero Totale di Ricorrenze",
      freqMuttashilVal: "Forma Suffissa (Muttashil)",
      freqMuttashilSub: "Come Pronome Suffisso",
      totalAyatLabel: "Versetti di Riferimento Totali",
      totalAyatSub: "Versetti di Esempio Disponibili",
      sampleAyatSuffix: "Versetti",
      transliterationPrefix: "Traslitterazione:",
      meaningPrefix: "Significato:",
      
      // References Section
      referencesTitlePrefix: "Versetti Coranici di Riferimento:",
      ayatCountBadgePattern: (cur, total) => `Versetto ${cur} di ${total}`,
      ayatCountZero: "0 Versetti",
      searchPlaceholder: "Cerca per nome della Sura o numero del versetto...",
      exportCsvBtn: "Esporta CSV",
      exportCsvTooltip: "Scarica tutti i versetti di riferimento per questa parola in formato CSV",
      
      // Ayat Card
      surahPrefix: "Sura",
      surahPositionTag: (cur, surahNo, ayatNo) => `Sura #${surahNo} • Versetto #${ayatNo}`,
      playTranslationBtn: "Traduzione Italiana",
      stopTranslationBtn: "Ferma Voce",
      playTilawahBtn: "Recitazione Coranica",
      pauseTilawahBtn: "Pausa Recitazione",
      askAiBtn: "Chiedi all'AI",
      askAiTooltip: "Fai una domanda all'AI sulla grammatica e il significato di questo versetto",
      aiModalTitle: "Assistente AI del Corano",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Analisi: Sura ${suratNama}:${ayat} • Parola "${kata}" (${noKata})`,
      aiTopicLabel: "Scegli l'argomento di analisi AI:",
      aiPromptPreviewLabel: "Prompt AI generato:",
      aiTopicNahwu: "🔍 Nahw (Grammatica e Sintassi Araba) e I'rab (Declinazione)",
      aiTopicTafsir: "📖 Tafsir (Esegesi e Contesto del Versetto)",
      aiTopicBalaghah: "✨ Balaghah (Retorica ed Eloquenza Coranica)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Copia Prompt",
      toastPromptCopied: "Prompt AI copiato negli appunti!",
      ayahPill: (n) => `Versetto ${n}`,
      flipToArabicBtn: "Mostra Testo Arabo",
      flipToTranslationBtn: "Mostra Traduzione Italiana",
      translationBoxHeader: "Traduzione Italiana (Hamza Roberto Piccardo)",
      latinBoxHeader: "Traslitterazione Latina",
      copyLatinBtn: "Copia Traslitterazione",
      arabicBoxHeader: "النص القرآني • Testo Arabo Completo",
      latinBackHeader: "Traslitterazione Latina:",
      copyBtn: "Copia",
      prevBtn: "Precedente",
      nextBtn: "Successivo",
      emptyStateText: "Nessuna Sura o versetto corrispondente alla ricerca.",
      
      // Toasts & Speech
      toastLangChanged: "Lingua cambiata con successo in Italiano 🇮🇹",
      toastTilawahPaused: "Recitazione coranica in pausa.",
      toastTilawahPlaying: (s, a) => `Riproduzione della recitazione della Sura ${s}:${a} (Mishary Rashid Alafasy)`,
      toastTilawahEnded: "Recitazione completata.",
      toastAudioFailed: "Errore di riproduzione audio. Controlla la connessione.",
      toastTranslationStopped: "Lettura della traduzione interrotta.",
      toastTtsNotSupported: "Il tuo browser non supporta la sintesi vocale (TTS).",
      toastTranslationNotAvail: "Testo di traduzione non disponibile.",
      toastSpeakingMeaning: (suratNama, ayat) => `Lettura traduzione italiana della Sura ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Pronuncia araba: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Lettura significato: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Lettura traslitterazione della Sura ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Parola araba "${word}" copiata negli appunti!`,
      toastLatinCopied: "Traslitterazione latina copiata!",
      toastSummaryCopied: "Dettagli completi della parola copiati negli appunti!",
      toastCsvExported: (nk) => `Versetti di riferimento per la parola ${nk} esportati in CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_it || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_it || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Pronome relativo' : 'Pronome';
        return `${prefix} ${cleanWord}, ${latin}significa ${arti}. ${desc ? 'Spiegazione: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    bs: {
      pageTitle: "Rječnik Jamid Mabny | Interaktivne kur'anske riječi i reference ajeta",
      brandTitle: "Rječnik <span>Jamid Mabny</span>",
      brandSubtitle: "Interaktivni rječnik za oblike i brojeve riječi u Kur'anu",
      themeToggleTitle: "Promijeni tamnu / svijetlu temu",
      labelLangSelect: "Jezik prijevoda i zvuka:",
      translationSourceHtml: "Prijevod: <strong>Besim Korkut</strong>",
      optgroupEastAsia: "🌏 Jugoistočna i Istočna Azija",
      optgroupMidEast: "🕌 Bliski Istok, Centralna Azija i Kavkaz",
      optgroupSouthAsia: "🪷 Južna Azija i Indijski okean",
      optgroupAfrica: "🌍 Afrika",
      optgroupEurope: "🏛️ Zapadna, Sjeverna, Srednja i Istočna Evropa",
      tabBadgeJamid: "7 oblika riječi",
      tabBadgeHarf: "17 oblika harfova",
      
      // Control Card
      step1Label: "1. Odaberite oblik riječi",
      step1Placeholder: "Odaberite oblik riječi",
      step1OptionDhamir: "1. Zamjenice (Dhamir - Lične i prisvojne zamjenice)",
      step1OptionMawshul: "2. Odnosne zamjenice (Mawshul - Relativne zamjenice)",
      step1OptionIstifham: "3. Upitne zamjenice (Istifham - Upitne riječi)",
      step1OptionSyarath: "4. Uslovne imenice (Syarath - Kondicionalne riječi)",
      step1OptionIsyarah: "5. Pokazne zamjenice (Isyarah - Demonstrativne zamjenice)",
      step1OptionIsimFiil: "6. Glagolske imenice (Isim Fi'il - Verbalne imenice)",
      step1OptionFiilJamid: "7. Nemenjivi glagoli (Fi'il Jamid - Statični glagoli)",
      step2Label: "2. Odaberite broj riječi",
      step2Placeholder: "Odaberite broj riječi",
      welcomeTitle: "Molimo odaberite oblik i broj riječi",
      welcomeSubtitle: "Odaberite oblik riječi iz gornjeg menija da biste vidjeli arapski tekst, značenje, učestalost u Kur'anu i listu referentnih ajeta.",
      
      // Spotlight Card
      wordFormBadge: "Oblik riječi",
      wordNoBadgePrefix: "Broj riječi:",
      arabicVoiceBtn: "Arapski glas",
      arabicVoiceTooltip: "Slušajte arapski izgovor (Arapski TTS)",
      meaningVoiceBtn: "Glas prijevoda",
      meaningVoiceTooltip: "Slušajte značenje na bosanskom jeziku (TTS)",
      copyArabicTooltip: "Kopiraj arapsku riječ",
      copyInfoBtn: "Kopiraj info",
      copyInfoTooltip: "Kopiraj sve detalje riječi",
      freqLabel: "Učestalost u Kur'anu",
      freqSub: "Ukupan broj pojavljivanja",
      freqMuttashilVal: "Spojeni oblik (Muttashil)",
      freqMuttashilSub: "Kao spojena zamjenica",
      totalAyatLabel: "Ukupno referentnih ajeta",
      totalAyatSub: "Dostupno u bazi podataka",
      sampleAyatSuffix: "Ajeta",
      transliterationPrefix: "Transliteracija:",
      meaningPrefix: "Značenje:",
      
      // References Section
      referencesTitlePrefix: "Kur'anski ajeti za riječ:",
      ayatCountBadgePattern: (cur, total) => `Ajet ${cur} od ${total}`,
      ayatCountZero: "0 Ajeta",
      searchPlaceholder: "Traži po nazivu sure ili broju ajeta...",
      exportCsvBtn: "Izvezi CSV",
      exportCsvTooltip: "Preuzmi sve referentne ajete za ovu riječ u CSV datoteku",
      
      // Ayat Card
      surahPrefix: "Sura",
      surahPositionTag: (cur, surahNo, ayatNo) => `Sura #${surahNo} • Ajet #${ayatNo}`,
      playTranslationBtn: "Prijevod na bosanski",
      stopTranslationBtn: "Zaustavi glas",
      playTilawahBtn: "Učenje Kur'ana",
      pauseTilawahBtn: "Pauziraj učenje",
      askAiBtn: "Pitaj AI",
      askAiTooltip: "Postavite pitanje AI asistentu o gramatici i tefsiru ovog ajeta",
      aiModalTitle: "Kur'anski AI Asistent",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Analiza Sure ${suratNama}:${ayat} • Riječ "${kata}" (${noKata})`,
      aiTopicLabel: "Odaberite temu analize:",
      aiPromptPreviewLabel: "Generisani AI upit (prompt):",
      aiTopicNahwu: "🔍 Nahv (Arapska gramatika i sintaksa) i I'rab",
      aiTopicTafsir: "📖 Tefsir (Tumačenje i kontekst ajeta)",
      aiTopicBalaghah: "✨ Belagat (Retorika i ljepota kur'anskog stila)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Kopiraj Prompt",
      toastPromptCopied: "AI prompt je uspješno kopiran u međuspremnik!",
      ayahPill: (n) => `Ajet ${n}`,
      flipToArabicBtn: "Prikaži arapski tekst",
      flipToTranslationBtn: "Prikaži prijevod",
      translationBoxHeader: "Prijevod na bosanski jezik (Besim Korkut)",
      latinBoxHeader: "Latinična transliteracija",
      copyLatinBtn: "Kopiraj transliteraciju",
      arabicBoxHeader: "النص القرآني • Kompletan arapski tekst ajeta",
      latinBackHeader: "Transliteracija:",
      copyBtn: "Kopiraj",
      prevBtn: "Prethodni",
      nextBtn: "Sljedeći",
      emptyStateText: "Nema pronađenih sura ili ajeta koji odgovaraju vašoj pretrazi.",
      
      // Toasts & Speech
      toastLangChanged: "Jezik je uspješno promijenjen na Bosanski 🇧🇦",
      toastTilawahPaused: "Učenje Kur'ana je pauzirano.",
      toastTilawahPlaying: (s, a) => `Učenje sure ${s}:${a} (Mishary Rashid Alafasy)`,
      toastTilawahEnded: "Učenje je završeno.",
      toastAudioFailed: "Greška pri učitavanju zvuka. Provjerite internet vezu.",
      toastTranslationStopped: "Glasovno čitanje prijevoda je zaustavljeno.",
      toastTtsNotSupported: "Vaš preglednik ne podržava sintezu govora (TTS).",
      toastTranslationNotAvail: "Tekst prijevoda nije dostupan.",
      toastSpeakingMeaning: (suratNama, ayat) => `Čitanje prijevoda sure ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Arapski izgovor: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Čitanje značenja: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Čitanje transliteracije sure ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Arapska riječ "${word}" je kopirana!`,
      toastLatinCopied: "Transliteracija je kopirana!",
      toastSummaryCopied: "Detalji riječi su uspješno kopirani!",
      toastCsvExported: (nk) => `Referentni ajeti za riječ ${nk} su izvezeni u CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_bs || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_bs || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Odnosna zamjenica' : 'Zamjenica';
        return `${prefix} ${cleanWord}, ${latin}znači ${arti}. ${desc ? 'Objašnjenje: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    sq: {
      pageTitle: "Fjalori Jamid Mabny | Referencat Interaktive të Fjalëve dhe Ajeteve Kur'anore",
      brandTitle: "Fjalori <span>Jamid Mabny</span>",
      brandSubtitle: "Fjalor Interaktiv për Format dhe Numrat e Fjalëve Kur'anore",
      themeToggleTitle: "Ndrysho Temën e Errët / të Çelët",
      labelLangSelect: "Gjuha e Përkthimit dhe Zërit:",
      translationSourceHtml: "Përkthimi: <strong>Sherif Ahmeti</strong>",
      optgroupEastAsia: "🌏 Azia Juglindore dhe Lindore",
      optgroupMidEast: "🕌 Lindja e Mesme, Azia Qendrore dhe Kaukazi",
      optgroupSouthAsia: "🪷 Azia Jugore dhe Oqeani Indian",
      optgroupAfrica: "🌍 Afrikë",
      optgroupEurope: "🏛️ Evropa Perëndimore, Veriore, Qendrore dhe Lindore",
      tabBadgeJamid: "7 Forma Fjalësh",
      tabBadgeHarf: "17 Forma Harfesh",
      
      // Control Card
      step1Label: "1. Zgjidhni Formën e Fjalës",
      step1Placeholder: "Zgjidhni Formën e Fjalës",
      step1OptionDhamir: "1. Përemrat (Dhamir - Përemrat vetorë dhe pronorë)",
      step1OptionMawshul: "2. Përemrat lidhorë (Mawshul - Përemrat relativë)",
      step1OptionIstifham: "3. Përemrat pyetës (Istifham - Fjalët pyetëse)",
      step1OptionSyarath: "4. Emrat kushtorë (Syarath - Fjalët kushtore)",
      step1OptionIsyarah: "5. Përemrat dëftorë (Isyarah - Përemrat demonstrativë)",
      step1OptionIsimFiil: "6. Emrat foljorë (Isim Fi'il - Emrat me kuptim foljeje)",
      step1OptionFiilJamid: "7. Foljet e ngurosura (Fi'il Jamid - Foljet e pandryshueshme)",
      step2Label: "2. Zgjidhni Numrin e Fjalës",
      step2Placeholder: "Zgjidhni Numrin e Fjalës",
      welcomeTitle: "Ju lutemi zgjidhni Formën dhe Numrin e Fjalës",
      welcomeSubtitle: "Zgjidhni një formë nga menyja e mësipërme për të parë shkrimin arab, kuptimin, frekuencën në Kur'an dhe ajetet e referencës.",
      
      // Spotlight Card
      wordFormBadge: "Forma e Fjalës",
      wordNoBadgePrefix: "Fjala Nr:",
      arabicVoiceBtn: "Zëri Arabisht",
      arabicVoiceTooltip: "Dëgjo shqiptimin në arabisht (TTS Arabisht)",
      meaningVoiceBtn: "Zëri Përkthimit",
      meaningVoiceTooltip: "Dëgjo kuptimin në gjuhën shqipe (TTS Shqip)",
      copyArabicTooltip: "Kopjo Fjalën në Arabisht",
      copyInfoBtn: "Kopjo Info",
      copyInfoTooltip: "Kopjo të Gjitha Detajet e Fjalës",
      freqLabel: "Frekuenca në Kur'an",
      freqSub: "Numri Total i Paraqitjeve",
      freqMuttashilVal: "Forma e Ngjitur (Muttashil)",
      freqMuttashilSub: "Si Përemër i Ngjitur",
      totalAyatLabel: "Ajetet Totale të Referencës",
      totalAyatSub: "Të Disponueshme në Bazën e të Dhënave",
      sampleAyatSuffix: "Ajete",
      transliterationPrefix: "Transliterimi:",
      meaningPrefix: "Kuptimi:",
      
      // References Section
      referencesTitlePrefix: "Ajetet Kur'anore të Referencës:",
      ayatCountBadgePattern: (cur, total) => `Ajeti ${cur} nga ${total}`,
      ayatCountZero: "0 Ajete",
      searchPlaceholder: "Kërko sipas emrit të sures ose numrit të ajetit...",
      exportCsvBtn: "Eksporto CSV",
      exportCsvTooltip: "Shkarko të gjitha ajetet e referencës për këtë fjalë në skedar CSV",
      
      // Ayat Card
      surahPrefix: "Surja",
      surahPositionTag: (cur, surahNo, ayatNo) => `Surja #${surahNo} • Ajeti #${ayatNo}`,
      playTranslationBtn: "Përkthimi Shqip",
      stopTranslationBtn: "Ndalo Zërin",
      playTilawahBtn: "Leximi Kur'anor",
      pauseTilawahBtn: "Pauzo Leximin",
      askAiBtn: "Pyet AI",
      askAiTooltip: "Bëj një pyetje asistentit AI mbi gramatikën dhe tefserin e këtij ajeti",
      aiModalTitle: "Asistenti AI i Kur'anit",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Analizë: Surja ${suratNama}:${ayat} • Fjala "${kata}" (${noKata})`,
      aiTopicLabel: "Zgjidhni temën e analizës AI:",
      aiPromptPreviewLabel: "Prompti AI i gjeneruar:",
      aiTopicNahwu: "🔍 Nahw (Gramatika & Sintaksa Arabe) dhe I'rab (Lakimi)",
      aiTopicTafsir: "📖 Tefsiri (Komenti dhe Konteksti i Ajetit)",
      aiTopicBalaghah: "✨ Balagah (Retorika dhe Bukuria Kur'anore)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Kopjo Promptin",
      toastPromptCopied: "Prompti AI u kopjua me sukses në clipboard!",
      ayahPill: (n) => `Ajeti ${n}`,
      flipToArabicBtn: "Shiko Tekstin Arabisht",
      flipToTranslationBtn: "Shiko Përkthimin Shqip",
      translationBoxHeader: "Përkthimi në Gjuhën Shqipe (Sherif Ahmeti)",
      latinBoxHeader: "Transliterimi Latin",
      copyLatinBtn: "Kopjo Transliterimin",
      arabicBoxHeader: "النص القرآني • Teksti i Plotë Arabisht",
      latinBackHeader: "Transliterimi:",
      copyBtn: "Kopjo",
      prevBtn: "Paraardhësi",
      nextBtn: "Pasardhësi",
      emptyStateText: "Nuk u gjet asnjë sure ose ajet që përputhet me kërkimin tuaj.",
      
      // Toasts & Speech
      toastLangChanged: "Gjuha u ndryshua me sukses në Shqip 🇦🇱",
      toastTilawahPaused: "Leximi i Kur'anit u pauzua.",
      toastTilawahPlaying: (s, a) => `Po luhet leximi i sures ${s}:${a} (Mishary Rashid Alafasy)`,
      toastTilawahEnded: "Leximi përfundoi.",
      toastAudioFailed: "Gabim në ngarkimin e audios. Ju lutemi kontrolloni lidhjen tuaj.",
      toastTranslationStopped: "Leximi me zë i përkthimit u ndalua.",
      toastTtsNotSupported: "Shfletuesi juaj nuk mbështet sintezën e zërit (TTS).",
      toastTranslationNotAvail: "Teksti i përkthimit nuk është i disponueshëm.",
      toastSpeakingMeaning: (suratNama, ayat) => `Po lexohet përkthimi shqip i sures ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Shqiptimi arabisht: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Po lexohet kuptimi: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Po lexohet transliterimi i sures ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Fjala arabe "${word}" u kopjua!`,
      toastLatinCopied: "Transliterimi u kopjua me sukses!",
      toastSummaryCopied: "Përmbledhja e plotë e fjalës u kopjua!",
      toastCsvExported: (nk) => `Ajetet e referencës për fjalën ${nk} u eksportuan në CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_sq || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_sq || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Përemër lidhor' : 'Përemër';
        return `${prefix} ${cleanWord}, ${latin}do të thotë ${arti}. ${desc ? 'Shpjegim: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    th: {
      pageTitle: "พจนานุกรมญามิดมับนีย์ | คำศัพท์และอายะฮ์อ้างอิงในอัลกุรอาน",
      brandTitle: "พจนานุกรม <span>ญามิด มับนีย์</span>",
      brandSubtitle: "พจนานุกรมคำศัพท์ รูปแบบคำ และหมายเลขคำในอัลกุรอาน",
      themeToggleTitle: "เปลี่ยนโหมดมืด / สว่าง",
      labelLangSelect: "ภาษาคำแปลและเสียงอ่าน:",
      translationSourceHtml: "คำแปล: <strong>สมาคมนักเรียนเก่าอาหรับ (King Fahd Complex)</strong>",
      optgroupEastAsia: "🌏 เอเชียตะวันออกเฉียงใต้และเอเชียตะวันออก",
      optgroupMidEast: "🕌 ตะวันออกกลาง เอเชียกลาง และคอเคซัส",
      optgroupSouthAsia: "🪷 เอเชียใต้และมหาสมุทรอินเดีย",
      optgroupAfrica: "🌍 แอฟริกา",
      optgroupEurope: "🏛️ ยุโรปตะวันตก ยุโรปเหนือ ยุโรปกลาง และยุโรปตะวันออก",
      tabBadgeJamid: "7 รูปแบบคำ",
      tabBadgeHarf: "17 รูปแบบฮัรฟ์",
      
      // Control Card
      step1Label: "1. เลือกรูปแบบคำ (หมวดหมู่)",
      step1Placeholder: "เลือกรูปแบบคำ",
      step1OptionDhamir: "1. คำสรรพนาม (ฎอมี้ร์ / Dhamir)",
      step1OptionMawshul: "2. ประพันธสรรพนาม (เมาศูล / Mawshul)",
      step1OptionIstifham: "3. คำปฤจฉา / คำถาม (อิสติฟฮาม / Istifham)",
      step1OptionSyarath: "4. คำเงื่อนไข (ชัรฏ์ / Syarath)",
      step1OptionIsyarah: "5. นิยมสรรพนาม / ชี้เฉพาะ (อิชารอฮ์ / Isyarah)",
      step1OptionIsimFiil: "6. นามกริยา (อิซมุลฟิอิล / Isim Fi'il)",
      step1OptionFiilJamid: "7. กริยาคงรูป (ฟิอิลญามิด / Fi'il Jamid)",
      step2Label: "2. เลือกหมายเลขคำ",
      step2Placeholder: "เลือกหมายเลขคำ",
      welcomeTitle: "กรุณาเลือกรูปแบบคำและหมายเลขคำ",
      welcomeSubtitle: "เลือกรูปแบบคำจากเมนูด้านบนเพื่อดูข้อความภาษาอาหรับ ความหมาย สถิติความถี่ในอัลกุรอาน และรายการอายะฮ์อ้างอิง",
      
      // Spotlight Card
      wordFormBadge: "รูปแบบคำ",
      wordNoBadgePrefix: "หมายเลขคำ:",
      arabicVoiceBtn: "เสียงภาษาอาหรับ",
      arabicVoiceTooltip: "ฟังการออกเสียงภาษาอาหรับ (TTS อาหรับ)",
      meaningVoiceBtn: "เสียงอ่านคำแปล",
      meaningVoiceTooltip: "ฟังคำแปลและความหมายภาษาไทย (TTS)",
      copyArabicTooltip: "คัดลอกคำภาษาอาหรับ",
      copyInfoBtn: "คัดลอกข้อมูล",
      copyInfoTooltip: "คัดลอกรายละเอียดและไวยากรณ์ทั้งหมด",
      freqLabel: "ความถี่ในอัลกุรอาน",
      freqSub: "จำนวนครั้งที่ปรากฏทั้งหมด",
      freqMuttashilVal: "สรรพนามเชื่อมต่อ (มุตตะศิล)",
      freqMuttashilSub: "ในรูปสรรพนามติดท้ายคำ",
      totalAyatLabel: "จำนวนอายะฮ์อ้างอิง",
      totalAyatSub: "ที่มีในฐานข้อมูล",
      sampleAyatSuffix: "อายะฮ์",
      transliterationPrefix: "คำอ่านทับศัพท์:",
      meaningPrefix: "ความหมาย:",
      
      // References Section
      referencesTitlePrefix: "อายะฮ์กุรอานอ้างอิงสำหรับคำ:",
      ayatCountBadgePattern: (cur, total) => `อายะฮ์ที่ ${cur} จาก ${total}`,
      ayatCountZero: "0 อายะฮ์",
      searchPlaceholder: "ค้นหาด้วยชื่อซูเราะฮ์ หรือหมายเลข หรือข้อความ...",
      exportCsvBtn: "ส่งออก CSV",
      exportCsvTooltip: "ดาวน์โหลดอายะฮ์อ้างอิงทั้งหมดของคำนี้เป็นไฟล์ CSV",
      
      // Ayat Card
      surahPrefix: "ซูเราะฮ์",
      surahPositionTag: (cur, surahNo, ayatNo) => `ซูเราะฮ์ #${surahNo} • อายะฮ์ #${ayatNo}`,
      playTranslationBtn: "เสียงคำแปลภาษาไทย",
      stopTranslationBtn: "หยุดเสียงอ่าน",
      playTilawahBtn: "ฟังการอ่านอัลกุรอาน",
      pauseTilawahBtn: "หยุดชั่วคราว",
      askAiBtn: "ถาม AI อัจฉริยะ",
      askAiTooltip: "ถามผู้ช่วย AI เกี่ยวกับไวยากรณ์ ตัฟซีร และความงดงามของอายะฮ์นี้",
      aiModalTitle: "ผู้ช่วย AI กุรอานอัจฉริยะ",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `การวิเคราะห์ ซูเราะฮ์ ${suratNama}:${ayat} • คำว่า "${kata}" (${noKata})`,
      aiTopicLabel: "เลือกหัวข้อการวิเคราะห์:",
      aiPromptPreviewLabel: "ข้อความคำถาม AI ที่สร้างขึ้น (Prompt):",
      aiTopicNahwu: "🔍 ไวยากรณ์ภาษาอาหรับ (นะฮ์วู/ศ็อรฟ์) และอิอ์รอบ",
      aiTopicTafsir: "📖 ตัฟซีร (คำอธิบายความหมายและบริบทของอายะฮ์)",
      aiTopicBalaghah: "✨ บาลาเฆาะฮ์ (ความงดงามเชิงโวหารและวรรณศิลป์กุรอาน)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "คัดลอก Prompt",
      toastPromptCopied: "คัดลอกคำถาม AI ไปยังคลิปบอร์ดแล้ว!",
      ayahPill: (n) => `อายะฮ์ ${n}`,
      flipToArabicBtn: "แสดงข้อความภาษาอาหรับ",
      flipToTranslationBtn: "แสดงคำแปลภาษาไทย",
      translationBoxHeader: "คำแปลภาษาไทย (สมาคมนักเรียนเก่าอาหรับ / King Fahd Complex)",
      
      // Pagination & Empty State
      emptyStateTitle: "ไม่พบผลลัพธ์ที่ตรงกับการค้นหา",
      emptyStateText: "ไม่พบซูเราะฮ์หรืออายะฮ์ที่ตรงกับคำค้นหาของคุณ",
      btnResetSearch: "ล้างการค้นหา",
      paginationPrev: "ก่อนหน้า",
      paginationNext: "ถัดไป",
      paginationInfo: (cur, total) => `หน้า ${cur} จาก ${total}`,
      
      // Toasts
      toastLangChanged: "เปลี่ยนภาษาเป็น ภาษาไทย (Thai) แล้ว",
      toastThemeChanged: (theme) => `เปลี่ยนเป็นโหมด ${theme === 'dark' ? 'มืด' : 'สว่าง'} แล้ว`,
      toastTilawahPlaying: (suratNama, ayat) => `กำลังเล่นเสียงอ่านซูเราะฮ์ ${suratNama}:${ayat}`,
      toastTilawahPaused: "หยุดเสียงอ่านชั่วคราวแล้ว",
      toastTilawahEnded: "การอ่านอัลกุรอานเสร็จสิ้นแล้ว",
      toastAudioFailed: "เกิดข้อผิดพลาดในการโหลดเสียง กรุณาตรวจสอบการเชื่อมต่ออินเทอร์เน็ต",
      toastTranslationStopped: "หยุดเสียงอ่านคำแปลแล้ว",
      toastTtsNotSupported: "เบราว์เซอร์ของคุณไม่รองรับการแปลงข้อความเป็นเสียงพูด (TTS)",
      toastTranslationNotAvail: "ไม่มีข้อความคำแปลในขณะนี้",
      toastSpeakingMeaning: (suratNama, ayat) => `กำลังอ่านคำแปลซูเราะฮ์ ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `การออกเสียงภาษาอาหรับ: ${word}`,
      toastSpeakingWordMeaning: (arti) => `กำลังอ่านความหมาย: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `กำลังอ่านคำอ่านทับศัพท์ ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `คัดลอกคำภาษาอาหรับ "${word}" แล้ว!`,
      toastLatinCopied: "คัดลอกคำอ่านทับศัพท์แล้ว!",
      toastSummaryCopied: "คัดลอกข้อมูลสรุปของคำศัพท์แล้ว!",
      toastCsvExported: (nk) => `ส่งออกอายะฮ์อ้างอิงสำหรับคำ ${nk} เป็น CSV แล้ว!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_th || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_th || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'ประพันธสรรพนาม' : 'คำสรรพนาม';
        return `${prefix} ${cleanWord}, ${latin}หมายถึง ${arti}. ${desc ? 'คำอธิบาย: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    ber: {
      pageTitle: "Asegzawal n Jamid Mabny | Awalen d Tseddariyin n Leqran",
      brandTitle: "Asegzawal <span>Jamid Mabny</span>",
      brandSubtitle: "Asegzawal amsawal n talɣiwin d wumiḍen n wawalen n Leqran",
      themeToggleTitle: "Beddel asentel tebra / tafat",
      labelLangSelect: "Tutlayt n usuqqel d taɣect:",
      translationSourceHtml: "Tasuqilt: <strong>Ramdane At Mansour (Tamaziɣt)</strong>",
      optgroupEastAsia: "🌏 Asya n Wenẓul-Agmuḍan & Asya n Wegmuḍ",
      optgroupMidEast: "🕌 Agmuḍ Alemmas, Asya Talemmast & Qafqaz",
      optgroupSouthAsia: "🪷 Asya n Wenẓul & Agaraw Ahendi",
      optgroupAfrica: "🌍 Tafriqt",
      optgroupEurope: "🏛️ Turuft n Umalu, n Ugafa, Talemmast & n Wegmuḍ",
      tabBadgeJamid: "7 n Talɣiwin n Wawalen",
      tabBadgeHarf: "17 n Talɣiwin n Isekkilen",
      
      // Control Card
      step1Label: "1. Fren talɣa n wawal (taggayt)",
      step1Placeholder: "Fren talɣa n wawal",
      step1OptionDhamir: "1. Imqimen (Dhamir - Iglamen)",
      step1OptionMawshul: "2. Imqimen Imassaɣen (Mawshul)",
      step1OptionIstifham: "3. Isteqsiyen (Istifham - Tisura n Usteqsi)",
      step1OptionSyarath: "4. Tseddariyin n Tawtilt (Syarath)",
      step1OptionIsyarah: "5. Imqimen n Usmmal (Isyarah)",
      step1OptionIsimFiil: "6. Ismawen n Tigawt (Isim Fi'il)",
      step1OptionFiilJamid: "7. Imyagen Ikiwanen (Fi'il Jamid)",
      step2Label: "2. Fren uṭṭun n wawal",
      step2Placeholder: "Fren uṭṭun n wawal",
      welcomeTitle: "Ttxil-k fren talɣa d wuṭṭun n wawal",
      welcomeSubtitle: "Fren talɣa n wawal seg tzelɣa n ufella iwakken ad twaliḍ aḍris aɛrab, anamek, tasnakta deg Leqran d tseddariyin n tsiwel.",
      
      // Spotlight Card
      wordFormBadge: "Talɣa n wawal",
      wordNoBadgePrefix: "Uṭṭun n wawal:",
      arabicVoiceBtn: "Taɣect Taɛrabt",
      arabicVoiceTooltip: "Sel i ususru n taɛrabt (TTS)",
      meaningVoiceBtn: "Taɣect n unamek",
      meaningVoiceTooltip: "Sel i unamek s tmaziɣt (TTS)",
      copyArabicTooltip: "Nɣel awal aɛrab",
      copyInfoBtn: "Nɣel talɣut",
      copyInfoTooltip: "Nɣel akk talɣut n wawal",
      freqLabel: "Tikwal n useqdec deg Leqran",
      freqSub: "Asemday n tikkal deg Leqran",
      freqMuttashilVal: "Talɣa tuddist (Muttashil)",
      freqMuttashilSub: "D amqim uddis",
      totalAyatLabel: "Asemday n tseddariyin",
      totalAyatSub: "Deg tebdart n yisefka",
      sampleAyatSuffix: "Tiseddariyin",
      transliterationPrefix: "Asusru:",
      meaningPrefix: "Anamek:",
      
      // References Section
      referencesTitlePrefix: "Tiseddariyin n Leqran i wawal:",
      ayatCountBadgePattern: (cur, total) => `Taseddarin ${cur} seg ${total}`,
      ayatCountZero: "0 Tseddariyin",
      searchPlaceholder: "Nadi s yisem n tsurat neɣ uṭṭun n tseddart...",
      exportCsvBtn: "Sifeḍ CSV",
      exportCsvTooltip: "Sider akk tiseddariyin n wawal-agi deg ufaylu CSV",
      
      // Ayat Card
      surahPrefix: "Tasuret",
      surahPositionTag: (cur, surahNo, ayatNo) => `Tasuret #${surahNo} • Taseddart #${ayatNo}`,
      playTranslationBtn: "Tasuqilt s tmaziɣt",
      stopTranslationBtn: "Sbedd taɣect",
      playTilawahBtn: "Tiɣri n Leqran",
      pauseTilawahBtn: "Sbedd cwiṭ",
      askAiBtn: "Seqsi AI",
      askAiTooltip: "Seqsi amallal n AI ɣef tjerrumt d usegzi n tseddart-agi",
      aiModalTitle: "Amallal n AI n Leqran",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Asleḍ n Tsurat ${suratNama}:${ayat} • Awal "${kata}" (${noKata})`,
      aiTopicLabel: "Fren asentel n usleḍ:",
      aiPromptPreviewLabel: "Asuter n AI (Prompt):",
      aiTopicNahwu: "🔍 Tajerrumt Taɛrabt (Naḥw/Ṣarf) d I'rab",
      aiTopicTafsir: "📖 Adegzi d Tmentilt (Tafsir)",
      aiTopicBalaghah: "✨ Tasekla d Lmeɛna n Leqran (Balaɣah)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Nɣel Prompt",
      toastPromptCopied: "Asuter n AI yenɣel s lferḥ!",
      ayahPill: (n) => `Taseddart ${n}`,
      flipToArabicBtn: "Sken aḍris aɛrab",
      flipToTranslationBtn: "Sken tasuqilt",
      translationBoxHeader: "Tasuqilt n Tamaziɣt (Ramdane At Mansour)",
      
      // Pagination & Empty State
      emptyStateTitle: "Ulac igmad n unadi",
      emptyStateText: "Ulac tisura neɣ tiseddariyin i yettemcabin ɣer wayen tebɣiḍ.",
      btnResetSearch: "Ales anadi",
      paginationPrev: "Uzwir",
      paginationNext: "Amḍafir",
      paginationInfo: (cur, total) => `Asebter ${cur} seg ${total}`,
      
      // Toasts
      toastLangChanged: "Tutlayt tbeddel ɣer Tamaziɣt (Amazigh)",
      toastThemeChanged: (theme) => `Asentel ibeddel ɣer ${theme === 'dark' ? 'Tebra' : 'Tafat'}`,
      toastTilawahPlaying: (suratNama, ayat) => `Tiɣri n Tsurat ${suratNama}:${ayat}`,
      toastTilawahPaused: "Tiɣri tebded cwiṭ.",
      toastTilawahEnded: "Tiɣri tekfa.",
      toastAudioFailed: "Tuccḍa deg uselkem n taɣect.",
      toastTranslationStopped: "Taɣect n tsuqilt tebded.",
      toastTtsNotSupported: "Iminig-ik ur yeqbil ara asusru n taɣect (TTS).",
      toastTranslationNotAvail: "Aḍris n tsuqilt ulac-it.",
      toastSpeakingMeaning: (suratNama, ayat) => `Asusru n tsuqilt ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Asusru aɛrab: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Anamek: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Asusru n tseddart ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Awal aɛrab "${word}" yenɣel!`,
      toastLatinCopied: "Asusru yenɣel!",
      toastSummaryCopied: "Agzul n wawal yenɣel s lferḥ!",
      toastCsvExported: (nk) => `Tiseddariyin n wawal ${nk} sfḍent ɣer CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ber || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ber || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Amqim amassaɣ' : 'Amqim';
        return `${prefix} ${cleanWord}, ${latin}anamek-is ${arti}. ${desc ? 'Asegzi: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    am: {
      pageTitle: "የጃሚድ መብኒይ መዝገበ-ቃላት | የቁርኣን ቃላትና የአንቀጾች ማጣቀሻ",
      brandTitle: "መዝገበ-ቃላት <span>ጃሚድ መብኒይ</span>",
      brandSubtitle: "በይነ-ተግባራዊ የቁርኣን ቃላት አወቃቀርና የቁጥር መመሪያ",
      themeToggleTitle: "የጨለማ / የብርሃን ሁነታ መቀየሪያ",
      labelLangSelect: "የትርጉምና የድምፅ ቋንቋ:",
      translationSourceHtml: "ትርጉም: <strong>ሳዲቅ እና ሳኒ ሐቢብ (አማርኛ)</strong>",
      optgroupEastAsia: "🌏 ደቡብ ምሥራቅ እና ምሥራቅ እስያ",
      optgroupMidEast: "🕌 መካከለኛው ምሥራቅ፣ መካከለኛው እስያ እና ካውካሰስ",
      optgroupSouthAsia: "🪷 ደቡብ እስያ እና ህንድ ውቅያኖስ",
      optgroupAfrica: "🌍 አፍሪካ",
      optgroupEurope: "🏛️ ምዕራብ፣ ሰሜን፣ መካከለኛ እና ምሥራቅ አውሮፓ",
      tabBadgeJamid: "7 የቃል ቅርጾች",
      tabBadgeHarf: "17 የሐርፍ ዓይነቶች",
      
      // Control Card
      step1Label: "1. የቃሉን አወቃቀር (ምድብ) ይምረጡ",
      step1Placeholder: "የቃሉን አወቃቀር ይምረጡ",
      step1OptionDhamir: "1. ተውላጠ ስሞች (ዳሚር / Dhamir)",
      step1OptionMawshul: "2. አዛማጅ ተውላጠ ስሞች (መውሱል / Mawshul)",
      step1OptionIstifham: "3. መጠይቅ ቃላት (ኢስቲፍሃም / Istifham)",
      step1OptionSyarath: "4. ቅድመ-ሁኔታ አመልካች ቃላት (ሻራት / Syarath)",
      step1OptionIsyarah: "5. አመላካች ተውላጠ ስሞች (ኢሻራህ / Isyarah)",
      step1OptionIsimFiil: "6. ግሳዊ ስሞች (ኢስሙል ፊዕል / Isim Fi'il)",
      step1OptionFiilJamid: "7. የማይዘረዘሩ ግሦች (ፊዕል ጃሚድ / Fi'il Jamid)",
      step2Label: "2. የቃሉን ቁጥር ይምረጡ",
      step2Placeholder: "የቃሉን ቁጥር ይምረጡ",
      welcomeTitle: "እባክዎ የቃሉን አወቃቀርና ቁጥር ይምረጡ",
      welcomeSubtitle: "የአረብኛ ጽሑፉን፣ ትርጉሙን፣ በቁርኣን ውስጥ የመጣበትን ድግግሞሽና የማጣቀሻ አንቀጾችን ዝርዝር ለማየት ከላይ ካለው ሜኑ የቃሉን አወቃቀር ይምረጡ።",
      
      // Spotlight Card
      wordFormBadge: "የቃል አወቃቀር",
      wordNoBadgePrefix: "የቃል ቁጥር:",
      arabicVoiceBtn: "የአረብኛ ድምፅ",
      arabicVoiceTooltip: "የአረብኛ አነባበብን ያዳምጡ (TTS)",
      meaningVoiceBtn: "የትርጉም ድምፅ",
      meaningVoiceTooltip: "የአማርኛ ትርጉሙን ያዳምጡ (TTS)",
      copyArabicTooltip: "የአረብኛውን ቃል ቅዳ",
      copyInfoBtn: "መረጃ ቅዳ",
      copyInfoTooltip: "ሙሉ የቃሉን መረጃና ሰዋሰው ቅዳ",
      freqLabel: "በቁርኣን ውስጥ የመጣበት ድግግሞሽ",
      freqSub: "አጠቃላይ የመጣበት ብዛት",
      freqMuttashilVal: "ተያያዥ ተውላጠ ስም (ሙተሲል)",
      freqMuttashilSub: "ከቃል ጋር በተያያዘ ቅርጽ",
      totalAyatLabel: "ጠቅላላ ማጣቀሻ አንቀጾች",
      totalAyatSub: "በመረጃ ቋት ውስጥ የሚገኝ",
      sampleAyatSuffix: "አንቀጾች",
      transliterationPrefix: "የድምፅ አነባበብ:",
      meaningPrefix: "ትርጉም:",
      
      // References Section
      referencesTitlePrefix: "ለቃሉ የተጠቀሱ የቁርኣን አንቀጾች:",
      ayatCountBadgePattern: (cur, total) => `አንቀጽ ${cur} ከ ${total}`,
      ayatCountZero: "0 አንቀጾች",
      searchPlaceholder: "በሱራ ስም ወይም በአንቀጽ ቁጥር ይፈልጉ...",
      exportCsvBtn: "ወደ CSV ላክ",
      exportCsvTooltip: "ሁሉንም ማጣቀሻ አንቀጾች በCSV ፋይል አውርድ",
      
      // Ayat Card
      surahPrefix: "ሱራ",
      surahPositionTag: (cur, surahNo, ayatNo) => `ሱራ #${surahNo} • አንቀጽ #${ayatNo}`,
      playTranslationBtn: "የአማርኛ ትርጉም ድምፅ",
      stopTranslationBtn: "ድምፅ አቁም",
      playTilawahBtn: "የቁርኣን ንባብ",
      pauseTilawahBtn: "ለጊዜው አቁም",
      askAiBtn: "AI ጠይቅ",
      askAiTooltip: "ስለ አንቀጹ ሰዋሰው፣ ተፍሲርና ውበት የAI ረዳትን ይጠይቁ",
      aiModalTitle: "የቁርኣን AI ረዳት",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `የሱራ ${suratNama}:${ayat} ትንተና • ቃል "${kata}" (${noKata})`,
      aiTopicLabel: "የትከረከረበትን የትንተና መስክ ይምረጡ:",
      aiPromptPreviewLabel: "የተፈጠረው የAI ጥያቄ (Prompt):",
      aiTopicNahwu: "🔍 የአረብኛ ሰዋሰው (ነሕው/ሶርፍ) እና ኢዕራብ",
      aiTopicTafsir: "📖 ተፍሲር (የአንቀጹ ማብራሪያና አስተምህሮ)",
      aiTopicBalaghah: "✨ በላጋህ (የቁርኣን አንደበተ-ርቱዕነትና ውበት)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "ጥያቄውን ቅዳ",
      toastPromptCopied: "የAI ጥያቄው ወደ ቅንጥብ ሰሌዳ ተቀድቷል!",
      ayahPill: (n) => `አንቀጽ ${n}`,
      flipToArabicBtn: "የአረብኛ ጽሑፍ አሳይ",
      flipToTranslationBtn: "የአማርኛ ትርጉም አሳይ",
      translationBoxHeader: "የአማርኛ ትርጉም (ሳዲቅ እና ሳኒ ሐቢብ)",
      
      // Pagination & Empty State
      emptyStateTitle: "ምንም የሚዛመድ ውጤት አልተገኘም",
      emptyStateText: "ከፍለጋዎ ጋር የሚዛመድ ሱራ ወይም አንቀጽ የለም።",
      btnResetSearch: "ፍለጋን ዳግም አስጀምር",
      paginationPrev: "ቀዳሚ",
      paginationNext: "ቀጣይ",
      paginationInfo: (cur, total) => `ገጽ ${cur} ከ ${total}`,
      
      // Toasts
      toastLangChanged: "ቋንቋ ወደ አማርኛ (Amharic) ተቀይሯል",
      toastThemeChanged: (theme) => `ገጽታ ወደ ${theme === 'dark' ? 'ጨለማ' : 'ብርሃን'} ተቀይሯል`,
      toastTilawahPlaying: (suratNama, ayat) => `የሱራ ${suratNama}:${ayat} ንባብ እየተጫወተ ነው`,
      toastTilawahPaused: "ንባቡ ለጊዜው ቆሟል።",
      toastTilawahEnded: "የቁርኣን ንባቡ ተጠናቋል።",
      toastAudioFailed: "ድምፅ በመጫን ላይ ስህተት ተፈጥሯል፤ እባክዎ ኢንተርኔትዎን ያረጋግጡ።",
      toastTranslationStopped: "የትርጉም ድምፅ ንባቡ ቆሟል።",
      toastTtsNotSupported: "የእርስዎ አሳሽ የጽሑፍ-ወደ-ድምፅ (TTS) አገልግሎትን አይደግፍም።",
      toastTranslationNotAvail: "የትርጉም ጽሑፍ በአሁኑ ጊዜ አይገኝም።",
      toastSpeakingMeaning: (suratNama, ayat) => `የሱራ ${suratNama}:${ayat} ትርጉም እየተነበበ ነው`,
      toastSpeakingArabic: (word) => `የአረብኛ አነባበብ: ${word}`,
      toastSpeakingWordMeaning: (arti) => `ትርጉም: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `የአንቀጽ ${suratNama}:${ayat} ድምፅ አነባበብ`,
      toastArabicCopied: (word) => `የአረብኛው ቃል "${word}" ተቀድቷል!`,
      toastLatinCopied: "የድምፅ አነባበቡ ተቀድቷል!",
      toastSummaryCopied: "ሙሉ የቃሉ መረጃ ተቀድቷል!",
      toastCsvExported: (nk) => `ለቃል ${nk} የተጠቀሱ አንቀጾች ወደ CSV ተልከዋል!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_am || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_am || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'አዛማጅ ተውላጠ ስም' : 'ተውላጠ ስም';
        return `${prefix} ${cleanWord}, ${latin}ትርጉሙ ${arti} ማለት ነው። ${desc ? 'ማብራሪያ: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    az: {
      pageTitle: "Camid Məbni Lüğəti | İnteraktiv Quran Sözləri və Ayə İstinadları",
      brandTitle: "Lüğət <span>Camid Məbni</span>",
      brandSubtitle: "Quran söz formaları və söz nömrələri üçün interaktiv lüğət",
      themeToggleTitle: "Qaranlıq / İşıqlı mövzuya keçid",
      labelLangSelect: "Tərcümə və səs dili:",
      translationSourceHtml: "Tərcümə: <strong>Vasim Məmmədəliyev & Ziya Bünyadov</strong>",
      optgroupEastAsia: "🌏 Cənub-Şərqi və Şərqi Asiya",
      optgroupMidEast: "🕌 Yaxın Şərq, Mərkəzi Asiya və Qafqaz",
      optgroupSouthAsia: "🪷 Cənubi Asiya və Hind Okeanı",
      optgroupAfrica: "🌍 Afrika",
      optgroupEurope: "🏛️ Qərbi, Şimali, Mərkəzi və Şərqi Avropa",
      tabBadgeJamid: "7 Söz Forması",
      tabBadgeHarf: "17 Hərf Forması",
      
      // Control Card
      step1Label: "1. Söz formasını (kateqoriyanı) seçin",
      step1Placeholder: "Söz formasını seçin",
      step1OptionDhamir: "1. Əvəzliklər (Zəmir / Dhamir)",
      step1OptionMawshul: "2. Nisbi Əvəzliklər (İsmi Mövsul / Mawshul)",
      step1OptionIstifham: "3. Sual Əvəzlikləri (İsmi İstifham)",
      step1OptionSyarath: "4. Şərt Əvəzlikləri (İsmi Şərt)",
      step1OptionIsyarah: "5. İşarə Əvəzlikləri (İsmi İşarə)",
      step1OptionIsimFiil: "6. Feili İsimlər (İsmi Feil / Isim Fi'il)",
      step1OptionFiilJamid: "7. Təsriflənməyən Feillər (Feili Camid / Fi'il Jamid)",
      step2Label: "2. Söz nömrəsini seçin",
      step2Placeholder: "Söz nömrəsini seçin",
      welcomeTitle: "Zəhmət olmasa söz forması və nömrəsini seçin",
      welcomeSubtitle: "Ərəb mətni, tərcüməsi, Quranda təkrarlanma sayı və ayə istinadlarını görmək üçün yuxarıdakı menyudan söz formasını seçin.",
      
      // Spotlight Card
      wordFormBadge: "Söz Forması",
      wordNoBadgePrefix: "Söz №:",
      arabicVoiceBtn: "Ərəbcə Səs",
      arabicVoiceTooltip: "Ərəbcə tələffüzü dinləyin (TTS)",
      meaningVoiceBtn: "Məna Səsi",
      meaningVoiceTooltip: "Azərbaycanca mənanı dinləyin (TTS)",
      copyArabicTooltip: "Ərəb sözünü kopyalayın",
      copyInfoBtn: "Məlumatı kopyala",
      copyInfoTooltip: "Bütün söz məlumatlarını kopyalayın",
      freqLabel: "Qurani-Kərimdə tezliyi",
      freqSub: "Ümumi qeyd olunma sayı",
      freqMuttashilVal: "Bitişik forma (Müttəsil)",
      freqMuttashilSub: "Bitişik əvəzlik kimi",
      totalAyatLabel: "Cəmi istinad ayələri",
      totalAyatSub: "Məlumat bazasında mövcuddur",
      sampleAyatSuffix: "Nümunə Ayə",
      transliterationPrefix: "Transliterasiya:",
      meaningPrefix: "Məna:",
      
      // References Section
      referencesTitlePrefix: "Söz üçün Quran ayələri:",
      ayatCountBadgePattern: (cur, total) => `Ayə ${cur} / ${total}`,
      ayatCountZero: "0 Ayə",
      searchPlaceholder: "Surə adı və ya ayə nömrəsi ilə axtarın...",
      exportCsvBtn: "CSV İxrac et",
      exportCsvTooltip: "Bu sözün bütün istinad ayələrini CSV faylına endirin",
      
      // Ayat Card
      surahPrefix: "Surə",
      surahPositionTag: (cur, surahNo, ayatNo) => `Surə #${surahNo} • Ayə #${ayatNo}`,
      playTranslationBtn: "Tərcüməni dinlə",
      stopTranslationBtn: "Səsi dayandır",
      playTilawahBtn: "Tilavəti dinlə",
      pauseTilawahBtn: "Fasilə ver",
      askAiBtn: "AI-dan soruş",
      askAiTooltip: "Bu ayənin qrammatikası və təfsiri haqqında AI köməkçisindən soruşun",
      aiModalTitle: "Quran AI Köməkçisi",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Surə ${suratNama}:${ayat} Təhlili • Söz "${kata}" (${noKata})`,
      aiTopicLabel: "AI təhlil mövzusunu seçin:",
      aiPromptPreviewLabel: "Hazırlanmış AI Sorğusu (Prompt):",
      aiTopicNahwu: "🔍 Ərəb Qrammatikası (Nəhv/Sərf) və İrab",
      aiTopicTafsir: "📖 Təfsir və Ayənin Mənası",
      aiTopicBalaghah: "✨ Quran Bəlağəti və Ədəbi İncəlikləri",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Sorğunu Kopyala",
      toastPromptCopied: "AI sorğusu mübadilə buferinə kopyalandı!",
      ayahPill: (n) => `Ayə ${n}`,
      flipToArabicBtn: "Ərəb mətnini göstər",
      flipToTranslationBtn: "Tərcüməni göstər",
      translationBoxHeader: "Azərbaycan Tərcüməsi (V. Məmmədəliyev & Z. Bünyadov)",
      
      // Pagination & Empty State
      emptyStateTitle: "Nəticə tapılmadı",
      emptyStateText: "Axtarışınıza uyğun surə və ya ayə tapılmadı.",
      btnResetSearch: "Axtarışı sıfırla",
      paginationPrev: "Əvvəlki",
      paginationNext: "Növbəti",
      paginationInfo: (cur, total) => `Səhifə ${cur} / ${total}`,
      
      // Toasts
      toastLangChanged: "Dil Azərbaycan dilinə dəyişdirildi 🇦🇿",
      toastThemeChanged: (theme) => `Mövzu ${theme === 'dark' ? 'Qaranlıq' : 'İşıqlı'} olaraq dəyişdirildi`,
      toastTilawahPlaying: (suratNama, ayat) => `Surə ${suratNama}:${ayat} tilavəti səsləndirilir`,
      toastTilawahPaused: "Tilavət dayandırıldı.",
      toastTilawahEnded: "Tilavət başa çatdı.",
      toastAudioFailed: "Audio səsləndirmədə xəta baş verdi.",
      toastTranslationStopped: "Tərcümə səsi dayandırıldı.",
      toastTtsNotSupported: "Brauzeriniz nitq sintezini (TTS) dəstəkləmir.",
      toastTranslationNotAvail: "Tərcümə mətni mövcud deyil.",
      toastSpeakingMeaning: (suratNama, ayat) => `Surə ${suratNama}:${ayat} tərcüməsi oxunur`,
      toastSpeakingArabic: (word) => `Ərəbcə tələffüz: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Məna oxunur: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Ayə ${suratNama}:${ayat} oxunur`,
      toastArabicCopied: (word) => `Ərəb sözü "${word}" kopyalandı!`,
      toastLatinCopied: "Transliterasiya kopyalandı!",
      toastSummaryCopied: "Söz haqqında tam məlumat kopyalandı!",
      toastCsvExported: (nk) => `Söz ${nk} üçün istinadlar CSV-yə ixrac olundu!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_az || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_az || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Nisbi əvəzlik' : 'Əvəzlik';
        return `${prefix} ${cleanWord}, ${latin}mənası: ${arti}. ${desc ? 'İzah: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    bg: {
      pageTitle: "Речник Джамид Мабни | Интерактивни Корански Думи и Препратки към Знамения",
      brandTitle: "Речник <span>Джамид Мабни</span>",
      brandSubtitle: "Интерактивен речник за неизменяеми думи и местоимения в Корана",
      themeToggleTitle: "Превключване на тъмна / светла тема",
      labelLangSelect: "Език на превода и гласа:",
      translationSourceHtml: "Превод: <strong>Цветан Теофанов (Български)</strong>",
      optgroupEastAsia: "🌏 Югоизточна и Източна Азия",
      optgroupMidEast: "🕌 Близък изток, Централна Азия и Кавказ",
      optgroupSouthAsia: "🪷 Южна Азия и Индийски океан",
      optgroupAfrica: "🌍 Африка",
      optgroupEurope: "🏛️ Западна, Северна, Централна и Източна Европа",
      tabBadgeJamid: "7 форми на думи",
      tabBadgeHarf: "17 форми на частици",
      
      // Control Card
      step1Label: "1. Изберете форма на думата (категория)",
      step1Placeholder: "Изберете форма на думата",
      step1OptionDhamir: "1. Местоимения (Дамир / Dhamir)",
      step1OptionMawshul: "2. Относителни местоимения (Маусул / Mawshul)",
      step1OptionIstifham: "3. Въпросителни думи (Истифхам / Istifham)",
      step1OptionSyarath: "4. Условни думи (Шарат / Syarath)",
      step1OptionIsyarah: "5. Показателни местоимения (Ишара / Isyarah)",
      step1OptionIsimFiil: "6. Глаголни имена (Исм ал-фи'л / Isim Fi'il)",
      step1OptionFiilJamid: "7. Неизменяеми глаголи (Фи'л Джамид / Fi'il Jamid)",
      step2Label: "2. Изберете номер на думата",
      step2Placeholder: "Изберете номер на думата",
      welcomeTitle: "Моля, изберете форма и номер на думата",
      welcomeSubtitle: "Изберете форма на думата от горното меню, за да видите арабския текст, българския превод, честотата в Корана и препратките към знаменията.",
      
      // Spotlight Card
      wordFormBadge: "Форма на думата",
      wordNoBadgePrefix: "Дума №:",
      arabicVoiceBtn: "Арабски глас",
      arabicVoiceTooltip: "Чуйте арабското произношение (TTS)",
      meaningVoiceBtn: "Глас на превода",
      meaningVoiceTooltip: "Чуйте българския превод (TTS)",
      copyArabicTooltip: "Копирайте арабската дума",
      copyInfoBtn: "Копирай инфо",
      copyInfoTooltip: "Копирайте пълната граматическа информация",
      freqLabel: "Честота в Свещения Коран",
      freqSub: "Общ брой споменавания",
      freqMuttashilVal: "Слята форма (Муттасил)",
      freqMuttashilSub: "Като слято местоимение",
      totalAyatLabel: "Общо референтни знамения",
      totalAyatSub: "Налични в базата данни",
      sampleAyatSuffix: "Примерни Знамения",
      transliterationPrefix: "Транслитерация:",
      meaningPrefix: "Значение:",
      
      // References Section
      referencesTitlePrefix: "Корански знамения за думата:",
      ayatCountBadgePattern: (cur, total) => `Знамение ${cur} от ${total}`,
      ayatCountZero: "0 Знамения",
      searchPlaceholder: "Търсене по име на сура или номер на знамение...",
      exportCsvBtn: "Експорт в CSV",
      exportCsvTooltip: "Изтеглете всички референтни знамения в CSV файл",
      
      // Ayat Card
      surahPrefix: "Сура",
      surahPositionTag: (cur, surahNo, ayatNo) => `Сура #${surahNo} • Знамение #${ayatNo}`,
      playTranslationBtn: "Чуй превода",
      stopTranslationBtn: "Спри гласа",
      playTilawahBtn: "Чуй рецитацията",
      pauseTilawahBtn: "Пауза",
      askAiBtn: "Питай AI",
      askAiTooltip: "Попитайте AI асистента за граматиката и тълкуванието на знамението",
      aiModalTitle: "Корански AI Асистент",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Анализ на Сура ${suratNama}:${ayat} • Дума "${kata}" (${noKata})`,
      aiTopicLabel: "Изберете тема за анализ:",
      aiPromptPreviewLabel: "Генерирано запитване (Prompt):",
      aiTopicNahwu: "🔍 Арабска Граматика (Наху/Сарф) и И'раб",
      aiTopicTafsir: "📖 Тафсир (Тълкувание и поуки)",
      aiTopicBalaghah: "✨ Балага (Коранско красноречие и естетика)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Копирай Запитването",
      toastPromptCopied: "Запитването към AI бе копирано успешно!",
      ayahPill: (n) => `Знамение ${n}`,
      flipToArabicBtn: "Покажи арабския текст",
      flipToTranslationBtn: "Покажи превода",
      translationBoxHeader: "Български Превод (Проф. Цветан Теофанов)",
      
      // Pagination & Empty State
      emptyStateTitle: "Няма намерени резултати",
      emptyStateText: "Няма намерени сури или знамения по вашите критерии.",
      btnResetSearch: "Нулирай търсенето",
      paginationPrev: "Предишна",
      paginationNext: "Следваща",
      paginationInfo: (cur, total) => `Страница ${cur} от ${total}`,
      
      // Toasts
      toastLangChanged: "Езикът бе променен на Български 🇧🇬",
      toastThemeChanged: (theme) => `Темата бе променена на ${theme === 'dark' ? 'Тъмна' : 'Светла'}`,
      toastTilawahPlaying: (suratNama, ayat) => `Рецитация на Сура ${suratNama}:${ayat} (Мишари Алафаси)`,
      toastTilawahPaused: "Рецитацията е на пауза.",
      toastTilawahEnded: "Рецитацията приключи.",
      toastAudioFailed: "Грешка при зареждане на аудиото.",
      toastTranslationStopped: "Аудио преводът бе спрян.",
      toastTtsNotSupported: "Вашият браузър не поддържа гласов синтез (TTS).",
      toastTranslationNotAvail: "Текстът на превода не е наличен.",
      toastSpeakingMeaning: (suratNama, ayat) => `Четене на превода на Сура ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Арабско произношение: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Четене на значението: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Четене на знамение ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Арабската дума "${word}" бе копирана!`,
      toastLatinCopied: "Транслитерацията бе копирана!",
      toastSummaryCopied: "Пълната информация бе копирана!",
      toastCsvExported: (nk) => `Знаменията за дума ${nk} бяха експортирани в CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_bg || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_bg || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Относително местоимение' : 'Местоимение';
        return `${prefix} ${cleanWord}, ${latin}означава: ${arti}. ${desc ? 'Обяснение: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    cs: {
      pageTitle: "Slovník Džámid Mabní | Interaktivní Koránská Slova a Odkazy na Verše",
      brandTitle: "Slovník <span>Džámid Mabní</span>",
      brandSubtitle: "Interaktivní slovník pro neohebná slova a zájmena v Koránu",
      themeToggleTitle: "Přepnout tmavý / světlý motiv",
      labelLangSelect: "Jazyk překladu a hlasu:",
      translationSourceHtml: "Překlad: <strong>Alois Richard Hrbek (Čeština)</strong>",
      optgroupEastAsia: "🌏 Jihovýchodní a východní Asie",
      optgroupMidEast: "🕌 Blízký východ, Střední Asie a Kavkaz",
      optgroupSouthAsia: "🪷 Jižní Asie a Indický oceán",
      optgroupAfrica: "🌍 Afrika",
      optgroupEurope: "🏛️ Západní, Severní, Střední a Východní Evropa",
      tabBadgeJamid: "7 tvarů slov",
      tabBadgeHarf: "17 tvarů částic",
      
      // Control Card
      step1Label: "1. Vyberte formu slova (kategorii)",
      step1Placeholder: "Vyberte formu slova",
      step1OptionDhamir: "1. Zájmena (Dhamír / Pronouns)",
      step1OptionMawshul: "2. Vztažná zájmena (Ism Mawshúl)",
      step1OptionIstifham: "3. Tázací zájmena (Ism Istifhám)",
      step1OptionSyarath: "4. Podmínková slova (Ism Šarath)",
      step1OptionIsyarah: "5. Ukazovací zájmena (Ism Išárah)",
      step1OptionIsimFiil: "6. Slovesná podstatná jména (Ism Fi'il)",
      step1OptionFiilJamid: "7. Neohebná slovesa (Fi'il Džámid)",
      step2Label: "2. Vyberte číslo slova",
      step2Placeholder: "Vyberte číslo slova",
      welcomeTitle: "Vyberte prosím formu a číslo slova",
      welcomeSubtitle: "Vyberte formu slova z nabídky výše a prohlédněte si arabský zápis, český překlad, četnost v Koránu a odkazy na verše.",
      
      // Spotlight Card
      wordFormBadge: "Forma slova",
      wordNoBadgePrefix: "Slovo č.:",
      arabicVoiceBtn: "Arabský hlas",
      arabicVoiceTooltip: "Poslechnout arabskou výslovnost (TTS)",
      meaningVoiceBtn: "Hlas překladu",
      meaningVoiceTooltip: "Poslechnout český význam (TTS)",
      copyArabicTooltip: "Kopírovat arabské slovo",
      copyInfoBtn: "Kopírovat info",
      copyInfoTooltip: "Kopírovat veškeré gramatické informace",
      freqLabel: "Četnost v Koránu",
      freqSub: "Celkový počet výskytů",
      freqMuttashilVal: "Připojená forma (Muttasil)",
      freqMuttashilSub: "Jako připojené zájmeno",
      totalAyatLabel: "Celkem referenčních veršů",
      totalAyatSub: "V databázi k dispozici",
      sampleAyatSuffix: "Příkladové verše",
      transliterationPrefix: "Transliterace:",
      meaningPrefix: "Význam:",
      
      // References Section
      referencesTitlePrefix: "Koránské verše pro slovo:",
      ayatCountBadgePattern: (cur, total) => `Verš ${cur} z ${total}`,
      ayatCountZero: "0 Veršů",
      searchPlaceholder: "Hledat podle názvu súry nebo čísla verše...",
      exportCsvBtn: "Exportovat do CSV",
      exportCsvTooltip: "Stáhnout všechny referenční verše do souboru CSV",
      
      // Ayat Card
      surahPrefix: "Súra",
      surahPositionTag: (cur, surahNo, ayatNo) => `Súra #${surahNo} • Verš #${ayatNo}`,
      playTranslationBtn: "Přehrát překlad",
      stopTranslationBtn: "Zastavit hlas",
      playTilawahBtn: "Přehrát recitaci",
      pauseTilawahBtn: "Pozastavit",
      askAiBtn: "Zeptat se AI",
      askAiTooltip: "Zeptat se AI asistenta na gramatiku a tafsír tohoto verše",
      aiModalTitle: "Koránský AI Asistent",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Analýza Súry ${suratNama}:${ayat} • Slovo "${kata}" (${noKata})`,
      aiTopicLabel: "Vyberte téma analýzy:",
      aiPromptPreviewLabel: "Vygenerovaný AI dotaz (Prompt):",
      aiTopicNahwu: "🔍 Arabská gramatika (Nahw/Sarf) a I'ráb",
      aiTopicTafsir: "📖 Tafsír (Výklad a poučení verše)",
      aiTopicBalaghah: "✨ Balágha (Rétorická krása a poetika Koránu)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Kopírovat Dotaz",
      toastPromptCopied: "AI dotaz byl zkopírován do schránky!",
      ayahPill: (n) => `Verš ${n}`,
      flipToArabicBtn: "Zobrazit arabský text",
      flipToTranslationBtn: "Zobrazit překlad",
      translationBoxHeader: "Český překlad (Alois Richard Hrbek)",
      
      // Pagination & Empty State
      emptyStateTitle: "Nebyly nalezeny žádné výsledky",
      emptyStateText: "Podle zadaných kritérií nebyla nalezena žádná súra ani verš.",
      btnResetSearch: "Obnovit hledání",
      paginationPrev: "Předchozí",
      paginationNext: "Další",
      paginationInfo: (cur, total) => `Strana ${cur} z ${total}`,
      
      // Toasts
      toastLangChanged: "Jazyk byl změněn na Češtinu 🇨🇿",
      toastThemeChanged: (theme) => `Motiv byl změněn na ${theme === 'dark' ? 'Tmavý' : 'Světlý'}`,
      toastTilawahPlaying: (suratNama, ayat) => `Přehrávání recitace Súry ${suratNama}:${ayat} (Mishary Alafasy)`,
      toastTilawahPaused: "Recitace byla pozastavena.",
      toastTilawahEnded: "Recitace byla dokončena.",
      toastAudioFailed: "Chyba při přehrávání audia.",
      toastTranslationStopped: "Hlasový překlad byl zastaven.",
      toastTtsNotSupported: "Váš prohlížeč nepodporuje syntézu řeči (TTS).",
      toastTranslationNotAvail: "Text překladu není k dispozici.",
      toastSpeakingMeaning: (suratNama, ayat) => `Předčítání překladu Súry ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Arabská výslovnost: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Předčítání významu: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Předčítání verše ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Arabské slovo "${word}" bylo zkopírováno!`,
      toastLatinCopied: "Transliterace byla zkopírována!",
      toastSummaryCopied: "Kompletní informace o slovu byly zkopírovány!",
      toastCsvExported: (nk) => `Verše pro slovo ${nk} byly exportovány do CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_cs || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_cs || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Vztažné zájmeno' : 'Zájmeno';
        return `${prefix} ${cleanWord}, ${latin}znamená: ${arti}. ${desc ? 'Výklad: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    dv: {
      pageTitle: "ޖާމިދު މަބްނީ ރަދީފު | ޤުރްއާނުގެ ބަސްތަކާއި އާޔަތްތަކުގެ ދަލީލު",
      brandTitle: "ރަދީފު <span>ޖާމިދު މަބްނީ</span>",
      brandSubtitle: "ޤުރްއާނުގެ ބަސްތަކުގެ ބާވަތްތަކާއި ނަންބަރުތައް ބަޔާންކުރާ ރަދީފު",
      themeToggleTitle: "ކުލަ އަނދިރި / އަލި މޯޑަށް ބަދަލުކުރުން",
      labelLangSelect: "ތަރުޖަމާ އަދި އަޑުގެ ބަސް:",
      translationSourceHtml: "ތަރުޖަމާ: <strong>ދިވެހިރާއްޖޭގެ ރައީސުލްޖުމްހޫރިއްޔާގެ އޮފީސް</strong>",
      optgroupEastAsia: "🌏 ދެކުނު އިރުމަތީ އަދި އިރުމަތީ އޭޝިއާ",
      optgroupMidEast: "🕌 މެދުއިރުމަތި، މެދުތެރޭ އޭޝިއާ އަދި ކައުކަސަސް",
      optgroupSouthAsia: "🪷 ދެކުނު އޭޝިއާ އަދި އިންޑިއާ ކަނޑު",
      optgroupAfrica: "🌍 އެފްރިކާ",
      optgroupEurope: "🏛️ ހުޅަނގު، އުތުރު، މެދުތެރޭ އަދި އިރުމަތީ ޔޫރަޕް",
      tabBadgeJamid: "7 ބަސްބަހުގެ ބައި",
      tabBadgeHarf: "17 ޙަރުފުގެ ބައި",
      
      // Control Card
      step1Label: "1. ބަހުގެ ބާވަތް (ބައި) ޚިޔާރުކުރައްވާ",
      step1Placeholder: "ބަހުގެ ބާވަތް ޚިޔާރުކުރައްވާ",
      step1OptionDhamir: "1. ޟަމީރުތައް (Dhamir - ކަންކުރާ އިސްމު)",
      step1OptionMawshul: "2. އިސްމު މައުޞޫލް (Mawshul - ގުޅުވައިދޭ އިސްމު)",
      step1OptionIstifham: "3. އިސްމު އިސްތިފްހާމް (Istifham - ސުވާލުކުރާ އިސްމު)",
      step1OptionSyarath: "4. އިސްމު ޝަރަތު (Syarath - ޝަރުޠުކުރާ އިސްމު)",
      step1OptionIsyarah: "5. އިސްމު އިޝާރާތް (Isyarah - އިޝާރާތްކުރާ އިސްމު)",
      step1OptionIsimFiil: "6. އިސްމު ފިޢުލު (Isim Fi'il - ފިޢުލުގެ މާނަދޭ އިސްމު)",
      step1OptionFiilJamid: "7. ފިޢުލު ޖާމިދު (Fi'il Jamid - ބަދަލުނުވާ ފިޢުލު)",
      step2Label: "2. ބަހުގެ ނަންބަރު ޚިޔާރުކުރައްވާ",
      step2Placeholder: "ބަހުގެ ނަންބަރު ޚިޔާރުކުރައްވާ",
      welcomeTitle: "ބަހުގެ ބާވަތާއި ނަންބަރު ޚިޔާރުކުރައްވާ",
      welcomeSubtitle: "ޢަރަބި ލަފްޒު، ދިވެހި ތަރުޖަމާ، ޤުރްއާނުގައި ތަކުރާރުވެފައިވާ ޢަދަދާއި އާޔަތްތައް ބެއްލެވުމަށް މަތީ މެނޫއިން ބަހުގެ ބާވަތް ޚިޔާރުކުރައްވާ.",
      
      // Spotlight Card
      wordFormBadge: "ބަހުގެ ބާވަތް",
      wordNoBadgePrefix: "ބަސް ނަންބަރު:",
      arabicVoiceBtn: "ޢަރަބި އަޑު",
      arabicVoiceTooltip: "ޢަރަބި ކިޔުމުގެ އަޑު އެއްސެވުމަށް (TTS)",
      meaningVoiceBtn: "މާނައިގެ އަޑު",
      meaningVoiceTooltip: "ދިވެހި ތަރުޖަމާގެ އަޑު އެއްސެވުމަށް (TTS)",
      copyArabicTooltip: "ޢަރަބި ބަސް ކޮޕީކުރައްވާ",
      copyInfoBtn: "މަޢުލޫމާތު ކޮޕީ",
      copyInfoTooltip: "ބަހުގެ ފުރިހަމަ މަޢުލޫމާތު ކޮޕީކުރައްވާ",
      freqLabel: "ކީރިތި ޤުރްއާނުގައި ތަކުރާރުވި ޢަދަދު",
      freqSub: "ޖުމްލަ އައިސްފައިވާ ޢަދަދު",
      freqMuttashilVal: "ގުޅިފައިވާ ބާވަތް (މުއްތަޞިލް)",
      freqMuttashilSub: "ގުޅިފައިވާ ޟަމީރެއްގެ ގޮތުގައި",
      totalAyatLabel: "ޖުމްލަ އާޔަތްތައް",
      totalAyatSub: "ޑޭޓާބޭސްގައި ހިމެނޭ",
      sampleAyatSuffix: "މިސާލު އާޔަތްތައް",
      transliterationPrefix: "ލިޔެކިޔުން:",
      meaningPrefix: "މާނަ:",
      
      // References Section
      referencesTitlePrefix: "މި ބަހަށް ކީރިތި ޤުރްއާނުން އައިސްފައިވާ އާޔަތްތައް:",
      ayatCountBadgePattern: (cur, total) => `އާޔަތް ${cur} / ${total}`,
      ayatCountZero: "0 އާޔަތް",
      searchPlaceholder: "ސޫރަތުގެ ނަން ނުވަތަ އާޔަތުގެ ނަންބަރުން ހޯއްދަވާ...",
      exportCsvBtn: "CSV އަށް އެކްސްޕޯޓް",
      exportCsvTooltip: "މި ބަހުގެ ހުރިހާ އާޔަތްތަކެއް CSV ފައިލަކަށް ޑައުންލޯޑްކުރައްވާ",
      
      // Ayat Card
      surahPrefix: "ސޫރަތް",
      surahPositionTag: (cur, surahNo, ayatNo) => `ސޫރަތް #${surahNo} • އާޔަތް #${ayatNo}`,
      playTranslationBtn: "ތަރުޖަމާގެ އަޑު",
      stopTranslationBtn: "އަޑު ހުއްޓުވާ",
      playTilawahBtn: "ތިލާވަތު އަޑުއައްސަވާ",
      pauseTilawahBtn: "މެދުކަނޑާލައްވާ",
      askAiBtn: "AI އާ ސުވާލުކުރައްވާ",
      askAiTooltip: "މި އާޔަތުގެ އިޢުރާބާއި ތަފްސީރާ ބެހޭގޮތުން AI އެހީތެރިޔާއާ ސުވާލުކުރައްވާ",
      aiModalTitle: "ޤުރްއާން AI އެހީތެރިޔާ",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `ސޫރަތް ${suratNama}:${ayat} ދިރާސާ • ބަސް "${kata}" (${noKata})`,
      aiTopicLabel: "ދިރާސާކުރަން ބޭނުންވާ ދާއިރާ:",
      aiPromptPreviewLabel: "އުފައްދާފައިވާ AI ސުވާލު (Prompt):",
      aiTopicNahwu: "🔍 ޢަރަބި ގްރެމަރ (ނަޙްވު/ޞަރްފު) އަދި އިޢުރާބު",
      aiTopicTafsir: "📖 ތަފްސީރާއި އާޔަތުގެ ޢިބްރަތްތައް",
      aiTopicBalaghah: "✨ ޤުރްއާނުގެ ބަލާޣާތާއި ފަޞާޙާތްތެރިކަން",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "ސުވާލު ކޮޕީކުރައްވާ",
      toastPromptCopied: "AI ސުވާލު ކްލިޕްބޯޑަށް ކޮޕީކުރެވިއްޖެ!",
      ayahPill: (n) => `އާޔަތް ${n}`,
      flipToArabicBtn: "ޢަރަބި ލިޔުން ދައްކަވާ",
      flipToTranslationBtn: "ތަރުޖަމާ ދައްކަވާ",
      translationBoxHeader: "ދިވެހި ތަރުޖަމާ (ދިވެހިރާއްޖޭގެ ރައީސުލްޖުމްހޫރިއްޔާގެ އޮފީސް)",
      
      // Pagination & Empty State
      emptyStateTitle: "އެއްވެސް ނަތީޖާއެއް ނުފެނުނު",
      emptyStateText: "ހޯއްދެވި ބަހާ ގުޅޭ ސޫރަތެއް ނުވަތަ އާޔަތެއް ނުފެނުނެވެ.",
      btnResetSearch: "އަލުން ހޯއްދަވާ",
      paginationPrev: "ކުރީގެ",
      paginationNext: "ދެން އޮތް",
      paginationInfo: (cur, total) => `ޞަފްޙާ ${cur} / ${total}`,
      
      // Toasts
      toastLangChanged: "ބަސް ދިވެހި ބަހަށް ބަދަލުކުރެވިއްޖެ 🇲🇻",
      toastThemeChanged: (theme) => `ކުލަ ${theme === 'dark' ? 'އަނދިރި' : 'އަލި'} މޯޑަށް ބަދަލުކުރެވިއްޖެ`,
      toastTilawahPlaying: (suratNama, ayat) => `ސޫރަތް ${suratNama}:${ayat} ގެ ތިލާވަތް ޖަހަނީ`,
      toastTilawahPaused: "ތިލާވަތު މެދުކަނޑައިލެވިއްޖެ.",
      toastTilawahEnded: "ތިލާވަތު ނިމިއްޖެ.",
      toastAudioFailed: "އަޑު ޖެހުމުގައި މައްސަލައެއް ޖެހިއްޖެ.",
      toastTranslationStopped: "ތަރުޖަމާގެ އަޑު ހުއްޓުވިއްޖެ.",
      toastTtsNotSupported: "ބްރައުޒަރުން އަޑު ޖެހުމަށް (TTS) ތާއީދެއް ނުކުރެއެވެ.",
      toastTranslationNotAvail: "ތަރުޖަމާގެ ލިޔުމެއް ނެތެވެ.",
      toastSpeakingMeaning: (suratNama, ayat) => `ސޫރަތް ${suratNama}:${ayat} ގެ ތަރުޖަމާ ކިޔަނީ`,
      toastSpeakingArabic: (word) => `ޢަރަބި ކިޔުން: ${word}`,
      toastSpeakingWordMeaning: (arti) => `މާނަ ކިޔަނީ: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `އާޔަތް ${suratNama}:${ayat} ކިޔަނީ`,
      toastArabicCopied: (word) => `ޢަރަބި ބަސް "${word}" ކޮޕީކުރެވިއްޖެ!`,
      toastLatinCopied: "ލިޔެކިޔުން ކޮޕީކުރެވިއްޖެ!",
      toastSummaryCopied: "ބަހުގެ ފުރިހަމަ މަޢުލޫމާތު ކޮޕީކުރެވިއްޖެ!",
      toastCsvExported: (nk) => `ބަސް ${nk} ގެ އާޔަތްތައް CSV އަށް އެކްސްޕޯޓްކުރެވިއްޖެ!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_dv || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_dv || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'އިސްމު މައުޞޫލް' : 'ޟަމީރު';
        return `${prefix} ${cleanWord}, ${latin}މާނައަކީ: ${arti}. ${desc ? 'ތަފްޞީލު: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    no: {
      pageTitle: "Jamid Mabny Ordbok | Interaktive Koranske Ord og Versreferanser",
      brandTitle: "Ordbok <span>Jamid Mabny</span>",
      brandSubtitle: "Interaktiv ordbok for uforanderlige ord og pronomen i Koranen",
      themeToggleTitle: "Bytt mørkt / lyst tema",
      labelLangSelect: "Oversettelses- og talespråk:",
      translationSourceHtml: "Oversettelse: <strong>Einar Berg (Koranen på norsk)</strong>",
      optgroupEastAsia: "🌏 Sørøst- og Øst-Asia",
      optgroupMidEast: "🕌 Midtøsten, Sentral-Asia og Kaukasus",
      optgroupSouthAsia: "🪷 Sør-Asia og Det indiske hav",
      optgroupAfrica: "🌍 Afrika",
      optgroupEurope: "🏛️ Vest-, Nord-, Sentral- og Øst-Europa",
      tabBadgeJamid: "7 ordformer",
      tabBadgeHarf: "17 partikkelformer",
      
      // Control Card
      step1Label: "1. Velg ordform (kategori)",
      step1Placeholder: "Velg ordform",
      step1OptionDhamir: "1. Pronomen (Dhamir / Pronomen)",
      step1OptionMawshul: "2. Relativpronomen (Ism Mawshul)",
      step1OptionIstifham: "3. Spørrepronomen (Ism Istifham)",
      step1OptionSyarath: "4. Betingelsesord (Ism Syarath)",
      step1OptionIsyarah: "5. Påpekende pronomen (Ism Isyarah)",
      step1OptionIsimFiil: "6. Verbale substantiv (Ism Fi'il)",
      step1OptionFiilJamid: "7. Uforanderlige verb (Fi'il Jamid)",
      step2Label: "2. Velg ordnummer",
      step2Placeholder: "Velg ordnummer",
      welcomeTitle: "Vennligst velg en ordform og et nummer",
      welcomeSubtitle: "Velg en ordform fra menyen over for å utforske arabisk tekst, norsk oversettelse, frekvens i Koranen og versreferanser.",
      
      // Spotlight Card
      wordFormBadge: "Ordform",
      wordNoBadgePrefix: "Ord nr.:",
      arabicVoiceBtn: "Arabisk tale",
      arabicVoiceTooltip: "Hør arabisk uttale (TTS)",
      meaningVoiceBtn: "Betydningslyd",
      meaningVoiceTooltip: "Hør norsk betydning (TTS)",
      copyArabicTooltip: "Kopier arabisk ord",
      copyInfoBtn: "Kopier info",
      copyInfoTooltip: "Kopier all grammatikkinformasjon",
      freqLabel: "Frekvens i Koranen",
      freqSub: "Totalt antall forekomster",
      freqMuttashilVal: "Tilknyttet form (Muttasil)",
      freqMuttashilSub: "Som tilknyttet pronomen",
      totalAyatLabel: "Totalt referansevers",
      totalAyatSub: "Tilgjengelig i databasen",
      sampleAyatSuffix: "Eksempelvers",
      transliterationPrefix: "Translitterasjon:",
      meaningPrefix: "Betydning:",
      
      // References Section
      referencesTitlePrefix: "Koranske vers for ordet:",
      ayatCountBadgePattern: (cur, total) => `Vers ${cur} av ${total}`,
      ayatCountZero: "0 Vers",
      searchPlaceholder: "Søk etter suranavn eller versnummer...",
      exportCsvBtn: "Eksporter til CSV",
      exportCsvTooltip: "Last ned alle referansevers til en CSV-fil",
      
      // Ayat Card
      surahPrefix: "Sura",
      surahPositionTag: (cur, surahNo, ayatNo) => `Sura #${surahNo} • Vers #${ayatNo}`,
      playTranslationBtn: "Spill oversettelse",
      stopTranslationBtn: "Stopp lyd",
      playTilawahBtn: "Spill resitasjon",
      pauseTilawahBtn: "Pause",
      askAiBtn: "Spør AI",
      askAiTooltip: "Spør AI-assistenten om grammatikk og tafsir for dette verset",
      aiModalTitle: "Koransk AI-assistent",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Analyse av Sura ${suratNama}:${ayat} • Ordet "${kata}" (${noKata})`,
      aiTopicLabel: "Velg analysetema:",
      aiPromptPreviewLabel: "Generert AI-spørsmål (Prompt):",
      aiTopicNahwu: "🔍 Arabisk grammatikk (Nahw/Sarf) og I'rab",
      aiTopicTafsir: "📖 Tafsir (Fortolkning og lærdommer)",
      aiTopicBalaghah: "✨ Balaghah (Koransk retorikk og veltalenhet)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Kopier Spørsmål",
      toastPromptCopied: "AI-spørsmålet ble kopiert til utklippstavlen!",
      ayahPill: (n) => `Vers ${n}`,
      flipToArabicBtn: "Vis arabisk tekst",
      flipToTranslationBtn: "Vis oversettelse",
      translationBoxHeader: "Norsk oversettelse (Einar Berg)",
      
      // Pagination & Empty State
      emptyStateTitle: "Ingen resultater funnet",
      emptyStateText: "Ingen sura eller vers samsvarte med søkekriteriene dine.",
      btnResetSearch: "Tilbakestill søk",
      paginationPrev: "Forrige",
      paginationNext: "Neste",
      paginationInfo: (cur, total) => `Side ${cur} av ${total}`,
      
      // Toasts
      toastLangChanged: "Språket ble endret til Norsk 🇳🇴",
      toastThemeChanged: (theme) => `Temaet ble endret til ${theme === 'dark' ? 'Mørkt' : 'Lyst'}`,
      toastTilawahPlaying: (suratNama, ayat) => `Spiller resitasjon av Sura ${suratNama}:${ayat} (Mishary Alafasy)`,
      toastTilawahPaused: "Resitasjonen er satt på pause.",
      toastTilawahEnded: "Resitasjonen er fullført.",
      toastAudioFailed: "Feil ved avspilling av lyd.",
      toastTranslationStopped: "Oversettelseslyden ble stoppet.",
      toastTtsNotSupported: "Nettleseren din støtter ikke talesyntese (TTS).",
      toastTranslationNotAvail: "Oversettelsestekst er ikke tilgjengelig.",
      toastSpeakingMeaning: (suratNama, ayat) => `Leser oversettelsen av Sura ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Arabisk uttale: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Leser betydning: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Leser vers ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Arabisk ord "${word}" ble kopiert!`,
      toastLatinCopied: "Translitterasjon ble kopiert!",
      toastSummaryCopied: "Fullstendig informasjon ble kopiert!",
      toastCsvExported: (nk) => `Vers for ord ${nk} ble eksportert til CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_no || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_no || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Relativpronomen' : 'Pronomen';
        return `${prefix} ${cleanWord}, ${latin}betyr: ${arti}. ${desc ? 'Forklaring: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    pl: {
      pageTitle: "Słownik Dżamid Mabni | Interaktywne Słowa i Referencje Wersetów Koranu",
      brandTitle: "Słownik <span>Dżamid Mabni</span>",
      brandSubtitle: "Interaktywny słownik nieodmiennych słów i zaimków w Koranie",
      themeToggleTitle: "Przełącz motyw ciemny / jasny",
      labelLangSelect: "Język tłumaczenia i głosu:",
      translationSourceHtml: "Tłumaczenie: <strong>Prof. Józef Bielawski (Koran po polsku)</strong>",
      optgroupEastAsia: "🌏 Azja Południowo-Wschodnia i Wschodnia",
      optgroupMidEast: "🕌 Bliski Wschód, Azja Środkowa i Kaukaz",
      optgroupSouthAsia: "🪷 Azja Południowa i Ocean Indyjski",
      optgroupAfrica: "🌍 Afryka",
      optgroupEurope: "🏛️ Europa Zachodnia, Północna, Środkowa i Wschodnia",
      tabBadgeJamid: "7 form wyrazów",
      tabBadgeHarf: "17 form partykuł",
      
      // Control Card
      step1Label: "1. Wybierz formę słowa (kategorię)",
      step1Placeholder: "Wybierz formę słowa",
      step1OptionDhamir: "1. Zaimki osobowe (Dhamir / Zaimki)",
      step1OptionMawshul: "2. Zaimki względne (Ism Mawshul)",
      step1OptionIstifham: "3. Zaimki pytające (Ism Istifham)",
      step1OptionSyarath: "4. Zaimki warunkowe (Ism Syarath)",
      step1OptionIsyarah: "5. Zaimki wskazujące (Ism Isyarah)",
      step1OptionIsimFiil: "6. Rzeczowniki czasownikowe (Ism Fi'il)",
      step1OptionFiilJamid: "7. Czasowniki nieodmienne (Fi'il Jamid)",
      step2Label: "2. Wybierz numer słowa",
      step2Placeholder: "Wybierz numer słowa",
      welcomeTitle: "Proszę wybrać formę i numer słowa",
      welcomeSubtitle: "Wybierz formę słowa z menu powyżej, aby zapoznać się z arabskim tekstem, polskim tłumaczeniem, częstością w Koranie i referencjami wersetów.",
      
      // Spotlight Card
      wordFormBadge: "Forma słowa",
      wordNoBadgePrefix: "Słowo nr:",
      arabicVoiceBtn: "Głos arabski",
      arabicVoiceTooltip: "Odsłuchaj arabską wymowę (TTS)",
      meaningVoiceBtn: "Głos tłumaczenia",
      meaningVoiceTooltip: "Odsłuchaj polskie znaczenie (TTS)",
      copyArabicTooltip: "Kopiuj słowo arabskie",
      copyInfoBtn: "Kopiuj info",
      copyInfoTooltip: "Kopiuj kompletne informacje gramatyczne",
      freqLabel: "Częstość w Koranie",
      freqSub: "Łączna liczba wystąpień",
      freqMuttashilVal: "Forma łączna (Muttasil)",
      freqMuttashilSub: "Jako zaimek łączny",
      totalAyatLabel: "Łącznie wersetów referencyjnych",
      totalAyatSub: "Dostępnych w bazie danych",
      sampleAyatSuffix: "Przykładowe wersety",
      transliterationPrefix: "Transliteracja:",
      meaningPrefix: "Znaczenie:",
      
      // References Section
      referencesTitlePrefix: "Wersety Koranu dla słowa:",
      ayatCountBadgePattern: (cur, total) => `Werset ${cur} z ${total}`,
      ayatCountZero: "0 Wersetów",
      searchPlaceholder: "Szukaj według nazwy sury lub numeru wersetu...",
      exportCsvBtn: "Eksportuj do CSV",
      exportCsvTooltip: "Pobierz wszystkie wersety referencyjne do pliku CSV",
      
      // Ayat Card
      surahPrefix: "Sura",
      surahPositionTag: (cur, surahNo, ayatNo) => `Sura #${surahNo} • Werset #${ayatNo}`,
      playTranslationBtn: "Odtwórz tłumaczenie",
      stopTranslationBtn: "Zatrzymaj głos",
      playTilawahBtn: "Odtwórz recytację",
      pauseTilawahBtn: "Wstrzymaj",
      askAiBtn: "Zapytaj AI",
      askAiTooltip: "Zapytaj asystenta AI o gramatykę i tafsir tego wersetu",
      aiModalTitle: "Koraniczny Asystent AI",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Analiza Sury ${suratNama}:${ayat} • Słowo "${kata}" (${noKata})`,
      aiTopicLabel: "Wybierz temat analizy:",
      aiPromptPreviewLabel: "Wygenerowane zapytanie AI (Prompt):",
      aiTopicNahwu: "🔍 Gramatyka arabska (Nahw/Sarf) i I'rab",
      aiTopicTafsir: "📖 Tafsir (Egzegeza i nauki wersetu)",
      aiTopicBalaghah: "✨ Balaghah (Retoryka i piękno Koranu)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Kopiuj Zapytanie",
      toastPromptCopied: "Zapytanie AI zostało skopiowane do schowka!",
      ayahPill: (n) => `Werset ${n}`,
      flipToArabicBtn: "Pokaż tekst arabski",
      flipToTranslationBtn: "Pokaż tłumaczenie",
      translationBoxHeader: "Polskie tłumaczenie (Prof. Józef Bielawski)",
      
      // Pagination & Empty State
      emptyStateTitle: "Nie znaleziono wyników",
      emptyStateText: "Żadna sura ani werset nie odpowiada wpisanym kryteriom wyszukiwania.",
      btnResetSearch: "Zresetuj wyszukiwanie",
      paginationPrev: "Poprzednia",
      paginationNext: "Następna",
      paginationInfo: (cur, total) => `Strona ${cur} z ${total}`,
      
      // Toasts
      toastLangChanged: "Język został zmieniony na Polski 🇵🇱",
      toastThemeChanged: (theme) => `Motyw został zmieniony na ${theme === 'dark' ? 'Ciemny' : 'Jasny'}`,
      toastTilawahPlaying: (suratNama, ayat) => `Odtwarzanie recytacji Sury ${suratNama}:${ayat} (Mishary Alafasy)`,
      toastTilawahPaused: "Recytacja została wstrzymana.",
      toastTilawahEnded: "Recytacja została zakończona.",
      toastAudioFailed: "Błąd podczas odtwarzania dźwięku.",
      toastTranslationStopped: "Głosowe tłumaczenie zostało zatrzymane.",
      toastTtsNotSupported: "Twoja przeglądarka nie obsługuje syntezy mowy (TTS).",
      toastTranslationNotAvail: "Tekst tłumaczenia jest niedostępny.",
      toastSpeakingMeaning: (suratNama, ayat) => `Czytanie tłumaczenia Sury ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Wymowa arabska: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Czytanie znaczenia: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Czytanie wersetu ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Arabskie słowo "${word}" zostało skopiowane!`,
      toastLatinCopied: "Transliteracja została skopiowana!",
      toastSummaryCopied: "Kompletne informacje o słowie zostały skopiowane!",
      toastCsvExported: (nk) => `Wersety dla słowa ${nk} zostały wyeksportowane do CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_pl || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_pl || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Zaimek względny' : 'Zaimek osobowy';
        return `${prefix} ${cleanWord}, ${latin}oznacza: ${arti}. ${desc ? 'Wyjaśnienie: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    ro: {
      pageTitle: "Dicționar Jamid Mabny | Cuvinte și Referințe Coranice Interactive",
      brandTitle: "Dicționar <span>Jamid Mabny</span>",
      brandSubtitle: "Dicționar interactiv pentru cuvinte invariabile și pronume din Coran",
      themeToggleTitle: "Comută tema întunecată / luminoasă",
      labelLangSelect: "Limba traducerii și a vocii:",
      translationSourceHtml: "Traducere: <strong>Prof. George Grigore (Coranul în limba română)</strong>",
      optgroupEastAsia: "🌏 Asia de Sud-Est și Asia de Est",
      optgroupMidEast: "🕌 Orientul Mijlociu, Asia Centrală și Caucaz",
      optgroupSouthAsia: "🪷 Asia de Sud și Oceanul Indian",
      optgroupAfrica: "🌍 Africa",
      optgroupEurope: "🏛️ Europa de Vest, Nord, Centrală și de Est",
      tabBadgeJamid: "7 Forme de Cuvinte",
      tabBadgeHarf: "17 Forme de Harf",
      
      // Control Card
      step1Label: "1. Alegeți forma cuvântului (categoria)",
      step1Placeholder: "Alegeți forma cuvântului",
      step1OptionDhamir: "1. Pronume (Dhamir / Pronume)",
      step1OptionMawshul: "2. Pronume relative (Ism Mawshul)",
      step1OptionIstifham: "3. Pronume interogative (Ism Istifham)",
      step1OptionSyarath: "4. Cuvinte condiționale (Ism Syarath)",
      step1OptionIsyarah: "5. Pronume demonstrative (Ism Isyarah)",
      step1OptionIsimFiil: "6. Substantive verbale (Ism Fi'il)",
      step1OptionFiilJamid: "7. Verbe invariabile (Fi'il Jamid)",
      step2Label: "2. Alegeți numărul cuvântului",
      step2Placeholder: "Alegeți numărul cuvântului",
      welcomeTitle: "Vă rugăm să alegeți o formă și un număr de cuvânt",
      welcomeSubtitle: "Selectați o formă din meniul de mai sus pentru a explora textul arab, traducerea în română, frecvența în Coran și referințele versetelor.",
      
      // Spotlight Card
      wordFormBadge: "Forma cuvântului",
      wordNoBadgePrefix: "Cuvânt nr:",
      arabicVoiceBtn: "Voce arabă",
      arabicVoiceTooltip: "Ascultă pronunția arabă (TTS)",
      meaningVoiceBtn: "Voce traducere",
      meaningVoiceTooltip: "Ascultă sensul în limba română (TTS)",
      copyArabicTooltip: "Copiază cuvântul arab",
      copyInfoBtn: "Copiază info",
      copyInfoTooltip: "Copiază toate informațiile gramaticale",
      freqLabel: "Frecvența în Coran",
      freqSub: "Număr total de apariții",
      freqMuttashilVal: "Formă alipită (Muttasil)",
      freqMuttashilSub: "Ca pronume alipit",
      totalAyatLabel: "Total versete de referință",
      totalAyatSub: "Disponibile în baza de date",
      sampleAyatSuffix: "Versete exemplificative",
      transliterationPrefix: "Transliterație:",
      meaningPrefix: "Sens:",
      
      // References Section
      referencesTitlePrefix: "Versete coranice pentru cuvântul:",
      ayatCountBadgePattern: (cur, total) => `Versetul ${cur} din ${total}`,
      ayatCountZero: "0 Versete",
      searchPlaceholder: "Căutare după numele surei sau numărul versetului...",
      exportCsvBtn: "Exportă în CSV",
      exportCsvTooltip: "Descarcă toate versetele de referință într-un fișier CSV",
      
      // Ayat Card
      surahPrefix: "Sura",
      surahPositionTag: (cur, surahNo, ayatNo) => `Sura #${surahNo} • Versetul #${ayatNo}`,
      playTranslationBtn: "Redă traducerea",
      stopTranslationBtn: "Oprește vocea",
      playTilawahBtn: "Redă recitarea",
      pauseTilawahBtn: "Pauză",
      askAiBtn: "Întreabă AI",
      askAiTooltip: "Întreabă asistentul AI despre gramatica și tafsirul acestui verset",
      aiModalTitle: "Asistent AI Coranic",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Analiza Surei ${suratNama}:${ayat} • Cuvântul "${kata}" (${noKata})`,
      aiTopicLabel: "Alegeți tema analizei:",
      aiPromptPreviewLabel: "Întrebare AI generată (Prompt):",
      aiTopicNahwu: "🔍 Gramatică arabă (Nahw/Sarf) și I'rab",
      aiTopicTafsir: "📖 Tafsir (Exegeză și învățături)",
      aiTopicBalaghah: "✨ Balaghah (Retorică și elocință coranică)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Copiază Întrebarea",
      toastPromptCopied: "Întrebarea AI a fost copiată în clipboard!",
      ayahPill: (n) => `Versetul ${n}`,
      flipToArabicBtn: "Afișează textul arab",
      flipToTranslationBtn: "Afișează traducerea",
      translationBoxHeader: "Traducere în limba română (Prof. George Grigore)",
      
      // Pagination & Empty State
      emptyStateTitle: "Niciun rezultat găsit",
      emptyStateText: "Nicio sură sau verset nu corespunde criteriilor dumneavoastră de căutare.",
      btnResetSearch: "Resetează căutarea",
      paginationPrev: "Anterior",
      paginationNext: "Următor",
      paginationInfo: (cur, total) => `Pagina ${cur} din ${total}`,
      
      // Toasts
      toastLangChanged: "Limba a fost schimbată în Română 🇷🇴",
      toastThemeChanged: (theme) => `Tema a fost schimbată în ${theme === 'dark' ? 'Întunecată' : 'Luminoasă'}`,
      toastTilawahPlaying: (suratNama, ayat) => `Se redă recitarea Surei ${suratNama}:${ayat} (Mishary Alafasy)`,
      toastTilawahPaused: "Recitarea a fost pusă pe pauză.",
      toastTilawahEnded: "Recitarea s-a încheiat.",
      toastAudioFailed: "Eroare la redarea audio.",
      toastTranslationStopped: "Vocea traducerii a fost oprită.",
      toastTtsNotSupported: "Browserul dumneavoastră nu acceptă sinteza vocală (TTS).",
      toastTranslationNotAvail: "Textul traducerii nu este disponibil.",
      toastSpeakingMeaning: (suratNama, ayat) => `Se citește traducerea Surei ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Pronunție arabă: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Se citește sensul: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Se citește versetul ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Cuvântul arab "${word}" a fost copiat!`,
      toastLatinCopied: "Transliterația a fost copiată!",
      toastSummaryCopied: "Informațiile complete au fost copiate!",
      toastCsvExported: (nk) => `Versetele pentru cuvântul ${nk} au fost exportate în CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ro || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ro || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Pronume relativ' : 'Pronume';
        return `${prefix} ${cleanWord}, ${latin}înseamnă: ${arti}. ${desc ? 'Explicație: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    sv: {
      pageTitle: "Jamid Mabny Ordbok | Interaktiva Koranska Ord och Versreferenser",
      brandTitle: "Ordbok <span>Jamid Mabny</span>",
      brandSubtitle: "Interaktiv ordbok för oböjliga ord och pronomen i Koranen",
      themeToggleTitle: "Växla mörkt / ljust tema",
      labelLangSelect: "Översättnings- och talspråk:",
      translationSourceHtml: "Översättning: <strong>Knut Bernström (Koranens budskap)</strong>",
      optgroupEastAsia: "🌏 Sydost- och Östasien",
      optgroupMidEast: "🕌 Mellanöstern, Centralasien och Kaukasien",
      optgroupSouthAsia: "🪷 Sydasien och Indiska oceanen",
      optgroupAfrica: "🌍 Afrika",
      optgroupEurope: "🏛️ Väst-, Nord-, Central- och Östeuropa",
      tabBadgeJamid: "7 ordformer",
      tabBadgeHarf: "17 partikelformer",
      
      // Control Card
      step1Label: "1. Välj ordform (kategori)",
      step1Placeholder: "Välj ordform",
      step1OptionDhamir: "1. Pronomen (Dhamir / Pronomen)",
      step1OptionMawshul: "2. Relativa pronomen (Ism Mawshul)",
      step1OptionIstifham: "3. Frågande pronomen (Ism Istifham)",
      step1OptionSyarath: "4. Villkorsord (Ism Syarath)",
      step1OptionIsyarah: "5. Påpekande pronomen (Ism Isyarah)",
      step1OptionIsimFiil: "6. Verbalsubstantiv (Ism Fi'il)",
      step1OptionFiilJamid: "7. Oböjliga verb (Fi'il Jamid)",
      step2Label: "2. Välj ordnummer",
      step2Placeholder: "Välj ordnummer",
      welcomeTitle: "Vänligen välj en ordform och ett nummer",
      welcomeSubtitle: "Välj en ordform från menyn ovan för att utforska arabisk text, svensk översättning, frekvens i Koranen och versreferenser.",
      
      // Spotlight Card
      wordFormBadge: "Ordform",
      wordNoBadgePrefix: "Ord nr:",
      arabicVoiceBtn: "Arabiskt tal",
      arabicVoiceTooltip: "Lyssna på arabiskt uttal (TTS)",
      meaningVoiceBtn: "Betydelseljud",
      meaningVoiceTooltip: "Lyssna på svensk betydelse (TTS)",
      copyArabicTooltip: "Kopiera arabiskt ord",
      copyInfoBtn: "Kopiera info",
      copyInfoTooltip: "Kopiera all grammatisk information",
      freqLabel: "Frekvens i Koranen",
      freqSub: "Totalt antal förekomster",
      freqMuttashilVal: "Fogad form (Muttasil)",
      freqMuttashilSub: "Som fogepronomen",
      totalAyatLabel: "Totalt referensverser",
      totalAyatSub: "Tillgängliga i databasen",
      sampleAyatSuffix: "Exempelverser",
      transliterationPrefix: "Translitteration:",
      meaningPrefix: "Betydelse:",
      
      // References Section
      referencesTitlePrefix: "Koranska verser för ordet:",
      ayatCountBadgePattern: (cur, total) => `Vers ${cur} av ${total}`,
      ayatCountZero: "0 Verser",
      searchPlaceholder: "Sök efter suranamn eller versnummer...",
      exportCsvBtn: "Exportera till CSV",
      exportCsvTooltip: "Ladda ner alla referensverser till en CSV-fil",
      
      // Ayat Card
      surahPrefix: "Sura",
      surahPositionTag: (cur, surahNo, ayatNo) => `Sura #${surahNo} • Vers #${ayatNo}`,
      playTranslationBtn: "Spela översättning",
      stopTranslationBtn: "Stoppa ljud",
      playTilawahBtn: "Spela recitation",
      pauseTilawahBtn: "Pausa",
      askAiBtn: "Fråga AI",
      askAiTooltip: "Fråga AI-assistenten om grammatik och tafsir för denna vers",
      aiModalTitle: "Koransk AI-assistent",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Analys av Sura ${suratNama}:${ayat} • Ordet "${kata}" (${noKata})`,
      aiTopicLabel: "Välj analystema:",
      aiPromptPreviewLabel: "Genererad AI-fråga (Prompt):",
      aiTopicNahwu: "🔍 Arabisk grammatik (Nahw/Sarf) och I'rab",
      aiTopicTafsir: "📖 Tafsir (Tolkning och lärdomar)",
      aiTopicBalaghah: "✨ Balaghah (Koransk retorik och vältalighet)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Kopiera Fråga",
      toastPromptCopied: "AI-frågan har kopierats till urklipp!",
      ayahPill: (n) => `Vers ${n}`,
      flipToArabicBtn: "Visa arabisk text",
      flipToTranslationBtn: "Visa översättning",
      translationBoxHeader: "Svensk översättning (Knut Bernström)",
      
      // Pagination & Empty State
      emptyStateTitle: "Inga resultat hittades",
      emptyStateText: "Ingen sura eller vers matchade dina sökkriterier.",
      btnResetSearch: "Återställ sökning",
      paginationPrev: "Föregående",
      paginationNext: "Nästa",
      paginationInfo: (cur, total) => `Sida ${cur} av ${total}`,
      
      // Toasts
      toastLangChanged: "Språket har ändrats till Svenska 🇸🇪",
      toastThemeChanged: (theme) => `Temat har ändrats till ${theme === 'dark' ? 'Mörkt' : 'Ljust'}`,
      toastTilawahPlaying: (suratNama, ayat) => `Spelar recitation av Sura ${suratNama}:${ayat} (Mishary Alafasy)`,
      toastTilawahPaused: "Recitationen är pausad.",
      toastTilawahEnded: "Recitationen är avslutad.",
      toastAudioFailed: "Fel vid ljuduppspelning.",
      toastTranslationStopped: "Översättningsljudet stoppades.",
      toastTtsNotSupported: "Din webbläsare stöder inte talsyntes (TTS).",
      toastTranslationNotAvail: "Översättningstext är inte tillgänglig.",
      toastSpeakingMeaning: (suratNama, ayat) => `Läser översättningen av Sura ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Arabiskt uttal: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Läser betydelse: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Läser vers ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Arabiska ordet "${word}" har kopierats!`,
      toastLatinCopied: "Translitterationen har kopierats!",
      toastSummaryCopied: "Fullständig information har kopierats!",
      toastCsvExported: (nk) => `Verser för ord ${nk} har exporterats till CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_sv || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_sv || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Relativt pronomen' : 'Pronomen';
        return `${prefix} ${cleanWord}, ${latin}betyder: ${arti}. ${desc ? 'Förklaring: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    tg: {
      pageTitle: "Луғати Ҷомид Мабнӣ | Калимаҳо ва Оятҳои Интерактивии Қуръон",
      brandTitle: "Луғати <span>Ҷомид Мабнӣ</span>",
      brandSubtitle: "Луғати интерактивии калимаҳои тағйирнаёбанда ва ҷонишинҳои Қуръони Карим",
      themeToggleTitle: "Иваз кардани мавзӯи торик / равшан",
      labelLangSelect: "Забони тарҷума ва овоз:",
      translationSourceHtml: "Тарҷума: <strong>Абдулмуҳаммад Оятӣ (Тарҷумаи Қуръони Карим)</strong>",
      optgroupEastAsia: "🌏 Осиёи Ҷанубу Шарқӣ ва Шарқӣ",
      optgroupMidEast: "🕌 Ховари Миёна, Осиёи Марказӣ ва Қафқоз",
      optgroupSouthAsia: "🪷 Осиёи Ҷанубӣ ва Уқёнуси Ҳинд",
      optgroupAfrica: "🌍 Африқо",
      optgroupEurope: "🏛️ Аврупои Ғарбӣ, Шимолӣ, Марказӣ ва Шарқӣ",
      tabBadgeJamid: "7 шакли калима",
      tabBadgeHarf: "17 шакли ҳарф",
      
      // Control Card
      step1Label: "1. Шакли калимаро интихоб кунед (гурӯҳ)",
      step1Placeholder: "Интихоби шакли калима",
      step1OptionDhamir: "1. Ҷонишинҳо (Замир / Pronoun)",
      step1OptionMawshul: "2. Исмҳои мавсул (Пайвандакҳо)",
      step1OptionIstifham: "3. Исмҳои пурсишӣ (Истифҳом)",
      step1OptionSyarath: "4. Калимаҳои шартӣ (Шарт)",
      step1OptionIsyarah: "5. Исмҳои ишоратӣ (Ишора)",
      step1OptionIsimFiil: "6. Исмҳои феъл (Исм Фиъл)",
      step1OptionFiilJamid: "7. Феълҳои ҷомид (Тағйирнаёбанда)",
      step2Label: "2. Рақами калимаро интихоб кунед",
      step2Placeholder: "Интихоби рақами калима",
      welcomeTitle: "Лутфан шакл ва рақами калимаро интихоб намоед",
      welcomeSubtitle: "Барои дидани матни арабӣ, тарҷумаи тоҷикӣ, такрор дар Қуръон ва оятҳои шоҳид, шакли калимаро интихоб кунед.",
      
      // Spotlight Card
      wordFormBadge: "Шакли калима",
      wordNoBadgePrefix: "Калимаи №:",
      arabicVoiceBtn: "Овози арабӣ",
      arabicVoiceTooltip: "Шунидани талаффузи арабӣ (TTS)",
      meaningVoiceBtn: "Овози маъно",
      meaningVoiceTooltip: "Шунидани маънои тоҷикӣ (TTS)",
      copyArabicTooltip: "Нусхабардории калимаи арабӣ",
      copyInfoBtn: "Нусхаи маълумот",
      copyInfoTooltip: "Нусхабардории маълумоти пурраи грамматикӣ",
      freqLabel: "Такрор дар Қуръон",
      freqSub: "Миқдори умумии омадан",
      freqMuttashilVal: "Шакли пайваст (Муттасил)",
      freqMuttashilSub: "Ҳамчун ҷонишини пайваст",
      totalAyatLabel: "Ҷамъи оятҳои шоҳид",
      totalAyatSub: "Дар пойгоҳи додаҳо мавҷуд аст",
      sampleAyatSuffix: "Оятҳои намунавӣ",
      transliterationPrefix: "Транслитератсия:",
      meaningPrefix: "Маъно:",
      
      // References Section
      referencesTitlePrefix: "Оятҳои Қуръонӣ барои калимаи:",
      ayatCountBadgePattern: (cur, total) => `Ояти ${cur} аз ${total}`,
      ayatCountZero: "0 Оят",
      searchPlaceholder: "Ҷустуҷӯ аз рӯи номи сура ё рақами оят...",
      exportCsvBtn: "Экспорт ба CSV",
      exportCsvTooltip: "Боргирии ҳамаи оятҳои шоҳид дар формати CSV",
      
      // Ayat Card
      surahPrefix: "Сураи",
      surahPositionTag: (cur, surahNo, ayatNo) => `Сураи #${surahNo} • Ояти #${ayatNo}`,
      playTranslationBtn: "Пахши тарҷума",
      stopTranslationBtn: "Қатъи овоз",
      playTilawahBtn: "Пахши қироат",
      pauseTilawahBtn: "Таваққуф",
      askAiBtn: "Пурсиш аз AI",
      askAiTooltip: "Пурсидани таҳлили грамматикӣ ва тафсири ин оят аз AI",
      aiModalTitle: "Ёрдамчии Зеҳни Сунъии Қуръонӣ",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Таҳлили Сураи ${suratNama}:${ayat} • Калимаи "${kata}" (${noKata})`,
      aiTopicLabel: "Мавзӯи таҳлилро интихоб кунед:",
      aiPromptPreviewLabel: "Матни омодашудаи пурсиш (Prompt):",
      aiTopicNahwu: "🔍 Сарфу наҳви арабӣ ва Эъроб",
      aiTopicTafsir: "📖 Тафсир ва ҳикматҳои оят",
      aiTopicBalaghah: "✨ Балоғат ва фасоҳати Қуръонӣ",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Нусхаи пурсиш",
      toastPromptCopied: "Матни пурсиши AI ба ҳофиза нусхабардорӣ шуд!",
      ayahPill: (n) => `Ояти ${n}`,
      flipToArabicBtn: "Намоиши матни арабӣ",
      flipToTranslationBtn: "Намоиши тарҷума",
      translationBoxHeader: "Тарҷумаи тоҷикӣ (Абдулмуҳаммад Оятӣ)",
      
      // Pagination & Empty State
      emptyStateTitle: "Ягон натиҷа ёфт нашуд",
      emptyStateText: "Ягон сура ё оят ба дархости ҷустуҷӯи шумо мувофиқ наомад.",
      btnResetSearch: "Бозсозии ҷустуҷӯ",
      paginationPrev: "Қаблӣ",
      paginationNext: "Баъдӣ",
      paginationInfo: (cur, total) => `Саҳифаи ${cur} аз ${total}`,
      
      // Toasts
      toastLangChanged: "Забон ба Тоҷикӣ иваз шуд 🇹🇯",
      toastThemeChanged: (theme) => `Мавзӯъ ба ${theme === 'dark' ? 'Торик' : 'Равшан'} иваз шуд`,
      toastTilawahPlaying: (suratNama, ayat) => `Пахши қироати Сураи ${suratNama}:${ayat} (Мишарӣ ал-Афосӣ)`,
      toastTilawahPaused: "Қироат муваққатан боздошта шуд.",
      toastTilawahEnded: "Қироат ба охир расид.",
      toastAudioFailed: "Хатогӣ ҳангоми пахши аудио.",
      toastTranslationStopped: "Овози тарҷума қатъ карда шуд.",
      toastTtsNotSupported: "Браузери шумо синтези овозро (TTS) дастгирӣ намекунад.",
      toastTranslationNotAvail: "Матни тарҷума дастрас нест.",
      toastSpeakingMeaning: (suratNama, ayat) => `Хондани тарҷумаи Сураи ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Талаффузи арабӣ: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Хондани маъно: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Хондани ояти ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Калимаи арабии "${word}" нусхабардорӣ шуд!`,
      toastLatinCopied: "Транслитератсия нусхабардорӣ шуд!",
      toastSummaryCopied: "Маълумоти пурраи калима нусхабардорӣ шуд!",
      toastCsvExported: (nk) => `Оятҳои калимаи ${nk} ба CSV содир шуданд!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_tg || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_tg || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Исми мавсул' : 'Ҷонишин';
        return `${prefix} ${cleanWord}, ${latin}маънояш: ${arti}. ${desc ? 'Тавзеҳ: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    ta: {
      pageTitle: "ஜாமித் மப்னீ அகராதி | திருக்குர்ஆன் சொற்கள் மற்றும் வசனக் குறிப்புகள்",
      brandTitle: "அகராதி <span>ஜாமித் மப்னீ</span>",
      brandSubtitle: "திருக்குர்ஆனின் மாறாச் சொற்கள் மற்றும் பிரதிப்பெயர்களுக்கான ஊடாடும் அகராதி",
      themeToggleTitle: "இருண்ட / வெளிச்ச தீம் மாற்றம்",
      labelLangSelect: "மொழிபெயர்ப்பு மற்றும் குரல் மொழி:",
      translationSourceHtml: "மொழிபெயர்ப்பு: <strong>ஜான் டிரஸ்ட் ஃபவுண்டேஷன் (திருக்குர்ஆன் தமிழாக்கம்)</strong>",
      optgroupEastAsia: "🌏 தென்கிழக்கு & கிழக்கு ஆசியா",
      optgroupMidEast: "🕌 மத்திய கிழக்கு, மத்திய ஆசியா & காகசஸ்",
      optgroupSouthAsia: "🪷 தெற்காசியா & இந்தியப் பெருங்கடல்",
      optgroupAfrica: "🌍 ஆப்பிரிக்கா",
      optgroupEurope: "🏛️ மேற்கு, வடக்கு, மத்திய & கிழக்கு ஐரோப்பா",
      tabBadgeJamid: "7 சொல் வடிவங்கள்",
      tabBadgeHarf: "17 இடைச்சொல் வடிவங்கள்",
      
      // Control Card
      step1Label: "1. சொல் வகையைத் தேர்ந்தெடுக்கவும் (பிரிவு)",
      step1Placeholder: "சொல் வகையைத் தேர்வுசெய்க",
      step1OptionDhamir: "1. பிரதிப்பெயர்கள் (ளமீர் / Pronoun)",
      step1OptionMawshul: "2. இணைப்புச் சொற்கள் (இஸ்மு மவ்ஸூல்)",
      step1OptionIstifham: "3. வினாப்பெயர்கள் (இஸ்மு இஸ்திஃப்ஹாம்)",
      step1OptionSyarath: "4. நிபந்தனைப் பெயர்கள் (இஸ்மு ஷரத்)",
      step1OptionIsyarah: "5. சுட்டுப் பெயர்கள் (இஸ்மு இஷாரா)",
      step1OptionIsimFiil: "6. வினைப் பெயர்ச்சொற்கள் (இஸ்மு ஃபிஇல்)",
      step1OptionFiilJamid: "7. மாறா வினைகள் (ஃபிஇல் ஜாமித்)",
      step2Label: "2. சொல் எண்ணைத் தேர்ந்தெடுக்கவும்",
      step2Placeholder: "சொல் எண்ணைத் தேர்வுசெய்க",
      welcomeTitle: "தயவுசெய்து ஒரு சொல் வகை மற்றும் எண்ணைத் தேர்ந்தெடுக்கவும்",
      welcomeSubtitle: "அரபு உரை, தமிழ் மொழிபெயர்ப்பு, குர்ஆனில் வந்துள்ள எண்ணிக்கை மற்றும் சான்று வசனங்களைப் பார்வையிட மேலே உள்ள மெனுவிலிருந்து சொல் வகையைத் தேர்ந்தெடுக்கவும்.",
      
      // Spotlight Card
      wordFormBadge: "சொல் வகை",
      wordNoBadgePrefix: "சொல் எண்:",
      arabicVoiceBtn: "அரபு குரல்",
      arabicVoiceTooltip: "அரபு உச்சரிப்பைக் கேட்கவும் (TTS)",
      meaningVoiceBtn: "பொருள் குரல்",
      meaningVoiceTooltip: "தமிழ் அர்த்தத்தைக் கேட்கவும் (TTS)",
      copyArabicTooltip: "அரபு சொல்லை நகலெடுக்கவும்",
      copyInfoBtn: "விவரம் நகல்",
      copyInfoTooltip: "முழு இலக்கண விவரங்களையும் நகலெடுக்கவும்",
      freqLabel: "குர்ஆனில் எண்ணிக்கை",
      freqSub: "மொத்த நிகழ்வுகள்",
      freqMuttashilVal: "இணைந்த வடிவம் (முத்தஸில்)",
      freqMuttashilSub: "இணைந்த பிரதிப்பெயராக",
      totalAyatLabel: "மொத்த சான்று வசனங்கள்",
      totalAyatSub: "தரவுத்தளத்தில் உள்ளது",
      sampleAyatSuffix: "மாதிரி வசனங்கள்",
      transliterationPrefix: "ஒலிபெயர்ப்பு:",
      meaningPrefix: "பொருள்:",
      
      // References Section
      referencesTitlePrefix: "இச்சொல்லுக்கான குர்ஆன் வசனங்கள்:",
      ayatCountBadgePattern: (cur, total) => `${total} இல் ${cur}-வது வசனம்`,
      ayatCountZero: "0 வசனங்கள்",
      searchPlaceholder: "சூரா பெயர் அல்லது வசன எண் மூலம் தேடவும்...",
      exportCsvBtn: "CSV ஆக ஏற்றுமதி செய்",
      exportCsvTooltip: "அனைத்து சான்று வசனங்களையும் CSV கோப்பாகப் பதிவிறக்கவும்",
      
      // Ayat Card
      surahPrefix: "சூரா",
      surahPositionTag: (cur, surahNo, ayatNo) => `சூரா #${surahNo} • வசனம் #${ayatNo}`,
      playTranslationBtn: "மொழிபெயர்ப்பைக் கேள்",
      stopTranslationBtn: "குரலை நிறுத்து",
      playTilawahBtn: "ஓதுதலைக் கேள்",
      pauseTilawahBtn: "இடைநிறுத்து",
      askAiBtn: "AI-யிடம் கேள்",
      askAiTooltip: "இவ்வசனத்தின் இலக்கணம் மற்றும் விளக்கவுரையை AI-யிடம் கேட்கவும்",
      aiModalTitle: "திருக்குர்ஆன் AI உதவியாளர்",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `சூரா ${suratNama}:${ayat} ஆய்வு • சொல் "${kata}" (${noKata})`,
      aiTopicLabel: "ஆய்வுத் தலைப்பைத் தேர்ந்தெடுக்கவும்:",
      aiPromptPreviewLabel: "உருவாக்கப்பட்ட AI கேள்வி (Prompt):",
      aiTopicNahwu: "🔍 அரபு இலக்கணம் (நஹ்வு/ஸர்ஃப்) மற்றும் ஈராப்",
      aiTopicTafsir: "📖 தஃப்ஸீர் (விளக்கவுரை மற்றும் படிப்பினைகள்)",
      aiTopicBalaghah: "✨ பலாகா (குர்ஆனின் சொல் நயம் மற்றும் எழில்)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "கேள்வியை நகலெடு",
      toastPromptCopied: "AI கேள்வி கிளிப்போர்டில் நகலெடுக்கப்பட்டது!",
      ayahPill: (n) => `வசனம் ${n}`,
      flipToArabicBtn: "அரபு உரையைக் காட்டு",
      flipToTranslationBtn: "மொழிபெயர்ப்பைக் காட்டு",
      translationBoxHeader: "தமிழ் மொழிபெயர்ப்பு (ஜான் டிரஸ்ட் ஃபவுண்டேஷன்)",
      
      // Pagination & Empty State
      emptyStateTitle: "முடிவுகள் எதுவும் கிடைக்கவில்லை",
      emptyStateText: "உங்கள் தேடல் அளவுகோலுக்கு எந்த சூராவும் வசனமும் பொருந்தவில்லை.",
      btnResetSearch: "தேடலை மீட்டமை",
      paginationPrev: "முந்தையது",
      paginationNext: "அடுத்தது",
      paginationInfo: (cur, total) => `பக்கம் ${cur} / ${total}`,
      
      // Toasts
      toastLangChanged: "மொழி தமிழாக மாற்றப்பட்டது 🇮🇳",
      toastThemeChanged: (theme) => `தீம் ${theme === 'dark' ? 'இருண்ட' : 'வெளிச்ச'} நிறமாக மாற்றப்பட்டது`,
      toastTilawahPlaying: (suratNama, ayat) => `சூரா ${suratNama}:${ayat} ஓதுதல் ஒலிக்கிறது (மிஷாரி அல்-அஃபாஸி)`,
      toastTilawahPaused: "ஓதுதல் இடைநிறுத்தப்பட்டது.",
      toastTilawahEnded: "ஓதுதல் நிறைவடைந்தது.",
      toastAudioFailed: "ஆடியோ இயக்குவதில் பிழை ஏற்பட்டது.",
      toastTranslationStopped: "மொழிபெயர்ப்புக் குரல் நிறுத்தப்பட்டது.",
      toastTtsNotSupported: "உங்கள் உலாவி குரல் தொகுப்பை (TTS) ஆதரிக்கவில்லை.",
      toastTranslationNotAvail: "மொழிபெயர்ப்பு உரை கிடைக்கவில்லை.",
      toastSpeakingMeaning: (suratNama, ayat) => `சூரா ${suratNama}:${ayat} மொழிபெயர்ப்பு வாசிக்கப்படுகிறது`,
      toastSpeakingArabic: (word) => `அரபு உச்சரிப்பு: ${word}`,
      toastSpeakingWordMeaning: (arti) => `பொருள் வாசிக்கப்படுகிறது: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `வசனம் ${suratNama}:${ayat} வாசிக்கப்படுகிறது`,
      toastArabicCopied: (word) => `அரபு சொல் "${word}" நகலெடுக்கப்பட்டது!`,
      toastLatinCopied: "ஒலிபெயர்ப்பு நகலெடுக்கப்பட்டது!",
      toastSummaryCopied: "முழு விவரங்களும் நகலெடுக்கப்பட்டன!",
      toastCsvExported: (nk) => `சொல் ${nk}-க்கான வசனங்கள் CSV கோப்பாக ஏற்றுமதி செய்யப்பட்டன!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ta || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ta || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'இணைப்புச் சொல்' : 'பிரதிப்பெயர்';
        return `${prefix} ${cleanWord}, ${latin}பொருள்: ${arti}. ${desc ? 'விளக்கம்: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    tt: {
      pageTitle: "Җәмид Мәбни сүзлеге | Интерактив Коръән сүзләре һәм аятьләре",
      brandTitle: "Сүзлек <span>Җәмид Мәбни</span>",
      brandSubtitle: "Коръәни Кәримнең үзгәрмәүче сүзләре һәм алмашлыклары сүзлеге",
      themeToggleTitle: "Караңгы / якты тема",
      labelLangSelect: "Тәрҗемә һәм тавыш теле:",
      translationSourceHtml: "Тәрҗемә: <strong>Якуб ибн Нугман (Кәлам Шәриф)</strong>",
      optgroupEastAsia: "🌏 Көньяк-Көнчыгыш һәм Көнчыгыш Азия",
      optgroupMidEast: "🕌 Якын Көнчыгыш, Үзәк Азия һәм Кавказ",
      optgroupSouthAsia: "🪷 Көньяк Азия һәм Индия океаны",
      optgroupAfrica: "🌍 Африка",
      optgroupEurope: "🏛️ Көнбатыш, Төньяк, Үзәк һәм Көнчыгыш Европа",
      tabBadgeJamid: "7 сүз формасы",
      tabBadgeHarf: "17 кисәкчә формасы",
      
      // Control Card
      step1Label: "1. Сүз төрен сайлагыз (төркем)",
      step1Placeholder: "Сүз төрен сайлагыз",
      step1OptionDhamir: "1. Алмашлыклар (Замир / Pronoun)",
      step1OptionMawshul: "2. Исем мәүсул (Бәйләүчеләр)",
      step1OptionIstifham: "3. Сорау алмашлыклары (Истифһам)",
      step1OptionSyarath: "4. Шарт сүзләре (Шарт)",
      step1OptionIsyarah: "5. Күрсәтү алмашлыклары (Ишарә)",
      step1OptionIsimFiil: "6. Исем фигыль (Исем Фигыль)",
      step1OptionFiilJamid: "7. Җәмид фигыльләр (Үзгәрмәүче)",
      step2Label: "2. Сүз санын сайлагыз",
      step2Placeholder: "Сүз санын сайлагыз",
      welcomeTitle: "Зинһар, сүз төрен һәм санын сайлагыз",
      welcomeSubtitle: "Гарәпчә текст, татарча тәрҗемә, Коръәндә кабатлану һәм аятьләрне күрү өчен югарыдагы менюдан сүз төрен сайлагыз.",
      
      // Spotlight Card
      wordFormBadge: "Сүз төре",
      wordNoBadgePrefix: "Сүз №:",
      arabicVoiceBtn: "Гарәпчә тавыш",
      arabicVoiceTooltip: "Гарәпчә укуны тыңлау (TTS)",
      meaningVoiceBtn: "Мәгънә тавышы",
      meaningVoiceTooltip: "Татарча мәгънәне тыңлау (TTS)",
      copyArabicTooltip: "Гарәпчә сүзне күчерү",
      copyInfoBtn: "Мәгълүмат күчерү",
      copyInfoTooltip: "Барлык грамматик мәгълүматны күчерү",
      freqLabel: "Коръәндә килү саны",
      freqSub: "Барлык килүләр",
      freqMuttashilVal: "Ялганма рәвеше (Мөттәсыйль)",
      freqMuttashilSub: "Ялганма алмашлык буларак",
      totalAyatLabel: "Барлык дәлил аятьләр",
      totalAyatSub: "Мәгълүматлар базасында бар",
      sampleAyatSuffix: "Үрнәк аятьләр",
      transliterationPrefix: "Транслитерация:",
      meaningPrefix: "Мәгънәсе:",
      
      // References Section
      referencesTitlePrefix: "Әлеге сүз өчен Коръән аятьләре:",
      ayatCountBadgePattern: (cur, total) => `${total} аятьтән ${cur}-нчесе`,
      ayatCountZero: "0 Аять",
      searchPlaceholder: "Сүрә исеме яки аять саны буенча эзләү...",
      exportCsvBtn: "CSV форматында йөкләү",
      exportCsvTooltip: "Барлык аятьләрне CSV файлы итеп йөкләп алу",
      
      // Ayat Card
      surahPrefix: "Сүрә",
      surahPositionTag: (cur, surahNo, ayatNo) => `Сүрә #${surahNo} • Аять #${ayatNo}`,
      playTranslationBtn: "Тәрҗемәне тыңлау",
      stopTranslationBtn: "Тавышны туктату",
      playTilawahBtn: "Кыйрәәтне тыңлау",
      pauseTilawahBtn: "Туктатып тору",
      askAiBtn: "AI-дан сорау",
      askAiTooltip: "Әлеге аятьнең грамматикасын һәм тәфсирен AI-дан сорау",
      aiModalTitle: "Коръән буенча ясалма фәһем (AI)",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `${suratNama}:${ayat} сүрәсен тикшерү • "${kata}" сүзе (${noKata})`,
      aiTopicLabel: "Анализ темасын сайлагыз:",
      aiPromptPreviewLabel: "Әзерләнгән AI соравы (Prompt):",
      aiTopicNahwu: "🔍 Гарәпчә нәхү/сарф грамматикасы һәм Игъраб",
      aiTopicTafsir: "📖 Тәфсир һәм аятьнең хикмәтләре",
      aiTopicBalaghah: "✨ Бәлагәть һәм Коръән матурлыгы",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Сорауны күчерү",
      toastPromptCopied: "AI соравы хәтергә күчерелде!",
      ayahPill: (n) => `${n}-нче аять`,
      flipToArabicBtn: "Гарәпчә текст",
      flipToTranslationBtn: "Тәрҗемәне күрсәтү",
      translationBoxHeader: "Татарча тәрҗемә (Якуб ибн Нугман)",
      
      // Pagination & Empty State
      emptyStateTitle: "Нәтиҗәләр табылмады",
      emptyStateText: "Сезнең эзләүгә туры килгән сүрә яки аять табылмады.",
      btnResetSearch: "Эзләүне яңарту",
      paginationPrev: "Алдагы",
      paginationNext: "Киләсе",
      paginationInfo: (cur, total) => `${total} биттән ${cur}-нчесе`,
      
      // Toasts
      toastLangChanged: "Тел Татарчага үзгәртелде 🇷🇺",
      toastThemeChanged: (theme) => `Тема ${theme === 'dark' ? 'Караңгы' : 'Якты'}га үзгәртелде`,
      toastTilawahPlaying: (suratNama, ayat) => `${suratNama}:${ayat} аяте кыйрәәте уйнатыла (Мишари Рашид)`,
      toastTilawahPaused: "Кыйрәәт туктатылып торды.",
      toastTilawahEnded: "Кыйрәәт тәмамланды.",
      toastAudioFailed: "Аудио уйнауда хата чыкты.",
      toastTranslationStopped: "Тәрҗемә тавышы туктатылды.",
      toastTtsNotSupported: "Сезнең браузер тавыш синтезын (TTS) хупламый.",
      toastTranslationNotAvail: "Тәрҗемә тексты табылмады.",
      toastSpeakingMeaning: (suratNama, ayat) => `${suratNama}:${ayat} аяте тәрҗемәсе укыла`,
      toastSpeakingArabic: (word) => `Гарәпчә әйтелеш: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Мәгънәсе: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `${suratNama}:${ayat} аяте укыла`,
      toastArabicCopied: (word) => `Гарәпчә "${word}" сүзе күчерелде!`,
      toastLatinCopied: "Транслитерация күчерелде!",
      toastSummaryCopied: "Сүз турында тулы мәгълүмат күчерелде!",
      toastCsvExported: (nk) => `${nk} сүзе өчен аятьләр CSV-га йөкләнде!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_tt || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_tt || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Исем мәүсул' : 'Зат алмашлыгы';
        return `${prefix} ${cleanWord}, ${latin}мәгънәсе: ${arti}. ${desc ? 'Аңлатма: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    ug: {
      pageTitle: "جامىد مەبنىي لۇغىتى | قۇرئان سۆزلىرى ۋە ئايەتلىرى",
      brandTitle: "لۇغەت <span>جامىد مەبنىي</span>",
      brandSubtitle: "قۇرئانى كەرىمدىكى ئۆزگەرمەس سۆزلەر ۋە ئالماشلارنىڭ ئۆزئارا تەسىرلىك لۇغىتى",
      themeToggleTitle: "قاراڭغۇ / يورۇق تېما",
      labelLangSelect: "تەرجىمە ۋە ئاۋاز تىلى:",
      translationSourceHtml: "تەرجىمە: <strong>مۇھەممەد سالىھ (قۇرئان كەرىم ئۇيغۇرچە تەرجىمىسى)</strong>",
      optgroupEastAsia: "🌏 شەرقىي جەنۇبىي ۋە شەرقىي ئاسىيا",
      optgroupMidEast: "🕌 ئوتتۇرا شەرق، ئوتتۇرا ئاسىيا ۋە كاۋكاز",
      optgroupSouthAsia: "🪷 جەنۇبىي ئاسىيا ۋە ھىندى ئوكيان",
      optgroupAfrica: "🌍 ئافرىقا",
      optgroupEurope: "🏛️ غەربىي، شىمالىي، ئوتتۇرا ۋە شەرقىي ياۋروپا",
      tabBadgeJamid: "7 سۆز شەكلى",
      tabBadgeHarf: "17 ھەرف تۈرى",
      
      // Control Card
      step1Label: "1. سۆز شەكلىنى تاللاڭ (تۈر)",
      step1Placeholder: "سۆز شەكلىنى تاللاڭ",
      step1OptionDhamir: "1. ئالماشلار (زەمىر / Pronoun)",
      step1OptionMawshul: "2. ئىسىم مەۋسۇل (باغلىغۇچىلار)",
      step1OptionIstifham: "3. سوئال ئالماشلىرى (ئىستىفھام)",
      step1OptionSyarath: "4. شەرت سۆزلىرى (شەرت)",
      step1OptionIsyarah: "5. كۆرسىتىش ئالماشلىرى (ئىشارەت)",
      step1OptionIsimFiil: "6. پېئىل ئىسىملىرى (ئىسىم فېئىل)",
      step1OptionFiilJamid: "7. تۇراقلىق پېئىللار (فېئىل جامىد)",
      step2Label: "2. سۆز نومۇرىنى تاللاڭ",
      step2Placeholder: "سۆز نومۇرىنى تاللاڭ",
      welcomeTitle: "بىر سۆز شەكلى ۋە نومۇرىنى تاللاڭ",
      welcomeSubtitle: "ئەرەبچە تېكىست، ئۇيغۇرچە تەرجىمە، قۇرئاندىكى سانى ۋە دەلىل ئايەتلەرنى كۆرۈش ئۈچۈن يۇقىرىدىن سۆز شەكلىنى تاللاڭ.",
      
      // Spotlight Card
      wordFormBadge: "سۆز شەكلى",
      wordNoBadgePrefix: "سۆز نومۇرى:",
      arabicVoiceBtn: "ئەرەبچە تەلەپپۇز",
      arabicVoiceTooltip: "ئەرەبچە تەلەپپۇزنى ئاڭلاش (TTS)",
      meaningVoiceBtn: "تەرجىمە ئاۋازى",
      meaningVoiceTooltip: "ئۇيغۇرچە تەرجىمىنى ئاڭلاش (TTS)",
      copyArabicTooltip: "ئەرەبچە سۆزنى كۆچۈرۈش",
      copyInfoBtn: "ئۇچۇر كۆچۈرۈش",
      copyInfoTooltip: "پۈتۈن گرامماتىكىلىق ئۇچۇرنى كۆچۈرۈش",
      freqLabel: "قۇرئاندىكى سانى",
      freqSub: "ئومۇمىي قېتىم سانى",
      freqMuttashilVal: "بىرىكمە شەكلى (مۇتتەسىل)",
      freqMuttashilSub: "بىرىكمە ئالماش سۈپىتىدە",
      totalAyatLabel: "دەلىل ئايەتلەر سانى",
      totalAyatSub: "سانداندا مەۋجۇت",
      sampleAyatSuffix: "ئۈلگە ئايەتلەر",
      transliterationPrefix: "ترانسكرىپسىيە:",
      meaningPrefix: "مەنىسى:",
      
      // References Section
      referencesTitlePrefix: "بۇ سۆز كەلگەن قۇرئان ئايەتلىرى:",
      ayatCountBadgePattern: (cur, total) => `${total} ئايەتتىن ${cur}-ئايەت`,
      ayatCountZero: "0 ئايەت",
      searchPlaceholder: "سۈرە نامى ياكى ئايەت نومۇرى بويىچە ئىزدەڭ...",
      exportCsvBtn: "CSV غا چىقىرىش",
      exportCsvTooltip: "بارلىق دەلىل ئايەتلەرنى CSV ھۆججىتى قىلىپ چۈشۈرۈش",
      
      // Ayat Card
      surahPrefix: "سۈرە",
      surahPositionTag: (cur, surahNo, ayatNo) => `سۈرە #${surahNo} • ئايەت #${ayatNo}`,
      playTranslationBtn: "تەرجىمىنى ئاڭلاش",
      stopTranslationBtn: "ئاۋازنى توختىتىش",
      playTilawahBtn: "قىرائەتنى ئاڭلاش",
      pauseTilawahBtn: "ۋاقىتلىق توختىتىش",
      askAiBtn: "AI دىن سوراش",
      askAiTooltip: "بۇ ئايەتنىڭ ئىعرابى ۋە تەپسىرىنى سۈنئىي ئەقىلدىن سوراش",
      aiModalTitle: "قۇرئانى كەرىم سۈنئىي ئەقىل ياردەمچىسى",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `سۈرە ${suratNama}:${ayat} تەھلىلى • "${kata}" سۆزى (${noKata})`,
      aiTopicLabel: "تەھلىل تېمىسىنى تاللاڭ:",
      aiPromptPreviewLabel: "تەييارلانغان سوئال تېكىستى (Prompt):",
      aiTopicNahwu: "🔍 ئەرەب تىلى گرامماتىكىسى (نەھۋى/سەرف) ۋە ئىعراب",
      aiTopicTafsir: "📖 تەپسىر ۋە ئايەتنىڭ ھېكمەتلىرى",
      aiTopicBalaghah: "✨ بەلاغەت ۋە قۇرئاننىڭ پاساھىتى",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "سوئالنى كۆچۈرۈش",
      toastPromptCopied: "سۈنئىي ئەقىل سوئالى كۆچۈرۈلدى!",
      ayahPill: (n) => `${n}-ئايەت`,
      flipToArabicBtn: "ئەرەبچە تېكىست",
      flipToTranslationBtn: "تەرجىمىنى كۆرسىتىش",
      translationBoxHeader: "ئۇيغۇرچە تەرجىمە (مۇھەممەد سالىھ)",
      
      // Pagination & Empty State
      emptyStateTitle: "ھېچقانداق نەتىجە تېپىلمىدى",
      emptyStateText: "ئىزدەش شەرتىڭىزگە ماس كېلىدىغان سۈرە ياكى ئايەت چىقمىدى.",
      btnResetSearch: "ئىزدەشنى ئەسلىگە كەلتۈرۈش",
      paginationPrev: "ئالدىنقى",
      paginationNext: "كېيىنكى",
      paginationInfo: (cur, total) => `${total} بەتتىن ${cur}-بەت`,
      
      // Toasts
      toastLangChanged: "تىل ئۇيغۇرچىغا ئۆزگەرتىلدى 🇨🇳",
      toastThemeChanged: (theme) => `تېما ${theme === 'dark' ? 'قاراڭغۇ' : 'يورۇق'}قا ئۆزگەرتىلدى`,
      toastTilawahPlaying: (suratNama, ayat) => `سۈرە ${suratNama}:${ayat} قىرائىتى قويۇلدى (مىشارى ئالفاسىي)`,
      toastTilawahPaused: "قىرائەت ۋاقىتلىق توختىتىلدى.",
      toastTilawahEnded: "قىرائەت ئاخىرلاشتى.",
      toastAudioFailed: "ئاۋاز قويۇشتا خاتالىق كۆرۈلدى.",
      toastTranslationStopped: "تەرجىمە ئاۋازى توختىتىلدى.",
      toastTtsNotSupported: "توركۆرگۈچىڭىز ئاۋاز بىرىكتۈرۈش (TTS) نى قوللىمايدۇ.",
      toastTranslationNotAvail: "تەرجىمە تېكىستى تېپىلمىدى.",
      toastSpeakingMeaning: (suratNama, ayat) => `سۈرە ${suratNama}:${ayat} تەرجىمىسى ئوقۇلۇۋاتىدۇ`,
      toastSpeakingArabic: (word) => `ئەرەبچە تەلەپپۇز: ${word}`,
      toastSpeakingWordMeaning: (arti) => `مەنىسى: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `ئايەت ${suratNama}:${ayat} ئوقۇلۇۋاتىدۇ`,
      toastArabicCopied: (word) => `ئەرەبچە سۆز "${word}" كۆچۈرۈلدى!`,
      toastLatinCopied: "ترانسكرىپسىيە كۆچۈرۈلدى!",
      toastSummaryCopied: "سۆز ھەققىدىكى تولۇق ئۇچۇر كۆچۈرۈلدى!",
      toastCsvExported: (nk) => `${nk}-سۆزنىڭ ئايەتلىرى CSV غا چىقىرىلدى!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ug || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ug || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'ئىسىم مەۋسۇل' : 'كىشىلىك ئالماش';
        return `${prefix} ${cleanWord}, ${latin}مەنىسى: ${arti}. ${desc ? 'ئىزاھات: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    uz: {
      pageTitle: "Jomid Mabniy Lug'ati | Interaktiv Qur'on So'zlari va Oyatlar",
      brandTitle: "Lug'at <span>Jomid Mabniy</span>",
      brandSubtitle: "Qur'oni Karimdagi o'zgarmas so'zlar va olmoshlarning interaktiv lug'ati",
      themeToggleTitle: "Tungi / kunduzgi mavzuni o'zgartirish",
      labelLangSelect: "Tarjima va ovoz tili:",
      translationSourceHtml: "Tarjima: <strong>Shayx Muhammad Sodiq Muhammad Yusuf (Tafsiri Hilol)</strong>",
      optgroupEastAsia: "🌏 Janubi-Sharqiy va Sharqiy Osiyo",
      optgroupMidEast: "🕌 Yaqin Sharq, Markaziy Osiyo va Kavkaz",
      optgroupSouthAsia: "🪷 Janubiy Osiyo va Hind Okeani",
      optgroupAfrica: "🌍 Afrika",
      optgroupEurope: "🏛️ G'arbiy, Shimoliy, Markaziy va Sharqiy Yevropa",
      tabBadgeJamid: "7 ta so'z shakli",
      tabBadgeHarf: "17 ta harf shakli",
      
      // Control Card
      step1Label: "1. So'z shaklini tanlang (turkum)",
      step1Placeholder: "So'z shaklini tanlang",
      step1OptionDhamir: "1. Olmoshlar (Zamir / Pronoun)",
      step1OptionMawshul: "2. Ismi mavsul (Bog'lovchilar)",
      step1OptionIstifham: "3. So'roq olmoshlari (Istifhom)",
      step1OptionSyarath: "4. Shart so'zlari (Shart)",
      step1OptionIsyarah: "5. Ko'rsatish olmoshlari (Ishora)",
      step1OptionIsimFiil: "6. Ismi fe'l (Ism Fe'l)",
      step1OptionFiilJamid: "7. Jomid fe'llar (O'zgarmas fe'llar)",
      step2Label: "2. So'z raqamini tanlang",
      step2Placeholder: "So'z raqamini tanlang",
      welcomeTitle: "Iltimos, so'z shakli va raqamini tanlang",
      welcomeSubtitle: "Arabcha matn, o'zbekcha tarjima, Qur'onda uchrash soni va dalil oyatlarni ko'rish uchun yuqoridagi menyudan so'z shaklini tanlang.",
      
      // Spotlight Card
      wordFormBadge: "So'z shakli",
      wordNoBadgePrefix: "So'z №:",
      arabicVoiceBtn: "Arabcha ovoz",
      arabicVoiceTooltip: "Arabcha talaffuzni eshitish (TTS)",
      meaningVoiceBtn: "Ma'no ovozi",
      meaningVoiceTooltip: "O'zbekcha ma'nosini eshitish (TTS)",
      copyArabicTooltip: "Arabcha so'zni nusxalash",
      copyInfoBtn: "Ma'lumotni nusxalash",
      copyInfoTooltip: "To'liq grammatik ma'lumotlarni nusxalash",
      freqLabel: "Qur'onda uchrashi",
      freqSub: "Jami uchrash soni",
      freqMuttashilVal: "Birikma shakli (Muttasil)",
      freqMuttashilSub: "Birikma olmosh sifatida",
      totalAyatLabel: "Jami dalil oyatlar",
      totalAyatSub: "Ma'lumotlar bazasida mavjud",
      sampleAyatSuffix: "Namunaviy oyatlar",
      transliterationPrefix: "Transliteratsiya:",
      meaningPrefix: "Ma'nosi:",
      
      // References Section
      referencesTitlePrefix: "Ushbu so'z qatnashgan Qur'on oyatlari:",
      ayatCountBadgePattern: (cur, total) => `${total} oyatdan ${cur}-si`,
      ayatCountZero: "0 Oyat",
      searchPlaceholder: "Sura nomi yoki oyat raqami bo'yicha qidirish...",
      exportCsvBtn: "CSV formatida yuklab olish",
      exportCsvTooltip: "Barcha dalil oyatlarni CSV fayliga yuklab olish",
      
      // Ayat Card
      surahPrefix: "Sura",
      surahPositionTag: (cur, surahNo, ayatNo) => `Sura #${surahNo} • Oyat #${ayatNo}`,
      playTranslationBtn: "Tarjimani tinglash",
      stopTranslationBtn: "Ovozni to'xtatish",
      playTilawahBtn: "Qiroatni tinglash",
      pauseTilawahBtn: "Vaqtincha to'xtatish",
      askAiBtn: "AI-dan so'rash",
      askAiTooltip: "Ushbu oyatning grammatikasi va tafsirini sun'iy intellektdan so'rash",
      aiModalTitle: "Qur'on bo'yicha sun'iy intellekt yordamchisi",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `${suratNama}:${ayat} surasi tahlili • "${kata}" so'zi (${noKata})`,
      aiTopicLabel: "Tahlil mavzusini tanlang:",
      aiPromptPreviewLabel: "Tayyorlangan AI so'rovi (Prompt):",
      aiTopicNahwu: "🔍 Arab tili grammatikasi (Nahv/Sarf) va E'rob",
      aiTopicTafsir: "📖 Tafsir va oyatning hikmatlari",
      aiTopicBalaghah: "✨ Balog'at va Qur'onning go'zalligi",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "So'rovni nusxalash",
      toastPromptCopied: "AI so'rovi xotiraga nusxalandi!",
      ayahPill: (n) => `${n}-oyat`,
      flipToArabicBtn: "Arabcha matn",
      flipToTranslationBtn: "Tarjimani ko'rsatish",
      translationBoxHeader: "O'zbekcha tarjima (Shayx Muhammad Sodiq)",
      
      // Pagination & Empty State
      emptyStateTitle: "Natijalar topilmadi",
      emptyStateText: "Qidiruv shartingizga mos keladigan sura yoki oyat topilmadi.",
      btnResetSearch: "Qidiruvni yangilash",
      paginationPrev: "Oldingi",
      paginationNext: "Keyingi",
      paginationInfo: (cur, total) => `${total} sahifadan ${cur}-si`,
      
      // Toasts
      toastLangChanged: "Til O'zbekchaga o'zgartirildi 🇺🇿",
      toastThemeChanged: (theme) => `Mavzu ${theme === 'dark' ? 'Tungi' : 'Kunduzgi'}ga o'zgartirildi`,
      toastTilawahPlaying: (suratNama, ayat) => `${suratNama}:${ayat} oyati qiroati yangramoqda (Mishariy Al-Afasiy)`,
      toastTilawahPaused: "Qiroat vaqtincha to'xtatildi.",
      toastTilawahEnded: "Qiroat yakunlandi.",
      toastAudioFailed: "Ovozni yangratishda xatolik yuz berdi.",
      toastTranslationStopped: "Tarjima ovozi to'xtatildi.",
      toastTtsNotSupported: "Brauzeringiz ovoz sintezini (TTS) qo'llab-quvvatlamaydi.",
      toastTranslationNotAvail: "Tarjima matni topilmadi.",
      toastSpeakingMeaning: (suratNama, ayat) => `${suratNama}:${ayat} oyati tarjimasi o'qilmoqda`,
      toastSpeakingArabic: (word) => `Arabcha talaffuz: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Ma'nosi: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `${suratNama}:${ayat} oyati o'qilmoqda`,
      toastArabicCopied: (word) => `Arabcha "${word}" so'zi nusxalandi!`,
      toastLatinCopied: "Transliteratsiya nusxalandi!",
      toastSummaryCopied: "So'z haqidagi to'liq ma'lumot nusxalandi!",
      toastCsvExported: (nk) => `${nk}-so'z uchun oyatlar CSV-ga yuklandi!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_uz || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_uz || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Ismi mavsul' : 'Shaxs olmoshi';
        return `${prefix} ${cleanWord}, ${latin}ma'nosi: ${arti}. ${desc ? 'Izoh: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
    ku: {
      pageTitle: "فەرهەنگی جامید مەبنی | وشە و ئایەتە کارلێککارەکانی قورئان",
      brandTitle: "فەرهەنگی <span>جامید مەبنی</span>",
      brandSubtitle: "فەرهەنگی کارلێککاری وشە نەگۆڕەکان و جێناوەکانی قورئانی پیرۆز",
      themeToggleTitle: "گۆڕینی ڕووکاری تاریک / ڕووناک",
      labelLangSelect: "زمانی وەرگێڕان و دەنگ:",
      translationSourceHtml: "وەرگێڕان: <strong>بورهان موحەممەد ئەمین (تەفسیری ئاسان)</strong>",
      optgroupEastAsia: "🌏 باشووری ڕۆژهەڵات و ڕۆژهەڵاتی ئاسیا",
      optgroupMidEast: "🕌 ڕۆژهەڵاتی ناوەڕاست، ئاسیای ناوەڕاست و قەوقاز",
      optgroupSouthAsia: "🪷 باشووری ئاسیا و زەریای هیندی",
      optgroupAfrica: "🌍 ئەفریقا",
      optgroupEurope: "🏛️ ئەورووپای ڕۆژاوا، باکوور، ناوەند و ڕۆژهەڵات",
      tabBadgeJamid: "٧ شێوازی وشە",
      tabBadgeHarf: "١٧ شێوازی پیت",
      
      // Control Card
      step1Label: "1. شێوازی وشە هەڵبژێرە (جۆر)",
      step1Placeholder: "شێوازی وشە هەڵبژێرە",
      step1OptionDhamir: "1. ڕەنگاڵە و جێناوەکان (زەمیر / Pronoun)",
      step1OptionMawshul: "2. ناوی مەوسوول (پەیوەندیی)",
      step1OptionIstifham: "3. ناوی پرسیار (ئیستیفھام)",
      step1OptionSyarath: "4. وشەی مەرج (شەرت)",
      step1OptionIsyarah: "5. ناوی ئاماژە (ئیشارە)",
      step1OptionIsimFiil: "6. ناوی کردار (ئیسم فیعل)",
      step1OptionFiilJamid: "7. کرداری نەگۆڕ (فیعل جامید)",
      step2Label: "2. ژمارەی وشە هەڵبژێرە",
      step2Placeholder: "ژمارەی وشە هەڵبژێرە",
      welcomeTitle: "تکایە شێواز و ژمارەی وشەیەک هەڵبژێرە",
      welcomeSubtitle: "بۆ بینینی دەقی عەرەبی، وەرگێڕانی کوردی، دووبارەبوونەوە لە قورئان و ئایەتە شاهیدەکان، لە سەرەوە جۆرێک دیاری بکە.",
      
      // Spotlight Card
      wordFormBadge: "شێوازی وشە",
      wordNoBadgePrefix: "وشەی ژمارە:",
      arabicVoiceBtn: "دەنگی عەرەبی",
      arabicVoiceTooltip: "گوێگرتن لە دەربڕینی عەرەبی (TTS)",
      meaningVoiceBtn: "دەنگی وەرگێڕان",
      meaningVoiceTooltip: "گوێگرتن لە واتای کوردی (TTS)",
      copyArabicTooltip: "لەبەرگرتنەوەی وشەی عەرەبی",
      copyInfoBtn: "لەبەرگرتنەوەی زانیاری",
      copyInfoTooltip: "لەبەرگرتنەوەی تەواوی زانیارییە ڕێزمانییەکان",
      freqLabel: "دووبارەبوونەوە لە قورئان",
      freqSub: "کۆی گشتیی هاتنەکان",
      freqMuttashilVal: "شێوازی لکاو (موتتەسیل)",
      freqMuttashilSub: "وەک جێناوی لکاو",
      totalAyatLabel: "کۆی ئایەتە شاهیدەکان",
      totalAyatSub: "لە بنکەدراوەدا هەیە",
      sampleAyatSuffix: "ئایەتە نموونەییەکان",
      transliterationPrefix: "تێپەڕنووسین:",
      meaningPrefix: "واتا:",
      
      // References Section
      referencesTitlePrefix: "ئایەتەکانی قورئان بۆ ئەم وشەیە:",
      ayatCountBadgePattern: (cur, total) => `ئایەتی ${cur} لە ${total}`,
      ayatCountZero: "0 ئایەت",
      searchPlaceholder: "گەڕان بەپێی ناوی سوورەت یان ژمارەی ئایەت...",
      exportCsvBtn: "هەناردەکردن بۆ CSV",
      exportCsvTooltip: "داگرتنی هەموو ئایەتە شاهیدەکان وەک پەڕگەی CSV",
      
      // Ayat Card
      surahPrefix: "سوورەتی",
      surahPositionTag: (cur, surahNo, ayatNo) => `سوورەتی #${surahNo} • ئایەتی #${ayatNo}`,
      playTranslationBtn: "لێدانی وەرگێڕان",
      stopTranslationBtn: "ڕاگرتنی دەنگ",
      playTilawahBtn: "لێدانی قورئانخوێندن",
      pauseTilawahBtn: "ڕاگرتنی کاتی",
      askAiBtn: "پرسیار لە AI",
      askAiTooltip: "پرسیارکردن لە بارەی ئیعراب و تەفسیری ئەم ئایەتە لە ژیریی دەستکرد",
      aiModalTitle: "یاریدەدەری ژیریی دەستکردی قورئانی",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `شیکاری سوورەتی ${suratNama}:${ayat} • وشەی "${kata}" (${noKata})`,
      aiTopicLabel: "بابەتی شیکاری دیاری بکە:",
      aiPromptPreviewLabel: "دەقی پرسیاری ئامادەکراو (Prompt):",
      aiTopicNahwu: "🔍 ڕێزمانی عەرەبی (نەحو/سەرف) و ئیعراب",
      aiTopicTafsir: "📖 تەفسیر و پەندەکانی ئایەت",
      aiTopicBalaghah: "✨ بەلاغەت و جوانکاریی قورئانی",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "لەبەرگرتنەوەی پرسیار",
      toastPromptCopied: "پرسیاری ژیریی دەستکرد لەبەرگیرایەوە!",
      ayahPill: (n) => `ئایەتی ${n}`,
      flipToArabicBtn: "دەقی عەرەبی",
      flipToTranslationBtn: "پیشاندانی وەرگێڕان",
      translationBoxHeader: "وەرگێڕانی کوردی (تەفسیری ئاسان)",
      
      // Pagination & Empty State
      emptyStateTitle: "هیچ ئەنجامێک نەدۆزرایەوە",
      emptyStateText: "هیچ سوورەت یان ئایەتێک لەگەڵ مەرجەکانی گەڕانەکەتدا یەکناگرێتەوە.",
      btnResetSearch: "نوێکردنەوەی گەڕان",
      paginationPrev: "پێشوو",
      paginationNext: "دواتر",
      paginationInfo: (cur, total) => `پەڕەی ${cur} لە ${total}`,
      
      // Toasts
      toastLangChanged: "زمان گۆڕدرا بۆ کوردی 🇮🇶",
      toastThemeChanged: (theme) => `ڕووکار گۆڕدرا بۆ ${theme === 'dark' ? 'تاریک' : 'ڕووناک'}`,
      toastTilawahPlaying: (suratNama, ayat) => `خوێندنەوەی سوورەتی ${suratNama}:${ayat} لێدەدرێت (میشاری ئەلعەفاسی)`,
      toastTilawahPaused: "خوێندنەوەکە ڕاگیرا.",
      toastTilawahEnded: "خوێندنەوەکە تەواو بوو.",
      toastAudioFailed: "هەڵەیەک لە لێدانی دەنگدا ڕوویدا.",
      toastTranslationStopped: "دەنگی وەرگێڕان ڕاگیرا.",
      toastTtsNotSupported: "وێبگەڕەکەت پشتگیری لە دروستکردنی دەنگ (TTS) ناکات.",
      toastTranslationNotAvail: "دەقی وەرگێڕان بەردەست نییە.",
      toastSpeakingMeaning: (suratNama, ayat) => `وەرگێڕانی سوورەتی ${suratNama}:${ayat} دەخوێندرێتەوە`,
      toastSpeakingArabic: (word) => `دەربڕینی عەرەبی: ${word}`,
      toastSpeakingWordMeaning: (arti) => `واتا: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `ئایەتی ${suratNama}:${ayat} دەخوێندرێتەوە`,
      toastArabicCopied: (word) => `وشەی عەرەبی "${word}" لەبەرگیرایەوە!`,
      toastLatinCopied: "تێپەڕنووسین لەبەرگیرایەوە!",
      toastSummaryCopied: "تەواوی زانیاریی وشەکە لەبەرگیرایەوە!",
      toastCsvExported: (nk) => `ئایەتەکانی وشەی ${nk} هەناردەی CSV کران!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\.\./g, '').replace(/\s*\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ku || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ku || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'ناوی مەوسوول' : 'جێناوی کەسی';
        return `${prefix} ${cleanWord}, ${latin}واتای: ${arti}. ${desc ? 'ڕوونکردنەوە: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }
  };

  // Helper for current i18n text
  function t(key, ...args) {
    const langDict = I18N[state.lang] || I18N.id;
    const val = langDict[key] !== undefined ? langDict[key] : (I18N.id[key] || key);
    if (typeof val === 'function') {
      return val(...args);
    }
    return val;
  }

  // Musytaq I18N Dictionary & Helper
  const MUSYTAQ_I18N = {
    tabTitle: { id: "Kamus Musytaq", en: "Musytaq Dictionary", tr: "Müştak Sözlüğü" },
    tabBadge: { id: "80 Akar Kata & Tasrif", en: "80 Roots & Tasrif", tr: "80 Kök & Tasrif" },
    metricRootTitle: { id: "Akar Kata Terpilih", en: "Selected Root", tr: "Seçilen Kök" },
    metricFreqTitle: { id: "Frekuensi di Al-Qur'an", en: "Quran Frequency", tr: "Kur'an Frekansı" },
    metricFreqSub: { id: "Total kemunculan kata turunan", en: "Total derived occurrences", tr: "Toplam türemiş kelime sayısı" },
    metricTasrifTitle: { id: "Total Bentuk Tasrif", en: "Total Conjugations", tr: "Toplam Tasrif Şekli" },
    metricTasrifSub: { id: "Bentuk kata turunan aktif", en: "Active derived forms", tr: "Aktif türetilmiş formlar" },
    morphologyTitle: { id: "Analisis Morfologi & Sharaf", en: "Morphology & Sarf Analysis", tr: "Morfoloji ve Sarf Analizi" },
    wazanTitle: { id: "Wazan & Pola Morfologi", en: "Wazan & Morphological Pattern", tr: "Vezin ve Kalıp" },
    asalTitle: { id: "Bentuk Dasar & Asal Kata", en: "Base Form & Origin", tr: "Asıl ve Kök Form" },
    babTitle: { id: "Bab Tasrif & Vokalisasi", en: "Conjugation Bab & Vocalization", tr: "Tasrif Babı" },
    grammarTitle: { id: "Peran Gramatikal & Kategori", en: "Grammatical Role & Category", tr: "Gramer Rolü ve Kategori" },
    ilalTitle: { id: "Kaidah I'lal & Perubahan Huruf", en: "I'lal Rules & Phonetic Shift", tr: "İ'lâl Kuralları" },
    chipAll: { id: "Semua Bentuk", en: "All Forms", tr: "Tüm Formlar" },
    chipMadhi: { id: "Fi'il Madhi", en: "Past (Madhi)", tr: "Geçmiş Zaman (Mâzî)" },
    chipMudhari: { id: "Fi'il Mudhari'", en: "Present (Mudhari')", tr: "Geniş/Şimdiki Zaman (Muzâri)" },
    chipAmr: { id: "Fi'il Amr", en: "Imperative (Amr)", tr: "Emir Kipi (Emir)" },
    chipMasdar: { id: "Masdar", en: "Verbal Noun (Masdar)", tr: "Mastarlar" },
    chipIsim: { id: "Isim Fa'il / Maf'ul", en: "Participle / Noun", tr: "İsm-i Fâil / Mef'ûl" },
    searchPlaceholder: { id: "Cari bentuk kata, wazan, arti, atau ayat...", en: "Search form, pattern, meaning, or verse...", tr: "Form, vezin, anlam veya ayet ara..." },
    emptyStateText: { id: "Tidak ada bentuk tasrif yang cocok dengan pencarian.", en: "No conjugations match your search.", tr: "Aramanızla eşleşen tasrif bulunamadı." },
    levelUnit: { id: "Akar Kata", en: "Roots", tr: "Kök" },
    akarSelectPlaceholder: { id: "Pilih Nomor Akar & Akar", en: "Select Root Number & Root", tr: "Kök Numarası ve Kök Seçin" },
    tasrifUnit: { id: "Bentuk", en: "Forms", tr: "Form" },
    tasrifSelectPlaceholder: { id: "Pilih Tasrif", en: "Select Conjugation", tr: "Tasrif Seçin" },
    rootMeaningPrefix: { id: "Arti Akar", en: "Root Meaning", tr: "Kök Anlamı" },
    tasrifTableTitlePrefix: { id: "Daftar Lengkap Seluruh Bentuk Tasrif Akar", en: "Complete List of Conjugations for Root", tr: "Kökün Tüm Tasrif Tablosu" },
    selectHint: { id: "Pilih ➔", en: "Select ➔", tr: "Seç ➔" }
  };

  function getMusytaqI18n(key) {
    const lang = state.lang || 'id';
    const item = MUSYTAQ_I18N[key];
    if (!item) return '';
    return item[lang] || item['en'] || item['id'] || '';
  }

  // DOM Elements Cache
  const elements = {
    docTitle: document.getElementById('docTitle'),
    brandTitle: document.getElementById('brandTitle'),
    brandSubtitle: document.getElementById('brandSubtitle'),
    labelLangSelect: document.getElementById('labelLangSelect'),
    langSelect: document.getElementById('langSelect'),
    translationSourceText: document.getElementById('translationSourceText'),
    themeToggleBtn: document.getElementById('themeToggleBtn'),
    themeIcon: document.getElementById('themeIcon'),
    
    // Tabs
    tabDictJamid: document.getElementById('tabDictJamid'),
    tabDictHarf: document.getElementById('tabDictHarf'),
    tabDictHarfAmil: document.getElementById('tabDictHarfAmil'),
    tabDictMusytaq: document.getElementById('tabDictMusytaq'),
    labelTabJamid: document.getElementById('labelTabJamid'),
    badgeTabJamid: document.getElementById('badgeTabJamid'),
    labelTabHarf: document.getElementById('labelTabHarf'),
    badgeTabHarf: document.getElementById('badgeTabHarf'),
    labelTabHarfAmil: document.getElementById('labelTabHarfAmil'),
    badgeTabHarfAmil: document.getElementById('badgeTabHarfAmil'),
    labelTabMusytaq: document.getElementById('labelTabMusytaq'),
    badgeTabMusytaq: document.getElementById('badgeTabMusytaq'),
    
    // Controls Grids
    standardDropdownGrid: document.getElementById('standardDropdownGrid'),
    musytaqDropdownGrid: document.getElementById('musytaqDropdownGrid'),
    bentukKataSelect: document.getElementById('bentukKataSelect'),
    noKataSelect: document.getElementById('noKataSelect'),
    musytaqLevelSelect: document.getElementById('musytaqLevelSelect'),
    musytaqAkarSelect: document.getElementById('musytaqAkarSelect'),
    musytaqTasrifSelect: document.getElementById('musytaqTasrifSelect'),
    
    // Musytaq Display Elements
    musytaqDisplaySection: document.getElementById('musytaqDisplaySection'),
    musytaqBadgeLevel: document.getElementById('musytaqBadgeLevel'),
    musytaqBadgeAkar: document.getElementById('musytaqBadgeAkar'),
    musytaqBadgeTasrifCode: document.getElementById('musytaqBadgeTasrifCode'),
    musytaqBadgeKategori: document.getElementById('musytaqBadgeKategori'),
    musytaqArabicWord: document.getElementById('musytaqArabicWord'),
    btnMusytaqAudio: document.getElementById('btnMusytaqAudio'),
    musytaqWordMeaning: document.getElementById('musytaqWordMeaning'),
    musytaqWordSub: document.getElementById('musytaqWordSub'),
    musytaqRootMeaning: document.getElementById('musytaqRootMeaning'),
    musytaqRootDisplay: document.getElementById('musytaqRootDisplay'),
    musytaqFreqDisplay: document.getElementById('musytaqFreqDisplay'),
    musytaqTotalTasrifBadge: document.getElementById('musytaqTotalTasrifBadge'),
    musytaqWazanDisplay: document.getElementById('musytaqWazanDisplay'),
    musytaqAsalContainer: document.getElementById('musytaqAsalContainer'),
    musytaqAsalDisplay: document.getElementById('musytaqAsalDisplay'),
    musytaqBabDisplay: document.getElementById('musytaqBabDisplay'),
    musytaqGrammarDetailDisplay: document.getElementById('musytaqGrammarDetailDisplay'),
    musytaqIlalContainer: document.getElementById('musytaqIlalContainer'),
    musytaqIlalText: document.getElementById('musytaqIlalText'),
    musytaqTasrifTableTitle: document.getElementById('musytaqTasrifTableTitle'),
    musytaqSearchInput: document.getElementById('musytaqSearchInput'),
    musytaqCategoryChips: document.getElementById('musytaqCategoryChips'),
    musytaqTasrifGrid: document.getElementById('musytaqTasrifGrid'),
    musytaqEmptyState: document.getElementById('musytaqEmptyState'),
    btnMusytaqAiAsk: document.getElementById('btnMusytaqAiAsk'),
    
    // Spotlight Card
    spotlightCard: document.getElementById('spotlightCard'),
    badgeBentukKata: document.getElementById('badgeBentukKata'),
    badgeNoKata: document.getElementById('badgeNoKata'),
    badgeJenis: document.getElementById('badgeJenis'),
    arabicWordDisplay: document.getElementById('arabicWordDisplay'),
    wordLatinDisplay: document.getElementById('wordLatinDisplay'),
    wordMeaningDisplay: document.getElementById('wordMeaningDisplay'),
    wordMeaningSub: document.getElementById('wordMeaningSub'),
    labelFreqTitle: document.getElementById('labelFreqTitle'),
    frekSubtitle: document.getElementById('frekSubtitle'),
    frekValueDisplay: document.getElementById('frekValueDisplay'),
    labelTotalAyatTitle: document.getElementById('labelTotalAyatTitle'),
    labelTotalAyatSub: document.getElementById('labelTotalAyatSub'),
    totalAyatBadge: document.getElementById('totalAyatBadge'),
    
    // Spotlight Actions
    btnAudioPlay: document.getElementById('btnAudioPlay'),
    labelAudioArab: document.getElementById('labelAudioArab'),
    btnAudioMeaning: document.getElementById('btnAudioMeaning'),
    labelAudioMeaning: document.getElementById('labelAudioMeaning'),
    btnCopyArabic: document.getElementById('btnCopyArabic'),
    btnCopyAll: document.getElementById('btnCopyAll'),
    
    // References Section
    referencesSection: document.getElementById('referencesSection'),
    ayatSectionTitle: document.getElementById('ayatSectionTitle'),
    ayatSearchInput: document.getElementById('ayatSearchInput'),
    btnExportCsv: document.getElementById('btnExportCsv'),
    labelExportCsv: document.getElementById('labelExportCsv'),
    ayatGridContainer: document.getElementById('ayatGridContainer'),
    emptyStateContainer: document.getElementById('emptyStateContainer'),
    emptyStateText: document.getElementById('emptyStateText'),
    
    // AI Modal
    aiModal: document.getElementById('aiModal'),
    aiModalTitle: document.getElementById('aiModalTitle'),
    aiModalSubtitle: document.getElementById('aiModalSubtitle'),
    aiModalCloseBtn: document.getElementById('aiModalCloseBtn'),
    aiModalArabicVerse: document.getElementById('aiModalArabicVerse'),
    aiModalTranslation: document.getElementById('aiModalTranslation'),
    labelAiTopic: document.getElementById('labelAiTopic'),
    aiTopicChips: document.getElementById('aiTopicChips'),
    labelPromptPreview: document.getElementById('labelPromptPreview'),
    aiPromptTextarea: document.getElementById('aiPromptTextarea'),
    btnOpenGemini: document.getElementById('btnOpenGemini'),
    labelOpenGemini: document.getElementById('labelOpenGemini'),
    btnOpenChatGpt: document.getElementById('btnOpenChatGpt'),
    labelOpenChatGpt: document.getElementById('labelOpenChatGpt'),
    btnCopyPrompt: document.getElementById('btnCopyPrompt'),
    labelCopyPrompt: document.getElementById('labelCopyPrompt'),
    
    // Toast
    toastNotification: document.getElementById('toastNotification')
  };

  // Preferred Sorting Orders for Jamid Mabny categories
  const PREFERRED_NO_KATA_ORDER = {
    '1. Dhamir': [
      '1a', '1b', '1c', '2a', '2b', '3a', '3b', '3c',
      '4a', '4b', '5a', '5b', '6a', '6b', '6c', '7a',
      '7b', '8a', '8b', '8c', '9a', '9b', '9c', '10a',
      '10b', '11a', '11b', '11c', '12a', '12b', '12c'
    ]
  };

  // Group Storage
  let groups = {};
  let availableBentukKatas = [];
  let noKatasByBentuk = {};

  // Audio Playback State
  let currentAudio = null;
  let currentAudioBtn = null;
  let activeUtterance = null;
  let currentPlayingAyatKey = null;
  let currentCloudAudio = null;
  let cloudAudioQueue = [];
  let cachedVoices = [];

  // AI Modal Context
  let currentAiContext = {
    surat: 1,
    ayat: 1,
    kata: '',
    noKata: '',
    bentuk: '',
    suratNama: '',
    teksArab: '',
    teksArti: '',
    grammarDesc: '',
    topic: 'nahwu'
  };

  // Group key helper
  function getGroupKey(bentuk, noKata) {
    return `${bentuk}__${noKata}`;
  }

  function getGroup(bentuk, noKata) {
    return groups[getGroupKey(bentuk, noKata)] || null;
  }

  // Multi-language Property Helpers
  function getGroupArti(group, lang) {
    if (!group) return '';
    const l = lang || state.lang;
    return group['arti_' + l] || group.arti_id || group.arti || '';
  }

  function getGroupBentuk(group, lang) {
    if (!group) return '';
    const l = lang || state.lang;
    return group['bentuk_' + l] || group.bentuk_id || group.bentuk || '';
  }

  function getGroupDesc(group, lang) {
    if (!group) return '';
    const l = lang || state.lang;
    const g = group.grammar || {};
    return g['desc_' + l] || g.desc_id || g.keterangan || '';
  }

  function getGroupJenis(group, lang) {
    if (!group) return '';
    const l = lang || state.lang;
    const g = group.grammar || {};
    return g['jenis_' + l] || g.jenis_id || g.jenis || getDefaultJenis(group.bentuk, l);
  }

  function getOccSuratArti(occ, lang) {
    if (!occ) return '';
    const l = (lang || state.lang).toUpperCase();
    return occ['suratArti' + l] || occ['SuratArti' + l] || occ.suratArtiEN || occ.SuratArtiEN || occ.suratArtiID || occ.SuratArtiID || occ.suratArti || occ.SuratArti || '';
  }

  function getOccTeksArti(occ, lang) {
    if (!occ) return '';
    const l = (lang || state.lang).toUpperCase();
    return occ['teksArti' + l] || occ['TeksArti' + l] || occ.teksArtiEN || occ.TeksArtiEN || occ.teksArtiID || occ.TeksArtiID || occ.teksArti || occ.TeksArti || '';
  }

  // Switch Active Dictionary ('jamid' | 'harf' | 'harf_amil' | 'musytaq')
  function switchDictionary(dictKey) {
    state.activeDict = dictKey;
    localStorage.setItem('dhamir_active_dict', dictKey);

    const tabs = [
      { el: elements.tabDictJamid, key: 'jamid' },
      { el: elements.tabDictHarf, key: 'harf' },
      { el: elements.tabDictHarfAmil, key: 'harf_amil' },
      { el: elements.tabDictMusytaq, key: 'musytaq' }
    ];

    tabs.forEach(tab => {
      if (tab.el) {
        if (tab.key === dictKey) {
          tab.el.classList.add('active');
          tab.el.setAttribute('aria-selected', 'true');
        } else {
          tab.el.classList.remove('active');
          tab.el.setAttribute('aria-selected', 'false');
        }
      }
    });

    updateHeaderTitles();

    if (dictKey === 'musytaq') {
      if (elements.standardDropdownGrid) elements.standardDropdownGrid.style.display = 'none';
      if (elements.musytaqDropdownGrid) elements.musytaqDropdownGrid.style.display = 'grid';
      if (elements.spotlightCard) elements.spotlightCard.style.display = 'none';
      if (elements.referencesSection) elements.referencesSection.style.display = 'none';
      if (elements.musytaqDisplaySection) elements.musytaqDisplaySection.style.display = 'block';

      populateMusytaqLevelDropdown();
      populateMusytaqAkarDropdown();
      populateMusytaqTasrifDropdown();
      renderMusytaqSpotlight();
      renderMusytaqTasrifGrid();
    } else {
      if (elements.standardDropdownGrid) elements.standardDropdownGrid.style.display = 'grid';
      if (elements.musytaqDropdownGrid) elements.musytaqDropdownGrid.style.display = 'none';
      if (elements.musytaqDisplaySection) elements.musytaqDisplaySection.style.display = 'none';

      initData();
      populateBentukDropdown();
      
      if (availableBentukKatas.length > 0) {
        selectBentuk(availableBentukKatas[0]);
      } else {
        selectBentuk('');
      }
    }
  }

  // Update Header Titles based on active dictionary

  function updateHeaderTitles() {
    if (!elements.brandTitle) return;
    if (state.activeDict === 'musytaq') {
      if (state.lang === 'en') {
        elements.brandTitle.innerHTML = 'Dictionary of <span>Derived Words</span> (Musytaq)';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'Interactive Quranic Roots, Morphology, Conjugation & I\'lal Rules (80 Roots · 3,012 Forms)';
        if (elements.docTitle) elements.docTitle.textContent = 'Musytaq Dictionary | Quranic Morphology & Root Conjugation';
      } else if (state.lang === 'ms') {
        elements.brandTitle.innerHTML = 'Kamus <span>Kata Musytaq</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'Kamus Interaktif 80 Akar Kata, Morfologi, Wazan & Kaedah I\'lal Al-Quran (3.012 Tasrif)';
        if (elements.docTitle) elements.docTitle.textContent = 'Kamus Musytaq | Morfologi & Tasrif Al-Quran';
      } else if (state.lang === 'fr') {
        elements.brandTitle.innerHTML = 'Dictionnaire des <span>Mots Dérivés</span> (Mushtaq)';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'Dictionnaire interactif de 80 racines, morphologie et règles d\'I\'lal du Coran';
        if (elements.docTitle) elements.docTitle.textContent = 'Dictionnaire Mushtaq | Morphologie Coranique';
      } else if (state.lang === 'de') {
        elements.brandTitle.innerHTML = 'Wörterbuch der <span>abgeleiteten Wörter</span> (Muschtaq)';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'Interaktives Wörterbuch für 80 Wurzeln, Konjugation und I\'lal-Regeln des Korans';
        if (elements.docTitle) elements.docTitle.textContent = 'Muschtaq Wörterbuch | Koranische Morphologie';
      } else if (state.lang === 'tr') {
        elements.brandTitle.innerHTML = 'Kur\'an <span>Müştak Kelimeler</span> Sözlüğü';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'İnteraktif 80 Kök Harf, Morfoloji, Vezin ve İ\'lâl Kuralları Rehberi (3.012 Tasrif)';
        if (elements.docTitle) elements.docTitle.textContent = 'Müştak Kelimeler Sözlüğü | Kur\'an Morfolojisi';
      } else if (state.lang === 'ur') {
        elements.brandTitle.innerHTML = 'لغت <span>کلمات مشتقہ</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'قرآن کریم کی ۸۰ بنیادی جڑوں، صرفی اوزان اور قواعد اعلال کی تعاملی لغت (۳،۰۱۲ تصاریف)';
        if (elements.docTitle) elements.docTitle.textContent = 'لغت مشتقات | قرآنی صرف و تصریف';
      } else if (state.lang === 'ar' || state.lang === 'fa') {
        elements.brandTitle.innerHTML = 'فرهنگ <span>کلمات مشتق</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'لغت‌نامه تعاملی ۸۰ ریشه اصلی، اوزان صرفی و قواعد اعلال قرآن کریم';
        if (elements.docTitle) elements.docTitle.textContent = 'فرهنگ مشتقات | صرف و اشتقاق قرآن';
      } else {
        elements.brandTitle.innerHTML = 'Kamus <span>Musytaq</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'Kamus Interaktif 80 Akar Kata, Morfologi, Wazan & Kaidah I\'lal Al-Qur\'an (3.012 Tasrif)';
        if (elements.docTitle) elements.docTitle.textContent = 'Kamus Musytaq | Morfologi, Wazan & Tasrif Al-Qur\'an';
      }
      return;
    }

    
    if (state.activeDict === 'harf_amil') {
      if (state.lang === 'ja') {
        elements.brandTitle.innerHTML = 'ハルフ・アーミル <span>辞書</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'クルアーン作用不変化詞インタラクティブ辞典 (6分類・54語)';
        if (elements.docTitle) elements.docTitle.textContent = 'ハルフ・アーミル辞書 | クルアーン不変化詞インタラクティブリファレンス';
      } else if (state.lang === 'ko') {
        elements.brandTitle.innerHTML = '하르프 아밀 <span>사전</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = '꾸란 지배 불변사 상호작용 사전 (6개 범주 · 54개 단어)';
        if (elements.docTitle) elements.docTitle.textContent = '하르프 아밀 사전 | 꾸란 불변사 참조';
      } else if (state.lang === 'fa') {
        elements.brandTitle.innerHTML = 'فرهنگ <span>حروف عامل</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'لغت‌نامه تعاملی ۶ دسته و ۵۴ حرف عامل قرآن کریم';
        if (elements.docTitle) elements.docTitle.textContent = 'فرهنگ حروف عامل | مراجع تعاملی حروف قرآن';
      } else if (state.lang === 'sw') {
        elements.brandTitle.innerHTML = "Kamusi ya <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Kamusi Shirikishi ya Herufi 54 Zenye Athari za Kisarufi Katika Qur'ani";
        if (elements.docTitle) elements.docTitle.textContent = "Kamusi ya Harf 'Amil | Qur'ani Tukufu";
      } else if (state.lang === 'ha') {
        elements.brandTitle.innerHTML = "Ƙamus ɗin <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Ƙamus Mai Ma'amala don Haruffa 54 Masu Canza Irabi a Al-Ƙur'ani";
        if (elements.docTitle) elements.docTitle.textContent = "Ƙamus ɗin Harf 'Amil | Al-Ƙur'ani";
      } else if (state.lang === 'pt') {
        elements.brandTitle.innerHTML = "Dicionário de <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Dicionário Interativo de 6 Formas e 54 Partículas Operativas do Alcorão";
        if (elements.docTitle) elements.docTitle.textContent = "Dicionário de Harf 'Amil | Alcorão";
      } else if (state.lang === 'tr') {
        elements.brandTitle.innerHTML = "Kur'an <span>Âmil Harfler</span> Sözlüğü";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "İnteraktif 6 Kategori ve 54 Âmil Harf Rehberi";
        if (elements.docTitle) elements.docTitle.textContent = "Âmil Harfler Sözlüğü | Kur'an-ı Kerim";
      } else if (state.lang === 'nl') {
        elements.brandTitle.innerHTML = "Woordenboek <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interactief Woordenboek voor 6 Vormen en 54 Werkzame Partikels van de Koran";
        if (elements.docTitle) elements.docTitle.textContent = "Woordenboek Harf 'Amil | Referentie van Koranpartikels";
      } else if (state.lang === 'it') {
        elements.brandTitle.innerHTML = "Dizionario di <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Dizionario Interattivo di 6 Forme e 54 Particelle Operative del Corano";
        if (elements.docTitle) elements.docTitle.textContent = "Dizionario di Harf 'Amil | Riferimenti Coranici";
      } else if (state.lang === 'bs') {
        elements.brandTitle.innerHTML = "Rječnik <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktivni rječnik za 6 oblika i 54 operativne čestice u Kur'anu";
        if (elements.docTitle) elements.docTitle.textContent = "Rječnik Harf 'Amil | Kur'anske čestice";
      } else if (state.lang === 'ber') {
        elements.brandTitle.innerHTML = "Asegzawal <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Asegzawal n 6 n talɣiwin d 54 n tseddariyin n Leqran";
        if (elements.docTitle) elements.docTitle.textContent = "Asegzawal Harf 'Amil | Leqran";
      } else if (state.lang === 'az') {
        elements.brandTitle.innerHTML = "Lüğət <span>Hərfi Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Qurani-Kərimdə 6 kateqoriya və 54 amil hərfin izahlı lüğəti";
        if (elements.docTitle) elements.docTitle.textContent = "Hərfi Amil Lüğəti | Qurani-Kərim";
      } else if (state.lang === 'bg') {
        elements.brandTitle.innerHTML = "Речник <span>Харф Амил</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Интерактивен речник за 6 форми и 54 управляващи частици в Корана";
        if (elements.docTitle) elements.docTitle.textContent = "Речник Харф Амил | Свещеният Коран";
      } else if (state.lang === 'am') {
        elements.brandTitle.innerHTML = "የ<span>ሐርፈ ዓሚል</span> መዝገበ-ቃላት";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "በቁርኣን ውስጥ የ6 ቅርጾችና የ54 ሰሪ ቅንጣቶች መመሪያ";
        if (elements.docTitle) elements.docTitle.textContent = "የሐርፈ ዓሚል መዝገበ-ቃላት | ቅዱስ ቁርኣን";
      } else if (state.lang === 'cs') {
        elements.brandTitle.innerHTML = "Slovník <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktivní slovník pro 6 forem a 54 řídících částic v Koránu";
        if (elements.docTitle) elements.docTitle.textContent = "Slovník Harf 'Amil | Svatý Korán";
      } else if (state.lang === 'dv') {
        elements.brandTitle.innerHTML = "ރަދީފު <span>ޙަރްފު ޢާމިލް</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "ކީރިތި ޤުރްއާނުގެ 6 ބާވަތާއި 54 ޢާމިލް އަކުރުގެ ރަދީފު";
        if (elements.docTitle) elements.docTitle.textContent = "ޙަރްފު ޢާމިލް ރަދީފު | ކީރިތި ޤުރްއާން";
      } else if (state.lang === 'no') {
        elements.brandTitle.innerHTML = "Ordbok <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktiv ordbok for 6 former og 54 styrende partikler i Koranen";
        if (elements.docTitle) elements.docTitle.textContent = "Ordbok Harf 'Amil | Den Hellige Koranen";
      } else if (state.lang === 'pl') {
        elements.brandTitle.innerHTML = "Słownik <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktywny słownik 6 form i 54 zarządzających partykuł w Koranie";
        if (elements.docTitle) elements.docTitle.textContent = "Słownik Harf 'Amil | Święty Koran";
      } else if (state.lang === 'ro') {
        elements.brandTitle.innerHTML = "Dicționar <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Dicționar interactiv pentru 6 forme și 54 de particule operative din Coran";
        if (elements.docTitle) elements.docTitle.textContent = "Dicționar Harf 'Amil | Coranul cel Sfânt";
      } else if (state.lang === 'sv') {
        elements.brandTitle.innerHTML = "Ordbok <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktiv ordbok för 6 former och 54 styrande partiklar i Koranen";
        if (elements.docTitle) elements.docTitle.textContent = "Ordbok Harf 'Amil | Den Heliga Koranen";
      } else if (state.lang === 'tg') {
        elements.brandTitle.innerHTML = "Луғати <span>Ҳарфҳои Омил</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Луғати интерактивии 6 гурӯҳ ва 54 ҳарфи омил дар Қуръон";
        if (elements.docTitle) elements.docTitle.textContent = "Луғати Ҳарфҳои Омил | Қуръони Карим";
      } else if (state.lang === 'ta') {
        elements.brandTitle.innerHTML = "அகராதி <span>ஹர்ஃப் ஆமில்</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "திருக்குர்ஆனின் 6 வகைகள் மற்றும் 54 செயல்படும் இடைச்சொற்களின் அகராதி";
        if (elements.docTitle) elements.docTitle.textContent = "ஹர்ஃப் ஆமில் அகராதி | புனித குர்ஆன்";
      } else if (state.lang === 'tt') {
        elements.brandTitle.innerHTML = "Сүзлек <span>Гамил Хәрефләр</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Коръәни Кәримнең 6 төре һәм 54 гамил кисәкчәсе сүзлеге";
        if (elements.docTitle) elements.docTitle.textContent = "Гамил Хәрефләр сүзлеге | Коръәни Кәрим";
      } else if (state.lang === 'ug') {
        elements.brandTitle.innerHTML = "لۇغەت <span>ئامىل ھەرپلەر</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "قۇرئاندىكى 6 تۈر ۋە 54 تەسىرلىك يۈكلىمىنىڭ لۇغىتى";
        if (elements.docTitle) elements.docTitle.textContent = "ئامىل ھەرپلەر لۇغىتى | قۇرئانى كەرىم";
      } else if (state.lang === 'uz') {
        elements.brandTitle.innerHTML = "Lug'at <span>Omil Harflar</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Qur'ondagi 6 tur va 54 ta amalli yuklamalar lug'ati";
        if (elements.docTitle) elements.docTitle.textContent = "Omil Harflar lug'ati | Qur'oni Karim";
      } else if (state.lang === 'ku') {
        elements.brandTitle.innerHTML = "فەرهەنگی <span>پیتە کارلێکەرەکان</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "فەرهەنگی 6 جۆر و 54 پیت و ئامرازی کارلێکەر لە قورئاندا";
        if (elements.docTitle) elements.docTitle.textContent = "فەرهەنگی پیتە کارلێکەرەکان | قورئانی پیرۆز";
      } else if (state.lang === 'th') {
        elements.brandTitle.innerHTML = "พจนานุกรม <span>ฮัรฟ์อามิล</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "พจนานุกรมคำศัพท์ 6 รูปแบบและ 54 ตัวอักษรออกฤทธิ์ในอัลกุรอาน";
        if (elements.docTitle) elements.docTitle.textContent = "พจนานุกรมฮัรฟ์อามิล | อายะฮ์อ้างอิงอัลกุรอาน";
      } else if (state.lang === 'sq') {
        elements.brandTitle.innerHTML = "Fjalori i <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Fjalor interaktiv për 6 forma dhe 54 pjesëza vepruese kur'anore";
        if (elements.docTitle) elements.docTitle.textContent = "Fjalori i Harf 'Amil | Pjesëzat kur'anore";
      } else if (state.lang === 'en') {
        elements.brandTitle.innerHTML = "Dictionary of <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interactive Dictionary of 6 Forms & 54 Operative Quranic Particles";
        if (elements.docTitle) elements.docTitle.textContent = "Dictionary of Harf 'Amil | Quranic Particles";
      } else if (state.lang === 'ur') {
        elements.brandTitle.innerHTML = "لغت <span>حروف عاملہ</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "قرآن کریم کے ۶ اشکال اور ۵۴ حروف عاملہ کی تعاملی لغت";
        if (elements.docTitle) elements.docTitle.textContent = "لغت حروف عاملہ | قرآن کریم کے حروف";
      } else if (state.lang === 'hi') {
        elements.brandTitle.innerHTML = "शब्दकोश <span>हर्फ़ 'आमिल</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "कुरआन के ६ रूपों और ५४ प्रभावी अव्यय शब्दों का संваदात्मक शब्दकोश";
        if (elements.docTitle) elements.docTitle.textContent = "हर्फ़ 'आमिल शब्दकोश | पवित्र कुरआन";
      } else if (state.lang === 'bn') {
        elements.brandTitle.innerHTML = "অভিধান <span>হরূফে আমেল</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "কুরআনের ৬টি রূপ ও ৫৪টি আমলকারী হরফের ইন্টারঅ্যাক্টিভ অভিধান";
        if (elements.docTitle) elements.docTitle.textContent = "হরূফে আমেল অভিধান | পবিত্র কুরআন";
      } else if (state.lang === 'ru') {
        elements.brandTitle.innerHTML = "Словарь <span>Харф Амиль</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Интерактивный словарь 6 форм и 54 управляющих частиц Корана";
        if (elements.docTitle) elements.docTitle.textContent = "Словарь Харф Амиль | Священный Коран";
      } else if (state.lang === 'zh') {
        elements.brandTitle.innerHTML = "<span>作用虚词</span> 词典 (Harf 'Amil)";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "《古兰经》6种形态与54个具语法作用虚词互动词典";
        if (elements.docTitle) elements.docTitle.textContent = "作用虚词词典 | 古兰经互动参考";
      } else if (state.lang === 'fr') {
        elements.brandTitle.innerHTML = "Dictionnaire de <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Dictionnaire Interactif de 6 Formes et 54 Particules Régissantes du Coran";
        if (elements.docTitle) elements.docTitle.textContent = "Dictionnaire de Harf 'Amil | Particules Régissantes du Coran";
      } else if (state.lang === 'de') {
        elements.brandTitle.innerHTML = "Wörterbuch <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktives Wörterbuch für 6 Formen und 54 regierende Partikeln des Korans";
        if (elements.docTitle) elements.docTitle.textContent = "Wörterbuch Harf 'Amil | Koranpartikeln";
      } else if (state.lang === 'es') {
        elements.brandTitle.innerHTML = "Diccionario de <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Diccionario Interactivo de 6 Formas y 54 Partículas Operativas del Corán";
        if (elements.docTitle) elements.docTitle.textContent = "Diccionario de Harf 'Amil | Partículas del Corán";
      } else {
        elements.brandTitle.innerHTML = "Kamus <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Kamus Interaktif 6 Bentuk Harf & 54 Kata Al-Qur'an";
        if (elements.docTitle) elements.docTitle.textContent = "Kamus Harf 'Amil | Rujukan Ayat Interaktif Al-Qur'an";
      }
    } else if (state.activeDict === 'harf') {
      if (state.lang === 'ja') {
        elements.brandTitle.innerHTML = 'ハルフ・ガイ・アーミル <span>辞書</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'クルアーン非作用不変化詞インタラクティブ辞典';
        if (elements.docTitle) elements.docTitle.textContent = 'ハルフ・ガイ・アーミル辞書 | クルアーン不変化詞インタラクティブリファレンス';
      } else if (state.lang === 'ko') {
        elements.brandTitle.innerHTML = '하르프 가이르 아밀 <span>사전</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = '꾸란 비지배 불변사 상호작용 사전';
        if (elements.docTitle) elements.docTitle.textContent = '하르프 가이르 아밀 사전 | 꾸란 불변사 참조';
      } else if (state.lang === 'fa') {
        elements.brandTitle.innerHTML = 'فرهنگ <span>حرف غیرعامل</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'لغت‌نامه تعاملی حروف غیرعامل قرآن کریم';
        if (elements.docTitle) elements.docTitle.textContent = 'فرهنگ حرف غیرعامل | مراجع تعاملی حروف قرآن';
      } else if (state.lang === 'sw') {
        elements.brandTitle.innerHTML = "Kamusi ya <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Kamusi Shirikishi ya Herufi Zisizo na Athari za Kisarufi";
        if (elements.docTitle) elements.docTitle.textContent = "Kamusi ya Harf Ghair 'Amil | Qur'ani Tukufu";
      } else if (state.lang === 'ha') {
        elements.brandTitle.innerHTML = "Ƙamus ɗin <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Ƙamus Mai Ma'amala don Haruffan da Ba Sa Canza Irabi";
        if (elements.docTitle) elements.docTitle.textContent = "Ƙamus ɗin Harf Ghair 'Amil | Al-Ƙur'ani";
      } else if (state.lang === 'pt') {
        elements.brandTitle.innerHTML = "Dicionário de <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Dicionário Interativo de Partículas Inoperantes do Alcorão";
        if (elements.docTitle) elements.docTitle.textContent = "Dicionário de Harf Ghair 'Amil | Alcorão";
      } else if (state.lang === 'tr') {
        elements.brandTitle.innerHTML = "Kur'an <span>Gayr-i Âmil Harfler</span> Sözlüğü";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "İnteraktif Gayr-i Âmil Harf ve Kelime Numarası Rehberi";
        if (elements.docTitle) elements.docTitle.textContent = "Gayr-i Âmil Harfler Sözlüğü | Kur'an-ı Kerim";
      } else if (state.lang === 'nl') {
        elements.brandTitle.innerHTML = "Woordenboek <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interactief Woordenboek voor Niet-werkzame Partikels van de Koran";
        if (elements.docTitle) elements.docTitle.textContent = "Woordenboek Harf Ghair 'Amil | Referentie van Koranpartikels";
      } else if (state.lang === 'it') {
        elements.brandTitle.innerHTML = "Dizionario di <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Dizionario Interattivo delle Particelle Inoperative del Corano";
        if (elements.docTitle) elements.docTitle.textContent = "Dizionario di Harf Ghair 'Amil | Riferimenti Coranici";
      } else if (state.lang === 'bs') {
        elements.brandTitle.innerHTML = "Rječnik <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktivni rječnik za 17 oblika i 52 čestice u Kur'anu";
        if (elements.docTitle) elements.docTitle.textContent = "Rječnik Harf Ghair 'Amil | Kur'anske čestice";

      } else if (state.lang === 'ber') {
        elements.brandTitle.innerHTML = "Asegzawal <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Asegzawal n 17 n talɣiwin d 52 n tseddariyin n Leqran";
        if (elements.docTitle) elements.docTitle.textContent = "Asegzawal Harf Ghair 'Amil | Leqran";
      } else if (state.lang === 'az') {
        elements.brandTitle.innerHTML = "Lüğət <span>Hərfi Qeyri-Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Qurani-Kərimdə 17 kateqoriya və 52 qeyri-amil hərfin izahlı lüğəti";
        if (elements.docTitle) elements.docTitle.textContent = "Hərfi Qeyri-Amil Lüğəti | Qurani-Kərim";
      } else if (state.lang === 'bg') {
        elements.brandTitle.innerHTML = "Речник <span>Харф Гайр Амил</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Интерактивен речник за 17 форми и 52 неуправляващи частици в Корана";
        if (elements.docTitle) elements.docTitle.textContent = "Речник Харф Гайр Амил | Свещеният Коран";
      } else if (state.lang === 'am') {
        elements.brandTitle.innerHTML = "የ<span>ሐርፈ ገይሩ ዓሚል</span> መዝገበ-ቃላት";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "በቁርኣን ውስጥ የ17 ቅርጾችና የ52 የማይሰሩ ቅንጣቶች መመሪያ";
        if (elements.docTitle) elements.docTitle.textContent = "የሐርፈ ገይሩ ዓሚል መዝገበ-ቃላት | ቅዱስ ቁርኣން";
      } else if (state.lang === 'cs') {
        elements.brandTitle.innerHTML = "Slovník <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktivní slovník pro 17 forem a 52 neřídících částic v Koránu";
        if (elements.docTitle) elements.docTitle.textContent = "Slovník Harf Ghair 'Amil | Svatý Korán";
      } else if (state.lang === 'dv') {
        elements.brandTitle.innerHTML = "ރަދީފު <span>ޙަރްފު ޣައިރު ޢާމިލް</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "ކީރިތި ޤުރްއާނުގެ 17 ބާވަތާއި 52 ޣައިރު ޢާމިލް އަކުރުގެ ރަދީފު";
        if (elements.docTitle) elements.docTitle.textContent = "ޙަރްފު ޣައިރު ޢާމިލް ރަދީފު | ކީރިތި ޤުރްއާން";
      } else if (state.lang === 'no') {
        elements.brandTitle.innerHTML = "Ordbok <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktiv ordbok for 17 former og 52 ikke-styrende partikler i Koranen";
        if (elements.docTitle) elements.docTitle.textContent = "Ordbok Harf Ghair 'Amil | Den Hellige Koranen";
      } else if (state.lang === 'pl') {
        elements.brandTitle.innerHTML = "Słownik <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktywny słownik 17 form i 52 niezarządzających partykuł w Koranie";
        if (elements.docTitle) elements.docTitle.textContent = "Słownik Harf Ghair 'Amil | Święty Koran";
      } else if (state.lang === 'ro') {
        elements.brandTitle.innerHTML = "Dicționar <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Dicționar interactiv pentru 17 forme și 52 de particule invariabile din Coran";
        if (elements.docTitle) elements.docTitle.textContent = "Dicționar Harf Ghair 'Amil | Coranul cel Sfânt";
      } else if (state.lang === 'sv') {
        elements.brandTitle.innerHTML = "Ordbok <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktiv ordbok för 17 former och 52 oböjliga partiklar i Koranen";
        if (elements.docTitle) elements.docTitle.textContent = "Ordbok Harf Ghair 'Amil | Den Heliga Koranen";
      } else if (state.lang === 'tg') {
        elements.brandTitle.innerHTML = "Луғати <span>Ҳарфҳои Ғайри Омил</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Луғати интерактивии 17 гурӯҳ ва 52 ҳарфи ғайри омил дар Қуръон";
        if (elements.docTitle) elements.docTitle.textContent = "Луғати Ҳарфҳои Ғайри Омил | Қуръони Карим";
      } else if (state.lang === 'ta') {
        elements.brandTitle.innerHTML = "அகராதி <span>ஹர்ஃப் ஃகைரு ஆமில்</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "திருக்குர்ஆனின் 17 வகைகள் மற்றும் 52 செயலற்ற இடைச்சொற்களின் அகராதி";
        if (elements.docTitle) elements.docTitle.textContent = "ஹர்ஃப் ஃகைரு ஆமில் அகராதி | புனித குர்ஆன்";
      } else if (state.lang === 'tt') {
        elements.brandTitle.innerHTML = "Сүзлек <span>Гайре Гамил Хәрефләр</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Коръәни Кәримнең 17 төре һәм 52 гайре гамил кисәкчәсе сүзлеге";
        if (elements.docTitle) elements.docTitle.textContent = "Гайре Гамил Хәрефләр сүзлеге | Коръәни Кәрим";
      } else if (state.lang === 'ug') {
        elements.brandTitle.innerHTML = "لۇغەت <span>غەيرى ئامىل ھەرپلەر</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "قۇرئاندىكى 17 تۈر ۋە 52 تەسىرسىز يۈكلىمىنىڭ لۇغىتى";
        if (elements.docTitle) elements.docTitle.textContent = "غەيرى ئامىل ھەرپلەر لۇغىتى | قۇرئانى كەرىم";
      } else if (state.lang === 'uz') {
        elements.brandTitle.innerHTML = "Lug'at <span>G'ayri Omil Harflar</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Qur'ondagi 17 tur va 52 ta amalsiz yuklamalar lug'ati";
        if (elements.docTitle) elements.docTitle.textContent = "G'ayri Omil Harflar lug'ati | Qur'oni Karim";
      } else if (state.lang === 'ku') {
        elements.brandTitle.innerHTML = "فەرهەنگی <span>پیتە بێ کارلێکەکان</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "فەرهەنگی 17 جۆر و 52 پیت و ئامرازی بێ کارلێک لە قورئاندا";
        if (elements.docTitle) elements.docTitle.textContent = "فەرهەنگی پیتە بێ کارلێکەکان | قورئانی پیرۆز";
      } else if (state.lang === 'th') {
        elements.brandTitle.innerHTML = "พจนานุกรม <span>ฮัรฟ์ ฆ็อยรุอามิล</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "พจนานุกรมคำศัพท์ 17 รูปแบบและ 52 ตัวอักษรไม่ออกฤทธิ์ในอัลกุรอาน";
        if (elements.docTitle) elements.docTitle.textContent = "พจนานุกรมฮัรฟ์ ฆ็อยรุอามิล | อายะฮ์อ้างอิงอัลกุรอาน";
      } else if (state.lang === 'sq') {
        elements.brandTitle.innerHTML = "Fjalori i <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Fjalor interaktiv për 17 forma dhe 52 pjesëza kur'anore";
        if (elements.docTitle) elements.docTitle.textContent = "Fjalori i Harf Ghair 'Amil | Pjesëzat kur'anore";
      } else if (state.lang === 'en') {
        elements.brandTitle.innerHTML = "Dictionary of <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interactive Dictionary of Inoperative Quranic Particles";
        if (elements.docTitle) elements.docTitle.textContent = "Dictionary of Harf Ghair 'Amil | Quranic Particles";
      } else {
        elements.brandTitle.innerHTML = "Kamus <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Kamus Interaktif 17 Bentuk Harf & 52 Kata Al-Qur'an";
        if (elements.docTitle) elements.docTitle.textContent = "Kamus Harf Ghair 'Amil | Rujukan Ayat Interaktif Al-Qur'an";
      }
    } else {
      elements.brandTitle.innerHTML = t('brandTitle');
      if (elements.brandSubtitle) elements.brandSubtitle.textContent = t('brandSubtitle');
      if (elements.docTitle) elements.docTitle.textContent = t('pageTitle');
    }
  }

  // Parse Raw Dataset into Organized Groupings
  function initData() {
    let rawDataset = [];
    if (state.activeDict === 'harf_amil' && typeof HARF_AMIL_DATA !== 'undefined') {
      rawDataset = HARF_AMIL_DATA;
    } else if (state.activeDict === 'harf' && typeof HARF_DATA !== 'undefined') {
      rawDataset = HARF_DATA;
    } else if (typeof DHAMIR_DATA !== 'undefined') {
      rawDataset = DHAMIR_DATA;
    }

    groups = {};
    availableBentukKatas = [];
    noKatasByBentuk = {};

    rawDataset.forEach(item => {
      const b = item['Bentuk Kata'] || item['BentukKata'] || '';
      const nk = item['No kata'] || item['NoKata'] || '';
      if (!b || !nk) return;

      const groupKey = getGroupKey(b, nk);

      if (!groups[groupKey]) {
        const grammar = item['Grammar'] || {};
        groups[groupKey] = {
          bentuk: b,
          noKata: nk,
          kata: item['Kata'] || '',
          latin: item['Latin'] || grammar.latin || item['Kata'] || '',
          frek: item['Frek kata'] || item['Frek'] || item['FrekKata'] || '',
          arti: item['Arti kata'] || item['Arti'] || '',
          grammar: grammar,
          
          // Multilingual Bentuk Kata
          bentuk_id: item['BentukKataID'] || b,
          bentuk_en: item['BentukKataEN'] || b,
          bentuk_ms: item['BentukKataMS'] || b,
          bentuk_fr: item['BentukKataFR'] || b,
          bentuk_de: item['BentukKataDE'] || b,
          bentuk_ur: item['BentukKataUR'] || b,
          bentuk_hi: item['BentukKataHI'] || b,
          bentuk_bn: item['BentukKataBN'] || b,
          bentuk_ru: item['BentukKataRU'] || b,
          bentuk_zh: item['BentukKataZH'] || b,
          bentuk_es: item['BentukKataES'] || b,
          bentuk_tr: item['BentukKataTR'] || b,
          bentuk_pt: item['BentukKataPT'] || b,
          bentuk_ha: item['BentukKataHA'] || b,
          bentuk_sw: item['BentukKataSW'] || b,
          bentuk_fa: item['BentukKataFA'] || b,
          bentuk_ja: item['BentukKataJA'] || b,
          bentuk_ko: item['BentukKataKO'] || b,
          bentuk_nl: item['BentukKataNL'] || b,
          bentuk_it: item['BentukKataIT'] || b,
          bentuk_bs: item['BentukKataBS'] || b,
          bentuk_sq: item['BentukKataSQ'] || b,
          bentuk_ber: item['BentukKataBER'] || b,
          bentuk_am: item['BentukKataAM'] || b,
          bentuk_az: item['BentukKataAZ'] || b,
          bentuk_bg: item['BentukKataBG'] || b,
          bentuk_cs: item['BentukKataCS'] || b,
          bentuk_dv: item['BentukKataDV'] || b,
          bentuk_no: item['BentukKataNO'] || b,
          bentuk_pl: item['BentukKataPL'] || b,
          bentuk_ro: item['BentukKataRO'] || b,
          bentuk_sv: item['BentukKataSV'] || b,
          bentuk_tg: item['BentukKataTG'] || b,
          bentuk_ta: item['BentukKataTA'] || b,
          bentuk_tt: item['BentukKataTT'] || b,
          bentuk_ug: item['BentukKataUG'] || b,
          bentuk_uz: item['BentukKataUZ'] || b,
          bentuk_ku: item['BentukKataKU'] || b,
          bentuk_th: item['BentukKataTH'] || b,
          
          // Multilingual Word Meanings
          arti_id: item['ArtiKataID'] || grammar.arti_id || item['Arti kata'] || '',
          arti_en: item['ArtiKataEN'] || grammar.arti_en || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_ms: item['ArtiKataMS'] || grammar.arti_ms || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_fr: item['ArtiKataFR'] || grammar.arti_fr || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_de: item['ArtiKataDE'] || grammar.arti_de || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_ur: item['ArtiKataUR'] || grammar.arti_ur || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_hi: item['ArtiKataHI'] || grammar.arti_hi || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_bn: item['ArtiKataBN'] || grammar.arti_bn || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_ru: item['ArtiKataRU'] || grammar.arti_ru || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_zh: item['ArtiKataZH'] || grammar.arti_zh || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_es: item['ArtiKataES'] || grammar.arti_es || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_tr: item['ArtiKataTR'] || grammar.arti_tr || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_pt: item['ArtiKataPT'] || grammar.arti_pt || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_ha: item['ArtiKataHA'] || grammar.arti_ha || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_sw: item['ArtiKataSW'] || grammar.arti_sw || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_fa: item['ArtiKataFA'] || grammar.arti_fa || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_ja: item['ArtiKataJA'] || grammar.arti_ja || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_ko: item['ArtiKataKO'] || grammar.arti_ko || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_nl: item['ArtiKataNL'] || grammar.arti_nl || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_it: item['ArtiKataIT'] || grammar.arti_it || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_bs: item['ArtiKataBS'] || grammar.arti_bs || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_sq: item['ArtiKataSQ'] || grammar.arti_sq || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_ber: item['ArtiKataBER'] || grammar.arti_ber || item['ArtiKataEN'] || '',
          arti_am: item['ArtiKataAM'] || grammar.arti_am || item['ArtiKataEN'] || '',
          arti_az: item['ArtiKataAZ'] || grammar.arti_az || item['ArtiKataEN'] || '',
          arti_bg: item['ArtiKataBG'] || grammar.arti_bg || item['ArtiKataEN'] || '',
          arti_cs: item['ArtiKataCS'] || grammar.arti_cs || item['ArtiKataEN'] || '',
          arti_dv: item['ArtiKataDV'] || grammar.arti_dv || item['ArtiKataEN'] || '',
          arti_no: item['ArtiKataNO'] || grammar.arti_no || item['ArtiKataEN'] || '',
          arti_pl: item['ArtiKataPL'] || grammar.arti_pl || item['ArtiKataEN'] || '',
          arti_ro: item['ArtiKataRO'] || grammar.arti_ro || item['ArtiKataEN'] || '',
          arti_sv: item['ArtiKataSV'] || grammar.arti_sv || item['ArtiKataEN'] || '',
          arti_tg: item['ArtiKataTG'] || grammar.arti_tg || item['ArtiKataEN'] || '',
          arti_ta: item['ArtiKataTA'] || grammar.arti_ta || item['ArtiKataEN'] || '',
          arti_tt: item['ArtiKataTT'] || grammar.arti_tt || item['ArtiKataEN'] || '',
          arti_ug: item['ArtiKataUG'] || grammar.arti_ug || item['ArtiKataEN'] || '',
          arti_uz: item['ArtiKataUZ'] || grammar.arti_uz || item['ArtiKataEN'] || '',
          arti_ku: item['ArtiKataKU'] || grammar.arti_ku || item['ArtiKataEN'] || '',
          arti_th: item['ArtiKataTH'] || grammar.arti_th || item['ArtiKataEN'] || '',

          occurrences: []
        };

        if (!availableBentukKatas.includes(b)) {
          availableBentukKatas.push(b);
          noKatasByBentuk[b] = [];
        }
        if (!noKatasByBentuk[b].includes(nk)) {
          noKatasByBentuk[b].push(nk);
        }
      }

      groups[groupKey].occurrences.push({
        surat: parseInt(item['SURAT'] || item['Surat'] || 1, 10),
        ayat: parseInt(item['AYAT'] || item['Ayat'] || 1, 10),
        suratNama: item['SuratNama'] || `Surat ${item['SURAT']}`,
        suratArab: item['SuratArab'] || '',
        
        // Surat Meanings
        suratArtiID: item['SuratArtiID'] || item['SuratArti'] || '',
        suratArtiEN: item['SuratArtiEN'] || item['SuratArti'] || '',
        suratArtiMS: item['SuratArtiMS'] || item['SuratArti'] || '',
        suratArtiFR: item['SuratArtiFR'] || item['SuratArtiEN'] || '',
        suratArtiDE: item['SuratArtiDE'] || item['SuratArtiEN'] || '',
        suratArtiUR: item['SuratArtiUR'] || item['SuratArtiEN'] || '',
        suratArtiHI: item['SuratArtiHI'] || item['SuratArtiEN'] || '',
        suratArtiBN: item['SuratArtiBN'] || item['SuratArtiEN'] || '',
        suratArtiRU: item['SuratArtiRU'] || item['SuratArtiEN'] || '',
        suratArtiZH: item['SuratArtiZH'] || item['SuratArtiEN'] || '',
        suratArtiES: item['SuratArtiES'] || item['SuratArtiEN'] || '',
        suratArtiTR: item['SuratArtiTR'] || item['SuratArtiEN'] || '',
        suratArtiPT: item['SuratArtiPT'] || item['SuratArtiEN'] || '',
        suratArtiHA: item['SuratArtiHA'] || item['SuratArtiEN'] || '',
        suratArtiSW: item['SuratArtiSW'] || item['SuratArtiEN'] || '',
        suratArtiFA: item['SuratArtiFA'] || item['SuratArtiEN'] || '',
        suratArtiJA: item['SuratArtiJA'] || item['SuratArtiEN'] || '',
        suratArtiKO: item['SuratArtiKO'] || item['SuratArtiEN'] || '',
        suratArtiNL: item['SuratArtiNL'] || item['SuratArtiEN'] || '',
        suratArtiIT: item['SuratArtiIT'] || item['SuratArtiEN'] || '',
        suratArtiBS: item['SuratArtiBS'] || item['SuratArtiEN'] || '',
        suratArtiSQ: item['SuratArtiSQ'] || item['SuratArtiEN'] || '',
        suratArtiBER: item['SuratArtiBER'] || item['SuratArtiEN'] || '',
        suratArtiAM: item['SuratArtiAM'] || item['SuratArtiEN'] || '',
        suratArtiAZ: item['SuratArtiAZ'] || item['SuratArtiEN'] || '',
        suratArtiBG: item['SuratArtiBG'] || item['SuratArtiEN'] || '',
        suratArtiCS: item['SuratArtiCS'] || item['SuratArtiEN'] || '',
        suratArtiDV: item['SuratArtiDV'] || item['SuratArtiEN'] || '',
        suratArtiNO: item['SuratArtiNO'] || item['SuratArtiEN'] || '',
        suratArtiPL: item['SuratArtiPL'] || item['SuratArtiEN'] || '',
        suratArtiRO: item['SuratArtiRO'] || item['SuratArtiEN'] || '',
        suratArtiSV: item['SuratArtiSV'] || item['SuratArtiEN'] || '',
        suratArtiTG: item['SuratArtiTG'] || item['SuratArtiEN'] || '',
        suratArtiTA: item['SuratArtiTA'] || item['SuratArtiEN'] || '',
        suratArtiTT: item['SuratArtiTT'] || item['SuratArtiEN'] || '',
        suratArtiUG: item['SuratArtiUG'] || item['SuratArtiEN'] || '',
        suratArtiUZ: item['SuratArtiUZ'] || item['SuratArtiEN'] || '',
        suratArtiKU: item['SuratArtiKU'] || item['SuratArtiEN'] || '',
        suratArtiTH: item['SuratArtiTH'] || item['SuratArtiEN'] || '',

        teksArab: item['TeksArab'] || '',
        teksLatin: item['TeksLatin'] || '',
        
        // Verse Translations
        teksArtiID: item['TeksArtiID'] || item['TeksArti'] || '',
        teksArtiEN: item['TeksArtiEN'] || item['TeksArti'] || '',
        teksArtiMS: item['TeksArtiMS'] || item['TeksArti'] || '',
        teksArtiFR: item['TeksArtiFR'] || item['TeksArtiEN'] || '',
        teksArtiDE: item['TeksArtiDE'] || item['TeksArtiEN'] || '',
        teksArtiUR: item['TeksArtiUR'] || item['TeksArti'] || '',
        teksArtiHI: item['TeksArtiHI'] || item['TeksArti'] || '',
        teksArtiBN: item['TeksArtiBN'] || item['TeksArti'] || '',
        teksArtiRU: item['TeksArtiRU'] || item['TeksArti'] || '',
        teksArtiZH: item['TeksArtiZH'] || item['TeksArti'] || '',
        teksArtiES: item['TeksArtiES'] || item['TeksArti'] || '',
        teksArtiTR: item['TeksArtiTR'] || item['TeksArti'] || '',
        teksArtiPT: item['TeksArtiPT'] || item['TeksArti'] || '',
        teksArtiHA: item['TeksArtiHA'] || item['TeksArti'] || '',
        teksArtiSW: item['TeksArtiSW'] || item['TeksArti'] || '',
        teksArtiFA: item['TeksArtiFA'] || item['TeksArti'] || '',
        teksArtiJA: item['TeksArtiJA'] || item['TeksArti'] || '',
        teksArtiKO: item['TeksArtiKO'] || item['TeksArti'] || '',
        teksArtiNL: item['TeksArtiNL'] || item['TeksArti'] || '',
        teksArtiIT: item['TeksArtiIT'] || item['TeksArti'] || '',
        teksArtiBS: item['TeksArtiBS'] || item['TeksArti'] || '',
        teksArtiSQ: item['TeksArtiSQ'] || item['TeksArti'] || '',
        teksArtiBER: item['TeksArtiBER'] || item['TeksArtiEN'] || '',
        teksArtiAM: item['TeksArtiAM'] || item['TeksArtiEN'] || '',
        teksArtiAZ: item['TeksArtiAZ'] || item['TeksArtiEN'] || '',
        teksArtiBG: item['TeksArtiBG'] || item['TeksArtiEN'] || '',
        teksArtiCS: item['TeksArtiCS'] || item['TeksArtiEN'] || '',
        teksArtiDV: item['TeksArtiDV'] || item['TeksArtiEN'] || '',
        teksArtiNO: item['TeksArtiNO'] || item['TeksArtiEN'] || '',
        teksArtiPL: item['TeksArtiPL'] || item['TeksArtiEN'] || '',
        teksArtiRO: item['TeksArtiRO'] || item['TeksArtiEN'] || '',
        teksArtiSV: item['TeksArtiSV'] || item['TeksArtiEN'] || '',
        teksArtiTG: item['TeksArtiTG'] || item['TeksArtiEN'] || '',
        teksArtiTA: item['TeksArtiTA'] || item['TeksArtiEN'] || '',
        teksArtiTT: item['TeksArtiTT'] || item['TeksArtiEN'] || '',
        teksArtiUG: item['TeksArtiUG'] || item['TeksArtiEN'] || '',
        teksArtiUZ: item['TeksArtiUZ'] || item['TeksArtiEN'] || '',
        teksArtiKU: item['TeksArtiKU'] || item['TeksArtiEN'] || '',
        teksArtiTH: item['TeksArtiTH'] || item['TeksArtiEN'] || '',

        audioUrl: item['AudioUrl'] || getAyatAudioUrl(item['SURAT'], item['AYAT'])
      });
    });

    // Sort categories numerically
    availableBentukKatas.sort((a, bVal) => {
      const numA = parseInt(a.split('.')[0], 10) || 0;
      const numB = parseInt(bVal.split('.')[0], 10) || 0;
      if (numA !== numB) return numA - numB;
      return a.localeCompare(bVal);
    });

    // Sort No Katas in each category
    Object.keys(noKatasByBentuk).forEach(b => {
      const preferred = PREFERRED_NO_KATA_ORDER[b];
      if (preferred) {
        noKatasByBentuk[b].sort((a, bVal) => {
          const idxA = preferred.indexOf(a);
          const idxB = preferred.indexOf(bVal);
          if (idxA !== -1 && idxB !== -1) return idxA - idxB;
          if (idxA !== -1) return -1;
          if (idxB !== -1) return 1;
          return a.localeCompare(bVal, undefined, { numeric: true });
        });
      } else {
        noKatasByBentuk[b].sort((a, bVal) => {
          const intA = parseInt(a, 10);
          const intB = parseInt(bVal, 10);
          if (!isNaN(intA) && !isNaN(intB)) return intA - intB;
          return a.localeCompare(bVal, undefined, { numeric: true });
        });
      }
    });

    // Validate selected options
    if (state.selectedBentuk && !availableBentukKatas.includes(state.selectedBentuk)) {
      state.selectedBentuk = '';
    }
    const currentBentukList = noKatasByBentuk[state.selectedBentuk] || [];
    if (state.selectedNoKata && !currentBentukList.includes(state.selectedNoKata)) {
      state.selectedNoKata = '';
    }
  }

  // Populate Bentuk Kata Dropdown
  function populateBentukDropdown() {
    if (!elements.bentukKataSelect) return;
    elements.bentukKataSelect.innerHTML = '';

    const placeholderOption = document.createElement('option');
    placeholderOption.value = '';
    placeholderOption.textContent = t('step1Placeholder');
    if (!state.selectedBentuk) {
      placeholderOption.selected = true;
    }
    elements.bentukKataSelect.appendChild(placeholderOption);

    function getBentukLabelText(b) {
      if (state.activeDict === 'harf_amil' && typeof HARF_AMIL_BENTUK_LABELS !== 'undefined' && HARF_AMIL_BENTUK_LABELS[b]) {
        return HARF_AMIL_BENTUK_LABELS[b][state.lang] || HARF_AMIL_BENTUK_LABELS[b]['id'] || b;
      }
      if (state.activeDict === 'harf' && typeof HARF_BENTUK_LABELS !== 'undefined' && HARF_BENTUK_LABELS[b]) {
        return HARF_BENTUK_LABELS[b][state.lang] || HARF_BENTUK_LABELS[b]['id'] || b;
      }
      const map = {
        '1. Dhamir': 'step1OptionDhamir',
        '2. Mawshul': 'step1OptionMawshul',
        '3. Istifham': 'step1OptionIstifham',
        '4. Syarath': 'step1OptionSyarath',
        '5. Isyarah': 'step1OptionIsyarah',
        "6. Isim Fi'il": 'step1OptionIsimFiil',
        "7. Fi'il Jamid": 'step1OptionFiilJamid'
      };
      const key = map[b];
      if (key && I18N[state.lang] && I18N[state.lang][key]) {
        return I18N[state.lang][key];
      }
      return b;
    }

    availableBentukKatas.forEach(b => {
      const option = document.createElement('option');
      option.value = b;
      option.textContent = getBentukLabelText(b);
      if (state.selectedBentuk === b) {
        option.selected = true;
      }
      elements.bentukKataSelect.appendChild(option);
    });

    elements.bentukKataSelect.value = state.selectedBentuk || '';
  }

  // Populate No Kata Dropdown
  function populateNoKataDropdown() {
    if (!elements.noKataSelect) return;
    elements.noKataSelect.innerHTML = '';

    const placeholderOption = document.createElement('option');
    placeholderOption.value = '';
    placeholderOption.textContent = t('step2Placeholder');
    if (!state.selectedNoKata) {
      placeholderOption.selected = true;
    }
    elements.noKataSelect.appendChild(placeholderOption);
    
    const activeList = noKatasByBentuk[state.selectedBentuk] || [];
    if (!state.selectedBentuk || activeList.length === 0) {
      elements.noKataSelect.disabled = true;
      elements.noKataSelect.value = '';
      return;
    }

    elements.noKataSelect.disabled = false;

    activeList.forEach(nk => {
      const group = getGroup(state.selectedBentuk, nk);
      if (!group) return;
      
      const option = document.createElement('option');
      option.value = nk;
      const latinPart = group.latin ? `[${group.latin}] ` : '';
      const localizedArti = getGroupArti(group, state.lang);
      
      option.textContent = `${nk} - ${group.kata} ${latinPart}(${localizedArti})`;
      if (state.selectedNoKata === nk) {
        option.selected = true;
      }
      elements.noKataSelect.appendChild(option);
    });

    elements.noKataSelect.value = state.selectedNoKata || '';
  }

  // Get Default Category Jenis (Fallback)
  function getDefaultJenis(bentuk, lang) {
    const defaultMap = {
      '1. Dhamir': {
        id: 'Munfashil', en: 'Munfashil', ms: 'Munfashil', fr: 'Munfashil', de: 'Munfashil',
        ur: 'منفصل', hi: 'मुन्फ़सिल', bn: 'মুনফাসিল', ru: 'Мунфасыль', zh: '独立代词', es: 'Munfashil (Independiente)', tr: 'Munfasıl (Ayrık Zamir)', pt: 'Munfashil (Independente)', ha: 'Munfashil (Mai Zaman Kansa)', sw: 'Munfashil (Kiwakilishi Huru)', fa: 'منفصل مرفوعی (ضمایر جدا)', ja: '主格分離代名詞', ko: '주격 분리대명사', nl: 'Losstaand voornaamwoord (Munfashil)', it: 'Pronome isolato (Munfashil)', bs: 'Samostalna zamjenica (Munfashil)', sq: 'Përemër i veçuar (Munfashil)', th: 'สรรพนามแยกเดี่ยว (มุนฟะศิล)', ber: 'Amqim Imserreḥ (Munfashil)', am: 'ተነጣይ ተውላጠ ስም (ሙንፈሲል)', az: 'Sərbəst adlıq əvəzliyi (Münfəsil)', bg: 'Самостоятелно именно местоимение (Мунфасил)', cs: 'Samostatné osobní zájmeno (Munfasil)', dv: 'ވަކިންވާ ޟަމީރު (މުންފަޞިލް)', no: 'Selvstendig personlig pronomen (Munfasil)', pl: 'Samodzielny zaimek osobowy (Munfasil)', ro: 'Pronume personal independent (Munfasil)', sv: 'Självständigt personligt pronomen (Munfasil)', tg: 'Ҷонишини шахсии ҷудогона (Мунфасил)', ta: 'தனித்துப் பிரதிப்பெயர் (முன்ஃபஸில்)', tt: 'Аерым зат алмашлыгы (Мөнфәсыйль)', ug: 'ئايرىم كىشىلىك ئالماش (مۇنفەسىل)', uz: 'Alohida shaxs olmoshi (Munfasil)', ku: 'جێناوی کەسیی سەربەخۆ (مونفەسیل)'
      },
      '2. Mawshul': {
        id: 'Isim Mawshul', en: 'Relative Pronoun', ms: 'Isim Mawshul', fr: 'Pronom Relatif', de: 'Relativpronomen',
        ur: 'اسم موصول', hi: 'संबंधवाचक सर्वनाम', bn: 'সম্বন্ধবাচক सर्वनाम', ru: 'Относительное местоимение', zh: '关系代词', es: 'Pronombre Relativo', tr: 'İsmi Mevsul (İlgi Zamiri)', pt: 'Pronome Relativo', ha: 'Isim Mawshul (Sunan Sadarwa)', sw: 'Isim Mawshul (Jina la Kuunganisha)', fa: 'اسم موصول', ja: '関係代名詞', ko: '관계대명사', nl: 'Betrekkelijk voornaamwoord (Mawshul)', it: 'Pronome relativo (Mawshul)', bs: 'Odnosna zamjenica (Isim Mawshul)', sq: 'Përemër lidhor (Isim Mawshul)', th: 'ประพันธสรรพนาม (เมาศูล)', ber: 'Amqim Amassaɣ (Mawshul)', am: 'አዛማጅ ተውላጠ ስም (መውሱል)', az: 'İsmi Mövsul (Nisbi əvəzlik)', bg: 'Относително местоимение (Маусул)', cs: 'Vztažné zájmeno (Ism Mawshúl)', dv: 'އިސްމު މައުޞޫލް (ގުޅުވައިދޭ އިސްމު)', no: 'Relativpronomen (Ism Mawshul)', pl: 'Zaimek względny (Ism Mawshul)', ro: 'Pronume relativ (Ism Mawshul)', sv: 'Relativt pronomen (Ism Mawshul)', tg: 'Исми мавсул (Пайвандак)', ta: 'இணைப்புச் சொல் (இஸ்மு மவ்ஸூல்)', tt: 'Исем мәүсул (Бәйләүче)', ug: 'ئىسىم مەۋسۇل (باغلىغۇچى)', uz: 'Ismi mavsul (Bog\'lovchi)', ku: 'ناوی مەوسوول (پەیوەندیی)'
      },
      '3. Istifham': {
        id: 'Isim Istifham', en: 'Interrogative', ms: 'Isim Istifham', fr: 'Mot Interrogatif', de: 'Fragewort',
        ur: 'اسم استفہام', hi: 'प्रश्नवाचक शब्द', bn: 'প্রশ্নবোধক शब्द', ru: 'Вопросительное слово', zh: '疑问代词', es: 'Interrogativo', tr: 'Soru Edatı (İstifham)', pt: 'Interrogativo', ha: 'Kalmar Tambaya (Istifham)', sw: 'Isim Istifham (Neno la Kuulizia)', fa: 'اسم استفهام (کلمات پرسشی)', ja: '疑問詞', ko: '의문사', nl: 'Vragend woord (Istifham)', it: 'Interrogativo (Istifham)', bs: 'Upitna zamjenica (Isim Istifham)', sq: 'Përemër pyetës (Isim Istifham)', th: 'คำถามปฤจฉา (อิสติฟฮาม)', ber: 'Isteqsi (Istifham)', am: 'መጠይቅ ቃል (ኢስቲፍሃም)', az: 'İsmi İstifham (Sual əvəzliyi)', bg: 'Въпросителна дума (Истифхам)', cs: 'Tázací zájmeno (Ism Istifhám)', dv: 'އިސްމު އިސްތިފްހާމް (ސުވާލުކުރާ އިސްމު)', no: 'Spørrepronomen (Ism Istifham)', pl: 'Zaimek pytający (Ism Istifham)', ro: 'Pronume interogativ (Ism Istifham)', sv: 'Frågepronomen (Ism Istifham)', tg: 'Исми пурсишӣ (Истифҳом)', ta: 'வினாப்பெயர் (இஸ்மு இஸ்திஃப்ஹாம்)', tt: 'Сорау алмашлыгы (Истифһам)', ug: 'سوئال ئالما Linux (ئىستىفھام)', uz: 'So\'roq olmoshi (Istifhom)', ku: 'ناوی پرسیار (ئیستیفھام)'
      },
      '4. Syarath': {
        id: 'Isim Syarat', en: 'Conditional', ms: 'Isim Syarat', fr: 'Mot Conditionnel', de: 'Konditionalwort',
        ur: 'اسم شرط', hi: 'शर्तवाचक शब्द', bn: 'শর্তমূলক शब्द', ru: 'Условное слово', zh: '条件代词', es: 'Condicional', tr: 'Şart Edatı', pt: 'Condicional', ha: 'Kalmar Sharaɗi (Syarath)', sw: 'Isim Syarat (Neno la Sharti)', fa: 'ادوات شرط', ja: '条件詞', ko: '조건사', nl: 'Voorwaardelijk woord (Syarath)', it: 'Condizionale (Syarath)', bs: 'Uslovna imenica (Isim Syarath)', sq: 'Emër kushtor (Isim Syarath)', th: 'คำเงื่อนไข (ชัรฏ์)', ber: 'Taseddariy n Tawtilt (Syarath)', am: 'ቅድመ-ሁኔታ ቃል (ሻራት)', az: 'İsmi Şərt (Şərt əvəzliyi)', bg: 'Условна дума (Шарат)', cs: 'Podmínkové slovo (Ism Šarath)', dv: 'އިސްމު ޝަރަތު (ޝަރުޠުކުރާ އިސްމު)', no: 'Betingelsesord (Ism Syarath)', pl: 'Zaimek warunkowy (Ism Syarath)', ro: 'Cuvânt condițional (Ism Syarath)', sv: 'Villkorsord (Ism Syarath)', tg: 'Калимаи шартӣ (Шарт)', ta: 'நிபந்தனைப் பெயர் (இஸ்மு ஷரத்)', tt: 'Шарт сүзе (Шарт)', ug: 'شەرت سۆزى (شەرت)', uz: 'Shart so\'zi (Shart)', ku: 'وشەی مەرج (شەرت)'
      },
      '5. Isyarah': {
        id: 'Isim Isyarah', en: 'Demonstrative', ms: 'Isim Isyarah', fr: 'Pronom Démonstratif', de: 'Demonstrativpronomen',
        ur: 'اسم اشارہ', hi: 'संकेतवाचक सर्वनाम', bn: 'নির্দেশক सर्वनाम', ru: 'Указательное местоимение', zh: '指示代词', es: 'Demonstrativo', tr: 'İşaret Zamiri', pt: 'Demonstrativo', ha: 'Sunan Nuni (Isyarah)', sw: 'Isim Isyarah (Jina la Kuonyeshea)', fa: 'اسم اشاره', ja: '指示代名詞', ko: '지시대명사', nl: 'Aanwijzend voornaamwoord (Isyarah)', it: 'Dimostrativo (Isyarah)', bs: 'Pokazna zamjenica (Isim Isyarah)', sq: 'Përemër dëftor (Isim Isyarah)', th: 'นิยมสรรพนาม (อิชารอฮ์)', ber: 'Amqim n Usmmal (Isyarah)', am: 'አመላካች ተውላጠ ስም (ኢሻራህ)', az: 'İsmi İşarə (İşarə əvəzliyi)', bg: 'Показателно местоимение (Ишара)', cs: 'Ukazovací zájmeno (Ism Išárah)', dv: 'އިސްމު އިޝާރާތް (އިޝާރާތްކުރާ އިސްމު)', no: 'Påpekende pronomen (Ism Isyarah)', pl: 'Zaimek wskazujący (Ism Isyarah)', ro: 'Pronume demonstrativ (Ism Isyarah)', sv: 'Påpekande pronomen (Ism Isyarah)', tg: 'Исми ишоратӣ (Ишора)', ta: 'சுட்டுப் பெயர் (இஸ்மு இஷாரா)', tt: 'Күрсәтү алмашлыгы (Ишарә)', ug: 'كۆرسىتىش ئالما Linux (ئىشارەت)', uz: 'Ko\'rsatish olmoshi (Ishora)', ku: 'ناوی ئاماژە (ئیشارە)'
      },
      "6. Isim Fi'il": {
        id: "Isim Fi'il", en: "Verbal Noun", ms: "Isim Fi'il", fr: "Nom Verbal", de: "Verbalnomen",
        ur: "اسم فعل", hi: "क्रियार्थک संज्ञा", bn: "ক্রিয়াভিত্তিক বিশেষ্য", ru: "Глагольное имя", zh: "动名词", es: "Nombre Verbal", tr: "İsim Fiil", pt: "Nome Verbal", ha: "Sunan Aiki (Isim Fi'il)", sw: "Isim Fi'il (Jina la Kitendo)", fa: "اسم فعل", ja: "動名詞", ko: "동명사", nl: "Verbale zelfstandig naamwoord (Isim Fi'il)", it: "Nome verbale (Isim Fi'il)", bs: "Glagolska imenica (Isim Fi'il)", sq: "Emër foljor (Isim Fi'il)", th: "นามกริยา (อิซมุลฟิอิล)", ber: "Isem n Tigawt (Isim Fi'il)", am: "ግሳዊ ስም (ኢስሙል ፊዕል)", az: "İsmi Feil (Feili İsim)", bg: "Глаголно име (Исм ал-фи'л)", cs: "Slovesné podstatné jméno (Ism Fi'il)", dv: "އިސްމު ފިޢުލު (ފިޢުލުގެ މާނަދޭ އިސްމު)", no: "Verbalt substantiv (Ism Fi'il)", pl: "Rzeczownik czasownikowy (Ism Fi'il)", ro: "Substantiv verbal (Ism Fi'il)", sv: "Verbalsubstantiv (Ism Fi'il)", tg: "Исми феъл (Исм Фиъл)", ta: "வினைப் பெயர்ச்சொல் (இஸ்மு ஃபிஇல்)", tt: "Исем фигыль (Исем Фигыль)", ug: "پېئىل ئىسمى (ئىسىم فېئىل)", uz: "Ismi fe'l (Ism Fe'l)", ku: "ناوی کردار (ئیسم فیعل)"
      },
      "7. Fi'il Jamid": {
        id: "Fi'il Jamid", en: "Inflexible Verb", ms: "Fi'il Jamid", fr: "Verbe Inflexible", de: "Inflexibles Verb",
        ur: "فعل جامد", hi: "रूढ़ क्रिया", bn: "অপরিবর্তনীয় ক্রিয়া", ru: "Неспрягаемый глагол", zh: "不变动词", es: "Verbo Inflexible", tr: "Câmid Fiil", pt: "Verbo Inflexível", ha: "Aiki Kafaffe (Fi'il Jamid)", sw: "Fi'il Jamid (Kitendo Kisichobadilika)", fa: "فعل جامد", ja: "不変化動詞", ko: "불변동사", nl: "Niet-vervoegbaar werkwoord (Fi'il Jamid)", it: "Verbo difettivo / inflessibile (Fi'il Jamid)", bs: "Nemenjivi glagol (Fi'il Jamid)", sq: "Folje e ngurosur (Fi'il Jamid)", th: "กริยาคงรูป (ฟิอิลญามิด)", ber: "Amyag Akiwan (Fi'il Jamid)", am: "የማይዘረዘር ግሥ (ፊዕል ጃሚድ)", az: "Feili Camid (Təsriflənməyən feil)", bg: "Неизменяем глагол (Фи'л Джамид)", cs: "Neohebné sloveso (Fi'il Džámid)", dv: "ފިޢުލު ޖާމިދު (ބަދަލުނުވާ ފިޢުލު)", no: "Uforanderlig verb (Fi'il Jamid)", pl: "Czasownik nieodmienny (Fi'il Jamid)", ro: "Verb invariabil (Fi'il Jamid)", sv: "Oböjligt verb (Fi'il Jamid)", tg: "Феъли ҷомид (Тағйирнаёбанда)", ta: "மாறா வினை (ஃபிஇல் ஜாமித்)", tt: "Җәмид фигыль (Үзгәрмәүче)", ug: "تۇراقلىق پېئىل (فېئىل جامىد)", uz: "Jomid fe'l (O'zgarmas fe'l)", ku: "کرداری نەگۆڕ (فیعل جامید)"
      }
    };
    const bMap = defaultMap[bentuk];
    if (bMap) {
      return bMap[lang] || bMap['id'] || bentuk;
    }
    return bentuk;
  }

  // Update Spotlight Card
  function updateSpotlightCard() {
    const group = getGroup(state.selectedBentuk, state.selectedNoKata);

    if (!group) {
      if (elements.spotlightCard) elements.spotlightCard.style.display = 'none';
      return;
    }

    if (elements.spotlightCard) elements.spotlightCard.style.display = 'block';

    // Badge texts
    if (elements.badgeBentukKata) elements.badgeBentukKata.textContent = getGroupBentuk(group, state.lang);
    if (elements.badgeNoKata) elements.badgeNoKata.textContent = `${t('wordNoBadgePrefix')} ${group.noKata}`;
    if (elements.badgeJenis) elements.badgeJenis.textContent = getGroupJenis(group, state.lang);

    // Displays
    if (elements.arabicWordDisplay) elements.arabicWordDisplay.textContent = group.kata;
    if (elements.wordLatinDisplay) elements.wordLatinDisplay.textContent = group.latin || group.kata;
    if (elements.wordMeaningDisplay) elements.wordMeaningDisplay.textContent = getGroupArti(group, state.lang);
    if (elements.wordMeaningSub) elements.wordMeaningSub.textContent = getGroupDesc(group, state.lang);

    // Frequency
    if (elements.labelFreqTitle) elements.labelFreqTitle.textContent = t('freqLabel');
    if (elements.frekValueDisplay) {
      if (group.frek) {
        elements.frekValueDisplay.textContent = `${group.frek} ×`;
        if (elements.frekSubtitle) elements.frekSubtitle.textContent = t('freqSub');
      } else {
        elements.frekValueDisplay.textContent = t('freqMuttashilVal');
        if (elements.frekSubtitle) elements.frekSubtitle.textContent = t('freqMuttashilSub');
      }
    }

    // Total Ayats
    const totalOccurrences = group.occurrences ? group.occurrences.length : 0;
    if (elements.labelTotalAyatTitle) elements.labelTotalAyatTitle.textContent = t('totalAyatLabel');
    if (elements.labelTotalAyatSub) elements.labelTotalAyatSub.textContent = t('totalAyatSub');
    if (elements.totalAyatBadge) elements.totalAyatBadge.textContent = `${totalOccurrences} Ayat`;
  }

  // Audio EveryAyah helper
  function getAyatAudioUrl(surat, ayat) {
    const s = String(surat).padStart(3, '0');
    const a = String(ayat).padStart(3, '0');
    return `https://everyayah.com/data/Alafasy_128kbps/${s}${a}.mp3`;
  }

  // Initialize Voice Cache for Web Speech API
  function updateVoiceCache() {
    if ('speechSynthesis' in window) {
      cachedVoices = window.speechSynthesis.getVoices() || [];
    }
  }
  if ('speechSynthesis' in window) {
    updateVoiceCache();
    if (typeof window.speechSynthesis.onvoiceschanged !== 'undefined') {
      window.speechSynthesis.onvoiceschanged = updateVoiceCache;
    }
  }

  // Stop All Audio and TTS
  function stopAllSpeech() {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
    if (currentCloudAudio) {
      currentCloudAudio.pause();
      currentCloudAudio.currentTime = 0;
      currentCloudAudio = null;
    }
    cloudAudioQueue = [];
    activeUtterance = null;
  }

  function stopVerseAudio() {
    if (currentAudio) {
      currentAudio.pause();
      currentAudio.currentTime = 0;
      currentAudio = null;
    }
    currentPlayingAyatKey = null;
  }

  function stopAllAudio() {
    stopAllSpeech();
    stopVerseAudio();
    updateAllAudioButtonStates();
  }

  // Update All Button States
  function updateAllAudioButtonStates() {
    document.querySelectorAll('.btn-play-tilawah, .btn-play-verse-audio').forEach(btn => {
      const icon = btn.querySelector('.audio-icon, .audio-icon-state');
      const label = btn.querySelector('.audio-label');
      if (icon) icon.innerHTML = '<polygon points="5 3 19 12 5 21 5 3"></polygon>';
      if (label) label.textContent = t('playTilawahBtn');
      btn.classList.remove('playing');
    });

    document.querySelectorAll('.btn-play-translation, .btn-play-translation-audio').forEach(btn => {
      const icon = btn.querySelector('.audio-icon, .audio-icon-state');
      const label = btn.querySelector('.audio-label');
      if (icon) icon.innerHTML = '<polygon points="5 3 19 12 5 21 5 3"></polygon>';
      if (label) label.textContent = t('playTranslationBtn');
      btn.classList.remove('playing', 'speaking');
    });
  }

  // Phonetic Normalizer for Amazigh (Tamaziɣt) Speech Synthesis
  function normalizeAmazighForTts(text) {
    if (!text) return '';
    let t = text.replace(/<[^>]*>/g, '').replace(/[()"]/g, ' ').trim();
    const subs = [
      ['č', 'tch'], ['Č', 'Tch'],
      ['ǧ', 'dj'],  ['Ǧ', 'Dj'],
      ['ɣ', 'gh'],  ['Ɣ', 'Gh'],
      ['ɛ', "'"],   ['Ɛ', "'"],
      ['ḥ', 'h'],   ['Ḥ', 'H'],
      ['ṭ', 't'],   ['Ṭ', 'T'],
      ['ṣ', 's'],   ['Ṣ', 'S'],
      ['ḍ', 'd'],   ['Ḍ', 'D'],
      ['ẓ', 'z'],   ['Ẓ', 'Z'],
      ['c', 'ch'],  ['C', 'Ch'],
      ['x', 'kh'],  ['X', 'Kh'],
      ['q', 'k'],   ['Q', 'K']
    ];
    subs.forEach(([orig, rep]) => {
      t = t.split(orig).join(rep);
    });
    return t;
  }

  // Phonetic Normalizer for Azerbaijani Speech Synthesis
  function normalizeAzerbaijaniForTts(text) {
    if (!text) return '';
    let t = text.replace(/<[^>]*>/g, '').replace(/[()"]/g, ' ').trim();
    const subs = [
      ['ə', 'e'], ['Ə', 'E'],
      ['x', 'h'], ['X', 'H'],
      ['q', 'k'], ['Q', 'K']
    ];
    subs.forEach(([orig, rep]) => {
      t = t.split(orig).join(rep);
    });
    return t;
  }

  // Phonetic Normalizer for Dhivehi (Thaana) Speech Synthesis Fallback
  function normalizeDhivehiForTts(text) {
    if (!text) return '';
    let t = text.replace(/<[^>]*>/g, '').replace(/[()"]/g, ' ').trim();
    const thaanaMap = {
      'ހ': 'h', 'ށ': 'sh', 'ނ': 'n', 'ރ': 'r', 'ބ': 'b', 'ޅ': 'lh', 'ކ': 'k', 'އ': 'a',
      'ވ': 'v', 'މ': 'm', 'ފ': 'f', 'ދ': 'd', 'ތ': 't', 'ލ': 'l', 'ގ': 'g', 'ޏ': 'gn',
      'ސ': 's', 'ޑ': 'd', 'ޒ': 'z', 'ޓ': 't', 'ޔ': 'y', 'ޕ': 'p', 'ޖ': 'j', 'ޗ': 'ch',
      'ޘ': 'th', 'ޙ': 'h', 'ޚ': 'kh', 'ޛ': 'dh', 'ޜ': 'zh', 'ޝ': 'sh', 'ޞ': 's', 'ޟ': 'd',
      'ޠ': 't', 'ޡ': 'z', 'ޢ': 'a', 'ޣ': 'gh', 'ޤ': 'q',
      'ަ': 'a', 'ާ': 'aa', 'ި': 'i', 'ީ': 'ee', 'ު': 'u', 'ޫ': 'oo', 'ެ': 'e', 'ޭ': 'ey',
      'ޮ': 'o', 'ޯ': 'oa', 'ް': ''
    };
    return t.split('').map(ch => thaanaMap[ch] !== undefined ? thaanaMap[ch] : ch).join('');
  }

  function normalizeTextForSpeech(rawText) {
    if (state.lang === 'dv') return normalizeDhivehiForTts(rawText);
    if (state.lang === 'ber') return normalizeAmazighForTts(rawText);
    if (state.lang === 'az') return normalizeAzerbaijaniForTts(rawText);
    return rawText;
  }

  // Helper for Google Cloud Native TTS Chunks (High quality native accents)


  function normalizeTatarForTts(text) {
    if (!text) return '';
    let t = text.replace(/<[^>]*>/g, '').replace(/"/g, ' ');
    const subs = [
      ['ә', 'э'], ['Ә', 'Э'],
      ['ө', 'о'], ['Ө', 'О'],
      ['ү', 'у'], ['Ү', 'У'],
      ['җ', 'дж'], ['Җ', 'Дж'],
      ['ң', 'н'], ['Ң', 'Н'],
      ['һ', 'х'], ['Һ', 'Х']
    ];
    subs.forEach(([orig, rep]) => {
      t = t.split(orig).join(rep);
    });
    return t;
  }

  function normalizeUzbekForTts(text) {
    if (!text) return '';
    let t = text.replace(/<[^>]*>/g, '').replace(/"/g, ' ');
    const subs = [
      ['ғ', 'г'], ['Ғ', 'Г'],
      ['қ', 'к'], ['Қ', 'К'],
      ['ҳ', 'х'], ['Ҳ', 'Х'],
      ['ў', 'у'], ['Ӯ', 'У'],
      ["o'", 'o'], ["g'", 'g'], ["sh", 'sh'], ["ch", 'ch']
    ];
    subs.forEach(([orig, rep]) => {
      t = t.split(orig).join(rep);
    });
    return t;
  }

  function normalizeTajikForTts(text) {
    if (!text) return '';
    let t = text.replace(/<[^>]*>/g, '').replace(/"/g, ' ');
    const subs = [
      ['ғ', 'г'], ['Ғ', 'Г'],
      ['ӣ', 'и'], ['Ӣ', 'И'],
      ['қ', 'к'], ['Қ', 'К'],
      ['ӯ', 'у'], ['Ӯ', 'У'],
      ['ҳ', 'х'], ['Ҳ', 'Х'],
      ['ҷ', 'дж'], ['Ҷ', 'Дж']
    ];
    subs.forEach(([orig, rep]) => {
      t = t.split(orig).join(rep);
    });
    return t;
  }

  function normalizeKurdishForTts(text) {
    if (!text) return '';
    let t = text.replace(/<[^>]*>/g, '').replace(/[()"\n\r]+/g, ' ');
    // Remove invisible unicode characters: ZWNJ (\u200c), ZWJ (\u200d), LTR/RTL marks (\u200e, \u200f), BOM (\ufeff)
    t = t.replace(/[\u200B-\u200F\uFEFF]/g, '');
    t = t.replace(/ـ/g, ''); // tatweel
    
    // Map Kurdish Sorani specific letters to Arabic phonetic equivalents for smooth pronunciation without letter-spelling
    const subs = [
      ['ڕ', 'ر'],
      ['ڵ', 'ل'],
      ['ێ', 'ي'],
      ['ۆ', 'و'],
      ['پ', 'ب'],
      ['چ', 'ج'],
      ['گ', 'ك'],
      ['ژ', 'ز'],
      ['ە', 'ه'],
      ['ڤ', 'ف'],
      ['ئ', 'ا'],
      ['ۇ', 'و'],
      ['ۊ', 'و']
    ];
    subs.forEach(([orig, rep]) => {
      t = t.split(orig).join(rep);
    });
    return t.replace(/\s+/g, ' ').trim();
  }

  function normalizeUyghurForTts(text) {
    if (!text) return '';
    let t = text.replace(/<[^>]*>/g, '').replace(/[()"\n\r]+/g, ' ');
    t = t.replace(/[\u200B-\u200F\uFEFF]/g, '');
    t = t.replace(/ـ/g, '');
    const subs = [
      ['ە', 'ه'],
      ['ۆ', 'و'],
      ['ۇ', 'و'],
      ['ۈ', 'و'],
      ['ې', 'ي'],
      ['ى', 'ي'],
      ['چ', 'ج'],
      ['ژ', 'ز'],
      ['گ', 'ك'],
      ['ڭ', 'نك'],
      ['ھ', 'ه'],
      ['ۋ', 'و'],
      ['پ', 'ب'],
      ['ق', 'ك'],
      ['ئ', 'ا']
    ];
    subs.forEach(([orig, rep]) => {
      t = t.split(orig).join(rep);
    });
    return t.replace(/\s+/g, ' ').trim();
  }

  function getGoogleTtsUrls(text, langCode) {
    let targetLang = langCode;
    let procText = text;
    if (langCode === 'ber') {
      targetLang = 'fr';
      procText = normalizeAmazighForTts(text);
    } else if (langCode === 'az') {
      targetLang = 'tr';
      procText = normalizeAzerbaijaniForTts(text);
    } else if (langCode === 'cs') {
      targetLang = 'cs';
    } else if (langCode === 'dv') {
      targetLang = 'ar';
      procText = normalizeDhivehiForTts(text);
    } else if (langCode === 'no') {
      targetLang = 'no';
    } else if (langCode === 'pl') {
      targetLang = 'pl';
    } else if (langCode === 'ro') {
      targetLang = 'ro';
    } else if (langCode === 'sv') {
      targetLang = 'sv';
    } else if (langCode === 'tg') {
      targetLang = 'ru';
      procText = normalizeTajikForTts(text);
    } else if (langCode === 'ta') {
      targetLang = 'ta';
    } else if (langCode === 'tt') {
      targetLang = 'ru';
      procText = normalizeTatarForTts(text);
    } else if (langCode === 'ug') {
      targetLang = 'ar';
      procText = normalizeUyghurForTts(text);
    } else if (langCode === 'uz') {
      targetLang = 'ru';
      procText = normalizeUzbekForTts(text);
    } else if (langCode === 'ku') {
      targetLang = 'ar';
      procText = normalizeKurdishForTts(text);
    }
    const clean = (procText || '').replace(/<[^>]*>/g, '').replace(/[()"\n\r]+/g, ' ').trim();
    if (!clean) return [];
    const chunks = [];
    const sentences = clean.match(/[^.!?،؛\n]+[.!?،؛\n]?/g) || [clean];
    let currentChunk = '';

    sentences.forEach(s => {
      s = s.trim();
      if (!s) return;
      if ((currentChunk + ' ' + s).length <= 150) {
        currentChunk = currentChunk ? (currentChunk + ' ' + s) : s;
      } else {
        if (currentChunk) chunks.push(currentChunk);
        if (s.length > 150) {
          const words = s.split(/\s+/);
          let wChunk = '';
          words.forEach(w => {
            if ((wChunk + ' ' + w).length <= 150) {
              wChunk = wChunk ? (wChunk + ' ' + w) : w;
            } else {
              if (wChunk) chunks.push(wChunk);
              wChunk = w;
            }
          });
          if (wChunk) chunks.push(wChunk);
          currentChunk = '';
        } else {
          currentChunk = s;
        }
      }
    });
    if (currentChunk) chunks.push(currentChunk);

    return chunks.map(c => `https://translate.google.com/translate_tts?ie=UTF-8&tl=${encodeURIComponent(targetLang)}&client=tw-ob&q=${encodeURIComponent(c)}`);
  }

  // Play Cloud Audio Queue Sequentially
  function playCloudAudioQueue(urls, onEnd, onError) {
    if (!urls || urls.length === 0) {
      if (onEnd) onEnd();
      return;
    }
    cloudAudioQueue = [...urls];

    function playNext() {
      if (cloudAudioQueue.length === 0) {
        currentCloudAudio = null;
        if (onEnd) onEnd();
        return;
      }
      const nextUrl = cloudAudioQueue.shift();
      currentCloudAudio = new Audio(nextUrl);
      currentCloudAudio.onended = playNext;
      currentCloudAudio.onerror = (err) => {
        console.warn('Cloud audio chunk failed, trying next:', err);
        if (cloudAudioQueue.length > 0) {
          playNext();
        } else if (onError) {
          onError(err);
        }
      };
      currentCloudAudio.play().catch(err => {
        console.warn('Playback error:', err);
        if (onError) onError(err);
      });
    }

    playNext();
  }

  // Toggle Verse Tilawah Audio (Mishary Alafasy)
  function toggleVerseAudio(surat, ayat, audioUrl, buttonEl) {
    const ayatKey = `${surat}:${ayat}`;

    if (currentPlayingAyatKey === ayatKey && currentAudio && !currentAudio.paused) {
      stopVerseAudio();
      updateAllAudioButtonStates();
      showToast(t('toastTilawahPaused'));
      return;
    }

    stopAllAudio();

    currentAudio = new Audio(audioUrl);
    currentPlayingAyatKey = ayatKey;
    currentAudioBtn = buttonEl;

    const icon = buttonEl.querySelector('.audio-icon, .audio-icon-state');
    const label = buttonEl.querySelector('.audio-label');
    if (icon) icon.innerHTML = '<rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect>';
    if (label) label.textContent = t('pauseTilawahBtn');
    buttonEl.classList.add('playing');

    showToast(t('toastTilawahPlaying', surat, ayat));

    currentAudio.play().catch(err => {
      console.error('Audio playback error:', err);
      stopVerseAudio();
      updateAllAudioButtonStates();
      showToast(t('toastAudioFailed'));
    });

    currentAudio.onended = () => {
      stopVerseAudio();
      updateAllAudioButtonStates();
      showToast(t('toastTilawahEnded'));
    };
  }

  // Speech Voice Selector Helper
  function getSpeechVoiceAndLang(langKey) {
    let speechLangCode = 'id-ID';
    let matchVoice = null;
    let hasNativeVoice = false;
    const voices = cachedVoices.length > 0 ? cachedVoices : (('speechSynthesis' in window) ? window.speechSynthesis.getVoices() : []);

    if (langKey === 'ar') {
      speechLangCode = 'ar-SA';
      matchVoice = voices.find(v => v.lang.startsWith('ar') && (v.name.includes('Maged') || v.name.includes('Tariq') || v.name.includes('Arabic') || v.name.includes('Saudi') || v.name.includes('Shakir'))) || voices.find(v => v.lang.startsWith('ar'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'en') {
      speechLangCode = 'en-US';
      matchVoice = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Samantha') || v.name.includes('David') || v.name.includes('US') || v.name.includes('English'))) || voices.find(v => v.lang.startsWith('en'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'ms') {
      speechLangCode = 'ms-MY';
      matchVoice = voices.find(v => v.lang.startsWith('ms'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'fr') {
      speechLangCode = 'fr-FR';
      matchVoice = voices.find(v => v.lang.startsWith('fr'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'de') {
      speechLangCode = 'de-DE';
      matchVoice = voices.find(v => v.lang.startsWith('de'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'ur') {
      speechLangCode = 'ur-PK';
      matchVoice = voices.find(v => v.lang.startsWith('ur'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'hi') {
      speechLangCode = 'hi-IN';
      matchVoice = voices.find(v => v.lang.startsWith('hi'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'bn') {
      speechLangCode = 'bn-BD';
      matchVoice = voices.find(v => v.lang.startsWith('bn'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'ru') {
      speechLangCode = 'ru-RU';
      matchVoice = voices.find(v => v.lang.startsWith('ru'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'zh') {
      speechLangCode = 'zh-CN';
      matchVoice = voices.find(v => v.lang.startsWith('zh'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'es') {
      speechLangCode = 'es-ES';
      matchVoice = voices.find(v => v.lang.startsWith('es'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'tr') {
      speechLangCode = 'tr-TR';
      matchVoice = voices.find(v => v.lang.startsWith('tr'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'pt') {
      speechLangCode = 'pt-PT';
      matchVoice = voices.find(v => v.lang.startsWith('pt'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'ha') {
      speechLangCode = 'ha-NG';
      matchVoice = voices.find(v => v.lang.startsWith('ha'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'sw') {
      speechLangCode = 'sw-TZ';
      matchVoice = voices.find(v => v.lang.startsWith('sw'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'fa') {
      speechLangCode = 'fa-IR';
      matchVoice = voices.find(v => v.lang.startsWith('fa'));
      hasNativeVoice = !!matchVoice;
      if (!matchVoice) {
        matchVoice = voices.find(v => v.lang.startsWith('ar'));
        if (matchVoice) speechLangCode = 'ar-SA';
      }
    } else if (langKey === 'ja') {
      speechLangCode = 'ja-JP';
      matchVoice = voices.find(v => v.lang.startsWith('ja'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'ko') {
      speechLangCode = 'ko-KR';
      matchVoice = voices.find(v => v.lang.startsWith('ko'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'nl') {
      speechLangCode = 'nl-NL';
      matchVoice = voices.find(v => v.lang.startsWith('nl'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'it') {
      speechLangCode = 'it-IT';
      matchVoice = voices.find(v => v.lang.startsWith('it'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'bs') {
      speechLangCode = 'bs-BA';
      matchVoice = voices.find(v => v.lang.startsWith('bs') || v.lang.startsWith('hr') || v.lang.startsWith('sr'));
      hasNativeVoice = !!matchVoice;

    } else if (langKey === 'az') {
      speechLangCode = 'az-AZ';
      matchVoice = voices.find(v => v.lang.startsWith('az')) ||
                   voices.find(v => v.lang.startsWith('tr') && (v.name.includes('Ahmet') || v.name.includes('Emel') || v.name.includes('Turkish') || v.name.includes('Turkey'))) ||
                   voices.find(v => v.lang.startsWith('tr'));
      hasNativeVoice = !!matchVoice;
      if (!voices.find(v => v.lang.startsWith('az')) && matchVoice) {
        speechLangCode = 'tr-TR';
      }
    } else if (langKey === 'bg') {
      speechLangCode = 'bg-BG';
      matchVoice = voices.find(v => v.lang.startsWith('bg'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'cs') {
      speechLangCode = 'cs-CZ';
      matchVoice = voices.find(v => v.lang.startsWith('cs'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'dv') {
      speechLangCode = 'dv-MV';
      matchVoice = voices.find(v => v.lang.startsWith('dv') || v.lang.startsWith('div'));
      hasNativeVoice = !!matchVoice;
      if (!matchVoice) {
        matchVoice = voices.find(v => v.lang.startsWith('ar'));
        if (matchVoice) speechLangCode = 'ar-SA';
      }
    } else if (langKey === 'no') {
      speechLangCode = 'nb-NO';
      matchVoice = voices.find(v => v.lang.startsWith('nb') || v.lang.startsWith('no') || v.lang.startsWith('nn'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'pl') {
      speechLangCode = 'pl-PL';
      matchVoice = voices.find(v => v.lang.startsWith('pl'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'ro') {
      speechLangCode = 'ro-RO';
      matchVoice = voices.find(v => v.lang.startsWith('ro'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'sv') {
      speechLangCode = 'sv-SE';
      matchVoice = voices.find(v => v.lang.startsWith('sv'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'tg') {
      speechLangCode = 'tg-TJ';
      matchVoice = voices.find(v => v.lang.startsWith('tg') || v.lang.startsWith('taj'));
      hasNativeVoice = !!matchVoice;
      if (!matchVoice) {
        matchVoice = voices.find(v => v.lang.startsWith('ru') || v.lang.startsWith('fa'));
        if (matchVoice) speechLangCode = matchVoice.lang;
      }
    } else if (langKey === 'ta') {
      speechLangCode = 'ta-IN';
      matchVoice = voices.find(v => v.lang.startsWith('ta'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'tt') {
      speechLangCode = 'tt-RU';
      matchVoice = voices.find(v => v.lang.startsWith('tt'));
      hasNativeVoice = !!matchVoice;
      if (!matchVoice) {
        matchVoice = voices.find(v => v.lang.startsWith('ru') || v.lang.startsWith('tr'));
        if (matchVoice) speechLangCode = matchVoice.lang;
      }
    } else if (langKey === 'ug') {
      speechLangCode = 'ug-CN';
      matchVoice = voices.find(v => v.lang.startsWith('ug'));
      hasNativeVoice = !!matchVoice;
      if (!matchVoice) {
        matchVoice = voices.find(v => v.lang.startsWith('ar') || v.lang.startsWith('tr'));
        if (matchVoice) speechLangCode = matchVoice.lang;
      }
    } else if (langKey === 'uz') {
      speechLangCode = 'uz-UZ';
      matchVoice = voices.find(v => v.lang.startsWith('uz'));
      hasNativeVoice = !!matchVoice;
      if (!matchVoice) {
        matchVoice = voices.find(v => v.lang.startsWith('tr') || v.lang.startsWith('ru'));
        if (matchVoice) speechLangCode = matchVoice.lang;
      }
    } else if (langKey === 'ku') {
      speechLangCode = 'ku-TR';
      matchVoice = voices.find(v => v.lang.startsWith('ku') || v.lang.startsWith('ckb') || v.lang.startsWith('kmr'));
      hasNativeVoice = !!matchVoice;
      if (!matchVoice) {
        matchVoice = voices.find(v => v.lang.startsWith('ar') || v.lang.startsWith('fa'));
        if (matchVoice) speechLangCode = matchVoice.lang;
      }
    } else if (langKey === 'am') {
      speechLangCode = 'am-ET';
      matchVoice = voices.find(v => v.lang.startsWith('am'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'ber') {
      speechLangCode = 'fr-FR';
      matchVoice = voices.find(v => v.lang.startsWith('ber') || v.lang.startsWith('kab') || v.lang.startsWith('zgh')) ||
                   voices.find(v => v.lang.startsWith('fr') && (v.name.includes('Denise') || v.name.includes('Henri') || v.name.includes('French') || v.name.includes('France'))) ||
                   voices.find(v => v.lang.startsWith('fr'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'th') {
      speechLangCode = 'th-TH';
      matchVoice = voices.find(v => v.lang.startsWith('th'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'sq') {
      speechLangCode = 'sq-AL';
      matchVoice = voices.find(v => v.lang.startsWith('sq'));
      hasNativeVoice = !!matchVoice;
    } else {
      speechLangCode = 'id-ID';
      matchVoice = voices.find(v => v.lang.startsWith('id'));
      hasNativeVoice = !!matchVoice;
    }

    return { speechLangCode, matchVoice, hasNativeVoice };
  }

  // Speak Arabic Word (Spotlight Card)
  function speakArabicWord(word) {
    stopAllAudio();
    const cleanWord = (word || '').replace(/\.\./g, '').replace(/\s*\d+$/, '').trim();
    if (!cleanWord) return;

    const { speechLangCode, matchVoice, hasNativeVoice } = getSpeechVoiceAndLang('ar');

    showToast(t('toastSpeakingArabic', cleanWord));

    if ('speechSynthesis' in window && hasNativeVoice) {
      const utterance = new SpeechSynthesisUtterance(cleanWord);
      utterance.lang = speechLangCode;
      utterance.rate = 0.85;
      if (matchVoice) utterance.voice = matchVoice;
      utterance.onerror = () => {
        const cloudUrls = getGoogleTtsUrls(cleanWord, 'ar');
        playCloudAudioQueue(cloudUrls);
      };
      window.speechSynthesis.speak(utterance);
    } else {
      const cloudUrls = getGoogleTtsUrls(cleanWord, 'ar');
      playCloudAudioQueue(cloudUrls, null, () => {
        if ('speechSynthesis' in window) {
          const utterance = new SpeechSynthesisUtterance(cleanWord);
          utterance.lang = 'ar-SA';
          window.speechSynthesis.speak(utterance);
        }
      });
    }
  }

  // Speak Dhamir Meaning (Spotlight Card)
  function speakDhamirMeaning(group) {
    if (!group) return;
    stopAllAudio();

    const langDict = I18N[state.lang] || I18N.id;
    const text = langDict.ttsMeaningSpeech ? langDict.ttsMeaningSpeech(group) : `${group.kata}, ${getGroupArti(group, state.lang)}`;
    const { speechLangCode, matchVoice, hasNativeVoice } = getSpeechVoiceAndLang(state.lang);

    showToast(t('toastSpeakingWordMeaning', getGroupArti(group, state.lang)));

    // For Turkish, Hausa, Swahili, Dutch, Italian without local voice: Use Google Cloud Native Voice
    if (!hasNativeVoice || state.lang === 'tr' || state.lang === 'ha' || state.lang === 'sw' || state.lang === 'nl' || state.lang === 'it' || state.lang === 'bs' || state.lang === 'sq' || state.lang === 'th' || state.lang === 'ber' || state.lang === 'am' || state.lang === 'az' || state.lang === 'bg' || state.lang === 'cs' || state.lang === 'dv' || state.lang === 'no' || state.lang === 'pl' || state.lang === 'ro' || state.lang === 'sv' || state.lang === 'tg' || state.lang === 'ta' || state.lang === 'tt' || state.lang === 'ug' || state.lang === 'uz' || state.lang === 'ku') {
      const cloudUrls = getGoogleTtsUrls(text, state.lang);
      playCloudAudioQueue(cloudUrls, null, () => {
        if ('speechSynthesis' in window) {
          const utterance = new SpeechSynthesisUtterance(normalizeTextForSpeech(text));
          utterance.lang = speechLangCode;
          if (matchVoice) utterance.voice = matchVoice;
          window.speechSynthesis.speak(utterance);
        }
      });
      return;
    }

    // For Persian: If no native voice, use Arabic voice or cloud stream
    if (state.lang === 'fa' && !hasNativeVoice) {
      if ('speechSynthesis' in window && matchVoice) {
        const utterance = new SpeechSynthesisUtterance(normalizeTextForSpeech(text));
        utterance.lang = speechLangCode;
        utterance.voice = matchVoice;
        window.speechSynthesis.speak(utterance);
      } else {
        const translitText = `${group.kata}, ${group.latin || group.arti_id || ''}`;
        const cloudUrls = getGoogleTtsUrls(translitText, 'ar');
        playCloudAudioQueue(cloudUrls);
      }
      return;
    }

    // Standard Web Speech API with fallback
    if ('speechSynthesis' in window) {
      const utterance = new SpeechSynthesisUtterance(normalizeTextForSpeech(text));
      utterance.lang = speechLangCode;
      utterance.rate = 0.95;
      if (matchVoice) utterance.voice = matchVoice;
      utterance.onerror = () => {
        const cloudUrls = getGoogleTtsUrls(text, state.lang === 'fa' ? 'ar' : state.lang);
        if (cloudUrls.length > 0) playCloudAudioQueue(cloudUrls);
      };
      window.speechSynthesis.speak(utterance);
    } else {
      const cloudUrls = getGoogleTtsUrls(text, state.lang === 'fa' ? 'ar' : state.lang);
      if (cloudUrls.length > 0) playCloudAudioQueue(cloudUrls);
    }
  }

  // Toggle Verse Translation Audio (Multi-tiered: Persian EveryAyah Recitation + Native Cloud Audio + Web Speech API)
  function toggleVerseTranslationAudio(surat, ayat, text, buttonEl) {
    const ayatKey = `${surat}:${ayat}`;

    // If currently playing, stop it
    if ((activeUtterance && window.speechSynthesis && window.speechSynthesis.speaking) ||
        (currentCloudAudio && !currentCloudAudio.paused && currentPlayingAyatKey === `trans_${ayatKey}`)) {
      stopAllSpeech();
      updateAllAudioButtonStates();
      showToast(t('toastTranslationStopped'));
      return;
    }

    stopAllAudio();

    if (!text || text.trim() === '') {
      showToast(t('toastTranslationNotAvail'));
      return;
    }

    currentPlayingAyatKey = `trans_${ayatKey}`;

    if (buttonEl) {
      buttonEl.classList.add('playing', 'speaking');
      const icon = buttonEl.querySelector('.audio-icon, .audio-icon-state');
      if (icon) icon.innerHTML = '<rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect>';
    }

    showToast(t('toastSpeakingMeaning', surat, ayat));

    function onFinished() {
      currentPlayingAyatKey = null;
      updateAllAudioButtonStates();
    }

    // 1. PERSIAN (FA): Play Studio-quality Human Recitation of Makarem Shirazi translation from EveryAyah
    if (state.lang === 'fa') {
      const s = String(surat).padStart(3, '0');
      const a = String(ayat).padStart(3, '0');
      const makaremUrl = `https://everyayah.com/data/translations/Makarem_Kabiri_16Kbps/${s}${a}.mp3`;
      const fooladvandUrl = `https://everyayah.com/data/translations/Fooladvand_Hedayatfar_40Kbps/${s}${a}.mp3`;

      currentCloudAudio = new Audio(makaremUrl);
      currentCloudAudio.onended = onFinished;
      currentCloudAudio.onerror = () => {
        currentCloudAudio = new Audio(fooladvandUrl);
        currentCloudAudio.onended = onFinished;
        currentCloudAudio.onerror = () => {
          const { speechLangCode, matchVoice } = getSpeechVoiceAndLang('fa');
          if ('speechSynthesis' in window) {
            const cleanText = text.replace(/<[^>]*>/g, '').replace(/[()"]/g, ' ');
            const utterance = new SpeechSynthesisUtterance(normalizeTextForSpeech(cleanText));
            utterance.lang = speechLangCode;
            if (matchVoice) utterance.voice = matchVoice;
            activeUtterance = utterance;
            utterance.onend = onFinished;
            utterance.onerror = onFinished;
            window.speechSynthesis.speak(utterance);
          } else {
            onFinished();
          }
        };
        currentCloudAudio.play().catch(onFinished);
      };
      currentCloudAudio.play().catch(() => {
        currentCloudAudio.onerror();
      });
      return;
    }

    // 2. NATIVE CLOUD TTS FOR LANGUAGES WITHOUT CONFIRMED LOCAL OS VOICE (Turkish, Hausa, Swahili, Dutch, Italian, etc.)
    const { speechLangCode, matchVoice, hasNativeVoice } = getSpeechVoiceAndLang(state.lang);
    if (!hasNativeVoice || state.lang === 'tr' || state.lang === 'ha' || state.lang === 'sw' || state.lang === 'nl' || state.lang === 'it' || state.lang === 'bs' || state.lang === 'sq' || state.lang === 'th' || state.lang === 'ber' || state.lang === 'am' || state.lang === 'az' || state.lang === 'bg' || state.lang === 'cs' || state.lang === 'dv' || state.lang === 'no' || state.lang === 'pl' || state.lang === 'ro' || state.lang === 'sv' || state.lang === 'tg' || state.lang === 'ta' || state.lang === 'tt' || state.lang === 'ug' || state.lang === 'uz' || state.lang === 'ku') {
      const cloudUrls = getGoogleTtsUrls(text, state.lang);
      if (cloudUrls.length > 0) {
        playCloudAudioQueue(cloudUrls, onFinished, () => {
          if ('speechSynthesis' in window) {
            const cleanText = text.replace(/<[^>]*>/g, '').replace(/[()"]/g, ' ');
            const utterance = new SpeechSynthesisUtterance(normalizeTextForSpeech(cleanText));
            utterance.lang = speechLangCode;
            if (matchVoice) utterance.voice = matchVoice;
            activeUtterance = utterance;
            utterance.onend = onFinished;
            utterance.onerror = onFinished;
            window.speechSynthesis.speak(utterance);
          } else {
            onFinished();
          }
        });
        return;
      }
    }

    // 3. OTHER LANGUAGES: Standard Web Speech API with automatic Cloud Fallback
    if ('speechSynthesis' in window) {
      const cleanText = text.replace(/<[^>]*>/g, '').replace(/[()"]/g, ' ');
      const utterance = new SpeechSynthesisUtterance(normalizeTextForSpeech(cleanText));
      utterance.lang = speechLangCode;
      utterance.rate = 0.95;
      if (matchVoice) utterance.voice = matchVoice;
      activeUtterance = utterance;

      utterance.onend = onFinished;
      utterance.onerror = () => {
        const cloudUrls = getGoogleTtsUrls(text, state.lang);
        if (cloudUrls.length > 0) {
          playCloudAudioQueue(cloudUrls, onFinished, onFinished);
        } else {
          onFinished();
        }
      };

      window.speechSynthesis.speak(utterance);
    } else {
      const cloudUrls = getGoogleTtsUrls(text, state.lang);
      if (cloudUrls.length > 0) {
        playCloudAudioQueue(cloudUrls, onFinished, onFinished);
      } else {
        showToast(t('toastTtsNotSupported'));
        onFinished();
      }
    }
  }

  // Comprehensive Arabic Normalizer for precise Quranic matching
  function cleanArabicForHighlight(text) {
    if (!text) return '';
    let t = text.replace(/[\.\d\(\)\[\]_\-ـ\s]/g, '');
    // Remove all tashkeel / harakat / dagger alif / waslah / quranic pause & annotation marks
    t = t.replace(/[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u08D0-\u08FF\u06DF\u06E0\u06E2\u06E5\u06E6]/g, '');
    // Normalize Alef variants
    t = t.replace(/[إأآٱ]/g, 'ا');
    // Normalize Yaa variants
    t = t.replace(/[ىيئ]/g, 'ي');
    // Normalize Waw Hamza & floating Hamza
    t = t.replace(/[ؤ]/g, 'و').replace(/[ء]/g, '');
    // Normalize Taa Marbuta
    t = t.replace(/ة/g, 'ه');
    return t;
  }

  const ARABIC_SPECIAL_EXPANSIONS = {
    // Harf 'Amil Special Word Expansions
    'مِنْ': ['من', 'ومن', 'فمن', 'لمن', 'بمن', 'عمن', 'ممن'],
    'فِي': ['في', 'وفي', 'ففي', 'لفي', 'وفيه', 'فيهم', 'فيها', 'فينا', 'فيكم', 'فيك', 'فيكما', 'فيهما'],
    'عَلَىٰ': ['علي', 'وعلي', 'فعلي', 'لعلي', 'عليه', 'عليهم', 'عليها', 'علينا', 'عليكم', 'عليك', 'عليهما'],
    'إِلَىٰ': ['الي', 'والي', 'فالي', 'اليه', 'اليهم', 'اليها', 'الينا', 'اليكم', 'اليك', 'اليهما'],
    'عَنْ': ['عن', 'وعن', 'فعن', 'عنه', 'عنهم', 'عنها', 'عنا', 'عنكم', 'عنك', 'عنهما'],
    'مِمَّا': ['مما', 'ومما', 'فمما'],
    'عَمَّا 1': ['عما', 'وعما', 'فعما'],
    'عَمَّا 2': ['عما', 'وعما', 'فعما'],
    'عَمَّ': ['عم', 'وعم', 'فعم'],
    'مِمَّن': ['ممن', 'وممن', 'فممن'],
    'مِمَّ': ['مم', 'ومم', 'فمم'],
    'فِيمَا': ['فيما', 'وفيما', 'ففيما'],
    'فِيمَ': ['فيم', 'وفيم', 'ففيم'],
    'حَتَّىٰ 3': ['حتي', 'وحتي', 'فحتي'],
    'حَتَّىٰ 1': ['حتي', 'وحتي', 'فحتي'],
    'حَتَّىٰ': ['حتي', 'وحتي', 'فحتي'],
    'رُّبَمَا': ['ربما', 'وربما', 'فربما'],
    'أَنْ 1': ['ان', 'وان', 'فان', 'بان', 'لان', 'ابان', 'فبان'],
    'أَنْ': ['ان', 'وان', 'فان', 'بان', 'لان'],
    'لَنْ': ['لن', 'ولن', 'فلن'],
    'كَيْ': ['كي', 'وكي', 'فكي', 'لكي', 'ولكي', 'فلكي'],
    'كَيۡلَا': ['كيلا', 'لكيلا', 'ولكيلا', 'فلكيلا'],
    'إِنْ 1': ['ان', 'وان', 'فان', 'ولئن', 'لئن', 'افان'],
    'إِنْ': ['ان', 'وان', 'فان', 'ولئن', 'لئن'],
    'لاَ 2': ['لا', 'ولا', 'فلا'],
    'لاَ': ['لا', 'ولا', 'فلا'],
    'لَمۡ': ['لم', 'ولم', 'فلم', 'الم', 'افلم', 'اولم'],
    'لَّمَّا 2': ['لما', 'ولما', 'فلما'],
    'لَّمَّا': ['لما', 'ولما', 'فلما'],
    'إِلَّا 1': ['الا', 'والا', 'فالا'],
    'إِلَّا 2': ['الا', 'والا', 'فالا'],
    'إِلَّا': ['الا', 'والا', 'فالا'],
    'إِلَّمۡ': ['الم', 'فالم', 'والا', 'فان لم', 'فالم'],
    'ثُمَّ': ['ثم', 'وثم', 'فثم'],
    'أَوْ': ['او', 'واو', 'فاو'],
    'بَلْ': ['بل', 'وبل', 'فبل'],
    'أَمْ': ['ام', 'وام', 'فام'],
    'لَٰكِنْ': ['لكن', 'ولكن', 'فلكن'],
    'إِمَّا 2': ['اما', 'واما', 'فاما'],
    'إِمَّا': ['اما', 'واما', 'فاما'],
    'أَمَّن 1': ['امن', 'وامن', 'فامن'],
    'أَمَّن 2': ['امن', 'وامن', 'فامن'],
    'أَمَّا': ['اما', 'واما', 'فاما'],
    'أَمَّاذَا': ['اماذا', 'واماذا', 'فاماذا'],
    'لَكِنْ أنا': ['لكنا', 'ولكنا', 'لكن انا', 'ولكن انا', 'لكن'],
    'إِنَّ': ['ان', 'وان', 'فان', 'لان', 'وانك', 'وانكم', 'واني', 'وانا', 'وانه', 'وانهم', 'وانهن', 'وانها', 'واننا'],
    'أَنَّ': ['ان', 'وان', 'فان', 'بان', 'لان', 'وانك', 'وانكم', 'واني', 'وانا', 'وانه', 'وانهم', 'وانهن', 'وانها', 'واننا', 'بانه', 'بانهم', 'بانكم'],
    'إِنَّمَا 1': ['انما', 'وانما', 'فانما'],
    'إِنَّمَا 2': ['انما', 'وانما', 'فانما'],
    'لَعَلَّ': ['لعل', 'ولعل', 'فلعل', 'لعله', 'لعلهم', 'لعلكم', 'لعلي', 'لعلنا', 'لعلها'],
    'لَكِنَّ': ['لكن', 'ولكن', 'فلكن', 'ولكنه', 'ولكنهم', 'ولكنكم', 'ولكني', 'ولكننا', 'ولكنها', 'ولكنهن'],
    'كَأَنَّ': ['كان', 'وكان', 'فكان', 'كانه', 'كانهم', 'كانك', 'كانكم', 'كانها', 'كاني', 'كاننا'],
    'لَيْتَ': ['ليت', 'وليت', 'فليت', 'ياليت', 'يا ليت', 'ياليتني', 'ياليتها', 'ياليتنا', 'ياليتهم', 'ياليت قومي'],
    'أَنَّمَا 1': ['انما', 'وانما', 'فانما', 'بانما'],
    'أَنَّمَا 2': ['انما', 'وانما', 'فانما', 'بانما', 'ان', 'ما'],
    'كَأَنَّمَا': ['كانما', 'وكانما', 'فكانما'],
    'أَلَّا 3': ['الا', 'والا', 'فالا', 'ان لا', 'وان لا'],
    'أَلَّا 4': ['الا', 'والا', 'فالا', 'ان لا', 'وان لا'],
    'أَلَّن': ['الن', 'والن', 'فلن', 'ان لن', 'وان لن'],
    'وَيۡكَأَنَّ': ['ويكان', 'فويكان', 'ويكانه', 'ويكانه لا'],
    'أَلَّو': ['الو', 'لو', 'ان', 'وان لو', 'وان لو استقاموا', 'والو'],
    '1b': ['ه', 'هو', 'هي', 'له', 'به', 'منه', 'عنه', 'فيه', 'عليه', 'اليه', 'كتابه', 'ربه', 'عنده', 'دونه', 'بيده', 'قلبه', 'اهله', 'نفسه', 'امره', 'اسمه'],
    '2b': ['هما', 'لهما', 'بهما', 'عنهما', 'منهما', 'فيهما', 'عليهما', 'اليهما', 'بينهما'],
    '3b': ['هم', 'همو', 'لهم', 'بهم', 'عنهم', 'منهم', 'عليهم', 'اليهم', 'فيهم', 'انفسهم', 'قلوبهم', 'اموالهم', 'ديارهم', 'اعمالهم', 'ابصارهم'],
    '4b': ['ها', 'لها', 'بها', 'عنها', 'منها', 'فيها', 'عليها', 'اليها', 'نفسها', 'عينها', 'اثرها'],
    '5b': ['هن', 'لهن', 'بهن', 'عنهن', 'منهن', 'فيهن', 'عليهن', 'اليهن', 'انفسهن', 'بيوتهن'],
    '6b': ['ك', 'لك', 'بك', 'عنك', 'منك', 'فيك', 'عليك', 'اليك', 'ربك', 'نفسك', 'يدك', 'صدرك'],
    '7b': ['كما', 'لكما', 'بكما', 'عنكما', 'منكما', 'فيكما', 'عليكما', 'اليكما', 'ربكما'],
    '8b': ['كم', 'كمو', 'لكم', 'بكم', 'عنكم', 'منكم', 'فيكم', 'عليكم', 'اليكم', 'انفسكم', 'دينكم', 'ربكم', 'اموالكم'],
    '9b': ['ك', 'لك', 'بك', 'عنك', 'منك', 'فيك', 'عليك', 'اليك'],
    '10b': ['كن', 'لكن', 'بكن', 'عنكن', 'منكن', 'فيكن', 'عليكن', 'اليكن'],
    '11b': ['ي', 'ني', 'لي', 'بي', 'عني', 'مني', 'في', 'علي', 'الي', 'ربي', 'صدري', 'امري', 'ديني', 'قومي', 'نفسي'],
    '12b': ['نا', 'لنا', 'بنا', 'عنا', 'منا', 'فينا', 'علينا', 'الينا', 'ربنا', 'انفسنا', 'ديننا', 'الهنا'],
    '11a': ['انا', 'انني', 'وانا', 'فانا'],
    '1a': ['هو', 'وهو', 'فهو', 'لهو'],
    '4a': ['هي', 'وهي', 'فهي', 'لهي'],
    '3a': ['هم', 'وهم', 'فهم', 'لهم'],
    '5a': ['هن', 'وهن', 'فهن'],
    '6a': ['انت', 'وانت', 'فانت'],
    '8a': ['انتم', 'وانتم', 'فانتم'],
    '12a': ['نحن', 'ونحن', 'فنحن'],
    'اللاَّتِي': ['اللاتي', 'التي', 'والاتي', 'والتي'],
    'اللائِي': ['اللائي', 'اللاي', 'الاي', 'الي', 'اللاءي', 'والائي', 'والي'],
    'اللَّذَانِ': ['اللذان', 'اللذين', 'الذان', 'الذين', 'والذان', 'والذين', 'الذن', 'والذن', 'اللذن'],
    'الَّذِينَ': ['الذين', 'والذين', 'فالذين', 'للذين'],
    'الَّذِي': ['الذي', 'والذي', 'فالذي', 'للذي', 'كالذي'],
    'الَّتِي': ['التي', 'والتي', 'فالتي', 'للتي'],
    'أَيّ 2': ['اي', 'بايك', 'ايكم', 'ايهم', 'فايهم', 'وايهم'],
    'أَيّ': ['اي', 'بايك', 'ايكم', 'ايهم', 'فايهم', 'وايهم'],
    'ذَا': ['ذا', 'هذا', 'ذلك', 'كذلك', 'فذلك', 'وكذلك', 'فذلكم', 'ذلكم', 'هذا'],
    'أُولاَءِ': ['اولاء', 'هولاء', 'اوليك', 'اولىك', 'فاوليك', 'واوليك', 'هاولاء'],
    'هَٰذَٰنِ': ['هذان', 'فذانك', 'ذانك', 'هذين', 'ذينك', 'ذنك', 'فذنك', 'هذن'],
    'تَانِ': ['تان', 'تانك', 'هاتين', 'هتين'],
    'هَٰذَا': ['هذا', 'فهذا', 'وهذا', 'بهذا', 'لهذا'],
    'ذَٰلِكَ': ['ذلك', 'فذلك', 'وذلك', 'كذلك', 'بذلك', 'لذلك', 'ذلكم'],
    'تِلْكَ': ['تلك', 'فتلك', 'وتلك', 'كتلك'],
    'هَٰؤُلَاءِ': ['هولاء', 'هاولاء', 'فهولاء', 'وهولاء'],
    'سُبْحَانَ': ['سبحان', 'فسبحان', 'سبحانه', 'سبحانك', 'سبحن', 'فسبحن'],
    'أُمُ': ['هاوم', 'هاؤم', 'هاام', 'هاوءم'],
    'لَيْسَ': ['ليس', 'لست', 'لسنا', 'ليسوا', 'ليست', 'لستم', 'لستن', 'وليس', 'فليس'],
    'نِعْمَ': ['نعم', 'فنعما', 'نعما', 'ولنعم'],
    'بِئْسَ': ['بئس', 'فبئس', 'ولبئس', 'بئسما'],
    'عَسَى': ['عسى', 'فعسى', 'وعسى'],
    'سَاءَ': ['ساء', 'وساء', 'فساء'],
    'تَبَارَكَ': ['تبارك', 'فتبارك']
  };

  // Arabic Target Word Highlight (Guaranteed 100% coverage across all 486 Quranic entries)
  function highlightArabicVerse(fullArabText, targetKata, noKata) {
    if (!fullArabText || !targetKata) return fullArabText || '';
    
    const tokens = new Set();
    const cleanK = cleanArabicForHighlight(targetKata);

    // 1. Check special expansion by targetKata
    Object.keys(ARABIC_SPECIAL_EXPANSIONS).forEach(expK => {
      if (targetKata.includes(expK) || expK === targetKata || cleanArabicForHighlight(expK) === cleanK) {
        ARABIC_SPECIAL_EXPANSIONS[expK].forEach(x => tokens.add(cleanArabicForHighlight(x)));
      }
    });

    // 2. Add individual parts separated by slash or space
    const parts = targetKata.split(/[/,\s]+/);
    parts.forEach(p => {
      const cl = cleanArabicForHighlight(p);
      if (cl && cl.length >= 1) tokens.add(cl);
    });

    const tokenList = Array.from(tokens).filter(t => Boolean(t));
    if (tokenList.length === 0) return fullArabText;

    const words = fullArabText.split(/\s+/);
    const highlightedWords = words.map(w => {
      const cleanW = cleanArabicForHighlight(w);
      let isMatch = false;

      for (let i = 0; i < tokenList.length; i++) {
        const tok = tokenList[i];
        if (cleanW === tok || (tok.length >= 2 && (cleanW.endsWith(tok) || cleanW.startsWith(tok) || cleanW.includes(tok)))) {
          isMatch = true;
          break;
        }
      }

      if (isMatch) {
        return `<span class="ayat-highlight-red">${w}</span>`;
      }
      return w;
    });

    return highlightedWords.join(' ');
  }

  // Render Ayat References in Grand Single-Ayat Screen Presentation
  function renderAyatReferences(groupOverride, queryOverride) {
    const group = groupOverride || getGroup(state.selectedBentuk, state.selectedNoKata);

    if (!elements.ayatGridContainer) return;
    elements.ayatGridContainer.innerHTML = '';

    if (!group || !group.occurrences || group.occurrences.length === 0) {
      if (elements.referencesSection) elements.referencesSection.style.display = 'none';
      return;
    }

    if (elements.referencesSection) elements.referencesSection.style.display = 'block';

    // Clean parentheses from word meaning
    const rawArti = getGroupArti(group, state.lang);
    const cleanArti = rawArti.replace(/^\((.*)\)$/, '$1');

    // Section title
    if (elements.ayatSectionTitle) {
      elements.ayatSectionTitle.innerHTML = `
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
          <polyline points="14 2 14 8 20 8"></polyline>
          <line x1="16" y1="13" x2="8" y2="13"></line>
          <line x1="16" y1="17" x2="8" y2="17"></line>
          <polyline points="10 9 9 9 8 9"></polyline>
        </svg>
        <span>${t('referencesTitlePrefix')} ${group.kata} (${cleanArti})</span>
      `;
    }

    // Filter occurrences by search query
    const q = (queryOverride !== undefined ? queryOverride : state.searchQuery).trim().toLowerCase();
    let filtered = group.occurrences;
    if (q) {
      filtered = group.occurrences.filter(occ => {
        const sNama = (occ.suratNama || '').toLowerCase();
        const sArti = getOccSuratArti(occ, state.lang).toLowerCase();
        const tArti = getOccTeksArti(occ, state.lang).toLowerCase();
        const sNum = String(occ.surat);
        const aNum = String(occ.ayat);
        return sNama.includes(q) || sArti.includes(q) || tArti.includes(q) || sNum === q || aNum === q || `${sNum}:${aNum}` === q;
      });
    }

    if (filtered.length === 0) {
      if (elements.emptyStateContainer) elements.emptyStateContainer.style.display = 'block';
      if (elements.emptyStateText) elements.emptyStateText.textContent = t('emptyStateText');
      return;
    } else {
      if (elements.emptyStateContainer) elements.emptyStateContainer.style.display = 'none';
    }

    const totalCount = filtered.length;
    if (state.currentAyatIndex >= totalCount) {
      state.currentAyatIndex = 0;
    }
    const currentIdx = state.currentAyatIndex;
    const occ = filtered[currentIdx];

    const singleScreenWrap = document.createElement('div');
    singleScreenWrap.className = 'single-ayat-screen animate-fade-in';

    // 1. Navigation Tabs & Arrows Toolbar
    const navBar = document.createElement('div');
    navBar.className = 'ayat-nav-toolbar';

    let tabsHtml = '';
    filtered.forEach((item, idx) => {
      const isActive = idx === currentIdx ? 'active' : '';
      tabsHtml += `
        <button type="button" class="ayat-select-tab ${isActive}" data-idx="${idx}" aria-label="Ayat ke-${idx + 1}">
          <span class="tab-number">${idx + 1}</span>
          <span>${item.suratNama} : ${item.ayat}</span>
        </button>
      `;
    });

    navBar.innerHTML = `
      <div class="ayat-tab-group">
        ${tabsHtml}
      </div>
    `;

    // 2. Grand Unified Verse Card
    const cardWrapper = document.createElement('div');
    cardWrapper.className = 'single-ayat-card-wrapper';

    const activeSuratArti = getOccSuratArti(occ, state.lang);
    const activeTeksArti = getOccTeksArti(occ, state.lang);
    const highlightedArab = highlightArabicVerse(occ.teksArab, group.kata, group.noKata);

    cardWrapper.innerHTML = `
      <div class="single-ayat-unified-card animate-fade-in">
        <div class="ayat-top-row">
          <div class="surat-identity-badge">
            <div>
              <div class="surat-main-name">
                ${occ.suratNama} 
                <span class="surat-meaning-bracket">${activeSuratArti ? '(' + activeSuratArti + ')' : ''}</span>
              </div>
              <div class="ayat-position-tag">${t('surahPositionTag', currentIdx + 1, occ.surat, occ.ayat)}</div>
            </div>
          </div>

          <div class="ayat-badge-actions">
            <!-- Audio Murottal Tilawah -->
            <button type="button" class="btn-play-verse-audio" data-surat="${occ.surat}" data-ayat="${occ.ayat}" data-audio="${occ.audioUrl || ''}" title="${t('playTilawahBtn')} (Mishary Alafasy)" aria-label="Putar Tilawah QS. ${occ.surat}:${occ.ayat}">
              <svg class="audio-icon-state" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <polygon points="5 3 19 12 5 21 5 3"></polygon>
              </svg>
            </button>

            <!-- Tombol Tanya AI -->
            <button type="button" class="btn-ask-ai" data-surat="${occ.surat}" data-ayat="${occ.ayat}" title="${t('askAiTooltip')}" aria-label="${t('askAiTooltip')}">
              <span class="ai-sparkle-icon">✨</span>
              <span>${t('askAiBtn')}</span>
            </button>
          </div>
        </div>

        <div class="ayat-body-content">
          <!-- 1. Teks Arab Penuh dengan Red Highlight -->
          <div class="arabic-verse-container notranslate" translate="no">
            <div class="single-ayat-arabic-text font-arabic notranslate" translate="no" dir="rtl">
              ${highlightedArab}
            </div>
          </div>

          <!-- 2. Terjemahan Ayat dengan Tombol Audio Suara -->
          <div class="verse-translation-box">
            <div class="translation-content-row">
              <blockquote class="single-ayat-translation">
                "${activeTeksArti || 'Translation loading...'}"
              </blockquote>
              <button type="button" class="btn-play-translation-audio" data-surat="${occ.surat}" data-ayat="${occ.ayat}" title="${t('meaningVoiceTooltip')}" aria-label="${t('meaningVoiceTooltip')}">
                <svg class="audio-icon-state" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <polygon points="5 3 19 12 5 21 5 3"></polygon>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    `;

    // Audio Play Buttons inside card (Murottal Tilawah)
    cardWrapper.querySelectorAll('.btn-play-verse-audio').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const surat = btn.getAttribute('data-surat');
        const ayat = btn.getAttribute('data-ayat');
        const audioUrl = btn.getAttribute('data-audio');
        toggleVerseAudio(surat, ayat, audioUrl, btn);
      });
    });

    // Ask AI Button inside card
    cardWrapper.querySelectorAll('.btn-ask-ai').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        openAiModal(occ.surat, occ.ayat, group.kata, group.noKata, group.bentuk);
      });
    });

    // Audio Translation Buttons inside card
    cardWrapper.querySelectorAll('.btn-play-translation-audio').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        toggleVerseTranslationAudio(occ.surat, occ.ayat, activeTeksArti, btn);
      });
    });

    // Tab buttons event
    navBar.querySelectorAll('.ayat-select-tab').forEach(tab => {
      tab.addEventListener('click', (e) => {
        const targetIdx = parseInt(tab.getAttribute('data-idx'), 10);
        if (!isNaN(targetIdx) && targetIdx !== state.currentAyatIndex) {
          state.currentAyatIndex = targetIdx;
          stopAllAudio();
          renderAyatReferences(group, state.searchQuery);
        }
      });
    });

    // Assemble and mount
    singleScreenWrap.appendChild(navBar);
    singleScreenWrap.appendChild(cardWrapper);
    elements.ayatGridContainer.appendChild(singleScreenWrap);
  }

  // Select Bentuk Kata
  function selectBentuk(bentuk) {
    state.selectedBentuk = bentuk;
    if (elements.bentukKataSelect) {
      elements.bentukKataSelect.value = bentuk || '';
    }
    
    populateNoKataDropdown();

    const activeList = noKatasByBentuk[bentuk] || [];
    if (activeList.length > 0) {
      selectNoKata(activeList[0]);
    } else {
      selectNoKata('');
    }
  }

  // Select No Kata
  function selectNoKata(noKata) {
    state.selectedNoKata = noKata;
    if (elements.noKataSelect) {
      elements.noKataSelect.value = noKata || '';
    }
    state.searchQuery = '';
    if (elements.ayatSearchInput) elements.ayatSearchInput.value = '';

    stopAllAudio();
    updateSpotlightCard();
    renderAyatReferences();
  }

  // Apply Language Change across entire app
  function applyLanguage(lang) {
    state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa', 'ja', 'ko', 'nl', 'it', 'bs', 'sq', 'th', 'ber', 'am', 'az', 'bg', 'cs', 'dv', 'no', 'pl', 'ro', 'sv', 'tg', 'ta', 'tt', 'ug', 'uz', 'ku'].includes(lang) ? lang : 'id';
    localStorage.setItem('dhamir_lang', state.lang);

    if (elements.langSelect) {
      elements.langSelect.value = state.lang;
    }

    // Set HTML lang and dir attribute
    document.documentElement.lang = state.lang;
    if (state.lang === 'ur' || state.lang === 'fa' || state.lang === 'dv' || state.lang === 'ug' || state.lang === 'ku') {
      document.documentElement.setAttribute('dir', 'rtl');
    } else {
      document.documentElement.removeAttribute('dir');
    }

    // Update document & brand titles
    updateHeaderTitles();

    // Update Static UI Labels
    if (elements.labelLangSelect) elements.labelLangSelect.textContent = t('labelLangSelect');
    if (elements.translationSourceText) elements.translationSourceText.innerHTML = t('translationSourceHtml');
    if (elements.themeToggleBtn) elements.themeToggleBtn.setAttribute('title', t('themeToggleTitle'));

        if (elements.labelTabJamid) elements.labelTabJamid.textContent = t('brandTitle').replace(/<[^>]*>/g, '');
    if (elements.frekSubtitle) elements.frekSubtitle.textContent = t('freqSub') || 'Frekuensi Kemunculan';
    if (elements.labelTotalAyatSub) elements.labelTotalAyatSub.textContent = t('totalAyatSub') || 'Tersedia dalam Dataset';
    if (elements.emptyStateText) elements.emptyStateText.textContent = t('emptyStateText') !== 'emptyStateText' ? t('emptyStateText') : 'Tidak ada surat atau ayat yang cocok dengan kata pencarian tersebut.';

    if (elements.badgeTabJamid) elements.badgeTabJamid.textContent = t('tabBadgeJamid') || '7 Bentuk Kata';
    if (elements.labelTabHarf) elements.labelTabHarf.textContent = (state.lang === 'en' ? "Harf Ghair 'Amil" : (state.lang === 'tr' ? "Gayr-i Âmil Harfler" : "Kamus Harf Ghair 'Amil"));
    if (elements.badgeTabHarf) elements.badgeTabHarf.textContent = t('tabBadgeHarf') || '17 Bentuk Harf';
    if (elements.labelTabHarfAmil) elements.labelTabHarfAmil.textContent = (state.lang === 'en' ? "Harf 'Amil Dictionary" : (state.lang === 'tr' ? "Âmil Harfler" : "Kamus Harf 'Amil"));
    if (elements.badgeTabHarfAmil) elements.badgeTabHarfAmil.textContent = (state.lang === 'en' ? '6 Categories' : (state.lang === 'tr' ? '6 Kategori' : '6 Bentuk Harf'));

    // Update Blue Optgroup Regional Headers in #langSelect
    if (elements.langSelect) {
      const optgroups = elements.langSelect.querySelectorAll('optgroup');
      if (optgroups.length >= 5) {
        optgroups[0].label = t('optgroupEastAsia') || '🌏 Asia Tenggara & Asia Timur';
        optgroups[1].label = t('optgroupMidEast') || '🕌 Timur Tengah, Asia Tengah & Kaukasus';
        optgroups[2].label = t('optgroupSouthAsia') || '🪷 Asia Selatan & Samudra Hindia';
        optgroups[3].label = t('optgroupAfrica') || '🌍 Afrika';
        optgroups[4].label = t('optgroupEurope') || '🏛️ Eropa Barat, Utara, Tengah & Timur';
      }
    }

    // Spotlight buttons
    if (elements.labelAudioArab) elements.labelAudioArab.textContent = t('arabicVoiceBtn');
    if (elements.btnAudioPlay) elements.btnAudioPlay.setAttribute('title', t('arabicVoiceTooltip'));

    if (elements.labelAudioMeaning) elements.labelAudioMeaning.textContent = t('meaningVoiceBtn');
    if (elements.btnAudioMeaning) elements.btnAudioMeaning.setAttribute('title', t('meaningVoiceTooltip'));

    if (elements.btnCopyArabic) elements.btnCopyArabic.setAttribute('title', t('copyArabicTooltip'));
    if (elements.btnCopyAll) elements.btnCopyAll.setAttribute('title', t('copyInfoTooltip'));

    if (elements.labelExportCsv) elements.labelExportCsv.textContent = t('exportCsvBtn');
    if (elements.btnExportCsv) elements.btnExportCsv.setAttribute('title', t('exportCsvTooltip'));

        if (elements.ayatSearchInput) {
      elements.ayatSearchInput.setAttribute('placeholder', t('searchPlaceholder') !== 'searchPlaceholder' ? t('searchPlaceholder') : 'Cari nama surat / ayat...');
    }
    if (elements.ayatSectionTitle && (!state.selectedBentuk || !state.selectedNoKata)) {
      elements.ayatSectionTitle.innerHTML = `
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
          <polyline points="14 2 14 8 20 8"></polyline>
          <line x1="16" y1="13" x2="8" y2="13"></line>
          <line x1="16" y1="17" x2="8" y2="17"></line>
          <polyline points="10 9 9 9 8 9"></polyline>
        </svg>
        <span></span>
      `;
    }



    // Update Kamus Musytaq UI Labels
    if (elements.labelTabMusytaq) elements.labelTabMusytaq.textContent = getMusytaqI18n('tabTitle');
    if (elements.badgeTabMusytaq) elements.badgeTabMusytaq.textContent = getMusytaqI18n('tabBadge');
    if (elements.labelMusytaqMetricRoot) elements.labelMusytaqMetricRoot.textContent = getMusytaqI18n('metricRootTitle');
    if (elements.labelMusytaqMetricFreq) elements.labelMusytaqMetricFreq.textContent = getMusytaqI18n('metricFreqTitle');
    if (elements.labelMusytaqMetricFreqSub) elements.labelMusytaqMetricFreqSub.textContent = getMusytaqI18n('metricFreqSub');
    if (elements.labelMusytaqMetricTasrif) elements.labelMusytaqMetricTasrif.textContent = getMusytaqI18n('metricTasrifTitle');
    if (elements.labelMusytaqMetricTasrifSub) elements.labelMusytaqMetricTasrifSub.textContent = getMusytaqI18n('metricTasrifSub');
    if (elements.labelMusytaqMorphologyTitle) elements.labelMusytaqMorphologyTitle.textContent = getMusytaqI18n('morphologyTitle');
    if (elements.labelMusytaqWazanTitle) elements.labelMusytaqWazanTitle.textContent = getMusytaqI18n('wazanTitle');
    if (elements.labelMusytaqAsalTitle) elements.labelMusytaqAsalTitle.textContent = getMusytaqI18n('asalTitle');
    if (elements.labelMusytaqBabTitle) elements.labelMusytaqBabTitle.textContent = getMusytaqI18n('babTitle');
    if (elements.labelMusytaqGrammarTitle) elements.labelMusytaqGrammarTitle.textContent = getMusytaqI18n('grammarTitle');
    if (elements.labelMusytaqIlalTitle) elements.labelMusytaqIlalTitle.textContent = getMusytaqI18n('ilalTitle');
    if (elements.chipAllText) elements.chipAllText.textContent = getMusytaqI18n('chipAll');
    if (elements.chipMadhiText) elements.chipMadhiText.textContent = getMusytaqI18n('chipMadhi');
    if (elements.chipMudhariText) elements.chipMudhariText.textContent = getMusytaqI18n('chipMudhari');
    if (elements.chipAmrText) elements.chipAmrText.textContent = getMusytaqI18n('chipAmr');
    if (elements.chipMasdarText) elements.chipMasdarText.textContent = getMusytaqI18n('chipMasdar');
    if (elements.chipIsimText) elements.chipIsimText.textContent = getMusytaqI18n('chipIsim');
    if (elements.musytaqSearchInput) elements.musytaqSearchInput.setAttribute('placeholder', getMusytaqI18n('searchPlaceholder'));
    if (elements.musytaqEmptyStateText) elements.musytaqEmptyStateText.textContent = getMusytaqI18n('emptyStateText');

    if (state.activeDict === 'musytaq') {
      populateMusytaqLevelDropdown();
      populateMusytaqAkarDropdown();
      populateMusytaqTasrifDropdown();
      renderMusytaqSpotlight();
      renderMusytaqTasrifGrid();
      return;
    }

    // Re-populate dropdowns and re-render cards
    populateBentukDropdown();
    populateNoKataDropdown();
    updateSpotlightCard();
    renderAyatReferences();
  }

  // Apply Theme ('dark' | 'light')
  function applyTheme(theme) {
    state.theme = theme;
    localStorage.setItem('dhamir_theme', theme);
    document.documentElement.setAttribute('data-theme', theme);

    if (elements.themeIcon) {
      if (theme === 'light') {
        elements.themeIcon.innerHTML = `
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
          </svg>`;
      } else {
        elements.themeIcon.innerHTML = `
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="5"></circle>
            <line x1="12" y1="1" x2="12" y2="3"></line>
            <line x1="12" y1="21" x2="12" y2="23"></line>
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
            <line x1="1" y1="12" x2="3" y2="12"></line>
            <line x1="21" y1="12" x2="23" y2="12"></line>
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
          </svg>`;
      }
    }
  }

  // Toast Notification System
  let toastTimer = null;
  function showToast(msg) {
    if (!elements.toastNotification) return;
    elements.toastNotification.textContent = msg;
    elements.toastNotification.classList.add('show');

    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      elements.toastNotification.classList.remove('show');
    }, 3500);
  }

  // AI Prompt Builder with Clean Multilingual Dispatch
  function buildAiPrompt(topic, surat, ayat, kata, noKata, bentuk, teksArab, teksArti, grammarDesc) {
    const suratNama = currentAiContext.suratNama;

    switch (state.lang) {
      case 'bs':
        if (topic === 'nahwu') {
          return `Molimo navedite detaljnu gramatičku analizu (Nahv/Sarf) i I'rab za riječ "${kata}" (${noKata}, ${bentuk}) u suri ${suratNama} (${surat}), ajet ${ayat}:\n\nArapski tekst: "${teksArab}"\nPrijevod na bosanski: "${teksArti}"\n\nMolimo obuhvatite sljedeće:\n1. Sintaktičku ulogu (položaj u I'rabu) riječi "${kata}" u ovoj rečenici (Merfu'/Mensub/Medžrur).\n2. Morfološku vrstu (Dhamir / Mawshul / itd.) i svojstva (Munfasil / Muttasil).\n3. Gramatičko objašnjenje: ${grammarDesc || "U skladu s pravilima klasičnog arapskog jezika Kur'ana"}.`;
        } else if (topic === 'tafsir') {
          return `Molimo navedite sažet i poučan tefsir za suru ${suratNama} (${surat}), ajet ${ayat}:\n\nArapski tekst: "${teksArab}"\nPrijevod na bosanski: "${teksArti}"\n\nS fokusom na riječ "${kata}": Koja je mudrost, povod objave (sebeb-i nuzul ako postoji) i poruke koje ovaj ajet nosi za život vjernika?`;
        } else {
          return `Molimo objasnite belagat (retoričku ljepotu i stilsku preciznost Kur'ana) u vezi s izborom riječi "${kata}" u suri ${suratNama} (${surat}), ajet ${ayat}:\n\nArapski tekst: "${teksArab}"\nPrijevod na bosanski: "${teksArti}"\n\nZašto je baš ova riječ/zamjenica upotrijebljena u ovom kontekstu i koju dubinu značenja daje ovom ajetu?`;
        }

      case 'az':
        if (topic === 'nahwu') {
          return `Zəhmət olmasa "${kata}" (${noKata}, ${bentuk}) sözü üçün ${suratNama} (${surat}) surəsinin ${ayat}-ci ayəsində ətraflı ərəb qrammatik (Nəhv/Sərf) və İrab təhlilini təqdim edin:\n\nƏrəb Mətni: "${teksArab}"\nAzərbaycanca Tərcümə: "${teksArti}"\n\nZəhmət olmasa aşağıdakıları qeyd edin:\n1. "${kata}" sözünün bu cümlədəki sintaktik mövqeyi (İrabı) (Mərfu/Mənsub/Məcrur).\n2. Morfoloji növü (Zəmir / Mövsul və s.) və xüsusiyyətləri (Münfəsil / Müttəsil).\n3. Qrammatik izah: ${grammarDesc || "Klassik Quran ərəb dilinin qrammatika qaydalarına əsasən"}.`;
        } else if (topic === 'tafsir') {
          return `Zəhmət olmasa ${suratNama} (${surat}) surəsi, ${ayat}-ci ayə üçün xülasə və dərin təfsir izahı təqdim edin:\n\nƏrəb Mətni: "${teksArab}"\nAzərbaycanca Tərcümə: "${teksArti}"\n\nXüsusilə "${kata}" sözünə diqqət yetirərək: Hikməti, nazil olma səbəbi (əgər varsa, əsbabun-nüzul) və möminlər üçün verdiyi dərslər nələrdir?`;
        } else {
          return `Zəhmət olmasa ${suratNama} (${surat}) surəsi, ${ayat}-ci ayədə "${kata}" sözünün seçilməsi ilə bağlı bəlağəti (Quranın ritorik və ədəbi gözəlliyini) izah edin:\n\nƏrəb Mətni: "${teksArab}"\nAzərbaycanca Tərcümə: "${teksArti}"\n\nNiyə bu kontekstdə məhz bu söz/əvəzlik işlədilmişdir və ayəyə hansı dərin mənanı qatır?`;
        }

      case 'bg':
        if (topic === 'nahwu') {
          return `Моля, направете подробен арабски граматичен (Наху/Сарф) и И'раб анализ за думата "${kata}" (${noKata}, ${bentuk}) в сура ${suratNama} (${surat}), знамение ${ayat}:\n\nАрабски текст: "${teksArab}"\nБългарски превод: "${teksArti}"\n\nМоля, включете следните точки:\n1. Синтактична роля (позиция в И'раб) на думата "${kata}" в това изречение (Марфу'/Мансуб/Маджрур).\n2. Морфологичен вид (Дамир / Маусул и т.н.) и свойства (Мунфасил / Муттасил).\n3. Граматично обяснение: ${grammarDesc || "Според класическите правила на коранския арабски език"}.`;
        } else if (topic === 'tafsir') {
          return `Моля, предоставете стегнато и дълбоко тафсир обяснение за сура ${suratNama} (${surat}), знамение ${ayat}:\n\nАрабски текст: "${teksArab}"\nБългарски превод: "${teksArti}"\n\nС фокус върху думата "${kata}": Каква е мъдростта, поводът за низпославане (асбаб ан-нузул, ако има) и поуките за вярващите?`;
        } else {
          return `Моля, разяснете балагата (коранското красноречие и естетическа красота) относно избора на думата "${kata}" в сура ${suratNama} (${surat}), знамение ${ayat}:\n\nАрабски текст: "${teksArab}"\nБългарски превод: "${teksArti}"\n\nЗащо точно тази дума/местоимение е употребена в този контекст и каква смислова дълбочина придава на знамението?`;
        }

      case 'ber':
        if (topic === 'nahwu') {
          return `Ttxil-k fker-d asleḍ ajerruman (Naḥw/Ṣarf) d I'rab leqqayen i wawal "${kata}" (${noKata}, ${bentuk}) deg tsurat ${suratNama} (${surat}), taseddart ${ayat}:\n\nAḍris Aɛrab: "${teksArab}"\nTasuqilt s Tmaziɣt: "${teksArti}"\n\nTtxil-k sfehem-d:\n1. Addad deg tjerrumt (I'rab) n wawal "${kata}" deg tefyirt-agi (Marfu'/Manshub/Majrur).\n2. Tawsit n wawal (Dhamir / Mawshul / atg.) d waddad-is (Munfashil / Muttashil).\n3. Asegzi n tjerrumt: ${grammarDesc || "Ilmend n yilugan n tutlayt taɛrabt n Leqran"}.`;
        } else if (topic === 'tafsir') {
          return `Ttxil-k fker-d asegzi d lmeɛna (Tafsir) yelhan i tsurat ${suratNama} (${surat}), taseddart ${ayat}:\n\nAḍris Aɛrab: "${teksArab}"\nTasuqilt s Tmaziɣt: "${teksArti}"\n\nS usekcem n wawal "${kata}": D acu i d tamsirt, sebba n trusi (asbab nuzul ma yella) d lfeṭna i yimumnen?`;
        } else {
          return `Ttxil-k sfehem-d tasekla d cbaḥa n wawal (Balaɣah) deg ufran n wawal "${kata}" deg tsurat ${suratNama} (${surat}), taseddart ${ayat}:\n\nAḍris Aɛrab: "${teksArab}"\nTasuqilt s Tmaziɣt: "${teksArti}"\n\nAcuɣer i d-yettwaferren wawal-agi deg wadeg-agi d wamek i yesnerna lmeɛna n tseddart?`;
        }

      case 'am':
        if (topic === 'nahwu') {
          return `እባክዎ ለቃል "${kata}" (${noKata}፣ ${bentuk}) በሱራ ${suratNama} (${surat}) አንቀጽ ${ayat} ውስጥ ዝርዝር የአረብኛ ሰዋሰዋዊ ትንተና (ነሕው/ሶርፍ) እና ኢዕራብ ይስጡ:\n\nየአረብኛ ጽሑፍ: "${teksArab}"\nየአማርኛ ትርጉም: "${teksArti}"\n\nእባክዎ የሚከተሉትን ያካትቱ:\n1. የቃሉ "${kata}" ሰዋሰዋዊ ቦታ (ኢዕራብ) በዚህ ዓረፍተ-ነገር ውስጥ (መርፉዕ/መንሱብ/መጅሩር)።\n2. የቃሉ ዓይነት (ዳሚር/መውሱል ወዘተ) እና ባህሪው (ሙንፈሲል/ሙተሲል)።\n3. ሰዋሰዋዊ ማብራሪያ: ${grammarDesc || "በጥንታዊ የቁርኣን አረብኛ ሰዋሰው ሕጎች መሠረት"}።`;
        } else if (topic === 'tafsir') {
          return `እባክዎ ለሱራ ${suratNama} (${surat}) አንቀጽ ${ayat} አጭርና ጥልቅ ተፍሲር (ማብራሪያ) ይስጡ:\n\nየአረብኛ ጽሑፍ: "${teksArab}"\nየአማርኛ ትርጉም: "${teksArti}"\n\nበተለይ በቃሉ "${kata}" ላይ በማተኮር: ጥበቡ፣ የወረደበት ምክንያት (አስባቡን ኑዙል ካለ) እና ለምእመናን የሚሰጠው ትምህርት ምንድን ነው?`;
        } else {
          return `እባክዎ በሱራ ${suratNama} (${surat}) አንቀጽ ${ayat} ውስጥ ቃል "${kata}" የተመረጠበትን የበላጋህ (የአንደበተ-ርቱዕነትና ውበት) ምስጢር ያብራሩ:\n\nየአረብኛ ጽሑፍ: "${teksArab}"\nየአማርኛ ትርጉም: "${teksArti}"\n\nይህ ቃል በዚህ አውድ ውስጥ ለምን ተመረጠ፣ ለአንቀጹስ ምን ዓይነት ጥልቅ ትርጉም ጨመረ?`;
        }

      case 'th':
        if (topic === 'nahwu') {
          return `กรุณาวิเคราะห์หลักไวยากรณ์ภาษาอาหรับ (นะฮ์วู/ศ็อรฟ์) และอิอ์รอบอย่างละเอียดสำหรับคำว่า "${kata}" (${noKata}, ${bentuk}) ในซูเราะฮ์ ${suratNama} (${surat}) อายะฮ์ที่ ${ayat}:\n\nข้อความภาษาอาหรับ: "${teksArab}"\nคำแปลภาษาไทย: "${teksArti}"\n\nโปรดระบุประเด็นต่อไปนี้:\n1. ตำแหน่งทางไวยากรณ์ (อิอ์รอบ) ของคำว่า "${kata}" ในประโยคนี้ (มัรฟูอ์/มันศูบ/มัจญ์รูร)\n2. ชนิดของคำทางสัณฐานวิทยา (ฎอมี้ร์ / เมาศูล ฯลฯ) และคุณลักษณะ (มุนฟะศิล / มุตตะศิล)\n3. คำอธิบายทางไวยากรณ์: ${grammarDesc || "ตามหลักไวยากรณ์ภาษาอาหรับคลาสสิกของอัลกุรอาน"}`;
        } else if (topic === 'tafsir') {
          return `กรุณาอธิบายตัฟซีร (ความหมายและคำอธิบาย) โดยสรุปและลึกซึ้งสำหรับซูเราะฮ์ ${suratNama} (${surat}) อายะฮ์ที่ ${ayat}:\n\nข้อความภาษาอาหรับ: "${teksArab}"\nคำแปลภาษาไทย: "${teksArti}"\n\nโดยเน้นที่คำว่า "${kata}": อะไรคือวิทยปัญญา สาเหตุของการประทานลงมา (อัสบาบุนนุซูล หากมี) และบทเรียนสำหรับผู้ศรัทธา?`;
        } else {
          return `กรุณาอธิบายบาลาเฆาะฮ์ (ความงดงามเชิงโวหารและวรรณศิลป์) ของการเลือกใช้คำว่า "${kata}" ในซูเราะฮ์ ${suratNama} (${surat}) อายะฮ์ที่ ${ayat}:\n\nข้อความภาษาอาหรับ: "${teksArab}"\nคำแปลภาษาไทย: "${teksArti}"\n\nเหตุใดจึงใช้คำ/สรรพนามนี้ในบริบทนี้ และช่วยเพิ่มความหมายอันลึกซึ้งแก่อายะฮ์อย่างไร?`;
        }

      case 'sq':
        if (topic === 'nahwu') {
          return `Ju lutemi jepni një analizë të hollësishme gramatikore arabe (Nahw/Sarf) dhe I'rab për fjalën "${kata}" (${noKata}, ${bentuk}) në suren ${suratNama} (${surat}), ajeti ${ayat}:\n\nTeksti Arabisht: "${teksArab}"\nPërkthimi Shqip: "${teksArti}"\n\nJu lutemi përfshini pikat e mëposhtme:\n1. Roli sintaktik (pozicioni në I'rab) i fjalës "${kata}" në këtë fjali (Marfu'/Manshub/Majrur).\n2. Lloji morfologjik (Dhamir / Mawshul / etj.) dhe veçoritë (Munfashil / Muttashil).\n3. Shënime gramatikore: ${grammarDesc || "Sipas rregullave klasike të gjuhës arabe kur'anore"}.`;
        } else if (topic === 'tafsir') {
          return `Ju lutemi jepni një tefsir të përmbledhur dhe domethënës për suren ${suratNama} (${surat}), ajeti ${ayat}:\n\nTeksti Arabisht: "${teksArab}"\nPërkthimi Shqip: "${teksArti}"\n\nMe fokus te fjala "${kata}": Cila është urtësia, shkaku i zbritjes (asbabun nuzul nëse ka) dhe mësimet që ky ajet përcjell për besimtarët?`;
        } else {
          return `Ju lutemi shpjegoni balagën (bukurinë retorike dhe stilistike kur'anore) lidhur me zgjedhjen e fjalës "${kata}" në suren ${suratNama} (${surat}), ajeti ${ayat}:\n\nTeksti Arabisht: "${teksArab}"\nPërkthimi Shqip: "${teksArti}"\n\nPërse u përdor pikërisht kjo fjalë/përemër në këtë kontekst dhe çfarë thellësie kuptimore i shton ajetit?`;
        }

      case 'fa':
        if (topic === 'nahwu') {
          return `لطفاً نکات صرفی، نحوی (قواعد زبان عربی) و اعراب کلمه «${kata}» (${noKata}, ${bentuk}) در سوره ${suratNama} (${surat})، آیه ${ayat} را به طور جامع تحلیل فرمایید:\n\nمتن عربی آیه: «${teksArab}»\nترجمه فارسی آیه: «${teksArti}»\n\nلطفاً موارد زیر را بررسی نمایید:\n۱. نقش نحوی، محل اعراب و کارکرد «${kata}» در این جمله (مرفوع / منصوب / مجرور).\n۲. نوع کلمه (ضمیر / موصول / ادوات شرط و غیره) و ویژگی‌های ساختاری آن (منفصل / متصل).\n۳. توضیحات تکمیلی نحوی: ${grammarDesc || "بر اساس قواعد بلاغی و ادبی قرآن کریم"}.`;
        } else if (topic === 'tafsir') {
          return `لطفاً تفسیر و شرحی پرمحتوا و مختصر درباره سوره ${suratNama} (${surat})، آیه ${ayat} ارائه فرمایید:\n\nمتن عربی آیه: «${teksArab}»\nترجمه فارسی آیه: «${teksArti}»\n\nبا تمرکز بر مفهوم و کارکرد کلمه «${kata}»: چه حکمت، شأن نزول (در صورت وجود) و پیام‌های هدایت‌بخشی در این آیه برای زندگی مؤمنان نهفته است؟`;
        } else {
          return `لطفاً زیبایی‌های بلاغی و اعجاز ادبی قرآن کریم (فصاحت، ایجاز و صنایع ادبی) در خصوص انتخاب کلمه «${kata}» در سوره ${suratNama} (${surat})، آیه ${ayat} را تبیین فرمایید:\n\nمتن عربی آیه: «${teksArab}»\nترجمه فارسی آیه: «${teksArti}»\n\nچرا این واژه یا ضمیر در این بافت خاص به کار رفته و چه عمق معنایی و ظرافتی به آیه بخشیده است؟`;
        }

      case 'sw':
        if (topic === 'nahwu') {
          return `Tafadhali fafanua kanuni za nahau (Nahwu/Sarf) na I'rabu kuhusu neno "${kata}" (${noKata}, ${bentuk}) katika Sura ${suratNama} (${surat}), Aya ${ayat}:\n\nMaandishi ya Kiarabu: "${teksArab}"\nTafsiri ya Kiswahili: "${teksArti}"\n\nTafadhali chambua vipengele vifuatavyo:\n1. Nafasi ya i'rabu na kazi ya "${kata}" katika sentensi hii (Marfu' / Manshub / Majrur).\n2. Aina ya neno (Dhamir / Mawshul / nk.) na sifa zake (Munfashil / Muttashil).\n3. Maelezo ya ziada ya kisarufi: ${grammarDesc || "Kulingana na kanuni za lugha ya Qur'ani"}.`;
        } else if (topic === 'tafsir') {
          return `Tafadhali toa muhtasari wa tafsiri yenye manufaa kuhusu Sura ${suratNama} (${surat}), Aya ${ayat}:\n\nMaandishi ya Kiarabu: "${teksArab}"\nTafsiri ya Kiswahili: "${teksArti}"\n\nUkiwa na msisitizo maalum juu ya neno "${kata}": Je, kuna hekima gani, sababu ya kuteremka aya (asbabun nuzul ikiwa ipo), na mafunzo gani ambayo aya hii inatoa kwa maisha ya waumini?`;
        } else {
          return `Tafadhali fafanua uzuri wa lugha na balagha ya Qur'ani (I'jaz na ufasaha wa maneno) kuhusiana na uteuzi wa neno "${kata}" katika Sura ${suratNama} (${surat}), Aya ${ayat}:\n\nMaandishi ya Kiarabu: "${teksArab}"\nTafsiri ya Kiswahili: "${teksArti}"\n\nKwa nini neno hili au kiwakilishi hiki kilitumika hapa? Je, kinaongeza kina gani cha maana na uzuri wa usemi katika muktadha wa aya hii?`;
        }

      case 'ha':
        if (topic === 'nahwu') {
          return `Da fatan za a yi cikakken bayanin ƙa'idojin nahawu (Nahwu/Sarf) da I'rabi game da kalmar "${kata}" (${noKata}, ${bentuk}) a cikin Surah ${suratNama} (${surat}), Aya ${ayat}:\n\nNassin Larabci: "${teksArab}"\nFassarar Hausa: "${teksArti}"\n\nDa fatan a duba waɗannan abubuwan:\n1. Matsayin i'rabi da aikin "${kata}" a cikin wannan jumla (Marfu' / Manshub / Majrur).\n2. Nau'in kalmar (Dhamir / Mawshul / da sauransu) da siffofinta (Munfashil / Muttashil).\n3. Ƙarin bayanin nahawu: ${grammarDesc || "Bisa ƙa'idar yaren Al-Ƙur'ani"}.`;
        } else if (topic === 'tafsir') {
          return `Da fatan a bayar da taƙaitaccen tafsiri mai fa'ida game da Surah ${suratNama} (${surat}), Aya ${ayat}:\n\nNassin Larabci: "${teksArab}"\nFassarar Hausa: "${teksArti}"\n\nTare da mai da hankali kan ma'anar kalmar "${kata}": Wace hikima, asalin saukar aya (asbabun nuzul idan akwai), da koyarwar da wannan aya ke isarwa ga rayuwar muminai?`;
        } else {
          return `Da fatan a bayyana balagar Al-Ƙur'ani (I'jaz da adon magana) dangane da zaɓin kalmar "${kata}" a cikin Surah ${suratNama} (${surat}), Aya ${ayat}:\n\nNassin Larabci: "${teksArab}"\nFassarar Hausa: "${teksArti}"\n\nMe ya sa aka yi amfani da wannan kalma ko damiri a nan? Wane zurfin ma'ana da kyawon lafazi take ƙarawa ga ayar?`;
        }

      case 'pt':
        if (topic === 'nahwu') {
          return `Por favor, faça uma análise gramatical árabe detalhada (Nahwu/Sarf) e I'rab sobre a palavra "${kata}" (${noKata}, ${bentuk}) na Surata ${suratNama} (${surat}), Versículo ${ayat}:\n\nTexto Árabe: "${teksArab}"\nTradução em Português: "${teksArti}"\n\nPor favor, aborde os seguintes pontos:\n1. Posição sintática (I'rab) e função de "${kata}" na oração (Marfu'/Manshub/Majrur).\n2. Classificação morfológica (Dhamir / Mawshul / etc.) e propriedades (Munfashil / Muttashil).\n3. Explicações gramaticais adicionais: ${grammarDesc || "De acordo com as regras gramaticais clássicas do Alcorão"}.`;
        } else if (topic === 'tafsir') {
          return `Por favor, forneça uma explicação contextual e Tafsir conciso sobre a Surata ${suratNama} (${surat}), Versículo ${ayat}:\n\nTexto Árabe: "${teksArab}"\nTradução em Português: "${teksArti}"\n\nCom foco no significado da palavra "${kata}": Qual é a sabedoria, o contexto da revelação (asbab an-nuzul, se aplicável) e as lições práticas que este versículo transmite?`;
        } else {
          return `Por favor, elucide os aspectos de Balaghah (eloquência e recursos estilísticos corânicos) relacionados à escolha da palavra "${kata}" na Surata ${suratNama} (${surat}), Versículo ${ayat}:\n\nTexto Árabe: "${teksArab}"\nTradução em Português: "${teksArti}"\n\nPor que esse termo ou pronome específico foi empregado aqui e que profundidade de significado ele confere ao versículo?`;
        }

      case 'en':
        if (topic === 'nahwu') {
          return `Please provide a detailed Arabic grammatical (Nahwu/Sarf) and I'rab analysis for the word "${kata}" (${noKata}, ${bentuk}) in Surah ${suratNama} (${surat}), Ayah ${ayat}:\n\nArabic Text: "${teksArab}"\nEnglish Translation: "${teksArti}"\n\nPlease cover:\n1. The grammatical role (I'rab position) of "${kata}" in this sentence (Marfu'/Manshub/Majrur).\n2. Morphological type (Dhamir / Mawshul / etc.) and attributes (Munfashil / Muttashil).\n3. Grammar notes: ${grammarDesc || "Based on Classical Quranic Arabic rules"}.`;
        } else if (topic === 'tafsir') {
          return `Please provide a concise and insightful Tafsir explanation for Surah ${suratNama} (${surat}), Ayah ${ayat}:\n\nArabic Text: "${teksArab}"\nEnglish Translation: "${teksArti}"\n\nFocusing on the word "${kata}": What is the wisdom, context of revelation (asbab an-nuzul if any), and lessons conveyed for believers?`;
        } else {
          return `Please explain the Balaghah (eloquence, rhetorical beauty, and stylistic precision) regarding the choice of the word "${kata}" in Surah ${suratNama} (${surat}), Ayah ${ayat}:\n\nArabic Text: "${teksArab}"\nEnglish Translation: "${teksArti}"\n\nWhy was this specific pronoun/word used in this context, and what subtle depth does it add to the Ayah?`;
        }

      default:
        // Indonesian (Default)
        if (topic === 'nahwu') {
          return `Tolong jelaskan analisis kaidah tata bahasa Arab (Nahwu/Shorof) dan I'rob secara mendalam mengenai kata "${kata}" (${noKata}, ${bentuk}) pada Surat ${suratNama} (${surat}) Ayat ${ayat}:\n\nTeks Arab: "${teksArab}"\nTerjemahan: "${teksArti}"\n\nMohon sertakan:\n1. Kedudukan i'rob kata "${kata}" dalam kalimat tersebut (Marfu'/Manshub/Majrur).\n2. Jenis kata (Dhamir / Mawshul / dsb) dan statusnya (Munfashil / Muttashil).\n3. Penjelasan kaidah: ${grammarDesc || "Sesuai kaidah bahasa Al-Qur'an"}.`;
        } else if (topic === 'tafsir') {
          return `Tolong berikan penjelasan tafsir ringkas dan kontekstual mengenai Surat ${suratNama} (${surat}) Ayat ${ayat}:\n\nTeks Arab: "${teksArab}"\nTerjemahan: "${teksArti}"\n\nFokus pada kata "${kata}": Apa hikmah, asbabun nuzul (jika ada), dan pelajaran utama yang dapat diambil oleh seorang muslim dari ayat ini?`;
        } else {
          return `Tolong jelaskan keindahan balaghah (sastra dan uslub Al-Qur'an) terkait pemilihan kata "${kata}" pada Surat ${suratNama} (${surat}) Ayat ${ayat}:\n\nTeks Arab: "${teksArab}"\nTerjemahan: "${teksArti}"\n\nMengapa kata/dhamir ini yang digunakan pada konteks ayat tersebut dan apa rahasia keindahan maknanya?`;
        }
    }
  }

  // Open AI Modal
  function openAiModal(surat, ayat, kata, noKata, bentuk) {
    const group = getGroup(state.selectedBentuk, state.selectedNoKata);
    const occ = group ? group.occurrences.find(o => o.surat === surat && o.ayat === ayat) : null;

    currentAiContext.surat = surat;
    currentAiContext.ayat = ayat;
    currentAiContext.kata = kata;
    currentAiContext.noKata = noKata;
    currentAiContext.bentuk = bentuk;
    currentAiContext.suratNama = occ ? occ.suratNama : `Surat ${surat}`;
    currentAiContext.teksArab = occ ? occ.teksArab : '';
    currentAiContext.teksArti = occ ? getOccTeksArti(occ, state.lang) : '';
    currentAiContext.grammarDesc = group ? getGroupDesc(group, state.lang) : '';
    currentAiContext.topic = 'nahwu';

    if (elements.aiModalTitle) elements.aiModalTitle.textContent = t('aiModalTitle');
    if (elements.aiModalSubtitle) elements.aiModalSubtitle.textContent = t('aiModalSubtitle', currentAiContext.suratNama, ayat, kata, noKata);
    if (elements.labelAiTopic) elements.labelAiTopic.textContent = t('aiTopicLabel');
    if (elements.labelPromptPreview) elements.labelPromptPreview.textContent = t('aiPromptPreviewLabel');
    if (elements.labelOpenGemini) elements.labelOpenGemini.textContent = t('aiOpenGemini');
    if (elements.labelOpenChatGpt) elements.labelOpenChatGpt.textContent = t('aiOpenChatGpt');
    if (elements.labelCopyPrompt) elements.labelCopyPrompt.textContent = t('aiCopyPrompt');

    if (elements.aiModalArabicVerse) elements.aiModalArabicVerse.textContent = currentAiContext.teksArab;
    if (elements.aiModalTranslation) elements.aiModalTranslation.textContent = currentAiContext.teksArti;

    const topicChips = elements.aiTopicChips ? elements.aiTopicChips.querySelectorAll('.ai-topic-chip') : [];
    topicChips.forEach(chip => {
      chip.classList.remove('active');
      const topicType = chip.getAttribute('data-topic');
      if (topicType === 'nahwu') chip.textContent = t('aiTopicNahwu');
      if (topicType === 'tafsir') chip.textContent = t('aiTopicTafsir');
      if (topicType === 'balaghah') chip.textContent = t('aiTopicBalaghah');
      if (topicType === 'nahwu') chip.classList.add('active');
    });

    updateAiModalPrompt();

    if (elements.aiModal) {
      elements.aiModal.classList.add('open');
      elements.aiModal.setAttribute('aria-hidden', 'false');
    }
  }

  // Close AI Modal
  function closeAiModal() {
    if (elements.aiModal) {
      elements.aiModal.classList.remove('open');
      elements.aiModal.setAttribute('aria-hidden', 'true');
    }
  }

  // Update AI Modal Prompt Preview
  function updateAiModalPrompt() {
    if (!elements.aiPromptTextarea) return;
    const prompt = buildAiPrompt(
      currentAiContext.topic,
      currentAiContext.surat,
      currentAiContext.ayat,
      currentAiContext.kata,
      currentAiContext.noKata,
      currentAiContext.bentuk,
      currentAiContext.teksArab,
      currentAiContext.teksArti,
      currentAiContext.grammarDesc
    );
    elements.aiPromptTextarea.value = prompt;
  }

  function openInGemini() {
    if (!elements.aiPromptTextarea) return;
    const prompt = elements.aiPromptTextarea.value;
    const url = `https://gemini.google.com/app?prompt=${encodeURIComponent(prompt)}`;
    window.open(url, '_blank');
  }

  function openInChatGpt() {
    if (!elements.aiPromptTextarea) return;
    const prompt = elements.aiPromptTextarea.value;
    const url = `https://chatgpt.com/?q=${encodeURIComponent(prompt)}`;
    window.open(url, '_blank');
  }

  function copyAiPrompt() {
    if (!elements.aiPromptTextarea) return;
    const prompt = elements.aiPromptTextarea.value;
    navigator.clipboard.writeText(prompt).then(() => {
      showToast(t('toastPromptCopied'));
    }).catch(() => {
      showToast('Gagal menyalin prompt.');
    });
  }

  // Export to CSV
  function exportToCsv() {
    const group = getGroup(state.selectedBentuk, state.selectedNoKata);
    if (!group || !group.occurrences || group.occurrences.length === 0) {
      showToast('Tidak ada data untuk diekspor.');
      return;
    }

    const headers = [
      'Surat', 'Nama Surat', 'Ayat', 'Kata Arab', 'No Kata', 'Bentuk Kata',
      'Arti (ID)', 'Arti (EN)', 'Arti (MS)', 'Arti (FR)', 'Arti (DE)',
      'Arti (UR)', 'Arti (HI)', 'Arti (BN)', 'Arti (RU)', 'Arti (ZH)',
      'Arti (ES)', 'Arti (TR)', 'Arti (PT)', 'Arti (HA)', 'Arti (SW)', 'Arti (FA)', 'Arti (JA)', 'Arti (KO)', 'Arti (NL)', 'Arti (IT)', 'Arti (BS)', 'Arti (SQ)', 'Arti (TH)', 'Arti (BER)', 'Arti (AM)', 'Arti (AZ)', 'Arti (BG)', 'Arti (CS)', 'Arti (DV)', 'Arti (NO)', 'Arti (PL)', 'Arti (RO)', 'Arti (SV)', 'Arti (TG)', 'Arti (TA)', 'Arti (TT)', 'Arti (UG)', 'Arti (UZ)', 'Arti (KU)',
      'Frekuensi', 'Teks Arab', 'Teks Latin',
      'Terjemahan (ID)', 'Terjemahan (EN)', 'Terjemahan (MS)', 'Terjemahan (FR)', 'Terjemahan (DE)',
      'Terjemahan (UR)', 'Terjemahan (HI)', 'Terjemahan (BN)', 'Terjemahan (RU)', 'Terjemahan (ZH)',
      'Terjemahan (ES)', 'Terjemahan (TR)', 'Terjemahan (PT)', 'Terjemahan (HA)', 'Terjemahan (SW)', 'Terjemahan (FA)', 'Terjemahan (JA)', 'Terjemahan (KO)', 'Terjemahan (NL)', 'Terjemahan (IT)', 'Terjemahan (BS)', 'Terjemahan (SQ)', 'Terjemahan (TH)', 'Terjemahan (BER)', 'Terjemahan (AM)', 'Terjemahan (AZ)', 'Terjemahan (BG)', 'Terjemahan (CS)', 'Terjemahan (DV)', 'Terjemahan (NO)', 'Terjemahan (PL)', 'Terjemahan (RO)', 'Terjemahan (SV)', 'Terjemahan (TG)', 'Terjemahan (TA)', 'Terjemahan (TT)', 'Terjemahan (UG)', 'Terjemahan (UZ)', 'Terjemahan (KU)'
    ];

    const rows = group.occurrences.map(occ => {
      const cleanField = str => `"${(str || '').replace(/"/g, '""')}"`;
      return [
        occ.surat,
        cleanField(occ.suratNama),
        occ.ayat,
        cleanField(group.kata),
        cleanField(group.noKata),
        cleanField(group.bentuk),
        cleanField(group.arti_id),
        cleanField(group.arti_en),
        cleanField(group.arti_ms),
        cleanField(group.arti_fr),
        cleanField(group.arti_de),
        cleanField(group.arti_ur),
        cleanField(group.arti_hi),
        cleanField(group.arti_bn),
        cleanField(group.arti_ru),
        cleanField(group.arti_zh),
        cleanField(group.arti_es),
        cleanField(group.arti_tr),
        cleanField(group.arti_pt),
        cleanField(group.arti_ha),
        cleanField(group.arti_sw),
        cleanField(group.arti_fa),
        cleanField(group.arti_ja),
        cleanField(group.arti_ko),
        cleanField(group.arti_nl),
        cleanField(group.arti_it),
        cleanField(group.arti_bs),
        cleanField(group.arti_sq),
        cleanField(group.arti_th),
        cleanField(group.arti_ber),
        cleanField(group.arti_am),
        cleanField(group.arti_az),
        cleanField(group.arti_bg),
        cleanField(group.arti_cs),
        cleanField(group.arti_dv),
        cleanField(group.arti_no),
        cleanField(group.arti_pl),
        cleanField(group.arti_ro),
        cleanField(group.arti_sv),
        cleanField(group.arti_tg),
        cleanField(group.arti_ta),
        cleanField(group.arti_tt),
        cleanField(group.arti_ug),
        cleanField(group.arti_uz),
        cleanField(group.arti_ku),
        cleanField(group.frek ? `${group.frek}x` : 'Muttashil'),
        cleanField(occ.teksArab),
        cleanField(occ.teksLatin),
        cleanField(occ.teksArtiID),
        cleanField(occ.teksArtiEN),
        cleanField(occ.teksArtiMS),
        cleanField(occ.teksArtiFR),
        cleanField(occ.teksArtiDE),
        cleanField(occ.teksArtiUR),
        cleanField(occ.teksArtiHI),
        cleanField(occ.teksArtiBN),
        cleanField(occ.teksArtiRU),
        cleanField(occ.teksArtiZH),
        cleanField(occ.teksArtiES),
        cleanField(occ.teksArtiTR),
        cleanField(occ.teksArtiPT),
        cleanField(occ.teksArtiHA),
        cleanField(occ.teksArtiSW),
        cleanField(occ.teksArtiFA),
        cleanField(occ.teksArtiJA),
        cleanField(occ.teksArtiKO),
        cleanField(occ.teksArtiNL),
        cleanField(occ.teksArtiIT),
        cleanField(occ.teksArtiBS),
        cleanField(occ.teksArtiSQ),
        cleanField(occ.teksArtiTH),
        cleanField(occ.teksArtiBER),
        cleanField(occ.teksArtiAM),
        cleanField(occ.teksArtiAZ),
        cleanField(occ.teksArtiBG),
        cleanField(occ.teksArtiCS),
        cleanField(occ.teksArtiDV),
        cleanField(occ.teksArtiNO),
        cleanField(occ.teksArtiPL),
        cleanField(occ.teksArtiRO),
        cleanField(occ.teksArtiSV),
        cleanField(occ.teksArtiTG),
        cleanField(occ.teksArtiTA),
        cleanField(occ.teksArtiTT),
        cleanField(occ.teksArtiUG),
        cleanField(occ.teksArtiUZ),
        cleanField(occ.teksArtiKU)
      ].join(',');
    });

    const csvContent = '\uFEFF' + headers.join(',') + '\n' + rows.join('\n');
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.setAttribute('href', url);
    link.setAttribute('download', `Dhamir_${group.noKata}_${group.kata}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    showToast(t('toastCsvExported', group.noKata));
  }


  // ============================================================================
  // KAMUS MUSYTAQ LOGIC & RENDERING FUNCTIONS
  // ============================================================================

  function getMusytaqDataset() {
    if (typeof MUSYTAQ_DATA !== 'undefined' && MUSYTAQ_DATA && MUSYTAQ_DATA.levels) {
      return MUSYTAQ_DATA;
    }
    return { levels: [] };
  }

  function getMusytaqLevelObj(lvl) {
    const data = getMusytaqDataset();
    const lInt = parseInt(lvl, 10) || 1;
    return data.levels.find(l => l.level === lInt) || data.levels[0] || null;
  }

  function getMusytaqAkarObj(lvl, noAkar) {
    const lvlObj = getMusytaqLevelObj(lvl);
    if (!lvlObj || !lvlObj.roots) return null;
    const nInt = parseInt(noAkar, 10) || 1;
    return lvlObj.roots.find(r => r.no_akar === nInt) || lvlObj.roots[0] || null;
  }

  function getMusytaqTasrifObj(lvl, noAkar, tasrifIdx) {
    const akarObj = getMusytaqAkarObj(lvl, noAkar);
    if (!akarObj || !akarObj.tasrif_list) return null;
    const idx = parseInt(tasrifIdx, 10) || 0;
    return akarObj.tasrif_list[idx] || akarObj.tasrif_list[0] || null;
  }

  function populateMusytaqLevelDropdown() {
    if (!elements.musytaqLevelSelect) return;
    const data = getMusytaqDataset();
    elements.musytaqLevelSelect.innerHTML = '';
    
    const rootUnit = getMusytaqI18n('levelUnit') || 'Akar Kata';

    if (!data.levels || data.levels.length === 0) {
      elements.musytaqLevelSelect.innerHTML = `<option value="1">Level 1 (80 ${rootUnit})</option>`;
      return;
    }

    data.levels.forEach(lvl => {
      const opt = document.createElement('option');
      opt.value = lvl.level;
      opt.textContent = `${lvl.level_name} (${lvl.total_roots} ${rootUnit})`;
      if (lvl.level === state.selectedMusytaqLevel) {
        opt.selected = true;
      }
      elements.musytaqLevelSelect.appendChild(opt);
    });
  }

  function populateMusytaqAkarDropdown() {
    if (!elements.musytaqAkarSelect) return;
    const lvlObj = getMusytaqLevelObj(state.selectedMusytaqLevel);
    const placeholder = getMusytaqI18n('akarSelectPlaceholder') || 'Pilih Nomor Akar & Akar';
    const tasrifUnit = getMusytaqI18n('tasrifUnit') || 'Bentuk';
    elements.musytaqAkarSelect.innerHTML = `<option value="">${placeholder}</option>`;
    
    if (!lvlObj || !lvlObj.roots) return;

    const lang = state.lang || 'id';

    lvlObj.roots.forEach(root => {
      const opt = document.createElement('option');
      opt.value = root.no_akar;
      const dasarTxt = root.dasar ? ` (${root.dasar})` : '';
      const artiStr = (root.arti_akar_multilingual && (root.arti_akar_multilingual[lang] || root.arti_akar_multilingual['en'])) || root.arti_akar || '';
      const artiTxt = artiStr ? ` - ${artiStr}` : '';
      opt.textContent = `${root.no_akar}. ${root.akar}${dasarTxt}${artiTxt} [${root.tasrif_count} ${tasrifUnit}]`;
      if (root.no_akar === state.selectedMusytaqAkarNo) {
        opt.selected = true;
      }
      elements.musytaqAkarSelect.appendChild(opt);
    });

    elements.musytaqAkarSelect.disabled = false;
  }

  function populateMusytaqTasrifDropdown() {
    if (!elements.musytaqTasrifSelect) return;
    const akarObj = getMusytaqAkarObj(state.selectedMusytaqLevel, state.selectedMusytaqAkarNo);
    const placeholder = getMusytaqI18n('tasrifSelectPlaceholder') || 'Pilih Tasrif';
    elements.musytaqTasrifSelect.innerHTML = `<option value="">${placeholder}</option>`;
    
    if (!akarObj || !akarObj.tasrif_list || akarObj.tasrif_list.length === 0) {
      elements.musytaqTasrifSelect.disabled = true;
      return;
    }

    const lang = state.lang || 'id';

    elements.musytaqTasrifSelect.disabled = false;
    akarObj.tasrif_list.forEach((t, idx) => {
      const opt = document.createElement('option');
      opt.value = idx;
      const artiTxt = t.arti_lafaz ? ` : ${t.arti_lafaz}` : '';
      const katStr = (t.kategori_multilingual && (t.kategori_multilingual[lang] || t.kategori_multilingual['en'])) || t.kategori || '';
      const katTxt = katStr ? ` (${katStr})` : '';
      opt.textContent = `[${t.tasrif}] ${t.lafaz}${artiTxt}${katTxt}`;
      if (idx === state.selectedMusytaqTasrifIndex) {
        opt.selected = true;
      }
      elements.musytaqTasrifSelect.appendChild(opt);
    });
  }

  function selectMusytaqLevel(lvl) {
    state.selectedMusytaqLevel = parseInt(lvl, 10) || 1;
    populateMusytaqAkarDropdown();
    const lvlObj = getMusytaqLevelObj(state.selectedMusytaqLevel);
    if (lvlObj && lvlObj.roots.length > 0) {
      selectMusytaqAkar(lvlObj.roots[0].no_akar);
    }
  }

  function selectMusytaqAkar(noAkar) {
    state.selectedMusytaqAkarNo = parseInt(noAkar, 10) || 1;
    state.selectedMusytaqTasrifIndex = 0;
    state.musytaqSearchQuery = '';
    state.musytaqCategoryFilter = 'all';
    if (elements.musytaqSearchInput) elements.musytaqSearchInput.value = '';

    populateMusytaqTasrifDropdown();
    renderMusytaqSpotlight();
    renderMusytaqTasrifGrid();
  }

  function selectMusytaqTasrif(index) {
    state.selectedMusytaqTasrifIndex = parseInt(index, 10) || 0;
    if (elements.musytaqTasrifSelect) {
      elements.musytaqTasrifSelect.value = state.selectedMusytaqTasrifIndex;
    }
    renderMusytaqSpotlight();
    
    if (elements.musytaqTasrifGrid) {
      const cards = elements.musytaqTasrifGrid.querySelectorAll('.tasrif-card');
      cards.forEach(card => {
        const cardIdx = parseInt(card.getAttribute('data-index'), 10);
        if (cardIdx === state.selectedMusytaqTasrifIndex) {
          card.classList.add('active');
        } else {
          card.classList.remove('active');
        }
      });
    }
  }

  function renderMusytaqSpotlight() {
    const rootObj = getMusytaqAkarObj(state.selectedMusytaqLevel, state.selectedMusytaqAkarNo);
    const tasrifObj = getMusytaqTasrifObj(state.selectedMusytaqLevel, state.selectedMusytaqAkarNo, state.selectedMusytaqTasrifIndex);

    if (!rootObj || !tasrifObj) {
      if (elements.musytaqDisplaySection) elements.musytaqDisplaySection.style.display = 'none';
      return;
    }

    if (elements.musytaqDisplaySection) elements.musytaqDisplaySection.style.display = 'block';

    const lang = state.lang || 'id';
    const rootMeaning = (rootObj.arti_akar_multilingual && (rootObj.arti_akar_multilingual[lang] || rootObj.arti_akar_multilingual['en'])) || rootObj.arti_akar || '-';
    const kategoriName = (tasrifObj.kategori_multilingual && (tasrifObj.kategori_multilingual[lang] || tasrifObj.kategori_multilingual['en'])) || tasrifObj.kategori || 'Tasrif';
    const babName = (tasrifObj.bab_multilingual && (tasrifObj.bab_multilingual[lang] || tasrifObj.bab_multilingual['en'])) || tasrifObj.bab || 'Tsulatsi Mujarrad';
    const subjekName = (tasrifObj.subjek_multilingual && (tasrifObj.subjek_multilingual[lang] || tasrifObj.subjek_multilingual['en'])) || tasrifObj.subjek || '';
    const suaraName = (tasrifObj.suara_multilingual && (tasrifObj.suara_multilingual[lang] || tasrifObj.suara_multilingual['en'])) || tasrifObj.suara || '';
    const irabName = (tasrifObj.irab_multilingual && (tasrifObj.irab_multilingual[lang] || tasrifObj.irab_multilingual['en'])) || tasrifObj.irab || '';

    // Badges
    if (elements.musytaqBadgeLevel) elements.musytaqBadgeLevel.textContent = `Level ${rootObj.level}`;
    if (elements.musytaqBadgeAkar) elements.musytaqBadgeAkar.textContent = `No. ${rootObj.no_akar} (${rootObj.akar})`;
    if (elements.musytaqBadgeTasrifCode) elements.musytaqBadgeTasrifCode.textContent = tasrifObj.tasrif;
    if (elements.musytaqBadgeKategori) {
      elements.musytaqBadgeKategori.textContent = kategoriName;
    }

    // Arabic Word & Subtitle
    if (elements.musytaqArabicWord) elements.musytaqArabicWord.textContent = tasrifObj.lafaz || rootObj.dasar || '-';
    if (elements.musytaqWordMeaning) elements.musytaqWordMeaning.textContent = tasrifObj.arti_lafaz || rootMeaning || '-';
    if (elements.musytaqWordSub) {
      const subParts = [];
      if (kategoriName) subParts.push(kategoriName);
      if (subjekName) subParts.push(subjekName);
      if (suaraName) subParts.push(suaraName);
      if (irabName) subParts.push(irabName);
      elements.musytaqWordSub.textContent = subParts.join(' • ') || tasrifObj.label || '';
    }

    // Root info
    if (elements.musytaqRootDisplay) {
      const dasar = rootObj.dasar ? ` (${rootObj.dasar})` : '';
      elements.musytaqRootDisplay.textContent = `${rootObj.akar}${dasar}`;
    }
    if (elements.musytaqRootMeaning) {
      const prefix = getMusytaqI18n('rootMeaningPrefix') || 'Arti Akar';
      elements.musytaqRootMeaning.textContent = `${prefix}: ${rootMeaning}`;
    }
    if (elements.musytaqFreqDisplay) {
      elements.musytaqFreqDisplay.textContent = rootObj.frekuensi ? `${rootObj.frekuensi.toLocaleString()} ×` : '-';
    }
    if (elements.musytaqTotalTasrifBadge) {
      const unit = getMusytaqI18n('tasrifUnit') || 'Bentuk';
      elements.musytaqTotalTasrifBadge.textContent = `${rootObj.tasrif_count || rootObj.tasrif_list.length} ${unit}`;
    }

    // Morphology & Sharaf Card
    if (elements.musytaqWazanDisplay) {
      elements.musytaqWazanDisplay.textContent = tasrifObj.wazan || '-';
    }
    if (elements.musytaqAsalDisplay && elements.musytaqAsalContainer) {
      if (tasrifObj.asal && tasrifObj.asal.trim() !== '') {
        elements.musytaqAsalContainer.style.display = 'block';
        elements.musytaqAsalDisplay.textContent = tasrifObj.asal;
      } else {
        elements.musytaqAsalContainer.style.display = 'none';
      }
    }
    if (elements.musytaqBabDisplay) {
      elements.musytaqBabDisplay.textContent = babName;
    }
    if (elements.musytaqGrammarDetailDisplay) {
      const gParts = [];
      if (subjekName) gParts.push(subjekName);
      if (suaraName) gParts.push(suaraName);
      if (irabName) gParts.push(irabName);
      if (tasrifObj.definiteness) gParts.push(tasrifObj.definiteness);
      elements.musytaqGrammarDetailDisplay.textContent = gParts.join(' • ') || '-';
    }

    // Kaidah I'lal
    if (elements.musytaqIlalContainer && elements.musytaqIlalText) {
      if (tasrifObj.ilal && tasrifObj.ilal.trim() !== '') {
        elements.musytaqIlalContainer.style.display = 'block';
        elements.musytaqIlalText.textContent = tasrifObj.ilal;
      } else {
        elements.musytaqIlalContainer.style.display = 'none';
      }
    }

    // Table Title
    if (elements.musytaqTasrifTableTitle) {
      const titlePrefix = getMusytaqI18n('tasrifTableTitlePrefix') || 'Daftar Lengkap Seluruh Bentuk Tasrif Akar';
      const unit = getMusytaqI18n('tasrifUnit') || 'Bentuk';
      elements.musytaqTasrifTableTitle.textContent = `${titlePrefix}: ${rootObj.akar} (${rootObj.tasrif_count} ${unit})`;
    }
  }

  function renderMusytaqTasrifGrid() {
    const rootObj = getMusytaqAkarObj(state.selectedMusytaqLevel, state.selectedMusytaqAkarNo);
    if (!rootObj || !rootObj.tasrif_list || !elements.musytaqTasrifGrid) return;

    const list = rootObj.tasrif_list;
    const lang = state.lang || 'id';

    // Counts for Category Filter Chips
    let cAll = list.length;
    let cMadhi = 0, cMudhari = 0, cAmr = 0, cMasdar = 0, cIsim = 0;

    list.forEach(t => {
      const kat = (t.kategori || '').toLowerCase();
      if (kat.includes('madhi')) cMadhi++;
      else if (kat.includes('mudhari')) cMudhari++;
      else if (kat.includes('amr')) cAmr++;
      else if (kat.includes('masdar')) cMasdar++;
      else if (kat.includes('isim')) cIsim++;
    });

    const setBadgeText = (id, val) => {
      const el = document.getElementById(id);
      if (el) el.textContent = val;
    };
    setBadgeText('countCatAll', cAll);
    setBadgeText('countCatMadhi', cMadhi);
    setBadgeText('countCatMudhari', cMudhari);
    setBadgeText('countCatAmr', cAmr);
    setBadgeText('countCatMasdar', cMasdar);
    setBadgeText('countCatIsim', cIsim);

    // Update active filter chip class
    if (elements.musytaqCategoryChips) {
      elements.musytaqCategoryChips.querySelectorAll('.tasrif-chip').forEach(chip => {
        if (chip.getAttribute('data-cat') === state.musytaqCategoryFilter) {
          chip.classList.add('active');
        } else {
          chip.classList.remove('active');
        }
      });
    }

    const q = (state.musytaqSearchQuery || '').trim().toLowerCase();
    const filterCat = state.musytaqCategoryFilter || 'all';

    const filtered = list.filter(t => {
      const kat = (t.kategori || '').toLowerCase();
      if (filterCat === 'madhi' && !kat.includes('madhi')) return false;
      if (filterCat === 'mudhari' && !kat.includes('mudhari')) return false;
      if (filterCat === 'amr' && !kat.includes('amr')) return false;
      if (filterCat === 'masdar' && !kat.includes('masdar')) return false;
      if (filterCat === 'isim' && !kat.includes('isim')) return false;

      if (!q) return true;
      const katMulti = (t.kategori_multilingual && (t.kategori_multilingual[lang] || t.kategori_multilingual['en'])) || '';
      const subjekMulti = (t.subjek_multilingual && (t.subjek_multilingual[lang] || t.subjek_multilingual['en'])) || '';
      return (
        (t.tasrif && t.tasrif.toLowerCase().includes(q)) ||
        (t.lafaz && t.lafaz.toLowerCase().includes(q)) ||
        (t.arti_lafaz && t.arti_lafaz.toLowerCase().includes(q)) ||
        (t.wazan && t.wazan.toLowerCase().includes(q)) ||
        (t.asal && t.asal.toLowerCase().includes(q)) ||
        (t.subjek && t.subjek.toLowerCase().includes(q)) ||
        (katMulti && katMulti.toLowerCase().includes(q)) ||
        (subjekMulti && subjekMulti.toLowerCase().includes(q)) ||
        (t.label && t.label.toLowerCase().includes(q))
      );
    });

    elements.musytaqTasrifGrid.innerHTML = '';

    if (filtered.length === 0) {
      if (elements.musytaqEmptyState) elements.musytaqEmptyState.style.display = 'block';
      return;
    }

    if (elements.musytaqEmptyState) elements.musytaqEmptyState.style.display = 'none';

    const selectHintText = getMusytaqI18n('selectHint') || 'Pilih ➔';

    filtered.forEach(item => {
      const card = document.createElement('div');
      card.className = `tasrif-card animate-fade-in ${item.index === state.selectedMusytaqTasrifIndex ? 'active' : ''}`;
      card.setAttribute('data-index', item.index);

      const katName = (item.kategori_multilingual && (item.kategori_multilingual[lang] || item.kategori_multilingual['en'])) || item.kategori || 'Tasrif';
      const subjekName = (item.subjek_multilingual && (item.subjek_multilingual[lang] || item.subjek_multilingual['en'])) || item.subjek || item.label || '';

      let catBadgeClass = 'badge-purple';
      if (item.kategori.includes('Mudhari')) catBadgeClass = 'badge-emerald';
      else if (item.kategori.includes('Amr')) catBadgeClass = 'badge-gold';
      else if (item.kategori.includes('Masdar')) catBadgeClass = 'badge-cyan';
      else if (item.kategori.includes('Isim')) catBadgeClass = 'badge-gold';

      card.innerHTML = `
        <div class="tasrif-row-col-meta">
          <div class="tasrif-row-badges">
            <span class="tasrif-code-badge">${item.tasrif}</span>
            <span class="badge ${catBadgeClass}">${katName}</span>
          </div>
          <div class="tasrif-card-subjek">${subjekName}</div>
        </div>

        <div class="tasrif-row-col-main">
          <div class="tasrif-row-main-top">
            <span class="tasrif-card-meaning">${item.arti_lafaz || '-'}</span>
            ${item.wazan ? `<span class="tasrif-row-wazan"><span style="font-size:0.75rem; color:var(--text-dim);">Wazan: </span><span class="tasrif-card-wazan font-arabic notranslate" translate="no">${item.wazan}</span></span>` : ''}
            ${item.asal ? `<span class="tasrif-row-asal"><span style="font-size:0.75rem; color:var(--text-dim);">Asal: </span><span class="tasrif-card-asal font-arabic notranslate" translate="no">${item.asal}</span></span>` : ''}
          </div>
          ${item.ilal && item.ilal.trim() !== '' ? `<div class="tasrif-row-ilal"><span class="tasrif-ilal-tag">I'lal:</span><span class="tasrif-ilal-text">${item.ilal}</span></div>` : ''}
        </div>

        <div class="tasrif-row-col-arabic">
          <div class="tasrif-card-arabic font-arabic notranslate" translate="no">${item.lafaz}</div>
        </div>
      `;

      card.addEventListener('click', () => {
        selectMusytaqTasrif(item.index);
        if (elements.musytaqDisplaySection) {
          const cardTop = elements.musytaqDisplaySection.getBoundingClientRect().top + window.pageYOffset - 80;
          window.scrollTo({ top: cardTop, behavior: 'smooth' });
        }
      });

      elements.musytaqTasrifGrid.appendChild(card);
    });
  }

  function openMusytaqAiModal() {
    const rootObj = getMusytaqAkarObj(state.selectedMusytaqLevel, state.selectedMusytaqAkarNo);
    const tasrifObj = getMusytaqTasrifObj(state.selectedMusytaqLevel, state.selectedMusytaqAkarNo, state.selectedMusytaqTasrifIndex);
    if (!rootObj || !tasrifObj) return;

    currentAiContext = {
      surat: 1,
      ayat: 1,
      kata: tasrifObj.lafaz,
      noKata: `${rootObj.no_akar} (${tasrifObj.tasrif})`,
      bentuk: `Kamus Musytaq (Akar: ${rootObj.akar}, Wazan: ${tasrifObj.wazan || '-'})`,
      suratNama: `Akar ${rootObj.akar}`,
      teksArab: tasrifObj.lafaz,
      teksArti: tasrifObj.arti_lafaz,
      grammarDesc: `Kategori: ${tasrifObj.kategori}, Wazan: ${tasrifObj.wazan || '-'}, Asal: ${tasrifObj.asal || '-'}, Kaidah: ${tasrifObj.ilal || '-'}`,
      topic: 'nahwu'
    };

    if (elements.aiModalArabicVerse) {
      elements.aiModalArabicVerse.textContent = tasrifObj.lafaz;
    }
    if (elements.aiModalTranslation) {
      elements.aiModalTranslation.textContent = `Arti: "${tasrifObj.arti_lafaz}" | Akar: ${rootObj.akar} (${rootObj.arti_akar})`;
    }

    updateAiModalPrompt();
    if (elements.aiModal) {
      elements.aiModal.classList.add('open');
      elements.aiModal.setAttribute('aria-hidden', 'false');
    }
  }

  // Setup Event Listeners
  function setupEventListeners() {
    // Dropdown 1: Bentuk Kata
    if (elements.bentukKataSelect) {
      elements.bentukKataSelect.addEventListener('change', (e) => {
        selectBentuk(e.target.value);
      });
    }

    // Dropdown 2: No Kata
    if (elements.noKataSelect) {
      elements.noKataSelect.addEventListener('change', (e) => {
        selectNoKata(e.target.value);
      });
    }

    // Language Selector
    if (elements.langSelect) {
      elements.langSelect.addEventListener('change', (e) => {
        applyLanguage(e.target.value);
        showToast(t('toastLangChanged'));
      });
    }

    // Search Input in References
    if (elements.ayatSearchInput) {
      elements.ayatSearchInput.addEventListener('input', (e) => {
        state.searchQuery = e.target.value;
        renderAyatReferences();
      });
    }

    // Copy Arabic Word Button
    if (elements.btnCopyArabic) {
      elements.btnCopyArabic.addEventListener('click', () => {
        const group = getGroup(state.selectedBentuk, state.selectedNoKata);
        if (!group) return;
        navigator.clipboard.writeText(group.kata).then(() => {
          showToast(t('toastArabicCopied', group.kata));
        }).catch(() => {
          showToast('Gagal menyalin kata Arab.');
        });
      });
    }

    // Copy Summary Info Button
    if (elements.btnCopyAll) {
      elements.btnCopyAll.addEventListener('click', () => {
        const group = getGroup(state.selectedBentuk, state.selectedNoKata);
        if (!group) return;

        const activeArti = getGroupArti(group, state.lang);
        const activeDesc = getGroupDesc(group, state.lang);

        let titlePrefix = "Kamus Al-Qur'an";
        if (group.bentuk.includes('Mawshul')) {
          titlePrefix = "Isim Mawshul Al-Qur'an";
        } else if (group.bentuk.includes('Dhamir')) {
          titlePrefix = "Dhamir Al-Qur'an";
        }

        const summary = `[${titlePrefix}]\n${group.noKata} - ${group.kata} (${group.latin || '-'})
${t('meaningPrefix')} ${activeArti}\n${activeDesc ? t('wordFormBadge') + ': ' + activeDesc + '\n' : ''}${t('freqLabel')}: ${group.frek ? group.frek + 'x' : t('freqMuttashilVal')}\n${t('totalAyatLabel')}: ${group.occurrences.length} ${t('sampleAyatSuffix')}`;
        
        navigator.clipboard.writeText(summary).then(() => {
          showToast(t('toastSummaryCopied'));
        }).catch(() => {
          showToast('Gagal menyalin ringkasan.');
        });
      });
    }

    // Keyboard Navigation
    document.addEventListener('keydown', (e) => {
      if (elements.aiModal && elements.aiModal.classList.contains('open')) {
        if (e.key === 'Escape') closeAiModal();
        return;
      }

      if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') {
        if (e.key === 'Escape') e.target.blur();
        return;
      }

      const activeList = noKatasByBentuk[state.selectedBentuk] || [];
      if (activeList.length === 0) return;

      const currentNKIndex = activeList.indexOf(state.selectedNoKata);

      if (e.key === 'ArrowRight' || e.key === 'j') {
        if (currentNKIndex < activeList.length - 1) {
          selectNoKata(activeList[currentNKIndex + 1]);
        }
      } else if (e.key === 'ArrowLeft' || e.key === 'k') {
        if (currentNKIndex > 0) {
          selectNoKata(activeList[currentNKIndex - 1]);
        }
      } else if (e.key === ' ' || e.key === 'Spacebar') {
        e.preventDefault();
        const currentGroup = getGroup(state.selectedBentuk, state.selectedNoKata);
        if (currentGroup) speakDhamirMeaning(currentGroup);
      }
    });

    // Theme Switcher Button
    if (elements.themeToggleBtn) {
      elements.themeToggleBtn.addEventListener('click', () => {
        const nextTheme = state.theme === 'light' ? 'dark' : 'light';
        applyTheme(nextTheme);
      });
    }

    // Audio Play Button (Arabic Pronunciation)
    if (elements.btnAudioPlay) {
      elements.btnAudioPlay.addEventListener('click', () => {
        const group = getGroup(state.selectedBentuk, state.selectedNoKata);
        if (group) speakArabicWord(group.kata);
      });
    }

    // Audio Meaning Button
    if (elements.btnAudioMeaning) {
      elements.btnAudioMeaning.addEventListener('click', () => {
        const group = getGroup(state.selectedBentuk, state.selectedNoKata);
        if (group) speakDhamirMeaning(group);
      });
    }

    // Export CSV Button
    if (elements.btnExportCsv) {
      elements.btnExportCsv.addEventListener('click', () => {
        exportToCsv();
      });
    }

    // Dictionary Tab Switcher
    if (elements.tabDictJamid) {
      elements.tabDictJamid.addEventListener('click', () => {
        switchDictionary('jamid');
      });
    }
    if (elements.tabDictHarf) {
      elements.tabDictHarf.addEventListener('click', () => {
        switchDictionary('harf');
      });
    }
    if (elements.tabDictHarfAmil) {
      elements.tabDictHarfAmil.addEventListener('click', () => {
        switchDictionary('harf_amil');
      });
    }

    // Kamus Musytaq Controls Event Listeners
    if (elements.musytaqLevelSelect) {
      elements.musytaqLevelSelect.addEventListener('change', (e) => {
        selectMusytaqLevel(e.target.value);
      });
    }

    if (elements.musytaqAkarSelect) {
      elements.musytaqAkarSelect.addEventListener('change', (e) => {
        selectMusytaqAkar(e.target.value);
      });
    }

    if (elements.musytaqTasrifSelect) {
      elements.musytaqTasrifSelect.addEventListener('change', (e) => {
        selectMusytaqTasrif(e.target.value);
      });
    }

    if (elements.musytaqSearchInput) {
      elements.musytaqSearchInput.addEventListener('input', (e) => {
        state.musytaqSearchQuery = e.target.value;
        renderMusytaqTasrifGrid();
      });
    }

    if (elements.musytaqCategoryChips) {
      elements.musytaqCategoryChips.addEventListener('click', (e) => {
        const chip = e.target.closest('.tasrif-chip');
        if (!chip) return;
        state.musytaqCategoryFilter = chip.getAttribute('data-cat') || 'all';
        renderMusytaqTasrifGrid();
      });
    }

    if (elements.btnMusytaqAudio) {
      elements.btnMusytaqAudio.addEventListener('click', () => {
        const tasrifObj = getMusytaqTasrifObj(state.selectedMusytaqLevel, state.selectedMusytaqAkarNo, state.selectedMusytaqTasrifIndex);
        if (tasrifObj && tasrifObj.lafaz) {
          speakArabicWord(tasrifObj.lafaz);
        }
      });
    }

    if (elements.btnMusytaqAiAsk) {
      elements.btnMusytaqAiAsk.addEventListener('click', () => {
        openMusytaqAiModal();
      });
    }

    if (elements.tabDictMusytaq) {
      elements.tabDictMusytaq.addEventListener('click', () => {
        switchDictionary('musytaq');
      });
    }


    // AI Modal Actions
    if (elements.aiModalCloseBtn) {
      elements.aiModalCloseBtn.addEventListener('click', closeAiModal);
    }
    if (elements.aiModal) {
      elements.aiModal.addEventListener('click', (e) => {
        if (e.target === elements.aiModal) closeAiModal();
      });
    }
    if (elements.aiTopicChips) {
      elements.aiTopicChips.addEventListener('click', (e) => {
        const chip = e.target.closest('.ai-topic-chip');
        if (!chip) return;
        elements.aiTopicChips.querySelectorAll('.ai-topic-chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        currentAiContext.topic = chip.getAttribute('data-topic');
        updateAiModalPrompt();
      });
    }
    if (elements.btnOpenGemini) {
      elements.btnOpenGemini.addEventListener('click', openInGemini);
    }
    if (elements.btnOpenChatGpt) {
      elements.btnOpenChatGpt.addEventListener('click', openInChatGpt);
    }
    if (elements.btnCopyPrompt) {
      elements.btnCopyPrompt.addEventListener('click', copyAiPrompt);
    }
  }

  // Initialize App
  function init() {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.onvoiceschanged = () => {
        window.speechSynthesis.getVoices();
      };
      window.speechSynthesis.getVoices();
    }
    applyTheme(state.theme);
    setupEventListeners();
    switchDictionary(state.activeDict);
    applyLanguage(state.lang);
  }

  // Run on DOM Content Loaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
