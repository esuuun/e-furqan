#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clean, flawless rebuild of app.js for Portuguese support.
"""

import sys
import re

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# First remove all stray pt_ai_prompt blocks
stray_pattern = r"\} else if \(state\.lang === 'pt'\) \{\s+if \(topic === 'nahwu'\) \{[\s\S]*?\} else \{\s+return `Explique a Balaghah[\s\S]*?`\;\s+\}\s+\}"

matches = list(re.finditer(stray_pattern, code))
print(f"Found {len(matches)} stray prompt blocks to remove.")

# Remove stray blocks
cleaned_code = re.sub(stray_pattern, "", code)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(cleaned_code)

print("Cleaned app.js")
