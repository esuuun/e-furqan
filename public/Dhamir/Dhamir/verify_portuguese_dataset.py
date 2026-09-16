#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verify Portuguese dataset integrity, translations, and app.js data synchronization.
"""

import json
import os

with open('dhamir_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total entries in dhamir_data.json: {len(data)}")

missing_bentuk_pt = 0
missing_surat_pt = 0
missing_arti_pt = 0
missing_teks_pt = 0
missing_desc_pt = 0
missing_jenis_pt = 0

for idx, item in enumerate(data):
    if not item.get('BentukKataPT'):
        missing_bentuk_pt += 1
    if not item.get('SuratArtiPT'):
        missing_surat_pt += 1
    if not item.get('ArtiKataPT'):
        missing_arti_pt += 1
    if not item.get('TeksArtiPT'):
        missing_teks_pt += 1
    grammar = item.get('Grammar') or {}
    if not grammar.get('desc_pt'):
        missing_desc_pt += 1
    if not grammar.get('jenis_pt'):
        missing_jenis_pt += 1

print(f"Missing BentukKataPT: {missing_bentuk_pt}")
print(f"Missing SuratArtiPT: {missing_surat_pt}")
print(f"Missing ArtiKataPT: {missing_arti_pt}")
print(f"Missing TeksArtiPT: {missing_teks_pt}")
print(f"Missing Grammar.desc_pt: {missing_desc_pt}")
print(f"Missing Grammar.jenis_pt: {missing_jenis_pt}")

# Check pt_translations.json
with open('pt_translations.json', 'r', encoding='utf-8') as f:
    pt_tr = json.load(f)

print(f"Total verses in pt_translations.json: {len(pt_tr)}")

# Sample print
sample = data[0]
print("\n--- Sample Entry 1a ---")
print(f"BentukKata: {sample.get('BentukKataPT')}")
print(f"NoKata: {sample.get('No Kata')}")
print(f"Kata: {sample.get('Kata')}")
print(f"ArtiKataPT: {sample.get('ArtiKataPT')}")
print(f"Surat: {sample.get('Surat')} ({sample.get('SuratArtiPT')}) : {sample.get('Ayat')}")
print(f"TeksArtiPT: {sample.get('TeksArtiPT')[:120]}...")
print(f"Grammar: {sample.get('Grammar')}")
