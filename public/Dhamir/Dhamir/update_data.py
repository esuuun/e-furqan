#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
SCRIPT PEMBARUAN DATA INTERAKTIF KAMUS JAMID MABNY AL-QUR'AN (8 BAHASA)
================================================================================
Mendukung 7 Kategori Bentuk Kata:
  1. Dhamir (Kata Ganti)
  2. Mawshul (Kata Sambung)
  3. Istifham (Kata Tanya)
  4. Syarath (Kata Syarat)
  5. Isyarah (Kata Tunjuk)
  6. Isim Fi'il (Kata Benda Makna Perbuatan)
  7. Fi'il Jamid (Kata Kerja Statis / Kaku)

Dan 8 Bahasa Terjemahan:
  - Bangla (Maulana Muhiuddin Khan)
  - Bahasa Indonesia (Kementerian Agama RI)
  - English (Sahih International)
  - Bahasa Melayu (Syeikh Abdullah Basmeih / JAKIM)
  - Français (Muhammad Hamidullah)
  - Deutsch (Frank Bubenheim & Nadeem Elyas)
  - Urdu (Maulana Fateh Muhammad Jalandhry)
  - Hindi (Dr. Suhel Farooq Khan & Dr. Saifur Rahman Nadwi)
================================================================================
"""

import os
import sys
import json
import time
import argparse
import urllib.request
import urllib.error
import re
from collections import defaultdict

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

try:
    import openpyxl
except ImportError:
    print("[ERROR] Modul 'openpyxl' belum terpasang.")
    print("Silakan pasang dengan menjalankan: pip install openpyxl")
    sys.exit(1)

from build_multilingual_dataset import SURAHS, GRAMMATICAL_METADATA, BENTUK_LABELS, BASE_DIR
from build_hausa_dataset import HAUSA_SURAHS, BENTUK_KATA_HA, HAUSA_GRAMMAR
from build_swahili_dataset import SWAHILI_SURAHS, BENTUK_KATA_SW, SWAHILI_GRAMMAR
from build_persian_dataset import PERSIAN_SURAHS, BENTUK_KATA_FA, PERSIAN_GRAMMAR
from build_japanese_dataset import JAPANESE_SURAHS, BENTUK_KATA_JA, JAPANESE_GRAMMAR
from build_korean_dataset import KOREAN_SURAHS, BENTUK_KATA_KO, KOREAN_GRAMMAR
from build_dutch_dataset import DUTCH_SURAHS, BENTUK_KATA_NL, DUTCH_GRAMMAR
from build_italian_dataset import ITALIAN_SURAHS, BENTUK_KATA_IT, ITALIAN_GRAMMAR
from build_bosnian_dataset import BOSNIAN_SURAHS, BENTUK_KATA_BS, BOSNIAN_GRAMMAR
from build_albanian_dataset import ALBANIAN_SURAHS, BENTUK_KATA_SQ, ALBANIAN_GRAMMAR
from build_thai_dataset import THAI_SURAHS, BENTUK_KATA_TH, THAI_GRAMMAR
from build_amazigh_amharic_dataset import AMAZIGH_SURAHS, BENTUK_KATA_BER, AMAZIGH_GRAMMAR, AMHARIC_SURAHS, BENTUK_KATA_AM, AMHARIC_GRAMMAR
from build_azerbaijani_bulgarian_dataset import AZERBAIJANI_SURAHS, BENTUK_KATA_AZ, AZERBAIJANI_GRAMMAR, BULGARIAN_SURAHS, BENTUK_KATA_BG, BULGARIAN_GRAMMAR
from build_czech_dhivehi_dataset import CZECH_SURAHS, BENTUK_KATA_CS, CZECH_GRAMMAR, DHIVEHI_SURAHS, BENTUK_KATA_DV, DHIVEHI_GRAMMAR
from build_norwegian_polish_dataset import NORWEGIAN_SURAHS, BENTUK_KATA_NO, NORWEGIAN_GRAMMAR, POLISH_SURAHS, BENTUK_KATA_PL, POLISH_GRAMMAR
from build_romanian_swedish_dataset import ROMANIAN_SURAHS, BENTUK_KATA_RO, ROMANIAN_GRAMMAR, SWEDISH_SURAHS, BENTUK_KATA_SV, SWEDISH_GRAMMAR
from build_tajik_tamil_dataset import TAJIK_SURAHS, BENTUK_KATA_TG, TAJIK_GRAMMAR, TAMIL_SURAHS, BENTUK_KATA_TA, TAMIL_GRAMMAR
from build_4_languages_dataset import TATAR_SURAHS, BENTUK_KATA_TT, TATAR_GRAMMAR, UYGHUR_SURAHS, BENTUK_KATA_UG, UZBEK_SURAHS, BENTUK_KATA_UZ, KURDISH_SURAHS, BENTUK_KATA_KU

def load_all_caches():
    caches = {
        'verse': {},
        'en': {},
        'ms': {},
        'fr': {},
        'de': {},
        'ur': {},
        'hi': {},
        'bn': {},
        'ru': {},
        'zh': {},
        'es': {},
        'tr': {},
        'pt': {},
        'ha': {},
        'sw': {},
        'fa': {},
        'ja': {},
        'ko': {},
        'nl': {},
        'it': {},
        'bs': {},
        'sq': {},
        'th': {},
        'ber': {},
        'am': {},
        'az': {},
        'bg': {},
        'cs': {},
        'dv': {},
        'no': {},
        'pl': {},
        'ro': {},
        'sv': {},
        'tg': {},
        'ta': {},
        'tt': {},
        'ug': {},
        'uz': {},
        'ku': {}
    }
    
    files = {
        'verse': 'verse_cache.json',
        'en': 'en_translations.json',
        'ms': 'ms_translations.json',
        'fr': 'fr_translations.json',
        'de': 'de_translations.json',
        'ur': 'ur_translations.json',
        'hi': 'hi_translations.json',
        'bn': 'bn_translations.json',
        'ru': 'ru_translations.json',
        'zh': 'zh_translations.json',
        'es': 'es_translations.json',
        'tr': 'tr_translations.json',
        'pt': 'pt_translations.json',
        'ha': 'ha_translations.json',
        'sw': 'sw_translations.json',
        'fa': 'fa_translations.json',
        'ja': 'ja_translations.json',
        'ko': 'ko_translations.json',
        'nl': 'nl_translations.json',
        'it': 'it_translations.json',
        'bs': 'bs_translations.json',
        'sq': 'sq_translations.json',
        'th': 'th_translations.json',
        'ber': 'ber_translations.json',
        'am': 'am_translations.json',
        'az': 'az_translations.json',
        'bg': 'bg_translations.json',
        'cs': 'cs_translations.json',
        'dv': 'dv_translations.json',
        'no': 'no_translations.json',
        'pl': 'pl_translations.json',
        'ro': 'ro_translations.json',
        'sv': 'sv_translations.json',
        'tg': 'tg_translations.json',
        'ta': 'ta_translations.json',
        'tt': 'tt_translations.json',
        'ug': 'ug_translations.json',
        'uz': 'uz_translations.json',
        'ku': 'ku_translations.json'
    }

    for key, fname in files.items():
        fpath = os.path.join(BASE_DIR, fname)
        if os.path.exists(fpath):
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    caches[key] = json.load(f)
            except Exception as e:
                print(f"[WARN] Gagal membaca {fname}: {e}")
                
    return caches


def save_caches(caches):
    files = {
        'verse': 'verse_cache.json',
        'en': 'en_translations.json',
        'ms': 'ms_translations.json',
        'fr': 'fr_translations.json',
        'de': 'de_translations.json',
        'ur': 'ur_translations.json',
        'hi': 'hi_translations.json',
        'bn': 'bn_translations.json',
        'ru': 'ru_translations.json',
        'zh': 'zh_translations.json',
        'es': 'es_translations.json',
        'tr': 'tr_translations.json',
        'pt': 'pt_translations.json',
        'ha': 'ha_translations.json',
        'sw': 'sw_translations.json',
        'fa': 'fa_translations.json',
        'ja': 'ja_translations.json',
        'ko': 'ko_translations.json',
        'nl': 'nl_translations.json',
        'it': 'it_translations.json',
        'bs': 'bs_translations.json',
        'sq': 'sq_translations.json',
        'th': 'th_translations.json',
        'ber': 'ber_translations.json',
        'am': 'am_translations.json',
        'az': 'az_translations.json',
        'bg': 'bg_translations.json',
        'cs': 'cs_translations.json',
        'dv': 'dv_translations.json',
        'no': 'no_translations.json',
        'pl': 'pl_translations.json',
        'ro': 'ro_translations.json',
        'sv': 'sv_translations.json',
        'tg': 'tg_translations.json',
        'ta': 'ta_translations.json',
        'tt': 'tt_translations.json',
        'ug': 'ug_translations.json',
        'uz': 'uz_translations.json',
        'ku': 'ku_translations.json'
    }
    for key, fname in files.items():
        try:
            with open(os.path.join(BASE_DIR, fname), 'w', encoding='utf-8') as f:
                json.dump(caches[key], f, ensure_ascii=False, indent=2)
        except Exception:
            pass


def find_excel_file(specified_path=None):
    if specified_path:
        full_path = os.path.abspath(specified_path)
        if os.path.exists(full_path):
            return full_path
        alt_path = os.path.join(BASE_DIR, specified_path)
        if os.path.exists(alt_path):
            return alt_path
        print(f"[ERROR] File Excel tidak ditemukan: {specified_path}")
        sys.exit(1)

    candidates = [
        'Kamus Jamid Mabny.xlsx',
        'DHAMIR and Mawshul.xlsx',
        'DHAMIR copy.xlsx',
        'DHAMIR_Interaktif.xlsx',
        'MAWSHUL - Copy.xlsx',
        'DHAMIR.xlsx'
    ]

    for fname in candidates:
        fpath = os.path.join(BASE_DIR, fname)
        if os.path.exists(fpath):
            return fpath

    for fname in os.listdir(BASE_DIR):
        if fname.endswith('.xlsx') and not fname.startswith('~$'):
            return os.path.join(BASE_DIR, fname)

    print("[ERROR] Tidak ditemukan file Excel (.xlsx) di folder kerja!")
    sys.exit(1)


def read_excel_data(excel_path, sheet_name=None):
    print(f"\n[1/4] Membuka file Excel: {os.path.basename(excel_path)}")
    wb = openpyxl.load_workbook(excel_path, data_only=True)
    
    if sheet_name and sheet_name in wb.sheetnames:
        sheet = wb[sheet_name]
    elif 'KAMUS KATA' in wb.sheetnames:
        sheet = wb['KAMUS KATA']
    elif 'Data Master' in wb.sheetnames:
        sheet = wb['Data Master']
    elif 'Sheet1' in wb.sheetnames:
        sheet = wb['Sheet1']
    else:
        sheet = wb.active

    print(f"      Sheet yang digunakan: '{sheet.title}'")
    rows = list(sheet.iter_rows(values_only=True))
    if not rows:
        print("[ERROR] Sheet kosong!")
        sys.exit(1)

    header = [str(c).strip() if c is not None else '' for c in rows[0]]
    data_rows = []

    for r_idx, r in enumerate(rows[1:], start=2):
        if not any(r): continue
        item = dict(zip(header, r))

        b = str(item.get('Bentuk Kata', '')).strip()
        nk = str(item.get('No kata', '')).strip()
        k = str(item.get('Kata', '')).strip()
        ak = str(item.get('Arti kata', '')).strip()
        fk = item.get('Frek kata')
        surat_val = item.get('SURAT')
        ayat_val = item.get('AYAT')

        if not b or not nk or surat_val is None or ayat_val is None:
            continue

        try:
            if str(surat_val).strip().upper() == 'K':
                s_int = 30
            else:
                s_int = int(surat_val)
            a_int = int(ayat_val)
        except (ValueError, TypeError):
            continue

        data_rows.append({
            'Bentuk Kata': b,
            'No kata': nk,
            'Kata': k,
            'Arti kata': ak,
            'Frek kata': fk,
            'SURAT': s_int,
            'AYAT': a_int
        })

    wb.close()
    print(f"      Berhasil membaca {len(data_rows)} baris data valid dari Excel.")
    return data_rows


def filter_shortest_verses(data_list, caches, max_per_word=5):
    if max_per_word is None or max_per_word <= 0:
        return data_list

    groups = defaultdict(list)
    seen_refs = set()

    for item in data_list:
        b = item['Bentuk Kata']
        nk = item['No kata']
        s = item['SURAT']
        a = item['AYAT']

        ref_key = (b, nk, s, a)
        if ref_key in seen_refs:
            continue
        seen_refs.add(ref_key)

        v_key = f"{s}:{a}"
        t_arab = caches['verse'].get(v_key, {}).get('TeksArab', '')
        item['arab_len'] = len(t_arab.strip()) if t_arab else 9999
        groups[(b, nk)].append(item)

    filtered_list = []
    for key in sorted(groups.keys()):
        items = groups[key]
        sorted_items = sorted(items, key=lambda x: (x['arab_len'], x['SURAT'], x['AYAT']))
        filtered_list.extend(sorted_items[:max_per_word])

    print(f"\n[2/4] Filter {max_per_word} Ayat Terpendek per Kata (Hasil: {len(filtered_list)} ayat dari {len(groups)} kata unik).")
    return filtered_list


def process_and_enrich(filtered_data, caches):
    print(f"\n[3/4] Mengayakan data ke 7 bahasa (ID, EN, MS, FR, DE, UR, HI)...")
    enriched_list = []

    for item in filtered_data:
        b = item['Bentuk Kata']
        nk = item['No kata']
        s = item['SURAT']
        a = item['AYAT']
        v_key = f"{s}:{a}"

        # 1. Bentuk Kata Labels
        b_labels = BENTUK_LABELS.get(b, {})
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
        item['BentukKataES'] = b_labels.get('es', b)
        item['BentukKataTR'] = b_labels.get('tr', b)
        item['BentukKataPT'] = b_labels.get('pt', b)
        item['BentukKataHA'] = b_labels.get('ha', b)
        item['BentukKataSW'] = b_labels.get('sw', b)
        item['BentukKataFA'] = b_labels.get('fa', b)
        item['BentukKataJA'] = BENTUK_KATA_JA.get(b, b)
        item['BentukKataKO'] = BENTUK_KATA_KO.get(b, b)
        item['BentukKataNL'] = BENTUK_KATA_NL.get(b, b)
        item['BentukKataIT'] = BENTUK_KATA_IT.get(b, b)
        item['BentukKataBS'] = BENTUK_KATA_BS.get(b, b)
        item['BentukKataSQ'] = BENTUK_KATA_SQ.get(b, b)
        item['BentukKataTH'] = BENTUK_KATA_TH.get(b, b)
        item['BentukKataBER'] = BENTUK_KATA_BER.get(b, b)
        item['BentukKataAM'] = BENTUK_KATA_AM.get(b, b)
        item['BentukKataAZ'] = BENTUK_KATA_AZ.get(b, b)
        item['BentukKataBG'] = BENTUK_KATA_BG.get(b, b)

        # 2. Surat Info
        s_key = str(s)
        if s_key in SURAHS or s in SURAHS:
            s_info = SURAHS.get(s_key, SURAHS.get(s, {}))
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
            item['SuratArtiES'] = s_info.get('arti_es', s_info['arti_en'])
            item['SuratArtiTR'] = s_info.get('arti_tr', s_info['arti_en'])
            item['SuratArtiPT'] = s_info.get('arti_pt', s_info['arti_en'])
            item['SuratArtiHA'] = s_info.get('arti_ha', s_info['arti_en'])
            item['SuratArtiSW'] = s_info.get('arti_sw', s_info['arti_en'])
            item['SuratArtiFA'] = s_info.get('arti_fa', s_info['arti_en'])
            item['SuratArtiJA'] = JAPANESE_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiKO'] = KOREAN_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiNL'] = DUTCH_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiIT'] = ITALIAN_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiBS'] = BOSNIAN_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiSQ'] = ALBANIAN_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiTH'] = THAI_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiBER'] = AMAZIGH_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiAM'] = AMHARIC_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiAZ'] = AZERBAIJANI_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiBG'] = BULGARIAN_SURAHS.get(str(s), s_info.get('arti_en', ''))
        else:
            item['SuratNama'] = f"Surat {s}"
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
            item['SuratArtiES'] = ""
            item['SuratArtiTR'] = ""
            item['SuratArtiPT'] = ""
            item['SuratArtiHA'] = ""
            item['SuratArtiSW'] = ""
            item['SuratArtiFA'] = ""
            item['SuratArtiJA'] = ""
            item['SuratArtiKO'] = ""
            item['SuratArtiNL'] = ""
            item['SuratArtiIT'] = ""
            item['SuratArtiBS'] = ""
            item['SuratArtiSQ'] = ""
            item['SuratArtiTH'] = ""
            item['SuratArtiBER'] = ""
            item['SuratArtiAM'] = ""
            item['SuratArtiAZ'] = ""
            item['SuratArtiBG'] = ""

        # 3. Grammar & Word Meaning Metadata
        meta_key = f"{b}__{nk}"
        gm = dict(GRAMMATICAL_METADATA.get(meta_key, GRAMMATICAL_METADATA.get(nk, {})))
        gm_ha = HAUSA_GRAMMAR.get(meta_key, {})
        gm_sw = SWAHILI_GRAMMAR.get(meta_key, {})
        gm_fa = PERSIAN_GRAMMAR.get(meta_key, {})
        gm_ja = JAPANESE_GRAMMAR.get(meta_key, {})
        gm_ko = KOREAN_GRAMMAR.get(meta_key, {})
        gm_nl = DUTCH_GRAMMAR.get(meta_key, {})
        gm_it = ITALIAN_GRAMMAR.get(meta_key, {})
        gm_bs = BOSNIAN_GRAMMAR.get(meta_key, {})
        gm_sq = ALBANIAN_GRAMMAR.get(meta_key, {})
        gm_th = THAI_GRAMMAR.get(meta_key, {})
        gm_ber = AMAZIGH_GRAMMAR.get(meta_key, {})
        gm_am = AMHARIC_GRAMMAR.get(meta_key, {})
        gm_az = AZERBAIJANI_GRAMMAR.get(meta_key, {})
        gm_bg = BULGARIAN_GRAMMAR.get(meta_key, {})
        if gm_ha.get('desc_ha'): gm['desc_ha'] = gm_ha['desc_ha']
        if gm_ha.get('jenis_ha'): gm['jenis_ha'] = gm_ha['jenis_ha']
        if gm_sw.get('desc_sw'): gm['desc_sw'] = gm_sw['desc_sw']
        if gm_sw.get('jenis_sw'): gm['jenis_sw'] = gm_sw['jenis_sw']
        if gm_fa.get('desc_fa'): gm['desc_fa'] = gm_fa['desc_fa']
        if gm_fa.get('jenis_fa'): gm['jenis_fa'] = gm_fa['jenis_fa']
        if gm_ja.get('desc_ja'): gm['desc_ja'] = gm_ja['desc_ja']
        if gm_ja.get('jenis_ja'): gm['jenis_ja'] = gm_ja['jenis_ja']
        if gm_ko.get('desc_ko'): gm['desc_ko'] = gm_ko['desc_ko']
        if gm_ko.get('jenis_ko'): gm['jenis_ko'] = gm_ko['jenis_ko']
        if gm_nl.get('desc_nl'): gm['desc_nl'] = gm_nl['desc_nl']
        if gm_nl.get('jenis_nl'): gm['jenis_nl'] = gm_nl['jenis_nl']
        if gm_it.get('desc_it'): gm['desc_it'] = gm_it['desc_it']
        if gm_it.get('jenis_it'): gm['jenis_it'] = gm_it['jenis_it']
        if gm_bs.get('desc_bs'): gm['desc_bs'] = gm_bs['desc_bs']
        if gm_bs.get('jenis_bs'): gm['jenis_bs'] = gm_bs['jenis_bs']
        if gm_sq.get('desc_sq'): gm['desc_sq'] = gm_sq['desc_sq']
        if gm_sq.get('jenis_sq'): gm['jenis_sq'] = gm_sq['jenis_sq']
        if gm_th.get('desc_th'): gm['desc_th'] = gm_th['desc_th']
        if gm_th.get('jenis_th'): gm['jenis_th'] = gm_th['jenis_th']
        if gm_ber.get('desc_ber'): gm['desc_ber'] = gm_ber['desc_ber']
        if gm_ber.get('jenis_ber'): gm['jenis_ber'] = gm_ber['jenis_ber']
        if gm_am.get('desc_am'): gm['desc_am'] = gm_am['desc_am']
        if gm_am.get('jenis_am'): gm['jenis_am'] = gm_am['jenis_am']
        if gm_az.get('desc_az'): gm['desc_az'] = gm_az['desc_az']
        if gm_az.get('jenis_az'): gm['jenis_az'] = gm_az['jenis_az']
        if gm_bg.get('desc_bg'): gm['desc_bg'] = gm_bg['desc_bg']
        if gm_bg.get('jenis_bg'): gm['jenis_bg'] = gm_bg['jenis_bg']
        
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
        item['ArtiKataES'] = gm.get('arti_es', item['Arti kata'])
        item['ArtiKataTR'] = gm.get('arti_tr', item['Arti kata'])
        item['ArtiKataPT'] = gm.get('arti_pt', item['Arti kata'])
        item['ArtiKataHA'] = gm_ha.get('arti_ha', gm.get('arti_ha', item['Arti kata']))
        item['ArtiKataSW'] = gm_sw.get('arti_sw', gm.get('arti_sw', item['Arti kata']))
        item['ArtiKataFA'] = gm_fa.get('arti_fa', gm.get('arti_fa', item['Arti kata']))
        item['ArtiKataJA'] = gm_ja.get('arti_ja', gm.get('arti_ja', item['Arti kata']))
        item['ArtiKataKO'] = gm_ko.get('arti_ko', gm.get('arti_ko', item['Arti kata']))
        item['ArtiKataNL'] = gm_nl.get('arti_nl', item['Arti kata'])
        item['ArtiKataIT'] = gm_it.get('arti_it', item['Arti kata'])
        item['ArtiKataBS'] = gm_bs.get('arti_bs', item['Arti kata'])
        item['ArtiKataSQ'] = gm_sq.get('arti_sq', item['Arti kata'])
        item['ArtiKataTH'] = gm_th.get('arti_th', item['Arti kata'])
        item['ArtiKataBER'] = gm_ber.get('arti_ber', item['ArtiKataEN'])
        item['ArtiKataAM'] = gm_am.get('arti_am', item['ArtiKataEN'])
        item['ArtiKataAZ'] = gm_az.get('arti_az', item['ArtiKataEN'])
        item['ArtiKataBG'] = gm_bg.get('arti_bg', item['ArtiKataEN'])

        # 4. Verse Data
        v_data = caches['verse'].get(v_key, {})
        item['TeksArab'] = v_data.get('TeksArab', '')
        item['TeksLatin'] = v_data.get('TeksLatin', '')
        
        teks_id = v_data.get('TeksArtiID', v_data.get('TeksArti', ''))
        item['TeksArti'] = teks_id
        item['TeksArtiID'] = teks_id
        item['TeksArtiEN'] = caches['en'].get(v_key, teks_id)
        item['TeksArtiMS'] = caches['ms'].get(v_key, teks_id)
        item['TeksArtiFR'] = caches['fr'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiDE'] = caches['de'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiUR'] = caches['ur'].get(v_key, teks_id)
        item['TeksArtiHI'] = caches['hi'].get(v_key, teks_id)
        item['TeksArtiBN'] = caches['bn'].get(v_key, teks_id)
        item['TeksArtiRU'] = caches['ru'].get(v_key, teks_id)
        item['TeksArtiZH'] = caches['zh'].get(v_key, teks_id)
        item['TeksArtiES'] = caches['es'].get(v_key, teks_id)
        item['TeksArtiTR'] = caches['tr'].get(v_key, teks_id)
        item['TeksArtiPT'] = caches['pt'].get(v_key, teks_id)
        item['TeksArtiHA'] = caches['ha'].get(v_key, teks_id)
        item['TeksArtiSW'] = caches['sw'].get(v_key, teks_id)
        item['TeksArtiFA'] = caches['fa'].get(v_key, teks_id)
        item['TeksArtiJA'] = caches['ja'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiKO'] = caches['ko'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiNL'] = caches['nl'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiIT'] = caches['it'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiBS'] = caches['bs'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiSQ'] = caches['sq'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiTH'] = caches['th'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiBER'] = caches['ber'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiAM'] = caches['am'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiAZ'] = caches['az'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiBG'] = caches['bg'].get(v_key, item['TeksArtiEN'])
        item['AudioUrl'] = v_data.get('AudioUrl', f"https://everyayah.com/data/Alafasy_128kbps/{str(s).zfill(3)}{str(a).zfill(3)}.mp3")

        item.pop('arab_len', None)
        enriched_list.append(item)

    return enriched_list


def export_files(enriched_list):
    print(f"\n[4/4] Mengekspor database aplikasi...")
    json_path = os.path.join(BASE_DIR, 'dhamir_data.json')
    js_path = os.path.join(BASE_DIR, 'dhamir_data.js')

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(enriched_list, f, ensure_ascii=False, indent=2)
    print(f"      [OK] dhamir_data.json ({len(enriched_list)} entri, {round(os.path.getsize(json_path)/1024, 1)} KB)")

    js_content = f"""/**
 * ==============================================================================
 * KAMUS JAMID MABNY AL-QUR'AN (MULTILINGUAL: 22 BAHASA)
 * ==============================================================================
 * File ini digenerate secara otomatis oleh update_data.py
 * Waktu Pembaruan: {time.strftime('%Y-%m-%d %H:%M:%S')}
 * Total Entri: {len(enriched_list)} baris
 * 22 Bahasa: ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT, HA, SW, FA, JA, KO, NL, IT, BS, SQ
 * Sumber: Dataset Kamus Jamid Mabny, Kemenag RI, Sahih International, Basmeih, Hamidullah, Bubenheim, Jalandhry, Farooq, Muhiuddin Khan, Elmir Kuliev, Muhammad Makin, Muhammad Isa García, Türkiye Diyanet Vakfı, Samir El-Hayek, Gumi, Barwani, Makarem Shirazi, Ryoichi Mita, Hamid Choi, Sofian S. Siregar, Hamza Roberto Piccardo, Besim Korkut, Sherif Ahmeti & EveryAyah
 * ==============================================================================
 */

const DHAMIR_DATA = {json.dumps(enriched_list, ensure_ascii=False, indent=2)};

const SURAH_DICT = {json.dumps(SURAHS, ensure_ascii=False, indent=2)};

const GRAMMAR_INFO = {json.dumps(GRAMMATICAL_METADATA, ensure_ascii=False, indent=2)};
"""
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"      [OK] dhamir_data.js ({round(os.path.getsize(js_path)/1024, 1)} KB)")


def print_stats(enriched_list):
    bentuks = sorted(list(set(d['Bentuk Kata'] for d in enriched_list)))
    print("\n" + "=" * 65)
    print("RINGKASAN STATISTIK PEMBARUAN DATA:")
    print("=" * 65)
    print(f"  • Total Rujukan Ayat : {len(enriched_list)} ayat")
    print(f"  • Jumlah Kategori    : {len(bentuks)} Bentuk Kata")
    for b in bentuks:
        b_items = [d for d in enriched_list if d['Bentuk Kata'] == b]
        b_words = sorted(list(set(d['No kata'] for d in b_items)))
        print(f"    - {b:<15} : {len(b_words)} kata ({len(b_items)} contoh ayat)")
    
    langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN', 'RU', 'ZH', 'ES', 'TR', 'PT', 'HA', 'SW', 'FA', 'JA', 'KO', 'NL', 'IT', 'BS', 'SQ']
    print(f"\n  • Kelengkapan Terjemahan {len(langs)} Bahasa:")
    for lang in langs:
        c = sum(1 for d in enriched_list if d.get(f'TeksArti{lang}'))
        pct = round((c / len(enriched_list)) * 100, 1) if enriched_list else 0
        print(f"    - {lang:<3} : {c} / {len(enriched_list)} ayat ({pct}%)")

    print("=" * 65)
    print("STATUS: DATA SUDAH BERHASIL DIPROSES & SIAP DIGUNAKAN DI INDEX.HTML!\n")


def update_harf_data(excel_path=None, limit=5):
    print("\n" + "=" * 65)
    print("   MEMPROSES KAMUS HARF GHAIR 'AMIL (39 BAHASA & 17 KATEGORI)    ")
    print("=" * 65)
    from build_harf_dataset import main as run_harf_build
    run_harf_build()


def update_harf_amil_data(excel_path=None, limit=5):
    print("\n" + "=" * 65)
    print("   MEMPROSES KAMUS HARF 'AMIL (39 BAHASA & 6 KATEGORI)           ")
    print("=" * 65)
    from build_harf_amil_dataset import main as run_harf_amil_build
    run_harf_amil_build()


def update_musytaq_data(excel_path=None):
    print("\n" + "=" * 65)
    print("   MEMPROSES KAMUS MUSYTAQ (80 AKAR KATA & 3.012 TASRIF)         ")
    print("=" * 65)
    from build_musytaq_dataset import build_musytaq_data
    build_musytaq_data()


def main():
    parser = argparse.ArgumentParser(description="Pembaruan Data Kamus Al-Qur'an (Jamid Mabny, Harf Ghair 'Amil, Harf 'Amil & Musytaq Multilingual).")
    parser.add_argument('-d', '--dict', choices=['all', 'jamid', 'harf', 'harf_amil', 'musytaq'], default='all', help="Pilih kamus yang ingin diperbarui: all, jamid, harf, harf_amil, musytaq (default: all)")
    parser.add_argument('-e', '--excel', help="Path file Excel sumber (.xlsx)", default=None)
    parser.add_argument('-s', '--sheet', help="Nama Sheet di file Excel", default=None)
    parser.add_argument('-l', '--limit', type=int, help="Batasi contoh ayat per nomor kata (default: 5)", default=5)
    args = parser.parse_args()

    print("==================================================================")
    print("   PEMBARUAN DATA KAMUS AL-QUR'AN MULTILINGUAL (4 KAMUS BESAR)    ")
    print("==================================================================")

    if args.dict in ('all', 'jamid'):
        print("\n[1/4] Memproses Kamus Jamid Mabny...")
        excel_file = find_excel_file(args.excel)
        caches = load_all_caches()
        raw_data = read_excel_data(excel_file, sheet_name=args.sheet)
        filtered_data = filter_shortest_verses(raw_data, caches, max_per_word=args.limit)
        enriched_data = process_and_enrich(filtered_data, caches)
        export_files(enriched_data)
        print_stats(enriched_data)

    if args.dict in ('all', 'harf'):
        print("\n[2/4] Memproses Kamus Harf Ghair 'Amil...")
        update_harf_data(limit=args.limit)

    if args.dict in ('all', 'harf_amil'):
        print("\n[3/4] Memproses Kamus Harf 'Amil...")
        update_harf_amil_data(limit=args.limit)

    if args.dict in ('all', 'musytaq'):
        print("\n[4/4] Memproses Kamus Musytaq...")
        update_musytaq_data()

    print("\n" + "=" * 65)
    print("SEMUA DATA KAMUS BERHASIL DIPERBARUI & SIAP DIGUNAKAN DI WEB!")
    print("=" * 65 + "\n")


if __name__ == '__main__':
    main()
