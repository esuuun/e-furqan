import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# The 52 Harf patterns
harf_patterns = {
    # 1. Harf Nafyi
    "1. Harf Nafyi__1": ["اَفَلَا", "أَفَلَا", "وَلَا", "وَلاَ", "فَلَا", "فَلاَ", "لَآ", "لَا", "لاَ"],
    "1. Harf Nafyi__2": ["اَفَمَا", "أَفَمَا", "فَمَآ", "فَمَا", "وَّمَا", "وَمَآ", "وَمَا", "مَآ", "مَّا", "مَا"],
    "1. Harf Nafyi__3": ["وَاِنْ", "وَإِنْ", "فَاِنْ", "فَإِنْ", "اِنْ", "إِنْ"],
    "1. Harf Nafyi__4": ["فَهَلْ", "وَهَلْ", "هَلْ"],
    "1. Harf Nafyi__5": ["وَّلَاتَ", "وَلَاتَ", "لَاتَ"],
    "1. Harf Nafyi__6": ["فَمَاذَا", "وَمَاذَا", "مَاذَا"],

    # 2. Harf Tahqiq Taswif
    "2. Harf Tahqiq Taswif__7": ["وَلَقَدْ", "فَقَدْ", "لَقَدْ", "قَدْ"],
    "2. Harf Tahqiq Taswif__8": ["وَلَسَوْفَ", "فَسَوْفَ", "لَسَوْفَ", "سَوْفَ"],

    # 3. Harf Syarat
    "3. Harf Syarat__9": ["وَلَوْ", "فَلَوْ", "لَّوْ", "لَوْ"],
    "3. Harf Syarat__10": ["وَلَوْلَآ", "وَلَوْلَا", "فَلَوْلَا", "لَوْلَآ", "لَوْلَا", "لَوۡلَا"],
    "3. Harf Syarat__11": ["وَلَوْ", "فَلَوْ", "لَّوْ", "لَوْ"],
    "3. Harf Syarat__12": ["وَاِمَّا", "فَاِمَّا", "وَإِمَّا", "فَإِمَّا", "اِمَّا", "إِمَّا"],
    "3. Harf Syarat__13": ["مَهْمَا", "مَهۡمَا"],

    # 4. Harf Mashdariyah
    "4. Harf Mashdariyah__14": ["كَمَآ", "كَمَا", "بِمَآ", "بِمَا", "مَآ", "مَّا", "مَا"],
    "4. Harf Mashdariyah__15": ["اَلَّا", "أَلَّا"],
    "4. Harf Mashdariyah__16": ["بِاَنْ", "بِأَنْ", "وَاَنْ", "وَأَنْ", "اَنْ", "أَنْ"],
    "4. Harf Mashdariyah__17": ["وَلَوْ", "فَلَوْ", "لَّوْ", "لَوْ"],
    "4. Harf Mashdariyah__18": ["اَلَّا", "أَلَّا"],
    "4. Harf Mashdariyah__19": ["اَلَّا", "أَلَّا"],

    # 5. Harf Zaidah
    "5. Harf Zaidah__20": ["كَمَآ", "كَمَا"],
    "5. Harf Zaidah__21": ["مَّا", "مَا"],
    "5. Harf Zaidah__22": ["فَلَآ", "فَلَا", "لَآ", "لَا", "لاَ"],
    "5. Harf Zaidah__23": ["فَبِمَآ", "فَبِمَا", "بِمَا"],
    "5. Harf Zaidah__24": ["اَنْ", "أَنْ"],

    # 6. Harf Istifham
    "6. Harf Istifham__25": ["فَهَلْ", "وَهَلْ", "هَلْ"],

    # 7. Harf Jawab
    "7. Harf Jawab__26": ["اِذًا", "إِذًا", "إِذَنْ", "اِذَنْ"],
    "7. Harf Jawab__27": ["بَلٰى", "بَلَىٰ", "بَلَى"],
    "7. Harf Jawab__28": ["نَعَمْ"],
    "7. Harf Jawab__29": ["اِيْ", "إِيْ", "إِي"],

    # 8. Harf Ibtida'
    "8. Harf Ibtida'__30": ["حَتّٰىٓ", "حَتّٰى", "حَتَّىٰ", "حَتَّى"],

    # 9. Harf Tafshil
    "9. Harf Tafshil__31": ["فَاَمَّا", "فَأَمَّا", "وَاَمَّا", "وَأَمَّا", "اَمَّا", "أَمَّا"],

    # 10. Harf Mufaja'ah
    "10. Harf Mufaja'ah__32": ["فَاِذَا", "فَإِذَا", "وَاِذَا", "وَإِذَا", "اِذَا", "إِذَا"],

    # 11. Harf Mufassirah
    "11. Harf Mufassirah__33": ["وَاَنِ", "وَاَنْ", "وَأَنْ", "اَنِ", "أَنِ", "اَنْ", "أَنْ"],

    # 12. Harf Istiftahiyah
    "12. Harf Istiftahiyah__34": ["اَلَآ", "اَلَا", "أَلَآ", "أَلَا", "أَلاَ"],

    # 13. Harf Rada'
    "13. Harf Rada'__35": ["كَلَّآ", "كَلَّا", "كَلاَّ"],

    # 14. Harf Ta'ajjub
    "14. Harf Ta'ajjub__36": ["مَآ", "مَا"],

    # 15. Harf Fariqah
    "15. Harf Fariqah__37": ["لَّمَّا", "لَمَّا"],

    # 16. Harf Mauthi'ah
    "16. Harf Mauthi'ah__38": ["لَّمَّا", "لَمَّا"],

    # 17. Harf Mabany (Fawatih as-Suwar)
    "17. Harf Mabany__39": ["حٰمۤ", "حٰمٓ", "حٰم", "حم"],
    "17. Harf Mabany__40": ["الۤمّۤ", "الۤمّۤ", "الۤم", "الٓمّٓ", "الٓم", "الم"],
    "17. Harf Mabany__41": ["الۤرٰ", "الۤر", "الٓرٰ", "الٓر", "الر"],
    "17. Harf Mabany__42": ["طٰسۤمّۤ", "طٰسۤم", "طٰسٓمّٓ", "طٰسٓم", "طسم"],
    "17. Harf Mabany__43": ["الۤمّۤرٰ", "الۤمّۤر", "الٓمّٓرٰ", "الٓمّٓر", "المر"],
    "17. Harf Mabany__44": ["الۤمّۤصۤ", "الۤمّۤص", "الٓمّٓصٓ", "الٓمّٓص", "المص"],
    "17. Harf Mabany__45": ["صۤ", "صٓ"],
    "17. Harf Mabany__46": ["طٰسۤ", "طٰسٓ", "طٰس", "طس"],
    "17. Harf Mabany__47": ["طٰهٰ", "طٰه", "طه"],
    "17. Harf Mabany__48": ["عۤسۤقۤ", "عۤسۤق", "عٓسٓقٓ", "عٓسٓق", "عسق"],
    "17. Harf Mabany__49": ["قۤ", "قٓ"],
    "17. Harf Mabany__50": ["كۤهٰيٰعۤصۤ", "كۤهٰيٰعۤص", "كٓهٰيٰعٓصٓ", "كٓهٰيٰعٓص", "كهيعص"],
    "17. Harf Mabany__51": ["نۤ", "نٓ"],
    "17. Harf Mabany__52": ["يٰسۤ", "يٰسٓ", "يٰس", "يس"]
}

with open('app.js', 'r', encoding='utf-8') as f:
    app_code = f.read()

target = '''    "7. Fi'il Jamid__8": [
        "فَنِعِمَّا",
        "نِعِمَّا"
    ]
};'''

replacement_chunks = ['''    "7. Fi'il Jamid__8": [
        "فَنِعِمَّا",
        "نِعِمَّا"
    ],''']

for k, patterns in harf_patterns.items():
    p_json = json.dumps(patterns, ensure_ascii=False, indent=8)
    replacement_chunks.append(f'    "{k}": {p_json},')

replacement_text = '\n'.join(replacement_chunks).rstrip(',') + '\n  };'

if target in app_code:
    app_code = app_code.replace(target, replacement_text, 1)
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(app_code)
    print("Successfully injected 52 Harf patterns into app.js!")
else:
    print("Error: Target anchor not found in app.js!")
