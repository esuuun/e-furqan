#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to fix applyLanguage, getDefaultJenis, updateHeaderTitles, and buildAiPrompt in app.js
for Bosnian (bs) and Albanian (sq).
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app_js_path = os.path.join(BASE_DIR, 'app.js')

with open(app_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix applyLanguage
old_apply = "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa', 'ja', 'ko', 'nl', 'it'].includes(lang) ? lang : 'id';"
new_apply = "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa', 'ja', 'ko', 'nl', 'it', 'bs', 'sq'].includes(lang) ? lang : 'id';"

if old_apply in content:
    content = content.replace(old_apply, new_apply)
    print("Fixed applyLanguage with bs and sq.")
else:
    print("applyLanguage check: not found or already updated.")

# 2. Fix getDefaultJenis
old_dhamir_jenis = "nl: 'Losstaand voornaamwoord (Munfashil)', it: 'Pronome isolato (Munfashil)'"
new_dhamir_jenis = "nl: 'Losstaand voornaamwoord (Munfashil)', it: 'Pronome isolato (Munfashil)', bs: 'Samostalna zamjenica (Munfashil)', sq: 'Përemër i veçuar (Munfashil)'"

old_mawshul_jenis = "nl: 'Betrekkelijk voornaamwoord (Mawshul)', it: 'Pronome relativo (Mawshul)'"
new_mawshul_jenis = "nl: 'Betrekkelijk voornaamwoord (Mawshul)', it: 'Pronome relativo (Mawshul)', bs: 'Odnosna zamjenica (Isim Mawshul)', sq: 'Përemër lidhor (Isim Mawshul)'"

old_istifham_jenis = "nl: 'Vragend woord (Istifham)', it: 'Interrogativo (Istifham)'"
new_istifham_jenis = "nl: 'Vragend woord (Istifham)', it: 'Interrogativo (Istifham)', bs: 'Upitna zamjenica (Isim Istifham)', sq: 'Përemër pyetës (Isim Istifham)'"

old_syarath_jenis = "nl: 'Voorwaardelijk woord (Syarath)', it: 'Condizionale (Syarath)'"
new_syarath_jenis = "nl: 'Voorwaardelijk woord (Syarath)', it: 'Condizionale (Syarath)', bs: 'Uslovna imenica (Isim Syarath)', sq: 'Emër kushtor (Isim Syarath)'"

old_isyarah_jenis = "nl: 'Aanwijzend voornaamwoord (Isyarah)', it: 'Dimostrativo (Isyarah)'"
new_isyarah_jenis = "nl: 'Aanwijzend voornaamwoord (Isyarah)', it: 'Dimostrativo (Isyarah)', bs: 'Pokazna zamjenica (Isim Isyarah)', sq: 'Përemër dëftor (Isim Isyarah)'"

old_isim_fiil_jenis = "nl: \"Verbale zelfstandig naamwoord (Isim Fi'il)\", it: \"Nome verbale (Isim Fi'il)\""
new_isim_fiil_jenis = "nl: \"Verbale zelfstandig naamwoord (Isim Fi'il)\", it: \"Nome verbale (Isim Fi'il)\", bs: \"Glagolska imenica (Isim Fi'il)\", sq: \"Emër foljor (Isim Fi'il)\""

old_fiil_jamid_jenis = "nl: \"Niet-vervoegbaar werkwoord (Fi'il Jamid)\", it: \"Verbo difettivo / inflessibile (Fi'il Jamid)\""
new_fiil_jamid_jenis = "nl: \"Niet-vervoegbaar werkwoord (Fi'il Jamid)\", it: \"Verbo difettivo / inflessibile (Fi'il Jamid)\", bs: \"Nemenjivi glagol (Fi'il Jamid)\", sq: \"Folje e ngurosur (Fi'il Jamid)\""

for old_j, new_j in [
    (old_dhamir_jenis, new_dhamir_jenis),
    (old_mawshul_jenis, new_mawshul_jenis),
    (old_istifham_jenis, new_istifham_jenis),
    (old_syarath_jenis, new_syarath_jenis),
    (old_isyarah_jenis, new_isyarah_jenis),
    (old_isim_fiil_jenis, new_isim_fiil_jenis),
    (old_fiil_jamid_jenis, new_fiil_jamid_jenis),
]:
    if old_j in content:
        content = content.replace(old_j, new_j)
        print("Updated jenis item in getDefaultJenis.")

# 3. Update updateHeaderTitles for Harf
old_header_titles = """      } else if (state.lang === 'it') {
        elements.brandTitle.innerHTML = "Dizionario di <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Dizionario Interattivo delle Particelle Inoperative del Corano";
        if (elements.docTitle) elements.docTitle.textContent = "Dizionario di Harf Ghair 'Amil | Riferimenti Coranici";
      } else if (state.lang === 'en') {"""

new_header_titles = """      } else if (state.lang === 'it') {
        elements.brandTitle.innerHTML = "Dizionario di <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Dizionario Interattivo delle Particelle Inoperative del Corano";
        if (elements.docTitle) elements.docTitle.textContent = "Dizionario di Harf Ghair 'Amil | Riferimenti Coranici";
      } else if (state.lang === 'bs') {
        elements.brandTitle.innerHTML = "Rječnik <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktivni rječnik za 17 oblika i 52 čestice u Kur'anu";
        if (elements.docTitle) elements.docTitle.textContent = "Rječnik Harf Ghair 'Amil | Kur'anske čestice";
      } else if (state.lang === 'sq') {
        elements.brandTitle.innerHTML = "Fjalori i <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Fjalor interaktiv për 17 forma dhe 52 pjesëza kur'anore";
        if (elements.docTitle) elements.docTitle.textContent = "Fjalori i Harf Ghair 'Amil | Pjesëzat kur'anore";
      } else if (state.lang === 'en') {"""

if old_header_titles in content:
    content = content.replace(old_header_titles, new_header_titles)
    print("Updated updateHeaderTitles with bs and sq.")

# 4. Add bs and sq to buildAiPrompt
old_ai_switch = """    switch (state.lang) {
      case 'fa':"""

new_ai_switch = """    switch (state.lang) {
      case 'bs':
        if (topic === 'nahwu') {
          return `Molimo navedite detaljnu gramatičku analizu (Nahv/Sarf) i I'rab za riječ "${kata}" (${noKata}, ${bentuk}) u suri ${suratNama} (${surat}), ajet ${ayat}:\\n\\nArapski tekst: "${teksArab}"\\nPrijevod na bosanski: "${teksArti}"\\n\\nMolimo obuhvatite sljedeće:\\n1. Sintaktičku ulogu (položaj u I'rabu) riječi "${kata}" u ovoj rečenici (Merfu'/Mensub/Medžrur).\\n2. Morfološku vrstu (Dhamir / Mawshul / itd.) i svojstva (Munfasil / Muttasil).\\n3. Gramatičko objašnjenje: ${grammarDesc || "U skladu s pravilima klasičnog arapskog jezika Kur'ana"}.`;
        } else if (topic === 'tafsir') {
          return `Molimo navedite sažet i poučan tefsir za suru ${suratNama} (${surat}), ajet ${ayat}:\\n\\nArapski tekst: "${teksArab}"\\nPrijevod na bosanski: "${teksArti}"\\n\\nS fokusom na riječ "${kata}": Koja je mudrost, povod objave (sebeb-i nuzul ako postoji) i poruke koje ovaj ajet nosi za život vjernika?`;
        } else {
          return `Molimo objasnite belagat (retoričku ljepotu i stilsku preciznost Kur'ana) u vezi s izborom riječi "${kata}" u suri ${suratNama} (${surat}), ajet ${ayat}:\\n\\nArapski tekst: "${teksArab}"\\nPrijevod na bosanski: "${teksArti}"\\n\\nZašto je baš ova riječ/zamjenica upotrijebljena u ovom kontekstu i koju dubinu značenja daje ovom ajetu?`;
        }

      case 'sq':
        if (topic === 'nahwu') {
          return `Ju lutemi jepni një analizë të hollësishme gramatikore arabe (Nahw/Sarf) dhe I'rab për fjalën "${kata}" (${noKata}, ${bentuk}) në suren ${suratNama} (${surat}), ajeti ${ayat}:\\n\\nTeksti Arabisht: "${teksArab}"\\nPërkthimi Shqip: "${teksArti}"\\n\\nJu lutemi përfshini pikat e mëposhtme:\\n1. Roli sintaktik (pozicioni në I'rab) i fjalës "${kata}" në këtë fjali (Marfu'/Manshub/Majrur).\\n2. Lloji morfologjik (Dhamir / Mawshul / etj.) dhe veçoritë (Munfashil / Muttashil).\\n3. Shënime gramatikore: ${grammarDesc || "Sipas rregullave klasike të gjuhës arabe kur'anore"}.`;
        } else if (topic === 'tafsir') {
          return `Ju lutemi jepni një tefsir të përmbledhur dhe domethënës për suren ${suratNama} (${surat}), ajeti ${ayat}:\\n\\nTeksti Arabisht: "${teksArab}"\\nPërkthimi Shqip: "${teksArti}"\\n\\nMe fokus te fjala "${kata}": Cila është urtësia, shkaku i zbritjes (asbabun nuzul nëse ka) dhe mësimet që ky ajet përcjell për besimtarët?`;
        } else {
          return `Ju lutemi shpjegoni balagën (bukurinë retorike dhe stilistike kur'anore) lidhur me zgjedhjen e fjalës "${kata}" në suren ${suratNama} (${surat}), ajeti ${ayat}:\\n\\nTeksti Arabisht: "${teksArab}"\\nPërkthimi Shqip: "${teksArti}"\\n\\nPërse u përdor pikërisht kjo fjalë/përemër në këtë kontekst dhe çfarë thellësie kuptimore i shton ajetit?`;
        }

      case 'fa':"""

if old_ai_switch in content:
    content = content.replace(old_ai_switch, new_ai_switch)
    print("Updated buildAiPrompt with bs and sq.")

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved app.js successfully.")
