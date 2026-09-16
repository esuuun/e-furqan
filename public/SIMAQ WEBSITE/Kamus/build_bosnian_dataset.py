#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script containing complete Bosnian (bs) dataset metadata:
- 114 Surah Names (BOSNIAN_SURAHS)
- 7 Bentuk Kata Categories (BENTUK_KATA_BS)
- 76 Jamid Mabny Words Grammar (BOSNIAN_GRAMMAR)
- 17 Bentuk Harf Categories (BENTUK_HARF_BS)
- 52 Harf Words Grammar (BOSNIAN_HARF_GRAMMAR)
"""

BOSNIAN_SURAHS = {
    "1": "Pristup (Al-Fatihah)",
    "2": "Krava (Al-Baqarah)",
    "3": "Imranova porodica (Ali 'Imran)",
    "4": "Žene (An-Nisa')",
    "5": "Trpeza (Al-Ma'idah)",
    "6": "Stoka (Al-An'am)",
    "7": "Bedemi (Al-A'raf)",
    "8": "Plijen (Al-Anfal)",
    "9": "Pokajanje (At-Tawbah)",
    "10": "Junus (Yunus)",
    "11": "Hud (Hud)",
    "12": "Jusuf (Yusuf)",
    "13": "Grom (Ar-Ra'd)",
    "14": "Ibrahim (Ibrahim)",
    "15": "Hidžr (Al-Hijr)",
    "16": "Pčele (An-Nahl)",
    "17": "Noćno putovanje (Al-Isra')",
    "18": "Pećina (Al-Kahf)",
    "19": "Merjem (Maryam)",
    "20": "Ta-Ha (Ta-Ha)",
    "21": "Vjerovjesnici (Al-Anbiya')",
    "22": "Hadždž (Al-Hajj)",
    "23": "Vjernici (Al-Mu'minun)",
    "24": "Svjetlost (An-Nur)",
    "25": "Furkan (Al-Furqan)",
    "26": "Pjesnici (Asy-Syu'ara')",
    "27": "Mravi (An-Naml)",
    "28": "Kazivanje (Al-Qasas)",
    "29": "Pauk (Al-'Ankabut)",
    "30": "Bizantinci (Ar-Rum)",
    "31": "Lukman (Luqman)",
    "32": "Sedžda (As-Sajdah)",
    "33": "Saveznici (Al-Ahzab)",
    "34": "Saba (Saba')",
    "35": "Stvoritelj (Fatir)",
    "36": "Ja-Sin (Ya-Sin)",
    "37": "Redovi (As-Saffat)",
    "38": "Sad (Sad)",
    "39": "Skupovi (Az-Zumar)",
    "40": "Oprostnik (Ghafir / Al-Mu'min)",
    "41": "Razjašnjenje (Fussilat)",
    "42": "Dogovaranje (Asy-Syura)",
    "43": "Ukras (Az-Zukhruf)",
    "44": "Dim (Ad-Dukhan)",
    "45": "Oni koji kleče (Al-Jathiyah)",
    "46": "Pješčani brežuljci (Al-Ahqaf)",
    "47": "Muhammed (Muhammad)",
    "48": "Pobjeda (Al-Fath)",
    "49": "Sobe (Al-Hujurat)",
    "50": "Kaf (Qaf)",
    "51": "Oni koji raznose (Adz-Dzariyat)",
    "52": "Gora (At-Tur)",
    "53": "Zvijezda (An-Najm)",
    "54": "Mjesec (Al-Qamar)",
    "55": "Milostivi (Ar-Rahman)",
    "56": "Događaj (Al-Waqi'ah)",
    "57": "Gvožđe (Al-Hadid)",
    "58": "Rasprava (Al-Mujadilah)",
    "59": "Progonstvo (Al-Hasyr)",
    "60": "Provjerena (Al-Mumtahanah)",
    "61": "Bojni red (As-Saff)",
    "62": "Petak (Al-Jumu'ah)",
    "63": "Licemjeri (Al-Munafiqun)",
    "64": "Samoobmana (At-Taghabun)",
    "65": "Razvod braka (At-Talaq)",
    "66": "Zabrana (At-Tahrim)",
    "67": "Vlast (Al-Mulk)",
    "68": "Pero (Al-Qalam)",
    "69": "Neizbježni dan (Al-Haqqah)",
    "70": "Stepeni (Al-Ma'arij)",
    "71": "Nuh (Nuh)",
    "72": "Džini (Al-Jinn)",
    "73": "Umotani (Al-Muzzammil)",
    "74": "Pokriveni (Al-Muddaththir)",
    "75": "Smak svijeta (Al-Qiyamah)",
    "76": "Čovjek (Al-Insan)",
    "77": "Poslani (Al-Mursalat)",
    "78": "Vijest (An-Naba')",
    "79": "Oni koji čupaju (An-Nazi'at)",
    "80": "Namrštio se ('Abasa)",
    "81": "Prestanak sjaja (At-Takwir)",
    "82": "Rascjepljenje (Al-Infitar)",
    "83": "Oni koji pri mjerenju zakidaju (Al-Mutaffifin)",
    "84": "Cijepanje (Al-Insyiqaq)",
    "85": "Sazviježđa (Al-Buruj)",
    "86": "Danica (At-Tariq)",
    "87": "Svevišnji (Al-A'la)",
    "88": "Teška nevolja (Al-Ghasyiyah)",
    "89": "Zora (Al-Fajr)",
    "90": "Grad (Al-Balad)",
    "91": "Sunce (Asy-Syams)",
    "92": "Noć (Al-Lail)",
    "93": "Jutro (Ad-Duha)",
    "94": "Širenje (Asy-Syarh / Al-Insyirah)",
    "95": "Smokva (At-Tin)",
    "96": "Ugrušak (Al-'Alaq)",
    "97": "Noć Kadr (Al-Qadr)",
    "98": "Dokaz jasni (Al-Bayyinah)",
    "99": "Zemljotres (Az-Zalzalah)",
    "100": "Oni koji jure (Al-'Adiyat)",
    "101": "Smak svijeta (Al-Qari'ah)",
    "102": "Nadmetanje (At-Takathur)",
    "103": "Vrijeme (Al-'Asr)",
    "104": "Klevetnik (Al-Humazah)",
    "105": "Slon (Al-Fil)",
    "106": "Kurejšije (Quraisy)",
    "107": "Davanje u naručje (Al-Ma'un)",
    "108": "Mnogo dobro (Al-Kautsar)",
    "109": "Nevjernici (Al-Kafirun)",
    "110": "Pomoć (An-Nasr)",
    "111": "Plamen (Al-Masad / Al-Lahab)",
    "112": "Iskrenost (Al-Ikhlas)",
    "113": "Svitanje (Al-Falaq)",
    "114": "Ljudi (An-Nas)"
}

BENTUK_KATA_BS = {
    "1. Dhamir": "1. Zamjenice (Dhamir - Lične i prisvojne zamjenice)",
    "2. Isim Mawshul": "2. Odnosne zamjenice (Mawshul - Relativne zamjenice)",
    "3. Isim Istifham": "3. Upitne zamjenice (Istifham - Upitne riječi)",
    "4. Isim Syarath": "4. Uslovne imenice (Syarath - Kondicionalne riječi)",
    "5. Isim Isyarah": "5. Pokazne zamjenice (Isyarah - Demonstrativne zamjenice)",
    "6. Isim Fi'il": "6. Glagolske imenice (Isim Fi'il - Verbalne imenice)",
    "7. Fi'il Jamid": "7. Nemenjivi glagoli (Fi'il Jamid - Statični glagoli)"
}

BOSNIAN_GRAMMAR = {
    "1. Dhamir__1a": {
        "arti_bs": "On (muški rod jednine)",
        "desc_bs": "On (3. lice jednine muškog roda, samostalna zamjenica u nominativu)",
        "jenis_bs": "Samostalna nominativna zamjenica"
    },
    "1. Dhamir__1b": {
        "arti_bs": "Njegov / njega / mu",
        "desc_bs": "Njegov / njega (3. lice jednine muškog roda, spojena zamjenica)",
        "jenis_bs": "Spojena zamjenica"
    },
    "1. Dhamir__1c": {
        "arti_bs": "Samo njega",
        "desc_bs": "Samo njega (3. lice jednine muškog roda, samostalna akuzativna zamjenica)",
        "jenis_bs": "Samostalna akuzativna zamjenica"
    },
    "1. Dhamir__2a": {
        "arti_bs": "Njih dvojica / njih dvije",
        "desc_bs": "Njih dvoje (3. lice dvojine, samostalna zamjenica u nominativu)",
        "jenis_bs": "Samostalna nominativna zamjenica (dvojina)"
    },
    "1. Dhamir__2b": {
        "arti_bs": "Njih dvoje / njima dvoma",
        "desc_bs": "Njih dvoje (3. lice dvojine, spojena zamjenica)",
        "jenis_bs": "Spojena zamjenica (dvojina)"
    },
    "1. Dhamir__3a": {
        "arti_bs": "Oni (muški rod množine)",
        "desc_bs": "Oni (3. lice množine muškog roda, samostalna zamjenica u nominativu)",
        "jenis_bs": "Samostalna nominativna zamjenica (množina)"
    },
    "1. Dhamir__3b": {
        "arti_bs": "Njih / im / njihovi",
        "desc_bs": "Njih / im (3. lice množine muškog roda, spojena zamjenica)",
        "jenis_bs": "Spojena zamjenica (množina)"
    },
    "1. Dhamir__3c": {
        "arti_bs": "Samo njih",
        "desc_bs": "Samo njih (3. lice množine muškog roda, samostalna akuzativna zamjenica)",
        "jenis_bs": "Samostalna akuzativna zamjenica (množina)"
    },
    "1. Dhamir__4a": {
        "arti_bs": "Ona (ženski rod jednine)",
        "desc_bs": "Ona (3. lice jednine ženskog roda, samostalna zamjenica u nominativu)",
        "jenis_bs": "Samostalna nominativna zamjenica (ženski rod)"
    },
    "1. Dhamir__4b": {
        "arti_bs": "Njena / nju / joj",
        "desc_bs": "Njena / nju (3. lice jednine ženskog roda, spojena zamjenica)",
        "jenis_bs": "Spojena zamjenica (ženski rod)"
    },
    "1. Dhamir__5a": {
        "arti_bs": "One (ženski rod množine)",
        "desc_bs": "One (3. lice množine ženskog roda, samostalna zamjenica u nominativu)",
        "jenis_bs": "Samostalna nominativna zamjenica (ženski rod množina)"
    },
    "1. Dhamir__5b": {
        "arti_bs": "Njih / im (ženski rod množine)",
        "desc_bs": "Njih / im (3. lice množine ženskog roda, spojena zamjenica)",
        "jenis_bs": "Spojena zamjenica (ženski rod množina)"
    },
    "1. Dhamir__6a": {
        "arti_bs": "Ti (muški rod jednine)",
        "desc_bs": "Ti (2. lice jednine muškog roda, samostalna zamjenica u nominativu)",
        "jenis_bs": "Samostalna nominativna zamjenica"
    },
    "1. Dhamir__6b": {
        "arti_bs": "Tvoj / tebe / ti",
        "desc_bs": "Tvoj / tebe (2. lice jednine muškog roda, spojena zamjenica)",
        "jenis_bs": "Spojena zamjenica"
    },
    "1. Dhamir__6c": {
        "arti_bs": "Samo tebi / samo tebe",
        "desc_bs": "Samo tebe (2. lice jednine muškog roda, samostalna akuzativna zamjenica)",
        "jenis_bs": "Samostalna akuzativna zamjenica"
    },
    "1. Dhamir__7a": {
        "arti_bs": "Vas dvojica / vas dvije",
        "desc_bs": "Vas dvoje (2. lice dvojine, samostalna zamjenica u nominativu)",
        "jenis_bs": "Samostalna nominativna zamjenica (dvojina)"
    },
    "1. Dhamir__7b": {
        "arti_bs": "Vas dvoje (spojeno)",
        "desc_bs": "Vas dvoje (2. lice dvojine, spojena zamjenica)",
        "jenis_bs": "Spojena zamjenica (dvojina)"
    },
    "1. Dhamir__8a": {
        "arti_bs": "Vi (muški rod množine)",
        "desc_bs": "Vi (2. lice množine muškog roda, samostalna zamjenica u nominativu)",
        "jenis_bs": "Samostalna nominativna zamjenica (množina)"
    },
    "1. Dhamir__8b": {
        "arti_bs": "Vas / vam / vaši",
        "desc_bs": "Vas / vam (2. lice množine muškog roda, spojena zamjenica)",
        "jenis_bs": "Spojena zamjenica (množina)"
    },
    "1. Dhamir__8c": {
        "arti_bs": "Samo vama / samo vas",
        "desc_bs": "Samo vas (2. lice množine muškog roda, samostalna akuzativna zamjenica)",
        "jenis_bs": "Samostalna akuzativna zamjenica (množina)"
    },
    "1. Dhamir__9a": {
        "arti_bs": "Ti (ženski rod jednine)",
        "desc_bs": "Ti (2. lice jednine ženskog roda, samostalna zamjenica u nominativu)",
        "jenis_bs": "Samostalna nominativna zamjenica (ženski rod)"
    },
    "1. Dhamir__9b": {
        "arti_bs": "Tvoj / tebi (ženski rod jednine)",
        "desc_bs": "Tvoj / tebe (2. lice jednine ženskog roda, spojena zamjenica)",
        "jenis_bs": "Spojena zamjenica (ženski rod)"
    },
    "1. Dhamir__10a": {
        "arti_bs": "Vi (ženski rod množine)",
        "desc_bs": "Vi (2. lice množine ženskog roda, samostalna zamjenica u nominativu)",
        "jenis_bs": "Samostalna nominativna zamjenica (ženski rod množina)"
    },
    "1. Dhamir__10b": {
        "arti_bs": "Vas / vam (ženski rod množine)",
        "desc_bs": "Vas / vam (2. lice množine ženskog roda, spojena zamjenica)",
        "jenis_bs": "Spojena zamjenica (ženski rod množina)"
    },
    "1. Dhamir__11a": {
        "arti_bs": "Ja (1. lice jednine)",
        "desc_bs": "Ja (1. lice jednine, samostalna zamjenica u nominativu)",
        "jenis_bs": "Samostalna nominativna zamjenica"
    },
    "1. Dhamir__11b": {
        "arti_bs": "Moj / mene / mi",
        "desc_bs": "Moj / mene (1. lice jednine, spojena zamjenica)",
        "jenis_bs": "Spojena zamjenica"
    },
    "1. Dhamir__11c": {
        "arti_bs": "Samo meni / samo mene",
        "desc_bs": "Samo mene (1. lice jednine, samostalna akuzativna zamjenica)",
        "jenis_bs": "Samostalna akuzativna zamjenica"
    },
    "1. Dhamir__12a": {
        "arti_bs": "Mi (1. lice množine)",
        "desc_bs": "Mi (1. lice množine, samostalna zamjenica u nominativu)",
        "jenis_bs": "Samostalna nominativna zamjenica (množina)"
    },
    "1. Dhamir__12b": {
        "arti_bs": "Naš / nas / nam",
        "desc_bs": "Naš / nas (1. lice množine, spojena zamjenica)",
        "jenis_bs": "Spojena zamjenica (množina)"
    },
    "1. Dhamir__12c": {
        "arti_bs": "Samo nama / samo nas",
        "desc_bs": "Samo nas (1. lice množine, samostalna akuzativna zamjenica)",
        "jenis_bs": "Samostalna akuzativna zamjenica (množina)"
    },
    "2. Mawshul__1": {
        "arti_bs": "Ono što / šta",
        "desc_bs": "Opća odnosna zamjenica za neživo i pojmove (Maa)",
        "jenis_bs": "Odnosna zamjenica (za neživo)"
    },
    "2. Mawshul__2": {
        "arti_bs": "Oni koji (muški rod množine)",
        "desc_bs": "Oni koji (odnosna zamjenica za muški rod množine)",
        "jenis_bs": "Odnosna zamjenica (množina)"
    },
    "2. Mawshul__3": {
        "arti_bs": "Onaj ko / ko",
        "desc_bs": "Opća odnosna zamjenica za razumna bića (Man)",
        "jenis_bs": "Opća odnosna zamjenica (za razumna bića)"
    },
    "2. Mawshul__4": {
        "arti_bs": "Onaj koji (muški rod jednine)",
        "desc_bs": "Onaj koji (odnosna zamjenica za muški rod jednine)",
        "jenis_bs": "Odnosna zamjenica (muški rod jednine)"
    },
    "2. Mawshul__5": {
        "arti_bs": "Koji god / ko god od njih",
        "desc_bs": "Koji god / ko od njih (promjenjiva odnosna zamjenica)",
        "jenis_bs": "Odnosna zamjenica"
    },
    "2. Mawshul__6": {
        "arti_bs": "Ona koja (ženski rod jednine)",
        "desc_bs": "Ona koja (odnosna zamjenica za ženski rod jednine)",
        "jenis_bs": "Odnosna zamjenica (ženski rod jednine)"
    },
    "2. Mawshul__7": {
        "arti_bs": "One koje (ženski rod množine)",
        "desc_bs": "One koje (odnosna zamjenica za ženski rod množine)",
        "jenis_bs": "Odnosna zamjenica (ženski rod množina)"
    },
    "2. Mawshul__8": {
        "arti_bs": "One žene koje (varijanta)",
        "desc_bs": "One koje (varijanta odnosne zamjenice za ženski rod množine)",
        "jenis_bs": "Odnosna zamjenica (ženski rod množina)"
    },
    "2. Mawshul__9": {
        "arti_bs": "Njih dvojica koji (dvojina)",
        "desc_bs": "Njih dvojica koji (odnosna zamjenica za dvojinu muškog roda)",
        "jenis_bs": "Odnosna zamjenica (dvojina)"
    },
    "2. Mawshul__10": {
        "arti_bs": "Koja god (ženski rod)",
        "desc_bs": "Koja god (odnosna zamjenica ženskog roda)",
        "jenis_bs": "Odnosna zamjenica (ženski rod)"
    },
    "3. Istifham__1": {
        "arti_bs": "Šta? / Kako?",
        "desc_bs": "Šta? (Upitna zamjenica za stvari i pojmove)",
        "jenis_bs": "Upitna zamjenica"
    },
    "3. Istifham__2": {
        "arti_bs": "Kako?",
        "desc_bs": "Kako? (Upitna riječ za stanje ili način)",
        "jenis_bs": "Upitna riječ za stanje"
    },
    "3. Istifham__3": {
        "arti_bs": "Ko?",
        "desc_bs": "Ko? (Upitna zamjenica za lica i razumna bića)",
        "jenis_bs": "Upitna zamjenica"
    },
    "3. Istifham__4": {
        "arti_bs": "Koji? / Kakav?",
        "desc_bs": "Koji? (Upitna riječ izbora)",
        "jenis_bs": "Upitna zamjenica izbora"
    },
    "3. Istifham__5": {
        "arti_bs": "Kako? / Odakle?",
        "desc_bs": "Odakle? / Kako? (Upitna riječ za porijeklo ili mogućnost)",
        "jenis_bs": "Upitna riječ"
    },
    "3. Istifham__6": {
        "arti_bs": "Šta je to što?",
        "desc_bs": "Šta je to? (Pojačana upitna fraza sa Dhaa)",
        "jenis_bs": "Složena upitna zamjenica"
    },
    "3. Istifham__7": {
        "arti_bs": "Koliko? / Koliko dugo?",
        "desc_bs": "Koliko? (Upitna riječ za broj ili vrijeme)",
        "jenis_bs": "Upitna riječ za količinu"
    },
    "3. Istifham__8": {
        "arti_bs": "Zašto? / Zbog čega?",
        "desc_bs": "Zašto? (Pitanje o uzroku ili razlogu, Li + Maa)",
        "jenis_bs": "Upitna riječ uzroka"
    },
    "3. Istifham__9": {
        "arti_bs": "Gdje? / Kuda?",
        "desc_bs": "Gdje? (Upitna riječ za mjesto)",
        "jenis_bs": "Upitna riječ za mjesto"
    },
    "3. Istifham__10": {
        "arti_bs": "Kada?",
        "desc_bs": "Kada? (Upitna riječ za vrijeme)",
        "jenis_bs": "Upitna riječ za vrijeme"
    },
    "4. Syarath__1": {
        "arti_bs": "Ko god / onaj ko",
        "desc_bs": "Ko god (Uslovna imenica za razumna bića)",
        "jenis_bs": "Uslovna imenica (za lica)"
    },
    "4. Syarath__2": {
        "arti_bs": "Šta god / ma šta",
        "desc_bs": "Šta god (Uslovna imenica za stvari i pojmove)",
        "jenis_bs": "Uslovna imenica (za neživo)"
    },
    "4. Syarath__3": {
        "arti_bs": "Svaki put kada / kad god",
        "desc_bs": "Kad god (Vremenski uslovni prilog)",
        "jenis_bs": "Vremenski uslovni prilog"
    },
    "4. Syarath__4": {
        "arti_bs": "Koji god od njih",
        "desc_bs": "Koji god (Uslovna imenica izbora)",
        "jenis_bs": "Uslovna imenica izbora"
    },
    "4. Syarath__5": {
        "arti_bs": "Koji god rok (pojačano)",
        "desc_bs": "Koji god od dva roka (Uslovna imenica pojačana sa Maa)",
        "jenis_bs": "Pojačana uslovna imenica"
    },
    "5. Isyarah__1": {
        "arti_bs": "Ovaj / taj / to",
        "desc_bs": "Ovaj / taj (Pokazna zamjenica muškog roda jednine)",
        "jenis_bs": "Pokazna zamjenica (muški rod)"
    },
    "5. Isyarah__2": {
        "arti_bs": "Ovi / oni (množina)",
        "desc_bs": "Ovi / oni (Pokazna zamjenica množine)",
        "jenis_bs": "Pokazna zamjenica (množina)"
    },
    "5. Isyarah__3": {
        "arti_bs": "Ova / ta (ženski rod)",
        "desc_bs": "Ova / ta (Pokazna zamjenica ženskog roda jednine)",
        "jenis_bs": "Pokazna zamjenica (ženski rod)"
    },
    "5. Isyarah__4": {
        "arti_bs": "Ona / ta (udaljeno)",
        "desc_bs": "Ona / ta (Pokazna zamjenica za daljinu)",
        "jenis_bs": "Pokazna zamjenica za daljinu"
    },
    "5. Isyarah__5": {
        "arti_bs": "Ovdje (blizina)",
        "desc_bs": "Ovdje (Pokazni prilog mjesta za blizinu)",
        "jenis_bs": "Pokazni prilog mjesta"
    },
    "5. Isyarah__6": {
        "arti_bs": "Tamo / ondje (daljina)",
        "desc_bs": "Tamo (Pokazni prilog mjesta za daljinu)",
        "jenis_bs": "Pokazni prilog mjesta za daljinu"
    },
    "5. Isyarah__7": {
        "arti_bs": "Ova dvojica (dvojina)",
        "desc_bs": "Ova dvojica (Pokazna zamjenica muške dvojine)",
        "jenis_bs": "Pokazna zamjenica (dvojina)"
    },
    "5. Isyarah__8": {
        "arti_bs": "Ove dvije (ženska dvojina)",
        "desc_bs": "Ove dvije (Pokazna zamjenica ženske dvojine)",
        "jenis_bs": "Pokazna zamjenica (ženska dvojina)"
    },
    "6. Isim Fi'il__1": {
        "arti_bs": "Slavljen neka je! (Uzvišenost)",
        "desc_bs": "Slavljen i uzvišen je Allah (Glagolska imenica slavljenja)",
        "jenis_bs": "Glagolska imenica slavljenja"
    },
    "6. Isim Fi'il__2": {
        "arti_bs": "Dajte! / Pokažite!",
        "desc_bs": "Dajte vaš dokaz (Glagolska imenica u imperativu)",
        "jenis_bs": "Glagolska imenica imperativa"
    },
    "6. Isim Fi'il__3": {
        "arti_bs": "Uh! / Eh! (uzvik negodovanja)",
        "desc_bs": "Uh / fuj (Glagolska imenica negodovanja i prezira)",
        "jenis_bs": "Glagolska imenica negodovanja"
    },
    "6. Isim Fi'il__4": {
        "arti_bs": "Daleko je! / Nemoguće je!",
        "desc_bs": "Daleko je / nemoguće je (Glagolska imenica prošlog vremena)",
        "jenis_bs": "Glagolska imenica prošlosti"
    },
    "6. Isim Fi'il__5": {
        "arti_bs": "Pazi! / Čuvaj se!",
        "desc_bs": "Čuvajte se / brinite o sebi (Glagolska imenica opreza)",
        "jenis_bs": "Glagolska imenica upozorenja"
    },
    "6. Isim Fi'il__6": {
        "arti_bs": "Dođite! / Pristupite!",
        "desc_bs": "Dođite ovamo (Glagolska imenica poziva)",
        "jenis_bs": "Glagolska imenica poziva"
    },
    "6. Isim Fi'il__7": {
        "arti_bs": "Evo, uzmite! / Čitajte!",
        "desc_bs": "Evo, uzmite i čitajte moju knjigu (Glagolska imenica ponude)",
        "jenis_bs": "Glagolska imenica davanja"
    },
    "6. Isim Fi'il__8": {
        "arti_bs": "Čudno je! / Kako se čudim!",
        "desc_bs": "Zar ne vidiš / kako se čudim (Glagolska imenica čuđenja)",
        "jenis_bs": "Glagolska imenica čuđenja"
    },
    "7. Fi'il Jamid__1": {
        "arti_bs": "Nije / ne postoji",
        "desc_bs": "Nije (Statični glagol negacije stanja)",
        "jenis_bs": "Nemenjivi glagol negacije"
    },
    "7. Fi'il Jamid__2": {
        "arti_bs": "Divan li je! / Izvrstan li je!",
        "desc_bs": "Divan je / krasan je (Statični glagol pohvale)",
        "jenis_bs": "Nemenjivi glagol pohvale"
    },
    "7. Fi'il Jamid__3": {
        "arti_bs": "Loš li je! / Mrzak li je!",
        "desc_bs": "Loš je / ružan je (Statični glagol pokude)",
        "jenis_bs": "Nemenjivi glagol pokude"
    },
    "7. Fi'il Jamid__4": {
        "arti_bs": "Možda / izgleda da",
        "desc_bs": "Možda / nadati se je (Glagol nade i iščekivanja)",
        "jenis_bs": "Nemenjivi glagol nade"
    },
    "7. Fi'il Jamid__5": {
        "arti_bs": "Grozan li je! / Užasan li je!",
        "desc_bs": "Grozan je / zao je (Statični glagol pokude)",
        "jenis_bs": "Nemenjivi glagol pokude"
    }
}

BENTUK_HARF_BS = {
    "1. Harf Nafyi": "1. Negacijske čestice (Harf Nafyi - Negacija)",
    "2. Harf Tahqiq Taswif": "2. Potvrdne čestice i čestice budućnosti (Tahqiq & Taswif)",
    "3. Harf Syarat": "3. Uslovne čestice (Harf Syarat - Kondicionalne čestice)",
    "4. Harf Mashdariyah": "4. Infinitivne čestice (Harf Mashdariyah)",
    "5. Harf Zaidah": "5. Pojačavajuće / dodatne čestice (Harf Zaidah)",
    "6. Harf Istifham": "6. Upitne čestice (Harf Istifham)",
    "7. Harf Jawab": "7. Čestice odgovora (Harf Jawab)",
    "8. Harf Ibtida'": "8. Početne čestice (Harf Ibtida')",
    "9. Harf Tafshil": "9. Čestice pojašnjenja i detaljisanja (Harf Tafshil)",
    "10. Harf Mufaja'ah": "10. Čestice iznenađenja (Harf Mufaja'ah)",
    "11. Harf Mufassirah": "11. Tumačeće čestice (Harf Mufassirah)",
    "12. Harf Istiftahiyah": "12. Uvodne čestice (Harf Istiftahiyah)",
    "13. Harf Rada'": "13. Čestice odbijanja i ukora (Harf Rada')",
    "14. Harf Ta'ajjub": "14. Čestice čuđenja (Harf Ta'ajjub)",
    "15. Harf Fariqah": "15. Razlikovne čestice (Harf Fariqah)",
    "16. Harf Mauthi'ah": "16. Čestice najave zakletve (Harf Mauthi'ah)",
    "17. Harf Mabany": "17. Konstrukcijske čestice / slova (Harf Mabany)"
}

BOSNIAN_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {
        "arti_bs": "Ne / nije / nema (negacija)",
        "desc_bs": "Opća negacijska čestica (Laa)",
        "jenis_bs": "Negacijska čestica"
    },
    "1. Harf Nafyi__2": {
        "arti_bs": "Ne / nije / ništa",
        "desc_bs": "Negacijska čestica za prošlo i sadašnje vrijeme (Maa)",
        "jenis_bs": "Negacijska čestica"
    },
    "1. Harf Nafyi__3": {
        "arti_bs": "Samo / ništa osim",
        "desc_bs": "Negacijska čestica restrikcije (In... illaa)",
        "jenis_bs": "Negacijska čestica ograničenja"
    },
    "1. Harf Nafyi__4": {
        "arti_bs": "Zar nema? / Zar postoji?",
        "desc_bs": "Retorička negacijska upitna čestica (Hal)",
        "jenis_bs": "Retorička negacijska čestica"
    },
    "1. Harf Nafyi__5": {
        "arti_bs": "Nema (vremena)",
        "desc_bs": "Negacijska čestica za vremenske pojmove (Laata)",
        "jenis_bs": "Vremenska negacijska čestica"
    },
    "1. Harf Nafyi__6": {
        "arti_bs": "Šta drugo nego / ništa",
        "desc_bs": "Složena retorička negacijska upitna čestica (Maadhaa)",
        "jenis_bs": "Složena retorička čestica"
    },
    "2. Harf Tahqiq Taswif__7": {
        "arti_bs": "Doista / već (potvrda)",
        "desc_bs": "Potvrdna čestica sigurnosti (Qad)",
        "jenis_bs": "Potvrdna čestica sigurnosti"
    },
    "2. Harf Tahqiq Taswif__8": {
        "arti_bs": "Kasnije će / sigurno će",
        "desc_bs": "Čestica dalje budućnosti (Sawfa)",
        "jenis_bs": "Čestica dalje budućnosti"
    },
    "3. Harf Syarat__9": {
        "arti_bs": "Da je / kad bi (neostvarivo)",
        "desc_bs": "Uslovna čestica neostvarivog uslova u prošlosti (Law)",
        "jenis_bs": "Uslovna čestica"
    },
    "3. Harf Syarat__10": {
        "arti_bs": "Da nije bilo... sigurno bi",
        "desc_bs": "Uslovna čestica sprečavanja postojanjem drugog (Lawlaa)",
        "jenis_bs": "Uslovna čestica prepreke"
    },
    "3. Harf Syarat__11": {
        "arti_bs": "Čak i da / makar",
        "desc_bs": "Dopusna uslovna čestica (Law)",
        "jenis_bs": "Dopusna uslovna čestica"
    },
    "3. Harf Syarat__12": {
        "arti_bs": "Ako / kad god",
        "desc_bs": "Pojačana uslovna čestica (Immaa = In + Maa)",
        "jenis_bs": "Pojačana uslovna čestica"
    },
    "3. Harf Syarat__13": {
        "arti_bs": "Kakav god znak / ma šta",
        "desc_bs": "Opća uslovna imenica (Mahmaa)",
        "jenis_bs": "Uslovna imenica"
    },
    "4. Harf Mashdariyah__14": {
        "arti_bs": "Dok god / tokom vremena",
        "desc_bs": "Vremenska masdarska čestica (Maa)",
        "jenis_bs": "Masdarska čestica trajanja"
    },
    "4. Harf Mashdariyah__15": {
        "arti_bs": "Da ne / kako ne bi",
        "desc_bs": "Masdarska negacijska čestica (Allaa = An + Laa)",
        "jenis_bs": "Masdarska negacijska čestica"
    },
    "4. Harf Mashdariyah__16": {
        "arti_bs": "Da / kako bi (masdarsko)",
        "desc_bs": "Glagolska masdarska čestica (An)",
        "jenis_bs": "Masdarska čestica"
    },
    "4. Harf Mashdariyah__17": {
        "arti_bs": "Kada bi / da (želja)",
        "desc_bs": "Masdarska čestica želje (Law)",
        "jenis_bs": "Masdarska čestica želje"
    },
    "4. Harf Mashdariyah__18": {
        "arti_bs": "Da ne robujete",
        "desc_bs": "Masdarska čestica zabrane (An + Laa)",
        "jenis_bs": "Masdarska čestica zabrane"
    },
    "4. Harf Mashdariyah__19": {
        "arti_bs": "Da (zaista)",
        "desc_bs": "Olakšana masdarska čestica (An olakšano od Enne)",
        "jenis_bs": "Olakšana masdarska čestica"
    },
    "5. Harf Zaidah__20": {
        "arti_bs": "Kao što / poput",
        "desc_bs": "Poredbena čestica sa dodatnim pojačanjem (Kamaa = Ka + Maa)",
        "jenis_bs": "Pojačavajuća čestica"
    },
    "5. Harf Zaidah__21": {
        "arti_bs": "Bilo kakav primjer",
        "desc_bs": "Neodređena pojačavajuća čestica (Maa Zaidah)",
        "jenis_bs": "Pojačavajući dodatak"
    },
    "5. Harf Zaidah__22": {
        "arti_bs": "Kunem se doista",
        "desc_bs": "Pojačavajuća čestica zakletve (Laa Zaidah)",
        "jenis_bs": "Zakletvena pojačavajuća čestica"
    },
    "5. Harf Zaidah__23": {
        "arti_bs": "Zbog milosti Allahove",
        "desc_bs": "Prijedlog sa dodatnom pojačavajućom česticom (Bimaa = Bi + Maa)",
        "jenis_bs": "Pojačavajuća čestica"
    },
    "5. Harf Zaidah__24": {
        "arti_bs": "Kada je došao donosilac radosne vijesti",
        "desc_bs": "Pojačavajuća čestica nakon vremenskog veznika (An nakon Lammaa)",
        "jenis_bs": "Vremenska pojačavajuća čestica"
    },
    "6. Harf Istifham__25": {
        "arti_bs": "Da li? / Zar?",
        "desc_bs": "Upitna čestica potvrde (Hal)",
        "jenis_bs": "Upitna čestica"
    },
    "7. Harf Jawab__26": {
        "arti_bs": "U tom slučaju / onda",
        "desc_bs": "Čestica odgovora i posljedice (Idhan)",
        "jenis_bs": "Čestica posljedice"
    },
    "7. Harf Jawab__27": {
        "arti_bs": "Svakako / da dakako!",
        "desc_bs": "Čestica pobijanja negacije u potvrdan odgovor (Belaa)",
        "jenis_bs": "Potvrdna čestica odgovora"
    },
    "7. Harf Jawab__28": {
        "arti_bs": "Da / jeste",
        "desc_bs": "Čestica slaganja i potvrde (Na'am)",
        "jenis_bs": "Čestica odgovora"
    },
    "7. Harf Jawab__29": {
        "arti_bs": "Da, tako mi Gospodara!",
        "desc_bs": "Zakletvena potvrdna čestica odgovora (I / Ii)",
        "jenis_bs": "Zakletvena čestica odgovora"
    },
    "8. Harf Ibtida'__30": {
        "arti_bs": "Sve dok / dotle da",
        "desc_bs": "Početna ciljna čestica (Hattaa)",
        "jenis_bs": "Početna čestica"
    },
    "9. Harf Tafshil__31": {
        "arti_bs": "Što se tiče / a što se tiče",
        "desc_bs": "Čestica uvođenja, pojašnjenja i uslova (Ammaa)",
        "jenis_bs": "Čestica detaljisanja"
    },
    "10. Harf Mufaja'ah__32": {
        "arti_bs": "Kad odjednom / iznenada",
        "desc_bs": "Čestica iznenadnog događaja (Idhaa)",
        "jenis_bs": "Čestica iznenađenja"
    },
    "11. Harf Mufassirah__33": {
        "arti_bs": "Naime / to jest",
        "desc_bs": "Tumačeća pojašnjavajuća čestica (An)",
        "jenis_bs": "Tumačeća čestica"
    },
    "12. Harf Istiftahiyah__34": {
        "arti_bs": "Pazite! / Znajte!",
        "desc_bs": "Uvodna čestica privlačenja pažnje i upozorenja (Alaa)",
        "jenis_bs": "Uvodna čestica pažnje"
    },
    "13. Harf Rada'__35": {
        "arti_bs": "Nikako! / Nipošto!",
        "desc_bs": "Čestica strogog odbijanja i ukora (Kallaa)",
        "jenis_bs": "Čestica ukora i odbijanja"
    },
    "14. Harf Ta'ajjub__36": {
        "arti_bs": "Kako su samo strpljivi!",
        "desc_bs": "Čestica ushićenja i čuđenja (Maa Ta'ajjubiyyah)",
        "jenis_bs": "Čestica čuđenja"
    },
    "15. Harf Fariqah__37": {
        "arti_bs": "Doista / sigurno",
        "desc_bs": "Razlikovno pojačavajuće Lam (Lam Fariqah uz olakšano In)",
        "jenis_bs": "Razlikovno Lam"
    },
    "16. Harf Mauthi'ah__38": {
        "arti_bs": "Ako... onda se zaista kunem",
        "desc_bs": "Čestica najave uslovne zakletve (La-in)",
        "jenis_bs": "Najavno Lam zakletve"
    },
    "17. Harf Mabany__39": {
        "arti_bs": "Ha-Mim",
        "desc_bs": "Skraćena kur'anska slova na početku sure (حم)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "17. Harf Mabany__40": {
        "arti_bs": "Alif-Lam-Mim",
        "desc_bs": "Skraćena kur'anska slova na početku sure (الم)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "17. Harf Mabany__41": {
        "arti_bs": "Alif-Lam-Ra",
        "desc_bs": "Skraćena kur'anska slova na početku sure (الر)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "17. Harf Mabany__42": {
        "arti_bs": "Ta-Sin-Mim",
        "desc_bs": "Skraćena kur'anska slova na početku sure (طسم)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "17. Harf Mabany__43": {
        "arti_bs": "Alif-Lam-Mim-Ra",
        "desc_bs": "Skraćena kur'anska slova na početku sure (المر)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "17. Harf Mabany__44": {
        "arti_bs": "Alif-Lam-Mim-Sad",
        "desc_bs": "Skraćena kur'anska slova na početku sure (المص)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "17. Harf Mabany__45": {
        "arti_bs": "Sad",
        "desc_bs": "Skraćeno kur'ansko slovo na početku sure (ص)",
        "jenis_bs": "Kur'anska skraćenica (Mukatta'at)"
    },
    "17. Harf Mabany__46": {
        "arti_bs": "Ta-Sin",
        "desc_bs": "Skraćena kur'anska slova na početku sure (طس)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "17. Harf Mabany__47": {
        "arti_bs": "Ta-Ha",
        "desc_bs": "Skraćena kur'anska slova na početku sure (طه)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "17. Harf Mabany__48": {
        "arti_bs": "'Ajn-Sin-Kaf",
        "desc_bs": "Skraćena kur'anska slova na početku sure (عسق)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "17. Harf Mabany__49": {
        "arti_bs": "Kaf",
        "desc_bs": "Skraćeno kur'ansko slovo na početku sure (ق)",
        "jenis_bs": "Kur'anska skraćenica (Mukatta'at)"
    },
    "17. Harf Mabany__50": {
        "arti_bs": "Kaf-Ha-Ja-'Ajn-Sad",
        "desc_bs": "Skraćena kur'anska slova na početku sure (كهيعص)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "17. Harf Mabany__51": {
        "arti_bs": "Nun",
        "desc_bs": "Skraćeno kur'ansko slovo na početku sure (ن)",
        "jenis_bs": "Kur'anska skraćenica (Mukatta'at)"
    },
    "17. Harf Mabany__52": {
        "arti_bs": "Ja-Sin",
        "desc_bs": "Skraćena kur'anska slova na početku sure (يس)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "1": {
        "arti_bs": "Ne / nije / nema (negacija)",
        "desc_bs": "Opća negacijska čestica (Laa)",
        "jenis_bs": "Negacijska čestica"
    },
    "2": {
        "arti_bs": "Ne / nije / ništa",
        "desc_bs": "Negacijska čestica za prošlo i sadašnje vrijeme (Maa)",
        "jenis_bs": "Negacijska čestica"
    },
    "3": {
        "arti_bs": "Samo / ništa osim",
        "desc_bs": "Negacijska čestica restrikcije (In... illaa)",
        "jenis_bs": "Negacijska čestica ograničenja"
    },
    "4": {
        "arti_bs": "Zar nema? / Zar postoji?",
        "desc_bs": "Retorička negacijska upitna čestica (Hal)",
        "jenis_bs": "Retorička negacijska čestica"
    },
    "5": {
        "arti_bs": "Nema (vremena)",
        "desc_bs": "Negacijska čestica za vremenske pojmove (Laata)",
        "jenis_bs": "Vremenska negacijska čestica"
    },
    "6": {
        "arti_bs": "Šta drugo nego / ništa",
        "desc_bs": "Složena retorička negacijska upitna čestica (Maadhaa)",
        "jenis_bs": "Složena retorička čestica"
    },
    "7": {
        "arti_bs": "Doista / već (potvrda)",
        "desc_bs": "Potvrdna čestica sigurnosti (Qad)",
        "jenis_bs": "Potvrdna čestica sigurnosti"
    },
    "8": {
        "arti_bs": "Kasnije će / sigurno će",
        "desc_bs": "Čestica dalje budućnosti (Sawfa)",
        "jenis_bs": "Čestica dalje budućnosti"
    },
    "9": {
        "arti_bs": "Da je / kad bi (neostvarivo)",
        "desc_bs": "Uslovna čestica neostvarivog uslova u prošlosti (Law)",
        "jenis_bs": "Uslovna čestica"
    },
    "10": {
        "arti_bs": "Da nije bilo... sigurno bi",
        "desc_bs": "Uslovna čestica sprečavanja postojanjem drugog (Lawlaa)",
        "jenis_bs": "Uslovna čestica prepreke"
    },
    "11": {
        "arti_bs": "Čak i da / makar",
        "desc_bs": "Dopusna uslovna čestica (Law)",
        "jenis_bs": "Dopusna uslovna čestica"
    },
    "12": {
        "arti_bs": "Ako / kad god",
        "desc_bs": "Pojačana uslovna čestica (Immaa = In + Maa)",
        "jenis_bs": "Pojačana uslovna čestica"
    },
    "13": {
        "arti_bs": "Kakav god znak / ma šta",
        "desc_bs": "Opća uslovna imenica (Mahmaa)",
        "jenis_bs": "Uslovna imenica"
    },
    "14": {
        "arti_bs": "Dok god / tokom vremena",
        "desc_bs": "Vremenska masdarska čestica (Maa)",
        "jenis_bs": "Masdarska čestica trajanja"
    },
    "15": {
        "arti_bs": "Da ne / kako ne bi",
        "desc_bs": "Masdarska negacijska čestica (Allaa = An + Laa)",
        "jenis_bs": "Masdarska negacijska čestica"
    },
    "16": {
        "arti_bs": "Da / kako bi (masdarsko)",
        "desc_bs": "Glagolska masdarska čestica (An)",
        "jenis_bs": "Masdarska čestica"
    },
    "17": {
        "arti_bs": "Kada bi / da (želja)",
        "desc_bs": "Masdarska čestica želje (Law)",
        "jenis_bs": "Masdarska čestica želje"
    },
    "18": {
        "arti_bs": "Da ne robujete",
        "desc_bs": "Masdarska čestica zabrane (An + Laa)",
        "jenis_bs": "Masdarska čestica zabrane"
    },
    "19": {
        "arti_bs": "Da (zaista)",
        "desc_bs": "Olakšana masdarska čestica (An olakšano od Enne)",
        "jenis_bs": "Olakšana masdarska čestica"
    },
    "20": {
        "arti_bs": "Kao što / poput",
        "desc_bs": "Poredbena čestica sa dodatnim pojačanjem (Kamaa = Ka + Maa)",
        "jenis_bs": "Pojačavajuća čestica"
    },
    "21": {
        "arti_bs": "Bilo kakav primjer",
        "desc_bs": "Neodređena pojačavajuća čestica (Maa Zaidah)",
        "jenis_bs": "Pojačavajući dodatak"
    },
    "22": {
        "arti_bs": "Kunem se doista",
        "desc_bs": "Pojačavajuća čestica zakletve (Laa Zaidah)",
        "jenis_bs": "Zakletvena pojačavajuća čestica"
    },
    "23": {
        "arti_bs": "Zbog milosti Allahove",
        "desc_bs": "Prijedlog sa dodatnom pojačavajućom česticom (Bimaa = Bi + Maa)",
        "jenis_bs": "Pojačavajuća čestica"
    },
    "24": {
        "arti_bs": "Kada je došao donosilac radosne vijesti",
        "desc_bs": "Pojačavajuća čestica nakon vremenskog veznika (An nakon Lammaa)",
        "jenis_bs": "Vremenska pojačavajuća čestica"
    },
    "25": {
        "arti_bs": "Da li? / Zar?",
        "desc_bs": "Upitna čestica potvrde (Hal)",
        "jenis_bs": "Upitna čestica"
    },
    "26": {
        "arti_bs": "U tom slučaju / onda",
        "desc_bs": "Čestica odgovora i posljedice (Idhan)",
        "jenis_bs": "Čestica posljedice"
    },
    "27": {
        "arti_bs": "Svakako / da dakako!",
        "desc_bs": "Čestica pobijanja negacije u potvrdan odgovor (Belaa)",
        "jenis_bs": "Potvrdna čestica odgovora"
    },
    "28": {
        "arti_bs": "Da / jeste",
        "desc_bs": "Čestica slaganja i potvrde (Na'am)",
        "jenis_bs": "Čestica odgovora"
    },
    "29": {
        "arti_bs": "Da, tako mi Gospodara!",
        "desc_bs": "Zakletvena potvrdna čestica odgovora (I / Ii)",
        "jenis_bs": "Zakletvena čestica odgovora"
    },
    "30": {
        "arti_bs": "Sve dok / dotle da",
        "desc_bs": "Početna ciljna čestica (Hattaa)",
        "jenis_bs": "Početna čestica"
    },
    "31": {
        "arti_bs": "Što se tiče / a što se tiče",
        "desc_bs": "Čestica uvođenja, pojašnjenja i uslova (Ammaa)",
        "jenis_bs": "Čestica detaljisanja"
    },
    "32": {
        "arti_bs": "Kad odjednom / iznenada",
        "desc_bs": "Čestica iznenadnog događaja (Idhaa)",
        "jenis_bs": "Čestica iznenađenja"
    },
    "33": {
        "arti_bs": "Naime / to jest",
        "desc_bs": "Tumačeća pojašnjavajuća čestica (An)",
        "jenis_bs": "Tumačeća čestica"
    },
    "34": {
        "arti_bs": "Pazite! / Znajte!",
        "desc_bs": "Uvodna čestica privlačenja pažnje i upozorenja (Alaa)",
        "jenis_bs": "Uvodna čestica pažnje"
    },
    "35": {
        "arti_bs": "Nikako! / Nipošto!",
        "desc_bs": "Čestica strogog odbijanja i ukora (Kallaa)",
        "jenis_bs": "Čestica ukora i odbijanja"
    },
    "36": {
        "arti_bs": "Kako su samo strpljivi!",
        "desc_bs": "Čestica ushićenja i čuđenja (Maa Ta'ajjubiyyah)",
        "jenis_bs": "Čestica čuđenja"
    },
    "37": {
        "arti_bs": "Doista / sigurno",
        "desc_bs": "Razlikovno pojačavajuće Lam (Lam Fariqah uz olakšano In)",
        "jenis_bs": "Razlikovno Lam"
    },
    "38": {
        "arti_bs": "Ako... onda se zaista kunem",
        "desc_bs": "Čestica najave uslovne zakletve (La-in)",
        "jenis_bs": "Najavno Lam zakletve"
    },
    "39": {
        "arti_bs": "Ha-Mim",
        "desc_bs": "Skraćena kur'anska slova na početku sure (حم)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "40": {
        "arti_bs": "Alif-Lam-Mim",
        "desc_bs": "Skraćena kur'anska slova na početku sure (الم)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "41": {
        "arti_bs": "Alif-Lam-Ra",
        "desc_bs": "Skraćena kur'anska slova na početku sure (الر)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "42": {
        "arti_bs": "Ta-Sin-Mim",
        "desc_bs": "Skraćena kur'anska slova na početku sure (طسم)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "43": {
        "arti_bs": "Alif-Lam-Mim-Ra",
        "desc_bs": "Skraćena kur'anska slova na početku sure (المر)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "44": {
        "arti_bs": "Alif-Lam-Mim-Sad",
        "desc_bs": "Skraćena kur'anska slova na početku sure (المص)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "45": {
        "arti_bs": "Sad",
        "desc_bs": "Skraćeno kur'ansko slovo na početku sure (ص)",
        "jenis_bs": "Kur'anska skraćenica (Mukatta'at)"
    },
    "46": {
        "arti_bs": "Ta-Sin",
        "desc_bs": "Skraćena kur'anska slova na početku sure (طس)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "47": {
        "arti_bs": "Ta-Ha",
        "desc_bs": "Skraćena kur'anska slova na početku sure (طه)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "48": {
        "arti_bs": "'Ajn-Sin-Kaf",
        "desc_bs": "Skraćena kur'anska slova na početku sure (عسق)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "49": {
        "arti_bs": "Kaf",
        "desc_bs": "Skraćeno kur'ansko slovo na početku sure (ق)",
        "jenis_bs": "Kur'anska skraćenica (Mukatta'at)"
    },
    "50": {
        "arti_bs": "Kaf-Ha-Ja-'Ajn-Sad",
        "desc_bs": "Skraćena kur'anska slova na početku sure (كهيعص)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    },
    "51": {
        "arti_bs": "Nun",
        "desc_bs": "Skraćeno kur'ansko slovo na početku sure (ن)",
        "jenis_bs": "Kur'anska skraćenica (Mukatta'at)"
    },
    "52": {
        "arti_bs": "Ja-Sin",
        "desc_bs": "Skraćena kur'anska slova na početku sure (يس)",
        "jenis_bs": "Kur'anske skraćenice (Mukatta'at)"
    }
}
