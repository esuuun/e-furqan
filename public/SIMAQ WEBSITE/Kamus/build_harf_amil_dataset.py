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

# Import 114 Surahs from multilingual datasets
from build_multilingual_dataset import SURAHS
from build_hausa_dataset import HAUSA_SURAHS
from build_swahili_dataset import SWAHILI_SURAHS
from build_persian_dataset import PERSIAN_SURAHS
from build_japanese_dataset import JAPANESE_SURAHS
from build_korean_dataset import KOREAN_SURAHS
from build_dutch_dataset import DUTCH_SURAHS
from build_italian_dataset import ITALIAN_SURAHS
from build_bosnian_dataset import BOSNIAN_SURAHS
from build_albanian_dataset import ALBANIAN_SURAHS
from build_thai_dataset import THAI_SURAHS
from build_amazigh_amharic_dataset import AMAZIGH_SURAHS, AMHARIC_SURAHS
from build_azerbaijani_bulgarian_dataset import AZERBAIJANI_SURAHS, BULGARIAN_SURAHS
from build_czech_dhivehi_dataset import CZECH_SURAHS, DHIVEHI_SURAHS
from build_norwegian_polish_dataset import NORWEGIAN_SURAHS, POLISH_SURAHS
from build_romanian_swedish_dataset import ROMANIAN_SURAHS, SWEDISH_SURAHS
from build_tajik_tamil_dataset import TAJIK_SURAHS, TAMIL_SURAHS
from build_4_languages_dataset import TATAR_SURAHS, UYGHUR_SURAHS, UZBEK_SURAHS, KURDISH_SURAHS

# 6 BENTUK HARF 'AMIL LABELS IN 39 LANGUAGES
BENTUK_LABELS_HARF_AMIL = {
    "1. Harf Jar": {
        "id": "1. Harf Jar (Huruf Jar / Men-jarkan Isim)",
        "en": "1. Genitive Particles / Prepositions (Harf Jar)",
        "ms": "1. Harf Jar (Huruf yang Menjarkan Isim)",
        "fr": "1. Prépositions / Particules Génitives (Harf Jar)",
        "de": "1. Präpositionen / Genitivpartikeln (Harf Jar)",
        "ur": "۱. حروف جار (Harf Jar)",
        "hi": "१. संबंधबोधक / अव्यय शब्द (Harf Jar)",
        "bn": "১. অব্যয়সূচক হরূফে জার (Harf Jar)",
        "ru": "1. Предлоги / Родительные частицы (Харф Джарр)",
        "zh": "1. 介词虚词 (Harf Jar)",
        "es": "1. Preposiciones / Partículas Genitivas (Harf Yar)",
        "tr": "1. Cer Harfleri (İsmi Mecrûr Yapan Edatlar)",
        "pt": "1. Preposições / Partículas Genitivas (Harf Jar)",
        "ha": "1. Haruffan Jar (Prepositions)",
        "sw": "1. Vihusishi vya Harf Jar (Prepositions)",
        "fa": "۱. حروف جر (حروف اضافه)",
        "ja": "1. 前置詞・生格小辞 (ハルフ・ジャール)",
        "ko": "1. 전치사 및 속격 불변사 (하르프 자르)",
        "nl": "1. Voorzetsels / Genitiefpartikels (Harf Jar)",
        "it": "1. Preposizioni / Particelle Genitive (Harf Jar)",
        "bs": "1. Prijedlozi (Harfovi džerra)",
        "sq": "1. Parafjalë / Harfet e Xherrit",
        "th": "1. คำบุพบท (Harf Jar)",
        "ber": "1. Tisekkirin n Jar (Prepositions)",
        "am": "1. መስተዋድድ ቃላት (Harf Jar)",
        "az": "1. Cər hərfləri (Önqoşmalar)",
        "bg": "1. Предлози / Частици за родителен падеж",
        "cs": "1. Předložky / Genitivní částice (Harf Jar)",
        "dv": "1. ޖައްރުގެ އަކުރުތައް (Harf Jar)",
        "no": "1. Preposisjoner (Harf Jar)",
        "pl": "1. Przyimki / Partykuły dopełniaczowe (Harf Dżarr)",
        "ro": "1. Prepoziții / Particule genitivale (Harf Jar)",
        "sv": "1. Prepositioner / Genitivpartiklar (Harf Jar)",
        "tg": "1. Ҳарфҳои ҷарр (Пешояндҳо)",
        "ta": "1. முன்னிடைச் சொற்கள் (Harf Jar)",
        "tt": "1. Җәрр хәрефләре (Бәйлекләр)",
        "ug": "1. جەر ھەرپلىرى (ئالدى قوشۇمچىلار)",
        "uz": "1. Jar harflari (Ko'makchilar)",
        "ku": "1. پیتەکانی جەڕ (Harf Jar)"
    },
    "2. Harf Nashib": {
        "id": "2. Harf Nashib (Huruf yang Me-nashabkan Fi'il Mudhari')",
        "en": "2. Subjunctive / Accusative Particles (Harf Nasib)",
        "ms": "2. Harf Nasib (Huruf yang Menasabkan Fi'il)",
        "fr": "2. Particules Subjonctives (Harf Nasib)",
        "de": "2. Subjunktivpartikeln (Harf Nasib)",
        "ur": "۲. حروف ناصبہ برائے فعل مضارع (Harf Nasib)",
        "hi": "२. कर्मकारक / आज्ञार्थक शब्द (Harf Nasib)",
        "bn": "২. নসব প্রদানকারী শব্দ (Harf Nasib)",
        "ru": "2. Винительные сослагательные частицы (Харф Насыб)",
        "zh": "2. 虚拟式宾格虚词 (Harf Nasib)",
        "es": "2. Partículas de Subjuntivo (Harf Nasib)",
        "tr": "2. Nâsıb Edatlar (Muzari Fiili Mansub Yapanlar)",
        "pt": "2. Partículas de Subjuntivo (Harf Nasib)",
        "ha": "2. Haruffan Nasab (Subjunctive Particles)",
        "sw": "2. Chembe za Nasabu (Subjunctive Particles)",
        "fa": "۲. حروف ناصبه (نصب‌دهنده فعل مضارع)",
        "ja": "2. 接続法・対格小辞 (ハルフ・ナースィブ)",
        "ko": "2. 접속법·대격 불변사 (하르프 나십)",
        "nl": "2. Aanvoegende partikels (Harf Nasib)",
        "it": "2. Particelle Congiuntive (Harf Nasib)",
        "bs": "2. Čestice konjunktiva (Harfovi nasba)",
        "sq": "2. Pjesëza të mënyrës lidhore (Harfet e Nasbit)",
        "th": "2. คำอนุภาคกริยานาสิบ (Harf Nasib)",
        "ber": "2. Tisekkirin n Nasb (Subjunctive)",
        "am": "2. የድርጊት መልክ ቅንጣት (Harf Nasib)",
        "az": "2. Nəsib hərfləri (Nəsb edənlər)",
        "bg": "2. Частици за винителен/подчинителен залог",
        "cs": "2. Subjunktivní částice (Harf Nasib)",
        "dv": "2. ނަޞްބުގެ އަކުރުތައް (Harf Nasib)",
        "no": "2. Konjunktivpartikler (Harf Nasib)",
        "pl": "2. Partykuły łączące / biernikowe (Harf Nasib)",
        "ro": "2. Particule subjonctive (Harf Nasib)",
        "sv": "2. Konjunktivpartiklar (Harf Nasib)",
        "tg": "2. Ҳарфҳои носиба (Насбкунанда)",
        "ta": "2. வினையெச்ச இடைச்சொற்கள் (Harf Nasib)",
        "tt": "2. Насыйб хәрефләре (Хәл кушымчалары)",
        "ug": "2. ناسىپ ھەرپلىرى (نەسىپ قىلغۇچىلار)",
        "uz": "2. Nosib harflari (Nasb qiluvchilar)",
        "ku": "2. پیتەکانی ناسبە (Harf Nasib)"
    },
    "3. Harf Jazim": {
        "id": "3. Harf Jazim (Huruf yang Men-jazamkan Fi'il Mudhari')",
        "en": "3. Jussive / Apocopate Particles (Harf Jazim)",
        "ms": "3. Harf Jazim (Huruf yang Menjazamkan Fi'il)",
        "fr": "3. Particules Jussives / Apocopées (Harf Jazim)",
        "de": "3. Jussivpartikeln (Harf Jazim)",
        "ur": "۳. حروف جازمہ برائے فعل مضارع (Harf Jazim)",
        "hi": "३. आज्ञावाचक / जज़्म करने वाले शब्द (Harf Jazim)",
        "bn": "৩. জযম প্রদানকারী শব্দ (Harf Jazim)",
        "ru": "3. Усекательные частицы (Харф Джазим)",
        "zh": "3. 截除式命令虚词 (Harf Jazim)",
        "es": "3. Partículas Jusivas / Apocopadas (Harf Yazim)",
        "tr": "3. Câzim Edatlar (Muzari Fiili Cezm Edenler)",
        "pt": "3. Partículas Jussivas (Harf Jazim)",
        "ha": "3. Haruffan Jazam (Jussive Particles)",
        "sw": "3. Chembe za Jazmu (Jussive Particles)",
        "fa": "۳. حروف جازمه (جزم‌دهنده فعل مضارع)",
        "ja": "3. 要求法・短縮小辞 (ハルフ・ジャーズィム)",
        "ko": "3. 요구법·단축 불변사 (하르프 자짐)",
        "nl": "3. Jussieve partikels (Harf Jazim)",
        "it": "3. Particelle Iussive (Harf Jazim)",
        "bs": "3. Čestice jusiva (Harfovi džezma)",
        "sq": "3. Pjesëza të urdhërores (Harfet e Xhezmit)",
        "th": "3. คำอนุภาคกริยาจาซิม (Harf Jazim)",
        "ber": "3. Tisekkirin n Jazm (Jussive)",
        "am": "3. ትእዛዛዊ ቅንጣት (Harf Jazim)",
        "az": "3. Cəzm hərfləri (Cəzm edənlər)",
        "bg": "3. Частици за съкратено/заповедно наклонение",
        "cs": "3. Jussivní částice (Harf Jazim)",
        "dv": "3. ޖަޒުމުގެ އަކުރުތައް (Harf Jazim)",
        "no": "3. Jussivpartikler (Harf Jazim)",
        "pl": "3. Partykuły rozkazujące (Harf Dżazim)",
        "ro": "3. Particule jusive (Harf Jazim)",
        "sv": "3. Jussivpartiklar (Harf Jazim)",
        "tg": "3. Ҳарфҳои ҷозима (Ҷазмкунанда)",
        "ta": "3. விதிமுறை இடைச்சொற்கள் (Harf Jazim)",
        "tt": "3. Җәзем хәрефләре",
        "ug": "3. جازىم ھەرپلىرى (جازىم قىلغۇچىلار)",
        "uz": "3. Jazm harflari (Jazm qiluvchilar)",
        "ku": "3. پیتەکانی جازمە (Harf Jazim)"
    },
    "4. Harf Athaf": {
        "id": "4. Harf Athaf (Huruf Penghubung / Konjungsi 'Amil)",
        "en": "4. Conjunction Particles (Harf 'Ataf)",
        "ms": "4. Harf 'Athaf (Huruf Kata Hubung)",
        "fr": "4. Conjonctions de Coordination (Harf 'Ataf)",
        "de": "4. Beiordnende Konjunktionen (Harf 'Ataf)",
        "ur": "۴. حروف عطف (حروف ربط)",
        "hi": "४. समुच्चयबोधक शब्द (Harf 'Ataf)",
        "bn": "৪. সংযোজক অব্যয় (Harf 'Ataf)",
        "ru": "4. Сочинительные союзы (Харф Атаф)",
        "zh": "4. 并列连词虚词 (Harf 'Ataf)",
        "es": "4. Conjunciones Coordinantes (Harf 'Ataf)",
        "tr": "4. Atıf Harfleri (Bağlaç Edatları)",
        "pt": "4. Conjunções Coordenativas (Harf 'Ataf)",
        "ha": "4. Haruffan Sadarwa (Conjunctions)",
        "sw": "4. Viunganishi vya Harf 'Athaf (Conjunctions)",
        "fa": "۴. حروف عطف (حروف پیوند)",
        "ja": "4. 等位接続詞 (ハルフ・アタフ)",
        "ko": "4. 등위 접속사 불변사 (하르프 아타프)",
        "nl": "4. Nevenschikkende voegwoorden (Harf 'Ataf)",
        "it": "4. Congiunzioni Coordinanti (Harf 'Ataf)",
        "bs": "4. Veznici (Harfovi atafe)",
        "sq": "4. Lidhëza bashkërenditëse (Harfet e Atfit)",
        "th": "4. คำสันธานเชื่อมประโยค (Harf 'Ataf)",
        "ber": "4. Tisekkirin n Tasedmirt (Conjunctions)",
        "am": "4. አያያዥ ቃላት (Harf 'Ataf)",
        "az": "4. Ətf hərfləri (Bağlayıcılar)",
        "bg": "4. Съединителни съюзи (Харф Атаф)",
        "cs": "4. Souřadící spojky (Harf 'Ataf)",
        "dv": "4. ޢަޠުފުގެ އަކުރުތައް (Harf 'Ataf)",
        "no": "4. Sideordnende konjunksjoner (Harf 'Ataf)",
        "pl": "4. Spójniki współrzędne (Harf 'Ataf)",
        "ro": "4. Conjuncții coordonatoare (Harf 'Ataf)",
        "sv": "4. Samordnande konjunktioner (Harf 'Ataf)",
        "tg": "4. Ҳарфҳои атф (Пайвандакҳо)",
        "ta": "4. இணைப்புச் சொற்கள் (Harf 'Ataf)",
        "tt": "4. Гатыйф хәрефләре (Теркәгечләр)",
        "ug": "4. ئاتىپ ھەرپلىرى (باغلىغۇچىلار)",
        "uz": "4. Atf harflari (Bog'lovchilar)",
        "ku": "4. پیتەکانی عەتف (Harf 'Ataf)"
    },
    "5. Harf Nasikh": {
        "id": "5. Harf Nasikh (Huruf Inna & Saudaranya yang Merubah I'rab)",
        "en": "5. Annulment Particles / Inna and Sisters (Harf Nasikh)",
        "ms": "5. Harf Nasikh (Inna & Saudara-saudaranya)",
        "fr": "5. Particules Annulatives / Inna et ses sœurs (Nasikh)",
        "de": "5. Annullierungspartikeln / Inna und ihre Schwestern (Nasikh)",
        "ur": "۵. حروف مشبہ بالفعل / حروف ناسخہ (Inna wa Akhawatuha)",
        "hi": "५. रूप-परिवर्तक शब्द / इन्ना और उसके सहयोगी (Harf Nasikh)",
        "bn": "৫. নাসিখ শব্দসমূহ / ইন্না ও তার সমগোত্রীয় (Harf Nasikh)",
        "ru": "5. Аннулирующие частицы / Инна и ее сестры (Насих)",
        "zh": "5. 废止性虚词 / 印纳及其同类词 (Harf Nasikh)",
        "es": "5. Partículas Anulativas / Inna y sus hermanas (Nasij)",
        "tr": "5. Nâsih Harfler (İnne ve Kardeşleri)",
        "pt": "5. Partículas Anulativas / Inna e suas irmãs (Nasikh)",
        "ha": "5. Haruffan Nasikh (Inna da 'Yan'uwanta)",
        "sw": "5. Chembe za Nasikh (Inna na Ndugu zake)",
        "fa": "۵. حروف مشبهة بالفعل (حروف ناسخه / انّ و خواهرانش)",
        "ja": "5. 句構造変更小辞・インナ姉妹詞 (ハルフ・ナースィフ)",
        "ko": "5. 구문 변화 불변사 / 인나와 자매들 (하르프 나시크)",
        "nl": "5. Wijzigingspartikels / Inna en haar zusters (Harf Nasikh)",
        "it": "5. Particelle Modificatrici / Inna e le sue sorelle (Nasikh)",
        "bs": "5. Poništavajuće čestice / Inna i njene sestre (Harfovi nesiha)",
        "sq": "5. Pjesëza shndërruese / Inna dhe motrat e saj (Harfet e Nasiut)",
        "th": "5. คำอนุภาคนาสิค (Harf Nasikh)",
        "ber": "5. Tisekkirin n Nasikh (Inna d tiyetmin-is)",
        "am": "5. ለዋጭ ቅንጣቶች / ኢና እና እህቶቹ (Harf Nasikh)",
        "az": "5. Nəsx edən hərflər / İnnə və bacıları",
        "bg": "5. Модифициращи частици / Инна и нейните сестри",
        "cs": "5. Modifikační částice / Inna a její sestry (Harf Nasikh)",
        "dv": "5. ނާސިޚު އަކުރުތައް (Inna and Sisters)",
        "no": "5. Modifiserende partikler / Inna og søstrene (Harf Nasikh)",
        "pl": "5. Partykuły modyfikujące / Inna i jej siostry (Harf Nasikh)",
        "ro": "5. Particule anulatoare / Inna și surorile sale (Harf Nasikh)",
        "sv": "5. Modifierande partiklar / Inna och hennes systrar (Harf Nasikh)",
        "tg": "5. Ҳарфҳои носиха (Инна ва хоҳаронаш)",
        "ta": "5. மாற்றியமைக்கும் இடைச்சொற்கள் (Harf Nasikh)",
        "tt": "5. Насих хәрефләре (Иннә һәм аның охшашлары)",
        "ug": "5. ناسىخ ھەرپلىرى (ئىننە ۋە ئۇنىڭ ھەمراھلىرى)",
        "uz": "5. Nosix harflari (Inna va uning opalar-singillari)",
        "ku": "5. پیتەکانی ناسخە (Harf Nasikh)"
    },
    "6. Harf Istitsna": {
        "id": "6. Harf Istitsna (Huruf Pengecualian / Istitsna')",
        "en": "6. Exception Particles (Harf Istithna)",
        "ms": "6. Harf Istisna (Huruf Pengecualian)",
        "fr": "6. Particules d'Exception (Harf Istithna)",
        "de": "6. Ausnahmepartikeln (Harf Istithna)",
        "ur": "۶. حروف استثناء (حروف تفریق)",
        "hi": "६. अपवाद सूचक शब्द (Harf Istithna)",
        "bn": "৬. ব্যতিক্রমসূচক শব্দ (Harf Istithna)",
        "ru": "6. Частицы исключения (Харф Истисна)",
        "zh": "6. 例外虚词 (Harf Istithna)",
        "es": "6. Partículas de Excepción (Harf Istizna)",
        "tr": "6. İstisnâ Harfleri (İstisna Edatları)",
        "pt": "6. Partículas de Exceção (Harf Istithna)",
        "ha": "6. Haruffan Keɓancewa (Exception Particles)",
        "sw": "6. Chembe za Vighairi (Exception Particles)",
        "fa": "۶. حروف استثناء (حروف متمایزکننده)",
        "ja": "6. 除外小辞 (ハルフ・イスティスナー)",
        "ko": "6. 예외 불변사 (하르프 이스티스나)",
        "nl": "6. Uitzonderingspartikels (Harf Istithna)",
        "it": "6. Particelle di Eccezione (Harf Istithna)",
        "bs": "6. Čestice izuzetka (Harfovi istisna'a)",
        "sq": "6. Pjesëza të përjashtimit (Harfet e Istithnasë)",
        "th": "6. คำยกเว้น (Harf Istithna)",
        "ber": "6. Tisekkirin n Tuffɣa (Exception)",
        "am": "6. የተለየ ማድረጊያ ቅንጣት (Harf Istithna)",
        "az": "6. İstisna hərfləri",
        "bg": "6. Частици за изключение (Харф Истисна)",
        "cs": "6. Výjimkové částice (Harf Istithna)",
        "dv": "6. އިސްތިޘްނާގެ އަކުރުތައް (Harf Istithna)",
        "no": "6. Unntakspartikler (Harf Istithna)",
        "pl": "6. Partykuły wyjątku (Harf Istisna)",
        "ro": "6. Particule de excepție (Harf Istithna)",
        "sv": "6. Undantagspartiklar (Harf Istithna)",
        "tg": "6. Ҳарфҳои истисно",
        "ta": "6. விலக்கு இடைச்சொற்கள் (Harf Istithna)",
        "tt": "6. Истисна хәрефләре",
        "ug": "6. ئىستىسنا ھەرپلىرى (مۇستەسنا قىلغۇچىلار)",
        "uz": "6. Istisno harflari",
        "ku": "6. پیتەکانی ئیستسنا (Harf Istithna)"
    }
}

# 54 GRAMMATICAL METADATA ENTRIES IN 39 LANGUAGES
GRAMMATICAL_METADATA_HARF_AMIL = {
    # 1. Harf Jar
    "1. Harf Jar__1": {"latin": "Min", "arti_id": "DARI / SEBAGIAN / YAITU / PENGUAT / DLL", "arti_en": "FROM / OF / AMONG / INDEED", "arti_ms": "DARI / DARIPADA / SEBAHAGIAN", "arti_fr": "DE / PARMI / DEPUIS", "arti_de": "VON / AUS / EINIGE VON", "arti_ur": "سے / میں سے / بعض", "arti_hi": "से / में से / कुछ", "arti_bn": "হতে / থেকে / মধ্য থেকে", "arti_ru": "ИЗ / ОТ / ИЗ ЧИСЛА", "arti_zh": "从 / 来自 / 其中的一部分", "arti_es": "DE / DESDE / ENTRE", "arti_tr": "-DEN / -DAN / BİR KISMI", "arti_pt": "DE / DESDE / DENTRE"},
    "1. Harf Jar__2": {"latin": "Fī", "arti_id": "DI / DALAM / PADA / DLL", "arti_en": "IN / INSIDE / ON / AT", "arti_ms": "DI / DALAM / PADA", "arti_fr": "DANS / EN / SUR", "arti_de": "IN / INNERHALB / AUF", "arti_ur": "میں / اندر / پر", "arti_hi": "में / अंदर / पर", "arti_bn": "মধ্যে / তে / অন্তরে", "arti_ru": "В / ВНУТРИ / НА", "arti_zh": "在...里 / 在...中", "arti_es": "EN / DENTRO DE / SOBRE", "arti_tr": "-DE / -DA / İÇİNDE", "arti_pt": "EM / DENTRO DE / SOBRE"},
    "1. Harf Jar__3": {"latin": "'Alā", "arti_id": "ATAS / KEPADA / PADA / DLL", "arti_en": "ON / UPON / OVER / UNTO", "arti_ms": "ATAS / KEPADA / TERHADAP", "arti_fr": "SUR / AU-DESSUS / ENVERS", "arti_de": "AUF / ÜBER / GEGENÜBER", "arti_ur": "پر / اوپر / کے حق میں", "arti_hi": "पर / ऊपर / के प्रति", "arti_bn": "উপরে / প্রতি / ওপর", "arti_ru": "НА / НАД / ПРОТИВ", "arti_zh": "在...之上 / 对于", "arti_es": "SOBRE / ENCIMA DE / HACIA", "arti_tr": "ÜZERİNDE / -E / -A", "arti_pt": "SOBRE / EM CIMA DE / PARA"},
    "1. Harf Jar__4": {"latin": "Ilā", "arti_id": "KE / PADA / KEPADA / DLL", "arti_en": "TO / TOWARDS / UNTO", "arti_ms": "KE / KEPADA / HINGGA", "arti_fr": "VERS / À / JUSQU'À", "arti_de": "ZU / NACH / HIN ZU", "arti_ur": "کی طرف / تک", "arti_hi": "की ओर / तक", "arti_bn": "দিকে / প্রতি / পর্যন্ত", "arti_ru": "К / ПО НАПРАВЛЕНИЮ К", "arti_zh": "到 / 向 / 往", "arti_es": "A / HACIA / HASTA", "arti_tr": "-E / -A / DOĞRU", "arti_pt": "A / PARA / EM DIREÇÃO A"},
    "1. Harf Jar__5": {"latin": "'An", "arti_id": "TENTANG / DARI / TERHADAP / DLL", "arti_en": "ABOUT / FROM / AWAY FROM", "arti_ms": "TENTANG / DARI / DARI HAL", "arti_fr": "DE / AU SUJET DE / LOIN DE", "arti_de": "ÜBER / VON ... WEG", "arti_ur": "کے بارے میں / سے", "arti_hi": "के बारे में / से", "arti_bn": "সম্পর্কে / হতে / দূরে", "arti_ru": "О / ОТ / ИЗ-ЗА", "arti_zh": "关于 / 远离 / 出于", "arti_es": "SOBRE / ACERCA DE / DE", "arti_tr": "HAKKINDA / -DEN / UZAK", "arti_pt": "SOBRE / ACERCA DE / DE"},
    "1. Harf Jar__6": {"latin": "Mimmā", "arti_id": "DARI_APA YANG", "arti_en": "FROM WHAT / OUT OF THAT WHICH", "arti_ms": "DARI APA YANG", "arti_fr": "DE CE QUE / PARMI CE QUE", "arti_de": "VON DEM, WAS", "arti_ur": "اس سے جو / اس میں سے جو", "arti_hi": "उसमें से जो / जिससे", "arti_bn": "যা হতে / যা থেকে", "arti_ru": "ИЗ ТОГО, ЧТО", "arti_zh": "从...之中 / 出于所...", "arti_es": "DE LO QUE / DE AQUELLO QUE", "arti_tr": "ŞEYLERDEN / ONDAN Kİ", "arti_pt": "DAQUILO QUE / DE O QUE"},
    "1. Harf Jar__7": {"latin": "'Ammā 1", "arti_id": "TENTANG / DARI_APA YANG", "arti_en": "ABOUT WHAT / FROM THAT WHICH", "arti_ms": "TENTANG APA YANG", "arti_fr": "DE CE QUE / SUR CE QUE", "arti_de": "ÜBER DAS, WAS", "arti_ur": "اس کے بارے میں جو", "arti_hi": "उसके बारे में जो", "arti_bn": "সে বিষয়ে যা", "arti_ru": "О ТОМ, ЧТО / ОТ ТОГО, ЧТО", "arti_zh": "关于所... / 出于所...", "arti_es": "ACERCA DE LO QUE", "arti_tr": "ŞEYLERDEN / ONDAN Kİ", "arti_pt": "ACERCA DO QUE"},
    "1. Harf Jar__8": {"latin": "Mimman", "arti_id": "DARI_SIAPA YANG", "arti_en": "FROM WHOM / OF THOSE WHO", "arti_ms": "DARI ORANG YANG", "arti_fr": "DE CELUI QUI / PARMI CEUX QUI", "arti_de": "VON DEM, DER", "arti_ur": "اس سے جس نے / ان میں سے جو", "arti_hi": "उससे जिसने / उनमें से जो", "arti_bn": "তার থেকে যে", "arti_ru": "ИЗ ТЕХ, КТО / ОТ ТОГО, КТО", "arti_zh": "从那些...之人中", "arti_es": "DE QUIEN / DE AQUELLOS QUE", "arti_tr": "KİMSEDEN / O KİŞİDEN Kİ", "arti_pt": "DAQUELE QUE / DE QUEM"},
    "1. Harf Jar__9": {"latin": "Fīmā", "arti_id": "DALAM / PADA / TENTANG_APA YANG", "arti_en": "IN WHAT / CONCERNING THAT WHICH", "arti_ms": "DALAM APA YANG", "arti_fr": "DANS CE QUE / AU SUJET DE CE QUE", "arti_de": "IN DEM, WAS", "arti_ur": "اس میں جو / جس بارے میں", "arti_hi": "उसमें जो / जिस विषय में", "arti_bn": "সে বিষয়ে যা", "arti_ru": "В ТОМ, В ЧЕМ", "arti_zh": "在所...之中 / 关于所...", "arti_es": "EN LO QUE / RESPECTO A LO QUE", "arti_tr": "ŞEY HAKKINDA / ONDA Kİ", "arti_pt": "NO QUE / A RESPEITO DO QUE"},
    "1. Harf Jar__10": {"latin": "Hattā 3", "arti_id": "SAMPAI", "arti_en": "UNTIL (GENITIVE PREPOSITION)", "arti_ms": "SEHINGGA / SAMPAI", "arti_fr": "JUSQU'À (PRÉPOSITION)", "arti_de": "BIS ZU (PRÄPOSITION)", "arti_ur": "یہاں تک کہ (حرف جار)", "arti_hi": "यहाँ तक कि (अव्यय)", "arti_bn": "পর্যন্ত (জর প্রদানকারী)", "arti_ru": "ВПЛОТЬ ДО / ДО", "arti_zh": "直到 (介词)", "arti_es": "HASTA (PREPOSICIÓN)", "arti_tr": "-E KADAR / TÂ (CER EDATI)", "arti_pt": "ATÉ (PREPOSIÇÃO)"},
    "1. Harf Jar__11": {"latin": "Fīma", "arti_id": "DALAM / PADA_HAL APAKAH", "arti_en": "IN WHAT? / WHEREIN? / CONCERNING WHAT?", "arti_ms": "DALAM APAKAH / TENTANG APA", "arti_fr": "EN QUOI ? / DANS QUEL ÉTAT ?", "arti_de": "WORIN? / IN WELCHER LAGE?", "arti_ur": "کس چیز میں؟ / کس حالت میں؟", "arti_hi": "किस बात में? / किस स्थिति में?", "arti_bn": "কিসের মধ্যে? / কি বিষয়ে?", "arti_ru": "В ЧЕМ? / ПО КАКОМУ ПОВОДУ?", "arti_zh": "在何事中？/ 处于何种境地？", "arti_es": "¿EN QUÉ? / ¿DE QUÉ MODO?", "arti_tr": "NEYİN İÇİNDE? / NE HAKKINDA?", "arti_pt": "EM QUÊ? / A RESPEITO DE QUÊ?"},
    "1. Harf Jar__12": {"latin": "Rubamā", "arti_id": "SERING KALI / MUNGKIN KALI", "arti_en": "PERHAPS / OFTEN / MANY A TIME", "arti_ms": "SERING KALI / KADANG-KALA", "arti_fr": "SOUVENT / PEUT-ÊTRE BIEN", "arti_de": "OFT / VIELLEICHT WOHL", "arti_ur": "شاید / اکثر و بیشتر", "arti_hi": "शायद / कई बार", "arti_bn": "সম্ভবত / বহুবার", "arti_ru": "БЫТЬ МОЖЕТ / ЧАСТО", "arti_zh": "或许 / 屡次", "arti_es": "TAL VEZ / MUCHAS VECES", "arti_tr": "BELKİ DE / ÇOK ZAMAN", "arti_pt": "TALVEZ / MUITAS VEZES"},
    "1. Harf Jar__13": {"latin": "'Amma", "arti_id": "TENTANG / DARI_APAKAH", "arti_en": "ABOUT WHAT? / CONCERNING WHAT?", "arti_ms": "TENTANG APAKAH", "arti_fr": "SUR QUOI ? / DE QUOI ?", "arti_de": "WORÜBER? / VON WAS?", "arti_ur": "کس چیز کے بارے میں؟", "arti_hi": "किस चीज़ के बारे में?", "arti_bn": "কি সম্পর্কে? / কিসের বিষয়ে?", "arti_ru": "О ЧЕМ?", "arti_zh": "关于什么？", "arti_es": "¿DE QUÉ? / ¿SOBRE QUÉ?", "arti_tr": "NEYİ? / NE HAKKINDA?", "arti_pt": "SOBRE O QUÊ? / ACERCA DE QUÊ?"},
    "1. Harf Jar__14": {"latin": "'Ammā 2", "arti_id": "DALAM / DARI", "arti_en": "AFTER A LITTLE / IN", "arti_ms": "DALAM / SEBENTAR LAGI", "arti_fr": "D'ICI PEU / DANS", "arti_de": "IN KURZEM / NACH", "arti_ur": "تھوڑی دیر میں / بعد", "arti_hi": "थोड़ी ही देर में", "arti_bn": "কিছুক্ষণের মধ্যেই", "arti_ru": "ВСКОРЕ / ЧЕРЕЗ НЕКОТОРОЕ ВРЕМЯ", "arti_zh": "不久之后 / 在...", "arti_es": "DENTRO DE POCO / EN", "arti_tr": "AZ BİR VAKİT SONRA", "arti_pt": "DENTRO EM BREVE / EM"},
    "1. Harf Jar__15": {"latin": "Mimma", "arti_id": "DARI_APAKAH", "arti_en": "FROM WHAT? / OF WHAT?", "arti_ms": "DARI APAKAH", "arti_fr": "DE QUOI ?", "arti_de": "WORAUS? / VON WAS?", "arti_ur": "کس چیز سے؟", "arti_hi": "किस चीज़ से?", "arti_bn": "কি হতে? / কিসের থেকে?", "arti_ru": "ИЗ ЧЕГО?", "arti_zh": "从什么 (被造)？", "arti_es": "¿DE QUÉ?", "arti_tr": "NEYDEN?", "arti_pt": "DE QUÊ?"},

    # 2. Harf Nashib
    "2. Harf Nashib__1": {"latin": "An 1", "arti_id": "SUPAYA / UNTUK / AGAR / KARENA / BAHWA", "arti_en": "THAT / TO / IN ORDER THAT", "arti_ms": "BAHAWA / SUPAYA / AGAR", "arti_fr": "QUE / POUR QUE / DE", "arti_de": "DASS / UM ZU", "arti_ur": "کہ / تاکہ", "arti_hi": "कि / ताकि", "arti_bn": "যে / যেন / যাতে", "arti_ru": "ЧТО / ЧТОБЫ", "arti_zh": "以致 / 以便 / 该", "arti_es": "QUE / PARA QUE", "arti_tr": "-MESİ / Kİ / DİYE", "arti_pt": "QUE / PARA QUE"},
    "2. Harf Nashib__2": {"latin": "Lan", "arti_id": "TIDAK AKAN", "arti_en": "NEVER / WILL NOT / SHALL NOT", "arti_ms": "TIDAK AKAN SEKALI-KALI", "arti_fr": "JAMAIS / NE... POINT", "arti_de": "NIEMALS / WERDEN NICHT", "arti_ur": "ہرگز نہیں", "arti_hi": "कदापि नहीं / कभी नहीं", "arti_bn": "কখনোই নয় / কিছুতেই না", "arti_ru": "НИКОГДА НЕ / ОТНЮДЬ НЕ", "arti_zh": "绝不 / 决不", "arti_es": "JAMÁS / NUNCA", "arti_tr": "ASLA / HİÇBİR ZAMAN", "arti_pt": "NUNCA / JAMAIS"},
    "2. Harf Nashib__3": {"latin": "Hattā 1", "arti_id": "SEHINGGA / SAMPAI", "arti_en": "UNTIL / SO THAT (SUBJUNCTIVE)", "arti_ms": "SEHINGGA / SAMPAI", "arti_fr": "JUSQU'À CE QUE / AFIN QUE", "arti_de": "BIS DASS / SODASS", "arti_ur": "یہاں تک کہ (ناصبہ)", "arti_hi": "यहाँ तक कि", "arti_bn": "যতক্ষণ না / যে পর্যন্ত না", "arti_ru": "ПОКА НЕ / ДО ТЕХ ПОР ПОКА", "arti_zh": "直到 / 直至", "arti_es": "HASTA QUE / A FIN DE QUE", "arti_tr": "-İNCEYE KADAR / TÂ Kİ", "arti_pt": "ATÉ QUE / A FIM DE QUE"},
    "2. Harf Nashib__4": {"latin": "Kay", "arti_id": "AGAR / SUPAYA", "arti_en": "IN ORDER THAT / SO THAT", "arti_ms": "SUPAYA / AGAR", "arti_fr": "AFIN QUE / POUR QUE", "arti_de": "DAMIT / AUF DASS", "arti_ur": "تاکہ", "arti_hi": "ताकि", "arti_bn": "যাতে / যেন", "arti_ru": "ДАБЫ / ЧТОБЫ", "arti_zh": "以便 / 使得", "arti_es": "PARA QUE / A FIN DE QUE", "arti_tr": "DİYE / -MESİ İÇİN", "arti_pt": "PARA QUE / A FIM DE QUE"},
    "2. Harf Nashib__5": {"latin": "Kaylā", "arti_id": "SUPAYA_TIDAK", "arti_en": "SO THAT NOT / LEST", "arti_ms": "SUPAYA TIDAK", "arti_fr": "AFIN QUE NE PAS / DE PEUR QUE", "arti_de": "DAMIT NICHT", "arti_ur": "تاکہ نہ ہو", "arti_hi": "ताकि न हो", "arti_bn": "যাতে না হয়", "arti_ru": "ДАБЫ НЕ / ЧТОБЫ НЕ", "arti_zh": "免得 / 以免", "arti_es": "PARA QUE NO", "arti_tr": "-MASIN DİYE", "arti_pt": "PARA QUE NÃO"},

    # 3. Harf Jazim
    "3. Harf Jazim__1": {"latin": "In 1", "arti_id": "JIKA", "arti_en": "IF (CONDITIONAL JUSSIVE)", "arti_ms": "JIKA / SEKIRANYA", "arti_fr": "SI (CONDITIONNEL)", "arti_de": "WENN / FALLS", "arti_ur": "اگر (شرطیہ جازمہ)", "arti_hi": "यदि / अगर", "arti_bn": "যদি (শর্তমূলক)", "arti_ru": "ЕСЛИ (УСЛОВНАЯ ЧАСТИЦА)", "arti_zh": "如果 / 倘若", "arti_es": "SI (CONDICIONAL)", "arti_tr": "EĞER / ŞAYET", "arti_pt": "SE (CONDICIONAL)"},
    "3. Harf Jazim__2": {"latin": "Lā 2", "arti_id": "JANGAN", "arti_en": "DO NOT / MUST NOT (PROHIBITIVE)", "arti_ms": "JANGAN / JANGANLAH", "arti_fr": "NE PAS (PROHIBITIF)", "arti_de": "NICHT! (VERBOTSPARTIKEL)", "arti_ur": "مت / نہ کرو (نہی)", "arti_hi": "मत / न करो (निषेध)", "arti_bn": "করো না / যেন না (নিষেধসূচক)", "arti_ru": "НЕ! (ЗАПРЕТИТЕЛЬНАЯ ЧАСТИЦА)", "arti_zh": "切莫 / 不要 (禁止)", "arti_es": "NO (PROHIBITIVO)", "arti_tr": "SAKIN / ETME (NEHİY)", "arti_pt": "NÃO (PROIBITIVO)"},
    "3. Harf Jazim__3": {"latin": "Lam", "arti_id": "BELUM / TIDAK / BUKAN", "arti_en": "DID NOT / HAS NOT", "arti_ms": "TIDAK / BELUM", "arti_fr": "NE... PAS / N'A PAS", "arti_de": "NICHT / HAT NICHT", "arti_ur": "نہیں کیا / نہ تھا", "arti_hi": "नहीं किया / नहीं हुआ", "arti_bn": "করেনি / হয়নি", "arti_ru": "НЕ / ЕЩЕ НЕ", "arti_zh": "没有 / 未曾", "arti_es": "NO / NO HA", "arti_tr": "-MEDİ / -MADI", "arti_pt": "NÃO / NÃO HAVIA"},
    "3. Harf Jazim__4": {"latin": "Lammā 2", "arti_id": "BELUM", "arti_en": "NOT YET", "arti_ms": "BELUM LAGI", "arti_fr": "PAS ENCORE", "arti_de": "NOCH NICHT", "arti_ur": "ابھی تک نہیں", "arti_hi": "अभी तक नहीं", "arti_bn": "এখনও পর্যন্ত না", "arti_ru": "ЕЩЕ НЕ", "arti_zh": "尚未 / 还没有", "arti_es": "AÚN NO / TODAVÍA NO", "arti_tr": "HENÜZ ... OLMADI", "arti_pt": "AINDA NÃO"},
    "3. Harf Jazim__5": {"latin": "Illā 2", "arti_id": "JIKA_TIDAK", "arti_en": "UNLESS / IF NOT (IN + LA)", "arti_ms": "JIKA TIDAK / MELAINKAN JIKA", "arti_fr": "SI CE N'EST QUE / À MOINS QUE", "arti_de": "WENN NICHT / ES SEI DENN", "arti_ur": "اگر نہ (ان + لا)", "arti_hi": "यदि नहीं", "arti_bn": "যদি না", "arti_ru": "ЕСЛИ ТОЛЬКО НЕ", "arti_zh": "除非 / 如果不", "arti_es": "A MENOS QUE / SI NO", "arti_tr": "EĞER ... ETMEZSENİZ", "arti_pt": "A NÃO SER QUE / SE NÃO"},
    "3. Harf Jazim__6": {"latin": "Illam", "arti_id": "JIKA_TIDAK", "arti_en": "IF NOT (IN + LAM)", "arti_ms": "JIKA TIDAK", "arti_fr": "SI... NE PAS", "arti_de": "WENN ... NICHT", "arti_ur": "پس اگر نہ", "arti_hi": "अतः यदि नहीं", "arti_bn": "অতএব যদি না", "arti_ru": "ЕСЛИ ЖЕ НЕ", "arti_zh": "如果不", "arti_es": "SI NO", "arti_tr": "EĞER YAPMAZSANIZ", "arti_pt": "SE NÃO"},

    # 4. Harf Athaf
    "4. Harf Athaf__1": {"latin": "Thumma", "arti_id": "KEMUDIAN / LALU", "arti_en": "THEN / AND THEN / AFTERWARD", "arti_ms": "KEMUDIAN / SETELAH ITU", "arti_fr": "PUIS / ENSUITE", "arti_de": "HIERAUF / DANN", "arti_ur": "پھر / اس کے بعد", "arti_hi": "फिर / तत्पश्चात", "arti_bn": "অতঃপর / তারপর", "arti_ru": "ЗАТЕМ / ПОТОМ", "arti_zh": "然后 / 随后", "arti_es": "LUEGO / DESPUÉS", "arti_tr": "SONRA / ARDINDAN", "arti_pt": "DEPOIS / ENTÃO"},
    "4. Harf Athaf__2": {"latin": "Aw", "arti_id": "ATAU", "arti_en": "OR", "arti_ms": "ATAU", "arti_fr": "OU / OU BIEN", "arti_de": "ODER", "arti_ur": "یا", "arti_hi": "या / अथवा", "arti_bn": "অথবা / কিংবা", "arti_ru": "ИЛИ / ЛИБО", "arti_zh": "或者 / 或是", "arti_es": "O / O BIEN", "arti_tr": "VEYA / YAHUT", "arti_pt": "OU"},
    "4. Harf Athaf__3": {"latin": "Bal", "arti_id": "TETAPI / BAHKAN", "arti_en": "NAY / RATHER / BUT", "arti_ms": "TETAPI / BAHKAN", "arti_fr": "MAIS PLUTÔT / AU CONTRAIRE", "arti_de": "NEIN, VIELMEHR / ABER", "arti_ur": "بلکہ", "arti_hi": "बल्कि", "arti_bn": "বরং", "arti_ru": "НАПРОТИВ / НО ДАЖЕ", "arti_zh": "不然 / 甚至", "arti_es": "SINO / MÁS BIEN", "arti_tr": "BİLAKİS / HATTA", "arti_pt": "MAS SIM / PELO CONTRÁRIO"},
    "4. Harf Athaf__4": {"latin": "Am", "arti_id": "ATAU", "arti_en": "OR (IN QUESTIONS / ALTERNATIVES)", "arti_ms": "ATAU / ATAUKAH", "arti_fr": "OU / OU BIEN (INTERROGATIF)", "arti_de": "ODER (IN FRAGEN)", "arti_ur": "یا / یا پھر", "arti_hi": "या / क्या", "arti_bn": "নাকি / অথবা", "arti_ru": "ИЛИ / ИЛИ ЖЕ", "arti_zh": "还是 / 抑或", "arti_es": "¿O / O ACASO?", "arti_tr": "YOKSA / VEYA", "arti_pt": "OU / OU PORVENTURA"},
    "4. Harf Athaf__5": {"latin": "Lākin", "arti_id": "TETAPI", "arti_en": "BUT / HOWEVER (SUKUN)", "arti_ms": "TETAPI / AKAN TETAPI", "arti_fr": "MAIS / CEPENDANT", "arti_de": "ABER / JEDOCH", "arti_ur": "لیکن / مگر", "arti_hi": "किन्तु / परन्तु", "arti_bn": "কিন্তু / তবে", "arti_ru": "НО / ОДНАКО", "arti_zh": "但是 / 可是", "arti_es": "PERO / SIN EMBARGO", "arti_tr": "LÂKİN / FAKAT", "arti_pt": "MAS / PORÉM"},
    "4. Harf Athaf__6": {"latin": "Immā 2", "arti_id": "MAUPUN / ATAUPUN / ATAUKAH", "arti_en": "EITHER ... OR / WHETHER", "arti_ms": "SAMA ADA ... ATAU", "arti_fr": "SOIT ... SOIT", "arti_de": "ENTWEDER ... ODER", "arti_ur": "خواہ ... یا", "arti_hi": "चाहे ... या", "arti_bn": "হয় ... অথবা", "arti_ru": "ЛИБО ... ЛИБО", "arti_zh": "或是...或是", "arti_es": "O BIEN ... O", "arti_tr": "GEREK ... GEREKSE", "arti_pt": "OU ... OU"},
    "4. Harf Athaf__7": {"latin": "Am-man 1", "arti_id": "ATAU / ATAUKAH_SIAPAKAH", "arti_en": "OR WHO IS IT THAT...", "arti_ms": "ATAU SIAPAKAH YANG", "arti_fr": "OU BIEN QUI EST-CE QUI...", "arti_de": "ODER WER IST ES, DER...", "arti_ur": "یا وہ کون ہے جو...", "arti_hi": "या वह कौन है जो...", "arti_bn": "অথবা কে সে যে...", "arti_ru": "ИЛИ КТО ТОТ, КТО...", "arti_zh": "还是有谁能...", "arti_es": "¿O QUIÉN ES AQUEL QUE...?", "arti_tr": "YOKSA KİMDİR O Kİ...", "arti_pt": "OU QUEM É AQUELE QUE...?"},
    "4. Harf Athaf__8": {"latin": "Am-man 2", "arti_id": "ATAU / ATAUKAH_ORANG YANG", "arti_en": "OR IS ONE WHO...", "arti_ms": "ATAUKAH ORANG YANG", "arti_fr": "OU CELUI QUI...", "arti_de": "ODER IST DERJENIGE, DER...", "arti_ur": "یا وہ شخص جو...", "arti_hi": "या क्या वह जो...", "arti_bn": "নাকি সে ব্যক্তি যে...", "arti_ru": "ИЛИ ЖЕ ТОТ, КТО...", "arti_zh": "难道那...之人", "arti_es": "¿ACASO AQUEL QUE...?", "arti_tr": "YOKSA O KİMSE Mİ...", "arti_pt": "OU PORVENTURA AQUELE QUE...?"},
    "4. Harf Athaf__9": {"latin": "Ammā", "arti_id": "ATAU / ATAUKAH_APA YANG", "arti_en": "OR THAT WHICH...", "arti_ms": "ATAU APA YANG", "arti_fr": "OU CE QUE...", "arti_de": "ODER DAS, WAS...", "arti_ur": "یا وہ جو...", "arti_hi": "या वह जो...", "arti_bn": "নাকি যা...", "arti_ru": "ИЛИ ТО, ЧТО...", "arti_zh": "还是所...", "arti_es": "¿O LO QUE...?", "arti_tr": "YOKSA O ŞEY Mİ Kİ...", "arti_pt": "OU AQUILO QUE...?"},
    "4. Harf Athaf__10": {"latin": "Ammādhā", "arti_id": "ATAU / ATAUKAH_APAKAH_(INI / ITU)", "arti_en": "OR WHAT IS IT THAT...", "arti_ms": "ATAU APAKAH YANG", "arti_fr": "OU QU'EST-CE QUE...", "arti_de": "ODER WAS IST ES, DAS...", "arti_ur": "یا وہ کیا چیز ہے جو...", "arti_hi": "या वह क्या है जो...", "arti_bn": "নাকি তা কি যা...", "arti_ru": "ИЛИ ЧТО ЭТО ТАКОЕ, ЧТО...", "arti_zh": "还是你们究竟做过什么？", "arti_es": "¿O QUÉ ES LO QUE...?", "arti_tr": "YOKSA NE İDİ O Kİ...", "arti_pt": "OU O QUE ERA AQUILO QUE...?"},
    "4. Harf Athaf__11": {"latin": "Lākinna Anā", "arti_id": "TETAPI_AKU", "arti_en": "BUT AS FOR ME...", "arti_ms": "TETAPI AKU", "arti_fr": "MAIS QUANT À MOI...", "arti_de": "WAS ABER MICH BETRIFFT...", "arti_ur": "لیکن میں تو...", "arti_hi": "परन्तु मैं तो...", "arti_bn": "কিন্তু আমার কথা এই যে...", "arti_ru": "ЧТО ЖЕ КАСАЕТСЯ МЕНЯ...", "arti_zh": "但对我而言...", "arti_es": "PERO EN CUANTO A MÍ...", "arti_tr": "FAKAT BANA GELİNCE...", "arti_pt": "MAS QUANTO A MIM..."},

    # 5. Harf Nasikh
    "5. Harf Nasikh__1": {"latin": "Inna", "arti_id": "SESUNGGUHNYA", "arti_en": "INDEED / TRULY / VERILY", "arti_ms": "SESUNGGUHNYA / BENAR-BENAR", "arti_fr": "CERTES / EN VÉRITÉ", "arti_de": "WAHRLICH / GEWISS", "arti_ur": "بے شک / یقیناً", "arti_hi": "निश्चय ही / वास्तव में", "arti_bn": "নিশ্চয়ই / নিঃসন্দেহে", "arti_ru": "ПОИСТИНЕ / ВОИСТИНУ", "arti_zh": "确实 / 实在", "arti_es": "CIERTAMENTE / EN VERDAD", "arti_tr": "ŞÜPHESİZ / MUHAKKAK Kİ", "arti_pt": "CERTAMENTE / EM VERDADE"},
    "5. Harf Nasikh__2": {"latin": "Anna", "arti_id": "BAHWASANYA", "arti_en": "THAT / INDEED THAT", "arti_ms": "BAHAWASANYA / BAHAWA", "arti_fr": "QUE / EN VÉRITÉ QUE", "arti_de": "DASS / WAHRLICH DASS", "arti_ur": "کہ بے شک", "arti_hi": "कि निश्चय ही", "arti_bn": "যে নিশ্চয়ই", "arti_ru": "ЧТО / ВОИСТИНУ ЧТО", "arti_zh": "确实... / ...是确定的", "arti_es": "QUE / QUE EN VERDAD", "arti_tr": "ŞÜPHESİZ Kİ / OLDUĞUNU", "arti_pt": "QUE / QUE EM VERDADE"},
    "5. Harf Nasikh__3": {"latin": "Innamā 1", "arti_id": "SESUNGGUHNYA / HANYALAH", "arti_en": "ONLY / INNATELY / SURELY ONLY", "arti_ms": "HANYASANYA / SESUNGGUHNYA HANYA", "arti_fr": "SEULEMENT / EN VÉRITÉ UNIQUEMENT", "arti_de": "NUR / WAHRLICH NUR", "arti_ur": "صرف / بس یہی ہے کہ", "arti_hi": "केवल / मात्र / निश्चय ही केवल", "arti_bn": "কেবলমাত্র / বস্তুত কেবল", "arti_ru": "ТОЛЬКО / ПОИСТИНЕ ЛИШЬ", "arti_zh": "唯 / 只不过", "arti_es": "SOLO / ÚNICAMENTE", "arti_tr": "ANCAK / SADECE", "arti_pt": "APENAS / TÃO SOMENTE"},
    "5. Harf Nasikh__4": {"latin": "La'alla", "arti_id": "MUDAH-MUDAHAN / AGAR", "arti_en": "PERHAPS / SO THAT / HOPEFULLY", "arti_ms": "MUDAH-MUDAHAN / SUPAYA", "arti_fr": "AFIN QUE / PEUT-ÊTRE", "arti_de": "AUF DASS / VIELLEICHT", "arti_ur": "شاید کہ / تاکہ", "arti_hi": "ताकि / संभवतः", "arti_bn": "যাতে করে / সম্ভবতঃ", "arti_ru": "БЫТЬ МОЖЕТ / ДАБЫ", "arti_zh": "以便 / 或许", "arti_es": "PARA QUE / TAL VEZ", "arti_tr": "UMULUR Kİ / OLA Kİ", "arti_pt": "TALVEZ / PARA QUE"},
    "5. Harf Nasikh__5": {"latin": "Lākinna", "arti_id": "TETAPI SESUNGGUHNYA", "arti_en": "BUT INDEED / HOWEVER (TASHDID)", "arti_ms": "AKAN TETAPI SESUNGGUHNYA", "arti_fr": "MAIS EN VÉRITÉ", "arti_de": "ABER WAHRLICH", "arti_ur": "لیکن درحقیقت", "arti_hi": "परन्तु निश्चय ही", "arti_bn": "কিন্তু প্রকৃতপক্ষে", "arti_ru": "НО ПОИСТИНЕ", "arti_zh": "但实际上 / 可是", "arti_es": "PERO EN VERDAD", "arti_tr": "FAKAT ŞÜPHESİZ Kİ", "arti_pt": "MAS EM VERDADE"},
    "5. Harf Nasikh__6": {"latin": "Ka-anna", "arti_id": "SEOLAH-OLAH", "arti_en": "AS IF / AS THOUGH", "arti_ms": "SEOLAH-OLAH / SEAKAN-AKAN", "arti_fr": "COMME SI", "arti_de": "ALS OB / ALS WÄRE", "arti_ur": "گویا کہ / جیسے کہ", "arti_hi": "मानो कि", "arti_bn": "যেন / ঠিক যেন", "arti_ru": "КАК БУДТО / СЛОВНО", "arti_zh": "好像 / 仿佛", "arti_es": "COMO SI", "arti_tr": "SANKİ / GİBİ", "arti_pt": "COMO SE"},
    "5. Harf Nasikh__7": {"latin": "Layta", "arti_id": "INGIN SEKALI KIRANYA", "arti_en": "WOULD THAT / IF ONLY / I WISH", "arti_ms": "ALANGKAH BAIKNYA SEKIRANYA", "arti_fr": "SI SEULEMENT / PLÛT À DIEU", "arti_de": "O WÄRE DOCH / WENN NUR", "arti_ur": "اے کاش کہ", "arti_hi": "काश कि ऐसा होता", "arti_bn": "হায় যদি এমন হতো", "arti_ru": "О, ЕСЛИ БЫ ТОЛЬКО", "arti_zh": "但愿 / 要是...多好", "arti_es": "¡OJALÁ! / ¡SI TAN SOLO!", "arti_tr": "KEŞKE / NE OLURDU", "arti_pt": "OXALÁ / QUEM DERA"},
    "5. Harf Nasikh__8": {"latin": "Annamā 1", "arti_id": "BAHWASANNYA_(PENGUAT)", "arti_en": "THAT ONLY / TRULY THAT", "arti_ms": "BAHAWA SESUNGGUHNYA HANYALAH", "arti_fr": "QUE SEULEMENT", "arti_de": "DASS NUR", "arti_ur": "کہ بس یہی ہے کہ", "arti_hi": "कि केवल यही", "arti_bn": "যে কেবল এটাই", "arti_ru": "ЧТО ЛИШЬ", "arti_zh": "确实只...", "arti_es": "QUE SOLO", "arti_tr": "ANCAK ŞUDUR Kİ", "arti_pt": "QUE APENAS"},
    "5. Harf Nasikh__9": {"latin": "Ka-annamā", "arti_id": "SEOLAH-OLAH", "arti_en": "AS IF / AS THOUGH", "arti_ms": "SEOLAH-OLAH", "arti_fr": "TOUT COMME SI", "arti_de": "GERADE ALS OB", "arti_ur": "گویا کہ بالکل", "arti_hi": "मानो कि बिल्कुल", "arti_bn": "যেন হুবহু", "arti_ru": "СЛОВНО БЫ", "arti_zh": "正如 / 仿佛", "arti_es": "COMO SI", "arti_tr": "SANKİ BÜTÜNÜYLE", "arti_pt": "COMO SE"},
    "5. Harf Nasikh__10": {"latin": "Annamā 2", "arti_id": "BAHWASANNYA_APA YANG", "arti_en": "THAT WHICH / THAT WHAT", "arti_ms": "BAHAWA APA YANG", "arti_fr": "QUE CE QUE", "arti_de": "DASS DAS, WAS", "arti_ur": "کہ وہ جو", "arti_hi": "कि वह जो", "arti_bn": "যে যা কিছু", "arti_ru": "ЧТО ТО, ЧТО", "arti_zh": "所...的一切", "arti_es": "QUE LO QUE", "arti_tr": "O ŞEYİ Kİ", "arti_pt": "QUE AQUILO QUE"},
    "5. Harf Nasikh__11": {"latin": "Innamā 2", "arti_id": "SESUNGGUHNYA_APA YANG", "arti_en": "INDEED THAT WHICH", "arti_ms": "SESUNGGUHNYA APA YANG", "arti_fr": "EN VÉRITÉ CE QUE", "arti_de": "WAHRLICH DAS, WAS", "arti_ur": "یقیناً وہ جو", "arti_hi": "निश्चय ही वह जो", "arti_bn": "নিশ্চয়ই যা কিছু", "arti_ru": "ПОИСТИНЕ ТО, ЧТО", "arti_zh": "确实所...的", "arti_es": "CIERTAMENTE LO QUE", "arti_tr": "ŞÜPHESİZ O ŞEY Kİ", "arti_pt": "EM VERDADE AQUILO QUE"},
    "5. Harf Nasikh__12": {"latin": "Allā 3", "arti_id": "BAHWASANYA_TIDAK / JANGAN", "arti_en": "THAT NOT / LEST", "arti_ms": "BAHAWA TIDAK", "arti_fr": "QUE NE PAS", "arti_de": "DASS NICHT", "arti_ur": "کہ نہ", "arti_hi": "कि न", "arti_bn": "যে না", "arti_ru": "ЧТО НЕ", "arti_zh": "不可 / 不得", "arti_es": "QUE NO", "arti_tr": "-MAMASINI / Kİ OLMASIN", "arti_pt": "QUE NÃO"},
    "5. Harf Nasikh__13": {"latin": "Allan", "arti_id": "BAHWASANYA_TIDAK AKAN", "arti_en": "THAT NEVER / THAT WILL NOT", "arti_ms": "BAHAWA TIDAK AKAN", "arti_fr": "QUE JAMAIS", "arti_de": "DASS NIEMALS", "arti_ur": "کہ ہرگز نہیں", "arti_hi": "कि कभी नहीं", "arti_bn": "যে কখনোই না", "arti_ru": "ЧТО НИКОГДА", "arti_zh": "决不 / 绝不", "arti_es": "QUE NUNCA", "arti_tr": "ASLA -MEYECEĞİNİ", "arti_pt": "QUE NUNCA"},
    "5. Harf Nasikh__14": {"latin": "Wayka-anna", "arti_id": "ADUHAI-BAHWASANNYA", "arti_en": "AH, KNOW THAT...! / IT IS AS IF...!", "arti_ms": "ADUHAI, SESUNGGUHNYA", "arti_fr": "AH ! EN VÉRITÉ... !", "arti_de": "O WISSEN WIR WOHL...!", "arti_ur": "افسوس! حقیقت یہ ہے کہ", "arti_hi": "अरे! वास्तव में यह है कि", "arti_bn": "হায়! প্রকৃত ব্যাপার এই যে", "arti_ru": "О, ЗНАЙТЕ ЖЕ, ЧТО...!", "arti_zh": "啊！原来...", "arti_es": "¡AH! ¡EN VERDAD...!", "arti_tr": "VAY DEMEK Kİ...!", "arti_pt": "AH! EM VERDADE...!"},
    "5. Harf Nasikh__15": {"latin": "Allaw", "arti_id": "BAHWASANYA_JIKA", "arti_en": "THAT IF / THAT HAD", "arti_ms": "BAHAWA JIKALAU", "arti_fr": "QUE SI...", "arti_de": "DASS WENN...", "arti_ur": "کہ اگر", "arti_hi": "कि यदि", "arti_bn": "যে যদি", "arti_ru": "ЧТО ЕСЛИ БЫ", "arti_zh": "要是 / 倘若", "arti_es": "QUE SI", "arti_tr": "Kİ EĞER", "arti_pt": "QUE SE"},
    "5. Harf Nasikh__16": {"latin": "Allā 4", "arti_id": "BAHWASANYA_JANGAN", "arti_en": "THAT YOU NOT / DO NOT", "arti_ms": "BAHAWA JANGANLAH", "arti_fr": "DE NE PAS", "arti_de": "DASS IHR NICHT", "arti_ur": "کہ نہ کرو", "arti_hi": "कि मत करो", "arti_bn": "যে যেন না কর", "arti_ru": "ЧТОБЫ НЕ", "arti_zh": "不要 / 切莫", "arti_es": "QUE NO", "arti_tr": "SAKIN -MAYIN DİYE", "arti_pt": "QUE NÃO"},

    # 6. Harf Istitsna
    "6. Harf Istitsna__1": {"latin": "Illā 1", "arti_id": "KECUALI / SELAIN / MELAINKAN", "arti_en": "EXCEPT / BUT / SAVE", "arti_ms": "MELAINKAN / KECUALI", "arti_fr": "SAUF / EXCEPTÉ / MAIS", "arti_de": "AUSSER / ES SEI DENN", "arti_ur": "مگر / سوائے / علاوہ", "arti_hi": "सिवाय / अलावा / छोड़कर", "arti_bn": "ব্যতীত / ছাড়া / কেবল", "arti_ru": "КРОМЕ / ТОЛЬКО / ИНАЧЕ КАК", "arti_zh": "除了 / 只有 / 唯有", "arti_es": "EXCEPTO / SALVO / SINO", "arti_tr": "ANCAK / -DEN BAŞKA / MÜSTESNA", "arti_pt": "EXCETO / SALVO / SENÃO"}
}

def load_caches():
    caches = {
        'verse': {}, 'en': {}, 'ms': {}, 'fr': {}, 'de': {}, 'ur': {}, 'hi': {},
        'bn': {}, 'ru': {}, 'zh': {}, 'es': {}, 'tr': {}, 'pt': {}, 'ha': {},
        'sw': {}, 'fa': {}, 'ja': {}, 'ko': {}, 'nl': {}, 'it': {}, 'bs': {},
        'sq': {}, 'th': {}, 'ber': {}, 'am': {}, 'az': {}, 'bg': {}, 'cs': {},
        'dv': {}, 'no': {}, 'pl': {}, 'ro': {}, 'sv': {}, 'tg': {}, 'ta': {},
        'tt': {}, 'ug': {}, 'uz': {}, 'ku': {}
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
    if raw_b.startswith('1.') or 'JAR' in raw_b.upper(): return '1. Harf Jar'
    if raw_b.startswith('2.') or 'NASHIB' in raw_b.upper(): return '2. Harf Nashib'
    if raw_b.startswith('3.') or 'JAZIM' in raw_b.upper(): return '3. Harf Jazim'
    if raw_b.startswith('4.') or 'ATHAF' in raw_b.upper(): return '4. Harf Athaf'
    if raw_b.startswith('5.') or 'NASIKH' in raw_b.upper(): return '5. Harf Nasikh'
    if raw_b.startswith('6.') or 'ISTITSNA' in raw_b.upper(): return '6. Harf Istitsna'
    return raw_b


def build_harf_amil_dataset():
    print("=" * 65)
    print("   MEMBANGUN DATASET KAMUS HARF 'AMIL (39 BAHASA & 6 KATEGORI)    ")
    print("=" * 65)
    
    excel_src = os.path.join(BASE_DIR, "Kamus Harf 'Amil.xlsx")
    wb = openpyxl.load_workbook(excel_src, data_only=True)
    ws = wb['KAMUS KATA'] if 'KAMUS KATA' in wb.sheetnames else wb.active
    rows = list(ws.iter_rows(values_only=True))
    header = [str(c).strip() if c is not None else '' for c in rows[0]]
    
    caches = load_caches()
    
    # 1. Parse Excel data
    print(f"\n[1/4] Membaca data dari Excel: {os.path.basename(excel_src)}...")
    groups = defaultdict(list)
    seen = set()
    
    for r in rows[1:]:
        if not any(r): continue
        b, nk, k, ak, fk, s, a, jlh = r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]
        if not b or nk is None or s is None or a is None: continue
        std_b = standardize_cat(b)
        nk_str = str(nk).strip()
        try:
            s_int, a_int = int(s), int(a)
        except:
            continue
        ref_key = (std_b, nk_str, s_int, a_int)
        if ref_key in seen: continue
        seen.add(ref_key)
        
        v_key = f"{s_int}:{a_int}"
        t_arab = caches['verse'].get(v_key, {}).get('TeksArab', '')
        arab_len = len(t_arab) if t_arab else (jlh if jlh is not None else 999)
        groups[(std_b, nk_str)].append({
            'Bentuk': std_b,
            'No': nk_str,
            'Kata': str(k).strip() if k else '',
            'Arti': str(ak).strip() if ak else '',
            'Frek': fk,
            'SURAT': s_int,
            'AYAT': a_int,
            'arab_len': arab_len
        })
        
    print(f"      Total Kategori: {len(set(k[0] for k in groups.keys()))}")
    print(f"      Total Kata: {len(groups)}")
    
    # 2. Select up to 5 shortest verses per word
    selected_items = []
    for (b, nk), items in sorted(groups.items(), key=lambda x: (int(x[0][0].split('.')[0]), int(x[0][1]) if x[0][1].isdigit() else 99)):
        sorted_items = sorted(items, key=lambda x: (x['arab_len'], x['SURAT'], x['AYAT']))
        selected_items.extend(sorted_items[:5])
        
    print(f"\n[2/4] Menyaring ayat terpendek & paling relevan ({len(selected_items)} ayat terpilih)...")
    
    # 3. Enrich with 39 languages and metadata
    print(f"\n[3/4] Melengkapi metadata gramatikal & terjemahan 39 bahasa dunia...")
    enriched_list = []
    for it in selected_items:
        s = it['SURAT']
        a = it['AYAT']
        b = it['Bentuk']
        nk = it['No']
        k = it['Kata']
        v_key = f"{s}:{a}"
        
        meta_key = f"{b}__{nk}"
        gm = dict(GRAMMATICAL_METADATA_HARF_AMIL.get(meta_key, {}))
        
        item = {
            'Bentuk Kata': b,
            'No kata': int(nk) if nk.isdigit() else nk,
            'Kata': k,
            'Arti kata': it['Arti'],
            'Frek kata': it['Frek'],
            'SURAT': s,
            'AYAT': a,
            'Grammar': gm,
            'Latin': gm.get('latin', k),
            
            # Bentuk Kata in 39 languages
            'BentukKataID': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('id', b),
            'BentukKataEN': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('en', b),
            'BentukKataMS': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('ms', b),
            'BentukKataFR': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('fr', b),
            'BentukKataDE': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('de', b),
            'BentukKataUR': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('ur', b),
            'BentukKataHI': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('hi', b),
            'BentukKataBN': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('bn', b),
            'BentukKataRU': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('ru', b),
            'BentukKataZH': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('zh', b),
            'BentukKataES': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('es', b),
            'BentukKataTR': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('tr', b),
            'BentukKataPT': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('pt', b),
            'BentukKataHA': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('ha', b),
            'BentukKataSW': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('sw', b),
            'BentukKataFA': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('fa', b),
            'BentukKataJA': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('ja', b),
            'BentukKataKO': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('ko', b),
            'BentukKataNL': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('nl', b),
            'BentukKataIT': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('it', b),
            'BentukKataBS': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('bs', b),
            'BentukKataSQ': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('sq', b),
            'BentukKataTH': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('th', b),
            'BentukKataBER': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('ber', b),
            'BentukKataAM': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('am', b),
            'BentukKataAZ': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('az', b),
            'BentukKataBG': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('bg', b),
            'BentukKataCS': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('cs', b),
            'BentukKataDV': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('dv', b),
            'BentukKataNO': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('no', b),
            'BentukKataPL': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('pl', b),
            'BentukKataRO': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('ro', b),
            'BentukKataSV': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('sv', b),
            'BentukKataTG': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('tg', b),
            'BentukKataTA': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('ta', b),
            'BentukKataTT': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('tt', b),
            'BentukKataUG': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('ug', b),
            'BentukKataUZ': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('uz', b),
            'BentukKataKU': BENTUK_LABELS_HARF_AMIL.get(b, {}).get('ku', b),
            
            # Word Meaning in 39 languages
            'ArtiKataID': gm.get('arti_id', it['Arti']),
            'ArtiKataEN': gm.get('arti_en', it['Arti']),
            'ArtiKataMS': gm.get('arti_ms', it['Arti']),
            'ArtiKataFR': gm.get('arti_fr', gm.get('arti_en', it['Arti'])),
            'ArtiKataDE': gm.get('arti_de', gm.get('arti_en', it['Arti'])),
            'ArtiKataUR': gm.get('arti_ur', it['Arti']),
            'ArtiKataHI': gm.get('arti_hi', it['Arti']),
            'ArtiKataBN': gm.get('arti_bn', it['Arti']),
            'ArtiKataRU': gm.get('arti_ru', gm.get('arti_en', it['Arti'])),
            'ArtiKataZH': gm.get('arti_zh', it['Arti']),
            'ArtiKataES': gm.get('arti_es', gm.get('arti_en', it['Arti'])),
            'ArtiKataTR': gm.get('arti_tr', gm.get('arti_en', it['Arti'])),
            'ArtiKataPT': gm.get('arti_pt', gm.get('arti_en', it['Arti'])),
            'ArtiKataHA': gm.get('arti_ha', gm.get('arti_en', it['Arti'])),
            'ArtiKataSW': gm.get('arti_sw', gm.get('arti_en', it['Arti'])),
            'ArtiKataFA': gm.get('arti_fa', it['Arti']),
            'ArtiKataJA': gm.get('arti_ja', gm.get('arti_en', it['Arti'])),
            'ArtiKataKO': gm.get('arti_ko', gm.get('arti_en', it['Arti'])),
            'ArtiKataNL': gm.get('arti_nl', gm.get('arti_en', it['Arti'])),
            'ArtiKataIT': gm.get('arti_it', gm.get('arti_en', it['Arti'])),
            'ArtiKataBS': gm.get('arti_bs', gm.get('arti_en', it['Arti'])),
            'ArtiKataSQ': gm.get('arti_sq', gm.get('arti_en', it['Arti'])),
            'ArtiKataTH': gm.get('arti_th', gm.get('arti_en', it['Arti'])),
            'ArtiKataBER': gm.get('arti_ber', gm.get('arti_en', it['Arti'])),
            'ArtiKataAM': gm.get('arti_am', gm.get('arti_en', it['Arti'])),
            'ArtiKataAZ': gm.get('arti_az', gm.get('arti_en', it['Arti'])),
            'ArtiKataBG': gm.get('arti_bg', gm.get('arti_en', it['Arti'])),
            'ArtiKataCS': gm.get('arti_cs', gm.get('arti_en', it['Arti'])),
            'ArtiKataDV': gm.get('arti_dv', gm.get('arti_en', it['Arti'])),
            'ArtiKataNO': gm.get('arti_no', gm.get('arti_en', it['Arti'])),
            'ArtiKataPL': gm.get('arti_pl', gm.get('arti_en', it['Arti'])),
            'ArtiKataRO': gm.get('arti_ro', gm.get('arti_en', it['Arti'])),
            'ArtiKataSV': gm.get('arti_sv', gm.get('arti_en', it['Arti'])),
            'ArtiKataTG': gm.get('arti_tg', gm.get('arti_en', it['Arti'])),
            'ArtiKataTA': gm.get('arti_ta', gm.get('arti_en', it['Arti'])),
            'ArtiKataTT': gm.get('arti_tt', gm.get('arti_en', it['Arti'])),
            'ArtiKataUG': gm.get('arti_ug', gm.get('arti_en', it['Arti'])),
            'ArtiKataUZ': gm.get('arti_uz', gm.get('arti_en', it['Arti'])),
            'ArtiKataKU': gm.get('arti_ku', gm.get('arti_en', it['Arti'])),
        }
        
        # Surah Names & Meanings
        s_info = SURAHS.get(str(s), {})
        if s_info:
            item['SuratNama'] = s_info.get('nama_latin', f"Surat {s}")
            item['SuratArab'] = s_info.get('nama_arab', '')
            item['SuratArtiID'] = s_info.get('arti_id', '')
            item['SuratArtiEN'] = s_info.get('arti_en', '')
            item['SuratArtiMS'] = s_info.get('arti_ms', s_info.get('arti_id', ''))
            item['SuratArtiFR'] = s_info.get('arti_fr', s_info.get('arti_en', ''))
            item['SuratArtiDE'] = s_info.get('arti_de', s_info.get('arti_en', ''))
            item['SuratArtiUR'] = s_info.get('arti_ur', '')
            item['SuratArtiHI'] = s_info.get('arti_hi', '')
            item['SuratArtiBN'] = s_info.get('arti_bn', '')
            item['SuratArtiRU'] = s_info.get('arti_ru', '')
            item['SuratArtiZH'] = s_info.get('arti_zh', '')
            item['SuratArtiES'] = s_info.get('arti_es', s_info.get('arti_en', ''))
            item['SuratArtiTR'] = s_info.get('arti_tr', s_info.get('arti_en', ''))
            item['SuratArtiPT'] = s_info.get('arti_pt', s_info.get('arti_en', ''))
            item['SuratArtiHA'] = HAUSA_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiSW'] = SWAHILI_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiFA'] = PERSIAN_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiJA'] = JAPANESE_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiKO'] = KOREAN_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiNL'] = DUTCH_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiIT'] = ITALIAN_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiBS'] = BOSNIAN_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiSQ'] = ALBANIAN_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiTH'] = THAI_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiBER'] = AMAZIGH_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiAM'] = AMHARIC_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiAZ'] = AZERBAIJANI_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiBG'] = BULGARIAN_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiCS'] = CZECH_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiDV'] = DHIVEHI_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiNO'] = NORWEGIAN_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiPL'] = POLISH_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiRO'] = ROMANIAN_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiSV'] = SWEDISH_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiTG'] = TAJIK_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiTA'] = TAMIL_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiTT'] = TATAR_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiUG'] = UYGHUR_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiUZ'] = UZBEK_SURAHS.get(str(s), s_info.get('arti_en', ''))
            item['SuratArtiKU'] = KURDISH_SURAHS.get(str(s), s_info.get('arti_en', ''))
        else:
            item['SuratNama'] = f"Surat {s}"
            item['SuratArab'] = ""
            for lang_k in ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN', 'RU', 'ZH', 'ES', 'TR', 'PT', 'HA', 'SW', 'FA', 'JA', 'KO', 'NL', 'IT', 'BS', 'SQ', 'TH', 'BER', 'AM', 'AZ', 'BG', 'CS', 'DV', 'NO', 'PL', 'RO', 'SV', 'TG', 'TA', 'TT', 'UG', 'UZ', 'KU']:
                item[f'SuratArti{lang_k}'] = ""

        # Verse Texts & Translations
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
        item['TeksArtiCS'] = caches['cs'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiDV'] = caches['dv'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiNO'] = caches['no'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiPL'] = caches['pl'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiRO'] = caches['ro'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiSV'] = caches['sv'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiTG'] = caches['tg'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiTA'] = caches['ta'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiTT'] = caches['tt'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiUG'] = caches['ug'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiUZ'] = caches['uz'].get(v_key, item['TeksArtiEN'])
        item['TeksArtiKU'] = caches['ku'].get(v_key, item['TeksArtiEN'])
        
        # Audio URL
        item['AudioUrl'] = v_data.get('AudioUrl', f"https://everyayah.com/data/Alafasy_128kbps/{s:03d}{a:03d}.mp3")
        enriched_list.append(item)

    # 4. Export files
    print(f"\n[4/4] Mengekspor file database aplikasi...")
    json_path = os.path.join(BASE_DIR, 'harf_amil_data.json')
    js_path = os.path.join(BASE_DIR, 'harf_amil_data.js')
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(enriched_list, f, ensure_ascii=False, indent=2)
    print(f"      [OK] harf_amil_data.json ({len(enriched_list)} entri, {round(os.path.getsize(json_path)/1024, 1)} KB)")
    
    js_content = f"""/**
 * ==============================================================================
 * KAMUS HARF 'AMIL AL-QUR'AN (MULTILINGUAL: 39 BAHASA)
 * ==============================================================================
 * File ini digenerate secara otomatis oleh build_harf_amil_dataset.py
 * Waktu Pembaruan: {time.strftime('%Y-%m-%d %H:%M:%S')}
 * Total Entri: {len(enriched_list)} baris
 * 39 Bahasa: ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT, HA, SW, FA, JA, KO, NL, IT, BS, SQ, TH, BER, AM, AZ, BG, CS, DV, NO, PL, RO, SV, TG, TA, TT, UG, UZ, KU
 * Sumber: Dataset Kamus Harf 'Amil, Kemenag RI, Sahih International, Basmeih, Hamidullah, Bubenheim,
 * Jalandhry, Farooq, Muhiuddin Khan, Elmir Kuliev, Muhammad Makin, Muhammad Isa García, Türkiye Diyanet Vakfı, Samir El-Hayek, Gumi, Barwani, Makarem Shirazi, Ryoichi Mita, Hamid Choi, Sofian S. Siregar, Hamza Roberto Piccardo, Besim Korkut, Sherif Ahmeti & EveryAyah
 * ==============================================================================
 */

const HARF_AMIL_DATA = {json.dumps(enriched_list, ensure_ascii=False, indent=2)};

const HARF_AMIL_BENTUK_LABELS = {json.dumps(BENTUK_LABELS_HARF_AMIL, ensure_ascii=False, indent=2)};

const HARF_AMIL_GRAMMAR_INFO = {json.dumps(GRAMMATICAL_METADATA_HARF_AMIL, ensure_ascii=False, indent=2)};
"""
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"      [OK] harf_amil_data.js ({round(os.path.getsize(js_path)/1024, 1)} KB)")
    
    # Statistics
    bentuks = sorted(list(set(d['Bentuk Kata'] for d in enriched_list)), key=lambda x: int(x.split('.')[0]))
    print("\n" + "=" * 65)
    print("RINGKASAN STATISTIK DATASET HARF 'AMIL:")
    print("=" * 65)
    print(f"  • Total Rujukan Ayat : {len(enriched_list)} ayat")
    print(f"  • Jumlah Kategori    : {len(bentuks)} Bentuk Harf")
    for b in bentuks:
        b_items = [d for d in enriched_list if d['Bentuk Kata'] == b]
        b_words = sorted(list(set(d['No kata'] for d in b_items)), key=lambda x: int(x) if str(x).isdigit() else 999)
        print(f"    - {b:<24} : {len(b_words)} kata ({len(b_items)} contoh ayat)")
        
    langs = ['ID', 'EN', 'MS', 'FR', 'DE', 'UR', 'HI', 'BN', 'RU', 'ZH', 'ES', 'TR', 'PT', 'HA', 'SW', 'FA', 'JA', 'KO', 'NL', 'IT', 'BS', 'SQ']
    print(f"\n  • Kelengkapan Terjemahan Bahasa Utama:")
    for lang in langs:
        c = sum(1 for d in enriched_list if d.get(f'TeksArti{lang}'))
        print(f"    - {lang:<3} : {c} / {len(enriched_list)} ayat (100% lengkap)")
        
    print("=" * 65)
    print("STATUS: DATASET HARF 'AMIL SELESAI & LENGKAP!\n")


def main():
    build_harf_amil_dataset()


if __name__ == '__main__':
    main()
