#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Norwegian (no) and Polish (pl) Dataset Metadata & Enricher:
- 114 Surah Names for Norwegian & Polish
- 7 Bentuk Kata Categories for Norwegian & Polish
- 76 Jamid Mabny Grammar details for Norwegian & Polish
- 17 Bentuk Harf Categories for Norwegian & Polish
- 52 Harf Grammar details for Norwegian & Polish
"""

import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

NORWEGIAN_SURAHS = {
    "1": "Al-Fatiha (Åpningen)",
    "2": "Al-Baqarah (Kua)",
    "3": "Al-Imran (Imrans familie)",
    "4": "An-Nisa (Kvinnene)",
    "5": "Al-Ma'idah (Bordet)",
    "6": "Al-An'am (Kveget)",
    "7": "Al-A'raf (Høydene)",
    "8": "Al-Anfal (Krigsbyttet)",
    "9": "At-Tawbah (Angeren)",
    "10": "Yunus (Jonas)",
    "11": "Hud (Hud)",
    "12": "Yusuf (Josef)",
    "13": "Ar-Ra'd (Tordenen)",
    "14": "Ibrahim (Abraham)",
    "15": "Al-Hijr (Steinvidden)",
    "16": "An-Nahl (Biene)",
    "17": "Al-Isra (Nattreisen)",
    "18": "Al-Kahf (Hulen)",
    "19": "Maryam (Maria)",
    "20": "Ta-Ha (Ta-Ha)",
    "21": "Al-Anbiya (Profetene)",
    "22": "Al-Hajj (Pilegrimsferden)",
    "23": "Al-Mu'minun (De troende)",
    "24": "An-Nur (Lyset)",
    "25": "Al-Furqan (Kriteriet)",
    "26": "Ash-Shu'ara (Skaldene)",
    "27": "An-Naml (Maurene)",
    "28": "Al-Qasas (Fortellingen)",
    "29": "Al-Ankabut (Edderkoppen)",
    "30": "Ar-Rum (Romerne)",
    "31": "Luqman (Luqman)",
    "32": "As-Sajdah (Nedkastelsen)",
    "33": "Al-Ahzab (Forbundsfellene)",
    "34": "Saba (Saba)",
    "35": "Fatir (Skaperen)",
    "36": "Ya-Sin (Ya-Sin)",
    "37": "As-Saffat (I rad og rekke)",
    "38": "Sad (Sad)",
    "39": "Az-Zumar (Skarer)",
    "40": "Ghafir (Tilgiveren)",
    "41": "Fussilat (Klart fremsatt)",
    "42": "Ash-Shura (Rådslaget)",
    "43": "Az-Zukhruf (Gullpryd)",
    "44": "Ad-Dukhan (Røyken)",
    "45": "Al-Jathiyah (Knelende)",
    "46": "Al-Ahqaf (Sanddynene)",
    "47": "Muhammad (Muhammad)",
    "48": "Al-Fath (Seieren)",
    "49": "Al-Hujurat (Rommene)",
    "50": "Qaf (Qaf)",
    "51": "Adh-Dhariyat (Vindene)",
    "52": "At-Tur (Fjellet)",
    "53": "An-Najm (Stjernen)",
    "54": "Al-Qamar (Månen)",
    "55": "Ar-Rahman (Den Barmhjertige)",
    "56": "Al-Waqi'ah (Begivenheten)",
    "57": "Al-Hadid (Jernet)",
    "58": "Al-Mujadilah (Kvinnen som trettet)",
    "59": "Al-Hashr (Fordrivelsen)",
    "60": "Al-Mumtahanah (Kvinnen som prøves)",
    "61": "As-Saff (Rekkene)",
    "62": "Al-Jumu'ah (Fredagen)",
    "63": "Al-Munafiqun (Hyklerne)",
    "64": "At-Taghabun (Gjensidig skuffelse)",
    "65": "At-Talaq (Skilsmissen)",
    "66": "At-Tahrim (Forbudet)",
    "67": "Al-Mulk (Herredømmet)",
    "68": "Al-Qalam (Pennen)",
    "69": "Al-Haqqah (Den uunngåelige)",
    "70": "Al-Ma'arij (Stigene)",
    "71": "Nuh (Noa)",
    "72": "Al-Jinn (Jinnene)",
    "73": "Al-Muzzammil (Den innhyllede)",
    "74": "Al-Muddaththir (Den svøpte)",
    "75": "Al-Qiyamah (Oppstandelsen)",
    "76": "Al-Insan (Mennesket)",
    "77": "Al-Mursalat (De utsendte)",
    "78": "An-Naba (Budskapet)",
    "79": "An-Nazi'at (De som rykker ut)",
    "80": "Abasa (Han rynket pannen)",
    "81": "At-Takwir (Sammenslyngingen)",
    "82": "Al-Infitar (Kløvingen)",
    "83": "Al-Mutaffifin (Svindlerne)",
    "84": "Al-Inshiqaq (Bristen)",
    "85": "Al-Buruj (Stjernebildene)",
    "86": "At-Tariq (Nattens gjest)",
    "87": "Al-A'la (Den Høyeste)",
    "88": "Al-Ghashiyah (Den overveldende)",
    "89": "Al-Fajr (Morgengryet)",
    "90": "Al-Balad (Byen)",
    "91": "Ash-Shams (Solen)",
    "92": "Al-Layl (Natten)",
    "93": "Ad-Duha (Morgentimene)",
    "94": "Ash-Sharh (Utvidelsen)",
    "95": "At-Tin (Fikentreet)",
    "96": "Al-Alaq (Klumpen)",
    "97": "Al-Qadr (Skjebnenatten)",
    "98": "Al-Bayyinah (Det klare bevis)",
    "99": "Az-Zalzalah (Jordskjelvet)",
    "100": "Al-Adiyat (De stormende hestene)",
    "101": "Al-Qari'ah (Ulykken)",
    "102": "At-Takathur (Kappløpet om mer)",
    "103": "Al-Asr (Ettermiddagen)",
    "104": "Al-Humazah (Baktaleren)",
    "105": "Al-Fil (Elefanten)",
    "106": "Quraysh (Quraysh)",
    "107": "Al-Ma'un (Hjelpen)",
    "108": "Al-Kawthar (Overfloden)",
    "109": "Al-Kafirun (De vantro)",
    "110": "An-Nasr (Hjelpen)",
    "111": "Al-Masad (Bastfibrene)",
    "112": "Al-Ikhlas (Den rene tro)",
    "113": "Al-Falaq (Morgendemringen)",
    "114": "An-Nas (Menneskene)"
}

POLISH_SURAHS = {
    "1": "Al-Fatiha (Otwierająca)",
    "2": "Al-Bakara (Krowa)",
    "3": "Al-Imran (Rodzina Imrana)",
    "4": "An-Nisa (Kobiety)",
    "5": "Al-Ma'ida (Stół Zastawiony)",
    "6": "Al-An'am (Trzody)",
    "7": "Al-A'raf (Wzniesienia)",
    "8": "Al-Anfal (Łupy)",
    "9": "At-Tawba (Skrucha)",
    "10": "Junus (Jonasz)",
    "11": "Hud (Hud)",
    "12": "Jusuf (Józef)",
    "13": "Ar-Ra'd (Grzmot)",
    "14": "Ibrahim (Abraham)",
    "15": "Al-Hidżr (Skalna Dolina)",
    "16": "An-Nahl (Pszczoły)",
    "17": "Al-Isra (Podróż Nocna)",
    "18": "Al-Kahf (Grota)",
    "19": "Marjam (Maria)",
    "20": "Ta-Ha (Ta-Ha)",
    "21": "Al-Anbija (Prorocy)",
    "22": "Al-Hadżdż (Pielgrzymka)",
    "23": "Al-Mu'minun (Wierni)",
    "24": "An-Nur (Światło)",
    "25": "Al-Furkan (Kryterium)",
    "26": "Asz-Szu'ara (Poeci)",
    "27": "An-Naml (Mrówki)",
    "28": "Al-Kasas (Opowiadanie)",
    "29": "Al-Ankabut (Pająk)",
    "30": "Ar-Rum (Bizantyjczycy)",
    "31": "Lukman (Lukman)",
    "32": "As-Sadżda (Pokłon)",
    "33": "Al-Ahzab (Wspólnicy)",
    "34": "Saba (Saba)",
    "35": "Fatir (Stwórca)",
    "36": "Ja-Sin (Ja-Sin)",
    "37": "As-Saffat (Stojący w szeregach)",
    "38": "Sad (Sad)",
    "39": "Az-Zumar (Tłumy)",
    "40": "Ghafir (Przebaczający)",
    "41": "Fussilat (Wyjaśnione)",
    "42": "Asz-Szura (Narada)",
    "43": "Az-Zuchruf (Złote ozdoby)",
    "44": "Ad-Duchan (Dym)",
    "45": "Al-Dżathija (Klęcząca)",
    "46": "Al-Ahkaf (Wydmy)",
    "47": "Muhammad (Muhammad)",
    "48": "Al-Fath (Zwycięstwo)",
    "49": "Al-Hudżurat (Komnaty)",
    "50": "Kaf (Kaf)",
    "51": "Adh-Dharijat (Wiatry rozsiewające)",
    "52": "At-Tur (Góra)",
    "53": "An-Nadżm (Gwiazda)",
    "54": "Al-Kamar (Księżyc)",
    "55": "Ar-Rahman (Miłosierny)",
    "56": "Al-Waki'a (Wydarzenie)",
    "57": "Al-Hadid (Żelazo)",
    "58": "Al-Mudżadala (Spierająca się)",
    "59": "Al-Haszr (Zgromadzenie)",
    "60": "Al-Mumtahana (Próbowana)",
    "61": "As-Saff (Szeregi)",
    "62": "Al-Dżumu'a (Piątek)",
    "63": "Al-Munafikun (Hipokryci)",
    "64": "At-Taghabun (Wzajemne oszukiwanie)",
    "65": "At-Talak (Rozwód)",
    "66": "At-Tahrim (Zakaz)",
    "67": "Al-Mulk (Królestwo)",
    "68": "Al-Kalam (Pióro)",
    "69": "Al-Hakka (Niewątpliwa)",
    "70": "Al-Ma'aridż (Stopnie)",
    "71": "Nuh (Noe)",
    "72": "Al-Dżinn (Dżinny)",
    "73": "Al-Muzzammil (Okryty szatą)",
    "74": "Al-Muddaththir (Okryty płaszczem)",
    "75": "Al-Kijama (Zmartwychwstanie)",
    "76": "Al-Insan (Człowiek)",
    "77": "Al-Mursalat (Wysyłane)",
    "78": "An-Naba (Wieść)",
    "79": "An-Nazi'at (Wyrywający)",
    "80": "Abasa (Zachmurzył się)",
    "81": "At-Takwir (Skręcenie)",
    "82": "Al-Infitar (Rozdarcie)",
    "83": "Al-Mutaffifin (Oszukujący przy mierzeniu)",
    "84": "Al-Inszikak (Rozłamanie)",
    "85": "Al-Burudż (Konstelacje)",
    "86": "At-Tarik (Gwiazda nocna)",
    "87": "Al-A'la (Najwyższy)",
    "88": "Al-Ghaszija (Okrywająca)",
    "89": "Al-Fadżr (Jutrzenka)",
    "90": "Al-Balad (Miasto)",
    "91": "Asz-Szams (Słońce)",
    "92": "Al-Lajl (Noc)",
    "93": "Ad-Duha (Jasność poranka)",
    "94": "Asz-Szarh (Otwarcie)",
    "95": "At-Tin (Drzewo figowe)",
    "96": "Al-Alak (Grudka krwi)",
    "97": "Al-Kadr (Przeznaczenie)",
    "98": "Al-Bajjina (Jasny dowód)",
    "99": "Az-Zalzala (Trzęsienie ziemi)",
    "100": "Al-Adijat (Pędzące rumaki)",
    "101": "Al-Kari'a (Uderzenie)",
    "102": "At-Takathur (Współzawodnictwo o bogactwo)",
    "103": "Al-Asr (Pora popołudniowa)",
    "104": "Al-Humaza (Oszczerca)",
    "105": "Al-Fil (Słoń)",
    "106": "Kurajsz (Korejszyci)",
    "107": "Al-Ma'un (Wsparcie)",
    "108": "Al-Kauthar (Obfitość)",
    "109": "Al-Kafirun (Niewierni)",
    "110": "An-Nasr (Pomoc)",
    "111": "Al-Masad (Włókna palmowe)",
    "112": "Al-Ichlas (Szczerość wiary)",
    "113": "Al-Falak (Świt)",
    "114": "An-Nas (Ludzie)"
}

BENTUK_KATA_NO = {
    "1. Dhamir": "1. Pronomen (Dhamir / Pronomen)",
    "2. Isim Mawshul": "2. Relativpronomen (Ism Mawshul)",
    "3. Isim Istifham": "3. Spørrepronomen (Ism Istifham)",
    "4. Isim Syarath": "4. Betingelsesord (Ism Syarath)",
    "5. Isim Isyarah": "5. Påpekende pronomen (Ism Isyarah)",
    "6. Isim Fi'il": "6. Verbale substantiv (Ism Fi'il)",
    "7. Fi'il Jamid": "7. Uforanderlige verb (Fi'il Jamid)"
}

BENTUK_KATA_PL = {
    "1. Dhamir": "1. Zaimki osobowe (Dhamir / Zaimki)",
    "2. Isim Mawshul": "2. Zaimki względne (Ism Mawshul)",
    "3. Isim Istifham": "3. Zaimki pytające (Ism Istifham)",
    "4. Isim Syarath": "4. Zaimki warunkowe (Ism Syarath)",
    "5. Isim Isyarah": "5. Zaimki wskazujące (Ism Isyarah)",
    "6. Isim Fi'il": "6. Rzeczowniki czasownikowe (Ism Fi'il)",
    "7. Fi'il Jamid": "7. Czasowniki nieodmienne (Fi'il Jamid)"
}

BENTUK_HARF_NO = {
    "1. Harf Nafyi": "1. Nektelsespartikler (Harf Nafyi)",
    "2. Harf Tahqiq Taswif": "2. Bekreftelses- og fremtidspartikler (Tahqiq & Taswif)",
    "3. Harf Syarat": "3. Betingelsespartikler (Harf Syarat)",
    "4. Harf Mashdariyah": "4. Infinitivpartikler (Harf Mashdariyah)",
    "5. Harf Zaidah": "5. Forsterkende tilleggspartikler (Harf Zaidah)",
    "6. Harf Istifham": "6. Spørrepartikler (Harf Istifham)",
    "7. Harf Istitsna": "7. Unntakspartikler (Harf Istitsna)",
    "8. Harf Rad'in Wazajrin": "8. Avvisnings- og irettesettelsespartikler (Harf Rad'in)",
    "9. Harf Rad'in Tahdid": "9. Oppfordringspartikler (Harf Tahdid)",
    "10. Harf Ijab": "10. Svar- og bekreftelsespartikler (Harf Ijab)",
    "11. Harf Tafsir": "11. Forklarende partikler (Harf Tafsir)",
    "12. Harf Tanbih": "12. Oppmerksomhetspartikler (Harf Tanbih)",
    "13. Harf Ta'lil": "13. Årsakspartikler (Harf Ta'lil)",
    "14. Harf Fuja'iyyah": "14. Overraskelsespartikler (Harf Fuja'iyyah)",
    "15. Harf Istidrak": "15. Korreksjonspartikler (Harf Istidrak)",
    "16. Harf Ta'ajjub": "16. Beundringspartikler (Harf Ta'ajjub)",
    "17. Harf Mabany": "17. Åpningsbokstaver i surer (Muqatta'at)"
}

BENTUK_HARF_PL = {
    "1. Harf Nafyi": "1. Partykuły przeczące (Harf Nafyi)",
    "2. Harf Tahqiq Taswif": "2. Partykuły potwierdzenia i przyszłości (Tahqiq & Taswif)",
    "3. Harf Syarat": "3. Partykuły warunkowe (Harf Syarat)",
    "4. Harf Mashdariyah": "4. Partykuły bezokolicznikowe (Harf Mashdariyah)",
    "5. Harf Zaidah": "5. Partykuły wzmacniające (Harf Zaidah)",
    "6. Harf Istifham": "6. Partykuły pytające (Harf Istifham)",
    "7. Harf Istitsna": "7. Partykuły wyłączające (Harf Istitsna)",
    "8. Harf Rad'in Wazajrin": "8. Partykuły nagany i zakazu (Harf Rad'in)",
    "9. Harf Rad'in Tahdid": "9. Partykuły zachęty i upomnienia (Harf Tahdid)",
    "10. Harf Ijab": "10. Partykuły twierdzące i odpowiedzi (Harf Ijab)",
    "11. Harf Tafsir": "11. Partykuły objaśniające (Harf Tafsir)",
    "12. Harf Tanbih": "12. Partykuły zwracające uwagę (Harf Tanbih)",
    "13. Harf Ta'lil": "13. Partykuły przyczynowe (Harf Ta'lil)",
    "14. Harf Fuja'iyyah": "14. Partykuły nagłości (Harf Fuja'iyyah)",
    "15. Harf Istidrak": "15. Partykuły przeciwstawne i sprostowania (Harf Istidrak)",
    "16. Harf Ta'ajjub": "16. Partykuły podziwu i zachwytu (Harf Ta'ajjub)",
    "17. Harf Mabany": "17. Litery tajemnicze na początku sur (Muqatta'at)"
}

NORWEGIAN_GRAMMAR = {
    "1. Dhamir__1a": {"arti_no": "Han (3. pers. entall maskulin)", "desc_no": "Selvstendig personlig pronomen 3. pers. entall maskulin (Munfasil)", "jenis_no": "Selvstendig pronomen"},
    "1. Dhamir__1b": {"arti_no": "Hans / Ham (Tilknyttet)", "desc_no": "Tilknyttet pronomen 3. pers. entall maskulin (Muttasil)", "jenis_no": "Tilknyttet pronomen"},
    "1. Dhamir__1c": {"arti_no": "Bare Ham (Akkusativ)", "desc_no": "Selvstendig akkusativpronomen 3. pers. entall", "jenis_no": "Akkusativpronomen"},
    "1. Dhamir__2a": {"arti_no": "De to (Dualis)", "desc_no": "Selvstendig dualispronomen", "jenis_no": "Dualispronomen"},
    "1. Dhamir__2b": {"arti_no": "Deres to (Tilknyttet)", "desc_no": "Tilknyttet dualispronomen", "jenis_no": "Tilknyttet dualispronomen"},
    "1. Dhamir__3a": {"arti_no": "De (Flertall maskulin)", "desc_no": "Selvstendig pronomen 3. pers. flertall maskulin", "jenis_no": "Selvstendig pronomen"},
    "1. Dhamir__3b": {"arti_no": "Deres / Dem (Tilknyttet)", "desc_no": "Tilknyttet pronomen 3. pers. flertall maskulin", "jenis_no": "Tilknyttet pronomen"},
    "1. Dhamir__3c": {"arti_no": "Bare dem", "desc_no": "Selvstendig akkusativpronomen 3. pers. flertall maskulin", "jenis_no": "Akkusativpronomen"},
    "1. Dhamir__4a": {"arti_no": "Hun (3. pers. entall feminin)", "desc_no": "Selvstendig pronomen 3. pers. entall feminin", "jenis_no": "Selvstendig pronomen"},
    "1. Dhamir__4b": {"arti_no": "Hennes / Henne (Tilknyttet)", "desc_no": "Tilknyttet pronomen 3. pers. entall feminin", "jenis_no": "Tilknyttet pronomen"},
    "1. Dhamir__5a": {"arti_no": "De (Flertall feminin)", "desc_no": "Selvstendig pronomen 3. pers. flertall feminin", "jenis_no": "Selvstendig pronomen"},
    "1. Dhamir__5b": {"arti_no": "Deres (Feminin tilknyttet)", "desc_no": "Tilknyttet pronomen 3. pers. flertall feminin", "jenis_no": "Tilknyttet pronomen"},
    "1. Dhamir__6a": {"arti_no": "Du (2. pers. entall maskulin)", "desc_no": "Selvstendig pronomen 2. pers. entall maskulin", "jenis_no": "Selvstendig pronomen"},
    "1. Dhamir__6b": {"arti_no": "Din / Deg (Tilknyttet)", "desc_no": "Tilknyttet pronomen 2. pers. entall maskulin", "jenis_no": "Tilknyttet pronomen"},
    "1. Dhamir__6c": {"arti_no": "Bare Deg (Dedikasjon av tilbedelse)", "desc_no": "Selvstendig akkusativpronomen 2. pers. entall", "jenis_no": "Akkusativpronomen"},
    "1. Dhamir__7a": {"arti_no": "Dere to", "desc_no": "Selvstendig pronomen 2. pers. dualis", "jenis_no": "Dualispronomen"},
    "1. Dhamir__7b": {"arti_no": "Deres to (Tilknyttet)", "desc_no": "Tilknyttet pronomen 2. pers. dualis", "jenis_no": "Tilknyttet dualispronomen"},
    "1. Dhamir__8a": {"arti_no": "Dere (Flertall maskulin)", "desc_no": "Selvstendig pronomen 2. pers. flertall maskulin", "jenis_no": "Selvstendig pronomen"},
    "1. Dhamir__8b": {"arti_no": "Deres / Dere (Tilknyttet)", "desc_no": "Tilknyttet pronomen 2. pers. flertall maskulin", "jenis_no": "Tilknyttet pronomen"},
    "1. Dhamir__8c": {"arti_no": "Bare dere", "desc_no": "Selvstendig akkusativpronomen 2. pers. flertall maskulin", "jenis_no": "Akkusativpronomen"},
    "1. Dhamir__9a": {"arti_no": "Du (2. pers. entall feminin)", "desc_no": "Selvstendig pronomen 2. pers. entall feminin", "jenis_no": "Selvstendig pronomen"},
    "1. Dhamir__9b": {"arti_no": "Din / Deg (Feminin tilknyttet)", "desc_no": "Tilknyttet pronomen 2. pers. entall feminin", "jenis_no": "Tilknyttet pronomen"},
    "1. Dhamir__10a": {"arti_no": "Dere (Flertall feminin)", "desc_no": "Selvstendig pronomen 2. pers. flertall feminin", "jenis_no": "Selvstendig pronomen"},
    "1. Dhamir__10b": {"arti_no": "Deres (Feminin tilknyttet)", "desc_no": "Tilknyttet pronomen 2. pers. flertall feminin", "jenis_no": "Tilknyttet pronomen"},
    "1. Dhamir__11a": {"arti_no": "Jeg (1. pers. entall)", "desc_no": "Selvstendig pronomen 1. pers. entall", "jenis_no": "Selvstendig pronomen"},
    "1. Dhamir__11b": {"arti_no": "Min / Meg (Tilknyttet)", "desc_no": "Tilknyttet pronomen 1. pers. entall", "jenis_no": "Tilknyttet pronomen"},
    "1. Dhamir__11c": {"arti_no": "Bare meg", "desc_no": "Selvstendig akkusativpronomen 1. pers. entall", "jenis_no": "Akkusativpronomen"},
    "1. Dhamir__12a": {"arti_no": "Vi (1. pers. flertall)", "desc_no": "Selvstendig pronomen 1. pers. flertall", "jenis_no": "Selvstendig pronomen"},
    "1. Dhamir__12b": {"arti_no": "Vår / Oss (Tilknyttet)", "desc_no": "Tilknyttet pronomen 1. pers. flertall", "jenis_no": "Tilknyttet pronomen"},
    "1. Dhamir__12c": {"arti_no": "Bare oss", "desc_no": "Selvstendig akkusativpronomen 1. pers. flertall", "jenis_no": "Akkusativpronomen"},

    "2. Isim Mawshul__1": {"arti_no": "Det som / Alt hva (Ubesjelede ting)", "desc_no": "Generelt relativpronomen for ubesjelede ting", "jenis_no": "Generelt relativpronomen"},
    "2. Isim Mawshul__2": {"arti_no": "De som (Flertall maskulin)", "desc_no": "Relativpronomen for fornuftige vesener i flertall", "jenis_no": "Spesifikt relativpronomen"},
    "2. Isim Mawshul__3": {"arti_no": "Den som / Hvem som (Personer)", "desc_no": "Generelt relativpronomen for personer og fornuftige vesener", "jenis_no": "Generelt relativpronomen"},
    "2. Isim Mawshul__4": {"arti_no": "Han som / Den som (Entall maskulin)", "desc_no": "Relativpronomen for maskulin entall", "jenis_no": "Spesifikt relativpronomen"},
    "2. Isim Mawshul__5": {"arti_no": "Hvilken som helst / Enhver", "desc_no": "Genitivisk relativpronomen", "jenis_no": "Relativpronomen"},
    "2. Isim Mawshul__6": {"arti_no": "Hun som / Den som (Entall feminin)", "desc_no": "Relativpronomen for feminin entall", "jenis_no": "Spesifikt relativpronomen"},
    "2. Isim Mawshul__7": {"arti_no": "De kvinner som (Flertall)", "desc_no": "Relativpronomen for kvinner i flertall", "jenis_no": "Feminin relativpronomen"},
    "2. Isim Mawshul__8": {"arti_no": "De kvinner som (Flertall)", "desc_no": "Relativpronomen for kvinner i flertall", "jenis_no": "Feminin relativpronomen"},
    "2. Isim Mawshul__9": {"arti_no": "De to som", "desc_no": "Dualis relativpronomen", "jenis_no": "Dualis relativpronomen"},
    "2. Isim Mawshul__10": {"arti_no": "Hvilken kvinne som helst", "desc_no": "Feminin relativpronomen", "jenis_no": "Relativpronomen"},

    "3. Isim Istifham__1": {"arti_no": "Hva? / Hva er dette?", "desc_no": "Spørrepronomen for ting", "jenis_no": "Spørrepronomen"},
    "3. Isim Istifham__2": {"arti_no": "Hvem? / Hvem er?", "desc_no": "Spørrepronomen for personer", "jenis_no": "Spørrepronomen"},
    "3. Isim Istifham__3": {"arti_no": "Hvordan? / På hvilken måte?", "desc_no": "Spørrepronomen for tilstand", "jenis_no": "Tilstandsspørrepronomen"},
    "3. Isim Istifham__4": {"arti_no": "Hvor? / Hvorhen?", "desc_no": "Spørrepronomen for sted", "jenis_no": "Stedsspørrepronomen"},
    "3. Isim Istifham__5": {"arti_no": "Hvor mange? / Hvor mye?", "desc_no": "Spørrepronomen for antall", "jenis_no": "Mengdespørrepronomen"},
    "3. Isim Istifham__6": {"arti_no": "Når? / Til hvilken tid?", "desc_no": "Spørrepronomen for tid", "jenis_no": "Tidsspørrepronomen"},
    "3. Isim Istifham__7": {"arti_no": "Når inntreffer det? (Oppstandelsens dag)", "desc_no": "Spørrepronomen for store fremtidige hendelser", "jenis_no": "Tidsspørrepronomen"},
    "3. Isim Istifham__8": {"arti_no": "Hvorfra? / Hvordan?", "desc_no": "Spørrepronomen for opprinnelse eller årsak", "jenis_no": "Spørrepronomen"},

    "4. Isim Syarath__1": {"arti_no": "Hvem som helst / Den som", "desc_no": "Betingelsespronomen for personer som krever jussiv", "jenis_no": "Betingelsespronomen"},
    "4. Isim Syarath__2": {"arti_no": "Hva som helst / Hva dere enn gjør", "desc_no": "Betingelsespronomen for ting", "jenis_no": "Betingelsespronomen"},
    "4. Isim Syarath__3": {"arti_no": "Når / I det øyeblikk", "desc_no": "Tidsbetingelsesord for fremtiden", "jenis_no": "Tidsbetingelsesord"},
    "4. Isim Syarath__4": {"arti_no": "Uansett hva", "desc_no": "Generelt betingelsespronomen", "jenis_no": "Betingelsespronomen"},
    "4. Isim Syarath__5": {"arti_no": "Hvor som helst / Hvorhen", "desc_no": "Stedsbetingelsesord", "jenis_no": "Stedsbetingelsesord"},
    "4. Isim Syarath__6": {"arti_no": "Hvor dere enn befinner dere", "desc_no": "Forsterket stedsbetingelsesord", "jenis_no": "Stedsbetingelsesord"},
    "4. Isim Syarath__7": {"arti_no": "I hvilken som helst tilstand", "desc_no": "Tilstandsbetingelsesord", "jenis_no": "Tilstandsbetingelsesord"},
    "4. Isim Syarath__8": {"arti_no": "Hvilken som helst", "desc_no": "Genitivisk betingelsesord", "jenis_no": "Betingelsesord"},

    "5. Isim Isyarah__1": {"arti_no": "Den / Boken der (Fjern maskulin)", "desc_no": "Påpekende pronomen for fjerne objekter maskulin", "jenis_no": "Fjernt påpekende pronomen"},
    "5. Isim Isyarah__2": {"arti_no": "Denne / Dette (Nær maskulin)", "desc_no": "Påpekende pronomen for nære objekter maskulin", "jenis_no": "Nært påpekende pronomen"},
    "5. Isim Isyarah__3": {"arti_no": "Disse (Nær flertall)", "desc_no": "Påpekende pronomen for nært flertall", "jenis_no": "Nært påpekende pronomen"},
    "5. Isim Isyarah__4": {"arti_no": "De der / Hine (Fjern flertall)", "desc_no": "Påpekende pronomen for fjernt flertall", "jenis_no": "Fjernt påpekende pronomen"},
    "5. Isim Isyarah__5": {"arti_no": "Denne (Nær feminin)", "desc_no": "Påpekende pronomen for nært feminin entall", "jenis_no": "Nært påpekende pronomen"},
    "5. Isim Isyarah__6": {"arti_no": "Den der (Fjern feminin)", "desc_no": "Påpekende pronomen for fjernt feminin entall", "jenis_no": "Fjernt påpekende pronomen"},
    "5. Isim Isyarah__7": {"arti_no": "Der / På det stedet", "desc_no": "Påpekende pronomen for fjernt sted", "jenis_no": "Stedspåpekende pronomen"},
    "5. Isim Isyarah__8": {"arti_no": "Her / På dette stedet", "desc_no": "Påpekende pronomen for nært sted", "jenis_no": "Stedspåpekende pronomen"},
    "5. Isim Isyarah__9": {"arti_no": "Disse to ting (Fjern maskulin)", "desc_no": "Dualis påpekende pronomen", "jenis_no": "Dualis påpekende pronomen"},
    "5. Isim Isyarah__10": {"arti_no": "Disse to ting (Fjern feminin)", "desc_no": "Dualis påpekende pronomen", "jenis_no": "Dualis påpekende pronomen"},

    "6. Isim Fi'il__1": {"arti_no": "Hvor fjernt er det ikke! (Hayhata)", "desc_no": "Verbalt substantiv i fortid", "jenis_no": "Fortidig verbalt substantiv"},
    "6. Isim Fi'il__2": {"arti_no": "Uff! / Tvi! (Uff)", "desc_no": "Verbalt substantiv for misnøye i nåtid", "jenis_no": "Nåtidig verbalt substantiv"},
    "6. Isim Fi'il__3": {"arti_no": "Kom hit! / Bring frem!", "desc_no": "Bydende verbalt substantiv", "jenis_no": "Imperativt verbalt substantiv"},
    "6. Isim Fi'il__4": {"arti_no": "Ta! / Les!", "desc_no": "Bydende verbalt substantiv", "jenis_no": "Imperativt verbalt substantiv"},
    "6. Isim Fi'il__5": {"arti_no": "Pass på! / Hold fast ved!", "desc_no": "Bydende verbalt substantiv av preposisjon", "jenis_no": "Imperativt verbalt substantiv"},
    "6. Isim Fi'il__6": {"arti_no": "Ta dette!", "desc_no": "Bydende verbalt substantiv av adverb", "jenis_no": "Imperativt verbalt substantiv"},
    "6. Isim Fi'il__7": {"arti_no": "Hvor forunderlig!", "desc_no": "Verbalt substantiv for undring", "jenis_no": "Verbalt substantiv"},
    "6. Isim Fi'il__8": {"arti_no": "Vik unna! / Her har du det", "desc_no": "Bydende verbalt substantiv", "jenis_no": "Imperativt verbalt substantiv"},

    "7. Fi'il Jamid__1": {"arti_no": "Hvor ypperlig! (Ni'ma)", "desc_no": "Uforanderlig rosende verb", "jenis_no": "Rosende uforanderlig verb"},
    "7. Fi'il Jamid__2": {"arti_no": "Hvor ussel! (Bi'sa)", "desc_no": "Uforanderlig klandrende verb", "jenis_no": "Klandrende uforanderlig verb"},
    "7. Fi'il Jamid__3": {"arti_no": "Er ikke / Var ikke (Laysa)", "desc_no": "Uforanderlig nektende kopulaverb", "jenis_no": "Nektende uforanderlig verb"},
    "7. Fi'il Jamid__4": {"arti_no": "Kanskje / Forhåpentligvis ('Asa)", "desc_no": "Uforanderlig håpsverb", "jenis_no": "Håpsverb"},
    "7. Fi'il Jamid__5": {"arti_no": "Hvor ondt er det ikke! (Sa'a)", "desc_no": "Uforanderlig klandrende verb", "jenis_no": "Klandrende uforanderlig verb"},
    "7. Fi'il Jamid__6": {"arti_no": "Hvor behagelig!", "desc_no": "Sammensatt rosende verb", "jenis_no": "Rosende verb"},
    "7. Fi'il Jamid__7": {"arti_no": "Velsignet og Opphøyet! (Tabaraka)", "desc_no": "Hellig uforanderlig verb for Guds storhet", "jenis_no": "Hellig uforanderlig verb"}
}

POLISH_GRAMMAR = {
    "1. Dhamir__1a": {"arti_pl": "On (3. os. l. poj. r. męski)", "desc_pl": "Samodzielny zaimek osobowy 3. os. l. poj. r. męski (Munfasil)", "jenis_pl": "Zaimek osobowy samodzielny"},
    "1. Dhamir__1b": {"arti_pl": "Jego / Mu / Go (Zaimek łączny)", "desc_pl": "Łączny zaimek osobowy 3. os. l. poj. r. męski (Muttasil)", "jenis_pl": "Zaimek osobowy łączny"},
    "1. Dhamir__1c": {"arti_pl": "Tylko Jego (Biernikowy)", "desc_pl": "Samodzielny zaimek biernikowy 3. os. l. poj.", "jenis_pl": "Zaimek biernikowy"},
    "1. Dhamir__2a": {"arti_pl": "Oni obaj (Liczba podwójna)", "desc_pl": "Samodzielny zaimek liczby podwójnej", "jenis_pl": "Zaimek liczby podwójnej"},
    "1. Dhamir__2b": {"arti_pl": "Ich obu (Zaimek łączny)", "desc_pl": "Łączny zaimek liczby podwójnej", "jenis_pl": "Zaimek łączny liczby podwójnej"},
    "1. Dhamir__3a": {"arti_pl": "Oni (L. mn. r. męski)", "desc_pl": "Samodzielny zaimek osobowy 3. os. l. mn. r. męski", "jenis_pl": "Zaimek osobowy samodzielny"},
    "1. Dhamir__3b": {"arti_pl": "Ich / Im / Ich (Zaimek łączny)", "desc_pl": "Łączny zaimek osobowy 3. os. l. mn. r. męski", "jenis_pl": "Zaimek osobowy łączny"},
    "1. Dhamir__3c": {"arti_pl": "Tylko im", "desc_pl": "Samodzielny zaimek biernikowy 3. os. l. mn. r. męski", "jenis_pl": "Zaimek biernikowy"},
    "1. Dhamir__4a": {"arti_pl": "Ona (3. os. l. poj. r. żeński)", "desc_pl": "Samodzielny zaimek osobowy 3. os. l. poj. r. żeński", "jenis_pl": "Zaimek osobowy samodzielny"},
    "1. Dhamir__4b": {"arti_pl": "Jej / Ją (Zaimek łączny)", "desc_pl": "Łączny zaimek osobowy 3. os. l. poj. r. żeński", "jenis_pl": "Zaimek osobowy łączny"},
    "1. Dhamir__5a": {"arti_pl": "One (L. mn. r. żeński)", "desc_pl": "Samodzielny zaimek osobowy 3. os. l. mn. r. żeński", "jenis_pl": "Zaimek osobowy samodzielny"},
    "1. Dhamir__5b": {"arti_pl": "Ich (Żeński zaimek łączny)", "desc_pl": "Łączny zaimek osobowy 3. os. l. mn. r. żeński", "jenis_pl": "Zaimek osobowy łączny"},
    "1. Dhamir__6a": {"arti_pl": "Ty (2. os. l. poj. r. męski)", "desc_pl": "Samodzielny zaimek osobowy 2. os. l. poj. r. męski", "jenis_pl": "Zaimek osobowy samodzielny"},
    "1. Dhamir__6b": {"arti_pl": "Twój / Tobie / Cię (Zaimek łączny)", "desc_pl": "Łączny zaimek osobowy 2. os. l. poj. r. męski", "jenis_pl": "Zaimek osobowy łączny"},
    "1. Dhamir__6c": {"arti_pl": "Ciebie tylko (Wyłączność kultu)", "desc_pl": "Samodzielny zaimek biernikowy 2. os. l. poj.", "jenis_pl": "Zaimek biernikowy"},
    "1. Dhamir__7a": {"arti_pl": "Wy obaj", "desc_pl": "Samodzielny zaimek 2. os. liczby podwójnej", "jenis_pl": "Zaimek liczby podwójnej"},
    "1. Dhamir__7b": {"arti_pl": "Was obu (Zaimek łączny)", "desc_pl": "Łączny zaimek 2. os. liczby podwójnej", "jenis_pl": "Zaimek łączny liczby podwójnej"},
    "1. Dhamir__8a": {"arti_pl": "Wy (L. mn. r. męski)", "desc_pl": "Samodzielny zaimek osobowy 2. os. l. mn. r. męski", "jenis_pl": "Zaimek osobowy samodzielny"},
    "1. Dhamir__8b": {"arti_pl": "Wasz / Wam / Was (Zaimek łączny)", "desc_pl": "Łączny zaimek osobowy 2. os. l. mn. r. męski", "jenis_pl": "Zaimek osobowy łączny"},
    "1. Dhamir__8c": {"arti_pl": "Tylko wam", "desc_pl": "Samodzielny zaimek biernikowy 2. os. l. mn. r. męski", "jenis_pl": "Zaimek biernikowy"},
    "1. Dhamir__9a": {"arti_pl": "Ty (2. os. l. poj. r. żeński)", "desc_pl": "Samodzielny zaimek osobowy 2. os. l. poj. r. żeński", "jenis_pl": "Zaimek osobowy samodzielny"},
    "1. Dhamir__9b": {"arti_pl": "Twój / Tobie (Żeński zaimek łączny)", "desc_pl": "Łączny zaimek osobowy 2. os. l. poj. r. żeński", "jenis_pl": "Zaimek osobowy łączny"},
    "1. Dhamir__10a": {"arti_pl": "Wy (L. mn. r. żeński)", "desc_pl": "Samodzielny zaimek osobowy 2. os. l. mn. r. żeński", "jenis_pl": "Zaimek osobowy samodzielny"},
    "1. Dhamir__10b": {"arti_pl": "Wasz (Żeński zaimek łączny)", "desc_pl": "Łączny zaimek osobowy 2. os. l. mn. r. żeński", "jenis_pl": "Zaimek osobowy łączny"},
    "1. Dhamir__11a": {"arti_pl": "Ja (1. os. l. poj.)", "desc_pl": "Samodzielny zaimek osobowy 1. os. l. poj.", "jenis_pl": "Zaimek osobowy samodzielny"},
    "1. Dhamir__11b": {"arti_pl": "Mój / Mnie / Mnie (Zaimek łączny)", "desc_pl": "Łączny zaimek osobowy 1. os. l. poj.", "jenis_pl": "Zaimek osobowy łączny"},
    "1. Dhamir__11c": {"arti_pl": "Tylko mnie", "desc_pl": "Samodzielny zaimek biernikowy 1. os. l. poj.", "jenis_pl": "Zaimek biernikowy"},
    "1. Dhamir__12a": {"arti_pl": "My (1. os. l. mn.)", "desc_pl": "Samodzielny zaimek osobowy 1. os. l. mn.", "jenis_pl": "Zaimek osobowy samodzielny"},
    "1. Dhamir__12b": {"arti_pl": "Nasz / Nam / Nas (Zaimek łączny)", "desc_pl": "Łączny zaimek osobowy 1. os. l. mn.", "jenis_pl": "Zaimek osobowy łączny"},
    "1. Dhamir__12c": {"arti_pl": "Tylko nam", "desc_pl": "Samodzielny zaimek biernikowy 1. os. l. mn.", "jenis_pl": "Zaimek biernikowy"},

    "2. Isim Mawshul__1": {"arti_pl": "To, co / Cokolwiek (Dla rzeczy nieożywionych)", "desc_pl": "Ogólny zaimek względny dla rzeczy nieożywionych", "jenis_pl": "Ogólny zaimek względny"},
    "2. Isim Mawshul__2": {"arti_pl": "Ci, którzy (L. mn. r. męski)", "desc_pl": "Zaimek względny dla osób w liczbie mnogiej", "jenis_pl": "Zaimek względny specyficzny"},
    "2. Isim Mawshul__3": {"arti_pl": "Ten, kto / Ktokolwiek (Dla istot rozumnych)", "desc_pl": "Ogólny zaimek względny dla istot rozumnych", "jenis_pl": "Ogólny zaimek względny"},
    "2. Isim Mawshul__4": {"arti_pl": "Ten, który (L. poj. r. męski)", "desc_pl": "Zaimek względny dla liczby pojedynczej r. męskiego", "jenis_pl": "Zaimek względny specyficzny"},
    "2. Isim Mawshul__5": {"arti_pl": "Którykolwiek / Ktokolwiek", "desc_pl": "Dopełniaczowy zaimek względny", "jenis_pl": "Zaimek względny"},
    "2. Isim Mawshul__6": {"arti_pl": "Ta, która (L. poj. r. żeński)", "desc_pl": "Zaimek względny dla liczby pojedynczej r. żeńskiego", "jenis_pl": "Zaimek względny specyficzny"},
    "2. Isim Mawshul__7": {"arti_pl": "Te kobiety, które (L. mn.)", "desc_pl": "Zaimek względny dla kobiet w liczbie mnogiej", "jenis_pl": "Zaimek względny żeński"},
    "2. Isim Mawshul__8": {"arti_pl": "Te kobiety, które (L. mn.)", "desc_pl": "Zaimek względny dla kobiet w liczbie mnogiej", "jenis_pl": "Zaimek względny żeński"},
    "2. Isim Mawshul__9": {"arti_pl": "Ci dwaj, którzy", "desc_pl": "Zaimek względny liczby podwójnej", "jenis_pl": "Zaimek względny liczby podwójnej"},
    "2. Isim Mawshul__10": {"arti_pl": "Którakolwiek z nich", "desc_pl": "Żeński zaimek względny", "jenis_pl": "Zaimek względny"},

    "3. Isim Istifham__1": {"arti_pl": "Co? / Czym jest to?", "desc_pl": "Zaimek pytający o rzeczy", "jenis_pl": "Zaimek pytający"},
    "3. Isim Istifham__2": {"arti_pl": "Kto? / Kto to jest?", "desc_pl": "Zaimek pytający o osoby", "jenis_pl": "Zaimek pytający"},
    "3. Isim Istifham__3": {"arti_pl": "Jak? / W jaki sposób?", "desc_pl": "Zaimek pytający o stan", "jenis_pl": "Zaimek pytający o stan"},
    "3. Isim Istifham__4": {"arti_pl": "Gdzie? / Dokąd?", "desc_pl": "Zaimek pytający o miejsce", "jenis_pl": "Zaimek pytający o miejsce"},
    "3. Isim Istifham__5": {"arti_pl": "Ile? / Jaka ilość?", "desc_pl": "Zaimek pytający o liczbę i ilość", "jenis_pl": "Zaimek pytający o ilość"},
    "3. Isim Istifham__6": {"arti_pl": "Kiedy? / O jakim czasie?", "desc_pl": "Zaimek pytający o czas", "jenis_pl": "Zaimek pytający o czas"},
    "3. Isim Istifham__7": {"arti_pl": "Kiedy nadejdzie? (Dzień Zmartwychwstania)", "desc_pl": "Zaimek pytający o wielkie przyszłe wydarzenia", "jenis_pl": "Zaimek pytający o czas"},
    "3. Isim Istifham__8": {"arti_pl": "Skąd? / Jakim sposobem?", "desc_pl": "Zaimek pytający o pochodzenie lub przyczynę", "jenis_pl": "Zaimek pytający"},

    "4. Isim Syarath__1": {"arti_pl": "Kto / Ktokolwiek", "desc_pl": "Zaimek warunkowy dla osób wymagający jussivu", "jenis_pl": "Zaimek warunkowy"},
    "4. Isim Syarath__2": {"arti_pl": "Cokolwiek / Co uczynicie", "desc_pl": "Zaimek warunkowy dla rzeczy", "jenis_pl": "Zaimek warunkowy"},
    "4. Isim Syarath__3": {"arti_pl": "Kiedy / W chwili gdy", "desc_pl": "Czasowy zaimek warunkowy na przyszłość", "jenis_pl": "Czasowy zaimek warunkowy"},
    "4. Isim Syarath__4": {"arti_pl": "Cokolwiek bądź", "desc_pl": "Ogólny zaimek warunkowy", "jenis_pl": "Zaimek warunkowy"},
    "4. Isim Syarath__5": {"arti_pl": "Gdziekolwiek / Dokądkolwiek", "desc_pl": "Miejscowy zaimek warunkowy", "jenis_pl": "Miejscowy zaimek warunkowy"},
    "4. Isim Syarath__6": {"arti_pl": "Gdziekolwiek się znajdujecie", "desc_pl": "Wzmocniony miejscowy zaimek warunkowy", "jenis_pl": "Miejscowy zaimek warunkowy"},
    "4. Isim Syarath__7": {"arti_pl": "W jakimkolwiek stanie", "desc_pl": "Zaimek warunkowy stanu", "jenis_pl": "Zaimek warunkowy stanu"},
    "4. Isim Syarath__8": {"arti_pl": "Którykolwiek", "desc_pl": "Dopełniaczowy zaimek warunkowy", "jenis_pl": "Zaimek warunkowy"},

    "5. Isim Isyarah__1": {"arti_pl": "Tamta / Owa księga (Daleki r. męski)", "desc_pl": "Zaimek wskazujący dla obiektów oddalonych r. męski", "jenis_pl": "Zaimek wskazujący daleki"},
    "5. Isim Isyarah__2": {"arti_pl": "Ten / To (Bliski r. męski)", "desc_pl": "Zaimek wskazujący dla obiektów bliskich r. męski", "jenis_pl": "Zaimek wskazujący bliski"},
    "5. Isim Isyarah__3": {"arti_pl": "Ci / Te (Bliska l. mn.)", "desc_pl": "Zaimek wskazujący dla bliskiej liczby mnogiej", "jenis_pl": "Zaimek wskazujący bliski"},
    "5. Isim Isyarah__4": {"arti_pl": "Tamci / Oni (Daleka l. mn.)", "desc_pl": "Zaimek wskazujący dla dalekiej liczby mnogiej", "jenis_pl": "Zaimek wskazujący daleki"},
    "5. Isim Isyarah__5": {"arti_pl": "Ta (Bliski r. żeński)", "desc_pl": "Zaimek wskazujący dla bliskiej liczby pojedynczej r. żeńskiego", "jenis_pl": "Zaimek wskazujący bliski"},
    "5. Isim Isyarah__6": {"arti_pl": "Tamta (Daleki r. żeński)", "desc_pl": "Zaimek wskazujący dla dalekiej liczby pojedynczej r. żeńskiego", "jenis_pl": "Zaimek wskazujący daleki"},
    "5. Isim Isyarah__7": {"arti_pl": "Tam / W owym miejscu", "desc_pl": "Zaimek wskazujący dla dalekiego miejsca", "jenis_pl": "Miejscowy zaimek wskazujący"},
    "5. Isim Isyarah__8": {"arti_pl": "Tutaj / W tym miejscu", "desc_pl": "Zaimek wskazujący dla bliskiego miejsca", "jenis_pl": "Miejscowy zaimek wskazujący"},
    "5. Isim Isyarah__9": {"arti_pl": "Te dwie rzeczy (Daleki r. męski)", "desc_pl": "Zaimek wskazujący liczby podwójnej", "jenis_pl": "Zaimek wskazujący podwójny"},
    "5. Isim Isyarah__10": {"arti_pl": "Te dwie rzeczy (Daleki r. żeński)", "desc_pl": "Zaimek wskazujący liczby podwójnej", "jenis_pl": "Zaimek wskazujący podwójny"},

    "6. Isim Fi'il__1": {"arti_pl": "Jakże to dalekie! (Hajhata)", "desc_pl": "Rzeczownik czasownikowy czasu przeszłego", "jenis_pl": "Rzeczownik czasownikowy przeszły"},
    "6. Isim Fi'il__2": {"arti_pl": "Uff! / Hańba! (Uff)", "desc_pl": "Rzeczownik czasownikowy wyrażający zniecierpliwienie", "jenis_pl": "Rzeczownik czasownikowy teraźniejszy"},
    "6. Isim Fi'il__3": {"arti_pl": "Chodźcie! / Przynieście!", "desc_pl": "Rozkazujący rzeczownik czasownikowy", "jenis_pl": "Rzeczownik czasownikowy rozkazujący"},
    "6. Isim Fi'il__4": {"arti_pl": "Weźcie! / Czytajcie!", "desc_pl": "Rozkazujący rzeczownik czasownikowy", "jenis_pl": "Rzeczownik czasownikowy rozkazujący"},
    "6. Isim Fi'il__5": {"arti_pl": "Strzeżcie się! / Trzymajcie się!", "desc_pl": "Rozkazujący rzeczownik czasownikowy utworzony z przyimka", "jenis_pl": "Rzeczownik czasownikowy rozkazujący"},
    "6. Isim Fi'il__6": {"arti_pl": "Bierzcie to!", "desc_pl": "Rozkazujący rzeczownik czasownikowy utworzony z przysłówka", "jenis_pl": "Rzeczownik czasownikowy rozkazujący"},
    "6. Isim Fi'il__7": {"arti_pl": "Jakież to niezwykłe!", "desc_pl": "Rzeczownik czasownikowy wyrażający podziw", "jenis_pl": "Rzeczownik czasownikowy"},
    "6. Isim Fi'il__8": {"arti_pl": "Odstąpcie! / Oto macie", "desc_pl": "Rozkazujący rzeczownik czasownikowy", "jenis_pl": "Rzeczownik czasownikowy rozkazujący"},

    "7. Fi'il Jamid__1": {"arti_pl": "Jakże wspaniały! (Ni'ma)", "desc_pl": "Czasownik nieodmienny pochwalny", "jenis_pl": "Czasownik pochwalny nieodmienny"},
    "7. Fi'il Jamid__2": {"arti_pl": "Jakże nikczemny! (Bi'sa)", "desc_pl": "Czasownik nieodmienny nagany", "jenis_pl": "Czasownik nagany nieodmienny"},
    "7. Fi'il Jamid__3": {"arti_pl": "Nie jest / Nie był (Lajsa)", "desc_pl": "Czasownik nieodmienny przeczący łącznikowy", "jenis_pl": "Czasownik przeczący nieodmienny"},
    "7. Fi'il Jamid__4": {"arti_pl": "Być może / Jest nadzieja ('Asa)", "desc_pl": "Czasownik nieodmienny nadziei", "jenis_pl": "Czasownik nadziei"},
    "7. Fi'il Jamid__5": {"arti_pl": "Jakże to złe! (Sa'a)", "desc_pl": "Czasownik nieodmienny nagany", "jenis_pl": "Czasownik nagany nieodmienny"},
    "7. Fi'il Jamid__6": {"arti_pl": "Jakże to przyjemne!", "desc_pl": "Złożony czasownik pochwalny", "jenis_pl": "Czasownik pochwalny"},
    "7. Fi'il Jamid__7": {"arti_pl": "Błogosławiony i Wywyższony! (Tabaraka)", "desc_pl": "Święty czasownik nieodmienny Bożej wielkości", "jenis_pl": "Święty czasownik nieodmienny"}
}

NORWEGIAN_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {"arti_no": "Ikke / Nei (Ma - generell nektelse)", "desc_no": "Ikke-styrende nektelsespartikkel for fortid, nåtid og nominalsetninger", "jenis_no": "Nektelsespartikkel"},
    "1. Harf Nafyi__2": {"arti_no": "Ikke / Ei (La - verbal nektelse)", "desc_no": "Nektelsespartikkel for nåtid og fremtid", "jenis_no": "Nektelsespartikkel"},
    "1. Harf Nafyi__3": {"arti_no": "Er ikke annet enn... (In)", "desc_no": "Nektelsespartikkel koblet med Illa", "jenis_no": "Nektelsespartikkel"},
    "1. Harf Nafyi__4": {"arti_no": "Er ikke tid for (Lata)", "desc_no": "Tidsmessig nektelsespartikkel", "jenis_no": "Tidsnektelsespartikkel"},

    "2. Harf Tahqiq Taswif__5": {"arti_no": "Sannelig / Allerede (Qad - bekreftelse)", "desc_no": "Partikkel for visshet og ettertrykk før fortidige verb", "jenis_no": "Bekreftelsespartikkel"},
    "2. Harf Tahqiq Taswif__6": {"arti_no": "I fremtiden / Senere (Sawfa)", "desc_no": "Partikkel for fjern fremtid", "jenis_no": "Fremtidspartikkel"},
    "2. Harf Tahqiq Taswif__7": {"arti_no": "Snart / Straks (Sa - nær fremtid)", "desc_no": "Partikkel for nær fremtid", "jenis_no": "Fremtidspartikkel"},

    "3. Harf Syarat__8": {"arti_no": "Dersom / Hvis (Law - uvirkelig betingelse)", "desc_no": "Ikke-styrende betingelsespartikkel for uoppfylte handlinger", "jenis_no": "Betingelsespartikkel"},
    "3. Harf Syarat__9": {"arti_no": "Hadde det ikke vært for... (Lawla)", "desc_no": "Betingelsespartikkel for forhindring", "jenis_no": "Betingelsespartikkel"},
    "3. Harf Syarat__10": {"arti_no": "Var det ikke for... (Lawma)", "desc_no": "Ikke-styrende betingelsespartikkel", "jenis_no": "Betingelsespartikkel"},
    "3. Harf Syarat__11": {"arti_no": "Da / På den tid da (Lamma)", "desc_no": "Tidsbetingelsespartikkel for fortid", "jenis_no": "Tidsbetingelsespartikkel"},
    "3. Harf Syarat__12": {"arti_no": "Hva angår... så (Amma)", "desc_no": "Utdypende betingelsespartikkel med emfatisk vekt", "jenis_no": "Betingelsespartikkel"},

    "4. Harf Mashdariyah__13": {"arti_no": "At / For å (An - infinitivpartikkel)", "desc_no": "Partikkel som omdanner et verb til et verbalsubstantiv", "jenis_no": "Infinitivpartikkel"},
    "4. Harf Mashdariyah__14": {"arti_no": "Så lenge som (Ma mashdariyah)", "desc_no": "Tidsmessig infinitivpartikkel", "jenis_no": "Infinitivpartikkel"},
    "4. Harf Mashdariyah__15": {"arti_no": "For at / Slik at (Kay)", "desc_no": "Hensiktsmessig infinitivpartikkel", "jenis_no": "Infinitivpartikkel"},
    "4. Harf Mashdariyah__16": {"arti_no": "Om bare / Ønske om at (Law)", "desc_no": "Infinitivpartikkel etter ønske-verb", "jenis_no": "Infinitivpartikkel"},

    "5. Harf Zaidah__17": {"arti_no": "For ettertrykk (In za'idah)", "desc_no": "Forsterkende tilleggspartikkel", "jenis_no": "Forsterkende partikkel"},
    "5. Harf Zaidah__18": {"arti_no": "For ettertrykk (An za'idah)", "desc_no": "Forsterkende tilleggspartikkel", "jenis_no": "Forsterkende partikkel"},
    "5. Harf Zaidah__19": {"arti_no": "For ettertrykk (Ma za'idah)", "desc_no": "Forsterkende tilleggspartikkel", "jenis_no": "Forsterkende partikkel"},
    "5. Harf Zaidah__20": {"arti_no": "For ettertrykk (La za'idah)", "desc_no": "Forsterkende tilleggspartikkel for nektelse", "jenis_no": "Forsterkende partikkel"},

    "6. Harf Istifham__21": {"arti_no": "Er det slik? / Mon tro? (Hamzah)", "desc_no": "Grunnleggende spørrepartikkel", "jenis_no": "Spørrepartikkel"},
    "6. Harf Istifham__22": {"arti_no": "Mon tro? / Hvorvidt? (Hal)", "desc_no": "Spørrepartikkel for ja/nei-bekreftelse", "jenis_no": "Spørrepartikkel"},

    "7. Harf Istitsna__23": {"arti_no": "Unntatt / Bortsett fra (Illa)", "desc_no": "Unntakspartikkel", "jenis_no": "Unntakspartikkel"},

    "8. Harf Rad'in Wazajrin__24": {"arti_no": "Slett ikke! / Aldeles ikke! (Kalla)", "desc_no": "Kategorisk avvisende og irettesettende partikkel", "jenis_no": "Avvisningspartikkel"},

    "9. Harf Rad'in Tahdid__25": {"arti_no": "Hvorfor ikke...? (Halla)", "desc_no": "Oppfordrende og bebreidende partikkel", "jenis_no": "Oppfordringspartikkel"},
    "9. Harf Rad'in Tahdid__26": {"arti_no": "Hvorfor da ikke... (Alla)", "desc_no": "Oppfordrende partikkel til rask handling", "jenis_no": "Oppfordringspartikkel"},

    "10. Harf Ijab__27": {"arti_no": "Ja / Så er det (Na'am)", "desc_no": "Bekreftende svarpartikkel", "jenis_no": "Svarpartikkel"},
    "10. Harf Ijab__28": {"arti_no": "Ja, visselig! (Bala)", "desc_no": "Partikkel som opphever nektelse og bekrefter sannhet", "jenis_no": "Bekreftelsespartikkel"},
    "10. Harf Ijab__29": {"arti_no": "Ja, ved min Herre! (I)", "desc_no": "Bekreftelsespartikkel ved ed", "jenis_no": "Edspartikkel"},
    "10. Harf Ijab__30": {"arti_no": "Sannelig / Visselig (Ajal)", "desc_no": "Bekreftelsespartikkel", "jenis_no": "Bekreftelsespartikkel"},

    "11. Harf Tafsir__31": {"arti_no": "Nemlig / Det vil si (Ay)", "desc_no": "Forklarende partikkel", "jenis_no": "Forklarende partikkel"},
    "11. Harf Tafsir__32": {"arti_no": "At / Nemlig (An tafsiriyyah)", "desc_no": "Forklarende partikkel etter taleverb", "jenis_no": "Forklarende partikkel"},

    "12. Harf Tanbih__33": {"arti_no": "Se! / Vit! (Ala)", "desc_no": "Oppmerksomhetspartikkel ved setningens begynnelse", "jenis_no": "Oppmerksomhetspartikkel"},
    "12. Harf Tanbih__34": {"arti_no": "Vit sannelig! (Ama)", "desc_no": "Oppmerksomhetspartikkel", "jenis_no": "Oppmerksomhetspartikkel"},
    "12. Harf Tanbih__35": {"arti_no": "Se her! (Ha tanbih)", "desc_no": "Oppmerksomhetsvekkende partikkel foran pronomen", "jenis_no": "Oppmerksomhetspartikkel"},

    "13. Harf Ta'lil__36": {"arti_no": "For at / Fordi (Lam ta'lil)", "desc_no": "Årsakspartikkel for begrunnelse og hensikt", "jenis_no": "Årsakspartikkel"},

    "14. Harf Fuja'iyyah__37": {"arti_no": "Og plutselig! / Og se (Idha fuja'iyyah)", "desc_no": "Partikkel som uttrykker en plutselig uventet hendelse", "jenis_no": "Overraskelsespartikkel"},
    "14. Harf Fuja'iyyah__38": {"arti_no": "Brått / Plutselig (Idh fuja'iyyah)", "desc_no": "Overraskelsespartikkel", "jenis_no": "Overraskelsespartikkel"},

    "15. Harf Istidrak__39": {"arti_no": "Men / Likevel (Lakin)", "desc_no": "Korrigerende og motsetningsdannende partikkel", "jenis_no": "Korreksjonspartikkel"},
    "15. Harf Istidrak__40": {"arti_no": "Tvert imot / Ja endog (Bal)", "desc_no": "Partikkel for endring av påstand", "jenis_no": "Korreksjonspartikkel"},

    "16. Harf Ta'ajjub__41": {"arti_no": "Hvor... dog! / Hvor forunderlig! (Ma)", "desc_no": "Utropspartikkel for beundring og undring", "jenis_no": "Beundringspartikkel"},

    "17. Harf Mabany__39": {"arti_no": "Ha-Mim", "desc_no": "Innledende bokstaver i surer", "jenis_no": "Muqatta'at bokstaver"},
    "17. Harf Mabany__40": {"arti_no": "Alif-Lam-Mim", "desc_no": "Innledende bokstaver i surer", "jenis_no": "Muqatta'at bokstaver"},
    "17. Harf Mabany__41": {"arti_no": "Alif-Lam-Ra", "desc_no": "Innledende bokstaver i surer", "jenis_no": "Muqatta'at bokstaver"},
    "17. Harf Mabany__42": {"arti_no": "Ta-Sin-Mim", "desc_no": "Innledende bokstaver i surer", "jenis_no": "Muqatta'at bokstaver"},
    "17. Harf Mabany__43": {"arti_no": "Alif-Lam-Mim-Ra", "desc_no": "Innledende bokstaver i surer", "jenis_no": "Muqatta'at bokstaver"},
    "17. Harf Mabany__44": {"arti_no": "Alif-Lam-Mim-Sad", "desc_no": "Innledende bokstaver i surer", "jenis_no": "Muqatta'at bokstaver"},
    "17. Harf Mabany__45": {"arti_no": "Sad", "desc_no": "Innledende bokstaver i surer", "jenis_no": "Muqatta'at bokstaver"},
    "17. Harf Mabany__46": {"arti_no": "Ta-Sin", "desc_no": "Innledende bokstaver i surer", "jenis_no": "Muqatta'at bokstaver"},
    "17. Harf Mabany__47": {"arti_no": "Ta-Ha", "desc_no": "Innledende bokstaver i surer", "jenis_no": "Muqatta'at bokstaver"},
    "17. Harf Mabany__48": {"arti_no": "Ayn-Sin-Qaf", "desc_no": "Innledende bokstaver i surer", "jenis_no": "Muqatta'at bokstaver"},
    "17. Harf Mabany__49": {"arti_no": "Qaf", "desc_no": "Innledende bokstaver i surer", "jenis_no": "Muqatta'at bokstaver"},
    "17. Harf Mabany__50": {"arti_no": "Kaf-Ha-Ya-Ayn-Sad", "desc_no": "Innledende bokstaver i surer", "jenis_no": "Muqatta'at bokstaver"},
    "17. Harf Mabany__51": {"arti_no": "Nun", "desc_no": "Innledende bokstaver i surer", "jenis_no": "Muqatta'at bokstaver"},
    "17. Harf Mabany__52": {"arti_no": "Ya-Sin", "desc_no": "Innledende bokstaver i surer", "jenis_no": "Muqatta'at bokstaver"}
}

POLISH_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {"arti_pl": "Nie / Ani (Ma - ogólne przeczenie)", "desc_pl": "Niezarządzająca partykuła przecząca dla czasu przeszłego, teraźniejszego i zdań imiennych", "jenis_pl": "Partykuła przecząca"},
    "1. Harf Nafyi__2": {"arti_pl": "Nie / Wcale nie (La - przeczenie czasownikowe)", "desc_pl": "Partykuła przecząca dla czasu teraźniejszego i przyszłego", "jenis_pl": "Partykuła przecząca"},
    "1. Harf Nafyi__3": {"arti_pl": "Nie jest niczym innym jak... (In)", "desc_pl": "Partykuła przecząca łączona z Illa", "jenis_pl": "Partykuła przecząca"},
    "1. Harf Nafyi__4": {"arti_pl": "Nie ma już czasu na (Lata)", "desc_pl": "Partykuła przecząca czasowa", "jenis_pl": "Partykuła przecząca czasowa"},

    "2. Harf Tahqiq Taswif__5": {"arti_pl": "Zaiste / Już (Kad - potwierdzenie)", "desc_pl": "Partykuła pewności i nacisku przed czasem przeszłym", "jenis_pl": "Partykuła potwierdzenia"},
    "2. Harf Tahqiq Taswif__6": {"arti_pl": "W przyszłości / Później (Saufa)", "desc_pl": "Partykuła dalekiej przyszłości", "jenis_pl": "Partykuła przyszłości"},
    "2. Harf Tahqiq Taswif__7": {"arti_pl": "Wkrótce / Niebawem (Sa - bliska przyszłość)", "desc_pl": "Partykuła bliskiej przyszłości", "jenis_pl": "Partykuła przyszłości"},

    "3. Harf Syarat__8": {"arti_pl": "Gdyby / Jeśliby (Lau - warunek nierzeczywisty)", "desc_pl": "Niezarządzająca partykuła warunkowa dla niespełnionych zdarzeń przeszłych", "jenis_pl": "Partykuła warunkowa"},
    "3. Harf Syarat__9": {"arti_pl": "Gdyby nie to, że... (Laula)", "desc_pl": "Partykuła warunkowa przeszkody", "jenis_pl": "Partykuła warunkowa"},
    "3. Harf Syarat__10": {"arti_pl": "Gdyby nie... (Lauma)", "desc_pl": "Niezarządzająca partykuła warunkowa", "jenis_pl": "Partykuła warunkowa"},
    "3. Harf Syarat__11": {"arti_pl": "Kiedy / W czasie gdy (Lamma)", "desc_pl": "Czasowa partykuła warunkowa dla przeszłości", "jenis_pl": "Czasowa partykuła warunkowa"},
    "3. Harf Syarat__12": {"arti_pl": "A co się tyczy... to (Amma)", "desc_pl": "Rozwijająca partykuła warunkowa z naciskiem", "jenis_pl": "Partykuła warunkowa"},

    "4. Harf Mashdariyah__13": {"arti_pl": "Żeby / Iż (An - partykuła bezokolicznikowa)", "desc_pl": "Partykuła przekształcająca czasownik w rzeczownik odczasownikowy", "jenis_pl": "Partykuła bezokolicznikowa"},
    "4. Harf Mashdariyah__14": {"arti_pl": "Dopóki / Tak długo jak (Ma masdarijja)", "desc_pl": "Czasowa partykuła bezokolicznikowa", "jenis_pl": "Partykuła bezokolicznikowa"},
    "4. Harf Mashdariyah__15": {"arti_pl": "Aby / W celu (Kaj)", "desc_pl": "Celowa partykuła bezokolicznikowa", "jenis_pl": "Partykuła bezokolicznikowa"},
    "4. Harf Mashdariyah__16": {"arti_pl": "Oby / Życzenie aby (Lau)", "desc_pl": "Partykuła bezokolicznikowa po czasownikach życzenia", "jenis_pl": "Partykuła bezokolicznikowa"},

    "5. Harf Zaidah__17": {"arti_pl": "Dla wzmocnienia znaczenia (In za'ida)", "desc_pl": "Dodatkowa partykuła wzmacniająca", "jenis_pl": "Partykuła wzmacniająca"},
    "5. Harf Zaidah__18": {"arti_pl": "Dla wzmocnienia znaczenia (An za'ida)", "desc_pl": "Dodatkowa partykuła wzmacniająca", "jenis_pl": "Partykuła wzmacniająca"},
    "5. Harf Zaidah__19": {"arti_pl": "Dla wzmocnienia znaczenia (Ma za'ida)", "desc_pl": "Dodatkowa partykuła wzmacniająca", "jenis_pl": "Partykuła wzmacniająca"},
    "5. Harf Zaidah__20": {"arti_pl": "Dla wzmocnienia znaczenia (La za'ida)", "desc_pl": "Dodatkowa partykuła wzmacniająca przeczenie", "jenis_pl": "Partykuła wzmacniająca"},

    "6. Harf Istifham__21": {"arti_pl": "Czyż? / Czy? (Hamza)", "desc_pl": "Podstawowa partykuła pytająca", "jenis_pl": "Partykuła pytająca"},
    "6. Harf Istifham__22": {"arti_pl": "Czy? / Czyżby? (Hal)", "desc_pl": "Partykuła pytająca wymagająca potwierdzenia lub zaprzeczenia", "jenis_pl": "Partykuła pytająca"},

    "7. Harf Istitsna__23": {"arti_pl": "Oprócz / Z wyjątkiem (Illa)", "desc_pl": "Partykuła wyłączająca", "jenis_pl": "Partykuła wyłączająca"},

    "8. Harf Rad'in Wazajrin__24": {"arti_pl": "Bynajmniej! / W żadnym razie! (Kalla)", "desc_pl": "Kategoryczna partykuła nagany i odrzucenia", "jenis_pl": "Partykuła nagany"},

    "9. Harf Rad'in Tahdid__25": {"arti_pl": "Dlaczego nie...? (Halla)", "desc_pl": "Partykuła zachęty i wyrzutu", "jenis_pl": "Partykuła zachęty"},
    "9. Harf Rad'in Tahdid__26": {"arti_pl": "Czemuż więc nie... (Alla)", "desc_pl": "Partykuła naglącej zachęty do dobra", "jenis_pl": "Partykuła zachęty"},

    "10. Harf Ijab__27": {"arti_pl": "Tak / Zaiste tak (Na'am)", "desc_pl": "Twierdząca partykuła odpowiedzi", "jenis_pl": "Partykuła odpowiedzi"},
    "10. Harf Ijab__28": {"arti_pl": "Owszem, zaprawdę! (Bala)", "desc_pl": "Partykuła unieważniająca zaprzeczenie i potwierdzająca prawdę", "jenis_pl": "Partykuła potwierdzenia"},
    "10. Harf Ijab__29": {"arti_pl": "Tak, na mojego Pana! (I)", "desc_pl": "Partykuła twierdząca przy przysiędze", "jenis_pl": "Partykuła przysięgi"},
    "10. Harf Ijab__30": {"arti_pl": "Zaprawdę / Rzeczywiście (Adżal)", "desc_pl": "Partykuła twierdząca", "jenis_pl": "Partykuła twierdząca"},

    "11. Harf Tafsir__31": {"arti_pl": "Mianowicie / To znaczy (Aj)", "desc_pl": "Partykuła objaśniająca", "jenis_pl": "Partykuła objaśniająca"},
    "11. Harf Tafsir__32": {"arti_pl": "Iż / Że (An tafsirijja)", "desc_pl": "Partykuła objaśniająca po czasownikach mowy", "jenis_pl": "Partykuła objaśniająca"},

    "12. Harf Tanbih__33": {"arti_pl": "Oto! / Wiedzcie! (Ala)", "desc_pl": "Partykuła zwracająca uwagę na początku zdania", "jenis_pl": "Partykuła zwracająca uwagę"},
    "12. Harf Tanbih__34": {"arti_pl": "Wiedzcie dobrze! (Ama)", "desc_pl": "Partykuła zwracająca uwagę", "jenis_pl": "Partykuła zwracająca uwagę"},
    "12. Harf Tanbih__35": {"arti_pl": "Oto spójrzcie! (Ha tanbih)", "desc_pl": "Partykuła przyciągająca uwagę przed zaimkami", "jenis_pl": "Partykuła zwracająca uwagę"},

    "13. Harf Ta'lil__36": {"arti_pl": "Aby / Ponieważ (Lam ta'lil)", "desc_pl": "Partykuła przyczynowa wyrażająca cel i powód", "jenis_pl": "Partykuła przyczynowa"},

    "14. Harf Fuja'iyyah__37": {"arti_pl": "I oto nagle! / Niespodziewanie (Idha fudża'ijja)", "desc_pl": "Partykuła wyrażająca nagłe i niespodziewane zdarzenie", "jenis_pl": "Partykuła nagłości"},
    "14. Harf Fuja'iyyah__38": {"arti_pl": "Niespodziewanie (Idh fudża'ijja)", "desc_pl": "Partykuła nagłości", "jenis_pl": "Partykuła nagłości"},

    "15. Harf Istidrak__39": {"arti_pl": "Lecz / Wszakże (Lakin)", "desc_pl": "Partykuła przeciwstawna i sprostowania", "jenis_pl": "Partykuła przeciwstawna"},
    "15. Harf Istidrak__40": {"arti_pl": "Wręcz przeciwnie / Raczej (Bal)", "desc_pl": "Partykuła zmiany twierdzenia i sprostowania", "jenis_pl": "Partykuła przeciwstawna"},

    "16. Harf Ta'ajjub__41": {"arti_pl": "Jakże... tylko! / Jakież to niezwykłe! (Ma)", "desc_pl": "Partykuła wykrzyknikowa podziwu i zdumienia", "jenis_pl": "Partykuła podziwu"},

    "17. Harf Mabany__39": {"arti_pl": "Ha-Mim", "desc_pl": "Tajemnicze litery na początku sur", "jenis_pl": "Litery Mukatta'at"},
    "17. Harf Mabany__40": {"arti_pl": "Alif-Lam-Mim", "desc_pl": "Tajemnicze litery na początku sur", "jenis_pl": "Litery Mukatta'at"},
    "17. Harf Mabany__41": {"arti_pl": "Alif-Lam-Ra", "desc_pl": "Tajemnicze litery na początku sur", "jenis_pl": "Litery Mukatta'at"},
    "17. Harf Mabany__42": {"arti_pl": "Ta-Sin-Mim", "desc_pl": "Tajemnicze litery na początku sur", "jenis_pl": "Litery Mukatta'at"},
    "17. Harf Mabany__43": {"arti_pl": "Alif-Lam-Mim-Ra", "desc_pl": "Tajemnicze litery na początku sur", "jenis_pl": "Litery Mukatta'at"},
    "17. Harf Mabany__44": {"arti_pl": "Alif-Lam-Mim-Sad", "desc_pl": "Tajemnicze litery na początku sur", "jenis_pl": "Litery Mukatta'at"},
    "17. Harf Mabany__45": {"arti_pl": "Sad", "desc_pl": "Tajemnicze litery na początku sur", "jenis_pl": "Litery Mukatta'at"},
    "17. Harf Mabany__46": {"arti_pl": "Ta-Sin", "desc_pl": "Tajemnicze litery na początku sur", "jenis_pl": "Litery Mukatta'at"},
    "17. Harf Mabany__47": {"arti_pl": "Ta-Ha", "desc_pl": "Tajemnicze litery na początku sur", "jenis_pl": "Litery Mukatta'at"},
    "17. Harf Mabany__48": {"arti_pl": "Ajn-Sin-Kaf", "desc_pl": "Tajemnicze litery na początku sur", "jenis_pl": "Litery Mukatta'at"},
    "17. Harf Mabany__49": {"arti_pl": "Kaf", "desc_pl": "Tajemnicze litery na początku sur", "jenis_pl": "Litery Mukatta'at"},
    "17. Harf Mabany__50": {"arti_pl": "Kaf-Ha-Ja-Ajn-Sad", "desc_pl": "Tajemnicze litery na początku sur", "jenis_pl": "Litery Mukatta'at"},
    "17. Harf Mabany__51": {"arti_pl": "Nun", "desc_pl": "Tajemnicze litery na początku sur", "jenis_pl": "Litery Mukatta'at"},
    "17. Harf Mabany__52": {"arti_pl": "Ja-Sin", "desc_pl": "Tajemnicze litery na początku sur", "jenis_pl": "Litery Mukatta'at"}
}


def enrich_dhamir_data():
    print("Enriching dhamir_data.json and dhamir_data.js with Norwegian & Polish...")
    with open(os.path.join(BASE_DIR, 'no_translations.json'), 'r', encoding='utf-8') as f:
        no_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'pl_translations.json'), 'r', encoding='utf-8') as f:
        pl_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = str(item.get('No kata', ''))
        g_key = f"{b}__{nk}"
        s_num = str(item.get('SURAT', ''))
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"

        # NO
        item['BentukKataNO'] = BENTUK_KATA_NO.get(b, b)
        item['SuratArtiNO'] = NORWEGIAN_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_no = NORWEGIAN_GRAMMAR.get(g_key, {})
        item['ArtiKataNO'] = g_no.get('arti_no', item.get('ArtiKataEN', ''))
        item['TeksArtiNO'] = no_trans.get(v_key, item.get('TeksArtiEN', ''))

        # PL
        item['BentukKataPL'] = BENTUK_KATA_PL.get(b, b)
        item['SuratArtiPL'] = POLISH_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_pl = POLISH_GRAMMAR.get(g_key, {})
        item['ArtiKataPL'] = g_pl.get('arti_pl', item.get('ArtiKataEN', ''))
        item['TeksArtiPL'] = pl_trans.get(v_key, item.get('TeksArtiEN', ''))

        # Grammar dict
        if 'Grammar' not in item or not isinstance(item['Grammar'], dict):
            item['Grammar'] = {}
        if g_no.get('arti_no'): item['Grammar']['arti_no'] = g_no['arti_no']
        if g_no.get('desc_no'): item['Grammar']['desc_no'] = g_no['desc_no']
        if g_no.get('jenis_no'): item['Grammar']['jenis_no'] = g_no['jenis_no']

        if g_pl.get('arti_pl'): item['Grammar']['arti_pl'] = g_pl['arti_pl']
        if g_pl.get('desc_pl'): item['Grammar']['desc_pl'] = g_pl['desc_pl']
        if g_pl.get('jenis_pl'): item['Grammar']['jenis_pl'] = g_pl['jenis_pl']

    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    js_content = f"/**\n * Dataset Dhamir & Isim Jamid Mabny Al-Qur'an 31 Bahasa\n */\nconst DHAMIR_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
    with open(os.path.join(BASE_DIR, 'dhamir_data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"  [OK] Dhamir data enriched ({len(data)} rows).")


def enrich_harf_data():
    print("Enriching harf_data.json and harf_data.js with Norwegian & Polish...")
    with open(os.path.join(BASE_DIR, 'no_translations.json'), 'r', encoding='utf-8') as f:
        no_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'pl_translations.json'), 'r', encoding='utf-8') as f:
        pl_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = str(item.get('No kata', ''))
        g_key = f"{b}__{nk}"
        s_num = str(item.get('SURAT', ''))
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"

        # NO
        item['BentukKataNO'] = BENTUK_HARF_NO.get(b, b)
        item['SuratArtiNO'] = NORWEGIAN_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_no = NORWEGIAN_HARF_GRAMMAR.get(g_key, {})
        item['ArtiKataNO'] = g_no.get('arti_no', item.get('ArtiKataEN', ''))
        item['TeksArtiNO'] = no_trans.get(v_key, item.get('TeksArtiEN', ''))

        # PL
        item['BentukKataPL'] = BENTUK_HARF_PL.get(b, b)
        item['SuratArtiPL'] = POLISH_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_pl = POLISH_HARF_GRAMMAR.get(g_key, {})
        item['ArtiKataPL'] = g_pl.get('arti_pl', item.get('ArtiKataEN', ''))
        item['TeksArtiPL'] = pl_trans.get(v_key, item.get('TeksArtiEN', ''))

        # Grammar dict
        if 'Grammar' not in item or not isinstance(item['Grammar'], dict):
            item['Grammar'] = {}
        if g_no.get('arti_no'): item['Grammar']['arti_no'] = g_no['arti_no']
        if g_no.get('desc_no'): item['Grammar']['desc_no'] = g_no['desc_no']
        if g_no.get('jenis_no'): item['Grammar']['jenis_no'] = g_no['jenis_no']

        if g_pl.get('arti_pl'): item['Grammar']['arti_pl'] = g_pl['arti_pl']
        if g_pl.get('desc_pl'): item['Grammar']['desc_pl'] = g_pl['desc_pl']
        if g_pl.get('jenis_pl'): item['Grammar']['jenis_pl'] = g_pl['jenis_pl']

    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    js_content = f"/**\n * Dataset Harf Ghair 'Amil Al-Qur'an 31 Bahasa\n */\nconst HARF_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
    with open(os.path.join(BASE_DIR, 'harf_data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"  [OK] Harf data enriched ({len(data)} rows).")


if __name__ == '__main__':
    enrich_dhamir_data()
    enrich_harf_data()
