import json

with open('it_translations.json', 'r', encoding='utf-8') as f:
    it = json.load(f)

v_2_2 = it.get('2:2', '')
print("IT 2:2 characters and their ord:")
for ch in v_2_2:
    if ord(ch) > 127:
        print(f"  char '{ch}' -> ord {ord(ch)} (hex {hex(ord(ch))})")

with open('nl_translations.json', 'r', encoding='utf-8') as f:
    nl = json.load(f)

v_nl = nl.get('2:2', '')
print("NL 2:2 characters and their ord:")
for ch in v_nl:
    if ord(ch) > 127:
        print(f"  char '{ch}' -> ord {ord(ch)} (hex {hex(ord(ch))})")
