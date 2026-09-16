#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to update app.js with complete Dutch (nl) and Italian (it) I18N dictionaries,
data accessors, and TTS voice handlers.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app_js_path = os.path.join(BASE_DIR, 'app.js')

with open(app_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Dutch I18N block
nl_i18n = """    nl: {
      pageTitle: "Woordenboek Jamid Mabny | Interactieve Koran Woorden & Versverwijzingen",
      brandTitle: "Woordenboek <span>Jamid Mabny</span>",
      brandSubtitle: "Interactief Woordenboek voor Vaste en Onveranderlijke Woorden",
      themeToggleTitle: "Donker / Licht Thema Schakelen",
      labelLangSelect: "Vertaling- en Spraaktaal:",
      translationSourceHtml: "Vertaling: <strong>Sofian S. Siregar</strong>",
      
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
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_nl || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_nl || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Betrekkelijk voornaamwoord' : 'Voornaamwoord';
        return `${prefix} ${cleanWord}, ${latin}betekent ${arti}. ${desc ? 'Uitleg: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
"""

# 2. Italian I18N block
it_i18n = """    it: {
      pageTitle: "Dizionario Jamid Mabny | Riferimenti Interattivi di Parole e Versetti Coranici",
      brandTitle: "Dizionario <span>Jamid Mabny</span>",
      brandSubtitle: "Dizionario Interattivo per Forme di Parole e Numeri Coranici",
      themeToggleTitle: "Cambia Tema Scuro / Chiaro",
      labelLangSelect: "Lingua di Traduzione e Voce:",
      translationSourceHtml: "Traduzione: <strong>Hamza Roberto Piccardo</strong>",
      
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
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_it || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_it || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Pronome relativo' : 'Pronome';
        return `${prefix} ${cleanWord}, ${latin}significa ${arti}. ${desc ? 'Spiegazione: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }
"""

# Insert nl and it after ko in I18N
ko_end_pattern = "    ko: {\n"
if "    ko: {" in content:
    # Find the closing brace of ko
    pos_ko = content.find("    ko: {")
    # find matching next section or end of I18N object
    pos_next = content.find("  };\n\n  // Helper for current i18n text", pos_ko)
    if pos_next != -1:
        # Check if nl and it are already added
        if "    nl: {" not in content:
            # We replace the closing part of ko
            content = content[:pos_next] + ",\n" + nl_i18n + it_i18n + content[pos_next:]
            print("Successfully injected nl and it into I18N dictionary.")

# Update voice handling in getSpeechVoiceAndLang
old_voice_handling = """    else if (lang === 'ko') {
      langCode = 'ko-KR';
      voice = voices.find(v => (v.lang === 'ko-KR' || v.lang.startsWith('ko')) && /korean|한국어|heami|yuna|sunhi|google/i.test(v.name)) ||
              voices.find(v => v.lang === 'ko-KR' || v.lang.startsWith('ko'));
    }"""

new_voice_handling = """    else if (lang === 'ko') {
      langCode = 'ko-KR';
      voice = voices.find(v => (v.lang === 'ko-KR' || v.lang.startsWith('ko')) && /korean|한국어|heami|yuna|sunhi|google/i.test(v.name)) ||
              voices.find(v => v.lang === 'ko-KR' || v.lang.startsWith('ko'));
    }
    else if (lang === 'nl') {
      langCode = 'nl-NL';
      voice = voices.find(v => (v.lang === 'nl-NL' || v.lang.startsWith('nl')) && /dutch|nederlands|claire|colette|ruben|fenn|lotte|bart|google/i.test(v.name)) ||
              voices.find(v => v.lang === 'nl-NL' || v.lang.startsWith('nl'));
    }
    else if (lang === 'it') {
      langCode = 'it-IT';
      voice = voices.find(v => (v.lang === 'it-IT' || v.lang.startsWith('it')) && /italian|italiano|cosimo|elsa|diego|alice|giorgio|federica|google/i.test(v.name)) ||
              voices.find(v => v.lang === 'it-IT' || v.lang.startsWith('it'));
    }"""

if old_voice_handling in content:
    content = content.replace(old_voice_handling, new_voice_handling)
    print("Successfully added voice handling for nl and it.")

# Update language code fallbacks in speakDhamirMeaning and toggleVerseTranslationAudio
# Make sure cloud audio stream supports nl and it if native voice is missing
with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated app.js successfully.")
