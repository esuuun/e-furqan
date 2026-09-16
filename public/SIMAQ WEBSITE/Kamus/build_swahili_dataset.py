#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to build Swahili dataset and enrich dhamir_data.json, dhamir_data.js,
harf_data.json, and harf_data.js with complete Swahili translations.
"""

import os
import sys
import json

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. 114 Surahs Swahili Names / Meanings (Sheikh Ali Muhsin Al-Barwani)
SWAHILI_SURAHS = {
    "1": "Ufunguzi (Al-Faatiha)",
    "2": "Ng'ombe (Al-Baqarah)",
    "3": "Ukoo wa Imran (Ali 'Imran)",
    "4": "Wanawake (An-Nisaa)",
    "5": "Meza ya Chakula (Al-Maa'idah)",
    "6": "Wanyama wa Mifugo (Al-An'aam)",
    "7": "Mahali pa Juu (Al-A'raaf)",
    "8": "Ngawira za Vita (Al-Anfaal)",
    "9": "Toba (At-Tawbah)",
    "10": "Yunus (Yunus)",
    "11": "Hud (Hud)",
    "12": "Yusuf (Yusuf)",
    "13": "Ngurumo (Ar-Ra'd)",
    "14": "Ibrahim (Ibrahim)",
    "15": "Nchi ya Mawe (Al-Hijr)",
    "16": "Nyuki (An-Nahl)",
    "17": "Safari ya Usiku (Al-Israa)",
    "18": "Pango (Al-Kahf)",
    "19": "Maryam (Maryam)",
    "20": "Twaaha (Taa-Haa)",
    "21": "Manabii (Al-Anbiyaa)",
    "22": "Hija (Al-Hajj)",
    "23": "Waumini (Al-Mu'minoon)",
    "24": "Nuru (An-Noor)",
    "25": "Upambanuzi (Al-Furqaan)",
    "26": "Washairi (Ash-Shu'araa)",
    "27": "Sisimizi (An-Naml)",
    "28": "Kisa (Al-Qasas)",
    "29": "Buibui (Al-Ankaboot)",
    "30": "Warumi (Ar-Room)",
    "31": "Luqman (Luqman)",
    "32": "Kusujudu (As-Sajdah)",
    "33": "Makundi (Al-Ahzaab)",
    "34": "Saba (Saba)",
    "35": "Muumbaji (Faatir)",
    "36": "Yaa-Siin (Yaa-Seen)",
    "37": "Wenye Kupanga Safu (As-Saaffaat)",
    "38": "Saad (Saad)",
    "39": "Makundi ya Watu (Az-Zumar)",
    "40": "Mwenye Kusamehe (Ghafir)",
    "41": "Yaliyoelezwa Wazi (Fussilat)",
    "42": "Mashauriano (Ash-Shooraa)",
    "43": "Mapambo ya Dhahabu (Az-Zukhruf)",
    "44": "Moshi (Ad-Dukhaan)",
    "45": "Kupiga Magoti (Al-Jaathiyah)",
    "46": "Vilima vya Mchanga (Al-Ahqaaf)",
    "47": "Muhammad (Muhammad)",
    "48": "Ushindi (Al-Fat-h)",
    "49": "Vyumba (Al-Hujuraat)",
    "50": "Qaaf (Qaaf)",
    "51": "Wenye Kutawanya (Adh-Dhaariyaat)",
    "52": "Mlima wa Toor (At-Toor)",
    "53": "Nyota (An-Najm)",
    "54": "Mwezi (Al-Qamar)",
    "55": "Mwingi wa Rehema (Ar-Rahmaan)",
    "56": "Tukio Kubwa (Al-Waaqi'ah)",
    "57": "Chuma (Al-Hadeed)",
    "58": "Mwanamke Anayejadili (Al-Mujaadilah)",
    "59": "Kufukuzwa (Al-Hashr)",
    "60": "Mwanamke Anayejaribiwa (Al-Mumtahanah)",
    "61": "Safu (As-Saff)",
    "62": "Ijumaa (Al-Jumu'ah)",
    "63": "Wanaafiki (Al-Munaafiqoon)",
    "64": "Kudhihiri Hasara (At-Taghaabun)",
    "65": "Talaka (At-Talaaq)",
    "66": "Kuharamisha (At-Tahreem)",
    "67": "Ufalme (Al-Mulk)",
    "68": "Kalamu (Al-Qalam)",
    "69": "Ukweli Ulio Hakika (Al-Haaqqah)",
    "70": "Vipandio (Al-Ma'aarij)",
    "71": "Nuhu (Nooh)",
    "72": "Majini (Al-Jinn)",
    "73": "Aliyejifunika Nguo (Al-Muzzammil)",
    "74": "Aliyejivika Nguo (Al-Muddaththir)",
    "75": "Kiyama (Al-Qiyaamah)",
    "76": "Mwanadamu (Al-Insaan)",
    "77": "Waliotumwa (Al-Mursalaat)",
    "78": "Habari Kubwa (An-Naba')",
    "79": "Wenye Kung'oa kwa Nguvu (An-Naazi'aat)",
    "80": "Alikunja Uso ('Abasa)",
    "81": "Kukunjwa (At-Takweer)",
    "82": "Kupasuka (Al-Infitaar)",
    "83": "Wapunjaji (Al-Mutaffifeen)",
    "84": "Kupasuka kwa Mbingu (Al-Inshiqaaq)",
    "85": "Minara ya Nyota (Al-Burooj)",
    "86": "Kinachokuja Usiku (At-Taariq)",
    "87": "Aliye Juu Zaidi (Al-A'laa)",
    "88": "Kinachofunika (Al-Ghaashiyah)",
    "89": "Alfajiri (Al-Fajr)",
    "90": "Mji (Al-Balad)",
    "91": "Jua (Ash-Shams)",
    "92": "Usiku (Al-Layl)",
    "93": "Mchana (Ad-Duhaa)",
    "94": "Kukunjua Kifua (Ash-Sharh)",
    "95": "Tini (At-Teen)",
    "96": "Tone la Damu (Al-'Alaq)",
    "97": "Usiku wa Cheo (Al-Qadr)",
    "98": "Ushahidi ulio Wazi (Al-Bayyinah)",
    "99": "Mtetemeko wa Ardhi (Az-Zalzalah)",
    "100": "Farasi Wanaokimbia (Al-'Aadiyaat)",
    "101": "Msiba Unaogonga (Al-Qaari'ah)",
    "102": "Kushindana Wingi (At-Takaathur)",
    "103": "Zama (Al-'Asr)",
    "104": "Msengenyaji (Al-Humazah)",
    "105": "Tembo (Al-Feel)",
    "106": "Maquraishi (Quraysh)",
    "107": "Msaada (Al-Maa'oon)",
    "108": "Kheri Nyingi (Al-Kawthar)",
    "109": "Makamu wa Makafiri (Al-Kaafiroon)",
    "110": "Msaada / Ushindi (An-Nasr)",
    "111": "Kamba ya Makumbi (Al-Masad)",
    "112": "Kusafisha Imani (Al-Ikhlaas)",
    "113": "Mapambazuko (Al-Falaq)",
    "114": "Watu (An-Naas)"
}

# 2. 7 Categories (Bentuk Kata) in Swahili
BENTUK_KATA_SW = {
    '1. Dhamir': '1. Viwakilishi vya Nafsi (Dhamir - Pronouns)',
    '2. Mawshul': '2. Majina ya Kuunganisha (Mawshul - Relative Pronouns)',
    '3. Istifham': '3. Maneno ya Kuulizia (Istifham - Interrogatives)',
    '4. Syarath': '4. Maneno ya Sharti (Syarath - Conditionals)',
    '5. Isyarah': '5. Majina ya Kuonyeshea (Isyarah - Demonstratives)',
    "6. Isim Fi'il": "6. Majina ya Vitendo (Isim Fi'il - Verbal Nouns)",
    "7. Fi'il Jamid": "7. Vitendo Visivyobadilika (Fi'il Jamid - Inflexible Verbs)"
}

# 3. 76 Jamid Mabny Grammatical Metadata in Swahili
SWAHILI_GRAMMAR = {
    # 1. Dhamir
    '1. Dhamir__1a': {
        'arti_sw': 'YEYE (MWANAUME)',
        'desc_sw': 'Yeye (Nafsi ya 3 umoja mwanamume, kiwakilishi huru)',
        'jenis_sw': 'Munfashil (Kiwakilishi Huru)'
    },
    '1. Dhamir__1b': {
        'arti_sw': '..YAKE / ..YE',
        'desc_sw': '...-yake / yeye (Nafsi ya 3 umoja mwanamume, kiwakilishi tegemezi)',
        'jenis_sw': 'Muttashil (Kiwakilishi Tegemezi)'
    },
    '1. Dhamir__1c': {
        'arti_sw': 'YEYE PEKEE',
        'desc_sw': 'Yeye pekee / Kwake yeye tu (Kiwakilishi huru cha mtendwa, umoja mwanamume)',
        'jenis_sw': 'Munfashil Manshub (Mtendwa Huru)'
    },
    '1. Dhamir__2a': {
        'arti_sw': 'WAO WAWILI',
        'desc_sw': 'Wao wawili (Nafsi ya 3 uwili wanaume/wanawake, kiwakilishi huru)',
        'jenis_sw': 'Munfashil (Kiwakilishi Huru)'
    },
    '1. Dhamir__2b': {
        'arti_sw': '..YAO WAWILI',
        'desc_sw': '...-yao wawili (Nafsi ya 3 uwili wanaume/wanawake, kiwakilishi tegemezi)',
        'jenis_sw': 'Muttashil (Kiwakilishi Tegemezi)'
    },
    '1. Dhamir__3a': {
        'arti_sw': 'WAO (WANAUME)',
        'desc_sw': 'Wao (Nafsi ya 3 wingi wanaume, kiwakilishi huru)',
        'jenis_sw': 'Munfashil (Kiwakilishi Huru)'
    },
    '1. Dhamir__3b': {
        'arti_sw': '..YAO / ..WAO',
        'desc_sw': '...-yao / wao (Nafsi ya 3 wingi wanaume, kiwakilishi tegemezi)',
        'jenis_sw': 'Muttashil (Kiwakilishi Tegemezi)'
    },
    '1. Dhamir__3c': {
        'arti_sw': 'WAO PEKEE',
        'desc_sw': 'Wao pekee / Kwao wao tu (Kiwakilishi huru cha mtendwa, wingi wanaume)',
        'jenis_sw': 'Munfashil Manshub (Mtendwa Huru)'
    },
    '1. Dhamir__4a': {
        'arti_sw': 'YEYE (MWANAMKE)',
        'desc_sw': 'Yeye (Nafsi ya 3 umoja mwanamke, kiwakilishi huru)',
        'jenis_sw': 'Munfashil (Kiwakilishi Huru)'
    },
    '1. Dhamir__4b': {
        'arti_sw': '..YAKE / ..YE (MWANAMKE)',
        'desc_sw': '...-yake / yeye (Nafsi ya 3 umoja mwanamke, kiwakilishi tegemezi)',
        'jenis_sw': 'Muttashil (Kiwakilishi Tegemezi)'
    },
    '1. Dhamir__5a': {
        'arti_sw': 'WAO (WANAWAKE)',
        'desc_sw': 'Wao (Nafsi ya 3 wingi wanawake, kiwakilishi huru)',
        'jenis_sw': 'Munfashil (Kiwakilishi Huru)'
    },
    '1. Dhamir__5b': {
        'arti_sw': '..YAO (WANAWAKE)',
        'desc_sw': '...-yao / wao (Nafsi ya 3 wingi wanawake, kiwakilishi tegemezi)',
        'jenis_sw': 'Muttashil (Kiwakilishi Tegemezi)'
    },
    '1. Dhamir__6a': {
        'arti_sw': 'WEWE (MWANAUME)',
        'desc_sw': 'Wewe (Nafsi ya 2 umoja mwanamume, kiwakilishi huru)',
        'jenis_sw': 'Munfashil (Kiwakilishi Huru)'
    },
    '1. Dhamir__6b': {
        'arti_sw': '..YAKO / ..WEWE',
        'desc_sw': '...-yako / wewe (Nafsi ya 2 umoja mwanamume, kiwakilishi tegemezi)',
        'jenis_sw': 'Muttashil (Kiwakilishi Tegemezi)'
    },
    '1. Dhamir__6c': {
        'arti_sw': 'WEWE PEKEE',
        'desc_sw': 'Wewe pekee / Kwako wewe tu (Kiwakilishi huru cha mtendwa, umoja mwanamume)',
        'jenis_sw': 'Munfashil Manshub (Mtendwa Huru)'
    },
    '1. Dhamir__7a': {
        'arti_sw': 'NYINYI WAWILI',
        'desc_sw': 'Nyinyi wawili (Nafsi ya 2 uwili wanaume/wanawake, kiwakilishi huru)',
        'jenis_sw': 'Munfashil (Kiwakilishi Huru)'
    },
    '1. Dhamir__7b': {
        'arti_sw': '..YENU WAWILI',
        'desc_sw': '...-yenu wawili (Nafsi ya 2 uwili wanaume/wanawake, kiwakilishi tegemezi)',
        'jenis_sw': 'Muttashil (Kiwakilishi Tegemezi)'
    },
    '1. Dhamir__8a': {
        'arti_sw': 'NYINYI (WANAUME)',
        'desc_sw': 'Nyinyi (Nafsi ya 2 wingi wanaume, kiwakilishi huru)',
        'jenis_sw': 'Munfashil (Kiwakilishi Huru)'
    },
    '1. Dhamir__8b': {
        'arti_sw': '..YENU / ..NYINYI',
        'desc_sw': '...-yenu / nyinyi (Nafsi ya 2 wingi wanaume, kiwakilishi tegemezi)',
        'jenis_sw': 'Muttashil (Kiwakilishi Tegemezi)'
    },
    '1. Dhamir__8c': {
        'arti_sw': 'NYINYI PEKEE',
        'desc_sw': 'Nyinyi pekee / Kwenu nyinyi tu (Kiwakilishi huru cha mtendwa, wingi wanaume)',
        'jenis_sw': 'Munfashil Manshub (Mtendwa Huru)'
    },
    '1. Dhamir__9b': {
        'arti_sw': '..YAKO / ..WEWE (MWANAMKE)',
        'desc_sw': '...-yako / wewe (Nafsi ya 2 umoja mwanamke, kiwakilishi tegemezi)',
        'jenis_sw': 'Muttashil (Kiwakilishi Tegemezi)'
    },
    '1. Dhamir__11a': {
        'arti_sw': 'MIMI',
        'desc_sw': 'Mimi (Nafsi ya 1 msemaji mmoja, mwanamume au mwanamke)',
        'jenis_sw': 'Munfashil (Kiwakilishi Huru)'
    },
    '1. Dhamir__11b': {
        'arti_sw': '..YANGU / ..MIMI',
        'desc_sw': '...-yangu / mimi (Nafsi ya 1 msemaji mmoja, kiwakilishi tegemezi)',
        'jenis_sw': 'Muttashil (Kiwakilishi Tegemezi)'
    },
    '1. Dhamir__11c': {
        'arti_sw': 'MIMI PEKEE',
        'desc_sw': 'Mimi pekee / Kwangu mimi tu (Kiwakilishi huru cha mtendwa, msemaji mmoja)',
        'jenis_sw': 'Munfashil Manshub (Mtendwa Huru)'
    },
    '1. Dhamir__12a': {
        'arti_sw': 'SISI',
        'desc_sw': 'Sisi (Nafsi ya 1 wingi wasemaji, wanaume au wanawake)',
        'jenis_sw': 'Munfashil (Kiwakilishi Huru)'
    },
    '1. Dhamir__12b': {
        'arti_sw': '..YETU / ..SISI',
        'desc_sw': '...-yetu / sisi (Nafsi ya 1 wingi wasemaji, kiwakilishi tegemezi)',
        'jenis_sw': 'Muttashil (Kiwakilishi Tegemezi)'
    },
    '1. Dhamir__12c': {
        'arti_sw': 'SISI PEKEE',
        'desc_sw': 'Sisi pekee / Kwetu sisi tu (Kiwakilishi huru cha mtendwa, wingi wasemaji)',
        'jenis_sw': 'Munfashil Manshub (Mtendwa Huru)'
    },

    # 2. Mawshul
    '2. Mawshul__1': {
        'arti_sw': 'KILE AMBACHO / KILICHO',
        'desc_sw': 'Kile ambacho / kile (Jina la kuunganisha kwa visivyo na akili)',
        'jenis_sw': "Isim Mawshul (Ghairu 'Aqil)"
    },
    '2. Mawshul__2': {
        'arti_sw': 'WALE AMBAO / WALIO',
        'desc_sw': 'Wale ambao / walio (Jina la kuunganisha kwa wingi watu wenye akili)',
        'jenis_sw': "Isim Mawshul Jam'i (Watu)"
    },
    '2. Mawshul__3': {
        'arti_sw': 'YULE AMBAYE / YEYOTE',
        'desc_sw': 'Yule ambaye / yeyote (Jina la kuunganisha kwa wenye akili)',
        'jenis_sw': "Isim Mawshul ('Aqil)"
    },
    '2. Mawshul__4': {
        'arti_sw': 'YULE AMBAYE (MWANAUME)',
        'desc_sw': 'Yule ambaye (Jina la kuunganisha umoja mwanamume)',
        'jenis_sw': 'Isim Mawshul Mufrad (Mwanamume)'
    },
    '2. Mawshul__5': {
        'arti_sw': 'IPI / YEYOTE KATI YAO',
        'desc_sw': 'Ipi / yeyote kati yao (Jina la kuunganisha linalobadilika irabu)',
        'jenis_sw': "Isim Mawshul Mu'rab"
    },
    '2. Mawshul__6': {
        'arti_sw': 'YULE AMBAYE (MWANAMKE)',
        'desc_sw': 'Yule ambaye / kile (Jina la kuunganisha umoja mwanamke au wingi usio na akili)',
        'jenis_sw': 'Isim Mawshul Mufrad (Mwanamke)'
    },
    '2. Mawshul__7': {
        'arti_sw': 'WALE WANAWAKE AMBAO',
        'desc_sw': 'Wale wanawake ambao (Jina la kuunganisha wingi wanawake - Al-Laa\'ii)',
        'jenis_sw': "Isim Mawshul Jam'i (Wanawake)"
    },
    '2. Mawshul__8': {
        'arti_sw': 'WALE WANAWAKE AMBAO (AL-LAATI)',
        'desc_sw': 'Wale wanawake ambao (Jina la kuunganisha wingi wanawake - Al-Laatee)',
        'jenis_sw': "Isim Mawshul Jam'i (Wanawake)"
    },
    '2. Mawshul__9': {
        'arti_sw': 'WAO WAWILI AMBAO',
        'desc_sw': 'Wao wawili ambao (Jina la kuunganisha uwili wanaume)',
        'jenis_sw': 'Isim Mawshul Muthanna (Uwili)'
    },
    '2. Mawshul__10': {
        'arti_sw': 'IPI KATI YAO (MWANAMKE)',
        'desc_sw': 'Yupi kati yao (Jina la kuunganisha mwanamke)',
        'jenis_sw': "Isim Mawshul Mu'annath"
    },

    # 3. Istifham
    '3. Istifham__1': {
        'arti_sw': 'NINI? / NI NINI?',
        'desc_sw': 'Ni nini? (Neno la kuulizia kwa visivyo na akili)',
        'jenis_sw': "Isim Istifham (Ghairu 'Aqil)"
    },
    '3. Istifham__2': {
        'arti_sw': 'VIPI? / KWA JINSI GANI?',
        'desc_sw': 'Vipi? / kwa vipi? (Neno la kuulizia hali au namna)',
        'jenis_sw': 'Isim Istifham (Hali / Hal)'
    },
    '3. Istifham__3': {
        'arti_sw': 'NANI? / NI NANI?',
        'desc_sw': 'Nani? (Neno la kuulizia kwa wenye akili)',
        'jenis_sw': "Isim Istifham ('Aqil)"
    },
    '3. Istifham__4': {
        'arti_sw': 'YUPI? / IPI?',
        'desc_sw': 'Yupi? / ipi? (Neno la kuulizia chaguo)',
        'jenis_sw': 'Isim Istifham (Chaguo)'
    },
    '3. Istifham__5': {
        'arti_sw': 'WAPI? / VIPI?',
        'desc_sw': 'Kutoka wapi? / vipi? (Neno la kuulizia mahali au hali)',
        'jenis_sw': 'Isim Istifham (Mahali / Hali)'
    },
    '3. Istifham__6': {
        'arti_sw': 'NI NINI HICHO AMBACHO?',
        'desc_sw': 'Ni nini hicho ambacho? (Swali lenye msisitizo kwa kuunganisha Ma na Dha)',
        'jenis_sw': 'Isim Istifham Murakkab'
    },
    '3. Istifham__7': {
        'arti_sw': 'NGAPI? / MUDA GANI?',
        'desc_sw': 'Ngapi? / muda gani? (Neno la kuulizia idadi au muda)',
        'jenis_sw': "Isim Istifham (Idadi / 'Adad)"
    },
    '3. Istifham__8': {
        'arti_sw': 'KWA NINI? / KWA SABABU GANI?',
        'desc_sw': 'Kwa nini? (Swali la sababu, Li + Ma)',
        'jenis_sw': 'Harf Jar + Istifham'
    },
    '3. Istifham__9': {
        'arti_sw': 'WAPI? / MAHALI GANI?',
        'desc_sw': 'Wapi? (Neno la kuulizia mahali)',
        'jenis_sw': 'Isim Istifham (Mahali / Makan)'
    },
    '3. Istifham__10': {
        'arti_sw': 'LINI? / WAKATI GANI?',
        'desc_sw': 'Lini? (Neno la kuulizia wakati ujao na siku ya Kiyama)',
        'jenis_sw': 'Isim Istifham (Wakati / Ayyana)'
    },

    # 4. Syarath
    '4. Syarath__1': {
        'arti_sw': 'YEYOTE ATAKAYE / MWENYE',
        'desc_sw': 'Yeyote atakaye (Neno la sharti linalofanya vitendo viwili jazm)',
        'jenis_sw': "Isim Syarat ('Aqil)"
    },
    '4. Syarath__2': {
        'arti_sw': 'CHOCHOTE MTAKACHO',
        'desc_sw': 'Chochote mtakachofanya (Neno la sharti kwa visivyo na akili)',
        'jenis_sw': "Isim Syarat (Ghairu 'Aqil)"
    },
    '4. Syarath__3': {
        'arti_sw': 'KILA MARA / WAKATI WOWOTE',
        'desc_sw': 'Kila mara / wakati wowote (Kullama ya sharti la wakati)',
        'jenis_sw': 'Dharf Sharat Zamani'
    },
    '4. Syarath__4': {
        'arti_sw': 'CHOCHOTE / YEYOTE',
        'desc_sw': 'Chochote / yeyote kati yao (Neno la sharti linalonyumbulika)',
        'jenis_sw': "Isim Syarat Mu'rab"
    },
    '4. Syarath__5': {
        'arti_sw': 'CHOCHOTE KILE (KWA MSISITIZO)',
        'desc_sw': 'Chochote kile (Sharti pamoja na msisitizo wa Ma)',
        'jenis_sw': 'Isim Syarat Murakkab'
    },

    # 5. Isyarah
    '5. Isyarah__1': {
        'arti_sw': 'HUU / HIKI / YULE (MWANAUME)',
        'desc_sw': 'Huyu / yule / hiki (Jina la kuonyeshea karibu au mbali, umoja mwanamume)',
        'jenis_sw': 'Isim Isyarah (Umoja Mwanamume)'
    },
    '5. Isyarah__2': {
        'arti_sw': 'HAWA / WALE',
        'desc_sw': 'Hawa / wale (Jina la kuonyeshea wingi watu, wanaume na wanawake)',
        'jenis_sw': "Isim Isyarah (Wingi / Jam'i)"
    },
    '5. Isyarah__3': {
        'arti_sw': 'HII / HUYU (MWANAMKE)',
        'desc_sw': 'Hii / huyu (Jina la kuonyeshea karibu, umoja mwanamke au wingi usio na akili)',
        'jenis_sw': 'Isim Isyarah (Umoja Mwanamke)'
    },
    '5. Isyarah__4': {
        'arti_sw': 'ILE / YULE (MWANAMKE)',
        'desc_sw': 'Ile / yule (Jina la kuonyeshea mbali, mwanamke)',
        'jenis_sw': "Isim Isyarah Ba'id (Mbali)"
    },
    '5. Isyarah__5': {
        'arti_sw': 'HAPA / MAHALI HAPA',
        'desc_sw': 'Hapa (Jina la kuonyeshea mahali pa karibu)',
        'jenis_sw': 'Isim Isyarah Makan (Karibu)'
    },
    '5. Isyarah__6': {
        'arti_sw': 'PALE / MAHALI PALE',
        'desc_sw': 'Pale / kule (Jina la kuonyeshea mahali pa mbali)',
        'jenis_sw': "Isim Isyarah Makan (Mbali / Ba'id)"
    },
    '5. Isyarah__7': {
        'arti_sw': 'HAWA WAWILI (WANAUME)',
        'desc_sw': 'Hawa wawili (Jina la kuonyeshea uwili wanaume)',
        'jenis_sw': 'Isim Isyarah Muthanna (Uwili Mwanamume)'
    },
    '5. Isyarah__8': {
        'arti_sw': 'HAWA WAWILI (WANAWAKE)',
        'desc_sw': 'Hawa wawili (Jina la kuonyeshea uwili wanawake)',
        'jenis_sw': 'Isim Isyarah Muthanna (Uwili Mwanamke)'
    },

    # 6. Isim Fi'il
    "6. Isim Fi'il__1": {
        'arti_sw': 'UTUKUFU NI WA ALLAH!',
        'desc_sw': 'Utukufu ni wa Allah (Tasbihi na kutukuza)',
        'jenis_sw': 'Isim Masdar / Tasbih'
    },
    "6. Isim Fi'il__2": {
        'arti_sw': 'LEETENI / TOENI!',
        'desc_sw': 'Leeteni / toeni ushahidi wenu (Jina la kitendo cha amri = Haatoo)',
        'jenis_sw': "Isim Fi'il Amr"
    },
    "6. Isim Fi'il__3": {
        'arti_sw': 'AH! / KERO!',
        'desc_sw': 'Ah! / ebo! (Jina la kitendo cha kuonyesha kuchukizwa = Uff)',
        'jenis_sw': "Isim Fi'il Mudhari'"
    },
    "6. Isim Fi'il__4": {
        'arti_sw': 'MUNGU APISHE MBALI!',
        'desc_sw': 'Najikinga kwa Allah (Kujilinda na maasi)',
        'jenis_sw': 'Isim Masdar Manshub'
    },
    "6. Isim Fi'il__5": {
        'arti_sw': 'NJOONI HAPA!',
        'desc_sw': 'Njooni hapa / songeeni karibu (Jina la kitendo cha amri = Halumma)',
        'jenis_sw': "Isim Fi'il Amr"
    },
    "6. Isim Fi'il__6": {
        'arti_sw': 'WAPI NA WAPI! / MBALI MNO!',
        'desc_sw': 'Wapi na wapi! Ni mbali mno kutokea (Jina la kitendo cha wakati uliopita = Hayhata)',
        'jenis_sw': "Isim Fi'il Madhi"
    },
    "6. Isim Fi'il__7": {
        'arti_sw': 'HAYA SOMENI!',
        'desc_sw': 'Haya someni kitabu changu (Jina la kitendo cha amri = Haa\'um)',
        'jenis_sw': "Isim Fi'il Amr"
    },
    "6. Isim Fi'il__8": {
        'arti_sw': 'NJOO! / KARIBIA!',
        'desc_sw': 'Njoo kwangu! / karibia hapa (Jina la kitendo cha amri = Hayta)',
        'jenis_sw': "Isim Fi'il Amr"
    },

    # 7. Fi'il Jamid
    "7. Fi'il Jamid__1": {
        'arti_sw': 'SIYO / HAKUNA',
        'desc_sw': 'Siyo / hakuna (Kitendo kisichobadilika cha kukanusha kutoka kundi la Kana)',
        'jenis_sw': "Fi'il Jamid Naqis (Nafyi)"
    },
    "7. Fi'il Jamid__2": {
        'arti_sw': 'ENDA IKAWA / LABDA',
        'desc_sw': 'Enda ikawa / huenda (Kitendo kisichobadilika cha matumaini = \'Asaa)',
        'jenis_sw': "Fi'il Jamid Raja' (Matumaini)"
    },
    "7. Fi'il Jamid__3": {
        'arti_sw': 'KIZURI SANA / BORA MNO',
        'desc_sw': 'Kizuri sana / ni bora mno (Kitendo kisichobadilika cha kusifu = Ni\'ma)',
        'jenis_sw': "Fi'il Jamid Madh (Sifa)"
    },
    "7. Fi'il Jamid__4": {
        'arti_sw': 'KIBAYA SANA / OVYO MNO',
        'desc_sw': 'Kibaya sana / ni ovu mno (Kitendo kisichobadilika cha kukemea = Bi\'sa)',
        'jenis_sw': "Fi'il Jamid Dzamm (Kemeo)"
    },
    "7. Fi'il Jamid__5": {
        'arti_sw': 'KIBAYA MNO WALICHONUNUA',
        'desc_sw': 'Kibaya mno walichonunua kwa nafsi zao (Bi\'sa + Ma)',
        'jenis_sw': "Fi'il Jamid Dzamm Murakkab"
    },
    "7. Fi'il Jamid__6": {
        'arti_sw': 'WAKAANZA / WAKAINGIA',
        'desc_sw': 'Wakaanza kujifunika majani (Kitendo cha kuanza jambo = Tafiqa)',
        'jenis_sw': "Fi'il Shuru' (Kuanza)"
    },
    "7. Fi'il Jamid__7": {
        'arti_sw': 'MUNGU APISHE MBALI KABISA',
        'desc_sw': 'Kutakasa Allah na kila upungufu (Haashaa lillah)',
        'jenis_sw': "Fi'il Jamid Tanzih"
    },
    "7. Fi'il Jamid__8": {
        'arti_sw': 'KIZURI SANA KILE',
        'desc_sw': 'Kizuri sana kile anachokuusieni (Ni\'ma + Ma)',
        'jenis_sw': "Fi'il Jamid Madh Murakkab"
    }
}

# 4. 17 Harf Categories in Swahili
BENTUK_HARF_SW = {
    "1. Harf Nafyi": "1. Herufi za Kukanusha (Harf Nafyi)",
    "2. Harf Tahqiq Taswif": "2. Herufi za Uhakika na Wakati Ujao (Tahqiq & Taswif)",
    "3. Harf Syarat": "3. Herufi za Sharti (Harf Syarat)",
    "4. Harf Mashdariyah": "4. Herufi za Kitenzi Jina (Harf Mashdariyah)",
    "5. Harf Zaidah": "5. Herufi za Ziada kwa Msisitizo (Harf Zaidah)",
    "6. Harf Istifham": "6. Herufi ya Kuulizia (Harf Istifham)",
    "7. Harf Jawab": "7. Herufi za Majibu (Harf Jawab)",
    "8. Harf Ibtida'": "8. Herufi ya Kuanzia / Msisitizo (Harf Ibtida')",
    "9. Harf Tafshil": "9. Herufi ya Ufafanuzi / Mgawanyo (Harf Tafshil)",
    "10. Harf Mufaja'ah": "10. Herufi ya Ghafla (Harf Mufaja'ah)",
    "11. Harf Mufassirah": "11. Herufi ya Ufafanuzi (Harf Mufassirah)",
    "12. Harf Istiftahiyah": "12. Herufi ya Kufungulia na Kuzindua (Harf Istiftahiyah)",
    "13. Harf Rada'": "13. Herufi ya Kuzuia na Kukaripia (Harf Rada')",
    "14. Harf Ta'ajjub": "14. Herufi ya Mshangao (Harf Ta'ajjub)",
    "15. Harf Fariqah": "15. Herufi ya Kutofautisha (Harf Fariqah)",
    "16. Harf Mauthi'ah": "16. Herufi ya Utangulizi wa Kiapo (Harf Mauthi'ah lil Qasam)",
    "17. Harf Mabany": "17. Herufi za Kufungulia Sura (Fawaatih as-Suwar)"
}

# 5. 52 Harf Words in Swahili
SWAHILI_HARF_GRAMMAR = {
    # 1. Harf Nafyi
    "1. Harf Nafyi__1": {
        "arti_sw": "SI / HAPANA / HAWANA",
        "desc_sw": "Si / hapana (Herufi ya kukanusha kwa ujumla)",
        "jenis_sw": "Harf Nafyi (Laa)"
    },
    "1. Harf Nafyi__2": {
        "arti_sw": "SI / HAPANA / SIYO",
        "desc_sw": "Si / siyo (Herufi ya kukanusha inayotumika kawaida)",
        "jenis_sw": "Harf Nafyi (Maa)"
    },
    "1. Harf Nafyi__3": {
        "arti_sw": "SI CHOCHOTE ILA",
        "desc_sw": "Si chochote isipokuwa (Herufi ya kukanusha inayoambatana na Illaa)",
        "jenis_sw": "Harf Nafyi (In)"
    },
    "1. Harf Nafyi__4": {
        "arti_sw": "JE, SIYE?",
        "desc_sw": "Je, siye? (Swali lenye maana ya kukanusha / kuthibitisha)",
        "jenis_sw": "Harf Istifham bi Ma'na an-Nafyi"
    },
    "1. Harf Nafyi__5": {
        "arti_sw": "WALA SI WAKATI WA",
        "desc_sw": "Wala si wakati wa kukimbia tena (Herufi ya kukanusha wakati)",
        "jenis_sw": "Harf Nafyi Mushabbah bi Laysa"
    },
    "1. Harf Nafyi__6": {
        "arti_sw": "HAKUNA JINGINE ILA",
        "desc_sw": "Hakuna baada ya haki isipokuwa upotofu",
        "jenis_sw": "Istifham bi Ma'na an-Nafyi"
    },

    # 2. Harf Tahqiq Taswif
    "2. Harf Tahqiq Taswif__7": {
        "arti_sw": "HAKIKA / BILA SHAKA",
        "desc_sw": "Hakika imekwisha dhihiri (Herufi ya kuthibitisha na kuweka wazi)",
        "jenis_sw": "Harf Tahqiq (Hakika)"
    },
    "2. Harf Tahqiq Taswif__8": {
        "arti_sw": "BAADAYE MTAKUJA JUA",
        "desc_sw": "Baadaye mtakuja jua (Herufi ya kuonyesha wakati ujao wa mbali)",
        "jenis_sw": "Harf Taswif (Wakati Ujao)"
    },

    # 3. Harf Syarat
    "3. Harf Syarat__9": {
        "arti_sw": "INGEKUWA / LAITI",
        "desc_sw": "Laiti ingekuwa (Herufi ya sharti ya jambo lisilowezekana)",
        "jenis_sw": "Harf Syarat Ghair Jazim (Law)"
    },
    "3. Harf Syarat__10": {
        "arti_sw": "INGELIKUWA SI",
        "desc_sw": "Ingelikuwa si fadhila za Allah (Kukosekana kwa jambo kwa sababu ya kuwepo jingine)",
        "jenis_sw": "Harf Imtina' li Wujud (Lawlaa)"
    },
    "3. Harf Syarat__11": {
        "arti_sw": "HATA KAMA / IKIWA",
        "desc_sw": "Hata kama (Herufi ya sharti ya kulinganisha)",
        "jenis_sw": "Harf Wasliyyah (Law)"
    },
    "3. Harf Syarat__12": {
        "arti_sw": "AMA IKIWA / IKITOKEA",
        "desc_sw": "Ikitokea (Sharti In ikiwa na Ma ya msisitizo)",
        "jenis_sw": "Harf Syarat Murakkab (Immaa)"
    },
    "3. Harf Syarat__13": {
        "arti_sw": "CHOCHOTE KILE",
        "desc_sw": "Chochote kile utakachotuletea (Neno la sharti pana)",
        "jenis_sw": "Isim Syarat (Mahmaa)"
    },

    # 4. Harf Mashdariyah
    "4. Harf Mashdariyah__14": {
        "arti_sw": "MAADAMU / MUDA WOTE",
        "desc_sw": "Maadamu niko hai (Herufi ya kubadili tendo kuwa jina na kueleza muda)",
        "jenis_sw": "Harf Masdariyyah Dharfiyyah"
    },
    "4. Harf Mashdariyah__15": {
        "arti_sw": "ILI WASIJE / ILI KUTOKUWA",
        "desc_sw": "Ili wasije (An ya masdari + Laa ya kukanusha)",
        "jenis_sw": "Harf Masdariyyah + Nafyi"
    },
    "4. Harf Mashdariyah__16": {
        "arti_sw": "KWAMBA / ILI",
        "desc_sw": "Kwamba / ili (Herufi ya kubadili jumla kuwa tendo jina)",
        "jenis_sw": "Harf Masdariyyah (An)"
    },
    "4. Harf Mashdariyah__17": {
        "arti_sw": "KUTAMANI / LAITI",
        "desc_sw": "Anatamani laiti angeishi miaka elfu (Law yenye maana ya An)",
        "jenis_sw": "Harf Masdariyyah (Law)"
    },
    "4. Harf Mashdariyah__18": {
        "arti_sw": "MSIJE MKAMWABUDU YEYOTE",
        "desc_sw": "Kwamba msimwabudu yeyote ila Allah pekee",
        "jenis_sw": "Harf Masdariyyah + Nahyi"
    },
    "4. Harf Mashdariyah__19": {
        "arti_sw": "KWAMBA HAKIKA",
        "desc_sw": "Kwamba hakika hakuna Mungu ila Yeye pekee",
        "jenis_sw": "Harf Masdari Mukhaffafah"
    },

    # 5. Harf Zaidah
    "5. Harf Zaidah__20": {
        "arti_sw": "KAMA VILE",
        "desc_sw": "Kama vile watu walivyoamini (Kaf ya mfanano + Ma)",
        "jenis_sw": "Kaf at-Tashbih + Ma"
    },
    "5. Harf Zaidah__21": {
        "arti_sw": "MFANO WOWOTE",
        "desc_sw": "Mfano wowote wa mbu (Ma ya kuongeza msisitizo)",
        "jenis_sw": "Ma al-Ibhamiyyah (Zaidah)"
    },
    "5. Harf Zaidah__22": {
        "arti_sw": "HAPANA! NINAAPA",
        "desc_sw": "Ninaapa (Laa ya kuweka msisitizo kwenye kiapo)",
        "jenis_sw": "Laa Zaidah li at-Ta'kid"
    },
    "5. Harf Zaidah__23": {
        "arti_sw": "KWA REHEMA",
        "desc_sw": "Kwa rehema itokayo kwa Allah (Ba + Ma ya msisitizo)",
        "jenis_sw": "Ba Harf Jar + Ma Zaidah"
    },
    "5. Harf Zaidah__24": {
        "arti_sw": "ALIPOKUJA",
        "desc_sw": "Mbashiri alipokuja (An ya ziada baada ya Lamma)",
        "jenis_sw": "An Zaidah Ba'da Lamma"
    },

    # 6. Harf Istifham
    "6. Harf Istifham__25": {
        "arti_sw": "JE? / HIVI?",
        "desc_sw": "Je, imekufikia habari? (Herufi ya kuulizia)",
        "jenis_sw": "Harf Istifham (Hal)"
    },

    # 7. Harf Jawab
    "7. Harf Jawab__26": {
        "arti_sw": "BASI HAPO",
        "desc_sw": "Basi hapo wasingetoa hata tundu ya kokwa ya tende",
        "jenis_sw": "Harf Jawab wa Jaza' (Idhan)"
    },
    "7. Harf Jawab__27": {
        "arti_sw": "KWANINI! / NDIO BILA SHAKA",
        "desc_sw": "Kwanini! Tumekuwa mashahidi (Jibu linalothibitisha kukanusha)",
        "jenis_sw": "Harf Jawab (Balaa)"
    },
    "7. Harf Jawab__28": {
        "arti_sw": "NDIO / NAAM",
        "desc_sw": "Ndio, na hakika nyinyi mtakuwa miongoni mwa waliokaribishwa",
        "jenis_sw": "Harf Jawab (Na'am)"
    },
    "7. Harf Jawab__29": {
        "arti_sw": "NDIO! NAAPA KWA MOLA WANGU",
        "desc_sw": "Ndio! Naapa kwa Mola wangu hakika hiyo ni haki",
        "jenis_sw": "Harf Jawab li al-Qasam (Iiy)"
    },

    # 8. Harf Ibtida'
    "8. Harf Ibtida'__30": {
        "arti_sw": "MPAKA AKAFIKIA",
        "desc_sw": "Mpaka mtume na walioamini pamoja naye wakasema",
        "jenis_sw": "Harf Ibtida' (Hattaa)"
    },

    # 9. Harf Tafshil
    "9. Harf Tafshil__31": {
        "arti_sw": "AMA KUHUSU",
        "desc_sw": "Ama yatima usimwonee (Herufi ya kugawa na kueleza kwa kina)",
        "jenis_sw": "Harf Sharat wa Tafsil (Ammaa)"
    },

    # 10. Harf Mufaja'ah
    "10. Harf Mufaja'ah__32": {
        "arti_sw": "MARA AKAGUNDUA",
        "desc_sw": "Mara ikawa joka linalokimbia (Herufi ya tukio la ghafla)",
        "jenis_sw": "Harf Mufaja'ah (Idhaa)"
    },

    # 11. Harf Mufassirah
    "11. Harf Mufassirah__33": {
        "arti_sw": "YAANI / KWAMBA",
        "desc_sw": "Tukamfunulia kwamba: Unda jahazi (Herufi ya ufafanuzi)",
        "jenis_sw": "Harf Tafsir (An)"
    },

    # 12. Harf Istiftahiyah
    "12. Harf Istiftahiyah__34": {
        "arti_sw": "ZINDUKENI! / FAHAMUNI!",
        "desc_sw": "Fahamuni! Hakika mawalii wa Allah hawana hofu",
        "jenis_sw": "Harf Istiftah wa Tanbih (Alaa)"
    },

    # 13. Harf Rada'
    "13. Harf Rada'__35": {
        "arti_sw": "HASHA! / SIVYO KABISA!",
        "desc_sw": "Sivyo kabisa! Karibuni mtajua ukweli (Herufi ya kukemea na kuzuia)",
        "jenis_sw": "Harf Rada' wa Zajr (Kallaa)"
    },

    # 14. Harf Ta'ajjub
    "14. Harf Ta'ajjub__36": {
        "arti_sw": "JAMANI! NI NINI KILICHOWAVUMILISHA!",
        "desc_sw": "Jamani! Ni nini kilichowavumilisha na Moto! (Herufi ya mshangao mkuu)",
        "jenis_sw": "Maa at-Ta'ajjubiyyah"
    },

    # 15. Harf Fariqah
    "15. Harf Fariqah__37": {
        "arti_sw": "BILA SHAKA / HAKIKA",
        "desc_sw": "Bila shaka kila mmoja atalipwa kikamilifu matendo yake",
        "jenis_sw": "Laam al-Fariqah / In Mukhaffafah"
    },

    # 16. Harf Mauthi'ah
    "16. Harf Mauthi'ah__38": {
        "arti_sw": "HAKIKA MKIMTII",
        "desc_sw": "Hakika mkimtii mtu kama nyinyi basi mtakuwa wenye hasara",
        "jenis_sw": "Laam al-Mauthi'ah li al-Qasam"
    },

    # 17. Harf Mabany (Fawaatih as-Suwar)
    "17. Harf Mabany__39": {"arti_sw": "Haa Miim", "desc_sw": "Herufi za mwanzo wa sura (Ha Meem)", "jenis_sw": "Harf Muqatta'ah"},
    "17. Harf Mabany__40": {"arti_sw": "Alif Laam Miim", "desc_sw": "Herufi za mwanzo wa sura (Alif Laam Meem)", "jenis_sw": "Harf Muqatta'ah"},
    "17. Harf Mabany__41": {"arti_sw": "Alif Laam Raa", "desc_sw": "Herufi za mwanzo wa sura (Alif Laam Raa)", "jenis_sw": "Harf Muqatta'ah"},
    "17. Harf Mabany__42": {"arti_sw": "Twaa Siin Miim", "desc_sw": "Herufi za mwanzo wa sura (Taa Seen Meem)", "jenis_sw": "Harf Muqatta'ah"},
    "17. Harf Mabany__43": {"arti_sw": "Alif Laam Miim Raa", "desc_sw": "Herufi za mwanzo wa sura (Alif Laam Meem Raa)", "jenis_sw": "Harf Muqatta'ah"},
    "17. Harf Mabany__44": {"arti_sw": "Alif Laam Miim Saad", "desc_sw": "Herufi za mwanzo wa sura (Alif Laam Meem Saad)", "jenis_sw": "Harf Muqatta'ah"},
    "17. Harf Mabany__45": {"arti_sw": "Saad", "desc_sw": "Herufi ya mwanzo wa sura (Saad)", "jenis_sw": "Harf Muqatta'ah"},
    "17. Harf Mabany__46": {"arti_sw": "Twaa Siin", "desc_sw": "Herufi za mwanzo wa sura (Taa Seen)", "jenis_sw": "Harf Muqatta'ah"},
    "17. Harf Mabany__47": {"arti_sw": "Twaa Haa", "desc_sw": "Herufi za mwanzo wa sura (Taa-Haa)", "jenis_sw": "Harf Muqatta'ah"},
    "17. Harf Mabany__48": {"arti_sw": "'Ain Siin Qaaf", "desc_sw": "Herufi za mwanzo wa sura ('Ayn Seen Qaaf)", "jenis_sw": "Harf Muqatta'ah"},
    "17. Harf Mabany__49": {"arti_sw": "Qaaf", "desc_sw": "Herufi ya mwanzo wa sura (Qaaf)", "jenis_sw": "Harf Muqatta'ah"},
    "17. Harf Mabany__50": {"arti_sw": "Kaaf Haa Yaa 'Ain Saad", "desc_sw": "Herufi za mwanzo wa sura (Kaaf Haa Yaa 'Ayn Saad)", "jenis_sw": "Harf Muqatta'ah"},
    "17. Harf Mabany__51": {"arti_sw": "Nuun", "desc_sw": "Herufi ya mwanzo wa sura (Noon)", "jenis_sw": "Harf Muqatta'ah"},
    "17. Harf Mabany__52": {"arti_sw": "Yaa Siin", "desc_sw": "Herufi za mwanzo wa sura (Yaa-Seen)", "jenis_sw": "Harf Muqatta'ah"}
}


def enrich_dhamir_data():
    print("Enriching dhamir_data.json and dhamir_data.js with Swahili...")
    
    with open(os.path.join(BASE_DIR, 'sw_translations.json'), 'r', encoding='utf-8') as f:
        sw_translations = json.load(f)

    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = item.get('No kata', '')
        g_key = f"{b}__{nk}"
        
        # 1. BentukKataSW
        item['BentukKataSW'] = BENTUK_KATA_SW.get(b, b)
        
        # 2. SuratArtiSW
        surat_num = str(item.get('SURAT', ''))
        item['SuratArtiSW'] = SWAHILI_SURAHS.get(surat_num, item.get('SuratArtiEN', ''))
        
        # 3. ArtiKataSW & Grammar SW
        g_info = SWAHILI_GRAMMAR.get(g_key, {})
        item['ArtiKataSW'] = g_info.get('arti_sw', item.get('ArtiKataEN', item.get('Arti kata', '')))
        
        if 'Grammar' not in item:
            item['Grammar'] = {}
        if g_info.get('arti_sw'):
            item['Grammar']['arti_sw'] = g_info['arti_sw']
        if g_info.get('desc_sw'):
            item['Grammar']['desc_sw'] = g_info['desc_sw']
        if g_info.get('jenis_sw'):
            item['Grammar']['jenis_sw'] = g_info['jenis_sw']
            
        # 4. TeksArtiSW
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"
        teks_sw = sw_translations.get(v_key, item.get('TeksArtiEN', item.get('TeksArtiID', '')))
        item['TeksArtiSW'] = teks_sw

    # Write dhamir_data.json
    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Write dhamir_data.js
    with open(os.path.join(BASE_DIR, 'dhamir_data.js'), 'w', encoding='utf-8') as f:
        f.write("const DHAMIR_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n\nif (typeof module !== 'undefined' && module.exports) {\n  module.exports = DHAMIR_DATA;\n}\n")

    print(f"dhamir_data successfully updated with Swahili! (Total items: {len(data)})")


def enrich_harf_data():
    print("Enriching harf_data.json and harf_data.js with Swahili...")
    
    with open(os.path.join(BASE_DIR, 'sw_translations.json'), 'r', encoding='utf-8') as f:
        sw_translations = json.load(f)

    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = item.get('No kata', '')
        g_key = f"{b}__{nk}"
        
        # 1. BentukKataSW
        item['BentukKataSW'] = BENTUK_HARF_SW.get(b, b)
        
        # 2. SuratArtiSW
        surat_num = str(item.get('SURAT', ''))
        item['SuratArtiSW'] = SWAHILI_SURAHS.get(surat_num, item.get('SuratArtiEN', ''))
        
        # 3. ArtiKataSW & Grammar SW
        g_info = SWAHILI_HARF_GRAMMAR.get(g_key, {})
        item['ArtiKataSW'] = g_info.get('arti_sw', item.get('ArtiKataEN', item.get('Arti kata', '')))
        
        if 'Grammar' not in item:
            item['Grammar'] = {}
        if g_info.get('arti_sw'):
            item['Grammar']['arti_sw'] = g_info['arti_sw']
        if g_info.get('desc_sw'):
            item['Grammar']['desc_sw'] = g_info['desc_sw']
        if g_info.get('jenis_sw'):
            item['Grammar']['jenis_sw'] = g_info['jenis_sw']
            
        # 4. TeksArtiSW
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"
        teks_sw = sw_translations.get(v_key, item.get('TeksArtiEN', item.get('TeksArtiID', '')))
        item['TeksArtiSW'] = teks_sw

    # Write harf_data.json
    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Write harf_data.js
    with open(os.path.join(BASE_DIR, 'harf_data.js'), 'w', encoding='utf-8') as f:
        f.write("const HARF_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n\nif (typeof module !== 'undefined' && module.exports) {\n  module.exports = HARF_DATA;\n}\n")

    print(f"harf_data successfully updated with Swahili! (Total items: {len(data)})")


if __name__ == '__main__':
    enrich_dhamir_data()
    enrich_harf_data()
