#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to synchronize Swahili (sw) across:
1. update_data.py
2. fetch_all_multilingual.py
3. PANDUAN_UPDATE_DATA.md
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
    "'ha': {}\n    }",
    "'ha': {},\n        'sw': {}\n    }"
)
ud_code = ud_code.replace(
    "'ha': 'ha_translations.json'\n    }",
    "'ha': 'ha_translations.json',\n        'sw': 'sw_translations.json'\n    }"
)
ud_code = ud_code.replace(
    "item['BentukKataHA'] = b_labels.get('ha', b)",
    "item['BentukKataHA'] = b_labels.get('ha', b)\n        item['BentukKataSW'] = b_labels.get('sw', b)"
)
ud_code = ud_code.replace(
    "item['SuratArtiHA'] = s_info.get('arti_ha', s_info['arti_en'])",
    "item['SuratArtiHA'] = s_info.get('arti_ha', s_info['arti_en'])\n            item['SuratArtiSW'] = s_info.get('arti_sw', s_info['arti_en'])"
)
ud_code = ud_code.replace(
    "item['ArtiKataHA'] = gm.get('arti_ha', item['Arti kata'])",
    "item['ArtiKataHA'] = gm.get('arti_ha', item['Arti kata'])\n        item['ArtiKataSW'] = gm.get('arti_sw', item['Arti kata'])"
)
ud_code = ud_code.replace(
    "item['TeksArtiHA'] = caches['ha'].get(v_key, teks_id)",
    "item['TeksArtiHA'] = caches['ha'].get(v_key, teks_id)\n        item['TeksArtiSW'] = caches['sw'].get(v_key, teks_id)"
)
ud_code = ud_code.replace(
    "langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN', 'RU', 'ZH', 'ES', 'TR', 'PT', 'HA']",
    "langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN', 'RU', 'ZH', 'ES', 'TR', 'PT', 'HA', 'SW']"
)

with open(os.path.join(BASE_DIR, 'update_data.py'), 'w', encoding='utf-8') as f:
    f.write(ud_code)
print("update_data.py updated!")

# 2. Update fetch_all_multilingual.py
print("Updating fetch_all_multilingual.py...")
with open(os.path.join(BASE_DIR, 'fetch_all_multilingual.py'), 'r', encoding='utf-8') as f:
    fam_code = f.read()

fam_code = fam_code.replace(
    "'ha': ('ha_translations.json', 'ha.gumi')\n}",
    "'ha': ('ha_translations.json', 'ha.gumi'),\n    'sw': ('sw_translations.json', 'sw.barwani')\n}"
)
with open(os.path.join(BASE_DIR, 'fetch_all_multilingual.py'), 'w', encoding='utf-8') as f:
    f.write(fam_code)
print("fetch_all_multilingual.py updated!")

# 3. Update PANDUAN_UPDATE_DATA.md
print("Updating PANDUAN_UPDATE_DATA.md...")
with open(os.path.join(BASE_DIR, 'PANDUAN_UPDATE_DATA.md'), 'r', encoding='utf-8') as f:
    p_code = f.read()

p_code = p_code.replace(
    "14 Bahasa dunia (ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT, HA)",
    "15 Bahasa dunia (ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT, HA, SW)"
)
p_code = p_code.replace(
    "## 📁 Struktur File Hasil Update & Cache 14 Bahasa",
    "## 📁 Struktur File Hasil Update & Cache 15 Bahasa"
)
if "sw_translations.json" not in p_code:
    p_code = p_code.replace(
        "| **`ha_translations.json`** | Terjemahan Bahasa Hausa (Sheikh Abubakar Mahmoud Gumi). |",
        "| **`ha_translations.json`** | Terjemahan Bahasa Hausa (Sheikh Abubakar Mahmoud Gumi). |\n| **`sw_translations.json`** | Terjemahan Bahasa Swahili / Kiswahili (Sheikh Ali Muhsin Al-Barwani). |"
    )

with open(os.path.join(BASE_DIR, 'PANDUAN_UPDATE_DATA.md'), 'w', encoding='utf-8') as f:
    f.write(p_code)
print("PANDUAN_UPDATE_DATA.md updated!")

# Re-run build_swahili_dataset to ensure 100% data completeness
from build_swahili_dataset import enrich_dhamir_data, enrich_harf_data
enrich_dhamir_data()
enrich_harf_data()

print("\nAll files synchronized successfully!")
