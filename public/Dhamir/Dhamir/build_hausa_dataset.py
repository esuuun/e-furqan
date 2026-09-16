#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to build Hausa dataset and enrich dhamir_data.json, dhamir_data.js,
harf_data.json, and harf_data.js with complete Hausa translations.
"""

import os
import sys
import json

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. 114 Surahs Hausa Names / Meanings
HAUSA_SURAHS = {
    "1": "Mabuɗiya (Buɗewa)",
    "2": "Saniya",
    "3": "Iyalan Imran",
    "4": "Mata",
    "5": "Teburin Abinci",
    "6": "Dabbobin Ni'ima",
    "7": "Makamai Masu Tsawo",
    "8": "Ganima",
    "9": "Tuba",
    "10": "Yunus",
    "11": "Hud",
    "12": "Yusuf",
    "13": "Tsawa",
    "14": "Ibrahim",
    "15": "Dutsen Hijr",
    "16": "Kudan Zuma",
    "17": "Tafiyar Dare",
    "18": "Kogo",
    "19": "Maryam",
    "20": "Ta-Ha",
    "21": "Annabawa",
    "22": "Aikin Hajji",
    "23": "Muminai",
    "24": "Haske",
    "25": "Rarrabewa (Furqan)",
    "26": "Mawaka",
    "27": "Tururuwa",
    "28": "Labarai",
    "29": "Gizo-gizo",
    "30": "Rumawa",
    "31": "Luqman",
    "32": "Sujada",
    "33": "Ƙungiyoyin Yaƙi",
    "34": "Saba'",
    "35": "Mahalicci",
    "36": "Ya-Sin",
    "37": "Masu Jeru-jeru",
    "38": "Sad",
    "39": "Rukuni-rukuni",
    "40": "Mai Gafara",
    "41": "Wadanda Aka Bayyana",
    "42": "Shawara",
    "43": "Kayan Ado (Zinariya)",
    "44": "Hayaki",
    "45": "Mai Durƙuso",
    "46": "Dutsen Yashi",
    "47": "Muhammad",
    "48": "Nasarar Buɗe Kasa",
    "49": "Dakuna",
    "50": "Qaf",
    "51": "Masu Watsawa",
    "52": "Dutsen Tur",
    "53": "Tauraro",
    "54": "Wata",
    "55": "Mai Rahama",
    "56": "Abin Da Zai Auku",
    "57": "Ƙarfe",
    "58": "Mai Jayayya",
    "59": "Taron Korar Kasa",
    "60": "Wadda Aka Jarabta",
    "61": "Sahu (Jeri)",
    "62": "Ranar Juma'a",
    "63": "Munafukai",
    "64": "Bayyanar Rashi",
    "65": "Saki",
    "66": "Haramt проек / Haramtaswa",
    "67": "Mulki",
    "68": "Alƙalami",
    "69": "Gaskiya Mai Tabbata",
    "70": "Matattakalar Sama",
    "71": "Nuhu",
    "72": "Aljanu",
    "73": "Mai Rufa da Tufafi",
    "74": "Mai Mayafi",
    "75": "Ranar Ƙiyama",
    "76": "Mutum",
    "77": "Wadanda Aka Aika",
    "78": "Babban Labari",
    "79": "Masu Fizge Rai",
    "80": "Ya Ɓata Fuska",
    "81": "Nannaɗewa",
    "82": "Tsagewa",
    "83": "Masu Satar Awo",
    "84": "Tsagewar Sama",
    "85": "Gidajen Taurari",
    "86": "Mai Ziyara Da Dare",
    "87": "Mafi Ɗaukaka",
    "88": "Mai Rufe Komai",
    "89": "Alfijir",
    "90": "Gari",
    "91": "Rana",
    "92": "Dare",
    "93": "Hantsi",
    "94": "Buɗe Ƙirji",
    "95": "Ɓaure",
    "96": "Gudan Jini",
    "97": "Daren Daraja",
    "98": "Hujja Bayyananniya",
    "99": "Girgizar Ƙasa",
    "100": "Dawakai Masu Gudu",
    "101": "Masifa Mai Ƙwanƙwasa",
    "102": "Gasar Tara Dukiya",
    "103": "Zamani",
    "104": "Mai Zagi da Gulma",
    "105": "Giwa",
    "106": "Kuraishawa",
    "107": "Taimakon Gaggawa",
    "108": "Alkawthara (Ni'ima Mai Yawa)",
    "109": "Kafirai",
    "110": "Taimako / Nasara",
    "111": "Zaren Kaba",
    "112": "Tsarkake Tauhidi",
    "113": "Hasken Asuba",
    "114": "Mutane"
}

# 2. 7 Categories (Bentuk Kata) in Hausa
BENTUK_KATA_HA = {
    '1. Dhamir': '1. Wakilan Suna (Dhamir - Pronouns)',
    '2. Mawshul': '2. Sunayen Sadarwa (Mawshul - Relative Pronouns)',
    '3. Istifham': '3. Kalmomin Tambaya (Istifham - Interrogatives)',
    '4. Syarath': '4. Kalmomin Sharaɗi (Syarath - Conditionals)',
    '5. Isyarah': '5. Sunayen Nuni (Isyarah - Demonstratives)',
    "6. Isim Fi'il": "6. Sunayen Aiki (Isim Fi'il - Verbal Nouns)",
    "7. Fi'il Jamid": "7. Ayyuka Kafaffu (Fi'il Jamid - Inflexible Verbs)"
}

# 3. 76 Jamid Mabny Grammatical Metadata in Hausa
HAUSA_GRAMMAR = {
    # 1. Dhamir
    '1. Dhamir__1a': {
        'arti_ha': 'SHI',
        'desc_ha': 'Shi (Mutum na 3 tilo na namiji, wakilin suna mai zaman kansa)',
        'jenis_ha': 'Munfashil (Mai Zaman Kansa)'
    },
    '1. Dhamir__1b': {
        'arti_ha': '..SA / ..SHI',
        'desc_ha': '...-sa / shi (Mutum na 3 tilo na namiji, wakilin suna mai maƙalewa)',
        'jenis_ha': 'Muttashil (Mai Maƙalewa)'
    },
    '1. Dhamir__1c': {
        'arti_ha': 'SHI KAƊAI',
        'desc_ha': 'Shi kaɗai / Gare shi kaɗai (Wakilin suna na abin yi mai zaman kansa, namiji tilo)',
        'jenis_ha': 'Munfashil Manshub (Abin Yi)'
    },
    '1. Dhamir__2a': {
        'arti_ha': 'SU BIYU',
        'desc_ha': 'Su biyu (Mutum na 3 biyu na maza ko mata, mai zaman kansa)',
        'jenis_ha': 'Munfashil (Mai Zaman Kansa)'
    },
    '1. Dhamir__2b': {
        'arti_ha': '..SU BIYU',
        'desc_ha': '...-su biyu (Mutum na 3 biyu na maza ko mata, mai maƙalewa)',
        'jenis_ha': 'Muttashil (Mai Maƙalewa)'
    },
    '1. Dhamir__3a': {
        'arti_ha': 'SU (MAZA)',
        'desc_ha': 'Su (Mutum na 3 jam\'i na maza, wakilin suna mai zaman kansa)',
        'jenis_ha': 'Munfashil (Mai Zaman Kansa)'
    },
    '1. Dhamir__3b': {
        'arti_ha': '..SU / ..SU (MAZA)',
        'desc_ha': '...-su (Mutum na 3 jam\'i na maza, wakilin suna mai maƙalewa)',
        'jenis_ha': 'Muttashil (Mai Maƙalewa)'
    },
    '1. Dhamir__3c': {
        'arti_ha': 'SU KAƊAI',
        'desc_ha': 'Su kaɗai / Gare su kaɗai (Wakilin suna na abin yi, jam\'in maza)',
        'jenis_ha': 'Munfashil Manshub (Abin Yi)'
    },
    '1. Dhamir__4a': {
        'arti_ha': 'ITA',
        'desc_ha': 'Ita (Mutum na 3 tilo na mace, wakilin suna mai zaman kansa)',
        'jenis_ha': 'Munfashil (Mai Zaman Kansa)'
    },
    '1. Dhamir__4b': {
        'arti_ha': '..TA / ..ITA',
        'desc_ha': '...-ta / ita (Mutum na 3 tilo na mace, wakilin suna mai maƙalewa)',
        'jenis_ha': 'Muttashil (Mai Maƙalewa)'
    },
    '1. Dhamir__5a': {
        'arti_ha': 'SU (MATA)',
        'desc_ha': 'Su (Mutum na 3 jam\'i na mata, wakilin suna mai zaman kansa)',
        'jenis_ha': 'Munfashil (Mai Zaman Kansa)'
    },
    '1. Dhamir__5b': {
        'arti_ha': '..SU (MATA)',
        'desc_ha': '...-su (Mutum na 3 jam\'i na mata, wakilin suna mai maƙalewa)',
        'jenis_ha': 'Muttashil (Mai Maƙalewa)'
    },
    '1. Dhamir__6a': {
        'arti_ha': 'KAI',
        'desc_ha': 'Kai (Mutum na 2 tilo na namiji, wakilin suna mai zaman kansa)',
        'jenis_ha': 'Munfashil (Mai Zaman Kansa)'
    },
    '1. Dhamir__6b': {
        'arti_ha': '..KA / ..KAI',
        'desc_ha': '...-ka / kai (Mutum na 2 tilo na namiji, wakilin suna mai maƙalewa)',
        'jenis_ha': 'Muttashil (Mai Maƙalewa)'
    },
    '1. Dhamir__6c': {
        'arti_ha': 'KAI KAƊAI',
        'desc_ha': 'Kai kaɗai / Gare ka kaɗai (Wakilin suna na abin yi, namiji tilo)',
        'jenis_ha': 'Munfashil Manshub (Abin Yi)'
    },
    '1. Dhamir__7a': {
        'arti_ha': 'KU BIYU',
        'desc_ha': 'Ku biyu (Mutum na 2 biyu na maza ko mata, mai zaman kansa)',
        'jenis_ha': 'Munfashil (Mai Zaman Kansa)'
    },
    '1. Dhamir__7b': {
        'arti_ha': '..KU BIYU',
        'desc_ha': '...-ku biyu (Mutum na 2 biyu na maza ko mata, mai maƙalewa)',
        'jenis_ha': 'Muttashil (Mai Maƙalewa)'
    },
    '1. Dhamir__8a': {
        'arti_ha': 'KU (MAZA)',
        'desc_ha': 'Ku (Mutum na 2 jam\'i na maza, wakilin suna mai zaman kansa)',
        'jenis_ha': 'Munfashil (Mai Zaman Kansa)'
    },
    '1. Dhamir__8b': {
        'arti_ha': '..KU (MAZA)',
        'desc_ha': '...-ku (Mutum na 2 jam\'i na maza, wakilin suna mai maƙalewa)',
        'jenis_ha': 'Muttashil (Mai Maƙalewa)'
    },
    '1. Dhamir__8c': {
        'arti_ha': 'KU KAƊAI',
        'desc_ha': 'Ku kaɗai / Gare ku kaɗai (Wakilin suna na abin yi, jam\'in maza)',
        'jenis_ha': 'Munfashil Manshub (Abin Yi)'
    },
    '1. Dhamir__9b': {
        'arti_ha': '..KI / ..KE',
        'desc_ha': '...-ki / ke (Mutum na 2 tilo na mace, wakilin suna mai maƙalewa)',
        'jenis_ha': 'Muttashil (Mai Maƙalewa)'
    },
    '1. Dhamir__11a': {
        'arti_ha': 'NI / INA',
        'desc_ha': 'Ni / Ina (Mutum na 1 mai magana tilo, namiji ko mace)',
        'jenis_ha': 'Munfashil (Mai Zaman Kansa)'
    },
    '1. Dhamir__11b': {
        'arti_ha': '..NA / ..NI',
        'desc_ha': '...-na / ni (Mutum na 1 mai magana tilo, mai maƙalewa)',
        'jenis_ha': 'Muttashil (Mai Maƙalewa)'
    },
    '1. Dhamir__11c': {
        'arti_ha': 'NI KAƊAI',
        'desc_ha': 'Ni kaɗai / Gare ni kaɗai (Wakilin suna na abin yi, mai magana tilo)',
        'jenis_ha': 'Munfashil Manshub (Abin Yi)'
    },
    '1. Dhamir__12a': {
        'arti_ha': 'MU / MUNA',
        'desc_ha': 'Mu / Muna (Mutum na 1 jam\'in masu magana, maza ko mata)',
        'jenis_ha': 'Munfashil (Mai Zaman Kansa)'
    },
    '1. Dhamir__12b': {
        'arti_ha': '..MU / ..MUNA',
        'desc_ha': '...-mu / mu (Mutum na 1 jam\'in masu magana, mai maƙalewa)',
        'jenis_ha': 'Muttashil (Mai Maƙalewa)'
    },
    '1. Dhamir__12c': {
        'arti_ha': 'MU KAƊAI',
        'desc_ha': 'Mu kaɗai / Gare mu kaɗai (Wakilin suna na abin yi, jam\'in masu magana)',
        'jenis_ha': 'Munfashil Manshub (Abin Yi)'
    },

    # 2. Mawshul
    '2. Mawshul__1': {
        'arti_ha': 'ABIN DA / WANDA',
        'desc_ha': 'Abin da / duk abin da (Sunan sadarwa ga abubuwan da ba su da hankali)',
        'jenis_ha': "Isim Mawshul (Ghairu 'Aqil)"
    },
    '2. Mawshul__2': {
        'arti_ha': 'WADANDA / WADANNAN DA',
        'desc_ha': 'Waɗanda (Sunan sadarwa na jam\'in maza masu hankali)',
        'jenis_ha': "Isim Mawshul Jam'i (Maza)"
    },
    '2. Mawshul__3': {
        'arti_ha': 'WANDA / DUK WANDA',
        'desc_ha': 'Wanda / duk wanda (Sunan sadarwa ga masu hankali)',
        'jenis_ha': "Isim Mawshul ('Aqil)"
    },
    '2. Mawshul__4': {
        'arti_ha': 'WANDA / ABIN DA',
        'desc_ha': 'Wanda / abin da (Sunan sadarwa na namiji tilo)',
        'jenis_ha': 'Isim Mawshul Mufrad (Namiji)'
    },
    '2. Mawshul__5': {
        'arti_ha': 'WANE / KOWANNE DAGA CIKI',
        'desc_ha': 'Wanne / kowane daga cikinsu (Sunan sadarwa mai shiga ko\'ina)',
        'jenis_ha': 'Isim Mawshul Mu\'rab'
    },
    '2. Mawshul__6': {
        'arti_ha': 'WADDA / ABIN DA',
        'desc_ha': 'Wadda / abin da (Sunan sadarwa na mace tilo ko jam\'in marasa hankali)',
        'jenis_ha': 'Isim Mawshul Mufrad (Mace)'
    },
    '2. Mawshul__7': {
        'arti_ha': 'WADANDA (MATA)',
        'desc_ha': 'Waɗanda (Sunan sadarwa na jam\'in mata)',
        'jenis_ha': "Isim Mawshul Jam'i (Mata)"
    },
    '2. Mawshul__8': {
        'arti_ha': 'WADANDA (MATA)',
        'desc_ha': 'Waɗanda (Sunan sadarwa na jam\'in mata - sigar Allaa\'ii)',
        'jenis_ha': "Isim Mawshul Jam'i (Mata)"
    },
    '2. Mawshul__9': {
        'arti_ha': 'SU BIYU WADANDA',
        'desc_ha': 'Su biyu waɗanda (Sunan sadarwa na maza biyu)',
        'jenis_ha': 'Isim Mawshul Muthanna (Maza biyu)'
    },
    '2. Mawshul__10': {
        'arti_ha': 'WACCE DAGA CIKI (MACE)',
        'desc_ha': 'Wacce daga cikinsu (Sunan sadarwa na mace)',
        'jenis_ha': 'Isim Mawshul Mu\'annath'
    },

    # 3. Istifham
    '3. Istifham__1': {
        'arti_ha': 'MENENE? / MECE CE?',
        'desc_ha': 'Menene? (Kalmar tambaya ga abubuwan da ba su da hankali)',
        'jenis_ha': "Isim Istifham (Ghairu 'Aqil)"
    },
    '3. Istifham__2': {
        'arti_ha': 'YAYA? / TA YAYA?',
        'desc_ha': 'Yaya? / ta yaya? (Kalmar tambayar yanayi ko hali)',
        'jenis_ha': 'Isim Istifham (Hal)'
    },
    '3. Istifham__3': {
        'arti_ha': 'WANENE? / SU WANENE?',
        'desc_ha': 'Wanene? (Kalmar tambaya ga masu hankali)',
        'jenis_ha': "Isim Istifham ('Aqil)"
    },
    '3. Istifham__4': {
        'arti_ha': 'WANNE? / WACCE?',
        'desc_ha': 'Wanne? / wacce? (Kalmar tambaya ta zaɓi)',
        'jenis_ha': 'Isim Istifham (Zaɓi)'
    },
    '3. Istifham__5': {
        'arti_ha': 'DAGA INA? / TA YAYA?',
        'desc_ha': 'Daga ina? / ta yaya? (Kalmar tambayar asali ko yanayi)',
        'jenis_ha': 'Isim Istifham (Wuri / Yanayi)'
    },
    '3. Istifham__6': {
        'arti_ha': 'MENENE WANNAN DA?',
        'desc_ha': 'Menene wannan da? (Tambaya mai ƙarfi da haɗa Ma da Dha)',
        'jenis_ha': 'Isim Istifham Murakkab'
    },
    '3. Istifham__7': {
        'arti_ha': 'NAWA? / TSAWON INA?',
        'desc_ha': 'Nawa? / tsawon yaya? (Kalmar tambayar adadi ko lokaci)',
        'jenis_ha': "Isim Istifham ('Adad)"
    },
    '3. Istifham__8': {
        'arti_ha': 'DON ME? / ME YA SA?',
        'desc_ha': 'Don me? / me ya sa? (Tambayar dalili, Li + Ma)',
        'jenis_ha': 'Harf Jar + Istifham'
    },
    '3. Istifham__9': {
        'arti_ha': 'A INA? / INA?',
        'desc_ha': 'A ina? / ina? (Kalmar tambayar wuri)',
        'jenis_ha': 'Isim Istifham (Wuri / Makan)'
    },
    '3. Istifham__10': {
        'arti_ha': 'YAUSHE?',
        'desc_ha': 'Yaushe? (Kalmar tambayar lokaci)',
        'jenis_ha': 'Isim Istifham (Lokaci / Zaman)'
    },

    # 4. Syarath
    '4. Syarath__1': {
        'arti_ha': 'DUK WANDA / WANDA YA',
        'desc_ha': 'Duk wanda / duk wanda ya (Kalmar sharaɗi mai sanya aikatau jazm)',
        'jenis_ha': "Isim Syarat ('Aqil)"
    },
    '4. Syarath__2': {
        'arti_ha': 'DUK ABIN DA',
        'desc_ha': 'Duk abin da (Kalmar sharaɗi ga abubuwan da ba su da hankali)',
        'jenis_ha': "Isim Syarat (Ghairu 'Aqil)"
    },
    '4. Syarath__3': {
        'arti_ha': 'DUK LOKACIN DA / KULLUM DA',
        'desc_ha': 'Duk lokacin da / duk sanda (Kowace da ta zama kalmar sharaɗin lokaci)',
        'jenis_ha': 'Dharf Sharat Zamani'
    },
    '4. Syarath__4': {
        'arti_ha': 'KOWANNE DAGA CIKI',
        'desc_ha': 'Kowanne / duk wanne daga cikinsu (Kalmar sharaɗi mai amsa kowane yanayi)',
        'jenis_ha': 'Isim Syarat Mu\'rab'
    },
    '4. Syarath__5': {
        'arti_ha': 'KOWANNE DAGA CIKI (MAI ƘARFI)',
        'desc_ha': 'Kowanne daga cikinsu (Sharaɗi tare da ƙarfafawar Ma)',
        'jenis_ha': 'Isim Syarat Murakkab'
    },

    # 5. Isyarah
    '5. Isyarah__1': {
        'arti_ha': 'WANNAN / WANCAN (NAMIJI)',
        'desc_ha': 'Wannan / wancan (Sunan nuni na kusa ko na nesa, namiji tilo)',
        'jenis_ha': 'Isim Isyarah (Namiji Tilo)'
    },
    '5. Isyarah__2': {
        'arti_ha': 'WADANNAN / WADANCAN',
        'desc_ha': 'Waɗannan / waɗancan (Sunan nuni na jam\'i, maza da mata)',
        'jenis_ha': "Isim Isyarah (Jam'i)"
    },
    '5. Isyarah__3': {
        'arti_ha': 'WANNAN (MACE)',
        'desc_ha': 'Wannan (Sunan nuni na kusa, mace tilo ko jam\'in marasa hankali)',
        'jenis_ha': 'Isim Isyarah (Mace Tilo)'
    },
    '5. Isyarah__4': {
        'arti_ha': 'WANCAN / WADANCAN (MACE)',
        'desc_ha': 'Wancan / waɗancan (Sunan nuni na nesa, mace tilo ko jam\'i)',
        'jenis_ha': 'Isim Isyarah Ba\'id'
    },
    '5. Isyarah__5': {
        'arti_ha': 'A NAN / NAN',
        'desc_ha': 'A nan (Sunan nuni na wuri na kusa)',
        'jenis_ha': 'Isim Isyarah Makan (Kusa)'
    },
    '5. Isyarah__6': {
        'arti_ha': 'A CAN / CAN',
        'desc_ha': 'A can (Sunan nuni na wuri na nesa)',
        'jenis_ha': 'Isim Isyarah Makan (Nesa)'
    },
    '5. Isyarah__7': {
        'arti_ha': 'WADAN NAN BIYU (MAZA)',
        'desc_ha': 'Waɗannan biyu (Sunan nuni na maza biyu)',
        'jenis_ha': 'Isim Isyarah Muthanna (Maza)'
    },
    '5. Isyarah__8': {
        'arti_ha': 'WADAN NAN BIYU (MATA)',
        'desc_ha': 'Waɗannan biyu (Sunan nuni na mata biyu)',
        'jenis_ha': 'Isim Isyarah Muthanna (Mata)'
    },

    # 6. Isim Fi'il
    "6. Isim Fi'il__1": {
        'arti_ha': 'TSARKI YA TABBATA!',
        'desc_ha': 'Tsarki ya tabbata ga Allah (Tasbihi da ɗaukaka)',
        'jenis_ha': 'Isim Masdar / Tasbih'
    },
    "6. Isim Fi'il__2": {
        'arti_ha': 'KU KAWO / KU FITAR DA',
        'desc_ha': 'Ku kawo / ku gabatar da hujja (Sunan aiki na umarni = Haatuu)',
        'jenis_ha': "Isim Fi'il Amr"
    },
    "6. Isim Fi'il__3": {
        'arti_ha': 'TUF! / ASHSHA!',
        'desc_ha': 'Tuf! / Ashsha! (Sunan aiki na nuna ƙyamata da kosawa = Uff)',
        'jenis_ha': "Isim Fi'il Mudhari'"
    },
    "6. Isim Fi'il__4": {
        'arti_ha': 'ALLAH YA TSARE / TSARI',
        'desc_ha': 'Ina neman tsari da Allah (Neman tsari daga aikin saɓo)',
        'jenis_ha': 'Isim Masdar Manshub'
    },
    "6. Isim Fi'il__5": {
        'arti_ha': 'KU ZO NAN!',
        'desc_ha': 'Ku zo nan / ku matso kusa (Sunan aiki na umarni = Halumma)',
        'jenis_ha': "Isim Fi'il Amr"
    },
    "6. Isim Fi'il__6": {
        'arti_ha': 'INA! YA YI NESA!',
        'desc_ha': 'Ina! Ya yi nesa kwarai / ba zai yiwu ba (Sunan aiki na da = Hayhata)',
        'jenis_ha': "Isim Fi'il Madhi"
    },
    "6. Isim Fi'il__7": {
        'arti_ha': 'GA SHI KU KARANTA!',
        'desc_ha': 'Ga shi ku karanta littafina (Sunan aiki na umarni = Haa\'um)',
        'jenis_ha': "Isim Fi'il Amr"
    },
    "6. Isim Fi'il__8": {
        'arti_ha': 'ZO MANA! / KA MATSO!',
        'desc_ha': 'Zo mana / ka matso (Sunan aiki na umarni = Hayta)',
        'jenis_ha': "Isim Fi'il Amr"
    },

    # 7. Fi'il Jamid
    "7. Fi'il Jamid__1": {
        'arti_ha': 'BA SHI BA NE / BA HAKA BA NE',
        'desc_ha': 'Ba shi ba ne / ba a ciki ba (Aiki kafaffe na ƙaryatawa daga \'yan uwan Kana)',
        'jenis_ha': "Fi'il Jamid Naqis (Nafi)"
    },
    "7. Fi'il Jamid__2": {
        'arti_ha': 'KILA / TASHEN TSAMMANI',
        'desc_ha': 'Kila / ana sa ran cewa (Aiki kafaffe na fata da sa rai = \'Asaa)',
        'jenis_ha': "Fi'il Jamid Raja'"
    },
    "7. Fi'il Jamid__3": {
        'arti_ha': 'MADALLA DA / MAFI KYAU',
        'desc_ha': 'Madalla da / mafi kyawun abu (Aiki kafaffe na yabo = Ni\'ma)',
        'jenis_ha': "Fi'il Jamid Madh (Yabo)"
    },
    "7. Fi'il Jamid__4": {
        'arti_ha': 'TIKƘAS DA / MAFI MUGU',
        'desc_ha': 'Tikƙas da / mafi munin abu (Aiki kafaffe na zagi da soki = Bi\'sa)',
        'jenis_ha': "Fi'il Jamid Dzamm (Soki)"
    },
    "7. Fi'il Jamid__5": {
        'arti_ha': 'TIKƘAS DA ABIN DA',
        'desc_ha': 'Tikƙas da abin da suka sayar da ransu da shi (Bi\'sa + Ma)',
        'jenis_ha': "Fi'il Jamid Dzamm Murakkab"
    },
    "7. Fi'il Jamid__6": {
        'arti_ha': 'SUKA FARA / SUKA DUƘUFA',
        'desc_ha': 'Suka fara / suka duƙufa (Aiki na fara wani aiki = Tafiqa)',
        'jenis_ha': "Fi'il Shuru'"
    },
    "7. Fi'il Jamid__7": {
        'arti_ha': 'TSARKI YA TABBATA GA ALLAH',
        'desc_ha': 'Karewa da tsarkake Allah daga kowane aibi (Haashaa lillah)',
        'jenis_ha': 'Fi\'il Jamid Tanzih'
    },
    "7. Fi'il Jamid__8": {
        'arti_ha': 'MADALLA DA ABIN DA',
        'desc_ha': 'Madalla da kyakkyawan abin da (Ni\'ma + Ma)',
        'jenis_ha': "Fi'il Jamid Madh Murakkab"
    }
}

# 4. 17 Harf Categories in Hausa
BENTUK_HARF_HA = {
    "1. Harf Nafyi": "1. Haruffan Hani / Ƙaryatawa (Harf Nafyi)",
    "2. Harf Tahqiq Taswif": "2. Haruffan Tabbatarwa da Nan Gaba (Tahqiq & Taswif)",
    "3. Harf Syarat": "3. Haruffan Sharaɗi (Harf Syarat)",
    "4. Harf Mashdariyah": "4. Haruffan Masdari (Harf Mashdariyah)",
    "5. Harf Zaidah": "5. Haruffan Ƙari don Ƙarfafawa (Harf Zaidah)",
    "6. Harf Istifham": "6. Harfin Tambaya (Harf Istifham)",
    "7. Harf Jawab": "7. Haruffan Amsawa (Harf Jawab)",
    "8. Harf Ibtida'": "8. Harfin Farawa (Harf Ibtida')",
    "9. Harf Tafshil": "9. Harfin Filla-filla / Bayani (Harf Tafshil)",
    "10. Harf Mufaja'ah": "10. Harfin Ba-zata (Harf Mufaja'ah)",
    "11. Harf Mufassirah": "11. Harfin Fassara (Harf Mufassirah)",
    "12. Harf Istiftahiyah": "12. Harfin Buɗewa da Jan Hankali (Harf Istiftahiyah)",
    "13. Harf Rada'": "13. Harfin Tsawatarwa (Harf Rada')",
    "14. Harf Ta'ajjub": "14. Harfin Mamaki (Harf Ta'ajjub)",
    "15. Harf Fariqah": "15. Harfin Bambancewa (Harf Fariqah)",
    "16. Harf Mauthi'ah": "16. Harfin Rantsuwa (Harf Mauthi'ah lil Qasam)",
    "17. Harf Mabany": "17. Haruffan Fawaatih as-Suwar (Harf Mabany)"
}

# 5. 52 Harf Words in Hausa
HAUSA_HARF_GRAMMAR = {
    # 1. Harf Nafyi
    "1. Harf Nafyi__1": {
        "arti_ha": "BA / BABU",
        "desc_ha": "Ba / babu (Harfin ƙaryatawa gaba ɗaya)",
        "jenis_ha": "Harf Nafyi (Laa)"
    },
    "1. Harf Nafyi__2": {
        "arti_ha": "BA / BABU",
        "desc_ha": "Ba / babu (Harfin ƙaryatawa na gama-gari)",
        "jenis_ha": "Harf Nafyi (Maa)"
    },
    "1. Harf Nafyi__3": {
        "arti_ha": "BA / BABU WANI",
        "desc_ha": "Babu wani ... face (Harfin ƙaryatawa mai zuwa tare da Illaa)",
        "jenis_ha": "Harf Nafyi (In)"
    },
    "1. Harf Nafyi__4": {
        "arti_ha": "ASHE BABU?",
        "desc_ha": "Ashe babu? (Tambayar da ke nufin ƙaryatawa)",
        "jenis_ha": "Harf Istifham bi Ma'na an-Nafyi"
    },
    "1. Harf Nafyi__5": {
        "arti_ha": "BA LOKACIN BA NE",
        "desc_ha": "Ba lokacin tserewa ba ne (Harfin ƙaryata lokaci)",
        "jenis_ha": "Harf Nafyi Mushabbah bi Laysa"
    },
    "1. Harf Nafyi__6": {
        "arti_ha": "BABU WANI ABU",
        "desc_ha": "Babu wani abu bayan gaskiya face ɓata",
        "jenis_ha": "Istifham bi Ma'na an-Nafyi"
    },

    # 2. Harf Tahqiq Taswif
    "2. Harf Tahqiq Taswif__7": {
        "arti_ha": "LALLAI / HAKIKA",
        "desc_ha": "Lallai / haƙiƙa ya tabbata (Harfin tabbatarwa)",
        "jenis_ha": "Harf Tahqiq"
    },
    "2. Harf Tahqiq Taswif__8": {
        "arti_ha": "NAN GABA ZA A",
        "desc_ha": "Nan gaba za a sani (Harfin nuna lokaci mai zuwa na nesa)",
        "jenis_ha": "Harf Taswif (Nan Gaba)"
    },

    # 3. Harf Syarat
    "3. Harf Syarat__9": {
        "arti_ha": "DA ACE / DA MA",
        "desc_ha": "Da ace (Harfin sharaɗi na abin da ba zai auku ba)",
        "jenis_ha": "Harf Syarat Ghair Jazim (Law)"
    },
    "3. Harf Syarat__10": {
        "arti_ha": "BA DON ... BA",
        "desc_ha": "Ba don falalar Allah ba (Harfin hanuwar wani abu saboda wanzuwar wani)",
        "jenis_ha": "Harf Imtina' li Wujud (Lawlaa)"
    },
    "3. Harf Syarat__11": {
        "arti_ha": "KODA KUWA / KODA ACE",
        "desc_ha": "Koda kuwa (Harfin sharaɗi na sauƙaƙawa)",
        "jenis_ha": "Harf Wasliyyah (Law)"
    },
    "3. Harf Syarat__12": {
        "arti_ha": "KODA ACE / IDAN",
        "desc_ha": "Idan kuma (In sharaɗi haɗe da Ma ta ƙarfafawa)",
        "jenis_ha": "Harf Syarat Murakkab (Immaa)"
    },
    "3. Harf Syarat__13": {
        "arti_ha": "KOMA MECE CE / DUK ABIN DA",
        "desc_ha": "Koma mece ce ka zo mana da ita (Kalmar sharaɗi mai faɗi)",
        "jenis_ha": "Isim Syarat (Mahmaa)"
    },

    # 4. Harf Mashdariyah
    "4. Harf Mashdariyah__14": {
        "arti_ha": "MATUƘAR / DUK LOKACIN DA",
        "desc_ha": "Matuƙar ina da rai (Harfin mayar da aiki masdari da nuna lokaci)",
        "jenis_ha": "Harf Masdariyyah Dharfiyyah"
    },
    "4. Harf Mashdariyah__15": {
        "arti_ha": "DON KADA / CEWA KADA",
        "desc_ha": "Don kada / cewa kada (An masdariyyah + Laa ta hani)",
        "jenis_ha": "Harf Masdariyyah + Nafyi"
    },
    "4. Harf Mashdariyah__16": {
        "arti_ha": "CEWA / DON",
        "desc_ha": "Cewa / domin (Harfin mayar da jumla masdari)",
        "jenis_ha": "Harf Masdariyyah (An)"
    },
    "4. Harf Mashdariyah__17": {
        "arti_ha": "DA ACE / BURIN",
        "desc_ha": "Yana son da ace ana raya shi (Law mai ma'anar An masdariyyah)",
        "jenis_ha": "Harf Masdariyyah (Law)"
    },
    "4. Harf Mashdariyah__18": {
        "arti_ha": "DON KADA KU",
        "desc_ha": "Don kada ku bauta wa kowa face Allah",
        "jenis_ha": "Harf Masdariyyah + Nahyi"
    },
    "4. Harf Mashdariyah__19": {
        "arti_ha": "CEWA LALLAI",
        "desc_ha": "Cewa lallai babu wani abin bauta face Shi",
        "jenis_ha": "Harf Masdari Mukhaffafah"
    },

    # 5. Harf Zaidah
    "5. Harf Zaidah__20": {
        "arti_ha": "KAMAR YADDA",
        "desc_ha": "Kamar yadda mutane suka yi imani (Kaf ta kamanceceniya + Ma)",
        "jenis_ha": "Kaf at-Tashbih + Ma"
    },
    "5. Harf Zaidah__21": {
        "arti_ha": "WANI / WATA",
        "desc_ha": "Wani misali na sauro (Ma ta ƙara zurfin bayani)",
        "jenis_ha": "Ma al-Ibhamiyyah (Zaidah)"
    },
    "5. Harf Zaidah__22": {
        "arti_ha": "LALLAI / TUNTUBE",
        "desc_ha": "Ina rantsuwa (Laa ta ƙarfafa rantsuwa)",
        "jenis_ha": "Laa Zaidah li at-Ta'kid"
    },
    "5. Harf Zaidah__23": {
        "arti_ha": "SABODA RAHAMAR",
        "desc_ha": "To saboda wata rahama daga Allah (Ba + Ma ta ƙarfafawa)",
        "jenis_ha": "Ba Harf Jar + Ma Zaidah"
    },
    "5. Harf Zaidah__24": {
        "arti_ha": "LOKACIN DA",
        "desc_ha": "A lokacin da mai bushara ya zo (An ta ƙari bayan Lamma)",
        "jenis_ha": "An Zaidah Ba'da Lamma"
    },

    # 6. Harf Istifham
    "6. Harf Istifham__25": {
        "arti_ha": "ASHE? / KO?",
        "desc_ha": "Ashe labari ya zo maka? (Harfin tambaya)",
        "jenis_ha": "Harf Istifham (Hal)"
    },

    # 7. Harf Jawab
    "7. Harf Jawab__26": {
        "arti_ha": "TO A WANNAN LOKACIN",
        "desc_ha": "To a wannan lokacin ba za su ba da ko kwayar zarra ba",
        "jenis_ha": "Harf Jawab wa Jaza' (Idhan)"
    },
    "7. Harf Jawab__27": {
        "arti_ha": "NA'AM! / TARE DA TABBACCI",
        "desc_ha": "Ƙwarai kuwa! Mun shaida (Amsa mai tabbatar da tambayar hani)",
        "jenis_ha": "Harf Jawab (Balaa)"
    },
    "7. Harf Jawab__28": {
        "arti_ha": "I / NA'AM",
        "desc_ha": "I, kuma lallai ku kuna daga makusanta",
        "jenis_ha": "Harf Jawab (Na'am)"
    },
    "7. Harf Jawab__29": {
        "arti_ha": "I! NA RANTSE DA UBANGIJINA",
        "desc_ha": "I! Na rantse da Ubangijina lallai shi gaskiya ne",
        "jenis_ha": "Harf Jawab li al-Qasam (Iiy)"
    },

    # 8. Harf Ibtida'
    "8. Harf Ibtida'__30": {
        "arti_ha": "HAR YA ZAMA",
        "desc_ha": "Har ya zama manzo da waɗanda suka yi imani suka ce",
        "jenis_ha": "Harf Ibtida' (Hattaa)"
    },

    # 9. Harf Tafshil
    "9. Harf Tafshil__31": {
        "arti_ha": "AMMA SHI / AMMA FA",
        "desc_ha": "Amma maraya kada ka wulaƙanta shi (Harfin rarrabe bayani)",
        "jenis_ha": "Harf Sharat wa Tafsil (Ammaa)"
    },

    # 10. Harf Mufaja'ah
    "10. Harf Mufaja'ah__32": {
        "arti_ha": "SAI GA SHI / FARAT ƊAYA",
        "desc_ha": "Sai ga shi farat ɗaya ta zama macijiya mai gudu",
        "jenis_ha": "Harf Mufaja'ah (Idhaa)"
    },

    # 11. Harf Mufassirah
    "11. Harf Mufassirah__33": {
        "arti_ha": "WATO / CEWA",
        "desc_ha": "Sai muka yi masa wahayi cewa ka ƙera jirgi (Harfin fassara)",
        "jenis_ha": "Harf Tafsir (An)"
    },

    # 12. Harf Istiftahiyah
    "12. Harf Istiftahiyah__34": {
        "arti_ha": "KU SAURARA! / KU SANI!",
        "desc_ha": "Ku saurara! Lallai waliyyan Allah babu tsoro a kansu",
        "jenis_ha": "Harf Istiftah wa Tanbih (Alaa)"
    },

    # 13. Harf Rada'
    "13. Harf Rada'__35": {
        "arti_ha": "A'A! / INA! SAM-SAM!",
        "desc_ha": "Ina! Sam-sam! Zai san gaskiya (Harfin tsawatarwa da hani mai tsanani)",
        "jenis_ha": "Harf Rada' wa Zajr (Kallaa)"
    },

    # 14. Harf Ta'ajjub
    "14. Harf Ta'ajjub__36": {
        "arti_ha": "KAI! ME YA BA SU HAƘURI!",
        "desc_ha": "Kai! Me ya ba su haƙurin zama a wuta! (Harfin nuna al\'ajabi da mamaki)",
        "jenis_ha": "Maa at-Ta'ajjubiyyah"
    },

    # 15. Harf Fariqah
    "15. Harf Fariqah__37": {
        "arti_ha": "LALLAI NE / HAƘIƘA",
        "desc_ha": "Lallai ne kowannensu za a cika masa sakamakon ayyukansa",
        "jenis_ha": "Laam al-Fariqah / In Mukhaffafah"
    },

    # 16. Harf Mauthi'ah
    "16. Harf Mauthi'ah__38": {
        "arti_ha": "LALLAI IDAN",
        "desc_ha": "Lallai idan kuka bi mutum irinku to kuna cikin asara",
        "jenis_ha": "Laam al-Mauthi'ah li al-Qasam"
    },

    # 17. Harf Mabany (Fawaatih as-Suwar)
    "17. Harf Mabany__39": {"arti_ha": "Haa Miim", "desc_ha": "Haruffan buɗe surah (Ha Meem)", "jenis_ha": "Harf Muqatta'ah"},
    "17. Harf Mabany__40": {"arti_ha": "Alif Laam Miim", "desc_ha": "Haruffan buɗe surah (Alif Laam Meem)", "jenis_ha": "Harf Muqatta'ah"},
    "17. Harf Mabany__41": {"arti_ha": "Alif Laam Raa", "desc_ha": "Haruffan buɗe surah (Alif Laam Raa)", "jenis_ha": "Harf Muqatta'ah"},
    "17. Harf Mabany__42": {"arti_ha": "Daa Siin Miim", "desc_ha": "Haruffan buɗe surah (Taa Seen Meem)", "jenis_ha": "Harf Muqatta'ah"},
    "17. Harf Mabany__43": {"arti_ha": "Alif Laam Miim Raa", "desc_ha": "Haruffan buɗe surah (Alif Laam Meem Raa)", "jenis_ha": "Harf Muqatta'ah"},
    "17. Harf Mabany__44": {"arti_ha": "Alif Laam Miim Saad", "desc_ha": "Haruffan buɗe surah (Alif Laam Meem Saad)", "jenis_ha": "Harf Muqatta'ah"},
    "17. Harf Mabany__45": {"arti_ha": "Saad", "desc_ha": "Harfin buɗe surah (Saad)", "jenis_ha": "Harf Muqatta'ah"},
    "17. Harf Mabany__46": {"arti_ha": "Daa Siin", "desc_ha": "Haruffan buɗe surah (Taa Seen)", "jenis_ha": "Harf Muqatta'ah"},
    "17. Harf Mabany__47": {"arti_ha": "Daa Haa", "desc_ha": "Haruffan buɗe surah (Ta-Ha)", "jenis_ha": "Harf Muqatta'ah"},
    "17. Harf Mabany__48": {"arti_ha": "'Ain Siin Qaaf", "desc_ha": "Haruffan buɗe surah ('Ayn Seen Qaaf)", "jenis_ha": "Harf Muqatta'ah"},
    "17. Harf Mabany__49": {"arti_ha": "Qaaf", "desc_ha": "Harfin buɗe surah (Qaaf)", "jenis_ha": "Harf Muqatta'ah"},
    "17. Harf Mabany__50": {"arti_ha": "Kaaf Haa Yaa 'Ain Saad", "desc_ha": "Haruffan buɗe surah (Kaaf Haa Yaa 'Ayn Saad)", "jenis_ha": "Harf Muqatta'ah"},
    "17. Harf Mabany__51": {"arti_ha": "Nuun", "desc_ha": "Harfin buɗe surah (Noon)", "jenis_ha": "Harf Muqatta'ah"},
    "17. Harf Mabany__52": {"arti_ha": "Yaa Siin", "desc_ha": "Haruffan buɗe surah (Ya-Sin)", "jenis_ha": "Harf Muqatta'ah"}
}


def enrich_dhamir_data():
    print("Enriching dhamir_data.json and dhamir_data.js with Hausa...")
    
    with open(os.path.join(BASE_DIR, 'ha_translations.json'), 'r', encoding='utf-8') as f:
        ha_translations = json.load(f)

    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = item.get('No kata', '')
        g_key = f"{b}__{nk}"
        
        # 1. BentukKataHA
        item['BentukKataHA'] = BENTUK_KATA_HA.get(b, b)
        
        # 2. SuratArtiHA
        surat_num = str(item.get('SURAT', ''))
        item['SuratArtiHA'] = HAUSA_SURAHS.get(surat_num, item.get('SuratArtiEN', ''))
        
        # 3. ArtiKataHA & Grammar HA
        g_info = HAUSA_GRAMMAR.get(g_key, {})
        item['ArtiKataHA'] = g_info.get('arti_ha', item.get('ArtiKataEN', item.get('Arti kata', '')))
        
        if 'Grammar' not in item:
            item['Grammar'] = {}
        if g_info.get('arti_ha'):
            item['Grammar']['arti_ha'] = g_info['arti_ha']
        if g_info.get('desc_ha'):
            item['Grammar']['desc_ha'] = g_info['desc_ha']
        if g_info.get('jenis_ha'):
            item['Grammar']['jenis_ha'] = g_info['jenis_ha']
            
        # 4. TeksArtiHA
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"
        teks_ha = ha_translations.get(v_key, item.get('TeksArtiEN', item.get('TeksArtiID', '')))
        item['TeksArtiHA'] = teks_ha

    # Write dhamir_data.json
    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Write dhamir_data.js
    js_content = f"/**\n * Dataset Dhamir & Isim Jamid Mabny Al-Qur'an Multibahasa (ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT, HA)\n */\nconst DHAMIR_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
    with open(os.path.join(BASE_DIR, 'dhamir_data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"Successfully enriched {len(data)} items in dhamir_data.json and dhamir_data.js with Hausa!")


def enrich_harf_data():
    print("Enriching harf_data.json and harf_data.js with Hausa...")
    
    with open(os.path.join(BASE_DIR, 'ha_translations.json'), 'r', encoding='utf-8') as f:
        ha_translations = json.load(f)

    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = item.get('No kata', '')
        g_key = f"{b}__{nk}"
        
        # 1. BentukKataHA
        item['BentukKataHA'] = BENTUK_HARF_HA.get(b, b)
        
        # 2. SuratArtiHA
        surat_num = str(item.get('SURAT', ''))
        item['SuratArtiHA'] = HAUSA_SURAHS.get(surat_num, item.get('SuratArtiEN', ''))
        
        # 3. ArtiKataHA & Grammar HA
        g_info = HAUSA_HARF_GRAMMAR.get(g_key, {})
        item['ArtiKataHA'] = g_info.get('arti_ha', item.get('ArtiKataEN', item.get('Arti kata', '')))
        
        if 'Grammar' not in item:
            item['Grammar'] = {}
        if g_info.get('arti_ha'):
            item['Grammar']['arti_ha'] = g_info['arti_ha']
        if g_info.get('desc_ha'):
            item['Grammar']['desc_ha'] = g_info['desc_ha']
        if g_info.get('jenis_ha'):
            item['Grammar']['jenis_ha'] = g_info['jenis_ha']
            
        # 4. TeksArtiHA
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"
        teks_ha = ha_translations.get(v_key, item.get('TeksArtiEN', item.get('TeksArtiID', '')))
        item['TeksArtiHA'] = teks_ha

    # Write harf_data.json
    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Write harf_data.js
    js_content = f"/**\n * Dataset Kamus Harf Ghair 'Amil Al-Qur'an Multibahasa (ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT, HA)\n */\nconst HARF_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
    with open(os.path.join(BASE_DIR, 'harf_data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"Successfully enriched {len(data)} items in harf_data.json and harf_data.js with Hausa!")


if __name__ == '__main__':
    enrich_dhamir_data()
    enrich_harf_data()
