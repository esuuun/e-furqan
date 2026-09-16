#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add Portuguese (pt) language support to app.js
"""

import sys
import os
import re

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Normalize line endings
crlf = '\r\n' in code
code = code.replace('\r\n', '\n')

# 1. State lang validation
code = code.replace(
    "['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr']",
    "['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt']"
)

# 2. Add I18N.pt dictionary
pt_dict = '''    pt: {
      pageTitle: "Dicionário Jamid Mabny | Vocabulário Alcorânico e Referências Interativas",
      brandTitle: "Dicionário <span>Jamid Mabny</span>",
      brandSubtitle: "Dicionário Interativo de Formas e Números de Palavras",
      themeToggleTitle: "Alternar Tema Claro / Escuro",
      labelLangSelect: "Idioma da Tradução e Voz:",
      translationSourceHtml: "Tradução: <strong>Prof. Samir El-Hayek (Centro Islâmico)</strong>",
      
      // Control Card
      step1Label: "1. Selecione a Forma da Palavra",
      step1Placeholder: "Selecione a Forma da Palavra",
      step1OptionDhamir: "1. Pronomes (Dhamir - Pronomes Pessoais)",
      step1OptionMawshul: "2. Pronomes Relativos (Mawshul)",
      step1OptionIstifham: "3. Interrogativos (Istifham)",
      step1OptionSyarath: "4. Condicionais (Syarath)",
      step1OptionIsyarah: "5. Demonstrativos (Isyarah)",
      step1OptionIsimFiil: "6. Nomes Verbais (Isim Fi'il)",
      step1OptionFiilJamid: "7. Verbos Inflexíveis (Fi'il Jamid)",
      step2Label: "2. Selecione o Número da Palavra",
      step2Placeholder: "Selecione o Número da Palavra",
      welcomeTitle: "Por favor, Selecione a Forma e o Número da Palavra",
      welcomeSubtitle: "Selecione a Forma da Palavra no menu acima para visualizar a palavra em árabe, significado, frequência no Alcorão e referências de versículos.",
      
      // Spotlight Card
      wordFormBadge: "Forma da Palavra",
      wordNoBadgePrefix: "Nº da Palavra:",
      arabicVoiceBtn: "Voz Árabe",
      arabicVoiceTooltip: "Ouvir Pronúncia em Árabe (TTS)",
      meaningVoiceBtn: "Voz do Significado",
      meaningVoiceTooltip: "Ouvir Significado em Português (TTS)",
      copyArabicTooltip: "Copiar Palavra em Árabe",
      copyInfoBtn: "Copiar Informações",
      copyInfoTooltip: "Copiar Resumo Completo",
      freqLabel: "Frequência no Alcorão Sagrado",
      freqSub: "Total de Ocorrências",
      freqMuttashilVal: "Muttashil (Ligado)",
      freqMuttashilSub: "Forma Ligada (Sufixo / Imbuhan)",
      totalAyatLabel: "Total de Versículos de Referência",
      totalAyatSub: "Disponíveis no Conjunto de Dados",
      sampleAyatSuffix: "Versículos de Exemplo",
      transliterationPrefix: "Transliteração:",
      meaningPrefix: "Significado:",
      
      // References Section
      referencesTitlePrefix: "Referências de Versículos para:",
      ayatCountBadgePattern: (cur, total) => `Exemplo ${cur} de ${total} Versículos`,
      ayatCountZero: "0 Versículos",
      searchPlaceholder: "Buscar por nome da surata ou número do versículo...",
      exportCsvBtn: "Exportar CSV",
      exportCsvTooltip: "Baixar todas as referências de versículos desta palavra em formato CSV",
      
      // Ayat Card
      surahPrefix: "Surata",
      surahPositionTag: (cur, surahNo, ayatNo) => `Surata nº ${surahNo} • Versículo nº ${ayatNo}`,
      playTranslationBtn: "Ouvir Tradução",
      stopTranslationBtn: "Parar Áudio",
      playTilawahBtn: "Ouvir Recitação",
      pauseTilawahBtn: "Pausar Recitação",
      askAiBtn: "Perguntar à IA",
      askAiTooltip: "Consultar IA sobre análise gramatical (Nahwu/I'rab) e Tafsir deste versículo",
      aiModalTitle: "Assistente de IA Alcorânica",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `Estudo: Surata ${suratNama}:${ayat} • Palavra "${kata}" (${noKata})`,
      aiTopicLabel: "Selecione o Tópico de Análise da IA:",
      aiPromptPreviewLabel: "Prompt Pronto para IA:",
      aiTopicNahwu: "🔍 Regras de Gramática (Nahwu/Sarf) & I'rab",
      aiTopicTafsir: "📖 Tafsir e Significado do Versículo",
      aiTopicBalaghah: "✨ Eloquência e Balaghah Alcorânica",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "Copiar Prompt",
      toastPromptCopied: "Prompt copiado para a área de transferência!",
      ayahPill: (n) => `Versículo ${n}`,
      flipToArabicBtn: "Ver Texto Árabe",
      flipToTranslationBtn: "Ver Tradução",
      translationBoxHeader: "TRADUÇÃO DO VERSÍCULO (PORTUGUÊS - PROF. SAMIR EL-HAYEK)",
      latinBoxHeader: "TRANSLITERAÇÃO EM CARACTERES LATINOS",
      copyLatinBtn: "Copiar Transliteração",
      arabicBoxHeader: "النص القرآني • TEXTO ÁRABE INTEGRAL DO VERSÍCULO",
      latinBackHeader: "TRANSLITERAÇÃO:",
      copyBtn: "Copiar",
      prevBtn: "Anterior",
      nextBtn: "Próximo",
      emptyStateText: "Nenhuma surata ou versículo encontrado para sua pesquisa.",
      
      // Toasts & Speech
      toastLangChanged: "Idioma alterado para Português 🇵🇹 🇧🇷",
      toastTilawahPaused: "Recitação pausada.",
      toastTilawahPlaying: (s, a) => `Reproduzindo recitação da Surata ${s}:${a} (Mishary Rashid Alafasy)`,
      toastTilawahEnded: "Recitação concluída.",
      toastAudioFailed: "Falha ao carregar arquivo de áudio. Verifique sua conexão com a internet.",
      toastTranslationStopped: "Reprodução da tradução interrompida.",
      toastTtsNotSupported: "Seu navegador não suporta síntese de voz (TTS).",
      toastTranslationNotAvail: "Texto de tradução não encontrado.",
      toastSpeakingMeaning: (suratNama, ayat) => `Reproduzindo tradução em português da Surata ${suratNama}:${ayat}`,
      toastSpeakingArabic: (word) => `Pronúncia em árabe da palavra: ${word}`,
      toastSpeakingWordMeaning: (arti) => `Reproduzindo significado: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `Reproduzindo transliteração da Surata ${suratNama}:${ayat}`,
      toastArabicCopied: (word) => `Palavra em árabe "${word}" copiada!`,
      toastLatinCopied: "Transliteração copiada!",
      toastSummaryCopied: "Resumo copiado com sucesso!",
      toastCsvExported: (nk) => `Dados da palavra ${nk} exportados para CSV com sucesso!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_pt || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_pt || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'Pronome relativo' : 'Pronome';
        return `${prefix} ${cleanWord}, ${latin}significado ${arti}. ${desc ? 'Explicação: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }'''

code = code.replace(
    '  };\n\n  // Helper for current i18n text',
    ',\n' + pt_dict + '\n  };\n\n  // Helper for current i18n text'
)

# 3. Update initData in app.js
code = code.replace(
    "bentuk_tr: item['BentukKataTR'] || (b === '1. Dhamir' ? '1. Zamirler (Dhamir - Şahıs Zamirleri)' : (b === '2. Mawshul' ? '2. İsmi Mevsul (Mawshul - İlgi Zamirleri)' : b)),",
    "bentuk_tr: item['BentukKataTR'] || (b === '1. Dhamir' ? '1. Zamirler (Dhamir - Şahıs Zamirleri)' : (b === '2. Mawshul' ? '2. İsmi Mevsul (Mawshul - İlgi Zamirleri)' : b)),\n          bentuk_pt: item['BentukKataPT'] || (b === '1. Dhamir' ? '1. Pronomes (Dhamir - Pronomes Pessoais)' : (b === '2. Mawshul' ? '2. Pronomes Relativos (Mawshul)' : b)),"
)

code = code.replace(
    "arti_tr: item['ArtiKataTR'] || grammar.arti_tr || item['ArtiKataID'] || item['Arti kata'],",
    "arti_tr: item['ArtiKataTR'] || grammar.arti_tr || item['ArtiKataID'] || item['Arti kata'],\n          arti_pt: item['ArtiKataPT'] || grammar.arti_pt || item['ArtiKataID'] || item['Arti kata'],"
)

code = code.replace(
    "suratArtiTR: item['SuratArtiTR'] || item['SuratArtiEN'] || item['SuratArti'] || '',",
    "suratArtiTR: item['SuratArtiTR'] || item['SuratArtiEN'] || item['SuratArti'] || '',\n        suratArtiPT: item['SuratArtiPT'] || item['SuratArtiEN'] || item['SuratArti'] || '',"
)

code = code.replace(
    "teksArtiTR: item['TeksArtiTR'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',",
    "teksArtiTR: item['TeksArtiTR'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',\n        teksArtiPT: item['TeksArtiPT'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',"
)

# 4. Update getDefaultJenis defaultMap
code = code.replace(
    "tr: 'Munfasıl (Ayrık Zamir)'",
    "tr: 'Munfasıl (Ayrık Zamir)', pt: 'Munfashil (Independente)'"
)
code = code.replace(
    "tr: 'İsmi Mevsul (İlgi Zamiri)'",
    "tr: 'İsmi Mevsul (İlgi Zamiri)', pt: 'Pronome Relativo'"
)
code = code.replace(
    "tr: 'Soru Edatı (İstifham)'",
    "tr: 'Soru Edatı (İstifham)', pt: 'Interrogativo'"
)
code = code.replace(
    "tr: 'Şart Edatı (Şart İsimleri)'",
    "tr: 'Şart Edatı (Şart İsimleri)', pt: 'Condicional'"
)
code = code.replace(
    "tr: 'İşaret İsmi (İsm-i İşâre)'",
    "tr: 'İşaret İsmi (İsm-i İşâre)', pt: 'Demonstrativo'"
)
code = code.replace(
    "tr: 'İsim Fiil (İsm-i Fiil)'",
    "tr: 'İsim Fiil (İsm-i Fiil)', pt: 'Nome Verbal'"
)
code = code.replace(
    "tr: 'Câmid Fiil (Çekimsiz Fiil)'",
    "tr: 'Câmid Fiil (Çekimsiz Fiil)', pt: 'Verbo Inflexível'"
)

# 5. Update populateNoKata in app.js
code = code.replace(
    "} else if (state.lang === 'tr') {\n        localizedArti = group.arti_tr || group.arti_id || group.arti;\n      }",
    "} else if (state.lang === 'tr') {\n        localizedArti = group.arti_tr || group.arti_id || group.arti;\n      } else if (state.lang === 'pt') {\n        localizedArti = group.arti_pt || group.arti_id || group.arti;\n      }"
)

# 6. Update updateSpotlightCard in app.js
code = code.replace(
    "} else if (state.lang === 'tr') {\n      elements.badgeBentukKata.textContent = group.bentuk_tr || group.bentuk_id;\n    } else {",
    "} else if (state.lang === 'tr') {\n      elements.badgeBentukKata.textContent = group.bentuk_tr || group.bentuk_id;\n    } else if (state.lang === 'pt') {\n      elements.badgeBentukKata.textContent = group.bentuk_pt || group.bentuk_id;\n    } else {"
)

code = code.replace(
    "} else if (state.lang === 'tr') {\n      jenisText = grammar.jenis_tr || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'tr');\n    } else {",
    "} else if (state.lang === 'tr') {\n      jenisText = grammar.jenis_tr || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'tr');\n    } else if (state.lang === 'pt') {\n      jenisText = grammar.jenis_pt || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'pt');\n    } else {"
)

code = code.replace(
    "} else if (state.lang === 'tr') {\n      currentMeaning = group.arti_tr || group.arti_id || group.arti;\n    }",
    "} else if (state.lang === 'tr') {\n      currentMeaning = group.arti_tr || group.arti_id || group.arti;\n    } else if (state.lang === 'pt') {\n      currentMeaning = group.arti_pt || group.arti_id || group.arti;\n    }"
)

code = code.replace(
    "} else if (state.lang === 'tr') {\n      currentDesc = grammar.desc_tr || grammar.desc_id || grammar.keterangan || '';\n    }",
    "} else if (state.lang === 'tr') {\n      currentDesc = grammar.desc_tr || grammar.desc_id || grammar.keterangan || '';\n    } else if (state.lang === 'pt') {\n      currentDesc = grammar.desc_pt || grammar.desc_id || grammar.keterangan || '';\n    }"
)

# 7. Update renderAyatReferences (search filter and card rendering) in app.js
code = code.replace(
    "} else if (state.lang === 'tr') {\n          sArti = occ.suratArtiTR;\n          tArti = occ.teksArtiTR;\n        }",
    "} else if (state.lang === 'tr') {\n          sArti = occ.suratArtiTR;\n          tArti = occ.teksArtiTR;\n        } else if (state.lang === 'pt') {\n          sArti = occ.suratArtiPT;\n          tArti = occ.teksArtiPT;\n        }"
)

code = code.replace(
    "} else if (state.lang === 'tr') {\n      activeSuratArti = occ.suratArtiTR || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }",
    "} else if (state.lang === 'tr') {\n      activeSuratArti = occ.suratArtiTR || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    } else if (state.lang === 'pt') {\n      activeSuratArti = occ.suratArtiPT || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }"
)

# 8. Update toggleVerseTranslationAudio in app.js
code = code.replace(
    "} else if (state.lang === 'tr') {\n      currentText = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }",
    "} else if (state.lang === 'tr') {\n      currentText = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    } else if (state.lang === 'pt') {\n      currentText = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }"
)

code = code.replace(
    "} else if (state.lang === 'tr') {\n      speechLangCode = 'tr-TR';\n      matchVoice = voices.find(v => v.lang.startsWith('tr') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Ahmet') || v.name.includes('Emel') || v.name.includes('Turkish') || v.name.includes('Filiz') || v.name.includes('Tolga'))) || voices.find(v => v.lang.startsWith('tr'));\n    }",
    "} else if (state.lang === 'tr') {\n      speechLangCode = 'tr-TR';\n      matchVoice = voices.find(v => v.lang.startsWith('tr') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Ahmet') || v.name.includes('Emel') || v.name.includes('Turkish') || v.name.includes('Filiz') || v.name.includes('Tolga'))) || voices.find(v => v.lang.startsWith('tr'));\n    } else if (state.lang === 'pt') {\n      speechLangCode = 'pt-PT';\n      matchVoice = voices.find(v => v.lang.startsWith('pt') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Heloisa') || v.name.includes('Raquel') || v.name.includes('Portuguese') || v.name.includes('Francisca') || v.name.includes('Duarte') || v.name.includes('Luciana') || v.name.includes('Yara') || v.name.includes('Daniel'))) || voices.find(v => v.lang.startsWith('pt'));\n    }"
)

# 9. Update speakDhamirMeaning in app.js
code = code.replace(
    "} else if (state.lang === 'tr') {\n      activeMeaning = group.arti_tr || group.arti_id || group.arti;\n    }",
    "} else if (state.lang === 'tr') {\n      activeMeaning = group.arti_tr || group.arti_id || group.arti;\n    } else if (state.lang === 'pt') {\n      activeMeaning = group.arti_pt || group.arti_id || group.arti;\n    }"
)

code = code.replace(
    "} else if (state.lang === 'tr') {\n      speechLangCode = 'tr-TR';\n      matchVoice = voices.find(v => v.lang.startsWith('tr') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Ahmet') || v.name.includes('Emel') || v.name.includes('Turkish') || v.name.includes('Filiz') || v.name.includes('Tolga'))) || voices.find(v => v.lang.startsWith('tr'));\n    } else if (state.lang === 'es') {",
    "} else if (state.lang === 'tr') {\n      speechLangCode = 'tr-TR';\n      matchVoice = voices.find(v => v.lang.startsWith('tr') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Ahmet') || v.name.includes('Emel') || v.name.includes('Turkish') || v.name.includes('Filiz') || v.name.includes('Tolga'))) || voices.find(v => v.lang.startsWith('tr'));\n    } else if (state.lang === 'pt') {\n      speechLangCode = 'pt-PT';\n      matchVoice = voices.find(v => v.lang.startsWith('pt') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Heloisa') || v.name.includes('Raquel') || v.name.includes('Portuguese') || v.name.includes('Francisca') || v.name.includes('Duarte') || v.name.includes('Luciana') || v.name.includes('Yara') || v.name.includes('Daniel'))) || voices.find(v => v.lang.startsWith('pt'));\n    } else if (state.lang === 'es') {"
)

# 10. Update openAiModal in app.js
code = code.replace(
    "} else if (state.lang === 'tr') {\n        activeArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }",
    "} else if (state.lang === 'tr') {\n        activeArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      } else if (state.lang === 'pt') {\n        activeArti = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }"
)

# 11. Update buildAiPrompt in app.js
code = code.replace(
    "} else if (state.lang === 'tr') {\n      teksArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_tr || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    }",
    "} else if (state.lang === 'tr') {\n      teksArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_tr || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    } else if (state.lang === 'pt') {\n      teksArti = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_pt || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    }"
)

pt_ai_prompt = """    } else if (state.lang === 'pt') {
      if (topic === 'nahwu') {
        return `Por favor, explique em detalhes a gramática árabe (Nahwu/Sarf) e a análise de I'rab para a palavra "${kata}" (${noKata}, ${bentuk}) na Surata ${suratNama} (${surat}): Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTradução: "${teksArti}"\\n\\nPor favor, aborde os seguintes pontos:\\n1. Função sintática e posição de I'rab de "${kata}" na estrutura desta oração (Marfu' / Manshub / Majrur).\\n2. Categoria morfológica (tipo de Dhamir / Mawshul / etc.) e propriedades do pronome (Munfashil / Muttashil).\\n3. Notas gramaticais: ${grammarDesc || "Uso alcorânico padrão"}.`;
      } else if (topic === 'tafsir') {
        return `Por favor, forneça uma explicação concisa e contextual de Tafsir para a Surata ${suratNama} (${surat}): Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTradução: "${teksArti}"\\n\\nCom foco especial no significado da palavra/pronome "${kata}": qual é a sabedoria principal, contexto de revelação (asbab an-nuzul, se aplicável) e a mensagem teológica transmitida neste versículo?`;
      } else {
        return `Explique a Balaghah alcorânica (Eloquência retórica e estilística) em relação à escolha da palavra "${kata}" na Surata ${suratNama} (${surat}) Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTradução: "${teksArti}"\\n\\nPor que essa forma específica de pronome foi utilizada aqui? Que nuances sutis, ênfase ou profundidade estética ela adiciona ao versículo?`;
      }"""

code = code.replace(
    "    } else if (state.lang === 'es') {",
    pt_ai_prompt + "\n    } else if (state.lang === 'es') {"
)

# 12. Update exportToCsv in app.js
code = code.replace(
    "const cleanArtiTR = (occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');",
    "const cleanArtiTR = (occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');\n        const cleanArtiPT = (occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');"
)

code = code.replace(
    ',\\"Significado (ES)\\",\\"Significado (TR)\\",',
    ',\\"Significado (ES)\\",\\"Significado (TR)\\",\\"Significado (PT)\\",'
)

code = code.replace(
    ',\\"Traducción (ES)\\",\\"Meal (TR)\\",',
    ',\\"Traducción (ES)\\",\\"Meal (TR)\\",\\"Tradução (PT)\\",'
)

code = code.replace(
    '"${group.arti_zh || \'\'}","${group.arti_es || \'\'}","${group.frek || \'Muttashil\'}"',
    '"${group.arti_zh || \'\'}","${group.arti_es || \'\'}","${group.arti_tr || \'\'}","${group.arti_pt || \'\'}","${group.frek || \'Muttashil\'}"'
)

code = code.replace(
    '"${cleanArtiZH}","${cleanArtiES}","${cleanArtiTR}",',
    '"${cleanArtiZH}","${cleanArtiES}","${cleanArtiTR}","${cleanArtiPT}",'
)

# 13. Update btnCopyAll in app.js
code = code.replace(
    "} else if (state.lang === 'tr') {\n          activeArti = group.arti_tr || group.arti_id || group.arti;\n        }",
    "} else if (state.lang === 'tr') {\n          activeArti = group.arti_tr || group.arti_id || group.arti;\n        } else if (state.lang === 'pt') {\n          activeArti = group.arti_pt || group.arti_id || group.arti;\n        }"
)

code = code.replace(
    "else if (state.lang === 'tr') titlePrefix = 'Kur\\'an-ı Kerim İsmi Mevsul (Mawshul)';",
    "else if (state.lang === 'tr') titlePrefix = 'Kur\\'an-ı Kerim İsmi Mevsul (Mawshul)';\n          else if (state.lang === 'pt') titlePrefix = 'Pronome Relativo do Alcorão (Mawshul)';"
)

code = code.replace(
    "else if (state.lang === 'tr') titlePrefix = 'Kur\\'an-ı Kerim Zamirleri (Dhamir)';",
    "else if (state.lang === 'tr') titlePrefix = 'Kur\\'an-ı Kerim Zamirleri (Dhamir)';\n          else if (state.lang === 'pt') titlePrefix = 'Pronomes do Alcorão (Dhamir)';"
)

# 14. Update applyLanguage in app.js
code = code.replace(
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr'].includes(lang) ? lang : 'id';",
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt'].includes(lang) ? lang : 'id';"
)

if crlf:
    code = code.replace('\n', '\r\n')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("app.js successfully updated with Portuguese support!")
