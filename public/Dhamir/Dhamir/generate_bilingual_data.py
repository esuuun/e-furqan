import json

# Load base data and fetched English translations
with open('d:/Dhamir/dhamir_data.json', encoding='utf-8') as f:
    raw_data = json.load(f)

with open('d:/Dhamir/en_translations.json', encoding='utf-8') as f:
    en_trans = json.load(f)

# Surah database (1-114) with both Indonesian and English translations
surahs = {
    1: {'nama': 'Al-Fatihah', 'arab': 'الفاتحة', 'arti_id': 'Pembukaan', 'arti_en': 'The Opening', 'ayat': 7},
    2: {'nama': 'Al-Baqarah', 'arab': 'البقرة', 'arti_id': 'Sapi Betina', 'arti_en': 'The Cow', 'ayat': 286},
    3: {'nama': "Ali 'Imran", 'arab': 'آل عمران', 'arti_id': 'Keluarga Imran', 'arti_en': 'The Family of Imran', 'ayat': 200},
    4: {'nama': "An-Nisa'", 'arab': 'النساء', 'arti_id': 'Wanita', 'arti_en': 'The Women', 'ayat': 176},
    5: {'nama': "Al-Ma'idah", 'arab': 'المائدة', 'arti_id': 'Hidangan', 'arti_en': 'The Table Spread', 'ayat': 120},
    6: {'nama': "Al-An'am", 'arab': 'الأنعام', 'arti_id': 'Binatang Ternak', 'arti_en': 'The Cattle', 'ayat': 165},
    7: {'nama': "Al-A'raf", 'arab': 'الأعراف', 'arti_id': 'Tempat yang Tertinggi', 'arti_en': 'The Heights', 'ayat': 206},
    8: {'nama': 'Al-Anfal', 'arab': 'الأنفال', 'arti_id': 'Harta Rampasan Perang', 'arti_en': 'The Spoils of War', 'ayat': 75},
    9: {'nama': 'At-Taubah', 'arab': 'التوبة', 'arti_id': 'Pengampunan', 'arti_en': 'The Repentance', 'ayat': 129},
    10: {'nama': 'Yunus', 'arab': 'يونس', 'arti_id': 'Nabi Yunus', 'arti_en': 'Jonah', 'ayat': 109},
    11: {'nama': 'Hud', 'arab': 'هود', 'arti_id': 'Nabi Hud', 'arti_en': 'Hud', 'ayat': 123},
    12: {'nama': 'Yusuf', 'arab': 'يوسف', 'arti_id': 'Nabi Yusuf', 'arti_en': 'Joseph', 'ayat': 111},
    13: {'nama': "Ar-Ra'd", 'arab': 'الرعد', 'arti_id': 'Guruh', 'arti_en': 'The Thunder', 'ayat': 43},
    14: {'nama': 'Ibrahim', 'arab': 'إبراهيم', 'arti_id': 'Nabi Ibrahim', 'arti_en': 'Abraham', 'ayat': 52},
    15: {'nama': 'Al-Hijr', 'arab': 'الحجر', 'arti_id': 'Gunung Al-Hijr', 'arti_en': 'The Rocky Tract', 'ayat': 99},
    16: {'nama': 'An-Nahl', 'arab': 'النحل', 'arti_id': 'Lebah', 'arti_en': 'The Bee', 'ayat': 128},
    17: {'nama': "Al-Isra'", 'arab': 'الإسراء', 'arti_id': 'Perjalanan Malam', 'arti_en': 'The Night Journey', 'ayat': 111},
    18: {'nama': 'Al-Kahf', 'arab': 'الكهف', 'arti_id': 'Penghuni Gua', 'arti_en': 'The Cave', 'ayat': 110},
    19: {'nama': 'Maryam', 'arab': 'مريم', 'arti_id': 'Maryam', 'arti_en': 'Mary', 'ayat': 98},
    20: {'nama': 'Taha', 'arab': 'طه', 'arti_id': 'Thaha', 'arti_en': 'Ta-Ha', 'ayat': 135},
    21: {'nama': "Al-Anbiya'", 'arab': 'الأنبياء', 'arti_id': 'Para Nabi', 'arti_en': 'The Prophets', 'ayat': 112},
    22: {'nama': 'Al-Hajj', 'arab': 'الحج', 'arti_id': 'Haji', 'arti_en': 'The Pilgrimage', 'ayat': 78},
    23: {'nama': "Al-Mu'minun", 'arab': 'المؤمنون', 'arti_id': 'Orang-Orang Mukmin', 'arti_en': 'The Believers', 'ayat': 118},
    24: {'nama': 'An-Nur', 'arab': 'النور', 'arti_id': 'Cahaya', 'arti_en': 'The Light', 'ayat': 64},
    25: {'nama': 'Al-Furqan', 'arab': 'الفرقان', 'arti_id': 'Pembeda', 'arti_en': 'The Criterion', 'ayat': 77},
    26: {'nama': "Asy-Syu'ara'", 'arab': 'الشعراء', 'arti_id': 'Penyair', 'arti_en': 'The Poets', 'ayat': 227},
    27: {'nama': 'An-Naml', 'arab': 'النمل', 'arti_id': 'Semut', 'arti_en': 'The Ants', 'ayat': 93},
    28: {'nama': 'Al-Qasas', 'arab': 'القصص', 'arti_id': 'Kisah-Kisah', 'arti_en': 'The Stories', 'ayat': 88},
    29: {'nama': "Al-'Ankabut", 'arab': 'العنكبوت', 'arti_id': 'Laba-Laba', 'arti_en': 'The Spider', 'ayat': 69},
    30: {'nama': 'Ar-Rum', 'arab': 'الروم', 'arti_id': 'Bangsa Romawi', 'arti_en': 'The Romans', 'ayat': 60},
    31: {'nama': 'Luqman', 'arab': 'لقمان', 'arti_id': 'Luqman', 'arti_en': 'Luqman', 'ayat': 34},
    32: {'nama': 'As-Sajdah', 'arab': 'السجدة', 'arti_id': 'Sujud', 'arti_en': 'The Prostration', 'ayat': 30},
    33: {'nama': 'Al-Ahzab', 'arab': 'الأحزاب', 'arti_id': 'Golongan yang Bersekutu', 'arti_en': 'The Combined Forces', 'ayat': 73},
    34: {'nama': "Saba'", 'arab': 'سبأ', 'arti_id': "Kaum Saba'", 'arti_en': 'Sheba', 'ayat': 54},
    35: {'nama': 'Fatir', 'arab': 'فاطر', 'arti_id': 'Pencipta', 'arti_en': 'The Originator', 'ayat': 45},
    36: {'nama': 'Ya-Sin', 'arab': 'يس', 'arti_id': 'Ya Sin', 'arti_en': 'Ya-Sin', 'ayat': 83},
    37: {'nama': 'As-Saffat', 'arab': 'الصافات', 'arti_id': 'Barisan-Barisan', 'arti_en': 'Those Ranked in Rows', 'ayat': 182},
    38: {'nama': 'Sad', 'arab': 'ص', 'arti_id': 'Shad', 'arti_en': 'The Letter Sad', 'ayat': 88},
    39: {'nama': 'Az-Zumar', 'arab': 'الزمر', 'arti_id': 'Rombongan', 'arti_en': 'The Groups', 'ayat': 75},
    40: {'nama': 'Gafir', 'arab': 'غافر', 'arti_id': 'Yang Mengampuni', 'arti_en': 'The Forgiver', 'ayat': 85},
    41: {'nama': 'Fussilat', 'arab': 'فصلت', 'arti_id': 'Dijelaskan', 'arti_en': 'Distinguished Verses', 'ayat': 54},
    42: {'nama': 'Asy-Syura', 'arab': 'الشورى', 'arti_id': 'Musyawarah', 'arti_en': 'The Consultation', 'ayat': 53},
    43: {'nama': 'Az-Zukhruf', 'arab': 'الزخرف', 'arti_id': 'Perhiasan', 'arti_en': 'The Gold Adornments', 'ayat': 89},
    44: {'nama': 'Ad-Dukhan', 'arab': 'الدخان', 'arti_id': 'Kabut', 'arti_en': 'The Smoke', 'ayat': 59},
    45: {'nama': 'Al-Jasiyah', 'arab': 'الجاثية', 'arti_id': 'Yang Berlutut', 'arti_en': 'The Crouching', 'ayat': 37},
    46: {'nama': 'Al-Ahqaf', 'arab': 'الأحقاف', 'arti_id': 'Bukit-Bukit Pasir', 'arti_en': 'The Wind-Curved Sandhills', 'ayat': 35},
    47: {'nama': 'Muhammad', 'arab': 'محمد', 'arti_id': 'Nabi Muhammad', 'arti_en': 'Muhammad', 'ayat': 38},
    48: {'nama': 'Al-Fath', 'arab': 'الفتح', 'arti_id': 'Kemenangan', 'arti_en': 'The Victory', 'ayat': 29},
    49: {'nama': 'Al-Hujurat', 'arab': 'الحجرات', 'arti_id': 'Kamar-Kamar', 'arti_en': 'The Rooms', 'ayat': 18},
    50: {'nama': 'Qaf', 'arab': 'ق', 'arti_id': 'Qaf', 'arti_en': 'The Letter Qaf', 'ayat': 45},
    51: {'nama': 'Az-Zariyat', 'arab': 'الذاريات', 'arti_id': 'Angin yang Menerbangkan', 'arti_en': 'The Winnowing Winds', 'ayat': 60},
    52: {'nama': 'At-Tur', 'arab': 'الطور', 'arti_id': 'Bukit Tursina', 'arti_en': 'The Mount', 'ayat': 49},
    53: {'nama': 'An-Najm', 'arab': 'النجم', 'arti_id': 'Bintang', 'arti_en': 'The Star', 'ayat': 62},
    54: {'nama': 'Al-Qamar', 'arab': 'القمر', 'arti_id': 'Bulan', 'arti_en': 'The Moon', 'ayat': 55},
    55: {'nama': 'Ar-Rahman', 'arab': 'الرحمن', 'arti_id': 'Yang Maha Pengasih', 'arti_en': 'The Beneficent', 'ayat': 78},
    56: {'nama': "Al-Waqi'ah", 'arab': 'الواقعة', 'arti_id': 'Hari Kiamat', 'arti_en': 'The Inevitable', 'ayat': 96},
    57: {'nama': 'Al-Hadid', 'arab': 'الحديد', 'arti_id': 'Besi', 'arti_en': 'The Iron', 'ayat': 29},
    58: {'nama': 'Al-Mujadilah', 'arab': 'المجادلة', 'arti_id': 'Gugatan', 'arti_en': 'The Pleading Woman', 'ayat': 22},
    59: {'nama': 'Al-Hasyr', 'arab': 'الحشر', 'arti_id': 'Pengusiran', 'arti_en': 'The Exile', 'ayat': 24},
    60: {'nama': 'Al-Mumtahanah', 'arab': 'الممتحنة', 'arti_id': 'Wanita yang Diuji', 'arti_en': 'The Examined One', 'ayat': 13},
    61: {'nama': 'As-Saff', 'arab': 'الصف', 'arti_id': 'Barisan', 'arti_en': 'The Ranks', 'ayat': 14},
    62: {'nama': "Al-Jumu'ah", 'arab': 'الجمعة', 'arti_id': "Hari Jum'at", 'arti_en': 'Friday', 'ayat': 11},
    63: {'nama': 'Al-Munafiqun', 'arab': 'المنافقون', 'arti_id': 'Orang-Orang Munafik', 'arti_en': 'The Hypocrites', 'ayat': 11},
    64: {'nama': 'At-Tagabun', 'arab': 'التغابن', 'arti_id': 'Pengungkapan Kesalahan', 'arti_en': 'Mutual Disillusion', 'ayat': 18},
    65: {'nama': 'At-Talaq', 'arab': 'الطلاق', 'arti_id': 'Talak', 'arti_en': 'The Divorce', 'ayat': 12},
    66: {'nama': 'At-Tahrim', 'arab': 'التحريم', 'arti_id': 'Pengharaman', 'arti_en': 'The Prohibition', 'ayat': 12},
    67: {'nama': 'Al-Mulk', 'arab': 'الملك', 'arti_id': 'Kerajaan', 'arti_en': 'The Sovereignty', 'ayat': 30},
    68: {'nama': 'Al-Qalam', 'arab': 'القلم', 'arti_id': 'Pena', 'arti_en': 'The Pen', 'ayat': 52},
    69: {'nama': 'Al-Haqqah', 'arab': 'الحاقة', 'arti_id': 'Hari Kiamat yang Pasti', 'arti_en': 'The Inevitable Reality', 'ayat': 52},
    70: {'nama': "Al-Ma'arij", 'arab': 'المعارج', 'arti_id': 'Tempat-Tempat Naik', 'arti_en': 'The Ascending Stairways', 'ayat': 44},
    71: {'nama': 'Nuh', 'arab': 'نوح', 'arti_id': 'Nabi Nuh', 'arti_en': 'Noah', 'ayat': 28},
    72: {'nama': 'Al-Jinn', 'arab': 'الجن', 'arti_id': 'Jin', 'arti_en': 'The Jinn', 'ayat': 28},
    73: {'nama': 'Al-Muzzammil', 'arab': 'المزمل', 'arti_id': 'Orang yang Berselimut', 'arti_en': 'The Enshrouded One', 'ayat': 20},
    74: {'nama': 'Al-Muddassir', 'arab': 'المدثر', 'arti_id': 'Orang yang Berkemul', 'arti_en': 'The Cloaked One', 'ayat': 56},
    75: {'nama': 'Al-Qiyamah', 'arab': 'القيامة', 'arti_id': 'Hari Kiamat', 'arti_en': 'The Resurrection', 'ayat': 40},
    76: {'nama': 'Al-Insan', 'arab': 'الإنسان', 'arti_id': 'Manusia', 'arti_en': 'Man', 'ayat': 31},
    77: {'nama': 'Al-Mursalat', 'arab': 'المرسلات', 'arti_id': 'Malaikat yang Diutus', 'arti_en': 'The Emissaries', 'ayat': 50},
    78: {'nama': "An-Naba'", 'arab': 'النبأ', 'arti_id': 'Berita Besar', 'arti_en': 'The Tidings', 'ayat': 40},
    79: {'nama': "An-Nazi'at", 'arab': 'النازعات', 'arti_id': 'Malaikat Pencabut Nyawa', 'arti_en': 'Those Who Drag Forth', 'ayat': 46},
    80: {'nama': "'Abasa", 'arab': 'عبس', 'arti_id': 'Bermuka Masam', 'arti_en': 'He Frowned', 'ayat': 42},
    81: {'nama': 'At-Takwir', 'arab': 'التكوير', 'arti_id': 'Menggulung Matahari', 'arti_en': 'The Overthrowing', 'ayat': 29},
    82: {'nama': 'Al-Infitar', 'arab': 'الانفطار', 'arti_id': 'Terbelah', 'arti_en': 'The Cleaving', 'ayat': 19},
    83: {'nama': 'Al-Mutaffifin', 'arab': 'المطففين', 'arti_id': 'Orang-Orang yang Curang', 'arti_en': 'The Defrauders', 'ayat': 36},
    84: {'nama': 'Al-Insyiqaq', 'arab': 'الانشقاق', 'arti_id': 'Terbelah', 'arti_en': 'The Splitting Open', 'ayat': 25},
    85: {'nama': 'Al-Buruj', 'arab': 'البروج', 'arti_id': 'Gugusan Bintang', 'arti_en': 'The Mansions of the Stars', 'ayat': 22},
    86: {'nama': 'At-Tariq', 'arab': 'الطارق', 'arti_id': 'Yang Datang di Malam Hari', 'arti_en': 'The Nightcomer', 'ayat': 17},
    87: {'nama': "Al-A'la", 'arab': 'الأعلى', 'arti_id': 'Yang Maha Tinggi', 'arti_en': 'The Most High', 'ayat': 19},
    88: {'nama': 'Al-Gasyiyah', 'arab': 'الغاشية', 'arti_id': 'Hari Pembalasan yang Menyelimuti', 'arti_en': 'The Overwhelming Event', 'ayat': 26},
    89: {'nama': 'Al-Fajr', 'arab': 'الفجر', 'arti_id': 'Fajar', 'arti_en': 'The Dawn', 'ayat': 30},
    90: {'nama': 'Al-Balad', 'arab': 'البلد', 'arti_id': 'Negeri', 'arti_en': 'The City', 'ayat': 20},
    91: {'nama': 'Asy-Syams', 'arab': 'الشمس', 'arti_id': 'Matahari', 'arti_en': 'The Sun', 'ayat': 15},
    92: {'nama': 'Al-Lail', 'arab': 'الليل', 'arti_id': 'Malam', 'arti_en': 'The Night', 'ayat': 21},
    93: {'nama': 'Ad-Duha', 'arab': 'الضحى', 'arti_id': 'Waktu Duha', 'arti_en': 'The Morning Brightness', 'ayat': 11},
    94: {'nama': 'Asy-Syarh', 'arab': 'الشرح', 'arti_id': 'Kelapangan Dada', 'arti_en': 'The Relief', 'ayat': 8},
    95: {'nama': 'At-Tin', 'arab': 'التين', 'arti_id': 'Buah Tin', 'arti_en': 'The Fig', 'ayat': 8},
    96: {'nama': "Al-'Alaq", 'arab': 'العلق', 'arti_id': 'Segumpal Darah', 'arti_en': 'The Clot', 'ayat': 19},
    97: {'nama': 'Al-Qadr', 'arab': 'القدر', 'arti_id': 'Kemuliaan', 'arti_en': 'The Night of Decree', 'ayat': 5},
    98: {'nama': 'Al-Bayyinah', 'arab': 'البينة', 'arti_id': 'Bukti Nyata', 'arti_en': 'The Clear Evidence', 'ayat': 8},
    99: {'nama': 'Az-Zalzalah', 'arab': 'الزلزلة', 'arti_id': 'Guncangan', 'arti_en': 'The Earthquake', 'ayat': 8},
    100: {'nama': "Al-'Adiyat", 'arab': 'العاديات', 'arti_id': 'Kuda Perang yang Berlari Kencang', 'arti_en': 'The Courser', 'ayat': 11},
    101: {'nama': "Al-Qari'ah", 'arab': 'القارعة', 'arti_id': 'Hari Kiamat', 'arti_en': 'The Calamity', 'ayat': 11},
    102: {'nama': 'At-Takasur', 'arab': 'التكاثر', 'arti_id': 'Bermegah-Megahan', 'arti_en': 'The Rivalry in World Increase', 'ayat': 8},
    103: {'nama': "Al-'Asr", 'arab': 'العصر', 'arti_id': 'Masa / Waktu Sore', 'arti_en': 'The Declining Day', 'ayat': 3},
    104: {'nama': 'Al-Humazah', 'arab': 'الهمزة', 'arti_id': 'Pengumpat', 'arti_en': 'The Traducer', 'ayat': 9},
    105: {'nama': 'Al-Fil', 'arab': 'الفيل', 'arti_id': 'Gajah', 'arti_en': 'The Elephant', 'ayat': 5},
    106: {'nama': 'Quraisy', 'arab': 'قريش', 'arti_id': 'Suku Quraisy', 'arti_en': 'Quraysh', 'ayat': 4},
    107: {'nama': "Al-Ma'un", 'arab': 'الماعون', 'arti_id': 'Barang-Barang yang Berguna', 'arti_en': 'The Small Kindness', 'ayat': 7},
    108: {'nama': 'Al-Kausar', 'arab': 'الكوثر', 'arti_id': 'Nikmat yang Berlimpah', 'arti_en': 'The Abundance', 'ayat': 3},
    109: {'nama': 'Al-Kafirun', 'arab': 'الكافرون', 'arti_id': 'Orang-Orang Kafir', 'arti_en': 'The Disbelievers', 'ayat': 6},
    110: {'nama': 'An-Nasr', 'arab': 'النصر', 'arti_id': 'Pertolongan', 'arti_en': 'The Divine Help', 'ayat': 3},
    111: {'nama': 'Al-Lahab', 'arab': 'اللهب', 'arti_id': 'Gejolak Api', 'arti_en': 'The Palm Fiber', 'ayat': 5},
    112: {'nama': 'Al-Ikhlas', 'arab': 'الإخلاص', 'arti_id': 'Kemurnian Keesaan Allah', 'arti_en': 'The Sincerity', 'ayat': 4},
    113: {'nama': 'Al-Falaq', 'arab': 'الفلق', 'arti_id': 'Waktu Subuh', 'arti_en': 'The Daybreak', 'ayat': 5},
    114: {'nama': 'An-Nas', 'arab': 'الناس', 'arti_id': 'Manusia', 'arti_en': 'Mankind', 'ayat': 6}
}

# Bilingual Grammatical Metadata for 15 Dhamir forms
grammatical_metadata = {
    '1a': {
        'latin': 'Huwa',
        'arti_id': 'DIA (LK)',
        'arti_en': 'HE / HIM',
        'desc_id': 'Dia (1 orang laki-laki)',
        'desc_en': 'He (Single Male, 3rd Person)',
        'jenis_id': 'Munfashil (Terpisah)',
        'jenis_en': 'Detached (Munfashil)',
        'dhamir_type_id': 'Ghaib (Orang ke-3)',
        'dhamir_type_en': '3rd Person (Ghaib)',
        'gender_id': 'Mudzakkar (Laki-laki)',
        'gender_en': 'Masculine (Mudzakkar)',
        'bilangan_id': 'Mufrad (Tunggal)',
        'bilangan_en': 'Singular (Mufrad)',
        'posisi_id': "Rafa' (Subjek)",
        'posisi_en': 'Nominative (Subject)',
        'keterangan': 'Dia (1 orang laki-laki)'
    },
    '1b': {
        'latin': '..hu / ..hi',
        'arti_id': '..NYA (LK)',
        'arti_en': '..HIS / ..HIM',
        'desc_id': '...-nya (1 orang laki-laki)',
        'desc_en': 'His / Him (Single Male, 3rd Person)',
        'jenis_id': 'Muttashil (Tersambung)',
        'jenis_en': 'Attached (Muttashil)',
        'dhamir_type_id': 'Ghaib (Orang ke-3)',
        'dhamir_type_en': '3rd Person (Ghaib)',
        'gender_id': 'Mudzakkar (Laki-laki)',
        'gender_en': 'Masculine (Mudzakkar)',
        'bilangan_id': 'Mufrad (Tunggal)',
        'bilangan_en': 'Singular (Mufrad)',
        'posisi_id': 'Nashab/Jar (Objek/Milik)',
        'posisi_en': 'Accusative/Genitive (Object/Possessive)',
        'keterangan': '...-nya (1 orang laki-laki)'
    },
    '3a': {
        'latin': 'Hum',
        'arti_id': 'MEREKA (LK)',
        'arti_en': 'THEY (MASC)',
        'desc_id': 'Mereka (banyak laki-laki)',
        'desc_en': 'They (Plural Male, 3rd Person)',
        'jenis_id': 'Munfashil (Terpisah)',
        'jenis_en': 'Detached (Munfashil)',
        'dhamir_type_id': 'Ghaib (Orang ke-3)',
        'dhamir_type_en': '3rd Person (Ghaib)',
        'gender_id': 'Mudzakkar (Laki-laki)',
        'gender_en': 'Masculine (Mudzakkar)',
        'bilangan_id': 'Jamak (Banyak)',
        'bilangan_en': 'Plural (Jamak)',
        'posisi_id': "Rafa' (Subjek)",
        'posisi_en': 'Nominative (Subject)',
        'keterangan': 'Mereka (banyak laki-laki)'
    },
    '3b': {
        'latin': '..hum / ..him',
        'arti_id': '..MEREKA (LK)',
        'arti_en': '..THEIR / ..THEM',
        'desc_id': '...-mereka (banyak laki-laki)',
        'desc_en': 'Their / Them (Plural Male, 3rd Person)',
        'jenis_id': 'Muttashil (Tersambung)',
        'jenis_en': 'Attached (Muttashil)',
        'dhamir_type_id': 'Ghaib (Orang ke-3)',
        'dhamir_type_en': '3rd Person (Ghaib)',
        'gender_id': 'Mudzakkar (Laki-laki)',
        'gender_en': 'Masculine (Mudzakkar)',
        'bilangan_id': 'Jamak (Banyak)',
        'bilangan_en': 'Plural (Jamak)',
        'posisi_id': 'Nashab/Jar (Objek/Milik)',
        'posisi_en': 'Accusative/Genitive (Object/Possessive)',
        'keterangan': '...-mereka (banyak laki-laki)'
    },
    '4a': {
        'latin': 'Hiya',
        'arti_id': 'DIA (PR)',
        'arti_en': 'SHE / HER',
        'desc_id': 'Dia (1 orang perempuan)',
        'desc_en': 'She (Single Female, 3rd Person)',
        'jenis_id': 'Munfashil (Terpisah)',
        'jenis_en': 'Detached (Munfashil)',
        'dhamir_type_id': 'Ghaib (Orang ke-3)',
        'dhamir_type_en': '3rd Person (Ghaib)',
        'gender_id': 'Muannats (Perempuan)',
        'gender_en': 'Feminine (Muannats)',
        'bilangan_id': 'Mufrad (Tunggal)',
        'bilangan_en': 'Singular (Mufrad)',
        'posisi_id': "Rafa' (Subjek)",
        'posisi_en': 'Nominative (Subject)',
        'keterangan': 'Dia (1 orang perempuan)'
    },
    '4b': {
        'latin': '..hā',
        'arti_id': '..NYA (PR)',
        'arti_en': '..HER',
        'desc_id': '...-nya (1 orang perempuan)',
        'desc_en': 'Her (Single Female, 3rd Person)',
        'jenis_id': 'Muttashil (Tersambung)',
        'jenis_en': 'Attached (Muttashil)',
        'dhamir_type_id': 'Ghaib (Orang ke-3)',
        'dhamir_type_en': '3rd Person (Ghaib)',
        'gender_id': 'Muannats (Perempuan)',
        'gender_en': 'Feminine (Muannats)',
        'bilangan_id': 'Mufrad (Tunggal)',
        'bilangan_en': 'Singular (Mufrad)',
        'posisi_id': 'Nashab/Jar (Objek/Milik)',
        'posisi_en': 'Accusative/Genitive (Object/Possessive)',
        'keterangan': '...-nya (1 orang perempuan)'
    },
    '6a': {
        'latin': 'Anta',
        'arti_id': 'KAMU (LK)',
        'arti_en': 'YOU (MASC)',
        'desc_id': 'Kamu / Engkau (1 orang laki-laki)',
        'desc_en': 'You (Single Male, 2nd Person)',
        'jenis_id': 'Munfashil (Terpisah)',
        'jenis_en': 'Detached (Munfashil)',
        'dhamir_type_id': 'Mukhatab (Orang ke-2)',
        'dhamir_type_en': '2nd Person (Mukhatab)',
        'gender_id': 'Mudzakkar (Laki-laki)',
        'gender_en': 'Masculine (Mudzakkar)',
        'bilangan_id': 'Mufrad (Tunggal)',
        'bilangan_en': 'Singular (Mufrad)',
        'posisi_id': "Rafa' (Subjek)",
        'posisi_en': 'Nominative (Subject)',
        'keterangan': 'Kamu / Engkau (1 orang laki-laki)'
    },
    '6b': {
        'latin': '..ka',
        'arti_id': '..MU (LK)',
        'arti_en': '..YOUR / ..YOU',
        'desc_id': '...-mu (1 orang laki-laki)',
        'desc_en': 'Your / You (Single Male, 2nd Person)',
        'jenis_id': 'Muttashil (Tersambung)',
        'jenis_en': 'Attached (Muttashil)',
        'dhamir_type_id': 'Mukhatab (Orang ke-2)',
        'dhamir_type_en': '2nd Person (Mukhatab)',
        'gender_id': 'Mudzakkar (Laki-laki)',
        'gender_en': 'Masculine (Mudzakkar)',
        'bilangan_id': 'Mufrad (Tunggal)',
        'bilangan_en': 'Singular (Mufrad)',
        'posisi_id': 'Nashab/Jar (Objek/Milik)',
        'posisi_en': 'Accusative/Genitive (Object/Possessive)',
        'keterangan': '...-mu (1 orang laki-laki)'
    },
    '6c': {
        'latin': 'Iyyāka',
        'arti_id': 'HANYA KEPADAMU (LK)',
        'arti_en': 'YOU ALONE (MASC)',
        'desc_id': 'Hanya kepada-Mu (1 orang laki-laki)',
        'desc_en': 'You alone / Unto You only (Single Male, 2nd Person)',
        'jenis_id': 'Munfashil (Terpisah - Iyyaka)',
        'jenis_en': 'Detached (Munfashil - Iyyaka)',
        'dhamir_type_id': 'Mukhatab (Orang ke-2)',
        'dhamir_type_en': '2nd Person (Mukhatab)',
        'gender_id': 'Mudzakkar (Laki-laki)',
        'gender_en': 'Masculine (Mudzakkar)',
        'bilangan_id': 'Mufrad (Tunggal)',
        'bilangan_en': 'Singular (Mufrad)',
        'posisi_id': 'Nashab (Objek Khusus)',
        'posisi_en': 'Accusative (Exclusive Object)',
        'keterangan': 'Hanya kepada-Mu (1 orang laki-laki)'
    },
    '8a': {
        'latin': 'Antum',
        'arti_id': 'KALIAN (LK)',
        'arti_en': 'YOU ALL (MASC)',
        'desc_id': 'Kalian (banyak laki-laki)',
        'desc_en': 'You all (Plural Male, 2nd Person)',
        'jenis_id': 'Munfashil (Terpisah)',
        'jenis_en': 'Detached (Munfashil)',
        'dhamir_type_id': 'Mukhatab (Orang ke-2)',
        'dhamir_type_en': '2nd Person (Mukhatab)',
        'gender_id': 'Mudzakkar (Laki-laki)',
        'gender_en': 'Masculine (Mudzakkar)',
        'bilangan_id': 'Jamak (Banyak)',
        'bilangan_en': 'Plural (Jamak)',
        'posisi_id': "Rafa' (Subjek)",
        'posisi_en': 'Nominative (Subject)',
        'keterangan': 'Kalian (banyak laki-laki)'
    },
    '8b': {
        'latin': '..kum',
        'arti_id': '..KALIAN (LK)',
        'arti_en': '..YOUR / ..YOU ALL',
        'desc_id': '...-kalian (banyak laki-laki)',
        'desc_en': 'Your / You all (Plural Male, 2nd Person)',
        'jenis_id': 'Muttashil (Tersambung)',
        'jenis_en': 'Attached (Muttashil)',
        'dhamir_type_id': 'Mukhatab (Orang ke-2)',
        'dhamir_type_en': '2nd Person (Mukhatab)',
        'gender_id': 'Mudzakkar (Laki-laki)',
        'gender_en': 'Masculine (Mudzakkar)',
        'bilangan_id': 'Jamak (Banyak)',
        'bilangan_en': 'Plural (Jamak)',
        'posisi_id': 'Nashab/Jar (Objek/Milik)',
        'posisi_en': 'Accusative/Genitive (Object/Possessive)',
        'keterangan': '...-kalian (banyak laki-laki)'
    },
    '11a': {
        'latin': 'Anā',
        'arti_id': 'SAYA / AKU',
        'arti_en': 'I / ME',
        'desc_id': 'Saya / Aku (Tunggal L/P)',
        'desc_en': 'I / Me (Single 1st Person M/F)',
        'jenis_id': 'Munfashil (Terpisah)',
        'jenis_en': 'Detached (Munfashil)',
        'dhamir_type_id': 'Mutakallim (Orang ke-1)',
        'dhamir_type_en': '1st Person (Mutakallim)',
        'gender_id': 'Mudzakkar / Muannats',
        'gender_en': 'Masculine / Feminine',
        'bilangan_id': 'Mufrad (Tunggal)',
        'bilangan_en': 'Singular (Mufrad)',
        'posisi_id': "Rafa' (Subjek)",
        'posisi_en': 'Nominative (Subject)',
        'keterangan': 'Saya / Aku (Tunggal L/P)'
    },
    '11b': {
        'latin': '..ī / ..ya',
        'arti_id': '..KU (AKU/SAYA LK/PR)',
        'arti_en': '..MY / ..ME',
        'desc_id': '...-ku (Tunggal L/P)',
        'desc_en': 'My / Me (Single 1st Person M/F)',
        'jenis_id': 'Muttashil (Tersambung)',
        'jenis_en': 'Attached (Muttashil)',
        'dhamir_type_id': 'Mutakallim (Orang ke-1)',
        'dhamir_type_en': '1st Person (Mutakallim)',
        'gender_id': 'Mudzakkar / Muannats',
        'gender_en': 'Masculine / Feminine',
        'bilangan_id': 'Mufrad (Tunggal)',
        'bilangan_en': 'Singular (Mufrad)',
        'posisi_id': 'Nashab/Jar (Objek/Milik)',
        'posisi_en': 'Accusative/Genitive (Object/Possessive)',
        'keterangan': '...-ku (Tunggal L/P)'
    },
    '12a': {
        'latin': 'Naḥnu',
        'arti_id': 'KAMI / KITA',
        'arti_en': 'WE / US',
        'desc_id': 'Kami / Kita (Jamak L/P)',
        'desc_en': 'We / Us (Plural / Royal 1st Person M/F)',
        'jenis_id': 'Munfashil (Terpisah)',
        'jenis_en': 'Detached (Munfashil)',
        'dhamir_type_id': 'Mutakallim (Orang ke-1)',
        'dhamir_type_en': '1st Person (Mutakallim)',
        'gender_id': 'Mudzakkar / Muannats',
        'gender_en': 'Masculine / Feminine',
        'bilangan_id': 'Jamak (Banyak/Agung)',
        'bilangan_en': 'Plural / Royal (Jamak)',
        'posisi_id': "Rafa' (Subjek)",
        'posisi_en': 'Nominative (Subject)',
        'keterangan': 'Kami / Kita (Jamak L/P)'
    },
    '12b': {
        'latin': '..nā',
        'arti_id': '..KAMI / ..KITA',
        'arti_en': '..OUR / ..US',
        'desc_id': '...-kami / ...-kita (Jamak L/P)',
        'desc_en': 'Our / Us (Plural / Royal 1st Person M/F)',
        'jenis_id': 'Muttashil (Tersambung)',
        'jenis_en': 'Attached (Muttashil)',
        'dhamir_type_id': 'Mutakallim (Orang ke-1)',
        'dhamir_type_en': '1st Person (Mutakallim)',
        'gender_id': 'Mudzakkar / Muannats',
        'gender_en': 'Masculine / Feminine',
        'bilangan_id': 'Jamak (Banyak/Agung)',
        'bilangan_en': 'Plural / Royal (Jamak)',
        'posisi_id': 'Nashab/Jar (Objek/Milik)',
        'posisi_en': 'Accusative/Genitive (Object/Possessive)',
        'keterangan': '...-kami / ...-kita (Jamak L/P)'
    }
}

for item in raw_data:
    s_no = int(item['SURAT']) if item['SURAT'] is not None else None
    a_no = int(item['AYAT']) if item['AYAT'] is not None else None
    
    if s_no and s_no in surahs:
        item['SuratNama'] = surahs[s_no]['nama']
        item['SuratArab'] = surahs[s_no]['arab']
        item['SuratArti'] = surahs[s_no]['arti_id']
        item['SuratArtiID'] = surahs[s_no]['arti_id']
        item['SuratArtiEN'] = surahs[s_no]['arti_en']
    else:
        item['SuratNama'] = f'Surat {s_no}'
        item['SuratArab'] = ''
        item['SuratArti'] = ''
        item['SuratArtiID'] = ''
        item['SuratArtiEN'] = ''
        
    nk = item.get('No kata')
    if nk in grammatical_metadata:
        gm = grammatical_metadata[nk]
        item['Grammar'] = gm
        item['Latin'] = gm['latin']
        item['ArtiKataID'] = gm['arti_id']
        item['ArtiKataEN'] = gm['arti_en']
        
    # Set English Verse Translation
    verse_key = f"{s_no}:{a_no}"
    item['TeksArtiID'] = item.get('TeksArti', '')
    item['TeksArtiEN'] = en_trans.get(verse_key, item.get('TeksArti', ''))

js_content = f'''/**
 * Data Dhamir Al-Qur'an & Kamus Surah (Bilingual: Indonesian & English)
 * Otomatis dibuat dari dataset DHAMIR & Sumber Kemenag RI / Sahih International
 */
const DHAMIR_DATA = {json.dumps(raw_data, ensure_ascii=False, indent=2)};

const SURAH_DICT = {json.dumps(surahs, ensure_ascii=False, indent=2)};

const GRAMMAR_INFO = {json.dumps(grammatical_metadata, ensure_ascii=False, indent=2)};
'''

with open('d:/Dhamir/dhamir_data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

with open('d:/Dhamir/dhamir_data.json', 'w', encoding='utf-8') as f:
    json.dump(raw_data, f, ensure_ascii=False, indent=2)

print(f"Berhasil menghasilkan dhamir_data.js & json dwibahasa dengan {len(raw_data)} entri lengkap!")
