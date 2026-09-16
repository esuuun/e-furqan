import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add I18N.es before the end of I18N
es_dict = '''    es: {
      pageTitle: "Diccionario Jamid Mabny | Léxico Interactivo y Referencias de Versículos del Corán",
      brandTitle: "Diccionario <span>Jamid Mabny</span>",
      brandSubtitle: "Diccionario Interactivo de Formas y Números de Palabras",
      themeToggleTitle: "Cambiar Tema Oscuro / Claro",
      labelLangSelect: "Idioma de Traducción y Voz:",
      translationSourceHtml: "Traducción: <strong>Muhammad Isa García</strong>",
      
      // Control Card
      step1Label: "Seleccionar Forma de Palabra",
      step1Placeholder: "Seleccionar Forma de Palabra",
      step1OptionDhamir: "1. Pronombres (Dhamir)",
      step1OptionMawshul: "2. Pronombres Relativos (Mawshul)",
      step1OptionIstifham: "3. Interrogativos (Istifham)",
      step1OptionSyarath: "4. Condicionales (Syarath)",
      step1OptionIsyarah: "5. Demostrativos (Isyarah)",
      step1OptionIsimFiil: "6. Nombres Verbales (Isim Fi'il)",
      step1OptionFiilJamid: "7. Verbos Inflexibles (Fi'il Jamid)",
      step2Label: "Seleccionar Número de Palabra",
      step2Placeholder: "Seleccionar Número de Palabra",
      welcomeTitle: "Por favor seleccione una Forma y Número de Palabra",
      welcomeSubtitle: "Seleccione una forma de palabra del menú superior para ver la pronunciación árabe, significado, frecuencia y referencias completas del Corán.",
      
      // Spotlight Card
      wordFormBadge: "Forma de Palabra",
      wordNoBadgePrefix: "Palabra N°:",
      arabicVoiceBtn: "Audio Árabe",
      arabicVoiceTooltip: "Escuchar la pronunciación en árabe (TTS Árabe)",
      meaningVoiceBtn: "Audio Significado",
      meaningVoiceTooltip: "Escuchar el significado en español (TTS Español)",
      copyArabicTooltip: "Copiar texto árabe",
      copyInfoBtn: "Copiar Información",
      copyInfoTooltip: "Copiar resumen completo de la palabra",
      freqLabel: "Frecuencia en el Corán",
      freqSub: "Frecuencia de Aparición",
      freqMuttashilVal: "Unido / Sufijo",
      freqMuttashilSub: "Forma Sufija / Prefija (Muttashil)",
      totalAyatLabel: "Total de Referencias",
      totalAyatSub: "Disponibles en el Dataset",
      sampleAyatSuffix: "Ejemplos de Versículos",
      transliterationPrefix: "Pronunciación (Transliteración):",
      meaningPrefix: "Significado:",
      
      // References Section
      referencesTitlePrefix: "Referencias de Versículos para",
      ayatCountBadgePattern: (cur, total) => `Ejemplo ${cur} de ${total} Versículos`,
      ayatCountZero: "0 Versículos",
      searchPlaceholder: "Buscar por sura, número o significado...",
      exportCsvBtn: "Exportar CSV",
      exportCsvTooltip: "Exportar las referencias de esta palabra en archivo CSV",
      
      // Ayat Card
      surahPrefix: "Sura",
      surahPositionTag: (cur, surahNo, ayatNo) => `Sura N°${surahNo} • Versículo N°${ayatNo}`,
      playTranslationBtn: "Escuchar Traducción",
      stopTranslationBtn: "Detener Voz",
      playTilawahBtn: "Escuchar Recitación",
      pauseTilawahBtn: "Pausar Recitación",
      askAiBtn: "Consultar IA",
      askAiTooltip: "Consultar a la IA sobre la gramática (Nahwu/I'rab) y Tafsir de este versículo",
      aiModalTitle: "Asistente de IA del Corán",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Estudio de Sura ${suratNama}:${ayat} • Palabra "${kata}" (${noKata})`,
      aiTopicLabel: "Seleccione el Tema de Análisis con IA:",
      aiPromptPreviewLabel: "Prompt para IA (Listo para Usar):",
      aiTopicNahwu: "🔍 Reglas de Nahw, Sarf e I'rab",
      aiTopicTafsir: "📖 Tafsir y Contexto del Versículo",
      aiTopicBalaghah: "✨ Retórica y Balaghah",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Copiar Prompt",
      toastPromptCopied: "¡Prompt de IA copiado al portapapeles!",
      ayahPill: (n) => `Versículo ${n}`,
      flipToArabicBtn: "Ver Texto Árabe",
      flipToTranslationBtn: "Ver Traducción",
      translationBoxHeader: "SIGNIFICADO / TRADUCCIÓN DEL VERSÍCULO (ESPAÑOL - MUHAMMAD ISA GARCÍA)",
      latinBoxHeader: "LECTURA EN TRANSLITERACIÓN",
      copyLatinBtn: "Copiar Transliteración",
      arabicBoxHeader: "النص القرآني • TEXTO ÁRABE COMPLETO",
      latinBackHeader: "TRANSLITERACIÓN:",
      copyBtn: "Copiar",
      prevBtn: "Anterior",
      nextBtn: "Siguiente",
      emptyStateText: "No se encontraron suras o versículos que coincidan con su búsqueda.",
      
      // Toasts & Speech
      toastLangChanged: "Idioma cambiado a Español 🇪🇸",
      toastTilawahPaused: "Recitación pausada.",
      toastTilawahPlaying: (s, a) => `Reproduciendo recitación de Sura ${s}:${a} (Mishary Alafasy)`,
      toastTilawahEnded: "Recitación finalizada.",
      toastAudioFailed: "Error al cargar el audio. Compruebe su conexión a internet.",
      toastTranslationStopped: "Lectura de traducción detenida.",
      toastTtsNotSupported: "La síntesis de voz (TTS) no es compatible con este navegador.",
      toastTranslationNotAvail: "Texto de traducción no disponible.",
      toastSpeakingMeaning: (suratNama, ayat) => `Leyendo traducción de Sura ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Pronunciación en árabe: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Leyendo significado: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Leyendo transliteración de Sura ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `¡Texto árabe "${word}" copiado!`,
      toastLatinCopied: "¡Transliteración copiada!",
      toastSummaryCopied: "¡Resumen copiado exitosamente!",
      toastCsvExported: (nk) => `¡Datos de ${nk} exportados exitosamente en CSV!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_es || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_es || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Pronombre relativo' : 'Pronombre';
        return `${prefix} ${cleanWord}, ${latin}significa ${arti}. ${desc ? 'Significado: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }'''

code = code.replace(
    '  };\n\n  // Helper for current i18n text',
    ',\n' + es_dict + '\n  };\n\n  // Helper for current i18n text'
)

# 2. Update initData in app.js
code = code.replace(
    "bentuk_zh: item['BentukKataZH'] || (b === '1. Dhamir' ? '1. 人称代词 (代名词 / Dhamir)' : (b === '2. Mawshul' ? '2. 关系代词 (接续词 / Mawshul)' : b)),",
    "bentuk_zh: item['BentukKataZH'] || (b === '1. Dhamir' ? '1. 人称代词 (代名词 / Dhamir)' : (b === '2. Mawshul' ? '2. 关系代词 (接续词 / Mawshul)' : b)),\n          bentuk_es: item['BentukKataES'] || (b === '1. Dhamir' ? '1. Pronombres (Dhamir)' : (b === '2. Mawshul' ? '2. Pronombres Relativos (Mawshul)' : b)),"
)

code = code.replace(
    "arti_zh: item['ArtiKataZH'] || grammar.arti_zh || item['ArtiKataID'] || item['Arti kata'],",
    "arti_zh: item['ArtiKataZH'] || grammar.arti_zh || item['ArtiKataID'] || item['Arti kata'],\n          arti_es: item['ArtiKataES'] || grammar.arti_es || item['ArtiKataID'] || item['Arti kata'],"
)

code = code.replace(
    "suratArtiZH: item['SuratArtiZH'] || item['SuratArtiEN'] || '',",
    "suratArtiZH: item['SuratArtiZH'] || item['SuratArtiEN'] || '',\n          suratArtiES: item['SuratArtiES'] || item['SuratArtiEN'] || '',"
)

code = code.replace(
    "teksArtiZH: item['TeksArtiZH'] || item['TeksArtiID'] || item['TeksArti'] || '',",
    "teksArtiZH: item['TeksArtiZH'] || item['TeksArtiID'] || item['TeksArti'] || '',\n          teksArtiES: item['TeksArtiES'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',"
)

# 3. Update getDefaultJenis in app.js
es_default_jenis = """      if (lang === 'es') {
        const jenisMapES = {
          '1. Dhamir': 'Pronombre (Dhamir)',
          '2. Mawshul': 'Pronombre Relativo (Mawshul)',
          '3. Istifham': 'Interrogativo (Istifham)',
          '4. Syarath': 'Condicional (Syarath)',
          '5. Isyarah': 'Demostrativo (Isyarah)',
          "6. Isim Fi'il": "Nombre Verbal (Isim Fi'il)",
          "7. Fi'il Jamid": "Verbo Inflexible (Fi'il Jamid)"
        };
        return jenisMapES[bentuk] || 'Gramática del Corán';
      }"""

code = code.replace(
    "if (lang === 'zh') {",
    es_default_jenis + "\n      if (lang === 'zh') {"
)

# 4. Update populateBentukKata in app.js
code = code.replace(
    "else if (state.lang === 'zh') localizedBentuk = group.bentuk_zh || group.bentuk_id || group.bentuk;",
    "else if (state.lang === 'zh') localizedBentuk = group.bentuk_zh || group.bentuk_id || group.bentuk;\n        else if (state.lang === 'es') localizedBentuk = group.bentuk_es || group.bentuk_id || group.bentuk;"
)

# 5. Update populateNoKata in app.js
code = code.replace(
    "else if (state.lang === 'zh') localizedArti = group.arti_zh || group.arti_id || group.arti;",
    "else if (state.lang === 'zh') localizedArti = group.arti_zh || group.arti_id || group.arti;\n          else if (state.lang === 'es') localizedArti = group.arti_es || group.arti_id || group.arti;"
)

# 6. Update updateSpotlightCard in app.js
code = code.replace(
    "else if (state.lang === 'zh') {\n      bentukText = group.bentuk_zh || group.bentuk_id || group.bentuk;\n    }",
    "else if (state.lang === 'zh') {\n      bentukText = group.bentuk_zh || group.bentuk_id || group.bentuk;\n    } else if (state.lang === 'es') {\n      bentukText = group.bentuk_es || group.bentuk_id || group.bentuk;\n    }"
)

code = code.replace(
    "else if (state.lang === 'zh') {\n      jenisText = grammar.jenis_zh || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'zh');\n    }",
    "else if (state.lang === 'zh') {\n      jenisText = grammar.jenis_zh || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'zh');\n    } else if (state.lang === 'es') {\n      jenisText = grammar.jenis_es || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'es');\n    }"
)

code = code.replace(
    "else if (state.lang === 'zh') {\n      currentMeaning = group.arti_zh || group.arti_id || group.arti;\n    }",
    "else if (state.lang === 'zh') {\n      currentMeaning = group.arti_zh || group.arti_id || group.arti;\n    } else if (state.lang === 'es') {\n      currentMeaning = group.arti_es || group.arti_id || group.arti;\n    }"
)

code = code.replace(
    "else if (state.lang === 'zh') {\n      currentDesc = grammar.desc_zh || grammar.desc_id || grammar.keterangan || '';\n    }",
    "else if (state.lang === 'zh') {\n      currentDesc = grammar.desc_zh || grammar.desc_id || grammar.keterangan || '';\n    } else if (state.lang === 'es') {\n      currentDesc = grammar.desc_es || grammar.desc_id || grammar.keterangan || '';\n    }"
)

# 7. Update renderAyatReferences in app.js
code = code.replace(
    "else if (state.lang === 'zh') {\n        currentSuratArti = occ.suratArtiZH || occ.suratArtiEN || '';\n      }",
    "else if (state.lang === 'zh') {\n        currentSuratArti = occ.suratArtiZH || occ.suratArtiEN || '';\n      } else if (state.lang === 'es') {\n        currentSuratArti = occ.suratArtiES || occ.suratArtiEN || '';\n      }"
)

code = code.replace(
    "else if (state.lang === 'zh') {\n        currentText = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;\n      }",
    "else if (state.lang === 'zh') {\n        currentText = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;\n      } else if (state.lang === 'es') {\n        currentText = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }"
)

# 8. Update TTS voice in speakDhamirMeaning and toggleVerseTranslationAudio
code = code.replace(
    "} else if (state.lang === 'zh') {\n        utterance.lang = 'zh-CN';\n        langVoice = voices.find(v => v.lang.startsWith('zh')) || voices.find(v => v.lang.includes('ZH'));\n      }",
    "} else if (state.lang === 'zh') {\n        utterance.lang = 'zh-CN';\n        langVoice = voices.find(v => v.lang.startsWith('zh')) || voices.find(v => v.lang.includes('ZH'));\n      } else if (state.lang === 'es') {\n        utterance.lang = 'es-ES';\n        langVoice = voices.find(v => v.lang.startsWith('es')) || voices.find(v => v.lang.includes('ES'));\n      }"
)

# 9. Update openAiModal in app.js
code = code.replace(
    "else if (state.lang === 'zh') activeTeksArti = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;",
    "else if (state.lang === 'zh') activeTeksArti = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;\n    else if (state.lang === 'es') activeTeksArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;"
)

# 10. Update buildAiPrompt in app.js
code = code.replace(
    "} else if (state.lang === 'zh') {\n      teksArti = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_zh || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    }",
    "} else if (state.lang === 'zh') {\n      teksArti = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_zh || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    } else if (state.lang === 'es') {\n      teksArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_es || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    }"
)

es_ai_prompt = """    } else if (state.lang === 'es') {
      if (topic === 'nahwu') {
        return `Por favor explique en detalle la gramática árabe (Nahw/Sarf) y el I'rab para la palabra "${kata}" (${noKata}, ${bentuk}) en el Corán, Sura ${suratNama} (${surat}): Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTraducción: "${teksArti}"\\n\\nPor favor detalle:\\n1. La función sintáctica / posición de I'rab de "${kata}" en la estructura de esta oración.\\n2. Categoría morfológica (tipo de Dhamir / Mawshul) y caso (Marfu'/Manshub/Mayrur).\\n3. Notas gramaticales: ${grammarDesc || 'Uso estándar en el Corán'}.`;
      } else if (topic === 'tafsir') {
        return `Por favor proporcione una explicación concisa y contextual de Tafsir para la Sura ${suratNama} (${surat}): Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTraducción: "${teksArti}"\\n\\nCon enfoque en el significado y trascendencia del pronombre / palabra "${kata}", ¿cuál es la sabiduría principal, contexto de revelación (asbab an-nuzul si aplica) y mensaje teológico transmitido en este versículo?`;
      } else {
        return `Explique la Balaghah coránica (Belleza retórica y estilística) en cuanto a la elección de la palabra "${kata}" en la Sura ${suratNama} (${surat}) Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTraducción: "${teksArti}"\\n\\n¿Por qué se emplea esta forma específica de pronombre aquí? ¿Qué matices sutiles, énfasis o elocuencia estética aporta al versículo?`;
      }"""

code = code.replace(
    "    } else if (state.lang === 'en') {",
    es_ai_prompt + "\n    } else if (state.lang === 'en') {"
)

# 11. Update exportToCsv in app.js
code = code.replace(
    "else if (state.lang === 'zh') {\n        activeArti = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;\n      }",
    "else if (state.lang === 'zh') {\n        activeArti = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;\n      } else if (state.lang === 'es') {\n        activeArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }"
)

code = code.replace(
    'let csvContent = "\\uFEFF\\"Bentuk Kata\\",\\"No Kata\\",\\"Kata\\",\\"Latin\\",\\"Arti Kata (ID)\\",\\"Arti Kata (EN)\\",\\"Arti Kata (MS)\\",\\"Arti Kata (FR)\\",\\"Arti Kata (DE)\\",\\"Arti Kata (UR)\\",\\"Arti Kata (HI)\\",\\"Arti Kata (BN)\\",\\"Arti Kata (RU)\\",\\"Arti Kata (ZH)\\",',
    'let csvContent = "\\uFEFF\\"Bentuk Kata\\",\\"No Kata\\",\\"Kata\\",\\"Latin\\",\\"Arti Kata (ID)\\",\\"Arti Kata (EN)\\",\\"Arti Kata (MS)\\",\\"Arti Kata (FR)\\",\\"Arti Kata (DE)\\",\\"Arti Kata (UR)\\",\\"Arti Kata (HI)\\",\\"Arti Kata (BN)\\",\\"Arti Kata (RU)\\",\\"Arti Kata (ZH)\\",\\"Arti Kata (ES)\\",'
)

code = code.replace(
    'const cleanArtiZH = (occ.teksArtiZH || occ.teksArtiID || \'\').replace(/"/g, \'""\');',
    'const cleanArtiZH = (occ.teksArtiZH || occ.teksArtiID || \'\').replace(/"/g, \'""\');\n        const cleanArtiES = (occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || \'\').replace(/"/g, \'""\');'
)

code = code.replace(
    '"${cleanArtiBN}","${cleanArtiRU}","${cleanArtiZH}"\\n`;',
    '"${cleanArtiBN}","${cleanArtiRU}","${cleanArtiZH}","${cleanArtiES}"\\n`;'
)

# 12. Update btnCopyAll in app.js
code = code.replace(
    "else if (state.lang === 'zh') {\n          activeArti = group.arti_zh || group.arti_id || group.arti;\n        }",
    "else if (state.lang === 'zh') {\n          activeArti = group.arti_zh || group.arti_id || group.arti;\n        } else if (state.lang === 'es') {\n          activeArti = group.arti_es || group.arti_id || group.arti;\n        }"
)

code = code.replace(
    "else if (state.lang === 'zh') titlePrefix = '古兰经关系代词 (Mawshul)';",
    "else if (state.lang === 'zh') titlePrefix = '古兰经关系代词 (Mawshul)';\n          else if (state.lang === 'es') titlePrefix = 'Pronombre Relativo del Corán (Mawshul)';"
)

code = code.replace(
    "else if (state.lang === 'zh') titlePrefix = '古兰经人称代词 (Dhamir)';",
    "else if (state.lang === 'zh') titlePrefix = '古兰经人称代词 (Dhamir)';\n          else if (state.lang === 'es') titlePrefix = 'Pronombre del Corán (Dhamir)';"
)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated app.js with Spanish support successfully!")
