#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chinese (zh / 简体中文) Quran translation metadata module.
Translators: 马坚 (Muhammad Makin - zh.jian)
Includes:
- 114 Surah meanings in Chinese (SURAH_ZH)
- 7 Bentuk labels in Chinese (BENTUK_ZH)
- 76 Grammatical entries metadata in Chinese (GRAMMAR_ZH)
"""

SURAH_ZH = {
    1: '开端章', 2: '黄牛章', 3: '仪姆兰的家属章', 4: '妇女章', 5: '筵席章',
    6: '牲畜章', 7: '高处章', 8: '战利品章', 9: '忏悔章', 10: '优努斯章',
    11: '呼德章', 12: '优素福章', 13: '雷霆章', 14: '易卜拉欣章', 15: '石谷章',
    16: '蜜蜂章', 17: '夜行章', 18: '山洞章', 19: '麦尔彦章', 20: '塔哈章',
    21: '众先知章', 22: '朝觐章', 23: '信士章', 24: '光明章', 25: '准则章',
    26: '众诗人章', 27: '蚂蚁章', 28: '故事章', 29: '蜘蛛章', 30: '罗马人章',
    31: '鲁格曼章', 32: '叩头章', 33: '同盟军章', 34: '赛伯邑章', 35: '创造者章',
    36: '雅辛章', 37: '列班者章', 38: '萨德章', 39: '队伍章', 40: '赦宥者章',
    41: '奉献章', 42: '协商章', 43: '金饰章', 44: '烟雾章', 45: '屈膝章',
    46: '沙丘章', 47: '穆罕默德章', 48: '胜利章', 49: '寝室章', 50: '戛弗章',
    51: '播种者章', 52: '山岳章', 53: '星宿章', 54: '月亮章', 55: '至仁主章',
    56: '大事章', 57: '铁章', 58: '辩诉者章', 59: '放逐章', 60: '受考验的妇人章',
    61: '列阵章', 62: '聚礼章', 63: '伪信者章', 64: '相欺章', 65: '离婚章',
    66: '禁戒章', 67: '国权章', 68: '笔章', 69: '真灾章', 70: '天梯章',
    71: '努哈章', 72: '精灵章', 73: '披衣的人章', 74: '盖被的人章', 75: '复活章',
    76: '人章', 77: '天使章', 78: '消息章', 79: '急拔章', 80: '皱眉章',
    81: '黯黮章', 82: '破裂章', 83: '称量不公章', 84: '绽裂章', 85: '十二宫章',
    86: '启明星章', 87: '至高者章', 88: '大灾章', 89: '黎明章', 90: '地方章',
    91: '太阳章', 92: '黑夜章', 93: '上午章', 94: '开拓章', 95: '无花果章',
    96: '血块章', 97: '高贵章', 98: '明证章', 99: '地震章', 100: '奔驰的马队章',
    101: '大难章', 102: '竞赛富庶章', 103: '时光章', 104: '诽谤者章', 105: '象章',
    106: '古莱氏章', 107: '什物章', 108: '多福章', 109: '不信道的人们章', 110: '援助章',
    111: '烈焰章', 112: '忠诚章', 113: '曙光章', 114: '人们章'
}

BENTUK_ZH = {
    '1. Dhamir': '1. 人称代词 (代名词 / Dhamir)',
    '2. Mawshul': '2. 关系代词 (接续词 / Mawshul)',
    '3. Istifham': '3. 疑问词 (疑问代词 / Istifham)',
    '4. Syarath': '4. 条件虚词 (条件代词 / Syarath)',
    '5. Isyarah': '5. 指示代词 (指示名词 / Isyarah)',
    "6. Isim Fi'il": "6. 动名词 (含动词义名词 / Isim Fi'il)",
    "7. Fi'il Jamid": "7. 固态动词 (不规则静态动词 / Fi'il Jamid)"
}

GRAMMAR_ZH = {
    # 1. Dhamir
    '1. Dhamir__1a': {'arti_zh': '他 (阳性单数)', 'desc_zh': '他（第三人称单数阳性独立人称代词）', 'jenis_zh': '独立代词 (Munfashil)'},
    '1. Dhamir__1b': {'arti_zh': '..他的 / ..他', 'desc_zh': '..他的/..他（第三人称单数阳性接尾代词）', 'jenis_zh': '接尾代词 (Muttashil)'},
    '1. Dhamir__1c': {'arti_zh': '唯独于他 / 只向他', 'desc_zh': '唯独于他（独立宾格代词）', 'jenis_zh': '独立宾格代词 (Munfashil Manshub)'},
    '1. Dhamir__2a': {'arti_zh': '他们俩 / 她们俩', 'desc_zh': '他们/她们俩（第三人称双数独立代词）', 'jenis_zh': '独立代词 (Munfashil)'},
    '1. Dhamir__2b': {'arti_zh': '..他们/她们俩的', 'desc_zh': '..他们俩的（第三人称双数接尾代词）', 'jenis_zh': '接尾代词 (Muttashil)'},
    '1. Dhamir__3a': {'arti_zh': '他们 (阳性复数)', 'desc_zh': '他们（第三人称阳性复数独立代词）', 'jenis_zh': '独立代词 (Munfashil)'},
    '1. Dhamir__3b': {'arti_zh': '..他们的 / ..他们', 'desc_zh': '..他们的/..他们（第三人称阳性复数接尾代词）', 'jenis_zh': '接尾代词 (Muttashil)'},
    '1. Dhamir__3c': {'arti_zh': '唯独于他们', 'desc_zh': '唯独于他们（独立宾格复数代词）', 'jenis_zh': '独立宾格代词 (Munfashil Manshub)'},
    '1. Dhamir__4a': {'arti_zh': '她 (阴性单数)', 'desc_zh': '她（第三人称单数阴性独立代词）', 'jenis_zh': '独立代词 (Munfashil)'},
    '1. Dhamir__4b': {'arti_zh': '..她的 / ..它', 'desc_zh': '..她的/..它（第三人称单数阴性接尾代词）', 'jenis_zh': '接尾代词 (Muttashil)'},
    '1. Dhamir__5a': {'arti_zh': '她们 (阴性复数)', 'desc_zh': '她们（第三人称阴性复数独立代词）', 'jenis_zh': '独立代词 (Munfashil)'},
    '1. Dhamir__5b': {'arti_zh': '..她们的 / ..她们', 'desc_zh': '..她们的（第三人称阴性复数接尾代词）', 'jenis_zh': '接尾代词 (Muttashil)'},
    '1. Dhamir__6a': {'arti_zh': '你 (阳性单数)', 'desc_zh': '你（第二人称单数阳性独立代词）', 'jenis_zh': '独立代词 (Munfashil)'},
    '1. Dhamir__6b': {'arti_zh': '..你的 / ..你', 'desc_zh': '..你的/..你（第二人称单数阳性接尾代词）', 'jenis_zh': '接尾代词 (Muttashil)'},
    '1. Dhamir__6c': {'arti_zh': '唯独于你 / 只向你', 'desc_zh': '唯独于你/只向你（第二人称独立宾格代词）', 'jenis_zh': '独立宾格代词 (Munfashil Manshub)'},
    '1. Dhamir__7a': {'arti_zh': '你们俩 (双数)', 'desc_zh': '你们俩（第二人称双数独立代词）', 'jenis_zh': '独立代词 (Munfashil)'},
    '1. Dhamir__7b': {'arti_zh': '..你们俩的', 'desc_zh': '..你们俩的（第二人称双数接尾代词）', 'jenis_zh': '接尾代词 (Muttashil)'},
    '1. Dhamir__8a': {'arti_zh': '你们 (阳性复数)', 'desc_zh': '你们（第二人称阳性复数独立代词）', 'jenis_zh': '独立代词 (Munfashil)'},
    '1. Dhamir__8b': {'arti_zh': '..你们的 / ..你们', 'desc_zh': '..你们的（第二人称阳性复数接尾代词）', 'jenis_zh': '接尾代词 (Muttashil)'},
    '1. Dhamir__8c': {'arti_zh': '唯独于你们', 'desc_zh': '唯独于你们（第二人称复数独立宾格代词）', 'jenis_zh': '独立宾格代词 (Munfashil Manshub)'},
    '1. Dhamir__9b': {'arti_zh': '..你的 (阴性)', 'desc_zh': '..你的（第二人称单数阴性接尾代词）', 'jenis_zh': '接尾代词 (Muttashil)'},
    '1. Dhamir__11a': {'arti_zh': '我 (第一人称)', 'desc_zh': '我（第一人称单数独立代词）', 'jenis_zh': '独立代词 (Munfashil)'},
    '1. Dhamir__11b': {'arti_zh': '..我的 / ..我', 'desc_zh': '..我的/..我（第一人称单数接尾代词）', 'jenis_zh': '接尾代词 (Muttashil)'},
    '1. Dhamir__11c': {'arti_zh': '唯独于我 / 只向我', 'desc_zh': '唯独于我（第一人称单数独立宾格代词）', 'jenis_zh': '独立宾格代词 (Munfashil Manshub)'},
    '1. Dhamir__12a': {'arti_zh': '我们 (第一人称复数)', 'desc_zh': '我们（第一人称复数独立代词）', 'jenis_zh': '独立代词 (Munfashil)'},
    '1. Dhamir__12b': {'arti_zh': '..我们的 / ..我们', 'desc_zh': '..我们的（第一人称复数接尾代词）', 'jenis_zh': '接尾代词 (Muttashil)'},
    '1. Dhamir__12c': {'arti_zh': '唯独于我们', 'desc_zh': '唯独于我们（第一人称复数独立宾格代词）', 'jenis_zh': '独立宾格代词 (Munfashil Manshub)'},

    # 2. Mawshul
    '2. Mawshul__1': {'arti_zh': '凡…的事物 / 所…的', 'desc_zh': '凡所…的事物（用于无理智事物的通用关系代词）', 'jenis_zh': '通用关系代词 (Mawshul Musytarak)'},
    '2. Mawshul__2': {'arti_zh': '那些…的人们 (阳性复数)', 'desc_zh': '那些…的人（阳性复数专用关系代词）', 'jenis_zh': '专用关系代词 (Mawshul Khash)'},
    '2. Mawshul__3': {'arti_zh': '凡…的人 / 谁', 'desc_zh': '凡…的人/谁（用于有理智者的通用关系代词）', 'jenis_zh': '通用关系代词 (Mawshul Musytarak)'},
    '2. Mawshul__4': {'arti_zh': '那个…的人/事物 (阳性单数)', 'desc_zh': '那个…的人/物（阳性单数专用关系代词）', 'jenis_zh': '专用关系代词 (Mawshul Khash)'},
    '2. Mawshul__5': {'arti_zh': '无论哪一个 / 任何人', 'desc_zh': '无论哪一个（可变格关系代词）', 'jenis_zh': '不定关系代词 (Mawshul Mubham)'},
    '2. Mawshul__6': {'arti_zh': '那个…的女性/事物 (阴性单数)', 'desc_zh': '那个…的女性/事物（阴性单数专用关系代词）', 'jenis_zh': '专用关系代词 (Mawshul Khash)'},
    '2. Mawshul__7': {'arti_zh': '那些…的妇女们', 'desc_zh': '那些…的妇女们（阴性复数专用关系代词）', 'jenis_zh': '专用关系代词 (Mawshul Khash)'},
    '2. Mawshul__8': {'arti_zh': '那些…的妇女们', 'desc_zh': '那些…的妇女们（阴性复数专用关系代词）', 'jenis_zh': '专用关系代词 (Mawshul Khash)'},
    '2. Mawshul__9': {'arti_zh': '他们俩…的人 (阳性双数)', 'desc_zh': '他们俩…的人（阳性双数专用关系代词）', 'jenis_zh': '专用关系代词 (Mawshul Khash)'},
    '2. Mawshul__10': {'arti_zh': '无论哪一个 (阴性)', 'desc_zh': '无论哪一个（阴性可变格关系代词）', 'jenis_zh': '不定关系代词 (Mawshul Mubham)'},

    # 3. Istifham
    '3. Istifham__1': {'arti_zh': '什么？ / 何物？', 'desc_zh': '什么？（用于非理智物的疑问代词）', 'jenis_zh': '疑问名词 (Ism Istifham)'},
    '3. Istifham__2': {'arti_zh': '怎样？ / 如何？', 'desc_zh': '怎样？如何？（询问情状的疑问词）', 'jenis_zh': '疑问名词 (Ism Istifham)'},
    '3. Istifham__3': {'arti_zh': '谁？ / 何人？', 'desc_zh': '谁？（用于有理智者的疑问代词）', 'jenis_zh': '疑问名词 (Ism Istifham)'},
    '3. Istifham__4': {'arti_zh': '哪一个？ / 谁？', 'desc_zh': '哪一个？谁？（可变格疑问词）', 'jenis_zh': '疑问名词 (Ism Istifham)'},
    '3. Istifham__5': {'arti_zh': '怎么？ / 从哪里？ / 何时？', 'desc_zh': '怎么？从哪里？（询问方式或来源的疑问词）', 'jenis_zh': '疑问名词 (Ism Istifham)'},
    '3. Istifham__6': {'arti_zh': '究竟是什么…？', 'desc_zh': '究竟是什么…？（复合疑问词 Mā + Dzā）', 'jenis_zh': '疑问名词 (Ism Istifham)'},
    '3. Istifham__7': {'arti_zh': '多少？ / 多久？', 'desc_zh': '多少？多久？（询问数量或时间的疑问词）', 'jenis_zh': '疑问名词 (Ism Istifham)'},
    '3. Istifham__8': {'arti_zh': '为什么？ / 为何？', 'desc_zh': '为什么？（Li + Ma 复合疑问词）', 'jenis_zh': '疑问名词 (Ism Istifham)'},
    '3. Istifham__9': {'arti_zh': '在哪里？ / 何处？', 'desc_zh': '在哪里？何处？（询问地点的疑问词）', 'jenis_zh': '疑问名词 (Ism Istifham)'},
    '3. Istifham__10': {'arti_zh': '何时？ / 什么时候？', 'desc_zh': '何时？（询问时间的疑问词）', 'jenis_zh': '疑问名词 (Ism Istifham)'},

    # 4. Syarath
    '4. Syarath__1': {'arti_zh': '无论谁 / 凡…的人', 'desc_zh': '无论谁/凡…的人（有理智条件代词）', 'jenis_zh': '断格条件词 (Ism Syarath Jazim)'},
    '4. Syarath__2': {'arti_zh': '无论什么 / 凡…的事物', 'desc_zh': '无论什么（非理智事物条件词）', 'jenis_zh': '断格条件词 (Ism Syarath Jazim)'},
    '4. Syarath__3': {'arti_zh': '每当…的时候 / 每次', 'desc_zh': '每当…的时候/每次（时间条件词）', 'jenis_zh': '不断格条件词 (Ghayr Jazim)'},
    '4. Syarath__4': {'arti_zh': '无论哪一个', 'desc_zh': '无论哪一个（可变格条件词）', 'jenis_zh': '断格条件词 (Ism Syarath Jazim)'},
    '4. Syarath__5': {'arti_zh': '无论怎样 / 无论哪一个', 'desc_zh': '无论哪一个（带强调词 Mā 的条件词）', 'jenis_zh': '断格条件词 (Ism Syarath Jazim)'},

    # 5. Isyarah
    '5. Isyarah__1': {'arti_zh': '这 / 那 (阳性单数)', 'desc_zh': '这/那（阳性单数指示代词）', 'jenis_zh': '指示名词 (Ism Isyarah)'},
    '5. Isyarah__2': {'arti_zh': '这些 / 那些 (复数)', 'desc_zh': '这些/那些（复数指示代词）', 'jenis_zh': '指示名词 (Ism Isyarah)'},
    '5. Isyarah__3': {'arti_zh': '这 / 那 (阴性单数)', 'desc_zh': '这/那（阴性单数指示代词）', 'jenis_zh': '指示名词 (Ism Isyarah)'},
    '5. Isyarah__4': {'arti_zh': '那些 (远指/非理智复数)', 'desc_zh': '那些（远指/非理智复数指示代词）', 'jenis_zh': '指示名词 (Ism Isyarah)'},
    '5. Isyarah__5': {'arti_zh': '在这里 / 此处', 'desc_zh': '在这里（近指地点指示词）', 'jenis_zh': '地点指示词 (Ism Isyarah Makan)'},
    '5. Isyarah__6': {'arti_zh': '在那里 / 彼处', 'desc_zh': '在那里（远指地点指示词）', 'jenis_zh': '地点指示词 (Ism Isyarah Makan)'},
    '5. Isyarah__7': {'arti_zh': '这两个 (阳性双数)', 'desc_zh': '这两个（阳性双数指示代词）', 'jenis_zh': '指示名词 (Ism Isyarah)'},
    '5. Isyarah__8': {'arti_zh': '这两位 (阴性双数)', 'desc_zh': '这两位（阴性双数指示代词）', 'jenis_zh': '指示名词 (Ism Isyarah)'},

    # 6. Isim Fi'il
    '6. Isim Fi\'il__1': {'arti_zh': '赞颂安拉超绝！(赞主清净)', 'desc_zh': '赞颂安拉超绝（表达赞颂与清净源动名词）', 'jenis_zh': "动名词 / 源词 (Mashdar)"},
    '6. Isim Fi\'il__2': {'arti_zh': '拿来！ / 拿证据来！', 'desc_zh': '拿来/出示证据（祈使动名词）', 'jenis_zh': "祈使动名词 (Isim Fi'il Amr)"},
    '6. Isim Fi\'il__3': {'arti_zh': '呸！ / 唉！ (厌恶之叹)', 'desc_zh': '表示极度厌恶与厌烦（现在时动名词）', 'jenis_zh': "现在时动名词 (Isim Fi'il Mudhari)"},
    '6. Isim Fi\'il__4': {'arti_zh': '求安拉保佑！ / 绝非如此！', 'desc_zh': '求安拉庇护（Ma\'ādzallāh）', 'jenis_zh': "动名词 / 源词 (Mashdar)"},
    '6. Isim Fi\'il__5': {'arti_zh': '到这里来！ / 拿出来！', 'desc_zh': '到这里来/带过来（祈使动名词）', 'jenis_zh': "祈使动名词 (Isim Fi'il Amr)"},
    '6. Isim Fi\'il__6': {'arti_zh': '太遥远了！ / 绝不可能！', 'desc_zh': '太遥远了/绝不可能（过去时动名词）', 'jenis_zh': "过去时动名词 (Isim Fi'il Madhi)"},
    '6. Isim Fi\'il__7': {'arti_zh': '拿去读吧！ / 瞧这！', 'desc_zh': '拿去读吧（祈使动名词）', 'jenis_zh': "祈使动名词 (Isim Fi'il Amr)"},
    '6. Isim Fi\'il__8': {'arti_zh': '快来吧！ / 到这儿来！', 'desc_zh': '快来吧（祈使动名词）', 'jenis_zh': "祈使动名词 (Isim Fi'il Amr)"},

    # 7. Fi'il Jamid
    '7. Fi\'il Jamid__1': {'arti_zh': '不是 / 并不存在', 'desc_zh': '不是/没有（否定性固态动词）', 'jenis_zh': "固态过去时动词 (Fi'il Madhi Jamid)"},
    '7. Fi\'il Jamid__2': {'arti_zh': '真恶劣！ / 最差劲的', 'desc_zh': '真恶劣（用于谴责的固态动词 / Adz-Dzamm）', 'jenis_zh': "固态过去时动词 (Fi'il Madhi Jamid)"},
    '7. Fi\'il Jamid__3': {'arti_zh': '但愿 / 或许 / 可能', 'desc_zh': '但愿/或许（表示希冀的固态动词 / Tarajji）', 'jenis_zh': "固态过去时动词 (Fi'il Madhi Jamid)"},
    '7. Fi\'il Jamid__4': {'arti_zh': '真优美！ / 最好的', 'desc_zh': '真优美/真好（用于赞美的固态动词 / Al-Madh）', 'jenis_zh': "固态过去时动词 (Fi'il Madhi Jamid)"},
    '7. Fi\'il Jamid__5': {'arti_zh': '他们所换取的真恶劣！', 'desc_zh': '真恶劣（Bi\'sa + Ma 复合谴责动词）', 'jenis_zh': "固态过去时动词 (Fi'il Madhi Jamid)"},
    '7. Fi\'il Jamid__6': {'arti_zh': '他们俩便开始 / 忙着', 'desc_zh': '开始着手做（起始动词 / Af\'al Asy-Syuru\'）', 'jenis_zh': "固态过去时动词 (Fi'il Madhi Jamid)"},
    '7. Fi\'il Jamid__7': {'arti_zh': '安拉超绝万物！ / 绝非如此', 'desc_zh': '赞颂安拉完美无缺（赞主清净）', 'jenis_zh': "固态动词 (Fi'il Jamid)"},
    '7. Fi\'il Jamid__8': {'arti_zh': '安拉用以劝戒你们的事真好！', 'desc_zh': '真优美（Ni\'ma + Ma 复合赞美动词）', 'jenis_zh': "固态过去时动词 (Fi'il Madhi Jamid)"}
}
