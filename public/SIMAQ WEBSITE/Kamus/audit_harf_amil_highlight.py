import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('harf_amil_data.json', 'r', encoding='utf-8') as f:
    harf_data = json.load(f)

print(f"Total entries in harf_amil_data: {len(harf_data)}")

def clean_arabic_for_highlight(text):
    if not text: return ''
    t = re.sub(r'[\.\d\(\)\[\]_\-ـ\s]', '', text)
    t = re.sub(r'[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u08D0-\u08FF\u06DF\u06E0\u06E2\u06E5\u06E6]', '', t)
    t = re.sub(r'[إأآٱ]', 'ا', t)
    t = re.sub(r'[ىيئ]', 'ي', t)
    t = re.sub(r'[ؤ]', 'و', t).replace('ء', '')
    t = re.sub(r'ة', 'ه', t)
    return t

# Check expansions needed for Harf 'Amil
ARABIC_SPECIAL_EXPANSIONS = {
    'مِنْ': ['من', 'ومن', 'فمن', 'لمن', 'بمن', 'عمن', 'ممن'],
    'فِي': ['في', 'وفي', 'ففي', 'لفي', 'وفيه', 'فيهم', 'فيها', 'فينا', 'فيكم', 'فيك', 'فيكما', 'فيهما'],
    'عَلَىٰ': ['علي', 'وعلي', 'فعلي', 'لعلي', 'عليه', 'عليهم', 'عليها', 'علينا', 'عليكم', 'عليك', 'عليهما'],
    'إِلَىٰ': ['الي', 'والي', 'فالي', 'اليه', 'اليهم', 'اليها', 'الينا', 'اليكم', 'اليك', 'اليهما'],
    'عَنْ': ['عن', 'وعن', 'فعن', 'عنه', 'عنهم', 'عنها', 'عنا', 'عنكم', 'عنك', 'عنهما'],
    'مِمَّا': ['مما', 'ومما', 'فمما'],
    'عَمَّا 1': ['عما', 'وعما', 'فعما'],
    'عَمَّا 2': ['عما', 'وعما', 'فعما'],
    'عَمَّ': ['عم', 'وعم', 'فعم'],
    'مِمَّن': ['ممن', 'وممن', 'فممن'],
    'مِمَّ': ['مم', 'ومم', 'فمم'],
    'فِيمَا': ['فيما', 'وفيما', 'ففيما'],
    'فِيمَ': ['فيم', 'وفيم', 'ففيم'],
    'حَتَّىٰ 3': ['حتي', 'وحتي', 'فحتي'],
    'حَتَّىٰ 1': ['حتي', 'وحتي', 'فحتي'],
    'حَتَّىٰ': ['حتي', 'وحتي', 'فحتي'],
    'رُّبَمَا': ['ربما', 'وربما', 'فربما'],
    'أَنْ 1': ['ان', 'وان', 'فان', 'بان', 'لان', 'ابان', 'فبان'],
    'أَنْ': ['ان', 'وان', 'فان', 'بان', 'لان'],
    'لَنْ': ['لن', 'ولن', 'فلن'],
    'كَيْ': ['كي', 'وكي', 'فكي', 'لكي', 'ولكي', 'فلكي'],
    'كَيۡلَا': ['كيلا', 'لكيلا', 'ولكيلا', 'فلكيلا'],
    'إِنْ 1': ['ان', 'وان', 'فان', 'ولئن', 'لئن', 'افان'],
    'إِنْ': ['ان', 'وان', 'فان', 'ولئن', 'لئن'],
    'لاَ 2': ['لا', 'ولا', 'فلا'],
    'لاَ': ['لا', 'ولا', 'فلا'],
    'لَمۡ': ['لم', 'ولم', 'فلم', 'الم', 'افلم', 'اولم'],
    'لَّمَّا 2': ['لما', 'ولما', 'فلما'],
    'لَّمَّا': ['لما', 'ولما', 'فلما'],
    'إِلَّا 1': ['الا', 'والا', 'فالا'],
    'إِلَّا 2': ['الا', 'والا', 'فالا'],
    'إِلَّا': ['الا', 'والا', 'فالا'],
    'إِلَّمۡ': ['الم', 'فالم', 'والا', 'فان لم', 'فالم'],
    'ثُمَّ': ['ثم', 'وثم', 'فثم'],
    'أَوْ': ['او', 'واو', 'فاو'],
    'بَلْ': ['بل', 'وبل', 'فبل'],
    'أَمْ': ['ام', 'وام', 'فام'],
    'لَٰكِنْ': ['لكن', 'ولكن', 'فلكن'],
    'إِمَّا 2': ['اما', 'واما', 'فاما'],
    'إِمَّا': ['اما', 'واما', 'فاما'],
    'أَمَّن 1': ['امن', 'وامن', 'فامن'],
    'أَمَّن 2': ['امن', 'وامن', 'فامن'],
    'أَمَّا': ['اما', 'واما', 'فاما'],
    'أَمَّاذَا': ['اماذا', 'واماذا', 'فاماذا'],
    'لَكِنْ أنا': ['لكنا', 'ولكنا', 'لكن انا', 'ولكن انا', 'لكن'],
    'إِنَّ': ['ان', 'وان', 'فان', 'لان', 'وانك', 'وانكم', 'واني', 'وانا', 'وانه', 'وانهم', 'وانهن', 'وانها', 'واننا'],
    'أَنَّ': ['ان', 'وان', 'فان', 'بان', 'لان', 'وانك', 'وانكم', 'واني', 'وانا', 'وانه', 'وانهم', 'وانهن', 'وانها', 'واننا', 'بانه', 'بانهم', 'بانكم'],
    'إِنَّمَا 1': ['انما', 'وانما', 'فانما'],
    'إِنَّمَا 2': ['انما', 'وانما', 'فانما'],
    'لَعَلَّ': ['لعل', 'ولعل', 'فلعل', 'لعله', 'لعلهم', 'لعلكم', 'لعلي', 'لعلنا', 'لعلها'],
    'لَكِنَّ': ['لكن', 'ولكن', 'فلكن', 'ولكنه', 'ولكنهم', 'ولكنكم', 'ولكني', 'ولكننا', 'ولكنها', 'ولكنهن'],
    'كَأَنَّ': ['كان', 'وكان', 'فكان', 'كانه', 'كانهم', 'كانك', 'كانكم', 'كانها', 'كاني', 'كاننا'],
    'لَيْتَ': ['ليت', 'وليت', 'فليت', 'ياليت', 'يا ليت', 'ياليتني', 'ياليتها', 'ياليتنا', 'ياليتهم', 'ياليت قومي'],
    'أَنَّمَا 1': ['انما', 'وانما', 'فانما', 'بانما'],
    'أَنَّمَا 2': ['انما', 'وانما', 'فانما', 'بانما', 'ان', 'ما'],
    'كَأَنَّمَا': ['كانما', 'وكانما', 'فكانما'],
    'أَلَّا 3': ['الا', 'والا', 'فالا', 'ان لا', 'وان لا'],
    'أَلَّا 4': ['الا', 'والا', 'فالا', 'ان لا', 'وان لا'],
    'أَلَّن': ['الن', 'والن', 'فلن', 'ان لن', 'وان لن'],
    'وَيۡكَأَنَّ': ['ويكان', 'فويكان', 'ويكانه', 'ويكانه لا'],
    'أَلَّو': ['الو', 'لو', 'ان', 'وان لو', 'وان لو استقاموا', 'والو']
}

def highlight_arabic_verse(full_arab_text, target_kata, no_kata):
    if not full_arab_text or not target_kata: return full_arab_text
    tokens = set()
    s_no = str(no_kata).strip() if no_kata is not None else ''
    clean_k = clean_arabic_for_highlight(target_kata)
    
    # 1. Special expansions by target_kata
    for exp_k, exp_list in ARABIC_SPECIAL_EXPANSIONS.items():
        if target_kata == exp_k or clean_arabic_for_highlight(exp_k) == clean_k:
            for x in exp_list:
                tokens.add(clean_arabic_for_highlight(x))
                
    # 2. Parts
    parts = re.split(r'[/,\s]+', target_kata)
    for p in parts:
        cl = clean_arabic_for_highlight(p)
        if cl:
            tokens.add(cl)
            for exp_k, exp_list in ARABIC_SPECIAL_EXPANSIONS.items():
                if cl == clean_arabic_for_highlight(exp_k):
                    for x in exp_list:
                        tokens.add(clean_arabic_for_highlight(x))
                        
    words = full_arab_text.split()
    matched_indices = []
    for idx, w in enumerate(words):
        clean_w = clean_arabic_for_highlight(w)
        if not clean_w: continue
        
        # Check exact token match or root contains
        is_match = False
        if clean_w in tokens:
            is_match = True
        else:
            for t in tokens:
                if len(t) >= 2 and (clean_w == t or clean_w.startswith(t) or clean_w.endswith(t) or t in clean_w):
                    is_match = True
                    break
        if is_match:
            matched_indices.append((idx, w))
            
    return matched_indices

unmatched = []
for idx, entry in enumerate(harf_data):
    s = entry['SURAT']
    a = entry['AYAT']
    b = entry['Bentuk Kata']
    nk = entry['No kata']
    k = entry['Kata']
    t_arab = entry.get('TeksArab', '')
    
    matches = highlight_arabic_verse(t_arab, k, nk)
    if not matches:
        unmatched.append({
            'idx': idx,
            'ref': f"QS. {s}:{a}",
            'bentuk': b,
            'no': nk,
            'kata': k,
            'teks': t_arab
        })

print(f"\nHighlight Audit Results for Kamus Harf 'Amil:")
print(f"Total Verses Tested: {len(harf_data)}")
print(f"Matched Successfully: {len(harf_data) - len(unmatched)}")
print(f"Unmatched: {len(unmatched)}")

if unmatched:
    print("\nUnmatched Details:")
    for u in unmatched:
        print(f"  [{u['ref']}] {u['bentuk']} #{u['no']} Kata: '{u['kata']}' -> Text: {u['teks']}")
else:
    print("\n[PERFECT] 100% of all Harf 'Amil verses have successful Arabic target highlights!")
