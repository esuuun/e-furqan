import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

cfg_start = text.find('const LANG_CONFIG = {')
snippet = text[cfg_start:cfg_start + 30000]
langs = re.findall(r"^\s*['\"]([a-zA-Z0-9\-_]+)['\"]:\s*\{", snippet, re.MULTILINE)
print(f"Found {len(langs)} languages in LANG_CONFIG:")
print(langs)
