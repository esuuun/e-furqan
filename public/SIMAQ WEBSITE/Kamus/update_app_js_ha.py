#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add Hausa (ha) language support to app.js
"""

import sys
import os
import re

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
    "['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt'].includes(localStorage.getItem('dhamir_lang'))",
    "['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha'].includes(localStorage.getItem('dhamir_lang'))"
)

# 2. Add I18N.ha dictionary
ha_dict = '''    ha: {
      pageTitle: "Ƙamus ɗin Jamid Mabny | Ƙamus da Manazartar Ayoyin Al-Ƙur'ani Mai Girma",
      brandTitle: "Ƙamus ɗin <span>Jamid Mabny</span>",
      brandSubtitle: "Ƙamus Mai Ma'amala don Sigar Kalmomi da Lambobin Kalmomi",
      themeToggleTitle: "Sauya Haske / Duhu na Fuska",
      labelLangSelect: "Harshen Fassara da Murya:",
      translationSourceHtml: "Fassara: <strong>Sheikh Abubakar Mahmoud Gumi</strong>",
      
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
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ha || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ha || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Sunan sadarwa' : 'Wakilin suna';
        return `${prefix} ${cleanWord}, ${latin}ma'ana ${arti}. ${desc ? 'Bayani: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }'''

code = code.replace(
    '  };\n\n  // Helper for current i18n text',
    ',\n' + ha_dict + '\n  };\n\n  // Helper for current i18n text'
)

# 3. Update initData in app.js
code = code.replace(
    "bentuk_pt: item['BentukKataPT'] || (b === '1. Dhamir' ? '1. Pronomes (Dhamir - Pronomes Pessoais)' : (b === '2. Mawshul' ? '2. Pronomes Relativos (Mawshul)' : b)),",
    "bentuk_pt: item['BentukKataPT'] || (b === '1. Dhamir' ? '1. Pronomes (Dhamir - Pronomes Pessoais)' : (b === '2. Mawshul' ? '2. Pronomes Relativos (Mawshul)' : b)),\n          bentuk_ha: item['BentukKataHA'] || (b === '1. Dhamir' ? '1. Wakilan Suna (Dhamir - Pronouns)' : (b === '2. Mawshul' ? '2. Sunayen Sadarwa (Mawshul - Relative Pronouns)' : b)),"
)

code = code.replace(
    "arti_pt: item['ArtiKataPT'] || grammar.arti_pt || item['ArtiKataID'] || item['Arti kata'],",
    "arti_pt: item['ArtiKataPT'] || grammar.arti_pt || item['ArtiKataID'] || item['Arti kata'],\n          arti_ha: item['ArtiKataHA'] || grammar.arti_ha || item['ArtiKataID'] || item['Arti kata'],"
)

code = code.replace(
    "suratArtiPT: item['SuratArtiPT'] || item['SuratArtiEN'] || item['SuratArti'] || '',",
    "suratArtiPT: item['SuratArtiPT'] || item['SuratArtiEN'] || item['SuratArti'] || '',\n        suratArtiHA: item['SuratArtiHA'] || item['SuratArtiEN'] || item['SuratArti'] || '',"
)

code = code.replace(
    "teksArtiPT: item['TeksArtiPT'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',",
    "teksArtiPT: item['TeksArtiPT'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',\n        teksArtiHA: item['TeksArtiHA'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',"
)

# 4. Update getDefaultJenis defaultMap
code = code.replace(
    "pt: 'Munfashil (Independente)'",
    "pt: 'Munfashil (Independente)', ha: 'Munfashil (Mai Zaman Kansa)'"
)
code = code.replace(
    "pt: 'Pronome Relativo'",
    "pt: 'Pronome Relativo', ha: 'Isim Mawshul (Sunan Sadarwa)'"
)
code = code.replace(
    "pt: 'Interrogativo'",
    "pt: 'Interrogativo', ha: 'Kalmar Tambaya (Istifham)'"
)
code = code.replace(
    "pt: 'Condicional'",
    "pt: 'Condicional', ha: 'Kalmar Sharaɗi (Syarath)'"
)
code = code.replace(
    "pt: 'Demonstrativo'",
    "pt: 'Demonstrativo', ha: 'Sunan Nuni (Isyarah)'"
)
code = code.replace(
    "pt: 'Nome Verbal'",
    "pt: 'Nome Verbal', ha: 'Sunan Aiki (Isim Fi\\'il)'"
)
code = code.replace(
    "pt: 'Verbo Inflexível'",
    "pt: 'Verbo Inflexível', ha: 'Aiki Kafaffe (Fi\\'il Jamid)'"
)

# 5. Update populateNoKata in app.js
code = code.replace(
    "} else if (state.lang === 'pt') {\n        localizedArti = group.arti_pt || group.arti_id || group.arti;\n      }",
    "} else if (state.lang === 'pt') {\n        localizedArti = group.arti_pt || group.arti_id || group.arti;\n      } else if (state.lang === 'ha') {\n        localizedArti = group.arti_ha || group.arti_id || group.arti;\n      }"
)

# 6. Update updateSpotlightCard in app.js
code = code.replace(
    "} else if (state.lang === 'pt') {\n      elements.badgeBentukKata.textContent = group.bentuk_pt || group.bentuk_id;\n    } else {",
    "} else if (state.lang === 'pt') {\n      elements.badgeBentukKata.textContent = group.bentuk_pt || group.bentuk_id;\n    } else if (state.lang === 'ha') {\n      elements.badgeBentukKata.textContent = group.bentuk_ha || group.bentuk_id;\n    } else {"
)

code = code.replace(
    "} else if (state.lang === 'pt') {\n      jenisText = grammar.jenis_pt || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'pt');\n    } else {",
    "} else if (state.lang === 'pt') {\n      jenisText = grammar.jenis_pt || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'pt');\n    } else if (state.lang === 'ha') {\n      jenisText = grammar.jenis_ha || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'ha');\n    } else {"
)

code = code.replace(
    "} else if (state.lang === 'pt') {\n      currentMeaning = group.arti_pt || group.arti_id || group.arti;\n    }",
    "} else if (state.lang === 'pt') {\n      currentMeaning = group.arti_pt || group.arti_id || group.arti;\n    } else if (state.lang === 'ha') {\n      currentMeaning = group.arti_ha || group.arti_id || group.arti;\n    }"
)

code = code.replace(
    "} else if (state.lang === 'pt') {\n      currentDesc = grammar.desc_pt || grammar.desc_id || grammar.keterangan || '';\n    }",
    "} else if (state.lang === 'pt') {\n      currentDesc = grammar.desc_pt || grammar.desc_id || grammar.keterangan || '';\n    } else if (state.lang === 'ha') {\n      currentDesc = grammar.desc_ha || grammar.desc_id || grammar.keterangan || '';\n    }"
)

# 7. Update renderAyatReferences (search filter and card rendering) in app.js
code = code.replace(
    "} else if (state.lang === 'pt') {\n          sArti = occ.suratArtiPT;\n          tArti = occ.teksArtiPT;\n        }",
    "} else if (state.lang === 'pt') {\n          sArti = occ.suratArtiPT;\n          tArti = occ.teksArtiPT;\n        } else if (state.lang === 'ha') {\n          sArti = occ.suratArtiHA;\n          tArti = occ.teksArtiHA;\n        }"
)

code = code.replace(
    "} else if (state.lang === 'pt') {\n      activeSuratArti = occ.suratArtiPT || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }",
    "} else if (state.lang === 'pt') {\n      activeSuratArti = occ.suratArtiPT || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    } else if (state.lang === 'ha') {\n      activeSuratArti = occ.suratArtiHA || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiHA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }"
)

# 8. Update toggleVerseTranslationAudio in app.js
code = code.replace(
    "} else if (state.lang === 'pt') {\n      currentText = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }",
    "} else if (state.lang === 'pt') {\n      currentText = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    } else if (state.lang === 'ha') {\n      currentText = occ.teksArtiHA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }"
)

# 9. Update getSpeechVoiceAndLang in app.js
code = code.replace(
    "} else if (langKey === 'pt') {\n      speechLangCode = 'pt-PT';\n      matchVoice = voices.find(v => v.lang.startsWith('pt') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Heloisa') || v.name.includes('Raquel') || v.name.includes('Portuguese') || v.name.includes('Francisca') || v.name.includes('Duarte') || v.name.includes('Luciana') || v.name.includes('Yara') || v.name.includes('Daniel'))) || voices.find(v => v.lang.startsWith('pt'));",
    "} else if (langKey === 'pt') {\n      speechLangCode = 'pt-PT';\n      matchVoice = voices.find(v => v.lang.startsWith('pt') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Heloisa') || v.name.includes('Raquel') || v.name.includes('Portuguese') || v.name.includes('Francisca') || v.name.includes('Duarte') || v.name.includes('Luciana') || v.name.includes('Yara') || v.name.includes('Daniel'))) || voices.find(v => v.lang.startsWith('pt'));\n    } else if (langKey === 'ha') {\n      speechLangCode = 'ha-NG';\n      matchVoice = voices.find(v => v.lang.startsWith('ha') || v.lang.includes('ha-') || v.name.toLowerCase().includes('hausa')) || voices.find(v => v.lang.startsWith('ha'));"
)

# 10. Update speakDhamirMeaning in app.js
code = code.replace(
    "} else if (state.lang === 'pt') {\n      activeMeaning = group.arti_pt || group.arti_id || group.arti;\n    }",
    "} else if (state.lang === 'pt') {\n      activeMeaning = group.arti_pt || group.arti_id || group.arti;\n    } else if (state.lang === 'ha') {\n      activeMeaning = group.arti_ha || group.arti_id || group.arti;\n    }"
)

# 11. Update openAiModal & buildAiPrompt in app.js
code = code.replace(
    "} else if (state.lang === 'pt') {\n        activeArti = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }",
    "} else if (state.lang === 'pt') {\n        activeArti = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      } else if (state.lang === 'ha') {\n        activeArti = occ.teksArtiHA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }"
)

code = code.replace(
    "} else if (state.lang === 'pt') {\n      teksArti = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_pt || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    }",
    "} else if (state.lang === 'pt') {\n      teksArti = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_pt || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    } else if (state.lang === 'ha') {\n      teksArti = occ.teksArtiHA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_ha || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    }"
)

ha_ai_prompt = """    } else if (state.lang === 'ha') {
      if (topic === 'nahwu') {
        return `Da fatan za a yi cikakken bayanin ƙa'idojin nahawu (Nahwu/Sarf) da I'rabi game da kalmar "${kata}" (${noKata}, ${bentuk}) a cikin Surah ${suratNama} (${surat}), Aya ${ayat}:\\n\\nNassin Larabci: "${teksArab}"\\nFassarar Hausa: "${teksArti}"\\n\\nDa fatan a duba waɗannan abubuwan:\\n1. Matsayin i'rabi da aikin "${kata}" a cikin wannan jumla (Marfu' / Manshub / Majrur).\\n2. Nau'in kalmar (Dhamir / Mawshul / da sauransu) da siffofinta (Munfashil / Muttashil).\\n3. Ƙarin bayanin nahawu: ${grammarDesc || "Bisa ƙa'idar yaren Al-Ƙur'ani"}.`;
      } else if (topic === 'tafsir') {
        return `Da fatan a bayar da taƙaitaccen tafsiri mai fa'ida game da Surah ${suratNama} (${surat}), Aya ${ayat}:\\n\\nNassin Larabci: "${teksArab}"\\nFassarar Hausa: "${teksArti}"\\n\\nTare da mai da hankali kan ma'anar kalmar "${kata}": Wace hikima, asalin saukar aya (asbabun nuzul idan akwai), da koyarwar da wannan aya ke isarwa ga rayuwar muminai?`;
      } else {
        return `Da fatan a bayyana balagar Al-Ƙur'ani (I'jaz da adon magana) dangane da zaɓin kalmar "${kata}" a cikin Surah ${suratNama} (${surat}), Aya ${ayat}:\\n\\nNassin Larabci: "${teksArab}"\\nFassarar Hausa: "${teksArti}"\\n\\nMe ya sa aka yi amfani da wannan kalma ko damiri a nan? Wane zurfin ma'ana da kyawon lafazi take ƙarawa ga ayar?`;
      }"""

code = code.replace(
    "    } else if (state.lang === 'pt') {",
    ha_ai_prompt + "\n    } else if (state.lang === 'pt') {"
)

# 12. Update exportToCsv in app.js
code = code.replace(
    "const cleanArtiPT = (occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');",
    "const cleanArtiPT = (occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');\n        const cleanArtiHA = (occ.teksArtiHA || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');"
)

code = code.replace(
    ',\\"Significado (PT)\\",',
    ',\\"Significado (PT)\\",\\"Ma\'ana (HA)\\",'
)

code = code.replace(
    ',\\"Tradução (PT)\\",',
    ',\\"Tradução (PT)\\",\\"Fassara (HA)\\",'
)

code = code.replace(
    '"${group.arti_tr || \'\'}","${group.arti_pt || \'\'}","${group.frek || \'Muttashil\'}"',
    '"${group.arti_tr || \'\'}","${group.arti_pt || \'\'}","${group.arti_ha || \'\'}","${group.frek || \'Muttashil\'}"'
)

code = code.replace(
    '"${cleanArtiTR}","${cleanArtiPT}",',
    '"${cleanArtiTR}","${cleanArtiPT}","${cleanArtiHA}",'
)

# 13. Update btnCopyAll in app.js
code = code.replace(
    "} else if (state.lang === 'pt') {\n          activeArti = group.arti_pt || group.arti_id || group.arti;\n        }",
    "} else if (state.lang === 'pt') {\n          activeArti = group.arti_pt || group.arti_id || group.arti;\n        } else if (state.lang === 'ha') {\n          activeArti = group.arti_ha || group.arti_id || group.arti;\n        }"
)

code = code.replace(
    "} else if (state.lang === 'pt') {\n          activeDesc = grammar.desc_pt || grammar.desc_id || grammar.keterangan || '';\n        }",
    "} else if (state.lang === 'pt') {\n          activeDesc = grammar.desc_pt || grammar.desc_id || grammar.keterangan || '';\n        } else if (state.lang === 'ha') {\n          activeDesc = grammar.desc_ha || grammar.desc_id || grammar.keterangan || '';\n        }"
)

code = code.replace(
    "else if (state.lang === 'pt') titlePrefix = 'Pronome Relativo do Alcorão (Mawshul)';",
    "else if (state.lang === 'pt') titlePrefix = 'Pronome Relativo do Alcorão (Mawshul)';\n          else if (state.lang === 'ha') titlePrefix = 'Sunan Sadarwa na Al-Ƙur\\'ani (Mawshul)';"
)

code = code.replace(
    "else if (state.lang === 'pt') titlePrefix = 'Pronomes do Alcorão (Dhamir)';",
    "else if (state.lang === 'pt') titlePrefix = 'Pronomes do Alcorão (Dhamir)';\n          else if (state.lang === 'ha') titlePrefix = 'Wakilan Suna na Al-Ƙur\\'ani (Dhamir)';"
)

# 14. Update applyLanguage in app.js
code = code.replace(
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt'].includes(lang) ? lang : 'id';",
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha'].includes(lang) ? lang : 'id';"
)

if crlf:
    code = code.replace('\n', '\r\n')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("app.js successfully updated with Hausa support!")
