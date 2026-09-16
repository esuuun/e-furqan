import re

with open('scratch/simaq_bundle.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

out = []
idx = text.find("sembilan pintu ilmu")
if idx != -1:
    out.append("=== SEMBILAN PINTU ILMU CONTEXT ===")
    out.append(text[max(0, idx-400):min(len(text), idx+2500)])

# Find all occurrences of link:
link_matches = re.findall(r'\{[^{}]*link:\"([^\"]+)\"[^{}]*\}', text)
out.append("\n=== ALL OBJECTS WITH LINKS ===")
for obj in link_matches:
    out.append(f"Link: {obj}")

# Let's search for arrays of features
arrays = re.findall(r'(\[(?:\{[^{}]+?(?:title|name|label):[^{}]+?\},?\s*)+\])', text)
out.append(f"\n=== ARRAYS FOUND: {len(arrays)} ===")
for i, arr in enumerate(arrays[:10]):
    out.append(f"\n--- Array {i+1} ---\n{arr[:500]}")

with open('scratch/modules_extracted.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Saved to scratch/modules_extracted.txt")
