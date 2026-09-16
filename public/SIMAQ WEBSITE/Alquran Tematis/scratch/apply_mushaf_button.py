# scratch/apply_mushaf_button.py
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update button in generateUraianGroupMarkup
old_btn = '''                                            <button class="tts-button" style="color: #38bdf8; border-color: #38bdf8; background-color: rgba(56, 189, 248, 0.1);" onclick="lookupVerseInSearch(${v.surah_num}, ${v.ayat_num}, event)" title="Lihat di Pencari Surat & Ayat">
                                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                                                <span data-i18n-orig="Cari Ayat">Cari Ayat</span>
                                            </button>'''

new_btn = '''                                            <button class="tts-button" style="color: #38bdf8; border-color: #38bdf8; background-color: rgba(56, 189, 248, 0.1);" onclick="lookupVerseInSearch(${v.surah_num}, ${v.ayat_num}, event)" title="Lihat Mushaf Per Kata">
                                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                                                <span data-i18n-orig="Lihat Mushaf Per Kata">Lihat Mushaf Per Kata</span>
                                            </button>'''

assert old_btn in c, 'old_btn not found'
c = c.replace(old_btn, new_btn, 1)

# 2. Add translations in LANG_UI_MAP
old_en = "'Cari Ayat': 'Search Ayah',"
new_en = "'Lihat Mushaf Per Kata': 'View Word-by-Word Mushaf',\n                'Cari Ayat': 'Search Ayah',"
assert old_en in c, 'old_en not found'
c = c.replace(old_en, new_en, 1)

old_ar = "'Cari Ayat': 'بحث عن الآية',"
new_ar = "'Lihat Mushaf Per Kata': 'عرض المصحف كلمة بكلمة',\n                'Cari Ayat': 'بحث عن الآية',"
assert old_ar in c, 'old_ar not found'
c = c.replace(old_ar, new_ar, 1)

old_ms = "'Cari Ayat': 'Cari Ayat',"
new_ms = "'Lihat Mushaf Per Kata': 'Lihat Mushaf Per Kata',\n                'Cari Ayat': 'Cari Ayat',"
assert old_ms in c, 'old_ms not found'
c = c.replace(old_ms, new_ms, 1)

old_ur = "'Cari Ayat': 'آیت تلاش کریں',"
new_ur = "'Lihat Mushaf Per Kata': 'مصحف لفظ بہ لفظ دیکھیں',\n                'Cari Ayat': 'آیت تلاش کریں',"
assert old_ur in c, 'old_ur not found'
c = c.replace(old_ur, new_ur, 1)

old_tr = "'Cari Ayat': 'Ayet Ara',"
new_tr = "'Lihat Mushaf Per Kata': 'Kelime Kelime Mushafı Görüntüle',\n                'Cari Ayat': 'Ayet Ara',"
assert old_tr in c, 'old_tr not found'
c = c.replace(old_tr, new_tr, 1)

old_fr = "'Cari Ayat': 'Chercher verset',"
new_fr = "'Lihat Mushaf Per Kata': 'Voir le Coran mot à mot',\n                'Cari Ayat': 'Chercher verset',"
assert old_fr in c, 'old_fr not found'
c = c.replace(old_fr, new_fr, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Successfully applied button change to index.html!')
