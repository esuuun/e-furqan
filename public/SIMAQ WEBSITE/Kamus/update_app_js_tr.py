#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to update app.js with Turkish (tr) support.
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

# 1. State lang validation
code = code.replace(
    "['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es']",
    "['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr']"
)

# 2. Add I18N.tr
tr_dict = '''    tr: {
      pageTitle: "Câmid Mebnî Sözlüğü | İnteraktif Kur'an Kelime & Ayet Referansları",
      brandTitle: "Câmid Mebnî <span>Sözlüğü</span>",
      brandSubtitle: "Kelime Formları ve Numaraları İçin İnteraktif Sözlük",
      themeToggleTitle: "Koyu / Açık Temayı Değiştir",
      labelLangSelect: "Meal ve Ses Dili:",
      translationSourceHtml: "Meal: <strong>Diyanet İşleri Başkanlığı</strong>",
      
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
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_tr || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_tr || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'İsmi mevsul' : 'Zamir';
        return `${prefix} ${cleanWord}, ${latin}anlamı ${arti}. ${desc ? 'Açıklama: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }'''

code = code.replace(
    '  };\n\n  // Helper for current i18n text',
    ',\n' + tr_dict + '\n  };\n\n  // Helper for current i18n text'
)

# 3. Update initData in app.js
code = code.replace(
    "bentuk_es: item['BentukKataES'] || (b === '1. Dhamir' ? '1. Pronombres (Dhamir)' : (b === '2. Mawshul' ? '2. Pronombres Relativos (Mawshul)' : b)),",
    "bentuk_es: item['BentukKataES'] || (b === '1. Dhamir' ? '1. Pronombres (Dhamir)' : (b === '2. Mawshul' ? '2. Pronombres Relativos (Mawshul)' : b)),\n          bentuk_tr: item['BentukKataTR'] || (b === '1. Dhamir' ? '1. Zamirler (Dhamir - Şahıs Zamirleri)' : (b === '2. Mawshul' ? '2. İsmi Mevsul (Mawshul - İlgi Zamirleri)' : b)),"
)

code = code.replace(
    "arti_es: item['ArtiKataES'] || grammar.arti_es || item['ArtiKataID'] || item['Arti kata'],",
    "arti_es: item['ArtiKataES'] || grammar.arti_es || item['ArtiKataID'] || item['Arti kata'],\n          arti_tr: item['ArtiKataTR'] || grammar.arti_tr || item['ArtiKataID'] || item['Arti kata'],"
)

code = code.replace(
    "suratArtiES: item['SuratArtiES'] || item['SuratArtiEN'] || item['SuratArti'] || '',",
    "suratArtiES: item['SuratArtiES'] || item['SuratArtiEN'] || item['SuratArti'] || '',\n        suratArtiTR: item['SuratArtiTR'] || item['SuratArtiEN'] || item['SuratArti'] || '',"
)

code = code.replace(
    "teksArtiES: item['TeksArtiES'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',",
    "teksArtiES: item['TeksArtiES'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',\n        teksArtiTR: item['TeksArtiTR'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',"
)

# 4. Update getDefaultJenis in app.js
tr_default_jenis = """      if (lang === 'tr') {
        const jenisMapTR = {
          '1. Dhamir': 'Zamirler (Dhamir)',
          '2. Mawshul': 'İsmi Mevsul (Mawshul)',
          '3. Istifham': 'Soru Edatları (İstifham)',
          '4. Syarath': 'Şart Edatları (Şart)',
          '5. Isyarah': 'İşaret İsimleri (İsm-i İşâre)',
          "6. Isim Fi'il": "İsim Fiil (İsm-i Fiil)",
          "7. Fi'il Jamid": "Camid Fiil (Fi'l-i Câmid)"
        };
        return jenisMapTR[bentuk] || "Kur'an Grameri";
      }"""

code = code.replace(
    "if (lang === 'es') {",
    tr_default_jenis + "\n      if (lang === 'es') {"
)

# 5. Update populateBentukKata in app.js
code = code.replace(
    "else if (state.lang === 'es') localizedBentuk = group.bentuk_es || group.bentuk_id || group.bentuk;",
    "else if (state.lang === 'es') localizedBentuk = group.bentuk_es || group.bentuk_id || group.bentuk;\n        else if (state.lang === 'tr') localizedBentuk = group.bentuk_tr || group.bentuk_id || group.bentuk;"
)

# 6. Update populateNoKata in app.js
code = code.replace(
    "else if (state.lang === 'es') localizedArti = group.arti_es || group.arti_id || group.arti;",
    "else if (state.lang === 'es') localizedArti = group.arti_es || group.arti_id || group.arti;\n          else if (state.lang === 'tr') localizedArti = group.arti_tr || group.arti_id || group.arti;"
)

# 7. Update updateSpotlightCard in app.js
code = code.replace(
    "} else if (state.lang === 'es') {\n      bentukText = group.bentuk_es || group.bentuk_id || group.bentuk;\n    }",
    "} else if (state.lang === 'es') {\n      bentukText = group.bentuk_es || group.bentuk_id || group.bentuk;\n    } else if (state.lang === 'tr') {\n      bentukText = group.bentuk_tr || group.bentuk_id || group.bentuk;\n    }"
)

code = code.replace(
    "} else if (state.lang === 'es') {\n      jenisText = grammar.jenis_es || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'es');\n    }",
    "} else if (state.lang === 'es') {\n      jenisText = grammar.jenis_es || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'es');\n    } else if (state.lang === 'tr') {\n      jenisText = grammar.jenis_tr || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'tr');\n    }"
)

code = code.replace(
    "} else if (state.lang === 'es') {\n      currentMeaning = group.arti_es || group.arti_id || group.arti;\n    }",
    "} else if (state.lang === 'es') {\n      currentMeaning = group.arti_es || group.arti_id || group.arti;\n    } else if (state.lang === 'tr') {\n      currentMeaning = group.arti_tr || group.arti_id || group.arti;\n    }"
)

code = code.replace(
    "} else if (state.lang === 'es') {\n      currentDesc = grammar.desc_es || grammar.desc_id || grammar.keterangan || '';\n    }",
    "} else if (state.lang === 'es') {\n      currentDesc = grammar.desc_es || grammar.desc_id || grammar.keterangan || '';\n    } else if (state.lang === 'tr') {\n      currentDesc = grammar.desc_tr || grammar.desc_id || grammar.keterangan || '';\n    }"
)

# 8. Update renderAyatReferences in app.js
code = code.replace(
    "} else if (state.lang === 'es') {\n        currentSuratArti = occ.suratArtiES || occ.suratArtiEN || '';\n      }",
    "} else if (state.lang === 'es') {\n        currentSuratArti = occ.suratArtiES || occ.suratArtiEN || '';\n      } else if (state.lang === 'tr') {\n        currentSuratArti = occ.suratArtiTR || occ.suratArtiEN || '';\n      }"
)

code = code.replace(
    "} else if (state.lang === 'es') {\n        currentText = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }",
    "} else if (state.lang === 'es') {\n        currentText = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      } else if (state.lang === 'tr') {\n        currentText = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }"
)

# 9. Update TTS voice in speakDhamirMeaning and toggleVerseTranslationAudio
code = code.replace(
    "} else if (state.lang === 'es') {\n        utterance.lang = 'es-ES';\n        langVoice = voices.find(v => v.lang.startsWith('es')) || voices.find(v => v.lang.includes('ES'));\n      }",
    "} else if (state.lang === 'es') {\n        utterance.lang = 'es-ES';\n        langVoice = voices.find(v => v.lang.startsWith('es')) || voices.find(v => v.lang.includes('ES'));\n      } else if (state.lang === 'tr') {\n        utterance.lang = 'tr-TR';\n        langVoice = voices.find(v => v.lang.startsWith('tr')) || voices.find(v => v.lang.includes('TR'));\n      }"
)

# 10. Update openAiModal in app.js
code = code.replace(
    "else if (state.lang === 'es') activeTeksArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;",
    "else if (state.lang === 'es') activeTeksArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    else if (state.lang === 'tr') activeTeksArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;"
)

# 11. Update buildAiPrompt in app.js
code = code.replace(
    "} else if (state.lang === 'es') {\n      teksArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_es || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    }",
    "} else if (state.lang === 'es') {\n      teksArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_es || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    } else if (state.lang === 'tr') {\n      teksArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_tr || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    }"
)

tr_ai_prompt = """    } else if (state.lang === 'tr') {
      if (topic === 'nahwu') {
        return `Lütfen Kur'an-ı Kerim ${suratNama} Suresi (${surat}), ${ayat}. Ayetinde geçen "${kata}" (${noKata}, ${bentuk}) kelimesinin Arapça Nahiv/Sarf kurallarını ve İ'rab analizini ayrıntılı olarak açıklayınız:\\n\\nArapça Metin: "${teksArab}"\\nTürkçe Meali: "${teksArti}"\\n\\nLütfen şu hususları detaylandırınız:\\n1. "${kata}" kelimesinin cümle içindeki sentaktik konumu ve İ'rab alameti (Merfû / Mansûb / Mecrûr).\\n2. Morfolojik kategorisi (Dhamir / Mevsul / Şart vb. türü) ve zamir özellikleri (Munfasıl / Muttasıl vb.).\\n3. Gramer notları: ${grammarDesc || "Kur'an'daki standart kullanımı"}.`;
      } else if (topic === 'tafsir') {
        return `Lütfen ${suratNama} Suresi (${surat}), ${ayat}. Ayeti için özlü ve bağlamsal bir Tefsir açıklaması sununuz:\\n\\nArapça Metin: "${teksArab}"\\nTürkçe Meali: "${teksArti}"\\n\\nÖzellikle seçilen "${kata}" kelimesine / zamirine odaklanarak; bu ayetin temel hikmeti, nüzul sebebi (varsa sebebi nüzul) ve içerdiği teolojik mesaj nedir?`;
      } else {
        return `Lütfen ${suratNama} Suresi (${surat}), ${ayat}. Ayetinde "${kata}" kelimesinin tercih edilmesindeki Kur'an Belâğatı ve edebî incelikleri açıklayınız:\\n\\nArapça Metin: "${teksArab}"\\nTürkçe Meali: "${teksArti}"\\n\\nNeden özellikle bu zamir / kelime formu tercih edilmiştir? Ayetin ahengine, anlamına ve vurgusuna ne gibi bir edebî derinlik katmaktadır?`;
      }"""

code = code.replace(
    "    } else if (state.lang === 'es') {",
    tr_ai_prompt + "\n    } else if (state.lang === 'es') {"
)

# 12. Update exportToCsv in app.js
code = code.replace(
    "} else if (state.lang === 'es') {\n        activeArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }",
    "} else if (state.lang === 'es') {\n        activeArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      } else if (state.lang === 'tr') {\n        activeArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }"
)

code = code.replace(
    ',\\"Arti Kata (ES)\\",',
    ',\\"Arti Kata (ES)\\",\\"Arti Kata (TR)\\",'
)

code = code.replace(
    "const cleanArtiES = (occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');",
    "const cleanArtiES = (occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');\n        const cleanArtiTR = (occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');"
)

code = code.replace(
    '"${cleanArtiZH}","${cleanArtiES}"\\n`;',
    '"${cleanArtiZH}","${cleanArtiES}","${cleanArtiTR}"\\n`;'
)

# 13. Update btnCopyAll in app.js
code = code.replace(
    "} else if (state.lang === 'es') {\n          activeArti = group.arti_es || group.arti_id || group.arti;\n        }",
    "} else if (state.lang === 'es') {\n          activeArti = group.arti_es || group.arti_id || group.arti;\n        } else if (state.lang === 'tr') {\n          activeArti = group.arti_tr || group.arti_id || group.arti;\n        }"
)

code = code.replace(
    "else if (state.lang === 'es') titlePrefix = 'Pronombre Relativo del Corán (Mawshul)';",
    "else if (state.lang === 'es') titlePrefix = 'Pronombre Relativo del Corán (Mawshul)';\n          else if (state.lang === 'tr') titlePrefix = 'Kur\\'an-ı Kerim İsmi Mevsul (Mawshul)';"
)

code = code.replace(
    "else if (state.lang === 'es') titlePrefix = 'Pronombre del Corán (Dhamir)';",
    "else if (state.lang === 'es') titlePrefix = 'Pronombre del Corán (Dhamir)';\n          else if (state.lang === 'tr') titlePrefix = 'Kur\\'an-ı Kerim Zamirleri (Dhamir)';"
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated app.js with Turkish support successfully!")
