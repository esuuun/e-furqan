import openpyxl
import json
import sys

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

wb = openpyxl.load_workbook('KAMUS Harf Ghair Amil.xlsx', data_only=True)
ws = wb['KAMUS KATA']
rows = list(ws.iter_rows(values_only=True))

def standardize_cat(raw_b, raw_nk):
    raw_b = str(raw_b).strip()
    raw_nk = str(raw_nk).strip()
    
    if raw_b.startswith('1.'): return '1. Harf Nafyi'
    if raw_b.startswith('2.'): return '2. Harf Tahqiq Taswif'
    if raw_b.startswith('3.'): return '3. Harf Syarat'
    if raw_b.startswith('4.'): return '4. Harf Mashdariyah'
    if raw_b.startswith('5.'): return '5. Harf Zaidah'
    if 'ISTIFHAM' in raw_b.upper(): return '6. Harf Istifham'
    if 'JAWAB' in raw_b.upper(): return '7. Harf Jawab'
    if 'IBTIDA' in raw_b.upper(): return '8. Harf Ibtida\''
    if 'TAFSHIL' in raw_b.upper(): return '9. Harf Tafshil'
    if 'MUFAJAAH' in raw_b.upper(): return '10. Harf Mufaja\'ah'
    if 'MUFASSIRAH' in raw_b.upper(): return '11. Harf Mufassirah'
    if 'ISTIFTAHIYAH' in raw_b.upper(): return '12. Harf Istiftahiyah'
    if 'RADA' in raw_b.upper(): return '13. Harf Rada\''
    if 'TA\'AJUB' in raw_b.upper() or 'TAAJUB' in raw_b.upper(): return '14. Harf Ta\'ajjub'
    if 'FARIQAH' in raw_b.upper(): return '15. Harf Fariqah'
    if 'MAUTHI' in raw_b.upper(): return '16. Harf Mauthi\'ah'
    if 'MABANY' in raw_b.upper(): return '17. Harf Mabany'
    return raw_b

cat_words = {}
for r in rows[1:]:
    if not any(r): continue
    b, nk, k, ak, fk, s, a, jlh = r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]
    std_b = standardize_cat(b, nk)
    nk_str = str(nk).strip()
    k_str = str(k).strip() if k is not None else ''
    ak_str = str(ak).strip() if ak is not None else ''
    
    if std_b not in cat_words:
        cat_words[std_b] = {}
    if nk_str not in cat_words[std_b]:
        cat_words[std_b][nk_str] = {'kata': k_str, 'arti': ak_str, 'frek': fk, 'count': 0}
    cat_words[std_b][nk_str]['count'] += 1

print(f"Total standardized categories: {len(cat_words)}")
for b in sorted(cat_words.keys(), key=lambda x: int(x.split('.')[0])):
    print(f"\n{b} ({len(cat_words[b])} kata):")
    for nk, info in sorted(cat_words[b].items(), key=lambda x: int(x[0])):
        print(f"   [{nk:>2}] {info['kata']:<12} | {info['arti']:<40} | Frek: {str(info['frek']):<5} | {info['count']} ayat")
