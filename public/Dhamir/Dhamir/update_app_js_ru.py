# -*- coding: utf-8 -*-
"""
Script to add complete Russian (ru) language support to app.js
"""
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app_js_path = os.path.join(BASE_DIR, 'app.js')

with open(app_js_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. State lang comment
code = code.replace(
    "lang: localStorage.getItem('dhamir_lang') || 'id', // 'id' | 'en' | 'ms' | 'fr' | 'de' | 'ur' | 'hi' | 'bn'",
    "lang: localStorage.getItem('dhamir_lang') || 'id', // 'id' | 'en' | 'ms' | 'fr' | 'de' | 'ur' | 'hi' | 'bn' | 'ru'"
)

# 2. Add 'ru' to I18N
ru_i18n = """    ru: {
      pageTitle: "Словарь Джамид Мабни | Интерактивный словарь и коранические ссылки на аяты",
      brandTitle: "Словарь <span>Джамид Мабни</span>",
      brandSubtitle: "Интерактивный словарь грамматических форм и номеров слов",
      themeToggleTitle: "Переключить тёмную / светлую тему",
      labelLangSelect: "Язык перевода и озвучивания:",
      translationSourceHtml: "Перевод: <strong>Эльмир Кулиев (Elmir Kuliev)</strong>",
      
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
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ru || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ru || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Относительное местоимение' : 'Местоимение';
        return `${prefix} ${cleanWord}, ${latin}значение ${arti}. ${desc ? 'Описание: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }"""

# Insert 'ru' after 'bn' in I18N
bn_anchor = """      ttsVerseSpeech: (suratNama, ayat, text) => text
    }
  };"""

code = code.replace(bn_anchor, """      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
""" + ru_i18n + """
  };""")

# 3. groupedData construction
old_group_data = """          bentuk_bn: item['BentukKataBN'] || (b === '1. Dhamir' ? '১. সর্বনাম (Dhamir)' : (b === '2. Mawshul' ? '২. সম্বন্ধবাচক সর্বনাম (Mawshul)' : b)),
          noKata: nk,"""
new_group_data = """          bentuk_bn: item['BentukKataBN'] || (b === '1. Dhamir' ? '১. সর্বনাম (Dhamir)' : (b === '2. Mawshul' ? '২. সম্বন্ধবাচক सर्वनाम (Mawshul)' : b)),
          bentuk_ru: item['BentukKataRU'] || (b === '1. Dhamir' ? '1. Местоимения (Дамир / Dhamir)' : (b === '2. Mawshul' ? '2. Относительные местоимения (Маусуль / Mawshul)' : b)),
          noKata: nk,"""
code = code.replace(old_group_data, new_group_data)

old_arti_bn = """          arti_bn: item['ArtiKataBN'] || grammar.arti_bn || item['ArtiKataID'] || item['Arti kata'],
          frek: item['Frek kata'],"""
new_arti_bn = """          arti_bn: item['ArtiKataBN'] || grammar.arti_bn || item['ArtiKataID'] || item['Arti kata'],
          arti_ru: item['ArtiKataRU'] || grammar.arti_ru || item['ArtiKataID'] || item['Arti kata'],
          frek: item['Frek kata'],"""
code = code.replace(old_arti_bn, new_arti_bn)

old_surat_arti = """        suratArtiBN: item['SuratArtiBN'] || item['SuratArti'] || '',
        teksArab: item['TeksArab'] || '',"""
new_surat_arti = """        suratArtiBN: item['SuratArtiBN'] || item['SuratArti'] || '',
        suratArtiRU: item['SuratArtiRU'] || item['SuratArti'] || '',
        teksArab: item['TeksArab'] || '',"""
code = code.replace(old_surat_arti, new_surat_arti)

old_teks_arti = """        teksArtiBN: item['TeksArtiBN'] || item['TeksArtiID'] || item['TeksArti'] || '',
        audioUrl: item['AudioUrl']"""
new_teks_arti = """        teksArtiBN: item['TeksArtiBN'] || item['TeksArtiID'] || item['TeksArti'] || '',
        teksArtiRU: item['TeksArtiRU'] || item['TeksArtiID'] || item['TeksArti'] || '',
        audioUrl: item['AudioUrl']"""
code = code.replace(old_teks_arti, new_teks_arti)

# 4. populateNoKataDropdown
old_no_kata = """      } else if (state.lang === 'bn') {
        localizedArti = group.arti_bn || group.arti_id || group.arti;
      }"""
new_no_kata = """      } else if (state.lang === 'bn') {
        localizedArti = group.arti_bn || group.arti_id || group.arti;
      } else if (state.lang === 'ru') {
        localizedArti = group.arti_ru || group.arti_id || group.arti;
      }"""
code = code.replace(old_no_kata, new_no_kata)

# 5. updateSpotlightCard
old_badge_bentuk = """    } else if (state.lang === 'bn') {
      elements.badgeBentukKata.textContent = group.bentuk_bn || group.bentuk_id;
    } else {"""
new_badge_bentuk = """    } else if (state.lang === 'bn') {
      elements.badgeBentukKata.textContent = group.bentuk_bn || group.bentuk_id;
    } else if (state.lang === 'ru') {
      elements.badgeBentukKata.textContent = group.bentuk_ru || group.bentuk_id;
    } else {"""
code = code.replace(old_badge_bentuk, new_badge_bentuk)

old_badge_jenis = """    } else if (state.lang === 'bn') {
      jenisText = grammar.jenis_bn || (group.bentuk.includes('Mawshul') ? 'সম্বন্ধবাচক সর্বনাম' : 'সর্বনাম');
    } else {"""
new_badge_jenis = """    } else if (state.lang === 'bn') {
      jenisText = grammar.jenis_bn || (group.bentuk.includes('Mawshul') ? 'সম্বন্ধবাচক সর্বনাম' : 'সর্বনাম');
    } else if (state.lang === 'ru') {
      jenisText = grammar.jenis_ru || (group.bentuk.includes('Mawshul') ? 'Относительное местоимение' : 'Местоимение');
    } else {"""
code = code.replace(old_badge_jenis, new_badge_jenis)

old_meaning = """    } else if (state.lang === 'bn') {
      currentMeaning = group.arti_bn || group.arti;
    }"""
new_meaning = """    } else if (state.lang === 'bn') {
      currentMeaning = group.arti_bn || group.arti;
    } else if (state.lang === 'ru') {
      currentMeaning = group.arti_ru || group.arti;
    }"""
code = code.replace(old_meaning, new_meaning)

old_desc = """    } else if (state.lang === 'bn') {
      currentDesc = grammar.desc_bn || grammar.desc_id || grammar.keterangan || '';
    }"""
new_desc = """    } else if (state.lang === 'bn') {
      currentDesc = grammar.desc_bn || grammar.desc_id || grammar.keterangan || '';
    } else if (state.lang === 'ru') {
      currentDesc = grammar.desc_ru || grammar.desc_id || grammar.keterangan || '';
    }"""
code = code.replace(old_desc, new_desc)

# 6. Audio in toggleVerseTranslationAudio
old_play_trans_text = """    } else if (state.lang === 'bn') {
      currentText = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
    }"""
new_play_trans_text = """    } else if (state.lang === 'bn') {
      currentText = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'ru') {
      currentText = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
    }"""
code = code.replace(old_play_trans_text, new_play_trans_text)

old_play_trans_lang = """    } else if (state.lang === 'bn') {
      utterance.lang = 'bn-BD';
      utterance.rate = 0.92;
    } else {"""
new_play_trans_lang = """    } else if (state.lang === 'bn') {
      utterance.lang = 'bn-BD';
      utterance.rate = 0.92;
    } else if (state.lang === 'ru') {
      utterance.lang = 'ru-RU';
      utterance.rate = 0.95;
    } else {"""
code = code.replace(old_play_trans_lang, new_play_trans_lang)

old_play_trans_voice = """    } else if (state.lang === 'bn') {
      const bnVoice = voices.find(v => v.lang.startsWith('bn') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Bashkar') || v.name.includes('Tanishaa'))) || voices.find(v => v.lang.startsWith('bn'));
      if (bnVoice) utterance.voice = bnVoice;
    } else {"""
new_play_trans_voice = """    } else if (state.lang === 'bn') {
      const bnVoice = voices.find(v => v.lang.startsWith('bn') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Bashkar') || v.name.includes('Tanishaa'))) || voices.find(v => v.lang.startsWith('bn'));
      if (bnVoice) utterance.voice = bnVoice;
    } else if (state.lang === 'ru') {
      const ruVoice = voices.find(v => v.lang.startsWith('ru') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Pavel') || v.name.includes('Irina') || v.name.includes('Yuri') || v.name.includes('Ekaterina') || v.name.includes('Dmitry'))) || voices.find(v => v.lang.startsWith('ru'));
      if (ruVoice) utterance.voice = ruVoice;
    } else {"""
code = code.replace(old_play_trans_voice, new_play_trans_voice)

# 7. speakDhamirMeaning
old_speak_dhamir_lang = """    } else if (state.lang === 'bn') {
      activeMeaning = group.arti_bn || group.arti_id || group.arti;
    }"""
new_speak_dhamir_lang = """    } else if (state.lang === 'bn') {
      activeMeaning = group.arti_bn || group.arti_id || group.arti;
    } else if (state.lang === 'ru') {
      activeMeaning = group.arti_ru || group.arti_id || group.arti;
    }"""
code = code.replace(old_speak_dhamir_lang, new_speak_dhamir_lang)

old_speak_dhamir_utter = """    } else if (state.lang === 'bn') {
      utterance.lang = 'bn-BD';
      utterance.rate = 0.92;
    } else {"""
new_speak_dhamir_utter = """    } else if (state.lang === 'bn') {
      utterance.lang = 'bn-BD';
      utterance.rate = 0.92;
    } else if (state.lang === 'ru') {
      utterance.lang = 'ru-RU';
      utterance.rate = 0.95;
    } else {"""
code = code.replace(old_speak_dhamir_utter, new_speak_dhamir_utter)

old_speak_dhamir_voice = """    } else if (state.lang === 'bn') {
      const bnVoice = voices.find(v => v.lang.startsWith('bn') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Bashkar') || v.name.includes('Tanishaa'))) || voices.find(v => v.lang.startsWith('bn'));
      if (bnVoice) utterance.voice = bnVoice;
    } else {"""
new_speak_dhamir_voice = """    } else if (state.lang === 'bn') {
      const bnVoice = voices.find(v => v.lang.startsWith('bn') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Bashkar') || v.name.includes('Tanishaa'))) || voices.find(v => v.lang.startsWith('bn'));
      if (bnVoice) utterance.voice = bnVoice;
    } else if (state.lang === 'ru') {
      const ruVoice = voices.find(v => v.lang.startsWith('ru') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Pavel') || v.name.includes('Irina') || v.name.includes('Yuri') || v.name.includes('Ekaterina') || v.name.includes('Dmitry'))) || voices.find(v => v.lang.startsWith('ru'));
      if (ruVoice) utterance.voice = ruVoice;
    } else {"""
code = code.replace(old_speak_dhamir_voice, new_speak_dhamir_voice)

# 8. renderAyatReferences
old_search_filter = """        } else if (state.lang === 'bn') {
          sArti = occ.suratArtiBN;
          tArti = occ.teksArtiBN;
        }"""
new_search_filter = """        } else if (state.lang === 'bn') {
          sArti = occ.suratArtiBN;
          tArti = occ.teksArtiBN;
        } else if (state.lang === 'ru') {
          sArti = occ.suratArtiRU;
          tArti = occ.teksArtiRU;
        }"""
code = code.replace(old_search_filter, new_search_filter)

old_verse_card_arti = """    } else if (state.lang === 'bn') {
      activeSuratArti = occ.suratArtiBN;
      activeTeksArti = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
    }"""
new_verse_card_arti = """    } else if (state.lang === 'bn') {
      activeSuratArti = occ.suratArtiBN;
      activeTeksArti = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'ru') {
      activeSuratArti = occ.suratArtiRU;
      activeTeksArti = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
    }"""
code = code.replace(old_verse_card_arti, new_verse_card_arti)

# 9. applyLanguage
code = code.replace(
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn'].includes(lang) ? lang : 'id';",
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru'].includes(lang) ? lang : 'id';"
)

# 10. buildAiPrompt
old_ai_vars = """    } else if (state.lang === 'bn') {
      teksArti = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_bn || group.grammar.keterangan)) || '';
    }"""
new_ai_vars = """    } else if (state.lang === 'bn') {
      teksArti = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_bn || group.grammar.keterangan)) || '';
    } else if (state.lang === 'ru') {
      teksArti = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_ru || group.grammar.desc_id || group.grammar.keterangan)) || '';
    }"""
code = code.replace(old_ai_vars, new_ai_vars)

old_ai_prompt_branches = """    } else if (state.lang === 'bn') {
      if (topic === 'nahwu') {
        return `অনুগ্রহ করে পবিত্র কুরআনের সূরা ${suratNama} (${surat}) আয়াত ${ayat}-এ অবস্থিত শব্দ "${kata}" (${noKata}, ${bentuk})-এর আরবি ব্যাকরণ (নাহব/সরফ) ও ই'রাব বিস্তারিতভাবে ব্যাখ্যা করুন:\\n\\nআরবি পাঠ: "${teksArab}"\\nঅনুবাদ: "${teksArti}"\\n\\nঅনুগ্রহ করে নিম্নলিখিত বিষয়গুলো আলোচনা করুন:\\n১. এই বাক্যের গঠনে "${kata}"-এর ব্যাকরণগত ভূমিকা ও ই'রাব (I'rab)।\\n২. শব্দের রূপগত প্রকার (যমীর মুনফাসিল/মুত্তাসিল অথবা ইসম মাওসুল) এবং এর অবস্থা (মারফু'/মানসুব/মাজরুর)।\\n৩. ব্যাকরণগত নোট: ${grammarDesc || 'প্রমিত কুরআনিক প্রয়োগ'}।`;
      } else if (topic === 'tafsir') {
        return `অনুগ্রহ করে সূরা ${suratNama} (${surat}) আয়াত ${ayat}-এর সংক্ষিপ্ত ও প্রাসঙ্গিক তাফসির (ব্যাখ্যা) উপস্থাপন করুন:\\n\\nআরবি পাঠ: "${teksArab}"\\nঅনুবাদ: "${teksArti}"\\n\\nবিশেষ করে শব্দ/সর্বনাম "${kata}"-এর তাৎপর্যের ওপর গুরুত্ব দিয়ে বলুন, এই আয়াতে কী মূল হেকমত, শানে নুযূল এবং ঐশী বার্তা নিহিত রয়েছে?`;
      } else {
        return `সূরা ${suratNama} (${surat}) আয়াত ${ayat}-এ শব্দ "${kata}" নির্বাচনের ক্ষেত্রে কুরআনিক বালাগাত (অলঙ্কারিক সৌন্দর্য ও রচনাশৈলী) ব্যাখ্যা করুন:\\n\\nআরবি পাঠ: "${teksArab}"\\nঅনুবাদ: "${teksArti}"\\n\\nএখানে সর্বনামের এই নির্দিষ্ট রূপটি কেন ব্যবহৃত হয়েছে? এটি আয়াতের অর্থ ও সাহিত্যের গভীরতায় কী সৌন্দর্য যোগ করে?`;
      }
    } else {"""

new_ai_prompt_branches = """    } else if (state.lang === 'bn') {
      if (topic === 'nahwu') {
        return `অনুগ্রহ করে পবিত্র কুরআনের সূরা ${suratNama} (${surat}) আয়াত ${ayat}-এ অবস্থিত শব্দ "${kata}" (${noKata}, ${bentuk})-এর আরবি ব্যাকরণ (নাহব/সরফ) ও ই'রাব বিস্তারিতভাবে ব্যাখ্যা করুন:\\n\\nআরবি পাঠ: "${teksArab}"\\nঅনুবাদ: "${teksArti}"\\n\\nঅনুগ্রহ করে নিম্নলিখিত বিষয়গুলো আলোচনা করুন:\\n১. এই বাক্যের গঠনে "${kata}"-এর ব্যাকরণগত ভূমিকা ও ই'রাব (I'rab)।\\n২. শব্দের রূপগত প্রকার (যমীর মুনফাসিল/মুত্তাসিল অথবা ইসম মাওসুল) এবং এর অবস্থা (মারফু'/মানসুব/মাজরুর)।\\n৩. ব্যাকরণগত নোট: ${grammarDesc || 'প্রমিত কুরআনিক প্রয়োগ'}।`;
      } else if (topic === 'tafsir') {
        return `অনুগ্রহ করে সূরা ${suratNama} (${surat}) আয়াত ${ayat}-এর সংক্ষিপ্ত ও প্রাসঙ্গিক তাফসির (ব্যাখ্যা) উপস্থাপন করুন:\\n\\nআরবি পাঠ: "${teksArab}"\\nঅনুবাদ: "${teksArti}"\\n\\nবিশেষ করে শব্দ/সর্বনাম "${kata}"-এর তাৎপর্যের ওপর গুরুত্ব দিয়ে বলুন, এই আয়াতে কী মূল হেকমত, শানে নুযূল এবং ঐশী বার্তা নিহিত রয়েছে?`;
      } else {
        return `সূরা ${suratNama} (${surat}) আয়াত ${ayat}-এ শব্দ "${kata}" নির্বাচনের ক্ষেত্রে কুরআনিক বালাগাত (অলঙ্কারিক সৌন্দর্য ও রচনাশৈলী) ব্যাখ্যা করুন:\\n\\nআরবি পাঠ: "${teksArab}"\\nঅনুবাদ: "${teksArti}"\\n\\nএখানে সর্বনামের এই নির্দিষ্ট রূপটি কেন ব্যবহৃত হয়েছে? এটি আয়াতের অর্থ ও সাহিত্যের গভীরতায় কী সৌন্দর্য যোগ করে?`;
      }
    } else if (state.lang === 'ru') {
      if (topic === 'nahwu') {
        return `Пожалуйста, подробно объясните арабскую грамматику (нахву/сарф) и и'раб (синтаксический разбор) слова "${kata}" (${noKata}, ${bentuk}) в Суре ${suratNama} (${surat}), аят ${ayat}:\\n\\nАрабский текст: "${teksArab}"\\nПеревод: "${teksArti}"\\n\\nПожалуйста, включите следующие пункты:\\n1. Грамматическая роль "${kata}" в структуре этого предложения и его и'раб (падежное состояние: марфу'/мансуб/маджрур).\\n2. Морфологическая классификация (Дамир мунфасыль/муттасыль или Исм маусуль).\\n3. Грамматическое примечание: ${grammarDesc || 'Классическое кораническое употребление'}.`;
      } else if (topic === 'tafsir') {
        return `Пожалуйста, представьте краткий и контекстуальный тафсир (толкование) Суры ${suratNama} (${surat}), аят ${ayat}:\\n\\nАрабский текст: "${teksArab}"\\nПеревод: "${teksArti}"\\n\\nУделив особое внимание значению слова/местоимения "${kata}", объясните, какой главный смысл, повод ниспослания (сабаб ан-нузуль) и духовное наставление заключены в этом аяте?`;
      } else {
        return `Объясните кораническую риторику и стилистику (баляга) в выборе слова "${kata}" в Суре ${suratNama} (${surat}), аят ${ayat}:\\n\\nАрабский текст: "${teksArab}"\\nПеревод: "${teksArti}"\\n\\nПочему здесь использована именно эта конкретная грамматическая форма? Какую смысловую глубину и красоту она придает аяту?`;
      }
    } else {"""
code = code.replace(old_ai_prompt_branches, new_ai_prompt_branches)

# 11. openAiModal
old_modal_arti = """      } else if (state.lang === 'bn') {
        activeArti = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
      }"""
new_modal_arti = """      } else if (state.lang === 'bn') {
        activeArti = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
      } else if (state.lang === 'ru') {
        activeArti = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
      }"""
code = code.replace(old_modal_arti, new_modal_arti)

# 12. CSV Export
old_csv_header = "Artha (HI),Orthobhed (BN),Frekuensi"
new_csv_header = "Artha (HI),Orthobhed (BN),Znachenie (RU),Frekuensi"
code = code.replace(old_csv_header, new_csv_header)

old_csv_header2 = "Anuvad (HI),Onubad (BN),Link Audio"
new_csv_header2 = "Anuvad (HI),Onubad (BN),Perevod (RU),Link Audio"
code = code.replace(old_csv_header2, new_csv_header2)

old_csv_body1 = """      const cleanArtiBN = (occ.teksArtiBN || '').replace(/"/g, '""');
      const audioLink = occ.audioUrl || '';"""
new_csv_body1 = """      const cleanArtiBN = (occ.teksArtiBN || '').replace(/"/g, '""');
      const cleanArtiRU = (occ.teksArtiRU || '').replace(/"/g, '""');
      const audioLink = occ.audioUrl || '';"""
code = code.replace(old_csv_body1, new_csv_body1)

code = code.replace(
    '="${group.arti_bn || \'\'}","${group.frek || \'Muttashil\'}"',
    '="${group.arti_bn || \'\'}","${group.arti_ru || \'\'}","${group.frek || \'Muttashil\'}"'
)
code = code.replace(
    '"${cleanArtiBN}","${audioLink}"',
    '"${cleanArtiBN}","${cleanArtiRU}","${audioLink}"'
)

# 13. btnCopyAll
old_copy_arti = """        } else if (state.lang === 'bn') {
          activeArti = group.arti_bn || group.arti;
        }"""
new_copy_arti = """        } else if (state.lang === 'bn') {
          activeArti = group.arti_bn || group.arti;
        } else if (state.lang === 'ru') {
          activeArti = group.arti_ru || group.arti;
        }"""
code = code.replace(old_copy_arti, new_copy_arti)

old_copy_mawshul = """          else if (state.lang === 'bn') titlePrefix = 'কুরআনিক সম্বন্ধবাচক সর্বনাম (Mawshul)';"""
new_copy_mawshul = """          else if (state.lang === 'bn') titlePrefix = 'কুরআনিক সম্বন্ধবাচক সর্বনাম (Mawshul)';
          else if (state.lang === 'ru') titlePrefix = 'Коранические относительные местоимения (Mawshul)';"""
code = code.replace(old_copy_mawshul, new_copy_mawshul)

old_copy_dhamir = """          else if (state.lang === 'bn') titlePrefix = 'কুরআনিক সর্বনাম (Dhamir)';"""
new_copy_dhamir = """          else if (state.lang === 'bn') titlePrefix = 'কুরআনিক সর্বনাম (Dhamir)';
          else if (state.lang === 'ru') titlePrefix = 'Коранические местоимения (Dhamir)';"""
code = code.replace(old_copy_dhamir, new_copy_dhamir)

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(code)

print(f"[OK] Successfully updated {app_js_path} for Russian (ru) language!")
