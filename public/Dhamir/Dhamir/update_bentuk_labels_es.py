import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('build_multilingual_dataset.py', 'r', encoding='utf-8') as f:
    code = f.read()

import build_multilingual_dataset as bmd
es_labels = {
    "1. Dhamir": "1. Pronombres (Dhamir)",
    "2. Mawshul": "2. Pronombres Relativos (Mawshul)",
    "3. Istifham": "3. Interrogativos (Istifham)",
    "4. Syarath": "4. Condicionales (Syarath)",
    "5. Isyarah": "5. Demostrativos (Isyarah)",
    "6. Isim Fi'il": "6. Nombres Verbales (Isim Fi'il)",
    "7. Fi'il Jamid": "7. Verbos Inflexibles (Fi'il Jamid)"
}

for b_key, es_val in es_labels.items():
    if b_key in bmd.BENTUK_LABELS:
        bmd.BENTUK_LABELS[b_key]['es'] = es_val

import json
b_str = 'BENTUK_LABELS = ' + json.dumps(bmd.BENTUK_LABELS, ensure_ascii=False, indent=4)
start_tag = 'BENTUK_LABELS = {'
pos_start = code.find(start_tag)
pos_end = code.find('\n\nGRAMMATICAL_METADATA', pos_start)

if pos_start != -1 and pos_end != -1:
    code = code[:pos_start] + b_str + code[pos_end:]
    with open('build_multilingual_dataset.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print('Updated BENTUK_LABELS successfully!')
else:
    print('Failed to find BENTUK_LABELS position markers:', pos_start, pos_end)
