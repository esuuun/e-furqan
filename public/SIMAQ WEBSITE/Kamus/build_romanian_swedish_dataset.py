#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Romanian (ro) and Swedish (sv) Dataset Metadata & Enricher:
- 114 Surah Names for Romanian & Swedish
- 7 Bentuk Kata Categories for Romanian & Swedish
- 76 Jamid Mabny Grammar details for Romanian & Swedish
- 17 Bentuk Harf Categories for Romanian & Swedish
- 52 Harf Grammar details for Romanian & Swedish
"""

import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ROMANIAN_SURAHS = {
    "1": "Al-Fatiha (Deschizătoarea)",
    "2": "Al-Baqarah (Vaca)",
    "3": "Al-'Imran (Familia lui 'Imran)",
    "4": "An-Nisa' (Femeile)",
    "5": "Al-Ma'idah (Masa)",
    "6": "Al-An'am (Vitele)",
    "7": "Al-A'raf (Înălțimile)",
    "8": "Al-Anfal (Prăzile de război)",
    "9": "At-Tawbah (Căința)",
    "10": "Yunus (Iona)",
    "11": "Hud (Hud)",
    "12": "Yusuf (Iosif)",
    "13": "Ar-Ra'd (Tunetul)",
    "14": "Ibrahim (Avraam)",
    "15": "Al-Hijr (Stânca)",
    "16": "An-Nahl (Albinele)",
    "17": "Al-Isra' (Călătoria de noapte)",
    "18": "Al-Kahf (Peștera)",
    "19": "Maryam (Maria)",
    "20": "Ta-Ha (Ta-Ha)",
    "21": "Al-Anbiya' (Profeții)",
    "22": "Al-Hajj (Pelerinajul)",
    "23": "Al-Mu'minun (Credincioșii)",
    "24": "An-Nur (Lumina)",
    "25": "Al-Furqan (Îndreptarul)",
    "26": "Ash-Shu'ara' (Poeții)",
    "27": "An-Naml (Furnicile)",
    "28": "Al-Qasas (Istorisirea)",
    "29": "Al-'Ankabut (Păianjenul)",
    "30": "Ar-Rum (Bizantinii)",
    "31": "Luqman (Luqman)",
    "32": "As-Sajdah (Prosternarea)",
    "33": "Al-Ahzab (Aliații)",
    "34": "Saba' (Saba)",
    "35": "Fatir (Creatorul)",
    "36": "Ya-Sin (Ya-Sin)",
    "37": "As-Saffat (Cei așezați în rânduri)",
    "38": "Sad (Sad)",
    "39": "Az-Zumar (Cetele)",
    "40": "Ghafir (Iertătorul)",
    "41": "Fussilat (Deslușite)",
    "42": "Ash-Shura (Sfatul)",
    "43": "Az-Zukhruf (Podoabele de aur)",
    "44": "Ad-Dukhan (Fumul)",
    "45": "Al-Jathiyah (Cea îngenuncheată)",
    "46": "Al-Ahqaf (Dunele)",
    "47": "Muhammad (Muhammad)",
    "48": "Al-Fath (Biruința)",
    "49": "Al-Hujurat (Încăperile)",
    "50": "Qaf (Qaf)",
    "51": "Adh-Dhariyat (Cele ce spulberă)",
    "52": "At-Tur (Muntele)",
    "53": "An-Najm (Steaua)",
    "54": "Al-Qamar (Luna)",
    "55": "Ar-Rahman (Milostivul)",
    "56": "Al-Waqi'ah (Cea care trebuie să vină)",
    "57": "Al-Hadid (Fierul)",
    "58": "Al-Mujadilah (Cea care se ceartă)",
    "59": "Al-Hashr (Adunarea)",
    "60": "Al-Mumtahanah (Cea încercată)",
    "61": "As-Saff (Rândul)",
    "62": "Al-Jumu'ah (Vinerea)",
    "63": "Al-Munafiqun (Fățarnicii)",
    "64": "At-Taghabun (Păgubirea reciprocă)",
    "65": "At-Talaq (Divorțul)",
    "66": "At-Tahrim (Oprirea)",
    "67": "Al-Mulk (Împărăția)",
    "68": "Al-Qalam (Condeiul)",
    "69": "Al-Haqqah (Cea adevărată)",
    "70": "Al-Ma'arij (Treptele)",
    "71": "Nuh (Noe)",
    "72": "Al-Jinn (Genii)",
    "73": "Al-Muzzammil (Cel înveșmântat)",
    "74": "Al-Muddaththir (Cel acoperit cu mantia)",
    "75": "Al-Qiyamah (Învierea)",
    "76": "Al-Insan (Omul)",
    "77": "Al-Mursalat (Cele trimise)",
    "78": "An-Naba' (Vestea)",
    "79": "An-Nazi'at (Cele ce smulg)",
    "80": "'Abasa (S-a încruntat)",
    "81": "At-Takwir (Întunecarea)",
    "82": "Al-Infitar (Despicarea)",
    "83": "Al-Mutaffifin (Cei care înșală la cântar)",
    "84": "Al-Inshiqaq (Crăparea)",
    "85": "Al-Buruj (Constelațiile)",
    "86": "At-Tariq (Steaua de noapte)",
    "87": "Al-A'la (Cel Preaînalt)",
    "88": "Al-Ghashiyah (Copleșitoarea)",
    "89": "Al-Fajr (Zorile)",
    "90": "Al-Balad (Cetatea)",
    "91": "Ash-Shams (Soarele)",
    "92": "Al-Layl (Noaptea)",
    "93": "Ad-Duha (Dimineața)",
    "94": "Ash-Sharh (Deschiderea)",
    "95": "At-Tin (Smochinul)",
    "96": "Al-'Alaq (Cheagul de sânge)",
    "97": "Al-Qadr (Destinul)",
    "98": "Al-Bayyinah (Dovada vădită)",
    "99": "Az-Zalzalah (Cutremurul)",
    "100": "Al-'Adiyat (Cele ce aleargă)",
    "101": "Al-Qari'ah (Marea Lovitură)",
    "102": "At-Takathur (Goana după înmulțire)",
    "103": "Al-'Asr (Timpul)",
    "104": "Al-Humazah (Clevetitorul)",
    "105": "Al-Fil (Elefantul)",
    "106": "Quraysh (Quraysh)",
    "107": "Al-Ma'un (Ajutorul)",
    "108": "Al-Kawthar (Abundența)",
    "109": "Al-Kafirun (Necredincioșii)",
    "110": "An-Nasr (Ajutorul)",
    "111": "Al-Masad (Fibrele de palmier)",
    "112": "Al-Ikhlas (Curăția credinței)",
    "113": "Al-Falaq (Revărsatul zorilor)",
    "114": "An-Nas (Oamenii)"
}

SWEDISH_SURAHS = {
    "1": "Al-Fatiha (Öppningen)",
    "2": "Al-Baqarah (Kon)",
    "3": "Al-Imran (Imrans ätt)",
    "4": "An-Nisa (Kvinnorna)",
    "5": "Al-Ma'idah (Den himmelska måltiden)",
    "6": "Al-An'am (Boskap)",
    "7": "Al-A'raf (Urskiljning)",
    "8": "Al-Anfal (Krigsbytet)",
    "9": "At-Tawbah (Ångern)",
    "10": "Yunus (Jona)",
    "11": "Hud (Hud)",
    "12": "Yusuf (Josef)",
    "13": "Ar-Ra'd (Åskan)",
    "14": "Ibrahim (Abraham)",
    "15": "Al-Hijr (Stenlandet)",
    "16": "An-Nahl (Bina)",
    "17": "Al-Isra (Den nattliga resan)",
    "18": "Al-Kahf (Grottan)",
    "19": "Maryam (Maria)",
    "20": "Ta-Ha (Ta-Ha)",
    "21": "Al-Anbiya (Profeterna)",
    "22": "Al-Hajj (Vallfärden)",
    "23": "Al-Mu'minun (De troende)",
    "24": "An-Nur (Ljuset)",
    "25": "Al-Furqan (Måttstocken)",
    "26": "Ash-Shu'ara (Skalderna)",
    "27": "An-Naml (Myrorna)",
    "28": "Al-Qasas (Berättelsen)",
    "29": "Al-Ankabut (Spindeln)",
    "30": "Ar-Rum (Bysantinerna)",
    "31": "Luqman (Luqman)",
    "32": "As-Sajdah (Nedfallandet i bön)",
    "33": "Al-Ahzab (De sammansvurna)",
    "34": "Saba (Saba)",
    "35": "Fatir (Himlens och jordens Skapare)",
    "36": "Ya-Sin (Ya-Sin)",
    "37": "As-Saffat (I slutna led)",
    "38": "Sad (Sad)",
    "39": "Az-Zumar (Skarorna)",
    "40": "Ghafir (Han som förlåter)",
    "41": "Fussilat (En fast och klar förkunnelse)",
    "42": "Ash-Shura (Samråd)",
    "43": "Az-Zukhruf (Guld och glitter)",
    "44": "Ad-Dukhan (Röken)",
    "45": "Al-Jathiyah (På knä)",
    "46": "Al-Ahqaf (Sanddynerna)",
    "47": "Muhammad (Muhammad)",
    "48": "Al-Fath (Segern)",
    "49": "Al-Hujurat (De inre rummen)",
    "50": "Qaf (Qaf)",
    "51": "Adh-Dhariyat (De som virvlar upp)",
    "52": "At-Tur (Berget)",
    "53": "An-Najm (Stjärnan)",
    "54": "Al-Qamar (Månen)",
    "55": "Ar-Rahman (Den Nåderike)",
    "56": "Al-Waqi'ah (Det som måste komma)",
    "57": "Al-Hadid (Järnet)",
    "58": "Al-Mujadilah (Hon som vädjar)",
    "59": "Al-Hashr (Mönstringen)",
    "60": "Al-Mumtahanah (Den som prövas)",
    "61": "As-Saff (I sluten ordning)",
    "62": "Al-Jumu'ah (Fredagsbönen)",
    "63": "Al-Munafiqun (Hycklarna)",
    "64": "At-Taghabun (Förlust och vinning)",
    "65": "At-Talaq (Skilsmässa)",
    "66": "At-Tahrim (Förbudet)",
    "67": "Al-Mulk (Herraväldet)",
    "68": "Al-Qalam (Pennan)",
    "69": "Al-Haqqah (Sanningens stund)",
    "70": "Al-Ma'arij (Vägarna uppåt)",
    "71": "Nuh (Noa)",
    "72": "Al-Jinn (De osynliga väsendena)",
    "73": "Al-Muzzammil (Du som täcker över dig)",
    "74": "Al-Muddaththir (Du som sveper in dig)",
    "75": "Al-Qiyamah (Uppståndelsens dag)",
    "76": "Al-Insan (Människan)",
    "77": "Al-Mursalat (De som sänds ut)",
    "78": "An-Naba (Budskapet)",
    "79": "An-Nazi'at (De som rycker upp)",
    "80": "Abasa (Han rynkade pannan)",
    "81": "At-Takwir (När solen lindas in)",
    "82": "Al-Infitar (När himlen brister)",
    "83": "Al-Mutaffifin (De som snålar)",
    "84": "Al-Inshiqaq (När himlen rämnar)",
    "85": "Al-Buruj (Stjärnbilderna)",
    "86": "At-Tariq (Nattens gäst)",
    "87": "Al-A'la (Den Högste)",
    "88": "Al-Ghashiyah (Det som överskuggar allt)",
    "89": "Al-Fajr (Gryningen)",
    "90": "Al-Balad (Staden)",
    "91": "Ash-Shams (Solen)",
    "92": "Al-Layl (Natten)",
    "93": "Ad-Duha (Morgonljuset)",
    "94": "Ash-Sharh (Har Vi inte öppnat ditt bröst)",
    "95": "At-Tin (Fikonträdet)",
    "96": "Al-Alaq (Grodden)",
    "97": "Al-Qadr (Allmaktens natt)",
    "98": "Al-Bayyinah (Det klara vittnesbördet)",
    "99": "Az-Zalzalah (Jordbävningen)",
    "100": "Al-Adiyat (De stormande)",
    "101": "Al-Qari'ah (Det dundrande slaget)",
    "102": "At-Takathur (Rikedomens lockelser)",
    "103": "Al-Asr (Eftermiddagstimmarna)",
    "104": "Al-Humazah (Baktalaren)",
    "105": "Al-Fil (Elefanten)",
    "106": "Quraysh (Quraysh)",
    "107": "Al-Ma'un (Den minsta hjälp)",
    "108": "Al-Kawthar (Det goda i överflöd)",
    "109": "Al-Kafirun (Sanningens förnekare)",
    "110": "An-Nasr (Guds hjälp)",
    "111": "Al-Masad (Det tvinnade repet)",
    "112": "Al-Ikhlas (Den rena tron)",
    "113": "Al-Falaq (Gryningens ljus)",
    "114": "An-Nas (Människorna)"
}

BENTUK_KATA_RO = {
    "1. Dhamir": "1. Pronume (Dhamir / Pronume)",
    "2. Isim Mawshul": "2. Pronume relative (Ism Mawshul)",
    "3. Isim Istifham": "3. Pronume interogative (Ism Istifham)",
    "4. Isim Syarath": "4. Cuvinte condiționale (Ism Syarath)",
    "5. Isim Isyarah": "5. Pronume demonstrative (Ism Isyarah)",
    "6. Isim Fi'il": "6. Substantive verbale (Ism Fi'il)",
    "7. Fi'il Jamid": "7. Verbe invariabile (Fi'il Jamid)"
}

BENTUK_KATA_SV = {
    "1. Dhamir": "1. Pronomen (Dhamir / Pronomen)",
    "2. Isim Mawshul": "2. Relativa pronomen (Ism Mawshul)",
    "3. Isim Istifham": "3. Frågande pronomen (Ism Istifham)",
    "4. Isim Syarath": "4. Villkorsord (Ism Syarath)",
    "5. Isim Isyarah": "5. Påpekande pronomen (Ism Isyarah)",
    "6. Isim Fi'il": "6. Verbalsubstantiv (Ism Fi'il)",
    "7. Fi'il Jamid": "7. Oböjliga verb (Fi'il Jamid)"
}

BENTUK_HARF_RO = {
    "1. Harf Nafyi": "1. Particule de negație (Harf Nafyi)",
    "2. Harf Tahqiq Taswif": "2. Particule de confirmare și viitor (Tahqiq & Taswif)",
    "3. Harf Syarat": "3. Particule condiționale (Harf Syarat)",
    "4. Harf Mashdariyah": "4. Particule infinitivale (Harf Mashdariyah)",
    "5. Harf Zaidah": "5. Particule suplimentare de întărire (Harf Zaidah)",
    "6. Harf Istifham": "6. Particule interogative (Harf Istifham)",
    "7. Harf Istitsna": "7. Particule de excepție (Harf Istitsna)",
    "8. Harf Rad'in Wazajrin": "8. Particule de respingere și dojană (Harf Rad'in)",
    "9. Harf Rad'in Tahdid": "9. Particule de îndemn și mustrare (Harf Tahdid)",
    "10. Harf Ijab": "10. Particule afirmative de răspuns (Harf Ijab)",
    "11. Harf Tafsir": "11. Particule explicative (Harf Tafsir)",
    "12. Harf Tanbih": "12. Particule de atenționare (Harf Tanbih)",
    "13. Harf Ta'lil": "13. Particule cauzale (Harf Ta'lil)",
    "14. Harf Fuja'iyyah": "14. Particule de surpriză (Harf Fuja'iyyah)",
    "15. Harf Istidrak": "15. Particule adversative și de corectare (Harf Istidrak)",
    "16. Harf Ta'ajjub": "16. Particule de admirație (Harf Ta'ajjub)",
    "17. Harf Mabany": "17. Litere introductive ale surelor (Muqatta'at)"
}

BENTUK_HARF_SV = {
    "1. Harf Nafyi": "1. Nekande partiklar (Harf Nafyi)",
    "2. Harf Tahqiq Taswif": "2. Bekräftelse- och framtidspartiklar (Tahqiq & Taswif)",
    "3. Harf Syarat": "3. Villkorliga partiklar (Harf Syarat)",
    "4. Harf Mashdariyah": "4. Infinitivpartiklar (Harf Mashdariyah)",
    "5. Harf Zaidah": "5. Förstärkande tilläggspartiklar (Harf Zaidah)",
    "6. Harf Istifham": "6. Frågepartiklar (Harf Istifham)",
    "7. Harf Istitsna": "7. Undantagspartiklar (Harf Istitsna)",
    "8. Harf Rad'in Wazajrin": "8. Avvisnings- och tillrättavisningspartiklar (Harf Rad'in)",
    "9. Harf Rad'in Tahdid": "9. Uppmaningspartiklar (Harf Tahdid)",
    "10. Harf Ijab": "10. Svars- och bekräftelsepartiklar (Harf Ijab)",
    "11. Harf Tafsir": "11. Förklarande partiklar (Harf Tafsir)",
    "12. Harf Tanbih": "12. Uppmärksamhetspartiklar (Harf Tanbih)",
    "13. Harf Ta'lil": "13. Orsakspartiklar (Harf Ta'lil)",
    "14. Harf Fuja'iyyah": "14. Överraskningspartiklar (Harf Fuja'iyyah)",
    "15. Harf Istidrak": "15. Rättelse- och motsatspartiklar (Harf Istidrak)",
    "16. Harf Ta'ajjub": "16. Beundringspartiklar (Harf Ta'ajjub)",
    "17. Harf Mabany": "17. Inledande bokstäver i suror (Muqatta'at)"
}

ROMANIAN_GRAMMAR = {
    "1. Dhamir__1a": {"arti_ro": "El (Pers. a 3-a sg. masc.)", "desc_ro": "Pronume personal independent pers. a 3-a sg. masc. (Munfasil)", "jenis_ro": "Pronume personal independent"},
    "1. Dhamir__1b": {"arti_ro": "Lui / Îl / -l (Pronume alipit)", "desc_ro": "Pronume personal alipit pers. a 3-a sg. masc. (Muttasil)", "jenis_ro": "Pronume personal alipit"},
    "1. Dhamir__1c": {"arti_ro": "Numai pe El (Acuzativ)", "desc_ro": "Pronume acuzatival independent pers. a 3-a sg.", "jenis_ro": "Pronume acuzatival"},
    "1. Dhamir__2a": {"arti_ro": "Ei doi (Dual)", "desc_ro": "Pronume personal independent pentru dual", "jenis_ro": "Pronume dual"},
    "1. Dhamir__2b": {"arti_ro": "Lor doi (Alipit)", "desc_ro": "Pronume personal alipit pentru dual", "jenis_ro": "Pronume dual alipit"},
    "1. Dhamir__3a": {"arti_ro": "Ei (Plural masc.)", "desc_ro": "Pronume personal independent pers. a 3-a pl. masc.", "jenis_ro": "Pronume personal independent"},
    "1. Dhamir__3b": {"arti_ro": "Lor / Îi / -i (Alipit)", "desc_ro": "Pronume personal alipit pers. a 3-a pl. masc.", "jenis_ro": "Pronume personal alipit"},
    "1. Dhamir__3c": {"arti_ro": "Numai lor", "desc_ro": "Pronume acuzatival independent pers. a 3-a pl. masc.", "jenis_ro": "Pronume acuzatival"},
    "1. Dhamir__4a": {"arti_ro": "Ea (Pers. a 3-a sg. fem.)", "desc_ro": "Pronume personal independent pers. a 3-a sg. fem.", "jenis_ro": "Pronume personal independent"},
    "1. Dhamir__4b": {"arti_ro": "Ei / O (Alipit)", "desc_ro": "Pronume personal alipit pers. a 3-a sg. fem.", "jenis_ro": "Pronume personal alipit"},
    "1. Dhamir__5a": {"arti_ro": "Ele (Plural fem.)", "desc_ro": "Pronume personal independent pers. a 3-a pl. fem.", "jenis_ro": "Pronume personal independent"},
    "1. Dhamir__5b": {"arti_ro": "Lor (Feminin alipit)", "desc_ro": "Pronume personal alipit pers. a 3-a pl. fem.", "jenis_ro": "Pronume personal alipit"},
    "1. Dhamir__6a": {"arti_ro": "Tu (Pers. a 2-a sg. masc.)", "desc_ro": "Pronume personal independent pers. a 2-a sg. masc.", "jenis_ro": "Pronume personal independent"},
    "1. Dhamir__6b": {"arti_ro": "Tău / Ție / Te (Alipit)", "desc_ro": "Pronume personal alipit pers. a 2-a sg. masc.", "jenis_ro": "Pronume personal alipit"},
    "1. Dhamir__6c": {"arti_ro": "Numai pe Tine (Închinare exclusivă)", "desc_ro": "Pronume acuzatival independent pers. a 2-a sg.", "jenis_ro": "Pronume acuzatival"},
    "1. Dhamir__7a": {"arti_ro": "Voi doi", "desc_ro": "Pronume personal independent pers. a 2-a dual", "jenis_ro": "Pronume dual"},
    "1. Dhamir__7b": {"arti_ro": "Vouă doi (Alipit)", "desc_ro": "Pronume personal alipit pers. a 2-a dual", "jenis_ro": "Pronume dual alipit"},
    "1. Dhamir__8a": {"arti_ro": "Voi (Plural masc.)", "desc_ro": "Pronume personal independent pers. a 2-a pl. masc.", "jenis_ro": "Pronume personal independent"},
    "1. Dhamir__8b": {"arti_ro": "Vostru / Vouă / Vă (Alipit)", "desc_ro": "Pronume personal alipit pers. a 2-a pl. masc.", "jenis_ro": "Pronume personal alipit"},
    "1. Dhamir__8c": {"arti_ro": "Numai vouă", "desc_ro": "Pronume acuzatival independent pers. a 2-a pl. masc.", "jenis_ro": "Pronume acuzatival"},
    "1. Dhamir__9a": {"arti_ro": "Tu (Pers. a 2-a sg. fem.)", "desc_ro": "Pronume personal independent pers. a 2-a sg. fem.", "jenis_ro": "Pronume personal independent"},
    "1. Dhamir__9b": {"arti_ro": "Tău / Ție (Feminin alipit)", "desc_ro": "Pronume personal alipit pers. a 2-a sg. fem.", "jenis_ro": "Pronume personal alipit"},
    "1. Dhamir__10a": {"arti_ro": "Voi (Plural fem.)", "desc_ro": "Pronume personal independent pers. a 2-a pl. fem.", "jenis_ro": "Pronume personal independent"},
    "1. Dhamir__10b": {"arti_ro": "Vostru (Feminin alipit)", "desc_ro": "Pronume personal alipit pers. a 2-a pl. fem.", "jenis_ro": "Pronume personal alipit"},
    "1. Dhamir__11a": {"arti_ro": "Eu (Pers. 1 sg.)", "desc_ro": "Pronume personal independent pers. 1 sg.", "jenis_ro": "Pronume personal independent"},
    "1. Dhamir__11b": {"arti_ro": "Meu / Mie / Mă (Alipit)", "desc_ro": "Pronume personal alipit pers. 1 sg.", "jenis_ro": "Pronume personal alipit"},
    "1. Dhamir__11c": {"arti_ro": "Numai mie", "desc_ro": "Pronume acuzatival independent pers. 1 sg.", "jenis_ro": "Pronume acuzatival"},
    "1. Dhamir__12a": {"arti_ro": "Noi (Pers. 1 pl.)", "desc_ro": "Pronume personal independent pers. 1 pl.", "jenis_ro": "Pronume personal independent"},
    "1. Dhamir__12b": {"arti_ro": "Nostru / Nouă / Ne (Alipit)", "desc_ro": "Pronume personal alipit pers. 1 pl.", "jenis_ro": "Pronume personal alipit"},
    "1. Dhamir__12c": {"arti_ro": "Numai nouă", "desc_ro": "Pronume acuzatival independent pers. 1 pl.", "jenis_ro": "Pronume acuzatival"},

    "2. Isim Mawshul__1": {"arti_ro": "Ceea ce / Tot ce (Pentru lucruri)", "desc_ro": "Pronume relativ general pentru lucruri neînsuflețite", "jenis_ro": "Pronume relativ general"},
    "2. Isim Mawshul__2": {"arti_ro": "Cei care (Plural masc.)", "desc_ro": "Pronume relativ pentru ființe raționale la plural", "jenis_ro": "Pronume relativ specific"},
    "2. Isim Mawshul__3": {"arti_ro": "Cel care / Cine (Pentru ființe raționale)", "desc_ro": "Pronume relativ general pentru persoane și ființe raționale", "jenis_ro": "Pronume relativ general"},
    "2. Isim Mawshul__4": {"arti_ro": "Cel care (Singular masc.)", "desc_ro": "Pronume relativ pentru masculin singular", "jenis_ro": "Pronume relativ specific"},
    "2. Isim Mawshul__5": {"arti_ro": "Oricare / Oricine", "desc_ro": "Pronume relativ genitival", "jenis_ro": "Pronume relativ"},
    "2. Isim Mawshul__6": {"arti_ro": "Cea care (Singular fem.)", "desc_ro": "Pronume relativ pentru feminin singular", "jenis_ro": "Pronume relativ specific"},
    "2. Isim Mawshul__7": {"arti_ro": "Cele care (Plural fem.)", "desc_ro": "Pronume relativ pentru femei la plural", "jenis_ro": "Pronume relativ feminin"},
    "2. Isim Mawshul__8": {"arti_ro": "Cele care (Plural fem.)", "desc_ro": "Pronume relativ pentru femei la plural", "jenis_ro": "Pronume relativ feminin"},
    "2. Isim Mawshul__9": {"arti_ro": "Cei doi care", "desc_ro": "Pronume relativ dual", "jenis_ro": "Pronume relativ dual"},
    "2. Isim Mawshul__10": {"arti_ro": "Oricare femeie", "desc_ro": "Pronume relativ feminin", "jenis_ro": "Pronume relativ"},

    "3. Isim Istifham__1": {"arti_ro": "Ce? / Ce este aceasta?", "desc_ro": "Pronume interogativ pentru lucruri", "jenis_ro": "Pronume interogativ"},
    "3. Isim Istifham__2": {"arti_ro": "Cine? / Cine este?", "desc_ro": "Pronume interogativ pentru persoane", "jenis_ro": "Pronume interogativ"},
    "3. Isim Istifham__3": {"arti_ro": "Cum? / În ce chip?", "desc_ro": "Pronume interogativ de stare", "jenis_ro": "Pronume interogativ de stare"},
    "3. Isim Istifham__4": {"arti_ro": "Unde? / Încotro?", "desc_ro": "Pronume interogativ de loc", "jenis_ro": "Pronume interogativ de loc"},
    "3. Isim Istifham__5": {"arti_ro": "Cât? / Câte?", "desc_ro": "Pronume interogativ de cantitate", "jenis_ro": "Pronume interogativ de cantitate"},
    "3. Isim Istifham__6": {"arti_ro": "Când? / În ce vreme?", "desc_ro": "Pronume interogativ de timp", "jenis_ro": "Pronume interogativ de timp"},
    "3. Isim Istifham__7": {"arti_ro": "Când se va întâmpla? (Ziua Învierii)", "desc_ro": "Pronume interogativ pentru mari evenimente viitoare", "jenis_ro": "Pronume interogativ de timp"},
    "3. Isim Istifham__8": {"arti_ro": "De unde? / Cum oare?", "desc_ro": "Pronume interogativ de origine sau cauză", "jenis_ro": "Pronume interogativ"},

    "4. Isim Syarath__1": {"arti_ro": "Oricine / Cel ce", "desc_ro": "Pronume condițional pentru persoane care cere jusiv", "jenis_ro": "Pronume condițional"},
    "4. Isim Syarath__2": {"arti_ro": "Orice / Orice ați face", "desc_ro": "Pronume condițional pentru lucruri", "jenis_ro": "Pronume condițional"},
    "4. Isim Syarath__3": {"arti_ro": "Când / În clipa când", "desc_ro": "Cuvânt condițional temporal pentru viitor", "jenis_ro": "Cuvânt condițional temporal"},
    "4. Isim Syarath__4": {"arti_ro": "Orice ar fi", "desc_ro": "Pronume condițional general", "jenis_ro": "Pronume condițional"},
    "4. Isim Syarath__5": {"arti_ro": "Oriunde / Încotro", "desc_ro": "Cuvânt condițional de loc", "jenis_ro": "Cuvânt condițional de loc"},
    "4. Isim Syarath__6": {"arti_ro": "Oriunde v-ați afla", "desc_ro": "Cuvânt condițional de loc întărit", "jenis_ro": "Cuvânt condițional de loc"},
    "4. Isim Syarath__7": {"arti_ro": "În orice stare", "desc_ro": "Cuvânt condițional de stare", "jenis_ro": "Cuvânt condițional de stare"},
    "4. Isim Syarath__8": {"arti_ro": "Oricare", "desc_ro": "Cuvânt condițional genitival", "jenis_ro": "Cuvânt condițional"},

    "5. Isim Isyarah__1": {"arti_ro": "Acea carte / Aceea (Depărtat masc.)", "desc_ro": "Pronume demonstrativ pentru obiecte depărtate masc.", "jenis_ro": "Pronume demonstrativ de depărtare"},
    "5. Isim Isyarah__2": {"arti_ro": "Acest / Acesta (Apropiat masc.)", "desc_ro": "Pronume demonstrativ pentru obiecte apropiate masc.", "jenis_ro": "Pronume demonstrativ de apropiere"},
    "5. Isim Isyarah__3": {"arti_ro": "Aceștia / Acestea (Apropiat pl.)", "desc_ro": "Pronume demonstrativ pentru plural apropiat", "jenis_ro": "Pronume demonstrativ de apropiere"},
    "5. Isim Isyarah__4": {"arti_ro": "Aceia / Acelea (Depărtat pl.)", "desc_ro": "Pronume demonstrativ pentru plural depărtat", "jenis_ro": "Pronume demonstrativ de depărtare"},
    "5. Isim Isyarah__5": {"arti_ro": "Aceasta (Apropiat fem.)", "desc_ro": "Pronume demonstrativ pentru feminin singular apropiat", "jenis_ro": "Pronume demonstrativ de apropiere"},
    "5. Isim Isyarah__6": {"arti_ro": "Aceea (Depărtat fem.)", "desc_ro": "Pronume demonstrativ pentru feminin singular depărtat", "jenis_ro": "Pronume demonstrativ de depărtare"},
    "5. Isim Isyarah__7": {"arti_ro": "Acolo / În acel loc", "desc_ro": "Pronume demonstrativ pentru loc depărtat", "jenis_ro": "Pronume demonstrativ de loc"},
    "5. Isim Isyarah__8": {"arti_ro": "Aici / În acest loc", "desc_ro": "Pronume demonstrativ pentru loc apropiat", "jenis_ro": "Pronume demonstrativ de loc"},
    "5. Isim Isyarah__9": {"arti_ro": "Aceste două lucruri (Depărtat masc.)", "desc_ro": "Pronume demonstrativ dual", "jenis_ro": "Pronume demonstrativ dual"},
    "5. Isim Isyarah__10": {"arti_ro": "Aceste două lucruri (Depărtat fem.)", "desc_ro": "Pronume demonstrativ dual", "jenis_ro": "Pronume demonstrativ dual"},

    "6. Isim Fi'il__1": {"arti_ro": "Cât de departe este! (Hayhata)", "desc_ro": "Substantiv verbal de trecut", "jenis_ro": "Substantiv verbal de trecut"},
    "6. Isim Fi'il__2": {"arti_ro": "Uff! / Vai! (Uff)", "desc_ro": "Substantiv verbal de prezent exprimând nemulțumirea", "jenis_ro": "Substantiv verbal de prezent"},
    "6. Isim Fi'il__3": {"arti_ro": "Veniți! / Aduceți!", "desc_ro": "Substantiv verbal imperativ", "jenis_ro": "Substantiv verbal imperativ"},
    "6. Isim Fi'il__4": {"arti_ro": "Luați! / Citiți!", "desc_ro": "Substantiv verbal imperativ", "jenis_ro": "Substantiv verbal imperativ"},
    "6. Isim Fi'il__5": {"arti_ro": "Păziți-vă! / Țineți-vă bine!", "desc_ro": "Substantiv verbal imperativ provenit din prepoziție", "jenis_ro": "Substantiv verbal imperativ"},
    "6. Isim Fi'il__6": {"arti_ro": "Luați aceasta!", "desc_ro": "Substantiv verbal imperativ provenit din adverb", "jenis_ro": "Substantiv verbal imperativ"},
    "6. Isim Fi'il__7": {"arti_ro": "Cât de minunat!", "desc_ro": "Substantiv verbal exprimând uimirea", "jenis_ro": "Substantiv verbal"},
    "6. Isim Fi'il__8": {"arti_ro": "Dați-vă la o parte! / Iată", "desc_ro": "Substantiv verbal imperativ", "jenis_ro": "Substantiv verbal imperativ"},

    "7. Fi'il Jamid__1": {"arti_ro": "Ce minunat! (Ni'ma)", "desc_ro": "Verb invariabil de laudă", "jenis_ro": "Verb invariabil de laudă"},
    "7. Fi'il Jamid__2": {"arti_ro": "Ce ticălos! (Bi'sa)", "desc_ro": "Verb invariabil de blamare", "jenis_ro": "Verb invariabil de blamare"},
    "7. Fi'il Jamid__3": {"arti_ro": "Nu este / Nu a fost (Laysa)", "desc_ro": "Verb copulativ invariabil de negație", "jenis_ro": "Verb invariabil de negație"},
    "7. Fi'il Jamid__4": {"arti_ro": "Poate / Este nădejde ('Asa)", "desc_ro": "Verb invariabil al speranței", "jenis_ro": "Verb al speranței"},
    "7. Fi'il Jamid__5": {"arti_ro": "Ce rău este! (Sa'a)", "desc_ro": "Verb invariabil de blamare", "jenis_ro": "Verb invariabil de blamare"},
    "7. Fi'il Jamid__6": {"arti_ro": "Ce plăcut!", "desc_ro": "Verb compus de laudă", "jenis_ro": "Verb de laudă"},
    "7. Fi'il Jamid__7": {"arti_ro": "Binecuvântat și Preaînalt! (Tabaraka)", "desc_ro": "Verb sacru invariabil al măreției divine", "jenis_ro": "Verb sacru invariabil"}
}

SWEDISH_GRAMMAR = {
    "1. Dhamir__1a": {"arti_sv": "Han (3:e pers. mask. sing.)", "desc_sv": "Självständigt personligt pronomen 3:e pers. mask. sing. (Munfasil)", "jenis_sv": "Självständigt personligt pronomen"},
    "1. Dhamir__1b": {"arti_sv": "Hans / Honom (Fogepronomen)", "desc_sv": "Fogepronomen 3:e pers. mask. sing. (Muttasil)", "jenis_sv": "Fogepronomen"},
    "1. Dhamir__1c": {"arti_sv": "Bara Honom (Ackusativ)", "desc_sv": "Självständigt ackusativpronomen 3:e pers. sing.", "jenis_sv": "Ackusativpronomen"},
    "1. Dhamir__2a": {"arti_sv": "De två (Dualis)", "desc_sv": "Självständigt dualispronomen", "jenis_sv": "Dualispronomen"},
    "1. Dhamir__2b": {"arti_sv": "Deras två (Fogepronomen)", "desc_sv": "Fogepronomen för dualis", "jenis_sv": "Dualis fogepronomen"},
    "1. Dhamir__3a": {"arti_sv": "De (Maskulint plural)", "desc_sv": "Självständigt pronomen 3:e pers. mask. plural", "jenis_sv": "Självständigt pronomen"},
    "1. Dhamir__3b": {"arti_sv": "Deras / Dem (Fogepronomen)", "desc_sv": "Fogepronomen 3:e pers. mask. plural", "jenis_sv": "Fogepronomen"},
    "1. Dhamir__3c": {"arti_sv": "Bara dem", "desc_sv": "Självständigt ackusativpronomen 3:e pers. mask. plural", "jenis_sv": "Ackusativpronomen"},
    "1. Dhamir__4a": {"arti_sv": "Hon (3:e pers. fem. sing.)", "desc_sv": "Självständigt pronomen 3:e pers. fem. sing.", "jenis_sv": "Självständigt pronomen"},
    "1. Dhamir__4b": {"arti_sv": "Hennes / Henne (Fogepronomen)", "desc_sv": "Fogepronomen 3:e pers. fem. sing.", "jenis_sv": "Fogepronomen"},
    "1. Dhamir__5a": {"arti_sv": "De (Feminint plural)", "desc_sv": "Självständigt pronomen 3:e pers. fem. plural", "jenis_sv": "Självständigt pronomen"},
    "1. Dhamir__5b": {"arti_sv": "Deras (Feminint fogepronomen)", "desc_sv": "Fogepronomen 3:e pers. fem. plural", "jenis_sv": "Fogepronomen"},
    "1. Dhamir__6a": {"arti_sv": "Du (2:a pers. mask. sing.)", "desc_sv": "Självständigt pronomen 2:a pers. mask. sing.", "jenis_sv": "Självständigt pronomen"},
    "1. Dhamir__6b": {"arti_sv": "Din / Dig (Fogepronomen)", "desc_sv": "Fogepronomen 2:a pers. mask. sing.", "jenis_sv": "Fogepronomen"},
    "1. Dhamir__6c": {"arti_sv": "Bara Dig (Exklusiv tillbedjan)", "desc_sv": "Självständigt ackusativpronomen 2:a pers. sing.", "jenis_sv": "Ackusativpronomen"},
    "1. Dhamir__7a": {"arti_sv": "Ni två", "desc_sv": "Självständigt pronomen 2:a pers. dualis", "jenis_sv": "Dualispronomen"},
    "1. Dhamir__7b": {"arti_sv": "Er två (Fogepronomen)", "desc_sv": "Fogepronomen 2:a pers. dualis", "jenis_sv": "Dualis fogepronomen"},
    "1. Dhamir__8a": {"arti_sv": "Ni (Maskulint plural)", "desc_sv": "Självständigt pronomen 2:a pers. mask. plural", "jenis_sv": "Självständigt pronomen"},
    "1. Dhamir__8b": {"arti_sv": "Er / Eder (Fogepronomen)", "desc_sv": "Fogepronomen 2:a pers. mask. plural", "jenis_sv": "Fogepronomen"},
    "1. Dhamir__8c": {"arti_sv": "Bara er", "desc_sv": "Självständigt ackusativpronomen 2:a pers. mask. plural", "jenis_sv": "Ackusativpronomen"},
    "1. Dhamir__9a": {"arti_sv": "Du (2:a pers. fem. sing.)", "desc_sv": "Självständigt pronomen 2:a pers. fem. sing.", "jenis_sv": "Självständigt pronomen"},
    "1. Dhamir__9b": {"arti_sv": "Din / Dig (Feminint fogepronomen)", "desc_sv": "Fogepronomen 2:a pers. fem. sing.", "jenis_sv": "Fogepronomen"},
    "1. Dhamir__10a": {"arti_sv": "Ni (Feminint plural)", "desc_sv": "Självständigt pronomen 2:a pers. fem. plural", "jenis_sv": "Självständigt pronomen"},
    "1. Dhamir__10b": {"arti_sv": "Er (Feminint fogepronomen)", "desc_sv": "Fogepronomen 2:a pers. fem. plural", "jenis_sv": "Fogepronomen"},
    "1. Dhamir__11a": {"arti_sv": "Jag (1:a pers. sing.)", "desc_sv": "Självständigt pronomen 1:a pers. sing.", "jenis_sv": "Självständigt pronomen"},
    "1. Dhamir__11b": {"arti_sv": "Min / Mig (Fogepronomen)", "desc_sv": "Fogepronomen 1:a pers. sing.", "jenis_sv": "Fogepronomen"},
    "1. Dhamir__11c": {"arti_sv": "Bara mig", "desc_sv": "Självständigt ackusativpronomen 1:a pers. sing.", "jenis_sv": "Ackusativpronomen"},
    "1. Dhamir__12a": {"arti_sv": "Vi (1:a pers. plural)", "desc_sv": "Självständigt pronomen 1:a pers. plural", "jenis_sv": "Självständigt pronomen"},
    "1. Dhamir__12b": {"arti_sv": "Vår / Oss (Fogepronomen)", "desc_sv": "Fogepronomen 1:a pers. plural", "jenis_sv": "Fogepronomen"},
    "1. Dhamir__12c": {"arti_sv": "Bara oss", "desc_sv": "Självständigt ackusativpronomen 1:a pers. plural", "jenis_sv": "Ackusativpronomen"},

    "2. Isim Mawshul__1": {"arti_sv": "Det som / Allt vad (Livlösa ting)", "desc_sv": "Allmänt relativt pronomen för livlösa ting", "jenis_sv": "Allmänt relativt pronomen"},
    "2. Isim Mawshul__2": {"arti_sv": "De som (Maskulint plural)", "desc_sv": "Relativt pronomen för förnuftiga varelser i plural", "jenis_sv": "Specifikt relativt pronomen"},
    "2. Isim Mawshul__3": {"arti_sv": "Den som / Vem som (Personer)", "desc_sv": "Allmänt relativt pronomen för personer och förnuftiga varelser", "jenis_sv": "Allmänt relativt pronomen"},
    "2. Isim Mawshul__4": {"arti_sv": "Han som / Den som (Maskulint sing.)", "desc_sv": "Relativt pronomen för maskulinum singular", "jenis_sv": "Specifikt relativt pronomen"},
    "2. Isim Mawshul__5": {"arti_sv": "Vilken som helst / Vemhelst", "desc_sv": "Genitiviskt relativt pronomen", "jenis_sv": "Relativt pronomen"},
    "2. Isim Mawshul__6": {"arti_sv": "Hon som / Den som (Feminint sing.)", "desc_sv": "Relativt pronomen för femininum singular", "jenis_sv": "Specifikt relativt pronomen"},
    "2. Isim Mawshul__7": {"arti_sv": "De kvinnor som (Plural)", "desc_sv": "Relativt pronomen för kvinnor i plural", "jenis_sv": "Feminint relativt pronomen"},
    "2. Isim Mawshul__8": {"arti_sv": "De kvinnor som (Plural)", "desc_sv": "Relativt pronomen för kvinnor i plural", "jenis_sv": "Feminint relativt pronomen"},
    "2. Isim Mawshul__9": {"arti_sv": "De två som", "desc_sv": "Dualis relativt pronomen", "jenis_sv": "Dualis relativt pronomen"},
    "2. Isim Mawshul__10": {"arti_sv": "Vilken kvinna som helst", "desc_sv": "Feminint relativt pronomen", "jenis_sv": "Relativt pronomen"},

    "3. Isim Istifham__1": {"arti_sv": "Vad? / Vad är detta?", "desc_sv": "Frågepronomen för ting", "jenis_sv": "Frågepronomen"},
    "3. Isim Istifham__2": {"arti_sv": "Vem? / Vem är?", "desc_sv": "Frågepronomen för personer", "jenis_sv": "Frågepronomen"},
    "3. Isim Istifham__3": {"arti_sv": "Hur? / På vilket sätt?", "desc_sv": "Frågepronomen för tillstånd", "jenis_sv": "Tillståndsfrågepronomen"},
    "3. Isim Istifham__4": {"arti_sv": "Var? / Varthän?", "desc_sv": "Frågepronomen för plats", "jenis_sv": "Platsfrågepronomen"},
    "3. Isim Istifham__5": {"arti_sv": "Hur många? / Hur mycket?", "desc_sv": "Frågepronomen för antal och mängd", "jenis_sv": "Mängdfrågepronomen"},
    "3. Isim Istifham__6": {"arti_sv": "När? / Vid vilken tid?", "desc_sv": "Frågepronomen för tid", "jenis_sv": "Tidsfrågepronomen"},
    "3. Isim Istifham__7": {"arti_sv": "När inträffar det? (Uppståndelsens dag)", "desc_sv": "Frågepronomen för stora framtida händelser", "jenis_sv": "Tidsfrågepronomen"},
    "3. Isim Istifham__8": {"arti_sv": "Varifrån? / Hur så?", "desc_sv": "Frågepronomen för ursprung eller orsak", "jenis_sv": "Frågepronomen"},

    "4. Isim Syarath__1": {"arti_sv": "Vem som helst / Den som", "desc_sv": "Villkorspronomen för personer som kräver jussiv", "jenis_sv": "Villkorspronomen"},
    "4. Isim Syarath__2": {"arti_sv": "Vad som helst / Vad ni än gör", "desc_sv": "Villkorspronomen för ting", "jenis_sv": "Villkorspronomen"},
    "4. Isim Syarath__3": {"arti_sv": "När / I samma stund som", "desc_sv": "Tidsvillkorsord för framtiden", "jenis_sv": "Tidsvillkorsord"},
    "4. Isim Syarath__4": {"arti_sv": "Vad det än må vara", "desc_sv": "Allmänt villkorspronomen", "jenis_sv": "Villkorspronomen"},
    "4. Isim Syarath__5": {"arti_sv": "Var som helst / Varthän", "desc_sv": "Platsvillkorsord", "jenis_sv": "Platsvillkorsord"},
    "4. Isim Syarath__6": {"arti_sv": "Var ni än befinner er", "desc_sv": "Förstärkt platsvillkorsord", "jenis_sv": "Platsvillkorsord"},
    "4. Isim Syarath__7": {"arti_sv": "I vilket tillstånd som helst", "desc_sv": "Tillståndsvillkorsord", "jenis_sv": "Tillståndsvillkorsord"},
    "4. Isim Syarath__8": {"arti_sv": "Vilken som helst", "desc_sv": "Genitiviskt villkorsord", "jenis_sv": "Villkorsord"},

    "5. Isim Isyarah__1": {"arti_sv": "Den / Boken där (Avlägsen mask.)", "desc_sv": "Påpekande pronomen för avlägsna föremål mask.", "jenis_sv": "Avlägset påpekande pronomen"},
    "5. Isim Isyarah__2": {"arti_sv": "Denna / Detta (Nära mask.)", "desc_sv": "Påpekande pronomen för nära föremål mask.", "jenis_sv": "Nära påpekande pronomen"},
    "5. Isim Isyarah__3": {"arti_sv": "Dessa (Nära plural)", "desc_sv": "Påpekande pronomen för nära plural", "jenis_sv": "Nära påpekande pronomen"},
    "5. Isim Isyarah__4": {"arti_sv": "De där / Hina (Avlägsen plural)", "desc_sv": "Påpekande pronomen för avlägsen plural", "jenis_sv": "Avlägset påpekande pronomen"},
    "5. Isim Isyarah__5": {"arti_sv": "Denna (Nära fem.)", "desc_sv": "Påpekande pronomen för nära femininum singular", "jenis_sv": "Nära påpekande pronomen"},
    "5. Isim Isyarah__6": {"arti_sv": "Den där (Avlägsen fem.)", "desc_sv": "Påpekande pronomen för avlägsen femininum singular", "jenis_sv": "Avlägset påpekande pronomen"},
    "5. Isim Isyarah__7": {"arti_sv": "Där / På den platsen", "desc_sv": "Påpekande pronomen för avlägsen plats", "jenis_sv": "Platspåpekande pronomen"},
    "5. Isim Isyarah__8": {"arti_sv": "Här / På denna plats", "desc_sv": "Påpekande pronomen för nära plats", "jenis_sv": "Platspåpekande pronomen"},
    "5. Isim Isyarah__9": {"arti_sv": "Dessa två ting (Avlägsen mask.)", "desc_sv": "Dualis påpekande pronomen", "jenis_sv": "Dualis påpekande pronomen"},
    "5. Isim Isyarah__10": {"arti_sv": "Dessa två ting (Avlägsen fem.)", "desc_sv": "Dualis påpekande pronomen", "jenis_sv": "Dualis påpekande pronomen"},

    "6. Isim Fi'il__1": {"arti_sv": "Hur fjärran är det inte! (Hayhata)", "desc_sv": "Verbalsubstantiv i dåtid", "jenis_sv": "Dåtidigt verbalsubstantiv"},
    "6. Isim Fi'il__2": {"arti_sv": "Fy! / Tvi! (Uff)", "desc_sv": "Verbalsubstantiv för missnöje i nutid", "jenis_sv": "Nutidigt verbalsubstantiv"},
    "6. Isim Fi'il__3": {"arti_sv": "Kom hit! / Bär fram!", "desc_sv": "Bjudande verbalsubstantiv", "jenis_sv": "Imperativt verbalsubstantiv"},
    "6. Isim Fi'il__4": {"arti_sv": "Tag! / Läs!", "desc_sv": "Bjudande verbalsubstantiv", "jenis_sv": "Imperativt verbalsubstantiv"},
    "6. Isim Fi'il__5": {"arti_sv": "Akta er! / Håll fast vid!", "desc_sv": "Bjudande verbalsubstantiv bildat av preposition", "jenis_sv": "Imperativt verbalsubstantiv"},
    "6. Isim Fi'il__6": {"arti_sv": "Tag detta!", "desc_sv": "Bjudande verbalsubstantiv bildat av adverb", "jenis_sv": "Imperativt verbalsubstantiv"},
    "6. Isim Fi'il__7": {"arti_sv": "Hur förunderligt!", "desc_sv": "Verbalsubstantiv för förundran", "jenis_sv": "Verbalsubstantiv"},
    "6. Isim Fi'il__8": {"arti_sv": "Träd tillbaka! / Här har du det", "desc_sv": "Bjudande verbalsubstantiv", "jenis_sv": "Imperativt verbalsubstantiv"},

    "7. Fi'il Jamid__1": {"arti_sv": "Hur förträfflig! (Ni'ma)", "desc_sv": "Oböjligt lovordande verb", "jenis_sv": "Lovordande oböjligt verb"},
    "7. Fi'il Jamid__2": {"arti_sv": "Hur usel! (Bi'sa)", "desc_sv": "Oböjligt klandrande verb", "jenis_sv": "Klandrande oböjligt verb"},
    "7. Fi'il Jamid__3": {"arti_sv": "Är inte / Var inte (Laysa)", "desc_sv": "Oböjligt nekande kopulaverb", "jenis_sv": "Nekande oböjligt verb"},
    "7. Fi'il Jamid__4": {"arti_sv": "Kanske / Förhoppningsvis ('Asa)", "desc_sv": "Oböjligt hoppverb", "jenis_sv": "Hoppverb"},
    "7. Fi'il Jamid__5": {"arti_sv": "Hur ont är det inte! (Sa'a)", "desc_sv": "Oböjligt klandrande verb", "jenis_sv": "Klandrande oböjligt verb"},
    "7. Fi'il Jamid__6": {"arti_sv": "Hur angenämt!", "desc_sv": "Sammansatt lovordande verb", "jenis_sv": "Lovordande verb"},
    "7. Fi'il Jamid__7": {"arti_sv": "Välsignad och Upphöjd! (Tabaraka)", "desc_sv": "Heligt oböjligt verb för Guds storhet", "jenis_sv": "Heligt oböjligt verb"}
}

ROMANIAN_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {"arti_ro": "Nu / Nicidecum (Ma - negație generală)", "desc_ro": "Particulă de negație fără regim pentru trecut, prezent și propoziții nominale", "jenis_ro": "Particulă de negație"},
    "1. Harf Nafyi__2": {"arti_ro": "Nu / Ba nu (La - negație verbală)", "desc_ro": "Particulă de negație pentru prezent și viitor", "jenis_ro": "Particulă de negație"},
    "1. Harf Nafyi__3": {"arti_ro": "Nu este altceva decât... (In)", "desc_ro": "Particulă de negație combinată cu Illa", "jenis_ro": "Particulă de negație"},
    "1. Harf Nafyi__4": {"arti_ro": "Nu mai este vreme de (Lata)", "desc_ro": "Particulă temporală de negație", "jenis_ro": "Particulă de negație temporală"},

    "2. Harf Tahqiq Taswif__5": {"arti_ro": "Într-adevăr / Deja (Qad - confirmare)", "desc_ro": "Particulă de certitudine și întărire înaintea verbelor trecute", "jenis_ro": "Particulă de confirmare"},
    "2. Harf Tahqiq Taswif__6": {"arti_ro": "În viitor / Mai târziu (Sawfa)", "desc_ro": "Particulă pentru viitor îndepărtat", "jenis_ro": "Particulă de viitor"},
    "2. Harf Tahqiq Taswif__7": {"arti_ro": "Curând / Îndată (Sa - viitor apropiat)", "desc_ro": "Particulă pentru viitor apropiat", "jenis_ro": "Particulă de viitor"},

    "3. Harf Syarat__8": {"arti_ro": "Dacă / Dacă ar fi fost (Law - condiție nerealizabilă)", "desc_ro": "Particulă condițională fără regim pentru acțiuni trecute neîmplinite", "jenis_ro": "Particulă condițională"},
    "3. Harf Syarat__9": {"arti_ro": "Dacă n-ar fi fost... (Lawla)", "desc_ro": "Particulă condițională de împiedicare", "jenis_ro": "Particulă condițională"},
    "3. Harf Syarat__10": {"arti_ro": "De n-ar fi... (Lawma)", "desc_ro": "Particulă condițională fără regim", "jenis_ro": "Particulă condițională"},
    "3. Harf Syarat__11": {"arti_ro": "Când / În vremea când (Lamma)", "desc_ro": "Particulă condițională temporală pentru trecut", "jenis_ro": "Particulă condițională temporală"},
    "3. Harf Syarat__12": {"arti_ro": "Cât despre... atunci (Amma)", "desc_ro": "Particulă condițională de detaliere cu accent emfatic", "jenis_ro": "Particulă condițională"},

    "4. Harf Mashdariyah__13": {"arti_ro": "Să / Că (An - particulă infinitivală)", "desc_ro": "Particulă care transformă verbul în substantiv verbal (masdar)", "jenis_ro": "Particulă infinitivală"},
    "4. Harf Mashdariyah__14": {"arti_ro": "Cât timp / Atâta vreme cât (Ma masdariyyah)", "desc_ro": "Particulă infinitivală temporală", "jenis_ro": "Particulă infinitivală"},
    "4. Harf Mashdariyah__15": {"arti_ro": "Pentru ca / Ca să (Kay)", "desc_ro": "Particulă infinitivală finală", "jenis_ro": "Particulă infinitivală"},
    "4. Harf Mashdariyah__16": {"arti_ro": "Măcar de / Dorința de a (Law)", "desc_ro": "Particulă infinitivală după verbe de dorință", "jenis_ro": "Particulă infinitivală"},

    "5. Harf Zaidah__17": {"arti_ro": "Pentru întărirea sensului (In za'idah)", "desc_ro": "Particulă suplimentară de întărire", "jenis_ro": "Particulă de întărire"},
    "5. Harf Zaidah__18": {"arti_ro": "Pentru întărirea sensului (An za'idah)", "desc_ro": "Particulă suplimentară de întărire", "jenis_ro": "Particulă de întărire"},
    "5. Harf Zaidah__19": {"arti_ro": "Pentru întărirea sensului (Ma za'idah)", "desc_ro": "Particulă suplimentară de întărire", "jenis_ro": "Particulă de întărire"},
    "5. Harf Zaidah__20": {"arti_ro": "Pentru întărirea sensului (La za'idah)", "desc_ro": "Particulă suplimentară de întărire a negației", "jenis_ro": "Particulă de întărire"},

    "6. Harf Istifham__21": {"arti_ro": "Oare? / Au doară? (Hamzah)", "desc_ro": "Particulă interogativă fundamentală", "jenis_ro": "Particulă interogativă"},
    "6. Harf Istifham__22": {"arti_ro": "Oare? / Este așa? (Hal)", "desc_ro": "Particulă interogativă cerând confirmare sau infirmare", "jenis_ro": "Particulă interogativă"},

    "7. Harf Istitsna__23": {"arti_ro": "Afară de / Cu excepția (Illa)", "desc_ro": "Particulă de excepție", "jenis_ro": "Particulă de excepție"},

    "8. Harf Rad'in Wazajrin__24": {"arti_ro": "Nicidecum! / În niciun caz! (Kalla)", "desc_ro": "Particulă categorică de respingere și dojană", "jenis_ro": "Particulă de respingere"},

    "9. Harf Rad'in Tahdid__25": {"arti_ro": "De ce oare nu...? (Halla)", "desc_ro": "Particulă de îndemn și dojană", "jenis_ro": "Particulă de îndemn"},
    "9. Harf Rad'in Tahdid__26": {"arti_ro": "De ce dar nu... (Alla)", "desc_ro": "Particulă de îndemn grabnic la fapte bune", "jenis_ro": "Particulă de îndemn"},

    "10. Harf Ijab__27": {"arti_ro": "Da / Așa este (Na'am)", "desc_ro": "Particulă afirmativă de răspuns", "jenis_ro": "Particulă de răspuns"},
    "10. Harf Ijab__28": {"arti_ro": "Ba da, cu adevărat! (Bala)", "desc_ro": "Particulă care anulează negația și confirmă adevărul", "jenis_ro": "Particulă de confirmare"},
    "10. Harf Ijab__29": {"arti_ro": "Da, pe Domnul meu! (I)", "desc_ro": "Particulă de confirmare la jurământ", "jenis_ro": "Particulă de jurământ"},
    "10. Harf Ijab__30": {"arti_ro": "Cu adevărat / Negreșit (Ajal)", "desc_ro": "Particulă de confirmare", "jenis_ro": "Particulă de confirmare"},

    "11. Harf Tafsir__31": {"arti_ro": "Adică / Anume (Ay)", "desc_ro": "Particulă explicativă", "jenis_ro": "Particulă explicativă"},
    "11. Harf Tafsir__32": {"arti_ro": "Că / Anume (An tafsiriyyah)", "desc_ro": "Particulă explicativă după verbe de zicere", "jenis_ro": "Particulă explicativă"},

    "12. Harf Tanbih__33": {"arti_ro": "Iată! / Luați aminte! (Ala)", "desc_ro": "Particulă de atenționare la începutul frazei", "jenis_ro": "Particulă de atenționare"},
    "12. Harf Tanbih__34": {"arti_ro": "Aflați bine! (Ama)", "desc_ro": "Particulă de atenționare", "jenis_ro": "Particulă de atenționare"},
    "12. Harf Tanbih__35": {"arti_ro": "Iată priviți! (Ha tanbih)", "desc_ro": "Particulă atrăgând atenția înaintea pronumelor", "jenis_ro": "Particulă de atenționare"},

    "13. Harf Ta'lil__36": {"arti_ro": "Pentru ca / Deoarece (Lam ta'lil)", "desc_ro": "Particulă cauzală exprimând scopul și motivul", "jenis_ro": "Particulă cauzală"},

    "14. Harf Fuja'iyyah__37": {"arti_ro": "Și deodată! / Și iată (Idha fuja'iyyah)", "desc_ro": "Particulă exprimând un eveniment brusc și neașteptat", "jenis_ro": "Particulă de surpriză"},
    "14. Harf Fuja'iyyah__38": {"arti_ro": "Pe neașteptate (Idh fuja'iyyah)", "desc_ro": "Particulă de surpriză", "jenis_ro": "Particulă de surpriză"},

    "15. Harf Istidrak__39": {"arti_ro": "Dar / Însă (Lakin)", "desc_ro": "Particulă adversativă și de corectare", "jenis_ro": "Particulă adversativă"},
    "15. Harf Istidrak__40": {"arti_ro": "Dimpotrivă / Ba chiar (Bal)", "desc_ro": "Particulă de schimbare a aserțiunii", "jenis_ro": "Particulă adversativă"},

    "16. Harf Ta'ajjub__41": {"arti_ro": "Cât de... doar! / Cât de minunat! (Ma)", "desc_ro": "Particulă exclamativă de admirație și uimire", "jenis_ro": "Particulă de admirație"},

    "17. Harf Mabany__39": {"arti_ro": "Ha-Mim", "desc_ro": "Litere introductive ale surelor", "jenis_ro": "Litere Muqatta'at"},
    "17. Harf Mabany__40": {"arti_ro": "Alif-Lam-Mim", "desc_ro": "Litere introductive ale surelor", "jenis_ro": "Litere Muqatta'at"},
    "17. Harf Mabany__41": {"arti_ro": "Alif-Lam-Ra", "desc_ro": "Litere introductive ale surelor", "jenis_ro": "Litere Muqatta'at"},
    "17. Harf Mabany__42": {"arti_ro": "Ta-Sin-Mim", "desc_ro": "Litere introductive ale surelor", "jenis_ro": "Litere Muqatta'at"},
    "17. Harf Mabany__43": {"arti_ro": "Alif-Lam-Mim-Ra", "desc_ro": "Litere introductive ale surelor", "jenis_ro": "Litere Muqatta'at"},
    "17. Harf Mabany__44": {"arti_ro": "Alif-Lam-Mim-Sad", "desc_ro": "Litere introductive ale surelor", "jenis_ro": "Litere Muqatta'at"},
    "17. Harf Mabany__45": {"arti_ro": "Sad", "desc_ro": "Litere introductive ale surelor", "jenis_ro": "Litere Muqatta'at"},
    "17. Harf Mabany__46": {"arti_ro": "Ta-Sin", "desc_ro": "Litere introductive ale surelor", "jenis_ro": "Litere Muqatta'at"},
    "17. Harf Mabany__47": {"arti_ro": "Ta-Ha", "desc_ro": "Litere introductive ale surelor", "jenis_ro": "Litere Muqatta'at"},
    "17. Harf Mabany__48": {"arti_ro": "'Ayn-Sin-Qaf", "desc_ro": "Litere introductive ale surelor", "jenis_ro": "Litere Muqatta'at"},
    "17. Harf Mabany__49": {"arti_ro": "Qaf", "desc_ro": "Litere introductive ale surelor", "jenis_ro": "Litere Muqatta'at"},
    "17. Harf Mabany__50": {"arti_ro": "Kaf-Ha-Ya-'Ayn-Sad", "desc_ro": "Litere introductive ale surelor", "jenis_ro": "Litere Muqatta'at"},
    "17. Harf Mabany__51": {"arti_ro": "Nun", "desc_ro": "Litere introductive ale surelor", "jenis_ro": "Litere Muqatta'at"},
    "17. Harf Mabany__52": {"arti_ro": "Ya-Sin", "desc_ro": "Litere introductive ale surelor", "jenis_ro": "Litere Muqatta'at"}
}

SWEDISH_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {"arti_sv": "Inte / Icke (Ma - allmän nekning)", "desc_sv": "Icke-styrande nekande partikel för dåtid, nutid och nominalsatser", "jenis_sv": "Nekande partikel"},
    "1. Harf Nafyi__2": {"arti_sv": "Inte / Ej (La - verbal nekning)", "desc_sv": "Nekande partikel för nutid och framtid", "jenis_sv": "Nekande partikel"},
    "1. Harf Nafyi__3": {"arti_sv": "Är inte annat än... (In)", "desc_sv": "Nekande partikel i förening med Illa", "jenis_sv": "Nekande partikel"},
    "1. Harf Nafyi__4": {"arti_sv": "Är inte tid för (Lata)", "desc_sv": "Tidsmässig nekande partikel", "jenis_sv": "Tidsnekande partikel"},

    "2. Harf Tahqiq Taswif__5": {"arti_sv": "Sannerligen / Redan (Qad - bekräftelse)", "desc_sv": "Partikel för visshet och eftertryck före dåtida verb", "jenis_sv": "Bekräftelsepartikel"},
    "2. Harf Tahqiq Taswif__6": {"arti_sv": "I framtiden / Senare (Sawfa)", "desc_sv": "Partikel för avlägsen framtid", "jenis_sv": "Framtidspartikel"},
    "2. Harf Tahqiq Taswif__7": {"arti_sv": "Snart / Strax (Sa - nära framtid)", "desc_sv": "Partikel för nära framtid", "jenis_sv": "Framtidspartikel"},

    "3. Harf Syarat__8": {"arti_sv": "Om / Hade (Law - overkligt villkor)", "desc_sv": "Icke-styrande villkorspartikel för ouppfyllda dåtida handlingar", "jenis_sv": "Villkorlig partikel"},
    "3. Harf Syarat__9": {"arti_sv": "Hade det inte varit för... (Lawla)", "desc_sv": "Villkorspartikel för förhinder", "jenis_sv": "Villkorlig partikel"},
    "3. Harf Syarat__10": {"arti_sv": "Vore det inte för... (Lawma)", "desc_sv": "Icke-styrande villkorspartikel", "jenis_sv": "Villkorlig partikel"},
    "3. Harf Syarat__11": {"arti_sv": "Då / Vid den tid då (Lamma)", "desc_sv": "Tidsvillkorspartikel för dåtid", "jenis_sv": "Tidsvillkorspartikel"},
    "3. Harf Syarat__12": {"arti_sv": "Vad beträffar... så (Amma)", "desc_sv": "Utvecklande villkorspartikel med emfatisk tonvikt", "jenis_sv": "Villkorlig partikel"},

    "4. Harf Mashdariyah__13": {"arti_sv": "Att / För att (An - infinitivpartikel)", "desc_sv": "Partikel som omvandlar ett verb till ett verbalsubstantiv", "jenis_sv": "Infinitivpartikel"},
    "4. Harf Mashdariyah__14": {"arti_sv": "Så länge som (Ma mashdariyah)", "desc_sv": "Tidsmässig infinitivpartikel", "jenis_sv": "Infinitivpartikel"},
    "4. Harf Mashdariyah__15": {"arti_sv": "För att / På det att (Kay)", "desc_sv": "Ändamålsenlig infinitivpartikel", "jenis_sv": "Infinitivpartikel"},
    "4. Harf Mashdariyah__16": {"arti_sv": "Om blott / Önskan att (Law)", "desc_sv": "Infinitivpartikel efter önske-verb", "jenis_sv": "Infinitivpartikel"},

    "5. Harf Zaidah__17": {"arti_sv": "För eftertryck (In za'idah)", "desc_sv": "Förstärkande tilläggspartikel", "jenis_sv": "Förstärkande partikel"},
    "5. Harf Zaidah__18": {"arti_sv": "För eftertryck (An za'idah)", "desc_sv": "Förstärkande tilläggspartikel", "jenis_sv": "Förstärkande partikel"},
    "5. Harf Zaidah__19": {"arti_sv": "För eftertryck (Ma za'idah)", "desc_sv": "Förstärkande tilläggspartikel", "jenis_sv": "Förstärkande partikel"},
    "5. Harf Zaidah__20": {"arti_sv": "För eftertryck (La za'idah)", "desc_sv": "Förstärkande tilläggspartikel för nekande", "jenis_sv": "Förstärkande partikel"},

    "6. Harf Istifham__21": {"arti_sv": "Är det så? / Månne? (Hamzah)", "desc_sv": "Grundläggande frågepartikel", "jenis_sv": "Frågepartikel"},
    "6. Harf Istifham__22": {"arti_sv": "Månne? / Huruvida? (Hal)", "desc_sv": "Frågepartikel för ja/nej-bekräftelse", "jenis_sv": "Frågepartikel"},

    "7. Harf Istitsna__23": {"arti_sv": "Utom / Förutom (Illa)", "desc_sv": "Undantagspartikel", "jenis_sv": "Undantagspartikel"},

    "8. Harf Rad'in Wazajrin__24": {"arti_sv": "Ingalunda! / Aldrig i livet! (Kalla)", "desc_sv": "Kategoriskt avvisande och tillrättavisande partikel", "jenis_sv": "Avvisningspartikel"},

    "9. Harf Rad'in Tahdid__25": {"arti_sv": "Varför inte...? (Halla)", "desc_sv": "Uppmanande och tillrättavisande partikel", "jenis_sv": "Uppmaningspartikel"},
    "9. Harf Rad'in Tahdid__26": {"arti_sv": "Varför då inte... (Alla)", "desc_sv": "Uppmanande partikel till skyndsam god handling", "jenis_sv": "Uppmaningspartikel"},

    "10. Harf Ijab__27": {"arti_sv": "Ja / Så är det (Na'am)", "desc_sv": "Bekräftande svarspartikel", "jenis_sv": "Svarspartikel"},
    "10. Harf Ijab__28": {"arti_sv": "Ja, sannerligen! (Bala)", "desc_sv": "Partikel som upphäver nekande och bekräftar sanning", "jenis_sv": "Bekräftelsepartikel"},
    "10. Harf Ijab__29": {"arti_sv": "Ja, vid min Herre! (I)", "desc_sv": "Bekräftelsepartikel vid ed", "jenis_sv": "Edspartikel"},
    "10. Harf Ijab__30": {"arti_sv": "Sannerligen / Visserligen (Ajal)", "desc_sv": "Bekräftelsepartikel", "jenis_sv": "Bekräftelsepartikel"},

    "11. Harf Tafsir__31": {"arti_sv": "Nämligen / Det vill säga (Ay)", "desc_sv": "Förklarande partikel", "jenis_sv": "Förklarande partikel"},
    "11. Harf Tafsir__32": {"arti_sv": "Att / Nämligen (An tafsiriyyah)", "desc_sv": "Förklarande partikel efter talverb", "jenis_sv": "Förklarande partikel"},

    "12. Harf Tanbih__33": {"arti_sv": "Se! / Vet! (Ala)", "desc_sv": "Uppmärksamhetspartikel i meningens början", "jenis_sv": "Uppmärksamhetspartikel"},
    "12. Harf Tanbih__34": {"arti_sv": "Vet sannerligen! (Ama)", "desc_sv": "Uppmärksamhetspartikel", "jenis_sv": "Uppmärksamhetspartikel"},
    "12. Harf Tanbih__35": {"arti_sv": "Se här! (Ha tanbih)", "desc_sv": "Uppmärksamhetsväckande partikel före pronomen", "jenis_sv": "Uppmärksamhetspartikel"},

    "13. Harf Ta'lil__36": {"arti_sv": "För att / Emedan (Lam ta'lil)", "desc_sv": "Orsakspartikel för motivering och syfte", "jenis_sv": "Orsakspartikel"},

    "14. Harf Fuja'iyyah__37": {"arti_sv": "Och plötsligt! / Och se (Idha fuja'iyyah)", "desc_sv": "Partikel som uttrycker en plötslig och oväntad händelse", "jenis_sv": "Överraskningspartikel"},
    "14. Harf Fuja'iyyah__38": {"arti_sv": "Brådstörtat / Plötsligt (Idh fuja'iyyah)", "desc_sv": "Överraskningspartikel", "jenis_sv": "Överraskningspartikel"},

    "15. Harf Istidrak__39": {"arti_sv": "Men / Dock (Lakin)", "desc_sv": "Korrigerande och motstatsbildande partikel", "jenis_sv": "Rättelsepartikel"},
    "15. Harf Istidrak__40": {"arti_sv": "Tvärtom / Ja till och med (Bal)", "desc_sv": "Partikel för ändring av påstående", "jenis_sv": "Rättelsepartikel"},

    "16. Harf Ta'ajjub__41": {"arti_sv": "Hur... ändå! / Hur förunderligt! (Ma)", "desc_sv": "Utropspartikel för beundran och förundran", "jenis_sv": "Beundringspartikel"},

    "17. Harf Mabany__39": {"arti_sv": "Ha-Mim", "desc_sv": "Inledande bokstäver i suror", "jenis_sv": "Muqatta'at bokstäver"},
    "17. Harf Mabany__40": {"arti_sv": "Alif-Lam-Mim", "desc_sv": "Inledande bokstäver i suror", "jenis_sv": "Muqatta'at bokstäver"},
    "17. Harf Mabany__41": {"arti_sv": "Alif-Lam-Ra", "desc_sv": "Inledande bokstäver i suror", "jenis_sv": "Muqatta'at bokstäver"},
    "17. Harf Mabany__42": {"arti_sv": "Ta-Sin-Mim", "desc_sv": "Inledande bokstäver i suror", "jenis_sv": "Muqatta'at bokstäver"},
    "17. Harf Mabany__43": {"arti_sv": "Alif-Lam-Mim-Ra", "desc_sv": "Inledande bokstäver i suror", "jenis_sv": "Muqatta'at bokstäver"},
    "17. Harf Mabany__44": {"arti_sv": "Alif-Lam-Mim-Sad", "desc_sv": "Inledande bokstäver i suror", "jenis_sv": "Muqatta'at bokstäver"},
    "17. Harf Mabany__45": {"arti_sv": "Sad", "desc_sv": "Inledande bokstäver i suror", "jenis_sv": "Muqatta'at bokstäver"},
    "17. Harf Mabany__46": {"arti_sv": "Ta-Sin", "desc_sv": "Inledande bokstäver i suror", "jenis_sv": "Muqatta'at bokstäver"},
    "17. Harf Mabany__47": {"arti_sv": "Ta-Ha", "desc_sv": "Inledande bokstäver i suror", "jenis_sv": "Muqatta'at bokstäver"},
    "17. Harf Mabany__48": {"arti_sv": "Ayn-Sin-Qaf", "desc_sv": "Inledande bokstäver i suror", "jenis_sv": "Muqatta'at bokstäver"},
    "17. Harf Mabany__49": {"arti_sv": "Qaf", "desc_sv": "Inledande bokstäver i suror", "jenis_sv": "Muqatta'at bokstäver"},
    "17. Harf Mabany__50": {"arti_sv": "Kaf-Ha-Ya-Ayn-Sad", "desc_sv": "Inledande bokstäver i suror", "jenis_sv": "Muqatta'at bokstäver"},
    "17. Harf Mabany__51": {"arti_sv": "Nun", "desc_sv": "Inledande bokstäver i suror", "jenis_sv": "Muqatta'at bokstäver"},
    "17. Harf Mabany__52": {"arti_sv": "Ya-Sin", "desc_sv": "Inledande bokstäver i suror", "jenis_sv": "Muqatta'at bokstäver"}
}


def enrich_dhamir_data():
    print("Enriching dhamir_data.json and dhamir_data.js with Romanian & Swedish...")
    with open(os.path.join(BASE_DIR, 'ro_translations.json'), 'r', encoding='utf-8') as f:
        ro_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'sv_translations.json'), 'r', encoding='utf-8') as f:
        sv_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = str(item.get('No kata', ''))
        g_key = f"{b}__{nk}"
        s_num = str(item.get('SURAT', ''))
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"

        # RO
        item['BentukKataRO'] = BENTUK_KATA_RO.get(b, b)
        item['SuratArtiRO'] = ROMANIAN_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_ro = ROMANIAN_GRAMMAR.get(g_key, {})
        item['ArtiKataRO'] = g_ro.get('arti_ro', item.get('ArtiKataEN', ''))
        item['TeksArtiRO'] = ro_trans.get(v_key, item.get('TeksArtiEN', ''))

        # SV
        item['BentukKataSV'] = BENTUK_KATA_SV.get(b, b)
        item['SuratArtiSV'] = SWEDISH_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_sv = SWEDISH_GRAMMAR.get(g_key, {})
        item['ArtiKataSV'] = g_sv.get('arti_sv', item.get('ArtiKataEN', ''))
        item['TeksArtiSV'] = sv_trans.get(v_key, item.get('TeksArtiEN', ''))

        # Grammar dict
        if 'Grammar' not in item or not isinstance(item['Grammar'], dict):
            item['Grammar'] = {}
        if g_ro.get('arti_ro'): item['Grammar']['arti_ro'] = g_ro['arti_ro']
        if g_ro.get('desc_ro'): item['Grammar']['desc_ro'] = g_ro['desc_ro']
        if g_ro.get('jenis_ro'): item['Grammar']['jenis_ro'] = g_ro['jenis_ro']

        if g_sv.get('arti_sv'): item['Grammar']['arti_sv'] = g_sv['arti_sv']
        if g_sv.get('desc_sv'): item['Grammar']['desc_sv'] = g_sv['desc_sv']
        if g_sv.get('jenis_sv'): item['Grammar']['jenis_sv'] = g_sv['jenis_sv']

    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    js_content = f"/**\n * Dataset Dhamir & Isim Jamid Mabny Al-Qur'an 33 Bahasa\n */\nconst DHAMIR_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
    with open(os.path.join(BASE_DIR, 'dhamir_data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"  [OK] Dhamir data enriched ({len(data)} rows).")


def enrich_harf_data():
    print("Enriching harf_data.json and harf_data.js with Romanian & Swedish...")
    with open(os.path.join(BASE_DIR, 'ro_translations.json'), 'r', encoding='utf-8') as f:
        ro_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'sv_translations.json'), 'r', encoding='utf-8') as f:
        sv_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = str(item.get('No kata', ''))
        g_key = f"{b}__{nk}"
        s_num = str(item.get('SURAT', ''))
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"

        # RO
        item['BentukKataRO'] = BENTUK_HARF_RO.get(b, b)
        item['SuratArtiRO'] = ROMANIAN_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_ro = ROMANIAN_HARF_GRAMMAR.get(g_key, {})
        item['ArtiKataRO'] = g_ro.get('arti_ro', item.get('ArtiKataEN', ''))
        item['TeksArtiRO'] = ro_trans.get(v_key, item.get('TeksArtiEN', ''))

        # SV
        item['BentukKataSV'] = BENTUK_HARF_SV.get(b, b)
        item['SuratArtiSV'] = SWEDISH_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_sv = SWEDISH_HARF_GRAMMAR.get(g_key, {})
        item['ArtiKataSV'] = g_sv.get('arti_sv', item.get('ArtiKataEN', ''))
        item['TeksArtiSV'] = sv_trans.get(v_key, item.get('TeksArtiEN', ''))

        # Grammar dict
        if 'Grammar' not in item or not isinstance(item['Grammar'], dict):
            item['Grammar'] = {}
        if g_ro.get('arti_ro'): item['Grammar']['arti_ro'] = g_ro['arti_ro']
        if g_ro.get('desc_ro'): item['Grammar']['desc_ro'] = g_ro['desc_ro']
        if g_ro.get('jenis_ro'): item['Grammar']['jenis_ro'] = g_ro['jenis_ro']

        if g_sv.get('arti_sv'): item['Grammar']['arti_sv'] = g_sv['arti_sv']
        if g_sv.get('desc_sv'): item['Grammar']['desc_sv'] = g_sv['desc_sv']
        if g_sv.get('jenis_sv'): item['Grammar']['jenis_sv'] = g_sv['jenis_sv']

    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    js_content = f"/**\n * Dataset Harf Ghair 'Amil Al-Qur'an 33 Bahasa\n */\nconst HARF_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
    with open(os.path.join(BASE_DIR, 'harf_data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"  [OK] Harf data enriched ({len(data)} rows).")


if __name__ == '__main__':
    enrich_dhamir_data()
    enrich_harf_data()
