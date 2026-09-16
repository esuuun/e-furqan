import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

app_js_path = 'app.js'
with open(app_js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update elements definition: add tabDictHarfAmil, labelTabHarfAmil, badgeTabHarfAmil
old_elements_tabs = """    // Tabs
    tabDictJamid: document.getElementById('tabDictJamid'),
    tabDictHarf: document.getElementById('tabDictHarf'),
    labelTabJamid: document.getElementById('labelTabJamid'),
    badgeTabJamid: document.getElementById('badgeTabJamid'),
    labelTabHarf: document.getElementById('labelTabHarf'),
    badgeTabHarf: document.getElementById('badgeTabHarf'),"""

new_elements_tabs = """    // Tabs
    tabDictJamid: document.getElementById('tabDictJamid'),
    tabDictHarf: document.getElementById('tabDictHarf'),
    tabDictHarfAmil: document.getElementById('tabDictHarfAmil'),
    labelTabJamid: document.getElementById('labelTabJamid'),
    badgeTabJamid: document.getElementById('badgeTabJamid'),
    labelTabHarf: document.getElementById('labelTabHarf'),
    badgeTabHarf: document.getElementById('badgeTabHarf'),
    labelTabHarfAmil: document.getElementById('labelTabHarfAmil'),
    badgeTabHarfAmil: document.getElementById('badgeTabHarfAmil'),"""

if old_elements_tabs in content:
    content = content.replace(old_elements_tabs, new_elements_tabs)
    print("[OK] Updated elements cache for tabDictHarfAmil")
else:
    print("[WARN] Could not find old_elements_tabs")

# 2. Update switchDictionary function
old_switch_dict = """  // Switch Active Dictionary ('jamid' | 'harf')
  function switchDictionary(dictKey) {
    state.activeDict = dictKey;
    localStorage.setItem('dhamir_active_dict', dictKey);

    if (elements.tabDictJamid && elements.tabDictHarf) {
      if (dictKey === 'jamid') {
        elements.tabDictJamid.classList.add('active');
        elements.tabDictJamid.setAttribute('aria-selected', 'true');
        elements.tabDictHarf.classList.remove('active');
        elements.tabDictHarf.setAttribute('aria-selected', 'false');
      } else {
        elements.tabDictHarf.classList.add('active');
        elements.tabDictHarf.setAttribute('aria-selected', 'true');
        elements.tabDictJamid.classList.remove('active');
        elements.tabDictJamid.setAttribute('aria-selected', 'false');
      }
    }

    updateHeaderTitles();
    initData();
    populateBentukDropdown();
    
    if (availableBentukKatas.length > 0) {
      selectBentuk(availableBentukKatas[0]);
    } else {
      selectBentuk('');
    }
  }"""

new_switch_dict = """  // Switch Active Dictionary ('jamid' | 'harf' | 'harf_amil')
  function switchDictionary(dictKey) {
    state.activeDict = dictKey;
    localStorage.setItem('dhamir_active_dict', dictKey);

    const tabs = [
      { el: elements.tabDictJamid, key: 'jamid' },
      { el: elements.tabDictHarf, key: 'harf' },
      { el: elements.tabDictHarfAmil, key: 'harf_amil' }
    ];

    tabs.forEach(tab => {
      if (tab.el) {
        if (tab.key === dictKey) {
          tab.el.classList.add('active');
          tab.el.setAttribute('aria-selected', 'true');
        } else {
          tab.el.classList.remove('active');
          tab.el.setAttribute('aria-selected', 'false');
        }
      }
    });

    updateHeaderTitles();
    initData();
    populateBentukDropdown();
    
    if (availableBentukKatas.length > 0) {
      selectBentuk(availableBentukKatas[0]);
    } else {
      selectBentuk('');
    }
  }"""

if old_switch_dict in content:
    content = content.replace(old_switch_dict, new_switch_dict)
    print("[OK] Updated switchDictionary function")
else:
    print("[WARN] Could not find old_switch_dict")

# 3. Update updateHeaderTitles to include Harf 'Amil
harf_amil_headers_code = """    if (state.activeDict === 'harf_amil') {
      if (state.lang === 'ja') {
        elements.brandTitle.innerHTML = 'ハルフ・アーミル <span>辞書</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'クルアーン作用不変化詞インタラクティブ辞典 (6分類・54語)';
        if (elements.docTitle) elements.docTitle.textContent = 'ハルフ・アーミル辞書 | クルアーン不変化詞インタラクティブリファレンス';
      } else if (state.lang === 'ko') {
        elements.brandTitle.innerHTML = '하르프 아밀 <span>사전</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = '꾸란 지배 불변사 상호작용 사전 (6개 범주 · 54개 단어)';
        if (elements.docTitle) elements.docTitle.textContent = '하르프 아밀 사전 | 꾸란 불변사 참조';
      } else if (state.lang === 'fa') {
        elements.brandTitle.innerHTML = 'فرهنگ <span>حروف عامل</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'لغت‌نامه تعاملی ۶ دسته و ۵۴ حرف عامل قرآن کریم';
        if (elements.docTitle) elements.docTitle.textContent = 'فرهنگ حروف عامل | مراجع تعاملی حروف قرآن';
      } else if (state.lang === 'sw') {
        elements.brandTitle.innerHTML = "Kamusi ya <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Kamusi Shirikishi ya Herufi 54 Zenye Athari za Kisarufi Katika Qur'ani";
        if (elements.docTitle) elements.docTitle.textContent = "Kamusi ya Harf 'Amil | Qur'ani Tukufu";
      } else if (state.lang === 'ha') {
        elements.brandTitle.innerHTML = "Ƙamus ɗin <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Ƙamus Mai Ma'amala don Haruffa 54 Masu Canza Irabi a Al-Ƙur'ani";
        if (elements.docTitle) elements.docTitle.textContent = "Ƙamus ɗin Harf 'Amil | Al-Ƙur'ani";
      } else if (state.lang === 'pt') {
        elements.brandTitle.innerHTML = "Dicionário de <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Dicionário Interativo de 6 Formas e 54 Partículas Operativas do Alcorão";
        if (elements.docTitle) elements.docTitle.textContent = "Dicionário de Harf 'Amil | Alcorão";
      } else if (state.lang === 'tr') {
        elements.brandTitle.innerHTML = "Kur'an <span>Âmil Harfler</span> Sözlüğü";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "İnteraktif 6 Kategori ve 54 Âmil Harf Rehberi";
        if (elements.docTitle) elements.docTitle.textContent = "Âmil Harfler Sözlüğü | Kur'an-ı Kerim";
      } else if (state.lang === 'nl') {
        elements.brandTitle.innerHTML = "Woordenboek <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interactief Woordenboek voor 6 Vormen en 54 Werkzame Partikels van de Koran";
        if (elements.docTitle) elements.docTitle.textContent = "Woordenboek Harf 'Amil | Referentie van Koranpartikels";
      } else if (state.lang === 'it') {
        elements.brandTitle.innerHTML = "Dizionario di <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Dizionario Interattivo di 6 Forme e 54 Particelle Operative del Corano";
        if (elements.docTitle) elements.docTitle.textContent = "Dizionario di Harf 'Amil | Riferimenti Coranici";
      } else if (state.lang === 'bs') {
        elements.brandTitle.innerHTML = "Rječnik <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktivni rječnik za 6 oblika i 54 operativne čestice u Kur'anu";
        if (elements.docTitle) elements.docTitle.textContent = "Rječnik Harf 'Amil | Kur'anske čestice";
      } else if (state.lang === 'ber') {
        elements.brandTitle.innerHTML = "Asegzawal <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Asegzawal n 6 n talɣiwin d 54 n tseddariyin n Leqran";
        if (elements.docTitle) elements.docTitle.textContent = "Asegzawal Harf 'Amil | Leqran";
      } else if (state.lang === 'az') {
        elements.brandTitle.innerHTML = "Lüğət <span>Hərfi Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Qurani-Kərimdə 6 kateqoriya və 54 amil hərfin izahlı lüğəti";
        if (elements.docTitle) elements.docTitle.textContent = "Hərfi Amil Lüğəti | Qurani-Kərim";
      } else if (state.lang === 'bg') {
        elements.brandTitle.innerHTML = "Речник <span>Харф Амил</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Интерактивен речник за 6 форми и 54 управляващи частици в Корана";
        if (elements.docTitle) elements.docTitle.textContent = "Речник Харф Амил | Свещеният Коран";
      } else if (state.lang === 'am') {
        elements.brandTitle.innerHTML = "የ<span>ሐርፈ ዓሚል</span> መዝገበ-ቃላት";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "በቁርኣን ውስጥ የ6 ቅርጾችና የ54 ሰሪ ቅንጣቶች መመሪያ";
        if (elements.docTitle) elements.docTitle.textContent = "የሐርፈ ዓሚል መዝገበ-ቃላት | ቅዱስ ቁርኣን";
      } else if (state.lang === 'cs') {
        elements.brandTitle.innerHTML = "Slovník <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktivní slovník pro 6 forem a 54 řídících částic v Koránu";
        if (elements.docTitle) elements.docTitle.textContent = "Slovník Harf 'Amil | Svatý Korán";
      } else if (state.lang === 'dv') {
        elements.brandTitle.innerHTML = "ރަދީފު <span>ޙަރްފު ޢާމިލް</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "ކީރިތި ޤުރްއާނުގެ 6 ބާވަތާއި 54 ޢާމިލް އަކުރުގެ ރަދީފު";
        if (elements.docTitle) elements.docTitle.textContent = "ޙަރްފު ޢާމިލް ރަދީފު | ކީރިތި ޤުރްއާން";
      } else if (state.lang === 'no') {
        elements.brandTitle.innerHTML = "Ordbok <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktiv ordbok for 6 former og 54 styrende partikler i Koranen";
        if (elements.docTitle) elements.docTitle.textContent = "Ordbok Harf 'Amil | Den Hellige Koranen";
      } else if (state.lang === 'pl') {
        elements.brandTitle.innerHTML = "Słownik <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktywny słownik 6 form i 54 zarządzających partykuł w Koranie";
        if (elements.docTitle) elements.docTitle.textContent = "Słownik Harf 'Amil | Święty Koran";
      } else if (state.lang === 'ro') {
        elements.brandTitle.innerHTML = "Dicționar <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Dicționar interactiv pentru 6 forme și 54 de particule operative din Coran";
        if (elements.docTitle) elements.docTitle.textContent = "Dicționar Harf 'Amil | Coranul cel Sfânt";
      } else if (state.lang === 'sv') {
        elements.brandTitle.innerHTML = "Ordbok <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktiv ordbok för 6 former och 54 styrande partiklar i Koranen";
        if (elements.docTitle) elements.docTitle.textContent = "Ordbok Harf 'Amil | Den Heliga Koranen";
      } else if (state.lang === 'tg') {
        elements.brandTitle.innerHTML = "Луғати <span>Ҳарфҳои Омил</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Луғати интерактивии 6 гурӯҳ ва 54 ҳарфи омил дар Қуръон";
        if (elements.docTitle) elements.docTitle.textContent = "Луғати Ҳарфҳои Омил | Қуръони Карим";
      } else if (state.lang === 'ta') {
        elements.brandTitle.innerHTML = "அகராதி <span>ஹர்ஃப் ஆமில்</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "திருக்குர்ஆனின் 6 வகைகள் மற்றும் 54 செயல்படும் இடைச்சொற்களின் அகராதி";
        if (elements.docTitle) elements.docTitle.textContent = "ஹர்ஃப் ஆமில் அகராதி | புனித குர்ஆன்";
      } else if (state.lang === 'tt') {
        elements.brandTitle.innerHTML = "Сүзлек <span>Гамил Хәрефләр</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Коръәни Кәримнең 6 төре һәм 54 гамил кисәкчәсе сүзлеге";
        if (elements.docTitle) elements.docTitle.textContent = "Гамил Хәрефләр сүзлеге | Коръәни Кәрим";
      } else if (state.lang === 'ug') {
        elements.brandTitle.innerHTML = "لۇغەت <span>ئامىل ھەرپلەر</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "قۇرئاندىكى 6 تۈر ۋە 54 تەسىرلىك يۈكلىمىنىڭ لۇغىتى";
        if (elements.docTitle) elements.docTitle.textContent = "ئامىل ھەرپلەر لۇغىتى | قۇرئانى كەرىم";
      } else if (state.lang === 'uz') {
        elements.brandTitle.innerHTML = "Lug'at <span>Omil Harflar</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Qur'ondagi 6 tur va 54 ta amalli yuklamalar lug'ati";
        if (elements.docTitle) elements.docTitle.textContent = "Omil Harflar lug'ati | Qur'oni Karim";
      } else if (state.lang === 'ku') {
        elements.brandTitle.innerHTML = "فەرهەنگی <span>پیتە کارلێکەرەکان</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "فەرهەنگی 6 جۆر و 54 پیت و ئامرازی کارلێکەر لە قورئاندا";
        if (elements.docTitle) elements.docTitle.textContent = "فەرهەنگی پیتە کارلێکەرەکان | قورئانی پیرۆز";
      } else if (state.lang === 'th') {
        elements.brandTitle.innerHTML = "พจนานุกรม <span>ฮัรฟ์อามิล</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "พจนานุกรมคำศัพท์ 6 รูปแบบและ 54 ตัวอักษรออกฤทธิ์ในอัลกุรอาน";
        if (elements.docTitle) elements.docTitle.textContent = "พจนานุกรมฮัรฟ์อามิล | อายะฮ์อ้างอิงอัลกุรอาน";
      } else if (state.lang === 'sq') {
        elements.brandTitle.innerHTML = "Fjalori i <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Fjalor interaktiv për 6 forma dhe 54 pjesëza vepruese kur'anore";
        if (elements.docTitle) elements.docTitle.textContent = "Fjalori i Harf 'Amil | Pjesëzat kur'anore";
      } else if (state.lang === 'en') {
        elements.brandTitle.innerHTML = "Dictionary of <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interactive Dictionary of 6 Forms & 54 Operative Quranic Particles";
        if (elements.docTitle) elements.docTitle.textContent = "Dictionary of Harf 'Amil | Quranic Particles";
      } else if (state.lang === 'ur') {
        elements.brandTitle.innerHTML = "لغت <span>حروف عاملہ</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "قرآن کریم کے ۶ اشکال اور ۵۴ حروف عاملہ کی تعاملی لغت";
        if (elements.docTitle) elements.docTitle.textContent = "لغت حروف عاملہ | قرآن کریم کے حروف";
      } else if (state.lang === 'hi') {
        elements.brandTitle.innerHTML = "शब्दकोश <span>हर्फ़ 'आमिल</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "कुरआन के ६ रूपों और ५४ प्रभावी अव्यय शब्दों का संваदात्मक शब्दकोश";
        if (elements.docTitle) elements.docTitle.textContent = "हर्फ़ 'आमिल शब्दकोश | पवित्र कुरआन";
      } else if (state.lang === 'bn') {
        elements.brandTitle.innerHTML = "অভিধান <span>হরূফে আমেল</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "কুরআনের ৬টি রূপ ও ৫৪টি আমলকারী হরফের ইন্টারঅ্যাক্টিভ অভিধান";
        if (elements.docTitle) elements.docTitle.textContent = "হরূফে আমেল অভিধান | পবিত্র কুরআন";
      } else if (state.lang === 'ru') {
        elements.brandTitle.innerHTML = "Словарь <span>Харф Амиль</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Интерактивный словарь 6 форм и 54 управляющих частиц Корана";
        if (elements.docTitle) elements.docTitle.textContent = "Словарь Харф Амиль | Священный Коран";
      } else if (state.lang === 'zh') {
        elements.brandTitle.innerHTML = "<span>作用虚词</span> 词典 (Harf 'Amil)";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "《古兰经》6种形态与54个具语法作用虚词互动词典";
        if (elements.docTitle) elements.docTitle.textContent = "作用虚词词典 | 古兰经互动参考";
      } else if (state.lang === 'fr') {
        elements.brandTitle.innerHTML = "Dictionnaire de <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Dictionnaire Interactif de 6 Formes et 54 Particules Régissantes du Coran";
        if (elements.docTitle) elements.docTitle.textContent = "Dictionnaire de Harf 'Amil | Particules Régissantes du Coran";
      } else if (state.lang === 'de') {
        elements.brandTitle.innerHTML = "Wörterbuch <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interaktives Wörterbuch für 6 Formen und 54 regierende Partikeln des Korans";
        if (elements.docTitle) elements.docTitle.textContent = "Wörterbuch Harf 'Amil | Koranpartikeln";
      } else if (state.lang === 'es') {
        elements.brandTitle.innerHTML = "Diccionario de <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Diccionario Interactivo de 6 Formas y 54 Partículas Operativas del Corán";
        if (elements.docTitle) elements.docTitle.textContent = "Diccionario de Harf 'Amil | Partículas del Corán";
      } else {
        elements.brandTitle.innerHTML = "Kamus <span>Harf 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Kamus Interaktif 6 Bentuk Harf & 54 Kata Al-Qur'an";
        if (elements.docTitle) elements.docTitle.textContent = "Kamus Harf 'Amil | Rujukan Ayat Interaktif Al-Qur'an";
      }
    } else """

target_update_header = """  function updateHeaderTitles() {
    if (!elements.brandTitle) return;
    
    if (state.activeDict === 'harf') {"""

if target_update_header in content:
    content = content.replace(target_update_header, f"""  function updateHeaderTitles() {{
    if (!elements.brandTitle) return;
    
{harf_amil_headers_code}if (state.activeDict === 'harf') {{""")
    print("[OK] Updated updateHeaderTitles with Harf 'Amil multilingual titles")
else:
    print("[WARN] Could not find target_update_header")

# 4. Update initData to support HARF_AMIL_DATA
old_init_data = """  // Parse Raw Dataset into Organized Groupings
  function initData() {
    let rawDataset = [];
    if (state.activeDict === 'harf' && typeof HARF_DATA !== 'undefined') {
      rawDataset = HARF_DATA;
    } else if (typeof DHAMIR_DATA !== 'undefined') {
      rawDataset = DHAMIR_DATA;
    }"""

new_init_data = """  // Parse Raw Dataset into Organized Groupings
  function initData() {
    let rawDataset = [];
    if (state.activeDict === 'harf_amil' && typeof HARF_AMIL_DATA !== 'undefined') {
      rawDataset = HARF_AMIL_DATA;
    } else if (state.activeDict === 'harf' && typeof HARF_DATA !== 'undefined') {
      rawDataset = HARF_DATA;
    } else if (typeof DHAMIR_DATA !== 'undefined') {
      rawDataset = DHAMIR_DATA;
    }"""

if old_init_data in content:
    content = content.replace(old_init_data, new_init_data)
    print("[OK] Updated initData with HARF_AMIL_DATA")
else:
    print("[WARN] Could not find old_init_data")

# 5. Update populateBentukDropdown to support HARF_AMIL_BENTUK_LABELS
old_populate_bentuk = """    function getBentukLabelText(b) {
      if (state.activeDict === 'harf' && typeof HARF_BENTUK_LABELS !== 'undefined' && HARF_BENTUK_LABELS[b]) {
        return HARF_BENTUK_LABELS[b][state.lang] || HARF_BENTUK_LABELS[b]['id'] || b;
      }"""

new_populate_bentuk = """    function getBentukLabelText(b) {
      if (state.activeDict === 'harf_amil' && typeof HARF_AMIL_BENTUK_LABELS !== 'undefined' && HARF_AMIL_BENTUK_LABELS[b]) {
        return HARF_AMIL_BENTUK_LABELS[b][state.lang] || HARF_AMIL_BENTUK_LABELS[b]['id'] || b;
      }
      if (state.activeDict === 'harf' && typeof HARF_BENTUK_LABELS !== 'undefined' && HARF_BENTUK_LABELS[b]) {
        return HARF_BENTUK_LABELS[b][state.lang] || HARF_BENTUK_LABELS[b]['id'] || b;
      }"""

if old_populate_bentuk in content:
    content = content.replace(old_populate_bentuk, new_populate_bentuk)
    print("[OK] Updated populateBentukDropdown for Harf 'Amil")
else:
    print("[WARN] Could not find old_populate_bentuk")

# 6. Update ARABIC_SPECIAL_EXPANSIONS
harf_amil_expansions_code = """    // Harf 'Amil Special Word Expansions
    'مِنْ': ['من', 'ومن', 'فمن', 'لمن', 'بمن', 'عمن', 'ممن'],
    'فِي': ['في', 'وفي', 'ففي', 'لفي', 'وفيه', 'فيهم', 'فيها', 'فينا', 'فيكم', 'فيك', 'فيكما', 'فيهما'],
    'عَلَىٰ': ['علي', 'وعلي', 'فعلي', 'لعلي', 'عليه', 'عليهم', 'عليها', 'علينا', 'عليكم', 'عليك', 'عليهما'],
    'إِلَىٰ': ['الي', 'والي', 'فالي', 'اليه', 'اليهم', 'اليها', 'الينا', 'اليكم', 'اليك', 'اليهما'],
    'عَنْ': ['عن', 'وعن', 'فعن', 'عنه', 'عنهم', 'عنها', 'عنا', 'عنكم', 'عنك', 'عنهما'],
    'مِمَّا': ['مما', 'ومما', 'فمما'],
    'عَمَّا 1': ['عما', 'وعما', 'فعما'],
    'عَمَّا 2': ['عما', 'وعما', 'فعما'],
    'عَمَّ': ['عم', 'وعم', 'فعم'],
    'مِمَّن': ['ممن', 'وممن', 'فممن'],
    'مِمَّ': ['مم', 'ومم', 'فمم'],
    'فِيمَا': ['فيما', 'وفيما', 'ففيما'],
    'فِيمَ': ['فيم', 'وفيم', 'ففيم'],
    'حَتَّىٰ 3': ['حتي', 'وحتي', 'فحتي'],
    'حَتَّىٰ 1': ['حتي', 'وحتي', 'فحتي'],
    'حَتَّىٰ': ['حتي', 'وحتي', 'فحتي'],
    'رُّبَمَا': ['ربما', 'وربما', 'فربما'],
    'أَنْ 1': ['ان', 'وان', 'فان', 'بان', 'لان', 'ابان', 'فبان'],
    'أَنْ': ['ان', 'وان', 'فان', 'بان', 'لان'],
    'لَنْ': ['لن', 'ولن', 'فلن'],
    'كَيْ': ['كي', 'وكي', 'فكي', 'لكي', 'ولكي', 'فلكي'],
    'كَيۡلَا': ['كيلا', 'لكيلا', 'ولكيلا', 'فلكيلا'],
    'إِنْ 1': ['ان', 'وان', 'فان', 'ولئن', 'لئن', 'افان'],
    'إِنْ': ['ان', 'وان', 'فان', 'ولئن', 'لئن'],
    'لاَ 2': ['لا', 'ولا', 'فلا'],
    'لاَ': ['لا', 'ولا', 'فلا'],
    'لَمۡ': ['لم', 'ولم', 'فلم', 'الم', 'افلم', 'اولم'],
    'لَّمَّا 2': ['لما', 'ولما', 'فلما'],
    'لَّمَّا': ['لما', 'ولما', 'فلما'],
    'إِلَّا 1': ['الا', 'والا', 'فالا'],
    'إِلَّا 2': ['الا', 'والا', 'فالا'],
    'إِلَّا': ['الا', 'والا', 'فالا'],
    'إِلَّمۡ': ['الم', 'فالم', 'والا', 'فان لم', 'فالم'],
    'ثُمَّ': ['ثم', 'وثم', 'فثم'],
    'أَوْ': ['او', 'واو', 'فاو'],
    'بَلْ': ['بل', 'وبل', 'فبل'],
    'أَمْ': ['ام', 'وام', 'فام'],
    'لَٰكِنْ': ['لكن', 'ولكن', 'فلكن'],
    'إِمَّا 2': ['اما', 'واما', 'فاما'],
    'إِمَّا': ['اما', 'واما', 'فاما'],
    'أَمَّن 1': ['امن', 'وامن', 'فامن'],
    'أَمَّن 2': ['امن', 'وامن', 'فامن'],
    'أَمَّا': ['اما', 'واما', 'فاما'],
    'أَمَّاذَا': ['اماذا', 'واماذا', 'فاماذا'],
    'لَكِنْ أنا': ['لكنا', 'ولكنا', 'لكن انا', 'ولكن انا', 'لكن'],
    'إِنَّ': ['ان', 'وان', 'فان', 'لان', 'وانك', 'وانكم', 'واني', 'وانا', 'وانه', 'وانهم', 'وانهن', 'وانها', 'واننا'],
    'أَنَّ': ['ان', 'وان', 'فان', 'بان', 'لان', 'وانك', 'وانكم', 'واني', 'وانا', 'وانه', 'وانهم', 'وانهن', 'وانها', 'واننا', 'بانه', 'بانهم', 'بانكم'],
    'إِنَّمَا 1': ['انما', 'وانما', 'فانما'],
    'إِنَّمَا 2': ['انما', 'وانما', 'فانما'],
    'لَعَلَّ': ['لعل', 'ولعل', 'فلعل', 'لعله', 'لعلهم', 'لعلكم', 'لعلي', 'لعلنا', 'لعلها'],
    'لَكِنَّ': ['لكن', 'ولكن', 'فلكن', 'ولكنه', 'ولكنهم', 'ولكنكم', 'ولكني', 'ولكننا', 'ولكنها', 'ولكنهن'],
    'كَأَنَّ': ['كان', 'وكان', 'فكان', 'كانه', 'كانهم', 'كانك', 'كانكم', 'كانها', 'كاني', 'كاننا'],
    'لَيْتَ': ['ليت', 'وليت', 'فليت', 'ياليت', 'يا ليت', 'ياليتني', 'ياليتها', 'ياليتنا', 'ياليتهم', 'ياليت قومي'],
    'أَنَّمَا 1': ['انما', 'وانما', 'فانما', 'بانما'],
    'أَنَّمَا 2': ['انما', 'وانما', 'فانما', 'بانما', 'ان', 'ما'],
    'كَأَنَّمَا': ['كانما', 'وكانما', 'فكانما'],
    'أَلَّا 3': ['الا', 'والا', 'فالا', 'ان لا', 'وان لا'],
    'أَلَّا 4': ['الا', 'والا', 'فالا', 'ان لا', 'وان لا'],
    'أَلَّن': ['الن', 'والن', 'فلن', 'ان لن', 'وان لن'],
    'وَيۡكَأَنَّ': ['ويكان', 'فويكان', 'ويكانه', 'ويكانه لا'],
    'أَلَّو': ['الو', 'لو', 'ان', 'وان لو', 'وان لو استقاموا', 'والو'],"""

old_arabic_expansions_start = "  const ARABIC_SPECIAL_EXPANSIONS = {"
if old_arabic_expansions_start in content:
    content = content.replace(old_arabic_expansions_start, f"{old_arabic_expansions_start}\n{harf_amil_expansions_code}")
    print("[OK] Merged ARABIC_SPECIAL_EXPANSIONS for Harf 'Amil")
else:
    print("[WARN] Could not find ARABIC_SPECIAL_EXPANSIONS")

# 7. Update updateLanguageUI for tab labels
old_tab_badges = """    if (elements.labelTabJamid) elements.labelTabJamid.textContent = t('brandTitle').replace(/<[^>]*>/g, '');
    if (elements.badgeTabJamid) elements.badgeTabJamid.textContent = t('tabBadgeJamid') || '7 Bentuk Kata';
    if (elements.badgeTabHarf) elements.badgeTabHarf.textContent = t('tabBadgeHarf') || '17 Bentuk Harf';"""

new_tab_badges = """    if (elements.labelTabJamid) elements.labelTabJamid.textContent = t('brandTitle').replace(/<[^>]*>/g, '');
    if (elements.badgeTabJamid) elements.badgeTabJamid.textContent = t('tabBadgeJamid') || '7 Bentuk Kata';
    if (elements.labelTabHarf) elements.labelTabHarf.textContent = (state.lang === 'en' ? "Harf Ghair 'Amil" : (state.lang === 'tr' ? "Gayr-i Âmil Harfler" : "Kamus Harf Ghair 'Amil"));
    if (elements.badgeTabHarf) elements.badgeTabHarf.textContent = t('tabBadgeHarf') || '17 Bentuk Harf';
    if (elements.labelTabHarfAmil) elements.labelTabHarfAmil.textContent = (state.lang === 'en' ? "Harf 'Amil Dictionary" : (state.lang === 'tr' ? "Âmil Harfler" : "Kamus Harf 'Amil"));
    if (elements.badgeTabHarfAmil) elements.badgeTabHarfAmil.textContent = (state.lang === 'en' ? '6 Categories' : (state.lang === 'tr' ? '6 Kategori' : '6 Bentuk Harf'));"""

if old_tab_badges in content:
    content = content.replace(old_tab_badges, new_tab_badges)
    print("[OK] Updated updateLanguageUI tab badges")
else:
    print("[WARN] Could not find old_tab_badges")

# 8. Update Event Listeners: add tabDictHarfAmil click listener
old_listeners = """    if (elements.tabDictHarf) {
      elements.tabDictHarf.addEventListener('click', () => {
        switchDictionary('harf');
      });
    }"""

new_listeners = """    if (elements.tabDictHarf) {
      elements.tabDictHarf.addEventListener('click', () => {
        switchDictionary('harf');
      });
    }
    if (elements.tabDictHarfAmil) {
      elements.tabDictHarfAmil.addEventListener('click', () => {
        switchDictionary('harf_amil');
      });
    }"""

if old_listeners in content:
    content = content.replace(old_listeners, new_listeners)
    print("[OK] Added event listener for tabDictHarfAmil")
else:
    print("[WARN] Could not find old_listeners")

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nSuccessfully patched {app_js_path}!")
