#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to update build_multilingual_dataset.py with Russian support (9 languages total: ID, EN, MS, FR, DE, UR, HI, BN, RU)
"""

import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
bmd_path = os.path.join(BASE_DIR, 'build_multilingual_dataset.py')

# 1. Russian Surah Meanings (114 Surahs)
SURAH_RU = {
    1: 'Открывающая Книгу', 2: 'Корова', 3: 'Семейство Имрана', 4: 'Женщины', 5: 'Трапеза',
    6: 'Скот', 7: 'Ограды', 8: 'Трофеи', 9: 'Покаяние', 10: 'Юнус',
    11: 'Худ', 12: 'Юсуф', 13: 'Гром', 14: 'Ибрахим', 15: 'Хиджр',
    16: 'Пчёлы', 17: 'Ночной перенос', 18: 'Пещера', 19: 'Марьям', 20: 'Та Ха',
    21: 'Пророки', 22: 'Паломничество', 23: 'Верующие', 24: 'Свет', 25: 'Различение',
    26: 'Поэты', 27: 'Муравьи', 28: 'Рассказ', 29: 'Паук', 30: 'Римляне',
    31: 'Лукман', 32: 'Земной поклон', 33: 'Союзники', 34: 'Саба', 35: 'Творец',
    36: 'Йа Син', 37: 'Выстроившиеся в ряды', 38: 'Сад', 39: 'Толпы', 40: 'Прощающий',
    41: 'Разъяснены', 42: 'Совет', 43: 'Украшения', 44: 'Дым', 45: 'Коленопреклонённые',
    46: 'Барханы', 47: 'Мухаммад', 48: 'Победа', 49: 'Комнаты', 50: 'Каф',
    51: 'Рассеивающие', 52: 'Гора', 53: 'Звезда', 54: 'Месяц', 55: 'Милостивый',
    56: 'Неотвратимое', 57: 'Железо', 58: 'Препирательство', 59: 'Сбор', 60: 'Испытуемая',
    61: 'Ряды', 62: 'Пятница', 63: 'Лицемеры', 64: 'Взаимное обделение', 65: 'Развод',
    66: 'Запрещение', 67: 'Власть', 68: 'Письменная трость', 69: 'Неминуемое', 70: 'Ступени',
    71: 'Нух', 72: 'Джинны', 73: 'Закутавшийся', 74: 'Завернувшийся', 75: 'Воскресение',
    76: 'Человек', 77: 'Посылаемые', 78: 'Весть', 79: 'Исторгающие', 80: 'Нахмурился',
    81: 'Скручивание', 82: 'Раскалывание', 83: 'Обвешивающие', 84: 'Разверзнется', 85: 'Созвездия',
    86: 'Ночной путник', 87: 'Высочайший', 88: 'Покрывающее', 89: 'Заря', 90: 'Город',
    91: 'Солнце', 92: 'Ночь', 93: 'Утро', 94: 'Раскрытие', 95: 'Смоковница',
    96: 'Сгусток крови', 97: 'Предопределение', 98: 'Ясное знамение', 99: 'Сотрясение', 100: 'Мчащиеся',
    101: 'Великое бедствие', 102: 'Страсть к приумножению', 103: 'Предвечернее время', 104: 'Хулитель', 105: 'Слон',
    106: 'Курейшиты', 107: 'Мелочь', 108: 'Изобилие', 109: 'Неверующие', 110: 'Помощь',
    111: 'Пальмовые волокна', 112: 'Искренность', 113: 'Рассвет', 114: 'Люди'
}

# 2. Russian Bentuk Labels
BENTUK_RU = {
    '1. Dhamir': '1. Местоимения (Дамир / Dhamir)',
    '2. Mawshul': '2. Относительные местоимения (Маусуль / Mawshul)',
    '3. Istifham': '3. Вопросительные слова (Истифхам / Istifham)',
    '4. Syarath': '4. Условные частицы (Шарат / Syarath)',
    '5. Isyarah': '5. Указательные местоимения (Ишара / Isyarah)',
    "6. Isim Fi'il": "6. Именные глаголы (Исм Фииль / Isim Fi'il)",
    "7. Fi'il Jamid": "7. Неизменяемые глаголы (Фииль Джамид / Fi'il Jamid)"
}

# 3. Russian Grammatical Metadata (76 items)
GRAMMAR_RU = {
    # 1. Dhamir
    '1. Dhamir__1a': {'arti_ru': 'ОН / ЕГО', 'desc_ru': 'Он (3-е лицо, ед.ч., муж.род, раздельное местоимение)', 'jenis_ru': 'Мунфасыль (Раздельное)'},
    '1. Dhamir__1b': {'arti_ru': '..ЕГО / ..ЕМУ / ..ИМ', 'desc_ru': '..его / ..ему (3-е лицо, ед.ч., муж.род, слитное местоимение)', 'jenis_ru': 'Муттасыль (Слитное)'},
    '1. Dhamir__1c': {'arti_ru': 'ТОЛЬКО ЕМУ / ЕГО ОДНОГО', 'desc_ru': 'Только Ему (Раздельное объектное местоимение, вин. падеж)', 'jenis_ru': 'Мунфасыль Мансуб'},
    '1. Dhamir__2a': {'arti_ru': 'ОНИ ДВОЕ (М/Ж)', 'desc_ru': 'Они вдвоем (дв.ч., муж./жен.род, раздельное местоимение)', 'jenis_ru': 'Мунфасыль (Раздельное)'},
    '1. Dhamir__2b': {'arti_ru': '..ИХ ДВОИХ', 'desc_ru': '..их двоих (дв.ч., муж./жен.род, слитное местоимение)', 'jenis_ru': 'Муттасыль (Слитное)'},
    '1. Dhamir__3a': {'arti_ru': 'ОНИ (МУЖ. Р.)', 'desc_ru': 'Они (мн.ч., муж.род, раздельное местоимение)', 'jenis_ru': 'Мунфасыль (Раздельное)'},
    '1. Dhamir__3b': {'arti_ru': '..ИХ / ..ИМ', 'desc_ru': '..их / ..им (мн.ч., муж.род, слитное местоимение)', 'jenis_ru': 'Муттасыль (Слитное)'},
    '1. Dhamir__3c': {'arti_ru': 'ТОЛЬКО ИМ / ИХ ОДНИХ', 'desc_ru': 'Только им (Раздельное объектное местоимение мн.ч., вин. падеж)', 'jenis_ru': 'Мунфасыль Мансуб'},
    '1. Dhamir__4a': {'arti_ru': 'ОНА / ЕЁ', 'desc_ru': 'Она (3-е лицо, ед.ч., жен.род, раздельное местоимение)', 'jenis_ru': 'Мунфасыль (Раздельное)'},
    '1. Dhamir__4b': {'arti_ru': '..ЕЁ / ..ЕЙ', 'desc_ru': '..её / ..ей (3-е лицо, ед.ч., жен.род, слитное местоимение)', 'jenis_ru': 'Муттасыль (Слитное)'},
    '1. Dhamir__5a': {'arti_ru': 'ОНИ (ЖЕН. Р.)', 'desc_ru': 'Они (мн.ч., жен.род, раздельное местоимение)', 'jenis_ru': 'Мунфасыль (Раздельное)'},
    '1. Dhamir__5b': {'arti_ru': '..ИХ (ЖЕН. Р.)', 'desc_ru': '..их (мн.ч., жен.род, слитное местоимение)', 'jenis_ru': 'Муттасыль (Слитное)'},
    '1. Dhamir__6a': {'arti_ru': 'ТЫ / ВЫ (МУЖ. Р.)', 'desc_ru': 'Ты (2-е лицо, ед.ч., муж.род, раздельное местоимение)', 'jenis_ru': 'Мунфасыль (Раздельное)'},
    '1. Dhamir__6b': {'arti_ru': '..ТВОЙ / ..ТЕБЯ / ..ТЕБЕ', 'desc_ru': '..твой / ..тебе (2-е лицо, ед.ч., муж.род, слитное)', 'jenis_ru': 'Муттасыль (Слитное)'},
    '1. Dhamir__6c': {'arti_ru': 'ТЕБЕ ОДНОМУ / ТОЛЬКО ТЕБЕ', 'desc_ru': 'Только Тебе (Раздельное объектное местоимение 2-го лица ед.ч.)', 'jenis_ru': 'Мунфасыль Мансуб'},
    '1. Dhamir__7a': {'arti_ru': 'ВЫ ДВОЕ (М/Ж)', 'desc_ru': 'Вы вдвоем (2-е лицо, дв.ч., муж./жен.род, раздельное)', 'jenis_ru': 'Мунфасыль (Раздельное)'},
    '1. Dhamir__7b': {'arti_ru': '..ВАШ (ДВОИХ)', 'desc_ru': '..вас двоих (2-е лицо, дв.ч., слитное)', 'jenis_ru': 'Муттасыль (Слитное)'},
    '1. Dhamir__8a': {'arti_ru': 'ВЫ (МУЖ. Р. МН. Ч.)', 'desc_ru': 'Вы (2-е лицо, мн.ч., муж.род, раздельное местоимение)', 'jenis_ru': 'Мунфасыль (Раздельное)'},
    '1. Dhamir__8b': {'arti_ru': '..ВАШ / ..ВАМ / ..ВАС', 'desc_ru': '..ваш / ..вам (2-е лицо, мн.ч., муж.род, слитное)', 'jenis_ru': 'Муттасыль (Слитное)'},
    '1. Dhamir__8c': {'arti_ru': 'ТОЛЬКО ВАМ / ВАС ОДНИХ', 'desc_ru': 'Только вам (Раздельное объектное местоимение 2-го лица мн.ч.)', 'jenis_ru': 'Мунфасыль Мансуб'},
    '1. Dhamir__9b': {'arti_ru': '..ТВОЙ / ..ТЕБЕ (ЖЕН. Р.)', 'desc_ru': '..твой / ..тебе (2-е лицо, ед.ч., жен.род, слитное)', 'jenis_ru': 'Муттасыль (Слитное)'},
    '1. Dhamir__11a': {'arti_ru': 'Я / МЕНЯ', 'desc_ru': 'Я (1-е лицо, ед.ч., раздельное местоимение)', 'jenis_ru': 'Мунфасыль (Раздельное)'},
    '1. Dhamir__11b': {'arti_ru': '..МОЙ / ..МНЕ / ..МЕНЯ', 'desc_ru': '..мой / ..мне / ..меня (1-е лицо, ед.ч., слитное местоимение)', 'jenis_ru': 'Муттасыль (Слитное)'},
    '1. Dhamir__11c': {'arti_ru': 'ТОЛЬКО МНЕ / МЕНЯ ОДНОГО', 'desc_ru': 'Только Мне (Раздельное объектное местоимение 1-го лица ед.ч.)', 'jenis_ru': 'Мунфасыль Мансуб'},
    '1. Dhamir__12a': {'arti_ru': 'МЫ / НАС', 'desc_ru': 'Мы (1-е лицо, мн.ч., раздельное местоимение)', 'jenis_ru': 'Мунфасыль (Раздельное)'},
    '1. Dhamir__12b': {'arti_ru': '..НАШ / ..НАМ / ..НАС', 'desc_ru': '..наш / ..нам / ..нас (1-е лицо, мн.ч., слитное местоимение)', 'jenis_ru': 'Муттасыль (Слитное)'},
    '1. Dhamir__12c': {'arti_ru': 'ТОЛЬКО НАМ / НАС ОДНИХ', 'desc_ru': 'Только нам (Раздельное объектное местоимение 1-го лица мн.ч.)', 'jenis_ru': 'Мунфасыль Мансуб'},

    # 2. Mawshul
    '2. Mawshul__1': {'arti_ru': 'ТО, ЧТО / ЧТО', 'desc_ru': 'То, что / что (Относительное местоимение для неодушевленных)', 'jenis_ru': 'Маусуль Муштарак'},
    '2. Mawshul__2': {'arti_ru': 'ТЕ, КОТОРЫЕ (МУЖ. Р.)', 'desc_ru': 'Те, которые (Относительное местоимение мн.ч., муж.род)', 'jenis_ru': 'Маусуль Хасс'},
    '2. Mawshul__3': {'arti_ru': 'ТОТ, КТО / КТО', 'desc_ru': 'Тот, кто / кто-либо (Относительное местоимение для разумных)', 'jenis_ru': 'Маусуль Муштарак'},
    '2. Mawshul__4': {'arti_ru': 'ТОТ, КОТОРЫЙ (МУЖ. Р. 1)', 'desc_ru': 'Тот, который (Относительное местоимение ед.ч., муж.род)', 'jenis_ru': 'Маусуль Хасс'},
    '2. Mawshul__5': {'arti_ru': 'КАКОЙ БЫ НИ / ЛЮБОЙ ИЗ', 'desc_ru': 'Какой бы ни / кто бы ни (Склоняемое относительное местоимение)', 'jenis_ru': 'Маусуль Мубхам'},
    '2. Mawshul__6': {'arti_ru': 'ТА, КОТОРАЯ (ЖЕН. Р. 1)', 'desc_ru': 'Та, которая (Относительное местоимение ед.ч., жен.род)', 'jenis_ru': 'Маусуль Хасс'},
    '2. Mawshul__7': {'arti_ru': 'ТЕ ЖЕНЩИНЫ, КОТОРЫЕ', 'desc_ru': 'Те женщины, которые (Относительное местоимение мн.ч., жен.род)', 'jenis_ru': 'Маусуль Хасс'},
    '2. Mawshul__8': {'arti_ru': 'ТЕ ЖЕНЩИНЫ, КОТОРЫЕ', 'desc_ru': 'Те женщины, которые (Относительное местоимение мн.ч., жен.род)', 'jenis_ru': 'Маусуль Хасс'},
    '2. Mawshul__9': {'arti_ru': 'ТЕ ДВОЕ, КОТОРЫЕ (МУЖ. Р.)', 'desc_ru': 'Те двое, которые (Относительное местоимение дв.ч., муж.род)', 'jenis_ru': 'Маусуль Хасс'},
    '2. Mawshul__10': {'arti_ru': 'КАКАЯ БЫ НИ (ЖЕН. Р.)', 'desc_ru': 'Какая бы ни (Относительное местоимение жен. рода)', 'jenis_ru': 'Маусуль Мубхам'},

    # 3. Istifham
    '3. Istifham__1': {'arti_ru': 'ЧТО? / ЧТО ЭТО?', 'desc_ru': 'Что? (Вопросительное местоимение для неодушевленных)', 'jenis_ru': 'Исм Истифхам'},
    '3. Istifham__2': {'arti_ru': 'КАК? / КАКИМ ОБРАЗОМ?', 'desc_ru': 'Как? (Вопросительное слово о состоянии или образе действия)', 'jenis_ru': 'Исм Истифхам'},
    '3. Istifham__3': {'arti_ru': 'КТО?', 'desc_ru': 'Кто? (Вопросительное местоимение для разумных существ)', 'jenis_ru': 'Исм Истифхам'},
    '3. Istifham__4': {'arti_ru': 'КОТОРЫЙ? / КАКОЙ?', 'desc_ru': 'Который? Какой? (Склоняемое вопросительное местоимение)', 'jenis_ru': 'Исм Истифхам'},
    '3. Istifham__5': {'arti_ru': 'КАК? / ОТКУДА? / КОГДА?', 'desc_ru': 'Как? Откуда? Когда? (Вопросительное слово об источнике/образе)', 'jenis_ru': 'Исм Истифхам'},
    '3. Istifham__6': {'arti_ru': 'ЧТО ЖЕ ЭТО, ЧТО..?', 'desc_ru': 'Что же такое, что..? (Составное вопросительное слово Mā + Dzā)', 'jenis_ru': 'Исм Истифхам'},
    '3. Istifham__7': {'arti_ru': 'СКОЛЬКО? / КАК ДОЛГО?', 'desc_ru': 'Сколько? Как долго? (Вопрос о количестве или времени)', 'jenis_ru': 'Исм Истифхам'},
    '3. Istifham__8': {'arti_ru': 'ПОЧЕМУ? / ЗАЧЕМ?', 'desc_ru': 'Почему? Зачем? Для чего? (Li + Ma)', 'jenis_ru': 'Исм Истифхам'},
    '3. Istifham__9': {'arti_ru': 'ГДЕ? / КУДА?', 'desc_ru': 'Где? Куда? (Вопросительное слово о месте)', 'jenis_ru': 'Исм Истифхам'},
    '3. Istifham__10': {'arti_ru': 'КОГДА?', 'desc_ru': 'Когда? (Вопросительное слово о времени)', 'jenis_ru': 'Исм Истифхам'},

    # 4. Syarath
    '4. Syarath__1': {'arti_ru': 'КТО БЫ НИ / ВСЯКИЙ, КТО', 'desc_ru': 'Кто бы ни (Усекающая условная частица для разумных)', 'jenis_ru': 'Исм Шарат Джазим'},
    '4. Syarath__2': {'arti_ru': 'ЧТО БЫ НИ / ВСЁ, ЧТО', 'desc_ru': 'Что бы ни (Усекающая условная частица для неодушевленных)', 'jenis_ru': 'Исм Шарат Джазим'},
    '4. Syarath__3': {'arti_ru': 'КАЖДЫЙ РАЗ, КОГДА', 'desc_ru': 'Каждый раз, когда / всякий раз (Условная временная частица)', 'jenis_ru': 'Исм Шарат Гайр Джазим'},
    '4. Syarath__4': {'arti_ru': 'КАКОЙ БЫ НИ / КОГО БЫ НИ', 'desc_ru': 'Какой бы ни (Склоняемая условная частица)', 'jenis_ru': 'Исм Шарат Джазим'},
    '4. Syarath__5': {'arti_ru': 'КАКОЙ БЫ НИ (УСИЛИТЕЛЬНОЕ)', 'desc_ru': 'Какой бы ни (Условная частица с усилительной частицей Mā)', 'jenis_ru': 'Исм Шарат Джазим'},

    # 5. Isyarah
    '5. Isyarah__1': {'arti_ru': 'ЭТОТ / ТОТ (МУЖ. Р. 1)', 'desc_ru': 'Этот / тот (Указательное местоимение ед.ч. муж. рода)', 'jenis_ru': 'Исм Ишара'},
    '5. Isyarah__2': {'arti_ru': 'ЭТИ / ТЕ (МН. Ч.)', 'desc_ru': 'Эти / те (Указательное местоимение множественного числа)', 'jenis_ru': 'Исм Ишара'},
    '5. Isyarah__3': {'arti_ru': 'ЭТА / ТА (ЖЕН. Р. 1)', 'desc_ru': 'Эта / та (Указательное местоимение ед.ч. жен. рода)', 'jenis_ru': 'Исм Ишара'},
    '5. Isyarah__4': {'arti_ru': 'ТА / ТЕ (ЖЕН. Р. / МН. Ч. НЕОДУШ.)', 'desc_ru': 'Та / те (Указательное местоимение далекого расстояния / мн.ч.)', 'jenis_ru': 'Исм Ишара'},
    '5. Isyarah__5': {'arti_ru': 'ЗДЕСЬ / ТУТ', 'desc_ru': 'Здесь (Указательное слово близкого места)', 'jenis_ru': 'Исм Ишара Макан'},
    '5. Isyarah__6': {'arti_ru': 'ТАМ / ТУДА', 'desc_ru': 'Там / туда (Указательное слово далекого места)', 'jenis_ru': 'Исм Ишара Макан'},
    '5. Isyarah__7': {'arti_ru': 'ЭТИ ДВОЕ (МУЖ. Р.)', 'desc_ru': 'Эти двое (Указательное местоимение дв.ч. муж. рода)', 'jenis_ru': 'Исм Ишара'},
    '5. Isyarah__8': {'arti_ru': 'ЭТИ/ТЕ ДВЕ (ЖЕН. Р.)', 'desc_ru': 'Эти / те две (Указательное местоимение дв.ч. жен. рода)', 'jenis_ru': 'Исм Ишара'},

    # 6. Isim Fi'il
    '6. Isim Fi\'il__1': {'arti_ru': 'ПРЕЧИСТ / СЛАВА АЛЛАХУ (ТАСБИХ)', 'desc_ru': 'Пречист Аллах (Масдар со значением восхваления и очищения)', 'jenis_ru': "Исм Фииль / Масдар"},
    '6. Isim Fi\'il__2': {'arti_ru': 'ПРЕДОСТАВЬТЕ / ПРИВЕДИТЕ', 'desc_ru': 'Приведите доказательство (Глагольное имя повелительного наклонения)', 'jenis_ru': "Исм Фииль Амр"},
    '6. Isim Fi\'il__3': {'arti_ru': 'ТЬФУ! / УФ! / ГОРЕ ВАМ!', 'desc_ru': 'Выражение крайнего отвращения и досады (Исм Фииль Мудари\')', 'jenis_ru': "Исм Фииль Мудари'"},
    '6. Isim Fi\'il__4': {'arti_ru': 'УПАСИ АЛЛАХ / ДА СОХРАНИТ АЛЛАХ', 'desc_ru': 'Ищу защиты у Аллаха (Ма\'азаллах)', 'jenis_ru': "Исм Фииль / Масдар"},
    '6. Isim Fi\'il__5': {'arti_ru': 'ИДИТЕ СЮДА! / ДАВАЙТЕ СЮДА!', 'desc_ru': 'Идите сюда / несите сюда (Исм Фииль Амр)', 'jenis_ru': "Исм Фииль Амр"},
    '6. Isim Fi\'il__6': {'arti_ru': 'КАК ДАЛЕКО! / НЕВОЗМОЖНО!', 'desc_ru': 'Как далеко / невероятно (Глагольное имя прошедшего времени)', 'jenis_ru': "Исм Фииль Мади"},
    '6. Isim Fi\'il__7': {'arti_ru': 'ВОТ, ВОЗЬМИТЕ И ЧИТАЙТЕ!', 'desc_ru': 'Возьмите и прочтите это (Исм Фииль Амр)', 'jenis_ru': "Исм Фииль Амр"},
    '6. Isim Fi\'il__8': {'arti_ru': 'ИДИ ЖЕ СЮДА! / СКОРЕЕ!', 'desc_ru': 'Подойди скорее (Исм Фииль Амр)', 'jenis_ru': "Исм Фииль Амр"},

    # 7. Fi'il Jamid
    '7. Fi\'il Jamid__1': {'arti_ru': 'НЕ ЯВЛЯЕТСЯ / НЕТ', 'desc_ru': 'Не является / нет (Неизменяемый глагол отрицания)', 'jenis_ru': "Фииль Мади Джамид"},
    '7. Fi\'il Jamid__2': {'arti_ru': 'КАК СКВЕРЕН... / ХУДШИЙ', 'desc_ru': 'Как скверен (Неизменяемый глагол порицания / Аз-Замм)', 'jenis_ru': "Фииль Мади Джамид"},
    '7. Fi\'il Jamid__3': {'arti_ru': 'БЫТЬ МОЖЕТ / ВОЗМОЖНО', 'desc_ru': 'Быть может / возможно (Неизменяемый глагол надежды / Тараджи)', 'jenis_ru': "Фииль Мади Джамид"},
    '7. Fi\'il Jamid__4': {'arti_ru': 'КАК ПРЕКРАСЕН... / ЛУЧШИЙ', 'desc_ru': 'Как прекрасен (Неизменяемый глагол похвалы / Аль-Мадх)', 'jenis_ru': "Фииль Мади Джамид"},
    '7. Fi\'il Jamid__5': {'arti_ru': 'КАК СКВЕРНО ТО, ЧТО...', 'desc_ru': 'Как скверно то, что (Bi\'sa + Ma)', 'jenis_ru': "Фииль Мади Джамид"},
    '7. Fi\'il Jamid__6': {'arti_ru': 'ОНИ СТАЛИ / ПРИНЯЛИСЬ', 'desc_ru': 'Принялись делать / начали (Глагол начинания / Афаль аш-Шуру\')', 'jenis_ru': "Фииль Мади Джамид"},
    '7. Fi\'il Jamid__7': {'arti_ru': 'ПРЕЧИСТ АЛЛАХ / УПАСИ БОГ', 'desc_ru': 'Пречист Аллах от всякого недостатка (Танзих)', 'jenis_ru': "Фииль Джамид"},
    '7. Fi\'il Jamid__8': {'arti_ru': 'КАК ПРЕКРАСНО ТО, ЧЕМ...', 'desc_ru': 'Как прекрасно то, что (Ni\'ma + Ma)', 'jenis_ru': "Фииль Мади Джамид"}
}

# Read build_multilingual_dataset.py
with open(bmd_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Let's dynamically rewrite build_multilingual_dataset.py cleanly
# 1. Update SURAHS lines to include 'arti_ru': '...'
new_lines = []
in_surahs = False
in_bentuk = False
in_grammar = False

for line in lines:
    # Check SURAHS line: 1: {'nama': ..., 'arti_bn': '...', 'ayat': ...}
    if line.strip().startswith('1: {\'nama\':'):
        in_surahs = True
    
    if in_surahs:
        # Check if line has surah definition
        import re
        m = re.match(r'^\s*(\d+):\s*\{(.+)\},\s*$', line)
        if m:
            s_num = int(m.group(1))
            body = m.group(2)
            ru_val = SURAH_RU.get(s_num, '')
            # If arti_ru not yet in body
            if "'arti_ru':" not in body:
                # insert before 'ayat':
                body = body.replace("'ayat':", f"'arti_ru': {json.dumps(ru_val, ensure_ascii=False)}, 'ayat':")
                line = f"    {s_num}: {{{body}}},\n"
        if line.strip().startswith('114:'):
            in_surahs = False

    # Check BENTUK_LABELS
    if line.strip().startswith("'bn': '১. সর্বনাম (Dhamir - Pronouns)'"):
        line = line.rstrip() + ",\n        'ru': '1. Местоимения (Дамир / Dhamir)'\n"
    elif line.strip().startswith("'bn': '২. সম্বন্ধবাচক সর্বনাম (Mawshul - Relative Pronouns)'"):
        line = line.rstrip() + ",\n        'ru': '2. Относительные местоимения (Маусуль / Mawshul)'\n"
    elif line.strip().startswith("'bn': '৩. প্রশ্নবোধক শব্দ (Istifham - Interrogatives)'"):
        line = line.rstrip() + ",\n        'ru': '3. Вопросительные слова (Истифхам / Istifham)'\n"
    elif line.strip().startswith("'bn': '৪. শর্তমূলক শব্দ (Syarath - Conditionals)'"):
        line = line.rstrip() + ",\n        'ru': '4. Условные частицы (Шарат / Syarath)'\n"
    elif line.strip().startswith("'bn': '৫. নির্দেশক সর্বনাম (Isyarah - Demonstratives)'"):
        line = line.rstrip() + ",\n        'ru': '5. Указательные местоимения (Ишара / Isyarah)'\n"
    elif line.strip().startswith("'hi': \"६. क्रियार्थक संज्ञा (Isim Fi'il)\""):
        line = line.rstrip() + ",\n        'bn': \"৬. ক্রিয়াভিত্তিক বিশেষ্য (Isim Fi'il - Verbal Nouns)\",\n        'ru': \"6. Именные глаголы (Исм Фииль / Isim Fi'il)\"\n"
    elif line.strip().startswith("'hi': \"७. रूढ़ क्रियाएं (Fi'il Jamid)\""):
        line = line.rstrip() + ",\n        'bn': \"৭. অপরিবর্তনীয় ক্রিয়া (Fi'il Jamid - Inflexible Verbs)\",\n        'ru': \"7. Неизменяемые глаголы (Фииль Джамид / Fi'il Jamid)\"\n"

    # Check GRAMMATICAL_METADATA lines
    if "GRAMMATICAL_METADATA = {" in line:
        in_grammar = True
    if in_grammar and line.strip().startswith("'"):
        # Match key like '1. Dhamir__1a': {...}
        import re
        m = re.match(r"^\s*'([^']+)':\s*\{(.+)\},\s*$", line)
        if m:
            g_key = m.group(1)
            g_body = m.group(2)
            if g_key in GRAMMAR_RU:
                ru_meta = GRAMMAR_RU[g_key]
                ru_arti = ru_meta['arti_ru']
                ru_desc = ru_meta['desc_ru']
                ru_jenis = ru_meta['jenis_ru']
                if "'arti_ru':" not in g_body:
                    # Insert arti_ru before 'desc_id':
                    if "'desc_id':" in g_body:
                        g_body = g_body.replace("'desc_id':", f"'arti_ru': {json.dumps(ru_arti, ensure_ascii=False)}, 'desc_ru': {json.dumps(ru_desc, ensure_ascii=False)}, 'jenis_ru': {json.dumps(ru_jenis, ensure_ascii=False)}, 'desc_id':")
                    else:
                        g_body += f", 'arti_ru': {json.dumps(ru_arti, ensure_ascii=False)}, 'desc_ru': {json.dumps(ru_desc, ensure_ascii=False)}, 'jenis_ru': {json.dumps(ru_jenis, ensure_ascii=False)}"
                    line = f"    '{g_key}': {{{g_body}}},\n"
    if in_grammar and line.strip() == "}":
        in_grammar = False

    new_lines.append(line)

code = "".join(new_lines)

# Update load_caches, editions, enriched_list
code = code.replace(
    "'bn': {}\n    }",
    "'bn': {},\n        'ru': {}\n    }"
)
code = code.replace(
    "'bn': 'bn_translations.json'\n    }",
    "'bn': 'bn_translations.json',\n        'ru': 'ru_translations.json'\n    }"
)
code = code.replace(
    "item['BentukKataBN'] = b_labels.get('bn', b)",
    "item['BentukKataBN'] = b_labels.get('bn', b)\n        item['BentukKataRU'] = b_labels.get('ru', b)"
)
code = code.replace(
    "item['SuratArtiBN'] = s_info.get('arti_bn', '')",
    "item['SuratArtiBN'] = s_info.get('arti_bn', '')\n            item['SuratArtiRU'] = s_info.get('arti_ru', '')"
)
code = code.replace(
    "item['SuratArtiBN'] = \"\"",
    "item['SuratArtiBN'] = \"\"\n            item['SuratArtiRU'] = \"\""
)
code = code.replace(
    "item['ArtiKataBN'] = gm.get('arti_bn', item['Arti kata'])",
    "item['ArtiKataBN'] = gm.get('arti_bn', item['Arti kata'])\n        item['ArtiKataRU'] = gm.get('arti_ru', item['Arti kata'])"
)
code = code.replace(
    "# BN\n        item['TeksArtiBN'] = caches['bn'].get(v_key, teks_id)",
    "# BN\n        item['TeksArtiBN'] = caches['bn'].get(v_key, teks_id)\n\n        # RU\n        item['TeksArtiRU'] = caches['ru'].get(v_key, teks_id)"
)
code = code.replace(
    "langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN']",
    "langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN', 'RU']"
)
code = code.replace(
    "8 Bahasa: Indonesia 🇮🇩, English 🇬🇧, Melayu 🇲🇾, Français 🇫🇷, Deutsch 🇩🇪, Urdu 🇵🇰, Hindi 🇮🇳, Bangla 🇧🇩",
    "9 Bahasa: Indonesia 🇮🇩, English 🇬🇧, Melayu 🇲🇾, Français 🇫🇷, Deutsch 🇩🇪, Urdu 🇵🇰, Hindi 🇮🇳, Bangla 🇧🇩, Русский 🇷🇺"
)
code = code.replace(
    "Jalandhry, Farooq, Muhiuddin Khan & EveryAyah",
    "Jalandhry, Farooq, Muhiuddin Khan, Elmir Kuliev & EveryAyah"
)

with open(bmd_path, 'w', encoding='utf-8') as f:
    f.write(code)

print(f"[OK] Updated {bmd_path} with Russian support!")
