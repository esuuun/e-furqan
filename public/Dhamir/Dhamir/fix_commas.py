import re

with open('build_multilingual_dataset.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'("es":\s*"[^"]+")\s*\n\s*("tr":)', r'\1,\n        \2', text)

with open('build_multilingual_dataset.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Fixed commas!')
