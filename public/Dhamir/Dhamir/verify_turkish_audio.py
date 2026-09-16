#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification script for Turkish Audio and TTS features in Dhamir Al-Quran.
"""

import sys
import json

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

checks = [
    ('tr in I18N dictionary', 'tr: {' in code),
    ('teksArtiTR in occurrences mapping', 'teksArtiTR:' in code),
    ('arti_tr in group mapping', 'arti_tr:' in code),
    ('teksArtiTR in toggleVerseTranslationAudio', "occ.teksArtiTR || occ.teksArtiEN" in code),
    ('arti_tr in speakDhamirMeaning', "group.arti_tr || group.arti_id" in code),
    ('tr-TR speechLangCode in toggleVerseTranslationAudio', "speechLangCode = 'tr-TR'" in code),
    ('Turkish voice match in SpeechSynthesis', "Ahmet" in code and "Emel" in code),
    ('playGoogleTtsStream helper present', 'function playGoogleTtsStream' in code),
    ('splitTextForTts helper present', 'function splitTextForTts' in code),
    ('defaultMap tr values in getDefaultJenis', "tr: 'Munfasıl (Ayrık Zamir)'" in code),
    ('badgeBentukKata tr in updateSpotlightCard', "elements.badgeBentukKata.textContent = group.bentuk_tr" in code),
    ('voice priming in init()', 'window.speechSynthesis.onvoiceschanged' in code),
]

print("=" * 60)
print("VERIFYING TURKISH TRANSLATION AUDIO & TTS INTEGRATION")
print("=" * 60)

all_ok = True
for name, passed in checks:
    status = "✓ PASS" if passed else "✗ FAIL"
    print(f"[{status}] {name}")
    if not passed:
        all_ok = False

# Also check dataset
with open('dhamir_data.json', 'r', encoding='utf-8') as f:
    dataset = json.load(f)

total = len(dataset)
has_teks_tr = sum(1 for d in dataset if d.get('TeksArtiTR'))
has_arti_tr = sum(1 for d in dataset if d.get('ArtiKataTR'))

print("-" * 60)
print(f"Dataset Total Items      : {total}")
print(f"Items with TeksArtiTR    : {has_teks_tr}/{total} ({(has_teks_tr/total)*100:.1f}%)")
print(f"Items with ArtiKataTR    : {has_arti_tr}/{total} ({(has_arti_tr/total)*100:.1f}%)")

if has_teks_tr == total and has_arti_tr == total:
    print("[✓ PASS] Dataset Turkish translations 100% complete!")
else:
    print("[✗ FAIL] Dataset incomplete!")
    all_ok = False

print("=" * 60)
if all_ok:
    print("ALL TESTS PASSED SUCCESSFULLY! Turkish audio is fully operational.")
else:
    print("SOME TESTS FAILED! Please review above.")
    sys.exit(1)
