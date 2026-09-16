# -*- coding: utf-8 -*-
"""
Updater script to add Bangla (bn) to build_multilingual_dataset.py and update_data.py
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Surah arti_bn mapping
SURAH_BN = {
    1: 'সূচনা / ভূমিকা',
    2: 'গাভী',
    3: 'ইমরানের পরিবার',
    4: 'নারী',
    5: 'খাবার টেবিল',
    6: 'গৃহপালিত পশু',
    7: 'উঁচু স্থান',
    8: 'যুদ্ধলব্ধ সম্পদ',
    9: 'অনুশোচনা / তওবা',
    10: 'নবী ইউনুস',
    11: 'নবী হূদ',
    12: 'নবী ইউসুফ',
    13: 'বজ্রপাত / মেঘের গর্জন',
    14: 'নবী ইব্রাহীম',
    15: 'পাথুরে পাহাড়',
    16: 'মৌমাছি',
    17: 'নৈশ ভ্রমণ / বনী ইসরাঈল',
    18: 'গুহা',
    19: 'মারইয়াম',
    20: 'ত্বা-হা',
    21: 'নবীগণ',
    22: 'হজ',
    23: 'মুমিনগণ',
    24: 'আলো / জ্যোতি',
    25: 'পার্থক্যকারী মানদণ্ড',
    26: 'কবিগণ',
    27: 'পিঁপড়া',
    28: 'কাহিনীসমূহ',
    29: 'মাকড়সা',
    30: 'রোমবাসী',
    31: 'লুকমান',
    32: 'সিজদা',
    33: 'সম্মিলিত বাহিনী',
    34: 'সাবা জাতি',
    35: 'সৃষ্টিকর্তা',
    36: 'ইয়া-সীন',
    37: 'সারিবদ্ধ দলসমূহ',
    38: 'সোয়াদ',
    39: 'দলসমূহ',
    40: 'ক্ষমাকারী',
    41: 'সুস্পষ্ট বিবরণ',
    42: 'পরামর্শ',
    43: 'স্বর্ণালঙ্কার',
    44: 'ধোঁয়া',
    45: 'নতজানু',
    46: 'বালিয়াড়ি',
    47: 'নবী মুহাম্মদ ﷺ',
    48: 'বিজয়',
    49: 'কক্ষসমূহ',
    50: 'ক্বাফ',
    51: 'বিক্ষিপ্তকারী বাতাস',
    52: 'তূর পর্বত',
    53: 'নক্ষত্র',
    54: 'চাঁদ',
    55: 'পরম করুণাময়',
    56: 'মহাপ্রলয়',
    57: 'লোহা',
    58: 'অভিযোগকারিণী',
    59: 'বিতাড়ন / সমাবেশ',
    60: 'পরীক্ষিত নারী',
    61: 'সারিবদ্ধ সৈন্যদল',
    62: 'শুক্রবার / জুমুআ',
    63: 'মুনাফিকগণ',
    64: 'লাভ-ক্ষতি প্রকাশ',
    65: 'তালাক',
    66: 'নিষিদ্ধকরণ',
    67: 'সার্বভৌমত্ব / রাজত্ব',
    68: 'কলম',
    69: 'অনিবার্য সত্য',
    70: 'উর্ধ্বগমনের সোপান',
    71: 'নবী নূহ',
    72: 'জিন জাতি',
    73: 'বস্ত্রাবৃত',
    74: 'পোশাকাবৃত',
    75: 'পুনরুত্থান দিবস',
    76: 'মানবজাতি',
    77: 'প্রেরিত দূতগণ',
    78: 'মহাসংবাদ',
    79: 'উৎপাটনকারী',
    80: 'ভ্রূকুটি করল',
    81: 'সূর্য অন্ধকার হওয়া',
    82: 'বিদীর্ণ হওয়া',
    83: 'মাপে কম দানকারী',
    84: 'খণ্ড-বিখণ্ড হওয়া',
    85: 'নক্ষত্রপুঞ্জ',
    86: 'রাতের আগমনকারী',
    87: 'সর্বোচ্চ মহান',
    88: 'আচ্ছন্নকারী প্রলয়',
    89: 'ভোরবেলা / প্রভাত',
    90: 'নগরী / শহর',
    91: 'সূর্য',
    92: 'রাত / রাত্রি',
    93: 'পূর্বাহ্ণ',
    94: 'বক্ষ প্রশস্তকরণ',
    95: 'ত্বীন / ডুমুর',
    96: 'রক্তপিণ্ড',
    97: 'মহিমান্বিত রাত',
    98: 'সুস্পষ্ট প্রমাণ',
    99: 'মহাকম্পন',
    100: 'অভিযানকারী অশ্ব',
    101: 'মহাবিপদ',
    102: 'প্রাচুর্যের প্রতিযোগিতা',
    103: 'সময় / মহাকাল',
    104: 'পরনিন্দাকারী',
    105: 'হাতি',
    106: 'কুরাইশ',
    107: 'নিত্যব্যবহার্য সাহায্য',
    108: 'অফুরন্ত কল্যাণ',
    109: 'কাফেরগণ',
    110: 'সাহায্য',
    111: 'জ্বলন্ত অঙ্গার',
    112: 'একনিষ্ঠতা',
    113: 'প্রভাত',
    114: 'মানবজাতি'
}

# Bentuk kata in Bengali
BENTUK_BN = {
    '1. Dhamir': '১. সর্বনাম (Dhamir - Pronouns)',
    '2. Mawshul': '২. সম্বন্ধবাচক সর্বনাম (Mawshul - Relative Pronouns)',
    '3. Istifham': '৩. প্রশ্নবোধক শব্দ (Istifham - Interrogatives)',
    '4. Syarath': '৪. শর্তমূলক শব্দ (Syarath - Conditionals)',
    '5. Isyarah': '৫. নির্দেশক সর্বনাম (Isyarah - Demonstratives)',
    "6. Isim Fi'il": "৬. ক্রিয়াভিত্তিক বিশেষ্য (Isim Fi'il - Verbal Nouns)",
    "7. Fi'il Jamid": "৭. অপরিবর্তনীয় ক্রিয়া (Fi'il Jamid - Inflexible Verbs)"
}

# Word arti_bn
GRAMMAR_BN = {
    '1. Dhamir__1a': {'arti_bn': 'সে / তিনি (পুরুষ)'},
    '1. Dhamir__1b': {'arti_bn': '..তার / ..তাকে (পুরুষ)'},
    '1. Dhamir__1c': {'arti_bn': 'কেবল তাকেই (পুরুষ)'},
    '1. Dhamir__2a': {'arti_bn': 'তারা দুজন (পু/স্ত্রী)'},
    '1. Dhamir__2b': {'arti_bn': '..তাদের দুজনের (পু/স্ত্রী)'},
    '1. Dhamir__3a': {'arti_bn': 'তারা সকলে (পুরুষ)'},
    '1. Dhamir__3b': {'arti_bn': '..তাদের / ..তাদেরকে (পুরুষ)'},
    '1. Dhamir__3c': {'arti_bn': 'কেবল তাদেরকেই (পুরুষ)'},
    '1. Dhamir__4a': {'arti_bn': 'সে / তিনি (স্ত্রী)'},
    '1. Dhamir__4b': {'arti_bn': '..তার / ..তাকে (স্ত্রী)'},
    '1. Dhamir__5a': {'arti_bn': 'তারা সকলে (স্ত্রী)'},
    '1. Dhamir__5b': {'arti_bn': '..তাদের (স্ত্রী)'},
    '1. Dhamir__6a': {'arti_bn': 'তুমি / আপনি (পুরুষ)'},
    '1. Dhamir__6b': {'arti_bn': '..তোমার / ..তোমাকে (পুরুষ)'},
    '1. Dhamir__6c': {'arti_bn': 'কেবল তোমাকেই / শুধু তোমারই'},
    '1. Dhamir__7a': {'arti_bn': 'তোমরা দুজন (পু/স্ত্রী)'},
    '1. Dhamir__7b': {'arti_bn': '..তোমাদের দুজনের (পু/স্ত্রী)'},
    '1. Dhamir__8a': {'arti_bn': 'তোমরা সকলে (পুরুষ)'},
    '1. Dhamir__8b': {'arti_bn': '..তোমাদের / ..তোমাদেরকে (পুরুষ)'},
    '1. Dhamir__8c': {'arti_bn': 'কেবল তোমাদেরকেই (পুরুষ)'},
    '1. Dhamir__9b': {'arti_bn': '..তোমার / ..তোমাকে (স্ত্রী)'},
    '1. Dhamir__11a': {'arti_bn': 'আমি / আমাকে'},
    '1. Dhamir__11b': {'arti_bn': '..আমার / ..আমাকে'},
    '1. Dhamir__11c': {'arti_bn': 'কেবল আমাকেই / শুধু আমারই'},
    '1. Dhamir__12a': {'arti_bn': 'আমরা / আমাদেরকে'},
    '1. Dhamir__12b': {'arti_bn': '..আমাদের / ..আমাদেরকে'},
    '1. Dhamir__12c': {'arti_bn': 'কেবল আমাদেরকেই'},

    '2. Mawshul__1': {'arti_bn': 'যা কিছু / যা'},
    '2. Mawshul__2': {'arti_bn': 'যারা / যেসকল ব্যক্তি (পুরুষ)'},
    '2. Mawshul__3': {'arti_bn': 'যে / যে কেউ / যারা'},
    '2. Mawshul__4': {'arti_bn': 'যিনি / যে ব্যক্তি / যা (১ পুরুষ)'},
    '2. Mawshul__5': {'arti_bn': 'যে কোনোটি / যে কেউ'},
    '2. Mawshul__6': {'arti_bn': 'যিনি / যে নারী / যা (১ স্ত্রী)'},
    '2. Mawshul__7': {'arti_bn': 'যে নারীরা / যে সকল নারী'},
    '2. Mawshul__8': {'arti_bn': 'যে নারীরা / যে সকল নারী'},
    '2. Mawshul__9': {'arti_bn': 'যে দুজন (পুরুষ)'},
    '2. Mawshul__10': {'arti_bn': 'যে কোনোটি (স্ত্রী)'},

    '3. Istifham__1': {'arti_bn': 'কী / কী বিষয়'},
    '3. Istifham__2': {'arti_bn': 'কীভাবে / কেমন করে'},
    '3. Istifham__3': {'arti_bn': 'কে / কারা'},
    '3. Istifham__4': {'arti_bn': 'কোনটি / কোন ব্যক্তি'},
    '3. Istifham__5': {'arti_bn': 'কীভাবে / কোথা থেকে'},
    '3. Istifham__6': {'arti_bn': 'কী এমন বিষয় যা'},
    '3. Istifham__7': {'arti_bn': 'কত / কতটা / কতক্ষণ'},
    '3. Istifham__8': {'arti_bn': 'কেন / কী কারণে'},
    '3. Istifham__9': {'arti_bn': 'কোথায় / কোন দিকে'},
    '3. Istifham__10': {'arti_bn': 'কখন / কোন সময়ে'},

    '4. Syarath__1': {'arti_bn': 'যে কেউ / যে ব্যক্তি'},
    '4. Syarath__2': {'arti_bn': 'যা কিছুই'},
    '4. Syarath__3': {'arti_bn': 'যতবারই / প্রতিবার যখন'},
    '4. Syarath__4': {'arti_bn': 'যে কোনোটি / যে কোনো'},
    '4. Syarath__5': {'arti_bn': 'যে কোনোটি (বিশেষ গুরুত্বসহ)'},

    '5. Isyarah__1': {'arti_bn': 'এই / ঐ (১ পুরুষ)'},
    '5. Isyarah__2': {'arti_bn': 'এরা / ওরা (বহুবচন)'},
    '5. Isyarah__3': {'arti_bn': 'এই / ঐ (১ স্ত্রী)'},
    '5. Isyarah__4': {'arti_bn': 'ঐ (স্ত্রী / জড় বহুবচন)'},
    '5. Isyarah__5': {'arti_bn': 'এখানে / এই স্থানে'},
    '5. Isyarah__6': {'arti_bn': 'সেখানে / ঐ স্থানে'},
    '5. Isyarah__7': {'arti_bn': 'এই দুজন (পুরুষ)'},
    '5. Isyarah__8': {'arti_bn': 'ঐ দুজন (স্ত্রী)'},

    "6. Isim Fi'il__1": {'arti_bn': 'পবিত্র ও মহান (তাসবীহ)'},
    "6. Isim Fi'il__2": {'arti_bn': 'নিয়ে এসো / হাজির করো'},
    "6. Isim Fi'il__3": {'arti_bn': 'উফ / ছিঃ (বিরক্তি প্রকাশ)'},
    "6. Isim Fi'il__4": {'arti_bn': 'আমি আশ্রয় চাই / আল্লাহ রক্ষা করুন'},
    "6. Isim Fi'il__5": {'arti_bn': 'এদিকে এসো! / নিয়ে এসো!'},
    "6. Isim Fi'il__6": {'arti_bn': 'কতই না দূর / অসম্ভব'},
    "6. Isim Fi'il__7": {'arti_bn': 'নাও ও পড়ো'},
    "6. Isim Fi'il__8": {'arti_bn': 'শীঘ্রই এসো! / প্রস্তুত হও!'},

    "7. Fi'il Jamid__1": {'arti_bn': 'নয় / নেই'},
    "7. Fi'il Jamid__2": {'arti_bn': 'কতই না নিকৃষ্ট / অত্যন্ত মন্দ'},
    "7. Fi'il Jamid__3": {'arti_bn': 'সম্ভবত / আশা করা যায়'},
    "7. Fi'il Jamid__4": {'arti_bn': 'কতই না উত্তম / শ্রেষ্ঠ'},
    "7. Fi'il Jamid__5": {'arti_bn': 'কতই না নিকৃষ্ট যা'},
    "7. Fi'il Jamid__6": {'arti_bn': 'তারা দুজন শুরু করল'},
    "7. Fi'il Jamid__7": {'arti_bn': 'আল্লাহ পবিত্র / আল্লাহর কাছে আশ্রয়'},
    "7. Fi'il Jamid__8": {'arti_bn': 'কতই না চমৎকার উপদেশ যা'}
}

# 1. Read build_multilingual_dataset.py
bmd_path = os.path.join(BASE_DIR, 'build_multilingual_dataset.py')
with open(bmd_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update SURAHS in content
for s_num, arti_bn in SURAH_BN.items():
    # Target pattern: "'arti_hi': '...', 'ayat':"
    # Replace with "'arti_hi': '...', 'arti_bn': '" + arti_bn + "', 'ayat':"
    # Find specific surah line
    import re
    pattern = rf"({s_num}:\s*\{{[^}}]*'arti_hi':\s*['\"][^'\"]*['\"]),\s*('ayat':\s*\d+\}})"
    def repl(m):
        return f"{m.group(1)}, 'arti_bn': '{arti_bn}', {m.group(2)}"
    content = re.sub(pattern, repl, content)

# Update BENTUK_LABELS
for b_key, b_label in BENTUK_BN.items():
    # Find "'hi': '...'" under b_key
    b_escaped = re.escape(b_key)
    pattern = rf"('{b_escaped}':\s*\{{[^}}]*'hi':\s*['\"][^'\"]*['\"])\s*(\}})"
    def repl_b(m):
        return f"{m.group(1)},\n        'bn': '{b_label}'{m.group(2)}"
    content = re.sub(pattern, repl_b, content)

# Update GRAMMATICAL_METADATA
for g_key, g_val in GRAMMAR_BN.items():
    g_escaped = re.escape(g_key)
    arti_bn = g_val['arti_bn']
    pattern = rf"('{g_escaped}':\s*\{{[^}}]*'arti_hi':\s*['\"][^'\"]*['\"])(,\s*[^}}]*\}})"
    def repl_g(m):
        return f"{m.group(1)}, 'arti_bn': '{arti_bn}'{m.group(2)}"
    content = re.sub(pattern, repl_g, content)

# Update load_caches
old_load_caches = """    caches = {
        'verse': {},
        'en': {},
        'ms': {},
        'fr': {},
        'de': {},
        'ur': {},
        'hi': {}
    }
    
    files = {
        'verse': 'verse_cache.json',
        'en': 'en_translations.json',
        'ms': 'ms_translations.json',
        'fr': 'fr_translations.json',
        'de': 'de_translations.json',
        'ur': 'ur_translations.json',
        'hi': 'hi_translations.json'
    }"""

new_load_caches = """    caches = {
        'verse': {},
        'en': {},
        'ms': {},
        'fr': {},
        'de': {},
        'ur': {},
        'hi': {},
        'bn': {}
    }
    
    files = {
        'verse': 'verse_cache.json',
        'en': 'en_translations.json',
        'ms': 'ms_translations.json',
        'fr': 'fr_translations.json',
        'de': 'de_translations.json',
        'ur': 'ur_translations.json',
        'hi': 'hi_translations.json',
        'bn': 'bn_translations.json'
    }"""
content = content.replace(old_load_caches, new_load_caches)

# Update enrichment in build_dataset
old_enrich_b = """        item['BentukKataDE'] = b_labels.get('de', b)
        item['BentukKataUR'] = b_labels.get('ur', b)
        item['BentukKataHI'] = b_labels.get('hi', b)"""
new_enrich_b = """        item['BentukKataDE'] = b_labels.get('de', b)
        item['BentukKataUR'] = b_labels.get('ur', b)
        item['BentukKataHI'] = b_labels.get('hi', b)
        item['BentukKataBN'] = b_labels.get('bn', b)"""
content = content.replace(old_enrich_b, new_enrich_b)

old_enrich_s = """            item['SuratArtiUR'] = s_info.get('arti_ur', '')
            item['SuratArtiHI'] = s_info.get('arti_hi', '')"""
new_enrich_s = """            item['SuratArtiUR'] = s_info.get('arti_ur', '')
            item['SuratArtiHI'] = s_info.get('arti_hi', '')
            item['SuratArtiBN'] = s_info.get('arti_bn', '')"""
content = content.replace(old_enrich_s, new_enrich_s)

old_enrich_s_else = '''            item['SuratArtiUR'] = ""
            item['SuratArtiHI'] = ""'''
new_enrich_s_else = '''            item['SuratArtiUR'] = ""
            item['SuratArtiHI'] = ""
            item['SuratArtiBN'] = ""'''
content = content.replace(old_enrich_s_else, new_enrich_s_else)

old_enrich_gm = """        item['ArtiKataUR'] = gm.get('arti_ur', item['Arti kata'])
        item['ArtiKataHI'] = gm.get('arti_hi', item['Arti kata'])"""
new_enrich_gm = """        item['ArtiKataUR'] = gm.get('arti_ur', item['Arti kata'])
        item['ArtiKataHI'] = gm.get('arti_hi', item['Arti kata'])
        item['ArtiKataBN'] = gm.get('arti_bn', item['Arti kata'])"""
content = content.replace(old_enrich_gm, new_enrich_gm)

old_enrich_teks = """        # HI
        item['TeksArtiHI'] = caches['hi'].get(v_key, teks_id)"""
new_enrich_teks = """        # HI
        item['TeksArtiHI'] = caches['hi'].get(v_key, teks_id)

        # BN
        item['TeksArtiBN'] = caches['bn'].get(v_key, teks_id)"""
content = content.replace(old_enrich_teks, new_enrich_teks)

# Update docstring and header comments in build_multilingual_dataset.py
content = content.replace(
    "(ID, EN, MS, FR, DE, UR, HI)",
    "(ID, EN, MS, FR, DE, UR, HI, BN)"
)
content = content.replace(
    "7 Bahasa: Indonesia 🇮🇩, English 🇬🇧, Melayu 🇲🇾, Français 🇫🇷, Deutsch 🇩🇪, Urdu 🇵🇰, Hindi 🇮🇳",
    "8 Bahasa: Indonesia 🇮🇩, English 🇬🇧, Melayu 🇲🇾, Français 🇫🇷, Deutsch 🇩🇪, Urdu 🇵🇰, Hindi 🇮🇳, Bangla 🇧🇩"
)
content = content.replace(
    "Basmeih, Hamidullah, Bubenheim, Jalandhry, Farooq & EveryAyah",
    "Basmeih, Hamidullah, Bubenheim, Jalandhry, Farooq, Muhiuddin Khan & EveryAyah"
)
content = content.replace(
    "langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI']",
    "langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN']"
)
content = content.replace(
    "Kelengkapan Terjemahan 7 Bahasa:",
    "Kelengkapan Terjemahan 8 Bahasa:"
)

with open(bmd_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"[OK] Updated {bmd_path}")

# 2. Update update_data.py
ud_path = os.path.join(BASE_DIR, 'update_data.py')
with open(ud_path, 'r', encoding='utf-8') as f:
    ud_content = f.read()

ud_content = ud_content.replace(
    "'hi': {}\n    }",
    "'hi': {},\n        'bn': {}\n    }"
)
ud_content = ud_content.replace(
    "'hi': 'hi_translations.json'\n    }",
    "'hi': 'hi_translations.json',\n        'bn': 'bn_translations.json'\n    }"
)
ud_content = ud_content.replace(
    "(7 BAHASA)",
    "(8 BAHASA)"
)
ud_content = ud_content.replace(
    "Dan 7 Bahasa Terjemahan:",
    "Dan 8 Bahasa Terjemahan:\n  - Bangla (Maulana Muhiuddin Khan)"
)

with open(ud_path, 'w', encoding='utf-8') as f:
    f.write(ud_content)

print(f"[OK] Updated {ud_path}")
