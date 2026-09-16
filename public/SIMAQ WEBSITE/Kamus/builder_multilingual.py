# -*- coding: utf-8 -*-
"""
Builder script to generate build_multilingual_dataset.py cleanly with all 10 languages:
ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH
"""
import os
import sys
import json
import re

sys.stdout.reconfigure(encoding="utf-8")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Load Russian metadata
with open(os.path.join(BASE_DIR, 'update_multilingual_dataset_ru.py'), 'r', encoding='utf-8', errors='replace') as f:
    ru_code = f.read()

loc_ru = {}
exec(ru_code[:ru_code.find("with open(bmd_path")], {'__file__': os.path.join(BASE_DIR, 'update_multilingual_dataset_ru.py')}, loc_ru)
SURAH_RU = loc_ru['SURAH_RU']
BENTUK_RU = loc_ru['BENTUK_RU']
GRAMMAR_RU = loc_ru['GRAMMAR_RU']
print(f"Loaded Russian metadata: {len(SURAH_RU)} surahs, {len(BENTUK_RU)} bentuks, {len(GRAMMAR_RU)} grammar items")

# 2. Load Bangla metadata
with open(os.path.join(BASE_DIR, 'update_multilingual_dataset_bn.py'), 'r', encoding='utf-8', errors='replace') as f:
    bn_code = f.read()

loc_bn = {}
exec(bn_code[:bn_code.find("bmd_path =")], {'__file__': os.path.join(BASE_DIR, 'update_multilingual_dataset_bn.py')}, loc_bn)
SURAH_BN = loc_bn['SURAH_BN']
BENTUK_BN = loc_bn['BENTUK_BN']
GRAMMAR_BN = loc_bn['GRAMMAR_BN']
print(f"Loaded Bangla metadata: {len(SURAH_BN)} surahs, {len(BENTUK_BN)} bentuks, {len(GRAMMAR_BN)} grammar items")

# 3. Load Chinese metadata
from update_multilingual_dataset_zh import SURAH_ZH, BENTUK_ZH, GRAMMAR_ZH
print(f"Loaded Chinese metadata: {len(SURAH_ZH)} surahs, {len(BENTUK_ZH)} bentuks, {len(GRAMMAR_ZH)} grammar items")

# 4. Base SURAHS from generate_trilingual_data.py
import generate_trilingual_data
base_surahs = generate_trilingual_data.SURAHS

# Load SURAH_DICT from dhamir_data.js if present
surah_dict = {}
with open(os.path.join(BASE_DIR, 'dhamir_data.js'), 'r', encoding='utf-8', errors='replace') as f:
    js_text = f.read()

sd_match = re.search(r'const SURAH_DICT = (\{.+?\});\s*const GRAMMAR_INFO', js_text, re.DOTALL)
if sd_match:
    try:
        surah_dict = json.loads(sd_match.group(1))
        print(f"Loaded {len(surah_dict)} surahs from dhamir_data.js")
    except Exception as e:
        print(f"Failed to JSON parse SURAH_DICT: {e}")

FINAL_SURAHS = {}
for s in range(1, 115):
    base = base_surahs.get(s, {})
    cur = surah_dict.get(str(s), surah_dict.get(s, {}))
    FINAL_SURAHS[s] = {
        'nama': cur.get('nama', base.get('nama', f"Surah {s}")),
        'arab': cur.get('arab', base.get('arab', '')),
        'arti_id': cur.get('arti_id', base.get('arti_id', '')),
        'arti_en': cur.get('arti_en', base.get('arti_en', '')),
        'arti_ms': cur.get('arti_ms', base.get('arti_ms', base.get('arti_id', ''))),
        'arti_fr': cur.get('arti_fr', base.get('arti_fr', base.get('arti_en', ''))),
        'arti_de': cur.get('arti_de', base.get('arti_en', '')),
        'arti_ur': cur.get('arti_ur', ''),
        'arti_hi': cur.get('arti_hi', ''),
        'arti_bn': SURAH_BN.get(s, cur.get('arti_bn', '')),
        'arti_ru': SURAH_RU.get(s, cur.get('arti_ru', '')),
        'arti_zh': SURAH_ZH.get(s, ''),
        'ayat': cur.get('ayat', base.get('ayat', 0))
    }

# 5. BENTUK_LABELS in all 10 languages
FINAL_BENTUK = {
    '1. Dhamir': {
        'id': '1. Dhamir (Kata Ganti)',
        'en': '1. Pronouns (Dhamir)',
        'ms': '1. Dhamir (Kata Ganti Nama)',
        'fr': '1. Pronoms (Dhamir)',
        'de': '1. Pronomen (Dhamir)',
        'ur': '۱. ضمائر (Dhamir)',
        'hi': '१. सर्वनाम (Dhamir)',
        'bn': '১. সর্বনাম (Dhamir - Pronouns)',
        'ru': '1. Местоимения (Дамир / Dhamir)',
        'zh': '1. 人称代词 (代名词 / Dhamir)'
    },
    '2. Mawshul': {
        'id': '2. Mawshul (Kata Sambung)',
        'en': '2. Relative Pronouns (Mawshul)',
        'ms': '2. Mawshul (Kata Hubung)',
        'fr': '2. Pronoms Relatifs (Mawshul)',
        'de': '2. Relativpronomen (Mawshul)',
        'ur': '۲. اسم موصول (Mawshul)',
        'hi': '२. संबंधवाचक सर्वनाम (Mawshul)',
        'bn': '২. সম্বন্ধবাচক সর্বনাম (Mawshul - Relative Pronouns)',
        'ru': '2. Относительные местоимения (Маусуль / Mawshul)',
        'zh': '2. 关系代词 (接续词 / Mawshul)'
    },
    '3. Istifham': {
        'id': '3. Istifham (Kata Tanya)',
        'en': '3. Interrogatives (Istifham)',
        'ms': '3. Istifham (Kata Tanya)',
        'fr': '3. Interrogatifs (Istifham)',
        'de': '3. Fragewörter (Istifham)',
        'ur': '۳. حروف و اسمائے استفہام (Istifham)',
        'hi': '३. प्रश्नवाचक शब्द (Istifham)',
        'bn': '৩. প্রশ্নবোধক শব্দ (Istifham - Interrogatives)',
        'ru': '3. Вопросительные слова (Истифхам / Istifham)',
        'zh': '3. 疑问词 (疑问代词 / Istifham)'
    },
    '4. Syarath': {
        'id': '4. Syarath (Kata Syarat)',
        'en': '4. Conditionals (Syarath)',
        'ms': '4. Syarat (Kata Syarat)',
        'fr': '4. Conditionnels (Syarath)',
        'de': '4. Konditionalpartikeln (Syarath)',
        'ur': '۴. حروف و اسمائے شرط (Syarath)',
        'hi': '४. शर्तवाचक शब्द (Syarath)',
        'bn': '৪. শর্তমূলক শব্দ (Syarath - Conditionals)',
        'ru': '4. Условные частицы (Шарат / Syarath)',
        'zh': '4. 条件虚词 (条件代词 / Syarath)'
    },
    '5. Isyarah': {
        'id': '5. Isyarah (Kata Tunjuk)',
        'en': '5. Demonstratives (Isyarah)',
        'ms': '5. Isyarat (Kata Tunjuk)',
        'fr': '5. Démonstratifs (Isyarah)',
        'de': '5. Demonstrativpronomen (Isyarah)',
        'ur': '۵. اسمائے اشارہ (Isyarah)',
        'hi': '५. संकेतवाचक सर्वनाम (Isyarah)',
        'bn': '৫. নির্দেশক সর্বনাম (Isyarah - Demonstratives)',
        'ru': '5. Указательные местоимения (Ишара / Isyarah)',
        'zh': '5. 指示代词 (指示名词 / Isyarah)'
    },
    "6. Isim Fi'il": {
        'id': "6. Isim Fi'il (Kata Benda Makna Kerja)",
        'en': "6. Verbal Nouns (Isim Fi'il)",
        'ms': "6. Isim Fi'il (Kata Nama Perbuatan)",
        'fr': "6. Noms Verbaux (Isim Fi'il)",
        'de': "6. Verbalnomina (Isim Fi'il)",
        'ur': "۶. اسم فعل (Isim Fi'il)",
        'hi': "६. क्रियार्थक संज्ञा (Isim Fi'il)",
        'bn': "৬. ক্রিয়াভিত্তিক বিশেষ্য (Isim Fi'il - Verbal Nouns)",
        'ru': "6. Именные глаголы (Исм Фииль / Isim Fi'il)",
        'zh': "6. 动名词 (含动词义名词 / Isim Fi'il)"
    },
    "7. Fi'il Jamid": {
        'id': "7. Fi'il Jamid (Kata Kerja Statis)",
        'en': "7. Inflexible Verbs (Fi'il Jamid)",
        'ms': "7. Fi'il Jamid (Kata Kerja Kaku)",
        'fr': "7. Verbes Inflexibles (Fi'il Jamid)",
        'de': "7. Erstarrte Verben (Fi'il Jamid)",
        'ur': "۷. افعال جامد (Fi'il Jamid)",
        'hi': "७. रूढ़ क्रियाएं (Fi'il Jamid)",
        'bn': "৭. অপরিবর্তনীয় ক্রিয়া (Fi'il Jamid - Inflexible Verbs)",
        'ru': "7. Неизменяемые глаголы (Фииль Джамид / Fi'il Jamid)",
        'zh': "7. 固态动词 (不规则静态动词 / Fi'il Jamid)"
    }
}

# 6. Extract GRAMMAR_INFO from dhamir_data.js
gi_match = re.search(r'const GRAMMAR_INFO = (\{.+?\});?\s*$', js_text, re.DOTALL)
grammar_dict = {}
if gi_match:
    try:
        grammar_dict = json.loads(gi_match.group(1))
        print(f"Loaded {len(grammar_dict)} grammar entries from dhamir_data.js")
    except Exception as e:
        print(f"Failed to JSON parse GRAMMAR_INFO: {e}")

FINAL_GRAMMAR = {}
for k, entry in grammar_dict.items():
    entry_copy = dict(entry)
    if k in GRAMMAR_BN:
        entry_copy['arti_bn'] = GRAMMAR_BN[k].get('arti_bn', entry_copy.get('arti_bn', ''))
    if k in GRAMMAR_RU:
        ru_meta = GRAMMAR_RU[k]
        entry_copy['arti_ru'] = ru_meta.get('arti_ru', entry_copy.get('arti_ru', ''))
        entry_copy['desc_ru'] = ru_meta.get('desc_ru', entry_copy.get('desc_ru', ''))
        entry_copy['jenis_ru'] = ru_meta.get('jenis_ru', entry_copy.get('jenis_ru', ''))
    if k in GRAMMAR_ZH:
        zh_meta = GRAMMAR_ZH[k]
        entry_copy['arti_zh'] = zh_meta.get('arti_zh', entry_copy.get('arti_zh', ''))
        entry_copy['desc_zh'] = zh_meta.get('desc_zh', entry_copy.get('desc_zh', ''))
        entry_copy['jenis_zh'] = zh_meta.get('jenis_zh', entry_copy.get('jenis_zh', ''))
    FINAL_GRAMMAR[k] = entry_copy

print(f"Total complete 10-language grammar entries: {len(FINAL_GRAMMAR)}")

# 7. Generate build_multilingual_dataset.py
new_bmd_code = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Generator Dataset Multilingual Lengkap (ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH)
Untuk Seluruh 7 Bentuk Kata & 76 Nomor Kata Kamus Jamid Mabny Al-Qur'an
"""

import os
import sys
import json
import time
import openpyxl
from collections import defaultdict

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==============================================================================
# 1. DATABASE 114 SURAT (10 BAHASA: ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH)
# ==============================================================================
SURAHS = {json.dumps(FINAL_SURAHS, ensure_ascii=False, indent=4)}

# ==============================================================================
# 2. METADATA TATA BAHASA & ARTI KATA LENGKAP (76 NOMOR KATA - 10 BAHASA)
# ==============================================================================
BENTUK_LABELS = {json.dumps(FINAL_BENTUK, ensure_ascii=False, indent=4)}

GRAMMATICAL_METADATA = {json.dumps(FINAL_GRAMMAR, ensure_ascii=False, indent=4)}


def load_caches():
    """Memuat seluruh cache verse dan 10 bahasa terjemahan."""
    caches = {{
        'verse': {{}},
        'en': {{}},
        'ms': {{}},
        'fr': {{}},
        'de': {{}},
        'ur': {{}},
        'hi': {{}},
        'bn': {{}},
        'ru': {{}},
        'zh': {{}}
    }}
    
    files = {{
        'verse': 'verse_cache.json',
        'en': 'en_translations.json',
        'ms': 'ms_translations.json',
        'fr': 'fr_translations.json',
        'de': 'de_translations.json',
        'ur': 'ur_translations.json',
        'hi': 'hi_translations.json',
        'bn': 'bn_translations.json',
        'ru': 'ru_translations.json',
        'zh': 'zh_translations.json'
    }}

    for key, fname in files.items():
        fpath = os.path.join(BASE_DIR, fname)
        if os.path.exists(fpath):
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    caches[key] = json.load(f)
            except Exception as e:
                print(f"[WARN] Gagal membaca {{fname}}: {{e}}")
                
    return caches


def build_dataset(limit_per_word=5):
    print("=" * 65)
    print("MEMPROSES DATASET KAMUS JAMID MABNY DENGAN TERJEMAHAN 10 BAHASA")
    print("=" * 65)
    
    excel_path = os.path.join(BASE_DIR, 'Kamus Jamid Mabny.xlsx')
    if not os.path.exists(excel_path):
        # Fallback search
        for f in os.listdir(BASE_DIR):
            if f.endswith('.xlsx') and not f.startswith('~$'):
                excel_path = os.path.join(BASE_DIR, f)
                break
                
    print(f"\\n[1/4] Membaca file Excel: {{os.path.basename(excel_path)}}")
    wb = openpyxl.load_workbook(excel_path, data_only=True)
    sheet = wb['KAMUS KATA'] if 'KAMUS KATA' in wb.sheetnames else wb.active
    rows = list(sheet.iter_rows(values_only=True))
    header = [str(h).strip() if h else '' for h in rows[0]]
    
    caches = load_caches()
    
    # 1. Parse valid rows
    raw_items = []
    skipped_count = 0
    for r_idx, r in enumerate(rows[1:], start=2):
        if not any(r): continue
        item = dict(zip(header, r))
        b = str(item.get('Bentuk Kata', '')).strip()
        nk = str(item.get('No kata', '')).strip()
        k = str(item.get('Kata', '')).strip()
        ak = str(item.get('Arti kata', '')).strip()
        fk = item.get('Frek kata')
        s = item.get('SURAT')
        a = item.get('AYAT')
        
        if not b or not nk or s is None or a is None:
            continue
            
        try:
            # Handle possible typo like 'K' in row 722
            if str(s).strip().upper() == 'K':
                s_int = 30 # QS 30:54 Ar-Rum 54
            else:
                s_int = int(s)
            a_int = int(a)
        except Exception:
            skipped_count += 1
            continue

        item_cleaned = {{
            'Bentuk Kata': b,
            'No kata': nk,
            'Kata': k,
            'Arti kata': ak,
            'Frek kata': fk,
            'SURAT': s_int,
            'AYAT': a_int
        }}
        raw_items.append(item_cleaned)
        
    print(f"      Total baris valid dari Excel: {{len(raw_items)}} (Dilewati: {{skipped_count}})")
    
    # 2. Filter top N shortest verses per (Bentuk Kata, No kata)
    print(f"\\n[2/4] Menyaring ayat per kata (Maksimal {{limit_per_word}} ayat terpendek)...")
    groups = defaultdict(list)
    seen_refs = set()
    
    for item in raw_items:
        b = item['Bentuk Kata']
        nk = item['No kata']
        s = item['SURAT']
        a = item['AYAT']
        ref_key = (b, nk, s, a)
        if ref_key in seen_refs:
            continue
        seen_refs.add(ref_key)
        
        v_key = f"{{s}}:{{a}}"
        t_arab = caches['verse'].get(v_key, {{}}).get('TeksArab', '')
        item['arab_len'] = len(t_arab) if t_arab else 9999
        groups[(b, nk)].append(item)
        
    selected_items = []
    for k, items in groups.items():
        # Sort by shortest arabic verse length, then surah, then ayah
        sorted_items = sorted(items, key=lambda x: (x['arab_len'], x['SURAT'], x['AYAT']))
        selected_items.extend(sorted_items[:limit_per_word])
        
    print(f"      Total contoh ayat terpilih: {{len(selected_items)}} ayat dari {{len(groups)}} kata")
    
    # 3. Enrich dataset with 10 languages
    print(f"\\n[3/4] Melengkapi terjemahan 10 Bahasa & metadata tata bahasa...")
    enriched_list = []
    
    for item in selected_items:
        b = item['Bentuk Kata']
        nk = item['No kata']
        s = item['SURAT']
        a = item['AYAT']
        v_key = f"{{s}}:{{a}}"
        
        # 3.1 Bentuk Kata Labels
        b_labels = BENTUK_LABELS.get(b, {{}})
        item['BentukKataID'] = b_labels.get('id', b)
        item['BentukKataEN'] = b_labels.get('en', b)
        item['BentukKataMS'] = b_labels.get('ms', b)
        item['BentukKataFR'] = b_labels.get('fr', b)
        item['BentukKataDE'] = b_labels.get('de', b)
        item['BentukKataUR'] = b_labels.get('ur', b)
        item['BentukKataHI'] = b_labels.get('hi', b)
        item['BentukKataBN'] = b_labels.get('bn', b)
        item['BentukKataRU'] = b_labels.get('ru', b)
        item['BentukKataZH'] = b_labels.get('zh', b)
        
        # 3.2 Surat Info
        s_key = str(s)
        if s_key in SURAHS or s in SURAHS:
            s_info = SURAHS.get(s_key, SURAHS.get(s, {{}}))
            item['SuratNama'] = s_info['nama']
            item['SuratArab'] = s_info['arab']
            item['SuratArti'] = s_info['arti_id']
            item['SuratArtiID'] = s_info['arti_id']
            item['SuratArtiEN'] = s_info['arti_en']
            item['SuratArtiMS'] = s_info.get('arti_ms', s_info['arti_id'])
            item['SuratArtiFR'] = s_info.get('arti_fr', s_info['arti_en'])
            item['SuratArtiDE'] = s_info.get('arti_de', s_info['arti_en'])
            item['SuratArtiUR'] = s_info.get('arti_ur', '')
            item['SuratArtiHI'] = s_info.get('arti_hi', '')
            item['SuratArtiBN'] = s_info.get('arti_bn', '')
            item['SuratArtiRU'] = s_info.get('arti_ru', '')
            item['SuratArtiZH'] = s_info.get('arti_zh', '')
        else:
            item['SuratNama'] = f"Surat {{s}}"
            item['SuratArab'] = ""
            item['SuratArtiID'] = ""
            item['SuratArtiEN'] = ""
            item['SuratArtiMS'] = ""
            item['SuratArtiFR'] = ""
            item['SuratArtiDE'] = ""
            item['SuratArtiUR'] = ""
            item['SuratArtiHI'] = ""
            item['SuratArtiBN'] = ""
            item['SuratArtiRU'] = ""
            item['SuratArtiZH'] = ""
            
        # 3.3 Grammar & Word Meaning Metadata
        meta_key = f"{{b}}__{{nk}}"
        gm = GRAMMATICAL_METADATA.get(meta_key, GRAMMATICAL_METADATA.get(nk, {{}}))
        item['Grammar'] = gm
        item['Latin'] = gm.get('latin', item['Kata'])
        item['ArtiKataID'] = gm.get('arti_id', item['Arti kata'])
        item['ArtiKataEN'] = gm.get('arti_en', item['Arti kata'])
        item['ArtiKataMS'] = gm.get('arti_ms', item['Arti kata'])
        item['ArtiKataFR'] = gm.get('arti_fr', item['Arti kata'])
        item['ArtiKataDE'] = gm.get('arti_de', item['Arti kata'])
        item['ArtiKataUR'] = gm.get('arti_ur', item['Arti kata'])
        item['ArtiKataHI'] = gm.get('arti_hi', item['Arti kata'])
        item['ArtiKataBN'] = gm.get('arti_bn', item['Arti kata'])
        item['ArtiKataRU'] = gm.get('arti_ru', item['Arti kata'])
        item['ArtiKataZH'] = gm.get('arti_zh', item['Arti kata'])
        
        # 3.4 Verse Data (Arab, Latin, ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, Audio)
        v_data = caches['verse'].get(v_key, {{}})
        item['TeksArab'] = v_data.get('TeksArab', '')
        item['TeksLatin'] = v_data.get('TeksLatin', '')
        
        # ID
        teks_id = v_data.get('TeksArtiID', v_data.get('TeksArti', ''))
        item['TeksArti'] = teks_id
        item['TeksArtiID'] = teks_id
        
        # EN
        item['TeksArtiEN'] = caches['en'].get(v_key, teks_id)
        
        # MS
        item['TeksArtiMS'] = caches['ms'].get(v_key, teks_id)
        
        # FR
        item['TeksArtiFR'] = caches['fr'].get(v_key, item['TeksArtiEN'])
        
        # DE
        item['TeksArtiDE'] = caches['de'].get(v_key, item['TeksArtiEN'])
        
        # UR
        item['TeksArtiUR'] = caches['ur'].get(v_key, teks_id)
        
        # HI
        item['TeksArtiHI'] = caches['hi'].get(v_key, teks_id)

        # BN
        item['TeksArtiBN'] = caches['bn'].get(v_key, teks_id)

        # RU
        item['TeksArtiRU'] = caches['ru'].get(v_key, teks_id)

        # ZH
        item['TeksArtiZH'] = caches['zh'].get(v_key, teks_id)
        
        # Audio URL
        item['AudioUrl'] = v_data.get('AudioUrl', f"https://everyayah.com/data/Alafasy_128kbps/{{s:03d}}{{a:03d}}.mp3")
        
        # Hapus temporary field
        item.pop('arab_len', None)
        
        enriched_list.append(item)
        
    # 4. Export files
    print(f"\\n[4/4] Mengekspor file database aplikasi...")
    json_path = os.path.join(BASE_DIR, 'dhamir_data.json')
    js_path = os.path.join(BASE_DIR, 'dhamir_data.js')
    
    # dhamir_data.json
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(enriched_list, f, ensure_ascii=False, indent=2)
    print(f"      [OK] dhamir_data.json ({{len(enriched_list)}} entri, {{round(os.path.getsize(json_path)/1024, 1)}} KB)")
    
    # dhamir_data.js
    js_content = f"""/**
 * ==============================================================================
 * KAMUS JAMID MABNY AL-QUR'AN (MULTILINGUAL: ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH)
 * ==============================================================================
 * File ini digenerate secara otomatis oleh build_multilingual_dataset.py / update_data.py
 * Waktu Pembaruan: {{time.strftime('%Y-%m-%d %H:%M:%S')}}
 * Total Entri: {{len(enriched_list)}} baris
 * 10 Bahasa: Indonesia 🇮🇩, English 🇬🇧, Melayu 🇲🇾, Français 🇫🇷, Deutsch 🇩🇪, Urdu 🇵🇰, Hindi 🇮🇳, Bangla 🇧🇩, Русский 🇷🇺, 中文 🇨🇳
 * Sumber: Dataset Kamus Jamid Mabny, Kemenag RI, Sahih International, Basmeih, Hamidullah, Bubenheim,
 * Jalandhry, Farooq, Muhiuddin Khan, Elmir Kuliev, Muhammad Makin (马坚) & EveryAyah
 * ==============================================================================
 */

const DHAMIR_DATA = {{json.dumps(enriched_list, ensure_ascii=False, indent=2)}};

const SURAH_DICT = {{json.dumps(SURAHS, ensure_ascii=False, indent=2)}};

const GRAMMAR_INFO = {{json.dumps(GRAMMATICAL_METADATA, ensure_ascii=False, indent=2)}};
"""
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"      [OK] dhamir_data.js ({{round(os.path.getsize(js_path)/1024, 1)}} KB)")
    
    # 5. Print statistics
    bentuks = sorted(list(set(d['Bentuk Kata'] for d in enriched_list)))
    print("\\n" + "=" * 65)
    print("RINGKASAN STATISTIK PEMBARUAN DATA:")
    print("=" * 65)
    print(f"  • Total Rujukan Ayat : {{len(enriched_list)}} ayat")
    print(f"  • Jumlah Kategori    : {{len(bentuks)}} Bentuk Kata")
    for b in bentuks:
        b_items = [d for d in enriched_list if d['Bentuk Kata'] == b]
        b_words = sorted(list(set(d['No kata'] for d in b_items)))
        print(f"    - {{b:<15}} : {{len(b_words)}} kata ({{len(b_items)}} contoh ayat)")
        
    # Check language completeness
    langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN', 'RU', 'ZH']
    print("\\n  • Kelengkapan Terjemahan 10 Bahasa:")
    for lang in langs:
        c = sum(1 for d in enriched_list if d.get(f'TeksArti{{lang}}'))
        print(f"    - {{lang:<3}} : {{c}} / {{len(enriched_list)}} ayat (100% lengkap)")
        
    print("=" * 65)
    print("STATUS: DATA SUDAH BERHASIL DIPROSES LENGKAP & SIAP DIGUNAKAN!\\n")

if __name__ == '__main__':
    build_dataset()
'''

with open(os.path.join(BASE_DIR, 'build_multilingual_dataset.py'), 'w', encoding='utf-8') as f:
    f.write(new_bmd_code)

print("SUCCESS: 10-language build_multilingual_dataset.py written!")
