#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to build Persian (Farsi - fa) dataset and enrich dhamir_data.json, dhamir_data.js,
harf_data.json, and harf_data.js with complete Persian translations.
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

# 1. 114 Surahs Persian Names / Meanings (Ayatollah Naser Makarem Shirazi)
PERSIAN_SURAHS = {
    "1": "حمد (فاتحه / گشاینده)",
    "2": "بقره (گاو ماده)",
    "3": "آل عمران (خاندان عمران)",
    "4": "نساء (زنان)",
    "5": "مائده (سفره غذا)",
    "6": "انعام (چهارپایان)",
    "7": "اعراف (بلندی‌ها)",
    "8": "انفال (غنیمت‌های جنگی)",
    "9": "توبه (بازگشت)",
    "10": "یونس (حضرت یونس ع)",
    "11": "هود (حضرت هود ع)",
    "12": "یوسف (حضرت یوسف ع)",
    "13": "رعد (غرش آسمان)",
    "14": "ابراهیم (حضرت ابراهیم ع)",
    "15": "حجر (سرزمین سنگستان)",
    "16": "نحل (زنبور عسل)",
    "17": "اسراء (سیر شبانه / معراج)",
    "18": "کهف (غار)",
    "19": "مریم (حضرت مریم س)",
    "20": "طه (طه)",
    "21": "انبیاء (پیامبران)",
    "22": "حج (مناسک حج)",
    "23": "مؤمنون (مؤمنان)",
    "24": "نور (روشنایی الهی)",
    "25": "فرقان (جداکننده حق از باطل)",
    "26": "شعراء (شاعران)",
    "27": "نمل (مورچه)",
    "28": "قصص (داستان‌ها)",
    "29": "عنکبوت (عنکبوت)",
    "30": "روم (رومیان)",
    "31": "لقمان (حضرت لقمان ع)",
    "32": "سجده (سجده کردن)",
    "33": "احزاب (گروه‌ها و لشکرها)",
    "34": "سبأ (قوم سبا)",
    "35": "فاطر (آفریننده)",
    "36": "یس (یاسین)",
    "37": "صافات (صف‌کشیدگان)",
    "38": "ص (صاد)",
    "39": "زمر (دسته‌ها و گروه‌ها)",
    "40": "غافر (بخشاینده گناهان)",
    "41": "فصلت (آیات روشن و متمایز)",
    "42": "شوری (مشورت)",
    "43": "زخرف (زیور و طلا)",
    "44": "دخان (دود)",
    "45": "جاثیه (زانو زده)",
    "46": "احقاف (شنزارها)",
    "47": "محمد (حضرت محمد ص)",
    "48": "فتح (پیروزی بزرگ)",
    "49": "حجرات (اتاق‌ها)",
    "50": "ق (قاف)",
    "51": "ذاریات (بادهای پراکنده‌کننده)",
    "52": "طور (کوه طور)",
    "53": "نجم (ستاره)",
    "54": "قمر (ماه)",
    "55": "الرحمن (بخشاینده)",
    "56": "واقعه (حادثه بزرگ قیامت)",
    "57": "حدید (آهن)",
    "58": "مجادله (زن گفتگوکننده)",
    "59": "حشر (راندن و گردآوری)",
    "60": "ممتحنه (زن آزمایش‌شده)",
    "61": "صف (صف بستن در راه خدا)",
    "62": "جمعه (روز جمعه)",
    "63": "منافقون (دورویان)",
    "64": "تغابن (زیانکاری آشکار)",
    "65": "طلاق (جدایی همسران)",
    "66": "تحریم (حرام کردن)",
    "67": "ملک (فرمانروایی و قدرت)",
    "68": "قلم (قلم و نگارش)",
    "69": "حاقه (قیامت حتمی)",
    "70": "معارج (درجات و پلکان آسمان)",
    "71": "نوح (حضرت نوح ع)",
    "72": "جن (پریان / جنیان)",
    "73": "مزمل (جامه‌به‌خودپیچیده)",
    "74": "مدثر (لباس‌برخودپوشیده)",
    "75": "قیامت (روز رستاخیز)",
    "76": "انسان (آدمی / دهر)",
    "77": "مرسلات (فرستادگان)",
    "78": "نبأ (خبر بزرگ)",
    "79": "نازعات (فرشتگان قبض روح)",
    "80": "عبس (چهره در هم کشید)",
    "81": "تکویر (درهم‌پیچیده شدن خورشید)",
    "82": "انفطار (شکافته شدن آسمان)",
    "83": "مطففین (کم‌فروشان)",
    "84": "انشقاق (شکافتن آسمان)",
    "85": "بروج (برج‌های فلکی)",
    "86": "طارق (ستاره شبگرد)",
    "87": "اعلی (بلندمرتبه‌ترین)",
    "88": "غاشیه (فراگیرنده / قیامت)",
    "89": "فجر (سپیده‌دم)",
    "90": "بلد (شهر مکه)",
    "91": "شمس (خورشید)",
    "92": "لیل (شب)",
    "93": "ضحی (روشنایی روز)",
    "94": "شرح (گشایش سینه)",
    "95": "تین (انجیر)",
    "96": "علق (خون بسته)",
    "97": "قدر (شب قدر و منزلت)",
    "98": "بینه (دلیل روشن و آشکار)",
    "99": "زلزله (زمین‌لرزه بزرگ)",
    "100": "عادیات (اسبان دونده)",
    "101": "قارعه (کوبنده / قیامت)",
    "102": "تکاثر (فخرفروشی به مال و ثروت)",
    "103": "عصر (زمانه / هنگام عصر)",
    "104": "همزه (عیب‌جو و طعنه‌زن)",
    "105": "فیل (فیل‌سواران ابرهه)",
    "106": "قریش (قبیله قریش)",
    "107": "ماعون (کمک‌های اندک و زکات)",
    "108": "کوثر (خیر و برکت فراوان)",
    "109": "کافرون (بی‌دینان و کافران)",
    "110": "نصر (یاری و پیروزی خدا)",
    "111": "مسد (ریسمان بافته از لیف خرما)",
    "112": "اخلاص (توحید و یگانگی خدا)",
    "113": "فلق (سپیده صبح)",
    "114": "ناس (مردم)"
}

# 2. 7 Categories (Bentuk Kata) in Persian
BENTUK_KATA_FA = {
    '1. Dhamir': '۱. ضمایر (Dhamir - Pronouns)',
    '2. Mawshul': '۲. اسم‌های موصول (Mawshul - Relative Pronouns)',
    '3. Istifham': '۳. کلمات پرسشی (Istifham - Interrogatives)',
    '4. Syarath': '۴. ادوات شرط (Syarath - Conditionals)',
    '5. Isyarah': '۵. اسم‌های اشاره (Isyarah - Demonstratives)',
    "6. Isim Fi'il": "۶. اسم‌های فعل (Isim Fi'il - Verbal Nouns)",
    "7. Fi'il Jamid": "۷. افعال جامد (Fi'il Jamid - Inflexible Verbs)"
}

# 3. 76 Jamid Mabny Grammatical Metadata in Persian
PERSIAN_GRAMMAR = {
    # 1. Dhamir
    '1. Dhamir__1a': {
        'arti_fa': 'او (مذکر)',
        'desc_fa': 'او (ضمیر منفصل مرفوعی، سوم شخص مفرد مذکر)',
        'jenis_fa': 'منفصل مرفوعی (ضمایر جدا)'
    },
    '1. Dhamir__1b': {
        'arti_fa': '..اش / ..او',
        'desc_fa': '...-اش / او (ضمیر متصل منصوبی یا مجروری، سوم شخص مفرد مذکر)',
        'jenis_fa': 'متصل (پیوسته)'
    },
    '1. Dhamir__1c': {
        'arti_fa': 'تنها او را',
        'desc_fa': 'تنها او را / فقط به او (ضمیر منفصل منصوبی مفعولی، مفرد مذکر)',
        'jenis_fa': 'منفصل منصوبی (مفعول به)'
    },
    '1. Dhamir__2a': {
        'arti_fa': 'آن دو تن',
        'desc_fa': 'آن دو تن (ضمیر منفصل مرفوعی، سوم شخص مثنی مذکر/مؤنث)',
        'jenis_fa': 'منفصل مرفوعی (مثنی)'
    },
    '1. Dhamir__2b': {
        'arti_fa': '..آن دو تن',
        'desc_fa': '...-شان (آن دو) (ضمیر متصل، سوم شخص مثنی)',
        'jenis_fa': 'متصل (مثنی)'
    },
    '1. Dhamir__3a': {
        'arti_fa': 'آنان / ایشان (مردان)',
        'desc_fa': 'آنان / ایشان (ضمیر منفصل مرفوعی، سوم شخص جمع مذکر)',
        'jenis_fa': 'منفصل مرفوعی (جمع مذکر)'
    },
    '1. Dhamir__3b': {
        'arti_fa': '..شان / ..آنان',
        'desc_fa': '...-شان / آنان (ضمیر متصل، سوم شخص جمع مذکر)',
        'jenis_fa': 'متصل (جمع مذکر)'
    },
    '1. Dhamir__3c': {
        'arti_fa': 'تنها آنان را',
        'desc_fa': 'تنها آنان را (ضمیر منفصل منصوبی مفعولی، جمع مذکر)',
        'jenis_fa': 'منفصل منصوبی (مفعول به)'
    },
    '1. Dhamir__4a': {
        'arti_fa': 'او (مؤنث)',
        'desc_fa': 'او (ضمیر منفصل مرفوعی، سوم شخص مفرد مؤنث)',
        'jenis_fa': 'منفصل مرفوعی (مفرد مؤنث)'
    },
    '1. Dhamir__4b': {
        'arti_fa': '..اش / ..او (مؤنث)',
        'desc_fa': '...-اش / او (ضمیر متصل، سوم شخص مفرد مؤنث)',
        'jenis_fa': 'متصل (مفرد مؤنث)'
    },
    '1. Dhamir__5a': {
        'arti_fa': 'آنان (زنان)',
        'desc_fa': 'آنان (ضمیر منفصل مرفوعی، سوم شخص جمع مؤنث)',
        'jenis_fa': 'منفصل مرفوعی (جمع مؤنث)'
    },
    '1. Dhamir__5b': {
        'arti_fa': '..شان (زنان)',
        'desc_fa': '...-شان (ضمیر متصل، سوم شخص جمع مؤنث)',
        'jenis_fa': 'متصل (جمع مؤنث)'
    },
    '1. Dhamir__6a': {
        'arti_fa': 'تو (مذکر)',
        'desc_fa': 'تو (ضمیر منفصل مرفوعی، دوم شخص مفرد مذکر)',
        'jenis_fa': 'منفصل مرفوعی (مفرد مذکر)'
    },
    '1. Dhamir__6b': {
        'arti_fa': '..ات / ..تو',
        'desc_fa': '...-ات / تو (ضمیر متصل، دوم شخص مفرد مذکر)',
        'jenis_fa': 'متصل (مفرد مذکر)'
    },
    '1. Dhamir__6c': {
        'arti_fa': 'تنها تو را',
        'desc_fa': 'تنها تو را / فقط تو را (ضمیر منفصل منصوبی مفعولی، دوم شخص مفرد مذکر)',
        'jenis_fa': 'منفصل منصوبی (مفعول به)'
    },
    '1. Dhamir__7a': {
        'arti_fa': 'شما دو تن',
        'desc_fa': 'شما دو تن (ضمیر منفصل مرفوعی، دوم شخص مثنی)',
        'jenis_fa': 'منفصل مرفوعی (مثنی)'
    },
    '1. Dhamir__7b': {
        'arti_fa': '..شما دو تن',
        'desc_fa': '...-تان (شما دو نفر) (ضمیر متصل، دوم شخص مثنی)',
        'jenis_fa': 'متصل (مثنی)'
    },
    '1. Dhamir__8a': {
        'arti_fa': 'شما (مردان)',
        'desc_fa': 'شما (ضمیر منفصل مرفوعی، دوم شخص جمع مذکر)',
        'jenis_fa': 'منفصل مرفوعی (جمع مذکر)'
    },
    '1. Dhamir__8b': {
        'arti_fa': '..تان / ..شما',
        'desc_fa': '...-تان / شما (ضمیر متصل، دوم شخص جمع مذکر)',
        'jenis_fa': 'متصل (جمع مذکر)'
    },
    '1. Dhamir__8c': {
        'arti_fa': 'تنها شما را',
        'desc_fa': 'تنها شما را (ضمیر منفصل منصوبی، جمع مخاطب)',
        'jenis_fa': 'منفصل منصوبی (مفعول به)'
    },
    '1. Dhamir__9b': {
        'arti_fa': '..ات / ..تو (مؤنث)',
        'desc_fa': '...-ات / تو (ضمیر متصل، دوم شخص مفرد مؤنث)',
        'jenis_fa': 'متصل (مفرد مؤنث)'
    },
    '1. Dhamir__11a': {
        'arti_fa': 'من',
        'desc_fa': 'من (ضمیر منفصل مرفوعی، متکلم وحده)',
        'jenis_fa': 'منفصل مرفوعی (متکلم وحده)'
    },
    '1. Dhamir__11b': {
        'arti_fa': '..ام / ..مرا',
        'desc_fa': '...-ام / من (ضمیر متصل، متکلم وحده)',
        'jenis_fa': 'متصل (متکلم وحده)'
    },
    '1. Dhamir__11c': {
        'arti_fa': 'تنها مرا',
        'desc_fa': 'تنها مرا / فقط مرا (ضمیر منفصل منصوبی، متکلم وحده)',
        'jenis_fa': 'منفصل منصوبی (مفعول به)'
    },
    '1. Dhamir__12a': {
        'arti_fa': 'ما',
        'desc_fa': 'ما (ضمیر منفصل مرفوعی، متکلم مع‌الغیر)',
        'jenis_fa': 'منفصل مرفوعی (متکلم مع‌الغیر)'
    },
    '1. Dhamir__12b': {
        'arti_fa': '..مان / ..ما',
        'desc_fa': '...-مان / ما (ضمیر متصل، متکلم مع‌الغیر)',
        'jenis_fa': 'متصل (متکلم مع‌الغیر)'
    },
    '1. Dhamir__12c': {
        'arti_fa': 'تنها ما را',
        'desc_fa': 'تنها ما را (ضمیر منفصل منصوبی، متکلم مع‌الغیر)',
        'jenis_fa': 'منفصل منصوبی (مفعول به)'
    },

    # 2. Mawshul
    '2. Mawshul__1': {
        'arti_fa': 'آنچه / هر آنچه',
        'desc_fa': 'آنچه / چیزی که (اسم موصول عام برای غیرعاقل)',
        'jenis_fa': 'اسم موصول (غیرعاقل)'
    },
    '2. Mawshul__2': {
        'arti_fa': 'کسانی که / آنان که',
        'desc_fa': 'کسانی که (اسم موصول خاص برای جمع مذکر عاقل)',
        'jenis_fa': 'اسم موصول (جمع مذکر)'
    },
    '2. Mawshul__3': {
        'arti_fa': 'کسی که / هر کس',
        'desc_fa': 'کسی که / هر کس (اسم موصول عام برای عاقل)',
        'jenis_fa': 'اسم موصول (عاقل)'
    },
    '2. Mawshul__4': {
        'arti_fa': 'آن کسی که (مرد)',
        'desc_fa': 'آن کسی که (اسم موصول خاص برای مفرد مذکر)',
        'jenis_fa': 'اسم موصول (مفرد مذکر)'
    },
    '2. Mawshul__5': {
        'arti_fa': 'کدام‌یک / هر کدام',
        'desc_fa': 'کدام‌یک از آنان (اسم موصول معرب)',
        'jenis_fa': 'اسم موصول معرب'
    },
    '2. Mawshul__6': {
        'arti_fa': 'آن زنی که / آن چیزی که',
        'desc_fa': 'آن زنی که / چیزی که (اسم موصول خاص مفرد مؤنث یا جمع غیرعاقل)',
        'jenis_fa': 'اسم موصول (مفرد مؤنث)'
    },
    '2. Mawshul__7': {
        'arti_fa': 'آن زنانی که (اللاء)',
        'desc_fa': 'آن زنانی که (اسم موصول خاص جمع مؤنث - اللائی)',
        'jenis_fa': 'اسم موصول (جمع مؤنث)'
    },
    '2. Mawshul__8': {
        'arti_fa': 'آن زنانی که (اللات)',
        'desc_fa': 'آن زنانی که (اسم موصول خاص جمع مؤنث - اللاتی)',
        'jenis_fa': 'اسم موصول (جمع مؤنث)'
    },
    '2. Mawshul__9': {
        'arti_fa': 'آن دو تنی که',
        'desc_fa': 'آن دو نفری که (اسم موصول خاص مثنی مذکر)',
        'jenis_fa': 'اسم موصول (مثنی)'
    },
    '2. Mawshul__10': {
        'arti_fa': 'کدام‌یک از زنان',
        'desc_fa': 'کدام‌یک از آنان (اسم موصول مؤنث)',
        'jenis_fa': 'اسم موصول مؤنث'
    },

    # 3. Istifham
    '3. Istifham__1': {
        'arti_fa': 'چه چیز؟ / چیست؟',
        'desc_fa': 'چه چیزی؟ (اسم استفهام برای غیرعاقل)',
        'jenis_fa': 'اسم استفهام (غیرعاقل)'
    },
    '3. Istifham__2': {
        'arti_fa': 'چگونه؟ / چطور؟',
        'desc_fa': 'چگونه؟ / به چه کیفیتی؟ (اسم استفهام از حال و چگونگی)',
        'jenis_fa': 'اسم استفهام (حال)'
    },
    '3. Istifham__3': {
        'arti_fa': 'چه کسی؟ / کیست؟',
        'desc_fa': 'چه کسی؟ (اسم استفهام برای عاقل)',
        'jenis_fa': 'اسم استفهام (عاقل)'
    },
    '3. Istifham__4': {
        'arti_fa': 'کدام‌یک؟',
        'desc_fa': 'کدام‌یک؟ (اسم استفهام برای تعیین و گزینش)',
        'jenis_fa': 'اسم استفهام (گزینش)'
    },
    '3. Istifham__5': {
        'arti_fa': 'از کجا؟ / چگونه؟',
        'desc_fa': 'از کجا؟ / چگونه؟ (اسم استفهام برای مکان یا کیفیت)',
        'jenis_fa': 'اسم استفهام (مکان / حال)'
    },
    '3. Istifham__6': {
        'arti_fa': 'این چه چیزی است که؟',
        'desc_fa': 'این چیست که؟ (استفهام مرکب مؤکد با ما و ذا)',
        'jenis_fa': 'اسم استفهام مرکب'
    },
    '3. Istifham__7': {
        'arti_fa': 'چند؟ / چه مدت؟',
        'desc_fa': 'چند تا؟ / چه مدت؟ (اسم استفهام برای عدد یا زمان)',
        'jenis_fa': 'اسم استفهام (عدد و زمان)'
    },
    '3. Istifham__8': {
        'arti_fa': 'برای چه؟ / چرا؟',
        'desc_fa': 'چرا؟ / به چه علت؟ (استفهام از علت و سبب، لـ + ما)',
        'jenis_fa': 'حرف جر + استفهام'
    },
    '3. Istifham__9': {
        'arti_fa': 'کجا؟ / در کجا؟',
        'desc_fa': 'کجا؟ (اسم استفهام از مکان)',
        'jenis_fa': 'اسم استفهام (مکان)'
    },
    '3. Istifham__10': {
        'arti_fa': 'چه وقت؟ / کی؟',
        'desc_fa': 'چه وقت؟ (اسم استفهام از زمان وقوع قیامت)',
        'jenis_fa': 'اسم استفهام (زمان)'
    },

    # 4. Syarath
    '4. Syarath__1': {
        'arti_fa': 'هر کس / هر آن‌که',
        'desc_fa': 'هر کس که (اسم شرط جازم دو فعل برای عاقل)',
        'jenis_fa': 'اسم شرط (عاقل)'
    },
    '4. Syarath__2': {
        'arti_fa': 'هر آنچه / هر چه',
        'desc_fa': 'هر چه که انجام دهید (اسم شرط برای غیرعاقل)',
        'jenis_fa': 'اسم شرط (غیرعاقل)'
    },
    '4. Syarath__3': {
        'arti_fa': 'هر بار که / هر زمان',
        'desc_fa': 'هر بار که / هر زمان که (ظرف شرط زمانی)',
        'jenis_fa': 'ظرف شرط زمانی'
    },
    '4. Syarath__4': {
        'arti_fa': 'هر کدام / هر یک',
        'desc_fa': 'هر کدام را که بخوانید (اسم شرط معرب)',
        'jenis_fa': 'اسم شرط معرب'
    },
    '4. Syarath__5': {
        'arti_fa': 'هر کدام از آن دو (مؤکد)',
        'desc_fa': 'هر کدام از آن دو مدت را (شرط همراه با ماء زائده تأکید)',
        'jenis_fa': 'اسم شرط مرکب'
    },

    # 5. Isyarah
    '5. Isyarah__1': {
        'arti_fa': 'این / آن (مذکر)',
        'desc_fa': 'این / آن (اسم اشاره به نزدیک یا دور، مفرد مذکر)',
        'jenis_fa': 'اسم اشاره (مفرد مذکر)'
    },
    '5. Isyarah__2': {
        'arti_fa': 'اینان / آنان',
        'desc_fa': 'اینان / آنان (اسم اشاره به جمع، مذکر و مؤنث)',
        'jenis_fa': 'اسم اشاره (جمع)'
    },
    '5. Isyarah__3': {
        'arti_fa': 'این (مؤنث)',
        'desc_fa': 'این (اسم اشاره به نزدیک، مفرد مؤنث یا جمع غیرعاقل)',
        'jenis_fa': 'اسم اشاره (مفرد مؤنث)'
    },
    '5. Isyarah__4': {
        'arti_fa': 'آن (مؤنث)',
        'desc_fa': 'آن (اسم اشاره به دور، مفرد مؤنث یا جمع غیرعاقل)',
        'jenis_fa': 'اسم اشاره به دور'
    },
    '5. Isyarah__5': {
        'arti_fa': 'اینجا / در این مکان',
        'desc_fa': 'اینجا (اسم اشاره به مکان نزدیک)',
        'jenis_fa': 'اسم اشاره مکان (نزدیک)'
    },
    '5. Isyarah__6': {
        'arti_fa': 'آنجا / در آن مکان',
        'desc_fa': 'آنجا (اسم اشاره به مکان دور)',
        'jenis_fa': 'اسم اشاره مکان (دور)'
    },
    '5. Isyarah__7': {
        'arti_fa': 'این دو تن (مردان)',
        'desc_fa': 'این دو تن (اسم اشاره به مثنی مذکر)',
        'jenis_fa': 'اسم اشاره (مثنی مذکر)'
    },
    '5. Isyarah__8': {
        'arti_fa': 'این دو تن (زنان)',
        'desc_fa': 'این دو تن (اسم اشاره به مثنی مؤنث)',
        'jenis_fa': 'اسم اشاره (مثنی مؤنث)'
    },

    # 6. Isim Fi'il
    "6. Isim Fi'il__1": {
        'arti_fa': 'پاک و منزه است خدا!',
        'desc_fa': 'منزه و پاک است خدا (اسم مصدر مفعول مطلق در معنای تسبیح)',
        'jenis_fa': 'اسم مصدر / تسبیح'
    },
    "6. Isim Fi'il__2": {
        'arti_fa': 'بیاورید! / حاضر کنید!',
        'desc_fa': 'بیاورید دلیل خود را (اسم فعل امر = هاتوا)',
        'jenis_fa': 'اسم فعل امر'
    },
    "6. Isim Fi'il__3": {
        'arti_fa': 'اف بر شما! / بیزاری!',
        'desc_fa': 'اف بر شما! (اسم فعل مضارع برای اظهار کراهت و ناراحتی = اف)',
        'jenis_fa': 'اسم فعل مضارع'
    },
    "6. Isim Fi'il__4": {
        'arti_fa': 'پناه بر خدا!',
        'desc_fa': 'پناه می‌برم به خدا (اسم مصدر منصوبی)',
        'jenis_fa': 'اسم مصدر منصوبی'
    },
    "6. Isim Fi'il__5": {
        'arti_fa': 'بیایید! / پیش آیید!',
        'desc_fa': 'بیایید و بشتابید (اسم فعل امر = هلم)',
        'jenis_fa': 'اسم فعل امر'
    },
    "6. Isim Fi'il__6": {
        'arti_fa': 'چه دور است! / هرگز!',
        'desc_fa': 'چه دور است و ناممکن (اسم فعل ماضی = هیهات)',
        'jenis_fa': 'اسم فعل ماضی'
    },
    "6. Isim Fi'il__7": {
        'arti_fa': 'بیایید و بخوانید!',
        'desc_fa': 'بیایید نامه اعمال مرا بخوانید (اسم فعل امر = هاؤم)',
        'jenis_fa': 'اسم فعل امر'
    },
    "6. Isim Fi'il__8": {
        'arti_fa': 'بشتاب! / پیش بیا!',
        'desc_fa': 'بشتاب به سوی من (اسم فعل امر = هیت لك)',
        'jenis_fa': 'اسم فعل امر'
    },

    # 7. Fi'il Jamid
    "7. Fi'il Jamid__1": {
        'arti_fa': 'نیست / وجود ندارد',
        'desc_fa': 'نیست (فعل جامد ناقص نفی از اخوات کان)',
        'jenis_fa': 'فعل جامد ناقص (نفی)'
    },
    "7. Fi'il Jamid__2": {
        'arti_fa': 'امید است / شاید',
        'desc_fa': 'امید است که / شاید (فعل جامد رجاء و امیدواری = عسی)',
        'jenis_fa': 'فعل جامد رجاء'
    },
    "7. Fi'il Jamid__3": {
        'arti_fa': 'چه نیکو است! / بهترین',
        'desc_fa': 'چه نیکو و خوب است (فعل جامد مدح و ستایش = نعم)',
        'jenis_fa': 'فعل جامد مدح'
    },
    "7. Fi'il Jamid__4": {
        'arti_fa': 'چه بد است! / بدترین',
        'desc_fa': 'چه بد و ناپسند است (فعل جامد ذم و نکوهش = بئس)',
        'jenis_fa': 'فعل جامد ذم'
    },
    "7. Fi'il Jamid__5": {
        'arti_fa': 'چه بد چیزی است آنچه',
        'desc_fa': 'چه بد است آنچه خود را بدان فروختند (بئس + ما)',
        'jenis_fa': 'فعل جامد ذم مرکب'
    },
    "7. Fi'il Jamid__6": {
        'arti_fa': 'شروع کردند / آغاز نمودند',
        'desc_fa': 'آغاز کردند به پوشاندن خود از برگ‌ها (فعل شروع = طفق)',
        'jenis_fa': 'افعال مقاربه (شروع)'
    },
    "7. Fi'il Jamid__7": {
        'arti_fa': 'منزه است خدا!',
        'desc_fa': 'پاک و منزه است خدا از هر عیب و نقصی (حاش لله)',
        'jenis_fa': 'فعل جامد تنزیه'
    },
    "7. Fi'il Jamid__8": {
        'arti_fa': 'چه نیکو اندرزی است آنچه',
        'desc_fa': 'چه نیکو چیزی است که شما را بدان پند می‌دهد (نعم + ما)',
        'jenis_fa': 'فعل جامد مدح مرکب'
    }
}

# 4. 17 Harf Categories in Persian
BENTUK_HARF_FA = {
    "1. Harf Nafyi": "۱. حروف نفی و انکار (Harf Nafyi)",
    "2. Harf Tahqiq Taswif": "۲. حروف تحقیق و استقبال (Tahqiq & Taswif)",
    "3. Harf Syarat": "۳. حروف شرط غیرجاسم (Harf Syarat)",
    "4. Harf Mashdariyah": "۴. حروف مصدریه (Harf Mashdariyah)",
    "5. Harf Zaidah": "۵. حروف زائده برای تأکید (Harf Zaidah)",
    "6. Harf Istifham": "۶. حرف استفهام و پرسش (Harf Istifham)",
    "7. Harf Jawab": "۷. حروف جواب و تصدیق (Harf Jawab)",
    "8. Harf Ibtida'": "۸. حرف ابتداء و آغاز (Harf Ibtida')",
    "9. Harf Tafshil": "۹. حرف تفصیل و تفکیک (Harf Tafshil)",
    "10. Harf Mufaja'ah": "۱۰. حرف مفاجأة و ناگهانی (Harf Mufaja'ah)",
    "11. Harf Mufassirah": "۱۱. حرف تفسیر و توضیح (Harf Mufassirah)",
    "12. Harf Istiftahiyah": "۱۲. حرف استفتاح و تنبیه (Harf Istiftahiyah)",
    "13. Harf Rada'": "۱۳. حرف ردع و بازدارندگی (Harf Rada')",
    "14. Harf Ta'ajjub": "۱۴. حرف تعجب و شگفتی (Harf Ta'ajjub)",
    "15. Harf Fariqah": "۱۵. حرف فارقه (Harf Fariqah)",
    "16. Harf Mauthi'ah": "۱۶. حرف موطئه برای قسم (Harf Mauthi'ah lil Qasam)",
    "17. Harf Mabany": "۱۷. حروف مقطعه و فواتح سور (Fawaatih as-Suwar)"
}

# 5. 52 Harf Words in Persian
PERSIAN_HARF_GRAMMAR = {
    # 1. Harf Nafyi
    "1. Harf Nafyi__1": {
        "arti_fa": "نه / نیست / هرگز",
        "desc_fa": "نه / نیست (حرف نفی مطلق)",
        "jenis_fa": "حرف نفی (لا)"
    },
    "1. Harf Nafyi__2": {
        "arti_fa": "نه / نیست / وجود ندارد",
        "desc_fa": "نه / نیست (حرف نفی عمومی)",
        "jenis_fa": "حرف نفی (ما)"
    },
    "1. Harf Nafyi__3": {
        "arti_fa": "هیچ نیست مگر",
        "desc_fa": "نیست جز / هیچ نیست مگر (حرف نفی همراه با الا)",
        "jenis_fa": "حرف نفی (إن)"
    },
    "1. Harf Nafyi__4": {
        "arti_fa": "آیا نیست؟ (استفهام انکاری)",
        "desc_fa": "آیا پاداش احسان جز احسان است؟ (استفهام در معنای نفی)",
        "jenis_fa": "استفهام به معنای نفی"
    },
    "1. Harf Nafyi__5": {
        "arti_fa": "وقت گریز نیست",
        "desc_fa": "دیگر وقت گریز و فرار نبود (حرف نفی زمان شبیه لیس)",
        "jenis_fa": "حرف نفی مشبه به لیس"
    },
    "1. Harf Nafyi__6": {
        "arti_fa": "چیست بعد از حق جز گمراهی",
        "desc_fa": "بعد از حق چه چیزی جز گمراهی است؟",
        "jenis_fa": "استفهام به معنای نفی"
    },

    # 2. Harf Tahqiq Taswif
    "2. Harf Tahqiq Taswif__7": {
        "arti_fa": "به راستی / قطعاً",
        "desc_fa": "به تحقیق و قطعاً رستگار شدند (حرف تحقیق و تأکید)",
        "jenis_fa": "حرف تحقیق (قد)"
    },
    "2. Harf Tahqiq Taswif__8": {
        "arti_fa": "به زودی در آینده",
        "desc_fa": "به زودی در آینده خواهید دانست (حرف استقبال و زمان آینده دور)",
        "jenis_fa": "حرف تسویف (آینده)"
    },

    # 3. Harf Syarat
    "3. Harf Syarat__9": {
        "arti_fa": "اگر / اگر چنانچه",
        "desc_fa": "اگر می‌خواستند (حرف شرط غیرجازم برای امتناع)",
        "jenis_fa": "حرف شرط غیرجازم (لو)"
    },
    "3. Harf Syarat__10": {
        "arti_fa": "اگر نبود / لولا",
        "desc_fa": "اگر فضل و رحمت خدا بر شما نبود (حرف امتناع لوجود)",
        "jenis_fa": "حرف امتناع لوجود (لولا)"
    },
    "3. Harf Syarat__11": {
        "arti_fa": "حتی اگر / هرچند",
        "desc_fa": "حتی اگر ناخوشایند باشد (حرف شرط وصلی)",
        "jenis_fa": "حرف شرط وصلی (لو)"
    },
    "3. Harf Syarat__12": {
        "arti_fa": "یا اینکه / اگر چنانچه",
        "desc_fa": "اگر چنانچه (إن شرطیه همراه با ماء تأکید)",
        "jenis_fa": "حرف شرط مرکب (إما)"
    },
    "3. Harf Syarat__13": {
        "arti_fa": "هر آیه‌ای که بیاوری",
        "desc_fa": "هر چه برای ما بیاوری از نشانه‌ها (اسم شرط عام)",
        "jenis_fa": "اسم شرط (مهما)"
    },

    # 4. Harf Mashdariyah
    "4. Harf Mashdariyah__14": {
        "arti_fa": "تا زمانی که / مادام که",
        "desc_fa": "مادام که زنده‌ام (حرف مصدریه ظرفیه زمانی)",
        "jenis_fa": "حرف مصدریه ظرفیه"
    },
    "4. Harf Mashdariyah__15": {
        "arti_fa": "تا اینکه ندانند / تا مبادا",
        "desc_fa": "تا اینکه اهل کتاب بدانند (أن مصدریه + لا نافیه)",
        "jenis_fa": "حرف مصدریه + نفی"
    },
    "4. Harf Mashdariyah__16": {
        "arti_fa": "اینکه / تا اینکه",
        "desc_fa": "اینکه روزه بگیرید برایتان بهتر است (أن مصدریه)",
        "jenis_fa": "حرف مصدریه (أن)"
    },
    "4. Harf Mashdariyah__17": {
        "arti_fa": "دوست دارد که کاش",
        "desc_fa": "دوست دارد کاش هزار سال عمر داده شود (لو مصدریه)",
        "jenis_fa": "حرف مصدریه (لو)"
    },
    "4. Harf Mashdariyah__18": {
        "arti_fa": "اینکه نپرستید جز خدا",
        "desc_fa": "اینکه جز خدای یکتا را عبادت نکنید (أن مصدریه + نهی)",
        "jenis_fa": "حرف مصدریه + نهی"
    },
    "4. Harf Mashdariyah__19": {
        "arti_fa": "اینکه به درستی",
        "desc_fa": "اینکه معبودی جز او نیست (أن مخففه از مثقله)",
        "jenis_fa": "حرف مصدری مخففه"
    },

    # 5. Harf Zaidah
    "5. Harf Zaidah__20": {
        "arti_fa": "همان‌گونه که",
        "desc_fa": "همان‌گونه که مردم ایمان آوردند (کاف تشبیه + ماء زائده)",
        "jenis_fa": "کاف تشبیه + ماء زائده"
    },
    "5. Harf Zaidah__21": {
        "arti_fa": "مثالی از پشه یا بالاتر",
        "desc_fa": "مثالی مانند پشه (ماء ابهامیه زائده برای تأکید)",
        "jenis_fa": "ماء ابهامیه زائده"
    },
    "5. Harf Zaidah__22": {
        "arti_fa": "سوگند می‌خورم",
        "desc_fa": "سوگند می‌خورم به روز رستاخیز (لا زائده برای تأکید قسم)",
        "jenis_fa": "لا زائده برای تأکید قسم"
    },
    "5. Harf Zaidah__23": {
        "arti_fa": "به سبب رحمتی از خدا",
        "desc_fa": "به لطف رحمتی از سوی خداوند (باء حرف جر + ماء زائده)",
        "jenis_fa": "حرف جر + ماء زائده"
    },
    "5. Harf Zaidah__24": {
        "arti_fa": "هنگامی که مژده‌رسان آمد",
        "desc_fa": "هنگامی که بشارت‌دهنده آمد (أن زائده بعد از لما)",
        "jenis_fa": "أن زائده بعد از لما"
    },

    # 6. Harf Istifham
    "6. Harf Istifham__25": {
        "arti_fa": "آیا؟ / مگر نه این است؟",
        "desc_fa": "آیا خبر غاشیه به تو رسیده است؟ (حرف استفهام)",
        "jenis_fa": "حرف استفهام (هل)"
    },

    # 7. Harf Jawab
    "7. Harf Jawab__26": {
        "arti_fa": "در این صورت / پس",
        "desc_fa": "در آن صورت ذره‌ای به مردم نمی‌دادند (حرف جواب و جزا)",
        "jenis_fa": "حرف جواب و جزا (إذن)"
    },
    "7. Harf Jawab__27": {
        "arti_fa": "آری! / چرا که نه!",
        "desc_fa": "آری، ما گواهی دادیم (جواب مثبت به پرسش منفی)",
        "jenis_fa": "حرف جواب و ابطال نفی (بلی)"
    },
    "7. Harf Jawab__28": {
        "arti_fa": "آری / بله",
        "desc_fa": "آری، و شما از مقربان خواهید بود (حرف جواب و تصدیق)",
        "jenis_fa": "حرف جواب و تصدیق (نعم)"
    },
    "7. Harf Jawab__29": {
        "arti_fa": "آری! سوگند به پروردگارم",
        "desc_fa": "آری! سوگند به پروردگارم که حق است (حرف جواب برای قسم)",
        "jenis_fa": "حرف جواب همراه با قسم (إی)"
    },

    # 8. Harf Ibtida'
    "8. Harf Ibtida'__30": {
        "arti_fa": "تا آنجا که پیامبر گفت",
        "desc_fa": "تا آنجا که پیامبر و مؤمنان گفتند (حرف ابتداء)",
        "jenis_fa": "حرف ابتداء (حتی)"
    },

    # 9. Harf Tafshil
    "9. Harf Tafshil__31": {
        "arti_fa": "اما / و اما",
        "desc_fa": "اما یتیم را میازار (حرف شرط و تفصیل)",
        "jenis_fa": "حرف شرط و تفصیل (أما)"
    },

    # 10. Harf Mufaja'ah
    "10. Harf Mufaja'ah__32": {
        "arti_fa": "ناگهان ماری شتابان شد",
        "desc_fa": "ناگهان ماری شد که با شتاب می‌دوید (حرف مفاجأة برای رویداد ناگهانی)",
        "jenis_fa": "حرف مفاجأة (إذا)"
    },

    # 11. Harf Mufassirah
    "11. Harf Mufassirah__33": {
        "arti_fa": "که / یعنی اینکه",
        "desc_fa": "به او وحی کردیم که: کشتی را بساز (حرف تفسیر)",
        "jenis_fa": "حرف تفسیر (أن)"
    },

    # 12. Harf Istiftahiyah
    "12. Harf Istiftahiyah__34": {
        "arti_fa": "آگاه باشید! / بدانید!",
        "desc_fa": "آگاه باشید! اولیای خدا نه ترسی دارند و نه اندوهگین می‌شوند",
        "jenis_fa": "حرف استفتاح و تنبیه (ألا)"
    },

    # 13. Harf Rada'
    "13. Harf Rada'__35": {
        "arti_fa": "هرگز چنین نیست! / نه هرگز!",
        "desc_fa": "هرگز چنین نیست! به زودی خواهید دانست (حرف ردع و بازدارندگی)",
        "jenis_fa": "حرف ردع و زجر (کلا)"
    },

    # 14. Harf Ta'ajjub
    "14. Harf Ta'ajjub__36": {
        "arti_fa": "شگفتا! چه صبری بر آتش دارند!",
        "desc_fa": "چقدر بر آتش دوزخ شکیبا هستند! (ماء تعجبیه)",
        "jenis_fa": "ماء تعجبیه"
    },
    
    # 15. Harf Fariqah
    "15. Harf Fariqah__37": {
        "arti_fa": "قطعاً / به درستی که",
        "desc_fa": "قطعاً به هر یک پاداش کامل اعمالشان داده می‌شود",
        "jenis_fa": "لام فارقه / إن مخففه"
    },

    # 16. Harf Mauthi'ah
    "16. Harf Mauthi'ah__38": {
        "arti_fa": "سوگند که اگر اطاعت کنید",
        "desc_fa": "اگر از بشری همانند خود اطاعت کنید زیانکارید",
        "jenis_fa": "لام موطئه برای قسم"
    },

    # 17. Harf Mabany (Fawaatih as-Suwar)
    "17. Harf Mabany__39": {"arti_fa": "حا میم", "desc_fa": "حروف مقطعه آغاز سوره (حم)", "jenis_fa": "حروف مقطعه"},
    "17. Harf Mabany__40": {"arti_fa": "الف لام میم", "desc_fa": "حروف مقطعه آغاز سوره (الم)", "jenis_fa": "حروف مقطعه"},
    "17. Harf Mabany__41": {"arti_fa": "الف لام را", "desc_fa": "حروف مقطعه آغاز سوره (الر)", "jenis_fa": "حروف مقطعه"},
    "17. Harf Mabany__42": {"arti_fa": "طا سین میم", "desc_fa": "حروف مقطعه آغاز سوره (طسم)", "jenis_fa": "حروف مقطعه"},
    "17. Harf Mabany__43": {"arti_fa": "الف لام میم را", "desc_fa": "حروف مقطعه آغاز سوره (المر)", "jenis_fa": "حروف مقطعه"},
    "17. Harf Mabany__44": {"arti_fa": "الف لام میم صاد", "desc_fa": "حروف مقطعه آغاز سوره (المص)", "jenis_fa": "حروف مقطعه"},
    "17. Harf Mabany__45": {"arti_fa": "صاد", "desc_fa": "حرف مقطعه آغاز سوره (ص)", "jenis_fa": "حروف مقطعه"},
    "17. Harf Mabany__46": {"arti_fa": "طا سین", "desc_fa": "حروف مقطعه آغاز سوره (طس)", "jenis_fa": "حروف مقطعه"},
    "17. Harf Mabany__47": {"arti_fa": "طا ها", "desc_fa": "حروف مقطعه آغاز سوره (طه)", "jenis_fa": "حروف مقطعه"},
    "17. Harf Mabany__48": {"arti_fa": "عین سین قاف", "desc_fa": "حروف مقطعه آغاز سوره (عسق)", "jenis_fa": "حروف مقطعه"},
    "17. Harf Mabany__49": {"arti_fa": "قاف", "desc_fa": "حرف مقطعه آغاز سوره (ق)", "jenis_fa": "حروف مقطعه"},
    "17. Harf Mabany__50": {"arti_fa": "کاف ها یا عین صاد", "desc_fa": "حروف مقطعه آغاز سوره (کهیعص)", "jenis_fa": "حروف مقطعه"},
    "17. Harf Mabany__51": {"arti_fa": "نون", "desc_fa": "حرف مقطعه آغاز سوره (ن)", "jenis_fa": "حروف مقطعه"},
    "17. Harf Mabany__52": {"arti_fa": "یا سین", "desc_fa": "حروف مقطعه آغاز سوره (یس)", "jenis_fa": "حروف مقطعه"}
}


def enrich_dhamir_data():
    print("Enriching dhamir_data.json and dhamir_data.js with Persian...")
    
    with open(os.path.join(BASE_DIR, 'fa_translations.json'), 'r', encoding='utf-8') as f:
        fa_translations = json.load(f)

    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = item.get('No kata', '')
        g_key = f"{b}__{nk}"
        
        # 1. BentukKataFA
        item['BentukKataFA'] = BENTUK_KATA_FA.get(b, b)
        
        # 2. SuratArtiFA
        surat_num = str(item.get('SURAT', ''))
        item['SuratArtiFA'] = PERSIAN_SURAHS.get(surat_num, item.get('SuratArtiEN', ''))
        
        # 3. ArtiKataFA & Grammar FA
        g_info = PERSIAN_GRAMMAR.get(g_key, {})
        item['ArtiKataFA'] = g_info.get('arti_fa', item.get('ArtiKataEN', item.get('Arti kata', '')))
        
        if 'Grammar' not in item:
            item['Grammar'] = {}
        if g_info.get('arti_fa'):
            item['Grammar']['arti_fa'] = g_info['arti_fa']
        if g_info.get('desc_fa'):
            item['Grammar']['desc_fa'] = g_info['desc_fa']
        if g_info.get('jenis_fa'):
            item['Grammar']['jenis_fa'] = g_info['jenis_fa']
            
        # 4. TeksArtiFA
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"
        teks_fa = fa_translations.get(v_key, item.get('TeksArtiEN', item.get('TeksArtiID', '')))
        item['TeksArtiFA'] = teks_fa

    # Write dhamir_data.json
    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Write dhamir_data.js
    with open(os.path.join(BASE_DIR, 'dhamir_data.js'), 'w', encoding='utf-8') as f:
        f.write("const DHAMIR_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n\nif (typeof module !== 'undefined' && module.exports) {\n  module.exports = DHAMIR_DATA;\n}\n")

    print(f"dhamir_data successfully updated with Persian! (Total items: {len(data)})")


def enrich_harf_data():
    print("Enriching harf_data.json and harf_data.js with Persian...")
    
    with open(os.path.join(BASE_DIR, 'fa_translations.json'), 'r', encoding='utf-8') as f:
        fa_translations = json.load(f)

    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = item.get('No kata', '')
        g_key = f"{b}__{nk}"
        
        # 1. BentukKataFA
        item['BentukKataFA'] = BENTUK_HARF_FA.get(b, b)
        
        # 2. SuratArtiFA
        surat_num = str(item.get('SURAT', ''))
        item['SuratArtiFA'] = PERSIAN_SURAHS.get(surat_num, item.get('SuratArtiEN', ''))
        
        # 3. ArtiKataFA & Grammar FA
        g_info = PERSIAN_HARF_GRAMMAR.get(g_key, {})
        item['ArtiKataFA'] = g_info.get('arti_fa', item.get('ArtiKataEN', item.get('Arti kata', '')))
        
        if 'Grammar' not in item:
            item['Grammar'] = {}
        if g_info.get('arti_fa'):
            item['Grammar']['arti_fa'] = g_info['arti_fa']
        if g_info.get('desc_fa'):
            item['Grammar']['desc_fa'] = g_info['desc_fa']
        if g_info.get('jenis_fa'):
            item['Grammar']['jenis_fa'] = g_info['jenis_fa']
            
        # 4. TeksArtiFA
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"
        teks_fa = fa_translations.get(v_key, item.get('TeksArtiEN', item.get('TeksArtiID', '')))
        item['TeksArtiFA'] = teks_fa

    # Write harf_data.json
    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Write harf_data.js
    with open(os.path.join(BASE_DIR, 'harf_data.js'), 'w', encoding='utf-8') as f:
        f.write("const HARF_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n\nif (typeof module !== 'undefined' && module.exports) {\n  module.exports = HARF_DATA;\n}\n")

    print(f"harf_data successfully updated with Persian! (Total items: {len(data)})")


if __name__ == '__main__':
    enrich_dhamir_data()
    enrich_harf_data()
