import re

LANG_COPY_MAP = {
    'id-ID': (' Salin Teks Ini', ' Tersalin!', 'Salin Teks Terjemahan'),
    'ms-MY': (' Salin Teks Ini', ' Disalin!', 'Salin Teks Terjemahan'),
    'en-US': (' Copy This Text', ' Copied!', 'Copy Translation Text'),
    'ur-PK': (' یہ متن کاپی کریں', ' کاپی ہو گیا!', 'ترجمہ کا متن کاپی کریں'),
    'bn-BD': (' এই পাঠটি অনুলিপি করুন', ' অনুলিপি করা হয়েছে!', 'অনুবাদ টেক্সট কপি করুন'),
    'hi-IN': (' यह पाठ कॉपी करें', ' कॉपी हो गया!', 'अनुवाद पाठ कॉपी करें'),
    'ru-RU': (' Копировать этот текст', ' Скопировано!', 'Копировать текст перевода'),
    'zh-CN': (' 复制此文本', ' 已复制！', '复制译文'),
    'fr-FR': (' Copier ce texte', ' Copié !', 'Copier le texte de la traduction'),
    'es-ES': (' Copiar este texto', ' ¡Copiado!', 'Copiar texto de traducción'),
    'pt-PT': (' Copiar este texto', ' Copiado!', 'Copiar texto da tradução'),
    'it-IT': (' Copia questo testo', ' Copiato!', 'Copia il testo della traduzione'),
    'tr-TR': (' Bu Metni Kopyala', ' Kopyalandı!', 'Çeviri Metnini Kopyala'),
    'de-DE': (' Diesen Text kopieren', ' Kopiert!', 'Übersetzungstext kopieren'),
    'ko-KR': (' 이 텍스트 복사', ' 복사됨!', '번역 텍스트 복사'),
    'ja-JP': (' このテキストをコピー', ' コピー完了！', '翻訳テキストをコピー'),
    'th-TH': (' คัดลอกข้อความนี้', ' คัดลอกแล้ว!', 'คัดลอกข้อความคำแปล'),
    'ha-NG': (' Kwafi Wannan Rubutun', ' An kwafa!', 'Kwafi Rubutun Fassara'),
    'sw-TZ': (' Nakili Maandishi Haya', ' Imenakiliwa!', 'Nakili Maandishi ya Tafsiri'),
    'bs-BA': (' Kopiraj ovaj tekst', ' Kopirano!', 'Kopiraj tekst prijevoda'),
    'sq-AL': (' Kopjo këtë tekst', ' U kopjua!', 'Kopjo tekstin e përkthimit'),
    'ber-DZ': (' ⵏⵖⴻⵍ ⴰⴹⵔⵉⵙ-ⴰ', ' ⵢⴻⵜⵜⵡⴰⵏⵖⴻⵍ!', 'ⵏⵖⴻⵍ ⴰⴹⵔⵉⵙ ⵏ ⵜⵙⵓⵇⵉⵍⵜ'),
    'am-ET': (' ይህንን ጽሑፍ ቅዳ', ' ተቀድቷል!', 'የትርጉም ጽሑፍ ቅዳ'),
    'az-AZ': (' Bu mətni kopyalayın', ' Kopyalandı!', 'Tərcümə mətnini kopyalayın'),
    'bg-BG': (' Копирай този текст', ' Копирано!', 'Копирай текста на превода'),
    'cs-CZ': (' Zkopírovat tento text', ' Zkopírováno!', 'Zkopírovat text překladu'),
    'dv-MV': (' މި ލިޔުން ކޮޕީކުރޭ', ' ކޮޕީ ކުރެވިއްޖެ!', 'ތަރުޖަމާގެ ލިޔުން ކޮޕީކުރޭ'),
    'nl-NL': (' Kopieer deze tekst', ' Gekopieerd!', 'Kopieer vertaaltekst'),
    'no-NO': (' Kopier denne teksten', ' Kopiert!', 'Kopier oversettelsestekst'),
    'pl-PL': (' Skopiuj ten tekst', ' Skopiowano!', 'Skopiuj tekst tłumaczenia'),
    'ro-RO': (' Copiază acest text', ' Copiat!', 'Copiază textul traducerii'),
    'sv-SE': (' Kopiera denna text', ' Kopierat!', 'Kopiera översättningstext'),
    'tg-TJ': (' Ин матнро нусхабардорӣ кунед', ' Нусхабардорӣ шуд!', 'Нусхабардории матни тарҷума'),
    'ta-IN': (' இந்த உரையை நகலெடுக்கவும்', ' நகலெடுக்கப்பட்டது!', 'மொழிபெயர்ப்பு உரையை நகலெடுக்கவும்'),
    'tt-RU': (' Бу текстны күчермәләү', ' Күчермәләнде!', 'Тәрҗемә текстын күчермәләү'),
    'ug-CN': (' بۇ تېكىستنى كۆچۈرۈش', ' كۆچۈرۈلدى!', 'تەرجىمە تېكىستىنى كۆچۈرۈش'),
    'ar-SA': (' نسخ هذا النص', ' تم النسخ!', 'نسخ نص الترجمة والتفسير'),
    'ku-IQ': (' ئەم دەقە کۆپی بکە', ' کۆپی کرا!', 'کۆپیکردنی دەقی وەرگێڕان'),
    'uz-UZ': (' Ushbu matnni nusxalash', ' Nusxalandi!', 'Tarjima matnini nusxalash')
}

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Normalize newline for regex processing
newline = '\r\n' if '\r\n' in content else '\n'

count = 0
for lang_key, (copy_txt, copied_txt, copy_title) in LANG_COPY_MAP.items():
    # Regex matching lang entry
    pat = re.compile(rf"('{re.escape(lang_key)}':\s*\{{[\s\S]*?aiText:\s*'[^\r\n']+',)", re.MULTILINE)
    m = pat.search(content)
    if m:
        matched = m.group(1)
        if 'copyText:' not in matched:
            replacement = matched + f"{newline}                copyText: '{copy_txt}',{newline}                copiedText: '{copied_txt}',{newline}                copyTitle: '{copy_title}',"
            content = content.replace(matched, replacement)
            count += 1
            print(f"Added copy config for {lang_key}")
        else:
            print(f"Already had copyText for {lang_key}")
    else:
        print(f"Pattern failed for {lang_key}")

print(f"Total updated: {count}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated index.html successfully!")
