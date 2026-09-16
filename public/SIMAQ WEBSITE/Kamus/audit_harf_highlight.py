import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('harf_data.json', 'r', encoding='utf-8') as f:
    harf_data = json.load(f)

print(f"Total entries in harf_data: {len(harf_data)}")

# Group by (Bentuk Kata, No kata)
groups = {}
for entry in harf_data:
    b = entry.get('Bentuk Kata')
    no = entry.get('No kata')
    k = entry.get('Kata')
    key = f"{b}__{no}"
    if key not in groups:
        groups[key] = {
            'bentuk': b,
            'noKata': str(no),
            'kata': k,
            'entries': []
        }
    groups[key]['entries'].append(entry)

def test_highlight(kata_clean, text):
    if not text or not kata_clean:
        return False
    # Exact literal or regex match
    pattern = re.escape(kata_clean)
    return bool(re.search(pattern, text))

results = []
for key, group in groups.items():
    kata = group['kata']
    clean_target = re.sub(r'\s*\d+$', '', kata).replace('..', '').strip()
    
    total = len(group['entries'])
    matched = 0
    failures = []
    
    for entry in group['entries']:
        surat = entry.get('SURAT')
        ayat = entry.get('AYAT')
        teks_arab = entry.get('TeksArab', '')
        
        # Test if clean_target matches
        if test_highlight(clean_target, teks_arab):
            matched += 1
        else:
            failures.append({
                'surat': surat,
                'ayat': ayat,
                'teks_arab': teks_arab
            })
            
    results.append({
        'key': key,
        'kata': kata,
        'clean_target': clean_target,
        'total': total,
        'matched': matched,
        'failures': failures
    })

print(f"\n=== HARF HIGHLIGHT AUDIT REPORT ===")
failed_count = 0
for r in results:
    if r['matched'] < r['total']:
        failed_count += 1
        print(f"\n[FAIL] {r['key']} | Kata: '{r['kata']}' -> Clean: '{r['clean_target']}' | Matched {r['matched']}/{r['total']}")
        for f in r['failures']:
            print(f"   QS. {f['surat']}:{f['ayat']}")
            print(f"   Verse: {f['teks_arab']}")
    else:
        print(f"[OK] {r['key']} | Kata: '{r['kata']}' ({r['matched']}/{r['total']})")

print(f"\nSummary: {failed_count} / {len(results)} groups have highlighting failures!")
