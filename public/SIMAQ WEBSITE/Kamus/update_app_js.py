import re
import sys

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. State lang comment
code = code.replace(
    "lang: localStorage.getItem('dhamir_lang') || 'id', // 'id' | 'en' | 'ms' | 'fr' | 'de'",
    "lang: localStorage.getItem('dhamir_lang') || 'id', // 'id' | 'en' | 'ms' | 'fr' | 'de' | 'ur'"
)

# 2. Add 'ur' to I18N
ur_i18n = """    ur: {
      pageTitle: "جامد مبنی لغت | انٹرایکٹو قرآنی الفاظ اور حوالہ جات",
      brandTitle: "Kamus <span>Jamid Mabny</span>",
      brandSubtitle: "انٹرایکٹو ڈکشنری برائے اشکال الفاظ و اعداد الفاظ",
      themeToggleTitle: "ڈارک / لائٹ موڈ تبدیل کریں",
      labelLangSelect: "ترجمہ اور آواز کی زبان:",
      translationSourceHtml: "ترجمہ: <strong>مولانا فتح محمد جالندھری (Fateh Jalandhry)</strong>",
      
      // Control Card
      step1Label: "۱. لفظ کی شکل منتخب کریں",
      step1Placeholder: "لفظ کی شکل منتخب کریں",
      step1OptionDhamir: "۱. ضمائر (Dhamir - Pronouns)",
      step1OptionMawshul: "۲. اسم موصول (Mawshul - Relative Pronouns)",
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
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ur || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ur || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'اسم موصول' : 'ضمیر';
        return `${prefix} ${cleanWord}، ${latin}معنی ${arti}۔ ${desc ? 'وضاحت: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }"""

de_anchor = """      ttsVerseSpeech: (suratNama, ayat, text) => text
    }
  };"""

code = code.replace(de_anchor, """      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
""" + ur_i18n + """
  };""")

# 3. groupedData construction
old_group_data = """          bentuk_de: item['BentukKataDE'] || (b === '1. Dhamir' ? '1. Pronomen (Dhamir)' : (b === '2. Mawshul' ? '2. Relativpronomen (Mawshul)' : b)),
          noKata: nk,"""
new_group_data = """          bentuk_de: item['BentukKataDE'] || (b === '1. Dhamir' ? '1. Pronomen (Dhamir)' : (b === '2. Mawshul' ? '2. Relativpronomen (Mawshul)' : b)),
          bentuk_ur: item['BentukKataUR'] || (b === '1. Dhamir' ? '۱. ضمائر (Dhamir)' : (b === '2. Mawshul' ? '۲. اسم موصول (Mawshul)' : b)),
          noKata: nk,"""
code = code.replace(old_group_data, new_group_data)

old_arti_de = """          arti_de: item['ArtiKataDE'] || grammar.arti_de || item['ArtiKataID'] || item['Arti kata'],
          frek: item['Frek kata'],"""
new_arti_de = """          arti_de: item['ArtiKataDE'] || grammar.arti_de || item['ArtiKataID'] || item['Arti kata'],
          arti_ur: item['ArtiKataUR'] || grammar.arti_ur || item['ArtiKataID'] || item['Arti kata'],
          frek: item['Frek kata'],"""
code = code.replace(old_arti_de, new_arti_de)

old_surat_arti = """        suratArtiDE: item['SuratArtiDE'] || item['SuratArti'] || '',
        teksArab: item['TeksArab'] || '',"""
new_surat_arti = """        suratArtiDE: item['SuratArtiDE'] || item['SuratArti'] || '',
        suratArtiUR: item['SuratArtiUR'] || item['SuratArti'] || '',
        teksArab: item['TeksArab'] || '',"""
code = code.replace(old_surat_arti, new_surat_arti)

old_teks_arti = """        teksArtiDE: item['TeksArtiDE'] || item['TeksArtiID'] || item['TeksArti'] || '',
        audioUrl: item['AudioUrl'] || getAyatAudioUrl(item['SURAT'], item['AYAT'])"""
new_teks_arti = """        teksArtiDE: item['TeksArtiDE'] || item['TeksArtiID'] || item['TeksArti'] || '',
        teksArtiUR: item['TeksArtiUR'] || item['TeksArtiID'] || item['TeksArti'] || '',
        audioUrl: item['AudioUrl'] || getAyatAudioUrl(item['SURAT'], item['AYAT'])"""
code = code.replace(old_teks_arti, new_teks_arti)

# 4. populateNoKataDropdown
old_no_kata = """      } else if (state.lang === 'de') {
        localizedArti = group.arti_de || group.arti_id || group.arti;
      }
      option.textContent = `${nk} - ${group.kata} ${latinPart}(${localizedArti})`;"""
new_no_kata = """      } else if (state.lang === 'de') {
        localizedArti = group.arti_de || group.arti_id || group.arti;
      } else if (state.lang === 'ur') {
        localizedArti = group.arti_ur || group.arti_id || group.arti;
      }
      option.textContent = `${nk} - ${group.kata} ${latinPart}(${localizedArti})`;"""
code = code.replace(old_no_kata, new_no_kata)

# 5. updateSpotlightCard
old_badge_bentuk = """    } else if (state.lang === 'de') {
      elements.badgeBentukKata.textContent = group.bentuk_de || group.bentuk_id;
    } else {
      elements.badgeBentukKata.textContent = group.bentuk_id;
    }"""
new_badge_bentuk = """    } else if (state.lang === 'de') {
      elements.badgeBentukKata.textContent = group.bentuk_de || group.bentuk_id;
    } else if (state.lang === 'ur') {
      elements.badgeBentukKata.textContent = group.bentuk_ur || group.bentuk_id;
    } else {
      elements.badgeBentukKata.textContent = group.bentuk_id;
    }"""
code = code.replace(old_badge_bentuk, new_badge_bentuk)

old_badge_jenis = """    } else if (state.lang === 'de') {
      jenisText = grammar.jenis_de || (group.bentuk.includes('Mawshul') ? 'Relativpronomen' : 'Pronomen');
    } else {
      jenisText = grammar.jenis_id || grammar.jenis || (group.bentuk.includes('Mawshul') ? 'Isim Mawshul' : 'Dhamir');
    }"""
new_badge_jenis = """    } else if (state.lang === 'de') {
      jenisText = grammar.jenis_de || (group.bentuk.includes('Mawshul') ? 'Relativpronomen' : 'Pronomen');
    } else if (state.lang === 'ur') {
      jenisText = grammar.jenis_ur || (group.bentuk.includes('Mawshul') ? 'اسم موصول' : 'ضمیر');
    } else {
      jenisText = grammar.jenis_id || grammar.jenis || (group.bentuk.includes('Mawshul') ? 'Isim Mawshul' : 'Dhamir');
    }"""
code = code.replace(old_badge_jenis, new_badge_jenis)

old_meaning = """    } else if (state.lang === 'de') {
      currentMeaning = group.arti_de || group.arti_id || group.arti;
    }
    elements.wordMeaningDisplay.textContent = currentMeaning;"""
new_meaning = """    } else if (state.lang === 'de') {
      currentMeaning = group.arti_de || group.arti_id || group.arti;
    } else if (state.lang === 'ur') {
      currentMeaning = group.arti_ur || group.arti_id || group.arti;
    }
    elements.wordMeaningDisplay.textContent = currentMeaning;"""
code = code.replace(old_meaning, new_meaning)

old_desc = """    } else if (state.lang === 'de') {
      currentDesc = grammar.desc_de || grammar.desc_id || grammar.keterangan || '';
    }
    elements.wordMeaningSub.textContent = currentDesc ? `${t('meaningPrefix')} ${currentDesc}` : '';"""
new_desc = """    } else if (state.lang === 'de') {
      currentDesc = grammar.desc_de || grammar.desc_id || grammar.keterangan || '';
    } else if (state.lang === 'ur') {
      currentDesc = grammar.desc_ur || grammar.desc_id || grammar.keterangan || '';
    }
    elements.wordMeaningSub.textContent = currentDesc ? `${t('meaningPrefix')} ${currentDesc}` : '';"""
code = code.replace(old_desc, new_desc)

# 6. playVerseTranslation
old_play_trans_text = """    } else if (state.lang === 'de') {
      currentText = occ.teksArtiDE || occ.teksArtiID || occ.teksArti;
    }
    const cleanText = (currentText || '').replace(/["“”]/g, '').trim();"""
new_play_trans_text = """    } else if (state.lang === 'de') {
      currentText = occ.teksArtiDE || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'ur') {
      currentText = occ.teksArtiUR || occ.teksArtiID || occ.teksArti;
    }
    const cleanText = (currentText || '').replace(/["“”]/g, '').trim();"""
code = code.replace(old_play_trans_text, new_play_trans_text)

old_play_trans_lang = """    } else if (state.lang === 'de') {
      utterance.lang = 'de-DE';
      utterance.rate = 0.95;
    } else {
      utterance.lang = 'id-ID';
      utterance.rate = 0.95;
    }"""
new_play_trans_lang = """    } else if (state.lang === 'de') {
      utterance.lang = 'de-DE';
      utterance.rate = 0.95;
    } else if (state.lang === 'ur') {
      utterance.lang = 'ur-PK';
      utterance.rate = 0.92;
    } else {
      utterance.lang = 'id-ID';
      utterance.rate = 0.95;
    }"""
code = code.replace(old_play_trans_lang, new_play_trans_lang)

old_play_trans_voice = """    } else if (state.lang === 'de') {
      const deVoice = voices.find(v => v.lang.startsWith('de') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Stefan') || v.name.includes('Hedda') || v.name.includes('Katja') || v.name.includes('Marlene') || v.name.includes('Hans'))) || voices.find(v => v.lang.startsWith('de'));
      if (deVoice) utterance.voice = deVoice;
    } else {
      const idVoice = voices.find(v => v.lang.startsWith('id') || v.lang.startsWith('in'));
      if (idVoice) utterance.voice = idVoice;
    }"""
new_play_trans_voice = """    } else if (state.lang === 'de') {
      const deVoice = voices.find(v => v.lang.startsWith('de') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Stefan') || v.name.includes('Hedda') || v.name.includes('Katja') || v.name.includes('Marlene') || v.name.includes('Hans'))) || voices.find(v => v.lang.startsWith('de'));
      if (deVoice) utterance.voice = deVoice;
    } else if (state.lang === 'ur') {
      const urVoice = voices.find(v => v.lang.startsWith('ur') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Asad') || v.name.includes('Uzma'))) || voices.find(v => v.lang.startsWith('ur')) || voices.find(v => v.lang.startsWith('ar'));
      if (urVoice) utterance.voice = urVoice;
    } else {
      const idVoice = voices.find(v => v.lang.startsWith('id') || v.lang.startsWith('in'));
      if (idVoice) utterance.voice = idVoice;
    }"""
code = code.replace(old_play_trans_voice, new_play_trans_voice)

# 7. speakDhamirMeaning
old_speak_dhamir_lang = """    } else if (state.lang === 'de') {
      utterance.lang = 'de-DE';
      utterance.rate = 0.95;
    } else {
      utterance.lang = 'id-ID';
      utterance.rate = 0.95;
    }"""
new_speak_dhamir_lang = """    } else if (state.lang === 'de') {
      utterance.lang = 'de-DE';
      utterance.rate = 0.95;
    } else if (state.lang === 'ur') {
      utterance.lang = 'ur-PK';
      utterance.rate = 0.92;
    } else {
      utterance.lang = 'id-ID';
      utterance.rate = 0.95;
    }"""
code = code.replace(old_speak_dhamir_lang, new_speak_dhamir_lang)

old_speak_dhamir_voice = """    } else if (state.lang === 'de') {
      const deVoice = voices.find(v => v.lang.startsWith('de') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Stefan') || v.name.includes('Hedda') || v.name.includes('Katja') || v.name.includes('Marlene') || v.name.includes('Hans'))) || voices.find(v => v.lang.startsWith('de'));
      if (deVoice) utterance.voice = deVoice;
    } else {
      const idVoice = voices.find(v => v.lang.startsWith('id') || v.lang.startsWith('in'));
      if (idVoice) utterance.voice = idVoice;
    }"""
new_speak_dhamir_voice = """    } else if (state.lang === 'de') {
      const deVoice = voices.find(v => v.lang.startsWith('de') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Stefan') || v.name.includes('Hedda') || v.name.includes('Katja') || v.name.includes('Marlene') || v.name.includes('Hans'))) || voices.find(v => v.lang.startsWith('de'));
      if (deVoice) utterance.voice = deVoice;
    } else if (state.lang === 'ur') {
      const urVoice = voices.find(v => v.lang.startsWith('ur') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Asad') || v.name.includes('Uzma'))) || voices.find(v => v.lang.startsWith('ur')) || voices.find(v => v.lang.startsWith('ar'));
      if (urVoice) utterance.voice = urVoice;
    } else {
      const idVoice = voices.find(v => v.lang.startsWith('id') || v.lang.startsWith('in'));
      if (idVoice) utterance.voice = idVoice;
    }"""
code = code.replace(old_speak_dhamir_voice, new_speak_dhamir_voice)

old_speak_active_meaning = """    } else if (state.lang === 'de') {
      activeMeaning = group.arti_de || group.arti_id || group.arti;
    }
    showToast(t('toastSpeakingWordMeaning', activeMeaning));"""
new_speak_active_meaning = """    } else if (state.lang === 'de') {
      activeMeaning = group.arti_de || group.arti_id || group.arti;
    } else if (state.lang === 'ur') {
      activeMeaning = group.arti_ur || group.arti_id || group.arti;
    }
    showToast(t('toastSpeakingWordMeaning', activeMeaning));"""
code = code.replace(old_speak_active_meaning, new_speak_active_meaning)

# 8. renderAyatReferences search filter
old_search_filter = """        } else if (state.lang === 'de') {
          sArti = occ.suratArtiDE;
          tArti = occ.teksArtiDE;
        }"""
new_search_filter = """        } else if (state.lang === 'de') {
          sArti = occ.suratArtiDE;
          tArti = occ.teksArtiDE;
        } else if (state.lang === 'ur') {
          sArti = occ.suratArtiUR;
          tArti = occ.teksArtiUR;
        }"""
code = code.replace(old_search_filter, new_search_filter)

# 9. Grand Unified Verse Card
old_verse_card_arti = """    } else if (state.lang === 'de') {
      activeSuratArti = occ.suratArtiDE;
      activeTeksArti = occ.teksArtiDE || occ.teksArtiID || occ.teksArti;
    }"""
new_verse_card_arti = """    } else if (state.lang === 'de') {
      activeSuratArti = occ.suratArtiDE;
      activeTeksArti = occ.teksArtiDE || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'ur') {
      activeSuratArti = occ.suratArtiUR;
      activeTeksArti = occ.teksArtiUR || occ.teksArtiID || occ.teksArti;
    }"""
code = code.replace(old_verse_card_arti, new_verse_card_arti)

# 10. applyLanguage
code = code.replace(
    "state.lang = ['en', 'ms', 'fr', 'de'].includes(lang) ? lang : 'id';",
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur'].includes(lang) ? lang : 'id';"
)

# 11. buildAiPrompt
old_ai_vars = """    } else if (state.lang === 'de') {
      teksArti = occ.teksArtiDE || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_de || group.grammar.desc_id || group.grammar.keterangan)) || '';
    }"""
new_ai_vars = """    } else if (state.lang === 'de') {
      teksArti = occ.teksArtiDE || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_de || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'ur') {
      teksArti = occ.teksArtiUR || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_ur || group.grammar.desc_id || group.grammar.keterangan)) || '';
    }"""
code = code.replace(old_ai_vars, new_ai_vars)

old_ai_prompt_branches = """    } else if (state.lang === 'de') {
      if (topic === 'nahwu') {
        return `Bitte erklären Sie ausführlich die arabische Grammatik (Nahw/Sarf) und das I'rab für das Wort "${kata}" (${noKata}, ${bentuk}) im Koran, Sure ${suratNama} (${surat}) : Vers ${ayat}:\\n\\nArabischer Text: "${teksArab}"\\nÜbersetzung: "${teksArti}"\\n\\nBitte erläutern Sie:\\n1. Die grammatikalische Funktion / I'rab von "${kata}" in dieser Satzstruktur.\\n2. Die morphologische Kategorie (Art des Dhamir / Mawshul) und den Fall (Marfu'/Manshub/Majrur).\\n3. Grammatikalische Anmerkungen: ${grammarDesc || 'Standardmäßiger koranischer Sprachgebrauch'}.`;
      } else if (topic === 'tafsir') {
        return `Bitte geben Sie eine prägnante und kontextbezogene Tafsir-Erklärung für Sure ${suratNama} (${surat}) : Vers ${ayat}:\\n\\nArabischer Text: "${teksArab}"\\nÜbersetzung: "${teksArti}"\\n\\nMit Fokus auf die Bedeutung des Pronomens / Wortes "${kata}": Was ist die wesentliche Weisheit, der Offenbarungsanlass (Asbab an-Nuzul, falls zutreffend) und die theologische Botschaft dieses Verses?`;
      } else {
        return `Erklären Sie die koranische Balagha (Rhetorische Schönheit & Stilistik) bezüglich der Wortwahl "${kata}" in Sure ${suratNama} (${surat}) Vers ${ayat}:\\n\\nArabischer Text: "${teksArab}"\\nÜbersetzung: "${teksArti}"\\n\\nWarum wird hier genau diese Pronomenform verwendet? Welche feinen Nuancen, Betonungen oder ästhetische Eloquenz verleiht sie dem Vers?`;
      }
    } else {"""

new_ai_prompt_branches = """    } else if (state.lang === 'de') {
      if (topic === 'nahwu') {
        return `Bitte erklären Sie ausführlich die arabische Grammatik (Nahw/Sarf) und das I'rab für das Wort "${kata}" (${noKata}, ${bentuk}) im Koran, Sure ${suratNama} (${surat}) : Vers ${ayat}:\\n\\nArabischer Text: "${teksArab}"\\nÜbersetzung: "${teksArti}"\\n\\nBitte erläutern Sie:\\n1. Die grammatikalische Funktion / I'rab von "${kata}" in dieser Satzstruktur.\\n2. Die morphologische Kategorie (Art des Dhamir / Mawshul) und den Fall (Marfu'/Manshub/Majrur).\\n3. Grammatikalische Anmerkungen: ${grammarDesc || 'Standardmäßiger koranischer Sprachgebrauch'}.`;
      } else if (topic === 'tafsir') {
        return `Bitte geben Sie eine prägnante und kontextbezogene Tafsir-Erklärung für Sure ${suratNama} (${surat}) : Vers ${ayat}:\\n\\nArabischer Text: "${teksArab}"\\nÜbersetzung: "${teksArti}"\\n\\nMit Fokus auf die Bedeutung des Pronomens / Wortes "${kata}": Was ist die wesentliche Weisheit, der Offenbarungsanlass (Asbab an-Nuzul, falls zutreffend) und die theologische Botschaft dieses Verses?`;
      } else {
        return `Erklären Sie die koranische Balagha (Rhetorische Schönheit & Stilistik) bezüglich der Wortwahl "${kata}" in Sure ${suratNama} (${surat}) Vers ${ayat}:\\n\\nArabischer Text: "${teksArab}"\\nÜbersetzung: "${teksArti}"\\n\\nWarum wird hier genau diese Pronomenform verwendet? Welche feinen Nuancen, Betonungen oder ästhetische Eloquenz verleiht sie dem Vers?`;
      }
    } else if (state.lang === 'ur') {
      if (topic === 'nahwu') {
        return `براہ کرم قرآن مجید کی سورۃ ${suratNama} (${surat}) آیت ${ayat} میں موجود لفظ "${kata}" (${noKata}، ${bentuk}) کے عربی قواعد و نحوی اعراب کی مفصل وضاحت کریں:\\n\\nعربی متن: "${teksArab}"\\nترجمہ: "${teksArti}"\\n\\nبراہ کرم درج ذیل نکات شامل کریں:\\n۱. اس جملے کی ترکیب میں "${kata}" کا نحوی کردار اور اعراب۔\\n۲. لفظ کی نوعیت (ضمیر منفصل/متصل یا اسم موصول) اور اس کی اعرابی حالت (مرفوع/منصوب/مجرور)۔\\n۳. نحوی نوٹس: ${grammarDesc || 'قرآنی معیاری استعمال'}۔`;
      } else if (topic === 'tafsir') {
        return `براہ کرم سورۃ ${suratNama} (${surat}) آیت ${ayat} کی مختصر اور سیاق و سباق کے مطابق تفسیری وضاحت پیش کریں:\\n\\nعربی متن: "${teksArab}"\\nترجمہ: "${teksArti}"\\n\\nخاص طور پر لفظ/ضمیر "${kata}" کی اہمیت کو مدنظر رکھتے ہوئے، اس آیت میں کیا بنیادی حکمت، شان نزول اور الٰہی پیغام بیان کیا گیا ہے؟`;
      } else {
        return `سورۃ ${suratNama} (${surat}) آیت ${ayat} میں لفظ "${kata}" کے انتخاب کے حوالے سے قرآنی بلاغت اور اسلوب کی خوبصورتی بیان کریں:\\n\\nعربی متن: "${teksArab}"\\nترجمہ: "${teksArti}"\\n\\nیہاں پر ضمیر کی یہی مخصوص شکل کیوں استعمال ہوئی ہے؟ یہ آیت کے حسن اور معنوی گہرائی میں کیا نکھار پیدا کرتی ہے؟`;
      }
    } else {"""
code = code.replace(old_ai_prompt_branches, new_ai_prompt_branches)

# 12. openAiModal
old_modal_arti = """      } else if (state.lang === 'de') {
        activeArti = occ.teksArtiDE || occ.teksArtiID || occ.teksArti;
      }"""
new_modal_arti = """      } else if (state.lang === 'de') {
        activeArti = occ.teksArtiDE || occ.teksArtiID || occ.teksArti;
      } else if (state.lang === 'ur') {
        activeArti = occ.teksArtiUR || occ.teksArtiID || occ.teksArti;
      }"""
code = code.replace(old_modal_arti, new_modal_arti)

# 13. exportToCsv
old_csv_header = "csvContent += 'Bentuk Kata,No Kata,Kata Arab,Transliterasi Latin,Arti Kata (ID),Meaning (EN),Maksud Kata (MS),Signification (FR),Bedeutung (DE),Frekuensi,Nomor Surat,Nama Surat,Ayat,Teks Arab Ayat,Transliterasi Latin Ayat,Terjemahan (ID),Translation (EN),Terjemahan (MS),Traduction (FR),Übersetzung (DE),Link Audio,Link QuranCom\\n';"
new_csv_header = "csvContent += 'Bentuk Kata,No Kata,Kata Arab,Transliterasi Latin,Arti Kata (ID),Meaning (EN),Maksud Kata (MS),Signification (FR),Bedeutung (DE),Mani (UR),Frekuensi,Nomor Surat,Nama Surat,Ayat,Teks Arab Ayat,Transliterasi Latin Ayat,Terjemahan (ID),Translation (EN),Terjemahan (MS),Traduction (FR),Übersetzung (DE),Tarjuma (UR),Link Audio,Link QuranCom\\n';"
code = code.replace(old_csv_header, new_csv_header)

old_csv_row = """      const cleanArtiDE = (occ.teksArtiDE || '').replace(/"/g, '""');
      const audioLink = occ.audioUrl || '';
      csvContent += `"${group.bentuk}","${group.noKata}","${group.kata}","${group.latin || ''}","${group.arti_id || group.arti}","${group.arti_en || ''}","${group.arti_ms || ''}","${group.arti_fr || ''}","${group.arti_de || ''}","${group.frek || 'Muttashil'}","${occ.surat}","${occ.suratNama}","${occ.ayat}","${cleanArab}","${cleanLatin}","${cleanArtiID}","${cleanArtiEN}","${cleanArtiMS}","${cleanArtiFR}","${cleanArtiDE}","${audioLink}","${link}"\\n`;"""
new_csv_row = """      const cleanArtiDE = (occ.teksArtiDE || '').replace(/"/g, '""');
      const cleanArtiUR = (occ.teksArtiUR || '').replace(/"/g, '""');
      const audioLink = occ.audioUrl || '';
      csvContent += `"${group.bentuk}","${group.noKata}","${group.kata}","${group.latin || ''}","${group.arti_id || group.arti}","${group.arti_en || ''}","${group.arti_ms || ''}","${group.arti_fr || ''}","${group.arti_de || ''}","${group.arti_ur || ''}","${group.frek || 'Muttashil'}","${occ.surat}","${occ.suratNama}","${occ.ayat}","${cleanArab}","${cleanLatin}","${cleanArtiID}","${cleanArtiEN}","${cleanArtiMS}","${cleanArtiFR}","${cleanArtiDE}","${cleanArtiUR}","${audioLink}","${link}"\\n`;"""
code = code.replace(old_csv_row, new_csv_row)

# 14. Copy Summary
old_copy_summary_arti = """        } else if (state.lang === 'de') {
          activeArti = group.arti_de || group.arti_id || group.arti;
        }"""
new_copy_summary_arti = """        } else if (state.lang === 'de') {
          activeArti = group.arti_de || group.arti_id || group.arti;
        } else if (state.lang === 'ur') {
          activeArti = group.arti_ur || group.arti_id || group.arti;
        }"""
code = code.replace(old_copy_summary_arti, new_copy_summary_arti)

old_copy_summary_title = """          else if (state.lang === 'de') titlePrefix = 'Koranisches Relativpronomen (Mawshul)';
          else titlePrefix = 'Isim Mawshul Al-Qur\\'an';
        } else {
          if (state.lang === 'en') titlePrefix = 'Quranic Pronoun (Dhamir)';
          else if (state.lang === 'ms') titlePrefix = 'Dhamir Al-Qur\\'an';
          else if (state.lang === 'fr') titlePrefix = 'Pronom du Coran (Dhamir)';
          else if (state.lang === 'de') titlePrefix = 'Koranisches Pronomen (Dhamir)';
          else titlePrefix = 'Dhamir Al-Qur\\'an';"""

new_copy_summary_title = """          else if (state.lang === 'de') titlePrefix = 'Koranisches Relativpronomen (Mawshul)';
          else if (state.lang === 'ur') titlePrefix = 'قرآنی اسم موصول (Mawshul)';
          else titlePrefix = 'Isim Mawshul Al-Qur\\'an';
        } else {
          if (state.lang === 'en') titlePrefix = 'Quranic Pronoun (Dhamir)';
          else if (state.lang === 'ms') titlePrefix = 'Dhamir Al-Qur\\'an';
          else if (state.lang === 'fr') titlePrefix = 'Pronom du Coran (Dhamir)';
          else if (state.lang === 'de') titlePrefix = 'Koranisches Pronomen (Dhamir)';
          else if (state.lang === 'ur') titlePrefix = 'قرآنی ضمیر (Dhamir)';
          else titlePrefix = 'Dhamir Al-Qur\\'an';"""
code = code.replace(old_copy_summary_title, new_copy_summary_title)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully updated app.js with full Urdu support!")
