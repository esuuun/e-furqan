import re

with open('scratch/simaq_bundle.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Search for .map(.*W1) or similar
matches = re.findall(r'([a-zA-Z0-9_$]+\.map\([^)]*W1[^)]*\))', text)
print("Map with W1:", matches)

# Find variable before W1=
idx = text.find("W1=")
print("Context before W1=:")
print(text[max(0, idx-1000):idx])
