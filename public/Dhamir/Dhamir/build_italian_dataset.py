#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script containing complete Italian (it) dataset metadata:
- 114 Surah Names (ITALIAN_SURAHS)
- 7 Bentuk Kata Categories (BENTUK_KATA_IT)
- 76 Jamid Mabny Words Grammar (ITALIAN_GRAMMAR)
- 17 Bentuk Harf Categories (BENTUK_HARF_IT)
- 52 Harf Words Grammar (ITALIAN_HARF_GRAMMAR)
"""

ITALIAN_SURAHS = {
    "1": "L'Aprente (Al-Fatihah)",
    "2": "La Giovenca (Al-Baqarah)",
    "3": "La Famiglia di Imran (Ali 'Imran)",
    "4": "Le Donne (An-Nisa')",
    "5": "La Tavola Imbandita (Al-Ma'idah)",
    "6": "Il Bestiame (Al-An'am)",
    "7": "Gli Alti Luoghi (Al-A'raf)",
    "8": "Il Bottino di Guerra (Al-Anfal)",
    "9": "Il Pentimento (At-Tawbah)",
    "10": "Giona (Yunus)",
    "11": "Hud (Hud)",
    "12": "Giuseppe (Yusuf)",
    "13": "Il Tuono (Ar-Ra'd)",
    "14": "Abramo (Ibrahim)",
    "15": "Al-Hijr (Al-Hijr)",
    "16": "Le Api (An-Nahl)",
    "17": "Il Viaggio Notturno (Al-Isra')",
    "18": "La Caverna (Al-Kahf)",
    "19": "Maria (Maryam)",
    "20": "Ta-Ha (Ta-Ha)",
    "21": "I Profeti (Al-Anbiya')",
    "22": "Il Pellegrinaggio (Al-Hajj)",
    "23": "I Credenti (Al-Mu'minun)",
    "24": "La Luce (An-Nur)",
    "25": "Il Discrimine (Al-Furqan)",
    "26": "I Poeti (Asy-Syu'ara')",
    "27": "Le Formiche (An-Naml)",
    "28": "Il Racconto (Al-Qasas)",
    "29": "Il Ragno (Al-'Ankabut)",
    "30": "I Romani (Ar-Rum)",
    "31": "Luqman (Luqman)",
    "32": "La Prosternazione (As-Sajdah)",
    "33": "I Coalizzati (Al-Ahzab)",
    "34": "Saba (Saba')",
    "35": "Il Creatore (Fatir)",
    "36": "Ya-Sin (Ya-Sin)",
    "37": "I Ranghiati (As-Saffat)",
    "38": "Sad (Sad)",
    "39": "I Gruppi (Az-Zumar)",
    "40": "Il Perdonatore (Ghafir / Al-Mu'min)",
    "41": "I Versetti Esposti Chiaramente (Fussilat)",
    "42": "La Consultazione (Asy-Syura)",
    "43": "Gli Ornamenti d'Oro (Az-Zukhruf)",
    "44": "Il Fumo (Ad-Dukhan)",
    "45": "La Ginocchiata (Al-Jathiyah)",
    "46": "Le Dune di Sabbia (Al-Ahqaf)",
    "47": "Maometto (Muhammad)",
    "48": "La Vittoria (Al-Fath)",
    "49": "Le Stanze Intime (Al-Hujurat)",
    "50": "Qaf (Qaf)",
    "51": "Quelle che Spargono (Adz-Dzariyat)",
    "52": "Il Monte (At-Tur)",
    "53": "La Stella (An-Najm)",
    "54": "La Luna (Al-Qamar)",
    "55": "Il Compassionevole (Ar-Rahman)",
    "56": "L'Evento Inevitabile (Al-Waqi'ah)",
    "57": "Il Ferro (Al-Hadid)",
    "58": "La Disputante (Al-Mujadilah)",
    "59": "L'Esilio (Al-Hasyr)",
    "60": "L'Esaminata (Al-Mumtahanah)",
    "61": "I Ranghi Serrati (As-Saff)",
    "62": "Il Venerdì (Al-Jumu'ah)",
    "63": "Gli Ipocriti (Al-Munafiqun)",
    "64": "Il Reciproco Inganno (At-Taghabun)",
    "65": "Il Ripudio (At-Talaq)",
    "66": "L'Interdizione (At-Tahrim)",
    "67": "La Sovranità (Al-Mulk)",
    "68": "Il Calamo (Al-Qalam)",
    "69": "L'Inevitabile (Al-Haqqah)",
    "70": "Le Vie dell'Ascensione (Al-Ma'arij)",
    "71": "Noè (Nuh)",
    "72": "I Jinn (Al-Jinn)",
    "73": "L'Avvolto (Al-Muzzammil)",
    "74": "L'Avvolto nel Mantello (Al-Muddaththir)",
    "75": "La Resurrezione (Al-Qiyamah)",
    "76": "L'Uomo (Al-Insan)",
    "77": "Le Inviate (Al-Mursalat)",
    "78": "L'Annuncio (An-Naba')",
    "79": "Gli Strappanti Violenti (An-Nazi'at)",
    "80": "Si Accigliò ('Abasa)",
    "81": "L'Oscuramento (At-Takwir)",
    "82": "Lo Squarcio (Al-Infitar)",
    "83": "I Frodatore (Al-Mutaffifin)",
    "84": "La Fenditura (Al-Insyiqaq)",
    "85": "Le Costellazioni (Al-Buruj)",
    "86": "L'Astro Notturno (At-Tariq)",
    "87": "L'Altissimo (Al-A'la)",
    "88": "L'Avvolgente (Al-Ghasyiyah)",
    "89": "L'Alba (Al-Fajr)",
    "90": "La Contrada (Al-Balad)",
    "91": "Il Sole (Asy-Syams)",
    "92": "La Notte (Al-Lail)",
    "93": "La Luce del Mattino (Ad-Duha)",
    "94": "L'Apertura (Asy-Syarh / Al-Insyirah)",
    "95": "Il Fico (At-Tin)",
    "96": "L'Aderenza (Al-'Alaq)",
    "97": "Il Destino (Al-Qadr)",
    "98": "La Prova Evidente (Al-Bayyinah)",
    "99": "Il Terremoto (Az-Zalzalah)",
    "100": "I Corridori (Al-'Adiyat)",
    "101": "La Percotente (Al-Qari'ah)",
    "102": "La Rivalità nel Moltiplicare (At-Takathur)",
    "103": "Il Pomeriggio (Al-'Asr)",
    "104": "Il Diffamatore (Al-Humazah)",
    "105": "L'Elefante (Al-Fil)",
    "106": "I Quraish (Quraisy)",
    "107": "L'Utensile (Al-Ma'un)",
    "108": "L'Abbondanza (Al-Kautsar)",
    "109": "I Miscredenti (Al-Kafirun)",
    "110": "Il Soccorso (An-Nasr)",
    "111": "Le Fibre di Palma (Al-Masad / Al-Lahab)",
    "112": "Il Puro Monoteismo (Al-Ikhlas)",
    "113": "L'Alba Nascente (Al-Falaq)",
    "114": "Gli Uomini (An-Nas)"
}

BENTUK_KATA_IT = {
    "1. Dhamir": "1. Pronomi (Dhamir - Pronomi Personali e Possessivi)",
    "2. Isim Mawshul": "2. Pronomi Relativi (Mawshul)",
    "3. Isim Istifham": "3. Pronomi Interrogativi (Istifham)",
    "4. Isim Syarath": "4. Sostantivi Condizionali (Syarath)",
    "5. Isim Isyarah": "5. Pronomi Dimostrativi (Isyarah)",
    "6. Isim Fi'il": "6. Nomi Verbali (Isim Fi'il)",
    "7. Fi'il Jamid": "7. Verbi Invariabili / Difettivi (Fi'il Jamid)"
}

ITALIAN_GRAMMAR = {
    "1. Dhamir__1a": {
        "arti_it": "Egli / Lui (singolare maschile)",
        "desc_it": "Egli / Lui (pronome personale isolato nominativo 3a persona maschile singolare)",
        "jenis_it": "Pronome personale isolato nominativo"
    },
    "1. Dhamir__1b": {
        "arti_it": "Suo / lo / gli",
        "desc_it": "Suo / lo / gli (pronome personale suffisso 3a persona maschile singolare)",
        "jenis_it": "Pronome suffisso"
    },
    "1. Dhamir__1c": {
        "arti_it": "Solo Lui",
        "desc_it": "Solo Lui (pronome personale isolato accusativo 3a persona maschile singolare)",
        "jenis_it": "Pronome isolato accusativo"
    },
    "1. Dhamir__2a": {
        "arti_it": "Essi due",
        "desc_it": "Essi due (pronome personale isolato nominativo 3a persona duale)",
        "jenis_it": "Pronome isolato nominativo (duale)"
    },
    "1. Dhamir__2b": {
        "arti_it": "Di loro due / loro due",
        "desc_it": "Di loro due / loro due (pronome personale suffisso 3a persona duale)",
        "jenis_it": "Pronome suffisso (duale)"
    },
    "1. Dhamir__3a": {
        "arti_it": "Essi / Loro (plurale maschile)",
        "desc_it": "Essi / Loro (pronome personale isolato nominativo 3a persona maschile plurale)",
        "jenis_it": "Pronome isolato nominativo (plurale)"
    },
    "1. Dhamir__3b": {
        "arti_it": "Loro / li (plurale maschile)",
        "desc_it": "Loro / li (pronome personale suffisso 3a persona maschile plurale)",
        "jenis_it": "Pronome suffisso (plurale)"
    },
    "1. Dhamir__3c": {
        "arti_it": "Solo loro (plurale maschile)",
        "desc_it": "Solo loro (pronome personale isolato accusativo 3a persona maschile plurale)",
        "jenis_it": "Pronome isolato accusativo (plurale)"
    },
    "1. Dhamir__4a": {
        "arti_it": "Ella / Lei (singolare femminile)",
        "desc_it": "Ella / Lei (pronome personale isolato nominativo 3a persona femminile singolare)",
        "jenis_it": "Pronome isolato nominativo (femminile)"
    },
    "1. Dhamir__4b": {
        "arti_it": "Suo / la / le",
        "desc_it": "Suo / la / le (pronome personale suffisso 3a persona femminile singolare)",
        "jenis_it": "Pronome suffisso (femminile)"
    },
    "1. Dhamir__5a": {
        "arti_it": "Esse / Loro (plurale femminile)",
        "desc_it": "Esse / Loro (pronome personale isolato nominativo 3a persona femminile plurale)",
        "jenis_it": "Pronome isolato nominativo (femminile plurale)"
    },
    "1. Dhamir__5b": {
        "arti_it": "Loro / le (plurale femminile)",
        "desc_it": "Loro / le (pronome personale suffisso 3a persona femminile plurale)",
        "jenis_it": "Pronome suffisso (femminile plurale)"
    },
    "1. Dhamir__6a": {
        "arti_it": "Tu (singolare maschile)",
        "desc_it": "Tu (pronome personale isolato nominativo 2a persona maschile singolare)",
        "jenis_it": "Pronome isolato nominativo"
    },
    "1. Dhamir__6b": {
        "arti_it": "Tuo / ti / te (singolare maschile)",
        "desc_it": "Tuo / ti / te (pronome personale suffisso 2a persona maschile singolare)",
        "jenis_it": "Pronome suffisso"
    },
    "1. Dhamir__6c": {
        "arti_it": "Solo Te (singolare maschile)",
        "desc_it": "Solo Te (pronome personale isolato accusativo 2a persona maschile singolare)",
        "jenis_it": "Pronome isolato accusativo"
    },
    "1. Dhamir__7a": {
        "arti_it": "Voi due",
        "desc_it": "Voi due (pronome personale isolato nominativo 2a persona duale)",
        "jenis_it": "Pronome isolato nominativo (duale)"
    },
    "1. Dhamir__7b": {
        "arti_it": "Di voi due / voi due",
        "desc_it": "Di voi due / voi due (pronome personale suffisso 2a persona duale)",
        "jenis_it": "Pronome suffisso (duale)"
    },
    "1. Dhamir__8a": {
        "arti_it": "Voi (plurale maschile)",
        "desc_it": "Voi (pronome personale isolato nominativo 2a persona maschile plurale)",
        "jenis_it": "Pronome isolato nominativo (plurale)"
    },
    "1. Dhamir__8b": {
        "arti_it": "Vostro / vi (plurale maschile)",
        "desc_it": "Vostro / vi (pronome personale suffisso 2a persona maschile plurale)",
        "jenis_it": "Pronome suffisso (plurale)"
    },
    "1. Dhamir__8c": {
        "arti_it": "Solo voi (plurale maschile)",
        "desc_it": "Solo voi (pronome personale isolato accusativo 2a persona maschile plurale)",
        "jenis_it": "Pronome isolato accusativo (plurale)"
    },
    "1. Dhamir__9a": {
        "arti_it": "Tu (singolare femminile)",
        "desc_it": "Tu (pronome personale isolato nominativo 2a persona femminile singolare)",
        "jenis_it": "Pronome isolato nominativo (femminile)"
    },
    "1. Dhamir__9b": {
        "arti_it": "Tuo / ti (singolare femminile)",
        "desc_it": "Tuo / ti (pronome personale suffisso 2a persona femminile singolare)",
        "jenis_it": "Pronome suffisso (femminile)"
    },
    "1. Dhamir__10a": {
        "arti_it": "Voi (plurale femminile)",
        "desc_it": "Voi (pronome personale isolato nominativo 2a persona femminile plurale)",
        "jenis_it": "Pronome isolato nominativo (femminile plurale)"
    },
    "1. Dhamir__10b": {
        "arti_it": "Vostro / vi (plurale femminile)",
        "desc_it": "Vostro / vi (pronome personale suffisso 2a persona femminile plurale)",
        "jenis_it": "Pronome suffisso (femminile plurale)"
    },
    "1. Dhamir__11a": {
        "arti_it": "Io (1a persona singolare)",
        "desc_it": "Io (pronome personale isolato nominativo 1a persona singolare)",
        "jenis_it": "Pronome isolato nominativo"
    },
    "1. Dhamir__11b": {
        "arti_it": "Mio / mi / me",
        "desc_it": "Mio / mi / me (pronome personale suffisso 1a persona singolare)",
        "jenis_it": "Pronome suffisso"
    },
    "1. Dhamir__11c": {
        "arti_it": "Solo me",
        "desc_it": "Solo me (pronome personale isolato accusativo 1a persona singolare)",
        "jenis_it": "Pronome isolato accusativo"
    },
    "1. Dhamir__12a": {
        "arti_it": "Noi (1a persona plurale)",
        "desc_it": "Noi (pronome personale isolato nominativo 1a persona plurale)",
        "jenis_it": "Pronome isolato nominativo (plurale)"
    },
    "1. Dhamir__12b": {
        "arti_it": "Nostro / ci",
        "desc_it": "Nostro / ci (pronome personale suffisso 1a persona plurale)",
        "jenis_it": "Pronome suffisso (plurale)"
    },
    "1. Dhamir__12c": {
        "arti_it": "Solo noi",
        "desc_it": "Solo noi (pronome personale isolato accusativo 1a persona plurale)",
        "jenis_it": "Pronome isolato accusativo (plurale)"
    },
    "2. Mawshul__1": {
        "arti_it": "Ciò che / quel che",
        "desc_it": "Pronome relativo generale per entità non razionali (Ma)",
        "jenis_it": "Pronome relativo generale (non razionale)"
    },
    "2. Mawshul__2": {
        "arti_it": "Coloro che (plurale maschile)",
        "desc_it": "Coloro che / i quali (pronome relativo plurale maschile)",
        "jenis_it": "Pronome relativo plurale maschile"
    },
    "2. Mawshul__3": {
        "arti_it": "Chi / colui che",
        "desc_it": "Pronome relativo generale per esseri razionali (Man)",
        "jenis_it": "Pronome relativo generale (razionale)"
    },
    "2. Mawshul__4": {
        "arti_it": "Colui che (maschile singolare)",
        "desc_it": "Colui che / il quale (pronome relativo maschile singolare)",
        "jenis_it": "Pronome relativo maschile singolare"
    },
    "2. Mawshul__5": {
        "arti_it": "Quale / chiunque di loro",
        "desc_it": "Quale / chiunque tra loro (pronome relativo declinabile)",
        "jenis_it": "Pronome relativo"
    },
    "2. Mawshul__6": {
        "arti_it": "Colei che (femminile singolare)",
        "desc_it": "Colei che / la quale (pronome relativo femminile singolare)",
        "jenis_it": "Pronome relativo femminile singolare"
    },
    "2. Mawshul__7": {
        "arti_it": "Coloro che / le donne che (plurale femminile)",
        "desc_it": "Coloro che / le quali (pronome relativo plurale femminile)",
        "jenis_it": "Pronome relativo plurale femminile"
    },
    "2. Mawshul__8": {
        "arti_it": "Coloro che / le donne che (plurale femminile variante)",
        "desc_it": "Coloro che / le quali (pronome relativo plurale femminile variante)",
        "jenis_it": "Pronome relativo plurale femminile"
    },
    "2. Mawshul__9": {
        "arti_it": "Coloro due che (duale maschile)",
        "desc_it": "Coloro due che (pronome relativo duale maschile)",
        "jenis_it": "Pronome relativo duale maschile"
    },
    "2. Mawshul__10": {
        "arti_it": "Qualunque / qualsiasi (femminile)",
        "desc_it": "Qualunque / qualsiasi (pronome relativo femminile)",
        "jenis_it": "Pronome relativo (femminile)"
    },
    "3. Istifham__1": {
        "arti_it": "Cosa? / Che cosa?",
        "desc_it": "Cosa? / Che cosa? (Pronome interrogativo per cose)",
        "jenis_it": "Pronome interrogativo"
    },
    "3. Istifham__2": {
        "arti_it": "Come?",
        "desc_it": "Come? (Pronome interrogativo di modo)",
        "jenis_it": "Pronome interrogativo di modo"
    },
    "3. Istifham__3": {
        "arti_it": "Chi?",
        "desc_it": "Chi? (Pronome interrogativo per persone)",
        "jenis_it": "Pronome interrogativo"
    },
    "3. Istifham__4": {
        "arti_it": "Quale?",
        "desc_it": "Quale? (Pronome interrogativo di scelta)",
        "jenis_it": "Pronome interrogativo di scelta"
    },
    "3. Istifham__5": {
        "arti_it": "Come? / Da dove?",
        "desc_it": "Come? / Da dove? (Pronome interrogativo di modo o provenienza)",
        "jenis_it": "Pronome interrogativo"
    },
    "3. Istifham__6": {
        "arti_it": "Che cos'è che?",
        "desc_it": "Che cos'è che? (Pronome interrogativo composto enfatico)",
        "jenis_it": "Pronome interrogativo composto"
    },
    "3. Istifham__7": {
        "arti_it": "Quanto? / Per quanto tempo?",
        "desc_it": "Quanto? (Pronome interrogativo di quantità o tempo)",
        "jenis_it": "Pronome interrogativo di quantità"
    },
    "3. Istifham__8": {
        "arti_it": "Perché? / A che scopo?",
        "desc_it": "Perché? / Per quale motivo? (Interrogativo di causa, Li + Ma)",
        "jenis_it": "Interrogativo di causa"
    },
    "3. Istifham__9": {
        "arti_it": "Dove?",
        "desc_it": "Dove? (Pronome interrogativo di luogo)",
        "jenis_it": "Pronome interrogativo di luogo"
    },
    "3. Istifham__10": {
        "arti_it": "Quando?",
        "desc_it": "Quando? (Pronome interrogativo di tempo)",
        "jenis_it": "Pronome interrogativo di tempo"
    },
    "4. Syarath__1": {
        "arti_it": "Chiunque / chi",
        "desc_it": "Chiunque (Sostantivo condizionale per persone)",
        "jenis_it": "Sostantivo condizionale (razionale)"
    },
    "4. Syarath__2": {
        "arti_it": "Qualsiasi cosa / qualunque cosa",
        "desc_it": "Qualsiasi cosa (Sostantivo condizionale per cose)",
        "jenis_it": "Sostantivo condizionale (non razionale)"
    },
    "4. Syarath__3": {
        "arti_it": "Ogni volta che / ogniqualvolta",
        "desc_it": "Ogni volta che (Avverbio condizionale temporale)",
        "jenis_it": "Avverbio condizionale temporale"
    },
    "4. Syarath__4": {
        "arti_it": "Qualunque / qualsiasi",
        "desc_it": "Qualunque (Sostantivo condizionale di scelta)",
        "jenis_it": "Sostantivo condizionale di scelta"
    },
    "4. Syarath__5": {
        "arti_it": "Qualunque dei due (enfatico)",
        "desc_it": "Qualunque dei due termini (Sostantivo condizionale con Ma enfatica)",
        "jenis_it": "Sostantivo condizionale composto"
    },
    "5. Isyarah__1": {
        "arti_it": "Questo / quello (maschile singolare)",
        "desc_it": "Questo / quello (Pronome dimostrativo maschile singolare)",
        "jenis_it": "Pronome dimostrativo (maschile singolare)"
    },
    "5. Isyarah__2": {
        "arti_it": "Questi / coloro (plurale)",
        "desc_it": "Questi / quelli (Pronome dimostrativo plurale)",
        "jenis_it": "Pronome dimostrativo (plurale)"
    },
    "5. Isyarah__3": {
        "arti_it": "Questa / quella (femminile singolare)",
        "desc_it": "Questa / quella (Pronome dimostrativo femminile singolare)",
        "jenis_it": "Pronome dimostrativo (femminile singolare)"
    },
    "5. Isyarah__4": {
        "arti_it": "Quella / quelle (femminile / plurale non razionale)",
        "desc_it": "Quella / quelle (Dimostrativo lontano per femminile o plurale)",
        "jenis_it": "Pronome dimostrativo lontano"
    },
    "5. Isyarah__5": {
        "arti_it": "Qui / in questo luogo",
        "desc_it": "Qui (Avverbio dimostrativo di luogo vicino)",
        "jenis_it": "Avverbio dimostrativo di luogo"
    },
    "5. Isyarah__6": {
        "arti_it": "Là / colà / in quel luogo",
        "desc_it": "Là (Avverbio dimostrativo di luogo lontano)",
        "jenis_it": "Avverbio dimostrativo di luogo"
    },
    "5. Isyarah__7": {
        "arti_it": "Questi due (duale maschile)",
        "desc_it": "Questi due (Pronome dimostrativo duale maschile)",
        "jenis_it": "Pronome dimostrativo duale"
    },
    "5. Isyarah__8": {
        "arti_it": "Queste due / quelle due (duale femminile)",
        "desc_it": "Queste due / quelle due (Dimostrativo duale femminile)",
        "jenis_it": "Pronome dimostrativo duale femminile"
    },
    "6. Isim Fi'il__1": {
        "arti_it": "Gloria a / Gloria sia ad Allah",
        "desc_it": "Gloria ad Allah, Egli è puro da ogni imperfezione (Nome verbale di lode)",
        "jenis_it": "Nome verbale (Lode)"
    },
    "6. Isim Fi'il__2": {
        "arti_it": "Portate! / Mostrate!",
        "desc_it": "Portate la vostra prova (Nome verbale imperativo)",
        "jenis_it": "Nome verbale (imperativo)"
    },
    "6. Isim Fi'il__3": {
        "arti_it": "Uffa! / Vergogna! (esclamazione di sdegno)",
        "desc_it": "Uffa / vergogna (Nome verbale tempo presente esprimente disgusto)",
        "jenis_it": "Nome verbale (disgusto)"
    },
    "6. Isim Fi'il__4": {
        "arti_it": "Mi rifugio in Allah / Che Allah non voglia",
        "desc_it": "Cerco rifugio in Allah (Nome verbale di rifugio)",
        "jenis_it": "Nome verbale (rifugio)"
    },
    "6. Isim Fi'il__5": {
        "arti_it": "Venite! / Accorrete!",
        "desc_it": "Venite qui / portate (Nome verbale imperativo)",
        "jenis_it": "Nome verbale (imperativo)"
    },
    "6. Isim Fi'il__6": {
        "arti_it": "Lungi da ciò! / Impossibile!",
        "desc_it": "Quanto è lontano! (Nome verbale tempo passato)",
        "jenis_it": "Nome verbale (tempo passato)"
    },
    "6. Isim Fi'il__7": {
        "arti_it": "Prendete e leggete!",
        "desc_it": "Prendete e leggete il mio libro (Nome verbale imperativo)",
        "jenis_it": "Nome verbale (imperativo)"
    },
    "6. Isim Fi'il__8": {
        "arti_it": "Vieni qui! / Fatti avanti!",
        "desc_it": "Vieni a me (Nome verbale imperativo di invito)",
        "jenis_it": "Nome verbale (invito)"
    },
    "7. Fi'il Jamid__1": {
        "arti_it": "Non è / non sono",
        "desc_it": "Non essere / non è (Verbo difettivo di negazione)",
        "jenis_it": "Verbo difettivo di negazione"
    },
    "7. Fi'il Jamid__2": {
        "arti_it": "Che pessimo...",
        "desc_it": "Che pessimo... (Verbo difettivo di biasimo)",
        "jenis_it": "Verbo difettivo di biasimo"
    },
    "7. Fi'il Jamid__3": {
        "arti_it": "Forse / può darsi che",
        "desc_it": "Forse / può darsi che (Verbo difettivo di speranza)",
        "jenis_it": "Verbo difettivo di speranza"
    },
    "7. Fi'il Jamid__4": {
        "arti_it": "Che eccellente...",
        "desc_it": "Che eccellente... (Verbo difettivo di lode)",
        "jenis_it": "Verbo difettivo di lode"
    },
    "7. Fi'il Jamid__5": {
        "arti_it": "Che pessima cosa è ciò che",
        "desc_it": "Che pessima cosa è ciò che (Verbo difettivo di biasimo composto con Ma)",
        "jenis_it": "Verbo difettivo di biasimo"
    },
    "7. Fi'il Jamid__6": {
        "arti_it": "Cominciarono a...",
        "desc_it": "Cominciarono a coprirsi con le foglie (Verbo difettivo di inizio)",
        "jenis_it": "Verbo difettivo di inizio"
    },
    "7. Fi'il Jamid__7": {
        "arti_it": "Che Allah non voglia! / Lungi da Allah",
        "desc_it": "Che Allah non voglia! (Verbo difettivo di esenzione e purezza)",
        "jenis_it": "Verbo difettivo di esenzione"
    },
    "7. Fi'il Jamid__8": {
        "arti_it": "Che eccellente cosa è ciò che",
        "desc_it": "Che eccellente cosa è ciò a cui vi esorta (Verbo difettivo di lode composto con Ma)",
        "jenis_it": "Verbo difettivo di lode"
    },
    "2. Isim Mawshul__1": {
        "arti_it": "Ciò che / quel che",
        "desc_it": "Pronome relativo generale per entità non razionali (Ma)",
        "jenis_it": "Pronome relativo generale (non razionale)"
    },
    "2. Isim Mawshul__2": {
        "arti_it": "Coloro che (plurale maschile)",
        "desc_it": "Coloro che / i quali (pronome relativo plurale maschile)",
        "jenis_it": "Pronome relativo plurale maschile"
    },
    "2. Isim Mawshul__3": {
        "arti_it": "Chi / colui che",
        "desc_it": "Pronome relativo generale per esseri razionali (Man)",
        "jenis_it": "Pronome relativo generale (razionale)"
    },
    "2. Isim Mawshul__4": {
        "arti_it": "Colui che (maschile singolare)",
        "desc_it": "Colui che / il quale (pronome relativo maschile singolare)",
        "jenis_it": "Pronome relativo maschile singolare"
    },
    "2. Isim Mawshul__5": {
        "arti_it": "Quale / chiunque di loro",
        "desc_it": "Quale / chiunque tra loro (pronome relativo declinabile)",
        "jenis_it": "Pronome relativo"
    },
    "2. Isim Mawshul__6": {
        "arti_it": "Colei che (femminile singolare)",
        "desc_it": "Colei che / la quale (pronome relativo femminile singolare)",
        "jenis_it": "Pronome relativo femminile singolare"
    },
    "2. Isim Mawshul__7": {
        "arti_it": "Coloro che / le donne che (plurale femminile)",
        "desc_it": "Coloro che / le quali (pronome relativo plurale femminile)",
        "jenis_it": "Pronome relativo plurale femminile"
    },
    "2. Isim Mawshul__8": {
        "arti_it": "Coloro che / le donne che (plurale femminile variante)",
        "desc_it": "Coloro che / le quali (pronome relativo plurale femminile variante)",
        "jenis_it": "Pronome relativo plurale femminile"
    },
    "2. Isim Mawshul__9": {
        "arti_it": "Coloro due che (duale maschile)",
        "desc_it": "Coloro due che (pronome relativo duale maschile)",
        "jenis_it": "Pronome relativo duale maschile"
    },
    "2. Isim Mawshul__10": {
        "arti_it": "Qualunque / qualsiasi (femminile)",
        "desc_it": "Qualunque / qualsiasi (pronome relativo femminile)",
        "jenis_it": "Pronome relativo (femminile)"
    },
    "3. Isim Istifham__1": {
        "arti_it": "Cosa? / Che cosa?",
        "desc_it": "Cosa? / Che cosa? (Pronome interrogativo per cose)",
        "jenis_it": "Pronome interrogativo"
    },
    "3. Isim Istifham__2": {
        "arti_it": "Come?",
        "desc_it": "Come? (Pronome interrogativo di modo)",
        "jenis_it": "Pronome interrogativo di modo"
    },
    "3. Isim Istifham__3": {
        "arti_it": "Chi?",
        "desc_it": "Chi? (Pronome interrogativo per persone)",
        "jenis_it": "Pronome interrogativo"
    },
    "3. Isim Istifham__4": {
        "arti_it": "Quale?",
        "desc_it": "Quale? (Pronome interrogativo di scelta)",
        "jenis_it": "Pronome interrogativo di scelta"
    },
    "3. Isim Istifham__5": {
        "arti_it": "Come? / Da dove?",
        "desc_it": "Come? / Da dove? (Pronome interrogativo di modo o provenienza)",
        "jenis_it": "Pronome interrogativo"
    },
    "3. Isim Istifham__6": {
        "arti_it": "Che cos'è che?",
        "desc_it": "Che cos'è che? (Pronome interrogativo composto enfatico)",
        "jenis_it": "Pronome interrogativo composto"
    },
    "3. Isim Istifham__7": {
        "arti_it": "Quanto? / Per quanto tempo?",
        "desc_it": "Quanto? (Pronome interrogativo di quantità o tempo)",
        "jenis_it": "Pronome interrogativo di quantità"
    },
    "3. Isim Istifham__8": {
        "arti_it": "Perché? / A che scopo?",
        "desc_it": "Perché? / Per quale motivo? (Interrogativo di causa, Li + Ma)",
        "jenis_it": "Interrogativo di causa"
    },
    "3. Isim Istifham__9": {
        "arti_it": "Dove?",
        "desc_it": "Dove? (Pronome interrogativo di luogo)",
        "jenis_it": "Pronome interrogativo di luogo"
    },
    "3. Isim Istifham__10": {
        "arti_it": "Quando?",
        "desc_it": "Quando? (Pronome interrogativo di tempo)",
        "jenis_it": "Pronome interrogativo di tempo"
    },
    "4. Isim Syarath__1": {
        "arti_it": "Chiunque / chi",
        "desc_it": "Chiunque (Sostantivo condizionale per persone)",
        "jenis_it": "Sostantivo condizionale (razionale)"
    },
    "4. Isim Syarath__2": {
        "arti_it": "Qualsiasi cosa / qualunque cosa",
        "desc_it": "Qualsiasi cosa (Sostantivo condizionale per cose)",
        "jenis_it": "Sostantivo condizionale (non razionale)"
    },
    "4. Isim Syarath__3": {
        "arti_it": "Ogni volta che / ogniqualvolta",
        "desc_it": "Ogni volta che (Avverbio condizionale temporale)",
        "jenis_it": "Avverbio condizionale temporale"
    },
    "4. Isim Syarath__4": {
        "arti_it": "Qualunque / qualsiasi",
        "desc_it": "Qualunque (Sostantivo condizionale di scelta)",
        "jenis_it": "Sostantivo condizionale di scelta"
    },
    "4. Isim Syarath__5": {
        "arti_it": "Qualunque dei due (enfatico)",
        "desc_it": "Qualunque dei due termini (Sostantivo condizionale con Ma enfatica)",
        "jenis_it": "Sostantivo condizionale composto"
    },
    "5. Isim Isyarah__1": {
        "arti_it": "Questo / quello (maschile singolare)",
        "desc_it": "Questo / quello (Pronome dimostrativo maschile singolare)",
        "jenis_it": "Pronome dimostrativo (maschile singolare)"
    },
    "5. Isim Isyarah__2": {
        "arti_it": "Questi / coloro (plurale)",
        "desc_it": "Questi / quelli (Pronome dimostrativo plurale)",
        "jenis_it": "Pronome dimostrativo (plurale)"
    },
    "5. Isim Isyarah__3": {
        "arti_it": "Questa / quella (femminile singolare)",
        "desc_it": "Questa / quella (Pronome dimostrativo femminile singolare)",
        "jenis_it": "Pronome dimostrativo (femminile singolare)"
    },
    "5. Isim Isyarah__4": {
        "arti_it": "Quella / quelle (femminile / plurale non razionale)",
        "desc_it": "Quella / quelle (Dimostrativo lontano per femminile o plurale)",
        "jenis_it": "Pronome dimostrativo lontano"
    },
    "5. Isim Isyarah__5": {
        "arti_it": "Qui / in questo luogo",
        "desc_it": "Qui (Avverbio dimostrativo di luogo vicino)",
        "jenis_it": "Avverbio dimostrativo di luogo"
    },
    "5. Isim Isyarah__6": {
        "arti_it": "Là / colà / in quel luogo",
        "desc_it": "Là (Avverbio dimostrativo di luogo lontano)",
        "jenis_it": "Avverbio dimostrativo di luogo"
    },
    "5. Isim Isyarah__7": {
        "arti_it": "Questi due (duale maschile)",
        "desc_it": "Questi due (Pronome dimostrativo duale maschile)",
        "jenis_it": "Pronome dimostrativo duale"
    },
    "5. Isim Isyarah__8": {
        "arti_it": "Queste due / quelle due (duale femminile)",
        "desc_it": "Queste due / quelle due (Dimostrativo duale femminile)",
        "jenis_it": "Pronome dimostrativo duale femminile"
    },
    "1a": {
        "arti_it": "Egli / Lui (singolare maschile)",
        "desc_it": "Egli / Lui (pronome personale isolato nominativo 3a persona maschile singolare)",
        "jenis_it": "Pronome personale isolato nominativo"
    },
    "1b": {
        "arti_it": "Suo / lo / gli",
        "desc_it": "Suo / lo / gli (pronome personale suffisso 3a persona maschile singolare)",
        "jenis_it": "Pronome suffisso"
    },
    "1c": {
        "arti_it": "Solo Lui",
        "desc_it": "Solo Lui (pronome personale isolato accusativo 3a persona maschile singolare)",
        "jenis_it": "Pronome isolato accusativo"
    },
    "2a": {
        "arti_it": "Essi due",
        "desc_it": "Essi due (pronome personale isolato nominativo 3a persona duale)",
        "jenis_it": "Pronome isolato nominativo (duale)"
    },
    "2b": {
        "arti_it": "Di loro due / loro due",
        "desc_it": "Di loro due / loro due (pronome personale suffisso 3a persona duale)",
        "jenis_it": "Pronome suffisso (duale)"
    },
    "3a": {
        "arti_it": "Essi / Loro (plurale maschile)",
        "desc_it": "Essi / Loro (pronome personale isolato nominativo 3a persona maschile plurale)",
        "jenis_it": "Pronome isolato nominativo (plurale)"
    },
    "3b": {
        "arti_it": "Loro / li (plurale maschile)",
        "desc_it": "Loro / li (pronome personale suffisso 3a persona maschile plurale)",
        "jenis_it": "Pronome suffisso (plurale)"
    },
    "3c": {
        "arti_it": "Solo loro (plurale maschile)",
        "desc_it": "Solo loro (pronome personale isolato accusativo 3a persona maschile plurale)",
        "jenis_it": "Pronome isolato accusativo (plurale)"
    },
    "4a": {
        "arti_it": "Ella / Lei (singolare femminile)",
        "desc_it": "Ella / Lei (pronome personale isolato nominativo 3a persona femminile singolare)",
        "jenis_it": "Pronome isolato nominativo (femminile)"
    },
    "4b": {
        "arti_it": "Suo / la / le",
        "desc_it": "Suo / la / le (pronome personale suffisso 3a persona femminile singolare)",
        "jenis_it": "Pronome suffisso (femminile)"
    },
    "5a": {
        "arti_it": "Esse / Loro (plurale femminile)",
        "desc_it": "Esse / Loro (pronome personale isolato nominativo 3a persona femminile plurale)",
        "jenis_it": "Pronome isolato nominativo (femminile plurale)"
    },
    "5b": {
        "arti_it": "Loro / le (plurale femminile)",
        "desc_it": "Loro / le (pronome personale suffisso 3a persona femminile plurale)",
        "jenis_it": "Pronome suffisso (femminile plurale)"
    },
    "6a": {
        "arti_it": "Tu (singolare maschile)",
        "desc_it": "Tu (pronome personale isolato nominativo 2a persona maschile singolare)",
        "jenis_it": "Pronome isolato nominativo"
    },
    "6b": {
        "arti_it": "Tuo / ti / te (singolare maschile)",
        "desc_it": "Tuo / ti / te (pronome personale suffisso 2a persona maschile singolare)",
        "jenis_it": "Pronome suffisso"
    },
    "6c": {
        "arti_it": "Solo Te (singolare maschile)",
        "desc_it": "Solo Te (pronome personale isolato accusativo 2a persona maschile singolare)",
        "jenis_it": "Pronome isolato accusativo"
    },
    "7a": {
        "arti_it": "Voi due",
        "desc_it": "Voi due (pronome personale isolato nominativo 2a persona duale)",
        "jenis_it": "Pronome isolato nominativo (duale)"
    },
    "7b": {
        "arti_it": "Di voi due / voi due",
        "desc_it": "Di voi due / voi due (pronome personale suffisso 2a persona duale)",
        "jenis_it": "Pronome suffisso (duale)"
    },
    "8a": {
        "arti_it": "Voi (plurale maschile)",
        "desc_it": "Voi (pronome personale isolato nominativo 2a persona maschile plurale)",
        "jenis_it": "Pronome isolato nominativo (plurale)"
    },
    "8b": {
        "arti_it": "Vostro / vi (plurale maschile)",
        "desc_it": "Vostro / vi (pronome personale suffisso 2a persona maschile plurale)",
        "jenis_it": "Pronome suffisso (plurale)"
    },
    "8c": {
        "arti_it": "Solo voi (plurale maschile)",
        "desc_it": "Solo voi (pronome personale isolato accusativo 2a persona maschile plurale)",
        "jenis_it": "Pronome isolato accusativo (plurale)"
    },
    "9a": {
        "arti_it": "Tu (singolare femminile)",
        "desc_it": "Tu (pronome personale isolato nominativo 2a persona femminile singolare)",
        "jenis_it": "Pronome isolato nominativo (femminile)"
    },
    "9b": {
        "arti_it": "Tuo / ti (singolare femminile)",
        "desc_it": "Tuo / ti (pronome personale suffisso 2a persona femminile singolare)",
        "jenis_it": "Pronome suffisso (femminile)"
    },
    "10a": {
        "arti_it": "Voi (plurale femminile)",
        "desc_it": "Voi (pronome personale isolato nominativo 2a persona femminile plurale)",
        "jenis_it": "Pronome isolato nominativo (femminile plurale)"
    },
    "10b": {
        "arti_it": "Vostro / vi (plurale femminile)",
        "desc_it": "Vostro / vi (pronome personale suffisso 2a persona femminile plurale)",
        "jenis_it": "Pronome suffisso (femminile plurale)"
    },
    "11a": {
        "arti_it": "Io (1a persona singolare)",
        "desc_it": "Io (pronome personale isolato nominativo 1a persona singolare)",
        "jenis_it": "Pronome isolato nominativo"
    },
    "11b": {
        "arti_it": "Mio / mi / me",
        "desc_it": "Mio / mi / me (pronome personale suffisso 1a persona singolare)",
        "jenis_it": "Pronome suffisso"
    },
    "11c": {
        "arti_it": "Solo me",
        "desc_it": "Solo me (pronome personale isolato accusativo 1a persona singolare)",
        "jenis_it": "Pronome isolato accusativo"
    },
    "12a": {
        "arti_it": "Noi (1a persona plurale)",
        "desc_it": "Noi (pronome personale isolato nominativo 1a persona plurale)",
        "jenis_it": "Pronome isolato nominativo (plurale)"
    },
    "12b": {
        "arti_it": "Nostro / ci",
        "desc_it": "Nostro / ci (pronome personale suffisso 1a persona plurale)",
        "jenis_it": "Pronome suffisso (plurale)"
    },
    "12c": {
        "arti_it": "Solo noi",
        "desc_it": "Solo noi (pronome personale isolato accusativo 1a persona plurale)",
        "jenis_it": "Pronome isolato accusativo (plurale)"
    },
    "1": {
        "arti_it": "Questo / quello (maschile singolare)",
        "desc_it": "Questo / quello (Pronome dimostrativo maschile singolare)",
        "jenis_it": "Pronome dimostrativo (maschile singolare)"
    },
    "2": {
        "arti_it": "Questi / coloro (plurale)",
        "desc_it": "Questi / quelli (Pronome dimostrativo plurale)",
        "jenis_it": "Pronome dimostrativo (plurale)"
    },
    "3": {
        "arti_it": "Questa / quella (femminile singolare)",
        "desc_it": "Questa / quella (Pronome dimostrativo femminile singolare)",
        "jenis_it": "Pronome dimostrativo (femminile singolare)"
    },
    "4": {
        "arti_it": "Quella / quelle (femminile / plurale non razionale)",
        "desc_it": "Quella / quelle (Dimostrativo lontano per femminile o plurale)",
        "jenis_it": "Pronome dimostrativo lontano"
    },
    "5": {
        "arti_it": "Qui / in questo luogo",
        "desc_it": "Qui (Avverbio dimostrativo di luogo vicino)",
        "jenis_it": "Avverbio dimostrativo di luogo"
    },
    "6": {
        "arti_it": "Là / colà / in quel luogo",
        "desc_it": "Là (Avverbio dimostrativo di luogo lontano)",
        "jenis_it": "Avverbio dimostrativo di luogo"
    },
    "7": {
        "arti_it": "Questi due (duale maschile)",
        "desc_it": "Questi due (Pronome dimostrativo duale maschile)",
        "jenis_it": "Pronome dimostrativo duale"
    },
    "8": {
        "arti_it": "Queste due / quelle due (duale femminile)",
        "desc_it": "Queste due / quelle due (Dimostrativo duale femminile)",
        "jenis_it": "Pronome dimostrativo duale femminile"
    },
    "9": {
        "arti_it": "Dove?",
        "desc_it": "Dove? (Pronome interrogativo di luogo)",
        "jenis_it": "Pronome interrogativo di luogo"
    },
    "10": {
        "arti_it": "Quando?",
        "desc_it": "Quando? (Pronome interrogativo di tempo)",
        "jenis_it": "Pronome interrogativo di tempo"
    }
}

BENTUK_HARF_IT = {
    "1. Harf Nafyi": "1. Particelle Negative (Harf Nafyi - Negazione)",
    "2. Harf Tahqiq Taswif": "2. Particelle di Certezza e Futuro (Tahqiq & Taswif)",
    "3. Harf Syarat": "3. Particelle Condizionali (Harf Syarat)",
    "4. Harf Mashdariyah": "4. Particelle Masdarique / Infinitive (Harf Mashdariyah)",
    "5. Harf Zaidah": "5. Particelle Enfatizzanti / Ridondanti (Harf Zaidah)",
    "6. Harf Istifham": "6. Particelle Interrogative (Harf Istifham)",
    "7. Harf Jawab": "7. Particelle di Risposta (Harf Jawab)",
    "8. Harf Ibtida'": "8. Particelle Introduttive (Harf Ibtida')",
    "9. Harf Tafshil": "9. Particelle di Dettaglio / Esplicative (Harf Tafshil)",
    "10. Harf Mufaja'ah": "10. Particelle di Sorpresa (Harf Mufaja'ah)",
    "11. Harf Mufassirah": "11. Particelle Interpretative (Harf Mufassirah)",
    "12. Harf Istiftahiyah": "12. Particelle di Apertura (Harf Istiftahiyah)",
    "13. Harf Rada'": "13. Particelle di Repulsione / Rimprovero (Harf Rada')",
    "14. Harf Ta'ajjub": "14. Particelle di Stupore (Harf Ta'ajjub)",
    "15. Harf Fariqah": "15. Particelle Distintive (Harf Fariqah)",
    "16. Harf Mauthi'ah": "16. Particelle Introduttive al Giuramento (Harf Mauthi'ah)",
    "17. Harf Mabany": "17. Particelle di Costruzione / Lettere (Harf Mabany)"
}

ITALIAN_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {
        "arti_it": "Non / no (negazione)",
        "desc_it": "Particella negativa generale (La)",
        "jenis_it": "Particella negativa"
    },
    "1. Harf Nafyi__2": {
        "arti_it": "Non / niente / affatto",
        "desc_it": "Particella negativa per passato e presente (Ma)",
        "jenis_it": "Particella negativa"
    },
    "1. Harf Nafyi__3": {
        "arti_it": "Non... se non / soltanto",
        "desc_it": "Particella negativa di eccezione e restrizione (In... illa)",
        "jenis_it": "Particella restrittiva"
    },
    "1. Harf Nafyi__4": {
        "arti_it": "Non c'è forse? / Non è così?",
        "desc_it": "Particella interrogativa con valore di negazione retorica (Hal)",
        "jenis_it": "Particella interrogativa retorica"
    },
    "1. Harf Nafyi__5": {
        "arti_it": "Non è più (tempo)",
        "desc_it": "Particella negativa applicata ai sostantivi di tempo (Lata)",
        "jenis_it": "Particella negativa temporale"
    },
    "1. Harf Nafyi__6": {
        "arti_it": "Cos'altro se non / niente",
        "desc_it": "Particella interrogativa composta con valore negativo (Madha)",
        "jenis_it": "Particella interrogativa retorica"
    },
    "2. Harf Tahqiq Taswif__7": {
        "arti_it": "Certamente / davvero / già",
        "desc_it": "Particella di asseverazione e certezza (Qad)",
        "jenis_it": "Particella di certezza (Tahqiq)"
    },
    "2. Harf Tahqiq Taswif__8": {
        "arti_it": "Presto / in futuro (avverrà)",
        "desc_it": "Particella indicante il futuro lontano (Sawfa)",
        "jenis_it": "Particella di futuro (Taswif)"
    },
    "3. Harf Syarat__9": {
        "arti_it": "Se / se mai (condizione irreale)",
        "desc_it": "Particella condizionale irreale o ipotetica (Law)",
        "jenis_it": "Particella condizionale"
    },
    "3. Harf Syarat__10": {
        "arti_it": "Se non fosse per / perché non",
        "desc_it": "Particella condizionale di impedimento (Lawla)",
        "jenis_it": "Particella condizionale di impedimento"
    },
    "3. Harf Syarat__11": {
        "arti_it": "Anche se / quand'anche",
        "desc_it": "Particella condizionale concessiva (Law)",
        "jenis_it": "Particella condizionale concessiva"
    },
    "3. Harf Syarat__12": {
        "arti_it": "Qualora / se mai",
        "desc_it": "Particella condizionale enfatica (Imma = In + Ma)",
        "jenis_it": "Particella condizionale enfatica"
    },
    "3. Harf Syarat__13": {
        "arti_it": "Qualsiasi segno / qualunque cosa",
        "desc_it": "Sostantivo condizionale generale (Mahma)",
        "jenis_it": "Sostantivo condizionale"
    },
    "4. Harf Mashdariyah__14": {
        "arti_it": "Finché / per tutto il tempo",
        "desc_it": "Particella infinitiva di durata temporale (Ma)",
        "jenis_it": "Particella infinitiva temporale"
    },
    "4. Harf Mashdariyah__15": {
        "arti_it": "Affinché non / per non",
        "desc_it": "Particella infinitiva con negazione (Alla = An + La)",
        "jenis_it": "Particella infinitiva negativa"
    },
    "4. Harf Mashdariyah__16": {
        "arti_it": "Che / di (infinitivo)",
        "desc_it": "Particella che trasforma la proposizione in infinito sostantivato (An)",
        "jenis_it": "Particella infinitiva (Masdariyyah)"
    },
    "4. Harf Mashdariyah__17": {
        "arti_it": "Desidererebbe che",
        "desc_it": "Particella infinitiva esprimente desiderio (Law)",
        "jenis_it": "Particella infinitiva di desiderio"
    },
    "4. Harf Mashdariyah__18": {
        "arti_it": "Di non adorare",
        "desc_it": "Particella infinitiva con divieto (An + La)",
        "jenis_it": "Particella infinitiva di divieto"
    },
    "4. Harf Mashdariyah__19": {
        "arti_it": "Che in verità",
        "desc_it": "Particella infinitiva alleggerita (An alleggerita da Anna)",
        "jenis_it": "Particella infinitiva alleggerita"
    },
    "5. Harf Zaidah__20": {
        "arti_it": "Così come / come",
        "desc_it": "Prefisso di comparazione con particella enfatica aggiunta (Kama = Ka + Ma)",
        "jenis_it": "Particella enfatica di comparazione"
    },
    "5. Harf Zaidah__21": {
        "arti_it": "Persino un moscerino o cosa superiore",
        "desc_it": "Particella enfatica esprimente indeterminatezza (Ma Za'idah)",
        "jenis_it": "Particella enfatica aggiunta"
    },
    "5. Harf Zaidah__22": {
        "arti_it": "Giuro solennemente",
        "desc_it": "Particella enfatica per rafforzare il giuramento (La Za'idah)",
        "jenis_it": "Particella enfatica di giuramento"
    },
    "5. Harf Zaidah__23": {
        "arti_it": "Per misericordia di Allah",
        "desc_it": "Preposizione con particella enfatica aggiunta (Bima = Bi + Ma)",
        "jenis_it": "Particella enfatica post-preposizionale"
    },
    "5. Harf Zaidah__24": {
        "arti_it": "Quando giunse il nunzio",
        "desc_it": "Particella enfatica dopo congiunzione temporale (An dopo Lamma)",
        "jenis_it": "Particella enfatica temporale"
    },
    "6. Harf Istifham__25": {
        "arti_it": "È forse? / Ha forse?",
        "desc_it": "Particella interrogativa per domande dirette e conferme (Hal)",
        "jenis_it": "Particella interrogativa (Istifham)"
    },
    "7. Harf Jawab__26": {
        "arti_it": "In tal caso / allora",
        "desc_it": "Particella di risposta e conseguenza (Idhan)",
        "jenis_it": "Particella di risposta e conseguenza"
    },
    "7. Harf Jawab__27": {
        "arti_it": "Sì, certamente! / Anzi!",
        "desc_it": "Particella di risposta affermativa a domanda negativa (Bala)",
        "jenis_it": "Particella di risposta affermativa"
    },
    "7. Harf Jawab__28": {
        "arti_it": "Sì / Certamente",
        "desc_it": "Particella di risposta affermativa di assenso (Na'am)",
        "jenis_it": "Particella affermativa"
    },
    "7. Harf Jawab__29": {
        "arti_it": "Sì, per il mio Signore!",
        "desc_it": "Particella di risposta affermativa con giuramento (I)",
        "jenis_it": "Particella affermativa con giuramento"
    },
    "8. Harf Ibtida'__30": {
        "arti_it": "Fino al punto che",
        "desc_it": "Particella introduttiva e iniziale (Hatta)",
        "jenis_it": "Particella introduttiva (Ibtida')"
    },
    "9. Harf Tafshil__31": {
        "arti_it": "Quanto a / per ciò che riguarda",
        "desc_it": "Particella di spiegazione dettagliata e condizione (Amma)",
        "jenis_it": "Particella esplicativa (Tafshil)"
    },
    "10. Harf Mufaja'ah__32": {
        "arti_it": "Ed ecco che all'improvviso",
        "desc_it": "Particella indicante evento improvviso e inaspettato (Idha)",
        "jenis_it": "Particella di sorpresa (Mufaja'ah)"
    },
    "11. Harf Mufassirah__33": {
        "arti_it": "Ossia / vale a dire",
        "desc_it": "Particella esplicativa introduttiva (An)",
        "jenis_it": "Particella esplicativa (Mufassirah)"
    },
    "12. Harf Istiftahiyah__34": {
        "arti_it": "Badate bene! / Sappiate!",
        "desc_it": "Particella di apertura e richiamo all'attenzione (Ala)",
        "jenis_it": "Particella di ammonimento iniziale"
    },
    "13. Harf Rada'__35": {
        "arti_it": "No davvero! / Niente affatto!",
        "desc_it": "Particella di energico rifiuto e severo rimprovero (Kalla)",
        "jenis_it": "Particella di rifiuto e rimprovero (Rada')"
    },
    "14. Harf Ta'ajjub__36": {
        "arti_it": "Quanto sono pazienti!",
        "desc_it": "Particella di esclamazione e stupore (Ma Ta'ajjubiyyah)",
        "jenis_it": "Particella esclamativa"
    },
    "15. Harf Fariqah__37": {
        "arti_it": "Certamente / per l'appunto",
        "desc_it": "Lam enfatica distintiva per affermazione (Lam Fariqah con In alleggerita)",
        "jenis_it": "Lam enfatica distintiva"
    },
    "16. Harf Mauthi'ah__38": {
        "arti_it": "Se... giuro certamente",
        "desc_it": "Lam preparatoria al giuramento condizionale (La-in)",
        "jenis_it": "Lam introduttiva al giuramento"
    },
    "17. Harf Mabany__39": {
        "arti_it": "Ha Mim",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (حم)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "17. Harf Mabany__40": {
        "arti_it": "Alif Lam Mim",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (الم)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "17. Harf Mabany__41": {
        "arti_it": "Alif Lam Ra",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (الر)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "17. Harf Mabany__42": {
        "arti_it": "Ta Sin Mim",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (طسم)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "17. Harf Mabany__43": {
        "arti_it": "Alif Lam Mim Ra",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (المر)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "17. Harf Mabany__44": {
        "arti_it": "Alif Lam Mim Sad",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (المص)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "17. Harf Mabany__45": {
        "arti_it": "Sad",
        "desc_it": "Lettera mistica isolata all'inizio della Sura (ص)",
        "jenis_it": "Lettera mistica (Muqatta'at)"
    },
    "17. Harf Mabany__46": {
        "arti_it": "Ta Sin",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (طس)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "17. Harf Mabany__47": {
        "arti_it": "Ta Ha",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (طه)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "17. Harf Mabany__48": {
        "arti_it": "'Ain Sin Qaf",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (عسق)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "17. Harf Mabany__49": {
        "arti_it": "Qaf",
        "desc_it": "Lettera mistica isolata all'inizio della Sura (ق)",
        "jenis_it": "Lettera mistica (Muqatta'at)"
    },
    "17. Harf Mabany__50": {
        "arti_it": "Kaf Ha Ya 'Ain Sad",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (كهيعص)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "17. Harf Mabany__51": {
        "arti_it": "Nun",
        "desc_it": "Lettera mistica isolata all'inizio della Sura (ن)",
        "jenis_it": "Lettera mistica (Muqatta'at)"
    },
    "17. Harf Mabany__52": {
        "arti_it": "Ya Sin",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (يس)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "1": {
        "arti_it": "Non / no (negazione)",
        "desc_it": "Particella negativa generale (La)",
        "jenis_it": "Particella negativa"
    },
    "2": {
        "arti_it": "Non / niente / affatto",
        "desc_it": "Particella negativa per passato e presente (Ma)",
        "jenis_it": "Particella negativa"
    },
    "3": {
        "arti_it": "Non... se non / soltanto",
        "desc_it": "Particella negativa di eccezione e restrizione (In... illa)",
        "jenis_it": "Particella restrittiva"
    },
    "4": {
        "arti_it": "Non c'è forse? / Non è così?",
        "desc_it": "Particella interrogativa con valore di negazione retorica (Hal)",
        "jenis_it": "Particella interrogativa retorica"
    },
    "5": {
        "arti_it": "Non è più (tempo)",
        "desc_it": "Particella negativa applicata ai sostantivi di tempo (Lata)",
        "jenis_it": "Particella negativa temporale"
    },
    "6": {
        "arti_it": "Cos'altro se non / niente",
        "desc_it": "Particella interrogativa composta con valore negativo (Madha)",
        "jenis_it": "Particella interrogativa retorica"
    },
    "7": {
        "arti_it": "Certamente / davvero / già",
        "desc_it": "Particella di asseverazione e certezza (Qad)",
        "jenis_it": "Particella di certezza (Tahqiq)"
    },
    "8": {
        "arti_it": "Presto / in futuro (avverrà)",
        "desc_it": "Particella indicante il futuro lontano (Sawfa)",
        "jenis_it": "Particella di futuro (Taswif)"
    },
    "9": {
        "arti_it": "Se / se mai (condizione irreale)",
        "desc_it": "Particella condizionale irreale o ipotetica (Law)",
        "jenis_it": "Particella condizionale"
    },
    "10": {
        "arti_it": "Se non fosse per / perché non",
        "desc_it": "Particella condizionale di impedimento (Lawla)",
        "jenis_it": "Particella condizionale di impedimento"
    },
    "11": {
        "arti_it": "Anche se / quand'anche",
        "desc_it": "Particella condizionale concessiva (Law)",
        "jenis_it": "Particella condizionale concessiva"
    },
    "12": {
        "arti_it": "Qualora / se mai",
        "desc_it": "Particella condizionale enfatica (Imma = In + Ma)",
        "jenis_it": "Particella condizionale enfatica"
    },
    "13": {
        "arti_it": "Qualsiasi segno / qualunque cosa",
        "desc_it": "Sostantivo condizionale generale (Mahma)",
        "jenis_it": "Sostantivo condizionale"
    },
    "14": {
        "arti_it": "Finché / per tutto il tempo",
        "desc_it": "Particella infinitiva di durata temporale (Ma)",
        "jenis_it": "Particella infinitiva temporale"
    },
    "15": {
        "arti_it": "Affinché non / per non",
        "desc_it": "Particella infinitiva con negazione (Alla = An + La)",
        "jenis_it": "Particella infinitiva negativa"
    },
    "16": {
        "arti_it": "Che / di (infinitivo)",
        "desc_it": "Particella che trasforma la proposizione in infinito sostantivato (An)",
        "jenis_it": "Particella infinitiva (Masdariyyah)"
    },
    "17": {
        "arti_it": "Desidererebbe che",
        "desc_it": "Particella infinitiva esprimente desiderio (Law)",
        "jenis_it": "Particella infinitiva di desiderio"
    },
    "18": {
        "arti_it": "Di non adorare",
        "desc_it": "Particella infinitiva con divieto (An + La)",
        "jenis_it": "Particella infinitiva di divieto"
    },
    "19": {
        "arti_it": "Che in verità",
        "desc_it": "Particella infinitiva alleggerita (An alleggerita da Anna)",
        "jenis_it": "Particella infinitiva alleggerita"
    },
    "20": {
        "arti_it": "Così come / come",
        "desc_it": "Prefisso di comparazione con particella enfatica aggiunta (Kama = Ka + Ma)",
        "jenis_it": "Particella enfatica di comparazione"
    },
    "21": {
        "arti_it": "Persino un moscerino o cosa superiore",
        "desc_it": "Particella enfatica esprimente indeterminatezza (Ma Za'idah)",
        "jenis_it": "Particella enfatica aggiunta"
    },
    "22": {
        "arti_it": "Giuro solennemente",
        "desc_it": "Particella enfatica per rafforzare il giuramento (La Za'idah)",
        "jenis_it": "Particella enfatica di giuramento"
    },
    "23": {
        "arti_it": "Per misericordia di Allah",
        "desc_it": "Preposizione con particella enfatica aggiunta (Bima = Bi + Ma)",
        "jenis_it": "Particella enfatica post-preposizionale"
    },
    "24": {
        "arti_it": "Quando giunse il nunzio",
        "desc_it": "Particella enfatica dopo congiunzione temporale (An dopo Lamma)",
        "jenis_it": "Particella enfatica temporale"
    },
    "25": {
        "arti_it": "È forse? / Ha forse?",
        "desc_it": "Particella interrogativa per domande dirette e conferme (Hal)",
        "jenis_it": "Particella interrogativa (Istifham)"
    },
    "26": {
        "arti_it": "In tal caso / allora",
        "desc_it": "Particella di risposta e conseguenza (Idhan)",
        "jenis_it": "Particella di risposta e conseguenza"
    },
    "27": {
        "arti_it": "Sì, certamente! / Anzi!",
        "desc_it": "Particella di risposta affermativa a domanda negativa (Bala)",
        "jenis_it": "Particella di risposta affermativa"
    },
    "28": {
        "arti_it": "Sì / Certamente",
        "desc_it": "Particella di risposta affermativa di assenso (Na'am)",
        "jenis_it": "Particella affermativa"
    },
    "29": {
        "arti_it": "Sì, per il mio Signore!",
        "desc_it": "Particella di risposta affermativa con giuramento (I)",
        "jenis_it": "Particella affermativa con giuramento"
    },
    "30": {
        "arti_it": "Fino al punto che",
        "desc_it": "Particella introduttiva e iniziale (Hatta)",
        "jenis_it": "Particella introduttiva (Ibtida')"
    },
    "31": {
        "arti_it": "Quanto a / per ciò che riguarda",
        "desc_it": "Particella di spiegazione dettagliata e condizione (Amma)",
        "jenis_it": "Particella esplicativa (Tafshil)"
    },
    "32": {
        "arti_it": "Ed ecco che all'improvviso",
        "desc_it": "Particella indicante evento improvviso e inaspettato (Idha)",
        "jenis_it": "Particella di sorpresa (Mufaja'ah)"
    },
    "33": {
        "arti_it": "Ossia / vale a dire",
        "desc_it": "Particella esplicativa introduttiva (An)",
        "jenis_it": "Particella esplicativa (Mufassirah)"
    },
    "34": {
        "arti_it": "Badate bene! / Sappiate!",
        "desc_it": "Particella di apertura e richiamo all'attenzione (Ala)",
        "jenis_it": "Particella di ammonimento iniziale"
    },
    "35": {
        "arti_it": "No davvero! / Niente affatto!",
        "desc_it": "Particella di energico rifiuto e severo rimprovero (Kalla)",
        "jenis_it": "Particella di rifiuto e rimprovero (Rada')"
    },
    "36": {
        "arti_it": "Quanto sono pazienti!",
        "desc_it": "Particella di esclamazione e stupore (Ma Ta'ajjubiyyah)",
        "jenis_it": "Particella esclamativa"
    },
    "37": {
        "arti_it": "Certamente / per l'appunto",
        "desc_it": "Lam enfatica distintiva per affermazione (Lam Fariqah con In alleggerita)",
        "jenis_it": "Lam enfatica distintiva"
    },
    "38": {
        "arti_it": "Se... giuro certamente",
        "desc_it": "Lam preparatoria al giuramento condizionale (La-in)",
        "jenis_it": "Lam introduttiva al giuramento"
    },
    "39": {
        "arti_it": "Ha Mim",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (حم)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "40": {
        "arti_it": "Alif Lam Mim",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (الم)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "41": {
        "arti_it": "Alif Lam Ra",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (الر)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "42": {
        "arti_it": "Ta Sin Mim",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (طسم)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "43": {
        "arti_it": "Alif Lam Mim Ra",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (المر)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "44": {
        "arti_it": "Alif Lam Mim Sad",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (المص)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "45": {
        "arti_it": "Sad",
        "desc_it": "Lettera mistica isolata all'inizio della Sura (ص)",
        "jenis_it": "Lettera mistica (Muqatta'at)"
    },
    "46": {
        "arti_it": "Ta Sin",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (طس)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "47": {
        "arti_it": "Ta Ha",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (طه)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "48": {
        "arti_it": "'Ain Sin Qaf",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (عسق)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "49": {
        "arti_it": "Qaf",
        "desc_it": "Lettera mistica isolata all'inizio della Sura (ق)",
        "jenis_it": "Lettera mistica (Muqatta'at)"
    },
    "50": {
        "arti_it": "Kaf Ha Ya 'Ain Sad",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (كهيعص)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    },
    "51": {
        "arti_it": "Nun",
        "desc_it": "Lettera mistica isolata all'inizio della Sura (ن)",
        "jenis_it": "Lettera mistica (Muqatta'at)"
    },
    "52": {
        "arti_it": "Ya Sin",
        "desc_it": "Lettere mistiche isolate all'inizio della Sura (يس)",
        "jenis_it": "Lettere mistiche (Muqatta'at)"
    }
}
