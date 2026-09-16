#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

import re

# Fix patterns like "; else if (state.lang" -> ";\n    } else if (state.lang"
code = re.sub(r';\s*else if \(state\.lang', ';\n    } else if (state.lang', code)

# Fix patterns like "; else if (lang" -> ";\n    } else if (lang"
code = re.sub(r';\s*else if \(lang', ';\n    } else if (lang', code)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fixed syntax in app.js!")
