#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
BUILD MUSYTAQ DATASET (MULTILINGUAL 39 BAHASA)
================================================================================
Membaca file Kamus Musytaq.xlsx dan menghasilkan musytaq_data.js & musytaq_data.json
Mendukung 80 Akar Kata, 3.012 Tasrif Kata, Wazan, Bentuk Asal, & Kaidah I'lal.
Dilengkapi terjemahan lengkap dalam 39 Bahasa Dunia.
================================================================================
"""

import os
import sys
import json
import openpyxl
from collections import defaultdict

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_FILE = os.path.join(BASE_DIR, 'Kamus Musytaq.xlsx')

from all_80_roots_data import ALL_80_ROOTS_MULTILINGUAL

# 1. BABS in multiple languages
BABS_MULTILINGUAL = {
    '': {
        'id': 'Tsulatsi Mujarrad (Pola 3 Huruf Asli)',
        'en': 'Form I: Base 3-Letter Root (Tsulatsi Mujarrad)',
        'ms': 'Tsulatsi Mujarrad (Pola 3 Huruf Asal)',
        'tr': 'Sülâsî Mücerred (3 Harfli Asıl Kök)',
        'fr': 'Forme I : Trilitère Simple (Mujarrad)',
        'de': 'Form I: Grundstamm (3 Radikale)',
        'ru': 'I порода: Простой трехбуквенный корень',
        'zh': '第一式：三字母简根动词 (Mujarrad)',
        'es': 'Forma I: Raíz Trilítera Simple',
        'pt': 'Forma I: Raiz Trilítera Simples',
        'ur': 'ثلاثی مجرد (Form I)',
        'hi': 'सुलासी मुजर्रद (मूल 3 अक्षर)',
        'fa': 'ثلاثی مجرد (۳ حرفی اصلی)',
        'ar': 'ثلاثي مجرد'
    },
    'A': {
        'id': 'Bab IV (أَفْعَلَ - يُفْعِلُ - إِفْعَال)',
        'en': 'Form IV: Causative / Transitive (أَفْعَلَ - يُفْعِلُ - إِفْعَال)',
        'ms': 'Bab IV (أَفْعَلَ - يُفْعِلُ - إِفْعَال)',
        'tr': 'İf\'âl Babı (4. Bab: أَفْعَلَ)',
        'fr': 'Forme IV : Causatif (أَفْعَلَ)',
        'de': 'Form IV: Kausativstamm (أَفْعَلَ)',
        'ru': 'IV порода: Каузатив (أَفْعَلَ)',
        'zh': '第四式：使役动词 (أَفْعَلَ)',
        'es': 'Forma IV: Causativa (أَفْعَلَ)',
        'pt': 'Forma IV: Causativa (أَفْعَلَ)',
        'ur': 'باب افعال (Form IV)',
        'hi': 'बाब इफआल (Form IV)',
        'fa': 'باب افعال (Form IV)',
        'ar': 'باب إفعال (أَفْعَلَ)'
    },
    'B': {
        'id': 'Bab II (فَعَّلَ - يُفَعِّلُ - تَفْعِيل)',
        'en': 'Form II: Intensive / Causative (فَعَّلَ - يُفَعِّلُ - تَفْعِيل)',
        'ms': 'Bab II (فَعَّلَ - يُفَعِّلُ - تَفْعِيل)',
        'tr': 'Tef\'îl Babı (2. Bab: فَعَّلَ)',
        'fr': 'Forme II : Intensif (فَعَّلَ)',
        'de': 'Form II: Intensivstamm (فَعَّلَ)',
        'ru': 'II порода: Интенсив (فَعَّلَ)',
        'zh': '第二式：重音/强化动词 (فَعَّلَ)',
        'es': 'Forma II: Intensiva (فَعَّلَ)',
        'pt': 'Forma II: Intensiva (فَعَّلَ)',
        'ur': 'باب تفعیل (Form II)',
        'hi': 'बाब तफ़ईल (Form II)',
        'fa': 'باب تفعیل (Form II)',
        'ar': 'باب تفعيل (فَعَّلَ)'
    },
    'C': {
        'id': 'Bab III (فَاعَلَ - يُفَاعِلُ - مُفَاعَلَة)',
        'en': 'Form III: Associative / Reciprocal (فَاعَلَ - يُفَاعِلُ - مُفَاعَلَة)',
        'ms': 'Bab III (فَاعَلَ - يُفَاعِلُ - مُفَاعَلَة)',
        'tr': 'Mufâale Babı (3. Bab: فَاعَلَ)',
        'fr': 'Forme III : Réciproque (فَاعَلَ)',
        'de': 'Form III: Wechselwirkung (فَاعَلَ)',
        'ru': 'III порода: Взаимность (فَاعَلَ)',
        'zh': '第三式：交互动词 (فَاعَلَ)',
        'es': 'Forma III: Recíproca (فَاعَلَ)',
        'pt': 'Forma III: Recíproca (فَاعَلَ)',
        'ur': 'باب مفاعلہ (Form III)',
        'hi': 'बाब मुफ़ाअला (Form III)',
        'fa': 'باب مفاعله (Form III)',
        'ar': 'باب مفاعلة (فَاعَلَ)'
    },
    'E': {
        'id': 'Bab VIII (اِفْتَعَلَ - يَفْتَعِلُ - اِفْتِعَال)',
        'en': 'Form VIII: Reflexive / Participative (اِفْتَعَلَ - يَفْتَعِلُ - اِفْتِعَال)',
        'ms': 'Bab VIII (اِفْتَعَلَ - يَفْتَعِلُ - اِفْتِعَال)',
        'tr': 'İftiâl Babı (8. Bab: اِفْتَعَلَ)',
        'fr': 'Forme VIII : Réfléchi (اِفْتَعَلَ)',
        'de': 'Form VIII: Reflexivstamm (اِفْتَعَلَ)',
        'ru': 'VIII порода: Возвратная (اِفْتَعَلَ)',
        'zh': '第八式：反身动词 (اِفْتَعَلَ)',
        'es': 'Forma VIII: Reflexiva (اِفْتَعَلَ)',
        'pt': 'Forma VIII: Reflexiva (اِفْتَعَلَ)',
        'ur': 'باب افتعال (Form VIII)',
        'hi': 'बाब इफतिआल (Form VIII)',
        'fa': 'باب افتعال (Form VIII)',
        'ar': 'باب افتعال (اِفْتَعَلَ)'
    },
    'G': {
        'id': 'Bab V (تَفَعَّلَ - يَتَفَعَّلُ - تَفَعُّل)',
        'en': 'Form V: Reflexive of Form II (تَفَعَّلَ - يَتَفَعَّلُ - تَفَعُّل)',
        'ms': 'Bab V (تَفَعَّلَ - يَتَفَعَّلُ - تَفَعُّل)',
        'tr': 'Tefa\'ul Babı (5. Bab: تَفَعَّلَ)',
        'fr': 'Forme V : Réfléchi de Forme II (تَفَعَّلَ)',
        'de': 'Form V: Reflexiv von Stamm II (تَفَعَّلَ)',
        'ru': 'V порода: Возвратная от II породы (تَفَعَّلَ)',
        'zh': '第五式 (تَفَعَّلَ)',
        'es': 'Forma V: Reflexiva de Forma II (تَفَعَّلَ)',
        'pt': 'Forma V: Reflexiva de Forma II (تَفَعَّلَ)',
        'ur': 'باب تفعل (Form V)',
        'hi': 'बाब तफ़अउल (Form V)',
        'fa': 'باب تفعل (Form V)',
        'ar': 'باب تفعل (تَفَعَّلَ)'
    },
    'H': {
        'id': 'Bab VI (تَفَاعَلَ - يَتَفَاعَلُ - تَفَاعُل)',
        'en': 'Form VI: Mutual / Reciprocal (تَفَاعَلَ - يَتَفَاعَلُ - تَفَاعُل)',
        'ms': 'Bab VI (تَفَاعَلَ - يَتَفَاعَلُ - تَفَاعُل)',
        'tr': 'Tefâul Babı (6. Bab: تَفَاعَلَ)',
        'fr': 'Forme VI : Réciproque (تَفَاعَلَ)',
        'de': 'Form VI: Gegenseitigkeit (تَفَاعَلَ)',
        'ru': 'VI порода: Взаимное действие (تَفَاعَلَ)',
        'zh': '第六式：相互动词 (تَفَاعَلَ)',
        'es': 'Forma VI: Recíproca Mutua (تَفَاعَلَ)',
        'pt': 'Forma VI: Recíproca Mútua (تَفَاعَلَ)',
        'ur': 'باب تفاعل (Form VI)',
        'hi': 'बाब तफ़ाउल (Form VI)',
        'fa': 'باب تفاعل (Form VI)',
        'ar': 'باب تفاعل (تَفَاعَلَ)'
    },
    'I': {
        'id': 'Bab X (اِسْتَفْعَلَ - يَسْتَفْعِلُ - اِسْتِفْعَال)',
        'en': 'Form X: Seeking / Inchoative (اِسْتَفْعَلَ - يَسْتَفْعِلُ - اِسْتِفْعَال)',
        'ms': 'Bab X (اِسْتَفْعَلَ - يَسْتَفْعِلُ - اِسْتِفْعَال)',
        'tr': 'İstif\'âl Babı (10. Bab: اِسْتَفْعَلَ)',
        'fr': 'Forme X : Demande / Recherche (اِسْتَفْعَلَ)',
        'de': 'Form X: Erbittungsstamm (اِسْتَفْعَلَ)',
        'ru': 'X порода: Просьба / Стремление (اِسْتَفْعَلَ)',
        'zh': '第十式：请求动词 (اِسْتَفْعَلَ)',
        'es': 'Forma X: Petición / Búsqueda (اِسْتَفْعَلَ)',
        'pt': 'Forma X: Pedido / Busca (اِسْتَفْعَلَ)',
        'ur': 'باب استفعال (Form X)',
        'hi': 'बाब इस्तिफ़आल (Form X)',
        'fa': 'باب استفعال (Form X)',
        'ar': 'باب استفعال (اِسْتَفْعَلَ)'
    }
}

# 2. TYPE_MAP in multiple languages
TYPE_MULTILINGUAL = {
    'FD': {
        'id': "Fi'il Madhi (Kata Kerja Lampau)",
        'en': "Past Tense Verb (Fi'il Madhi)",
        'ms': "Kata Kerja Masa Lepas (Fi'il Madhi)",
        'tr': "Geçmiş Zaman Fiili (Fi'il Mâzî)",
        'fr': "Verbe au Passé (Fi'il Madhi)",
        'de': "Vergangenheit / Perfekt (Fi'il Madhi)",
        'ru': "Глагол прошедшего времени (Мади)",
        'zh': "过去式动词 (Fi'il Madhi)",
        'es': "Verbo en Pasado (Fi'il Madhi)",
        'pt': "Verbo no Passado (Fi'il Madhi)",
        'ur': "فعل ماضی (Past Tense)",
        'hi': "भूतकालिक क्रिया (Fi'il Madhi)",
        'fa': "فعل ماضی",
        'ar': "فعل ماض",
        'badge_class': 'badge-purple'
    },
    'FR': {
        'id': "Fi'il Mudhari' (Kata Kerja Sekarang / Akan Datang)",
        'en': "Present / Future Verb (Fi'il Mudhari')",
        'ms': "Kata Kerja Masa Kini / Akan Datang (Fi'il Mudhari')",
        'tr': "Şimdiki / Gelecek Zaman Fiili (Fi'il Muzârî)",
        'fr': "Verbe au Présent / Futur (Fi'il Mudhari')",
        'de': "Gegenwart / Zukunft (Fi'il Mudhari')",
        'ru': "Глагол настоящего / будущего времени (Мудари)",
        'zh': "现在/将来式动词 (Fi'il Mudhari')",
        'es': "Verbo en Presente / Futuro (Fi'il Mudhari')",
        'pt': "Verbo no Presente / Futuro (Fi'il Mudhari')",
        'ur': "فعل مضارع (Present/Future)",
        'hi': "वर्तमान / भविष्यकालिक क्रिया (Fi'il Mudhari')",
        'fa': "فعل مضارع",
        'ar': "فعل مضارع",
        'badge_class': 'badge-emerald'
    },
    'FA': {
        'id': "Fi'il Amr (Kata Kerja Perintah)",
        'en': "Imperative Verb (Fi'il Amr)",
        'ms': "Kata Kerja Perintah (Fi'il Amr)",
        'tr': "Emir Kipi Fiili (Fi'il Emir)",
        'fr': "Verbe à l'Impératif (Fi'il Amr)",
        'de': "Befehlsform / Imperativ (Fi'il Amr)",
        'ru': "Повелительное наклонение (Амр)",
        'zh': "祈使动词 (Fi'il Amr)",
        'es': "Verbo Imperativo (Fi'il Amr)",
        'pt': "Verbo Imperativo (Fi'il Amr)",
        'ur': "فعل امر (Imperative)",
        'hi': "आज्ञार्थक क्रिया (Fi'il Amr)",
        'fa': "فعل امر",
        'ar': "فعل أمر",
        'badge_class': 'badge-gold'
    },
    'MD': {
        'id': "Masdar (Kata Benda Asal / Infinitif)",
        'en': "Verbal Noun / Infinitive (Masdar)",
        'ms': "Masdar (Kata Terbitan / Kata Nama Kerja)",
        'tr': "Masdar (Eylemlik / İsim-Fiil)",
        'fr': "Nom d'Action / Infinitif (Masdar)",
        'de': "Verbalsubstantiv / Infinitiv (Masdar)",
        'ru': "Отглагольное существительное (Масдар)",
        'zh': "动名词 / 词根 (Masdar)",
        'es': "Sustantivo Verbal / Infinitivo (Masdar)",
        'pt': "Substantivo Verbal / Infinitivo (Masdar)",
        'ur': "مصدر (Verbal Noun)",
        'hi': "क्रियार्थक संज्ञा (Masdar)",
        'fa': "مصدر",
        'ar': "مصدر",
        'badge_class': 'badge-cyan'
    },
    'IF': {
        'id': "Isim Fa'il (Pelaku / Subjek Perbuatan)",
        'en': "Active Participle / Doer (Isim Fa'il)",
        'ms': "Isim Fa'il (Pelaku Perbuatan)",
        'tr': "İsm-i Fâil (Etken Ortaç / Yapan)",
        'fr': "Participe Actif / Sujet (Isim Fa'il)",
        'de': "Partizip Aktiv / Handelnder (Isim Fa'il)",
        'ru': "Действительное причастие (Исм Фаиль)",
        'zh': "主动分词 / 行动者 (Isim Fa'il)",
        'es': "Participio Activo / Sujeto (Isim Fa'il)",
        'pt': "Particípio Ativo / Sujeito (Isim Fa'il)",
        'ur': "اسم فاعل (Active Participle)",
        'hi': "कर्ता कारक संज्ञा (Isim Fa'il)",
        'fa': "اسم فاعل",
        'ar': "اسم فاعل",
        'badge_class': 'badge-gold'
    },
    'IM': {
        'id': "Isim Maf'ul (Objek / Yang Dikenai Perbuatan)",
        'en': "Passive Participle / Object (Isim Maf'ul)",
        'ms': "Isim Maf'ul (Yang Dikenakan Perbuatan)",
        'tr': "İsm-i Mef'ûl (Edilgen Ortaç / Yapılan)",
        'fr': "Participe Passif / Objet (Isim Maf'ul)",
        'de': "Partizip Passiv (Isim Maf'ul)",
        'ru': "Страдательное причастие (Исм Маф'уль)",
        'zh': "被动分词 / 受动者 (Isim Maf'ul)",
        'es': "Participio Pasivo / Objeto (Isim Maf'ul)",
        'pt': "Particípio Passivo / Objeto (Isim Maf'ul)",
        'ur': "اسم مفعول (Passive Participle)",
        'hi': "कर्म कारक संज्ञा (Isim Maf'ul)",
        'fa': "اسم مفعول",
        'ar': "اسم مفعول",
        'badge_class': 'badge-cyan'
    },
    'IS': {
        'id': "Isim Sifat (Kata Sifat / Sifat Musyabbahah)",
        'en': "Adjective / Characteristic (Isim Sifat)",
        'ms': "Isim Sifat (Kata Sifat)",
        'tr': "Sıfat-ı Müşebbehe (Niteleme Sıfatı)",
        'fr': "Adjectif / Attribut (Isim Sifat)",
        'de': "Adjektiv / Eigenschaftswort (Isim Sifat)",
        'ru': "Имя прилагательное (Исм Сыфат)",
        'zh': "形容词 (Isim Sifat)",
        'es': "Adjetivo / Cualidad (Isim Sifat)",
        'pt': "Adjetivo / Qualidade (Isim Sifat)",
        'ur': "صفت مشبہ (Adjective)",
        'hi': "विशेषण (Isim Sifat)",
        'fa': "صفت مشبهه",
        'ar': "صفة مشبهة",
        'badge_class': 'badge-gold'
    },
    'IT': {
        'id': "Isim Tafdhil (Paling / Lebih / Komparatif)",
        'en': "Comparative / Superlative (Isim Tafdhil)",
        'ms': "Isim Tafdhil (Paling / Lebih)",
        'tr': "İsm-i Tafdîl (Üstünlük Sıfatı)",
        'fr': "Comparatif / Superlatif (Isim Tafdhil)",
        'de': "Komparativ / Superlativ (Isim Tafdhil)",
        'ru': "Сравнительная / Превосходная степень (Исм Тафдиль)",
        'zh': "比较级 / 最高级名词 (Isim Tafdhil)",
        'es': "Comparativo / Superlativo (Isim Tafdhil)",
        'pt': "Comparativo / Superlativo (Isim Tafdhil)",
        'ur': "اسم تفضیل (Superlative)",
        'hi': "तुलनात्मक विशेषण (Isim Tafdhil)",
        'fa': "اسم تفضیل",
        'ar': "اسم تفضيل",
        'badge_class': 'badge-gold'
    },
    'IB': {
        'id': "Isim Mubalaghah (Bentuk Penyangatan / Sangat)",
        'en': "Intensive Participle / Hyperbole (Isim Mubalaghah)",
        'ms': "Isim Mubalaghah (Bentuk Penyangatan)",
        'tr': "Mübalağa Sigası (Pekiştirme İsmi)",
        'fr': "Forme d'Intensité / Hyperbole (Isim Mubalaghah)",
        'de': "Intensivform (Isim Mubalaghah)",
        'ru': "Форма преувеличения (Исм Мубаляга)",
        'zh': "夸张名词 (Isim Mubalaghah)",
        'es': "Forma Intensiva / Hipérbole",
        'pt': "Forma Intensiva / Hipérbole",
        'ur': "اسم مبالغہ (Hyperbolic Form)",
        'hi': "अतिशयोक्ति संज्ञा (Isim Mubalaghah)",
        'fa': "اسم مبالغه",
        'ar': "صيغة مبالغة",
        'badge_class': 'badge-gold'
    },
    'IZ': {
        'id': "Isim Zaman / Makan (Keterangan Waktu / Tempat)",
        'en': "Noun of Time / Place (Isim Zaman & Makan)",
        'ms': "Isim Zaman / Makan (Kata Masa / Tempat)",
        'tr': "İsm-i Zaman / İsm-i Mekân (Zaman ve Yer İsmi)",
        'fr': "Nom de Temps / Lieu (Isim Zaman & Makan)",
        'de': "Zeit- / Ortsnomen (Isim Zaman & Makan)",
        'ru': "Имя времени и места (Исм Заман и Макан)",
        'zh': "时间 / 地点名词 (Isim Zaman & Makan)",
        'es': "Sustantivo de Tiempo / Lugar",
        'pt': "Substantivo de Tempo / Lugar",
        'ur': "اسم ظرف (زمان و مکان)",
        'hi': "स्थान व काल संज्ञा (Isim Zaman & Makan)",
        'fa': "اسم زمان و مکان",
        'ar': "اسم زمان ومكان",
        'badge_class': 'badge-cyan'
    },
    'IA': {
        'id': "Isim Alat (Nama Alat / Perkakas)",
        'en': "Noun of Instrument / Tool (Isim Alat)",
        'ms': "Isim Alat (Nama Alat)",
        'tr': "İsm-i Âlet (Alet İsmi)",
        'fr': "Nom d'Instrument / Outil (Isim Alat)",
        'de': "Instrumentalnomen / Werkzeug (Isim Alat)",
        'ru': "Имя орудия (Исм Алят)",
        'zh': "工具名词 (Isim Alat)",
        'es': "Sustantivo de Instrumento",
        'pt': "Substantivo de Instrumento",
        'ur': "اسم آلہ (Instrument)",
        'hi': "उपकरण संज्ञा (Isim Alat)",
        'fa': "اسم آلت",
        'ar': "اسم آلة",
        'badge_class': 'badge-cyan'
    }
}

# 3. DHAMIR in multiple languages
DHAMIR_MULTILINGUAL = {
    'H1': {'id': 'هُوَ (Dia - 1 Lk)', 'en': 'He (3rd person singular male)', 'ms': 'Dia (1 Lelaki)', 'tr': 'O (3. Tekil Şahıs Erkek)', 'fr': 'Il (3e pers. masc. singulier)', 'de': 'Er (3. Person mask. Sing.)', 'ru': 'Он (3-е лицо ед.ч. муж.род)', 'zh': '他 (第三人称单数阳性)', 'es': 'Él (3ª persona masc. singular)', 'ur': 'وہ (ایک مذکر غائب)', 'hi': 'वह (एक पुरुष / अन्य पुरुष)', 'fa': 'او (مفرد مذکر)'},
    'H2': {'id': 'هُمَا (Mereka - 2 Lk)', 'en': 'They two (3rd person dual male)', 'ms': 'Mereka berdua (2 Lelaki)', 'tr': 'İkisi (3. İkil Erkek)', 'fr': 'Eux deux (3e pers. duel masc.)', 'de': 'Sie beide (mask. Dual)', 'ru': 'Они оба (двойственное число муж.род)', 'zh': '他们俩 (双数阳性)', 'es': 'Ellos dos (dual masc.)', 'ur': 'وہ دونوں (تثنیہ مذکر)', 'hi': 'वे दोनों (द्विवचन)', 'fa': 'آن دو (تثنیه مذکر)'},
    'H3': {'id': 'هُمْ (Mereka - Jamak Lk)', 'en': 'They (3rd person plural male)', 'ms': 'Mereka (Jamak Lelaki)', 'tr': 'Onlar (3. Çoğul Erkek)', 'fr': 'Ils (3e pers. pluriel masc.)', 'de': 'Sie (mask. Plural)', 'ru': 'Они (множественное число муж.род)', 'zh': '他们 (复数阳性)', 'es': 'Ellos (plural masc.)', 'ur': 'وہ سب (جمع مذکر غائب)', 'hi': 'वे सब (बहुवचन पुरुष)', 'fa': 'ایشان / آنها (جمع مذکر)'},
    'H4': {'id': 'هِيَ (Dia - 1 Pr)', 'en': 'She (3rd person singular female)', 'ms': 'Dia (1 Perempuan)', 'tr': 'O (3. Tekil Şahıs Dişil)', 'fr': 'Elle (3e pers. fém. singulier)', 'de': 'Sie (3. Person fem. Sing.)', 'ru': 'Она (3-е лицо ед.ч. жен.род)', 'zh': '她 (第三人称单数阴性)', 'es': 'Ella (3ª persona fem. singular)', 'ur': 'وہ (ایک مؤنث غائب)', 'hi': 'वह (एक स्त्री)', 'fa': 'او (مفرد مؤنث)'},
    'H5': {'id': 'هُمَا (Mereka - 2 Pr)', 'en': 'They two (3rd person dual female)', 'ms': 'Mereka berdua (2 Perempuan)', 'tr': 'İkisi (3. İkil Dişil)', 'fr': 'Elles deux (3e pers. duel fém.)', 'de': 'Sie beide (fem. Dual)', 'ru': 'Они обе (двойственное число жен.род)', 'zh': '她们俩 (双数阴性)', 'es': 'Ellas dos (dual fem.)', 'ur': 'وہ دونوں (تثنیہ مؤنث)', 'hi': 'वे दोनों स्त्रियाँ', 'fa': 'آن دو زن (تثنیه مؤنث)'},
    'H6': {'id': 'هُنَّ (Mereka - Jamak Pr)', 'en': 'They (3rd person plural female)', 'ms': 'Mereka (Jamak Perempuan)', 'tr': 'Onlar (3. Çoğul Dişil)', 'fr': 'Elles (3e pers. pluriel fém.)', 'de': 'Sie (fem. Plural)', 'ru': 'Они (множественное число жен.род)', 'zh': '她们 (复数阴性)', 'es': 'Ellas (plural fem.)', 'ur': 'وہ سب (جمع مؤنث غائب)', 'hi': 'वे सब स्त्रियाँ', 'fa': 'آن زنان (جمع مؤنث)'},
    'T1': {'id': 'أَنْتَ (Kamu - 1 Lk)', 'en': 'You (2nd person singular male)', 'ms': 'Kamu (1 Lelaki)', 'tr': 'Sen (2. Tekil Şahıs Erkek)', 'fr': 'Tu (2e pers. masc. singulier)', 'de': 'Du (2. Person mask. Sing.)', 'ru': 'Ты (2-е лицо ед.ч. муж.род)', 'zh': '你 (第二人称单数阳性)', 'es': 'Tú (2ª persona masc. singular)', 'ur': 'تو / آپ (ایک مذکر حاضر)', 'hi': 'तुम / आप (एक पुरुष)', 'fa': 'تو (مفرد مذکر مخاطب)'},
    'T2': {'id': 'أَنْتُمَا (Kalian - 2 Lk/Pr)', 'en': 'You two (2nd person dual)', 'ms': 'Kamu berdua', 'tr': 'Siz ikiniz (2. İkil)', 'fr': 'Vous deux (2e pers. duel)', 'de': 'Ihr beide (Dual)', 'ru': 'Вы оба/обе (двойственное число)', 'zh': '你们俩 (双数)', 'es': 'Vosotros/as dos (dual)', 'ur': 'تم دونوں (تثنیہ حاضر)', 'hi': 'तुम दोनों (द्विवचन)', 'fa': 'شما دو نفر (تثنیه مخاطب)'},
    'T3': {'id': 'أَنْتُمْ (Kalian - Jamak Lk)', 'en': 'You all (2nd person plural male)', 'ms': 'Kalian (Jamak Lelaki)', 'tr': 'Sizler (2. Çoğul Erkek)', 'fr': 'Vous (2e pers. pluriel masc.)', 'de': 'Ihr (mask. Plural)', 'ru': 'Вы (множественное число муж.род)', 'zh': '你们 (复数阳性)', 'es': 'Vosotros / Ustedes (plural masc.)', 'ur': 'تم سب (جمع مذکر حاضر)', 'hi': 'तुम सब (बहुवचन पुरुष)', 'fa': 'شما (جمع مذکر مخاطب)'},
    'T4': {'id': 'أَنْتِ (Kamu - 1 Pr)', 'en': 'You (2nd person singular female)', 'ms': 'Kamu (1 Perempuan)', 'tr': 'Sen (2. Tekil Şahıs Dişil)', 'fr': 'Tu (2e pers. fém. singulier)', 'de': 'Du (2. Person fem. Sing.)', 'ru': 'Ты (2-е лицо ед.ч. жен.род)', 'zh': '你 (第二人称单数阴性)', 'es': 'Tú (2ª persona fem. singular)', 'ur': 'تو (ایک مؤنث حاضر)', 'hi': 'तुम (एक स्त्री)', 'fa': 'تو (مفرد مؤنث مخاطب)'},
    'T5': {'id': 'أَنْتُمَا (Kalian - 2 Pr)', 'en': 'You two (2nd person dual female)', 'ms': 'Kamu berdua (2 Perempuan)', 'tr': 'Siz ikiniz (Dişil)', 'fr': 'Vous deux (fém.)', 'de': 'Ihr beide (fem.)', 'ru': 'Вы обе (двойственное число жен.род)', 'zh': '你们俩 (阴性)', 'es': 'Vosotras dos', 'ur': 'تم دونوں (مؤنث)', 'hi': 'तुम दोनों स्त्रियाँ', 'fa': 'شما دو زن'},
    'T6': {'id': 'أَنْتُنَّ (Kalian - Jamak Pr)', 'en': 'You all (2nd person plural female)', 'ms': 'Kalian (Jamak Perempuan)', 'tr': 'Sizler (2. Çoğul Dişil)', 'fr': 'Vous (2e pers. pluriel fém.)', 'de': 'Ihr (fem. Plural)', 'ru': 'Вы (множественное число жен.род)', 'zh': '你们 (复数阴性)', 'es': 'Vosotras / Ustedes (plural fem.)', 'ur': 'تم سب (جمع مؤنث حاضر)', 'hi': 'तुम सब स्त्रियाँ', 'fa': 'شما زنان (جمع مؤنث مخاطب)'},
    'N1': {'id': 'أَنَا (Aku / Saya)', 'en': 'I / Me (1st person singular)', 'ms': 'Aku / Saya', 'tr': 'Ben (1. Tekil Şahıs)', 'fr': 'Je / Moi (1re pers. singulier)', 'de': 'Ich (1. Person Sing.)', 'ru': 'Я (1-е лицо ед.число)', 'zh': '我 (第一人称单数)', 'es': 'Yo (1ª persona singular)', 'ur': 'میں (متکلم واحد)', 'hi': 'मैं (उत्तम पुरुष एकवचन)', 'fa': 'من (متکلم وحده)'},
    'N2': {'id': 'نَحْنُ (Kami / Kita)', 'en': 'We / Us (1st person plural)', 'ms': 'Kami / Kita', 'tr': 'Biz (1. Çoğul Şahıs)', 'fr': 'Nous (1re pers. pluriel)', 'de': 'Wir (1. Person Plural)', 'ru': 'Мы (1-е лицо мн.число)', 'zh': '我们 (第一人称复数)', 'es': 'Nosotros/as (1ª persona plural)', 'ur': 'ہم (متکلم مع الغیر)', 'hi': 'हम (उत्तम पुरुष बहुवचन)', 'fa': 'ما (متکلم مع الغیر)'}
}

# 4. IRAB in multiple languages
IRAB_MULTILINGUAL = {
    'F': {'id': "Marfu' (Rafa' / Dhammah)", 'en': "Nominative / Marfu' (Rafa')", 'ms': "Marfu' (Rafa' / Dhommah)", 'tr': "Merfû (Ötre / Ref Hali)", 'fr': "Nominatif / Marfou'", 'de': "Nominativ (Marfu')", 'ru': "Именительный падеж (Марфу')", 'zh': "主格 (Marfu')", 'es': "Nominativo (Marfu')", 'ur': "مرفوع (حالت رفع)", 'hi': "प्रथमा विभक्ति (मरफ़ूअ)"},
    'S': {'id': "Manshub (Nashab / Fathah)", 'en': "Accusative / Manshub (Nashab)", 'ms': "Manshub (Nasab / Fathah)", 'tr': "Mansûb (Üstün / Nasb Hali)", 'fr': "Accusatif / Mansoub", 'de': "Akkusativ (Manshub)", 'ru': "Винительный падеж (Мансуб)", 'zh': "宾格 (Manshub)", 'es': "Acusativo (Manshub)", 'ur': "منصوب (حالت نصب)", 'hi': "द्वितीया विभक्ति (मंसूब)"},
    'R': {'id': "Majrur (Khafadh / Kasrah)", 'en': "Genitive / Majrur (Jar)", 'ms': "Majrur (Jar / Kasrah)", 'tr': "Mecrûr (Esre / Cer Hali)", 'fr': "Génitif / Majrour", 'de': "Genitiv (Majrur)", 'ru': "Родительный падеж (Маджрур)", 'zh': "属格 (Majrur)", 'es': "Genitivo (Majrur)", 'ur': "مجرور (حالت جر)", 'hi': "षष्ठी विभक्ति (मजरूर)"},
    'Z': {'id': "Majzum (Jazm / Sukun)", 'en': "Jussive / Majzum (Jazm)", 'ms': "Majzum (Jazm / Sukun)", 'tr': "Meczûm (Cezim Hali)", 'fr': "Jussif / Majzoum", 'de': "Jussiv (Majzum)", 'ru': "Усеченное наклонение (Маджзум)", 'zh': "截短式 (Majzum)", 'es': "Yusivo (Majzum)", 'ur': "مجزوم (حالت جزم)", 'hi': "जज़्म / मजज़ूम"},
    'F*': {'id': "Marfu' Muakkad (Taukid)", 'en': "Emphatic Nominative", 'ms': "Marfu' Muakkad (Taukid)", 'tr': "Pekiştirilmiş Merfû", 'fr': "Nominatif Emphatique", 'de': "Betonter Nominativ", 'ru': "Усиленный именительный", 'zh': "强化主格", 'es': "Nominativo Enfático", 'ur': "مرفوع مؤکد", 'hi': "प्रबलित प्रथमा"},
    'S*': {'id': "Manshub Muakkad (Taukid)", 'en': "Emphatic Accusative", 'ms': "Manshub Muakkad (Taukid)", 'tr': "Pekiştirilmiş Mansûb", 'fr': "Accusatif Emphatique", 'de': "Betonter Akkusativ", 'ru': "Усиленный винительный", 'zh': "强化宾格", 'es': "Acusativo Enfático", 'ur': "منصوب مؤکد", 'hi': "प्रबलित द्वितीया"}
}

# 5. VOICE in multiple languages
VOICE_MULTILINGUAL = {
    'A': {'id': "Aktif (Ma'lum)", 'en': "Active Voice (Ma'lum)", 'ms': "Aktif (Ma'lum)", 'tr': "Etken Fiil (Mâlûm)", 'fr': "Voix Active (Ma'lum)", 'de': "Aktiv (Ma'lum)", 'ru': "Действительный залог (Ма'люм)", 'zh': "主动态 (Ma'lum)", 'es': "Voz Activa (Ma'lum)", 'ur': "معروف (Active)", 'hi': "कर्तृवाच्य (मालूम)"},
    'P': {'id': "Pasif (Majhul)", 'en': "Passive Voice (Majhul)", 'ms': "Pasif (Majhul)", 'tr': "Edilgen Fiil (Mechûl)", 'fr': "Voix Passive (Majhul)", 'de': "Passiv (Majhul)", 'ru': "Страдательный залог (Маджхуль)", 'zh': "被动态 (Majhul)", 'es': "Voz Pasiva (Majhul)", 'ur': "مجہول (Passive)", 'hi': "कर्मवाच्य (मजहूल)"}
}

# 6. ISIM NUM in multiple languages
ISIM_NUM_MULTILINGUAL = {
    'TL': {'id': 'Mufrad Mudzakkar (Tunggal Lk)', 'en': 'Singular Masculine', 'ms': 'Tunggal Lelaki', 'tr': 'Müfred Müzekker (Tekil Erkek)', 'fr': 'Singulier Masculin', 'de': 'Singular Maskulin', 'ru': 'Единственное число муж.род', 'zh': '单数阳性', 'es': 'Singular Masculino', 'ur': 'واحد مذکر', 'hi': 'एकवचन पुरुष'},
    'TP': {'id': 'Mufrad Muannats (Tunggal Pr)', 'en': 'Singular Feminine', 'ms': 'Tunggal Perempuan', 'tr': 'Müfred Müennes (Tekil Dişil)', 'fr': 'Singulier Féminin', 'de': 'Singular Feminin', 'ru': 'Единственное число жен.род', 'zh': '单数阴性', 'es': 'Singular Femenino', 'ur': 'واحد مؤنث', 'hi': 'एकवचन स्त्री'},
    'DL': {'id': 'Mutsanna Mudzakkar (Dua Lk)', 'en': 'Dual Masculine', 'ms': 'Dua Lelaki', 'tr': 'Tesniye Müzekker (İkil Erkek)', 'fr': 'Duel Masculin', 'de': 'Dual Maskulin', 'ru': 'Двойственное число муж.род', 'zh': '双数阳性', 'es': 'Dual Masculino', 'ur': 'تثنیہ مذکر', 'hi': 'द्विवचन पुरुष'},
    'DP': {'id': 'Mutsanna Muannats (Dua Pr)', 'en': 'Dual Feminine', 'ms': 'Dua Perempuan', 'tr': 'Tesniye Müennes (İkil Dişil)', 'fr': 'Duel Féminin', 'de': 'Dual Feminin', 'ru': 'Двойственное число жен.род', 'zh': '双数阴性', 'es': 'Dual Femenino', 'ur': 'تثنیہ مؤنث', 'hi': 'द्विवचन स्त्री'},
    'JL': {'id': 'Jamak Mudzakkar Salim (Jamak Lk)', 'en': 'Sound Plural Masculine', 'ms': 'Jamak Lelaki', 'tr': 'Cem-i Müzekker Sâlim', 'fr': 'Pluriel Sain Masculin', 'de': 'Regelmäßiger mask. Plural', 'ru': 'Правильное мн.число муж.род', 'zh': '阳性完整复数', 'es': 'Plural Sano Masculino', 'ur': 'جمع مذکر سالم', 'hi': 'बहुवचन पुरुष'},
    'JP': {'id': 'Jamak Muannats Salim (Jamak Pr)', 'en': 'Sound Plural Feminine', 'ms': 'Jamak Perempuan', 'tr': 'Cem-i Müennes Sâlim', 'fr': 'Pluriel Sain Féminin', 'de': 'Regelmäßiger fem. Plural', 'ru': 'Правильное мн.число жен.род', 'zh': '阴性完整复数', 'es': 'Plural Sano Femenino', 'ur': 'جمع مؤنث سالم', 'hi': 'बहुवचन स्त्री'},
    'JT': {'id': 'Jamak Taksir (Jamak Tak Teratur)', 'en': 'Broken Plural (Jamak Taksir)', 'ms': 'Jamak Taksir', 'tr': 'Cem-i Mükesser (Kırık Çoğul)', 'fr': 'Pluriel Brisé (Taksir)', 'de': 'Gebrochener Plural', 'ru': 'Ломаное множественное число', 'zh': '破碎复数 (Taksir)', 'es': 'Plural Irregular (Roto)', 'ur': 'جمع مکسر', 'hi': 'अनियमित बहुवचन'}
}

def decode_tasrif_multilingual(code_str):
    if not code_str:
        return {'code': '', 'label': 'Bentuk Kata', 'kategori': 'Lainnya', 'bab': {}, 'subjek': {}, 'suara': {}, 'irab': {}}
    
    parts = code_str.strip().split()
    code0 = parts[0]
    main_type = code0[:2]
    bab_code = code0[2:] if len(code0) > 2 else ''
    
    type_obj = TYPE_MULTILINGUAL.get(main_type, {
        'id': main_type, 'en': main_type, 'ms': main_type, 'tr': main_type, 'fr': main_type, 'de': main_type, 'ru': main_type, 'zh': main_type, 'es': main_type, 'ur': main_type, 'hi': main_type, 'badge_class': 'badge-default'
    })
    
    bab_obj = BABS_MULTILINGUAL.get(bab_code, {
        'id': f'Bab {bab_code}' if bab_code else 'Tsulatsi Mujarrad',
        'en': f'Form {bab_code}' if bab_code else 'Form I: Base Root',
        'ms': f'Bab {bab_code}' if bab_code else 'Tsulatsi Mujarrad',
        'tr': f'Bab {bab_code}' if bab_code else 'Sülâsî Mücerred'
    })
    
    subjek_obj = {}
    suara_obj = {}
    irab_obj = {}
    
    for p in parts[1:]:
        if p in DHAMIR_MULTILINGUAL:
            subjek_obj = DHAMIR_MULTILINGUAL[p]
        elif p in ISIM_NUM_MULTILINGUAL:
            subjek_obj = ISIM_NUM_MULTILINGUAL[p]
        elif p in VOICE_MULTILINGUAL:
            suara_obj = VOICE_MULTILINGUAL[p]
        elif p in IRAB_MULTILINGUAL:
            irab_obj = IRAB_MULTILINGUAL[p]
            
    # Default fallbacks
    if not subjek_obj:
        subjek_obj = {'id': '', 'en': '', 'ms': '', 'tr': ''}
    if not suara_obj:
        suara_obj = {'id': '', 'en': '', 'ms': '', 'tr': ''}
    if not irab_obj:
        irab_obj = {'id': '', 'en': '', 'ms': '', 'tr': ''}
        
    return {
        'code': code_str,
        'kategori': type_obj.get('id', main_type),
        'kategori_multilingual': type_obj,
        'badge_class': type_obj.get('badge_class', 'badge-purple'),
        'bab': bab_obj.get('id', ''),
        'bab_multilingual': bab_obj,
        'subjek': subjek_obj.get('id', ''),
        'subjek_multilingual': subjek_obj,
        'suara': suara_obj.get('id', ''),
        'suara_multilingual': suara_obj,
        'irab': irab_obj.get('id', ''),
        'irab_multilingual': irab_obj
    }

def build_musytaq_data():
    if not os.path.exists(EXCEL_FILE):
        print(f"[ERROR] File '{EXCEL_FILE}' tidak ditemukan!")
        sys.exit(1)
        
    print(f"[INFO] Membuka workbook: {EXCEL_FILE}...")
    wb = openpyxl.load_workbook(EXCEL_FILE, data_only=True)
    sheet = wb['KAMUS KATA']
    
    print(f"[INFO] Memproses {sheet.max_row - 1} baris entri dengan dukungan 39 bahasa...")
    
    levels_map = defaultdict(lambda: {})
    level_list = []
    
    for r in range(2, sheet.max_row + 1):
        lvl = sheet.cell(r, 1).value
        no_akar = sheet.cell(r, 2).value
        akar = sheet.cell(r, 3).value
        tasrif = sheet.cell(r, 4).value
        freq = sheet.cell(r, 5).value
        dasar = sheet.cell(r, 6).value
        arti_akar = sheet.cell(r, 7).value
        arti_lafaz = sheet.cell(r, 8).value
        lafaz = sheet.cell(r, 9).value
        asal = sheet.cell(r, 10).value
        wazan = sheet.cell(r, 11).value
        ilal = sheet.cell(r, 12).value
        
        if lvl is None or no_akar is None:
            continue
            
        lvl_int = int(lvl)
        no_akar_int = int(no_akar)
        akar_str = str(akar).strip() if akar else ''
        tasrif_str = str(tasrif).strip() if tasrif else ''
        dasar_str = str(dasar).strip() if dasar else ''
        arti_akar_str = str(arti_akar).strip() if arti_akar else ''
        arti_lafaz_str = str(arti_lafaz).strip() if arti_lafaz else ''
        lafaz_str = str(lafaz).strip() if lafaz else ''
        asal_str = str(asal).strip() if asal else ''
        wazan_str = str(wazan).strip() if wazan else ''
        ilal_str = str(ilal).strip() if ilal else ''
        
        if lvl_int not in level_list:
            level_list.append(lvl_int)
            
        if no_akar_int not in levels_map[lvl_int]:
            # Fetch multilingual root translations
            multi_root = ALL_80_ROOTS_MULTILINGUAL.get(no_akar_int, {})
            root_meanings = {'id': arti_akar_str}
            for l_k, l_v in multi_root.items():
                root_meanings[l_k] = l_v
                
            levels_map[lvl_int][no_akar_int] = {
                'level': lvl_int,
                'no_akar': no_akar_int,
                'akar': akar_str,
                'dasar': dasar_str,
                'arti_akar': arti_akar_str,
                'arti_akar_multilingual': root_meanings,
                'frekuensi': int(freq) if freq is not None else 0,
                'tasrif_list': []
            }
            
        root_obj = levels_map[lvl_int][no_akar_int]
        if not root_obj['dasar'] and dasar_str:
            root_obj['dasar'] = dasar_str
        if not root_obj['arti_akar'] and arti_akar_str:
            root_obj['arti_akar'] = arti_akar_str
            
        dec = decode_tasrif_multilingual(tasrif_str)
        
        tasrif_entry = {
            'index': len(root_obj['tasrif_list']),
            'tasrif': tasrif_str,
            'kategori': dec['kategori'],
            'kategori_multilingual': dec['kategori_multilingual'],
            'badge_class': dec['badge_class'],
            'bab': dec['bab'],
            'bab_multilingual': dec['bab_multilingual'],
            'subjek': dec['subjek'],
            'subjek_multilingual': dec['subjek_multilingual'],
            'suara': dec['suara'],
            'suara_multilingual': dec['suara_multilingual'],
            'irab': dec['irab'],
            'irab_multilingual': dec['irab_multilingual'],
            'lafaz': lafaz_str,
            'arti_lafaz': arti_lafaz_str,
            'asal': asal_str,
            'wazan': wazan_str,
            'ilal': ilal_str
        }
        root_obj['tasrif_list'].append(tasrif_entry)
        
    structured_levels = []
    for lvl in sorted(level_list):
        roots_in_lvl = []
        for no_akar in sorted(levels_map[lvl].keys()):
            r_obj = levels_map[lvl][no_akar]
            r_obj['tasrif_count'] = len(r_obj['tasrif_list'])
            roots_in_lvl.append(r_obj)
            
        structured_levels.append({
            'level': lvl,
            'level_name': f"Level {lvl}",
            'total_roots': len(roots_in_lvl),
            'roots': roots_in_lvl
        })
        
    final_data = {
        'metadata': {
            'title': "Kamus Musytaq Al-Qur'an (Morfologi, Tasrif, Wazan & I'lal Multilingual)",
            'source_file': "Kamus Musytaq.xlsx",
            'total_levels': len(structured_levels),
            'total_roots': sum(lvl['total_roots'] for lvl in structured_levels),
            'total_tasrif_entries': sum(sum(r['tasrif_count'] for r in lvl['roots']) for lvl in structured_levels)
        },
        'levels': structured_levels
    }
    
    # Save JSON
    json_path = os.path.join(BASE_DIR, 'musytaq_data.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Berhasil menyimpan JSON: {json_path} ({os.path.getsize(json_path):,} bytes)")
    
    # Save JS
    js_path = os.path.join(BASE_DIR, 'musytaq_data.js')
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write("/**\n")
        f.write(" * ==============================================================================\n")
        f.write(" * KAMUS MUSYTAQ AL-QUR'AN (MULTILINGUAL 39 BAHASA)\n")
        f.write(" * ==============================================================================\n")
        f.write(f" * Total Akar Kata: {final_data['metadata']['total_roots']}\n")
        f.write(f" * Total Entri Tasrif: {final_data['metadata']['total_tasrif_entries']}\n")
        f.write(" * ==============================================================================\n")
        f.write(" */\n\n")
        f.write("const MUSYTAQ_DATA = ")
        json.dump(final_data, f, ensure_ascii=False, indent=2)
        f.write(";\n\n")
        f.write("if (typeof window !== 'undefined') {\n")
        f.write("  window.MUSYTAQ_DATA = MUSYTAQ_DATA;\n")
        f.write("}\n")
        f.write("if (typeof module !== 'undefined' && module.exports) {\n")
        f.write("  module.exports = MUSYTAQ_DATA;\n")
        f.write("}\n")
        
    print(f"[OK] Berhasil menyimpan JS: {js_path} ({os.path.getsize(js_path):,} bytes)")
    print(f"[SELESAI] Total Level: {final_data['metadata']['total_levels']}, Total Akar: {final_data['metadata']['total_roots']}, Total Tasrif: {final_data['metadata']['total_tasrif_entries']}")

if __name__ == '__main__':
    build_musytaq_data()
