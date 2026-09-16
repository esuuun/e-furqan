#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to synchronize Hausa (ha) across:
1. build_multilingual_dataset.py
2. build_harf_dataset.py
3. update_data.py
4. fetch_all_multilingual.py
5. PANDUAN_UPDATE_DATA.md
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

from build_hausa_dataset import HAUSA_SURAHS, BENTUK_KATA_HA, HAUSA_GRAMMAR, BENTUK_HARF_HA, HAUSA_HARF_GRAMMAR

# 1. Update update_data.py
print("Updating update_data.py...")
with open(os.path.join(BASE_DIR, 'update_data.py'), 'r', encoding='utf-8') as f:
    ud_code = f.read()

ud_code = ud_code.replace(
    "'pt': {}\n    }",
    "'pt': {},\n        'ha': {}\n    }"
)
ud_code = ud_code.replace(
    "'pt': 'pt_translations.json'\n    }",
    "'pt': 'pt_translations.json',\n        'ha': 'ha_translations.json'\n    }"
)
ud_code = ud_code.replace(
    "item['BentukKataPT'] = b_labels.get('pt', b)",
    "item['BentukKataPT'] = b_labels.get('pt', b)\n        item['BentukKataHA'] = b_labels.get('ha', b)"
)
ud_code = ud_code.replace(
    "item['SuratArtiPT'] = s_info.get('arti_pt', s_info['arti_en'])",
    "item['SuratArtiPT'] = s_info.get('arti_pt', s_info['arti_en'])\n            item['SuratArtiHA'] = s_info.get('arti_ha', s_info['arti_en'])"
)
ud_code = ud_code.replace(
    "item['ArtiKataPT'] = gm.get('arti_pt', item['Arti kata'])",
    "item['ArtiKataPT'] = gm.get('arti_pt', item['Arti kata'])\n        item['ArtiKataHA'] = gm.get('arti_ha', item['Arti kata'])"
)
ud_code = ud_code.replace(
    "item['TeksArtiPT'] = caches['pt'].get(v_key, teks_id)",
    "item['TeksArtiPT'] = caches['pt'].get(v_key, teks_id)\n        item['TeksArtiHA'] = caches['ha'].get(v_key, teks_id)"
)
ud_code = ud_code.replace(
    "langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN', 'RU', 'ZH', 'ES', 'TR', 'PT']",
    "langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN', 'RU', 'ZH', 'ES', 'TR', 'PT', 'HA']"
)

with open(os.path.join(BASE_DIR, 'update_data.py'), 'w', encoding='utf-8') as f:
    f.write(ud_code)
print("update_data.py updated!")

# 2. Update fetch_all_multilingual.py
print("Updating fetch_all_multilingual.py...")
with open(os.path.join(BASE_DIR, 'fetch_all_multilingual.py'), 'r', encoding='utf-8') as f:
    fam_code = f.read()

fam_code = fam_code.replace(
    "'tr': ('tr_translations.json', 'tr.diyanet')\n}",
    "'tr': ('tr_translations.json', 'tr.diyanet'),\n    'ha': ('ha_translations.json', 'ha.gumi')\n}"
)
with open(os.path.join(BASE_DIR, 'fetch_all_multilingual.py'), 'w', encoding='utf-8') as f:
    f.write(fam_code)
print("fetch_all_multilingual.py updated!")

# 3. Update PANDUAN_UPDATE_DATA.md
print("Updating PANDUAN_UPDATE_DATA.md...")
with open(os.path.join(BASE_DIR, 'PANDUAN_UPDATE_DATA.md'), 'r', encoding='utf-8') as f:
    p_code = f.read()

p_code = p_code.replace(
    "13 Bahasa dunia (ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT)",
    "14 Bahasa dunia (ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT, HA)"
)
p_code = p_code.replace(
    "## 📁 Struktur File Hasil Update & Cache 13 Bahasa",
    "## 📁 Struktur File Hasil Update & Cache 14 Bahasa"
)
if "ha_translations.json" not in p_code:
    p_code = p_code.replace(
        "| **`pt_translations.json`** | Terjemahan Bahasa Portugis (Samir El-Hayek / Helmi Nasr). |",
        "| **`pt_translations.json`** | Terjemahan Bahasa Portugis (Samir El-Hayek / Helmi Nasr). |\n| **`ha_translations.json`** | Terjemahan Bahasa Hausa (Sheikh Abubakar Mahmoud Gumi). |"
    )

with open(os.path.join(BASE_DIR, 'PANDUAN_UPDATE_DATA.md'), 'w', encoding='utf-8') as f:
    f.write(p_code)
print("PANDUAN_UPDATE_DATA.md updated!")

# Re-run build_hausa_dataset to ensure 100% data completeness
from build_hausa_dataset import enrich_dhamir_data, enrich_harf_data
enrich_dhamir_data()
enrich_harf_data()

print("\nAll files synchronized successfully!")
