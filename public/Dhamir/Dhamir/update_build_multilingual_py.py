import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

from build_spanish_metadata import SPANISH_SURAHS, BENTUK_KATA_ES, SPANISH_GRAMMAR

with open('build_multilingual_dataset.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update SURAHS in build_multilingual_dataset.py
for s_num, es_name in SPANISH_SURAHS.items():
    # find "arti_zh": "..." in this surah block
    target = f'"{s_num}": {{\n'
    pos = code.find(target)
    if pos != -1:
        end_surah = code.find('},\n', pos)
        if end_surah != -1:
            zh_pos = code.find('"arti_zh":', pos)
            if zh_pos != -1 and zh_pos < end_surah:
                zh_line_end = code.find('\n', zh_pos)
                if '"arti_es":' not in code[pos:end_surah]:
                    insert_str = f'\n        "arti_es": "{es_name}",'
                    code = code[:zh_line_end] + insert_str + code[zh_line_end:]

# 2. Update GRAMMATICAL_METADATA in build_multilingual_dataset.py
import build_multilingual_dataset as bmd
for k, val in SPANISH_GRAMMAR.items():
    if k in bmd.GRAMMATICAL_METADATA:
        bmd.GRAMMATICAL_METADATA[k].update(val)

start_tag = 'GRAMMATICAL_METADATA = {'
start_pos = code.find(start_tag)
pos_last = code.find('7. Fi\'il Jamid__8')
end_pos = code.find('}\n}', pos_last) + 3

if start_pos != -1 and end_pos != -1:
    new_block = 'GRAMMATICAL_METADATA = ' + json.dumps(bmd.GRAMMATICAL_METADATA, ensure_ascii=False, indent=4)
    code = code[:start_pos] + new_block + code[end_pos:]

# 3. Update load_caches() in build_multilingual_dataset.py
code = code.replace(
    "'zh': {}\n    }",
    "'zh': {},\n        'es': {}\n    }"
)
code = code.replace(
    "'zh': 'zh_translations.json'\n    }",
    "'zh': 'zh_translations.json',\n        'es': 'es_translations.json'\n    }"
)

# 4. Update BentukKataES & SuratArtiES & TeksArtiES in build_multilingual_dataset.py
code = code.replace(
    "item['SuratArtiZH'] = s_info.get('arti_zh', '')",
    "item['SuratArtiZH'] = s_info.get('arti_zh', '')\n            item['SuratArtiES'] = s_info.get('arti_es', s_info['arti_en'])"
)

code = code.replace(
    "item['SuratArtiZH'] = \"\"",
    "item['SuratArtiZH'] = \"\"\n            item['SuratArtiES'] = \"\""
)

code = code.replace(
    "item['TeksArtiZH'] = caches['zh'].get(v_key, teks_id)",
    "item['TeksArtiZH'] = caches['zh'].get(v_key, teks_id)\n\n        # ES\n        item['TeksArtiES'] = caches['es'].get(v_key, teks_id)"
)

code = code.replace(
    "item['BentukKataZH'] = item.get('BentukKataZH', b)",
    "item['BentukKataZH'] = item.get('BentukKataZH', b)\n        item['BentukKataES'] = BENTUK_KATA_ES.get(b, b)"
)

# Add BENTUK_KATA_ES definition if not present
if 'BENTUK_KATA_ES =' not in code:
    b_def = 'BENTUK_KATA_ES = ' + json.dumps(BENTUK_KATA_ES, ensure_ascii=False, indent=4) + '\n\n'
    code = code.replace('def highlight_arabic_verse', b_def + 'def highlight_arabic_verse')

with open('build_multilingual_dataset.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_multilingual_dataset.py successfully!")
