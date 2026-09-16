#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Perfect Turkish Grammar Metadata Injector for build_multilingual_dataset.py
"""

import os
import sys

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ALL_GRAMMAR_TR = {
    # 1. Dhamir
    '1. Dhamir__1a': {'arti_tr': 'O (ERKEK)', 'desc_tr': 'O (3. tekil şahıs eril, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__1b': {'arti_tr': '..ONUN / ..ONU / ..ONA (ERKEK)', 'desc_tr': '..onun/..ona/..onu (3. tekil şahıs eril, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__1c': {'arti_tr': 'YALNIZCA ONA (ERKEK)', 'desc_tr': 'Yalnızca ona / yalnız onu (3. tekil şahıs eril, munfasıl mansub zamir)', 'jenis_tr': "Munfasıl Mansub (Ayrık Mef'ul Zamiri)"},
    '1. Dhamir__2a': {'arti_tr': 'O İKİSİ', 'desc_tr': 'O ikisi (3. şahıs tesniye/ikil, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__2b': {'arti_tr': '..O İKİSİNİN / ..O İKİSİNE', 'desc_tr': '..o ikisinin/..o ikisine (3. şahıs tesniye, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__3a': {'arti_tr': 'ONLAR (ERKEK ÇOĞUL)', 'desc_tr': 'Onlar (3. çoğul şahıs eril, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__3b': {'arti_tr': '..ONLARIN / ..ONLARA (ERKEK ÇOĞUL)', 'desc_tr': '..onların/..onlara/..onları (3. çoğul şahıs eril, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__3c': {'arti_tr': 'YALNIZCA ONLARA (ERKEK)', 'desc_tr': 'Yalnızca onlara / yalnız onları (3. çoğul şahıs eril, munfasıl mansub zamir)', 'jenis_tr': "Munfasıl Mansub (Ayrık Mef'ul Zamiri)"},
    '1. Dhamir__4a': {'arti_tr': 'O (KADIN)', 'desc_tr': 'O (3. tekil şahıs dişil, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__4b': {'arti_tr': '..ONUN / ..ONU / ..ONA (KADIN)', 'desc_tr': '..onun/..ona/..onu (3. tekil şahıs dişil, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__5a': {'arti_tr': 'ONLAR (KADIN ÇOĞUL)', 'desc_tr': 'Onlar (3. çoğul şahıs dişil, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__5b': {'arti_tr': '..ONLARIN / ..ONLARA (KADIN ÇOĞUL)', 'desc_tr': '..onların/..onlara/..onları (3. çoğul şahıs dişil, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__6a': {'arti_tr': 'SEN (ERKEK)', 'desc_tr': 'Sen (2. tekil şahıs eril, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__6b': {'arti_tr': '..SENİN / ..SANA / ..SENİ (ERKEK)', 'desc_tr': '..senin/..sana/..seni (2. tekil şahıs eril, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__6c': {'arti_tr': 'YALNIZCA SANA / YALNIZ SENİ', 'desc_tr': 'Yalnızca Sana / Yalnız Seni (2. tekil şahıs eril, munfasıl mansub zamir)', 'jenis_tr': "Munfasıl Mansub (Ayrık Mef'ul Zamiri)"},
    '1. Dhamir__7a': {'arti_tr': 'SİZ İKİNİZ', 'desc_tr': 'Siz ikiniz (2. şahıs tesniye/ikil, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__7b': {'arti_tr': '..SİZ İKİNİZİN / ..SİZ İKİNİZE', 'desc_tr': '..siz ikinizin/..siz ikinize (2. şahıs tesniye, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__8a': {'arti_tr': 'SİZLER (ERKEK ÇOĞUL)', 'desc_tr': 'Sizler (2. çoğul şahıs eril, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__8b': {'arti_tr': '..SİZİN / ..SİZE / ..SİZLERİ', 'desc_tr': '..sizin/..size/..sizleri (2. çoğul şahıs eril, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__8c': {'arti_tr': 'YALNIZCA SİZE (ÇOĞUL)', 'desc_tr': 'Yalnızca size / yalnız sizleri (2. çoğul şahıs eril, munfasıl mansub zamir)', 'jenis_tr': "Munfasıl Mansub (Ayrık Mef'ul Zamiri)"},
    '1. Dhamir__9b': {'arti_tr': '..SENİN / ..SANA (KADIN)', 'desc_tr': '..senin/..sana/..seni (2. tekil şahıs dişil, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__11a': {'arti_tr': 'BEN', 'desc_tr': 'Ben (1. tekil şahıs, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__11b': {'arti_tr': '..BENİM / ..BANA / ..BENİ', 'desc_tr': '..benim/..bana/..beni (1. tekil şahıs, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__11c': {'arti_tr': 'YALNIZCA BANA', 'desc_tr': 'Yalnızca bana / yalnız beni (1. tekil şahıs, munfasıl mansub zamir)', 'jenis_tr': "Munfasıl Mansub (Ayrık Mef'ul Zamiri)"},
    '1. Dhamir__12a': {'arti_tr': 'BİZ', 'desc_tr': 'Biz (1. çoğul şahıs, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__12b': {'arti_tr': '..BİZİM / ..BİZE / ..BİZİ', 'desc_tr': '..bizim/..bize/..bizi (1. çoğul şahıs, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__12c': {'arti_tr': 'YALNIZCA BİZE', 'desc_tr': 'Yalnızca bize / yalnız bizi (1. çoğul şahıs, munfasıl mansub zamir)', 'jenis_tr': "Munfasıl Mansub (Ayrık Mef'ul Zamiri)"},

    # 2. Mawshul
    '2. Mawshul__1': {'arti_tr': 'HER NE Kİ / O ŞEY Kİ / NELER Kİ', 'desc_tr': 'O şey ki / her ne ki (akılsız varlıklar için müşterek ilgi zamiri)', 'jenis_tr': 'Müşterek İsmi Mevsul (Mavsûl Müşterek)'},
    '2. Mawshul__2': {'arti_tr': 'O KİMSELER Kİ / ONLAR Kİ (ERKEK ÇOĞUL)', 'desc_tr': 'O kimseler ki (eril çoğul has ilgi zamiri)', 'jenis_tr': 'Has İsmi Mevsul (Mavsûl Hâs)'},
    '2. Mawshul__3': {'arti_tr': 'KİM Kİ / HER KİM', 'desc_tr': 'Kim ki / her kim (akıllı varlıklar için müşterek ilgi zamiri)', 'jenis_tr': 'Müşterek İsmi Mevsul (Mavsûl Müşterek)'},
    '2. Mawshul__4': {'arti_tr': 'O KİMSE Kİ / O Kİ (ERKEK TEKİL)', 'desc_tr': 'O kimse ki / o şey ki (eril tekil has ilgi zamiri)', 'jenis_tr': 'Has İsmi Mevsul (Mavsûl Hâs)'},
    '2. Mawshul__5': {'arti_tr': 'HANGİSİ Kİ / HER HANGİ BİRİ', 'desc_tr': 'Hangisi ki / her kim ki (mureb ilgi zamiri)', 'jenis_tr': 'Müphem İsmi Mevsul'},
    '2. Mawshul__6': {'arti_tr': 'O KADIN Kİ / O ŞEY Kİ (DİŞİL TEKİL)', 'desc_tr': 'O kadın ki / o şey ki (dişil tekil has ilgi zamiri)', 'jenis_tr': 'Has İsmi Mevsul (Mavsûl Hâs)'},
    '2. Mawshul__7': {'arti_tr': 'O KADINLAR Kİ (DİŞİL ÇOĞUL)', 'desc_tr': 'O kadınlar ki (dişil çoğul has ilgi zamiri)', 'jenis_tr': 'Has İsmi Mevsul (Mavsûl Hâs)'},
    '2. Mawshul__8': {'arti_tr': 'O KADINLAR Kİ (DİŞİL ÇOĞUL)', 'desc_tr': 'O kadınlar ki (dişil çoğul has ilgi zamiri)', 'jenis_tr': 'Has İsmi Mevsul (Mavsûl Hâs)'},
    '2. Mawshul__9': {'arti_tr': 'O İKİ KİMSE Kİ (ERİL İKİL)', 'desc_tr': 'O iki kimse ki (eril ikil has ilgi zamiri)', 'jenis_tr': 'Has İsmi Mevsul (Mavsûl Hâs)'},
    '2. Mawshul__10': {'arti_tr': 'HANGİSİ Kİ (DİŞİL)', 'desc_tr': 'Hangisi ki (dişil mureb ilgi zamiri)', 'jenis_tr': 'Müphem İsmi Mevsul'},

    # 3. Istifham
    '3. Istifham__1': {'arti_tr': 'NE? / NEDİR?', 'desc_tr': 'Ne? Nedir? (akılsız varlıklar için soru ismi)', 'jenis_tr': 'Soru İsmi (İsm-i İstifhâm)'},
    '3. Istifham__2': {'arti_tr': 'NASIL?', 'desc_tr': 'Nasıl? (durum/hâl soran soru ismi)', 'jenis_tr': 'Soru İsmi (İsm-i İstifhâm)'},
    '3. Istifham__3': {'arti_tr': 'KİM?', 'desc_tr': 'Kim? (akıllı varlıklar için soru ismi)', 'jenis_tr': 'Soru İsmi (İsm-i İstifhâm)'},
    '3. Istifham__4': {'arti_tr': 'HANGİSİ? / HANGİ?', 'desc_tr': 'Hangisi? Hangi? (mureb soru ismi)', 'jenis_tr': 'Soru İsmi (İsm-i İstifhâm)'},
    '3. Istifham__5': {'arti_tr': 'NASIL? / NEREDEN? / NE ZAMAN?', 'desc_tr': 'Nasıl? Nereden? (durum veya yön soran soru ismi)', 'jenis_tr': 'Soru İsmi (İsm-i İstifhâm)'},
    '3. Istifham__6': {'arti_tr': 'NE O Kİ? / NEDİR Kİ?', 'desc_tr': 'Nedir o? Ne şeydir? (Mā + Dzā birleşik soru ismi)', 'jenis_tr': 'Soru İsmi (İsm-i İstifhâm)'},
    '3. Istifham__7': {'arti_tr': 'KAÇ? / NE KADAR? / NE ÇOK?', 'desc_tr': 'Kaç? Ne kadar? (sayı veya süre soran soru ismi)', 'jenis_tr': 'Soru İsmi (İsm-i İstifhâm)'},
    '3. Istifham__8': {'arti_tr': 'NİÇİN? / NEDEN?', 'desc_tr': 'Niçin? Neden? (Li + Ma birleşik soru ismi)', 'jenis_tr': 'Soru İsmi (İsm-i İstifhâm)'},
    '3. Istifham__9': {'arti_tr': 'NEREDE? / NEREYE?', 'desc_tr': 'Nerede? Nereye? (mekân soran soru ismi)', 'jenis_tr': 'Soru İsmi (İsm-i İstifhâm)'},
    '3. Istifham__10': {'arti_tr': 'NE ZAMAN?', 'desc_tr': 'Ne zaman? (zaman soran soru ismi)', 'jenis_tr': 'Soru İsmi (İsm-i İstifhâm)'},

    # 4. Syarath
    '4. Syarath__1': {'arti_tr': 'HER KİM / KİM Kİ', 'desc_tr': 'Her kim (akıllılar için iki fiili cezmeden şart ismi)', 'jenis_tr': 'Şart İsmi (İsm-i Şart)'},
    '4. Syarath__2': {'arti_tr': 'HER NE Kİ / NE YAPARSANIZ', 'desc_tr': 'Her ne ki (akılsızlar için iki fiili cezmeden şart ismi)', 'jenis_tr': 'Şart İsmi (İsm-i Şart)'},
    '4. Syarath__3': {'arti_tr': 'HER NE ZAMAN ... İSE / HER DEFA', 'desc_tr': 'Her ne zaman ... ise (tekrar bildiren şart edatı)', 'jenis_tr': 'Şart İsmi (İsm-i Şart)'},
    '4. Syarath__4': {'arti_tr': 'HANGİSİ OLURSA / HER HANGİ BİRİ', 'desc_tr': 'Hangisi olursa (mureb şart ismi)', 'jenis_tr': 'Şart İsmi (İsm-i Şart)'},
    '4. Syarath__5': {'arti_tr': 'HANGİSİNİ OLURSA OLSUN (TEKİD)', 'desc_tr': 'Hangisini olursa olsun (tekidli mureb şart ismi)', 'jenis_tr': 'Şart İsmi (İsm-i Şart)'},

    # 5. Isyarah
    '5. Isyarah__1': {'arti_tr': 'BU / ŞU / O (ERKEK TEKİL)', 'desc_tr': 'Bu / Şu / O (eril tekil işaret ismi)', 'jenis_tr': 'İşaret İsmi (İsm-i İşâre)'},
    '5. Isyarah__2': {'arti_tr': 'İŞTE ONLAR / ŞUNLAR / BUNLAR', 'desc_tr': 'İşte onlar / şunlar / bunlar (çoğul işaret ismi)', 'jenis_tr': 'İşaret İsmi (İsm-i İşâre)'},
    '5. Isyarah__3': {'arti_tr': 'BU / ŞU / O (KADIN TEKİL / AKILSIZ ÇOĞUL)', 'desc_tr': 'Bu / Şu / O (dişil tekil ve akılsız çoğul işaret ismi)', 'jenis_tr': 'İşaret İsmi (İsm-i İşâre)'},
    '5. Isyarah__4': {'arti_tr': 'ŞU / O (KADIN UZAK / AKILSIZ ÇOĞUL)', 'desc_tr': 'Şu / O (uzak için dişil tekil ve akılsız çoğul işaret ismi)', 'jenis_tr': 'Uzak İşaret İsmi (İsm-i İşâre)'},
    '5. Isyarah__5': {'arti_tr': 'BURADA / BURASI', 'desc_tr': 'Burada / burası (yakın mekân işaret ismi)', 'jenis_tr': 'Mekân İşaret İsmi (İsm-i İşâre Mekân)'},
    '5. Isyarah__6': {'arti_tr': 'ORADA / ORASI', 'desc_tr': 'Orada / orası (uzak mekân işaret ismi)', 'jenis_tr': 'Mekân İşaret İsmi (İsm-i İşâre Mekân)'},
    '5. Isyarah__7': {'arti_tr': 'BU İKİSİ (ERİL İKİL)', 'desc_tr': 'Bu ikisi (yakın için eril ikil işaret ismi)', 'jenis_tr': 'İkil İşaret İsmi (İsm-i İşâre Tesniye)'},
    '5. Isyarah__8': {'arti_tr': 'BU İKİSİ / ŞU İKİSİ (DİŞİL İKİL)', 'desc_tr': 'Bu ikisi / şu ikisi (dişil ikil işaret ismi)', 'jenis_tr': 'İkil İşaret İsmi (İsm-i İşâre Tesniye)'},

    # 6. Isim Fi'il
    '6. Isim Fi\'il__1': {'arti_tr': 'MÜNEZZEHTİR / SÜBHANALLAH (TESBİH)', 'desc_tr': 'Her türlü eksiklikten münezzehtir (tenzih ve tesbih mastarı/isim fiil)', 'jenis_tr': 'Tesbih İsim Fiili'},
    '6. Isim Fi\'il__2': {'arti_tr': 'GETİRİN! / ORTAYA KOYUN!', 'desc_tr': 'Delilinizi getirin / ortaya koyun (emir anlamlı isim fiil / hātû)', 'jenis_tr': 'Emir Anlamlı İsim Fiil (İsm-i Fiil Emir)'},
    '6. Isim Fi\'il__3': {'arti_tr': 'ÖF! / YAZIKLAR OLSUN!', 'desc_tr': 'Öf! / Bıktım! (şimdiki zaman anlamlı bıkkınlık bildiren isim fiil / etedaccaru)', 'jenis_tr': 'Muzari Anlamlı İsim Fiil (İsm-i Fiil Muzâri)'},
    '6. Isim Fi\'il__4': {'arti_tr': "ALLAH'A SIĞINIRIM!", 'desc_tr': "Allah'a sığınırım / Maazallah (sığınma bildiren isim fiil / e'ûzu billâh)", 'jenis_tr': 'Sığınma İsim Fiili (İsm-i Fiil İ\'âze)'},
    '6. Isim Fi\'il__5': {'arti_tr': 'GELİN! / GETİRİN!', 'desc_tr': 'Gelin! Getirin! (emir anlamlı isim fiil / te\'âlev)', 'jenis_tr': 'Emir Anlamlı İsim Fiil (İsm-i Fiil Emir)'},
    '6. Isim Fi\'il__6': {'arti_tr': 'NE KADAR UZAK! / HEYHAT!', 'desc_tr': 'Ne kadar uzak! / İmkansız! (geçmiş zaman anlamlı isim fiil / ba\'uda)', 'jenis_tr': 'Geçmiş Anlamlı İsim Fiil (İsm-i Fiil Mâzî)'},
    '6. Isim Fi\'il__7': {'arti_tr': 'ALIN, OKUYUN!', 'desc_tr': 'Alın, okuyun şunu! (emir anlamlı isim fiil / hā\'umu)', 'jenis_tr': 'Emir Anlamlı İsim Fiil (İsm-i Fiil Emir)'},
    '6. Isim Fi\'il__8': {'arti_tr': 'HAYDİ GEL! / GELSENE!', 'desc_tr': 'Haydi gel! (emir anlamlı isim fiil / heyte leke)', 'jenis_tr': 'Emir Anlamlı İsim Fiil (İsm-i Fiil Emir)'},

    # 7. Fi'il Jamid
    '7. Fi\'il Jamid__1': {'arti_tr': 'DEĞİLDİR', 'desc_tr': 'Değildir (olumsuzluk bildiren donuk/çekimsiz mâzî fiil)', 'jenis_tr': 'Camid Fiil (Fi\'l-i Câmid)'},
    '7. Fi\'il Jamid__2': {'arti_tr': 'NE KÖTÜDÜR!', 'desc_tr': 'Ne kötüdür! (yergi bildiren donuk/çekimsiz fiil / fi\'lu\'z-zemm)', 'jenis_tr': 'Yergi Camid Fiili (Fi\'lu\'z-Zemm)'},
    '7. Fi\'il Jamid__3': {'arti_tr': 'UMULUR Kİ / BELKİ DE', 'desc_tr': 'Umulur ki / belki (ümit/beklenti bildiren donuk fiil / fi\'lu\'r-recâ)', 'jenis_tr': 'Recâ Camid Fiili (Fi\'lu\'r-Recâ)'},
    '7. Fi\'il Jamid__4': {'arti_tr': 'NE GÜZELDİR! / NE İYİDİR!', 'desc_tr': 'Ne güzeldir! (övgü bildiren donuk/çekimsiz fiil / fi\'lu\'l-medh)', 'jenis_tr': 'Övgü Camid Fiili (Fi\'lu\'l-Medh)'},
    '7. Fi\'il Jamid__5': {'arti_tr': 'NE KÖTÜDÜR O ŞEY Kİ!', 'desc_tr': 'Ne kötüdür o şey ki (Bi\'se + Mâ birleşik yergi fiili)', 'jenis_tr': 'Yergi Camid Fiili (Fi\'lu\'z-Zemm)'},
    '7. Fi\'il Jamid__6': {'arti_tr': 'BAŞLADI / KOYULDU', 'desc_tr': 'Başladı / koyuldu (başlama bildiren nâkıs/câmid fiil / ef\'âlü\'ş-şürû\')', 'jenis_tr': 'Şürû\' Fiili (Ef\'âlü\'ş-Şürû\')'},
    '7. Fi\'il Jamid__7': {'arti_tr': 'HAŞA! / TENZİH EDERİZ!', 'desc_tr': 'Hâşâ! / Allah korusun, tenzih ederiz (tenzih bildiren câmid istisnâ fiili)', 'jenis_tr': 'Tenzih Câmid Fiili (Fi\'l-i Tenzîh)'},
    '7. Fi\'il Jamid__8': {'arti_tr': 'NE GÜZELDİR O ŞEY Kİ!', 'desc_tr': 'Ne güzeldir o şey ki (Ni\'me + Mâ birleşik övgü fiili)', 'jenis_tr': 'Övgü Câmid Fiili (Fi\'lu\'l-Medh)'}
}

file_path = 'build_multilingual_dataset.py'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

out_lines = []
in_grammar = False
current_key = None

for line in lines:
    if 'GRAMMATICAL_METADATA = {' in line:
        in_grammar = True
        out_lines.append(line)
        continue
    
    if in_grammar and line.startswith('}'):
        in_grammar = False
        out_lines.append(line)
        continue

    if in_grammar:
        # Check if new key
        stripped = line.strip()
        if stripped.startswith('"') and '": {' in stripped:
            current_key = stripped.split('": {')[0].replace('"', '')
            out_lines.append(line)
            continue
        
        # If line contains arti_tr, desc_tr, jenis_tr, skip it since we will write exact
        if any(tag in line for tag in ['"arti_tr":', '"desc_tr":', '"jenis_tr":']):
            continue

        # If line contains "jenis_es":, we append the Turkish fields right after it
        if '"jenis_es":' in line:
            # Ensure line has comma
            line_clean = line.rstrip('\r\n')
            if not line_clean.endswith(','):
                line_clean += ','
            out_lines.append(line_clean + '\n')

            if current_key in ALL_GRAMMAR_TR:
                tr_info = ALL_GRAMMAR_TR[current_key]
                out_lines.append(f'        "arti_tr": "{tr_info["arti_tr"]}",\n')
                out_lines.append(f'        "desc_tr": "{tr_info["desc_tr"]}",\n')
                out_lines.append(f'        "jenis_tr": "{tr_info["jenis_tr"]}"\n')
            continue

    out_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(out_lines)

print("Injected perfect Turkish grammar metadata into build_multilingual_dataset.py!")
