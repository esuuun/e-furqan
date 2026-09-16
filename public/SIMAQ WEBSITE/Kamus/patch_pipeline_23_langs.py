#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Patch update_data.py and build_harf_dataset.py for 23 Languages (ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT, HA, SW, FA, JA, KO, NL, IT, BS, SQ, TH).
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Patch update_data.py
ud_file = os.path.join(BASE_DIR, 'update_data.py')
with open(ud_file, 'r', encoding='utf-8') as f:
    ud = f.read()

ud = ud.replace("from build_arabic_thai_dataset import ARABIC_SURAHS, BENTUK_KATA_AR, ARABIC_GRAMMAR, THAI_SURAHS, BENTUK_KATA_TH, THAI_GRAMMAR", "from build_thai_dataset import THAI_SURAHS, BENTUK_KATA_TH, THAI_GRAMMAR")
ud = ud.replace("'ar': {},\n        'th': {}", "'th': {}")
ud = ud.replace("'ar': 'ar_translations.json',\n        'th': 'th_translations.json'", "'th': 'th_translations.json'")
ud = ud.replace("        item['BentukKataAR'] = BENTUK_KATA_AR.get(b, b)\n", "")
ud = ud.replace("        item['SuratArtiAR'] = ARABIC_SURAHS.get(str(s), item['SuratArab'])\n", "")
ud = ud.replace("        gm_ar = ARABIC_GRAMMAR.get(meta_key, {})\n", "")
ud = ud.replace("        if gm_ar.get('desc_ar'): gm['desc_ar'] = gm_ar['desc_ar']\n        if gm_ar.get('jenis_ar'): gm['jenis_ar'] = gm_ar['jenis_ar']\n", "")
ud = ud.replace("        item['ArtiKataAR'] = gm_ar.get('arti_ar', item['Kata'])\n", "")
ud = ud.replace("        item['TeksArtiAR'] = caches['ar'].get(v_key, item['TeksArab'])\n", "")

with open(ud_file, 'w', encoding='utf-8') as f:
    f.write(ud)
print("Updated update_data.py for 23 languages.")

# 2. Patch build_harf_dataset.py
hf_file = os.path.join(BASE_DIR, 'build_harf_dataset.py')
with open(hf_file, 'r', encoding='utf-8') as f:
    hf = f.read()

hf = hf.replace("from build_arabic_thai_dataset import ARABIC_SURAHS, BENTUK_HARF_AR, ARABIC_HARF_GRAMMAR, THAI_SURAHS, BENTUK_HARF_TH, THAI_HARF_GRAMMAR", "from build_thai_dataset import THAI_SURAHS, BENTUK_HARF_TH, THAI_HARF_GRAMMAR")
hf = hf.replace("'ar': {},\n        'th': {}", "'th': {}")
hf = hf.replace("'ar': 'ar_translations.json',\n        'th': 'th_translations.json'", "'th': 'th_translations.json'")
hf = hf.replace("        item['BentukKataAR'] = BENTUK_HARF_AR.get(b, b)\n", "")
hf = hf.replace("        item['SuratArtiAR'] = ARABIC_SURAHS.get(str(s), item['SuratArab'])\n", "")
hf = hf.replace("        gm_ar = ARABIC_HARF_GRAMMAR.get(meta_key, {})\n", "")
hf = hf.replace("        item['ArtiKataAR'] = gm_ar.get('arti_ar', item['Kata'])\n", "")
hf = hf.replace("        if gm_ar.get('desc_ar'): item['Grammar']['desc_ar'] = gm_ar['desc_ar']\n        if gm_ar.get('jenis_ar'): item['Grammar']['jenis_ar'] = gm_ar['jenis_ar']\n", "")
hf = hf.replace("        item['TeksArtiAR'] = caches['ar'].get(v_key, item['TeksArab'])\n", "")
hf = hf.replace("        if b_k in BENTUK_HARF_AR: b_obj['ar'] = BENTUK_HARF_AR[b_k]\n", "")

with open(hf_file, 'w', encoding='utf-8') as f:
    f.write(hf)
print("Updated build_harf_dataset.py for 23 languages.")
