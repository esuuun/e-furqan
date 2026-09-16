import re

with open('scratch/simaq_bundle.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's search for W1 usages
# e.g. jsx(W1, {title: ...}) or similar
idx = text.find("W1=")
if idx != -1:
    print(text[idx:idx+3000])

with open('scratch/w1_snippet.txt', 'w', encoding='utf-8') as f:
    f.write(text[idx:idx+4000])
