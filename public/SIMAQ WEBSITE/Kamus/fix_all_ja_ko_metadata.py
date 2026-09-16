#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to properly format Japanese and Korean datasets and app.js mappings
with 100% key parity with Persian and Swahili datasets.
"""

import os
import sys
import json
import re

# 1. Read Japanese Surahs and Korean Surahs
from build_japanese_dataset import JAPANESE_SURAHS, BENTUK_KATA_JA, BENTUK_HARF_JA
from build_korean_dataset import KOREAN_SURAHS, BENTUK_KATA_KO, BENTUK_HARF_KO
from build_persian_dataset import PERSIAN_GRAMMAR, PERSIAN_HARF_GRAMMAR

# Define 76 Jamid Japanese Grammar
JAPANESE_GRAMMAR = {
    # 1. Dhamir
    '1. Dhamir__1a': {'arti_ja': '彼 (単数男性)', 'desc_ja': '彼（三人称単数男性主格分離代名詞）', 'jenis_ja': '主格分離代名詞'},
    '1. Dhamir__1b': {'arti_ja': '彼の / 彼を', 'desc_ja': '彼の／彼を（三人称単数男性接尾代名詞）', 'jenis_ja': '接尾代名詞'},
    '1. Dhamir__1c': {'arti_ja': '彼だけを', 'desc_ja': '彼だけを（三人称単数男性対格分離代名詞）', 'jenis_ja': '対格分離代名詞'},
    '1. Dhamir__2a': {'arti_ja': '彼ら二人', 'desc_ja': '彼ら二人（三人称双数主格分離代名詞）', 'jenis_ja': '主格分離代名詞（双数）'},
    '1. Dhamir__2b': {'arti_ja': '彼ら二人の / 二人を', 'desc_ja': '彼ら二人の／二人を（三人称双数接尾代名詞）', 'jenis_ja': '接尾代名詞（双数）'},
    '1. Dhamir__3a': {'arti_ja': '彼ら (複数男性)', 'desc_ja': '彼ら（三人称複数男性主格分離代名詞）', 'jenis_ja': '主格分離代名詞（複数男性）'},
    '1. Dhamir__3b': {'arti_ja': '彼らの / 彼らを', 'desc_ja': '彼らの／彼らを（三人称複数男性接尾代名詞）', 'jenis_ja': '接尾代名詞（複数男性）'},
    '1. Dhamir__3c': {'arti_ja': '彼らだけを', 'desc_ja': '彼らだけを（三人称複数男性対格分離代名詞）', 'jenis_ja': '対格分離代名詞（複数男性）'},
    '1. Dhamir__4a': {'arti_ja': '彼女 (単数女性)', 'desc_ja': '彼女（三人称単数女性主格分離代名詞）', 'jenis_ja': '主格分離代名詞（単数女性）'},
    '1. Dhamir__4b': {'arti_ja': '彼女の / 彼女を', 'desc_ja': '彼女の／彼女を（三人称単数女性接尾代名詞）', 'jenis_ja': '接尾代名詞（単数女性）'},
    '1. Dhamir__5a': {'arti_ja': '彼女たち (複数女性)', 'desc_ja': '彼女たち（三人称複数女性主格分離代名詞）', 'jenis_ja': '主格分離代名詞（複数女性）'},
    '1. Dhamir__5b': {'arti_ja': '彼女たちの / 彼女たちを', 'desc_ja': '彼女たちの／彼女たちを（三人称複数女性接尾代名詞）', 'jenis_ja': '接尾代名詞（複数女性）'},
    '1. Dhamir__6a': {'arti_ja': 'あなた (単数男性)', 'desc_ja': 'あなた（二人称単数男性主格分離代名詞）', 'jenis_ja': '主格分離代名詞（単数男性）'},
    '1. Dhamir__6b': {'arti_ja': 'あなたの / あなたを', 'desc_ja': 'あなたの／あなたを（二人称単数男性接尾代名詞）', 'jenis_ja': '接尾代名詞（単数男性）'},
    '1. Dhamir__6c': {'arti_ja': 'あなただけを', 'desc_ja': 'あなただけを（二人称単数男性対格分離代名詞）', 'jenis_ja': '対格分離代名詞（単数男性）'},
    '1. Dhamir__7a': {'arti_ja': 'あなた方二人', 'desc_ja': 'あなた方二人（二人称双数主格分離代名詞）', 'jenis_ja': '主格分離代名詞（双数）'},
    '1. Dhamir__7b': {'arti_ja': 'あなた方二人の', 'desc_ja': 'あなた方二人の／二人を（二人称双数接尾代名詞）', 'jenis_ja': '接尾代名詞（双数）'},
    '1. Dhamir__8a': {'arti_ja': 'あなた方 (複数男性)', 'desc_ja': 'あなた方（二人称複数男性主格分離代名詞）', 'jenis_ja': '主格分離代名詞（複数男性）'},
    '1. Dhamir__8b': {'arti_ja': 'あなた方の / あなた方を', 'desc_ja': 'あなた方の／あなた方を（二人称複数男性接尾代名詞）', 'jenis_ja': '接尾代名詞（複数男性）'},
    '1. Dhamir__8c': {'arti_ja': 'あなた方だけを', 'desc_ja': 'あなた方だけを（二人称複数男性対格分離代名詞）', 'jenis_ja': '対格分離代名詞（複数男性）'},
    '1. Dhamir__9b': {'arti_ja': 'あなたの / あなたを (女性)', 'desc_ja': 'あなたの／あなたを（二人称単数女性接尾代名詞）', 'jenis_ja': '接尾代名詞（単数女性）'},
    '1. Dhamir__11a': {'arti_ja': '私', 'desc_ja': '私（一人称単数主格分離代名詞）', 'jenis_ja': '主格分離代名詞（一人称単数）'},
    '1. Dhamir__11b': {'arti_ja': '私の / 私を', 'desc_ja': '私の／私を（一人称単数接尾代名詞）', 'jenis_ja': '接尾代名詞（一人称単数）'},
    '1. Dhamir__11c': {'arti_ja': '私だけを', 'desc_ja': '私だけを（一人称単数対格分離代名詞）', 'jenis_ja': '対格分離代名詞（一人称単数）'},
    '1. Dhamir__12a': {'arti_ja': '私たち', 'desc_ja': '私たち（一人称複数主格分離代名詞）', 'jenis_ja': '主格分離代名詞（一人称複数）'},
    '1. Dhamir__12b': {'arti_ja': '私たちの / 私たちを', 'desc_ja': '私たちの／私たちを（一人称複数接尾代名詞）', 'jenis_ja': '接尾代名詞（一人称複数）'},
    '1. Dhamir__12c': {'arti_ja': '私たちだけを', 'desc_ja': '私たちだけを（一人称複数対格分離代名詞）', 'jenis_ja': '対格分離代名詞（一人称複数）'},

    # 2. Mawshul
    '2. Mawshul__1': {'arti_ja': '〜するもの (無理性)', 'desc_ja': '非有理名詞に用いられる一般的な関係名詞（マー）', 'jenis_ja': '関係名詞（無理性）'},
    '2. Mawshul__2': {'arti_ja': '〜する者たち (複数男性)', 'desc_ja': '関係代名詞（複数男性・有理性）', 'jenis_ja': '関係名詞（特定）'},
    '2. Mawshul__3': {'arti_ja': '〜する者 (有理性)', 'desc_ja': '有理名詞に用いられる一般的な関係詞（マン）', 'jenis_ja': '関係名詞（有理性）'},
    '2. Mawshul__4': {'arti_ja': '〜する者 (単数男性)', 'desc_ja': '関係代名詞（単数男性）', 'jenis_ja': '関係名詞（特定）'},
    '2. Mawshul__5': {'arti_ja': 'どれ / どちらの', 'desc_ja': 'どちらの／どれ（関係名詞・疑問名詞）', 'jenis_ja': '関係名詞（格変化）'},
    '2. Mawshul__6': {'arti_ja': '〜する者 (単数女性)', 'desc_ja': '関係代名詞（単数女性）', 'jenis_ja': '関係名詞（特定）'},
    '2. Mawshul__7': {'arti_ja': '〜する者たち (複数女性・アッラーイー)', 'desc_ja': '関係代名詞（複数女性・アッラーイー）', 'jenis_ja': '関係名詞（特定）'},
    '2. Mawshul__8': {'arti_ja': '〜する者たち (複数女性・アッラーティー)', 'desc_ja': '関係代名詞（複数女性・アッラーティー）', 'jenis_ja': '関係名詞（特定）'},
    '2. Mawshul__9': {'arti_ja': '〜する二人 (双数男性)', 'desc_ja': '関係代名詞（双数男性主格）', 'jenis_ja': '関係名詞（双数）'},
    '2. Mawshul__10': {'arti_ja': 'どちらの女性', 'desc_ja': '関係代名詞（女性形）', 'jenis_ja': '関係名詞（女性）'},

    # 3. Istifham
    '3. Istifham__1': {'arti_ja': '何が？ / 何', 'desc_ja': '非有理存在や物事を尋ねる疑問詞（マー）', 'jenis_ja': '疑問名詞（無理性）'},
    '3. Istifham__2': {'arti_ja': 'どのように？', 'desc_ja': '状態や様態を尋ねる疑問詞（カイファ）', 'jenis_ja': '疑問副詞（様態）'},
    '3. Istifham__3': {'arti_ja': '誰が？ / 誰', 'desc_ja': '有理存在を尋ねる疑問詞（マン）', 'jenis_ja': '疑問名詞（有理性）'},
    '3. Istifham__4': {'arti_ja': 'どれ？ / どちら？', 'desc_ja': '選択を求める疑問詞（アイユ）', 'jenis_ja': '選択疑問詞'},
    '3. Istifham__5': {'arti_ja': 'どこから？ / どのように？', 'desc_ja': '場所・状態・出所を尋ねる疑問詞（アンナー）', 'jenis_ja': '疑問副詞（様態・場所）'},
    '3. Istifham__6': {'arti_ja': '一体何が？', 'desc_ja': '強い疑問を表す疑問詞（マーザー）', 'jenis_ja': '強調疑問詞'},
    '3. Istifham__7': {'arti_ja': 'いくつ？ / どれほど？', 'desc_ja': '数量や時間を尋ねる疑問詞（カム）', 'jenis_ja': '疑問副詞（数量）'},
    '3. Istifham__8': {'arti_ja': 'なぜ？ / 何のために', 'desc_ja': '理由や目的を尋ねる疑問詞（リマ）', 'jenis_ja': '前置詞＋疑問詞'},
    '3. Istifham__9': {'arti_ja': 'どこに？', 'desc_ja': '場所を尋ねる疑問詞（アイナ）', 'jenis_ja': '疑問副詞（場所）'},
    '3. Istifham__10': {'arti_ja': 'いつ？ (審判の日)', 'desc_ja': '重大な時（終末等）を尋ねる疑問詞（アイヤーナ）', 'jenis_ja': '疑問副詞（重大な時）'},

    # 4. Syarath
    '4. Syarath__1': {'arti_ja': '誰でも〜する者は', 'desc_ja': '有理名詞に用いられる条件名詞（マン）', 'jenis_ja': '条件名詞（有理性）'},
    '4. Syarath__2': {'arti_ja': '何であれ〜するものは', 'desc_ja': '非有理名詞に用いられる条件名詞（マー）', 'jenis_ja': '条件名詞（無理性）'},
    '4. Syarath__3': {'arti_ja': '〜する時はいつでも', 'desc_ja': '時間を表す条件名詞（イズマー／クルラマー）', 'jenis_ja': '時間条件名詞'},
    '4. Syarath__4': {'arti_ja': 'いかなるものであれ', 'desc_ja': '包括的選択を表す条件名詞（アイヤン）', 'jenis_ja': '選択条件名詞'},
    '4. Syarath__5': {'arti_ja': 'その二つのどちらであれ', 'desc_ja': '強調された二者択一条件名詞（アイヤマ）', 'jenis_ja': '強調条件名詞'},

    # 5. Isyarah
    '5. Isyarah__1': {'arti_ja': 'これ / あれ (単数男性)', 'desc_ja': '指示代名詞（単数男性）', 'jenis_ja': '指示名詞（単数男性）'},
    '5. Isyarah__2': {'arti_ja': 'これら / あれら (複数)', 'desc_ja': '指示代名詞（複数）', 'jenis_ja': '指示名詞（複数）'},
    '5. Isyarah__3': {'arti_ja': 'これ (単数女性)', 'desc_ja': '近称指示代名詞（単数女性）', 'jenis_ja': '指示名詞（単数女性）'},
    '5. Isyarah__4': {'arti_ja': 'あれ (単数女性)', 'desc_ja': '遠称指示代名詞（単数女性）', 'jenis_ja': '遠称指示名詞（女性）'},
    '5. Isyarah__5': {'arti_ja': 'ここに', 'desc_ja': '近称の場所を表す指示副詞（ハーハナ）', 'jenis_ja': '場所指示副詞（近称）'},
    '5. Isyarah__6': {'arti_ja': 'あそこに / そこに', 'desc_ja': '遠称の場所を表す指示副詞（フナーリカ）', 'jenis_ja': '場所指示副詞（遠称）'},
    '5. Isyarah__7': {'arti_ja': 'これら二人 (男性)', 'desc_ja': '双数男性指示代名詞（ザーニカ）', 'jenis_ja': '指示名詞（双数男性）'},
    '5. Isyarah__8': {'arti_ja': 'これら二人 (女性)', 'desc_ja': '双数女性指示代名詞（ターニカ）', 'jenis_ja': '指示名詞（双数女性）'},

    # 6. Isim Fi'il
    "6. Isim Fi'il__1": {'arti_ja': '神に栄光あれ！ (スブハーナ)', 'desc_ja': '讃美・賛美の絶対対格名詞', 'jenis_ja': '動詞性讃美名詞'},
    "6. Isim Fi'il__2": {'arti_ja': 'さあ持っておいで！', 'desc_ja': '命令を表す動詞性名詞（ハートゥー）', 'jenis_ja': '命令動詞性名詞'},
    "6. Isim Fi'il__3": {'arti_ja': 'ああ！ (うんざりだ)', 'desc_ja': '不快・嫌悪を表す現在動詞性名詞（ウッフ）', 'jenis_ja': '現在動詞性名詞'},
    "6. Isim Fi'il__4": {'arti_ja': '神の御加護を！', 'desc_ja': '保護・避難を求める動詞性名詞（マアーザッラー）', 'jenis_ja': '祈願動詞性名詞'},
    "6. Isim Fi'il__5": {'arti_ja': 'さあ来なさい！', 'desc_ja': '促し・集合を表す動詞性名詞（ハルンマ）', 'jenis_ja': '命令動詞性名詞'},
    "6. Isim Fi'il__6": {'arti_ja': 'なんと遠いことか！', 'desc_ja': '距離の隔たりを表す過去動詞性名詞（ハイハータ）', 'jenis_ja': '過去動詞性名詞'},
    "6. Isim Fi'il__7": {'arti_ja': 'さあ、これを取って読め！', 'desc_ja': '命令を表す動詞性名詞（ハーウム）', 'jenis_ja': '命令動詞性名詞'},
    "6. Isim Fi'il__8": {'arti_ja': 'さあ、おいで！', 'desc_ja': '呼びかけ・促しを表す動詞性名詞（ハイタ・ラク）', 'jenis_ja': '命令動詞性名詞'},

    # 7. Fi'il Jamid
    "7. Fi'il Jamid__1": {'arti_ja': '〜ではない (否定)', 'desc_ja': '否定を表す不完全固着動詞（ライサ）', 'jenis_ja': '不完全固着動詞（否定）'},
    "7. Fi'il Jamid__2": {'arti_ja': '〜かもしれない (希望)', 'desc_ja': '希望・期待を表す固着動詞（アサー）', 'jenis_ja': '希望固着動詞'},
    "7. Fi'il Jamid__3": {'arti_ja': 'なんと良いことか！ (賞賛)', 'desc_ja': '賞賛を表す固着動詞（ニウマ）', 'jenis_ja': '賞賛固着動詞'},
    "7. Fi'il Jamid__4": {'arti_ja': 'なんと悪いことか！ (非難)', 'desc_ja': '非難を表す固着動詞（ビウサ）', 'jenis_ja': '非難固着動詞'},
    "7. Fi'il Jamid__5": {'arti_ja': 'なんと悪いことか！ (複合)', 'desc_ja': '非難を表す複合固着動詞（ビウサマー）', 'jenis_ja': '複合非難動詞'},
    "7. Fi'il Jamid__6": {'arti_ja': '〜し始めた (開始)', 'desc_ja': '開始を表す固着動詞（タフィカ）', 'jenis_ja': '開始動詞'},
    "7. Fi'il Jamid__7": {'arti_ja': '神よ、お許しください！', 'desc_ja': '除外・神聖化の固着動詞（ハーシャ・リッラー）', 'jenis_ja': '神聖化固着動詞'},
    "7. Fi'il Jamid__8": {'arti_ja': 'なんと良い教訓か！', 'desc_ja': '賞賛を表す複合固着動詞（ニインマー）', 'jenis_ja': '複合賞賛動詞'}
}

# Define 52 Harf Japanese Grammar
JAPANESE_HARF_GRAMMAR = {
    # 1. Harf Nafyi
    "1. Harf Nafyi__1": {"arti_ja": "〜ではない (否定・ラー)", "desc_ja": "絶対否定小辞（ラー）", "jenis_ja": "否定小辞"},
    "1. Harf Nafyi__2": {"arti_ja": "〜ではない (否定・マー)", "desc_ja": "一般的否定小辞（マー）", "jenis_ja": "否定小辞"},
    "1. Harf Nafyi__3": {"arti_ja": "〜にほかならない (イン)", "desc_ja": "除外を伴う否定小辞（イン）", "jenis_ja": "否定小辞"},
    "1. Harf Nafyi__4": {"arti_ja": "〜であろうか？ (反語否定)", "desc_ja": "否定の意味を含む疑問詞（ハル）", "jenis_ja": "反語否定疑問詞"},
    "1. Harf Nafyi__5": {"arti_ja": "逃げる時ではない", "desc_ja": "時を表す名詞に付く否定小辞（ラアタ）", "jenis_ja": "否定小辞"},
    "1. Harf Nafyi__6": {"arti_ja": "真理のほかに何があろうか", "desc_ja": "否定を含む疑問詞（マーザー）", "jenis_ja": "反語否定疑問詞"},

    # 2. Harf Tahqiq Taswif
    "2. Harf Tahqiq Taswif__7": {"arti_ja": "確かに〜した (確証のカド)", "desc_ja": "過去形と共に確証を表す小辞（カド）", "jenis_ja": "確証小辞"},
    "2. Harf Tahqiq Taswif__8": {"arti_ja": "いずれ〜するであろう", "desc_ja": "未来を表す小辞（サウファ）", "jenis_ja": "未来小辞"},

    # 3. Harf Syarat
    "3. Harf Syarat__9": {"arti_ja": "もし〜ならば (ロウ)", "desc_ja": "反事実的条件小辞（ロウ）", "jenis_ja": "条件小辞"},
    "3. Harf Syarat__10": {"arti_ja": "もし〜がなかったならば", "desc_ja": "存在の否定を条件とする小辞（ロウラー）", "jenis_ja": "留保条件小辞"},
    "3. Harf Syarat__11": {"arti_ja": "たとえ〜であっても", "desc_ja": "譲歩的条件小辞（ロウ）", "jenis_ja": "譲歩条件小辞"},
    "3. Harf Syarat__12": {"arti_ja": "もし〜ならば (イムマー)", "desc_ja": "強調条件小辞（イン＋マー）", "jenis_ja": "強調条件小辞"},
    "3. Harf Syarat__13": {"arti_ja": "いかなる徴であれ", "desc_ja": "包括的条件名詞（マフマー）", "jenis_ja": "包括条件名詞"},

    # 4. Harf Mashdariyah
    "4. Harf Mashdariyah__14": {"arti_ja": "〜である限り", "desc_ja": "時間を表す名詞化小辞（マー）", "jenis_ja": "時間名詞化小辞"},
    "4. Harf Mashdariyah__15": {"arti_ja": "〜しないように", "desc_ja": "否定を伴う名詞化小辞（アン＋ラー）", "jenis_ja": "名詞化否定小辞"},
    "4. Harf Mashdariyah__16": {"arti_ja": "〜ということ (アン)", "desc_ja": "動詞を名詞句化する小辞（アン）", "jenis_ja": "名詞化小辞"},
    "4. Harf Mashdariyah__17": {"arti_ja": "〜することを願う", "desc_ja": "願望の名詞化小辞（ロウ）", "jenis_ja": "願望名詞化小辞"},
    "4. Harf Mashdariyah__18": {"arti_ja": "〜しないこと", "desc_ja": "禁止を伴う名詞化小辞（アン＋ラー）", "jenis_ja": "名詞化禁止小辞"},
    "4. Harf Mashdariyah__19": {"arti_ja": "〜であること", "desc_ja": "事実の名詞化小辞（アン短縮形）", "jenis_ja": "名詞化小辞"},

    # 5. Harf Zaidah
    "5. Harf Zaidah__20": {"arti_ja": "〜のように (強調)", "desc_ja": "比喩の接頭辞＋強調添え字（カ＋マー）", "jenis_ja": "強調添え字"},
    "5. Harf Zaidah__21": {"arti_ja": "たとえ蚊のようなものであれ", "desc_ja": "漠然・強調の添え字（マー）", "jenis_ja": "強調添え字"},
    "5. Harf Zaidah__22": {"arti_ja": "我は誓う", "desc_ja": "誓約を強める添え字（ラー）", "jenis_ja": "誓約強調添え字"},
    "5. Harf Zaidah__23": {"arti_ja": "神の慈悲によって", "desc_ja": "前置詞に伴う強調添え字（ビ＋マー）", "jenis_ja": "前置詞強調添え字"},
    "5. Harf Zaidah__24": {"arti_ja": "吉報をもたらす者が来た時", "desc_ja": "時間接続詞に伴う添え字（アン）", "jenis_ja": "時間強調添え字"},

    # 6. Harf Istifham
    "6. Harf Istifham__25": {"arti_ja": "〜か？ (疑問のハル)", "desc_ja": "質問・確認を表す疑問小辞（ハル）", "jenis_ja": "疑問小辞"},

    # 7. Harf Jawab
    "7. Harf Jawab__26": {"arti_ja": "その時には / ならば", "desc_ja": "応答・帰結を表す小辞（イザン）", "jenis_ja": "応答帰結小辞"},
    "7. Harf Jawab__27": {"arti_ja": "いや / その通りです", "desc_ja": "否定に対する肯定応答詞（バラー）", "jenis_ja": "肯定応答小辞"},
    "7. Harf Jawab__28": {"arti_ja": "はい / その通り", "desc_ja": "肯定応答詞（ナアム）", "jenis_ja": "肯定応答小辞"},
    "7. Harf Jawab__29": {"arti_ja": "そうだ！主にかけて", "desc_ja": "誓いを伴う肯定応答詞（イー）", "jenis_ja": "誓約応答小辞"},

    # 8. Harf Ibtida'
    "8. Harf Ibtida'__30": {"arti_ja": "〜に至るまで", "desc_ja": "文頭・発端を表す小辞（ハッター）", "jenis_ja": "発端小辞"},

    # 9. Harf Tafshil
    "9. Harf Tafshil__31": {"arti_ja": "〜に関しては", "desc_ja": "詳細化・主題提示小辞（アンマー）", "jenis_ja": "詳細化小辞"},

    # 10. Harf Mufaja'ah
    "10. Harf Mufaja'ah__32": {"arti_ja": "たちまち〜となった", "desc_ja": "突発・不意の出来事を表す小辞（イザー）", "jenis_ja": "突発事象小辞"},

    # 11. Harf Mufassirah
    "11. Harf Mufassirah__33": {"arti_ja": "すなわち〜と", "desc_ja": "解説・説明を導く小辞（アン）", "jenis_ja": "説明小辞"},

    # 12. Harf Istiftahiyah
    "12. Harf Istiftahiyah__34": {"arti_ja": "見よ！ / 心せよ", "desc_ja": "注意喚起・開始小辞（アラー）", "jenis_ja": "注意喚起小辞"},

    # 13. Harf Rada'
    "13. Harf Rada'__35": {"arti_ja": "断じて否！", "desc_ja": "戒め・強い拒絶の小辞（カッラー）", "jenis_ja": "戒め・拒絶小辞"},

    # 14. Harf Ta'ajjub
    "14. Harf Ta'ajjub__36": {"arti_ja": "なんと忍耐強いことか！", "desc_ja": "感嘆・驚きを表す小辞（マー）", "jenis_ja": "感嘆小辞"},

    # 15. Harf Fariqah
    "15. Harf Fariqah__37": {"arti_ja": "確かに / まさに", "desc_ja": "肯定を区別する強調ラーム（イン短縮形に伴う）", "jenis_ja": "区別強調ラーム"},

    # 16. Harf Mauthi'ah
    "16. Harf Mauthi'ah__38": {"arti_ja": "もし〜ならば誓って", "desc_ja": "誓約を導く条件ラーム（ラ・イン）", "jenis_ja": "誓約前置ラーム"},

    # 17. Harf Mabany
    "17. Harf Mabany__39": {"arti_ja": "ハー・ミーム", "desc_ja": "章冒頭の神秘的独立文字（حم）", "jenis_ja": "独立文字 (ムカッタアート)"},
    "17. Harf Mabany__40": {"arti_ja": "アリフ・ラーム・ミーム", "desc_ja": "章冒頭の神秘的独立文字（الم）", "jenis_ja": "独立文字 (ムカッタアート)"},
    "17. Harf Mabany__41": {"arti_ja": "アリフ・ラーム・ラー", "desc_ja": "章冒頭の神秘的独立文字（الر）", "jenis_ja": "独立文字 (ムカッタアート)"},
    "17. Harf Mabany__42": {"arti_ja": "ター・スィーン・ミーム", "desc_ja": "章冒頭の神秘的独立文字（طسم）", "jenis_ja": "独立文字 (ムカッタアート)"},
    "17. Harf Mabany__43": {"arti_ja": "アリフ・ラーム・ミーム・ラー", "desc_ja": "章冒頭の神秘的独立文字（المر）", "jenis_ja": "独立文字 (ムカッタアート)"},
    "17. Harf Mabany__44": {"arti_ja": "アリフ・ラーム・ミーム・サード", "desc_ja": "章冒頭の神秘的独立文字（المص）", "jenis_ja": "独立文字 (ムカッタアート)"},
    "17. Harf Mabany__45": {"arti_ja": "サード", "desc_ja": "章冒頭の神秘的独立文字（ص）", "jenis_ja": "独立文字 (ムカッタアート)"},
    "17. Harf Mabany__46": {"arti_ja": "ター・スィーン", "desc_ja": "章冒頭の神秘的独立文字（طس）", "jenis_ja": "独立文字 (ムカッタアート)"},
    "17. Harf Mabany__47": {"arti_ja": "ター・ハー", "desc_ja": "章冒頭の神秘的独立文字（طه）", "jenis_ja": "独立文字 (ムカッタアート)"},
    "17. Harf Mabany__48": {"arti_ja": "アイン・スィーン・カーフ", "desc_ja": "章冒頭の神秘的独立文字（عسق）", "jenis_ja": "独立文字 (ムカッタアート)"},
    "17. Harf Mabany__49": {"arti_ja": "カーフ", "desc_ja": "章冒頭の神秘的独立文字（ق）", "jenis_ja": "独立文字 (ムカッタアート)"},
    "17. Harf Mabany__50": {"arti_ja": "カーフ・ハー・ヤー・アイン・サード", "desc_ja": "章冒頭の神秘的独立文字（كهيعص）", "jenis_ja": "独立文字 (ムカッタアート)"},
    "17. Harf Mabany__51": {"arti_ja": "ヌーン", "desc_ja": "章冒頭の神秘的独立文字（ن）", "jenis_ja": "独立文字 (ムカッタアート)"},
    "17. Harf Mabany__52": {"arti_ja": "ヤー・スィーン", "desc_ja": "章冒頭の神秘的独立文字（يس）", "jenis_ja": "独立文字 (ムカッタアート)"}
}

# Define 76 Jamid Korean Grammar
KOREAN_GRAMMAR = {
    # 1. Dhamir
    '1. Dhamir__1a': {'arti_ko': '그 (남성 단수)', 'desc_ko': '그 (3인칭 남성 단수 주격 분리대명사)', 'jenis_ko': '주격 분리대명사'},
    '1. Dhamir__1b': {'arti_ko': '그의 / 그를', 'desc_ko': '그의 / 그를 (3인칭 남성 단수 접미대명사)', 'jenis_ko': '접미대명사'},
    '1. Dhamir__1c': {'arti_ko': '오직 그분만을', 'desc_ko': '오직 그를 (3인칭 남성 단수 목적격 분리대명사)', 'jenis_ko': '목적격 분리대명사'},
    '1. Dhamir__2a': {'arti_ko': '그들 두 사람', 'desc_ko': '그들 두 사람 (3인칭 쌍수 주격 분리대명사)', 'jenis_ko': '주격 분리대명사 (쌍수)'},
    '1. Dhamir__2b': {'arti_ko': '그들 두 사람의 / 두 사람을', 'desc_ko': '그들 둘의 / 둘을 (3인칭 쌍수 접미대명사)', 'jenis_ko': '접미대명사 (쌍수)'},
    '1. Dhamir__3a': {'arti_ko': '그들 (남성 복수)', 'desc_ko': '그들 (3인칭 남성 복수 주격 분리대명사)', 'jenis_ko': '주격 분리대명사 (남성 복수)'},
    '1. Dhamir__3b': {'arti_ko': '그들의 / 그들을', 'desc_ko': '그들의 / 그들을 (3인칭 남성 복수 접미대명사)', 'jenis_ko': '접미대명사 (남성 복수)'},
    '1. Dhamir__3c': {'arti_ko': '오직 그들만을', 'desc_ko': '오직 그들을 (3인칭 남성 복수 목적격 분리대명사)', 'jenis_ko': '목적격 분리대명사 (남성 복수)'},
    '1. Dhamir__4a': {'arti_ko': '그녀 (여성 단수)', 'desc_ko': '그녀 (3인칭 여성 단수 주격 분리대명사)', 'jenis_ko': '주격 분리대명사 (여성 단수)'},
    '1. Dhamir__4b': {'arti_ko': '그녀의 / 그녀를', 'desc_ko': '그녀의 / 그녀를 (3인칭 여성 단수 접미대명사)', 'jenis_ko': '접미대명사 (여성 단수)'},
    '1. Dhamir__5a': {'arti_ko': '그녀들 (여성 복수)', 'desc_ko': '그녀들 (3인칭 여성 복수 주격 분리대명사)', 'jenis_ko': '주격 분리대명사 (여성 복수)'},
    '1. Dhamir__5b': {'arti_ko': '그녀들의 / 그녀들을', 'desc_ko': '그녀들의 / 그녀들을 (3인칭 여성 복수 접미대명사)', 'jenis_ko': '접미대명사 (여성 복수)'},
    '1. Dhamir__6a': {'arti_ko': '당신 / 너 (남성 단수)', 'desc_ko': '너 (2인칭 남성 단수 주격 분리대명사)', 'jenis_ko': '주격 분리대명사 (남성 단수)'},
    '1. Dhamir__6b': {'arti_ko': '당신의 / 너를', 'desc_ko': '너의 / 너를 (2인칭 남성 단수 접미대명사)', 'jenis_ko': '접미대명사 (남성 단수)'},
    '1. Dhamir__6c': {'arti_ko': '오직 당신만을', 'desc_ko': '오직 너를 (2인칭 남성 단수 목적격 분리대명사)', 'jenis_ko': '목적격 분리대명사 (남성 단수)'},
    '1. Dhamir__7a': {'arti_ko': '당신들 두 사람', 'desc_ko': '너희 둘 (2인칭 쌍수 주격 분리대명사)', 'jenis_ko': '주격 분리대명사 (쌍수)'},
    '1. Dhamir__7b': {'arti_ko': '당신들 두 사람의', 'desc_ko': '너희 둘의 / 둘을 (2인칭 쌍수 접미대명사)', 'jenis_ko': '접미대명사 (쌍수)'},
    '1. Dhamir__8a': {'arti_ko': '당신들 / 너희들 (남성 복수)', 'desc_ko': '너희들 (2인칭 남성 복수 주격 분리대명사)', 'jenis_ko': '주격 분리대명사 (남성 복수)'},
    '1. Dhamir__8b': {'arti_ko': '당신들의 / 너희들을', 'desc_ko': '너희들의 / 너희들을 (2인칭 남성 복수 접미대명사)', 'jenis_ko': '접미대명사 (남성 복수)'},
    '1. Dhamir__8c': {'arti_ko': '오직 당신들만을', 'desc_ko': '오직 너희들을 (2인칭 남성 복수 목적격 분리대명사)', 'jenis_ko': '목적격 분리대명사 (남성 복수)'},
    '1. Dhamir__9b': {'arti_ko': '당신의 / 너를 (여성)', 'desc_ko': '너의 / 너를 (2인칭 여성 단수 접미대명사)', 'jenis_ko': '접미대명사 (여성 단수)'},
    '1. Dhamir__11a': {'arti_ko': '나 / 저', 'desc_ko': '나 (1인칭 단수 주격 분리대명사)', 'jenis_ko': '주격 분리대명사 (1인칭 단수)'},
    '1. Dhamir__11b': {'arti_ko': '나의 / 나를', 'desc_ko': '나의 / 나를 (1인칭 단수 접미대명사)', 'jenis_ko': '접미대명사 (1인칭 단수)'},
    '1. Dhamir__11c': {'arti_ko': '오직 나만을', 'desc_ko': '오직 나를 (1인칭 단수 목적격 분리대명사)', 'jenis_ko': '목적격 분리대명사 (1인칭 단수)'},
    '1. Dhamir__12a': {'arti_ko': '우리', 'desc_ko': '우리 (1인칭 복수 주격 분리대명사)', 'jenis_ko': '주격 분리대명사 (1인칭 복수)'},
    '1. Dhamir__12b': {'arti_ko': '우리의 / 우리를', 'desc_ko': '우리의 / 우리를 (1인칭 복수 접미대명사)', 'jenis_ko': '접미대명사 (1인칭 복수)'},
    '1. Dhamir__12c': {'arti_ko': '오직 우리만을', 'desc_ko': '오직 우리를 (1인칭 복수 목적격 분리대명사)', 'jenis_ko': '목적격 분리대명사 (1인칭 복수)'},

    # 2. Mawshul
    '2. Mawshul__1': {'arti_ko': '~하는 것 (무이성)', 'desc_ko': '무이성 명사에 쓰이는 일반 관계사 (마)', 'jenis_ko': '관계명사 (무이성)'},
    '2. Mawshul__2': {'arti_ko': '~하는 자들 (남성 복수)', 'desc_ko': '관계대명사 (남성 복수 유이성)', 'jenis_ko': '한정 관계대명사'},
    '2. Mawshul__3': {'arti_ko': '~하는 자 (유이성)', 'desc_ko': '유이성 명사에 쓰이는 일반 관계사 (만)', 'jenis_ko': '관계명사 (유이성)'},
    '2. Mawshul__4': {'arti_ko': '~하는 자 (남성 단수)', 'desc_ko': '관계대명사 (남성 단수)', 'jenis_ko': '한정 관계대명사'},
    '2. Mawshul__5': {'arti_ko': '어느 쪽의 / 어느 것', 'desc_ko': '어느 쪽의 (관계사 및 의문사)', 'jenis_ko': '격변화 관계명사'},
    '2. Mawshul__6': {'arti_ko': '~하는 자 (여성 단수)', 'desc_ko': '관계대명사 (여성 단수)', 'jenis_ko': '한정 관계대명사'},
    '2. Mawshul__7': {'arti_ko': '~하는 자들 (여성 복수 - 알라이)', 'desc_ko': '관계대명사 (여성 복수 - 알라이)', 'jenis_ko': '한정 관계대명사'},
    '2. Mawshul__8': {'arti_ko': '~하는 자들 (여성 복수 - 알라티)', 'desc_ko': '관계대명사 (여성 복수 - 알라티)', 'jenis_ko': '한정 관계대명사'},
    '2. Mawshul__9': {'arti_ko': '~하는 두 사람 (남성 쌍수)', 'desc_ko': '관계대명사 (남성 쌍수 주격)', 'jenis_ko': '쌍수 관계대명사'},
    '2. Mawshul__10': {'arti_ko': '어느 여성', 'desc_ko': '관계대명사 (여성형)', 'jenis_ko': '여성 관계대명사'},

    # 3. Istifham
    '3. Istifham__1': {'arti_ko': '무엇이? / 무엇', 'desc_ko': '사물이나 행위를 묻는 의문사 (마)', 'jenis_ko': '의문명사 (사물)'},
    '3. Istifham__2': {'arti_ko': '어떻게? (상태)', 'desc_ko': '상태나 양태를 묻는 의문사 (카이파)', 'jenis_ko': '의문부사 (상태)'},
    '3. Istifham__3': {'arti_ko': '누가? / 누구', 'desc_ko': '인물이나 유이성 존재를 묻는 의문사 (만)', 'jenis_ko': '의문명사 (인물)'},
    '3. Istifham__4': {'arti_ko': '어느 것? / 어느 쪽', 'desc_ko': '선택을 묻는 의문사 (아이유)', 'jenis_ko': '선택 의문사'},
    '3. Istifham__5': {'arti_ko': '어디서부터? / 어떻게?', 'desc_ko': '장소·방법·상태를 묻는 의문사 (안나)', 'jenis_ko': '의문부사 (양태/장소)'},
    '3. Istifham__6': {'arti_ko': '도대체 무엇이?', 'desc_ko': '강한 의문을 나타내는 복합 의문사 (마다)', 'jenis_ko': '강조 복합의문사'},
    '3. Istifham__7': {'arti_ko': '얼마나? / 몇 개', 'desc_ko': '수량이나 기간을 묻는 의문사 (캄)', 'jenis_ko': '의문부사 (수량)'},
    '3. Istifham__8': {'arti_ko': '왜? / 무엇을 위해', 'desc_ko': '이유나 원인을 묻는 의문사 (리마)', 'jenis_ko': '전치사+의문사'},
    '3. Istifham__9': {'arti_ko': '어디에? / 어디서', 'desc_ko': '장소를 묻는 의문사 (아이나)', 'jenis_ko': '의문부사 (장소)'},
    '3. Istifham__10': {'arti_ko': '언제? (심판의 날)', 'desc_ko': '심판의 날 등 중대한 때를 묻는 의문사 (아야나)', 'jenis_ko': '의문부사 (중대 시점)'},

    # 4. Syarath
    '4. Syarath__1': {'arti_ko': '누구든지 ~하는 자는', 'desc_ko': '유이성 명사에 쓰이는 조건명사 (만)', 'jenis_ko': '조건명사 (유이성)'},
    '4. Syarath__2': {'arti_ko': '무엇이든 ~하는 것은', 'desc_ko': '무이성 명사에 쓰이는 조건명사 (마)', 'jenis_ko': '조건명사 (무이성)'},
    '4. Syarath__3': {'arti_ko': '~할 때마다 / 언제든', 'desc_ko': '시간을 나타내는 조건명사 (이즈마 / 쿨라마)', 'jenis_ko': '시간 조건명사'},
    '4. Syarath__4': {'arti_ko': '어느 것이든 간에', 'desc_ko': '포괄적 선택을 나타내는 조건명사 (아이얀)', 'jenis_ko': '선택 조건명사'},
    '4. Syarath__5': {'arti_ko': '그 둘 중 어느 것이든', 'desc_ko': '강조된 양자택일 조건명사 (아이야마)', 'jenis_ko': '강조 조건명사'},

    # 5. Isyarah
    '5. Isyarah__1': {'arti_ko': '이것 / 저것 (남성 단수)', 'desc_ko': '지시대명사 (남성 단수)', 'jenis_ko': '지시명사 (남성 단수)'},
    '5. Isyarah__2': {'arti_ko': '이들 / 저들 (복수)', 'desc_ko': '지시대명사 (복수)', 'jenis_ko': '지시명사 (복수)'},
    '5. Isyarah__3': {'arti_ko': '이것 (여성 단수)', 'desc_ko': '근칭 지시대명사 (여성 단수)', 'jenis_ko': '지시명사 (여성 단수)'},
    '5. Isyarah__4': {'arti_ko': '저것 (여성 단수)', 'desc_ko': '원칭 지시대명사 (여성 단수)', 'jenis_ko': '원칭 지시명사 (여성)'},
    '5. Isyarah__5': {'arti_ko': '여기에', 'desc_ko': '근칭 장소를 나타내는 지시부사 (하후나)', 'jenis_ko': '장소 지시부사 (근칭)'},
    '5. Isyarah__6': {'arti_ko': '저기에 / 그곳에', 'desc_ko': '원칭 장소를 나타내는 지시부사 (후날리카)', 'jenis_ko': '장소 지시부사 (원칭)'},
    '5. Isyarah__7': {'arti_ko': '이 두 사람 (남성 쌍수)', 'desc_ko': '쌍수 남성 지시대명사 (다니카)', 'jenis_ko': '지시명사 (남성 쌍수)'},
    '5. Isyarah__8': {'arti_ko': '이 두 사람 (여성 쌍수)', 'desc_ko': '쌍수 여성 지시대명사 (타니카)', 'jenis_ko': '지시명사 (여성 쌍수)'},

    # 6. Isim Fi'il
    "6. Isim Fi'il__1": {'arti_ko': '하나님께 영광이! (수브하나)', 'desc_ko': '찬미·칭송의 절대목적격 명사', 'jenis_ko': '동사성 찬미명사'},
    "6. Isim Fi'il__2": {'arti_ko': '자, 가져오라!', 'desc_ko': '명령을 나타내는 동사성 명사 (하투)', 'jenis_ko': '명령 동사성 명사'},
    "6. Isim Fi'il__3": {'arti_ko': '아아! (지겹도다)', 'desc_ko': '불쾌감과 혐오를 나타내는 현재 동사성 명사 (우프)', 'jenis_ko': '현재 동사성 명사'},
    "6. Isim Fi'il__4": {'arti_ko': '하나님의 보호를!', 'desc_ko': '구원과 보호를 구하는 동사성 명사 (마아달라)', 'jenis_ko': '기도 동사성 명사'},
    "6. Isim Fi'il__5": {'arti_ko': '자, 오라!', 'desc_ko': '재촉과 모임을 나타내는 동사성 명사 (할룸마)', 'jenis_ko': '명령 동사성 명사'},
    "6. Isim Fi'il__6": {'arti_ko': '얼마나 아득히 먼가!', 'desc_ko': '거리의 아득함을 나타내는 과거 동사성 명사 (하이하타)', 'jenis_ko': '과거 동사성 명사'},
    "6. Isim Fi'il__7": {'arti_ko': '자, 이것을 받아 읽으라!', 'desc_ko': '명령을 나타내는 동사성 명사 (하움)', 'jenis_ko': '명령 동사성 명사'},
    "6. Isim Fi'il__8": {'arti_ko': '자, 이리로 오라!', 'desc_ko': '부름과 재촉의 동사성 명사 (하이라 라크)', 'jenis_ko': '명령 동사성 명사'},

    # 7. Fi'il Jamid
    "7. Fi'il Jamid__1": {'arti_ko': '~가 아니다 (부정)', 'desc_ko': '부정을 나타내는 불완전 불변동사 (라이사)', 'jenis_ko': '불완전 불변동사 (부정)'},
    "7. Fi'il Jamid__2": {'arti_ko': '~일지도 모른다 (희망)', 'desc_ko': '희망과 기대를 나타내는 불변동사 (아사)', 'jenis_ko': '희망 불변동사'},
    "7. Fi'il Jamid__3": {'arti_ko': '얼마나 훌륭한가! (찬양)', 'desc_ko': '칭찬과 찬양을 나타내는 불변동사 (니으마)', 'jenis_ko': '찬양 불변동사'},
    "7. Fi'il Jamid__4": {'arti_ko': '얼마나 나쁜가! (비난)', 'desc_ko': '비난과 질책의 불변동사 (비으사)', 'jenis_ko': '비난 불변동사'},
    "7. Fi'il Jamid__5": {'arti_ko': '얼마나 사악한 것인가!', 'desc_ko': '비난을 나타내는 복합 불변동사 (비으사마)', 'jenis_ko': '복합 비난동사'},
    "7. Fi'il Jamid__6": {'arti_ko': '~하기 시작했다 (착수)', 'desc_ko': '시작을 나타내는 불변동사 (타피카)', 'jenis_ko': '착수동사'},
    "7. Fi'il Jamid__7": {'arti_ko': '하나님께 결백하도다!', 'desc_ko': '제외 및 신성화의 불변동사 (하샤 릴라)', 'jenis_ko': '신성화 불변동사'},
    "7. Fi'il Jamid__8": {'arti_ko': '얼마나 훌륭한 교훈인가!', 'desc_ko': '찬양을 나타내는 복합 불변동사 (니임마)', 'jenis_ko': '복합 찬양동사'}
}

# Define 52 Harf Korean Grammar
KOREAN_HARF_GRAMMAR = {
    # 1. Harf Nafyi
    "1. Harf Nafyi__1": {"arti_ko": "~하지 않는다 (부정의 라)", "desc_ko": "절대 부정 소사 (라)", "jenis_ko": "부정 소사"},
    "1. Harf Nafyi__2": {"arti_ko": "~가 아니다 (부정의 마)", "desc_ko": "일반적 부정 소사 (마)", "jenis_ko": "부정 소사"},
    "1. Harf Nafyi__3": {"arti_ko": "~에 지나지 않는다 (인)", "desc_ko": "예외를 수반하는 부정 소사 (인)", "jenis_ko": "부정 소사"},
    "1. Harf Nafyi__4": {"arti_ko": "~하겠는가? (반어적 부정)", "desc_ko": "부정의 의미를 내포한 의문사 (할)", "jenis_ko": "반어 부정 의문사"},
    "1. Harf Nafyi__5": {"arti_ko": "도망칠 때가 아니다", "desc_ko": "시간 명사에 결합하는 부정 소사 (라아타)", "jenis_ko": "부정 소사"},
    "1. Harf Nafyi__6": {"arti_ko": "진리 외에 무엇이 있겠는가", "desc_ko": "부정을 내포한 의문사 (마다)", "jenis_ko": "반어 부정 의문사"},

    # 2. Harf Tahqiq Taswif
    "2. Harf Tahqiq Taswif__7": {"arti_ko": "과연 ~하였다 (확증의 카드)", "desc_ko": "과거형과 함께 확증을 나타내는 소사 (카드)", "jenis_ko": "확증 소사"},
    "2. Harf Tahqiq Taswif__8": {"arti_ko": "머지않아 ~하리라", "desc_ko": "미래를 나타내는 소사 (사우파)", "jenis_ko": "미래 소사"},

    # 3. Harf Syarat
    "3. Harf Syarat__9": {"arti_ko": "만약 ~라면 (가정의 라우)", "desc_ko": "반사실적 조건 소사 (라우)", "jenis_ko": "조건 소사"},
    "3. Harf Syarat__10": {"arti_ko": "만약 ~가 없었다면", "desc_ko": "존재의 부정을 전제로 하는 조건 소사 (라우라)", "jenis_ko": "유보 조건소사"},
    "3. Harf Syarat__11": {"arti_ko": "비록 ~일지라도", "desc_ko": "양보적 조건 소사 (라우)", "jenis_ko": "양보 조건소사"},
    "3. Harf Syarat__12": {"arti_ko": "만약 ~한다면 (임마)", "desc_ko": "강조 조건 소사 (인 + 마)", "jenis_ko": "강조 조건소사"},
    "3. Harf Syarat__13": {"arti_ko": "어떠한 표징을 가져오든", "desc_ko": "포괄적 조건명사 (마흐마)", "jenis_ko": "포괄 조건명사"},

    # 4. Harf Mashdariyah
    "4. Harf Mashdariyah__14": {"arti_ko": "~하는 한 / ~동안", "desc_ko": "시간을 나타내는 명사화 소사 (마)", "jenis_ko": "시간 명사화소사"},
    "4. Harf Mashdariyah__15": {"arti_ko": "~하지 않도록", "desc_ko": "부정을 수반하는 명사화 소사 (안 + 라)", "jenis_ko": "명사화 부정소사"},
    "4. Harf Mashdariyah__16": {"arti_ko": "~라는 것 (안)", "desc_ko": "동사를 명사구로 만드는 소사 (안)", "jenis_ko": "명사화 소사"},
    "4. Harf Mashdariyah__17": {"arti_ko": "~하기를 바라다", "desc_ko": "소망의 명사화 소사 (라우)", "jenis_ko": "소망 명사화소사"},
    "4. Harf Mashdariyah__18": {"arti_ko": "~하지 말 것", "desc_ko": "금지를 수반하는 명사화 소사 (안 + 라)", "jenis_ko": "명사화 금지소사"},
    "4. Harf Mashdariyah__19": {"arti_ko": "~라는 사실", "desc_ko": "사실의 명사화 소사 (안 축약형)", "jenis_ko": "명사화 소사"},

    # 5. Harf Zaidah
    "5. Harf Zaidah__20": {"arti_ko": "~처럼 (강조)", "desc_ko": "비유 접두사 + 강조 첨가사 (카 + 마)", "jenis_ko": "강조 첨가사"},
    "5. Harf Zaidah__21": {"arti_ko": "모기와 같은 미물이라도", "desc_ko": "막연함과 강조의 첨가사 (마)", "jenis_ko": "강조 첨가사"},
    "5. Harf Zaidah__22": {"arti_ko": "내가 맹세하노니", "desc_ko": "맹세를 강화하는 첨가사 (라)", "jenis_ko": "맹세 강조첨가사"},
    "5. Harf Zaidah__23": {"arti_ko": "하나님의 자비로 인하여", "desc_ko": "전치사에 결합된 강조 첨가사 (비 + 마)", "jenis_ko": "전치사 강조첨가사"},
    "5. Harf Zaidah__24": {"arti_ko": "기쁜 소식을 전하는 자가 왔을 때", "desc_ko": "시간 접속사에 수반된 첨가사 (안)", "jenis_ko": "시간 강조첨가사"},

    # 6. Harf Istifham
    "6. Harf Istifham__25": {"arti_ko": "~인가? (의문의 할)", "desc_ko": "질문과 확인을 나타내는 의문 소사 (할)", "jenis_ko": "의문 소사"},

    # 7. Harf Jawab
    "7. Harf Jawab__26": {"arti_ko": "그렇다면 / 과연", "desc_ko": "응답과 귀결을 나타내는 소사 (이잔)", "jenis_ko": "응답 귀결소사"},
    "7. Harf Jawab__27": {"arti_ko": "그렇고말고요 / 참으로", "desc_ko": "부정에 대한 긍정 응답 소사 (발라)", "jenis_ko": "긍정 응답소사"},
    "7. Harf Jawab__28": {"arti_ko": "예 / 그렇습니다", "desc_ko": "긍정 응답 소사 (나암)", "jenis_ko": "긍정 응답소사"},
    "7. Harf Jawab__29": {"arti_ko": "그러하다! 주님을 두고 맹세컨대", "desc_ko": "맹세를 수반하는 긍정 응답 소사 (이)", "jenis_ko": "맹세 응답소사"},

    # 8. Harf Ibtida'
    "8. Harf Ibtida'__30": {"arti_ko": "~에 이르기까지", "desc_ko": "문두 및 발단을 나타내는 소사 (핫타)", "jenis_ko": "발단 소사"},

    # 9. Harf Tafshil
    "9. Harf Tafshil__31": {"arti_ko": "~에 관하여는", "desc_ko": "상세화 및 주제 제시 소사 (암마)", "jenis_ko": "상세화 소사"},

    # 10. Harf Mufaja'ah
    "10. Harf Mufaja'ah__32": {"arti_ko": "뜻밖에 ~가 되었다", "desc_ko": "돌발적 사태를 나타내는 소사 (이다)", "jenis_ko": "돌발 사태소사"},

    # 11. Harf Mufassirah
    "11. Harf Mufassirah__33": {"arti_ko": "즉 ~라고", "desc_ko": "해설 및 설명을 이끄는 소사 (안)", "jenis_ko": "설명 소사"},

    # 12. Harf Istiftahiyah
    "12. Harf Istiftahiyah__34": {"arti_ko": "보라! / 명심하라", "desc_ko": "주의환기 및 개시 소사 (알라)", "jenis_ko": "주의환기 소사"},

    # 13. Harf Rada'
    "13. Harf Rada'__35": {"arti_ko": "결코 아니다!", "desc_ko": "경계 및 강한 거절의 소사 (칼라)", "jenis_ko": "경계 거절소사"},

    # 14. Harf Ta'ajjub
    "14. Harf Ta'ajjub__36": {"arti_ko": "어찌 그리 잘 참는가!", "desc_ko": "감탄과 놀라움을 나타내는 소사 (마)", "jenis_ko": "감탄 소사"},

    # 15. Harf Fariqah
    "15. Harf Fariqah__37": {"arti_ko": "정녕 / 진실로", "desc_ko": "긍정을 구분하는 강조 람 (인 축약형 수반)", "jenis_ko": "구분 강조람"},

    # 16. Harf Mauthi'ah
    "16. Harf Mauthi'ah__38": {"arti_ko": "만약 ~한다면 맹세코", "desc_ko": "맹세를 이끄는 조건 람 (라 인)", "jenis_ko": "맹세 전치람"},

    # 17. Harf Mabany
    "17. Harf Mabany__39": {"arti_ko": "하 밈", "desc_ko": "장 서두의 신비로운 독립문자 (حم)", "jenis_ko": "독립문자 (무캇타아트)"},
    "17. Harf Mabany__40": {"arti_ko": "알리프 람 밈", "desc_ko": "장 서두의 신비로운 독립문자 (الم)", "jenis_ko": "독립문자 (무캇타아트)"},
    "17. Harf Mabany__41": {"arti_ko": "알리프 람 라", "desc_ko": "장 서두의 신비로운 독립문자 (الر)", "jenis_ko": "독립문자 (무캇타아트)"},
    "17. Harf Mabany__42": {"arti_ko": "따 신 밈", "desc_ko": "장 서두의 신비로운 독립문자 (طسم)", "jenis_ko": "독립문자 (무캇타아트)"},
    "17. Harf Mabany__43": {"arti_ko": "알리프 람 밈 라", "desc_ko": "장 서두의 신비로운 독립문자 (المر)", "jenis_ko": "독립문자 (무캇타아트)"},
    "17. Harf Mabany__44": {"arti_ko": "알리프 람 밈 사드", "desc_ko": "장 서두의 신비로운 독립문자 (المص)", "jenis_ko": "독립문자 (무캇타아트)"},
    "17. Harf Mabany__45": {"arti_ko": "사드", "desc_ko": "장 서두의 신비로운 독립문자 (ص)", "jenis_ko": "독립문자 (무캇타아트)"},
    "17. Harf Mabany__46": {"arti_ko": "따 신", "desc_ko": "장 서두의 신비로운 독립문자 (طس)", "jenis_ko": "독립문자 (무캇타아트)"},
    "17. Harf Mabany__47": {"arti_ko": "따 하", "desc_ko": "장 서두의 신비로운 독립문자 (طه)", "jenis_ko": "독립문자 (무캇타아트)"},
    "17. Harf Mabany__48": {"arti_ko": "아인 신 까프", "desc_ko": "장 서두의 신비로운 독립문자 (عسق)", "jenis_ko": "독립문자 (무캇타아트)"},
    "17. Harf Mabany__49": {"arti_ko": "까프", "desc_ko": "장 서두의 신비로운 독립문자 (ق)", "jenis_ko": "독립문자 (무캇타아트)"},
    "17. Harf Mabany__50": {"arti_ko": "까프 하 야 아인 사드", "desc_ko": "장 서두의 신비로운 독립문자 (كهيعص)", "jenis_ko": "독립문자 (무캇타아트)"},
    "17. Harf Mabany__51": {"arti_ko": "눈", "desc_ko": "장 서두의 신비로운 독립문자 (ن)", "jenis_ko": "독립문자 (무캇타아트)"},
    "17. Harf Mabany__52": {"arti_ko": "야 씬", "desc_ko": "장 서두의 신비로운 독립문자 (يس)", "jenis_ko": "독립문자 (무캇타아트)"}
}

# Update build_japanese_dataset.py content
def update_builder_ja():
    with open('build_japanese_dataset.py', 'r', encoding='utf-8') as f:
        code = f.read()
    
    code = re.sub(r'JAPANESE_GRAMMAR = \{[\s\S]*?\n\}\n\n# 4\. 17 Harf', 'JAPANESE_GRAMMAR = ' + json.dumps(JAPANESE_GRAMMAR, ensure_ascii=False, indent=4) + '\n\n# 4. 17 Harf', code)
    code = re.sub(r'JAPANESE_HARF_GRAMMAR = \{[\s\S]*?\n\}\n\n\ndef enrich_dhamir_data', 'JAPANESE_HARF_GRAMMAR = ' + json.dumps(JAPANESE_HARF_GRAMMAR, ensure_ascii=False, indent=4) + '\n\n\ndef enrich_dhamir_data', code)
    
    with open('build_japanese_dataset.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("build_japanese_dataset.py updated with exact grammar keys!")

# Update build_korean_dataset.py content
def update_builder_ko():
    with open('build_korean_dataset.py', 'r', encoding='utf-8') as f:
        code = f.read()
    
    code = re.sub(r'KOREAN_GRAMMAR = \{[\s\S]*?\n\}\n\n# 4\. 17 Harf', 'KOREAN_GRAMMAR = ' + json.dumps(KOREAN_GRAMMAR, ensure_ascii=False, indent=4) + '\n\n# 4. 17 Harf', code)
    code = re.sub(r'KOREAN_HARF_GRAMMAR = \{[\s\S]*?\n\}\n\n\ndef enrich_dhamir_data', 'KOREAN_HARF_GRAMMAR = ' + json.dumps(KOREAN_HARF_GRAMMAR, ensure_ascii=False, indent=4) + '\n\n\ndef enrich_dhamir_data', code)
    
    with open('build_korean_dataset.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("build_korean_dataset.py updated with exact grammar keys!")

# Update app.js initData
def update_app_js():
    with open('app.js', 'r', encoding='utf-8') as f:
        app_js = f.read()
        
    crlf = '\r\n' in app_js
    app_js = app_js.replace('\r\n', '\n')
    
    # 1. Check bentuk_fa -> add bentuk_ja and bentuk_ko
    if 'bentuk_ja:' not in app_js:
        app_js = app_js.replace(
            "bentuk_fa: item['BentukKataFA'] || b,",
            "bentuk_fa: item['BentukKataFA'] || b,\n          bentuk_ja: item['BentukKataJA'] || b,\n          bentuk_ko: item['BentukKataKO'] || b,"
        )

    # 2. Check arti_fa -> add arti_ja and arti_ko
    if 'arti_ja:' not in app_js:
        app_js = app_js.replace(
            "arti_fa: item['ArtiKataFA'] || grammar.arti_fa || item['ArtiKataID'] || item['Arti kata'] || '',",
            "arti_fa: item['ArtiKataFA'] || grammar.arti_fa || item['ArtiKataID'] || item['Arti kata'] || '',\n          arti_ja: item['ArtiKataJA'] || grammar.arti_ja || item['ArtiKataID'] || item['Arti kata'] || '',\n          arti_ko: item['ArtiKataKO'] || grammar.arti_ko || item['ArtiKataID'] || item['Arti kata'] || '',"
        )

    # 3. Check suratArtiFA -> add suratArtiJA and suratArtiKO
    if 'suratArtiJA:' not in app_js:
        app_js = app_js.replace(
            "suratArtiFA: item['SuratArtiFA'] || item['SuratArtiEN'] || '',",
            "suratArtiFA: item['SuratArtiFA'] || item['SuratArtiEN'] || '',\n        suratArtiJA: item['SuratArtiJA'] || item['SuratArtiEN'] || '',\n        suratArtiKO: item['SuratArtiKO'] || item['SuratArtiEN'] || '',"
        )

    # 4. Check teksArtiFA -> add teksArtiJA and teksArtiKO
    if 'teksArtiJA:' not in app_js:
        app_js = app_js.replace(
            "teksArtiFA: item['TeksArtiFA'] || item['TeksArti'] || '',",
            "teksArtiFA: item['TeksArtiFA'] || item['TeksArti'] || '',\n        teksArtiJA: item['TeksArtiJA'] || item['TeksArti'] || '',\n        teksArtiKO: item['TeksArtiKO'] || item['TeksArti'] || '',"
        )

    if crlf:
        app_js = app_js.replace('\n', '\r\n')
        
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(app_js)
    print("app.js initData mappings successfully verified and updated!")

if __name__ == '__main__':
    update_builder_ja()
    update_builder_ko()
    update_app_js()
