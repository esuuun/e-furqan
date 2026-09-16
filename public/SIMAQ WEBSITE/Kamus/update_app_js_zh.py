# -*- coding: utf-8 -*-
"""
Script to add complete Chinese (zh / 简体中文) language support to app.js
"""
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app_js_path = os.path.join(BASE_DIR, 'app.js')

with open(app_js_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. State lang comment
code = code.replace(
    "lang: localStorage.getItem('dhamir_lang') || 'id', // 'id' | 'en' | 'ms' | 'fr' | 'de' | 'ur' | 'hi' | 'bn' | 'ru'",
    "lang: localStorage.getItem('dhamir_lang') || 'id', // 'id' | 'en' | 'ms' | 'fr' | 'de' | 'ur' | 'hi' | 'bn' | 'ru' | 'zh'"
)

# 2. Add 'zh' to I18N
zh_i18n = """    zh: {
      pageTitle: "贾米德·马布尼词典 | 古兰经互动词汇与经文参考",
      brandTitle: "贾米德·马布尼 <span>词典</span>",
      brandSubtitle: "词形与词号古兰经交互式词典",
      themeToggleTitle: "切换深色 / 浅色主题",
      labelLangSelect: "翻译与语音语言:",
      translationSourceHtml: "译文: <strong>马坚 (Muhammad Makin)</strong>",
      
      // Control Card
      step1Label: "1. 请选择词形类别",
      step1Placeholder: "请选择词形类别",
      step1OptionDhamir: "1. 人称代词 (代名词 / Dhamir)",
      step1OptionMawshul: "2. 关系代词 (接续词 / Mawshul)",
      step1OptionIstifham: "3. 疑问词 (疑问代词 / Istifham)",
      step1OptionSyarath: "4. 条件虚词 (条件代词 / Syarath)",
      step1OptionIsyarah: "5. 指示代词 (指示名词 / Isyarah)",
      step1OptionIsimFiil: "6. 动名词 (含动词义名词 / Isim Fi'il)",
      step1OptionFiilJamid: "7. 固态动词 (不规则静态动词 / Fi'il Jamid)",
      step2Label: "2. 请选择词号",
      step2Placeholder: "请选择词号",
      welcomeTitle: "请选择词形与词号",
      welcomeSubtitle: "请在上方菜单中选择词形（代词、关系代词等），以查看阿拉伯语原文、含义、古兰经中出现频次及经文参考列表。",
      
      // Spotlight Card
      wordFormBadge: "词形类别",
      wordNoBadgePrefix: "词号:",
      arabicVoiceBtn: "阿拉伯语发音",
      arabicVoiceTooltip: "收听阿拉伯语音频 (TTS)",
      meaningVoiceBtn: "词义朗读",
      meaningVoiceTooltip: "收听中文翻译与释义 (TTS)",
      copyArabicTooltip: "复制阿拉伯语单词",
      copyInfoBtn: "复制信息",
      copyInfoTooltip: "复制完整摘要",
      freqLabel: "古兰经中出现频次",
      freqSub: "经文出现次数",
      freqMuttashilVal: "接尾代词 (Muttashil)",
      freqMuttashilSub: "附着词缀形式",
      totalAyatLabel: "参考经文总数",
      totalAyatSub: "数据库中收录",
      sampleAyatSuffix: "条示例经文",
      transliterationPrefix: "罗马拼音:",
      meaningPrefix: "释义:",
      
      // References Section
      referencesTitlePrefix: "古兰经经文参考 —",
      ayatCountBadgePattern: (cur, total) => `示例 ${cur} / 共 ${total} 节经文`,
      ayatCountZero: "0 节经文",
      searchPlaceholder: "搜索苏拉名称 / 节数...",
      exportCsvBtn: "导出 CSV",
      exportCsvTooltip: "下载该词的所有参考经文 CSV 文件",
      
      // Ayat Card
      surahPrefix: "苏拉",
      surahPositionTag: (cur, surahNo, ayatNo) => `第 ${surahNo} 章 • 第 ${ayatNo} 节`,
      playTranslationBtn: "朗读译文",
      stopTranslationBtn: "停止播放",
      playTilawahBtn: "诵读音频",
      pauseTilawahBtn: "暂停诵读",
      askAiBtn: "向 AI 提问",
      askAiTooltip: "向 AI 询问本节经文的语法与经注 (Tafsir)",
      aiModalTitle: "古兰经 AI 学习助手",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `研读: 苏拉 ${suratNama}:${ayat} • 词汇 "${kata}" (${noKata})`,
      aiTopicLabel: "选择 AI 分析主题:",
      aiPromptPreviewLabel: "生成的 AI 提示词 (可直接复制):",
      aiTopicNahwu: "🔍 语法 (Nahwu) 与语法分析 (I'rab)",
      aiTopicTafsir: "📖 经注 (Tafsir) 与经文内涵",
      aiTopicBalaghah: "✨ 修辞学 (Balaghah) 鉴赏",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "复制提示词",
      toastPromptCopied: "AI 提示词已成功复制到剪贴板！",
      ayahPill: (n) => `第 ${n} 节`,
      flipToArabicBtn: "查看阿拉伯语原文",
      flipToTranslationBtn: "查看中文译文",
      translationBoxHeader: "经文译文 (中文 - 马坚 译本)",
      latinBoxHeader: "罗马拼音转写 (TRANSLITERATION)",
      copyLatinBtn: "复制拼音",
      arabicBoxHeader: "النص القرآني • 古兰经完整阿拉伯语经文",
      latinBackHeader: "罗马拼音:",
      copyBtn: "复制",
      prevBtn: "上一节",
      nextBtn: "下一节",
      emptyStateText: "未找到与您的搜索条件匹配的苏拉或经文。",
      
      // Toasts & Speech
      toastLangChanged: "语言已成功切换为中文 🇨🇳",
      toastTilawahPaused: "诵读已暂停。",
      toastTilawahPlaying: (s, a) => `正在播放苏拉 ${s}:${a} 阿拉伯语诵读 (米沙里·拉希德)`,
      toastTilawahEnded: "诵读播放完毕。",
      toastAudioFailed: "音频加载失败，请检查网络连接。",
      toastTranslationStopped: "译文朗读已停止。",
      toastTtsNotSupported: "当前浏览器不支持语音合成 (TTS)。",
      toastTranslationNotAvail: "未找到译文内容。",
      toastSpeakingMeaning: (suratNama, ayat) => `正在朗读苏拉 ${suratNama}:${ayat} 中文译文`,
      toastSpeakingArabic: (word) => `阿拉伯语词汇发音: ${word}`,
      toastSpeakingWordMeaning: (arti) => `正在朗读词义: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `正在朗读苏拉 ${suratNama}:${ayat} 罗马拼音`,
      toastArabicCopied: (word) => `阿拉伯语词汇 "${word}" 已复制！`,
      toastLatinCopied: "拼音转写已复制！",
      toastSummaryCopied: "详细摘要已成功复制！",
      toastCsvExported: (nk) => `词号 ${nk} 的数据已成功导出为 CSV！`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_zh || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_zh || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? '关系代词' : '人称代词';
        return `${prefix} ${cleanWord}, ${latin}含义 ${arti}。${desc ? '语法解析: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }"""

# Insert 'zh' after 'ru' in I18N
ru_anchor = """      ttsVerseSpeech: (suratNama, ayat, text) => text
    }
  };"""

code = code.replace(ru_anchor, """      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
""" + zh_i18n + """
  };""")

# 3. groupedData construction
old_group_data = """          bentuk_ru: item['BentukKataRU'] || (b === '1. Dhamir' ? '1. Местоимения (Дамир / Dhamir)' : (b === '2. Mawshul' ? '2. Относительные местоимения (Маусуль / Mawshul)' : b)),
          noKata: nk,"""
new_group_data = """          bentuk_ru: item['BentukKataRU'] || (b === '1. Dhamir' ? '1. Местоимения (Дамир / Dhamir)' : (b === '2. Mawshul' ? '2. Относительные местоимения (Маусуль / Mawshul)' : b)),
          bentuk_zh: item['BentukKataZH'] || (b === '1. Dhamir' ? '1. 人称代词 (代名词 / Dhamir)' : (b === '2. Mawshul' ? '2. 关系代词 (接续词 / Mawshul)' : b)),
          noKata: nk,"""
code = code.replace(old_group_data, new_group_data)

old_arti_ru = """          arti_ru: item['ArtiKataRU'] || grammar.arti_ru || item['ArtiKataID'] || item['Arti kata'],
          frek: item['Frek kata'],"""
new_arti_ru = """          arti_ru: item['ArtiKataRU'] || grammar.arti_ru || item['ArtiKataID'] || item['Arti kata'],
          arti_zh: item['ArtiKataZH'] || grammar.arti_zh || item['ArtiKataID'] || item['Arti kata'],
          frek: item['Frek kata'],"""
code = code.replace(old_arti_ru, new_arti_ru)

old_surat_arti = """        suratArtiRU: item['SuratArtiRU'] || item['SuratArti'] || '',
        teksArab: item['TeksArab'] || '',"""
new_surat_arti = """        suratArtiRU: item['SuratArtiRU'] || item['SuratArti'] || '',
        suratArtiZH: item['SuratArtiZH'] || item['SuratArti'] || '',
        teksArab: item['TeksArab'] || '',"""
code = code.replace(old_surat_arti, new_surat_arti)

old_teks_arti = """        teksArtiRU: item['TeksArtiRU'] || item['TeksArtiID'] || item['TeksArti'] || '',
        audioUrl: item['AudioUrl']"""
new_teks_arti = """        teksArtiRU: item['TeksArtiRU'] || item['TeksArtiID'] || item['TeksArti'] || '',
        teksArtiZH: item['TeksArtiZH'] || item['TeksArtiID'] || item['TeksArti'] || '',
        audioUrl: item['AudioUrl']"""
code = code.replace(old_teks_arti, new_teks_arti)

# 4. populateNoKataDropdown
old_no_kata = """      } else if (state.lang === 'ru') {
        localizedArti = group.arti_ru || group.arti_id || group.arti;
      }"""
new_no_kata = """      } else if (state.lang === 'ru') {
        localizedArti = group.arti_ru || group.arti_id || group.arti;
      } else if (state.lang === 'zh') {
        localizedArti = group.arti_zh || group.arti_id || group.arti;
      }"""
code = code.replace(old_no_kata, new_no_kata)

# 5. updateSpotlightCard
old_badge_bentuk = """    } else if (state.lang === 'ru') {
      elements.badgeBentukKata.textContent = group.bentuk_ru || group.bentuk_id;
    } else {"""
new_badge_bentuk = """    } else if (state.lang === 'ru') {
      elements.badgeBentukKata.textContent = group.bentuk_ru || group.bentuk_id;
    } else if (state.lang === 'zh') {
      elements.badgeBentukKata.textContent = group.bentuk_zh || group.bentuk_id;
    } else {"""
code = code.replace(old_badge_bentuk, new_badge_bentuk)

old_badge_jenis = """    } else if (state.lang === 'ru') {
      jenisText = grammar.jenis_ru || (group.bentuk.includes('Mawshul') ? 'Относительное местоимение' : 'Местоимение');
    } else {"""
new_badge_jenis = """    } else if (state.lang === 'ru') {
      jenisText = grammar.jenis_ru || (group.bentuk.includes('Mawshul') ? 'Относительное местоимение' : 'Местоимение');
    } else if (state.lang === 'zh') {
      jenisText = grammar.jenis_zh || (group.bentuk.includes('Mawshul') ? '关系代词' : '人称代词');
    } else {"""
code = code.replace(old_badge_jenis, new_badge_jenis)

old_meaning = """    } else if (state.lang === 'ru') {
      currentMeaning = group.arti_ru || group.arti;
    }"""
new_meaning = """    } else if (state.lang === 'ru') {
      currentMeaning = group.arti_ru || group.arti;
    } else if (state.lang === 'zh') {
      currentMeaning = group.arti_zh || group.arti;
    }"""
code = code.replace(old_meaning, new_meaning)

old_desc = """    } else if (state.lang === 'ru') {
      currentDesc = grammar.desc_ru || grammar.desc_id || grammar.keterangan || '';
    }"""
new_desc = """    } else if (state.lang === 'ru') {
      currentDesc = grammar.desc_ru || grammar.desc_id || grammar.keterangan || '';
    } else if (state.lang === 'zh') {
      currentDesc = grammar.desc_zh || grammar.desc_id || grammar.keterangan || '';
    }"""
code = code.replace(old_desc, new_desc)

# 6. Audio in toggleVerseTranslationAudio
old_play_trans_text = """    } else if (state.lang === 'ru') {
      currentText = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
    }"""
new_play_trans_text = """    } else if (state.lang === 'ru') {
      currentText = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'zh') {
      currentText = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;
    }"""
code = code.replace(old_play_trans_text, new_play_trans_text)

old_play_trans_lang = """    } else if (state.lang === 'ru') {
      utterance.lang = 'ru-RU';
      utterance.rate = 0.95;
    } else {"""
new_play_trans_lang = """    } else if (state.lang === 'ru') {
      utterance.lang = 'ru-RU';
      utterance.rate = 0.95;
    } else if (state.lang === 'zh') {
      utterance.lang = 'zh-CN';
      utterance.rate = 0.95;
    } else {"""
code = code.replace(old_play_trans_lang, new_play_trans_lang)

old_play_trans_voice = """    } else if (state.lang === 'ru') {
      const ruVoice = voices.find(v => v.lang.startsWith('ru') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Pavel') || v.name.includes('Irina') || v.name.includes('Yuri') || v.name.includes('Ekaterina') || v.name.includes('Dmitry'))) || voices.find(v => v.lang.startsWith('ru'));
      if (ruVoice) utterance.voice = ruVoice;
    } else {"""
new_play_trans_voice = """    } else if (state.lang === 'ru') {
      const ruVoice = voices.find(v => v.lang.startsWith('ru') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Pavel') || v.name.includes('Irina') || v.name.includes('Yuri') || v.name.includes('Ekaterina') || v.name.includes('Dmitry'))) || voices.find(v => v.lang.startsWith('ru'));
      if (ruVoice) utterance.voice = ruVoice;
    } else if (state.lang === 'zh') {
      const zhVoice = voices.find(v => v.lang.startsWith('zh') && (v.name.includes('Xiaoxiao') || v.name.includes('Yunxi') || v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Chinese') || v.name.includes('Huihui') || v.name.includes('Yaoyao') || v.name.includes('Kangkang'))) || voices.find(v => v.lang.startsWith('zh'));
      if (zhVoice) utterance.voice = zhVoice;
    } else {"""
code = code.replace(old_play_trans_voice, new_play_trans_voice)

# 7. speakDhamirMeaning
old_speak_dhamir_lang = """    } else if (state.lang === 'ru') {
      activeMeaning = group.arti_ru || group.arti_id || group.arti;
    }"""
new_speak_dhamir_lang = """    } else if (state.lang === 'ru') {
      activeMeaning = group.arti_ru || group.arti_id || group.arti;
    } else if (state.lang === 'zh') {
      activeMeaning = group.arti_zh || group.arti_id || group.arti;
    }"""
code = code.replace(old_speak_dhamir_lang, new_speak_dhamir_lang)

old_speak_dhamir_utter = """    } else if (state.lang === 'ru') {
      utterance.lang = 'ru-RU';
      utterance.rate = 0.95;
    } else {"""
new_speak_dhamir_utter = """    } else if (state.lang === 'ru') {
      utterance.lang = 'ru-RU';
      utterance.rate = 0.95;
    } else if (state.lang === 'zh') {
      utterance.lang = 'zh-CN';
      utterance.rate = 0.95;
    } else {"""
code = code.replace(old_speak_dhamir_utter, new_speak_dhamir_utter)

old_speak_dhamir_voice = """    } else if (state.lang === 'ru') {
      const ruVoice = voices.find(v => v.lang.startsWith('ru') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Pavel') || v.name.includes('Irina') || v.name.includes('Yuri') || v.name.includes('Ekaterina') || v.name.includes('Dmitry'))) || voices.find(v => v.lang.startsWith('ru'));
      if (ruVoice) utterance.voice = ruVoice;
    } else {"""
new_speak_dhamir_voice = """    } else if (state.lang === 'ru') {
      const ruVoice = voices.find(v => v.lang.startsWith('ru') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Pavel') || v.name.includes('Irina') || v.name.includes('Yuri') || v.name.includes('Ekaterina') || v.name.includes('Dmitry'))) || voices.find(v => v.lang.startsWith('ru'));
      if (ruVoice) utterance.voice = ruVoice;
    } else if (state.lang === 'zh') {
      const zhVoice = voices.find(v => v.lang.startsWith('zh') && (v.name.includes('Xiaoxiao') || v.name.includes('Yunxi') || v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Chinese') || v.name.includes('Huihui') || v.name.includes('Yaoyao') || v.name.includes('Kangkang'))) || voices.find(v => v.lang.startsWith('zh'));
      if (zhVoice) utterance.voice = zhVoice;
    } else {"""
code = code.replace(old_speak_dhamir_voice, new_speak_dhamir_voice)

# 8. renderAyatReferences
old_search_filter = """        } else if (state.lang === 'ru') {
          sArti = occ.suratArtiRU;
          tArti = occ.teksArtiRU;
        }"""
new_search_filter = """        } else if (state.lang === 'ru') {
          sArti = occ.suratArtiRU;
          tArti = occ.teksArtiRU;
        } else if (state.lang === 'zh') {
          sArti = occ.suratArtiZH;
          tArti = occ.teksArtiZH;
        }"""
code = code.replace(old_search_filter, new_search_filter)

old_verse_card_arti = """    } else if (state.lang === 'ru') {
      activeSuratArti = occ.suratArtiRU;
      activeTeksArti = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
    }"""
new_verse_card_arti = """    } else if (state.lang === 'ru') {
      activeSuratArti = occ.suratArtiRU;
      activeTeksArti = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'zh') {
      activeSuratArti = occ.suratArtiZH;
      activeTeksArti = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;
    }"""
code = code.replace(old_verse_card_arti, new_verse_card_arti)

# 9. applyLanguage
code = code.replace(
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru'].includes(lang) ? lang : 'id';",
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh'].includes(lang) ? lang : 'id';"
)

# 10. buildAiPrompt
old_ai_vars = """    } else if (state.lang === 'ru') {
      teksArti = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_ru || group.grammar.desc_id || group.grammar.keterangan)) || '';
    }"""
new_ai_vars = """    } else if (state.lang === 'ru') {
      teksArti = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_ru || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'zh') {
      teksArti = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_zh || group.grammar.desc_id || group.grammar.keterangan)) || '';
    }"""
code = code.replace(old_ai_vars, new_ai_vars)

old_ai_prompt_branches = """    } else if (state.lang === 'ru') {
      if (topic === 'nahwu') {
        return `Пожалуйста, подробно объясните арабскую грамматику (нахву/сарф) и и'раб (синтаксический разбор) слова "${kata}" (${noKata}, ${bentuk}) в Суре ${suratNama} (${surat}), аят ${ayat}:\\n\\nАрабский текст: "${teksArab}"\\nПеревод: "${teksArti}"\\n\\nПожалуйста, включите следующие пункты:\\n1. Грамматическая роль "${kata}" в структуре этого предложения и его и'раб (падежное состояние: марфу'/мансуб/маджрур).\\n2. Морфологическая классификация (Дамир мунфасыль/муттасыль или Исм маусуль).\\n3. Грамматическое примечание: ${grammarDesc || 'Классическое кораническое употребление'}.`;
      } else if (topic === 'tafsir') {
        return `Пожалуйста, представьте краткий и контекстуальный тафсир (толкование) Суры ${suratNama} (${surat}), аят ${ayat}:\\n\\nАрабский текст: "${teksArab}"\\nПеревод: "${teksArti}"\\n\\nУделив особое внимание значению слова/местоимения "${kata}", объясните, какой главный смысл, повод ниспослания (сабаб ан-нузуль) и духовное наставление заключены в этом аяте?`;
      } else {
        return `Объясните кораническую риторику и стилистику (баляга) в выборе слова "${kata}" в Суре ${suratNama} (${surat}), аят ${ayat}:\\n\\nАрабский текст: "${teksArab}"\\nПеревод: "${teksArti}"\\n\\nПочему здесь использована именно эта конкретная грамматическая форма? Какую смысловую глубину и красоту она придает аяту?`;
      }
    } else {"""

new_ai_prompt_branches = """    } else if (state.lang === 'ru') {
      if (topic === 'nahwu') {
        return `Пожалуйста, подробно объясните арабскую грамматику (нахву/сарф) и и'раб (синтаксический разбор) слова "${kata}" (${noKata}, ${bentuk}) в Суре ${suratNama} (${surat}), аят ${ayat}:\\n\\nАрабский текст: "${teksArab}"\\nПеревод: "${teksArti}"\\n\\nПожалуйста, включите следующие пункты:\\n1. Грамматическая роль "${kata}" в структуре этого предложения и его и'раб (падежное состояние: марфу'/мансуб/маджрур).\\n2. Морфологическая классификация (Дамир мунфасыль/муттасыль или Исм маусуль).\\n3. Грамматическое примечание: ${grammarDesc || 'Классическое кораническое употребление'}.`;
      } else if (topic === 'tafsir') {
        return `Пожалуйста, представьте краткий и контекстуальный тафсир (толкование) Суры ${suratNama} (${surat}), аят ${ayat}:\\n\\nАрабский текст: "${teksArab}"\\nПеревод: "${teksArti}"\\n\\nУделив особое внимание значению слова/местоимения "${kata}", объясните, какой главный смысл, повод ниспослания (сабаб ан-нузуль) и духовное наставление заключены в этом аяте?`;
      } else {
        return `Объясните кораническую риторику и стилистику (баляга) в выборе слова "${kata}" в Суре ${suratNama} (${surat}), аят ${ayat}:\\n\\nАрабский текст: "${teksArab}"\\nПеревод: "${teksArti}"\\n\\nПочему здесь использована именно эта конкретная грамматическая форма? Какую смысловую глубину и красоту она придает аяту?`;
      }
    } else if (state.lang === 'zh') {
      if (topic === 'nahwu') {
        return `请详细解析古兰经苏拉 ${suratNama} (${surat}) 第 ${ayat} 节中词汇 "${kata}" (${noKata}, ${bentuk}) 的阿拉伯语语法 (Nahwu / Sarf) 及语法定位 (I'rab)：\\n\\n阿拉伯语原文: "${teksArab}"\\n中文译文: "${teksArti}"\\n\\n请包含以下要点：\\n1. "${kata}" 在该句子结构中的语法成分与格位状态 (主格/宾格/属格/断格)。\\n2. 词形形态分类 (独立人称代词/接尾人称代词/关系代词)。\\n3. 语法特别说明: ${grammarDesc || '标准古兰经语言用法'}。`;
      } else if (topic === 'tafsir') {
        return `请对苏拉 ${suratNama} (${surat}) 第 ${ayat} 节提供简明且结合语境的经注 (Tafsir) 与内涵阐释：\\n\\n阿拉伯语原文: "${teksArab}"\\n中文译文: "${teksArti}"\\n\\n请重点结合词汇/代词 "${kata}" 的用法，阐明本节经文所蕴含的核心教诲、启示背景 (Sabab al-Nuzul) 以及精神指导意义？`;
      } else {
        return `请赏析苏拉 ${suratNama} (${surat}) 第 ${ayat} 节中选用词汇 "${kata}" 的古兰经修辞美学 (Balaghah) 与文体风格：\\n\\n阿拉伯语原文: "${teksArab}"\\n中文译文: "${teksArti}"\\n\\n为什么此处使用了该特定词形？它为经文的意境深度与文学表现力增添了怎样的色彩？`;
      }
    } else {"""
code = code.replace(old_ai_prompt_branches, new_ai_prompt_branches)

# 11. openAiModal
old_modal_arti = """      } else if (state.lang === 'ru') {
        activeArti = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
      }"""
new_modal_arti = """      } else if (state.lang === 'ru') {
        activeArti = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
      } else if (state.lang === 'zh') {
        activeArti = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;
      }"""
code = code.replace(old_modal_arti, new_modal_arti)

# 12. CSV Export
old_csv_header = "Orthobhed (BN),Znachenie (RU),Frekuensi"
new_csv_header = "Orthobhed (BN),Znachenie (RU),Biaoda (ZH),Frekuensi"
code = code.replace(old_csv_header, new_csv_header)

old_csv_header2 = "Onubad (BN),Perevod (RU),Link Audio"
new_csv_header2 = "Onubad (BN),Perevod (RU),Fanyi (ZH),Link Audio"
code = code.replace(old_csv_header2, new_csv_header2)

old_csv_body1 = """      const cleanArtiRU = (occ.teksArtiRU || '').replace(/"/g, '""');
      const audioLink = occ.audioUrl || '';"""
new_csv_body1 = """      const cleanArtiRU = (occ.teksArtiRU || '').replace(/"/g, '""');
      const cleanArtiZH = (occ.teksArtiZH || '').replace(/"/g, '""');
      const audioLink = occ.audioUrl || '';"""
code = code.replace(old_csv_body1, new_csv_body1)

code = code.replace(
    '="${group.arti_ru || \'\'}","${group.frek || \'Muttashil\'}"',
    '="${group.arti_ru || \'\'}","${group.arti_zh || \'\'}","${group.frek || \'Muttashil\'}"'
)
code = code.replace(
    '"${cleanArtiRU}","${audioLink}"',
    '"${cleanArtiRU}","${cleanArtiZH}","${audioLink}"'
)

# 13. btnCopyAll
old_copy_arti = """        } else if (state.lang === 'ru') {
          activeArti = group.arti_ru || group.arti;
        }"""
new_copy_arti = """        } else if (state.lang === 'ru') {
          activeArti = group.arti_ru || group.arti;
        } else if (state.lang === 'zh') {
          activeArti = group.arti_zh || group.arti;
        }"""
code = code.replace(old_copy_arti, new_copy_arti)

old_copy_mawshul = """          else if (state.lang === 'ru') titlePrefix = 'Коранические относительные местоимения (Mawshul)';"""
new_copy_mawshul = """          else if (state.lang === 'ru') titlePrefix = 'Коранические относительные местоимения (Mawshul)';
          else if (state.lang === 'zh') titlePrefix = '古兰经关系代词 (Mawshul)';"""
code = code.replace(old_copy_mawshul, new_copy_mawshul)

old_copy_dhamir = """          else if (state.lang === 'ru') titlePrefix = 'Коранические местоимения (Dhamir)';"""
new_copy_dhamir = """          else if (state.lang === 'ru') titlePrefix = 'Коранические местоимения (Dhamir)';
          else if (state.lang === 'zh') titlePrefix = '古兰经人称代词 (Dhamir)';"""
code = code.replace(old_copy_dhamir, new_copy_dhamir)

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(code)

print(f"[OK] Successfully updated {app_js_path} for Chinese (zh) language!")
