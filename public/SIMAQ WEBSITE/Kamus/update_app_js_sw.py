#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add Swahili (sw) language support to app.js
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
    "['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha'].includes(localStorage.getItem('dhamir_lang'))",
    "['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw'].includes(localStorage.getItem('dhamir_lang'))"
)

# 2. Add I18N.sw dictionary
sw_dict = '''    sw: {
      pageTitle: "Kamusi ya Jamid Mabny | Kamusi na Marejeleo ya Aya za Qur'ani Tukufu",
      brandTitle: "Kamusi ya <span>Jamid Mabny</span>",
      brandSubtitle: "Kamusi Shirikishi ya Aina za Maneno na Nambari za Maneno",
      themeToggleTitle: "Badilisha Mandhari ya Mwangaza / Giza",
      labelLangSelect: "Lugha ya Tafsiri na Sauti:",
      translationSourceHtml: "Tafsiri: <strong>Sheikh Ali Muhsin Al-Barwani</strong>",
      
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
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_sw || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_sw || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Jina la kuunganisha' : 'Kiwakilishi cha nafsi';
        return `${prefix} ${cleanWord}, ${latin}maana yake ni ${arti}. ${desc ? 'Maelezo: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }'''

code = code.replace(
    '  };\n\n  // Helper for current i18n text',
    ',\n' + sw_dict + '\n  };\n\n  // Helper for current i18n text'
)

# 3. Update initData in app.js
code = code.replace(
    "bentuk_ha: item['BentukKataHA'] || (b === '1. Dhamir' ? '1. Wakilan Suna (Dhamir - Pronouns)' : (b === '2. Mawshul' ? '2. Sunayen Sadarwa (Mawshul - Relative Pronouns)' : b)),",
    "bentuk_ha: item['BentukKataHA'] || (b === '1. Dhamir' ? '1. Wakilan Suna (Dhamir - Pronouns)' : (b === '2. Mawshul' ? '2. Sunayen Sadarwa (Mawshul - Relative Pronouns)' : b)),\n          bentuk_sw: item['BentukKataSW'] || (b === '1. Dhamir' ? '1. Viwakilishi vya Nafsi (Dhamir - Pronouns)' : (b === '2. Mawshul' ? '2. Majina ya Kuunganisha (Mawshul - Relative Pronouns)' : b)),"
)

code = code.replace(
    "arti_ha: item['ArtiKataHA'] || grammar.arti_ha || item['ArtiKataID'] || item['Arti kata'],",
    "arti_ha: item['ArtiKataHA'] || grammar.arti_ha || item['ArtiKataID'] || item['Arti kata'],\n          arti_sw: item['ArtiKataSW'] || grammar.arti_sw || item['ArtiKataID'] || item['Arti kata'],"
)

code = code.replace(
    "suratArtiHA: item['SuratArtiHA'] || item['SuratArtiEN'] || item['SuratArti'] || '',",
    "suratArtiHA: item['SuratArtiHA'] || item['SuratArtiEN'] || item['SuratArti'] || '',\n        suratArtiSW: item['SuratArtiSW'] || item['SuratArtiEN'] || item['SuratArti'] || '',"
)

code = code.replace(
    "teksArtiHA: item['TeksArtiHA'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',",
    "teksArtiHA: item['TeksArtiHA'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',\n        teksArtiSW: item['TeksArtiSW'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',"
)

# 4. Update getDefaultJenis defaultMap
code = code.replace(
    "ha: 'Munfashil (Mai Zaman Kansa)'",
    "ha: 'Munfashil (Mai Zaman Kansa)', sw: 'Munfashil (Kiwakilishi Huru)'"
)
code = code.replace(
    "ha: 'Isim Mawshul (Sunan Sadarwa)'",
    "ha: 'Isim Mawshul (Sunan Sadarwa)', sw: 'Isim Mawshul (Jina la Kuunganisha)'"
)
code = code.replace(
    "ha: 'Kalmar Tambaya (Istifham)'",
    "ha: 'Kalmar Tambaya (Istifham)', sw: 'Isim Istifham (Neno la Kuulizia)'"
)
code = code.replace(
    "ha: 'Kalmar Sharaɗi (Syarath)'",
    "ha: 'Kalmar Sharaɗi (Syarath)', sw: 'Isim Syarat (Neno la Sharti)'"
)
code = code.replace(
    "ha: 'Sunan Nuni (Isyarah)'",
    "ha: 'Sunan Nuni (Isyarah)', sw: 'Isim Isyarah (Jina la Kuonyeshea)'"
)
code = code.replace(
    "ha: 'Sunan Aiki (Isim Fi\\'il)'",
    "ha: 'Sunan Aiki (Isim Fi\\'il)', sw: 'Isim Fi\\'il (Jina la Kitendo)'"
)
code = code.replace(
    "ha: 'Aiki Kafaffe (Fi\\'il Jamid)'",
    "ha: 'Aiki Kafaffe (Fi\\'il Jamid)', sw: 'Fi\\'il Jamid (Kitendo Kisichobadilika)'"
)

# 5. Update populateNoKata in app.js
code = code.replace(
    "} else if (state.lang === 'ha') {\n        localizedArti = group.arti_ha || group.arti_id || group.arti;\n      }",
    "} else if (state.lang === 'ha') {\n        localizedArti = group.arti_ha || group.arti_id || group.arti;\n      } else if (state.lang === 'sw') {\n        localizedArti = group.arti_sw || group.arti_id || group.arti;\n      }"
)

# 6. Update updateSpotlightCard in app.js
code = code.replace(
    "} else if (state.lang === 'ha') {\n      elements.badgeBentukKata.textContent = group.bentuk_ha || group.bentuk_id;\n    } else {",
    "} else if (state.lang === 'ha') {\n      elements.badgeBentukKata.textContent = group.bentuk_ha || group.bentuk_id;\n    } else if (state.lang === 'sw') {\n      elements.badgeBentukKata.textContent = group.bentuk_sw || group.bentuk_id;\n    } else {"
)

code = code.replace(
    "} else if (state.lang === 'ha') {\n      jenisText = grammar.jenis_ha || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'ha');\n    } else {",
    "} else if (state.lang === 'ha') {\n      jenisText = grammar.jenis_ha || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'ha');\n    } else if (state.lang === 'sw') {\n      jenisText = grammar.jenis_sw || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'sw');\n    } else {"
)

code = code.replace(
    "} else if (state.lang === 'ha') {\n      currentMeaning = group.arti_ha || group.arti_id || group.arti;\n    }",
    "} else if (state.lang === 'ha') {\n      currentMeaning = group.arti_ha || group.arti_id || group.arti;\n    } else if (state.lang === 'sw') {\n      currentMeaning = group.arti_sw || group.arti_id || group.arti;\n    }"
)

code = code.replace(
    "} else if (state.lang === 'ha') {\n      currentDesc = grammar.desc_ha || grammar.desc_id || grammar.keterangan || '';\n    }",
    "} else if (state.lang === 'ha') {\n      currentDesc = grammar.desc_ha || grammar.desc_id || grammar.keterangan || '';\n    } else if (state.lang === 'sw') {\n      currentDesc = grammar.desc_sw || grammar.desc_id || grammar.keterangan || '';\n    }"
)

# 7. Update renderAyatReferences (search filter and card rendering) in app.js
code = code.replace(
    "} else if (state.lang === 'ha') {\n          sArti = occ.suratArtiHA;\n          tArti = occ.teksArtiHA;\n        }",
    "} else if (state.lang === 'ha') {\n          sArti = occ.suratArtiHA;\n          tArti = occ.teksArtiHA;\n        } else if (state.lang === 'sw') {\n          sArti = occ.suratArtiSW;\n          tArti = occ.teksArtiSW;\n        }"
)

code = code.replace(
    "} else if (state.lang === 'ha') {\n      activeSuratArti = occ.suratArtiHA || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiHA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }",
    "} else if (state.lang === 'ha') {\n      activeSuratArti = occ.suratArtiHA || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiHA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    } else if (state.lang === 'sw') {\n      activeSuratArti = occ.suratArtiSW || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiSW || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }"
)

# 8. Update toggleVerseTranslationAudio in app.js
code = code.replace(
    "} else if (state.lang === 'ha') {\n      currentText = occ.teksArtiHA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }",
    "} else if (state.lang === 'ha') {\n      currentText = occ.teksArtiHA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    } else if (state.lang === 'sw') {\n      currentText = occ.teksArtiSW || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }"
)

# 9. Update getSpeechVoiceAndLang in app.js
code = code.replace(
    "} else if (langKey === 'ha') {\n      speechLangCode = 'ha-NG';\n      matchVoice = voices.find(v => v.lang.startsWith('ha') || v.lang.includes('ha-') || v.name.toLowerCase().includes('hausa')) || voices.find(v => v.lang.startsWith('ha'));",
    "} else if (langKey === 'ha') {\n      speechLangCode = 'ha-NG';\n      matchVoice = voices.find(v => v.lang.startsWith('ha') || v.lang.includes('ha-') || v.name.toLowerCase().includes('hausa')) || voices.find(v => v.lang.startsWith('ha'));\n    } else if (langKey === 'sw') {\n      speechLangCode = 'sw-TZ';\n      matchVoice = voices.find(v => v.lang.startsWith('sw') || v.lang.includes('sw-') || v.name.toLowerCase().includes('swahili') || v.name.toLowerCase().includes('kiswahili')) || voices.find(v => v.lang.startsWith('sw'));"
)

# 10. Update speakDhamirMeaning in app.js
code = code.replace(
    "} else if (state.lang === 'ha') {\n      activeMeaning = group.arti_ha || group.arti_id || group.arti;\n    }",
    "} else if (state.lang === 'ha') {\n      activeMeaning = group.arti_ha || group.arti_id || group.arti;\n    } else if (state.lang === 'sw') {\n      activeMeaning = group.arti_sw || group.arti_id || group.arti;\n    }"
)

# 11. Update openAiModal & buildAiPrompt in app.js
code = code.replace(
    "} else if (state.lang === 'ha') {\n        activeArti = occ.teksArtiHA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }",
    "} else if (state.lang === 'ha') {\n        activeArti = occ.teksArtiHA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      } else if (state.lang === 'sw') {\n        activeArti = occ.teksArtiSW || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }"
)

code = code.replace(
    "} else if (state.lang === 'ha') {\n      teksArti = occ.teksArtiHA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_ha || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    }",
    "} else if (state.lang === 'ha') {\n      teksArti = occ.teksArtiHA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_ha || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    } else if (state.lang === 'sw') {\n      teksArti = occ.teksArtiSW || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_sw || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    }"
)

sw_ai_prompt = """    } else if (state.lang === 'sw') {
      if (topic === 'nahwu') {
        return `Tafadhali fafanua kanuni za nahau (Nahwu/Sarf) na I'rabu kuhusu neno "${kata}" (${noKata}, ${bentuk}) katika Sura ${suratNama} (${surat}), Aya ${ayat}:\\n\\nMaandishi ya Kiarabu: "${teksArab}"\\nTafsiri ya Kiswahili: "${teksArti}"\\n\\nTafadhali chambua vipengele vifuatavyo:\\n1. Nafasi ya i'rabu na kazi ya "${kata}" katika sentensi hii (Marfu' / Manshub / Majrur).\\n2. Aina ya neno (Dhamir / Mawshul / nk.) na sifa zake (Munfashil / Muttashil).\\n3. Maelezo ya ziada ya kisarufi: ${grammarDesc || "Kulingana na kanuni za lugha ya Qur'ani"}.`;
      } else if (topic === 'tafsir') {
        return `Tafadhali toa muhtasari wa tafsiri yenye manufaa kuhusu Sura ${suratNama} (${surat}), Aya ${ayat}:\\n\\nMaandishi ya Kiarabu: "${teksArab}"\\nTafsiri ya Kiswahili: "${teksArti}"\\n\\nUkiwa na msisitizo maalum juu ya neno "${kata}": Je, kuna hekima gani, sababu ya kuteremka aya (asbabun nuzul ikiwa ipo), na mafunzo gani ambayo aya hii inatoa kwa maisha ya waumini?`;
      } else {
        return `Tafadhali fafanua uzuri wa lugha na balagha ya Qur'ani (I'jaz na ufasaha wa maneno) kuhusiana na uteuzi wa neno "${kata}" katika Sura ${suratNama} (${surat}), Aya ${ayat}:\\n\\nMaandishi ya Kiarabu: "${teksArab}"\\nTafsiri ya Kiswahili: "${teksArti}"\\n\\nKwa nini neno hili au kiwakilishi hiki kilitumika hapa? Je, kinaongeza kina gani cha maana na uzuri wa usemi katika muktadha wa aya hii?`;
      }"""

code = code.replace(
    "    } else if (state.lang === 'ha') {",
    sw_ai_prompt + "\n    } else if (state.lang === 'ha') {"
)

# 12. Update exportToCsv in app.js
code = code.replace(
    "const cleanArtiHA = (occ.teksArtiHA || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');",
    "const cleanArtiHA = (occ.teksArtiHA || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');\n        const cleanArtiSW = (occ.teksArtiSW || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');"
)

code = code.replace(
    ',\\"Ma\'ana (HA)\\",',
    ',\\"Ma\'ana (HA)\\",\\"Maana (SW)\\",'
)

code = code.replace(
    ',\\"Fassara (HA)\\",',
    ',\\"Fassara (HA)\\",\\"Tafsiri (SW)\\",'
)

code = code.replace(
    '"${group.arti_pt || \'\'}","${group.arti_ha || \'\'}","${group.frek || \'Muttashil\'}"',
    '"${group.arti_pt || \'\'}","${group.arti_ha || \'\'}","${group.arti_sw || \'\'}","${group.frek || \'Muttashil\'}"'
)

code = code.replace(
    '"${cleanArtiPT}","${cleanArtiHA}",',
    '"${cleanArtiPT}","${cleanArtiHA}","${cleanArtiSW}",'
)

# 13. Update btnCopyAll in app.js
code = code.replace(
    "} else if (state.lang === 'ha') {\n          activeArti = group.arti_ha || group.arti_id || group.arti;\n        }",
    "} else if (state.lang === 'ha') {\n          activeArti = group.arti_ha || group.arti_id || group.arti;\n        } else if (state.lang === 'sw') {\n          activeArti = group.arti_sw || group.arti_id || group.arti;\n        }"
)

code = code.replace(
    "} else if (state.lang === 'ha') {\n          activeDesc = grammar.desc_ha || grammar.desc_id || grammar.keterangan || '';\n        }",
    "} else if (state.lang === 'ha') {\n          activeDesc = grammar.desc_ha || grammar.desc_id || grammar.keterangan || '';\n        } else if (state.lang === 'sw') {\n          activeDesc = grammar.desc_sw || grammar.desc_id || grammar.keterangan || '';\n        }"
)

code = code.replace(
    "else if (state.lang === 'ha') titlePrefix = 'Sunan Sadarwa na Al-Ƙur\\'ani (Mawshul)';",
    "else if (state.lang === 'ha') titlePrefix = 'Sunan Sadarwa na Al-Ƙur\\'ani (Mawshul)';\n          else if (state.lang === 'sw') titlePrefix = 'Majina ya Kuunganisha ya Qur\\'ani (Mawshul)';"
)

code = code.replace(
    "else if (state.lang === 'ha') titlePrefix = 'Wakilan Suna na Al-Ƙur\\'ani (Dhamir)';",
    "else if (state.lang === 'ha') titlePrefix = 'Wakilan Suna na Al-Ƙur\\'ani (Dhamir)';\n          else if (state.lang === 'sw') titlePrefix = 'Viwakilishi vya Nafsi vya Qur\\'ani (Dhamir)';"
)

# 14. Update applyLanguage in app.js
code = code.replace(
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha'].includes(lang) ? lang : 'id';",
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw'].includes(lang) ? lang : 'id';"
)

if crlf:
    code = code.replace('\n', '\r\n')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("app.js successfully updated with Swahili support!")
