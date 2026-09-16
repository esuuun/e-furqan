#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add Persian / Farsi (fa) language support to app.js
"""

import sys
import os

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Normalize line endings
crlf = '\r\n' in code
code = code.replace('\r\n', '\n')

# 1. State lang validation
code = code.replace(
    "['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw'].includes(localStorage.getItem('dhamir_lang'))",
    "['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa'].includes(localStorage.getItem('dhamir_lang'))"
)

# 2. Add I18N.fa dictionary
fa_dict = '''    fa: {
      pageTitle: "فرهنگ جامع جامد مبنی | لغت‌نامه و مراجع تعاملی آیات قرآن کریم",
      brandTitle: "فرهنگ <span>جامد مبنی</span>",
      brandSubtitle: "لغت‌نامه تعاملی انواع کلمات و شماره کلمات قرآن کریم",
      themeToggleTitle: "تغییر حالت روشن / تاریک",
      labelLangSelect: "زبان ترجمه و صوت:",
      translationSourceHtml: "ترجمه: <strong>آیت‌الله ناصر مکارم شیرازی</strong>",
      
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
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_fa || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_fa || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'اسم موصول' : 'ضمیر';
        return `${prefix} ${cleanWord}, ${latin}به معنی ${arti}. ${desc ? 'توضیحات: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }'''

code = code.replace(
    '  };\n\n  // Helper for current i18n text',
    ',\n' + fa_dict + '\n  };\n\n  // Helper for current i18n text'
)

# 3. Update initData in app.js
code = code.replace(
    "bentuk_sw: item['BentukKataSW'] || (b === '1. Dhamir' ? '1. Viwakilishi vya Nafsi (Dhamir - Pronouns)' : (b === '2. Mawshul' ? '2. Majina ya Kuunganisha (Mawshul - Relative Pronouns)' : b)),",
    "bentuk_sw: item['BentukKataSW'] || (b === '1. Dhamir' ? '1. Viwakilishi vya Nafsi (Dhamir - Pronouns)' : (b === '2. Mawshul' ? '2. Majina ya Kuunganisha (Mawshul - Relative Pronouns)' : b)),\n          bentuk_fa: item['BentukKataFA'] || (b === '1. Dhamir' ? '۱. ضمایر (Dhamir - Pronouns)' : (b === '2. Mawshul' ? '۲. اسم‌های موصول (Mawshul - Relative Pronouns)' : b)),"
)

code = code.replace(
    "arti_sw: item['ArtiKataSW'] || grammar.arti_sw || item['ArtiKataID'] || item['Arti kata'],",
    "arti_sw: item['ArtiKataSW'] || grammar.arti_sw || item['ArtiKataID'] || item['Arti kata'],\n          arti_fa: item['ArtiKataFA'] || grammar.arti_fa || item['ArtiKataID'] || item['Arti kata'],"
)

code = code.replace(
    "suratArtiSW: item['SuratArtiSW'] || item['SuratArtiEN'] || item['SuratArti'] || '',",
    "suratArtiSW: item['SuratArtiSW'] || item['SuratArtiEN'] || item['SuratArti'] || '',\n        suratArtiFA: item['SuratArtiFA'] || item['SuratArtiEN'] || item['SuratArti'] || '',"
)

code = code.replace(
    "teksArtiSW: item['TeksArtiSW'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',",
    "teksArtiSW: item['TeksArtiSW'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',\n        teksArtiFA: item['TeksArtiFA'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',"
)

# 4. Update getDefaultJenis defaultMap
code = code.replace(
    "sw: 'Munfashil (Kiwakilishi Huru)'",
    "sw: 'Munfashil (Kiwakilishi Huru)', fa: 'منفصل مرفوعی (ضمایر جدا)'"
)
code = code.replace(
    "sw: 'Isim Mawshul (Jina la Kuunganisha)'",
    "sw: 'Isim Mawshul (Jina la Kuunganisha)', fa: 'اسم موصول'"
)
code = code.replace(
    "sw: 'Isim Istifham (Neno la Kuulizia)'",
    "sw: 'Isim Istifham (Neno la Kuulizia)', fa: 'اسم استفهام (کلمات پرسشی)'"
)
code = code.replace(
    "sw: 'Isim Syarat (Neno la Sharti)'",
    "sw: 'Isim Syarat (Neno la Sharti)', fa: 'ادوات شرط'"
)
code = code.replace(
    "sw: 'Isim Isyarah (Jina la Kuonyeshea)'",
    "sw: 'Isim Isyarah (Jina la Kuonyeshea)', fa: 'اسم اشاره'"
)
code = code.replace(
    "sw: 'Isim Fi\\'il (Jina la Kitendo)'",
    "sw: 'Isim Fi\\'il (Jina la Kitendo)', fa: 'اسم فعل'"
)
code = code.replace(
    "sw: 'Fi\\'il Jamid (Kitendo Kisichobadilika)'",
    "sw: 'Fi\\'il Jamid (Kitendo Kisichobadilika)', fa: 'فعل جامد'"
)

# 5. Update populateNoKata in app.js
code = code.replace(
    "} else if (state.lang === 'sw') {\n        localizedArti = group.arti_sw || group.arti_id || group.arti;\n      }",
    "} else if (state.lang === 'sw') {\n        localizedArti = group.arti_sw || group.arti_id || group.arti;\n      } else if (state.lang === 'fa') {\n        localizedArti = group.arti_fa || group.arti_id || group.arti;\n      }"
)

# 6. Update updateSpotlightCard in app.js
code = code.replace(
    "} else if (state.lang === 'sw') {\n      elements.badgeBentukKata.textContent = group.bentuk_sw || group.bentuk_id;\n    } else {",
    "} else if (state.lang === 'sw') {\n      elements.badgeBentukKata.textContent = group.bentuk_sw || group.bentuk_id;\n    } else if (state.lang === 'fa') {\n      elements.badgeBentukKata.textContent = group.bentuk_fa || group.bentuk_id;\n    } else {"
)

code = code.replace(
    "} else if (state.lang === 'sw') {\n      jenisText = grammar.jenis_sw || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'sw');\n    } else {",
    "} else if (state.lang === 'sw') {\n      jenisText = grammar.jenis_sw || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'sw');\n    } else if (state.lang === 'fa') {\n      jenisText = grammar.jenis_fa || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'fa');\n    } else {"
)

code = code.replace(
    "} else if (state.lang === 'sw') {\n      currentMeaning = group.arti_sw || group.arti_id || group.arti;\n    }",
    "} else if (state.lang === 'sw') {\n      currentMeaning = group.arti_sw || group.arti_id || group.arti;\n    } else if (state.lang === 'fa') {\n      currentMeaning = group.arti_fa || group.arti_id || group.arti;\n    }"
)

code = code.replace(
    "} else if (state.lang === 'sw') {\n      currentDesc = grammar.desc_sw || grammar.desc_id || grammar.keterangan || '';\n    }",
    "} else if (state.lang === 'sw') {\n      currentDesc = grammar.desc_sw || grammar.desc_id || grammar.keterangan || '';\n    } else if (state.lang === 'fa') {\n      currentDesc = grammar.desc_fa || grammar.desc_id || grammar.keterangan || '';\n    }"
)

# 7. Update renderAyatReferences (search filter and card rendering) in app.js
code = code.replace(
    "} else if (state.lang === 'sw') {\n          sArti = occ.suratArtiSW;\n          tArti = occ.teksArtiSW;\n        }",
    "} else if (state.lang === 'sw') {\n          sArti = occ.suratArtiSW;\n          tArti = occ.teksArtiSW;\n        } else if (state.lang === 'fa') {\n          sArti = occ.suratArtiFA;\n          tArti = occ.teksArtiFA;\n        }"
)

code = code.replace(
    "} else if (state.lang === 'sw') {\n      activeSuratArti = occ.suratArtiSW || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiSW || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }",
    "} else if (state.lang === 'sw') {\n      activeSuratArti = occ.suratArtiSW || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiSW || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    } else if (state.lang === 'fa') {\n      activeSuratArti = occ.suratArtiFA || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiFA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }"
)

# 8. Update toggleVerseTranslationAudio in app.js
code = code.replace(
    "} else if (state.lang === 'sw') {\n      currentText = occ.teksArtiSW || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }",
    "} else if (state.lang === 'sw') {\n      currentText = occ.teksArtiSW || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    } else if (state.lang === 'fa') {\n      currentText = occ.teksArtiFA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }"
)

# 9. Update getSpeechVoiceAndLang in app.js
code = code.replace(
    "} else if (langKey === 'sw') {\n      speechLangCode = 'sw-TZ';\n      matchVoice = voices.find(v => v.lang.startsWith('sw') || v.lang.includes('sw-') || v.name.toLowerCase().includes('swahili') || v.name.toLowerCase().includes('kiswahili')) || voices.find(v => v.lang.startsWith('sw'));",
    "} else if (langKey === 'sw') {\n      speechLangCode = 'sw-TZ';\n      matchVoice = voices.find(v => v.lang.startsWith('sw') || v.lang.includes('sw-') || v.name.toLowerCase().includes('swahili') || v.name.toLowerCase().includes('kiswahili')) || voices.find(v => v.lang.startsWith('sw'));\n    } else if (langKey === 'fa') {\n      speechLangCode = 'fa-IR';\n      matchVoice = voices.find(v => v.lang.startsWith('fa') || v.lang.includes('fa-') || v.name.toLowerCase().includes('persian') || v.name.toLowerCase().includes('farsi') || v.name.includes('فارسی') || v.name.includes('Dilara') || v.name.includes('Farid')) || voices.find(v => v.lang.startsWith('fa'));"
)

# 10. Update speakDhamirMeaning in app.js
code = code.replace(
    "} else if (state.lang === 'sw') {\n      activeMeaning = group.arti_sw || group.arti_id || group.arti;\n    }",
    "} else if (state.lang === 'sw') {\n      activeMeaning = group.arti_sw || group.arti_id || group.arti;\n    } else if (state.lang === 'fa') {\n      activeMeaning = group.arti_fa || group.arti_id || group.arti;\n    }"
)

# 11. Update openAiModal & buildAiPrompt in app.js
code = code.replace(
    "} else if (state.lang === 'sw') {\n        activeArti = occ.teksArtiSW || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }",
    "} else if (state.lang === 'sw') {\n        activeArti = occ.teksArtiSW || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      } else if (state.lang === 'fa') {\n        activeArti = occ.teksArtiFA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }"
)

code = code.replace(
    "} else if (state.lang === 'sw') {\n      teksArti = occ.teksArtiSW || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_sw || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    }",
    "} else if (state.lang === 'sw') {\n      teksArti = occ.teksArtiSW || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_sw || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    } else if (state.lang === 'fa') {\n      teksArti = occ.teksArtiFA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_fa || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    }"
)

fa_ai_prompt = """    } else if (state.lang === 'fa') {
      if (topic === 'nahwu') {
        return `لطفاً نکات صرفی، نحوی (قواعد زبان عربی) و اعراب کلمه «${kata}» (${noKata}, ${bentuk}) در سوره ${suratNama} (${surat})، آیه ${ayat} را به طور جامع تحلیل فرمایید:\\n\\nمتن عربی آیه: «${teksArab}»\\nترجمه فارسی آیه: «${teksArti}»\\n\\nلطفاً موارد زیر را بررسی نمایید:\\n۱. نقش نحوی، محل اعراب و کارکرد «${kata}» در این جمله (مرفوع / منصوب / مجرور).\\n۲. نوع کلمه (ضمیر / موصول / ادوات شرط و غیره) و ویژگی‌های ساختاری آن (منفصل / متصل).\\n۳. توضیحات تکمیلی نحوی: ${grammarDesc || "بر اساس قواعد بلاغی و ادبی قرآن کریم"}.`;
      } else if (topic === 'tafsir') {
        return `لطفاً تفسیر و شرحی پرمحتوا و مختصر درباره سوره ${suratNama} (${surat})، آیه ${ayat} ارائه فرمایید:\\n\\nمتن عربی آیه: «${teksArab}»\\nترجمه فارسی آیه: «${teksArti}»\\n\\nبا تمرکز بر مفهوم و کارکرد کلمه «${kata}»: چه حکمت، شأن نزول (در صورت وجود) و پیام‌های هدایت‌بخشی در این آیه برای زندگی مؤمنان نهفته است؟`;
      } else {
        return `لطفاً زیبایی‌های بلاغی و اعجاز ادبی قرآن کریم (فصاحت، ایجاز و صنایع ادبی) در خصوص انتخاب کلمه «${kata}» در سوره ${suratNama} (${surat})، آیه ${ayat} را تبیین فرمایید:\\n\\nمتن عربی آیه: «${teksArab}»\\nترجمه فارسی آیه: «${teksArti}»\\n\\nچرا این واژه یا ضمیر در این بافت خاص به کار رفته و چه عمق معنایی و ظرافتی به آیه بخشیده است؟`;
      }"""

code = code.replace(
    "    } else if (state.lang === 'sw') {",
    fa_ai_prompt + "\n    } else if (state.lang === 'sw') {"
)

# 12. Update exportToCsv in app.js
code = code.replace(
    "const cleanArtiSW = (occ.teksArtiSW || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');",
    "const cleanArtiSW = (occ.teksArtiSW || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');\n        const cleanArtiFA = (occ.teksArtiFA || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');"
)

code = code.replace(
    ',\\"Maana (SW)\\",',
    ',\\"Maana (SW)\\",\\"معنی (FA)\\",'
)

code = code.replace(
    ',\\"Tafsiri (SW)\\",',
    ',\\"Tafsiri (SW)\\",\\"ترجمه (FA)\\",'
)

code = code.replace(
    '"${group.arti_ha || \'\'}","${group.arti_sw || \'\'}","${group.frek || \'Muttashil\'}"',
    '"${group.arti_ha || \'\'}","${group.arti_sw || \'\'}","${group.arti_fa || \'\'}","${group.frek || \'Muttashil\'}"'
)

code = code.replace(
    '"${cleanArtiHA}","${cleanArtiSW}",',
    '"${cleanArtiHA}","${cleanArtiSW}","${cleanArtiFA}",'
)

# 13. Update btnCopyAll in app.js
code = code.replace(
    "} else if (state.lang === 'sw') {\n          activeArti = group.arti_sw || group.arti_id || group.arti;\n        }",
    "} else if (state.lang === 'sw') {\n          activeArti = group.arti_sw || group.arti_id || group.arti;\n        } else if (state.lang === 'fa') {\n          activeArti = group.arti_fa || group.arti_id || group.arti;\n        }"
)

code = code.replace(
    "} else if (state.lang === 'sw') {\n          activeDesc = grammar.desc_sw || grammar.desc_id || grammar.keterangan || '';\n        }",
    "} else if (state.lang === 'sw') {\n          activeDesc = grammar.desc_sw || grammar.desc_id || grammar.keterangan || '';\n        } else if (state.lang === 'fa') {\n          activeDesc = grammar.desc_fa || grammar.desc_id || grammar.keterangan || '';\n        }"
)

code = code.replace(
    "else if (state.lang === 'sw') titlePrefix = 'Majina ya Kuunganisha ya Qur\\'ani (Mawshul)';",
    "else if (state.lang === 'sw') titlePrefix = 'Majina ya Kuunganisha ya Qur\\'ani (Mawshul)';\n          else if (state.lang === 'fa') titlePrefix = 'اسم‌های موصول قرآن کریم (موصول)';"
)

code = code.replace(
    "else if (state.lang === 'sw') titlePrefix = 'Viwakilishi vya Nafsi vya Qur\\'ani (Dhamir)';",
    "else if (state.lang === 'sw') titlePrefix = 'Viwakilishi vya Nafsi vya Qur\\'ani (Dhamir)';\n          else if (state.lang === 'fa') titlePrefix = 'ضمایر قرآن کریم (ضمیر)';"
)

# 14. Update applyLanguage in app.js
code = code.replace(
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw'].includes(lang) ? lang : 'id';",
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa'].includes(lang) ? lang : 'id';"
)

if crlf:
    code = code.replace('\n', '\r\n')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("app.js successfully updated with Persian support!")
