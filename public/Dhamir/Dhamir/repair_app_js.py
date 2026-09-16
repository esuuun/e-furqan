#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to cleanly repair and finalize app.js for Turkish and all languages.
"""

import sys
import re

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all stray Turkish AI prompt blocks except the one inside buildAiPrompt
prompt_pattern = re.compile(
    r"\s*\} else if \(state\.lang === 'tr'\) \{\s*if \(topic === 'nahwu'\) \{[\s\S]*?Neden özellikle bu zamir / kelime formu tercih edilmiştir[\s\S]*?\}\s*\}",
    re.MULTILINE
)

# Find where buildAiPrompt is
build_ai_pos = content.find('function buildAiPrompt(')

before_ai = content[:build_ai_pos]
after_ai = content[build_ai_pos:]

# Remove stray prompt patterns from before buildAiPrompt
before_ai_cleaned = prompt_pattern.sub('', before_ai)

# In after_ai, only keep the prompt inside buildAiPrompt
# Find openAiModal
open_modal_pos = after_ai.find('function openAiModal(')
inside_ai = after_ai[:open_modal_pos]
rest_after_ai = after_ai[open_modal_pos:]

# Clean up any stray prompt after buildAiPrompt as well
rest_after_ai_cleaned = prompt_pattern.sub('', rest_after_ai)

content = before_ai_cleaned + inside_ai + rest_after_ai_cleaned

# Now let's ensure each section has the correct Turkish handler:

# 1. populateNoKata:
content = re.sub(
    r"(\s*else if \(state\.lang === 'es'\) localizedArti = group\.arti_es \|\| group\.arti_id \|\| group\.arti;)",
    r"\1\n          else if (state.lang === 'tr') localizedArti = group.arti_tr || group.arti_id || group.arti;",
    content
)

# 2. updateSpotlightCard:
# bentukText
content = re.sub(
    r"(\s*\} else if \(state\.lang === 'es'\) \{\s*bentukText = group\.bentuk_es \|\| group\.bentuk_id \|\| group\.bentuk;\s*\})",
    r"\1 else if (state.lang === 'tr') {\n      bentukText = group.bentuk_tr || group.bentuk_id || group.bentuk;\n    }",
    content
)

# jenisText
content = re.sub(
    r"(\s*\} else if \(state\.lang === 'es'\) \{\s*jenisText = grammar\.jenis_es \|\| grammar\.jenis_id \|\| grammar\.jenis \|\| getDefaultJenis\(group\.bentuk, 'es'\);\s*\})",
    r"\1 else if (state.lang === 'tr') {\n      jenisText = grammar.jenis_tr || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'tr');\n    }",
    content
)

# currentMeaning
content = re.sub(
    r"(\s*\} else if \(state\.lang === 'es'\) \{\s*currentMeaning = group\.arti_es \|\| group\.arti_id \|\| group\.arti;\s*\})",
    r"\1 else if (state.lang === 'tr') {\n      currentMeaning = group.arti_tr || group.arti_id || group.arti;\n    }",
    content
)

# currentDesc
content = re.sub(
    r"(\s*\} else if \(state\.lang === 'es'\) \{\s*currentDesc = grammar\.desc_es \|\| grammar\.desc_id \|\| grammar\.keterangan \|\| '';\s*\})",
    r"\1 else if (state.lang === 'tr') {\n      currentDesc = grammar.desc_tr || grammar.desc_id || grammar.keterangan || '';\n    }",
    content
)

# 3. renderAyatReferences:
# currentSuratArti
content = re.sub(
    r"(\s*\} else if \(state\.lang === 'es'\) \{\s*currentSuratArti = occ\.suratArtiES \|\| occ\.suratArtiEN \|\| '';\s*\})",
    r"\1 else if (state.lang === 'tr') {\n        currentSuratArti = occ.suratArtiTR || occ.suratArtiEN || '';\n      }",
    content
)

# currentText
content = re.sub(
    r"(\s*\} else if \(state\.lang === 'es'\) \{\s*currentText = occ\.teksArtiES \|\| occ\.teksArtiEN \|\| occ\.teksArtiID \|\| occ\.teksArti;\s*\})",
    r"\1 else if (state.lang === 'tr') {\n        currentText = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }",
    content
)

# 4. renderAyatCard:
content = re.sub(
    r"(\s*\} else if \(state\.lang === 'es'\) \{\s*activeSuratArti = occ\.suratArtiES \|\| occ\.suratArtiEN \|\| '';\s*activeTeksArti = occ\.teksArtiES \|\| occ\.teksArtiEN \|\| occ\.teksArtiID \|\| occ\.teksArti;\s*\})",
    r"\1 else if (state.lang === 'tr') {\n      activeSuratArti = occ.suratArtiTR || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }",
    content
)

# 5. speakMeaning and toggleVerseTranslationAudio:
# utterance.lang
content = re.sub(
    r"(\s*\} else if \(state\.lang === 'es'\) \{\s*utterance\.lang = 'es-ES';\s*utterance\.rate = 0\.95;\s*\})",
    r"\1 else if (state.lang === 'tr') {\n      utterance.lang = 'tr-TR';\n      utterance.rate = 0.95;\n    }",
    content
)

# voice selection
content = re.sub(
    r"(\s*\} else if \(state\.lang === 'es'\) \{\s*const esVoice = voices\.find\([^\)]+\) \|\| voices\.find\([^\)]+\);\s*if \(esVoice\) utterance\.voice = esVoice;\s*\})",
    r"\1 else if (state.lang === 'tr') {\n      const trVoice = voices.find(v => v.lang.startsWith('tr') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Ahmet') || v.name.includes('Emel') || v.name.includes('Turkish') || v.name.includes('Filiz') || v.name.includes('Tolga'))) || voices.find(v => v.lang.startsWith('tr'));\n      if (trVoice) utterance.voice = trVoice;\n    }",
    content
)

# 6. openAiModal:
content = re.sub(
    r"(\s*else if \(state\.lang === 'es'\) activeTeksArti = occ\.teksArtiES \|\| occ\.teksArtiEN \|\| occ\.teksArtiID \|\| occ\.teksArti;)",
    r"\1\n    else if (state.lang === 'tr') activeTeksArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;",
    content
)

# 7. exportToCsv:
content = re.sub(
    r"(\s*\} else if \(state\.lang === 'es'\) \{\s*activeArti = occ\.teksArtiES \|\| occ\.teksArtiEN \|\| occ\.teksArtiID \|\| occ\.teksArti;\s*\})",
    r"\1 else if (state.lang === 'tr') {\n        activeArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }",
    content
)

# 8. btnCopyAll:
content = re.sub(
    r"(\s*\} else if \(state\.lang === 'es'\) \{\s*activeArti = group\.arti_es \|\| group\.arti_id \|\| group\.arti;\s*\})",
    r"\1 else if (state.lang === 'tr') {\n          activeArti = group.arti_tr || group.arti_id || group.arti;\n        }",
    content
)

# Deduplicate any duplicate tr branches that might have been created
content = re.sub(
    r"(\s*else if \(state\.lang === 'tr'\) localizedArti = group\.arti_tr \|\| group\.arti_id \|\| group\.arti;)+",
    r"\n          else if (state.lang === 'tr') localizedArti = group.arti_tr || group.arti_id || group.arti;",
    content
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Repaired app.js successfully!")
