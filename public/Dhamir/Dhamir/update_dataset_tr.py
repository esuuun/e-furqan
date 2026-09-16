#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to inject Turkish metadata into build_multilingual_dataset.py
and update update_data.py.
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

SURAH_TR = {
    1: 'Fâtiha (Açılış)', 2: 'Bakara (Sığır / İnek)', 3: 'Âl-i İmrân (İmrân Ailesi)', 4: 'Nisâ (Kadınlar)', 5: 'Mâide (Sofra)',
    6: "En'âm (Evcil Hayvanlar)", 7: "A'râf (Yüksek Yerler)", 8: 'Enfâl (Savaş Ganimetleri)', 9: 'Tevbe (Tövbe)', 10: 'Yûnus (Yunus Peygamber)',
    11: 'Hûd (Hud Peygamber)', 12: 'Yûsuf (Yusuf Peygamber)', 13: "Ra'd (Gök Gürültüsü)", 14: 'İbrâhîm (İbrahim Peygamber)', 15: 'Hicr (Hicr Bölgesi)',
    16: 'Nahl (Bal Arısı)', 17: 'İsrâ (Gece Yürüyüşü)', 18: 'Kehf (Mağara)', 19: 'Meryem (Meryem)', 20: 'Tâhâ (Tâ-Hâ)',
    21: 'Enbiyâ (Peygamberler)', 22: 'Hac (Hac İbadeti)', 23: "Mü'minûn (İnananlar / Müminler)", 24: 'Nûr (Nur / Işık)', 25: 'Furkân (Hak ile Bâtılı Ayıran)',
    26: 'Şuarâ (Şairler)', 27: 'Neml (Karınca)', 28: 'Kasas (Kıssalar)', 29: 'Ankebût (Örümcek)', 30: 'Rûm (Romalılar / Bizans)',
    31: 'Lokmân (Lokman Hekim)', 32: 'Secde (Secde)', 33: 'Ahzâb (Gruplar / Müttefikler)', 34: "Sebe' (Sebe Kavmi)", 35: 'Fâtır (Yaratan)',
    36: 'Yâsîn (Yâ-Sîn)', 37: 'Sâffât (Sıra Sıra Duranlar)', 38: 'Sâd (Sâd Harfi)', 39: 'Zümer (Kümeler / Gruplar)', 40: "Mü'min (Gâfir / Bağışlayan)",
    41: 'Fussilet (Ayrıntılı Açıklanmış)', 42: 'Şûrâ (Danışma / Şûra)', 43: 'Zuhruf (Altın / Mücevher)', 44: 'Duhân (Duman)', 45: 'Câsiye (Diz Üstü Çökenler)',
    46: 'Ahkâf (Kum Tepeleri)', 47: 'Muhammed (Muhammed Peygamber)', 48: 'Fetih (Zafer)', 49: 'Hucurât (Odalar)', 50: 'Kâf (Kâf Harfi)',
    51: 'Zâriyât (Tozutup Savuranlar)', 52: 'Tûr (Tûr Dağı)', 53: 'Necm (Yıldız)', 54: 'Kamer (Ay)', 55: 'Rahmân (Sonsuz Merhamet Sahibi)',
    56: "Vâkı'a (Gerçekleşen Kıyamet)", 57: 'Hadîd (Demir)', 58: 'Mücâdele (Tartışan Kadın)', 59: 'Haşr (Toplanma / Sürgün)', 60: 'Mümtehine (Sınanan Kadın)',
    61: 'Saf (Dizi / Saf Bağlama)', 62: 'Cuma (Cuma Günü)', 63: 'Münâfikûn (İkiyüzlüler / Münafıklar)', 64: 'Tegâbün (Aldanma / Kâr-Zarar)', 65: 'Talâk (Boşanma)',
    66: 'Tahrîm (Haram Kılma)', 67: 'Mülk (Hükümranlık / Mülk)', 68: 'Kalem (Kalem)', 69: 'Hâkka (Gerçekleşecek Olan)', 70: "Me'âric (Yükselme Dereceleri)",
    71: 'Nûh (Nuh Peygamber)', 72: 'Cin (Cinler)', 73: 'Müzzemmil (Örtünüp Bürünen)', 74: 'Müddessir (Örtüsüne Sarınan)', 75: 'Kıyâme (Kıyamet Günü)',
    76: 'İnsân (Dehr / İnsan)', 77: 'Mürselât (Gönderilen Rüzgarlar)', 78: "Nebe' (Büyük Haber)", 79: "Nâzi'ât (Çekip Çıkaranlar)", 80: 'Abese (Yüzünü Ekşitti)',
    81: 'Tekvîr (Güneşin Dürülmesi)', 82: 'İnfitâr (Gök Yarılması)', 83: 'Mutaffifîn (Ölçüde Hile Yapanlar)', 84: 'İnşikâk (Yarılma)', 85: 'Bürûc (Burçlar)',
    86: 'Târık (Gece Gelen / Sabah Yıldızı)', 87: "A'lâ (En Yüce)", 88: 'Gâşiye (Kaplayıp Basiyan Felaket)', 89: 'Fecr (Şafak Vakti)', 90: 'Beled (Şehir / Belde)',
    91: 'Şems (Güneş)', 92: 'Leyl (Gece)', 93: 'Duhâ (Kuşluk Vakti)', 94: 'İnşirâh (Gönül Ferahlığı)', 95: 'Tîn (İncir)',
    96: 'Alak (Asılıp Tutunan / Kan Pıhtısı)', 97: 'Kadir (Kadir Gecesi)', 98: 'Beyyine (Açık Delil)', 99: 'Zilzâl (Deprem / Sarsıntı)', 100: 'Âdiyât (Koşan Atlar)',
    101: "Kâri'a (Kapı Çalan Büyük Felaket)", 102: 'Tekâsür (Çokluk Yarışı)', 103: 'Asr (Zaman / Asır)', 104: 'Hümeze (Arkadan Çekiştiren)', 105: 'Fîl (Fil Olayı)',
    106: 'Kureyş (Kureyş Kabilesi)', 107: "Mâ'ûn (Küçük Yardım)", 108: 'Kevser (Bol Nimet / Kevser Havuzu)', 109: 'Kâfirûn (İnkarcılar)', 110: 'Nasr (Yardım / Zafer)',
    111: 'Tebbet (Mesed / Alev)', 112: 'İhlâs (Samimiyet / Tevhid)', 113: 'Felak (Sabah Aydınlığı)', 114: 'Nâs (İnsanlar)'
}

BENTUK_TR = {
    '1. Dhamir': '1. Zamirler (Dhamir - Şahıs Zamirleri)',
    '2. Mawshul': '2. İsmi Mevsul (Mawshul - İlgi Zamirleri)',
    '3. Istifham': '3. Soru Edatları (İstifham - Soru İsimleri)',
    '4. Syarath': '4. Şart Edatları (Şart - Şart İsimleri)',
    '5. Isyarah': '5. İşaret İsimleri (İşaret Zamirleri / İsm-i İşâre)',
    "6. Isim Fi'il": "6. İsim Fiil (Fiil Anlamlı İsimler / İsm-i Fiil)",
    "7. Fi'il Jamid": "7. Camid Fiiller (Çekimsiz / Donuk Fiiller)"
}

GRAMMAR_TR = {
    # 1. Dhamir
    '1. Dhamir__1a': {'arti_tr': 'O (ERKEK)', 'desc_tr': 'O (3. tekil şahıs eril, munfasıl/ayrık zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__1b': {'arti_tr': '..ONUN / ..ONU / ..ONA (ERKEK)', 'desc_tr': '..onun/..ona (3. tekil şahıs eril, muttasıl/bitişik zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__1c': {'arti_tr': 'YALNIZCA ONA (ERKEK)', 'desc_tr': 'Yalnızca ona (3. tekil şahıs eril, munfasıl mansub zamir)', 'jenis_tr': 'Munfasıl Mansub (Ayrık Mef\'ul Zamiri)'},
    '1. Dhamir__2a': {'arti_tr': 'O İKİSİ', 'desc_tr': 'O ikisi (3. şahıs tesniye/ikil, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__2b': {'arti_tr': '..O İKİSİNİN / ..O İKİSİNE', 'desc_tr': '..o ikisinin/..o ikisine (3. şahıs tesniye, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__3a': {'arti_tr': 'ONLAR (ERKEK ÇOĞUL)', 'desc_tr': 'Onlar (3. çoğul şahıs eril, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__3b': {'arti_tr': '..ONLARIN / ..ONLARA (ERKEK ÇOĞUL)', 'desc_tr': '..onların/..onlara (3. çoğul şahıs eril, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__3c': {'arti_tr': 'YALNIZCA ONLARA (ERKEK)', 'desc_tr': 'Yalnızca onlara (3. çoğul şahıs eril, munfasıl mansub zamir)', 'jenis_tr': 'Munfasıl Mansub (Ayrık Mef\'ul Zamiri)'},
    '1. Dhamir__4a': {'arti_tr': 'O (KADIN)', 'desc_tr': 'O (3. tekil şahıs dişil, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__4b': {'arti_tr': '..ONUN / ..ONU / ..ONA (KADIN)', 'desc_tr': '..onun/..ona (3. tekil şahıs dişil, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__5a': {'arti_tr': 'ONLAR (KADIN ÇOĞUL)', 'desc_tr': 'Onlar (3. çoğul şahıs dişil, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__5b': {'arti_tr': '..ONLARIN / ..ONLARA (KADIN ÇOĞUL)', 'desc_tr': '..onların/..onlara (3. çoğul şahıs dişil, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__6a': {'arti_tr': 'SEN (ERKEK)', 'desc_tr': 'Sen (2. tekil şahıs eril, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__6b': {'arti_tr': '..SENİN / ..SANA / ..SENİ (ERKEK)', 'desc_tr': '..senin/..sana (2. tekil şahıs eril, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__6c': {'arti_tr': 'YALNIZCA SANA / YALNIZ SENİ', 'desc_tr': 'Yalnızca Sana / Yalnız Seni (2. tekil şahıs eril, munfasıl mansub zamir)', 'jenis_tr': 'Munfasıl Mansub (Ayrık Mef\'ul Zamiri)'},
    '1. Dhamir__7a': {'arti_tr': 'SİZ İKİNİZ', 'desc_tr': 'Siz ikiniz (2. şahıs tesniye/ikil, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__7b': {'arti_tr': '..SİZ İKİNİZİN / ..SİZ İKİNİZE', 'desc_tr': '..siz ikinizin/..siz ikinize (2. şahıs tesniye, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__8a': {'arti_tr': 'SİZLER (ERKEK ÇOĞUL)', 'desc_tr': 'Sizler (2. çoğul şahıs eril, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__8b': {'arti_tr': '..SİZİN / ..SİZE / ..SİZLERİ', 'desc_tr': '..sizin/..size (2. çoğul şahıs eril, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__8c': {'arti_tr': 'YALNIZCA SİZE (ÇOĞUL)', 'desc_tr': 'Yalnızca size (2. çoğul şahıs eril, munfasıl mansub zamir)', 'jenis_tr': 'Munfasıl Mansub (Ayrık Mef\'ul Zamiri)'},
    '1. Dhamir__9b': {'arti_tr': '..SENİN / ..SANA (KADIN)', 'desc_tr': '..senin/..sana (2. tekil şahıs dişil, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__11a': {'arti_tr': 'BEN', 'desc_tr': 'Ben (1. tekil şahıs nefsi mütekellim vahdehu, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__11b': {'arti_tr': '..BENİM / ..BANA / ..BENİ', 'desc_tr': '..benim/..bana (1. tekil şahıs, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__11c': {'arti_tr': 'YALNIZCA BANA', 'desc_tr': 'Yalnızca bana (1. tekil şahıs, munfasıl mansub zamir)', 'jenis_tr': 'Munfasıl Mansub (Ayrık Mef\'ul Zamiri)'},
    '1. Dhamir__12a': {'arti_tr': 'BİZ', 'desc_tr': 'Biz (1. çoğul şahıs nefsi mütekellim mea\'l-gayr, munfasıl zamir)', 'jenis_tr': 'Munfasıl (Ayrık Zamir)'},
    '1. Dhamir__12b': {'arti_tr': '..BİZİM / ..BİZE / ..BİZİ', 'desc_tr': '..bizim/..bize (1. çoğul şahıs, muttasıl zamir)', 'jenis_tr': 'Muttasıl (Bitişik Zamir)'},
    '1. Dhamir__12c': {'arti_tr': 'YALNIZCA BİZE', 'desc_tr': 'Yalnızca bize (1. çoğul şahıs, munfasıl mansub zamir)', 'jenis_tr': 'Munfasıl Mansub (Ayrık Mef\'ul Zamiri)'},

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
    '3. Istifham__10': {'arti_tr': 'NE ZAMAN? (KIYAMET GÜNÜ İÇİN)', 'desc_tr': 'Ne zaman? (özellikle büyük gelecek olaylar/kıyamet için zaman soran soru ismi)', 'jenis_tr': 'Soru İsmi (İsm-i İstifhâm)'},
    '3. Istifham__11': {'arti_tr': 'NE ZAMAN?', 'desc_tr': 'Ne zaman? (genel zaman soran soru ismi)', 'jenis_tr': 'Soru İsmi (İsm-i İstifhâm)'},

    # 4. Syarath
    '4. Syarath__1': {'arti_tr': 'EĞER / ŞAYET / -SE, -SA', 'desc_tr': 'Eğer, şayet (iki fiili cezmeden şart harfi)', 'jenis_tr': 'Şart Harfi (Harf-i Şart)'},
    '4. Syarath__2': {'arti_tr': 'ZAMAN / -DIĞI ZAMAN / İKEN', 'desc_tr': '-dığı zaman / o vakit (cezmetmeyen zaman bildiren şart ismi)', 'jenis_tr': 'Şart İsmi (İsm-i Şart)'},
    '4. Syarath__3': {'arti_tr': 'EĞER ... OLSAYDI (İMKANSIZ ŞART)', 'desc_tr': 'Eğer ... olsaydı (geçmişte gerçekleşmemiş şart harfi / harf-i imtina\')', 'jenis_tr': 'Şart Harfi (Harf-i Şart)'},
    '4. Syarath__4': {'arti_tr': 'HER KİM / KİM Kİ', 'desc_tr': 'Her kim (akıllılar için iki fiili cezmeden şart ismi)', 'jenis_tr': 'Şart İsmi (İsm-i Şart)'},
    '4. Syarath__5': {'arti_tr': 'HER NE Kİ / NE YAPARSANIZ', 'desc_tr': 'Her ne ki (akılsızlar için iki fiili cezmeden şart ismi)', 'jenis_tr': 'Şart İsmi (İsm-i Şart)'},
    '4. Syarath__6': {'arti_tr': 'NE ZAMAN Kİ / -İNCE / -DİĞİNDE', 'desc_tr': '-dığında / o vakit (geçmiş zaman bildiren şart edatı)', 'jenis_tr': 'Şart İsmi (İsm-i Şart)'},
    '4. Syarath__7': {'arti_tr': 'EĞER OLMASAYDI...', 'desc_tr': 'Eğer ... olmasaydı (bir şeyin varlığı sebebiyle diğerinin yokluğunu bildiren şart harfi)', 'jenis_tr': 'Şart Harfi (Harf-i Şart)'},
    '4. Syarath__8': {'arti_tr': 'HER NE ZAMAN ... İSE / HER DEFA', 'desc_tr': 'Her ne zaman ... ise (tekrar bildiren şart edatı)', 'jenis_tr': 'Şart İsmi (İsm-i Şart)'},
    '4. Syarath__9': {'arti_tr': 'HER KİM / ŞUNA GELİNCE...', 'desc_tr': '...e gelince / her kim ki (detay ve şart harfi)', 'jenis_tr': 'Şart ve Tafsil Harfi'},
    '4. Syarath__10': {'arti_tr': 'HER NEREDE OLURSANIZ', 'desc_tr': 'Her nerede (mekân bildiren şart ismi)', 'jenis_tr': 'Şart İsmi (İsm-i Şart)'},
    '4. Syarath__11': {'arti_tr': 'O HALDE / ÖYLE İSE', 'desc_tr': 'O halde / öyleyse (cevap ve ceza harfi)', 'jenis_tr': 'Cevap Harfi (Harf-i Cevap)'},
    '4. Syarath__12': {'arti_tr': 'O VAKİT Kİ / ÇÜNKÜ / -DİĞİNDE', 'desc_tr': 'O vakit ki / hani (geçmiş zaman zarfı)', 'jenis_tr': 'Zaman Zarfı (Zarf-ı Zaman)'},
    '4. Syarath__13': {'arti_tr': 'HER NE OLURSA OLSUN / NE KADAR', 'desc_tr': 'Her ne olursa olsun (akılsız varlıklar için cezmeden şart ismi)', 'jenis_tr': 'Şart İsmi (İsm-i Şart)'},
    '4. Syarath__14': {'arti_tr': 'HER HANGİ BİRİ / HANGİSİ OLURSA', 'desc_tr': 'Hangisi olursa (mureb şart ismi)', 'jenis_tr': 'Şart İsmi (İsm-i Şart)'},
    '4. Syarath__15': {'arti_tr': 'HER NEREDE', 'desc_tr': 'Her nerede (mekân şart ismi)', 'jenis_tr': 'Şart İsmi (İsm-i Şart)'},

    # 5. Isyarah
    '5. Isyarah__1': {'arti_tr': 'BU (ERKEK TEKİL)', 'desc_tr': 'Bu (yakın için eril tekil işaret ismi)', 'jenis_tr': 'Yakın İşaret İsmi (İsm-i İşâre)'},
    '5. Isyarah__2': {'arti_tr': 'ŞU / O (ERKEK UZAK)', 'desc_tr': 'Şu / O (uzak için eril tekil işaret ismi)', 'jenis_tr': 'Uzak İşaret İsmi (İsm-i İşâre)'},
    '5. Isyarah__3': {'arti_tr': 'BU (KADIN TEKİL / AKILSIZ ÇOĞUL)', 'desc_tr': 'Bu (yakın için dişil tekil ve akılsız çoğul işaret ismi)', 'jenis_tr': 'Yakın İşaret İsmi (İsm-i İşâre)'},
    '5. Isyarah__4': {'arti_tr': 'İŞTE ONLAR / ŞUNLAR (ÇOĞUL)', 'desc_tr': 'İşte onlar / şunlar (uzak için çoğul işaret ismi)', 'jenis_tr': 'Uzak İşaret İsmi (İsm-i İşâre)'},
    '5. Isyarah__5': {'arti_tr': 'BUNLAR (ÇOĞUL)', 'desc_tr': 'Bunlar (yakın için çoğul işaret ismi)', 'jenis_tr': 'Yakın İşaret İsmi (İsm-i İşâre)'},
    '5. Isyarah__6': {'arti_tr': 'ŞU / O (KADIN UZAK / AKILSIZ ÇOĞUL)', 'desc_tr': 'Şu / O (uzak için dişil tekil ve akılsız çoğul işaret ismi)', 'jenis_tr': 'Uzak İşaret İsmi (İsm-i İşâre)'},
    '5. Isyarah__7': {'arti_tr': 'BU İKİSİ (ERİL İKİL)', 'desc_tr': 'Bu ikisi (yakın için eril ikil işaret ismi)', 'jenis_tr': 'Yakın İşaret İsmi (İsm-i İşâre)'},
    '5. Isyarah__8': {'arti_tr': 'ŞU İKİSİ / O İKİSİ (UZAK İKİL)', 'desc_tr': 'Şu ikisi / o ikisi (uzak için eril ikil işaret ismi)', 'jenis_tr': 'Uzak İşaret İsmi (İsm-i İşâre)'},

    # 6. Isim Fi'il
    '6. Isim Fi\'il__1': {'arti_tr': 'NE KADAR UZAK! / HEYHAT!', 'desc_tr': 'Ne kadar uzak! / İmkansız! (geçmiş zaman anlamlı isim fiil / ba\'uda)', 'jenis_tr': 'Geçmiş Anlamlı İsim Fiil (İsm-i Fiil Mâzî)'},
    '6. Isim Fi\'il__2': {'arti_tr': 'HAYDİ GELİN! / GEL!', 'desc_tr': 'Haydi gelin! (emir anlamlı isim fiil / akbil)', 'jenis_tr': 'Emir Anlamlı İsim Fiil (İsm-i Fiil Emir)'},
    '6. Isim Fi\'il__3': {'arti_tr': 'ÖF! / YAZIKLAR OLSUN!', 'desc_tr': 'Öf! / Bıktım! (şimdiki zaman anlamlı bıkkınlık bildiren isim fiil / etedaccaru)', 'jenis_tr': 'Muzari Anlamlı İsim Fiil (İsm-i Fiil Muzâri)'},
    '6. Isim Fi\'il__4': {'arti_tr': 'KABUL ET / DUAMIZI KABUL EYLE', 'desc_tr': 'Duamızı kabul buyur Allahım (emir anlamlı isim fiil / istacib)', 'jenis_tr': 'Emir Anlamlı İsim Fiil (İsm-i Fiil Emir)'},
    '6. Isim Fi\'il__5': {'arti_tr': 'GELİN! / GETİRİN!', 'desc_tr': 'Gelin! Getirin! (emir anlamlı isim fiil / te\'âlev)', 'jenis_tr': 'Emir Anlamlı İsim Fiil (İsm-i Fiil Emir)'},

    # 7. Fi'il Jamid
    '7. Fi\'il Jamid__1': {'arti_tr': 'DEĞİLDİR', 'desc_tr': 'Değildir (olumsuzluk bildiren donuk/çekimsiz mâzî fiil)', 'jenis_tr': 'Camid Fiil (Fi\'l-i Câmid)'},
    '7. Fi\'il Jamid__2': {'arti_tr': 'NE GÜZELDİR! / NE İYİDİR!', 'desc_tr': 'Ne güzeldir! (övgü bildiren donuk/çekimsiz fiil / fi\'lu\'l-medh)', 'jenis_tr': 'Övgü Camid Fiili (Fi\'lu\'l-Medh)'},
    '7. Fi\'il Jamid__3': {'arti_tr': 'NE KÖTÜDÜR!', 'desc_tr': 'Ne kötüdür! (yergi bildiren donuk/çekimsiz fiil / fi\'lu\'z-zemm)', 'jenis_tr': 'Yergi Camid Fiili (Fi\'lu\'z-Zemm)'},
    '7. Fi\'il Jamid__4': {'arti_tr': 'UMULUR Kİ / BELKİ DE', 'desc_tr': 'Umulur ki / belki (ümit/beklenti bildiren donuk fiil / fi\'lu\'r-recâ)', 'jenis_tr': 'Recâ Camid Fiili (Fi\'lu\'r-Recâ)'},
    '7. Fi\'il Jamid__5': {'arti_tr': 'NE HOŞTUR! / NE GÜZELDİR!', 'desc_tr': 'Ne hoştur! (övgü bildiren birleşik donuk fiil)', 'jenis_tr': 'Övgü Camid Fiili (Fi\'lu\'l-Medh)'}
}

# Update build_multilingual_dataset.py
dataset_file = os.path.join(BASE_DIR, 'build_multilingual_dataset.py')
with open(dataset_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update SURAHS in build_multilingual_dataset.py
# Add "arti_tr": "..." to each surah entry if not present
for s_num, tr_meaning in SURAH_TR.items():
    s_key = str(s_num)
    # look for "arti_es": ... followed by "ayat": in surah entry
    pattern_es = f'"arti_es":'
    # Check if this surah already has arti_tr
    # We can inject after arti_es
    surah_block_marker = f'"{s_key}": {{'
    if surah_block_marker in content:
        idx = content.find(surah_block_marker)
        next_block = content.find('},\n', idx)
        if next_block != -1:
            block = content[idx:next_block]
            if '"arti_tr":' not in block:
                target = '"arti_es":'
                pos = block.find(target)
                if pos != -1:
                    line_end = block.find('\n', pos)
                    full_line = block[pos:line_end]
                    new_line = full_line + f'\n        "arti_tr": "{tr_meaning}",'
                    block_new = block.replace(full_line, new_line, 1)
                    content = content[:idx] + block_new + content[next_block:]

# 2. Update BENTUK_LABELS
for b_key, tr_val in BENTUK_TR.items():
    bentuk_marker = f'"{b_key}": {{'
    if bentuk_marker in content:
        idx = content.find(bentuk_marker)
        next_block = content.find('},\n', idx)
        if next_block != -1:
            block = content[idx:next_block]
            if '"tr":' not in block:
                target = '"es":'
                pos = block.find(target)
                if pos != -1:
                    line_end = block.find('\n', pos)
                    full_line = block[pos:line_end]
                    new_line = full_line + f'\n        "tr": "{tr_val}",'
                    block_new = block.replace(full_line, new_line, 1)
                    content = content[:idx] + block_new + content[next_block:]

# 3. Update GRAMMATICAL_METADATA
for g_key, g_dict in GRAMMAR_TR.items():
    g_marker = f'"{g_key}": {{'
    if g_marker in content:
        idx = content.find(g_marker)
        next_block = content.find('},\n', idx)
        if next_block != -1:
            block = content[idx:next_block]
            if '"arti_tr":' not in block:
                target = '"jenis_es":'
                pos = block.find(target)
                if pos != -1:
                    line_end = block.find('\n', pos)
                    full_line = block[pos:line_end]
                    extra = (
                        f'\n        "arti_tr": "{g_dict["arti_tr"]}",'
                        f'\n        "desc_tr": "{g_dict["desc_tr"]}",'
                        f'\n        "jenis_tr": "{g_dict["jenis_tr"]}"'
                    )
                    new_line = full_line + ',' + extra
                    block_new = block.replace(full_line, new_line, 1)
                    content = content[:idx] + block_new + content[next_block:]

# 4. Update enrich loop in build_multilingual_dataset.py
if "item['BentukKataTR']" not in content:
    content = content.replace(
        "item['BentukKataES'] = b_labels.get('es', b)",
        "item['BentukKataES'] = b_labels.get('es', b)\n        item['BentukKataTR'] = b_labels.get('tr', b)"
    )

if "item['SuratArtiTR']" not in content:
    content = content.replace(
        "item['SuratArtiES'] = s_info.get('arti_es', s_info['arti_en'])",
        "item['SuratArtiES'] = s_info.get('arti_es', s_info['arti_en'])\n            item['SuratArtiTR'] = s_info.get('arti_tr', s_info['arti_en'])"
    )
    content = content.replace(
        "item['SuratArtiES'] = \"\"",
        "item['SuratArtiES'] = \"\"\n            item['SuratArtiTR'] = \"\""
    )

if "item['ArtiKataTR']" not in content:
    content = content.replace(
        "item['ArtiKataES'] = gm.get('arti_es', item['Arti kata'])",
        "item['ArtiKataES'] = gm.get('arti_es', item['Arti kata'])\n        item['ArtiKataTR'] = gm.get('arti_tr', item['Arti kata'])"
    )

if "item['TeksArtiTR']" not in content:
    content = content.replace(
        "item['TeksArtiES'] = caches['es'].get(v_key, teks_id)",
        "item['TeksArtiES'] = caches['es'].get(v_key, teks_id)\n        item['TeksArtiTR'] = caches['tr'].get(v_key, teks_id)"
    )

with open(dataset_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated {dataset_file} with Turkish metadata successfully!")
