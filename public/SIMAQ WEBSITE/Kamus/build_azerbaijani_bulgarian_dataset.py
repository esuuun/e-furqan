#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Azerbaijani (az) and Bulgarian (bg) Dataset Metadata & Enricher:
- 114 Surah Names for Azerbaijani & Bulgarian
- 7 Bentuk Kata Categories for Azerbaijani & Bulgarian
- 76 Jamid Mabny Grammar details for Azerbaijani & Bulgarian
- 17 Bentuk Harf Categories for Azerbaijani & Bulgarian
- 52 Harf Grammar details for Azerbaijani & Bulgarian
"""

import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AZERBAIJANI_SURAHS = {
    "1": "əl-Fatihə (Kitabı açan)",
    "2": "əl-Bəqərə (Inək)",
    "3": "Ali-İmran (İmran ailəsi)",
    "4": "ən-Nisa (Qadınlar)",
    "5": "əl-Maidə (Süfrə)",
    "6": "əl-Ənam (Dördayaqlılar)",
    "7": "əl-Əraf (Sədd)",
    "8": "əl-Ənfal (Qənimət)",
    "9": "ət-Tövbə (Tövbə)",
    "10": "Yunus (Yunus peyğəmbər)",
    "11": "Hud (Hud peyğəmbər)",
    "12": "Yusuf (Yusuf peyğəmbər)",
    "13": "ər-Rəd (Göy gurultusu)",
    "14": "İbrahim (İbrahim peyğəmbər)",
    "15": "əl-Hicr (Daşlı sahə)",
    "16": "ən-Nəhl (Bal arısı)",
    "17": "əl-İsra (Gecə vaxtı seyr)",
    "18": "əl-Kəhf (Mağara)",
    "19": "Məryəm (Məryəm)",
    "20": "Ta ha (Taha)",
    "21": "əl-Ənbiya (Peyğəmbərlər)",
    "22": "əl-Həcc (Həcc)",
    "23": "əl-Muminun (Möminlər)",
    "24": "ən-Nur (Nur)",
    "25": "əl-Furqan (Haqqı batildən ayıran)",
    "26": "əş-Şüəra (Şairlər)",
    "27": "ən-Nəml (Qarışqa)",
    "28": "əl-Qəsəs (Hekayət)",
    "29": "əl-Ənkəbut (Hörümçək)",
    "30": "ər-Rum (Rumlular)",
    "31": "Loğman (Loğman)",
    "32": "əs-Səcdə (Səcdə)",
    "33": "əl-Əhzab (Dəstələr)",
    "34": "Səba (Səba)",
    "35": "əl-Fatir (Yaradan)",
    "36": "Ya Sin (Yasin)",
    "37": "əs-Saffat (Səf-səf duranlar)",
    "38": "Sad (Sad)",
    "39": "əz-Zümər (Zümrələr)",
    "40": "əl-Mumin (Mömin / Qafir)",
    "41": "Fussilət (Müfəssəl izah edilmiş)",
    "42": "əş-Şura (Şura)",
    "43": "əz-Zuxruf (Qızıl bəzəklər)",
    "44": "əd-Duxan (Duman)",
    "45": "əl-Casiyə (Diz çökmüş camaat)",
    "46": "əl-Əhqaf (Qum təpələri)",
    "47": "Məhəmməd (Məhəmməd peyğəmbər)",
    "48": "əl-Fəth (Qələbə)",
    "49": "əl-Hucurat (Otaqlar)",
    "50": "Qaf (Qaf)",
    "51": "əz-Zariyat (Toz sovuran küləklər)",
    "52": "ət-Tur (Tur dağı)",
    "53": "ən-Nəcm (Ulduz)",
    "54": "əl-Qəmər (Ay)",
    "55": "ər-Rəhman (Rəhmli olan)",
    "56": "əl-Vaqiə (Vaqiə / Qiyamət)",
    "57": "əl-Hədid (Dəmir)",
    "58": "əl-Mücadilə (Mübahisə edən qadın)",
    "59": "əl-Həşr (Toplanma)",
    "60": "əl-Mumtəhinə (İmtahana çəkilən qadın)",
    "61": "əs-Səff (Səf)",
    "62": "əl-Cümə (Cümə)",
    "63": "əl-Munafiqun (Münafiqlər)",
    "64": "ət-Təğabun (Qarşılıqlı aldanma)",
    "65": "ət-Talaq (Boşanma)",
    "66": "ət-Təhrim (Qadağan etmə)",
    "67": "əl-Mülk (Mülk)",
    "68": "əl-Qələm (Qələm)",
    "69": "əl-Haqqə (Haqq olan qiyamət)",
    "70": "əl-Məaric (Dərəcələr)",
    "71": "Nuh (Nuh peyğəmbər)",
    "72": "əl-Cinn (Cinlər)",
    "73": "əl-Müzzəmmil (Örtüyə bürünmüş)",
    "74": "əl-Müddəssir (Bürünən)",
    "75": "əl-Qiyamə (Qiyamət)",
    "76": "əl-İnsan (İnsan)",
    "77": "əl-Mursəlat (Göndərilənlər)",
    "78": "ən-Nəbə (Böyük xəbər)",
    "79": "ən-Naziat (Can alanlar)",
    "80": "Əbəsə (Qaşqabağını tökdü)",
    "81": "ət-Təkvir (Bükülmə)",
    "82": "əl-İnfitar (Yarılma)",
    "83": "əl-Mutəffifin (Çəkidə aldadanlar)",
    "84": "əl-İnşiqaq (Parçalanma)",
    "85": "əl-Buruc (Bürclər)",
    "86": "ət-Tariq (Gecə gələn)",
    "87": "əl-Əla (Ən uca)",
    "88": "əl-Ğaşiyə (Bürüyən qiyamət)",
    "89": "əl-Fəcr (Dan yeri)",
    "90": "əl-Bələd (Şəhər)",
    "91": "əş-Şəms (Günəş)",
    "92": "əl-Leyl (Gecə)",
    "93": "əz-Zuha (Səhər vaxtı)",
    "94": "əl-İnşirah (Açılma)",
    "95": "ət-Tin (Əncir)",
    "96": "əl-Ələq (Laxtalanmış qan)",
    "97": "əl-Qədr (Qədr gecəsi)",
    "98": "əl-Bəyyinə (Aydın dəlil)",
    "99": "əz-Zəlzələ (Zəlzələ)",
    "100": "əl-Adiyat (Qaçan atlar)",
    "101": "əl-Qariə (Ürəkləri qorxuya salan)",
    "102": "ət-Təkasur (Çoxluqla öyünmə)",
    "103": "əl-Əsr (Əsr / Zaman)",
    "104": "əl-Huməzə (Qeybətçilər)",
    "105": "əl-Fil (Fil)",
    "106": "Qureyş (Qureyş qəbiləsi)",
    "107": "əl-Maun (Xırda kömək)",
    "108": "əl-Kövsər (Kövsər)",
    "109": "əl-Kafirun (Kafirlər)",
    "110": "ən-Nəsr (Kömək)",
    "111": "əl-Məsəd (Xurma lifi)",
    "112": "əl-İxlas (Təmiz etiqad)",
    "113": "əl-Fələq (Sübh)",
    "114": "ən-Nas (İnsanlar)"
}

BULGARIAN_SURAHS = {
    "1": "Ал-Фатиха (Откриващата)",
    "2": "Ал-Бакара (Кравата)",
    "3": "Ал-Имран (Родът на Имран)",
    "4": "Ан-Ниса (Жените)",
    "5": "Ал-Маида (Трапезата)",
    "6": "Ал-Анам (Добитъкът)",
    "7": "Ал-Араф (Стената)",
    "8": "Ал-Анфал (Трофеите)",
    "9": "Ат-Тауба (Покаянието)",
    "10": "Юнус (Пророкът Юнус)",
    "11": "Худ (Пророкът Худ)",
    "12": "Юсуф (Пророкът Юсуф)",
    "13": "Ар-Раад (Гърмът)",
    "14": "Ибрахим (Пророкът Ибрахим)",
    "15": "Ал-Хиджр (Каменната долина)",
    "16": "Ан-Нахл (Пчелите)",
    "17": "Ал-Исра (Нощното пътешествие)",
    "18": "Ал-Кахф (Пещерата)",
    "19": "Мариам (Мария)",
    "20": "Та-ха (Та-ха)",
    "21": "Ал-Анбия (Пророците)",
    "22": "Ал-Хадж (Поклонението)",
    "23": "Ал-Муминун (Вярващите)",
    "24": "Ан-Нур (Светлината)",
    "25": "Ал-Фуркан (Разграничението)",
    "26": "Аш-Шуара (Поетите)",
    "27": "Ан-Намл (Мравките)",
    "28": "Ал-Касас (Разказът)",
    "29": "Ал-Анкабут (Паякът)",
    "30": "Ар-Рум (Ромеите)",
    "31": "Лукман (Лукман)",
    "32": "Ас-Саджда (Поклона)",
    "33": "Ал-Ахзаб (Съюзниците)",
    "34": "Саба (Сава)",
    "35": "Фатир (Сътворителят)",
    "36": "Йа Син (Йа Син)",
    "37": "Ас-Саффат (Строените в редици)",
    "38": "Сад (Сад)",
    "39": "Аз-Зумар (Тълпите)",
    "40": "Гафир (Опрощаващият)",
    "41": "Фуссилат (Разяснените)",
    "42": "Аш-Шура (Съвещанието)",
    "43": "Аз-Зухруф (Украсата)",
    "44": "Ад-Духан (Димът)",
    "45": "Ал-Джасийа (Коленичилата)",
    "46": "Ал-Ахкаф (Пясъчните хълмове)",
    "47": "Мухаммад (Пророкът Мухаммад)",
    "48": "Ал-Фатх (Победата)",
    "49": "Ал-Худжурат (Стаите)",
    "50": "Каф (Каф)",
    "51": "Аз-Зарийат (Разпръскващите)",
    "52": "Ат-Тур (Планината)",
    "53": "Ан-Наджм (Звездата)",
    "54": "Ал-Камар (Луната)",
    "55": "Ар-Рахман (Всемилостивият)",
    "56": "Ал-Уакиа (Неизбежното събитие)",
    "57": "Ал-Хадид (Желязото)",
    "58": "Ал-Муджадала (Препиращата се)",
    "59": "Ал-Хашр (Събирането)",
    "60": "Ал-Мумтахана (Изпитваната)",
    "61": "Ас-Сафф (Редицата)",
    "62": "Ал-Джумуа (Петък)",
    "63": "Ал-Мунафикун (Лицемерите)",
    "64": "Ат-Тагабун (Взаимното надхитряне)",
    "65": "Ат-Талак (Разводът)",
    "66": "Ат-Тахрим (Възбраната)",
    "67": "Ал-Мулк (Владението)",
    "68": "Ал-Калам (Калемът)",
    "69": "Ал-Хакка (Неизбежният час)",
    "70": "Ал-Мааридж (Степените)",
    "71": "Нух (Пророкът Нух)",
    "72": "Ал-Джинн (Джиновете)",
    "73": "Ал-Муззаммил (Завитият)",
    "74": "Ал-Муддассир (Покритият)",
    "75": "Ал-Кийама (Възкресението)",
    "76": "Ал-Инсан (Човекът)",
    "77": "Ал-Мурсалат (Изпращаните)",
    "78": "Ан-Наба (Вестта)",
    "79": "Ан-Назиат (Изтръгващите)",
    "80": "Абаса (Той се намръщи)",
    "81": "Ат-Такуир (Потъмняването)",
    "82": "Ал-Инфитар (Разпукването)",
    "83": "Ал-Мутаффифин (Мамещите в мярката)",
    "84": "Ал-Иншикак (Разцепването)",
    "85": "Ал-Бурудж (Съзвездията)",
    "86": "Ат-Тарик (Нощната звезда)",
    "87": "Ал-Ала (Всевишният)",
    "88": "Ал-Гашийа (Покриващото бедствие)",
    "89": "Ал-Фаджр (Зората)",
    "90": "Ал-Балад (Градът)",
    "91": "Аш-Шамс (Слънцето)",
    "92": "Ал-Лайл (Нощта)",
    "93": "Ад-Духа (Утрото)",
    "94": "Аш-Шарх (Разтварянето)",
    "95": "Ат-Тин (Смокинята)",
    "96": "Ал-Алак (Съсирекът)",
    "97": "Ал-Кадр (Могъществото)",
    "98": "Ал-Баййина (Ясният знак)",
    "99": "Аз-Залзала (Земетресението)",
    "100": "Ал-Адийат (Препускащите коне)",
    "101": "Ал-Кариа (Поразяващото бедствие)",
    "102": "Ат-Такасур (Стремежът към трупане)",
    "103": "Ал-Аср (Следобедът)",
    "104": "Ал-Хумаза (Клеветникът)",
    "105": "Ал-Фил (Слонът)",
    "106": "Курайш (Курайшите)",
    "107": "Ал-Маун (Добрината)",
    "108": "Ал-Каусар (Изобилието)",
    "109": "Ал-Кафирун (Неверниците)",
    "110": "Ан-Наср (Подкрепата)",
    "111": "Ал-Масад (Палещите влакна)",
    "112": "Ал-Ихлас (Пречистването)",
    "113": "Ал-Фалак (Разсъмването)",
    "114": "Ан-Нас (Хората)"
}

BENTUK_KATA_AZ = {
    "1. Dhamir": "1. Əvəzliklər (Zəmir / Dhamir)",
    "2. Isim Mawshul": "2. Nisbi Əvəzliklər (İsmi Mövsul / Mawshul)",
    "3. Isim Istifham": "3. Sual Əvəzlikləri (İsmi İstifham)",
    "4. Isim Syarath": "4. Şərt Əvəzlikləri (İsmi Şərt)",
    "5. Isim Isyarah": "5. İşarə Əvəzlikləri (İsmi İşarə)",
    "6. Isim Fi'il": "6. Feili İsimlər (İsmi Feil / Isim Fi'il)",
    "7. Fi'il Jamid": "7. Təsriflənməyən Feillər (Feili Camid / Fi'il Jamid)"
}

BENTUK_KATA_BG = {
    "1. Dhamir": "1. Местоимения (Дамир / Dhamir)",
    "2. Isim Mawshul": "2. Относителни местоимения (Маусул / Mawshul)",
    "3. Isim Istifham": "3. Въпросителни думи (Истифхам / Istifham)",
    "4. Isim Syarath": "4. Условни думи (Шарат / Syarath)",
    "5. Isim Isyarah": "5. Показателни местоимения (Ишара / Isyarah)",
    "6. Isim Fi'il": "6. Глаголни имена (Исм ал-фи'л / Isim Fi'il)",
    "7. Fi'il Jamid": "7. Неизменяеми глаголи (Фи'л Джамид / Fi'il Jamid)"
}

BENTUK_HARF_AZ = {
    "1. Harf Nafyi": "1. Inkar Ədatları (Hərfi Nəfy / Harf Nafy)",
    "2. Harf Tahqiq Taswif": "2. Təhqiq və Gələcək Zaman Ədatları (Tahqiq & Taswif)",
    "3. Harf Syarat": "3. Əməlsiz Şərt Ədatları (Hərfi Şərt / Harf Syarat)",
    "4. Harf Mashdariyah": "4. Məsdər Ədatları (Hərfi Məsdəriyyə / Harf Mashdariyah)",
    "5. Harf Zaidah": "5. Qüvvətləndirici Əlavə Ədatlar (Hərfi Zaidə / Harf Zaidah)",
    "6. Harf Istifham": "6. Sual Ədatları (Hərfi İstifham / Harf Istifham)",
    "7. Harf Istitsna": "7. İstisna Ədatları (Hərfi İstisna / Harf Istitsna)",
    "8. Harf Rad'in Wazajrin": "8. Çəkindirmə və Qadağan Ədatları (Hərfi Rəd / Harf Rad'in)",
    "9. Harf Rad'in Tahdid": "9. Təhrik və Qınama Ədatları (Hərfi Təhdid / Harf Tahdid)",
    "10. Harf Ijab": "10. Cavab və Təsdiq Ədatları (Hərfi İcab / Harf Ijab)",
    "11. Harf Tafsir": "11. İzah və Təfsir Ədatları (Hərfi Təfsir / Harf Tafsir)",
    "12. Harf Tanbih": "12. Xəbərdarlıq və Diqqət Ədatları (Hərfi Tənbeh / Harf Tanbih)",
    "13. Harf Ta'lil": "13. Səbəb Ədatları (Hərfi Təlil / Harf Ta'lil)",
    "14. Harf Fuja'iyyah": "14. Qəfil Başvermə Ədatları (Hərfi Fucaiyyə / Harf Fuja'iyyah)",
    "15. Harf Istidrak": "15. Düzəliş və İsdidrak Ədatları (Hərfi İstidrak / Harf Istidrak)",
    "16. Harf Ta'ajjub": "16. Təəccüb Ədatları (Hərfi Təəccüb / Harf Ta'ajjub)",
    "17. Harf Mabany": "17. Surə Başlanğıcı Hərfləri (Müqəttəat / Muqatta'at)"
}

BENTUK_HARF_BG = {
    "1. Harf Nafyi": "1. Отрицателни частици (Харф Нафи / Harf Nafy)",
    "2. Harf Tahqiq Taswif": "2. Частици за потвърждение и бъдеще (Тахкик и Тасвиф)",
    "3. Harf Syarat": "3. Неуправляващи условни частици (Харф Шарт / Harf Syarat)",
    "4. Harf Mashdariyah": "4. Масдарни / отглаголни частици (Харф Масдарийя)",
    "5. Harf Zaidah": "5. Подсилващи допълнителни частици (Харф Заида / Harf Zaidah)",
    "6. Harf Istifham": "6. Въпросителни частици (Харф Истифхам / Harf Istifham)",
    "7. Harf Istitsna": "7. Изключващи частици (Харф Истисна / Harf Istitsna)",
    "8. Harf Rad'in Wazajrin": "8. Възпиращи и порицаващи частици (Харф Рад' / Harf Rad'in)",
    "9. Harf Rad'in Tahdid": "9. Подбудителни и укоряващи частици (Харф Тахдид)",
    "10. Harf Ijab": "10. Частици за утвърдителен отговор (Харф Иджаб / Harf Ijab)",
    "11. Harf Tafsir": "11. Обяснителни частици (Харф Тафсир / Harf Tafsir)",
    "12. Harf Tanbih": "12. Частици за привличане на вниманието (Харф Танбих)",
    "13. Harf Ta'lil": "13. Причинни частици (Харф Та'лил / Harf Ta'lil)",
    "14. Harf Fuja'iyyah": "14. Частици за внезапно действие (Харф Фуджаийя)",
    "15. Harf Istidrak": "15. Коригиращи частици (Харф Истидрак / Harf Istidrak)",
    "16. Harf Ta'ajjub": "16. Частици за възклицание и удивление (Харф Та'аджуб)",
    "17. Harf Mabany": "17. Начални съкратени букви на сурите (Мукатта'ат)"
}

AZERBAIJANI_GRAMMAR = {
    "1. Dhamir__1a": {"arti_az": "O (3-cü şəxs kişi tək)", "desc_az": "3-cü şəxs kişi cinsi tək sərbəst adlıq əvəzliyi (Münfəsil)", "jenis_az": "Sərbəst adlıq əvəzliyi"},
    "1. Dhamir__1b": {"arti_az": "Onun / Ona / Onu (Bitişik)", "desc_az": "3-cü şəxs kişi cinsi tək bitişik əvəzlik (Müttəsil)", "jenis_az": "Bitişik əvəzlik"},
    "1. Dhamir__1c": {"arti_az": "Yalnız Ona (Sərbəst təsirlik)", "desc_az": "3-cü şəxs kişi cinsi tək sərbəst təsirlik əvəzliyi", "jenis_az": "Sərbəst təsirlik əvəzliyi"},
    "1. Dhamir__2a": {"arti_az": "O ikisi (Təsniyə)", "desc_az": "3-cü şəxs təsniyə (iki nəfər) sərbəst adlıq əvəzliyi", "jenis_az": "Sərbəst təsniyə əvəzliyi"},
    "1. Dhamir__2b": {"arti_az": "O ikisinin / O ikisinə (Bitişik)", "desc_az": "3-cü şəxs təsniyə bitişik əvəzlik", "jenis_az": "Bitişik təsniyə əvəzlik"},
    "1. Dhamir__3a": {"arti_az": "Onlar (Kişilər cəm)", "desc_az": "3-cü şəxs kişi cinsi cəm sərbəst adlıq əvəzliyi", "jenis_az": "Sərbəst cəm əvəzliyi"},
    "1. Dhamir__3b": {"arti_az": "Onların / Onlara (Bitişik)", "desc_az": "3-cü şəxs kişi cinsi cəm bitişik əvəzlik", "jenis_az": "Bitişik cəm əvəzlik"},
    "1. Dhamir__3c": {"arti_az": "Yalnız onlara", "desc_az": "3-cü şəxs kişi cinsi cəm sərbəst təsirlik əvəzliyi", "jenis_az": "Sərbəst təsirlik əvəzliyi"},
    "1. Dhamir__4a": {"arti_az": "O (Qadın tək)", "desc_az": "3-cü şəxs qadın cinsi tək sərbəst adlıq əvəzliyi", "jenis_az": "Sərbəst adlıq əvəzliyi"},
    "1. Dhamir__4b": {"arti_az": "Onun / Ona (Qadın bitişik)", "desc_az": "3-cü şəxs qadın cinsi tək bitişik əvəzlik", "jenis_az": "Bitişik əvəzlik"},
    "1. Dhamir__5a": {"arti_az": "Onlar (Qadınlar cəm)", "desc_az": "3-cü şəxs qadın cinsi cəm sərbəst adlıq əvəzliyi", "jenis_az": "Sərbəst qadın cəm əvəzliyi"},
    "1. Dhamir__5b": {"arti_az": "Onların (Qadınlar bitişik)", "desc_az": "3-cü şəxs qadın cinsi cəm bitişik əvəzlik", "jenis_az": "Bitişik qadın cəm əvəzlik"},
    "1. Dhamir__6a": {"arti_az": "Sən (Kişi tək)", "desc_az": "2-ci şəxs kişi cinsi tək sərbəst adlıq əvəzliyi", "jenis_az": "Sərbəst adlıq əvəzliyi"},
    "1. Dhamir__6b": {"arti_az": "Sənin / Sənə (Bitişik)", "desc_az": "2-ci şəxs kişi cinsi tək bitişik əvəzlik", "jenis_az": "Bitişik əvəzlik"},
    "1. Dhamir__6c": {"arti_az": "Yalnız Sənə (İbadətdə xüsusiləşdirmə)", "desc_az": "2-ci şəxs kişi cinsi tək sərbəst təsirlik əvəzliyi", "jenis_az": "Sərbəst təsirlik əvəzliyi"},
    "1. Dhamir__7a": {"arti_az": "Siz ikiniz (Təsniyə)", "desc_az": "2-ci şəxs təsniyə sərbəst adlıq əvəzliyi", "jenis_az": "Sərbəst təsniyə əvəzliyi"},
    "1. Dhamir__7b": {"arti_az": "Siz ikinizin (Bitişik)", "desc_az": "2-ci şəxs təsniyə bitişik əvəzlik", "jenis_az": "Bitişik təsniyə əvəzlik"},
    "1. Dhamir__8a": {"arti_az": "Sizlər (Kişilər cəm)", "desc_az": "2-ci şəxs kişi cinsi cəm sərbəst adlıq əvəzliyi", "jenis_az": "Sərbəst cəm əvəzliyi"},
    "1. Dhamir__8b": {"arti_az": "Sizin / Sizə (Bitişik)", "desc_az": "2-ci şəxs kişi cinsi cəm bitişik əvəzlik", "jenis_az": "Bitişik cəm əvəzlik"},
    "1. Dhamir__8c": {"arti_az": "Yalnız sizə", "desc_az": "2-ci şəxs kişi cinsi cəm sərbəst təsirlik əvəzliyi", "jenis_az": "Sərbəst təsirlik əvəzliyi"},
    "1. Dhamir__9a": {"arti_az": "Sən (Qadın tək)", "desc_az": "2-ci şəxs qadın cinsi tək sərbəst adlıq əvəzliyi", "jenis_az": "Sərbəst adlıq əvəzliyi"},
    "1. Dhamir__9b": {"arti_az": "Sənin / Sənə (Qadın bitişik)", "desc_az": "2-ci şəxs qadın cinsi tək bitişik əvəzlik", "jenis_az": "Bitişik əvəzlik"},
    "1. Dhamir__10a": {"arti_az": "Sizlər (Qadınlar cəm)", "desc_az": "2-ci şəxs qadın cinsi cəm sərbəst adlıq əvəzliyi", "jenis_az": "Sərbəst qadın cəm əvəzliyi"},
    "1. Dhamir__10b": {"arti_az": "Sizin (Qadınlar bitişik)", "desc_az": "2-ci şəxs qadın cinsi cəm bitişik əvəzlik", "jenis_az": "Bitişik qadın cəm əvəzlik"},
    "1. Dhamir__11a": {"arti_az": "Mən (1-ci şəxs tək)", "desc_az": "1-ci şəxs tək sərbəst adlıq əvəzliyi", "jenis_az": "Sərbəst adlıq əvəzliyi"},
    "1. Dhamir__11b": {"arti_az": "Mənim / Mənə (Bitişik)", "desc_az": "1-ci şəxs tək bitişik əvəzlik", "jenis_az": "Bitişik əvəzlik"},
    "1. Dhamir__11c": {"arti_az": "Yalnız mənə", "desc_az": "1-ci şəxs tək sərbəst təsirlik əvəzliyi", "jenis_az": "Sərbəst təsirlik əvəzliyi"},
    "1. Dhamir__12a": {"arti_az": "Biz (1-ci şəxs cəm)", "desc_az": "1-ci şəxs cəm sərbəst adlıq əvəzliyi", "jenis_az": "Sərbəst cəm əvəzliyi"},
    "1. Dhamir__12b": {"arti_az": "Bizim / Bizə (Bitişik)", "desc_az": "1-ci şəxs cəm bitişik əvəzlik", "jenis_az": "Bitişik cəm əvəzlik"},
    "1. Dhamir__12c": {"arti_az": "Yalnız bizə", "desc_az": "1-ci şəxs cəm sərbəst təsirlik əvəzliyi", "jenis_az": "Sərbəst təsirlik əvəzliyi"},

    "2. Isim Mawshul__1": {"arti_az": "O şey ki / Nə ki (Cansızlar üçün)", "desc_az": "Cansız və qeyri-şüuri varlıqlar üçün ümumi nisbi əvəzlik", "jenis_az": "Ümumi nisbi əvəzlik"},
    "2. Isim Mawshul__2": {"arti_az": "O kəslər ki / O kəslər (Kişilər cəm)", "desc_az": "Ağıllı varlıqlar (kişi cinsi cəm) üçün xüsusi nisbi əvəzlik", "jenis_az": "Xüsusi nisbi əvəzlik"},
    "2. Isim Mawshul__3": {"arti_az": "Kim ki / O kəs ki (Şüurlular üçün)", "desc_az": "İnsan və şüurlu varlıqlar üçün ümumi nisbi əvəzlik", "jenis_az": "Ümumi nisbi əvəzlik"},
    "2. Isim Mawshul__4": {"arti_az": "O kəs ki / O şey ki (Kişi tək)", "desc_az": "Kişi cinsi tək üçün xüsusi nisbi əvəzlik", "jenis_az": "Xüsusi nisbi əvəzlik"},
    "2. Isim Mawshul__5": {"arti_az": "Hansı biri / Hər kim", "desc_az": "İzafə olunan nisbi əvəzlik", "jenis_az": "Nisbi əvəzlik"},
    "2. Isim Mawshul__6": {"arti_az": "O qadın ki (Qadın tək)", "desc_az": "Qadın cinsi tək üçün xüsusi nisbi əvəzlik", "jenis_az": "Xüsusi nisbi əvəzlik"},
    "2. Isim Mawshul__7": {"arti_az": "O qadınlar ki (Qadınlar cəm)", "desc_az": "Qadın cinsi cəm üçün xüsusi nisbi əvəzlik", "jenis_az": "Xüsusi qadın nisbi əvəzliyi"},
    "2. Isim Mawshul__8": {"arti_az": "O qadınlar ki (Qadınlar cəm)", "desc_az": "Qadın cinsi cəm üçün xüsusi nisbi əvəzlik", "jenis_az": "Xüsusi qadın nisbi əvəzliyi"},
    "2. Isim Mawshul__9": {"arti_az": "O iki kəs ki (Kişilər təsniyə)", "desc_az": "Kişi cinsi təsniyə nisbi əvəzlik", "jenis_az": "Təsniyə nisbi əvəzlik"},
    "2. Isim Mawshul__10": {"arti_az": "Hansı biri (Qadın cinsi)", "desc_az": "Qadın cinsi nisbi əvəzlik", "jenis_az": "Nisbi əvəzlik"},

    "3. Isim Istifham__1": {"arti_az": "Nə? / Nədir?", "desc_az": "Cansız və qeyri-şüuri şeylər haqqında sual əvəzliyi", "jenis_az": "Sual əvəzliyi"},
    "3. Isim Istifham__2": {"arti_az": "Kim? / Kimdir?", "desc_az": "Şüurlu varlıqlar və şəxslər haqqında sual əvəzliyi", "jenis_az": "Sual əvəzliyi"},
    "3. Isim Istifham__3": {"arti_az": "Necə? / Nə cür?", "desc_az": "Hal və vəziyyət soruşan sual əvəzliyi", "jenis_az": "Hal sual əvəzliyi"},
    "3. Isim Istifham__4": {"arti_az": "Harada? / Haraya?", "desc_az": "Məkan soruşan sual əvəzliyi", "jenis_az": "Məkan sual əvəzliyi"},
    "3. Isim Istifham__5": {"arti_az": "Neçə? / Nə qədər?", "desc_az": "Say və miqdar soruşan sual əvəzliyi", "jenis_az": "Miqdar sual əvəzliyi"},
    "3. Isim Istifham__6": {"arti_az": "Nə vaxt? / Haçan?", "desc_az": "Zaman soruşan sual əvəzliyi", "jenis_az": "Zaman sual əvəzliyi"},
    "3. Isim Istifham__7": {"arti_az": "Nə vaxt olacaq? (Qiyamət kimi böyük zaman)", "desc_az": "Gələcəkdəki böyük hadisələr üçün zaman sual əvəzliyi", "jenis_az": "Zaman sual əvəzliyi"},
    "3. Isim Istifham__8": {"arti_az": "Haradan? / Necə oldu ki?", "desc_az": "Mənbə və səbəb soruşan sual əvəzliyi", "jenis_az": "Sual əvəzliyi"},

    "4. Isim Syarath__1": {"arti_az": "Hər kəs ki / Kim ki", "desc_az": "Şəxslər üçün iki feili cəzm edən şərt əvəzliyi", "jenis_az": "Cəzm edən şərt əvəzliyi"},
    "4. Isim Syarath__2": {"arti_az": "Hər nə ki / Nə etsəniz", "desc_az": "Cansızlar üçün iki feili cəzm edən şərt əvəzliyi", "jenis_az": "Cəzm edən şərt əvəzliyi"},
    "4. Isim Syarath__3": {"arti_az": "O zaman ki / Zamanında", "desc_az": "Gələcək üçün qeyri-cəzm edən zaman şərt ismi", "jenis_az": "Zaman şərt ismi"},
    "4. Isim Syarath__4": {"arti_az": "Hər nə qədər / Hər nə olsa", "desc_az": "Ümumilik bildirən iki feili cəzm edən şərt əvəzliyi", "jenis_az": "Cəzm edən şərt əvəzliyi"},
    "4. Isim Syarath__5": {"arti_az": "Harada olsanız / Harada ki", "desc_az": "Məkan bildirən cəzm edici şərt ismi", "jenis_az": "Məkan şərt ismi"},
    "4. Isim Syarath__6": {"arti_az": "Harada ki", "desc_az": "Məkan bildirən cəzm edici şərt ismi", "jenis_az": "Məkan şərt ismi"},
    "4. Isim Syarath__7": {"arti_az": "Hansı halda olursa olsun", "desc_az": "Hal bildirən şərt ismi", "jenis_az": "Hal şərt ismi"},
    "4. Isim Syarath__8": {"arti_az": "Hansı biri olursa olsun", "desc_az": "İzafə olunan cəzm edici şərt əvəzliyi", "jenis_az": "Cəzm edən şərt əvəzliyi"},

    "5. Isim Isyarah__1": {"arti_az": "O / O kitab (Uzaq kişi)", "desc_az": "Uzaq məsafəli tək kişi cinsi işarə əvəzliyi", "jenis_az": "Uzaq işarə əvəzliyi"},
    "5. Isim Isyarah__2": {"arti_az": "Bu (Yaxın kişi)", "desc_az": "Yaxın məsafəli tək kişi cinsi işarə əvəzliyi", "jenis_az": "Yaxın işarə əvəzliyi"},
    "5. Isim Isyarah__3": {"arti_az": "Bunlar (Yaxın cəm)", "desc_az": "Yaxın məsafəli cəm işarə əvəzliyi", "jenis_az": "Yaxın cəm işarə əvəzliyi"},
    "5. Isim Isyarah__4": {"arti_az": "Onlar / O kəslər (Uzaq cəm)", "desc_az": "Uzaq məsafəli cəm işarə əvəzliyi", "jenis_az": "Uzaq cəm işarə əvəzliyi"},
    "5. Isim Isyarah__5": {"arti_az": "Bu (Yaxın qadın)", "desc_az": "Yaxın məsafəli tək qadın cinsi işarə əvəzliyi", "jenis_az": "Yaxın qadın işarə əvəzliyi"},
    "5. Isim Isyarah__6": {"arti_az": "O (Uzaq qadın)", "desc_az": "Uzaq məsafəli tək qadın cinsi işarə əvəzliyi", "jenis_az": "Uzaq qadın işarə əvəzliyi"},
    "5. Isim Isyarah__7": {"arti_az": "Orada / O yerdə", "desc_az": "Uzaq məkan bildirən işarə əvəzliyi", "jenis_az": "Məkan işarə əvəzliyi"},
    "5. Isim Isyarah__8": {"arti_az": "Burada / Bu yerdə", "desc_az": "Yaxın məkan bildirən işarə əvəzliyi", "jenis_az": "Məkan işarə əvəzliyi"},
    "5. Isim Isyarah__9": {"arti_az": "O ikisi (Uzaq kişi təsniyə)", "desc_az": "Uzaq kişi cinsi təsniyə işarə əvəzliyi", "jenis_az": "Uzaq təsniyə işarə əvəzliyi"},
    "5. Isim Isyarah__10": {"arti_az": "O ikisi (Uzaq qadın təsniyə)", "desc_az": "Uzaq qadın cinsi təsniyə işarə əvəzliyi", "jenis_az": "Uzaq təsniyə işarə əvəzliyi"},

    "6. Isim Fi'il__1": {"arti_az": "Nə qədər də uzaqdır! (Heyhat)", "desc_az": "Keçmiş zaman mənalı feili isim", "jenis_az": "Keçmiş zaman feili ismi"},
    "6. Isim Fi'il__2": {"arti_az": "Uff! / Bezdim! (Uff)", "desc_az": "İndiki zaman mənalı bezikmə bildirən feili isim", "jenis_az": "İndiki zaman feili ismi"},
    "6. Isim Fi'il__3": {"arti_az": "Gəlin! / Gətirin!", "desc_az": "Əmr mənalı feili isim", "jenis_az": "Əmr feili ismi"},
    "6. Isim Fi'il__4": {"arti_az": "Alın! / Götürün oxuyun!", "desc_az": "Əmr mənalı feili isim", "jenis_az": "Əmr feili ismi"},
    "6. Isim Fi'il__5": {"arti_az": "Özünüzü qoruyun! / Möhkəm yapışın!", "desc_az": "Əmr mənalı ön qoşmadan yaranmış feili isim", "jenis_az": "Əmr feili ismi"},
    "6. Isim Fi'il__6": {"arti_az": "Götürün!", "desc_az": "Əmr mənalı zərfdən yaranmış feili isim", "jenis_az": "Əmr feili ismi"},
    "6. Isim Fi'il__7": {"arti_az": "Təəccüblüdür! / Necə də qəribədir!", "desc_az": "Təəccüb bildirən indiki zaman feili ismi", "jenis_az": "İndiki zaman feili ismi"},
    "6. Isim Fi'il__8": {"arti_az": "Uzaq durun! / Budur sizə", "desc_az": "Əmr mənalı feili isim", "jenis_az": "Əmr feili ismi"},

    "7. Fi'il Jamid__1": {"arti_az": "Nə gözəldir! (Tərif feili)", "desc_az": "Tərif bildirən təsriflənməyən camid feil", "jenis_az": "Tərif camid feili"},
    "7. Fi'il Jamid__2": {"arti_az": "Nə pisdir! (Məzəmmət feili)", "desc_az": "Məzəmmət və pisləmə bildirən təsriflənməyən camid feil", "jenis_az": "Məzəmmət camid feili"},
    "7. Fi'il Jamid__3": {"arti_az": "Deyildir (İnkar feili)", "desc_az": "İnkar bildirən naqis camid feil (Kanənin bacısı)", "jenis_az": "İnkar camid feili"},
    "7. Fi'il Jamid__4": {"arti_az": "Ola bilsin ki / Ümid edilir ki", "desc_az": "Ümid bildirən təsriflənməyən rəca feili", "jenis_az": "Rəca camid feili"},
    "7. Fi'il Jamid__5": {"arti_az": "Nə yaman pis oldu!", "desc_az": "Şiddətli məzəmmət bildirən camid feil", "jenis_az": "Məzəmmət camid feili"},
    "7. Fi'il Jamid__6": {"arti_az": "Nə xoşdur!", "desc_az": "Tərif bildirən mürəkkəb camid feil", "jenis_az": "Tərif camid feili"},
    "7. Fi'il Jamid__7": {"arti_az": "Ucadır, bərəkətlidir! (Təbarəkə)", "desc_az": "Allaha məxsus ucalıq bildirən müqəddəs camid feil", "jenis_az": "Müqəddəs camid feil"}
}

BULGARIAN_GRAMMAR = {
    "1. Dhamir__1a": {"arti_bg": "Той (3 л. ед. ч. м. р.)", "desc_bg": "Самостоятелно именно местоимение за 3 л. ед. ч. м. р. (Мунфасил)", "jenis_bg": "Самостоятелно местоимение"},
    "1. Dhamir__1b": {"arti_bg": "Негов / На него / Него (Слято)", "desc_bg": "Слято местоимение за 3 л. ед. ч. м. р. (Муттасил)", "jenis_bg": "Слято местоимение"},
    "1. Dhamir__1c": {"arti_bg": "Само Него (Винително самостоятелно)", "desc_bg": "Самостоятелно винително местоимение за 3 л. ед. ч. м. р.", "jenis_bg": "Винително местоимение"},
    "1. Dhamir__2a": {"arti_bg": "Те двамата (Двойствено число)", "desc_bg": "Самостоятелно местоимение за двойствено число", "jenis_bg": "Двойствено местоимение"},
    "1. Dhamir__2b": {"arti_bg": "На двамата / Тях двамата (Слято)", "desc_bg": "Слято местоимение за двойствено число", "jenis_bg": "Слято двойствено местоимение"},
    "1. Dhamir__3a": {"arti_bg": "Те (м. р. мн. ч.)", "desc_bg": "Самостоятелно именно местоимение за 3 л. мн. ч. м. р.", "jenis_bg": "Самостоятелно местоимение"},
    "1. Dhamir__3b": {"arti_bg": "Тяхен / На тях (Слято)", "desc_bg": "Слято местоимение за 3 л. мн. ч. м. р.", "jenis_bg": "Слято местоимение"},
    "1. Dhamir__3c": {"arti_bg": "Само тях", "desc_bg": "Самостоятелно винително местоимение за 3 л. мн. ч. м. р.", "jenis_bg": "Винително местоимение"},
    "1. Dhamir__4a": {"arti_bg": "Тя (3 л. ед. ч. ж. р.)", "desc_bg": "Самостоятелно именно местоимение за 3 л. ед. ч. ж. р.", "jenis_bg": "Самостоятелно местоимение"},
    "1. Dhamir__4b": {"arti_bg": "Неин / На нея (ж. р. слято)", "desc_bg": "Слято местоимение за 3 л. ед. ч. ж. р.", "jenis_bg": "Слято местоимение"},
    "1. Dhamir__5a": {"arti_bg": "Те (ж. р. мн. ч.)", "desc_bg": "Самостоятелно именно местоимение за 3 л. мн. ч. ж. р.", "jenis_bg": "Самостоятелно местоимение"},
    "1. Dhamir__5b": {"arti_bg": "Тяхен (ж. р. слято)", "desc_bg": "Слято местоимение за 3 л. мн. ч. ж. р.", "jenis_bg": "Слято местоимение"},
    "1. Dhamir__6a": {"arti_bg": "Ти (2 л. ед. ч. м. р.)", "desc_bg": "Самостоятелно именно местоимение за 2 л. ед. ч. м. р.", "jenis_bg": "Самостоятелно местоимение"},
    "1. Dhamir__6b": {"arti_bg": "Твой / На теб (Слято)", "desc_bg": "Слято местоимение за 2 л. ед. ч. м. р.", "jenis_bg": "Слято местоимение"},
    "1. Dhamir__6c": {"arti_bg": "Само на Теб (Посвещаване в молитва)", "desc_bg": "Самостоятелно винително местоимение за 2 л. ед. ч.", "jenis_bg": "Винително местоимение"},
    "1. Dhamir__7a": {"arti_bg": "Вие двамата", "desc_bg": "Самостоятелно местоимение за 2 л. двойствено число", "jenis_bg": "Двойствено местоимение"},
    "1. Dhamir__7b": {"arti_bg": "На вас двамата (Слято)", "desc_bg": "Слято местоимение за 2 л. двойствено число", "jenis_bg": "Слято двойствено местоимение"},
    "1. Dhamir__8a": {"arti_bg": "Вие (м. р. мн. ч.)", "desc_bg": "Самостоятелно именно местоимение за 2 л. мн. ч. м. р.", "jenis_bg": "Самостоятелно местоимение"},
    "1. Dhamir__8b": {"arti_bg": "Ваш / На вас (Слято)", "desc_bg": "Слято местоимение за 2 л. мн. ч. м. р.", "jenis_bg": "Слято местоимение"},
    "1. Dhamir__8c": {"arti_bg": "Само на вас", "desc_bg": "Самостоятелно винително местоимение за 2 л. мн. ч. м. р.", "jenis_bg": "Винително местоимение"},
    "1. Dhamir__9a": {"arti_bg": "Ти (2 л. ед. ч. ж. р.)", "desc_bg": "Самостоятелно именно местоимение за 2 л. ед. ч. ж. р.", "jenis_bg": "Самостоятелно местоимение"},
    "1. Dhamir__9b": {"arti_bg": "Твой / На теб (ж. р. слято)", "desc_bg": "Слято местоимение за 2 л. ед. ч. ж. р.", "jenis_bg": "Слято местоимение"},
    "1. Dhamir__10a": {"arti_bg": "Вие (ж. р. мн. ч.)", "desc_bg": "Самостоятелно именно местоимение за 2 л. мн. ч. ж. р.", "jenis_bg": "Самостоятелно местоимение"},
    "1. Dhamir__10b": {"arti_bg": "Ваш (ж. р. слято)", "desc_bg": "Слято местоимение за 2 л. мн. ч. ж. р.", "jenis_bg": "Слято местоимение"},
    "1. Dhamir__11a": {"arti_bg": "Аз (1 л. ед. ч.)", "desc_bg": "Самостоятелно именно местоимение за 1 л. ед. ч.", "jenis_bg": "Самостоятелно местоимение"},
    "1. Dhamir__11b": {"arti_bg": "Мой / На мен (Слято)", "desc_bg": "Слято местоимение за 1 л. ед. ч.", "jenis_bg": "Слято местоимение"},
    "1. Dhamir__11c": {"arti_bg": "Само на мен", "desc_bg": "Самостоятелно винително местоимение за 1 л. ед. ч.", "jenis_bg": "Винително местоимение"},
    "1. Dhamir__12a": {"arti_bg": "Ние (1 л. мн. ч.)", "desc_bg": "Самостоятелно именно местоимение за 1 л. мн. ч.", "jenis_bg": "Самостоятелно местоимение"},
    "1. Dhamir__12b": {"arti_bg": "Наш / На нас (Слято)", "desc_bg": "Слято местоимение за 1 л. мн. ч.", "jenis_bg": "Слято местоимение"},
    "1. Dhamir__12c": {"arti_bg": "Само на нас", "desc_bg": "Самостоятелно винително местоимение за 1 л. мн. ч.", "jenis_bg": "Винително местоимение"},

    "2. Isim Mawshul__1": {"arti_bg": "Онова, което / Каквото (За неодушевени)", "desc_bg": "Общо относително местоимение за неодушевени предмети", "jenis_bg": "Общо относително местоимение"},
    "2. Isim Mawshul__2": {"arti_bg": "Онези, които (м. р. мн. ч.)", "desc_bg": "Специално относително местоимение за разумни същества", "jenis_bg": "Специално относително местоимение"},
    "2. Isim Mawshul__3": {"arti_bg": "Който / Всеки, който (За разумни)", "desc_bg": "Общо относително местоимение за хора и разумни същества", "jenis_bg": "Общо относително местоимение"},
    "2. Isim Mawshul__4": {"arti_bg": "Онзи, който (м. р. ед. ч.)", "desc_bg": "Специално относително местоимение за ед. ч. м. р.", "jenis_bg": "Специално относително местоимение"},
    "2. Isim Mawshul__5": {"arti_bg": "Който и да е / Което и да е", "desc_bg": "Присъединително относително местоимение", "jenis_bg": "Относително местоимение"},
    "2. Isim Mawshul__6": {"arti_bg": "Оная, която (ж. р. ед. ч.)", "desc_bg": "Специално относително местоимение за ед. ч. ж. р.", "jenis_bg": "Специално относително местоимение"},
    "2. Isim Mawshul__7": {"arti_bg": "Онези жени, които (мн. ч.)", "desc_bg": "Специално относително местоимение за жени", "jenis_bg": "Относително местоимение"},
    "2. Isim Mawshul__8": {"arti_bg": "Онези жени, които (мн. ч.)", "desc_bg": "Специално относително местоимение за жени", "jenis_bg": "Относително местоимение"},
    "2. Isim Mawshul__9": {"arti_bg": "Онези двама, които", "desc_bg": "Двойствено относително местоимение", "jenis_bg": "Двойствено относително местоимение"},
    "2. Isim Mawshul__10": {"arti_bg": "Която и да е (ж. р.)", "desc_bg": "Относително местоимение за ж. р.", "jenis_bg": "Относително местоимение"},

    "3. Isim Istifham__1": {"arti_bg": "Какво? / Що за нещо?", "desc_bg": "Въпросителна дума за неодушевени предмети", "jenis_bg": "Въпросителна дума"},
    "3. Isim Istifham__2": {"arti_bg": "Кой? / Кой е?", "desc_bg": "Въпросителна дума за лица и разумни същества", "jenis_bg": "Въпросителна дума"},
    "3. Isim Istifham__3": {"arti_bg": "Как? / По какъв начин?", "desc_bg": "Въпросителна дума за състояние и начин", "jenis_bg": "Въпросителна дума за състояние"},
    "3. Isim Istifham__4": {"arti_bg": "Къде? / Накъде?", "desc_bg": "Въпросителна дума за място", "jenis_bg": "Въпросителна дума за място"},
    "3. Isim Istifham__5": {"arti_bg": "Колко? / Какво количество?", "desc_bg": "Въпросителна дума за брой и количество", "jenis_bg": "Въпросителна дума за количество"},
    "3. Isim Istifham__6": {"arti_bg": "Кога? / В кое време?", "desc_bg": "Въпросителна дума за време", "jenis_bg": "Въпросителна дума за време"},
    "3. Isim Istifham__7": {"arti_bg": "Кога ще настъпи? (За великия Съден ден)", "desc_bg": "Въпросителна дума за бъдещи грандиозни събития", "jenis_bg": "Въпросителна дума за време"},
    "3. Isim Istifham__8": {"arti_bg": "Откъде? / Как така?", "desc_bg": "Въпросителна дума за произход и причина", "jenis_bg": "Въпросителна дума"},

    "4. Isim Syarath__1": {"arti_bg": "Който / Всеки, който", "desc_bg": "Условна дума за лица, изискваща усечено глаголно наклонение", "jenis_bg": "Условна дума"},
    "4. Isim Syarath__2": {"arti_bg": "Каквото и да / Всичко, което", "desc_bg": "Условна дума за предмети", "jenis_bg": "Условна дума"},
    "4. Isim Syarath__3": {"arti_bg": "Когато / В мига, когато", "desc_bg": "Времева условна дума за бъдещето", "jenis_bg": "Времева условна дума"},
    "4. Isim Syarath__4": {"arti_bg": "Колкото и да / Каквото и да е", "desc_bg": "Всеобхватна условна дума за предмети", "jenis_bg": "Условна дума"},
    "4. Isim Syarath__5": {"arti_bg": "Където и да / Накъдето и да", "desc_bg": "Условна дума за място", "jenis_bg": "Условна дума за място"},
    "4. Isim Syarath__6": {"arti_bg": "Където и да се намирате", "desc_bg": "Условна дума за място с подсилване", "jenis_bg": "Условна дума за място"},
    "4. Isim Syarath__7": {"arti_bg": "В каквото и състояние да е", "desc_bg": "Условна дума за състояние", "jenis_bg": "Условна дума за състояние"},
    "4. Isim Syarath__8": {"arti_bg": "Което и да е / Който и да е", "desc_bg": "Присъединителна условна дума", "jenis_bg": "Условна дума"},

    "5. Isim Isyarah__1": {"arti_bg": "Това / Онази книга (м. р. отдалечено)", "desc_bg": "Показателно местоимение за далечно разстояние м. р.", "jenis_bg": "Далечно показателно местоимение"},
    "5. Isim Isyarah__2": {"arti_bg": "Това / Този (м. р. близко)", "desc_bg": "Показателно местоимение за близко разстояние м. р.", "jenis_bg": "Близко показателно местоимение"},
    "5. Isim Isyarah__3": {"arti_bg": "Тези (близко мн. ч.)", "desc_bg": "Показателно местоимение за близко разстояние мн. ч.", "jenis_bg": "Близко показателно местоимение"},
    "5. Isim Isyarah__4": {"arti_bg": "Онези (отдалечено мн. ч.)", "desc_bg": "Показателно местоимение за далечно разстояние мн. ч.", "jenis_bg": "Далечно показателно местоимение"},
    "5. Isim Isyarah__5": {"arti_bg": "Тази (ж. р. близко)", "desc_bg": "Показателно местоимение за близко разстояние ж. р.", "jenis_bg": "Близко показателно местоимение"},
    "5. Isim Isyarah__6": {"arti_bg": "Оная (ж. р. отдалечено)", "desc_bg": "Показателно местоимение за далечно разстояние ж. р.", "jenis_bg": "Далечно показателно местоимение"},
    "5. Isim Isyarah__7": {"arti_bg": "Там / На онова място", "desc_bg": "Показателно местоимение за далечно място", "jenis_bg": "Показателно за място"},
    "5. Isim Isyarah__8": {"arti_bg": "Тук / На това място", "desc_bg": "Показателно местоимение за близко място", "jenis_bg": "Показателно за място"},
    "5. Isim Isyarah__9": {"arti_bg": "Онези две неща (отдалечено м. р.)", "desc_bg": "Двойствено показателно местоимение", "jenis_bg": "Двойствено показателно"},
    "5. Isim Isyarah__10": {"arti_bg": "Онези две неща (отдалечено ж. р.)", "desc_bg": "Двойствено показателно местоимение", "jenis_bg": "Двойствено показателно"},

    "6. Isim Fi'il__1": {"arti_bg": "Колко е далеч! (Хайхата)", "desc_bg": "Глаголно име за минало време", "jenis_bg": "Глаголно име за минало"},
    "6. Isim Fi'il__2": {"arti_bg": "Уф! / Досада! (Уфф)", "desc_bg": "Глаголно име за сегашно време изразяващо отегчение", "jenis_bg": "Глаголно име за сегашно"},
    "6. Isim Fi'il__3": {"arti_bg": "Елате! / Донесете!", "desc_bg": "Повелително глаголно име", "jenis_bg": "Повелително глаголно име"},
    "6. Isim Fi'il__4": {"arti_bg": "Вземете! / Прочетете!", "desc_bg": "Повелително глаголно име", "jenis_bg": "Повелително глаголно име"},
    "6. Isim Fi'il__5": {"arti_bg": "Пазете се! / Дръжте се здраво!", "desc_bg": "Повелително глаголно име образувано от предлог", "jenis_bg": "Повелително глаголно име"},
    "6. Isim Fi'il__6": {"arti_bg": "Вземете го!", "desc_bg": "Повелително глаголно име образувано от наречие", "jenis_bg": "Повелително глаголно име"},
    "6. Isim Fi'il__7": {"arti_bg": "Колко е чудно!", "desc_bg": "Глаголно име за удивление", "jenis_bg": "Глаголно име"},
    "6. Isim Fi'il__8": {"arti_bg": "Отдръпнете се! / Ето ви", "desc_bg": "Повелително глаголно име", "jenis_bg": "Повелително глаголно име"},

    "7. Fi'il Jamid__1": {"arti_bg": "Колко е прекрасно! (Ни'ма)", "desc_bg": "Неизменяем похвален глагол", "jenis_bg": "Похвален неизменяем глагол"},
    "7. Fi'il Jamid__2": {"arti_bg": "Колко е лошо! (Би'са)", "desc_bg": "Неизменяем порицателен глагол", "jenis_bg": "Порицателен неизменяем глагол"},
    "7. Fi'il Jamid__3": {"arti_bg": "Не е / Не беше (Лайса)", "desc_bg": "Неизменяем отрицателен спомагателен глагол", "jenis_bg": "Отрицателен неизменяем глагол"},
    "7. Fi'il Jamid__4": {"arti_bg": "Може би / Надежда има ('Аса)", "desc_bg": "Неизменяем глагол за надежда", "jenis_bg": "Глагол за надежда"},
    "7. Fi'il Jamid__5": {"arti_bg": "Колко е злощастно! (Са'а)", "desc_bg": "Неизменяем порицателен глагол", "jenis_bg": "Порицателен неизменяем глагол"},
    "7. Fi'il Jamid__6": {"arti_bg": "Колко е приятно!", "desc_bg": "Сложен похвален глагол", "jenis_bg": "Похвален глагол"},
    "7. Fi'il Jamid__7": {"arti_bg": "Благословен и превъзнесен е! (Табарака)", "desc_bg": "Свещен неизменяем глагол за Божието величие", "jenis_bg": "Свещен неизменяем глагол"}
}

AZERBAIJANI_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {"arti_az": "Deyil / -mədi (Ümumi inkar ədatı)", "desc_az": "Keçmiş, indiki zaman və isim cümlələrini inkar edən əməlsiz ədat", "jenis_az": "İnkar ədatı"},
    "1. Harf Nafyi__2": {"arti_az": "Yox / -məz (Feil inkar ədatı)", "desc_az": "İndiki və gələcək zaman feillərini inkar edən əməlsiz ədat", "jenis_az": "İnkar ədatı"},
    "1. Harf Nafyi__3": {"arti_az": "Başqa bir şey deyil, yalnız...", "desc_az": "İlla ilə birlikdə işlənən inkar ədatı", "jenis_az": "İnkar ədatı"},
    "1. Harf Nafyi__4": {"arti_az": "Zamanı deyildir (Latə)", "desc_az": "Leysə kimi təsir edən zaman inkar ədatı", "jenis_az": "Zaman inkar ədatı"},

    "2. Harf Tahqiq Taswif__5": {"arti_az": "Həqiqətən / Artıq / Şübhəsiz (Qad)", "desc_az": "Keçmiş zaman qarşısında qətilik bildirən təhqiq ədatı", "jenis_az": "Təhqiq ədatı"},
    "2. Harf Tahqiq Taswif__6": {"arti_az": "Gələcəkdə / Vaxtı çatanda (Səvfə)", "desc_az": "Uzaq gələcək zaman bildirən təsvif ədatı", "jenis_az": "Gələcək zaman ədatı"},
    "2. Harf Tahqiq Taswif__7": {"arti_az": "Tezliklə / -acaq (Sə - yaxın gələcək)", "desc_az": "Yaxın gələcək zaman bildirən təsvif ədatı", "jenis_az": "Gələcək zaman ədatı"},

    "3. Harf Syarat__8": {"arti_az": "Əgər / Olsaydı (Ləv - qeyri-mümkün şərt)", "desc_az": "Keçmişdə baş verməmiş hadisələr üçün əməlsiz şərt ədatı", "jenis_az": "Əməlsiz şərt ədatı"},
    "3. Harf Syarat__9": {"arti_az": "Əgər olmasaydı... (Ləvla)", "desc_az": "Bir şeyin varlığına görə digərinin olmamasını bildirən şərt ədatı", "jenis_az": "Əməlsiz şərt ədatı"},
    "3. Harf Syarat__10": {"arti_az": "Əgər olmasaydı... (Ləvma)", "desc_az": "Əməlsiz şərt ədatı", "jenis_az": "Əməlsiz şərt ədatı"},
    "3. Harf Syarat__11": {"arti_az": "O zaman ki / Zamanında (Ləmma)", "desc_az": "Keçmiş zaman üçün zaman şərt ədatı", "jenis_az": "Zaman şərt ədatı"},
    "3. Harf Syarat__12": {"arti_az": "O ki qaldı... isə (Əmma)", "desc_az": "Təfsilat və təkid bildirən şərt ədatı", "jenis_az": "Təfsilat şərt ədatı"},

    "4. Harf Mashdariyah__13": {"arti_az": "-maq / -məsi (Ən - məsdər ədatı)", "desc_az": "Feili məsdər mənasına çevirən ədat", "jenis_az": "Məsdər ədatı"},
    "4. Harf Mashdariyah__14": {"arti_az": "Nə qədər ki / Müddətcə (Ma məsdəriyyə)", "desc_az": "Zaman və hal məsdəri bildirən ədat", "jenis_az": "Məsdər ədatı"},
    "4. Harf Mashdariyah__15": {"arti_az": "Olsun deyə / Məqsədilə (Kəy)", "desc_az": "Məqsəd və məsdər bildirən ədat", "jenis_az": "Məsdər ədatı"},
    "4. Harf Mashdariyah__16": {"arti_az": "İstərdi ki / Kaş (Ləv məsdəriyyə)", "desc_az": "Arzu feillərindən sonra işlənən məsdər ədatı", "jenis_az": "Məsdər ədatı"},

    "5. Harf Zaidah__17": {"arti_az": "Qüvvətləndirmə üçün (İn zaidə)", "desc_az": "Cümlənin mənasını gücləndirən əlavə ədat", "jenis_az": "Qüvvətləndirici ədat"},
    "5. Harf Zaidah__18": {"arti_az": "Qüvvətləndirmə üçün (Ən zaidə)", "desc_az": "Qüvvətləndirici əlavə ədat", "jenis_az": "Qüvvətləndirici ədat"},
    "5. Harf Zaidah__19": {"arti_az": "Qüvvətləndirmə üçün (Ma zaidə)", "desc_az": "Qüvvətləndirici əlavə ədat", "jenis_az": "Qüvvətləndirici ədat"},
    "5. Harf Zaidah__20": {"arti_az": "Qüvvətləndirmə üçün (La zaidə)", "desc_az": "İnkarı və ya təsdiqi gücləndirən əlavə ədat", "jenis_az": "Qüvvətləndirici ədat"},

    "6. Harf Istifham__21": {"arti_az": "Mı? / Yoxsa? (Həmzə)", "desc_az": "Əsas sual hərfi", "jenis_az": "Sual hərfi"},
    "6. Harf Istifham__22": {"arti_az": "Məgər? / Heç? (Həl)", "desc_az": "Təsdiq və ya inkar cavabı tələb edən sual ədatı", "jenis_az": "Sual ədatı"},

    "7. Harf Istitsna__23": {"arti_az": "Yalnız / Başqa / İstisna olaraq (İlla)", "desc_az": "Həsr və istisna bildirən ədat", "jenis_az": "İstisna ədatı"},

    "8. Harf Rad'in Wazajrin__24": {"arti_az": "Xeyr, əsla! / Qətiyyən! (Kəlla)", "desc_az": "Şiddətli çəkindirmə və batili rədd etmə ədatı", "jenis_az": "Çəkindirmə ədatı"},

    "9. Harf Rad'in Tahdid__25": {"arti_az": "Məgər etməyəcəksinizmi? (Həlla)", "desc_az": "Xeyir işə təşviq və ya qınama ədatı", "jenis_az": "Təhrik ədatı"},
    "9. Harf Rad'in Tahdid__26": {"arti_az": "Bəs niyə... deyil? (Əlla)", "desc_az": "Təşviq və təhrik ədatı", "jenis_az": "Təhrik ədatı"},

    "10. Harf Ijab__27": {"arti_az": "Bəli / Doğrudur (Nəəm)", "desc_az": "Təsdiq və cavab ədatı", "jenis_az": "Cavab ədatı"},
    "10. Harf Ijab__28": {"arti_az": "Bəli, əlbəttə! (Bəla)", "desc_az": "İnkarı ləğv edib həqiqəti təsdiqləyən cavab ədatı", "jenis_az": "Təsdiq ədatı"},
    "10. Harf Ijab__29": {"arti_az": "Bəli, Rəbbimə and olsun! (İ)", "desc_az": "And ilə birlikdə işlənən təsdiq ədatı", "jenis_az": "And təsdiq ədatı"},
    "10. Harf Ijab__30": {"arti_az": "Doğrudur / Əlbəttə (Əcəl)", "desc_az": "Təsdiq ədatı", "jenis_az": "Təsdiq ədatı"},

    "11. Harf Tafsir__31": {"arti_az": "Yəni / Yəni ki (Əy)", "desc_az": "Əvvəlki sözü izah edən təfsir ədatı", "jenis_az": "Təfsir ədatı"},
    "11. Harf Tafsir__32": {"arti_az": "Ki / Yəni deyə (Ən təfsiriyyə)", "desc_az": "Söz və ya vəhy bildirən feillərdən sonra gələn izah ədatı", "jenis_az": "Təfsir ədatı"},

    "12. Harf Tanbih__33": {"arti_az": "Bilin ki! / Agah olun! (Əla)", "desc_az": "Başlanğıc və diqqəti cəlb etmə ədatı", "jenis_az": "Xəbərdarlıq ədatı"},
    "12. Harf Tanbih__34": {"arti_az": "Bilin ki! (Əma)", "desc_az": "Xəbərdarlıq və başlanğıc ədatı", "jenis_az": "Xəbərdarlıq ədatı"},
    "12. Harf Tanbih__35": {"arti_az": "Baxın! / Budur! (Ha tənbeh)", "desc_az": "İşarə və əvəzliklərin əvvəlində gələn diqqət çəkmə hərfi", "jenis_az": "Diqqət hərfi"},

    "13. Harf Ta'lil__36": {"arti_az": "Görə / Çünki / Olsun deyə (Lam təlil)", "desc_az": "Səbəb və məqsəd bildirən ədat", "jenis_az": "Səbəb ədatı"},

    "14. Harf Fuja'iyyah__37": {"arti_az": "Birdən / Bir də gördü ki (İza fucaiyyə)", "desc_az": "Hadisənin qəfil baş verdiyini bildirən ədat", "jenis_az": "Qəfil hadisə ədatı"},
    "14. Harf Fuja'iyyah__38": {"arti_az": "Qəflətən (İz fucaiyyə)", "desc_az": "Qəfil başvermə ədatı", "jenis_az": "Qəfil hadisə ədatı"},

    "15. Harf Istidrak__39": {"arti_az": "Lakin / Lakin belədir ki (Lakin)", "desc_az": "Düzəliş və yanlış anlamanı aradan qaldıran ədat", "jenis_az": "İstidrak ədatı"},
    "15. Harf Istidrak__40": {"arti_az": "Əksinə / Hətta (Bəl)", "desc_az": "Fikri dəyişmə və ya düzəliş ədatı", "jenis_az": "İstidrak ədatı"},

    "16. Harf Ta'ajjub__41": {"arti_az": "Nə qədər də... / Necə də gözəldir! (Ma)", "desc_az": "Təəccüb və heyrət bildirən ədat", "jenis_az": "Təəccüb ədatı"},

    "17. Harf Mabany__39": {"arti_az": "Ha-Mim", "desc_az": "Surə başlanğıcı müqəttəat hərfləri", "jenis_az": "Müqəttəat hərfləri"},
    "17. Harf Mabany__40": {"arti_az": "Əlif-Lam-Mim", "desc_az": "Surə başlanğıcı müqəttəat hərfləri", "jenis_az": "Müqəttəat hərfləri"},
    "17. Harf Mabany__41": {"arti_az": "Əlif-Lam-Ra", "desc_az": "Surə başlanğıcı müqəttəat hərfləri", "jenis_az": "Müqəttəat hərfləri"},
    "17. Harf Mabany__42": {"arti_az": "Ta-Sin-Mim", "desc_az": "Surə başlanğıcı müqəttəat hərfləri", "jenis_az": "Müqəttəat hərfləri"},
    "17. Harf Mabany__43": {"arti_az": "Əlif-Lam-Mim-Ra", "desc_az": "Surə başlanğıcı müqəttəat hərfləri", "jenis_az": "Müqəttəat hərfləri"},
    "17. Harf Mabany__44": {"arti_az": "Əlif-Lam-Mim-Sad", "desc_az": "Surə başlanğıcı müqəttəat hərfləri", "jenis_az": "Müqəttəat hərfləri"},
    "17. Harf Mabany__45": {"arti_az": "Sad", "desc_az": "Surə başlanğıcı müqəttəat hərfləri", "jenis_az": "Müqəttəat hərfləri"},
    "17. Harf Mabany__46": {"arti_az": "Ta-Sin", "desc_az": "Surə başlanğıcı müqəttəat hərfləri", "jenis_az": "Müqəttəat hərfləri"},
    "17. Harf Mabany__47": {"arti_az": "Ta-Ha", "desc_az": "Surə başlanğıcı müqəttəat hərfləri", "jenis_az": "Müqəttəat hərfləri"},
    "17. Harf Mabany__48": {"arti_az": "Ayn-Sin-Qaf", "desc_az": "Surə başlanğıcı müqəttəat hərfləri", "jenis_az": "Müqəttəat hərfləri"},
    "17. Harf Mabany__49": {"arti_az": "Qaf", "desc_az": "Surə başlanğıcı müqəttəat hərfləri", "jenis_az": "Müqəttəat hərfləri"},
    "17. Harf Mabany__50": {"arti_az": "Kaf-Ha-Ya-Ayn-Sad", "desc_az": "Surə başlanğıcı müqəttəat hərfləri", "jenis_az": "Müqəttəat hərfləri"},
    "17. Harf Mabany__51": {"arti_az": "Nun", "desc_az": "Surə başlanğıcı müqəttəat hərfləri", "jenis_az": "Müqəttəat hərfləri"},
    "17. Harf Mabany__52": {"arti_az": "Ya-Sin", "desc_az": "Surə başlanğıcı müqəttəat hərfləri", "jenis_az": "Müqəttəat hərfləri"}
}

BULGARIAN_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {"arti_bg": "Не / Не е (Ма - общо отрицание)", "desc_bg": "Неуправляваща отрицателна частица за минало, сегашно време и именни изречения", "jenis_bg": "Отрицателна частица"},
    "1. Harf Nafyi__2": {"arti_bg": "Не / Няма да (Ла - глаголно отрицание)", "desc_bg": "Отрицателна частица за сегашно и бъдеще време", "jenis_bg": "Отрицателна частица"},
    "1. Harf Nafyi__3": {"arti_bg": "Не е нищо друго освен... (Ин)", "desc_bg": "Отрицателна частица съчетавана с Илла", "jenis_bg": "Отрицателна частица"},
    "1. Harf Nafyi__4": {"arti_bg": "Не е време за (Лата)", "desc_bg": "Отрицателна частица за време", "jenis_bg": "Отрицателна частица за време"},

    "2. Harf Tahqiq Taswif__5": {"arti_bg": "Наистина / Вече (Кад - потвърждение)", "desc_bg": "Частица за категоричност и потвърждение пред минало време", "jenis_bg": "Потвърдителна частица"},
    "2. Harf Tahqiq Taswif__6": {"arti_bg": "В бъдеще / Ще (Сауфа - далечно бъдеще)", "desc_bg": "Частица за далечно бъдеще време", "jenis_bg": "Частица за бъдеще време"},
    "2. Harf Tahqiq Taswif__7": {"arti_bg": "Ще (Са - близко бъдеще)", "desc_bg": "Частица за близко бъдеще време", "jenis_bg": "Частица за бъдеще време"},

    "3. Harf Syarat__8": {"arti_bg": "Ако / Ако беше (Лау - невъзможно условие)", "desc_bg": "Неуправляваща условна частица за неосъществени събития", "jenis_bg": "Условна частица"},
    "3. Harf Syarat__9": {"arti_bg": "Ако не беше... (Лаула)", "desc_bg": "Условна частица за възпрепятстване", "jenis_bg": "Условна частица"},
    "3. Harf Syarat__10": {"arti_bg": "Ако не беше... (Лаума)", "desc_bg": "Неуправляваща условна частица", "jenis_bg": "Условна частица"},
    "3. Harf Syarat__11": {"arti_bg": "Когато / В мига, в който (Ламма)", "desc_bg": "Времева условна частица за минало време", "jenis_bg": "Времева условна частица"},
    "3. Harf Syarat__12": {"arti_bg": "А колкото до... то (Амма)", "desc_bg": "Подробна условна частица с подчертаване", "jenis_bg": "Условна частица"},

    "4. Harf Mashdariyah__13": {"arti_bg": "Да / Че (Ан - масдарна частица)", "desc_bg": "Частица превръщаща глагола в отглаголно съществително", "jenis_bg": "Масдарна частица"},
    "4. Harf Mashdariyah__14": {"arti_bg": "Докато / Доколкото (Ма масдарийя)", "desc_bg": "Времева отглаголна частица", "jenis_bg": "Масдарна частица"},
    "4. Harf Mashdariyah__15": {"arti_bg": "За да / С цел да (Кай)", "desc_bg": "Целева отглаголна частица", "jenis_bg": "Масдарна частица"},
    "4. Harf Mashdariyah__16": {"arti_bg": "Дано / Желанието да (Лау)", "desc_bg": "Отглаголна частица след глаголи за желание", "jenis_bg": "Масдарна частица"},

    "5. Harf Zaidah__17": {"arti_bg": "За подсилване (Ин заида)", "desc_bg": "Допълнителна подсилваща частица", "jenis_bg": "Подсилваща частица"},
    "5. Harf Zaidah__18": {"arti_bg": "За подсилване (Ан заида)", "desc_bg": "Допълнителна подсилваща частица", "jenis_bg": "Подсилваща частица"},
    "5. Harf Zaidah__19": {"arti_bg": "За подсилване (Ма заида)", "desc_bg": "Допълнителна подсилваща частица", "jenis_bg": "Подсилваща частица"},
    "5. Harf Zaidah__20": {"arti_bg": "За подсилване (Ла заида)", "desc_bg": "Допълнителна подсилваща отрицанието частица", "jenis_bg": "Подсилваща частица"},

    "6. Harf Istifham__21": {"arti_bg": "Нима? / Дали? (Хамза)", "desc_bg": "Основна въпросителна частица", "jenis_bg": "Въпросителна частица"},
    "6. Harf Istifham__22": {"arti_bg": "Нима? / Възможно ли е? (Хал)", "desc_bg": "Въпросителна частица търсеща утвърждение или отрицание", "jenis_bg": "Въпросителна частица"},

    "7. Harf Istitsna__23": {"arti_bg": "Освен / Единствено (Илла)", "desc_bg": "Изключваща частица за ограничаване", "jenis_bg": "Изключваща частица"},

    "8. Harf Rad'in Wazajrin__24": {"arti_bg": "Съвсем не! / В никакъв случай! (Калла)", "desc_bg": "Възпираща и категорично отричаща лъжата частица", "jenis_bg": "Възпираща частица"},

    "9. Harf Rad'in Tahdid__25": {"arti_bg": "Защо не... / Нима няма да (Халла)", "desc_bg": "Подбудителна или укоряваща частица", "jenis_bg": "Подбудителна частица"},
    "9. Harf Rad'in Tahdid__26": {"arti_bg": "Защо не... (Алла)", "desc_bg": "Подбудителна частица за бързо извършване на добро", "jenis_bg": "Подбудителна частица"},

    "10. Harf Ijab__27": {"arti_bg": "Да / Така е (На'ам)", "desc_bg": "Частица за утвърдителен отговор", "jenis_bg": "Утвърдителна частица"},
    "10. Harf Ijab__28": {"arti_bg": "Да, разбира се! (Бала)", "desc_bg": "Частица отменяща отрицанието и потвърждаваща истината", "jenis_bg": "Утвърдителна частица"},
    "10. Harf Ijab__29": {"arti_bg": "Да, кълна се в моя Господ! (И)", "desc_bg": "Утвърдителна частица при клетва", "jenis_bg": "Клетвена частица"},
    "10. Harf Ijab__30": {"arti_bg": "Вярно е / Разбира се (Аджал)", "desc_bg": "Утвърдителна частица", "jenis_bg": "Утвърдителна частица"},

    "11. Harf Tafsir__31": {"arti_bg": "Тоест / Сиреч (Ай)", "desc_bg": "Пояснителна частица", "jenis_bg": "Пояснителна частица"},
    "11. Harf Tafsir__32": {"arti_bg": "Че / А именно (Ан тафсирийя)", "desc_bg": "Обяснителна частица след глаголи за казване или откровение", "jenis_bg": "Пояснителна частица"},

    "12. Harf Tanbih__33": {"arti_bg": "Внимавайте! / Знайте! (Ала)", "desc_bg": "Частица за привличане на вниманието в началото", "jenis_bg": "Предупредителна частица"},
    "12. Harf Tanbih__34": {"arti_bg": "Знайте добре! (Ама)", "desc_bg": "Предупредителна частица", "jenis_bg": "Предупредителна частица"},
    "12. Harf Tanbih__35": {"arti_bg": "Ето! / Вижте! (Ха танбих)", "desc_bg": "Частица за привличане на вниманието пред местоимения", "jenis_bg": "Частица за внимание"},

    "13. Harf Ta'lil__36": {"arti_bg": "За да / Понеже (Лам та'лил)", "desc_bg": "Причинна частица за мотив и следствие", "jenis_bg": "Причинна частица"},

    "14. Harf Fuja'iyyah__37": {"arti_bg": "И изведнъж! / И ето че (Иза фуджаийя)", "desc_bg": "Частица за внезапно настъпило събитие", "jenis_bg": "Частица за внезапност"},
    "14. Harf Fuja'iyyah__38": {"arti_bg": "Внезапно (Из фуджаийя)", "desc_bg": "Частица за внезапност", "jenis_bg": "Частица за внезапност"},

    "15. Harf Istidrak__39": {"arti_bg": "Ала / Но / Обаче (Лакин)", "desc_bg": "Коригираща частица за премахване на недоразумения", "jenis_bg": "Коригираща частица"},
    "15. Harf Istidrak__40": {"arti_bg": "Напротив / Дори (Бал)", "desc_bg": "Частица за промяна на тезата и корекция", "jenis_bg": "Коригираща частица"},

    "16. Harf Ta'ajjub__41": {"arti_bg": "Колко... само! / Колко е чудно! (Ма)", "desc_bg": "Частица за удивление и възклицание", "jenis_bg": "Частица за удивление"},

    "17. Harf Mabany__39": {"arti_bg": "Ха-Мим", "desc_bg": "Начални съкратени букви на сурите", "jenis_bg": "Мукатта'ат букви"},
    "17. Harf Mabany__40": {"arti_bg": "Алиф-Лам-Мим", "desc_bg": "Начални съкратени букви на сурите", "jenis_bg": "Мукатта'ат букви"},
    "17. Harf Mabany__41": {"arti_bg": "Алиф-Лам-Ра", "desc_bg": "Начални съкратени букви на сурите", "jenis_bg": "Мукатта'ат букви"},
    "17. Harf Mabany__42": {"arti_bg": "Та-Син-Мим", "desc_bg": "Начални съкратени букви на сурите", "jenis_bg": "Мукатта'ат букви"},
    "17. Harf Mabany__43": {"arti_bg": "Алиф-Лам-Мим-Ра", "desc_bg": "Начални съкратени букви на сурите", "jenis_bg": "Мукатта'ат букви"},
    "17. Harf Mabany__44": {"arti_bg": "Алиф-Лам-Мим-Сад", "desc_bg": "Начални съкратени букви на сурите", "jenis_bg": "Мукатта'ат букви"},
    "17. Harf Mabany__45": {"arti_bg": "Сад", "desc_bg": "Начални съкратени букви на сурите", "jenis_bg": "Мукатта'ат букви"},
    "17. Harf Mabany__46": {"arti_bg": "Та-Син", "desc_bg": "Начални съкратени букви на сурите", "jenis_bg": "Мукатта'ат букви"},
    "17. Harf Mabany__47": {"arti_bg": "Та-Ха", "desc_bg": "Начални съкратени букви на сурите", "jenis_bg": "Мукатта'ат букви"},
    "17. Harf Mabany__48": {"arti_bg": "Айн-Син-Каф", "desc_bg": "Начални съкратени букви на сурите", "jenis_bg": "Мукатта'ат букви"},
    "17. Harf Mabany__49": {"arti_bg": "Каф", "desc_bg": "Начални съкратени букви на сурите", "jenis_bg": "Мукатта'ат букви"},
    "17. Harf Mabany__50": {"arti_bg": "Каф-Ха-Йа-Айн-Сад", "desc_bg": "Начални съкратени букви на сурите", "jenis_bg": "Мукатта'ат букви"},
    "17. Harf Mabany__51": {"arti_bg": "Нун", "desc_bg": "Начални съкратени букви на сурите", "jenis_bg": "Мукатта'ат букви"},
    "17. Harf Mabany__52": {"arti_bg": "Йа-Син", "desc_bg": "Начални съкратени букви на сурите", "jenis_bg": "Мукатта'ат букви"}
}


def enrich_dhamir_data():
    print("Enriching dhamir_data.json and dhamir_data.js with Azerbaijani & Bulgarian...")
    with open(os.path.join(BASE_DIR, 'az_translations.json'), 'r', encoding='utf-8') as f:
        az_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'bg_translations.json'), 'r', encoding='utf-8') as f:
        bg_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = str(item.get('No kata', ''))
        g_key = f"{b}__{nk}"
        s_num = str(item.get('SURAT', ''))
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"

        # AZ
        item['BentukKataAZ'] = BENTUK_KATA_AZ.get(b, b)
        item['SuratArtiAZ'] = AZERBAIJANI_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_az = AZERBAIJANI_GRAMMAR.get(g_key, {})
        item['ArtiKataAZ'] = g_az.get('arti_az', item.get('ArtiKataEN', ''))
        item['TeksArtiAZ'] = az_trans.get(v_key, item.get('TeksArtiEN', ''))

        # BG
        item['BentukKataBG'] = BENTUK_KATA_BG.get(b, b)
        item['SuratArtiBG'] = BULGARIAN_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_bg = BULGARIAN_GRAMMAR.get(g_key, {})
        item['ArtiKataBG'] = g_bg.get('arti_bg', item.get('ArtiKataEN', ''))
        item['TeksArtiBG'] = bg_trans.get(v_key, item.get('TeksArtiEN', ''))

        # Grammar dict
        if 'Grammar' not in item or not isinstance(item['Grammar'], dict):
            item['Grammar'] = {}
        if g_az.get('arti_az'): item['Grammar']['arti_az'] = g_az['arti_az']
        if g_az.get('desc_az'): item['Grammar']['desc_az'] = g_az['desc_az']
        if g_az.get('jenis_az'): item['Grammar']['jenis_az'] = g_az['jenis_az']

        if g_bg.get('arti_bg'): item['Grammar']['arti_bg'] = g_bg['arti_bg']
        if g_bg.get('desc_bg'): item['Grammar']['desc_bg'] = g_bg['desc_bg']
        if g_bg.get('jenis_bg'): item['Grammar']['jenis_bg'] = g_bg['jenis_bg']

    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    js_content = f"/**\n * Dataset Dhamir & Isim Jamid Mabny Al-Qur'an 27 Bahasa\n */\nconst DHAMIR_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
    with open(os.path.join(BASE_DIR, 'dhamir_data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"  [OK] Dhamir data enriched ({len(data)} rows).")


def enrich_harf_data():
    print("Enriching harf_data.json and harf_data.js with Azerbaijani & Bulgarian...")
    with open(os.path.join(BASE_DIR, 'az_translations.json'), 'r', encoding='utf-8') as f:
        az_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'bg_translations.json'), 'r', encoding='utf-8') as f:
        bg_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = str(item.get('No kata', ''))
        g_key = f"{b}__{nk}"
        s_num = str(item.get('SURAT', ''))
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"

        # AZ
        item['BentukKataAZ'] = BENTUK_HARF_AZ.get(b, b)
        item['SuratArtiAZ'] = AZERBAIJANI_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_az = AZERBAIJANI_HARF_GRAMMAR.get(g_key, {})
        item['ArtiKataAZ'] = g_az.get('arti_az', item.get('ArtiKataEN', ''))
        item['TeksArtiAZ'] = az_trans.get(v_key, item.get('TeksArtiEN', ''))

        # BG
        item['BentukKataBG'] = BENTUK_HARF_BG.get(b, b)
        item['SuratArtiBG'] = BULGARIAN_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_bg = BULGARIAN_HARF_GRAMMAR.get(g_key, {})
        item['ArtiKataBG'] = g_bg.get('arti_bg', item.get('ArtiKataEN', ''))
        item['TeksArtiBG'] = bg_trans.get(v_key, item.get('TeksArtiEN', ''))

        # Grammar dict
        if 'Grammar' not in item or not isinstance(item['Grammar'], dict):
            item['Grammar'] = {}
        if g_az.get('arti_az'): item['Grammar']['arti_az'] = g_az['arti_az']
        if g_az.get('desc_az'): item['Grammar']['desc_az'] = g_az['desc_az']
        if g_az.get('jenis_az'): item['Grammar']['jenis_az'] = g_az['jenis_az']

        if g_bg.get('arti_bg'): item['Grammar']['arti_bg'] = g_bg['arti_bg']
        if g_bg.get('desc_bg'): item['Grammar']['desc_bg'] = g_bg['desc_bg']
        if g_bg.get('jenis_bg'): item['Grammar']['jenis_bg'] = g_bg['jenis_bg']

    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    js_content = f"/**\n * Dataset Harf Ghair 'Amil Al-Qur'an 27 Bahasa\n */\nconst HARF_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
    with open(os.path.join(BASE_DIR, 'harf_data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"  [OK] Harf data enriched ({len(data)} rows).")


if __name__ == '__main__':
    enrich_dhamir_data()
    enrich_harf_data()
