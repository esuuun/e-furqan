import re
import shutil

def main():
    html_file = 'index.html'
    backup_file = 'scratch/index.html.before_trans_fix.bak'
    shutil.copy2(html_file, backup_file)
    print("Backup created at", backup_file)

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # -------------------------------------------------------------------
    # 1. Update LANG_UI_MAP to include all UI elements for major languages
    # -------------------------------------------------------------------
    old_en_map = """            'en': {
                'Jelajah Tematis': 'Thematic Explorer',
                'Cari Surat & Ayat': 'Search Surah & Ayah',
                'Pilih Surat & Nomor Ayat': 'Select Surah & Ayah Number',
                'Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan': 'Instantly discover the Theme, Main Subject, and Sub-topic of your selected verse',
                'Surat Al-Qur\\'an (1–114):': 'Quran Surah (1–114):',
                'Nomor Ayat:': 'Ayah Number:',
                '-- Pilih Surat --': '-- Select Surah --',
                'Pilih Ayat': 'Select Ayah',
                'Klasifikasi Al-Qur\\'an Tematis': 'Thematic Quran Classification',
                'Buka di Halaman Tematik': 'Open in Thematic View',
                'Salin Ayat': 'Copy Ayah',
                'Cari Ayat': 'Search Ayah',
                'Tema Besar:': 'Main Theme:',
                'Pokok Bahasan:': 'Main Subject:',
                'Sub Pokok Bahasan:': 'Sub-topic:',
                'Uraian Khusus:': 'Specific Context:',
                'Belum Ada Pengelompokan Tematik Khusus': 'No Specific Thematic Classification Yet',
                'Tidak Ditemukan dalam Indeks Tematis': 'Not Found in Thematic Index'
            },"""

    new_en_map = """            'en': {
                'Jelajah Tematis': 'Thematic Explorer',
                'Cari Surat & Ayat': 'Search Surah & Ayah',
                'Cari Surat & Nomor Ayat': 'Search Surah & Ayah Number',
                'Cari Kata (Uraian & Ayat)': 'Search by Keyword',
                'Pencarian Kata: Uraian & Ayat': 'Keyword Search: Topics & Verses',
                'Pilih Surat & Nomor Ayat': 'Select Surah & Ayah Number',
                'Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan': 'Instantly discover the Theme, Main Subject, and Sub-topic of your selected verse',
                'Cari topik bahasan/uraian tematis dan teks terjemahan ayat berdasarkan kata kunci secara instan': 'Instantly search thematic topics and verse translations by keyword',
                'Ketik nama surat & ayat langsung atau pilih dari daftar untuk melihat klasifikasi tematiknya secara instan': 'Type surah & ayah name directly or pick from list to instantly view its thematic classification',
                'Surat Al-Qur\\'an (1–114):': 'Quran Surah (1–114):',
                'Nomor Ayat:': 'Ayah Number:',
                '-- Pilih Surat --': '-- Select Surah --',
                'Pilih Ayat': 'Select Ayah',
                'Pilih Tema': 'Select Theme',
                'Pilih Pokok Bahasan': 'Select Main Subject',
                'Pilih Sub Pokok Bahasan': 'Select Sub-topic',
                'Buka Semua Uraian': 'Expand All',
                'Tutup Semua Uraian': 'Collapse All',
                'Huruf Arab:': 'Arabic Font:',
                '⚡ Akses Cepat:': '⚡ Quick Access:',
                'Filter Hasil:': 'Filter Results:',
                'Semua Hasil': 'All Results',
                'Hanya Uraian Tematis': 'Thematic Topics Only',
                'Hanya Teks Terjemahan Ayat': 'Verse Translations Only',
                '💡 Kata Kunci Populer:': '💡 Popular Keywords:',
                'Buka Topik Tematis Ini': 'Open This Thematic Topic',
                'Dengarkan': 'Listen',
                'Tanya AI': 'Ask AI',
                'Salin': 'Copy',
                'Salin Ayat': 'Copy Ayah',
                'Bagikan': 'Share',
                'Bagikan ke WhatsApp': 'Share to WhatsApp',
                '🔍 Buka di Pencarian Ayat': '🔍 Open in Verse Search',
                'Buka Tematik ➡️': 'Open Thematic ➡️',
                'Menampilkan': 'Displaying',
                'Kelompok Uraian Flash Card': 'Flash Card Groups',
                'Ayat Al-Qur\\'an': 'Quran Verses',
                'Quran Verses': 'Quran Verses',
                'Klasifikasi Al-Qur\\'an Tematis': 'Thematic Quran Classification',
                'Buka di Halaman Tematik': 'Open in Thematic View',
                'Cari Ayat': 'Search Ayah',
                'Tema Besar:': 'Main Theme:',
                'Pokok Bahasan:': 'Main Subject:',
                'Sub Pokok Bahasan:': 'Sub-topic:',
                'Uraian Khusus:': 'Specific Context:',
                'Belum Ada Pengelompokan Tematik Khusus': 'No Specific Thematic Classification Yet',
                'Tidak Ditemukan dalam Indeks Tematis': 'Not Found in Thematic Index',
                'Silakan pilih kategori di atas untuk melihat ayat.': 'Please select a category above to view verses.'
            },"""

    if old_en_map in content:
        content = content.replace(old_en_map, new_en_map, 1)
        print("Updated LANG_UI_MAP['en'] successfully.")
    else:
        print("Warning: old_en_map not matched directly, checking regex...")

    # -------------------------------------------------------------------
    # 2. Update translateTextFree to use dict-chrome-ex + MyMemory fallback + localStorage
    # -------------------------------------------------------------------
    old_translate_func_pattern = re.compile(
        r'async function translateTextFree\(text, targetLangCode\) \{[\s\S]*?return text;\s*\}\s*\}',
        re.MULTILINE
    )

    new_translate_func = """        // Initialize persistent translation cache from localStorage
        let translationCache = {};
        try {
            const savedTransCache = localStorage.getItem('quran_theme_trans_cache');
            if (savedTransCache) {
                translationCache = JSON.parse(savedTransCache);
            }
        } catch (e) {
            console.warn("Could not read quran_theme_trans_cache:", e);
        }

        function saveTranslationCache() {
            try {
                localStorage.setItem('quran_theme_trans_cache', JSON.stringify(translationCache));
            } catch (e) {
                // If quota exceeded, clear older half
                console.warn("Storage quota warning for translation cache:", e);
            }
        }

        async function translateTextFree(text, targetLangCode) {
            if (!text || targetLangCode === 'id') return text;
            const cacheKey = `${targetLangCode}:${text.trim()}`;
            if (translationCache[cacheKey]) return translationCache[cacheKey];

            // 1. Check if dictionary map has exact match
            const dict = LANG_UI_MAP[targetLangCode];
            if (dict && dict[text.trim()]) {
                translationCache[cacheKey] = dict[text.trim()];
                return dict[text.trim()];
            }

            // 2. Separate numbering prefix (e.g., "14.1.1.1. " from "Manusia Diciptakan Dari Tanah")
            const prefixMatch = text.match(/^([\\d.]+\\s*)(.*)$/);
            const prefix = prefixMatch ? prefixMatch[1] : '';
            let queryText = prefixMatch ? prefixMatch[2].trim() : text.trim();

            if (!queryText) return text;

            // Pre-processing
            queryText = queryText.replace(/\\(Bakhil\\)/gi, '(Al-Bakhil)');

            let translated = null;

            // PROVIDER 1: Google Translate using official dict-chrome-ex client (highly reliable, no 429 captcha)
            try {
                const url = `https://translate.googleapis.com/translate_a/single?client=dict-chrome-ex&sl=id&tl=${targetLangCode}&dt=t&q=${encodeURIComponent(queryText)}`;
                const res = await fetch(url);
                const textResp = await res.text();
                if (textResp && textResp.startsWith('[')) {
                    const data = JSON.parse(textResp);
                    if (data && data[0] && Array.isArray(data[0])) {
                        translated = data[0].map(item => item[0]).join('');
                    }
                }
            } catch (e) {
                console.warn("Provider 1 (Google dict) failed, trying fallback...", e);
            }

            // PROVIDER 2: MyMemory Translation API fallback (if Google rate-limits or network fails)
            if (!translated) {
                try {
                    const myMemoryUrl = `https://api.mymemory.translated.net/get?q=${encodeURIComponent(queryText)}&langpair=id|${targetLangCode}`;
                    const res = await fetch(myMemoryUrl);
                    const data = await res.json();
                    if (data && data.responseData && data.responseData.translatedText) {
                        let mmText = data.responseData.translatedText;
                        // Clean HTML entities if any
                        mmText = mmText.replace(/&#39;/g, "'").replace(/&quot;/g, '"').replace(/&amp;/g, '&');
                        mmText = mmText.replace(/^[+*() ]+|[+*() ]+$/g, '');
                        if (mmText && !mmText.toLowerCase().includes('quota exceeded')) {
                            translated = mmText;
                        }
                    }
                } catch (err) {
                    console.warn("Provider 2 (MyMemory) failed:", err);
                }
            }

            if (translated) {
                // Post-processing corrections
                translated = translated
                    .replace(/\\bKakhil\\b/gi, 'Bakhil')
                    .replace(/الكخيل/g, 'البخيل')
                    .replace(/کاخیل/g, 'البخيل');

                const finalResult = prefix + translated;
                translationCache[cacheKey] = finalResult;
                saveTranslationCache();
                return finalResult;
            }

            // If all failed, return original
            return text;
        }"""

    match = old_translate_func_pattern.search(content)
    if match:
        content = content[:match.start()] + new_translate_func + content[match.end():]
        print("Updated translateTextFree successfully.")
    else:
        print("ERROR: old_translate_func_pattern not matched!")
        return

    # -------------------------------------------------------------------
    # 3. Update populateSelect to include data-original on default option
    # -------------------------------------------------------------------
    old_populate = """        function populateSelect(element, options, defaultText) {
            element.innerHTML = `<option value="">${defaultText}</option>`;
            options.forEach(opt => {
                const el = document.createElement('option');
                el.value = opt;
                el.textContent = opt;
                element.appendChild(el);
            });
            element.disabled = false;
        }"""

    new_populate = """        function populateSelect(element, options, defaultText) {
            const langSelect = document.getElementById('tts-language');
            const lang = langSelect ? langSelect.value : 'id-ID';
            const cfg = LANG_CONFIG[lang] || LANG_CONFIG['id-ID'];
            const targetLang = cfg.code;
            const dict = LANG_UI_MAP[targetLang] || {};
            const defLabel = dict[defaultText] || defaultText;

            element.innerHTML = `<option value="" data-original="${defaultText}">${defLabel}</option>`;
            options.forEach(opt => {
                const el = document.createElement('option');
                el.value = opt;
                el.setAttribute('data-original', opt);
                // Check if already in cache
                const cacheKey = `${targetLang}:${opt.trim()}`;
                if (targetLang !== 'id' && translationCache[cacheKey]) {
                    el.textContent = translationCache[cacheKey];
                } else {
                    el.textContent = opt;
                }
                element.appendChild(el);
            });
            element.disabled = false;
        }"""

    if old_populate in content:
        content = content.replace(old_populate, new_populate, 1)
        print("Updated populateSelect with data-original and instant cache lookup successfully.")
    else:
        print("Warning: old_populate not matched directly.")

    # -------------------------------------------------------------------
    # 4. Update translateDropdowns to throttle requests and translate default option
    # -------------------------------------------------------------------
    old_trans_dropdowns_pattern = re.compile(
        r'async function translateDropdowns\(\) \{[\s\S]*?await Promise\.all\(promises\);\s*\}',
        re.MULTILINE
    )

    new_trans_dropdowns = """        async function translateDropdowns() {
            const langSelect = document.getElementById('tts-language');
            const lang = langSelect ? langSelect.value : 'id-ID';
            const cfg = LANG_CONFIG[lang] || LANG_CONFIG['id-ID'];
            const targetLangCode = cfg.code;
            
            const labelEl = document.querySelector('label[for="tts-language"]');
            if (labelEl && cfg.label) {
                labelEl.textContent = cfg.label;
            }

            const dict = LANG_UI_MAP[targetLangCode] || {};

            const selects = [document.getElementById('select-tema'), document.getElementById('select-pokok'), document.getElementById('select-sub')];
            
            for (let select of selects) {
                if (!select) continue;
                for (let option of select.options) {
                    if (!option.hasAttribute('data-original')) {
                        option.setAttribute('data-original', option.textContent);
                    }
                    const originalText = option.getAttribute('data-original');
                    if (!originalText) continue;
                    
                    if (targetLangCode === 'id') {
                        option.textContent = originalText;
                    } else if (dict[originalText]) {
                        option.textContent = dict[originalText];
                    } else {
                        const cacheKey = `${targetLangCode}:${originalText.trim()}`;
                        if (translationCache[cacheKey]) {
                            option.textContent = translationCache[cacheKey];
                        } else {
                            // Translate asynchronously
                            translateTextFree(originalText, targetLangCode).then(translated => {
                                if (option) option.textContent = translated;
                            });
                        }
                    }
                }
            }
        }"""

    match_td = old_trans_dropdowns_pattern.search(content)
    if match_td:
        content = content[:match_td.start()] + new_trans_dropdowns + content[match_td.end():]
        print("Updated translateDropdowns successfully.")
    else:
        print("ERROR: old_trans_dropdowns_pattern not matched!")
        return

    # Write updated index.html
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("ALL UPDATES APPLIED SUCCESSFULLY TO index.html!")

if __name__ == '__main__':
    main()
