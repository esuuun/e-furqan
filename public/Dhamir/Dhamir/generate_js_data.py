import openpyxl
import json

with open('d:/Dhamir/dhamir_data.json', encoding='utf-8') as f:
    raw_data = json.load(f)

# Surah database (1-114)
surahs = {
    1: {'nama': 'Al-Fatihah', 'arab': 'الفاتحة', 'arti': 'Pembukaan', 'ayat': 7},
    2: {'nama': 'Al-Baqarah', 'arab': 'البقرة', 'arti': 'Sapi Betina', 'ayat': 286},
    3: {'nama': "Ali 'Imran", 'arab': 'آل عمران', 'arti': 'Keluarga Imran', 'ayat': 200},
    4: {'nama': "An-Nisa'", 'arab': 'النساء', 'arti': 'Wanita', 'ayat': 176},
    5: {'nama': "Al-Ma'idah", 'arab': 'المائدة', 'arti': 'Hidangan', 'ayat': 120},
    6: {'nama': "Al-An'am", 'arab': 'الأنعام', 'arti': 'Binatang Ternak', 'ayat': 165},
    7: {'nama': "Al-A'raf", 'arab': 'الأعراف', 'arti': 'Tempat yang Tertinggi', 'ayat': 206},
    8: {'nama': 'Al-Anfal', 'arab': 'الأنفال', 'arti': 'Harta Rampasan Perang', 'ayat': 75},
    9: {'nama': 'At-Taubah', 'arab': 'التوبة', 'arti': 'Pengampunan', 'ayat': 129},
    10: {'nama': 'Yunus', 'arab': 'يونس', 'arti': 'Nabi Yunus', 'ayat': 109},
    11: {'nama': 'Hud', 'arab': 'هود', 'arti': 'Nabi Hud', 'ayat': 123},
    12: {'nama': 'Yusuf', 'arab': 'يوسف', 'arti': 'Nabi Yusuf', 'ayat': 111},
    13: {'nama': "Ar-Ra'd", 'arab': 'الرعد', 'arti': 'Guruh', 'ayat': 43},
    14: {'nama': 'Ibrahim', 'arab': 'إبراهيم', 'arti': 'Nabi Ibrahim', 'ayat': 52},
    15: {'nama': 'Al-Hijr', 'arab': 'الحجر', 'arti': 'Gunung Al-Hijr', 'ayat': 99},
    16: {'nama': 'An-Nahl', 'arab': 'النحل', 'arti': 'Lebah', 'ayat': 128},
    17: {'nama': "Al-Isra'", 'arab': 'الإسراء', 'arti': 'Perjalanan Malam', 'ayat': 111},
    18: {'nama': 'Al-Kahf', 'arab': 'الكهف', 'arti': 'Penghuni Gua', 'ayat': 110},
    19: {'nama': 'Maryam', 'arab': 'مريم', 'arti': 'Maryam', 'ayat': 98},
    20: {'nama': 'Taha', 'arab': 'طه', 'arti': 'Thaha', 'ayat': 135},
    21: {'nama': "Al-Anbiya'", 'arab': 'الأنبياء', 'arti': 'Para Nabi', 'ayat': 112},
    22: {'nama': 'Al-Hajj', 'arab': 'الحج', 'arti': 'Haji', 'ayat': 78},
    23: {'nama': "Al-Mu'minun", 'arab': 'المؤمنون', 'arti': 'Orang-Orang Mukmin', 'ayat': 118},
    24: {'nama': 'An-Nur', 'arab': 'النور', 'arti': 'Cahaya', 'ayat': 64},
    25: {'nama': 'Al-Furqan', 'arab': 'الفرقان', 'arti': 'Pembeda', 'ayat': 77},
    26: {'nama': "Asy-Syu'ara'", 'arab': 'الشعراء', 'arti': 'Penyair', 'ayat': 227},
    27: {'nama': 'An-Naml', 'arab': 'النمل', 'arti': 'Semut', 'ayat': 93},
    28: {'nama': 'Al-Qasas', 'arab': 'القصص', 'arti': 'Kisah-Kisah', 'ayat': 88},
    29: {'nama': "Al-'Ankabut", 'arab': 'العنكبوت', 'arti': 'Laba-Laba', 'ayat': 69},
    30: {'nama': 'Ar-Rum', 'arab': 'الروم', 'arti': 'Bangsa Romawi', 'ayat': 60},
    31: {'nama': 'Luqman', 'arab': 'لقمان', 'arti': 'Luqman', 'ayat': 34},
    32: {'nama': 'As-Sajdah', 'arab': 'السجدة', 'arti': 'Sujud', 'ayat': 30},
    33: {'nama': 'Al-Ahzab', 'arab': 'الأحزاب', 'arti': 'Golongan yang Bersekutu', 'ayat': 73},
    34: {'nama': "Saba'", 'arab': 'سبأ', 'arti': "Kaum Saba'", 'ayat': 54},
    35: {'nama': 'Fatir', 'arab': 'فاطر', 'arti': 'Pencipta', 'ayat': 45},
    36: {'nama': 'Ya-Sin', 'arab': 'يس', 'arti': 'Ya Sin', 'ayat': 83},
    37: {'nama': 'As-Saffat', 'arab': 'الصافات', 'arti': 'Barisan-Barisan', 'ayat': 182},
    38: {'nama': 'Sad', 'arab': 'ص', 'arti': 'Shad', 'ayat': 88},
    39: {'nama': 'Az-Zumar', 'arab': 'الزmer', 'arti': 'Rombongan', 'ayat': 75},
    40: {'nama': 'Gafir', 'arab': 'غافر', 'arti': 'Yang Mengampuni', 'ayat': 85},
    41: {'nama': 'Fussilat', 'arab': 'فصلت', 'arti': 'Dijelaskan', 'ayat': 54},
    42: {'nama': 'Asy-Syura', 'arab': 'الشورى', 'arti': 'Musyawarah', 'ayat': 53},
    43: {'nama': 'Az-Zukhruf', 'arab': 'الزخرف', 'arti': 'Perhiasan', 'ayat': 89},
    44: {'nama': 'Ad-Dukhan', 'arab': 'الدخان', 'arti': 'Kabut', 'ayat': 59},
    45: {'nama': 'Al-Jasiyah', 'arab': 'الجاثية', 'arti': 'Yang Berlutut', 'ayat': 37},
    46: {'nama': 'Al-Ahqaf', 'arab': 'الأحقاف', 'arti': 'Bukit-Bukit Pasir', 'ayat': 35},
    47: {'nama': 'Muhammad', 'arab': 'محمد', 'arti': 'Nabi Muhammad', 'ayat': 38},
    48: {'nama': 'Al-Fath', 'arab': 'الفتح', 'arti': 'Kemenangan', 'ayat': 29},
    49: {'nama': 'Al-Hujurat', 'arab': 'الحجرات', 'arti': 'Kamar-Kamar', 'ayat': 18},
    50: {'nama': 'Qaf', 'arab': 'ق', 'arti': 'Qaf', 'ayat': 45},
    51: {'nama': 'Az-Zariyat', 'arab': 'الذاريات', 'arti': 'Angin yang Menerbangkan', 'ayat': 60},
    52: {'nama': 'At-Tur', 'arab': 'الطور', 'arti': 'Bukit Tursina', 'ayat': 49},
    53: {'nama': 'An-Najm', 'arab': 'النجم', 'arti': 'Bintang', 'ayat': 62},
    54: {'nama': 'Al-Qamar', 'arab': 'القمر', 'arti': 'Bulan', 'ayat': 55},
    55: {'nama': 'Ar-Rahman', 'arab': 'الرحمن', 'arti': 'Yang Maha Pengasih', 'ayat': 78},
    56: {'nama': "Al-Waqi'ah", 'arab': 'الواقعة', 'arti': 'Hari Kiamat', 'ayat': 96},
    57: {'nama': 'Al-Hadid', 'arab': 'الحديد', 'arti': 'Besi', 'ayat': 29},
    58: {'nama': 'Al-Mujadilah', 'arab': 'المجادلة', 'arti': 'Gugatan', 'ayat': 22},
    59: {'nama': 'Al-Hasyr', 'arab': 'الحشر', 'arti': 'Pengusiran', 'ayat': 24},
    60: {'nama': 'Al-Mumtahanah', 'arab': 'الممتحنة', 'arti': 'Wanita yang Diuji', 'ayat': 13},
    61: {'nama': 'As-Saff', 'arab': 'الصف', 'arti': 'Barisan', 'ayat': 14},
    62: {'nama': "Al-Jumu'ah", 'arab': 'الجمعة', 'arti': "Hari Jum'at", 'ayat': 11},
    63: {'nama': 'Al-Munafiqun', 'arab': 'المنافقون', 'arti': 'Orang-Orang Munafik', 'ayat': 11},
    64: {'nama': 'At-Tagabun', 'arab': 'التغابن', 'arti': 'Pengungkapan Kesalahan', 'ayat': 18},
    65: {'nama': 'At-Talaq', 'arab': 'الطلاق', 'arti': 'Talak', 'ayat': 12},
    66: {'nama': 'At-Tahrim', 'arab': 'التحريم', 'arti': 'Pengharaman', 'ayat': 12},
    67: {'nama': 'Al-Mulk', 'arab': 'الملك', 'arti': 'Kerajaan', 'ayat': 30},
    68: {'nama': 'Al-Qalam', 'arab': 'القلم', 'arti': 'Pena', 'ayat': 52},
    69: {'nama': 'Al-Haqqah', 'arab': 'الحاقة', 'arti': 'Hari Kiamat yang Pasti', 'ayat': 52},
    70: {'nama': "Al-Ma'arij", 'arab': 'المعارج', 'arti': 'Tempat-Tempat Naik', 'ayat': 44},
    71: {'nama': 'Nuh', 'arab': 'نوح', 'arti': 'Nabi Nuh', 'ayat': 28},
    72: {'nama': 'Al-Jinn', 'arab': 'الجن', 'arti': 'Jin', 'ayat': 28},
    73: {'nama': 'Al-Muzzammil', 'arab': 'المزمل', 'arti': 'Orang yang Berselimut', 'ayat': 20},
    74: {'nama': 'Al-Muddassir', 'arab': 'المدثر', 'arti': 'Orang yang Berkemul', 'ayat': 56},
    75: {'nama': 'Al-Qiyamah', 'arab': 'القيامة', 'arti': 'Hari Kiamat', 'ayat': 40},
    76: {'nama': 'Al-Insan', 'arab': 'الإنسان', 'arti': 'Manusia', 'ayat': 31},
    77: {'nama': 'Al-Mursalat', 'arab': 'المرسلات', 'arti': 'Malaikat yang Diutus', 'ayat': 50},
    78: {'nama': "An-Naba'", 'arab': 'النبأ', 'arti': 'Berita Besar', 'ayat': 40},
    79: {'nama': "An-Nazi'at", 'arab': 'النازعات', 'arti': 'Malaikat Pencabut Nyawa', 'ayat': 46},
    80: {'nama': "'Abasa", 'arab': 'عبس', 'arti': 'Bermuka Masam', 'ayat': 42},
    81: {'nama': 'At-Takwir', 'arab': 'التكوير', 'arti': 'Menggulung Matahari', 'ayat': 29},
    82: {'nama': 'Al-Infitar', 'arab': 'الانفطار', 'arti': 'Terbelah', 'ayat': 19},
    83: {'nama': 'Al-Mutaffifin', 'arab': 'المطففين', 'arti': 'Orang-Orang yang Curang', 'ayat': 36},
    84: {'nama': 'Al-Insyiqaq', 'arab': 'الانشقاق', 'arti': 'Terbelah', 'ayat': 25},
    85: {'nama': 'Al-Buruj', 'arab': 'البروج', 'arti': 'Gugusan Bintang', 'ayat': 22},
    86: {'nama': 'At-Tariq', 'arab': 'الطارق', 'arti': 'Yang Datang di Malam Hari', 'ayat': 17},
    87: {'nama': "Al-A'la", 'arab': 'الأعلى', 'arti': 'Yang Maha Tinggi', 'ayat': 19},
    88: {'nama': 'Al-Gasyiyah', 'arab': 'الغاشية', 'arti': 'Hari Pembalasan yang Menyelimuti', 'ayat': 26},
    89: {'nama': 'Al-Fajr', 'arab': 'الفجر', 'arti': 'Fajar', 'ayat': 30},
    90: {'nama': 'Al-Balad', 'arab': 'البلد', 'arti': 'Negeri', 'ayat': 20},
    91: {'nama': 'Asy-Syams', 'arab': 'الشمس', 'arti': 'Matahari', 'ayat': 15},
    92: {'nama': 'Al-Lail', 'arab': 'الليل', 'arti': 'Malam', 'ayat': 21},
    93: {'nama': 'Ad-Duha', 'arab': 'الضحى', 'arti': 'Waktu Duha', 'ayat': 11},
    94: {'nama': 'Asy-Syarh', 'arab': 'الشرح', 'arti': 'Kelapangan Dada', 'ayat': 8},
    95: {'nama': 'At-Tin', 'arab': 'التين', 'arti': 'Buah Tin', 'ayat': 8},
    96: {'nama': "Al-'Alaq", 'arab': 'العلق', 'arti': 'Segumpal Darah', 'ayat': 19},
    97: {'nama': 'Al-Qadr', 'arab': 'القدر', 'arti': 'Kemuliaan', 'ayat': 5},
    98: {'nama': 'Al-Bayyinah', 'arab': 'البينة', 'arti': 'Bukti Nyata', 'ayat': 8},
    99: {'nama': 'Az-Zalzalah', 'arab': 'الزلزلة', 'arti': 'Guncangan', 'ayat': 8},
    100: {'nama': "Al-'Adiyat", 'arab': 'العاديات', 'arti': 'Kuda Perang yang Berlari Kencang', 'ayat': 11},
    101: {'nama': "Al-Qari'ah", 'arab': 'القارعة', 'arti': 'Hari Kiamat', 'ayat': 11},
    102: {'nama': 'At-Takasur', 'arab': 'التكاثر', 'arti': 'Bermegah-Megahan', 'ayat': 8},
    103: {'nama': "Al-'Asr", 'arab': 'العصر', 'arti': 'Masa / Waktu Sore', 'ayat': 3},
    104: {'nama': 'Al-Humazah', 'arab': 'الهمزة', 'arti': 'Pengumpat', 'ayat': 9},
    105: {'nama': 'Al-Fil', 'arab': 'الفيل', 'arti': 'Gajah', 'ayat': 5},
    106: {'nama': 'Quraisy', 'arab': 'قريش', 'arti': 'Suku Quraisy', 'ayat': 4},
    107: {'nama': "Al-Ma'un", 'arab': 'الماعون', 'arti': 'Barang-Barang yang Berguna', 'ayat': 7},
    108: {'nama': 'Al-Kausar', 'arab': 'الكوثر', 'arti': 'Nikmat yang Berlimpah', 'ayat': 3},
    109: {'nama': 'Al-Kafirun', 'arab': 'الكافرون', 'arti': 'Orang-Orang Kafir', 'ayat': 6},
    110: {'nama': 'An-Nasr', 'arab': 'النصر', 'arti': 'Pertolongan', 'ayat': 3},
    111: {'nama': 'Al-Lahab', 'arab': 'اللهب', 'arti': 'Gejolak Api', 'ayat': 5},
    112: {'nama': 'Al-Ikhlas', 'arab': 'الإخلاص', 'arti': 'Kemurnian Keesaan Allah', 'ayat': 4},
    113: {'nama': 'Al-Falaq', 'arab': 'الفلق', 'arti': 'Waktu Subuh', 'ayat': 5},
    114: {'nama': 'An-Nas', 'arab': 'الناس', 'arti': 'Manusia', 'ayat': 6}
}

# Grammatical metadata for Dhamir including Latin Transliteration
grammatical_metadata = {
    '1a': {
        'latin': 'Huwa',
        'jenis': 'Munfashil (Terpisah)',
        'dhamir_type': 'Ghaib (Orang ke-3)',
        'gender': 'Mudzakkar (Laki-laki)',
        'bilangan': 'Mufrad (Tunggal)',
        'posisi': "Rafa' (Subjek)",
        'keterangan': 'Dia (1 orang laki-laki)'
    },
    '1b': {
        'latin': '..hu / ..hi',
        'jenis': 'Muttashil (Tersambung)',
        'dhamir_type': 'Ghaib (Orang ke-3)',
        'gender': 'Mudzakkar (Laki-laki)',
        'bilangan': 'Mufrad (Tunggal)',
        'posisi': 'Nashab/Jar (Objek/Milik)',
        'keterangan': '...-nya (1 orang laki-laki)'
    },
    '3a': {
        'latin': 'Hum',
        'jenis': 'Munfashil (Terpisah)',
        'dhamir_type': 'Ghaib (Orang ke-3)',
        'gender': 'Mudzakkar (Laki-laki)',
        'bilangan': 'Jamak (Banyak)',
        'posisi': "Rafa' (Subjek)",
        'keterangan': 'Mereka (banyak laki-laki)'
    },
    '3b': {
        'latin': '..hum / ..him',
        'jenis': 'Muttashil (Tersambung)',
        'dhamir_type': 'Ghaib (Orang ke-3)',
        'gender': 'Mudzakkar (Laki-laki)',
        'bilangan': 'Jamak (Banyak)',
        'posisi': 'Nashab/Jar (Objek/Milik)',
        'keterangan': '...-mereka (banyak laki-laki)'
    },
    '4a': {
        'latin': 'Hiya',
        'jenis': 'Munfashil (Terpisah)',
        'dhamir_type': 'Ghaib (Orang ke-3)',
        'gender': 'Muannats (Perempuan)',
        'bilangan': 'Mufrad (Tunggal)',
        'posisi': "Rafa' (Subjek)",
        'keterangan': 'Dia (1 orang perempuan)'
    },
    '4b': {
        'latin': '..hā',
        'jenis': 'Muttashil (Tersambung)',
        'dhamir_type': 'Ghaib (Orang ke-3)',
        'gender': 'Muannats (Perempuan)',
        'bilangan': 'Mufrad (Tunggal)',
        'posisi': 'Nashab/Jar (Objek/Milik)',
        'keterangan': '...-nya (1 orang perempuan)'
    },
    '6a': {
        'latin': 'Anta',
        'jenis': 'Munfashil (Terpisah)',
        'dhamir_type': 'Mukhatab (Orang ke-2)',
        'gender': 'Mudzakkar (Laki-laki)',
        'bilangan': 'Mufrad (Tunggal)',
        'posisi': "Rafa' (Subjek)",
        'keterangan': 'Kamu / Engkau (1 orang laki-laki)'
    },
    '6b': {
        'latin': '..ka',
        'jenis': 'Muttashil (Tersambung)',
        'dhamir_type': 'Mukhatab (Orang ke-2)',
        'gender': 'Mudzakkar (Laki-laki)',
        'bilangan': 'Mufrad (Tunggal)',
        'posisi': 'Nashab/Jar (Objek/Milik)',
        'keterangan': '...-mu (1 orang laki-laki)'
    },
    '6c': {
        'latin': 'Iyyāka',
        'jenis': 'Munfashil (Terpisah - Iyyaka)',
        'dhamir_type': 'Mukhatab (Orang ke-2)',
        'gender': 'Mudzakkar (Laki-laki)',
        'bilangan': 'Mufrad (Tunggal)',
        'posisi': 'Nashab (Objek Khusus)',
        'keterangan': 'Hanya kepada-Mu (1 orang laki-laki)'
    },
    '8a': {
        'latin': 'Antum',
        'jenis': 'Munfashil (Terpisah)',
        'dhamir_type': 'Mukhatab (Orang ke-2)',
        'gender': 'Mudzakkar (Laki-laki)',
        'bilangan': 'Jamak (Banyak)',
        'posisi': "Rafa' (Subjek)",
        'keterangan': 'Kalian (banyak laki-laki)'
    },
    '8b': {
        'latin': '..kum',
        'jenis': 'Muttashil (Tersambung)',
        'dhamir_type': 'Mukhatab (Orang ke-2)',
        'gender': 'Mudzakkar (Laki-laki)',
        'bilangan': 'Jamak (Banyak)',
        'posisi': 'Nashab/Jar (Objek/Milik)',
        'keterangan': '...-kalian (banyak laki-laki)'
    },
    '11a': {
        'latin': 'Anā',
        'jenis': 'Munfashil (Terpisah)',
        'dhamir_type': 'Mutakallim (Orang ke-1)',
        'gender': 'Mudzakkar / Muannats',
        'bilangan': 'Mufrad (Tunggal)',
        'posisi': "Rafa' (Subjek)",
        'keterangan': 'Saya / Aku (Tunggal L/P)'
    },
    '11b': {
        'latin': '..ī / ..ya',
        'jenis': 'Muttashil (Tersambung)',
        'dhamir_type': 'Mutakallim (Orang ke-1)',
        'gender': 'Mudzakkar / Muannats',
        'bilangan': 'Mufrad (Tunggal)',
        'posisi': 'Nashab/Jar (Objek/Milik)',
        'keterangan': '...-ku (Tunggal L/P)'
    },
    '12a': {
        'latin': 'Naḥnu',
        'jenis': 'Munfashil (Terpisah)',
        'dhamir_type': 'Mutakallim (Orang ke-1)',
        'gender': 'Mudzakkar / Muannats',
        'bilangan': 'Jamak (Banyak/Agung)',
        'posisi': "Rafa' (Subjek)",
        'keterangan': 'Kami / Kita (Jamak L/P)'
    },
    '12b': {
        'latin': '..nā',
        'jenis': 'Muttashil (Tersambung)',
        'dhamir_type': 'Mutakallim (Orang ke-1)',
        'gender': 'Mudzakkar / Muannats',
        'bilangan': 'Jamak (Banyak/Agung)',
        'posisi': 'Nashab/Jar (Objek/Milik)',
        'keterangan': '...-kami / ...-kita (Jamak L/P)'
    }
}

for item in raw_data:
    s_no = int(item['SURAT']) if item['SURAT'] is not None else None
    if s_no and s_no in surahs:
        item['SuratNama'] = surahs[s_no]['nama']
        item['SuratArab'] = surahs[s_no]['arab']
        item['SuratArti'] = surahs[s_no]['arti']
    else:
        item['SuratNama'] = f'Surat {s_no}'
        item['SuratArab'] = ''
        item['SuratArti'] = ''
    
    nk = item.get('No kata')
    if nk in grammatical_metadata:
        item['Grammar'] = grammatical_metadata[nk]
        item['Latin'] = grammatical_metadata[nk]['latin']

js_content = f'''/**
 * Data Dhamir Al-Qur'an & Kamus Surah
 * Otomatis dibuat dari dataset DHAMIR copy.xlsx & Sumber Kemenag RI
 */
const DHAMIR_DATA = {json.dumps(raw_data, ensure_ascii=False, indent=2)};

const SURAH_DICT = {json.dumps(surahs, ensure_ascii=False, indent=2)};

const GRAMMAR_INFO = {json.dumps(grammatical_metadata, ensure_ascii=False, indent=2)};
'''

with open('d:/Dhamir/dhamir_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

with open('d:/Dhamir/dhamir_data.json', 'w', encoding='utf-8') as f:
    json.dump(raw_data, f, ensure_ascii=False, indent=2)

print(f"Berhasil memperbarui dhamir_data.js dan dhamir_data.json dengan {len(raw_data)} entri lengkap!")
