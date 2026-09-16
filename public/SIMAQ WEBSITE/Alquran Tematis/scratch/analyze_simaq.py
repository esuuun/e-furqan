import re
import sys

with open('scratch/simaq_bundle.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

out_lines = []

# Extract features and cards from landing page
# Find sections like hero, features, testimonials, footer
out_lines.append("=== ALL EXTRACTED UI HEADINGS & DESCRIPTIONS ===")

matches = re.findall(r'children:\"([^\"]{10,250})\"', text)
for m in matches:
    if any(w in m.lower() for w in ['quran', 'al-qur', 'simaq', 'belajar', 'fitur', 'metode', 'arab', 'tajwid', 'mushaf', 'tematis', 'hafalan', 'tahfidz', 'nahwu', 'terjemah', 'materi', 'interaktif', 'modern', 'gratis']):
        out_lines.append(f"- {m}")

# Search for component definitions or module names
out_lines.append("\n=== MODULES & FEATURES ===")
# Find module descriptions
module_names = ['QMushaf', 'QTajwid', 'QTahfidz', 'QNahwu', 'QThematic']
for mod in module_names:
    out_lines.append(f"\n--- {mod} ---")
    pos = 0
    found_count = 0
    while True:
        idx = text.lower().find(mod.lower(), pos)
        if idx == -1 or found_count >= 5:
            break
        snippet = text[max(0, idx-150):min(len(text), idx+300)]
        out_lines.append(f"[Snippet {found_count+1}]: {snippet}\n")
        pos = idx + len(mod)
        found_count += 1

with open('scratch/simaq_analysis.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))

print("Analysis saved to scratch/simaq_analysis.txt")
