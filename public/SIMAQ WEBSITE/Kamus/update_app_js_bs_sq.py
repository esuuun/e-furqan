#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to update app.js with complete Bosnian (bs) and Albanian (sq) I18N dictionaries,
data accessors, TTS voice handlers, and CSV export.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app_js_path = os.path.join(BASE_DIR, 'app.js')

with open(app_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update state.lang validation list
old_lang_state = "lang: ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa', 'ja', 'ko', 'nl', 'it'].includes(localStorage.getItem('dhamir_lang')) ? localStorage.getItem('dhamir_lang') : 'id',"
new_lang_state = "lang: ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa', 'ja', 'ko', 'nl', 'it', 'bs', 'sq'].includes(localStorage.getItem('dhamir_lang')) ? localStorage.getItem('dhamir_lang') : 'id',"

if old_lang_state in content:
    content = content.replace(old_lang_state, new_lang_state)
    print("Updated state.lang with bs and sq.")

# 2. Bosnian & Albanian I18N blocks
bs_i18n = """    bs: {
      pageTitle: "Rječnik Jamid Mabny | Interaktivne kur'anske riječi i reference ajeta",
      brandTitle: "Rječnik <span>Jamid Mabny</span>",
      brandSubtitle: "Interaktivni rječnik za oblike i brojeve riječi u Kur'anu",
      themeToggleTitle: "Promijeni tamnu / svijetlu temu",
      labelLangSelect: "Jezik prijevoda i zvuka:",
      translationSourceHtml: "Prijevod: <strong>Besim Korkut</strong>",
      
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
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_bs || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_bs || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Odnosna zamjenica' : 'Zamjenica';
        return `${prefix} ${cleanWord}, ${latin}znači ${arti}. ${desc ? 'Objašnjenje: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },"""

sq_i18n = """    sq: {
      pageTitle: "Fjalori Jamid Mabny | Referencat Interaktive të Fjalëve dhe Ajeteve Kur'anore",
      brandTitle: "Fjalori <span>Jamid Mabny</span>",
      brandSubtitle: "Fjalor Interaktiv për Format dhe Numrat e Fjalëve Kur'anore",
      themeToggleTitle: "Ndrysho Temën e Errët / të Çelët",
      labelLangSelect: "Gjuha e Përkthimit dhe Zërit:",
      translationSourceHtml: "Përkthimi: <strong>Sherif Ahmeti</strong>",
      
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
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_sq || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_sq || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Përemër lidhor' : 'Përemër';
        return `${prefix} ${cleanWord}, ${latin}do të thotë ${arti}. ${desc ? 'Shpjegim: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }"""

# Inject bs and sq into I18N after it
if "    it: {" in content and "    bs: {" not in content:
    # Find the end of it block before `  };`
    it_marker = "      ttsVerseSpeech: (suratNama, ayat, text) => text\n    }\n  };"
    if it_marker in content:
        replacement = f"      ttsVerseSpeech: (suratNama, ayat, text) => text\n    }},\n{bs_i18n}\n{sq_i18n}\n  }};"
        content = content.replace(it_marker, replacement)
        print("Injected bs and sq into I18N.")
    else:
        # try find alternative matching
        pos_it = content.find("    it: {")
        pos_close = content.find("  };\n\n  // Helper for current i18n text", pos_it)
        if pos_close != -1:
            content = content[:pos_close] + ",\n" + bs_i18n + "\n" + sq_i18n + "\n" + content[pos_close:]
            print("Injected bs and sq into I18N (alternative position).")

# 3. Add bentuk_bs, bentuk_sq, arti_bs, arti_sq in initData
old_bentuk_block = """          bentuk_nl: item['BentukKataNL'] || b,
          bentuk_it: item['BentukKataIT'] || b,"""

new_bentuk_block = """          bentuk_nl: item['BentukKataNL'] || b,
          bentuk_it: item['BentukKataIT'] || b,
          bentuk_bs: item['BentukKataBS'] || b,
          bentuk_sq: item['BentukKataSQ'] || b,"""

if old_bentuk_block in content:
    content = content.replace(old_bentuk_block, new_bentuk_block)
    print("Updated bentuk_bs and bentuk_sq in initData.")

old_arti_block = """          arti_nl: item['ArtiKataNL'] || grammar.arti_nl || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_it: item['ArtiKataIT'] || grammar.arti_it || item['ArtiKataID'] || item['Arti kata'] || '',"""

new_arti_block = """          arti_nl: item['ArtiKataNL'] || grammar.arti_nl || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_it: item['ArtiKataIT'] || grammar.arti_it || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_bs: item['ArtiKataBS'] || grammar.arti_bs || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_sq: item['ArtiKataSQ'] || grammar.arti_sq || item['ArtiKataID'] || item['Arti kata'] || '',"""

if old_arti_block in content:
    content = content.replace(old_arti_block, new_arti_block)
    print("Updated arti_bs and arti_sq in initData.")

# 4. Add suratArtiBS, suratArtiSQ, teksArtiBS, teksArtiSQ in occurrences
old_surat_arti_block = """        suratArtiNL: item['SuratArtiNL'] || item['SuratArtiEN'] || '',
        suratArtiIT: item['SuratArtiIT'] || item['SuratArtiEN'] || '',"""

new_surat_arti_block = """        suratArtiNL: item['SuratArtiNL'] || item['SuratArtiEN'] || '',
        suratArtiIT: item['SuratArtiIT'] || item['SuratArtiEN'] || '',
        suratArtiBS: item['SuratArtiBS'] || item['SuratArtiEN'] || '',
        suratArtiSQ: item['SuratArtiSQ'] || item['SuratArtiEN'] || '',"""

if old_surat_arti_block in content:
    content = content.replace(old_surat_arti_block, new_surat_arti_block)
    print("Updated suratArtiBS and suratArtiSQ in occurrences.")

old_teks_arti_block = """        teksArtiNL: item['TeksArtiNL'] || item['TeksArti'] || '',
        teksArtiIT: item['TeksArtiIT'] || item['TeksArti'] || '',"""

new_teks_arti_block = """        teksArtiNL: item['TeksArtiNL'] || item['TeksArti'] || '',
        teksArtiIT: item['TeksArtiIT'] || item['TeksArti'] || '',
        teksArtiBS: item['TeksArtiBS'] || item['TeksArti'] || '',
        teksArtiSQ: item['TeksArtiSQ'] || item['TeksArti'] || '',"""

if old_teks_arti_block in content:
    content = content.replace(old_teks_arti_block, new_teks_arti_block)
    print("Updated teksArtiBS and teksArtiSQ in occurrences.")

# 5. Add voice handlers in getSpeechVoiceAndLang
old_voice_handling = """    else if (langKey === 'it') {
      speechLangCode = 'it-IT';
      matchVoice = voices.find(v => v.lang.startsWith('it'));
      hasNativeVoice = !!matchVoice;
    } else {"""

new_voice_handling = """    else if (langKey === 'it') {
      speechLangCode = 'it-IT';
      matchVoice = voices.find(v => v.lang.startsWith('it'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'bs') {
      speechLangCode = 'bs-BA';
      matchVoice = voices.find(v => v.lang.startsWith('bs') || v.lang.startsWith('hr') || v.lang.startsWith('sr'));
      hasNativeVoice = !!matchVoice;
    } else if (langKey === 'sq') {
      speechLangCode = 'sq-AL';
      matchVoice = voices.find(v => v.lang.startsWith('sq'));
      hasNativeVoice = !!matchVoice;
    } else {"""

if old_voice_handling in content:
    content = content.replace(old_voice_handling, new_voice_handling)
    print("Updated getSpeechVoiceAndLang with bs and sq.")

# 6. Update cloud voice fallback condition in speakDhamirMeaning and toggleVerseTranslationAudio
old_cloud_cond = "state.lang === 'tr' || state.lang === 'ha' || state.lang === 'sw' || state.lang === 'nl' || state.lang === 'it'"
new_cloud_cond = "state.lang === 'tr' || state.lang === 'ha' || state.lang === 'sw' || state.lang === 'nl' || state.lang === 'it' || state.lang === 'bs' || state.lang === 'sq'"

if old_cloud_cond in content:
    content = content.replace(old_cloud_cond, new_cloud_cond)
    print("Updated cloud fallback conditions with bs and sq.")

# 7. Update CSV export headers and rows
old_csv_headers = """      'Arti (ES)', 'Arti (TR)', 'Arti (PT)', 'Arti (HA)', 'Arti (SW)', 'Arti (FA)', 'Arti (JA)', 'Arti (KO)', 'Arti (NL)', 'Arti (IT)',
      'Frekuensi', 'Teks Arab', 'Teks Latin',
      'Terjemahan (ID)', 'Terjemahan (EN)', 'Terjemahan (MS)', 'Terjemahan (FR)', 'Terjemahan (DE)',
      'Terjemahan (UR)', 'Terjemahan (HI)', 'Terjemahan (BN)', 'Terjemahan (RU)', 'Terjemahan (ZH)',
      'Terjemahan (ES)', 'Terjemahan (TR)', 'Terjemahan (PT)', 'Terjemahan (HA)', 'Terjemahan (SW)', 'Terjemahan (FA)', 'Terjemahan (JA)', 'Terjemahan (KO)', 'Terjemahan (NL)', 'Terjemahan (IT)'"""

new_csv_headers = """      'Arti (ES)', 'Arti (TR)', 'Arti (PT)', 'Arti (HA)', 'Arti (SW)', 'Arti (FA)', 'Arti (JA)', 'Arti (KO)', 'Arti (NL)', 'Arti (IT)', 'Arti (BS)', 'Arti (SQ)',
      'Frekuensi', 'Teks Arab', 'Teks Latin',
      'Terjemahan (ID)', 'Terjemahan (EN)', 'Terjemahan (MS)', 'Terjemahan (FR)', 'Terjemahan (DE)',
      'Terjemahan (UR)', 'Terjemahan (HI)', 'Terjemahan (BN)', 'Terjemahan (RU)', 'Terjemahan (ZH)',
      'Terjemahan (ES)', 'Terjemahan (TR)', 'Terjemahan (PT)', 'Terjemahan (HA)', 'Terjemahan (SW)', 'Terjemahan (FA)', 'Terjemahan (JA)', 'Terjemahan (KO)', 'Terjemahan (NL)', 'Terjemahan (IT)', 'Terjemahan (BS)', 'Terjemahan (SQ)'"""

if old_csv_headers in content:
    content = content.replace(old_csv_headers, new_csv_headers)
    print("Updated CSV headers.")

old_csv_rows = """        cleanField(group.arti_nl),
        cleanField(group.arti_it),
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
        cleanField(occ.teksArtiIT)"""

new_csv_rows = """        cleanField(group.arti_nl),
        cleanField(group.arti_it),
        cleanField(group.arti_bs),
        cleanField(group.arti_sq),
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
        cleanField(occ.teksArtiSQ)"""

if old_csv_rows in content:
    content = content.replace(old_csv_rows, new_csv_rows)
    print("Updated CSV row fields.")

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated app.js.")
