import json

LANG_UI_MAP = {
    'en': {
        'Jelajah Tematis': 'Thematic Explorer',
        'Cari Surat & Ayat': 'Search Surah & Ayah',
        'Pilih Surat & Nomor Ayat': 'Select Surah & Ayah Number',
        'Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan': 'Instantly discover the Theme, Main Subject, and Sub-topic of your selected verse',
        'Surat Al-Qur\'an (1–114):': 'Quran Surah (1–114):',
        'Nomor Ayat:': 'Ayah Number:',
        '-- Pilih Surat --': '-- Select Surah --',
        'Pilih Ayat': 'Select Ayah',
        'Klasifikasi Al-Qur\'an Tematis': 'Thematic Quran Classification',
        'Buka di Halaman Tematik': 'Open in Thematic View',
        'Salin Ayat': 'Copy Ayah',
        'Cari Ayat': 'Search Ayah',
        'Tema Besar:': 'Main Theme:',
        'Pokok Bahasan:': 'Main Subject:',
        'Sub Pokok Bahasan:': 'Sub-topic:',
        'Uraian Khusus:': 'Specific Context:',
        'Pembahasan Tematis': 'Thematic Topics',
        'Belum Ada Pengelompokan Tematik Khusus': 'No Specific Thematic Classification Yet'
    },
    'ar': {
        'Jelajah Tematis': 'التصفح الموضوعي',
        'Cari Surat & Ayat': 'البحث بالسورة والآية',
        'Pilih Surat & Nomor Ayat': 'اختر السورة ورقم الآية',
        'Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan': 'تعرف على الموضوع والمحور الرئيسي والفرعي للآية المختارة فوراً',
        'Surat Al-Qur\'an (1–114):': 'سور القرآن الكريم (1–114):',
        'Nomor Ayat:': 'رقم الآية:',
        '-- Pilih Surat --': '-- اختر السورة --',
        'Pilih Ayat': 'اختر الآية',
        'Klasifikasi Al-Qur\'an Tematis': 'التصنيف الموضوعي للقرآن الكريم',
        'Buka di Halaman Tematik': 'عرض في الصفحة الموضوعية',
        'Salin Ayat': 'نسخ الآية',
        'Cari Ayat': 'بحث عن الآية',
        'Tema Besar:': 'الموضوع الرئيسي:',
        'Pokok Bahasan:': 'المحور الأساسي:',
        'Sub Pokok Bahasan:': 'المحور الفرعي:',
        'Uraian Khusus:': 'البيان التفصيلي:',
        'Pembahasan Tematis': 'مواضيع موضوعية',
        'Belum Ada Pengelompokan Tematik Khusus': 'لا يوجد تصنيف موضوعي محدد حتى الآن'
    },
    'ms': {
        'Jelajah Tematis': 'Jelajah Tematik',
        'Cari Surat & Ayat': 'Cari Surah & Ayat',
        'Pilih Surat & Nomor Ayat': 'Pilih Surah & Nombor Ayat',
        'Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan': 'Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat pilihan anda secara pantas',
        'Surat Al-Qur\'an (1–114):': 'Surah Al-Quran (1–114):',
        'Nomor Ayat:': 'Nombor Ayat:',
        '-- Pilih Surat --': '-- Pilih Surah --',
        'Pilih Ayat': 'Pilih Ayat',
        'Klasifikasi Al-Qur\'an Tematis': 'Klasifikasi Al-Quran Tematik',
        'Buka di Halaman Tematik': 'Buka di Halaman Tematik',
        'Salin Ayat': 'Salin Ayat',
        'Cari Ayat': 'Cari Ayat',
        'Tema Besar:': 'Tema Utama:',
        'Pokok Bahasan:': 'Pokok Bahasan:',
        'Sub Pokok Bahasan:': 'Sub Pokok Bahasan:',
        'Uraian Khusus:': 'Huraian Khusus:',
        'Pembahasan Tematis': 'Perbincangan Tematik',
        'Belum Ada Pengelompokan Tematik Khusus': 'Belum Ada Pengelompokan Tematik Khusus'
    }
}

print("Loaded languages in test:", list(LANG_UI_MAP.keys()))
for lang, mapping in LANG_UI_MAP.items():
    print(f"{lang}: {mapping['Jelajah Tematis']} | {mapping['Cari Surat & Ayat']}")
