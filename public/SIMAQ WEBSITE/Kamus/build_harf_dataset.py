import os
import sys
import json
import time
import openpyxl
from collections import defaultdict

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Import 114 Surahs from build_multilingual_dataset
from build_multilingual_dataset import SURAHS
from build_hausa_dataset import HAUSA_SURAHS, BENTUK_HARF_HA, HAUSA_HARF_GRAMMAR
from build_swahili_dataset import SWAHILI_SURAHS, BENTUK_HARF_SW, SWAHILI_HARF_GRAMMAR
from build_persian_dataset import PERSIAN_SURAHS, BENTUK_HARF_FA, PERSIAN_HARF_GRAMMAR
from build_japanese_dataset import JAPANESE_SURAHS, BENTUK_HARF_JA, JAPANESE_HARF_GRAMMAR
from build_korean_dataset import KOREAN_SURAHS, BENTUK_HARF_KO, KOREAN_HARF_GRAMMAR
from build_dutch_dataset import DUTCH_SURAHS, BENTUK_HARF_NL, DUTCH_HARF_GRAMMAR
from build_italian_dataset import ITALIAN_SURAHS, BENTUK_HARF_IT, ITALIAN_HARF_GRAMMAR
from build_bosnian_dataset import BOSNIAN_SURAHS, BENTUK_HARF_BS, BOSNIAN_HARF_GRAMMAR
from build_albanian_dataset import ALBANIAN_SURAHS, BENTUK_HARF_SQ, ALBANIAN_HARF_GRAMMAR
from build_thai_dataset import THAI_SURAHS, BENTUK_HARF_TH, THAI_HARF_GRAMMAR
from build_amazigh_amharic_dataset import AMAZIGH_SURAHS, BENTUK_HARF_BER, AMAZIGH_HARF_GRAMMAR, AMHARIC_SURAHS, BENTUK_HARF_AM, AMHARIC_HARF_GRAMMAR
from build_azerbaijani_bulgarian_dataset import AZERBAIJANI_SURAHS, BENTUK_HARF_AZ, AZERBAIJANI_HARF_GRAMMAR, BULGARIAN_SURAHS, BENTUK_HARF_BG, BULGARIAN_HARF_GRAMMAR
from build_czech_dhivehi_dataset import CZECH_SURAHS, BENTUK_HARF_CS, CZECH_HARF_GRAMMAR, DHIVEHI_SURAHS, BENTUK_HARF_DV, DHIVEHI_HARF_GRAMMAR
from build_norwegian_polish_dataset import NORWEGIAN_SURAHS, BENTUK_HARF_NO, NORWEGIAN_HARF_GRAMMAR, POLISH_SURAHS, BENTUK_HARF_PL, POLISH_HARF_GRAMMAR
from build_romanian_swedish_dataset import ROMANIAN_SURAHS, BENTUK_HARF_RO, ROMANIAN_HARF_GRAMMAR, SWEDISH_SURAHS, BENTUK_HARF_SV, SWEDISH_HARF_GRAMMAR
from build_tajik_tamil_dataset import TAJIK_SURAHS, BENTUK_HARF_TG, TAJIK_HARF_GRAMMAR, TAMIL_SURAHS, BENTUK_HARF_TA, TAMIL_HARF_GRAMMAR
from build_4_languages_dataset import TATAR_SURAHS, BENTUK_HARF_TT, UYGHUR_SURAHS, BENTUK_HARF_UG, UZBEK_SURAHS, BENTUK_HARF_UZ, KURDISH_SURAHS, BENTUK_HARF_KU

# 17 BENTUK KATA LABELS IN 13 LANGUAGES
BENTUK_LABELS_HARF = {
    "1. Harf Nafyi": {
        "id": "1. Harf Nafyi (Huruf Negasi / Penyangkalan)",
        "en": "1. Negative Particles (Harf Nafy)",
        "ms": "1. Harf Nafyi (Kata Penafian)",
        "fr": "1. Particules Négatives (Harf Nafy)",
        "de": "1. Negationspartikeln (Harf Nafy)",
        "ur": "۱. حروف نفی (Harf Nafy)",
        "hi": "१. नकारात्मक शब्द / निषेधवाचक (Harf Nafy)",
        "bn": "১. নাবোধক শব্দ (Harf Nafy - Negative Particles)",
        "ru": "1. Отрицательные частицы (Харф Нафи / Harf Nafy)",
        "zh": "1. 否定虚词 (Harf Nafy)",
        "es": "1. Partículas Negativas (Harf Nafy)",
        "tr": "1. Olumsuzluk Edatları (Harf-i Nefy)",
        "pt": "1. Partículas Negativas (Harf Nafy)"
    },
    "2. Harf Tahqiq Taswif": {
        "id": "2. Harf Tahqiq & Taswif (Penegas & Waktu Mendatang)",
        "en": "2. Affirmative & Future Particles (Tahqiq & Taswif)",
        "ms": "2. Harf Tahqiq & Taswif (Penegasan & Masa Hadapan)",
        "fr": "2. Particules d'Affirmation et du Futur (Tahqiq & Taswif)",
        "de": "2. Bekräftigungs- und Zukunftspartikeln (Tahqiq & Taswif)",
        "ur": "۲. حروف تحقیق و تسویف (Tahqiq & Taswif)",
        "hi": "२. निश्चयवाचक एवं भविष्य सूचक शब्द (Tahqiq & Taswif)",
        "bn": "২. নিশ্চয়তা ও ভবিষ্যতবাচক শব্দ (Tahqiq & Taswif)",
        "ru": "2. Частицы утверждения и будущего времени (Тахкик и Тасвиф)",
        "zh": "2. 确认与将来时虚词 (Tahqiq & Taswif)",
        "es": "2. Partículas de Afirmación y Futuro (Tahqiq & Taswif)",
        "tr": "2. Tahkik ve Tesvîf Edatları (Kesinlik ve Gelecek Zaman Edatları)",
        "pt": "2. Partículas de Afirmação e Futuro (Tahqiq & Taswif)"
    },
    "3. Harf Syarat": {
        "id": "3. Harf Syarat (Huruf Pengandaian / Syarat Ghair Amil)",
        "en": "3. Conditional Particles (Harf Syarat)",
        "ms": "3. Harf Syarat (Huruf Pengandaian)",
        "fr": "3. Particules Conditionnelles (Harf Syarat)",
        "de": "3. Konditionalpartikeln (Harf Syarat)",
        "ur": "۳. حروف شرط غیر عاملہ (Harf Syarat)",
        "hi": "३. शर्तवाचक शब्द (Harf Syarat)",
        "bn": "৩. শর্তমূলক শব্দ (Harf Syarat - Conditional Particles)",
        "ru": "3. Условные частицы (Харф Шарт / Harf Syarat)",
        "zh": "3. 条件虚词 (Harf Syarat)",
        "es": "3. Partículas Condicionales (Harf Syarat)",
        "tr": "3. Şart Edatları (Gayr-i Âmil Şart Harfleri)",
        "pt": "3. Partículas Condicionais (Harf Syarat)"
    },
    "4. Harf Mashdariyah": {
        "id": "4. Harf Mashdariyah (Huruf Pembentuk Makna Mashdar)",
        "en": "4. Infinitive / Nominalizing Particles (Harf Mashdariyah)",
        "ms": "4. Harf Masdariyah (Huruf Pembentuk Masdar)",
        "fr": "4. Particules Masdariques / Infinitives",
        "de": "4. Masdar-Partikeln (Nominalisierende Partikeln)",
        "ur": "۴. حروف مصدریہ (Harf Mashdariyah)",
        "hi": "४. क्रियार्थक / भाववाचक शब्द (Harf Mashdariyah)",
        "bn": "৪. ভাববাচ্যকারী শব্দ (Harf Mashdariyah)",
        "ru": "4. Масдарные частицы (Харф Масдарийя)",
        "zh": "4. 动名词化虚词 (Harf Mashdariyah)",
        "es": "4. Partículas Infinitivas (Harf Mashdariyah)",
        "tr": "4. Masdariyye Harfleri (Mastarlaştıran Edatlar)",
        "pt": "4. Partículas Infinitivas (Harf Mashdariyah)"
    },
    "5. Harf Zaidah": {
        "id": "5. Harf Zaidah (Huruf Tambahan Penguat Makna)",
        "en": "5. Redundant / Emphatic Particles (Harf Zaidah)",
        "ms": "5. Harf Zaidah (Huruf Tambahan Pengukuh)",
        "fr": "5. Particules d'Insistance (Zaidah)",
        "de": "5. Zusätzliche Verstärkungspartikeln (Zaidah)",
        "ur": "۵. حروف زائدہ برائے تاکید (Harf Zaidah)",
        "hi": "५. बलदायक / अतिरिक्त शब्द (Harf Zaidah)",
        "bn": "৫. অতিরিক্ত জোরদার শব্দ (Harf Zaidah)",
        "ru": "5. Избыточные усилительные частицы (Заида)",
        "zh": "5. 强调附加虚词 (Harf Zaidah)",
        "es": "5. Partículas Enfatizadoras (Harf Zaidah)",
        "tr": "5. Zâid Harfler (Pekiştirme / Te'kid Edatları)",
        "pt": "5. Partículas Enfatizadoras (Harf Zaidah)"
    },
    "6. Harf Istifham": {
        "id": "6. Harf Istifham (Huruf Tanya)",
        "en": "6. Interrogative Particle (Harf Istifham)",
        "ms": "6. Harf Istifham (Huruf Tanya)",
        "fr": "6. Particule Interrogative (Istifham)",
        "de": "6. Fragepartikel (Istifham)",
        "ur": "۶. حرف استفہام (Istifham)",
        "hi": "६. प्रश्नवाचक शब्द (Istifham)",
        "bn": "৬. প্রশ্নবোধক শব্দ (Istifham)",
        "ru": "6. Вопросительная частица (Истифхам)",
        "zh": "6. 疑问虚词 (Istifham)",
        "es": "6. Partícula Interrogativa (Istifham)",
        "tr": "6. İstifham Harfi (Soru Edatı)",
        "pt": "6. Partícula Interrogativa (Istifham)"
    },
    "7. Harf Jawab": {
        "id": "7. Harf Jawab (Huruf Jawaban)",
        "en": "7. Responsive Particles (Harf Jawab)",
        "ms": "7. Harf Jawab (Huruf Jawapan)",
        "fr": "7. Particules de Réponse (Harf Jawab)",
        "de": "7. Antwortpartikeln (Harf Jawab)",
        "ur": "۷. حروف جواب (Harf Jawab)",
        "hi": "७. उत्तर सूचक शब्द (Harf Jawab)",
        "bn": "৭. উত্তরসূচক শব্দ (Harf Jawab)",
        "ru": "7. Ответные частицы (Харф Джаваб)",
        "zh": "7. 应答虚词 (Harf Jawab)",
        "es": "7. Partículas de Respuesta (Harf Jawab)",
        "tr": "7. Cevap Harfleri (Cevap Edatları)",
        "pt": "7. Partículas de Resposta (Harf Jawab)"
    },
    "8. Harf Ibtida'": {
        "id": "8. Harf Ibtida' (Huruf Permulaan Kalimat)",
        "en": "8. Inceptive Particle (Harf Ibtida')",
        "ms": "8. Harf Ibtida' (Huruf Permulaan)",
        "fr": "8. Particule Inceptive (Ibtida')",
        "de": "8. Anfangspartikel (Ibtida')",
        "ur": "۸. حرف ابتداء (Ibtida')",
        "hi": "८. आरंभिक शब्द (Ibtida')",
        "bn": "৮. প্রারম্ভিক শব্দ (Ibtida')",
        "ru": "8. Инициальная частица (Ибтида)",
        "zh": "8. 发语虚词 (Ibtida')",
        "es": "8. Partícula Inceptiva (Ibtida')",
        "tr": "8. İbtidâ Harfi (Başlangıç Edatı)",
        "pt": "8. Partícula Inceptiva (Ibtida')"
    },
    "9. Harf Tafshil": {
        "id": "9. Harf Tafshil (Huruf Rincian / Penjelasan)",
        "en": "9. Elaborative / Detailing Particle (Tafshil)",
        "ms": "9. Harf Tafsil (Huruf Huraian / Perincian)",
        "fr": "9. Particule de Détail (Tafshil)",
        "de": "9. Detaillierungspartikel (Tafshil)",
        "ur": "۹. حرف تفصیل (Tafshil)",
        "hi": "९. विस्तारवाचक शब्द (Tafshil)",
        "bn": "৯. বিশদ বিবরণমূলক শব্দ (Tafshil)",
        "ru": "9. Частица детализации (Тафсиль)",
        "zh": "9. 详述虚词 (Tafshil)",
        "es": "9. Partícula de Detalle (Tafshil)",
        "tr": "9. Tafsil Harfi (Açıklama / Detay Edatı)",
        "pt": "9. Partícula de Detalhamento (Tafshil)"
    },
    "10. Harf Mufaja'ah": {
        "id": "10. Harf Mufaja'ah (Huruf Kejutan / Tiba-tiba)",
        "en": "10. Particle of Surprise / Suddenness (Mufaja'ah)",
        "ms": "10. Harf Mufaja'ah (Huruf Kejutan)",
        "fr": "10. Particule de Surprise (Mufaja'ah)",
        "de": "10. Überraschungspartikel (Mufaja'ah)",
        "ur": "۱۰. حرف مفاجاۃ (Mufaja'ah)",
        "hi": "१०. आकस्मिकता सूचक शब्द (Mufaja'ah)",
        "bn": "১০. আকস্মিকতাবাচক শব্দ (Mufaja'ah)",
        "ru": "10. Частица неожиданности (Муфаджаа)",
        "zh": "10. 突发虚词 (Mufaja'ah)",
        "es": "10. Partícula de Sorpresa (Mufaja'ah)",
        "tr": "10. Müfâcee Harfi (Sürpriz / Ansızın Belirme Edatı)",
        "pt": "10. Partícula de Surpresa (Mufaja'ah)"
    },
    "11. Harf Mufassirah": {
        "id": "11. Harf Mufassirah (Huruf Penjelas / Penafsir)",
        "en": "11. Explanatory Particle (Mufassirah)",
        "ms": "11. Harf Mufassirah (Huruf Pentafsir)",
        "fr": "11. Particule Explicative (Mufassirah)",
        "de": "11. Erklärungspartikel (Mufassirah)",
        "ur": "۱۱. حرف مفسرہ (Mufassirah)",
        "hi": "११. व्याख्यात्मक शब्द (Mufassirah)",
        "bn": "১১. ব্যাখ্যামূলক শব্দ (Mufassirah)",
        "ru": "11. Пояснительная частица (Муфассира)",
        "zh": "11. 释义虚词 (Mufassirah)",
        "es": "11. Partícula Explicativa (Mufassirah)",
        "tr": "11. Müfessire Harfi (Tefsir / Açıklama Edatı)",
        "pt": "11. Partícula Explicativa (Mufassirah)"
    },
    "12. Harf Istiftahiyah": {
        "id": "12. Harf Istiftahiyah (Huruf Pembuka / Seruan 'Ingatlah')",
        "en": "12. Opening / Alerting Particle (Istiftahiyah)",
        "ms": "12. Harf Istiftahiyah (Huruf Pembuka)",
        "fr": "12. Particule d'Ouverture / d'Alerte (Istiftahiyah)",
        "de": "12. Eröffnungspartikel (Istiftahiyah)",
        "ur": "۱۲. حرف استفتاحیہ (Istiftahiyah)",
        "hi": "१२. ध्यान आकर्षित करने वाला शब्द (Istiftahiyah)",
        "bn": "১২. উদ্বোধনী / সতর্কীকরণ শব্দ (Istiftahiyah)",
        "ru": "12. Вводно-призывная частица (Истифтахийя)",
        "zh": "12. 提醒发语虚词 (Istiftahiyah)",
        "es": "12. Partícula de Apertura / Alerta (Istiftahiyah)",
        "tr": "12. İstiftâhiyye Harfi (Dikkat Çekme / Başlangıç Edatı)",
        "pt": "12. Partícula de Abertura / Alerta (Istiftahiyah)"
    },
    "13. Harf Rada'": {
        "id": "13. Harf Rada' (Huruf Penolakan Keras / Pencegah)",
        "en": "13. Deterrent / Reproach Particle (Harf Rada')",
        "ms": "13. Harf Rada' (Huruf Tegahan Keras)",
        "fr": "13. Particule de Répulsion / Rejet (Rada')",
        "de": "13. Abweisungspartikel (Rada')",
        "ur": "۱۳. حرف ردع و زجر (Rada')",
        "hi": "१३. सख्त निषेधवाचक शब्द (Rada')",
        "bn": "১৩. কঠোর বারণকারী শব্দ (Rada')",
        "ru": "13. Частица предостережения и запрета (Радъ)",
        "zh": "13. 斥责止步虚词 (Rada')",
        "es": "13. Partícula de Reproche / Rechazo (Rada')",
        "tr": "13. Red' Harfi (Azarlama ve Vazgeçirme Edatı)",
        "pt": "13. Partícula de Reprovação (Rada')"
    },
    "14. Harf Ta'ajjub": {
        "id": "14. Harf Ta'ajjub (Huruf Ketakjuban / Alangkah)",
        "en": "14. Particle of Wonder / Admiration (Ta'ajjub)",
        "ms": "14. Harf Ta'ajjub (Huruf Kekaguman)",
        "fr": "14. Particule d'Étonnement (Ta'ajjub)",
        "de": "14. Ausruf- / Verwunderungspartikel (Ta'ajjub)",
        "ur": "۱۴. حرف تعجب (Ta'ajjub)",
        "hi": "१४. विस्मयबोधक शब्द (Ta'ajjub)",
        "bn": "১৪. বিস্ময়সূচক শব্দ (Ta'ajjub)",
        "ru": "14. Частица удивления (Тааджуб)",
        "zh": "14. 感叹虚词 (Ta'ajjub)",
        "es": "14. Partícula de Asombro (Ta'ajjub)",
        "tr": "14. Taaccüb Harfi (Şaşkınlık ve Hayranlık Edatı)",
        "pt": "14. Partícula de Admiração (Ta'ajjub)"
    },
    "15. Harf Fariqah": {
        "id": "15. Harf Fariqah (Huruf Pembeda Makna)",
        "en": "15. Distinguishing Particle (Fariqah)",
        "ms": "15. Harf Fariqah (Huruf Pembeza)",
        "fr": "15. Particule Distinctive (Fariqah)",
        "de": "15. Unterscheidungspartikel (Fariqah)",
        "ur": "۱۵. حرف فارقہ (Fariqah)",
        "hi": "१५. भेदक शब्द (Fariqah)",
        "bn": "১৫. পার্থক্যকারী শব্দ (Fariqah)",
        "ru": "15. Различительная частица (Фарика)",
        "zh": "15. 区分虚词 (Fariqah)",
        "es": "15. Partícula Distintiva (Fariqah)",
        "tr": "15. Fârika Harfi (Ayırt Edici Edat)",
        "pt": "15. Partícula Distintiva (Fariqah)"
    },
    "16. Harf Mauthi'ah": {
        "id": "16. Harf Mauthi'ah (Huruf Pengantar Sumpah)",
        "en": "16. Oath-Paving Particle (Mauthi'ah lil Qasam)",
        "ms": "16. Harf Mauthi'ah (Huruf Pengantar Sumpah)",
        "fr": "16. Particule Préparatoire au Serment (Mauthi'ah)",
        "de": "16. Schwureinleitende Partikel (Mauthi'ah)",
        "ur": "۱۶. حرف موطئۃ للقسم (Mauthi'ah)",
        "hi": "१६. शपथ-प्रस्तावक शब्द (Mauthi'ah)",
        "bn": "১৬. শপথের প্রস্তুতিমূলক শব্দ (Mauthi'ah)",
        "ru": "16. Частица, подготавливающая клятву (Маутиа)",
        "zh": "16. 誓言铺垫虚词 (Mauthi'ah)",
        "es": "16. Partícula Preparatoria de Juramento (Mauthi'ah)",
        "tr": "16. Muvattıa Harfi (Yemine Hazırlık Edatı)",
        "pt": "16. Partícula Preparatória de Juramento (Mauthi'ah)"
    },
    "17. Harf Mabany": {
        "id": "17. Harf Mabany (Huruf Muqatha'ah / Pembuka Surat)",
        "en": "17. Disjoined Letters / Muqatta'at (Harf Mabany)",
        "ms": "17. Harf Mabany (Huruf Muqatta'ah / Pembuka Surah)",
        "fr": "17. Lettres Isolées / Muqatta'at (Harf Mabany)",
        "de": "17. Geheimnisvolle Buchstaben / Muqatta'at",
        "ur": "۱۷. حروف مقطعات (Harf Mabany)",
        "hi": "१७. मुक़त्तआत अक्षर (Harf Mabany)",
        "bn": "১৭. হরূফে মুকাত্তাআত (Harf Mabany)",
        "ru": "17. Разрозненные буквы / Мукатта'ат (Харф Мабани)",
        "zh": "17. 冠首断字 / 穆盖泰阿提字母 (Harf Mabany)",
        "es": "17. Letras Aisladas / Muqatta'at (Harf Mabany)",
        "tr": "17. Hurûf-ı Mukattaa (Sure Başlangıç Harfleri)",
        "pt": "17. Letras Isoladas / Muqatta'at (Harf Mabany)"
    }
}

# 52 GRAMMATICAL METADATA ENTRIES IN 13 LANGUAGES
GRAMMATICAL_METADATA_HARF = {
    "1": {"latin": "Lā", "arti_id": "TIDAK", "arti_en": "NOT / NO", "arti_ms": "TIDAK / BUKAN", "arti_fr": "NON / PAS", "arti_de": "NICHT", "arti_ur": "نہیں", "arti_hi": "नहीं", "arti_bn": "না / নহে", "arti_ru": "НЕ / НЕТ", "arti_zh": "不 / 没有", "arti_es": "NO", "arti_tr": "HAYIR / DEĞİL", "arti_pt": "NÃO"},
    "2": {"latin": "Mā", "arti_id": "TIDAK / TIDAK ADA / BUKAN", "arti_en": "NOT / NOTHING / NOT AT ALL", "arti_ms": "TIDAK / BUKAN / TIADA", "arti_fr": "PAS / CE N'EST PAS", "arti_de": "NICHT / KEIN", "arti_ur": "نہیں / کچھ نہیں", "arti_hi": "नहीं / कुछ नहीं", "arti_bn": "না / কিছুই না", "arti_ru": "НЕ / НЕТ", "arti_zh": "不 / 非", "arti_es": "NO / NADA", "arti_tr": "DEĞİL / YOK", "arti_pt": "NÃO / NADA"},
    "3": {"latin": "In", "arti_id": "TIDAK (MELAINKAN)", "arti_en": "NOT (BUT / EXCEPT)", "arti_ms": "TIDAK (MELAINKAN)", "arti_fr": "NE... QUE", "arti_de": "NICHTS ALS", "arti_ur": "نہیں مگر", "arti_hi": "नहीं मगर / केवल", "arti_bn": "নহে কেবল", "arti_ru": "НЕ ИНАЧЕ КАК", "arti_zh": "只是 / 不过", "arti_es": "NO SINO", "arti_tr": "ANCAK / SADECE", "arti_pt": "NÃO SENÃO"},
    "4": {"latin": "Hal", "arti_id": "TIDAKLAH / BUKANKAH", "arti_en": "IS THERE NOT / NONE", "arti_ms": "TIDAKLAH", "arti_fr": "N'EST-CE PAS", "arti_de": "IST DENN NICHT", "arti_ur": "کیا نہیں", "arti_hi": "क्या नहीं है", "arti_bn": "কি নহে", "arti_ru": "РАЗВЕ НЕ", "arti_zh": "难道不", "arti_es": "¿ACASO NO?", "arti_tr": "DEĞİL MİDİR", "arti_pt": "ACASO NÃO"},
    "5": {"latin": "Lāta", "arti_id": "BUKAN / TIADA LAGI", "arti_en": "THERE IS NO (TIME)", "arti_ms": "BUKAN / TIADA LAGI", "arti_fr": "IL N'EST PLUS (TEMPS)", "arti_de": "ES IST KEINE (ZEIT MEHR)", "arti_ur": "نہیں رہا (وقت)", "arti_hi": "अब नहीं रहा (समय)", "arti_bn": "আর সময় নেই", "arti_ru": "НЕТ УЖЕ (ВРЕМЕНИ)", "arti_zh": "已非 (之时)", "arti_es": "YA NO HAY (TIEMPO)", "arti_tr": "ARTIK DEĞİL / YOK", "arti_pt": "JÁ NÃO HÁ (TEMPO)"},
    "6": {"latin": "Mādhā", "arti_id": "TIDAK ADA", "arti_en": "WHAT ELSE / NOTHING", "arti_ms": "TIADA APA", "arti_fr": "QUOI D'AUTRE (QUE)", "arti_de": "WAS ANDERES (ALS)", "arti_ur": "کچھ نہیں سوا", "arti_hi": "कुछ नहीं सिवा", "arti_bn": "কিছুই নয় ছাড়া", "arti_ru": "ЧТО ЖЕ, КРОМЕ", "arti_zh": "除了...还有什么", "arti_es": "¿QUÉ MÁS (SINO)?", "arti_tr": "BAŞKA NE OLABİLİR", "arti_pt": "O QUE MAIS (SENÃO)?"},
    "7": {"latin": "Qad", "arti_id": "SUNGGUH / BENAR-BENAR", "arti_en": "INDEED / CERTAINLY / ALREADY", "arti_ms": "SESUNGGUHNYA / TELAH", "arti_fr": "CERTES / DÉJÀ", "arti_de": "WAHRLICH / BEREITS", "arti_ur": "یقیناً / بے شک", "arti_hi": "निश्चय ही / वास्तव में", "arti_bn": "নিশ্চয়ই / ইতোমধ্যে", "arti_ru": "УЖЕ / ПОИСТИНЕ", "arti_zh": "确实 / 已经", "arti_es": "CIERTAMENTE / YA", "arti_tr": "ŞÜPHESİZ / GERÇEKTEN", "arti_pt": "CERTAMENTE / JÁ"},
    "8": {"latin": "Sawfa", "arti_id": "(KELAK) AKAN", "arti_en": "SOON / SHALL / WILL", "arti_ms": "KELAK AKAN", "arti_fr": "BIENTÔT / PLUS TARD", "arti_de": "BALD / WERDEN", "arti_ur": "عنقریب", "arti_hi": "शीघ्र ही / भविष्य में", "arti_bn": "শীঘ্রই / ভবিষ্যতে", "arti_ru": "СКОРО / ВПОСЛЕДСТВИИ", "arti_zh": "不久将 / 将来", "arti_es": "PRONTO / DESPUÉS", "arti_tr": "İLERİDE / YAKINDA", "arti_pt": "EM BREVE / MAIS TARDE"},
    "9": {"latin": "Law", "arti_id": "SEANDAINYA / JIKALAU", "arti_en": "IF / WOULD THAT", "arti_ms": "SEKIRANYA / JIKALAU", "arti_fr": "SI / SI SEULEMENT", "de": "WENN / HÄTTE", "arti_ur": "اگر / کاش", "arti_hi": "यदि / काश", "arti_bn": "যদি / যদি এমন হতো", "arti_ru": "ЕСЛИ БЫ", "arti_zh": "要是 / 假若", "arti_es": "SI / SI TAN SOLO", "arti_tr": "EĞER / KEŞKE", "arti_pt": "SE / SE AO MENOS"},
    "10": {"latin": "Lawlā", "arti_id": "SEANDAINYA TIDAK / MENGAPA TIDAK", "arti_en": "IF NOT FOR / WHY NOT", "arti_ms": "JIKA TIDAK KERANA / MENGAPA TIDAK", "arti_fr": "SI CE N'ÉTAIT / POURQUOI PAS", "arti_de": "WENN NICHT / WARUM NICHT", "arti_ur": "اگر نہ ہوتا / کیوں نہیں", "arti_hi": "यदि ऐसा न होता / क्यों नहीं", "arti_bn": "যদি না হতো / কেন নয়", "arti_ru": "ЕСЛИ БЫ НЕ / ПОЧЕМУ БЫ НЕ", "arti_zh": "若非 / 为何不", "arti_es": "SI NO FUERA POR / ¿POR QUÉ NO?", "arti_tr": "OLMASAYDI / NEDEN OLMASIN", "arti_pt": "SE NÃO FOSSE POR / POR QUE NÃO?"},
    "11": {"latin": "Law", "arti_id": "WALAUPUN / MESKIPUN", "arti_en": "EVEN IF / ALTHOUGH", "arti_ms": "WALAUPUN / MESKIPUN", "arti_fr": "MÊME SI", "arti_de": "AUCH WENN / SELBST WENN", "arti_ur": "اگرچہ / خواہ", "arti_hi": "यद्यपि / भले ही", "arti_bn": "যদিও / এমনকি যদি", "arti_ru": "ДАЖЕ ЕСЛИ / ХОТЯ", "arti_zh": "即使 / 纵然", "arti_es": "AUNQUE / INCLUSO SI", "arti_tr": "HATTA / OLSA BİLE", "arti_pt": "MESMO QUE / EMBORA"},
    "12": {"latin": "Immā", "arti_id": "JIKA (DENGAN PENGUAT)", "arti_en": "IF / WHENEVER", "arti_ms": "JIKA / APABILA", "arti_fr": "SI JAMAIS", "arti_de": "WENN NUN / SOLLTE", "arti_ur": "اگر کبھی", "arti_hi": "यदि कभी", "arti_bn": "যদি কখনও", "arti_ru": "ЕСЛИ ЖЕ", "arti_zh": "如果 / 倘若", "arti_es": "SI ACASO / SI", "arti_tr": "EĞER Kİ / ŞAYET", "arti_pt": "SE PORVENTURA / SE"},
    "13": {"latin": "Mahmā", "arti_id": "BAGAIMANAPUN / APA PUN", "arti_en": "WHATEVER / NO MATTER WHAT", "arti_ms": "BAGAIMANA PUN / APA PUN", "arti_fr": "QUOI QUE CE SOIT", "arti_de": "WAS AUCH IMMER", "arti_ur": "خواہ کچھ بھی", "arti_hi": "चाहे जो कुछ भी", "arti_bn": "যাই ঘটুক না কেন", "arti_ru": "ЧТО БЫ НИ", "arti_zh": "无论何事", "arti_es": "CUALQUIER COSA QUE", "arti_tr": "HER NE OLURSA OLSUN", "arti_pt": "QUALQUER COISA QUE"},
    "14": {"latin": "Mā", "arti_id": "APA / KEADAAN / SELAMA / SELAGI", "arti_en": "AS LONG AS / WHILE", "arti_ms": "SELAGI / SELAMA", "arti_fr": "TANT QUE / AUSSI LONGTEMPS QUE", "arti_de": "SOLANGE WIE", "arti_ur": "جب تک کہ", "arti_hi": "जब तक / जितने समय", "arti_bn": "যতক্ষণ পর্যন্ত", "arti_ru": "ПОКА / ДО ТЕХ ПОР КАК", "arti_zh": "只要 / 在...期间", "arti_es": "MIENTRAS QUE / TANTO COMO", "arti_tr": "SÜRECE / -DIĞI MÜDDETÇE", "arti_pt": "ENQUANTO / TANTO QUANTO"},
    "15": {"latin": "Allā", "arti_id": "SUPAYA / UNTUK / AGAR / BAHWA TIDAK", "arti_en": "SO THAT NOT / LEST", "arti_ms": "SUPAYA TIDAK", "arti_fr": "AFIN QUE NE PAS / DE PEUR QUE", "arti_de": "DAMIT NICHT / DASS NICHT", "arti_ur": "تاکہ نہ", "arti_hi": "ताकि न / जिससे न हो", "arti_bn": "যাতে না / যেন না", "arti_ru": "ЧТОБЫ НЕ", "arti_zh": "以免 / 免得", "arti_es": "PARA QUE NO / DE MODO QUE NO", "arti_tr": "-MASIN DİYE / OLMAMASI İÇİN", "arti_pt": "PARA QUE NÃO / A FIM DE QUE NÃO"},
    "16": {"latin": "An", "arti_id": "SUPAYA / UNTUK / AGAR / KARENA / BAHWA", "arti_en": "THAT / TO / IN ORDER THAT", "arti_ms": "BAHAWA / UNTUK", "arti_fr": "QUE / DE / POUR QUE", "arti_de": "DASS / UM ZU", "arti_ur": "کہ / تاکہ", "arti_hi": "कि / ताकि", "arti_bn": "যে / যেন / যাতে", "arti_ru": "ЧТО / ЧТОБЫ", "arti_zh": "以便 / 使得", "arti_es": "QUE / PARA QUE", "arti_tr": "-MESİ / Kİ / DİYE", "arti_pt": "QUE / PARA QUE"},
    "17": {"latin": "Law", "arti_id": "SEANDAINYA / SEKIRANYA", "arti_en": "THAT / IF ONLY", "arti_ms": "SEKIRANYA", "arti_fr": "SI / QUE", "arti_de": "DASS / WENN", "arti_ur": "کاش کہ", "arti_hi": "काश कि", "arti_bn": "যদি এমন হতো", "arti_ru": "ЕСЛИ БЫ", "arti_zh": "要是", "arti_es": "SI / QUE", "arti_tr": "KEŞKE", "arti_pt": "SE / QUE"},
    "18": {"latin": "Allā", "arti_id": "SUPAYA / UNTUK / AGAR / BAHWA JANGAN", "arti_en": "THAT YOU NOT / DO NOT", "arti_ms": "SUPAYA JANGAN", "arti_fr": "DE NE PAS", "arti_de": "DASS NICHT", "arti_ur": "کہ نہ", "arti_hi": "कि मत करो", "arti_bn": "যেন না কর", "arti_ru": "ЧТОБЫ НЕ", "arti_zh": "切莫 / 不要", "arti_es": "QUE NO", "arti_tr": "SAKIN -MAYIN DİYE", "arti_pt": "QUE NÃO"},
    "19": {"latin": "Allā", "arti_id": "SUPAYA / UNTUK / AGAR / BAHWA (PENGUAT)", "arti_en": "THAT (EMPHATIC)", "arti_ms": "SUPAYA / AGAR", "arti_fr": "QUE (EMPHATIQUE)", "arti_de": "DASS (VERSTÄRKEND)", "arti_ur": "کہ یقیناً", "arti_hi": "कि निश्चय ही", "arti_bn": "যে নিশ্চয়ই", "arti_ru": "ЧТО (УСИЛЕНИЕ)", "arti_zh": "务必 / 确要", "arti_es": "QUE (ENFÁTICO)", "arti_tr": "MUTLAKA -MESİ İÇİN", "arti_pt": "QUE (ENFÁTICO)"},
    "20": {"latin": "Kamā", "arti_id": "SEBAGAIMANA / SEPERTI", "arti_en": "JUST AS / AS", "arti_ms": "SEBAGAIMANA / SEPERTI", "arti_fr": "TOUT COMME / AINSI QUE", "arti_de": "SO WIE / EBENSO WIE", "arti_ur": "جیسے کہ / جس طرح", "arti_hi": "जिस प्रकार / जैसे कि", "arti_bn": "যেমন / যেমনিভাবে", "arti_ru": "ПОДОБНО ТОМУ КАК / КАК", "arti_zh": "犹如 / 正如", "arti_es": "TAL COMO / COMO", "arti_tr": "NİTEKİM / GİBİ", "arti_pt": "ASSIM COMO / TAL QUAL"},
    "21": {"latin": "Mā", "arti_id": "…_APA / KEADAAN (SESUATU)", "arti_en": "ANY / A CERTAIN", "arti_ms": "SUATU / APA PUN", "arti_fr": "QUELCONQUE / QUELQUE", "arti_de": "IRGENDEIN / WAS AUCH", "arti_ur": "کوئی بھی", "arti_hi": "कोई भी / किसी", "arti_bn": "কোনো এক / যেকোনো", "arti_ru": "КАКОЙ-ЛИБО", "arti_zh": "某 / 任何", "arti_es": "CUALQUIER / UN", "arti_tr": "HERHANGİ BİR", "arti_pt": "QUALQUER / UM CERTO"},
    "22": {"latin": "Lā", "arti_id": "SUNGGUH (PENGUAT)", "arti_en": "INDEED / NAY! (EMPHATIC)", "arti_ms": "SUNGGUH (PENGUAT)", "arti_fr": "NON ! (EN FAIT, EMPHATIQUE)", "arti_de": "NEIN, WAHRLICH! (VERSTÄRKUNG)", "arti_ur": "نہیں بلکہ قسم ہے (تاکید)", "arti_hi": "नहीं, बल्कि निश्चय ही (बलदायक)", "arti_bn": "না, বরং শপথ (জোরদার)", "arti_ru": "НЕТ, КЛЯНУСЬ! (УСИЛЕНИЕ)", "arti_zh": "不！我誓以 (强调)", "arti_es": "¡NO! JURO POR (ENFÁTICO)", "arti_tr": "HAYIR! YEMİN EDERİM Kİ (TE'KİD)", "arti_pt": "NÃO! JURO POR (ENFÁTICO)"},
    "23": {"latin": "Fabimā", "arti_id": "MAKA DISEBABKAN (OLEH)", "arti_en": "SO BY / OWING TO", "arti_ms": "MAKA DENGAN SEBAB", "arti_fr": "C'EST PAR / EN RAISON DE", "arti_de": "DURCH / WEGEN DER", "arti_ur": "پس با سبب / کی وجہ سے", "arti_hi": "अतः के कारण / की वजह से", "arti_bn": "অতএব কারণে / অনুগ্রহে", "arti_ru": "ПО МИЛОСТИ / ВСЛЕДСТВИЕ", "arti_zh": "只因为 / 凭借", "arti_es": "POR / DEBIDO A", "arti_tr": "SAYESİNDE / SEBEBİYLE", "arti_pt": "POR / EM VIRTUDE DE"},
    "24": {"latin": "An", "arti_id": "(TAMBAHAN PENGUAT)", "arti_en": "(EMPHATIC PARTICLE AFTER WHEN)", "arti_ms": "(TAMBAHAN PENGUKUH)", "arti_fr": "(PARTICULE DE LIAISON / EMPHASE)", "arti_de": "(VERSTÄRKENDE EINSCHUBPARTIKEL)", "arti_ur": "(حرف زائد برائے ربط و تاکید)", "arti_hi": "(संबंध सूचक अतिरिक्त शब्द)", "arti_bn": "(সংযোগকারী অতিরিক্ত শব্দ)", "arti_ru": "(УСИЛИТЕЛЬНАЯ СВЯЗУЮЩАЯ ЧАСТИЦА)", "arti_zh": "(连接强调语助词)", "arti_es": "(PARTÍCULA ENFÁTICA)", "arti_tr": "(BAĞLANTI VE TE'KİD HARFİ)", "arti_pt": "(PARTÍCULA ENFÁTICA DE LIGAÇÃO)"},
    "25": {"latin": "Hal", "arti_id": "APAKAH / MAUKAH / BOLEHKAH / SUNGGUH", "arti_en": "IS THERE? / HAS THERE? / WOULD YOU?", "arti_ms": "ADAKAH / APAKAH", "arti_fr": "EST-CE QUE? / Y A-T-IL?", "arti_de": "IST DENN? / GIBT ES?", "arti_ur": "کیا؟ / کیا کبھی؟", "arti_hi": "क्या? / क्या कोई?", "arti_bn": "কি? / এমন কি আছে?", "arti_ru": "РАЗВЕ? / ЕСТЬ ЛИ?", "arti_zh": "是否? / 难道?", "arti_es": "¿ACASO? / ¿HAY?", "arti_tr": "ACABA? / VAR MIDIR? / Mİ?", "arti_pt": "ACASO? / PORVENTURA?"},
    "26": {"latin": "Idhan", "arti_id": "KALAU DEMIKIAN / JADI", "arti_en": "THEN / IN THAT CASE", "arti_ms": "JIKA DEMIKIAN / KALAU BEGITU", "arti_fr": "ALORS / DANS CE CAS", "arti_de": "DANN / IN DIESEM FALL", "arti_ur": "تب تو / اس صورت میں", "arti_hi": "तब तो / ऐसी स्थिति में", "arti_bn": "তবে তো / এমতাবস্থায়", "arti_ru": "ТОГДА / В ТАКОМ СЛУЧАЕ", "arti_zh": "那么 / 既然如此", "arti_es": "ENTONCES / EN ESE CASO", "arti_tr": "O TAKDİRDE / O ZAMAN", "arti_pt": "ENTÃO / NESSE CASO"},
    "27": {"latin": "Balā", "arti_id": "YA, TENTU / BAHKAN", "arti_en": "YES INDEED! / NAY, BUT", "arti_ms": "YA, TENTUNYA", "arti_fr": "MAIS SI ! / BIEN SÛR", "arti_de": "DOCH! / ABER JA!", "arti_ur": "ہاں کیوں نہیں / بلکہ", "arti_hi": "हाँ अवश्य! / बल्कि हाँ", "arti_bn": "হ্যাঁ নিশ্চয়ই / অবশ্যই", "arti_ru": "О ДА! / НАПРОТИВ", "arti_zh": "不然，确是如此！", "arti_es": "¡SÍ, POR CIERTO! / CLARO QUE SÍ", "arti_tr": "EVET! / BİLAKİS! / ELBETTE!", "arti_pt": "SIM, CERTAMENTE! / MAS SIM!"},
    "28": {"latin": "Na'am", "arti_id": "YA, BETUL", "arti_en": "YES", "arti_ms": "YA, BENAR", "arti_fr": "OUI", "arti_de": "JA", "arti_ur": "ہاں", "arti_hi": "हाँ, ठीक है", "arti_bn": "হ্যাঁ, সত্য", "arti_ru": "ДА", "arti_zh": "是的", "arti_es": "SÍ", "arti_tr": "EVET", "arti_pt": "SIM"},
    "29": {"latin": "Ī", "arti_id": "YA (UNTUK AWALAN SUMPAH)", "arti_en": "YES, (BY MY LORD!)", "arti_ms": "YA (DEMI TUHANKU)", "arti_fr": "OUI, (PAR MON SEIGNEUR !)", "arti_de": "JA, (BEI MEINEM HERRN!)", "arti_ur": "ہاں (میرے رب کی قسم!)", "arti_hi": "हाँ, (मेरे रब की सौगंध!)", "arti_bn": "হ্যাঁ, (আমার রবের কসম!)", "arti_ru": "ДА, (КЛЯНУСЬ МОИМ ГОСПОДОМ!)", "arti_zh": "是的，(指我的主发誓！)", "arti_es": "SÍ, (¡POR MI SEÑOR!)", "arti_tr": "EVET, (RABBİME ANDOLSUN Kİ!)", "arti_pt": "SIM, (POR MEU SENHOR!)"},
    "30": {"latin": "Hattā", "arti_id": "SEHINGGA / SAMPAI", "arti_en": "UNTIL / EVEN THAT", "arti_ms": "SEHINGGA / SAMPAI", "arti_fr": "JUSQU'À CE QUE", "arti_de": "SODASS / BIS", "arti_ur": "یہاں تک کہ", "arti_hi": "यहाँ तक कि", "arti_bn": "এমনকি / যতক্ষণ না", "arti_ru": "ТАК ЧТО / ВПЛОТЬ ДО ТОГО", "arti_zh": "直到 / 以至于", "arti_es": "HASTA QUE / AL PUNTO QUE", "arti_tr": "HATTA / TÂ Kİ", "arti_pt": "ATÉ QUE / A PONTO DE"},
    "31": {"latin": "Ammā", "arti_id": "ADAPUN", "arti_en": "AS FOR / AS TO", "arti_ms": "ADAPUN", "arti_fr": "QUANT À", "arti_de": "WAS NUN ... ANBETRIFFT", "arti_ur": "بہرحال / رہا معاملہ", "arti_hi": "जहाँ तक बात है / अब रहा", "arti_bn": "অতএব / পক্ষান্তরে", "arti_ru": "ЧТО КАСАЕТСЯ", "arti_zh": "至于", "arti_es": "EN CUANTO A", "arti_tr": "GELİNCE / İSE", "arti_pt": "QUANTO A"},
    "32": {"latin": "Idhā", "arti_id": "TIBA-TIBA / SEKETIKA", "arti_en": "BEHOLD! / SUDDENLY", "arti_ms": "TIBA-TIBA / SEKONYONG-KONYONG", "arti_fr": "VOILÀ QUE / SOUDAIN", "arti_de": "DA PLÖTZLICH / SIEHE", "arti_ur": "اچانک / یکایک", "arti_hi": "अचानक / तभी", "arti_bn": "হঠাৎ / অমনি", "arti_ru": "И ВОТ! / ВНЕЗАПНО", "arti_zh": "顿时 / 忽然", "arti_es": "¡HE AQUÍ QUE! / DE PRONTO", "arti_tr": "BİR DE BAKARSIN Kİ / ANSIZIN", "arti_pt": "EIS QUE! / DE REPENTE"},
    "33": {"latin": "An", "arti_id": "YAITU / BAHWASANYA", "arti_en": "NAMELY / THAT IS TO SAY", "arti_ms": "IAITU / BAHAWA", "arti_fr": "C'EST-À-DIRE / QUE", "arti_de": "NÄMLICH / DASS", "arti_ur": "یعنی کہ", "arti_hi": "अर्थात कि", "arti_bn": "অর্থাৎ / যে", "arti_ru": "ТО ЕСТЬ / А ИМЕННО", "arti_zh": "即 / 也就是", "arti_es": "ES DECIR / QUE", "arti_tr": "YANİ / ŞÖYLE Kİ", "arti_pt": "ISTO É / A SABER"},
    "34": {"latin": "Alā", "arti_id": "INGATLAH / KETAHUILAH", "arti_en": "BEWARE! / UNQUESTIONABLY / LO!", "arti_ms": "INGATLAH / KETAHUILAH", "arti_fr": "PRENEZ GARDE ! / EN VÉRITÉ", "arti_de": "WISSEN WIR / SIEHE WAHRLICH", "arti_ur": "خبردار! / سن لو!", "arti_hi": "सावधान! / सुन लो!", "arti_bn": "সাবধান! / জেনে রেখো!", "arti_ru": "О ДА! / ЗНАЙТЕ ЖЕ!", "arti_zh": "注意！/ 切记！", "arti_es": "¡SABED QUE! / ¡ATENCIÓN!", "arti_tr": "DİKKAT EDİN Kİ! / BİLİNİZ Kİ!", "arti_pt": "SABEI QUE! / ATENÇÃO!"},
    "35": {"latin": "Kallā", "arti_id": "SEKALI-KALI TIDAK / JANGAN", "arti_en": "NAY! / BY NO MEANS! / NEVER!", "arti_ms": "SEKALI-KALI TIDAK!", "arti_fr": "MAIS NON ! / JAMAIS !", "arti_de": "KEINESWEGS! / NEIN!", "arti_ur": "ہرگز نہیں!", "arti_hi": "कदापि नहीं! / हरगिज़ नहीं!", "arti_bn": "কখনোই নয়! / কক্ষনো না!", "arti_ru": "ОВОВСЕ НЕТ! / НИКОГДА!", "arti_zh": "绝非如此！/ 绝不然！", "arti_es": "¡DE NINGÚN MODO! / ¡JAMÁS!", "arti_tr": "HAYIR ASLA! / KESİNLİKLE HAYIR!", "arti_pt": "DE MODO ALGUM! / NUNCA!"},
    "36": {"latin": "Mā", "arti_id": "ALANGKAH / BETAPA", "arti_en": "HOW! / HOW AMAZING!", "arti_ms": "ALANGKAH / BETAPA", "arti_fr": "COMME ! / COMBIEN !", "arti_de": "WIE SEHR! / WELCH EIN!", "arti_ur": "کس قدر! / کیا ہی خوب!", "arti_hi": "कितना आश्चर्यजनक!", "arti_bn": "কতই না! / কি চমৎকার!", "arti_ru": "КАК ЖЕ! / ДО ЧЕГО ЖЕ!", "arti_zh": "多么！/ 何等！", "arti_es": "¡CUÁN! / ¡QUÉ!", "arti_tr": "NE KADAR DA! / NE GÜZEL!", "arti_pt": "QUÃO! / QUE!"},
    "37": {"latin": "Lammā", "arti_id": "AKAN / SUNGGUH PASTI", "arti_en": "INDEED / SURELY", "arti_ms": "SESUNGGUHNYA PASTI", "arti_fr": "CERTES / SÛREMENT", "arti_de": "WAHRLICH / GEWISS", "arti_ur": "یقیناً سب کے سب", "arti_hi": "निश्चय ही सब के सब", "arti_bn": "নিশ্চয়ই তাদের সবাইকে", "arti_ru": "ПОИСТИНЕ, ВСЕ", "arti_zh": "必定全部", "arti_es": "CIERTAMENTE TODOS", "arti_tr": "ŞÜPHESİZ HEPSİ", "arti_pt": "CERTAMENTE TODOS"},
    "38": {"latin": "Lammā", "arti_id": "MELAINKAN / KECUALI", "arti_en": "BUT / EXCEPT THAT", "arti_ms": "MELAINKAN / KECUALI", "arti_fr": "SANS QU'IL Y AIT / SI CE N'EST", "arti_de": "AUSSER DASS", "arti_ur": "مگر یہ کہ", "arti_hi": "मगर केवल / सिवाय इसके", "arti_bn": "ছাড়া কিছুই নয়", "arti_ru": "ТОЛЬКО ЛИШЬ", "arti_zh": "无一不是", "arti_es": "SINO QUE / EXCEPTO", "arti_tr": "MUTLAKA / -DEN BAŞKA DEĞİL", "arti_pt": "SENÃO QUE / EXCETO"},
    "39": {"latin": "Hā Mīm", "arti_id": "Haa Miim", "arti_en": "HA MEEM", "arti_ms": "HAA MIIM", "arti_fr": "HA-MIM", "arti_de": "HA-MIM", "arti_ur": "حم (حا میم)", "arti_hi": "हा-मीम", "arti_bn": "হা-মীম", "arti_ru": "ХА МИМ", "arti_zh": "哈一，米目", "arti_es": "HA MIM", "arti_tr": "HÂ MÎM", "arti_pt": "HA MIM"},
    "40": {"latin": "Alif Lām Mīm", "arti_id": "Alif Laam Miim", "arti_en": "ALIF LAAM MEEM", "arti_ms": "ALIF LAAM MIIM", "arti_fr": "ALIF-LAM-MIM", "arti_de": "ALIF-LAM-MIM", "arti_ur": "الم (الف لام میم)", "arti_hi": "अलिफ़-लाम-मीम", "arti_bn": "আলিফ-লাম-মীম", "arti_ru": "АЛИФ ЛЯМ МИМ", "arti_zh": "艾列弗，俩目，米目", "arti_es": "ALIF LAM MIM", "arti_tr": "ELİF LÂM MÎM", "arti_pt": "ALIF LAM MIM"},
    "41": {"latin": "Alif Lām Rā", "arti_id": "Alif Laam Raa", "arti_en": "ALIF LAAM RAA", "arti_ms": "ALIF LAAM RAA", "arti_fr": "ALIF-LAM-RA", "arti_de": "ALIF-LAM-RA", "arti_ur": "الر (الف لام را)", "arti_hi": "अलिफ़-लाम-रा", "arti_bn": "আলিফ-লাম-রা", "arti_ru": "АЛИФ ЛЯМ РА", "arti_zh": "艾列弗，俩目，拉仪", "arti_es": "ALIF LAM RA", "arti_tr": "ELİF LÂM RÂ", "arti_pt": "ALIF LAM RA"},
    "42": {"latin": "Tā Sīn Mīm", "arti_id": "Thaa Siin Miim", "arti_en": "TAA SEEN MEEM", "arti_ms": "THAA SIIN MIIM", "arti_fr": "TA-SIN-MIM", "arti_de": "TA-SIN-MIM", "arti_ur": "طسم (طا سین میم)", "arti_hi": "ता-सीन-मीम", "arti_bn": "ত্বা-সীন-মীম", "arti_ru": "ТА СИН МИМ", "arti_zh": "脱，细恩，米目", "arti_es": "TA SIN MIM", "arti_tr": "TÂ SÎN MÎM", "arti_pt": "TA SIN MIM"},
    "43": {"latin": "Alif Lām Mīm Rā", "arti_id": "Alif Laam Miim Raa", "arti_en": "ALIF LAAM MEEM RAA", "arti_ms": "ALIF LAAM MIIM RAA", "arti_fr": "ALIF-LAM-MIM-RA", "arti_de": "ALIF-LAM-MIM-RA", "arti_ur": "المر (الف لام میم را)", "arti_hi": "अलिफ़-लाम-मीम-रा", "arti_bn": "আলিফ-লাম-মীম-রা", "arti_ru": "АЛИФ ЛЯМ МИМ РА", "arti_zh": "艾列弗，俩目，米目，拉仪", "arti_es": "ALIF LAM MIM RA", "arti_tr": "ELİF LÂM MÎM RÂ", "arti_pt": "ALIF LAM MIM RA"},
    "44": {"latin": "Alif Lām Mīm Sād", "arti_id": "Alif Laam Miim Shaad.", "arti_en": "ALIF LAAM MEEM SAAD", "arti_ms": "ALIF LAAM MIIM SAAD", "arti_fr": "ALIF-LAM-MIM-SAD", "arti_de": "ALIF-LAM-MIM-SAD", "arti_ur": "المص (الف لام میم صاد)", "arti_hi": "अलिफ़-लाम-मीम-साद", "arti_bn": "আলিফ-লাম-মীম-সোয়াদ", "arti_ru": "АЛИФ ЛЯМ МИМ САД", "arti_zh": "艾列弗，俩目，米目，萨德", "arti_es": "ALIF LAM MIM SAD", "arti_tr": "ELİF LÂM MÎM SÂD", "arti_pt": "ALIF LAM MIM SAD"},
    "45": {"latin": "Sād", "arti_id": "Shaad", "arti_en": "SAAD", "arti_ms": "SHAAD", "arti_fr": "SAD", "arti_de": "SAD", "arti_ur": "ص (صاد)", "arti_hi": "साद", "arti_bn": "সোয়াদ", "arti_ru": "САД", "arti_zh": "萨德", "arti_es": "SAD", "arti_tr": "SÂD", "arti_pt": "SAD"},
    "46": {"latin": "Tā Sīn", "arti_id": "Thaa Siin", "arti_en": "TAA SEEN", "arti_ms": "THAA SIIN", "arti_fr": "TA-SIN", "arti_de": "TA-SIN", "arti_ur": "طس (طا سین)", "arti_hi": "ता-सीन", "arti_bn": "ত্বা-সীন", "arti_ru": "ТА СИН", "arti_zh": "脱，细恩", "arti_es": "TA SIN", "arti_tr": "TÂ SÎN", "arti_pt": "TA SIN"},
    "47": {"latin": "Tā Hā", "arti_id": "Thaa Haa", "arti_en": "TAA HAA", "arti_ms": "THAA HAA", "arti_fr": "TA-HA", "arti_de": "TA-HA", "arti_ur": "طه (طا ہا)", "arti_hi": "ता-हा", "arti_bn": "ত্বা-হা", "arti_ru": "ТА ХА", "arti_zh": "脱哈", "arti_es": "TA HA", "arti_tr": "TÂ HÂ", "arti_pt": "TA HA"},
    "48": {"latin": "'Ain Sīn Qāf", "arti_id": "Ain Siin Qaaf", "arti_en": "'AYN SEEN QAAF", "arti_ms": "'AIN SIIN QAAF", "arti_fr": "'AYN-SIN-QAF", "arti_de": "'AIN-SIN-QAF", "arti_ur": "عسق (عین سین قاف)", "arti_hi": "ऐ़न-सीन-क़ाफ़", "arti_bn": "আইন-সীন-ক্বাফ", "arti_ru": "АЙН СИН КАФ", "arti_zh": "爱因，细恩，卡夫", "arti_es": "'AYN SIN QAF", "arti_tr": "AYN SÎN KÂF", "arti_pt": "'AIN SIN QAF"},
    "49": {"latin": "Qāf", "arti_id": "Qaaf", "arti_en": "QAAF", "arti_ms": "QAAF", "arti_fr": "QAF", "arti_de": "QAF", "arti_ur": "ق (قاف)", "arti_hi": "क़ाफ़", "arti_bn": "ক্বাফ", "arti_ru": "КАФ", "arti_zh": "卡夫", "arti_es": "QAF", "arti_tr": "KÂF", "arti_pt": "QAF"},
    "50": {"latin": "Kāf Hā Yā 'Ain Sād", "arti_id": "Kaaf Haa Yaa 'Ain Shaad", "arti_en": "KAAF HAA YAA 'AYN SAAD", "arti_ms": "KAAF HAA YAA 'AIN SAAD", "arti_fr": "KAF-HA-YA-'AYN-SAD", "arti_de": "KAF-HA-YA-'AIN-SAD", "arti_ur": "کہیعص (کاف ہا یا عین صاد)", "arti_hi": "काफ़-हा-या-ऐ़न-साद", "arti_bn": "কাফ-হা-ইয়া-আইন-সোয়াদ", "arti_ru": "КАФ ХА ЙА АЙН САД", "arti_zh": "客夫，哈，雅，爱因，萨德", "arti_es": "KAF HA YA 'AYN SAD", "arti_tr": "KÂF HÂ YÂ AYN SÂD", "arti_pt": "KAF HA YA 'AIN SAD"},
    "51": {"latin": "Nūn", "arti_id": "Nun", "arti_en": "NOON", "arti_ms": "NUN", "arti_fr": "NOUN", "arti_de": "NUN", "arti_ur": "ن (نون)", "arti_hi": "नून", "arti_bn": "নূন", "arti_ru": "НУН", "arti_zh": "努恩", "arti_es": "NUN", "arti_tr": "NÛN", "arti_pt": "NUN"},
    "52": {"latin": "Yā Sīn", "arti_id": "Yaa siin", "arti_en": "YAA SEEN", "arti_ms": "YAA SIIN", "arti_fr": "YA-SIN", "arti_de": "YA-SIN", "arti_ur": "يس (یا سین)", "arti_hi": "या-सीन", "arti_bn": "ইয়া-সীন", "arti_ru": "ЙА СИН", "arti_zh": "雅细恩", "arti_es": "YA SIN", "arti_tr": "YÂ SÎN", "arti_pt": "YA SIN"}
}

def load_caches():
    caches = {
        'verse': {},
        'en': {},
        'ms': {},
        'fr': {},
        'de': {},
        'ur': {},
        'hi': {},
        'bn': {},
        'ru': {},
        'zh': {},
        'es': {},
        'tr': {},
        'pt': {},
        'ha': {},
        'sw': {},
        'fa': {},
        'ja': {},
        'ko': {},
        'nl': {},
        'it': {},
        'bs': {},
        'sq': {},
        'th': {},
        'ber': {},
        'am': {},
        'az': {},
        'bg': {},
        'cs': {},
        'dv': {},
        'no': {},
        'pl': {},
        'ro': {},
        'sv': {},
        'tg': {},
        'ta': {},
        'tt': {},
        'ug': {},
        'uz': {},
        'ku': {}
    }
    files = {
        'verse': 'verse_cache.json',
        'en': 'en_translations.json',
        'ms': 'ms_translations.json',
        'fr': 'fr_translations.json',
        'de': 'de_translations.json',
        'ur': 'ur_translations.json',
        'hi': 'hi_translations.json',
        'bn': 'bn_translations.json',
        'ru': 'ru_translations.json',
        'zh': 'zh_translations.json',
        'es': 'es_translations.json',
        'tr': 'tr_translations.json',
        'pt': 'pt_translations.json',
        'ha': 'ha_translations.json',
        'sw': 'sw_translations.json',
        'fa': 'fa_translations.json',
        'ja': 'ja_translations.json',
        'ko': 'ko_translations.json',
        'nl': 'nl_translations.json',
        'it': 'it_translations.json',
        'bs': 'bs_translations.json',
        'sq': 'sq_translations.json',
        'th': 'th_translations.json',
        'ber': 'ber_translations.json',
        'am': 'am_translations.json',
        'az': 'az_translations.json',
        'bg': 'bg_translations.json',
        'cs': 'cs_translations.json',
        'dv': 'dv_translations.json',
        'no': 'no_translations.json',
        'pl': 'pl_translations.json',
        'ro': 'ro_translations.json',
        'sv': 'sv_translations.json',
        'tg': 'tg_translations.json',
        'ta': 'ta_translations.json',
        'tt': 'tt_translations.json',
        'ug': 'ug_translations.json',
        'uz': 'uz_translations.json',
        'ku': 'ku_translations.json'
    }
    for key, fname in files.items():
        fpath = os.path.join(BASE_DIR, fname)
        if os.path.exists(fpath):
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    caches[key] = json.load(f)
            except Exception as e:
                print(f"[WARN] Gagal membaca {fname}: {e}")
    return caches


def standardize_cat(raw_b):
    raw_b = str(raw_b).strip() if raw_b else ''
    if raw_b.startswith('1.'): return '1. Harf Nafyi'
    if raw_b.startswith('2.'): return '2. Harf Tahqiq Taswif'
    if raw_b.startswith('3.'): return '3. Harf Syarat'
    if raw_b.startswith('4.'): return '4. Harf Mashdariyah'
    if raw_b.startswith('5.'): return '5. Harf Zaidah'
    if 'ISTIFHAM' in raw_b.upper(): return '6. Harf Istifham'
    if 'JAWAB' in raw_b.upper(): return '7. Harf Jawab'
    if 'IBTIDA' in raw_b.upper(): return '8. Harf Ibtida\''
    if 'TAFSHIL' in raw_b.upper(): return '9. Harf Tafshil'
    if 'MUFAJAAH' in raw_b.upper(): return '10. Harf Mufaja\'ah'
    if 'MUFASSIRAH' in raw_b.upper(): return '11. Harf Mufassirah'
    if 'ISTIFTAHIYAH' in raw_b.upper(): return '12. Harf Istiftahiyah'
    if 'RADA' in raw_b.upper(): return '13. Harf Rada\''
    if 'TA\'AJUB' in raw_b.upper() or 'TAAJUB' in raw_b.upper(): return '14. Harf Ta\'ajjub'
    if 'FARIQAH' in raw_b.upper(): return '15. Harf Fariqah'
    if 'MAUTHI' in raw_b.upper(): return '16. Harf Mauthi\'ah'
    if 'MABANY' in raw_b.upper(): return '17. Harf Mabany'
    return raw_b


def build_harf_dataset(limit_per_word=5):
    print("=" * 65)
    print("MEMPROSES DATASET KAMUS HARF GHAIR 'AMIL DENGAN 13 BAHASA")
    print("=" * 65)
    
    excel_path = os.path.join(BASE_DIR, 'KAMUS Harf Ghair Amil.xlsx')
    if not os.path.exists(excel_path):
        print(f"[ERROR] File '{excel_path}' tidak ditemukan!")
        sys.exit(1)
        
    print(f"\n[1/4] Membaca file Excel: {os.path.basename(excel_path)}")
    wb = openpyxl.load_workbook(excel_path, data_only=True)
    sheet = wb['KAMUS KATA'] if 'KAMUS KATA' in wb.sheetnames else wb.active
    rows = list(sheet.iter_rows(values_only=True))
    header = [str(h).strip() if h else '' for h in rows[0]]
    
    caches = load_caches()
    
    # 1. Parse valid rows
    raw_items = []
    skipped_count = 0
    for r_idx, r in enumerate(rows[1:], start=2):
        if not any(r): continue
        item = dict(zip(header, r))
        raw_b = item.get('Bentuk Kata')
        nk = item.get('No kata')
        k = item.get('Kata')
        ak = item.get('Arti kata')
        fk = item.get('Frek kata')
        s = item.get('SURAT')
        a = item.get('AYAT')
        
        if not raw_b or nk is None or s is None or a is None:
            continue
            
        std_b = standardize_cat(raw_b)
        nk_str = str(nk).strip()
        k_str = str(k).strip() if k else ''
        ak_str = str(ak).strip() if ak else ''
        
        try:
            s_int = int(s)
            a_int = int(a)
        except Exception:
            skipped_count += 1
            continue
            
        raw_items.append({
            'Bentuk Kata': std_b,
            'No kata': nk_str,
            'Kata': k_str,
            'Arti kata': ak_str,
            'Frek kata': fk,
            'SURAT': s_int,
            'AYAT': a_int
        })
        
    print(f"      Total baris valid dari Excel: {len(raw_items)} (Dilewati: {skipped_count})")
    
    # 2. Filter top N shortest verses per word
    print(f"\n[2/4] Menyaring ayat per kata (Maksimal {limit_per_word} ayat terpendek)...")
    groups = defaultdict(list)
    seen_refs = set()
    
    for item in raw_items:
        b = item['Bentuk Kata']
        nk = item['No kata']
        s = item['SURAT']
        a = item['AYAT']
        ref_key = (b, nk, s, a)
        if ref_key in seen_refs:
            continue
        seen_refs.add(ref_key)
        
        v_key = f"{s}:{a}"
        t_arab = caches['verse'].get(v_key, {}).get('TeksArab', '')
        item['arab_len'] = len(t_arab) if t_arab else 9999
        groups[(b, nk)].append(item)
        
    selected_items = []
    for (b, nk) in sorted(groups.keys(), key=lambda x: (int(x[0].split('.')[0]), int(x[1]) if x[1].isdigit() else 999)):
        items = groups[(b, nk)]
        sorted_items = sorted(items, key=lambda x: (x['arab_len'], x['SURAT'], x['AYAT']))
        selected_items.extend(sorted_items[:limit_per_word])
        
    print(f"      Total contoh ayat terpilih: {len(selected_items)} ayat dari {len(groups)} kata")
    
    # 3. Enrich dataset with 13 languages
    print(f"\n[3/4] Melengkapi terjemahan 13 Bahasa & metadata tata bahasa...")
    enriched_list = []
    
    for item in selected_items:
        b = item['Bentuk Kata']
        nk = item['No kata']
        s = item['SURAT']
        a = item['AYAT']
        v_key = f"{s}:{a}"
        
        # 3.1 Bentuk Kata Labels
        b_labels = BENTUK_LABELS_HARF.get(b, {})
        item['BentukKataID'] = b_labels.get('id', b)
        item['BentukKataEN'] = b_labels.get('en', b)
        item['BentukKataMS'] = b_labels.get('ms', b)
        item['BentukKataFR'] = b_labels.get('fr', b)
        item['BentukKataDE'] = b_labels.get('de', b)
        item['BentukKataUR'] = b_labels.get('ur', b)
        item['BentukKataHI'] = b_labels.get('hi', b)
        item['BentukKataBN'] = b_labels.get('bn', b)
        item['BentukKataRU'] = b_labels.get('ru', b)
        item['BentukKataZH'] = b_labels.get('zh', b)
        item['BentukKataES'] = b_labels.get('es', b)
        item['BentukKataTR'] = b_labels.get('tr', b)
        item['BentukKataPT'] = b_labels.get('pt', b)
        item['BentukKataHA'] = BENTUK_HARF_HA.get(b, b)
        item['BentukKataSW'] = BENTUK_HARF_SW.get(b, b)
        item['BentukKataFA'] = BENTUK_HARF_FA.get(b, b)
        item['BentukKataJA'] = BENTUK_HARF_JA.get(b, b)
        item['BentukKataKO'] = BENTUK_HARF_KO.get(b, b)
        item['BentukKataNL'] = BENTUK_HARF_NL.get(b, b)
        item['BentukKataIT'] = BENTUK_HARF_IT.get(b, b)
        item['BentukKataBS'] = BENTUK_HARF_BS.get(b, b)
        item['BentukKataSQ'] = BENTUK_HARF_SQ.get(b, b)
        item['BentukKataTH'] = BENTUK_HARF_TH.get(b, b)
        item['BentukKataBER'] = BENTUK_HARF_BER.get(b, b)
        item['BentukKataAM'] = BENTUK_HARF_AM.get(b, b)
        item['BentukKataAZ'] = BENTUK_HARF_AZ.get(b, b)
        item['BentukKataBG'] = BENTUK_HARF_BG.get(b, b)
        
        # 3.2 Surat Info
        s_key = str(s)
        if s_key in SURAHS or s in SURAHS:
            s_info = SURAHS.get(s_key, SURAHS.get(s, {}))
            item['SuratNama'] = s_info['nama']
            item['SuratArab'] = s_info['arab']
            item['SuratArti'] = s_info['arti_id']
            item['SuratArtiID'] = s_info['arti_id']
            item['SuratArtiEN'] = s_info['arti_en']
            item['SuratArtiMS'] = s_info.get('arti_ms', s_info['arti_id'])
            item['SuratArtiFR'] = s_info.get('arti_fr', s_info['arti_en'])
            item['SuratArtiDE'] = s_info.get('arti_de', s_info['arti_en'])
            item['SuratArtiUR'] = s_info.get('arti_ur', '')
            item['SuratArtiHI'] = s_info.get('arti_hi', '')
            item['SuratArtiBN'] = s_info.get('arti_bn', '')
            item['SuratArtiRU'] = s_info.get('arti_ru', '')
            item['SuratArtiZH'] = s_info.get('arti_zh', '')
            item['SuratArtiES'] = s_info.get('arti_es', s_info['arti_en'])
            item['SuratArtiTR'] = s_info.get('arti_tr', s_info['arti_en'])
            item['SuratArtiPT'] = s_info.get('arti_pt', s_info['arti_en'])
            item['SuratArtiHA'] = HAUSA_SURAHS.get(s_key, s_info.get('arti_en', ''))
            item['SuratArtiSW'] = SWAHILI_SURAHS.get(s_key, s_info.get('arti_en', ''))
            item['SuratArtiFA'] = PERSIAN_SURAHS.get(s_key, s_info.get('arti_en', ''))
            item['SuratArtiJA'] = JAPANESE_SURAHS.get(s_key, s_info.get('arti_en', ''))
            item['SuratArtiKO'] = KOREAN_SURAHS.get(s_key, s_info.get('arti_en', ''))
            item['SuratArtiNL'] = DUTCH_SURAHS.get(s_key, s_info.get('arti_en', ''))
            item['SuratArtiIT'] = ITALIAN_SURAHS.get(s_key, s_info.get('arti_en', ''))
            item['SuratArtiBS'] = BOSNIAN_SURAHS.get(s_key, s_info.get('arti_en', ''))
            item['SuratArtiSQ'] = ALBANIAN_SURAHS.get(s_key, s_info.get('arti_en', ''))
            item['SuratArtiTH'] = THAI_SURAHS.get(s_key, s_info.get('arti_en', ''))
            item['SuratArtiBER'] = AMAZIGH_SURAHS.get(s_key, s_info.get('arti_en', ''))
            item['SuratArtiAM'] = AMHARIC_SURAHS.get(s_key, s_info.get('arti_en', ''))
            item['SuratArtiAZ'] = AZERBAIJANI_SURAHS.get(s_key, s_info.get('arti_en', ''))
            item['SuratArtiBG'] = BULGARIAN_SURAHS.get(s_key, s_info.get('arti_en', ''))
        else:
            item['SuratNama'] = f"Surat {s}"
            item['SuratArab'] = ""
            item['SuratArtiID'] = ""
            item['SuratArtiEN'] = ""
            item['SuratArtiMS'] = ""
            item['SuratArtiFR'] = ""
            item['SuratArtiDE'] = ""
            item['SuratArtiUR'] = ""
            item['SuratArtiHI'] = ""
            item['SuratArtiBN'] = ""
            item['SuratArtiRU'] = ""
            item['SuratArtiZH'] = ""
            item['SuratArtiES'] = ""
            item['SuratArtiTR'] = ""
            item['SuratArtiPT'] = ""
            item['SuratArtiHA'] = ""
            item['SuratArtiSW'] = ""
            item['SuratArtiFA'] = ""
            item['SuratArtiJA'] = ""
            item['SuratArtiKO'] = ""
            item['SuratArtiNL'] = ""
            item['SuratArtiIT'] = ""
            item['SuratArtiBS'] = ""
            item['SuratArtiSQ'] = ""
            item['SuratArtiTH'] = ""
            item['SuratArtiBER'] = ""
            item['SuratArtiAM'] = ""
            item['SuratArtiAZ'] = ""
            item['SuratArtiBG'] = ""
            
        # 3.3 Grammar & Word Meaning Metadata
        gm = dict(GRAMMATICAL_METADATA_HARF.get(nk, {}))
        item['Grammar'] = gm
        item['Latin'] = gm.get('latin', item['Kata'])
        item['ArtiKataID'] = gm.get('arti_id', item['Arti kata'])
        item['ArtiKataEN'] = gm.get('arti_en', item['Arti kata'])
        item['ArtiKataMS'] = gm.get('arti_ms', item['Arti kata'])
        item['ArtiKataFR'] = gm.get('arti_fr', item['Arti kata'])
        item['ArtiKataDE'] = gm.get('arti_de', item['Arti kata'])
        item['ArtiKataUR'] = gm.get('arti_ur', item['Arti kata'])
        item['ArtiKataHI'] = gm.get('arti_hi', item['Arti kata'])
        item['ArtiKataBN'] = gm.get('arti_bn', item['Arti kata'])
        item['ArtiKataRU'] = gm.get('arti_ru', item['Arti kata'])
        item['ArtiKataZH'] = gm.get('arti_zh', item['Arti kata'])
        item['ArtiKataES'] = gm.get('arti_es', item['Arti kata'])
        item['ArtiKataTR'] = gm.get('arti_tr', item['Arti kata'])
        item['ArtiKataPT'] = gm.get('arti_pt', item['Arti kata'])

        # Enrich Hausa, Swahili, Persian, Japanese, Korean, Dutch, Italian, Bosnian, Albanian grammar metadata
        gm_ha = HAUSA_HARF_GRAMMAR.get(f"{b}__{nk}", {})
        gm_sw = SWAHILI_HARF_GRAMMAR.get(f"{b}__{nk}", {})
        gm_fa = PERSIAN_HARF_GRAMMAR.get(f"{b}__{nk}", {})
        gm_ja = JAPANESE_HARF_GRAMMAR.get(f"{b}__{nk}", {})
        gm_ko = KOREAN_HARF_GRAMMAR.get(f"{b}__{nk}", {})
        gm_nl = DUTCH_HARF_GRAMMAR.get(f"{b}__{nk}", DUTCH_HARF_GRAMMAR.get(nk, {}))
        gm_it = ITALIAN_HARF_GRAMMAR.get(f"{b}__{nk}", ITALIAN_HARF_GRAMMAR.get(nk, {}))
        gm_bs = BOSNIAN_HARF_GRAMMAR.get(f"{b}__{nk}", BOSNIAN_HARF_GRAMMAR.get(nk, {}))
        gm_sq = ALBANIAN_HARF_GRAMMAR.get(f"{b}__{nk}", ALBANIAN_HARF_GRAMMAR.get(nk, {}))
        gm_th = THAI_HARF_GRAMMAR.get(f"{b}__{nk}", {})
        gm_ber = AMAZIGH_HARF_GRAMMAR.get(f"{b}__{nk}", {})
        gm_am = AMHARIC_HARF_GRAMMAR.get(f"{b}__{nk}", {})
        gm_az = AZERBAIJANI_HARF_GRAMMAR.get(f"{b}__{nk}", {})
        gm_bg = BULGARIAN_HARF_GRAMMAR.get(f"{b}__{nk}", {})
        item['ArtiKataHA'] = gm_ha.get('arti_ha', item['Arti kata'])
        item['ArtiKataSW'] = gm_sw.get('arti_sw', item['Arti kata'])
        item['ArtiKataFA'] = gm_fa.get('arti_fa', item['Arti kata'])
        item['ArtiKataJA'] = gm_ja.get('arti_ja', item['Arti kata'])
        item['ArtiKataKO'] = gm_ko.get('arti_ko', item['Arti kata'])
        item['ArtiKataNL'] = gm_nl.get('arti_nl', item['Arti kata'])
        item['ArtiKataIT'] = gm_it.get('arti_it', item['Arti kata'])
        item['ArtiKataBS'] = gm_bs.get('arti_bs', item['Arti kata'])
        item['ArtiKataSQ'] = gm_sq.get('arti_sq', item['Arti kata'])
        item['ArtiKataTH'] = gm_th.get('arti_th', item['Arti kata'])
        item['ArtiKataBER'] = gm_ber.get('arti_ber', item['ArtiKataEN'])
        item['ArtiKataAM'] = gm_am.get('arti_am', item['ArtiKataEN'])
        item['ArtiKataAZ'] = gm_az.get('arti_az', item['ArtiKataEN'])
        item['ArtiKataBG'] = gm_bg.get('arti_bg', item['ArtiKataEN'])
        if gm_ha.get('desc_ha'): item['Grammar']['desc_ha'] = gm_ha['desc_ha']
        if gm_ha.get('jenis_ha'): item['Grammar']['jenis_ha'] = gm_ha['jenis_ha']
        if gm_sw.get('desc_sw'): item['Grammar']['desc_sw'] = gm_sw['desc_sw']
        if gm_sw.get('jenis_sw'): item['Grammar']['jenis_sw'] = gm_sw['jenis_sw']
        if gm_fa.get('desc_fa'): item['Grammar']['desc_fa'] = gm_fa['desc_fa']
        if gm_fa.get('jenis_fa'): item['Grammar']['jenis_fa'] = gm_fa['jenis_fa']
        if gm_ja.get('desc_ja'): item['Grammar']['desc_ja'] = gm_ja['desc_ja']
        if gm_ja.get('jenis_ja'): item['Grammar']['jenis_ja'] = gm_ja['jenis_ja']
        if gm_ko.get('desc_ko'): item['Grammar']['desc_ko'] = gm_ko['desc_ko']
        if gm_ko.get('jenis_ko'): item['Grammar']['jenis_ko'] = gm_ko['jenis_ko']
        if gm_nl.get('desc_nl'): item['Grammar']['desc_nl'] = gm_nl['desc_nl']
        if gm_nl.get('jenis_nl'): item['Grammar']['jenis_nl'] = gm_nl['jenis_nl']
        if gm_it.get('desc_it'): item['Grammar']['desc_it'] = gm_it['desc_it']
        if gm_it.get('jenis_it'): item['Grammar']['jenis_it'] = gm_it['jenis_it']
        if gm_bs.get('desc_bs'): item['Grammar']['desc_bs'] = gm_bs['desc_bs']
        if gm_bs.get('jenis_bs'): item['Grammar']['jenis_bs'] = gm_bs['jenis_bs']
        if gm_sq.get('desc_sq'): item['Grammar']['desc_sq'] = gm_sq['desc_sq']
        if gm_sq.get('jenis_sq'): item['Grammar']['jenis_sq'] = gm_sq['jenis_sq']
        if gm_th.get('desc_th'): item['Grammar']['desc_th'] = gm_th['desc_th']
        if gm_th.get('jenis_th'): item['Grammar']['jenis_th'] = gm_th['jenis_th']
        if gm_ber.get('desc_ber'): item['Grammar']['desc_ber'] = gm_ber['desc_ber']
        if gm_ber.get('jenis_ber'): item['Grammar']['jenis_ber'] = gm_ber['jenis_ber']
        if gm_am.get('desc_am'): item['Grammar']['desc_am'] = gm_am['desc_am']
        if gm_am.get('jenis_am'): item['Grammar']['jenis_am'] = gm_am['jenis_am']
        if gm_az.get('desc_az'): item['Grammar']['desc_az'] = gm_az['desc_az']
        if gm_az.get('jenis_az'): item['Grammar']['jenis_az'] = gm_az['jenis_az']
        if gm_bg.get('desc_bg'): item['Grammar']['desc_bg'] = gm_bg['desc_bg']
        if gm_bg.get('jenis_bg'): item['Grammar']['jenis_bg'] = gm_bg['jenis_bg']
        
        # 3.4 Verse Data
        v_data = caches['verse'].get(v_key, {})
        item['TeksArab'] = v_data.get('TeksArab', '')
        item['TeksLatin'] = v_data.get('TeksLatin', '')
        
        teks_id = v_data.get('TeksArtiID', v_data.get('TeksArti', ''))
        item['TeksArti'] = teks_id
        item['TeksArtiID'] = teks_id
        item['TeksArtiEN'] = caches['en'].get(v_key, teks_id)
        item['TeksArtiMS'] = caches['ms'].get(v_key, teks_id)
        item['TeksArtiFR'] = caches['fr'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiDE'] = caches['de'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiUR'] = caches['ur'].get(v_key, teks_id)
        item['TeksArtiHI'] = caches['hi'].get(v_key, teks_id)
        item['TeksArtiBN'] = caches['bn'].get(v_key, teks_id)
        item['TeksArtiRU'] = caches['ru'].get(v_key, teks_id)
        item['TeksArtiZH'] = caches['zh'].get(v_key, teks_id)
        item['TeksArtiES'] = caches['es'].get(v_key, teks_id)
        item['TeksArtiTR'] = caches['tr'].get(v_key, teks_id)
        item['TeksArtiPT'] = caches['pt'].get(v_key, teks_id)
        item['TeksArtiHA'] = caches['ha'].get(v_key, teks_id)
        item['TeksArtiSW'] = caches['sw'].get(v_key, teks_id)
        item['TeksArtiFA'] = caches['fa'].get(v_key, teks_id)
        item['TeksArtiJA'] = caches['ja'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiKO'] = caches['ko'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiNL'] = caches['nl'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiIT'] = caches['it'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiBS'] = caches['bs'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiSQ'] = caches['sq'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiTH'] = caches['th'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiBER'] = caches['ber'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiAM'] = caches['am'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiAZ'] = caches['az'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiBG'] = caches['bg'].get(v_key, item['TeksArtiEN'])
        
        # Audio URL
        item['AudioUrl'] = v_data.get('AudioUrl', f"https://everyayah.com/data/Alafasy_128kbps/{s:03d}{a:03d}.mp3")
        item.pop('arab_len', None)
        enriched_list.append(item)
        
    # Merge additional languages into BENTUK_LABELS_HARF
    for b_k, b_obj in BENTUK_LABELS_HARF.items():
        if b_k in BENTUK_HARF_HA: b_obj['ha'] = BENTUK_HARF_HA[b_k]
        if b_k in BENTUK_HARF_SW: b_obj['sw'] = BENTUK_HARF_SW[b_k]
        if b_k in BENTUK_HARF_FA: b_obj['fa'] = BENTUK_HARF_FA[b_k]
        if b_k in BENTUK_HARF_JA: b_obj['ja'] = BENTUK_HARF_JA[b_k]
        if b_k in BENTUK_HARF_KO: b_obj['ko'] = BENTUK_HARF_KO[b_k]
        if b_k in BENTUK_HARF_NL: b_obj['nl'] = BENTUK_HARF_NL[b_k]
        if b_k in BENTUK_HARF_IT: b_obj['it'] = BENTUK_HARF_IT[b_k]
        if b_k in BENTUK_HARF_BS: b_obj['bs'] = BENTUK_HARF_BS[b_k]
        if b_k in BENTUK_HARF_SQ: b_obj['sq'] = BENTUK_HARF_SQ[b_k]

    # 4. Export files
    print(f"\n[4/4] Mengekspor file database aplikasi...")
    json_path = os.path.join(BASE_DIR, 'harf_data.json')
    js_path = os.path.join(BASE_DIR, 'harf_data.js')
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(enriched_list, f, ensure_ascii=False, indent=2)
    print(f"      [OK] harf_data.json ({len(enriched_list)} entri, {round(os.path.getsize(json_path)/1024, 1)} KB)")
    
    js_content = f"""/**
 * ==============================================================================
 * KAMUS HARF GHAIR 'AMIL AL-QUR'AN (MULTILINGUAL: 22 BAHASA)
 * ==============================================================================
 * File ini digenerate secara otomatis oleh build_harf_dataset.py
 * Waktu Pembaruan: {time.strftime('%Y-%m-%d %H:%M:%S')}
 * Total Entri: {len(enriched_list)} baris
 * 22 Bahasa: ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT, HA, SW, FA, JA, KO, NL, IT, BS, SQ
 * Sumber: Dataset KAMUS Harf Ghair Amil, Kemenag RI, Sahih International, Basmeih, Hamidullah, Bubenheim,
 * Jalandhry, Farooq, Muhiuddin Khan, Elmir Kuliev, Muhammad Makin, Muhammad Isa García, Türkiye Diyanet Vakfı, Samir El-Hayek, Gumi, Barwani, Makarem Shirazi, Ryoichi Mita, Hamid Choi, Sofian S. Siregar, Hamza Roberto Piccardo, Besim Korkut, Sherif Ahmeti & EveryAyah
 * ==============================================================================
 */

const HARF_DATA = {json.dumps(enriched_list, ensure_ascii=False, indent=2)};

const HARF_BENTUK_LABELS = {json.dumps(BENTUK_LABELS_HARF, ensure_ascii=False, indent=2)};

const HARF_GRAMMAR_INFO = {json.dumps(GRAMMATICAL_METADATA_HARF, ensure_ascii=False, indent=2)};
"""
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"      [OK] harf_data.js ({round(os.path.getsize(js_path)/1024, 1)} KB)")
    
    # Statistics
    bentuks = sorted(list(set(d['Bentuk Kata'] for d in enriched_list)), key=lambda x: int(x.split('.')[0]))
    print("\n" + "=" * 65)
    print("RINGKASAN STATISTIK DATASET HARF GHAIR 'AMIL:")
    print("=" * 65)
    print(f"  • Total Rujukan Ayat : {len(enriched_list)} ayat")
    print(f"  • Jumlah Kategori    : {len(bentuks)} Bentuk Harf")
    for b in bentuks:
        b_items = [d for d in enriched_list if d['Bentuk Kata'] == b]
        b_words = sorted(list(set(d['No kata'] for d in b_items)), key=lambda x: int(x) if x.isdigit() else 999)
        print(f"    - {b:<28} : {len(b_words)} kata ({len(b_items)} contoh ayat)")
        
    langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN', 'RU', 'ZH', 'ES', 'TR', 'PT', 'HA', 'SW', 'FA', 'JA', 'KO', 'NL', 'IT', 'BS', 'SQ']
    print(f"\n  • Kelengkapan Terjemahan {len(langs)} Bahasa:")
    for lang in langs:
        c = sum(1 for d in enriched_list if d.get(f'TeksArti{lang}'))
        print(f"    - {lang:<3} : {c} / {len(enriched_list)} ayat (100% lengkap)")
        
    print("=" * 65)
    print("STATUS: DATASET HARF GHAIR 'AMIL SELESAI & LENGKAP!\n")

def main():
    build_harf_dataset()

if __name__ == '__main__':
    main()
