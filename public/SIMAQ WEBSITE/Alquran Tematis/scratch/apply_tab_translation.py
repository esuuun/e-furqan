import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Mode Tabs HTML with data-i18n-orig
old_tabs_html = """        <!-- Mode Navigation Tabs -->
        <div class="mode-nav-tabs">
            <button id="tab-btn-thematic" class="mode-tab-btn active" onclick="switchMainMode('thematic')">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                <span>Jelajah Tematis</span>
            </button>
            <button id="tab-btn-search" class="mode-tab-btn" onclick="switchMainMode('search')">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                <span>Cari Surat & Ayat</span>
            </button>
        </div>"""

new_tabs_html = """        <!-- Mode Navigation Tabs -->
        <div class="mode-nav-tabs">
            <button id="tab-btn-thematic" class="mode-tab-btn active" onclick="switchMainMode('thematic')">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                <span id="tab-text-thematic" data-i18n-orig="Jelajah Tematis">Jelajah Tematis</span>
            </button>
            <button id="tab-btn-search" class="mode-tab-btn" onclick="switchMainMode('search')">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                <span id="tab-text-search" data-i18n-orig="Cari Surat & Ayat">Cari Surat & Ayat</span>
            </button>
        </div>"""

if old_tabs_html in html:
    html = html.replace(old_tabs_html, new_tabs_html)
    print("Updated Mode Tabs HTML with data-i18n-orig.")
else:
    print("Old tabs HTML not found directly.")

# 2. Update Search Console Header & Labels with data-i18n-orig
old_console_html = """            <div class="search-console-header">
                <div class="search-console-title">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                    <span>Pilih Surat & Nomor Ayat</span>
                </div>
                <div class="search-console-subtitle">Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan</div>
            </div>

            <div class="search-controls-row">
                <div class="search-field-group surah-field">
                    <label for="select-search-surah">Surat Al-Qur'an (1–114):</label>
                    <select id="select-search-surah" class="custom-select search-select" onchange="onSearchSurahChange()">
                        <option value="">-- Pilih Surat --</option>
                    </select>
                </div>

                <div class="search-field-group ayat-field">
                    <label for="select-search-ayat">Nomor Ayat:</label>"""

new_console_html = """            <div class="search-console-header">
                <div class="search-console-title">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                    <span data-i18n-orig="Pilih Surat & Nomor Ayat">Pilih Surat & Nomor Ayat</span>
                </div>
                <div class="search-console-subtitle" data-i18n-orig="Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan">Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan</div>
            </div>

            <div class="search-controls-row">
                <div class="search-field-group surah-field">
                    <label for="select-search-surah" data-i18n-orig="Surat Al-Qur'an (1–114):">Surat Al-Qur'an (1–114):</label>
                    <select id="select-search-surah" class="custom-select search-select" onchange="onSearchSurahChange()">
                        <option value="" data-i18n-orig="-- Pilih Surat --">-- Pilih Surat --</option>
                    </select>
                </div>

                <div class="search-field-group ayat-field">
                    <label for="select-search-ayat" data-i18n-orig="Nomor Ayat:">Nomor Ayat:</label>"""

if old_console_html in html:
    html = html.replace(old_console_html, new_console_html)
    print("Updated Search Console HTML with data-i18n-orig.")
else:
    print("Old console HTML not found directly.")

# 3. Add LANG_UI_MAP dictionary and update translatePageContent()
ui_map_code = """
        const LANG_UI_MAP = {
            'en': {
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
            },
            'ar': {
                'Jelajah Tematis': 'التصفح الموضوعي',
                'Cari Surat & Ayat': 'البحث بالسورة والآية',
                'Pilih Surat & Nomor Ayat': 'اختر السورة ورقم الآية',
                'Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan': 'تعرف على الموضوع والمحور الرئيسي والفرعي للآية المختارة فوراً',
                'Surat Al-Qur\\'an (1–114):': 'سور القرآن الكريم (1–114):',
                'Nomor Ayat:': 'رقم الآية:',
                '-- Pilih Surat --': '-- اختر السورة --',
                'Pilih Ayat': 'اختر الآية',
                'Klasifikasi Al-Qur\\'an Tematis': 'التصنيف الموضوعي للقرآن الكريم',
                'Buka di Halaman Tematik': 'عرض في الصفحة الموضوعية',
                'Salin Ayat': 'نسخ الآية',
                'Cari Ayat': 'بحث عن الآية',
                'Tema Besar:': 'الموضوع الرئيسي:',
                'Pokok Bahasan:': 'المحور الأساسي:',
                'Sub Pokok Bahasan:': 'المحور الفرعي:',
                'Uraian Khusus:': 'البيان التفصيلي:',
                'Belum Ada Pengelompokan Tematik Khusus': 'لا يوجد تصنيف موضوعي محدد حتى الآن',
                'Tidak Ditemukan dalam Indeks Tematis': 'غير مدرج في الفهرس الموضوعي'
            },
            'ms': {
                'Jelajah Tematis': 'Jelajah Tematik',
                'Cari Surat & Ayat': 'Cari Surah & Ayat',
                'Pilih Surat & Nomor Ayat': 'Pilih Surah & Nombor Ayat',
                'Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan': 'Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat pilihan anda secara pantas',
                'Surat Al-Qur\\'an (1–114):': 'Surah Al-Quran (1–114):',
                'Nomor Ayat:': 'Nombor Ayat:',
                '-- Pilih Surat --': '-- Pilih Surah --',
                'Pilih Ayat': 'Pilih Ayat',
                'Klasifikasi Al-Qur\\'an Tematis': 'Klasifikasi Al-Quran Tematik',
                'Buka di Halaman Tematik': 'Buka di Halaman Tematik',
                'Salin Ayat': 'Salin Ayat',
                'Cari Ayat': 'Cari Ayat',
                'Tema Besar:': 'Tema Utama:',
                'Pokok Bahasan:': 'Pokok Bahasan:',
                'Sub Pokok Bahasan:': 'Sub Pokok Bahasan:',
                'Uraian Khusus:': 'Huraian Khusus:',
                'Belum Ada Pengelompokan Tematik Khusus': 'Belum Ada Pengelompokan Tematik Khusus',
                'Tidak Ditemukan dalam Indeks Tematis': 'Tidak Ditemui dalam Indeks Tematik'
            },
            'ur': {
                'Jelajah Tematis': 'موضوعاتی مطالعہ',
                'Cari Surat & Ayat': 'سورۃ اور آیت تلاش کریں',
                'Pilih Surat & Nomor Ayat': 'سورۃ اور آیت کا نمبر منتخب کریں',
                'Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan': 'اپنی منتخب کردہ آیت کا موضوع، مرکزی اور ذیلی عنوان فوراً جانیں',
                'Surat Al-Qur\\'an (1–114):': 'قرآن کی سورتیں (1–114):',
                'Nomor Ayat:': 'آیت نمبر:',
                '-- Pilih Surat --': '-- سورۃ منتخب کریں --',
                'Pilih Ayat': 'آیت منتخب کریں',
                'Klasifikasi Al-Qur\\'an Tematis': 'قرآنی موضوعاتی درجہ بندی',
                'Buka di Halaman Tematik': 'موضوعاتی صفحہ پر دیکھیں',
                'Salin Ayat': 'آیت کاپی کریں',
                'Cari Ayat': 'آیت تلاش کریں',
                'Tema Besar:': 'مرکزی موضوع:',
                'Pokok Bahasan:': 'بنیادی عنوان:',
                'Sub Pokok Bahasan:': 'ذیلی موضوع:',
                'Uraian Khusus:': 'تفصیلی وضاحت:'
            },
            'tr': {
                'Jelajah Tematis': 'Konusal Gezinti',
                'Cari Surat & Ayat': 'Sure ve Ayet Ara',
                'Pilih Surat & Nomor Ayat': 'Sure ve Ayet Numarası Seçin',
                'Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan': 'Seçtiğiniz ayetin Tema, Ana Konu ve Alt Konularını anında öğrenin',
                'Surat Al-Qur\\'an (1–114):': 'Kur\\'an Sureleri (1–114):',
                'Nomor Ayat:': 'Ayet Numarası:',
                '-- Pilih Surat --': '-- Sure Seçin --',
                'Pilih Ayat': 'Ayet Seçin',
                'Klasifikasi Al-Qur\\'an Tematis': 'Tematik Kur\\'an Sınıflandırması',
                'Buka di Halaman Tematik': 'Tematik Sayfada Aç',
                'Salin Ayat': 'Ayeti Kopyala',
                'Cari Ayat': 'Ayet Ara',
                'Tema Besar:': 'Ana Tema:',
                'Pokok Bahasan:': 'Ana Konu:',
                'Sub Pokok Bahasan:': 'Alt Konu:',
                'Uraian Khusus:': 'Özel Açıklama:'
            },
            'fr': {
                'Jelajah Tematis': 'Exploration thématique',
                'Cari Surat & Ayat': 'Chercher Sourate & Verset',
                'Pilih Surat & Nomor Ayat': 'Sélectionner la sourate et le verset',
                'Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan': 'Découvrez instantanément le thème et les sous-thèmes du verset sélectionné',
                'Surat Al-Qur\\'an (1–114):': 'Sourates du Coran (1–114):',
                'Nomor Ayat:': 'Numéro du verset:',
                '-- Pilih Surat --': '-- Choisir une sourate --',
                'Pilih Ayat': 'Choisir le verset',
                'Klasifikasi Al-Qur\\'an Tematis': 'Classification thématique du Coran',
                'Buka di Halaman Tematik': 'Ouvrir dans la vue thématique',
                'Salin Ayat': 'Copier le verset',
                'Cari Ayat': 'Chercher verset',
                'Tema Besar:': 'Thème principal:',
                'Pokok Bahasan:': 'Sujet principal:',
                'Sub Pokok Bahasan:': 'Sous-thème:',
                'Uraian Khusus:': 'Contexte spécifique:'
            }
        };
"""

if 'const LANG_UI_MAP =' not in html:
    html = html.replace('        let quranData = {};', ui_map_code + '\n        let quranData = {};')
    print("Added LANG_UI_MAP.")

# 4. Update translatePageContent to translate tabs and UI elements
old_translate_end = """            // 5. Tombol aksi di depan kartu
            const playBtns = document.querySelectorAll('.play-btn');
            playBtns.forEach(btn => {
                if (btn.classList.contains('is-playing')) {
                    const spinnerSvg = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="animate-spin"><circle cx="12" cy="12" r="10" stroke-dasharray="32" stroke-dashoffset="10" stroke-opacity="0.3"></circle><path d="M12 2a10 10 0 0 1 10 10" stroke="currentColor"></path></svg>`;
                    btn.innerHTML = spinnerSvg + cfg.playText;
                } else {
                    const svg = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path><path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path></svg>`;
                    btn.innerHTML = svg + cfg.playText;
                }
            });



            const aiBtns = document.querySelectorAll('.ai-btn');
            aiBtns.forEach(btn => {
                const svg = btn.querySelector('svg') ? btn.querySelector('svg').outerHTML : '';
                btn.innerHTML = svg + cfg.aiText;
            });"""

new_translate_end = """            // 5. Tombol aksi di depan kartu
            const playBtns = document.querySelectorAll('.play-btn');
            playBtns.forEach(btn => {
                if (btn.classList.contains('is-playing')) {
                    const spinnerSvg = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="animate-spin"><circle cx="12" cy="12" r="10" stroke-dasharray="32" stroke-dashoffset="10" stroke-opacity="0.3"></circle><path d="M12 2a10 10 0 0 1 10 10" stroke="currentColor"></path></svg>`;
                    btn.innerHTML = spinnerSvg + cfg.playText;
                } else {
                    const svg = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path><path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path></svg>`;
                    btn.innerHTML = svg + cfg.playText;
                }
            });

            const aiBtns = document.querySelectorAll('.ai-btn');
            aiBtns.forEach(btn => {
                const svg = btn.querySelector('svg') ? btn.querySelector('svg').outerHTML : '';
                btn.innerHTML = svg + cfg.aiText;
            });

            // 5b. Terjemahkan Mode Tabs & Elemen UI Lainnya (data-i18n-orig)
            const i18nElements = document.querySelectorAll('[data-i18n-orig]');
            i18nElements.forEach(async el => {
                const orig = el.getAttribute('data-i18n-orig');
                if (!orig) return;
                if (targetLangCode === 'id') {
                    el.textContent = orig;
                } else {
                    const dict = LANG_UI_MAP[targetLangCode];
                    if (dict && dict[orig]) {
                        el.textContent = dict[orig];
                    } else {
                        el.textContent = await translateTextFree(orig, targetLangCode);
                    }
                }
            });

            // 5c. Terjemahkan hierarki tematik pada kartu hasil pencarian
            const thematicStepVals = document.querySelectorAll('.thematic-step .step-val');
            thematicStepVals.forEach(async el => {
                const orig = el.getAttribute('data-original') || el.textContent;
                if (!el.hasAttribute('data-original')) el.setAttribute('data-original', orig);
                if (orig) {
                    if (targetLangCode === 'id') {
                        el.textContent = orig;
                    } else {
                        el.textContent = await translateTextFree(orig, targetLangCode);
                    }
                }
            });

            // 5d. Terjemahkan badge jumlah pembahasan tematik
            const countBadge = document.querySelector('.thematic-count-badge');
            if (countBadge) {
                const count = parseInt(countBadge.getAttribute('data-count') || '0');
                if (count > 0) {
                    if (targetLangCode === 'id') {
                        countBadge.textContent = `Ditemukan dalam ${count} Pembahasan Tematis`;
                    } else if (targetLangCode === 'en') {
                        countBadge.textContent = `Found in ${count} Thematic Topics`;
                    } else if (targetLangCode === 'ar') {
                        countBadge.textContent = `موجود في ${count} مواضيع موضوعية`;
                    } else {
                        const prefix = await translateTextFree('Ditemukan dalam', targetLangCode);
                        const suffix = await translateTextFree('Pembahasan Tematis', targetLangCode);
                        countBadge.textContent = `${prefix} ${count} ${suffix}`;
                    }
                } else {
                    const emptyText = 'Tidak Ditemukan dalam Indeks Tematis';
                    if (targetLangCode === 'id') {
                        countBadge.textContent = emptyText;
                    } else {
                        countBadge.textContent = await translateTextFree(emptyText, targetLangCode);
                    }
                }
            }"""

if old_translate_end in html:
    html = html.replace(old_translate_end, new_translate_end)
    print("Updated translatePageContent with UI & Tab translations.")
else:
    print("old_translate_end not found directly.")

# 5. In renderSearchVerseResult, add data-i18n-orig to all rendered elements
old_render_part = """                    <div class="search-actions-bar">
                            <div class="search-action-btns-left">
                                <button class="tts-button play-btn" data-text="${encodeURIComponent(verseObj.indo)}" onclick="playTTS(this, event)" title="Dengarkan Terjemahan Suara">
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path><path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path></svg>
                                    Dengarkan
                                </button>
                                <button class="tts-button ai-btn" style="color: #8b5cf6; border-color: #8b5cf6; background-color: rgba(139, 92, 246, 0.1);" onclick="tanyaAI(this, event, 'QS. ${surahInfo.name}: ${ayatNum}')" title="Tanya AI Tafsir Ayat Ini">
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                                    Tanya AI
                                </button>
                                <button class="tts-button copy-btn" onclick="copyAyatText(this, event, '${surahInfo.name}', ${surahNum}, ${ayatNum})" title="Salin Teks Arab & Terjemahan">
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                                    Salin Ayat
                                </button>
                            </div>"""

new_render_part = """                    <div class="search-actions-bar">
                            <div class="search-action-btns-left">
                                <button class="tts-button play-btn" data-text="${encodeURIComponent(verseObj.indo)}" onclick="playTTS(this, event)" title="Dengarkan Terjemahan Suara">
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path><path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path></svg>
                                    Dengarkan
                                </button>
                                <button class="tts-button ai-btn" style="color: #8b5cf6; border-color: #8b5cf6; background-color: rgba(139, 92, 246, 0.1);" onclick="tanyaAI(this, event, 'QS. ${surahInfo.name}: ${ayatNum}')" title="Tanya AI Tafsir Ayat Ini">
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                                    Tanya AI
                                </button>
                                <button class="tts-button copy-btn" onclick="copyAyatText(this, event, '${surahInfo.name}', ${surahNum}, ${ayatNum})" title="Salin Teks Arab & Terjemahan">
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                                    <span data-i18n-orig="Salin Ayat">Salin Ayat</span>
                                </button>
                            </div>"""

if old_render_part in html:
    html = html.replace(old_render_part, new_render_part)
    print("Updated copy button in renderSearchVerseResult.")

old_thematic_section_header = """                <!-- Section Hasil Klasifikasi Tematis -->
                <div class="thematic-results-section">
                    <div class="thematic-results-header">
                        <h3 class="thematic-results-title">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--accent);"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                            Klasifikasi Al-Qur'an Tematis
                        </h3>
                        <span class="thematic-count-badge">
                            ${topicsCount > 0 ? `Ditemukan dalam ${topicsCount} Pembahasan Tematis` : 'Tidak Ditemukan dalam Indeks Tematis'}
                        </span>
                    </div>"""

new_thematic_section_header = """                <!-- Section Hasil Klasifikasi Tematis -->
                <div class="thematic-results-section">
                    <div class="thematic-results-header">
                        <h3 class="thematic-results-title">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--accent);"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                            <span data-i18n-orig="Klasifikasi Al-Qur'an Tematis">Klasifikasi Al-Qur'an Tematis</span>
                        </h3>
                        <span class="thematic-count-badge" data-count="${topicsCount}">
                            ${topicsCount > 0 ? `Ditemukan dalam ${topicsCount} Pembahasan Tematis` : 'Tidak Ditemukan dalam Indeks Tematis'}
                        </span>
                    </div>"""

if old_thematic_section_header in html:
    html = html.replace(old_thematic_section_header, new_thematic_section_header)
    print("Updated thematic section header.")

old_steps_markup = """                                <div class="thematic-step tema-step">
                                    <span class="step-label">🏷️ Tema Besar:</span>
                                    <span class="step-val">${t.tema}</span>
                                </div>
                                <div class="thematic-step pokok-step">
                                    <span class="step-label">📂 Pokok Bahasan:</span>
                                    <span class="step-val">${t.pokok}</span>
                                </div>
                                <div class="thematic-step sub-step">
                                    <span class="step-label">📑 Sub Pokok Bahasan:</span>
                                    <span class="step-val">${t.sub}</span>
                                </div>
                                <div class="thematic-step uraian-step">
                                    <span class="step-label">📝 Uraian Khusus:</span>
                                    <span class="step-val">${t.uraian}</span>
                                </div>
                            </div>
                            <button class="btn-jump-thematic" onclick="navigateToThematicTopic('${t.tema.replace(/'/g, "\\\\'") }', '${t.pokok.replace(/'/g, "\\\\'") }', '${t.sub.replace(/'/g, "\\\\'") }', '${t.uraian.replace(/'/g, "\\\\'") }', ${surahNum}, ${ayatNum})">
                                <span>Buka di Halaman Tematik</span>"""

new_steps_markup = """                                <div class="thematic-step tema-step">
                                    <span class="step-label" data-i18n-orig="Tema Besar:">🏷️ Tema Besar:</span>
                                    <span class="step-val" data-original="${t.tema}">${t.tema}</span>
                                </div>
                                <div class="thematic-step pokok-step">
                                    <span class="step-label" data-i18n-orig="Pokok Bahasan:">📂 Pokok Bahasan:</span>
                                    <span class="step-val" data-original="${t.pokok}">${t.pokok}</span>
                                </div>
                                <div class="thematic-step sub-step">
                                    <span class="step-label" data-i18n-orig="Sub Pokok Bahasan:">📑 Sub Pokok Bahasan:</span>
                                    <span class="step-val" data-original="${t.sub}">${t.sub}</span>
                                </div>
                                <div class="thematic-step uraian-step">
                                    <span class="step-label" data-i18n-orig="Uraian Khusus:">📝 Uraian Khusus:</span>
                                    <span class="step-val" data-original="${t.uraian}">${t.uraian}</span>
                                </div>
                            </div>
                            <button class="btn-jump-thematic" onclick="navigateToThematicTopic('${t.tema.replace(/'/g, "\\\\'") }', '${t.pokok.replace(/'/g, "\\\\'") }', '${t.sub.replace(/'/g, "\\\\'") }', '${t.uraian.replace(/'/g, "\\\\'") }', ${surahNum}, ${ayatNum})">
                                <span data-i18n-orig="Buka di Halaman Tematik">Buka di Halaman Tematik</span>"""

if old_steps_markup in html:
    html = html.replace(old_steps_markup, new_steps_markup)
    print("Updated steps markup with data-i18n-orig.")

# 6. Also update Cari Ayat on flip cards
old_cari_ayat_btn = """                                            <button class="tts-button" style="color: #38bdf8; border-color: #38bdf8; background-color: rgba(56, 189, 248, 0.1);" onclick="lookupVerseInSearch(${v.surah_num}, ${v.ayat_num}, event)" title="Lihat di Pencari Surat & Ayat">
                                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                                                Cari Ayat
                                            </button>"""

new_cari_ayat_btn = """                                            <button class="tts-button" style="color: #38bdf8; border-color: #38bdf8; background-color: rgba(56, 189, 248, 0.1);" onclick="lookupVerseInSearch(${v.surah_num}, ${v.ayat_num}, event)" title="Lihat di Pencari Surat & Ayat">
                                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                                                <span data-i18n-orig="Cari Ayat">Cari Ayat</span>
                                            </button>"""

if old_cari_ayat_btn in html:
    html = html.replace(old_cari_ayat_btn, new_cari_ayat_btn)
    print("Updated flip card Cari Ayat button with data-i18n-orig.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated index.html successfully!")
