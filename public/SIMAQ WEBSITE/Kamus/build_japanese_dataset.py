#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to build Japanese (ja) dataset and enrich dhamir_data.json, dhamir_data.js,
harf_data.json, and harf_data.js with complete Japanese translations and grammatical terms.
"""

import os
import sys
import json

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. 114 Surahs Japanese Names & Meanings (Ryoichi Mita / 日本ムスリム協会)
JAPANESE_SURAHS = {
    "1": "開端 (開扉 / アル・ファーティハ)",
    "2": "雌牛 (アル・バカラ)",
    "3": "イムラーン家 (アール・イムラーン)",
    "4": "婦人 (アン・ニサー)",
    "5": "食卓 (アル・マーイダ)",
    "6": "家畜 (アル・アンアーム)",
    "7": "高壁 (アル・アアラーフ)",
    "8": "戦利品 (アル・アンファール)",
    "9": "悔悟 (アッ・タウバ)",
    "10": "ユーヌス (預言者ヨナ)",
    "11": "フード (預言者フード)",
    "12": "ユースフ (預言者ヨセフ)",
    "13": "雷雲 (アッ・ラアド)",
    "14": "イブラーヒーム (アブラハム)",
    "15": "ヒジュル (アル・ヒジュル)",
    "16": "蜜蜂 (アン・ナフル)",
    "17": "夜の旅 (アル・イスラー)",
    "18": "洞窟 (アル・カハフ)",
    "19": "マルヤム (聖母マリア)",
    "20": "ター・ハー",
    "21": "預言者たち (アル・アンビヤー)",
    "22": "巡礼 (アル・ハッジ)",
    "23": "信者たち (アル・ムウミヌーン)",
    "24": "御光 (アン・ヌール)",
    "25": "識別 (アル・フルカーン)",
    "26": "詩人たち (アッ・シュアラー)",
    "27": "蟻 (アン・ナムル)",
    "28": "物語 (アル・カサス)",
    "29": "蜘蛛 (アル・アンカブート)",
    "30": "ビザンツ (アッ・ルーム)",
    "31": "ルクマーン (賢者ルクマーン)",
    "32": "伏拝 (アッ・サジダ)",
    "33": "部族連合 (アル・アハザーブ)",
    "34": "サバア (サバア国)",
    "35": "創造者 (ファーティル)",
    "36": "ヤー・スィーン",
    "37": "整列者 (アッ・サッファート)",
    "38": "サード",
    "39": "集団 (アッ・ズマル)",
    "40": "ガーフィル (信者 / 赦す者)",
    "41": "明解 (フッシラト)",
    "42": "相談 (アッ・シューラー)",
    "43": "黄金の装飾 (アッ・ズフルフ)",
    "44": "煙霧 (アッ・ドハーン)",
    "45": "跪く者 (アル・ジャーシヤ)",
    "46": "砂丘 (アル・アフカーフ)",
    "47": "ムハンマド (預言者ムハンマド)",
    "48": "勝利 (アル・ファトフ)",
    "49": "部屋 (アル・フジュラート)",
    "50": "カーフ",
    "51": "撒き散らす風 (アッ・ザーリヤート)",
    "52": "山 (アッ・トゥール)",
    "53": "星 (アン・ナジュム)",
    "54": "月 (アル・カマル)",
    "55": "慈悲深き御方 (アッ・ラフマーン)",
    "56": "出来事 (アル・ワーキア)",
    "57": "鉄 (アル・ハディード)",
    "58": "抗弁する女 (アル・ムジャーディラ)",
    "59": "集合 (アル・ハシュル)",
    "60": "試問される女 (アル・ムムタハナ)",
    "61": "戦列 (アッ・サッフ)",
    "62": "合同礼拝 (アル・ジュムア)",
    "63": "偽善者たち (アル・ムナーフィクーン)",
    "64": "欺瞞 (アッ・タグワーブン)",
    "65": "離婚 (アッ・タラーク)",
    "66": "禁止 (アッ・タハリーム)",
    "67": "主権 (アル・ムルク)",
    "68": "筆 (アル・カラム)",
    "69": "真実 (アル・ハッカ)",
    "70": "階段 (アル・マアーリジュ)",
    "71": "ヌーフ (預言者ノア)",
    "72": "幽精 (アル・ジン)",
    "73": "身を包む者 (アル・ムッザンミル)",
    "74": "外衣を纏う者 (アル・ムッダッシル)",
    "75": "復活 (アル・キヤーマ)",
    "76": "人間 (アル・インサーン)",
    "77": "送られるもの (アル・ムルサラート)",
    "78": "消息 (アン・ナバア)",
    "79": "引き離すもの (アン・ナージアート)",
    "80": "眉をひそめて (アバサ)",
    "81": "包み隠す (アッ・タクウィール)",
    "82": "裂ける (アル・インフィタール)",
    "83": "詐欺 (アル・ムタッフィフィーン)",
    "84": "破裂 (アル・インシカーク)",
    "85": "星座 (アル・ブルージュ)",
    "86": "夜訪れるもの (アッ・ターリク)",
    "87": "至高者 (アル・アアラー)",
    "88": "圧倒的事態 (アル・ガーシヤ)",
    "89": "暁 (アル・ファジュル)",
    "90": "町 (アル・バラド)",
    "91": "太陽 (アッ・シャムス)",
    "92": "夜 (アル・ライル)",
    "93": "朝 (アッ・ドゥハー)",
    "94": "胸を広げる (アッ・シャルフ)",
    "95": "無花果 (アッ・ティーン)",
    "96": "凝血 (アル・アラク)",
    "97": "みいつ (アル・カドル / 栄光)",
    "98": "明証 (アル・バイイナ)",
    "99": "地震 (アッ・ザルザラ)",
    "100": "突撃する馬 (アル・アーディヤート)",
    "101": "恐れ戦く日 (アル・カーリア)",
    "102": "蓄積競争 (アッ・タカースル)",
    "103": "衰微の時 (アル・アスル)",
    "104": "中傷者 (アル・フマザ)",
    "105": "象 (アル・フィール)",
    "106": "クライシュ族 (クライシュ)",
    "107": "慈善 (アル・マーウーン)",
    "108": "潤沢 (アル・カウサル)",
    "109": "不信者たち (アル・カーフィルーン)",
    "110": "援助 (アン・ナスル)",
    "111": "棕櫚 (アル・マスド / 炎)",
    "112": "純正 (アル・イフラース / 唯一神)",
    "113": "黎明 (アル・ファラク)",
    "114": "人々 (アン・ナース)"
}

# 2. 7 Categories (Bentuk Kata) in Japanese
BENTUK_KATA_JA = {
    '1. Dhamir': '1. 代名詞 (Dhamir - Pronouns)',
    '2. Mawshul': '2. 関係代名詞 (Mawshul - Relative Pronouns)',
    '3. Istifham': '3. 疑問詞 (Istifham - Interrogatives)',
    '4. Syarath': '4. 条件詞 (Syarath - Conditionals)',
    '5. Isyarah': '5. 指示代名詞 (Isyarah - Demonstratives)',
    "6. Isim Fi'il": "6. 動詞性名詞 (Isim Fi'il - Verbal Nouns)",
    "7. Fi'il Jamid": "7. 固着動詞 (Fi'il Jamid - Inflexible Verbs)"
}

# 3. 76 Jamid Mabny Grammatical Metadata in Japanese
JAPANESE_GRAMMAR = {
    "1. Dhamir__1a": {
        "arti_ja": "彼 (単数男性)",
        "desc_ja": "彼（三人称単数男性主格分離代名詞）",
        "jenis_ja": "主格分離代名詞"
    },
    "1. Dhamir__1b": {
        "arti_ja": "彼の / 彼を",
        "desc_ja": "彼の／彼を（三人称単数男性接尾代名詞）",
        "jenis_ja": "接尾代名詞"
    },
    "1. Dhamir__1c": {
        "arti_ja": "彼だけを",
        "desc_ja": "彼だけを（三人称単数男性対格分離代名詞）",
        "jenis_ja": "対格分離代名詞"
    },
    "1. Dhamir__2a": {
        "arti_ja": "彼ら二人",
        "desc_ja": "彼ら二人（三人称双数主格分離代名詞）",
        "jenis_ja": "主格分離代名詞（双数）"
    },
    "1. Dhamir__2b": {
        "arti_ja": "彼ら二人の / 二人を",
        "desc_ja": "彼ら二人の／二人を（三人称双数接尾代名詞）",
        "jenis_ja": "接尾代名詞（双数）"
    },
    "1. Dhamir__3a": {
        "arti_ja": "彼ら (複数男性)",
        "desc_ja": "彼ら（三人称複数男性主格分離代名詞）",
        "jenis_ja": "主格分離代名詞（複数男性）"
    },
    "1. Dhamir__3b": {
        "arti_ja": "彼らの / 彼らを",
        "desc_ja": "彼らの／彼らを（三人称複数男性接尾代名詞）",
        "jenis_ja": "接尾代名詞（複数男性）"
    },
    "1. Dhamir__3c": {
        "arti_ja": "彼らだけを",
        "desc_ja": "彼らだけを（三人称複数男性対格分離代名詞）",
        "jenis_ja": "対格分離代名詞（複数男性）"
    },
    "1. Dhamir__4a": {
        "arti_ja": "彼女 (単数女性)",
        "desc_ja": "彼女（三人称単数女性主格分離代名詞）",
        "jenis_ja": "主格分離代名詞（単数女性）"
    },
    "1. Dhamir__4b": {
        "arti_ja": "彼女の / 彼女を",
        "desc_ja": "彼女の／彼女を（三人称単数女性接尾代名詞）",
        "jenis_ja": "接尾代名詞（単数女性）"
    },
    "1. Dhamir__5a": {
        "arti_ja": "彼女たち (複数女性)",
        "desc_ja": "彼女たち（三人称複数女性主格分離代名詞）",
        "jenis_ja": "主格分離代名詞（複数女性）"
    },
    "1. Dhamir__5b": {
        "arti_ja": "彼女たちの / 彼女たちを",
        "desc_ja": "彼女たちの／彼女たちを（三人称複数女性接尾代名詞）",
        "jenis_ja": "接尾代名詞（複数女性）"
    },
    "1. Dhamir__6a": {
        "arti_ja": "あなた (単数男性)",
        "desc_ja": "あなた（二人称単数男性主格分離代名詞）",
        "jenis_ja": "主格分離代名詞（単数男性）"
    },
    "1. Dhamir__6b": {
        "arti_ja": "あなたの / あなたを",
        "desc_ja": "あなたの／あなたを（二人称単数男性接尾代名詞）",
        "jenis_ja": "接尾代名詞（単数男性）"
    },
    "1. Dhamir__6c": {
        "arti_ja": "あなただけを",
        "desc_ja": "あなただけを（二人称単数男性対格分離代名詞）",
        "jenis_ja": "対格分離代名詞（単数男性）"
    },
    "1. Dhamir__7a": {
        "arti_ja": "あなた方二人",
        "desc_ja": "あなた方二人（二人称双数主格分離代名詞）",
        "jenis_ja": "主格分離代名詞（双数）"
    },
    "1. Dhamir__7b": {
        "arti_ja": "あなた方二人の",
        "desc_ja": "あなた方二人の／二人を（二人称双数接尾代名詞）",
        "jenis_ja": "接尾代名詞（双数）"
    },
    "1. Dhamir__8a": {
        "arti_ja": "あなた方 (複数男性)",
        "desc_ja": "あなた方（二人称複数男性主格分離代名詞）",
        "jenis_ja": "主格分離代名詞（複数男性）"
    },
    "1. Dhamir__8b": {
        "arti_ja": "あなた方の / あなた方を",
        "desc_ja": "あなた方の／あなた方を（二人称複数男性接尾代名詞）",
        "jenis_ja": "接尾代名詞（複数男性）"
    },
    "1. Dhamir__8c": {
        "arti_ja": "あなた方だけを",
        "desc_ja": "あなた方だけを（二人称複数男性対格分離代名詞）",
        "jenis_ja": "対格分離代名詞（複数男性）"
    },
    "1. Dhamir__9b": {
        "arti_ja": "あなたの / あなたを (女性)",
        "desc_ja": "あなたの／あなたを（二人称単数女性接尾代名詞）",
        "jenis_ja": "接尾代名詞（単数女性）"
    },
    "1. Dhamir__11a": {
        "arti_ja": "私",
        "desc_ja": "私（一人称単数主格分離代名詞）",
        "jenis_ja": "主格分離代名詞（一人称単数）"
    },
    "1. Dhamir__11b": {
        "arti_ja": "私の / 私を",
        "desc_ja": "私の／私を（一人称単数接尾代名詞）",
        "jenis_ja": "接尾代名詞（一人称単数）"
    },
    "1. Dhamir__11c": {
        "arti_ja": "私だけを",
        "desc_ja": "私だけを（一人称単数対格分離代名詞）",
        "jenis_ja": "対格分離代名詞（一人称単数）"
    },
    "1. Dhamir__12a": {
        "arti_ja": "私たち",
        "desc_ja": "私たち（一人称複数主格分離代名詞）",
        "jenis_ja": "主格分離代名詞（一人称複数）"
    },
    "1. Dhamir__12b": {
        "arti_ja": "私たちの / 私たちを",
        "desc_ja": "私たちの／私たちを（一人称複数接尾代名詞）",
        "jenis_ja": "接尾代名詞（一人称複数）"
    },
    "1. Dhamir__12c": {
        "arti_ja": "私たちだけを",
        "desc_ja": "私たちだけを（一人称複数対格分離代名詞）",
        "jenis_ja": "対格分離代名詞（一人称複数）"
    },
    "2. Mawshul__1": {
        "arti_ja": "〜するもの (無理性)",
        "desc_ja": "非有理名詞に用いられる一般的な関係名詞（マー）",
        "jenis_ja": "関係名詞（無理性）"
    },
    "2. Mawshul__2": {
        "arti_ja": "〜する者たち (複数男性)",
        "desc_ja": "関係代名詞（複数男性・有理性）",
        "jenis_ja": "関係名詞（特定）"
    },
    "2. Mawshul__3": {
        "arti_ja": "〜する者 (有理性)",
        "desc_ja": "有理名詞に用いられる一般的な関係詞（マン）",
        "jenis_ja": "関係名詞（有理性）"
    },
    "2. Mawshul__4": {
        "arti_ja": "〜する者 (単数男性)",
        "desc_ja": "関係代名詞（単数男性）",
        "jenis_ja": "関係名詞（特定）"
    },
    "2. Mawshul__5": {
        "arti_ja": "どれ / どちらの",
        "desc_ja": "どちらの／どれ（関係名詞・疑問名詞）",
        "jenis_ja": "関係名詞（格変化）"
    },
    "2. Mawshul__6": {
        "arti_ja": "〜する者 (単数女性)",
        "desc_ja": "関係代名詞（単数女性）",
        "jenis_ja": "関係名詞（特定）"
    },
    "2. Mawshul__7": {
        "arti_ja": "〜する者たち (複数女性・アッラーイー)",
        "desc_ja": "関係代名詞（複数女性・アッラーイー）",
        "jenis_ja": "関係名詞（特定）"
    },
    "2. Mawshul__8": {
        "arti_ja": "〜する者たち (複数女性・アッラーティー)",
        "desc_ja": "関係代名詞（複数女性・アッラーティー）",
        "jenis_ja": "関係名詞（特定）"
    },
    "2. Mawshul__9": {
        "arti_ja": "〜する二人 (双数男性)",
        "desc_ja": "関係代名詞（双数男性主格）",
        "jenis_ja": "関係名詞（双数）"
    },
    "2. Mawshul__10": {
        "arti_ja": "どちらの女性",
        "desc_ja": "関係代名詞（女性形）",
        "jenis_ja": "関係名詞（女性）"
    },
    "3. Istifham__1": {
        "arti_ja": "何が？ / 何",
        "desc_ja": "非有理存在や物事を尋ねる疑問詞（マー）",
        "jenis_ja": "疑問名詞（無理性）"
    },
    "3. Istifham__2": {
        "arti_ja": "どのように？",
        "desc_ja": "状態や様態を尋ねる疑問詞（カイファ）",
        "jenis_ja": "疑問副詞（様態）"
    },
    "3. Istifham__3": {
        "arti_ja": "誰が？ / 誰",
        "desc_ja": "有理存在を尋ねる疑問詞（マン）",
        "jenis_ja": "疑問名詞（有理性）"
    },
    "3. Istifham__4": {
        "arti_ja": "どれ？ / どちら？",
        "desc_ja": "選択を求める疑問詞（アイユ）",
        "jenis_ja": "選択疑問詞"
    },
    "3. Istifham__5": {
        "arti_ja": "どこから？ / どのように？",
        "desc_ja": "場所・状態・出所を尋ねる疑問詞（アンナー）",
        "jenis_ja": "疑問副詞（様態・場所）"
    },
    "3. Istifham__6": {
        "arti_ja": "一体何が？",
        "desc_ja": "強い疑問を表す疑問詞（マーザー）",
        "jenis_ja": "強調疑問詞"
    },
    "3. Istifham__7": {
        "arti_ja": "いくつ？ / どれほど？",
        "desc_ja": "数量や時間を尋ねる疑問詞（カム）",
        "jenis_ja": "疑問副詞（数量）"
    },
    "3. Istifham__8": {
        "arti_ja": "なぜ？ / 何のために",
        "desc_ja": "理由や目的を尋ねる疑問詞（リマ）",
        "jenis_ja": "前置詞＋疑問詞"
    },
    "3. Istifham__9": {
        "arti_ja": "どこに？",
        "desc_ja": "場所を尋ねる疑問詞（アイナ）",
        "jenis_ja": "疑問副詞（場所）"
    },
    "3. Istifham__10": {
        "arti_ja": "いつ？ (審判の日)",
        "desc_ja": "重大な時（終末等）を尋ねる疑問詞（アイヤーナ）",
        "jenis_ja": "疑問副詞（重大な時）"
    },
    "4. Syarath__1": {
        "arti_ja": "誰でも〜する者は",
        "desc_ja": "有理名詞に用いられる条件名詞（マン）",
        "jenis_ja": "条件名詞（有理性）"
    },
    "4. Syarath__2": {
        "arti_ja": "何であれ〜するものは",
        "desc_ja": "非有理名詞に用いられる条件名詞（マー）",
        "jenis_ja": "条件名詞（無理性）"
    },
    "4. Syarath__3": {
        "arti_ja": "〜する時はいつでも",
        "desc_ja": "時間を表す条件名詞（イズマー／クルラマー）",
        "jenis_ja": "時間条件名詞"
    },
    "4. Syarath__4": {
        "arti_ja": "いかなるものであれ",
        "desc_ja": "包括的選択を表す条件名詞（アイヤン）",
        "jenis_ja": "選択条件名詞"
    },
    "4. Syarath__5": {
        "arti_ja": "その二つのどちらであれ",
        "desc_ja": "強調された二者択一条件名詞（アイヤマ）",
        "jenis_ja": "強調条件名詞"
    },
    "5. Isyarah__1": {
        "arti_ja": "これ / あれ (単数男性)",
        "desc_ja": "指示代名詞（単数男性）",
        "jenis_ja": "指示名詞（単数男性）"
    },
    "5. Isyarah__2": {
        "arti_ja": "これら / あれら (複数)",
        "desc_ja": "指示代名詞（複数）",
        "jenis_ja": "指示名詞（複数）"
    },
    "5. Isyarah__3": {
        "arti_ja": "これ (単数女性)",
        "desc_ja": "近称指示代名詞（単数女性）",
        "jenis_ja": "指示名詞（単数女性）"
    },
    "5. Isyarah__4": {
        "arti_ja": "あれ (単数女性)",
        "desc_ja": "遠称指示代名詞（単数女性）",
        "jenis_ja": "遠称指示名詞（女性）"
    },
    "5. Isyarah__5": {
        "arti_ja": "ここに",
        "desc_ja": "近称の場所を表す指示副詞（ハーハナ）",
        "jenis_ja": "場所指示副詞（近称）"
    },
    "5. Isyarah__6": {
        "arti_ja": "あそこに / そこに",
        "desc_ja": "遠称の場所を表す指示副詞（フナーリカ）",
        "jenis_ja": "場所指示副詞（遠称）"
    },
    "5. Isyarah__7": {
        "arti_ja": "これら二人 (男性)",
        "desc_ja": "双数男性指示代名詞（ザーニカ）",
        "jenis_ja": "指示名詞（双数男性）"
    },
    "5. Isyarah__8": {
        "arti_ja": "これら二人 (女性)",
        "desc_ja": "双数女性指示代名詞（ターニカ）",
        "jenis_ja": "指示名詞（双数女性）"
    },
    "6. Isim Fi'il__1": {
        "arti_ja": "神に栄光あれ！ (スブハーナ)",
        "desc_ja": "讃美・賛美の絶対対格名詞",
        "jenis_ja": "動詞性讃美名詞"
    },
    "6. Isim Fi'il__2": {
        "arti_ja": "さあ持っておいで！",
        "desc_ja": "命令を表す動詞性名詞（ハートゥー）",
        "jenis_ja": "命令動詞性名詞"
    },
    "6. Isim Fi'il__3": {
        "arti_ja": "ああ！ (うんざりだ)",
        "desc_ja": "不快・嫌悪を表す現在動詞性名詞（ウッフ）",
        "jenis_ja": "現在動詞性名詞"
    },
    "6. Isim Fi'il__4": {
        "arti_ja": "神の御加護を！",
        "desc_ja": "保護・避難を求める動詞性名詞（マアーザッラー）",
        "jenis_ja": "祈願動詞性名詞"
    },
    "6. Isim Fi'il__5": {
        "arti_ja": "さあ来なさい！",
        "desc_ja": "促し・集合を表す動詞性名詞（ハルンマ）",
        "jenis_ja": "命令動詞性名詞"
    },
    "6. Isim Fi'il__6": {
        "arti_ja": "なんと遠いことか！",
        "desc_ja": "距離の隔たりを表す過去動詞性名詞（ハイハータ）",
        "jenis_ja": "過去動詞性名詞"
    },
    "6. Isim Fi'il__7": {
        "arti_ja": "さあ、これを取って読め！",
        "desc_ja": "命令を表す動詞性名詞（ハーウム）",
        "jenis_ja": "命令動詞性名詞"
    },
    "6. Isim Fi'il__8": {
        "arti_ja": "さあ、おいで！",
        "desc_ja": "呼びかけ・促しを表す動詞性名詞（ハイタ・ラク）",
        "jenis_ja": "命令動詞性名詞"
    },
    "7. Fi'il Jamid__1": {
        "arti_ja": "〜ではない (否定)",
        "desc_ja": "否定を表す不完全固着動詞（ライサ）",
        "jenis_ja": "不完全固着動詞（否定）"
    },
    "7. Fi'il Jamid__2": {
        "arti_ja": "〜かもしれない (希望)",
        "desc_ja": "希望・期待を表す固着動詞（アサー）",
        "jenis_ja": "希望固着動詞"
    },
    "7. Fi'il Jamid__3": {
        "arti_ja": "なんと良いことか！ (賞賛)",
        "desc_ja": "賞賛を表す固着動詞（ニウマ）",
        "jenis_ja": "賞賛固着動詞"
    },
    "7. Fi'il Jamid__4": {
        "arti_ja": "なんと悪いことか！ (非難)",
        "desc_ja": "非難を表す固着動詞（ビウサ）",
        "jenis_ja": "非難固着動詞"
    },
    "7. Fi'il Jamid__5": {
        "arti_ja": "なんと悪いことか！ (複合)",
        "desc_ja": "非難を表す複合固着動詞（ビウサマー）",
        "jenis_ja": "複合非難動詞"
    },
    "7. Fi'il Jamid__6": {
        "arti_ja": "〜し始めた (開始)",
        "desc_ja": "開始を表す固着動詞（タフィカ）",
        "jenis_ja": "開始動詞"
    },
    "7. Fi'il Jamid__7": {
        "arti_ja": "神よ、お許しください！",
        "desc_ja": "除外・神聖化の固着動詞（ハーシャ・リッラー）",
        "jenis_ja": "神聖化固着動詞"
    },
    "7. Fi'il Jamid__8": {
        "arti_ja": "なんと良い教訓か！",
        "desc_ja": "賞賛を表す複合固着動詞（ニインマー）",
        "jenis_ja": "複合賞賛動詞"
    }
}

# 4. 17 Harf Ghair 'Amil Categories in Japanese
BENTUK_HARF_JA = {
    "1. Harf Istifham": "1. 疑問詞 (Harf Istifham)",
    "2. Harf Nida'": "2. 呼びかけ詞 (Harf Nida')",
    "3. Harf 'Athaf": "3. 接続詞 (Harf 'Athaf)",
    "4. Harf Jawab": "4. 応答詞 (Harf Jawab)",
    "5. Harf Rad'": "5. 拒絶・戒め詞 (Harf Rad')",
    "6. Harf Tanbih": "6. 注意喚起詞 (Harf Tanbih)",
    "7. Harf Ijabah": "7. 肯定詞 (Harf Ijabah)",
    "8. Harf Syarath": "8. 条件詞 (Harf Syarath)",
    "9. Harf Mashdariyah": "9. 語幹詞 (Harf Mashdariyah)",
    "10. Harf Tahdidh": "10. 勧奨・督促詞 (Harf Tahdidh)",
    "11. Harf Ta'lil": "11. 理由説明詞 (Harf Ta'lil)",
    "12. Harf Nafyi": "12. 否定詞 (Harf Nafyi)",
    "13. Harf Nahyi": "13. 禁止詞 (Harf Nahyi)",
    "14. Harf Istiqbal": "14. 未来詞 (Harf Istiqbal)",
    "15. Harf Taukid": "15. 強調詞 (Harf Taukid)",
    "16. Harf Ziyadah": "16. 添え字・修辞詞 (Harf Ziyadah)",
    "17. Harf Mabany": "17. 独立文字 (Harf Mabany / 冒頭頭文字)"
}

# 5. 52 Harf Grammatical Metadata in Japanese
JAPANESE_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {
        "arti_ja": "〜ではない (否定・ラー)",
        "desc_ja": "絶対否定小辞（ラー）",
        "jenis_ja": "否定小辞"
    },
    "1. Harf Nafyi__2": {
        "arti_ja": "〜ではない (否定・マー)",
        "desc_ja": "一般的否定小辞（マー）",
        "jenis_ja": "否定小辞"
    },
    "1. Harf Nafyi__3": {
        "arti_ja": "〜にほかならない (イン)",
        "desc_ja": "除外を伴う否定小辞（イン）",
        "jenis_ja": "否定小辞"
    },
    "1. Harf Nafyi__4": {
        "arti_ja": "〜であろうか？ (反語否定)",
        "desc_ja": "否定の意味を含む疑問詞（ハル）",
        "jenis_ja": "反語否定疑問詞"
    },
    "1. Harf Nafyi__5": {
        "arti_ja": "逃げる時ではない",
        "desc_ja": "時を表す名詞に付く否定小辞（ラアタ）",
        "jenis_ja": "否定小辞"
    },
    "1. Harf Nafyi__6": {
        "arti_ja": "真理のほかに何があろうか",
        "desc_ja": "否定を含む疑問詞（マーザー）",
        "jenis_ja": "反語否定疑問詞"
    },
    "2. Harf Tahqiq Taswif__7": {
        "arti_ja": "確かに〜した (確証のカド)",
        "desc_ja": "過去形と共に確証を表す小辞（カド）",
        "jenis_ja": "確証小辞"
    },
    "2. Harf Tahqiq Taswif__8": {
        "arti_ja": "いずれ〜するであろう",
        "desc_ja": "未来を表す小辞（サウファ）",
        "jenis_ja": "未来小辞"
    },
    "3. Harf Syarat__9": {
        "arti_ja": "もし〜ならば (ロウ)",
        "desc_ja": "反事実的条件小辞（ロウ）",
        "jenis_ja": "条件小辞"
    },
    "3. Harf Syarat__10": {
        "arti_ja": "もし〜がなかったならば",
        "desc_ja": "存在の否定を条件とする小辞（ロウラー）",
        "jenis_ja": "留保条件小辞"
    },
    "3. Harf Syarat__11": {
        "arti_ja": "たとえ〜であっても",
        "desc_ja": "譲歩的条件小辞（ロウ）",
        "jenis_ja": "譲歩条件小辞"
    },
    "3. Harf Syarat__12": {
        "arti_ja": "もし〜ならば (イムマー)",
        "desc_ja": "強調条件小辞（イン＋マー）",
        "jenis_ja": "強調条件小辞"
    },
    "3. Harf Syarat__13": {
        "arti_ja": "いかなる徴であれ",
        "desc_ja": "包括的条件名詞（マフマー）",
        "jenis_ja": "包括条件名詞"
    },
    "4. Harf Mashdariyah__14": {
        "arti_ja": "〜である限り",
        "desc_ja": "時間を表す名詞化小辞（マー）",
        "jenis_ja": "時間名詞化小辞"
    },
    "4. Harf Mashdariyah__15": {
        "arti_ja": "〜しないように",
        "desc_ja": "否定を伴う名詞化小辞（アン＋ラー）",
        "jenis_ja": "名詞化否定小辞"
    },
    "4. Harf Mashdariyah__16": {
        "arti_ja": "〜ということ (アン)",
        "desc_ja": "動詞を名詞句化する小辞（アン）",
        "jenis_ja": "名詞化小辞"
    },
    "4. Harf Mashdariyah__17": {
        "arti_ja": "〜することを願う",
        "desc_ja": "願望の名詞化小辞（ロウ）",
        "jenis_ja": "願望名詞化小辞"
    },
    "4. Harf Mashdariyah__18": {
        "arti_ja": "〜しないこと",
        "desc_ja": "禁止を伴う名詞化小辞（アン＋ラー）",
        "jenis_ja": "名詞化禁止小辞"
    },
    "4. Harf Mashdariyah__19": {
        "arti_ja": "〜であること",
        "desc_ja": "事実の名詞化小辞（アン短縮形）",
        "jenis_ja": "名詞化小辞"
    },
    "5. Harf Zaidah__20": {
        "arti_ja": "〜のように (強調)",
        "desc_ja": "比喩の接頭辞＋強調添え字（カ＋マー）",
        "jenis_ja": "強調添え字"
    },
    "5. Harf Zaidah__21": {
        "arti_ja": "たとえ蚊のようなものであれ",
        "desc_ja": "漠然・強調の添え字（マー）",
        "jenis_ja": "強調添え字"
    },
    "5. Harf Zaidah__22": {
        "arti_ja": "我は誓う",
        "desc_ja": "誓約を強める添え字（ラー）",
        "jenis_ja": "誓約強調添え字"
    },
    "5. Harf Zaidah__23": {
        "arti_ja": "神の慈悲によって",
        "desc_ja": "前置詞に伴う強調添え字（ビ＋マー）",
        "jenis_ja": "前置詞強調添え字"
    },
    "5. Harf Zaidah__24": {
        "arti_ja": "吉報をもたらす者が来た時",
        "desc_ja": "時間接続詞に伴う添え字（アン）",
        "jenis_ja": "時間強調添え字"
    },
    "6. Harf Istifham__25": {
        "arti_ja": "〜か？ (疑問のハル)",
        "desc_ja": "質問・確認を表す疑問小辞（ハル）",
        "jenis_ja": "疑問小辞"
    },
    "7. Harf Jawab__26": {
        "arti_ja": "その時には / ならば",
        "desc_ja": "応答・帰結を表す小辞（イザン）",
        "jenis_ja": "応答帰結小辞"
    },
    "7. Harf Jawab__27": {
        "arti_ja": "いや / その通りです",
        "desc_ja": "否定に対する肯定応答詞（バラー）",
        "jenis_ja": "肯定応答小辞"
    },
    "7. Harf Jawab__28": {
        "arti_ja": "はい / その通り",
        "desc_ja": "肯定応答詞（ナアム）",
        "jenis_ja": "肯定応答小辞"
    },
    "7. Harf Jawab__29": {
        "arti_ja": "そうだ！主にかけて",
        "desc_ja": "誓いを伴う肯定応答詞（イー）",
        "jenis_ja": "誓約応答小辞"
    },
    "8. Harf Ibtida'__30": {
        "arti_ja": "〜に至るまで",
        "desc_ja": "文頭・発端を表す小辞（ハッター）",
        "jenis_ja": "発端小辞"
    },
    "9. Harf Tafshil__31": {
        "arti_ja": "〜に関しては",
        "desc_ja": "詳細化・主題提示小辞（アンマー）",
        "jenis_ja": "詳細化小辞"
    },
    "10. Harf Mufaja'ah__32": {
        "arti_ja": "たちまち〜となった",
        "desc_ja": "突発・不意の出来事を表す小辞（イザー）",
        "jenis_ja": "突発事象小辞"
    },
    "11. Harf Mufassirah__33": {
        "arti_ja": "すなわち〜と",
        "desc_ja": "解説・説明を導く小辞（アン）",
        "jenis_ja": "説明小辞"
    },
    "12. Harf Istiftahiyah__34": {
        "arti_ja": "見よ！ / 心せよ",
        "desc_ja": "注意喚起・開始小辞（アラー）",
        "jenis_ja": "注意喚起小辞"
    },
    "13. Harf Rada'__35": {
        "arti_ja": "断じて否！",
        "desc_ja": "戒め・強い拒絶の小辞（カッラー）",
        "jenis_ja": "戒め・拒絶小辞"
    },
    "14. Harf Ta'ajjub__36": {
        "arti_ja": "なんと忍耐強いことか！",
        "desc_ja": "感嘆・驚きを表す小辞（マー）",
        "jenis_ja": "感嘆小辞"
    },
    "15. Harf Fariqah__37": {
        "arti_ja": "確かに / まさに",
        "desc_ja": "肯定を区別する強調ラーム（イン短縮形に伴う）",
        "jenis_ja": "区別強調ラーム"
    },
    "16. Harf Mauthi'ah__38": {
        "arti_ja": "もし〜ならば誓って",
        "desc_ja": "誓約を導く条件ラーム（ラ・イン）",
        "jenis_ja": "誓約前置ラーム"
    },
    "17. Harf Mabany__39": {
        "arti_ja": "ハー・ミーム",
        "desc_ja": "章冒頭の神秘的独立文字（حم）",
        "jenis_ja": "独立文字 (ムカッタアート)"
    },
    "17. Harf Mabany__40": {
        "arti_ja": "アリフ・ラーム・ミーム",
        "desc_ja": "章冒頭の神秘的独立文字（الم）",
        "jenis_ja": "独立文字 (ムカッタアート)"
    },
    "17. Harf Mabany__41": {
        "arti_ja": "アリフ・ラーム・ラー",
        "desc_ja": "章冒頭の神秘的独立文字（الر）",
        "jenis_ja": "独立文字 (ムカッタアート)"
    },
    "17. Harf Mabany__42": {
        "arti_ja": "ター・スィーン・ミーム",
        "desc_ja": "章冒頭の神秘的独立文字（طسم）",
        "jenis_ja": "独立文字 (ムカッタアート)"
    },
    "17. Harf Mabany__43": {
        "arti_ja": "アリフ・ラーム・ミーム・ラー",
        "desc_ja": "章冒頭の神秘的独立文字（المر）",
        "jenis_ja": "独立文字 (ムカッタアート)"
    },
    "17. Harf Mabany__44": {
        "arti_ja": "アリフ・ラーム・ミーム・サード",
        "desc_ja": "章冒頭の神秘的独立文字（المص）",
        "jenis_ja": "独立文字 (ムカッタアート)"
    },
    "17. Harf Mabany__45": {
        "arti_ja": "サード",
        "desc_ja": "章冒頭の神秘的独立文字（ص）",
        "jenis_ja": "独立文字 (ムカッタアート)"
    },
    "17. Harf Mabany__46": {
        "arti_ja": "ター・スィーン",
        "desc_ja": "章冒頭の神秘的独立文字（طس）",
        "jenis_ja": "独立文字 (ムカッタアート)"
    },
    "17. Harf Mabany__47": {
        "arti_ja": "ター・ハー",
        "desc_ja": "章冒頭の神秘的独立文字（طه）",
        "jenis_ja": "独立文字 (ムカッタアート)"
    },
    "17. Harf Mabany__48": {
        "arti_ja": "アイン・スィーン・カーフ",
        "desc_ja": "章冒頭の神秘的独立文字（عسق）",
        "jenis_ja": "独立文字 (ムカッタアート)"
    },
    "17. Harf Mabany__49": {
        "arti_ja": "カーフ",
        "desc_ja": "章冒頭の神秘的独立文字（ق）",
        "jenis_ja": "独立文字 (ムカッタアート)"
    },
    "17. Harf Mabany__50": {
        "arti_ja": "カーフ・ハー・ヤー・アイン・サード",
        "desc_ja": "章冒頭の神秘的独立文字（كهيعص）",
        "jenis_ja": "独立文字 (ムカッタアート)"
    },
    "17. Harf Mabany__51": {
        "arti_ja": "ヌーン",
        "desc_ja": "章冒頭の神秘的独立文字（ن）",
        "jenis_ja": "独立文字 (ムカッタアート)"
    },
    "17. Harf Mabany__52": {
        "arti_ja": "ヤー・スィーン",
        "desc_ja": "章冒頭の神秘的独立文字（يس）",
        "jenis_ja": "独立文字 (ムカッタアート)"
    }
}


def enrich_dhamir_data():
    print("Enriching dhamir_data.json and dhamir_data.js with Japanese...")
    
    with open(os.path.join(BASE_DIR, 'ja_translations.json'), 'r', encoding='utf-8') as f:
        ja_translations = json.load(f)

    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = item.get('No kata', '')
        g_key = f"{b}__{nk}"
        
        # 1. BentukKataJA
        item['BentukKataJA'] = BENTUK_KATA_JA.get(b, b)
        
        # 2. SuratArtiJA
        surat_num = str(item.get('SURAT', ''))
        item['SuratArtiJA'] = JAPANESE_SURAHS.get(surat_num, item.get('SuratArtiEN', ''))
        
        # 3. ArtiKataJA & Grammar JA
        g_info = JAPANESE_GRAMMAR.get(g_key, {})
        item['ArtiKataJA'] = g_info.get('arti_ja', item.get('ArtiKataEN', item.get('Arti kata', '')))
        
        if 'Grammar' not in item:
            item['Grammar'] = {}
        if g_info.get('arti_ja'):
            item['Grammar']['arti_ja'] = g_info['arti_ja']
        if g_info.get('desc_ja'):
            item['Grammar']['desc_ja'] = g_info['desc_ja']
        if g_info.get('jenis_ja'):
            item['Grammar']['jenis_ja'] = g_info['jenis_ja']
            
        # 4. TeksArtiJA
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"
        teks_ja = ja_translations.get(v_key, item.get('TeksArtiEN', item.get('TeksArtiID', '')))
        item['TeksArtiJA'] = teks_ja

    # Write dhamir_data.json
    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Write dhamir_data.js
    with open(os.path.join(BASE_DIR, 'dhamir_data.js'), 'w', encoding='utf-8') as f:
        f.write("const DHAMIR_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n\nif (typeof module !== 'undefined' && module.exports) {\n  module.exports = DHAMIR_DATA;\n}\n")

    print(f"dhamir_data successfully updated with Japanese! (Total items: {len(data)})")


def enrich_harf_data():
    print("Enriching harf_data.json and harf_data.js with Japanese...")
    
    with open(os.path.join(BASE_DIR, 'ja_translations.json'), 'r', encoding='utf-8') as f:
        ja_translations = json.load(f)

    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = item.get('No kata', '')
        g_key = f"{b}__{nk}"
        
        # 1. BentukKataJA
        item['BentukKataJA'] = BENTUK_HARF_JA.get(b, b)
        
        # 2. SuratArtiJA
        surat_num = str(item.get('SURAT', ''))
        item['SuratArtiJA'] = JAPANESE_SURAHS.get(surat_num, item.get('SuratArtiEN', ''))
        
        # 3. ArtiKataJA & Grammar JA
        g_info = JAPANESE_HARF_GRAMMAR.get(g_key, {})
        item['ArtiKataJA'] = g_info.get('arti_ja', item.get('ArtiKataEN', item.get('Arti kata', '')))
        
        if 'Grammar' not in item:
            item['Grammar'] = {}
        if g_info.get('arti_ja'):
            item['Grammar']['arti_ja'] = g_info['arti_ja']
        if g_info.get('desc_ja'):
            item['Grammar']['desc_ja'] = g_info['desc_ja']
        if g_info.get('jenis_ja'):
            item['Grammar']['jenis_ja'] = g_info['jenis_ja']
            
        # 4. TeksArtiJA
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"
        teks_ja = ja_translations.get(v_key, item.get('TeksArtiEN', item.get('TeksArtiID', '')))
        item['TeksArtiJA'] = teks_ja

    # Write harf_data.json
    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Write harf_data.js
    with open(os.path.join(BASE_DIR, 'harf_data.js'), 'w', encoding='utf-8') as f:
        f.write("const HARF_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n\nif (typeof module !== 'undefined' && module.exports) {\n  module.exports = HARF_DATA;\n}\n")

    print(f"harf_data successfully updated with Japanese! (Total items: {len(data)})")


if __name__ == '__main__':
    enrich_dhamir_data()
    enrich_harf_data()
