#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to synchronize Persian (fa) across:
1. update_data.py
2. build_harf_dataset.py
3. fetch_all_multilingual.py
4. PANDUAN_UPDATE_DATA.md
And re-build all datasets.
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

# 1. Update update_data.py
print("Updating update_data.py...")
with open(os.path.join(BASE_DIR, 'update_data.py'), 'r', encoding='utf-8') as f:
    ud_code = f.read()

ud_code = ud_code.replace(
    "from build_swahili_dataset import SWAHILI_SURAHS, BENTUK_KATA_SW, SWAHILI_GRAMMAR",
    "from build_swahili_dataset import SWAHILI_SURAHS, BENTUK_KATA_SW, SWAHILI_GRAMMAR\nfrom build_persian_dataset import PERSIAN_SURAHS, BENTUK_KATA_FA, PERSIAN_GRAMMAR"
)
ud_code = ud_code.replace(
    "'sw': {}\n    }",
    "'sw': {},\n        'fa': {}\n    }"
)
ud_code = ud_code.replace(
    "'sw': 'sw_translations.json'\n    }",
    "'sw': 'sw_translations.json',\n        'fa': 'fa_translations.json'\n    }"
)
ud_code = ud_code.replace(
    "item['BentukKataSW'] = b_labels.get('sw', b)",
    "item['BentukKataSW'] = b_labels.get('sw', b)\n        item['BentukKataFA'] = b_labels.get('fa', b)"
)
ud_code = ud_code.replace(
    "item['SuratArtiSW'] = s_info.get('arti_sw', s_info['arti_en'])",
    "item['SuratArtiSW'] = s_info.get('arti_sw', s_info['arti_en'])\n            item['SuratArtiFA'] = s_info.get('arti_fa', s_info['arti_en'])"
)
ud_code = ud_code.replace(
    "gm_sw = SWAHILI_GRAMMAR.get(meta_key, {})",
    "gm_sw = SWAHILI_GRAMMAR.get(meta_key, {})\n        gm_fa = PERSIAN_GRAMMAR.get(meta_key, {})"
)
ud_code = ud_code.replace(
    "if gm_sw.get('jenis_sw'): gm['jenis_sw'] = gm_sw['jenis_sw']",
    "if gm_sw.get('jenis_sw'): gm['jenis_sw'] = gm_sw['jenis_sw']\n        if gm_fa.get('desc_fa'): gm['desc_fa'] = gm_fa['desc_fa']\n        if gm_fa.get('jenis_fa'): gm['jenis_fa'] = gm_fa['jenis_fa']"
)
ud_code = ud_code.replace(
    "item['ArtiKataSW'] = gm_sw.get('arti_sw', gm.get('arti_sw', item['Arti kata']))",
    "item['ArtiKataSW'] = gm_sw.get('arti_sw', gm.get('arti_sw', item['Arti kata']))\n        item['ArtiKataFA'] = gm_fa.get('arti_fa', gm.get('arti_fa', item['Arti kata']))"
)
ud_code = ud_code.replace(
    "item['TeksArtiSW'] = caches['sw'].get(v_key, teks_id)",
    "item['TeksArtiSW'] = caches['sw'].get(v_key, teks_id)\n        item['TeksArtiFA'] = caches['fa'].get(v_key, teks_id)"
)
ud_code = ud_code.replace(
    "langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN', 'RU', 'ZH', 'ES', 'TR', 'PT', 'HA', 'SW']",
    "langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN', 'RU', 'ZH', 'ES', 'TR', 'PT', 'HA', 'SW', 'FA']"
)

with open(os.path.join(BASE_DIR, 'update_data.py'), 'w', encoding='utf-8') as f:
    f.write(ud_code)
print("update_data.py updated!")

# 2. Update build_harf_dataset.py
print("Updating build_harf_dataset.py...")
with open(os.path.join(BASE_DIR, 'build_harf_dataset.py'), 'r', encoding='utf-8') as f:
    bhd_code = f.read()

bhd_code = bhd_code.replace(
    "from build_swahili_dataset import SWAHILI_SURAHS, BENTUK_HARF_SW, SWAHILI_HARF_GRAMMAR",
    "from build_swahili_dataset import SWAHILI_SURAHS, BENTUK_HARF_SW, SWAHILI_HARF_GRAMMAR\nfrom build_persian_dataset import PERSIAN_SURAHS, BENTUK_HARF_FA, PERSIAN_HARF_GRAMMAR"
)
bhd_code = bhd_code.replace(
    "'sw': {}\n    }",
    "'sw': {},\n        'fa': {}\n    }"
)
bhd_code = bhd_code.replace(
    "'sw': 'sw_translations.json'\n    }",
    "'sw': 'sw_translations.json',\n        'fa': 'fa_translations.json'\n    }"
)
bhd_code = bhd_code.replace(
    "item['BentukKataSW'] = BENTUK_HARF_SW.get(b, b)",
    "item['BentukKataSW'] = BENTUK_HARF_SW.get(b, b)\n        item['BentukKataFA'] = BENTUK_HARF_FA.get(b, b)"
)
bhd_code = bhd_code.replace(
    "item['SuratArtiSW'] = SWAHILI_SURAHS.get(s_key, s_info.get('arti_en', ''))",
    "item['SuratArtiSW'] = SWAHILI_SURAHS.get(s_key, s_info.get('arti_en', ''))\n            item['SuratArtiFA'] = PERSIAN_SURAHS.get(s_key, s_info.get('arti_en', ''))"
)
bhd_code = bhd_code.replace(
    "item['SuratArtiSW'] = \"\"",
    "item['SuratArtiSW'] = \"\"\n            item['SuratArtiFA'] = \"\""
)
bhd_code = bhd_code.replace(
    "gm_sw = SWAHILI_HARF_GRAMMAR.get(f\"{b}__{nk}\", {})",
    "gm_sw = SWAHILI_HARF_GRAMMAR.get(f\"{b}__{nk}\", {})\n        gm_fa = PERSIAN_HARF_GRAMMAR.get(f\"{b}__{nk}\", {})"
)
bhd_code = bhd_code.replace(
    "item['ArtiKataSW'] = gm_sw.get('arti_sw', item['Arti kata'])",
    "item['ArtiKataSW'] = gm_sw.get('arti_sw', item['Arti kata'])\n        item['ArtiKataFA'] = gm_fa.get('arti_fa', item['Arti kata'])"
)
bhd_code = bhd_code.replace(
    "if gm_sw.get('jenis_sw'): item['Grammar']['jenis_sw'] = gm_sw['jenis_sw']",
    "if gm_sw.get('jenis_sw'): item['Grammar']['jenis_sw'] = gm_sw['jenis_sw']\n        if gm_fa.get('desc_fa'): item['Grammar']['desc_fa'] = gm_fa['desc_fa']\n        if gm_fa.get('jenis_fa'): item['Grammar']['jenis_fa'] = gm_fa['jenis_fa']"
)
bhd_code = bhd_code.replace(
    "item['TeksArtiSW'] = caches['sw'].get(v_key, teks_id)",
    "item['TeksArtiSW'] = caches['sw'].get(v_key, teks_id)\n        item['TeksArtiFA'] = caches['fa'].get(v_key, teks_id)"
)
bhd_code = bhd_code.replace(
    "15 Bahasa: ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT, HA, SW",
    "16 Bahasa: ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT, HA, SW, FA"
)
bhd_code = bhd_code.replace(
    "langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN', 'RU', 'ZH', 'ES', 'TR', 'PT', 'HA', 'SW']",
    "langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN', 'RU', 'ZH', 'ES', 'TR', 'PT', 'HA', 'SW', 'FA']"
)

with open(os.path.join(BASE_DIR, 'build_harf_dataset.py'), 'w', encoding='utf-8') as f:
    f.write(bhd_code)
print("build_harf_dataset.py updated!")

# 3. Update fetch_all_multilingual.py
print("Updating fetch_all_multilingual.py...")
with open(os.path.join(BASE_DIR, 'fetch_all_multilingual.py'), 'r', encoding='utf-8') as f:
    fam_code = f.read()

fam_code = fam_code.replace(
    "'sw': ('sw_translations.json', 'sw.barwani')\n}",
    "'sw': ('sw_translations.json', 'sw.barwani'),\n    'fa': ('fa_translations.json', 'fa.makarem')\n}"
)
with open(os.path.join(BASE_DIR, 'fetch_all_multilingual.py'), 'w', encoding='utf-8') as f:
    f.write(fam_code)
print("fetch_all_multilingual.py updated!")

# 4. Update PANDUAN_UPDATE_DATA.md
print("Updating PANDUAN_UPDATE_DATA.md...")
with open(os.path.join(BASE_DIR, 'PANDUAN_UPDATE_DATA.md'), 'r', encoding='utf-8') as f:
    p_code = f.read()

p_code = p_code.replace(
    "15 Bahasa dunia (ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT, HA, SW)",
    "16 Bahasa dunia (ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT, HA, SW, FA)"
)
p_code = p_code.replace(
    "## 📁 Struktur File Hasil Update & Cache 15 Bahasa",
    "## 📁 Struktur File Hasil Update & Cache 16 Bahasa"
)
if "fa_translations.json" not in p_code:
    p_code = p_code.replace(
        "| **`sw_translations.json`** | Terjemahan Bahasa Swahili / Kiswahili (Sheikh Ali Muhsin Al-Barwani). |",
        "| **`sw_translations.json`** | Terjemahan Bahasa Swahili / Kiswahili (Sheikh Ali Muhsin Al-Barwani). |\n| **`fa_translations.json`** | Terjemahan Bahasa Persia / Farsi (Ayatullah Naser Makarem Shirazi). |"
    )

with open(os.path.join(BASE_DIR, 'PANDUAN_UPDATE_DATA.md'), 'w', encoding='utf-8') as f:
    f.write(p_code)
print("PANDUAN_UPDATE_DATA.md updated!")

# Re-run build_persian_dataset to ensure 100% data completeness
from build_persian_dataset import enrich_dhamir_data, enrich_harf_data
enrich_dhamir_data()
enrich_harf_data()

print("\nAll files synchronized successfully!")
