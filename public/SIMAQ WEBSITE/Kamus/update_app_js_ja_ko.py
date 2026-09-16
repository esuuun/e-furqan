#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add Japanese (ja) and Korean (ko) language support to app.js
"""

import sys
import os

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
    "['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa'].includes(localStorage.getItem('dhamir_lang'))",
    "['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa', 'ja', 'ko'].includes(localStorage.getItem('dhamir_lang'))"
)

# 2. Add I18N.ja and I18N.ko dictionaries
ja_dict = '''    ja: {
      pageTitle: "ジャーミド・マブニー辞書 | クルアーン語形・節対話型リファレンス",
      brandTitle: "ジャーミド・マブニー <span>辞書</span>",
      brandSubtitle: "クルアーン語形と語番号の対話型辞典",
      themeToggleTitle: "ダーク / ライトテーマ切り替え",
      labelLangSelect: "翻訳言語と音声:",
      translationSourceHtml: "翻訳: <strong>日本ムスリム協会 / 三田了一 訳 (Ryoichi Mita)</strong>",
      
      // Control Card
      step1Label: "1. 語形を選択",
      step1Placeholder: "語形を選択してください",
      step1OptionDhamir: "1. 代名詞 (Dhamir - Pronouns)",
      step1OptionMawshul: "2. 関係代名詞 (Mawshul - Relative Pronouns)",
      step1OptionIstifham: "3. 疑問詞 (Istifham - Interrogatives)",
      step1OptionSyarath: "4. 条件詞 (Syarath - Conditionals)",
      step1OptionIsyarah: "5. 指示代名詞 (Isyarah - Demonstratives)",
      step1OptionIsimFiil: "6. 動詞性名詞 (Isim Fi'il - Verbal Nouns)",
      step1OptionFiilJamid: "7. 固着動詞 (Fi'il Jamid - Inflexible Verbs)",
      step2Label: "2. 語番号を選択",
      step2Placeholder: "語番号を選択してください",
      welcomeTitle: "語形と語番号を選択してください",
      welcomeSubtitle: "上のメニューから語形を選択すると、アラビア語表記、日本語訳、クルアーン内出現頻度、および参照節が表示されます。",
      
      // Spotlight Card
      wordFormBadge: "語形",
      wordNoBadgePrefix: "語番号:",
      arabicVoiceBtn: "アラビア語音声",
      arabicVoiceTooltip: "アラビア語の発音を聞く (TTS)",
      meaningVoiceBtn: "意味の音声",
      meaningVoiceTooltip: "日本語の意味・訳を聞く (TTS)",
      copyArabicTooltip: "アラビア語単語をコピー",
      copyInfoBtn: "情報をコピー",
      copyInfoTooltip: "単語の全詳細をコピー",
      freqLabel: "クルアーン内出現頻度",
      freqSub: "総出現回数",
      freqMuttashilVal: "接尾形（ムッタスィル）",
      freqMuttashilSub: "接尾辞・結合構造",
      totalAyatLabel: "参照節の総数",
      totalAyatSub: "データセット内収録数",
      sampleAyatSuffix: "例文・参照節",
      transliterationPrefix: "ローマ字転写:",
      meaningPrefix: "意味:",
      
      // References Section
      referencesTitlePrefix: "クルアーン参照節:",
      ayatCountBadgePattern: (cur, total) => `節 ${cur} / ${total}`,
      ayatCountZero: "0 節",
      searchPlaceholder: "章名または節番号で検索...",
      exportCsvBtn: "CSVエクスポート",
      exportCsvTooltip: "この単語の全参照節をCSV形式でダウンロード",
      
      // Ayat Card
      surahPrefix: "章 (スーラ)",
      surahPositionTag: (cur, surahNo, ayatNo) => `第${surahNo}章 • 第${ayatNo}節`,
      playTranslationBtn: "訳文を聞く",
      stopTranslationBtn: "音声を停止",
      playTilawahBtn: "朗誦を聞く",
      pauseTilawahBtn: "朗誦を一時停止",
      askAiBtn: "AIに質問",
      askAiTooltip: "この節の文法や注釈についてAIに質問する",
      aiModalTitle: "クルアーンAIアシスタント",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `分析: 第${suratNama}章:${ayat} • 単語「${kata}」(${noKata})`,
      aiTopicLabel: "AI分析トピックを選択:",
      aiPromptPreviewLabel: "作成されたAIプロンプト:",
      aiTopicNahwu: "🔍 ナフウ (文法・構文解析) と格変化 (イアラーブ)",
      aiTopicTafsir: "📖 タフスィール (節の注釈と教訓)",
      aiTopicBalaghah: "✨ バラーガ (クルアーンの修辞美と文体)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "プロンプトをコピー",
      toastPromptCopied: "AIプロンプトをクリップボードにコピーしました！",
      ayahPill: (n) => `第${n}節`,
      flipToArabicBtn: "アラビア語本文を見る",
      flipToTranslationBtn: "日本語訳を見る",
      translationBoxHeader: "節の日本語訳 (三田了一 訳 / 日本ムスリム協会)",
      latinBoxHeader: "ローマ字転写 (TRANSLITERATION)",
      copyLatinBtn: "転写をコピー",
      arabicBoxHeader: "النص القرآني • アラビア語全文",
      latinBackHeader: "ローマ字転写:",
      copyBtn: "コピー",
      prevBtn: "前へ",
      nextBtn: "次へ",
      emptyStateText: "検索条件に一致する章や節が見つかりませんでした。",
      
      // Toasts & Speech
      toastLangChanged: "言語を日本語に切り替えました 🇯🇵",
      toastTilawahPaused: "朗誦を一時停止しました。",
      toastTilawahPlaying: (s, a) => `第${s}章:${a}節の朗誦を再生中 (ミシャリー・ラシード・アル＝アファスィー)`,
      toastTilawahEnded: "朗誦が終了しました。",
      toastAudioFailed: "音声の再生に失敗しました。接続をご確認ください。",
      toastTranslationStopped: "訳文の読み上げを停止しました。",
      toastTtsNotSupported: "お使いのブラウザは音声合成 (TTS) に対応していません。",
      toastTranslationNotAvail: "翻訳テキストが利用できません。",
      toastSpeakingMeaning: (suratNama, ayat) => `第${suratNama}章:${ayat}節の日本語訳を読み上げ中`,
      toastSpeakingArabic: (word) => `アラビア語発音: ${word}`,
      toastSpeakingWordMeaning: (arti) => `意味を読み上げ中: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `第${suratNama}章:${ayat}節の転写を読み上げ中`,
      toastArabicCopied: (word) => `アラビア語「${word}」をコピーしました！`,
      toastLatinCopied: "ローマ字転写をコピーしました！",
      toastSummaryCopied: "単語の全詳細をコピーしました！",
      toastCsvExported: (nk) => `単語 ${nk} の参照節をCSVに出力しました！`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ja || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ja || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? '関係代名詞' : '代名詞';
        return `${prefix} ${cleanWord}、${latin}意味は「${arti}」。${desc ? '解説：' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }'''

ko_dict = '''    ko: {
      pageTitle: "자미드 맙니 사전 | 꾸란 단어 및 구절 대화형 참조",
      brandTitle: "자미드 맙니 <span>사전</span>",
      brandSubtitle: "꾸란 단어 형태 및 단어 번호 대화형 사전",
      themeToggleTitle: "다크 / 라이트 테마 전환",
      labelLangSelect: "번역 언어 및 음성:",
      translationSourceHtml: "번역: <strong>최영길 박사 번역 (파드 국왕 성원 출판)</strong>",
      
      // Control Card
      step1Label: "1. 단어 형태 선택",
      step1Placeholder: "단어 형태를 선택하세요",
      step1OptionDhamir: "1. 대명사 (Dhamir - Pronouns)",
      step1OptionMawshul: "2. 관계대명사 (Mawshul - Relative Pronouns)",
      step1OptionIstifham: "3. 의문사 (Istifham - Interrogatives)",
      step1OptionSyarath: "4. 조건사 (Syarath - Conditionals)",
      step1OptionIsyarah: "5. 지시대명사 (Isyarah - Demonstratives)",
      step1OptionIsimFiil: "6. 동사성 명사 (Isim Fi'il - Verbal Nouns)",
      step1OptionFiilJamid: "7. 불변동사 (Fi'il Jamid - Inflexible Verbs)",
      step2Label: "2. 단어 번호 선택",
      step2Placeholder: "단어 번호를 선택하세요",
      welcomeTitle: "단어 형태와 번호를 선택해 주세요",
      welcomeSubtitle: "위 메뉴에서 단어 형태를 선택하면 아랍어 표기, 한국어 번역, 꾸란 내 빈도 및 참조 구절이 표시됩니다.",
      
      // Spotlight Card
      wordFormBadge: "단어 형태",
      wordNoBadgePrefix: "단어 번호:",
      arabicVoiceBtn: "아랍어 음성",
      arabicVoiceTooltip: "아랍어 발음 듣기 (TTS)",
      meaningVoiceBtn: "의미 음성",
      meaningVoiceTooltip: "한국어 의미 및 번역 듣기 (TTS)",
      copyArabicTooltip: "아랍어 단어 복사",
      copyInfoBtn: "정보 복사",
      copyInfoTooltip: "단어 전체 상세 정보 복사",
      freqLabel: "꾸란 내 출현 빈도",
      freqSub: "총 언급 횟수",
      freqMuttashilVal: "접미형 (뭇타실)",
      freqMuttashilSub: "접미 결합 구조",
      totalAyatLabel: "총 참조 구절 수",
      totalAyatSub: "데이터셋 수록 구절",
      sampleAyatSuffix: "예시 구절",
      transliterationPrefix: "로마자 전사:",
      meaningPrefix: "의미:",
      
      // References Section
      referencesTitlePrefix: "꾸란 참조 구절:",
      ayatCountBadgePattern: (cur, total) => `구절 ${cur} / ${total}`,
      ayatCountZero: "0 구절",
      searchPlaceholder: "장 이름 또는 구절 번호 검색...",
      exportCsvBtn: "CSV 내보내기",
      exportCsvTooltip: "이 단어의 모든 참조 구절을 CSV 파일로 다운로드",
      
      // Ayat Card
      surahPrefix: "장 (수라)",
      surahPositionTag: (cur, surahNo, ayatNo) => `제${surahNo}장 • 제${ayatNo}절`,
      playTranslationBtn: "번역 듣기",
      stopTranslationBtn: "음성 정지",
      playTilawahBtn: "낭송 듣기",
      pauseTilawahBtn: "낭송 일시정지",
      askAiBtn: "AI에게 질문",
      askAiTooltip: "이 구절의 문법 및 해석에 대해 AI에게 질문하기",
      aiModalTitle: "꾸란 AI 어시스턴트",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `분석: 제${suratNama}장:${ayat} • 단어 "${kata}" (${noKata})`,
      aiTopicLabel: "AI 분석 주제 선택:",
      aiPromptPreviewLabel: "생성된 AI 프롬프트:",
      aiTopicNahwu: "🔍 나흐우 (아랍어 문법) 및 격변화 (이라브)",
      aiTopicTafsir: "📖 타프시르 (구절의 주석 및 교훈)",
      aiTopicBalaghah: "✨ 발라가 (꾸란의 수사학적 아름다움)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "프롬프트 복사",
      toastPromptCopied: "AI 프롬프트가 클립보드에 복사되었습니다!",
      ayahPill: (n) => `제${n}절`,
      flipToArabicBtn: "아랍어 본문 보기",
      flipToTranslationBtn: "한국어 번역 보기",
      translationBoxHeader: "구절 한국어 번역 (최영길 박사 번역)",
      latinBoxHeader: "로마자 발음 전사 (TRANSLITERATION)",
      copyLatinBtn: "전사 복사",
      arabicBoxHeader: "النص القرآني • 아랍어 전문",
      latinBackHeader: "로마자 전사:",
      copyBtn: "복사",
      prevBtn: "이전",
      nextBtn: "다음",
      emptyStateText: "검색 조건과 일치하는 장 또는 구절을 찾을 수 없습니다.",
      
      // Toasts & Speech
      toastLangChanged: "언어가 한국어로 변경되었습니다 🇰🇷",
      toastTilawahPaused: "낭송이 일시정지되었습니다.",
      toastTilawahPlaying: (s, a) => `제${s}장:${a}절 낭송 재생 중 (미샤리 라시드 알아파시)`,
      toastTilawahEnded: "낭송이 종료되었습니다.",
      toastAudioFailed: "오디오 재생 오류. 인터넷 연결을 확인해 주세요.",
      toastTranslationStopped: "번역 음성 재생이 정지되었습니다.",
      toastTtsNotSupported: "사용 중인 브라우저가 텍스트 음성 변환 (TTS)을 지원하지 않습니다.",
      toastTranslationNotAvail: "번역 텍스트를 사용할 수 없습니다.",
      toastSpeakingMeaning: (suratNama, ayat) => `제${suratNama}장:${ayat}절 한국어 번역 낭독 중`,
      toastSpeakingArabic: (word) => `아랍어 발음: ${word}`,
      toastSpeakingWordMeaning: (arti) => `의미 낭독 중: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `제${suratNama}장:${ayat}절 로마자 전사 낭독 중`,
      toastArabicCopied: (word) => `아랍어 "${word}" 복사 완료!`,
      toastLatinCopied: "로마자 전사가 복사되었습니다!",
      toastSummaryCopied: "단어 상세 정보가 클립보드에 복사되었습니다!",
      toastCsvExported: (nk) => `단어 ${nk}의 참조 구절이 CSV로 저장되었습니다!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_ko || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_ko || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? '관계대명사' : '대명사';
        return `${prefix} ${cleanWord}, ${latin}의미는 ${arti}. ${desc ? '설명: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }'''

code = code.replace(
    '  };\n\n  // Helper for current i18n text',
    ',\n' + ja_dict + ',\n' + ko_dict + '\n  };\n\n  // Helper for current i18n text'
)

# 3. Update initData in app.js
code = code.replace(
    "bentuk_fa: item['BentukKataFA'] || (b === '1. Dhamir' ? '۱. ضمایر (Dhamir - Pronouns)' : (b === '2. Mawshul' ? '۲. اسم‌های موصول (Mawshul - Relative Pronouns)' : b)),",
    "bentuk_fa: item['BentukKataFA'] || (b === '1. Dhamir' ? '۱. ضمایر (Dhamir - Pronouns)' : (b === '2. Mawshul' ? '۲. اسم‌های موصول (Mawshul - Relative Pronouns)' : b)),\n          bentuk_ja: item['BentukKataJA'] || (b === '1. Dhamir' ? '1. 代名詞 (Dhamir - Pronouns)' : (b === '2. Mawshul' ? '2. 関係代名詞 (Mawshul - Relative Pronouns)' : b)),\n          bentuk_ko: item['BentukKataKO'] || (b === '1. Dhamir' ? '1. 대명사 (Dhamir - Pronouns)' : (b === '2. Mawshul' ? '2. 관계대명사 (Mawshul - Relative Pronouns)' : b)),"
)

code = code.replace(
    "arti_fa: item['ArtiKataFA'] || grammar.arti_fa || item['ArtiKataID'] || item['Arti kata'],",
    "arti_fa: item['ArtiKataFA'] || grammar.arti_fa || item['ArtiKataID'] || item['Arti kata'],\n          arti_ja: item['ArtiKataJA'] || grammar.arti_ja || item['ArtiKataID'] || item['Arti kata'],\n          arti_ko: item['ArtiKataKO'] || grammar.arti_ko || item['ArtiKataID'] || item['Arti kata'],"
)

code = code.replace(
    "suratArtiFA: item['SuratArtiFA'] || item['SuratArtiEN'] || item['SuratArti'] || '',",
    "suratArtiFA: item['SuratArtiFA'] || item['SuratArtiEN'] || item['SuratArti'] || '',\n        suratArtiJA: item['SuratArtiJA'] || item['SuratArtiEN'] || item['SuratArti'] || '',\n        suratArtiKO: item['SuratArtiKO'] || item['SuratArtiEN'] || item['SuratArti'] || '',"
)

code = code.replace(
    "teksArtiFA: item['TeksArtiFA'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',",
    "teksArtiFA: item['TeksArtiFA'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',\n        teksArtiJA: item['TeksArtiJA'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',\n        teksArtiKO: item['TeksArtiKO'] || item['TeksArtiEN'] || item['TeksArtiID'] || item['TeksArti'] || '',"
)

# 4. Update getDefaultJenis defaultMap
code = code.replace(
    "fa: 'منفصل مرفوعی (ضمایر جدا)'",
    "fa: 'منفصل مرفوعی (ضمایر جدا)', ja: '主格分離代名詞', ko: '주격 분리대명사'"
)
code = code.replace(
    "fa: 'اسم موصول'",
    "fa: 'اسم موصول', ja: '関係代名詞', ko: '관계대명사'"
)
code = code.replace(
    "fa: 'اسم استفهام (کلمات پرسشی)'",
    "fa: 'اسم استفهام (کلمات پرسشی)', ja: '疑問詞', ko: '의문사'"
)
code = code.replace(
    "fa: 'ادوات شرط'",
    "fa: 'ادوات شرط', ja: '条件詞', ko: '조건사'"
)
code = code.replace(
    "fa: 'اسم اشاره'",
    "fa: 'اسم اشاره', ja: '指示代名詞', ko: '지시대명사'"
)
code = code.replace(
    "fa: 'اسم فعل'",
    "fa: 'اسم فعل', ja: '動詞性名詞', ko: '동사성 명사'"
)
code = code.replace(
    "fa: 'فعل جامد'",
    "fa: 'فعل جامد', ja: '固着動詞', ko: '불변동사'"
)

# 5. Update populateNoKata in app.js
code = code.replace(
    "} else if (state.lang === 'fa') {\n        localizedArti = group.arti_fa || group.arti_id || group.arti;\n      }",
    "} else if (state.lang === 'fa') {\n        localizedArti = group.arti_fa || group.arti_id || group.arti;\n      } else if (state.lang === 'ja') {\n        localizedArti = group.arti_ja || group.arti_id || group.arti;\n      } else if (state.lang === 'ko') {\n        localizedArti = group.arti_ko || group.arti_id || group.arti;\n      }"
)

# 6. Update updateSpotlightCard in app.js
code = code.replace(
    "} else if (state.lang === 'fa') {\n      elements.badgeBentukKata.textContent = group.bentuk_fa || group.bentuk_id;\n    } else {",
    "} else if (state.lang === 'fa') {\n      elements.badgeBentukKata.textContent = group.bentuk_fa || group.bentuk_id;\n    } else if (state.lang === 'ja') {\n      elements.badgeBentukKata.textContent = group.bentuk_ja || group.bentuk_id;\n    } else if (state.lang === 'ko') {\n      elements.badgeBentukKata.textContent = group.bentuk_ko || group.bentuk_id;\n    } else {"
)

code = code.replace(
    "} else if (state.lang === 'fa') {\n      jenisText = grammar.jenis_fa || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'fa');\n    } else {",
    "} else if (state.lang === 'fa') {\n      jenisText = grammar.jenis_fa || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'fa');\n    } else if (state.lang === 'ja') {\n      jenisText = grammar.jenis_ja || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'ja');\n    } else if (state.lang === 'ko') {\n      jenisText = grammar.jenis_ko || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'ko');\n    } else {"
)

code = code.replace(
    "} else if (state.lang === 'fa') {\n      currentMeaning = group.arti_fa || group.arti_id || group.arti;\n    }",
    "} else if (state.lang === 'fa') {\n      currentMeaning = group.arti_fa || group.arti_id || group.arti;\n    } else if (state.lang === 'ja') {\n      currentMeaning = group.arti_ja || group.arti_id || group.arti;\n    } else if (state.lang === 'ko') {\n      currentMeaning = group.arti_ko || group.arti_id || group.arti;\n    }"
)

code = code.replace(
    "} else if (state.lang === 'fa') {\n      currentDesc = grammar.desc_fa || grammar.desc_id || grammar.keterangan || '';\n    }",
    "} else if (state.lang === 'fa') {\n      currentDesc = grammar.desc_fa || grammar.desc_id || grammar.keterangan || '';\n    } else if (state.lang === 'ja') {\n      currentDesc = grammar.desc_ja || grammar.desc_id || grammar.keterangan || '';\n    } else if (state.lang === 'ko') {\n      currentDesc = grammar.desc_ko || grammar.desc_id || grammar.keterangan || '';\n    }"
)

# 7. Update renderAyatReferences in app.js
code = code.replace(
    "} else if (state.lang === 'fa') {\n          sArti = occ.suratArtiFA;\n          tArti = occ.teksArtiFA;\n        }",
    "} else if (state.lang === 'fa') {\n          sArti = occ.suratArtiFA;\n          tArti = occ.teksArtiFA;\n        } else if (state.lang === 'ja') {\n          sArti = occ.suratArtiJA;\n          tArti = occ.teksArtiJA;\n        } else if (state.lang === 'ko') {\n          sArti = occ.suratArtiKO;\n          tArti = occ.teksArtiKO;\n        }"
)

code = code.replace(
    "} else if (state.lang === 'fa') {\n      activeSuratArti = occ.suratArtiFA || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiFA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }",
    "} else if (state.lang === 'fa') {\n      activeSuratArti = occ.suratArtiFA || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiFA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    } else if (state.lang === 'ja') {\n      activeSuratArti = occ.suratArtiJA || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiJA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    } else if (state.lang === 'ko') {\n      activeSuratArti = occ.suratArtiKO || occ.suratArtiEN || '';\n      activeTeksArti = occ.teksArtiKO || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }"
)

# 8. Update toggleVerseTranslationAudio in app.js
code = code.replace(
    "} else if (state.lang === 'fa') {\n      currentText = occ.teksArtiFA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }",
    "} else if (state.lang === 'fa') {\n      currentText = occ.teksArtiFA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    } else if (state.lang === 'ja') {\n      currentText = occ.teksArtiJA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    } else if (state.lang === 'ko') {\n      currentText = occ.teksArtiKO || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n    }"
)

# 9. Update getSpeechVoiceAndLang in app.js
ja_ko_voice = """    } else if (langKey === 'ja') {
      speechLangCode = 'ja-JP';
      matchVoice = voices.find(v => v.lang.startsWith('ja') || v.lang.includes('ja-') || v.name.toLowerCase().includes('japanese') || v.name.includes('日本語') || v.name.toLowerCase().includes('kyoko') || v.name.toLowerCase().includes('otoya') || v.name.toLowerCase().includes('haruka') || v.name.toLowerCase().includes('ichiro') || v.name.toLowerCase().includes('ayumi')) || voices.find(v => v.lang.startsWith('ja'));
    } else if (langKey === 'ko') {
      speechLangCode = 'ko-KR';
      matchVoice = voices.find(v => v.lang.startsWith('ko') || v.lang.includes('ko-') || v.name.toLowerCase().includes('korean') || v.name.includes('한국어') || v.name.toLowerCase().includes('sunhi') || v.name.toLowerCase().includes('insoo') || v.name.toLowerCase().includes('yuna') || v.name.toLowerCase().includes('heami')) || voices.find(v => v.lang.startsWith('ko'));"""

code = code.replace(
    "    } else if (langKey === 'fa') {\n      speechLangCode = 'fa-IR';\n      matchVoice = voices.find(v => v.lang.startsWith('fa') || v.name.toLowerCase().includes('persian') || v.name.toLowerCase().includes('farsi') || v.name.includes('فارسی')) || voices.find(v => v.lang.startsWith('fa'));",
    "    } else if (langKey === 'fa') {\n      speechLangCode = 'fa-IR';\n      matchVoice = voices.find(v => v.lang.startsWith('fa') || v.name.toLowerCase().includes('persian') || v.name.toLowerCase().includes('farsi') || v.name.includes('فارسی')) || voices.find(v => v.lang.startsWith('fa'));\n" + ja_ko_voice
)

# 10. Update speakDhamirMeaning in app.js
code = code.replace(
    "} else if (state.lang === 'fa') {\n      activeMeaning = group.arti_fa || group.arti_id || group.arti;\n    }",
    "} else if (state.lang === 'fa') {\n      activeMeaning = group.arti_fa || group.arti_id || group.arti;\n    } else if (state.lang === 'ja') {\n      activeMeaning = group.arti_ja || group.arti_id || group.arti;\n    } else if (state.lang === 'ko') {\n      activeMeaning = group.arti_ko || group.arti_id || group.arti;\n    }"
)

# 11. Update openAiModal & buildAiPrompt in app.js
code = code.replace(
    "} else if (state.lang === 'fa') {\n        activeArti = occ.teksArtiFA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }",
    "} else if (state.lang === 'fa') {\n        activeArti = occ.teksArtiFA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      } else if (state.lang === 'ja') {\n        activeArti = occ.teksArtiJA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      } else if (state.lang === 'ko') {\n        activeArti = occ.teksArtiKO || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      }"
)

code = code.replace(
    "} else if (state.lang === 'fa') {\n      teksArti = occ.teksArtiFA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_fa || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    }",
    "} else if (state.lang === 'fa') {\n      teksArti = occ.teksArtiFA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_fa || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    } else if (state.lang === 'ja') {\n      teksArti = occ.teksArtiJA || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_ja || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    } else if (state.lang === 'ko') {\n      teksArti = occ.teksArtiKO || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;\n      grammarDesc = (group.grammar && (group.grammar.desc_ko || group.grammar.desc_id || group.grammar.keterangan)) || '';\n    }"
)

ja_ko_ai_prompt = """    } else if (state.lang === 'ja') {
      if (topic === 'nahwu') {
        return `第${suratNama}章 (${surat})、第${ayat}節における単語「${kata}」(${noKata}, ${bentuk})のアラビア語文法（ナフウ・サルフ）と構文・格変化（イアラーブ）について詳細に解説してください：\\n\\nアラビア語本文:「${teksArab}」\\n日本語訳:「${teksArti}」\\n\\n以下の点を含めてください：\\n1. 文中における「${kata}」の統語的役割と格（主格・対格・属格）。\\n2. 単語の種類（代名詞・関係詞・条件詞等）および形態的特徴（分離形・接尾形）。\\n3. 文法補足解説: ${grammarDesc || "標準的なクルアーン文法規則に基づく解説"}。`;
      } else if (topic === 'tafsir') {
        return `第${suratNama}章 (${surat})、第${ayat}節について、洞察に満ちた簡潔なタフスィール（注釈・解説）を提示してください：\\n\\nアラビア語本文:「${teksArab}」\\n日本語訳:「${teksArti}」\\n\\n単語「${kata}」の意味と役割に焦点を当て、この節が持つ教訓、啓示の背景（サバブ・ヌズール）、信徒の生活への実践的指針を解説してください。`;
      } else {
        return `第${suratNama}章 (${surat})、第${ayat}節における単語「${kata}」の選定に見られるクルアーンの修辞的・文学的卓越性（バラーガ）について解説してください：\\n\\nアラビア語本文:「${teksArab}」\\n日本語訳:「${teksArti}」\\n\\nなぜこの文脈でこの特定の単語や代名詞が選ばれたのか、その言葉が節全体にもたらす深い意味や美しさについて説明してください。`;
      }
    } else if (state.lang === 'ko') {
      if (topic === 'nahwu') {
        return `제${suratNama}장 (${surat}), 제${ayat}절에 나타난 단어 "${kata}" (${noKata}, ${bentuk})의 아랍어 문법(나흐우 및 사르프)과 격변화(이라브)에 대해 심도 있게 분석해 주세요:\\n\\n아랍어 본문: "${teksArab}"\\n한국어 번역: "${teksArti}"\\n\\n다음 사항을 포함해 주세요:\\n1. 문장 내에서 "${kata}"의 통사적 역할과 격(주격/대격/속격).\\n2. 단어의 유형(대명사/관계대명사/조건사 등) 및 형태적 특성(분리형/접미형).\\n3. 문법적 추가 설명: ${grammarDesc || "표준 꾸란 문법 규칙에 따른 분석"}.`;
      } else if (topic === 'tafsir') {
        return `제${suratNama}장 (${surat}), 제${ayat}절에 대한 깊이 있고 간결한 타프시르(주석 및 해설)를 제시해 주세요:\\n\\n아랍어 본문: "${teksArab}"\\n한국어 번역: "${teksArti}"\\n\\n단어 "${kata}"의 의미와 기능에 초점을 맞추어, 이 구절이 주는 영적 교훈, 계시 배경(사밥 안 누줄), 신앙생활에 주는 메시지를 설명해 주세요.`;
      } else {
        return `제${suratNama}장 (${surat}), 제${ayat}절에서 단어 "${kata}"가 사용된 꾸란의 수사학적 아름다움(발라가)과 문학적 우수성을 설명해 주세요:\\n\\n아랍어 본문: "${teksArab}"\\n한국어 번역: "${teksArti}"\\n\\n이 특정한 문맥에서 왜 이 단어나 대명사가 선택되었으며, 구절의 깊은 의미와 표현에 어떠한 정교함을 더하는지 분석해 주세요.`;
      }"""

code = code.replace(
    "    } else if (state.lang === 'fa') {",
    ja_ko_ai_prompt + "\n    } else if (state.lang === 'fa') {"
)

# 12. Update exportToCsv in app.js
code = code.replace(
    "const cleanArtiFA = (occ.teksArtiFA || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');",
    "const cleanArtiFA = (occ.teksArtiFA || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');\n        const cleanArtiJA = (occ.teksArtiJA || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');\n        const cleanArtiKO = (occ.teksArtiKO || occ.teksArtiEN || occ.teksArtiID || '').replace(/\"/g, '\"\"');"
)

code = code.replace(
    ',\\"معنی (FA)\\",',
    ',\\"معنی (FA)\\",\\"意味 (JA)\\",\\"의미 (KO)\\",'
)

code = code.replace(
    ',\\"ترجمه (FA)\\",',
    ',\\"ترجمه (FA)\\",\\"翻訳 (JA)\\",\\"번역 (KO)\\",'
)

code = code.replace(
    '"${group.arti_sw || \'\'}","${group.arti_fa || \'\'}","${group.frek || \'Muttashil\'}"',
    '"${group.arti_sw || \'\'}","${group.arti_fa || \'\'}","${group.arti_ja || \'\'}","${group.arti_ko || \'\'}","${group.frek || \'Muttashil\'}"'
)

code = code.replace(
    '"${cleanArtiSW}","${cleanArtiFA}",',
    '"${cleanArtiSW}","${cleanArtiFA}","${cleanArtiJA}","${cleanArtiKO}",'
)

# 13. Update btnCopyAll in app.js
code = code.replace(
    "} else if (state.lang === 'fa') {\n          activeArti = group.arti_fa || group.arti_id || group.arti;\n        }",
    "} else if (state.lang === 'fa') {\n          activeArti = group.arti_fa || group.arti_id || group.arti;\n        } else if (state.lang === 'ja') {\n          activeArti = group.arti_ja || group.arti_id || group.arti;\n        } else if (state.lang === 'ko') {\n          activeArti = group.arti_ko || group.arti_id || group.arti;\n        }"
)

code = code.replace(
    "} else if (state.lang === 'fa') {\n          activeDesc = grammar.desc_fa || grammar.desc_id || grammar.keterangan || '';\n        }",
    "} else if (state.lang === 'fa') {\n          activeDesc = grammar.desc_fa || grammar.desc_id || grammar.keterangan || '';\n        } else if (state.lang === 'ja') {\n          activeDesc = grammar.desc_ja || grammar.desc_id || grammar.keterangan || '';\n        } else if (state.lang === 'ko') {\n          activeDesc = grammar.desc_ko || grammar.desc_id || grammar.keterangan || '';\n        }"
)

code = code.replace(
    "else if (state.lang === 'fa') titlePrefix = 'اسم‌های موصول قرآن کریم (موصول)';",
    "else if (state.lang === 'fa') titlePrefix = 'اسم‌های موصول قرآن کریم (موصول)';\n          else if (state.lang === 'ja') titlePrefix = 'クルアーン関係代名詞 (マウシュール)';\n          else if (state.lang === 'ko') titlePrefix = '꾸란 관계대명사 (마우슐)';"
)

code = code.replace(
    "else if (state.lang === 'fa') titlePrefix = 'ضمایر قرآن کریم (ضمیر)';",
    "else if (state.lang === 'fa') titlePrefix = 'ضمایر قرآن کریم (ضمیر)';\n          else if (state.lang === 'ja') titlePrefix = 'クルアーン代名詞 (ダミール)';\n          else if (state.lang === 'ko') titlePrefix = '꾸란 인칭대명사 (다미르)';"
)

# 14. Update applyLanguage in app.js
code = code.replace(
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa'].includes(lang) ? lang : 'id';",
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa', 'ja', 'ko'].includes(lang) ? lang : 'id';"
)

# 15. Update updateHeaderTitles in app.js
header_titles_ja_ko = """      } else if (state.lang === 'ja') {
        elements.brandTitle.innerHTML = 'ハルフ・ガイ・アーミル <span>辞書</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'クルアーン非作用不変化詞インタラクティブ辞典';
        if (elements.docTitle) elements.docTitle.textContent = 'ハルフ・ガイ・アーミル辞書 | クルアーン不変化詞インタラクティブリファレンス';
      } else if (state.lang === 'ko') {
        elements.brandTitle.innerHTML = '하르프 가이르 아밀 <span>사전</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = '꾸란 비지배 불변사 상호작용 사전';
        if (elements.docTitle) elements.docTitle.textContent = '하르프 가이르 아밀 사전 | 꾸란 불변사 참조';"""

code = code.replace(
    "      if (state.lang === 'fa') {",
    "      " + header_titles_ja_ko + "\n      } else if (state.lang === 'fa') {"
)

if crlf:
    code = code.replace('\n', '\r\n')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("app.js successfully updated with Japanese (ja) and Korean (ko) support!")
