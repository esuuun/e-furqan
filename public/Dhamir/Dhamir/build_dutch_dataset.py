#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script containing complete Dutch (nl) dataset metadata:
- 114 Surah Names (DUTCH_SURAHS)
- 7 Bentuk Kata Categories (BENTUK_KATA_NL)
- 76 Jamid Mabny Words Grammar (DUTCH_GRAMMAR)
- 17 Bentuk Harf Categories (BENTUK_HARF_NL)
- 52 Harf Words Grammar (DUTCH_HARF_GRAMMAR)
"""

DUTCH_SURAHS = {
    "1": "De Opening (Al-Fatihah)",
    "2": "De Koe (Al-Baqarah)",
    "3": "Het Huis van Imraan (Ali 'Imran)",
    "4": "De Vrouwen (An-Nisa')",
    "5": "De Tafel (Al-Ma'idah)",
    "6": "Het Vee (Al-An'am)",
    "7": "De Hoogten (Al-A'raf)",
    "8": "De Oorlogsbuit (Al-Anfal)",
    "9": "Het Berouw (At-Tawbah)",
    "10": "Jonas (Yunus)",
    "11": "Hoed (Hud)",
    "12": "Jozef (Yusuf)",
    "13": "De Donder (Ar-Ra'd)",
    "14": "Abraham (Ibrahim)",
    "15": "Het Rotsachtige Land (Al-Hijr)",
    "16": "De Bij (An-Nahl)",
    "17": "De Nachtreis (Al-Isra')",
    "18": "De Grot (Al-Kahf)",
    "19": "Maria (Maryam)",
    "20": "Ta Ha (Ta-Ha)",
    "21": "De Profeten (Al-Anbiya')",
    "22": "De Bedevaart (Al-Hajj)",
    "23": "De Gelovigen (Al-Mu'minun)",
    "24": "Het Licht (An-Nur)",
    "25": "Het Onderscheid (Al-Furqan)",
    "26": "De Dichters (Asy-Syu'ara')",
    "27": "De Mieren (An-Naml)",
    "28": "Het Verhaal (Al-Qasas)",
    "29": "De Spin (Al-'Ankabut)",
    "30": "De Romeinen (Ar-Rum)",
    "31": "Loeqman (Luqman)",
    "32": "De Prosternatie (As-Sajdah)",
    "33": "De Bondgenoten (Al-Ahzab)",
    "34": "Saba' (Saba')",
    "35": "De Grondlegger (Fatir)",
    "36": "Ya Sin (Ya-Sin)",
    "37": "Degenen die in Rangen Staan (As-Saffat)",
    "38": "Sad (Sad)",
    "39": "De Groepen (Az-Zumar)",
    "40": "De Vergever (Ghafir / Al-Mu'min)",
    "41": "Uiteengezet (Fussilat)",
    "42": "Het Beraad (Asy-Syura)",
    "43": "Gouden Pracht (Az-Zukhruf)",
    "44": "De Rook (Ad-Dukhan)",
    "45": "Het Knielen (Al-Jathiyah)",
    "46": "De Zandduinen (Al-Ahqaf)",
    "47": "Mohammed (Muhammad)",
    "48": "De Overwinning (Al-Fath)",
    "49": "De Binnenkamers (Al-Hujurat)",
    "50": "Qaf (Qaf)",
    "51": "De Strooiende Winden (Adz-Dzariyat)",
    "52": "De Berg (At-Tur)",
    "53": "De Ster (An-Najm)",
    "54": "De Maan (Al-Qamar)",
    "55": "De Barmhartige (Ar-Rahman)",
    "56": "De Onoverkomelijke Gebeurtenis (Al-Waqi'ah)",
    "57": "Het IJzer (Al-Hadid)",
    "58": "De Pleitende Vrouw (Al-Mujadilah)",
    "59": "De Verbanning (Al-Hasyr)",
    "60": "De Ondervraagde Vrouw (Al-Mumtahanah)",
    "61": "De Gelederen (As-Saff)",
    "62": "De Vrijdagbijeenkomst (Al-Jumu'ah)",
    "63": "De Huichelaars (Al-Munafiqun)",
    "64": "Wederzijds Verlies en Winst (At-Taghabun)",
    "65": "De Scheiding (At-Talaq)",
    "66": "Het Verbod (At-Tahrim)",
    "67": "De Heerschappij (Al-Mulk)",
    "68": "De Pen (Al-Qalam)",
    "69": "De Werkelijkheid (Al-Haqqah)",
    "70": "De Wegen van Opstijging (Al-Ma'arij)",
    "71": "Noach (Nuh)",
    "72": "De Djinn (Al-Jinn)",
    "73": "De Ommantelde (Al-Muzzammil)",
    "74": "De Omgorde (Al-Muddaththir)",
    "75": "De Wederopstanding (Al-Qiyamah)",
    "76": "De Mens (Al-Insan)",
    "77": "De Uitgezondenen (Al-Mursalat)",
    "78": "De Grote Aankondiging (An-Naba')",
    "79": "Degenen die Uitrukken (An-Nazi'at)",
    "80": "Hij Fronste ('Abasa)",
    "81": "Het Oprollen (At-Takwir)",
    "82": "De Splijting (Al-Infitar)",
    "83": "De Oplichters (Al-Mutaffifin)",
    "84": "De Scheuring (Al-Insyiqaq)",
    "85": "De Sterrenbeelden (Al-Buruj)",
    "86": "De Nachtelijke Bezoeker (At-Tariq)",
    "87": "De Allerhoogste (Al-A'la)",
    "88": "De Overstelpende Gebeurtenis (Al-Ghasyiyah)",
    "89": "De Dageraad (Al-Fajr)",
    "90": "De Stad (Al-Balad)",
    "91": "De Zon (Asy-Syams)",
    "92": "De Nacht (Al-Lail)",
    "93": "De Ochtendstond (Ad-Duha)",
    "94": "De Verlichting (Asy-Syarh / Al-Insyirah)",
    "95": "De Vijgenboom (At-Tin)",
    "96": "De Bloedklonter (Al-'Alaq)",
    "97": "De Waardevolle Nacht (Al-Qadr)",
    "98": "Het Duidelijke Bewijs (Al-Bayyinah)",
    "99": "De Beving (Az-Zalzalah)",
    "100": "De Rennende Paarden (Al-'Adiyat)",
    "101": "De Rampramp (Al-Qari'ah)",
    "102": "De Vermeerdering (At-Takathur)",
    "103": "De Tijd (Al-'Asr)",
    "104": "De Lasteraar (Al-Humazah)",
    "105": "De Olifant (Al-Fil)",
    "106": "Qoeraisj (Quraisy)",
    "107": "De Noodzakelijke Hulp (Al-Ma'un)",
    "108": "De Overvloed (Al-Kautsar)",
    "109": "De Ongelovigen (Al-Kafirun)",
    "110": "De Hulp (An-Nasr)",
    "111": "De Palmvezels (Al-Masad / Al-Lahab)",
    "112": "De Zuiverheid van Geloof (Al-Ikhlas)",
    "113": "De Dageraad (Al-Falaq)",
    "114": "De Mensheid (An-Nas)"
}

BENTUK_KATA_NL = {
    "1. Dhamir": "1. Voornaamwoorden (Dhamir - Persoonlijke & Bezittelijke Voornaamwoorden)",
    "2. Isim Mawshul": "2. Betrekkelijke Voornaamwoorden (Mawshul - Relatieve Voornaamwoorden)",
    "3. Isim Istifham": "3. Vragende Voornaamwoorden (Istifham - Vraagelementen)",
    "4. Isim Syarath": "4. Voorwaardelijke Zelfstandige Naamwoorden (Syarath - Conditionele Nomina)",
    "5. Isim Isyarah": "5. Aanwijzende Voornaamwoorden (Isyarah - Demonstratieve Voornaamwoorden)",
    "6. Isim Fi'il": "6. Werkwoordelijke Zelfstandige Naamwoorden (Isim Fi'il - Verbale Nomina)",
    "7. Fi'il Jamid": "7. Niet-vervoegbare Werkwoorden (Fi'il Jamid - Onvervoegde Werkwoorden)"
}

DUTCH_GRAMMAR = {
    "1. Dhamir__1a": {
        "arti_nl": "Hij (mannelijk enkelvoud)",
        "desc_nl": "Hij (3e persoon mannelijk enkelvoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord"
    },
    "1. Dhamir__1b": {
        "arti_nl": "Zijn / hem",
        "desc_nl": "Zijn / hem (3e persoon mannelijk enkelvoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord"
    },
    "1. Dhamir__1c": {
        "arti_nl": "Alleen hem",
        "desc_nl": "Alleen hem (3e persoon mannelijk enkelvoud losstaand accusatief voornaamwoord)",
        "jenis_nl": "Losstaand accusatief voornaamwoord"
    },
    "1. Dhamir__2a": {
        "arti_nl": "Zij beiden",
        "desc_nl": "Zij beiden (3e persoon tweevoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (tweevoud)"
    },
    "1. Dhamir__2b": {
        "arti_nl": "Hun beiden / hen beiden",
        "desc_nl": "Hun beiden / hen beiden (3e persoon tweevoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (tweevoud)"
    },
    "1. Dhamir__3a": {
        "arti_nl": "Zij (mannelijk meervoud)",
        "desc_nl": "Zij (3e persoon mannelijk meervoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (meervoud)"
    },
    "1. Dhamir__3b": {
        "arti_nl": "Hun / hen (mannelijk meervoud)",
        "desc_nl": "Hun / hen (3e persoon mannelijk meervoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (meervoud)"
    },
    "1. Dhamir__3c": {
        "arti_nl": "Alleen hen (mannelijk meervoud)",
        "desc_nl": "Alleen hen (3e persoon mannelijk meervoud losstaand accusatief voornaamwoord)",
        "jenis_nl": "Losstaand accusatief voornaamwoord (meervoud)"
    },
    "1. Dhamir__4a": {
        "arti_nl": "Zij (vrouwelijk enkelvoud)",
        "desc_nl": "Zij (3e persoon vrouwelijk enkelvoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (vrouwelijk)"
    },
    "1. Dhamir__4b": {
        "arti_nl": "Haar (vrouwelijk enkelvoud)",
        "desc_nl": "Haar (3e persoon vrouwelijk enkelvoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (vrouwelijk)"
    },
    "1. Dhamir__5a": {
        "arti_nl": "Zij (vrouwelijk meervoud)",
        "desc_nl": "Zij (3e persoon vrouwelijk meervoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (vrouwelijk meervoud)"
    },
    "1. Dhamir__5b": {
        "arti_nl": "Hun / hen (vrouwelijk meervoud)",
        "desc_nl": "Hun / hen (3e persoon vrouwelijk meervoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (vrouwelijk meervoud)"
    },
    "1. Dhamir__6a": {
        "arti_nl": "Jij / u (mannelijk enkelvoud)",
        "desc_nl": "Jij / u (2e persoon mannelijk enkelvoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord"
    },
    "1. Dhamir__6b": {
        "arti_nl": "Jouw / je / jou (mannelijk enkelvoud)",
        "desc_nl": "Jouw / je / jou (2e persoon mannelijk enkelvoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord"
    },
    "1. Dhamir__6c": {
        "arti_nl": "Alleen jou / u (mannelijk enkelvoud)",
        "desc_nl": "Alleen jou / u (2e persoon mannelijk enkelvoud losstaand accusatief voornaamwoord)",
        "jenis_nl": "Losstaand accusatief voornaamwoord"
    },
    "1. Dhamir__7a": {
        "arti_nl": "Jullie beiden",
        "desc_nl": "Jullie beiden (2e persoon tweevoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (tweevoud)"
    },
    "1. Dhamir__7b": {
        "arti_nl": "Jullie beiden (aangehecht)",
        "desc_nl": "Jullie beiden (2e persoon tweevoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (tweevoud)"
    },
    "1. Dhamir__8a": {
        "arti_nl": "Jullie (mannelijk meervoud)",
        "desc_nl": "Jullie (2e persoon mannelijk meervoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (meervoud)"
    },
    "1. Dhamir__8b": {
        "arti_nl": "Jullie (aangehecht mannelijk meervoud)",
        "desc_nl": "Jullie / uw (2e persoon mannelijk meervoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (meervoud)"
    },
    "1. Dhamir__8c": {
        "arti_nl": "Alleen jullie (mannelijk meervoud)",
        "desc_nl": "Alleen jullie (2e persoon mannelijk meervoud losstaand accusatief voornaamwoord)",
        "jenis_nl": "Losstaand accusatief voornaamwoord (meervoud)"
    },
    "1. Dhamir__9a": {
        "arti_nl": "Jij / u (vrouwelijk enkelvoud)",
        "desc_nl": "Jij / u (2e persoon vrouwelijk enkelvoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (vrouwelijk)"
    },
    "1. Dhamir__9b": {
        "arti_nl": "Jouw / je (vrouwelijk enkelvoud)",
        "desc_nl": "Jouw / je (2e persoon vrouwelijk enkelvoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (vrouwelijk)"
    },
    "1. Dhamir__10a": {
        "arti_nl": "Jullie (vrouwelijk meervoud)",
        "desc_nl": "Jullie (2e persoon vrouwelijk meervoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (vrouwelijk meervoud)"
    },
    "1. Dhamir__10b": {
        "arti_nl": "Jullie (aangehecht vrouwelijk meervoud)",
        "desc_nl": "Jullie / uw (2e persoon vrouwelijk meervoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (vrouwelijk meervoud)"
    },
    "1. Dhamir__11a": {
        "arti_nl": "Ik (1e persoon enkelvoud)",
        "desc_nl": "Ik (1e persoon enkelvoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord"
    },
    "1. Dhamir__11b": {
        "arti_nl": "Mijn / mij",
        "desc_nl": "Mijn / mij (1e persoon enkelvoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord"
    },
    "1. Dhamir__11c": {
        "arti_nl": "Alleen mij",
        "desc_nl": "Alleen mij (1e persoon enkelvoud losstaand accusatief voornaamwoord)",
        "jenis_nl": "Losstaand accusatief voornaamwoord"
    },
    "1. Dhamir__12a": {
        "arti_nl": "Wij (1e persoon meervoud)",
        "desc_nl": "Wij (1e persoon meervoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (meervoud)"
    },
    "1. Dhamir__12b": {
        "arti_nl": "Ons / onze",
        "desc_nl": "Ons / onze (1e persoon meervoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (meervoud)"
    },
    "1. Dhamir__12c": {
        "arti_nl": "Alleen ons",
        "desc_nl": "Alleen ons (1e persoon meervoud losstaand accusatief voornaamwoord)",
        "jenis_nl": "Losstaand accusatief voornaamwoord (meervoud)"
    },
    "2. Mawshul__1": {
        "arti_nl": "Wat / datgene wat",
        "desc_nl": "Algemeen betrekkelijk voornaamwoord voor niet-rationele zaken (Maa)",
        "jenis_nl": "Betrekkelijk voornaamwoord (niet-rationeel)"
    },
    "2. Mawshul__2": {
        "arti_nl": "Degenen die (mannelijk meervoud)",
        "desc_nl": "Zij die / degenen die (mannelijk meervoud betrekkelijk voornaamwoord)",
        "jenis_nl": "Betrekkelijk voornaamwoord (meervoud mannelijk)"
    },
    "2. Mawshul__3": {
        "arti_nl": "Wie / degene die",
        "desc_nl": "Algemeen betrekkelijk voornaamwoord voor rationele wezens (Man)",
        "jenis_nl": "Algemeen betrekkelijk voornaamwoord (rationeel)"
    },
    "2. Mawshul__4": {
        "arti_nl": "Degene die (mannelijk enkelvoud)",
        "desc_nl": "Degene die / dat (mannelijk enkelvoud betrekkelijk voornaamwoord)",
        "jenis_nl": "Betrekkelijk voornaamwoord (mannelijk enkelvoud)"
    },
    "2. Mawshul__5": {
        "arti_nl": "Welke / wie dan ook",
        "desc_nl": "Welke / wie van hen (verbuigbaar betrekkelijk voornaamwoord)",
        "jenis_nl": "Betrekkelijk voornaamwoord"
    },
    "2. Mawshul__6": {
        "arti_nl": "Zij die (vrouwelijk enkelvoud)",
        "desc_nl": "Zij die / datgene wat (vrouwelijk enkelvoud betrekkelijk voornaamwoord)",
        "jenis_nl": "Betrekkelijk voornaamwoord (vrouwelijk enkelvoud)"
    },
    "2. Mawshul__7": {
        "arti_nl": "Vrouwen die (meervoud vrouwelijk)",
        "desc_nl": "Zij die (vrouwelijk meervoud betrekkelijk voornaamwoord)",
        "jenis_nl": "Betrekkelijk voornaamwoord (meervoud vrouwelijk)"
    },
    "2. Mawshul__8": {
        "arti_nl": "Vrouwen die (meervoud vrouwelijk variant)",
        "desc_nl": "Zij die (vrouwelijk meervoud betrekkelijk voornaamwoord variant)",
        "jenis_nl": "Betrekkelijk voornaamwoord (meervoud vrouwelijk)"
    },
    "2. Mawshul__9": {
        "arti_nl": "Zij beiden die (tweevoud mannelijk)",
        "desc_nl": "Zij beiden die (tweevoud mannelijk betrekkelijk voornaamwoord)",
        "jenis_nl": "Betrekkelijk voornaamwoord (tweevoud mannelijk)"
    },
    "2. Mawshul__10": {
        "arti_nl": "Welke dan ook (vrouwelijk)",
        "desc_nl": "Welke dan ook (vrouwelijk betrekkelijk voornaamwoord)",
        "jenis_nl": "Betrekkelijk voornaamwoord (vrouwelijk)"
    },
    "3. Istifham__1": {
        "arti_nl": "Wat? / Hoe?",
        "desc_nl": "Wat? / Hoe? (Vragend voornaamwoord voor zaken)",
        "jenis_nl": "Vragend voornaamwoord"
    },
    "3. Istifham__2": {
        "arti_nl": "Hoe?",
        "desc_nl": "Hoe? (Vragend voornaamwoord van toestand of hoedanigheid)",
        "jenis_nl": "Vragend voornaamwoord van toestand"
    },
    "3. Istifham__3": {
        "arti_nl": "Wie?",
        "desc_nl": "Wie? (Vragend voornaamwoord voor personen)",
        "jenis_nl": "Vragend voornaamwoord"
    },
    "3. Istifham__4": {
        "arti_nl": "Welke? / Wat?",
        "desc_nl": "Welke? (Vragend voornaamwoord van keuze)",
        "jenis_nl": "Vragend voornaamwoord van keuze"
    },
    "3. Istifham__5": {
        "arti_nl": "Hoe? / Vanwaar?",
        "desc_nl": "Hoe / vanwaar? (Vragend voornaamwoord van herkomst of mogelijkheid)",
        "jenis_nl": "Vragend voornaamwoord"
    },
    "3. Istifham__6": {
        "arti_nl": "Wat is het dat?",
        "desc_nl": "Wat is het dat? (Versterkt vragend voornaamwoord samengesteld met Dhaa)",
        "jenis_nl": "Samengesteld vragend voornaamwoord"
    },
    "3. Istifham__7": {
        "arti_nl": "Hoeveel? / Hoe lang?",
        "desc_nl": "Hoeveel? / Hoe lang? (Vragend voornaamwoord van aantal of duur)",
        "jenis_nl": "Vragend voornaamwoord van aantal"
    },
    "3. Istifham__8": {
        "arti_nl": "Waarom? / Waartoe?",
        "desc_nl": "Waarom? (Vraag naar reden of doel, Li + Maa)",
        "jenis_nl": "Vragend voornaamwoord van oorzaak"
    },
    "3. Istifham__9": {
        "arti_nl": "Waar? / Waarheen?",
        "desc_nl": "Waar? (Vragend voornaamwoord van plaats)",
        "jenis_nl": "Vragend voornaamwoord van plaats"
    },
    "3. Istifham__10": {
        "arti_nl": "Wanneer?",
        "desc_nl": "Wanneer? (Vragend voornaamwoord van tijd)",
        "jenis_nl": "Vragend voornaamwoord van tijd"
    },
    "4. Syarath__1": {
        "arti_nl": "Wie ook maar / al wie",
        "desc_nl": "Wie ook maar (Voorwaardelijk zelfstandig naamwoord voor personen)",
        "jenis_nl": "Voorwaardelijk nomen (rationeel)"
    },
    "4. Syarath__2": {
        "arti_nl": "Wat ook maar / al wat",
        "desc_nl": "Wat ook maar (Voorwaardelijk zelfstandig naamwoord voor zaken)",
        "jenis_nl": "Voorwaardelijk nomen (niet-rationeel)"
    },
    "4. Syarath__3": {
        "arti_nl": "Elke keer dat / telkens wanneer",
        "desc_nl": "Elke keer dat (Tijdsbepalend voorwaardelijk bijwoord)",
        "jenis_nl": "Tijdsbepalend voorwaardelijk bijwoord"
    },
    "4. Syarath__4": {
        "arti_nl": "Welke ook maar",
        "desc_nl": "Welke van de twee / welke ook maar (Voorwaardelijk nomen van keuze)",
        "jenis_nl": "Voorwaardelijk nomen van keuze"
    },
    "4. Syarath__5": {
        "arti_nl": "Welke van beide ook (benadrukt)",
        "desc_nl": "Welke termijn ook (Voorwaardelijk nomen versterkt met Maa)",
        "jenis_nl": "Versterkt voorwaardelijk nomen"
    },
    "5. Isyarah__1": {
        "arti_nl": "Dit / dat (mannelijk enkelvoud)",
        "desc_nl": "Dit / dat (Aanwijzend voornaamwoord mannelijk enkelvoud dichtbij/veraf)",
        "jenis_nl": "Aanwijzend voornaamwoord (mannelijk enkelvoud)"
    },
    "5. Isyarah__2": {
        "arti_nl": "Dezen / genen (meervoud)",
        "desc_nl": "Dezen / diegenen (Aanwijzend voornaamwoord meervoud dichtbij/veraf)",
        "jenis_nl": "Aanwijzend voornaamwoord (meervoud)"
    },
    "5. Isyarah__3": {
        "arti_nl": "Dit / dat (vrouwelijk enkelvoud)",
        "desc_nl": "Dit / dat (Aanwijzend voornaamwoord vrouwelijk enkelvoud dichtbij/veraf)",
        "jenis_nl": "Aanwijzend voornaamwoord (vrouwelijk enkelvoud)"
    },
    "5. Isyarah__4": {
        "arti_nl": "Dat / die (vrouwelijk / meervoud)",
        "desc_nl": "Dat / die (Aanwijzend voornaamwoord veraf voor vrouwelijk of meervoud)",
        "jenis_nl": "Aanwijzend voornaamwoord veraf"
    },
    "5. Isyarah__5": {
        "arti_nl": "Hier / op deze plaats",
        "desc_nl": "Hier (Aanwijzend bijwoord van plaats dichtbij)",
        "jenis_nl": "Aanwijzend bijwoord van plaats"
    },
    "5. Isyarah__6": {
        "arti_nl": "Daar / aldaar",
        "desc_nl": "Daar (Aanwijzend bijwoord van plaats veraf)",
        "jenis_nl": "Aanwijzend bijwoord van plaats veraf"
    },
    "5. Isyarah__7": {
        "arti_nl": "Deze twee (mannelijk tweevoud)",
        "desc_nl": "Deze twee (Aanwijzend voornaamwoord mannelijk tweevoud dichtbij)",
        "jenis_nl": "Aanwijzend voornaamwoord tweevoud"
    },
    "5. Isyarah__8": {
        "arti_nl": "Deze/die twee (vrouwelijk tweevoud)",
        "desc_nl": "Deze/die twee (Aanwijzend voornaamwoord vrouwelijk tweevoud)",
        "jenis_nl": "Aanwijzend voornaamwoord vrouwelijk tweevoud"
    },
    "6. Isim Fi'il__1": {
        "arti_nl": "Heilig is / glorie zij (Glorificatie)",
        "desc_nl": "Heilig en verheven is Allah (Verbaal nomen van lofprijzing)",
        "jenis_nl": "Verbaal nomen (Lofprijzing)"
    },
    "6. Isim Fi'il__2": {
        "arti_nl": "Breng voort! / Toon aan!",
        "desc_nl": "Breng jullie bewijs voort (Verbaal nomen gebiedende wijs)",
        "jenis_nl": "Verbaal nomen (gebiedende wijs)"
    },
    "6. Isim Fi'il__3": {
        "arti_nl": "Foei! / Bah! (uitroep van ergernis)",
        "desc_nl": "Foei / bah (Verbaal nomen tegenwoordige tijd van afkeer)",
        "jenis_nl": "Verbaal nomen (afkeer)"
    },
    "6. Isim Fi'il__4": {
        "arti_nl": "Ik zoek toevlucht (Moge Allah verhoeden)",
        "desc_nl": "Ik zoek bescherming bij Allah (Verbaal nomen van toevlucht)",
        "jenis_nl": "Verbaal nomen (toevlucht)"
    },
    "6. Isim Fi'il__5": {
        "arti_nl": "Kom hier! / Breng voort!",
        "desc_nl": "Kom hierheen / breng voort (Verbaal nomen gebiedende wijs)",
        "jenis_nl": "Verbaal nomen (gebiedende wijs)"
    },
    "6. Isim Fi'il__6": {
        "arti_nl": "Verre van! / Onmogelijk!",
        "desc_nl": "Hoe ver weg is het! (Verbaal nomen verleden tijd)",
        "jenis_nl": "Verbaal nomen (verleden tijd)"
    },
    "6. Isim Fi'il__7": {
        "arti_nl": "Neem hier en lees!",
        "desc_nl": "Neem en lees mijn boek (Verbaal nomen gebiedende wijs)",
        "jenis_nl": "Verbaal nomen (gebiedende wijs)"
    },
    "6. Isim Fi'il__8": {
        "arti_nl": "Kom hier! / Haast je!",
        "desc_nl": "Kom tot mij / ik ben gereed (Verbaal nomen van uitnodiging)",
        "jenis_nl": "Verbaal nomen (uitnodiging)"
    },
    "7. Fi'il Jamid__1": {
        "arti_nl": "Is niet / zijn niet",
        "desc_nl": "Is niet / zijn niet (Niet-vervoegbaar werkwoord van ontkenning)",
        "jenis_nl": "Niet-vervoegbaar werkwoord van ontkenning"
    },
    "7. Fi'il Jamid__2": {
        "arti_nl": "Wat een slechte...",
        "desc_nl": "Hoe slecht is... (Niet-vervoegbaar werkwoord van afkeuring)",
        "jenis_nl": "Niet-vervoegbaar werkwoord van afkeuring"
    },
    "7. Fi'il Jamid__3": {
        "arti_nl": "Moge het zijn / wellicht",
        "desc_nl": "Moge het zijn dat / wellicht (Niet-vervoegbaar werkwoord van hoop)",
        "jenis_nl": "Niet-vervoegbaar werkwoord van hoop"
    },
    "7. Fi'il Jamid__4": {
        "arti_nl": "Wat een voortreffelijke...",
        "desc_nl": "Hoe voortreffelijk is... (Niet-vervoegbaar werkwoord van lofprijzing)",
        "jenis_nl": "Niet-vervoegbaar werkwoord van lofprijzing"
    },
    "7. Fi'il Jamid__5": {
        "arti_nl": "Hoe slecht is datgene wat",
        "desc_nl": "Hoe slecht is wat zij kochten (Niet-vervoegbaar werkwoord van afkeuring samengesteld met Maa)",
        "jenis_nl": "Niet-vervoegbaar werkwoord van afkeuring"
    },
    "7. Fi'il Jamid__6": {
        "arti_nl": "Zij begonnen te...",
        "desc_nl": "Zij begonnen bladeren over zich heen te leggen (Niet-vervoegbaar werkwoord van aanvang)",
        "jenis_nl": "Niet-vervoegbaar werkwoord van aanvang"
    },
    "7. Fi'il Jamid__7": {
        "arti_nl": "Allah verhoede! / Verheven is Allah",
        "desc_nl": "Verre zij het van Allah! (Niet-vervoegbaar werkwoord van vrijwaring)",
        "jenis_nl": "Niet-vervoegbaar werkwoord van vrijwaring"
    },
    "7. Fi'il Jamid__8": {
        "arti_nl": "Hoe voortreffelijk is datgene wat",
        "desc_nl": "Hoe voortreffelijk is waar Hij jullie toe vermaant (Niet-vervoegbaar werkwoord van lof samengesteld met Maa)",
        "jenis_nl": "Niet-vervoegbaar werkwoord van lofprijzing"
    },
    "2. Isim Mawshul__1": {
        "arti_nl": "Wat / datgene wat",
        "desc_nl": "Algemeen betrekkelijk voornaamwoord voor niet-rationele zaken (Maa)",
        "jenis_nl": "Betrekkelijk voornaamwoord (niet-rationeel)"
    },
    "2. Isim Mawshul__2": {
        "arti_nl": "Degenen die (mannelijk meervoud)",
        "desc_nl": "Zij die / degenen die (mannelijk meervoud betrekkelijk voornaamwoord)",
        "jenis_nl": "Betrekkelijk voornaamwoord (meervoud mannelijk)"
    },
    "2. Isim Mawshul__3": {
        "arti_nl": "Wie / degene die",
        "desc_nl": "Algemeen betrekkelijk voornaamwoord voor rationele wezens (Man)",
        "jenis_nl": "Algemeen betrekkelijk voornaamwoord (rationeel)"
    },
    "2. Isim Mawshul__4": {
        "arti_nl": "Degene die (mannelijk enkelvoud)",
        "desc_nl": "Degene die / dat (mannelijk enkelvoud betrekkelijk voornaamwoord)",
        "jenis_nl": "Betrekkelijk voornaamwoord (mannelijk enkelvoud)"
    },
    "2. Isim Mawshul__5": {
        "arti_nl": "Welke / wie dan ook",
        "desc_nl": "Welke / wie van hen (verbuigbaar betrekkelijk voornaamwoord)",
        "jenis_nl": "Betrekkelijk voornaamwoord"
    },
    "2. Isim Mawshul__6": {
        "arti_nl": "Zij die (vrouwelijk enkelvoud)",
        "desc_nl": "Zij die / datgene wat (vrouwelijk enkelvoud betrekkelijk voornaamwoord)",
        "jenis_nl": "Betrekkelijk voornaamwoord (vrouwelijk enkelvoud)"
    },
    "2. Isim Mawshul__7": {
        "arti_nl": "Vrouwen die (meervoud vrouwelijk)",
        "desc_nl": "Zij die (vrouwelijk meervoud betrekkelijk voornaamwoord)",
        "jenis_nl": "Betrekkelijk voornaamwoord (meervoud vrouwelijk)"
    },
    "2. Isim Mawshul__8": {
        "arti_nl": "Vrouwen die (meervoud vrouwelijk variant)",
        "desc_nl": "Zij die (vrouwelijk meervoud betrekkelijk voornaamwoord variant)",
        "jenis_nl": "Betrekkelijk voornaamwoord (meervoud vrouwelijk)"
    },
    "2. Isim Mawshul__9": {
        "arti_nl": "Zij beiden die (tweevoud mannelijk)",
        "desc_nl": "Zij beiden die (tweevoud mannelijk betrekkelijk voornaamwoord)",
        "jenis_nl": "Betrekkelijk voornaamwoord (tweevoud mannelijk)"
    },
    "2. Isim Mawshul__10": {
        "arti_nl": "Welke dan ook (vrouwelijk)",
        "desc_nl": "Welke dan ook (vrouwelijk betrekkelijk voornaamwoord)",
        "jenis_nl": "Betrekkelijk voornaamwoord (vrouwelijk)"
    },
    "3. Isim Istifham__1": {
        "arti_nl": "Wat? / Hoe?",
        "desc_nl": "Wat? / Hoe? (Vragend voornaamwoord voor zaken)",
        "jenis_nl": "Vragend voornaamwoord"
    },
    "3. Isim Istifham__2": {
        "arti_nl": "Hoe?",
        "desc_nl": "Hoe? (Vragend voornaamwoord van toestand of hoedanigheid)",
        "jenis_nl": "Vragend voornaamwoord van toestand"
    },
    "3. Isim Istifham__3": {
        "arti_nl": "Wie?",
        "desc_nl": "Wie? (Vragend voornaamwoord voor personen)",
        "jenis_nl": "Vragend voornaamwoord"
    },
    "3. Isim Istifham__4": {
        "arti_nl": "Welke? / Wat?",
        "desc_nl": "Welke? (Vragend voornaamwoord van keuze)",
        "jenis_nl": "Vragend voornaamwoord van keuze"
    },
    "3. Isim Istifham__5": {
        "arti_nl": "Hoe? / Vanwaar?",
        "desc_nl": "Hoe / vanwaar? (Vragend voornaamwoord van herkomst of mogelijkheid)",
        "jenis_nl": "Vragend voornaamwoord"
    },
    "3. Isim Istifham__6": {
        "arti_nl": "Wat is het dat?",
        "desc_nl": "Wat is het dat? (Versterkt vragend voornaamwoord samengesteld met Dhaa)",
        "jenis_nl": "Samengesteld vragend voornaamwoord"
    },
    "3. Isim Istifham__7": {
        "arti_nl": "Hoeveel? / Hoe lang?",
        "desc_nl": "Hoeveel? / Hoe lang? (Vragend voornaamwoord van aantal of duur)",
        "jenis_nl": "Vragend voornaamwoord van aantal"
    },
    "3. Isim Istifham__8": {
        "arti_nl": "Waarom? / Waartoe?",
        "desc_nl": "Waarom? (Vraag naar reden of doel, Li + Maa)",
        "jenis_nl": "Vragend voornaamwoord van oorzaak"
    },
    "3. Isim Istifham__9": {
        "arti_nl": "Waar? / Waarheen?",
        "desc_nl": "Waar? (Vragend voornaamwoord van plaats)",
        "jenis_nl": "Vragend voornaamwoord van plaats"
    },
    "3. Isim Istifham__10": {
        "arti_nl": "Wanneer?",
        "desc_nl": "Wanneer? (Vragend voornaamwoord van tijd)",
        "jenis_nl": "Vragend voornaamwoord van tijd"
    },
    "4. Isim Syarath__1": {
        "arti_nl": "Wie ook maar / al wie",
        "desc_nl": "Wie ook maar (Voorwaardelijk zelfstandig naamwoord voor personen)",
        "jenis_nl": "Voorwaardelijk nomen (rationeel)"
    },
    "4. Isim Syarath__2": {
        "arti_nl": "Wat ook maar / al wat",
        "desc_nl": "Wat ook maar (Voorwaardelijk zelfstandig naamwoord voor zaken)",
        "jenis_nl": "Voorwaardelijk nomen (niet-rationeel)"
    },
    "4. Isim Syarath__3": {
        "arti_nl": "Elke keer dat / telkens wanneer",
        "desc_nl": "Elke keer dat (Tijdsbepalend voorwaardelijk bijwoord)",
        "jenis_nl": "Tijdsbepalend voorwaardelijk bijwoord"
    },
    "4. Isim Syarath__4": {
        "arti_nl": "Welke ook maar",
        "desc_nl": "Welke van de twee / welke ook maar (Voorwaardelijk nomen van keuze)",
        "jenis_nl": "Voorwaardelijk nomen van keuze"
    },
    "4. Isim Syarath__5": {
        "arti_nl": "Welke van beide ook (benadrukt)",
        "desc_nl": "Welke termijn ook (Voorwaardelijk nomen versterkt met Maa)",
        "jenis_nl": "Versterkt voorwaardelijk nomen"
    },
    "5. Isim Isyarah__1": {
        "arti_nl": "Dit / dat (mannelijk enkelvoud)",
        "desc_nl": "Dit / dat (Aanwijzend voornaamwoord mannelijk enkelvoud dichtbij/veraf)",
        "jenis_nl": "Aanwijzend voornaamwoord (mannelijk enkelvoud)"
    },
    "5. Isim Isyarah__2": {
        "arti_nl": "Dezen / genen (meervoud)",
        "desc_nl": "Dezen / diegenen (Aanwijzend voornaamwoord meervoud dichtbij/veraf)",
        "jenis_nl": "Aanwijzend voornaamwoord (meervoud)"
    },
    "5. Isim Isyarah__3": {
        "arti_nl": "Dit / dat (vrouwelijk enkelvoud)",
        "desc_nl": "Dit / dat (Aanwijzend voornaamwoord vrouwelijk enkelvoud dichtbij/veraf)",
        "jenis_nl": "Aanwijzend voornaamwoord (vrouwelijk enkelvoud)"
    },
    "5. Isim Isyarah__4": {
        "arti_nl": "Dat / die (vrouwelijk / meervoud)",
        "desc_nl": "Dat / die (Aanwijzend voornaamwoord veraf voor vrouwelijk of meervoud)",
        "jenis_nl": "Aanwijzend voornaamwoord veraf"
    },
    "5. Isim Isyarah__5": {
        "arti_nl": "Hier / op deze plaats",
        "desc_nl": "Hier (Aanwijzend bijwoord van plaats dichtbij)",
        "jenis_nl": "Aanwijzend bijwoord van plaats"
    },
    "5. Isim Isyarah__6": {
        "arti_nl": "Daar / aldaar",
        "desc_nl": "Daar (Aanwijzend bijwoord van plaats veraf)",
        "jenis_nl": "Aanwijzend bijwoord van plaats veraf"
    },
    "5. Isim Isyarah__7": {
        "arti_nl": "Deze twee (mannelijk tweevoud)",
        "desc_nl": "Deze twee (Aanwijzend voornaamwoord mannelijk tweevoud dichtbij)",
        "jenis_nl": "Aanwijzend voornaamwoord tweevoud"
    },
    "5. Isim Isyarah__8": {
        "arti_nl": "Deze/die twee (vrouwelijk tweevoud)",
        "desc_nl": "Deze/die twee (Aanwijzend voornaamwoord vrouwelijk tweevoud)",
        "jenis_nl": "Aanwijzend voornaamwoord vrouwelijk tweevoud"
    },
    "1a": {
        "arti_nl": "Hij (mannelijk enkelvoud)",
        "desc_nl": "Hij (3e persoon mannelijk enkelvoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord"
    },
    "1b": {
        "arti_nl": "Zijn / hem",
        "desc_nl": "Zijn / hem (3e persoon mannelijk enkelvoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord"
    },
    "1c": {
        "arti_nl": "Alleen hem",
        "desc_nl": "Alleen hem (3e persoon mannelijk enkelvoud losstaand accusatief voornaamwoord)",
        "jenis_nl": "Losstaand accusatief voornaamwoord"
    },
    "2a": {
        "arti_nl": "Zij beiden",
        "desc_nl": "Zij beiden (3e persoon tweevoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (tweevoud)"
    },
    "2b": {
        "arti_nl": "Hun beiden / hen beiden",
        "desc_nl": "Hun beiden / hen beiden (3e persoon tweevoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (tweevoud)"
    },
    "3a": {
        "arti_nl": "Zij (mannelijk meervoud)",
        "desc_nl": "Zij (3e persoon mannelijk meervoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (meervoud)"
    },
    "3b": {
        "arti_nl": "Hun / hen (mannelijk meervoud)",
        "desc_nl": "Hun / hen (3e persoon mannelijk meervoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (meervoud)"
    },
    "3c": {
        "arti_nl": "Alleen hen (mannelijk meervoud)",
        "desc_nl": "Alleen hen (3e persoon mannelijk meervoud losstaand accusatief voornaamwoord)",
        "jenis_nl": "Losstaand accusatief voornaamwoord (meervoud)"
    },
    "4a": {
        "arti_nl": "Zij (vrouwelijk enkelvoud)",
        "desc_nl": "Zij (3e persoon vrouwelijk enkelvoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (vrouwelijk)"
    },
    "4b": {
        "arti_nl": "Haar (vrouwelijk enkelvoud)",
        "desc_nl": "Haar (3e persoon vrouwelijk enkelvoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (vrouwelijk)"
    },
    "5a": {
        "arti_nl": "Zij (vrouwelijk meervoud)",
        "desc_nl": "Zij (3e persoon vrouwelijk meervoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (vrouwelijk meervoud)"
    },
    "5b": {
        "arti_nl": "Hun / hen (vrouwelijk meervoud)",
        "desc_nl": "Hun / hen (3e persoon vrouwelijk meervoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (vrouwelijk meervoud)"
    },
    "6a": {
        "arti_nl": "Jij / u (mannelijk enkelvoud)",
        "desc_nl": "Jij / u (2e persoon mannelijk enkelvoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord"
    },
    "6b": {
        "arti_nl": "Jouw / je / jou (mannelijk enkelvoud)",
        "desc_nl": "Jouw / je / jou (2e persoon mannelijk enkelvoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord"
    },
    "6c": {
        "arti_nl": "Alleen jou / u (mannelijk enkelvoud)",
        "desc_nl": "Alleen jou / u (2e persoon mannelijk enkelvoud losstaand accusatief voornaamwoord)",
        "jenis_nl": "Losstaand accusatief voornaamwoord"
    },
    "7a": {
        "arti_nl": "Jullie beiden",
        "desc_nl": "Jullie beiden (2e persoon tweevoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (tweevoud)"
    },
    "7b": {
        "arti_nl": "Jullie beiden (aangehecht)",
        "desc_nl": "Jullie beiden (2e persoon tweevoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (tweevoud)"
    },
    "8a": {
        "arti_nl": "Jullie (mannelijk meervoud)",
        "desc_nl": "Jullie (2e persoon mannelijk meervoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (meervoud)"
    },
    "8b": {
        "arti_nl": "Jullie (aangehecht mannelijk meervoud)",
        "desc_nl": "Jullie / uw (2e persoon mannelijk meervoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (meervoud)"
    },
    "8c": {
        "arti_nl": "Alleen jullie (mannelijk meervoud)",
        "desc_nl": "Alleen jullie (2e persoon mannelijk meervoud losstaand accusatief voornaamwoord)",
        "jenis_nl": "Losstaand accusatief voornaamwoord (meervoud)"
    },
    "9a": {
        "arti_nl": "Jij / u (vrouwelijk enkelvoud)",
        "desc_nl": "Jij / u (2e persoon vrouwelijk enkelvoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (vrouwelijk)"
    },
    "9b": {
        "arti_nl": "Jouw / je (vrouwelijk enkelvoud)",
        "desc_nl": "Jouw / je (2e persoon vrouwelijk enkelvoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (vrouwelijk)"
    },
    "10a": {
        "arti_nl": "Jullie (vrouwelijk meervoud)",
        "desc_nl": "Jullie (2e persoon vrouwelijk meervoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (vrouwelijk meervoud)"
    },
    "10b": {
        "arti_nl": "Jullie (aangehecht vrouwelijk meervoud)",
        "desc_nl": "Jullie / uw (2e persoon vrouwelijk meervoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (vrouwelijk meervoud)"
    },
    "11a": {
        "arti_nl": "Ik (1e persoon enkelvoud)",
        "desc_nl": "Ik (1e persoon enkelvoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord"
    },
    "11b": {
        "arti_nl": "Mijn / mij",
        "desc_nl": "Mijn / mij (1e persoon enkelvoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord"
    },
    "11c": {
        "arti_nl": "Alleen mij",
        "desc_nl": "Alleen mij (1e persoon enkelvoud losstaand accusatief voornaamwoord)",
        "jenis_nl": "Losstaand accusatief voornaamwoord"
    },
    "12a": {
        "arti_nl": "Wij (1e persoon meervoud)",
        "desc_nl": "Wij (1e persoon meervoud losstaand nominatief voornaamwoord)",
        "jenis_nl": "Losstaand nominatief voornaamwoord (meervoud)"
    },
    "12b": {
        "arti_nl": "Ons / onze",
        "desc_nl": "Ons / onze (1e persoon meervoud aangehecht voornaamwoord)",
        "jenis_nl": "Aangehecht voornaamwoord (meervoud)"
    },
    "12c": {
        "arti_nl": "Alleen ons",
        "desc_nl": "Alleen ons (1e persoon meervoud losstaand accusatief voornaamwoord)",
        "jenis_nl": "Losstaand accusatief voornaamwoord (meervoud)"
    },
    "1": {
        "arti_nl": "Dit / dat (mannelijk enkelvoud)",
        "desc_nl": "Dit / dat (Aanwijzend voornaamwoord mannelijk enkelvoud dichtbij/veraf)",
        "jenis_nl": "Aanwijzend voornaamwoord (mannelijk enkelvoud)"
    },
    "2": {
        "arti_nl": "Dezen / genen (meervoud)",
        "desc_nl": "Dezen / diegenen (Aanwijzend voornaamwoord meervoud dichtbij/veraf)",
        "jenis_nl": "Aanwijzend voornaamwoord (meervoud)"
    },
    "3": {
        "arti_nl": "Dit / dat (vrouwelijk enkelvoud)",
        "desc_nl": "Dit / dat (Aanwijzend voornaamwoord vrouwelijk enkelvoud dichtbij/veraf)",
        "jenis_nl": "Aanwijzend voornaamwoord (vrouwelijk enkelvoud)"
    },
    "4": {
        "arti_nl": "Dat / die (vrouwelijk / meervoud)",
        "desc_nl": "Dat / die (Aanwijzend voornaamwoord veraf voor vrouwelijk of meervoud)",
        "jenis_nl": "Aanwijzend voornaamwoord veraf"
    },
    "5": {
        "arti_nl": "Hier / op deze plaats",
        "desc_nl": "Hier (Aanwijzend bijwoord van plaats dichtbij)",
        "jenis_nl": "Aanwijzend bijwoord van plaats"
    },
    "6": {
        "arti_nl": "Daar / aldaar",
        "desc_nl": "Daar (Aanwijzend bijwoord van plaats veraf)",
        "jenis_nl": "Aanwijzend bijwoord van plaats veraf"
    },
    "7": {
        "arti_nl": "Deze twee (mannelijk tweevoud)",
        "desc_nl": "Deze twee (Aanwijzend voornaamwoord mannelijk tweevoud dichtbij)",
        "jenis_nl": "Aanwijzend voornaamwoord tweevoud"
    },
    "8": {
        "arti_nl": "Deze/die twee (vrouwelijk tweevoud)",
        "desc_nl": "Deze/die twee (Aanwijzend voornaamwoord vrouwelijk tweevoud)",
        "jenis_nl": "Aanwijzend voornaamwoord vrouwelijk tweevoud"
    },
    "9": {
        "arti_nl": "Waar? / Waarheen?",
        "desc_nl": "Waar? (Vragend voornaamwoord van plaats)",
        "jenis_nl": "Vragend voornaamwoord van plaats"
    },
    "10": {
        "arti_nl": "Wanneer?",
        "desc_nl": "Wanneer? (Vragend voornaamwoord van tijd)",
        "jenis_nl": "Vragend voornaamwoord van tijd"
    }
}

BENTUK_HARF_NL = {
    "1. Harf Nafyi": "1. Ontkennende Partikels (Harf Nafyi - Negatie)",
    "2. Harf Tahqiq Taswif": "2. Bevestigende & Toekomstige Partikels (Tahqiq & Taswif)",
    "3. Harf Syarat": "3. Voorwaardelijke Partikels (Harf Syarat - Conditionele Partikels)",
    "4. Harf Mashdariyah": "4. Infinitiefvormende Partikels (Harf Mashdariyah)",
    "5. Harf Zaidah": "5. Nadruk- / Extra Partikels (Harf Zaidah)",
    "6. Harf Istifham": "6. Vragende Partikels (Harf Istifham)",
    "7. Harf Jawab": "7. Antwoordpartikels (Harf Jawab)",
    "8. Harf Ibtida'": "8. Begin- / Aanhefpartikels (Harf Ibtida')",
    "9. Harf Tafshil": "9. Uiteenzettende Partikels (Harf Tafshil)",
    "10. Harf Mufaja'ah": "10. Verrassingspartikels (Harf Mufaja'ah)",
    "11. Harf Mufassirah": "11. Verklarende Partikels (Harf Mufassirah)",
    "12. Harf Istiftahiyah": "12. Openingspartikels (Harf Istiftahiyah)",
    "13. Harf Rada'": "13. Afwijzende / Berispende Partikels (Harf Rada')",
    "14. Harf Ta'ajjub": "14. Verwonderingspartikels (Harf Ta'ajjub)",
    "15. Harf Fariqah": "15. Onderscheidende Partikels (Harf Fariqah)",
    "16. Harf Mauthi'ah": "16. Eed-inleidende Partikels (Harf Mauthi'ah)",
    "17. Harf Mabany": "17. Constructiepartikels / Alfabetische Letters (Harf Mabany)"
}

DUTCH_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {
        "arti_nl": "Niet / geen (ontkenning)",
        "desc_nl": "Algemeen ontkennend partikel (Laa)",
        "jenis_nl": "Ontkennend partikel"
    },
    "1. Harf Nafyi__2": {
        "arti_nl": "Niet / niets / geenszins",
        "desc_nl": "Ontkennend partikel voor verleden en tegenwoordige tijd (Maa)",
        "jenis_nl": "Ontkennend partikel"
    },
    "1. Harf Nafyi__3": {
        "arti_nl": "Niet anders dan / slechts",
        "desc_nl": "Ontkennend partikel van uitzondering (In... illaa)",
        "jenis_nl": "Ontkennend partikel van beperking"
    },
    "1. Harf Nafyi__4": {
        "arti_nl": "Is er dan geen?",
        "desc_nl": "Retorisch ontkennend vraagpartikel (Hal)",
        "jenis_nl": "Retorisch ontkennend partikel"
    },
    "1. Harf Nafyi__5": {
        "arti_nl": "Er is geen (tijd)",
        "desc_nl": "Ontkennend partikel voor tijdsbegrippen (Laata)",
        "jenis_nl": "Ontkennend partikel van tijd"
    },
    "1. Harf Nafyi__6": {
        "arti_nl": "Wat anders dan / niets",
        "desc_nl": "Retorisch ontkennend samengesteld vraagpartikel (Maadhaa)",
        "jenis_nl": "Retorisch vraagpartikel"
    },
    "2. Harf Tahqiq Taswif__7": {
        "arti_nl": "Voorzeker / waarlijk / reeds",
        "desc_nl": "Bevestigend partikel van zekerheid (Qad)",
        "jenis_nl": "Bevestigend partikel (Tahqiq)"
    },
    "2. Harf Tahqiq Taswif__8": {
        "arti_nl": "(Binnenkort) zal / zullen",
        "desc_nl": "Toekomstpartikel voor verre toekomst (Sawfa)",
        "jenis_nl": "Toekomstpartikel (Taswif)"
    },
    "3. Harf Syarat__9": {
        "arti_nl": "Indien / ware het dat (onmogelijk)",
        "desc_nl": "Irreëel voorwaardelijk partikel (Law)",
        "jenis_nl": "Voorwaardelijk partikel"
    },
    "3. Harf Syarat__10": {
        "arti_nl": "Ware het niet dat / waarom niet",
        "desc_nl": "Voorwaardelijk partikel van verhindering (Lawlaa)",
        "jenis_nl": "Voorwaardelijk partikel van verhindering"
    },
    "3. Harf Syarat__11": {
        "arti_nl": "Zelfs al / hoewel",
        "desc_nl": "Toegevend voorwaardelijk partikel (Law)",
        "jenis_nl": "Toegevend voorwaardelijk partikel"
    },
    "3. Harf Syarat__12": {
        "arti_nl": "Als / wanneer dan ook",
        "desc_nl": "Benadrukt voorwaardelijk partikel (Immaa = In + Maa)",
        "jenis_nl": "Benadrukt voorwaardelijk partikel"
    },
    "3. Harf Syarat__13": {
        "arti_nl": "Wat voor teken dan ook",
        "desc_nl": "Algemeen voorwaardelijk zelfstandig naamwoord (Mahmaa)",
        "jenis_nl": "Voorwaardelijk nomen"
    },
    "4. Harf Mashdariyah__14": {
        "arti_nl": "Zolang als / tijdens",
        "desc_nl": "Tijdsbepalend nominaliserend partikel (Maa)",
        "jenis_nl": "Nominaliserend partikel van tijdsduur"
    },
    "4. Harf Mashdariyah__15": {
        "arti_nl": "Opdat niet / zodat niet",
        "desc_nl": "Nominaliserend partikel met ontkenning (Allaa = An + Laa)",
        "jenis_nl": "Nominaliserend ontkennend partikel"
    },
    "4. Harf Mashdariyah__16": {
        "arti_nl": "Dat / om te (nominaliserend)",
        "desc_nl": "Werkwoord-nominaliserend partikel (An)",
        "jenis_nl": "Nominaliserend partikel (Masdariyyah)"
    },
    "4. Harf Mashdariyah__17": {
        "arti_nl": "Zou wensen dat",
        "desc_nl": "Nominaliserend partikel van wens (Law)",
        "jenis_nl": "Nominaliserend partikel van wens"
    },
    "4. Harf Mashdariyah__18": {
        "arti_nl": "Dat jullie niet dienen",
        "desc_nl": "Nominaliserend partikel met verbod (An + Laa)",
        "jenis_nl": "Nominaliserend partikel van verbod"
    },
    "4. Harf Mashdariyah__19": {
        "arti_nl": "Dat (waarlijk)",
        "desc_nl": "Verlicht nominaliserend partikel (An verlicht van Anna)",
        "jenis_nl": "Verlicht nominaliserend partikel"
    },
    "5. Harf Zaidah__20": {
        "arti_nl": "Zoals / net zoals",
        "desc_nl": "Vergelijkend partikel met extra versterking (Kamaa = Ka + Maa)",
        "jenis_nl": "Versterkend partikel"
    },
    "5. Harf Zaidah__21": {
        "arti_nl": "Zelfs een mug of iets daarboven",
        "desc_nl": "Onbepaald versterkend partikel (Maa Zaa'idah)",
        "jenis_nl": "Versterkend toevoegsel"
    },
    "5. Harf Zaidah__22": {
        "arti_nl": "Ik zweer voorwaar",
        "desc_nl": "Versterkend partikel voor een eed (Laa Zaa'idah)",
        "jenis_nl": "Eed-versterkend partikel"
    },
    "5. Harf Zaidah__23": {
        "arti_nl": "Door de genade van Allah",
        "desc_nl": "Voorzetsel met extra versterkend partikel (Bimaa = Bi + Maa)",
        "jenis_nl": "Versterkend partikel na voorzetsel"
    },
    "5. Harf Zaidah__24": {
        "arti_nl": "Toen de brenger van blijde tijding kwam",
        "desc_nl": "Versterkend partikel na tijdsverbindingswoord (An na Lammaa)",
        "jenis_nl": "Versterkend tijdsverbindingspartikel"
    },
    "6. Harf Istifham__25": {
        "arti_nl": "Is er? / Heeft?",
        "desc_nl": "Vragend partikel voor vragen en bevestiging (Hal)",
        "jenis_nl": "Vragend partikel (Istifham)"
    },
    "7. Harf Jawab__26": {
        "arti_nl": "In dat geval / dan",
        "desc_nl": "Antwoordend en gevolg-aanduidend partikel (Idhan)",
        "jenis_nl": "Antwoord- en gevolgpartikel"
    },
    "7. Harf Jawab__27": {
        "arti_nl": "Jawel / zeker wel!",
        "desc_nl": "Bevestigend antwoordpartikel op ontkennende vraag (Balaa)",
        "jenis_nl": "Bevestigend antwoordpartikel"
    },
    "7. Harf Jawab__28": {
        "arti_nl": "Ja / inderdaad",
        "desc_nl": "Instemmend antwoordpartikel (Na'am)",
        "jenis_nl": "Instemmend antwoordpartikel"
    },
    "7. Harf Jawab__29": {
        "arti_nl": "Ja, bij mijn Heer!",
        "desc_nl": "Eed-bevestigend antwoordpartikel (Iiy)",
        "jenis_nl": "Eed-bevestigend antwoordpartikel"
    },
    "8. Harf Ibtida'__30": {
        "arti_nl": "Totdat / zover dat",
        "desc_nl": "Begin-aanduidend partikel (Hattaa)",
        "jenis_nl": "Begin-partikel (Ibtidaa')"
    },
    "9. Harf Tafshil__31": {
        "arti_nl": "Wat betreft / aangaande",
        "desc_nl": "Partikel van nadere toelichting en voorwaarde (Ammaa)",
        "jenis_nl": "Toelichtend partikel (Tafshil)"
    },
    "10. Harf Mufaja'ah__32": {
        "arti_nl": "Plotseling / eensklaps",
        "desc_nl": "Partikel van plotselinge gebeurtenis (Idhaa)",
        "jenis_nl": "Partikel van plotselinge wending"
    },
    "11. Harf Mufassirah__33": {
        "arti_nl": "Namelijk / dat wil zeggen",
        "desc_nl": "Verklarend partikel (An)",
        "jenis_nl": "Verklarend partikel (Mufassirah)"
    },
    "12. Harf Istiftahiyah__34": {
        "arti_nl": "Weet wel! / Let op!",
        "desc_nl": "Aandachttrekkend openingspartikel (Alaa)",
        "jenis_nl": "Openings- en waarschuwingspartikel"
    },
    "13. Harf Rada'__35": {
        "arti_nl": "Geenszins! / Absoluut niet!",
        "desc_nl": "Bestraffend en fel afwijzend partikel (Kallaa)",
        "jenis_nl": "Afwijzend en bestraffend partikel (Rada')"
    },
    "14. Harf Ta'ajjub__36": {
        "arti_nl": "Hoe geduldig zijn zij!",
        "desc_nl": "Partikel van verbazing en uitroep (Maa Ta'ajjubiyyah)",
        "jenis_nl": "Uitroep- en verwonderingspartikel"
    },
    "15. Harf Fariqah__37": {
        "arti_nl": "Waarlijk / inderdaad",
        "desc_nl": "Onderscheidende versterkende Laam (Laam Fariqah bij verlichte In)",
        "jenis_nl": "Onderscheidende Laam"
    },
    "16. Harf Mauthi'ah__38": {
        "arti_nl": "Als... dan zweer ik voorzeker",
        "desc_nl": "Eed-inleidende voorwaardelijke Laam (La-in)",
        "jenis_nl": "Eed-inleidende Laam"
    },
    "17. Harf Mabany__39": {
        "arti_nl": "Haa Miim",
        "desc_nl": "Mystieke openingsletters van de Soerah (حم)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "17. Harf Mabany__40": {
        "arti_nl": "Alif Laam Miim",
        "desc_nl": "Mystieke openingsletters van de Soerah (الم)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "17. Harf Mabany__41": {
        "arti_nl": "Alif Laam Raa",
        "desc_nl": "Mystieke openingsletters van de Soerah (الر)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "17. Harf Mabany__42": {
        "arti_nl": "Thaa Siin Miim",
        "desc_nl": "Mystieke openingsletters van de Soerah (طسم)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "17. Harf Mabany__43": {
        "arti_nl": "Alif Laam Miim Raa",
        "desc_nl": "Mystieke openingsletters van de Soerah (المر)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "17. Harf Mabany__44": {
        "arti_nl": "Alif Laam Miim Shaad",
        "desc_nl": "Mystieke openingsletters van de Soerah (المص)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "17. Harf Mabany__45": {
        "arti_nl": "Shaad",
        "desc_nl": "Mystieke openingsletter van de Soerah (ص)",
        "jenis_nl": "Losse openingsletter (Muqatta'at)"
    },
    "17. Harf Mabany__46": {
        "arti_nl": "Thaa Siin",
        "desc_nl": "Mystieke openingsletters van de Soerah (طس)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "17. Harf Mabany__47": {
        "arti_nl": "Thaa Haa",
        "desc_nl": "Mystieke openingsletters van de Soerah (طه)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "17. Harf Mabany__48": {
        "arti_nl": "'Ain Siin Qaaf",
        "desc_nl": "Mystieke openingsletters van de Soerah (عسق)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "17. Harf Mabany__49": {
        "arti_nl": "Qaaf",
        "desc_nl": "Mystieke openingsletter van de Soerah (ق)",
        "jenis_nl": "Losse openingsletter (Muqatta'at)"
    },
    "17. Harf Mabany__50": {
        "arti_nl": "Kaaf Haa Yaa 'Ain Shaad",
        "desc_nl": "Mystieke openingsletters van de Soerah (كهيعص)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "17. Harf Mabany__51": {
        "arti_nl": "Noen",
        "desc_nl": "Mystieke openingsletter van de Soerah (ن)",
        "jenis_nl": "Losse openingsletter (Muqatta'at)"
    },
    "17. Harf Mabany__52": {
        "arti_nl": "Yaa Siin",
        "desc_nl": "Mystieke openingsletters van de Soerah (يس)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "1": {
        "arti_nl": "Niet / geen (ontkenning)",
        "desc_nl": "Algemeen ontkennend partikel (Laa)",
        "jenis_nl": "Ontkennend partikel"
    },
    "2": {
        "arti_nl": "Niet / niets / geenszins",
        "desc_nl": "Ontkennend partikel voor verleden en tegenwoordige tijd (Maa)",
        "jenis_nl": "Ontkennend partikel"
    },
    "3": {
        "arti_nl": "Niet anders dan / slechts",
        "desc_nl": "Ontkennend partikel van uitzondering (In... illaa)",
        "jenis_nl": "Ontkennend partikel van beperking"
    },
    "4": {
        "arti_nl": "Is er dan geen?",
        "desc_nl": "Retorisch ontkennend vraagpartikel (Hal)",
        "jenis_nl": "Retorisch ontkennend partikel"
    },
    "5": {
        "arti_nl": "Er is geen (tijd)",
        "desc_nl": "Ontkennend partikel voor tijdsbegrippen (Laata)",
        "jenis_nl": "Ontkennend partikel van tijd"
    },
    "6": {
        "arti_nl": "Wat anders dan / niets",
        "desc_nl": "Retorisch ontkennend samengesteld vraagpartikel (Maadhaa)",
        "jenis_nl": "Retorisch vraagpartikel"
    },
    "7": {
        "arti_nl": "Voorzeker / waarlijk / reeds",
        "desc_nl": "Bevestigend partikel van zekerheid (Qad)",
        "jenis_nl": "Bevestigend partikel (Tahqiq)"
    },
    "8": {
        "arti_nl": "(Binnenkort) zal / zullen",
        "desc_nl": "Toekomstpartikel voor verre toekomst (Sawfa)",
        "jenis_nl": "Toekomstpartikel (Taswif)"
    },
    "9": {
        "arti_nl": "Indien / ware het dat (onmogelijk)",
        "desc_nl": "Irreëel voorwaardelijk partikel (Law)",
        "jenis_nl": "Voorwaardelijk partikel"
    },
    "10": {
        "arti_nl": "Ware het niet dat / waarom niet",
        "desc_nl": "Voorwaardelijk partikel van verhindering (Lawlaa)",
        "jenis_nl": "Voorwaardelijk partikel van verhindering"
    },
    "11": {
        "arti_nl": "Zelfs al / hoewel",
        "desc_nl": "Toegevend voorwaardelijk partikel (Law)",
        "jenis_nl": "Toegevend voorwaardelijk partikel"
    },
    "12": {
        "arti_nl": "Als / wanneer dan ook",
        "desc_nl": "Benadrukt voorwaardelijk partikel (Immaa = In + Maa)",
        "jenis_nl": "Benadrukt voorwaardelijk partikel"
    },
    "13": {
        "arti_nl": "Wat voor teken dan ook",
        "desc_nl": "Algemeen voorwaardelijk zelfstandig naamwoord (Mahmaa)",
        "jenis_nl": "Voorwaardelijk nomen"
    },
    "14": {
        "arti_nl": "Zolang als / tijdens",
        "desc_nl": "Tijdsbepalend nominaliserend partikel (Maa)",
        "jenis_nl": "Nominaliserend partikel van tijdsduur"
    },
    "15": {
        "arti_nl": "Opdat niet / zodat niet",
        "desc_nl": "Nominaliserend partikel met ontkenning (Allaa = An + Laa)",
        "jenis_nl": "Nominaliserend ontkennend partikel"
    },
    "16": {
        "arti_nl": "Dat / om te (nominaliserend)",
        "desc_nl": "Werkwoord-nominaliserend partikel (An)",
        "jenis_nl": "Nominaliserend partikel (Masdariyyah)"
    },
    "17": {
        "arti_nl": "Zou wensen dat",
        "desc_nl": "Nominaliserend partikel van wens (Law)",
        "jenis_nl": "Nominaliserend partikel van wens"
    },
    "18": {
        "arti_nl": "Dat jullie niet dienen",
        "desc_nl": "Nominaliserend partikel met verbod (An + Laa)",
        "jenis_nl": "Nominaliserend partikel van verbod"
    },
    "19": {
        "arti_nl": "Dat (waarlijk)",
        "desc_nl": "Verlicht nominaliserend partikel (An verlicht van Anna)",
        "jenis_nl": "Verlicht nominaliserend partikel"
    },
    "20": {
        "arti_nl": "Zoals / net zoals",
        "desc_nl": "Vergelijkend partikel met extra versterking (Kamaa = Ka + Maa)",
        "jenis_nl": "Versterkend partikel"
    },
    "21": {
        "arti_nl": "Zelfs een mug of iets daarboven",
        "desc_nl": "Onbepaald versterkend partikel (Maa Zaa'idah)",
        "jenis_nl": "Versterkend toevoegsel"
    },
    "22": {
        "arti_nl": "Ik zweer voorwaar",
        "desc_nl": "Versterkend partikel voor een eed (Laa Zaa'idah)",
        "jenis_nl": "Eed-versterkend partikel"
    },
    "23": {
        "arti_nl": "Door de genade van Allah",
        "desc_nl": "Voorzetsel met extra versterkend partikel (Bimaa = Bi + Maa)",
        "jenis_nl": "Versterkend partikel na voorzetsel"
    },
    "24": {
        "arti_nl": "Toen de brenger van blijde tijding kwam",
        "desc_nl": "Versterkend partikel na tijdsverbindingswoord (An na Lammaa)",
        "jenis_nl": "Versterkend tijdsverbindingspartikel"
    },
    "25": {
        "arti_nl": "Is er? / Heeft?",
        "desc_nl": "Vragend partikel voor vragen en bevestiging (Hal)",
        "jenis_nl": "Vragend partikel (Istifham)"
    },
    "26": {
        "arti_nl": "In dat geval / dan",
        "desc_nl": "Antwoordend en gevolg-aanduidend partikel (Idhan)",
        "jenis_nl": "Antwoord- en gevolgpartikel"
    },
    "27": {
        "arti_nl": "Jawel / zeker wel!",
        "desc_nl": "Bevestigend antwoordpartikel op ontkennende vraag (Balaa)",
        "jenis_nl": "Bevestigend antwoordpartikel"
    },
    "28": {
        "arti_nl": "Ja / inderdaad",
        "desc_nl": "Instemmend antwoordpartikel (Na'am)",
        "jenis_nl": "Instemmend antwoordpartikel"
    },
    "29": {
        "arti_nl": "Ja, bij mijn Heer!",
        "desc_nl": "Eed-bevestigend antwoordpartikel (Iiy)",
        "jenis_nl": "Eed-bevestigend antwoordpartikel"
    },
    "30": {
        "arti_nl": "Totdat / zover dat",
        "desc_nl": "Begin-aanduidend partikel (Hattaa)",
        "jenis_nl": "Begin-partikel (Ibtidaa')"
    },
    "31": {
        "arti_nl": "Wat betreft / aangaande",
        "desc_nl": "Partikel van nadere toelichting en voorwaarde (Ammaa)",
        "jenis_nl": "Toelichtend partikel (Tafshil)"
    },
    "32": {
        "arti_nl": "Plotseling / eensklaps",
        "desc_nl": "Partikel van plotselinge gebeurtenis (Idhaa)",
        "jenis_nl": "Partikel van plotselinge wending"
    },
    "33": {
        "arti_nl": "Namelijk / dat wil zeggen",
        "desc_nl": "Verklarend partikel (An)",
        "jenis_nl": "Verklarend partikel (Mufassirah)"
    },
    "34": {
        "arti_nl": "Weet wel! / Let op!",
        "desc_nl": "Aandachttrekkend openingspartikel (Alaa)",
        "jenis_nl": "Openings- en waarschuwingspartikel"
    },
    "35": {
        "arti_nl": "Geenszins! / Absoluut niet!",
        "desc_nl": "Bestraffend en fel afwijzend partikel (Kallaa)",
        "jenis_nl": "Afwijzend en bestraffend partikel (Rada')"
    },
    "36": {
        "arti_nl": "Hoe geduldig zijn zij!",
        "desc_nl": "Partikel van verbazing en uitroep (Maa Ta'ajjubiyyah)",
        "jenis_nl": "Uitroep- en verwonderingspartikel"
    },
    "37": {
        "arti_nl": "Waarlijk / inderdaad",
        "desc_nl": "Onderscheidende versterkende Laam (Laam Fariqah bij verlichte In)",
        "jenis_nl": "Onderscheidende Laam"
    },
    "38": {
        "arti_nl": "Als... dan zweer ik voorzeker",
        "desc_nl": "Eed-inleidende voorwaardelijke Laam (La-in)",
        "jenis_nl": "Eed-inleidende Laam"
    },
    "39": {
        "arti_nl": "Haa Miim",
        "desc_nl": "Mystieke openingsletters van de Soerah (حم)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "40": {
        "arti_nl": "Alif Laam Miim",
        "desc_nl": "Mystieke openingsletters van de Soerah (الم)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "41": {
        "arti_nl": "Alif Laam Raa",
        "desc_nl": "Mystieke openingsletters van de Soerah (الر)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "42": {
        "arti_nl": "Thaa Siin Miim",
        "desc_nl": "Mystieke openingsletters van de Soerah (طسم)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "43": {
        "arti_nl": "Alif Laam Miim Raa",
        "desc_nl": "Mystieke openingsletters van de Soerah (المر)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "44": {
        "arti_nl": "Alif Laam Miim Shaad",
        "desc_nl": "Mystieke openingsletters van de Soerah (المص)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "45": {
        "arti_nl": "Shaad",
        "desc_nl": "Mystieke openingsletter van de Soerah (ص)",
        "jenis_nl": "Losse openingsletter (Muqatta'at)"
    },
    "46": {
        "arti_nl": "Thaa Siin",
        "desc_nl": "Mystieke openingsletters van de Soerah (طس)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "47": {
        "arti_nl": "Thaa Haa",
        "desc_nl": "Mystieke openingsletters van de Soerah (طه)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "48": {
        "arti_nl": "'Ain Siin Qaaf",
        "desc_nl": "Mystieke openingsletters van de Soerah (عسق)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "49": {
        "arti_nl": "Qaaf",
        "desc_nl": "Mystieke openingsletter van de Soerah (ق)",
        "jenis_nl": "Losse openingsletter (Muqatta'at)"
    },
    "50": {
        "arti_nl": "Kaaf Haa Yaa 'Ain Shaad",
        "desc_nl": "Mystieke openingsletters van de Soerah (كهيعص)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    },
    "51": {
        "arti_nl": "Noen",
        "desc_nl": "Mystieke openingsletter van de Soerah (ن)",
        "jenis_nl": "Losse openingsletter (Muqatta'at)"
    },
    "52": {
        "arti_nl": "Yaa Siin",
        "desc_nl": "Mystieke openingsletters van de Soerah (يس)",
        "jenis_nl": "Losse openingsletters (Muqatta'at)"
    }
}
