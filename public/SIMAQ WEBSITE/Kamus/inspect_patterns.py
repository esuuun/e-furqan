import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract ARABIC_WORD_PATTERNS object
start = content.find('const ARABIC_WORD_PATTERNS = {')
if start != -1:
    end = content.find('};', start)
    patterns_text = content[start:end+2]
    # Find all keys
    keys = re.findall(r'"([^"]+)":\s*\[', patterns_text)
    print(f"Total keys in ARABIC_WORD_PATTERNS: {len(keys)}")
    harf_keys = [k for k in keys if 'Harf' in k]
    print(f"Harf keys ({len(harf_keys)}):")
    for k in harf_keys:
        print(f"  {k}")
    
    print("\nNon-Harf keys sample:")
    for k in keys[:15]:
        print(f"  {k}")
