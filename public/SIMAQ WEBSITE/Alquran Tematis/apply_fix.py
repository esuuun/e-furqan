import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Normalize newlines temporarily to find and replace cleanly
is_crlf = '\r\n' in content
lines = content.splitlines()

print(f"Total lines: {len(lines)}")
print(f"Line 5289 (1-indexed): {lines[5288][:60]}...")
print(f"Line 5290 (1-indexed): {lines[5289][:60]}...")
print(f"Line 5527 (1-indexed): {lines[5526][:60]}...")

assert "lookupVerseInSearch" in lines[5288]
assert "stroke=" in lines[5289]
assert "function switchMainMode(mode)" in lines[5526]

clean_replacement_code = """                                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                                                <span data-i18n-orig="Cari Ayat">Cari Ayat</span>
                                            </button>
                                        </div>
                                    </div>
                                    <div class="flip-card-back">${v.arab}</div>
                                </div>
                            </div>
                        </div>
                    `;
                });
            }

            markup += `
                    </div>
                </div>
            `;
            return markup;
        }

        function renderContentAll(tema, pokok, sub) {
            saveCurrentState();
            const subData = quranData[tema] && quranData[tema][pokok] && quranData[tema][pokok][sub];
            if (!subData) return;
            const keys = naturalSort(Object.keys(subData));
            let html = `
                <div class="sub-header-banner-card">
                    <div class="sub-header-info">
                        <h2 class="sub-header-title" data-original="${sub}">${sub}</h2>
                        <div class="sub-header-meta" data-count="${keys.length}">Menampilkan ${keys.length} Kelompok Uraian Flash Card</div>
                    </div>
                    <div class="sub-header-actions">
                        <button id="btn-toggle-all-groups" class="toggle-verses-btn" onclick="toggleAllGroups()">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="7 13 12 18 17 13"></polyline><polyline points="7 6 12 11 17 6"></polyline></svg>
                            <span id="toggle-all-text" data-i18n-orig="Buka Semua Uraian">Buka Semua Uraian</span>
                        </button>
                    </div>
                </div>
            `;

            const navContainer = document.getElementById('bottom-nav-container');
            let totalVerses = 0;

            keys.forEach((uraianTitle, idx) => {
                const data = subData[uraianTitle];
                html += generateUraianGroupMarkup(uraianTitle, data, idx);
                if (data && data.verses) totalVerses += data.verses.length;
            });

            elHint.style.display = 'none';

            if (totalVerses > 0) {
                if (navContainer) navContainer.style.display = 'block';
            } else {
                if (navContainer) navContainer.style.display = 'none';
            }

            elContent.innerHTML = html;
            updateNavButtonState();
            translatePageContent();
        }

        function renderContentSingle(tema, pokok, sub, uraianTitle) {
            saveCurrentState();
            const subData = quranData[tema] && quranData[tema][pokok] && quranData[tema][pokok][sub];
            if (!subData || !subData[uraianTitle]) return;

            const data = subData[uraianTitle];
            const navContainer = document.getElementById('bottom-nav-container');

            let html = generateUraianGroupMarkup(uraianTitle, data, 0);

            elHint.style.display = 'none';

            if (data.verses && data.verses.length > 0) {
                if (navContainer) navContainer.style.display = 'block';
            } else {
                if (navContainer) navContainer.style.display = 'none';
            }

            elContent.innerHTML = html;
            updateNavButtonState();
            translatePageContent();
        }

        const elTtsLanguage = document.getElementById('tts-language');
        if (elTtsLanguage) {
            elTtsLanguage.addEventListener('change', () => {
                stopTTS();
                saveCurrentState();
                translatePageContent();
                translateDropdowns();
                updateTranslatorInfo();
            });
        }

        async function translatePageContent() {
            const langSelect = document.getElementById('tts-language');
            const lang = langSelect ? langSelect.value : 'id-ID';
            const cfg = LANG_CONFIG[lang] || LANG_CONFIG['id-ID'];
            const targetLangCode = cfg.code;

            updateTranslatorInfo();

            // 1. Petunjuk / Hint
            const elHint = document.getElementById('hint-text');
            if (elHint) {
                elHint.innerHTML = cfg.hint;
            }

            // 2. Tombol Navigasi Bawah
            const btnPrev = document.getElementById('btn-prev-uraian');
            const btnNext = document.getElementById('btn-next-uraian');
            if (btnPrev) btnPrev.textContent = cfg.prevBtn;
            if (btnNext) btnNext.textContent = cfg.nextBtn;

            // 3. Judul Sub Header & Meta
            const subTitleEls = document.querySelectorAll('.sub-header-title');
            subTitleEls.forEach(async el => {
                const orig = el.getAttribute('data-original');
                if (orig) {
                    if (targetLangCode === 'id') el.textContent = orig;
                    else el.textContent = await translateTextFree(orig, targetLangCode);
                }
            });

            const subMetaEls = document.querySelectorAll('.sub-header-meta');
            subMetaEls.forEach(el => {
                const count = el.getAttribute('data-count');
                el.textContent = cfg.subMeta(count);
            });

            // 4. Judul Kelompok Uraian & Meta Jumlah Ayat
            const groupTitleEls = document.querySelectorAll('.group-title');
            groupTitleEls.forEach(async el => {
                const orig = el.getAttribute('data-original');
                if (orig) {
                    if (targetLangCode === 'id') el.textContent = orig;
                    else el.textContent = await translateTextFree(orig, targetLangCode);
                }
            });

            const groupMetaEls = document.querySelectorAll('.group-meta');
            groupMetaEls.forEach(el => {
                const count = el.getAttribute('data-count');
                el.textContent = cfg.groupMeta(count);
            });

            // 5. Tombol aksi di depan kartu
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

            // 5b2. Terjemahkan Placeholders Input (data-i18n-placeholder)
            const placeholderElements = document.querySelectorAll('[data-i18n-placeholder]');
            placeholderElements.forEach(async el => {
                const orig = el.getAttribute('data-i18n-placeholder');
                if (!orig) return;
                if (targetLangCode === 'id') {
                    el.placeholder = orig;
                } else {
                    const dict = LANG_UI_MAP[targetLangCode];
                    if (dict && dict[orig]) {
                        el.placeholder = dict[orig];
                    } else {
                        el.placeholder = await translateTextFree(orig, targetLangCode);
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
            }

            // 5e. Terjemahkan kartu hasil pencarian kata kunci (Uraian, Path, dan Badge)
            const kwUraianElements = document.querySelectorAll('.keyword-uraian-title, .keyword-uraian-path span[data-original], .kw-topic-badge[data-original]');
            kwUraianElements.forEach(async el => {
                const orig = el.getAttribute('data-original');
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

            // 6. Terjemahan Ayat pada Kartu Flip (di bagian depan), Hasil Pencarian Ayat, dan Hasil Pencarian Kata Kunci
            const cards = document.querySelectorAll('.flip-card-front, .search-card-front, .keyword-verse-card');
            if (lang === 'id-ID') {
                cards.forEach(card => {
                    const origIndo = card.getAttribute('data-indo') ? decodeURIComponent(card.getAttribute('data-indo')) : '';
                    const textEl = card.querySelector('.translation-text');
                    const text = origIndo || (textEl ? textEl.getAttribute('data-original') || '' : '');
                    if (textEl && text) {
                        textEl.className = 'translation-text' + (textEl.classList.contains('keyword-trans-box') ? ' keyword-trans-box' : '');
                        textEl.textContent = text;
                    }
                    const playBtn = card.querySelector('.play-btn');
                    if (playBtn && text) playBtn.setAttribute('data-text', encodeURIComponent(text));
                });
                return;
            }
            
            const edition = cfg.edition;
            const cssClass = cfg.cssClass ? ' ' + cfg.cssClass : '';
            
            const promises = Array.from(cards).map(async card => {
                const surah = card.getAttribute('data-surah');
                const ayat = card.getAttribute('data-ayat');
                const textEl = card.querySelector('.translation-text');
                const playBtn = card.querySelector('.play-btn');
                
                if (textEl) {
                    textEl.className = 'translation-text' + (textEl.classList.contains('keyword-trans-box') ? ' keyword-trans-box' : '') + cssClass;
                }
                
                const cacheKey = `${edition}:${surah}:${ayat}`;
                if (ayahTranslationCache[cacheKey]) {
                    const translatedText = ayahTranslationCache[cacheKey];
                    if (textEl) textEl.textContent = translatedText;
                    if (playBtn) playBtn.setAttribute('data-text', encodeURIComponent(translatedText));
                    return;
                }
                
                if (textEl) textEl.textContent = cfg.loadingText;
                
                try {
                    const res = await fetch(`https://api.alquran.cloud/v1/ayah/${surah}:${ayat}/${edition}`);
                    const json = await res.json();
                    if (json && json.data && json.data.text) {
                        const translatedText = json.data.text;
                        ayahTranslationCache[cacheKey] = translatedText;
                        if (textEl) textEl.textContent = translatedText;
                        if (playBtn) playBtn.setAttribute('data-text', encodeURIComponent(translatedText));
                    } else {
                        if (textEl) textEl.textContent = cfg.errorText;
                    }
                } catch (e) {
                    console.error(e);
                    if (textEl) textEl.textContent = cfg.connErrorText;
                }
            });
            await Promise.all(promises);
        }

        /* ==========================================================================
           FITUR PILIH SURAT & AYAT (PENCARIAN TEMATIK TERBALIK)
           ========================================================================== */
        const SURAH_LIST = [{"no": 1, "name": "Al-Fatihah", "arab": "الفاتحة", "ayat": 7, "type": "Mekah"}, {"no": 2, "name": "Al-Baqarah", "arab": "البقرة", "ayat": 286, "type": "Madinah"}, {"no": 3, "name": "Ali 'Imran", "arab": "اٰل عمران", "ayat": 200, "type": "Madinah"}, {"no": 4, "name": "An-Nisa'", "arab": "النساۤء", "ayat": 176, "type": "Madinah"}, {"no": 5, "name": "Al-Ma'idah", "arab": "الماۤئدة", "ayat": 120, "type": "Madinah"}, {"no": 6, "name": "Al-An'am", "arab": "الانعام", "ayat": 165, "type": "Mekah"}, {"no": 7, "name": "Al-A'raf", "arab": "الاعراف", "ayat": 206, "type": "Mekah"}, {"no": 8, "name": "Al-Anfal", "arab": "الانفال", "ayat": 75, "type": "Madinah"}, {"no": 9, "name": "At-Taubah", "arab": "التوبة", "ayat": 129, "type": "Madinah"}, {"no": 10, "name": "Yunus", "arab": "يونس", "ayat": 109, "type": "Mekah"}, {"no": 11, "name": "Hud", "arab": "هود", "ayat": 123, "type": "Mekah"}, {"no": 12, "name": "Yusuf", "arab": "يوسف", "ayat": 111, "type": "Mekah"}, {"no": 13, "name": "Ar-Ra'd", "arab": "الرّعد", "ayat": 43, "type": "Madinah"}, {"no": 14, "name": "Ibrahim", "arab": "ابرٰهيم", "ayat": 52, "type": "Mekah"}, {"no": 15, "name": "Al-Hijr", "arab": "الحجر", "ayat": 99, "type": "Mekah"}, {"no": 16, "name": "An-Nahl", "arab": "النحل", "ayat": 128, "type": "Mekah"}, {"no": 17, "name": "Al-Isra'", "arab": "الاسراۤء", "ayat": 111, "type": "Mekah"}, {"no": 18, "name": "Al-Kahf", "arab": "الكهف", "ayat": 110, "type": "Mekah"}, {"no": 19, "name": "Maryam", "arab": "مريم", "ayat": 98, "type": "Mekah"}, {"no": 20, "name": "Taha", "arab": "طٰهٰ", "ayat": 135, "type": "Mekah"}, {"no": 21, "name": "Al-Anbiya'", "arab": "الانبياۤء", "ayat": 112, "type": "Mekah"}, {"no": 22, "name": "Al-Hajj", "arab": "الحج", "ayat": 78, "type": "Madinah"}, {"no": 23, "name": "Al-Mu'minun", "arab": "المؤمنون", "ayat": 118, "type": "Mekah"}, {"no": 24, "name": "An-Nur", "arab": "النّور", "ayat": 64, "type": "Madinah"}, {"no": 25, "name": "Al-Furqan", "arab": "الفرقان", "ayat": 77, "type": "Mekah"}, {"no": 26, "name": "Asy-Syu'ara'", "arab": "الشعراۤء", "ayat": 227, "type": "Mekah"}, {"no": 27, "name": "An-Naml", "arab": "النمل", "ayat": 93, "type": "Mekah"}, {"no": 28, "name": "Al-Qasas", "arab": "القصص", "ayat": 88, "type": "Mekah"}, {"no": 29, "name": "Al-'Ankabut", "arab": "العنكبوت", "ayat": 69, "type": "Mekah"}, {"no": 30, "name": "Ar-Rum", "arab": "الرّوم", "ayat": 60, "type": "Mekah"}, {"no": 31, "name": "Luqman", "arab": "لقمٰن", "ayat": 34, "type": "Mekah"}, {"no": 32, "name": "As-Sajdah", "arab": "السّجدة", "ayat": 30, "type": "Mekah"}, {"no": 33, "name": "Al-Ahzab", "arab": "الاحزاب", "ayat": 73, "type": "Madinah"}, {"no": 34, "name": "Saba'", "arab": "سبأ", "ayat": 54, "type": "Mekah"}, {"no": 35, "name": "Fatir", "arab": "فاطر", "ayat": 45, "type": "Mekah"}, {"no": 36, "name": "Yasin", "arab": "يٰسۤ", "ayat": 83, "type": "Mekah"}, {"no": 37, "name": "As-Saffat", "arab": "الصّٰۤفّٰت", "ayat": 182, "type": "Mekah"}, {"no": 38, "name": "Sad", "arab": "ص", "ayat": 88, "type": "Mekah"}, {"no": 39, "name": "Az-Zumar", "arab": "الزمر", "ayat": 75, "type": "Mekah"}, {"no": 40, "name": "Ghafir", "arab": "غافر", "ayat": 85, "type": "Mekah"}, {"no": 41, "name": "Fussilat", "arab": "فصّلت", "ayat": 54, "type": "Mekah"}, {"no": 42, "name": "Asy-Syura", "arab": "الشورى", "ayat": 53, "type": "Mekah"}, {"no": 43, "name": "Az-Zukhruf", "arab": "الزخرف", "ayat": 89, "type": "Mekah"}, {"no": 44, "name": "Ad-Dukhan", "arab": "الدخان", "ayat": 59, "type": "Mekah"}, {"no": 45, "name": "Al-Jasiyah", "arab": "الجاثية", "ayat": 37, "type": "Mekah"}, {"no": 46, "name": "Al-Ahqaf", "arab": "الاحقاف", "ayat": 35, "type": "Mekah"}, {"no": 47, "name": "Muhammad", "arab": "محمّد", "ayat": 38, "type": "Madinah"}, {"no": 48, "name": "Al-Fath", "arab": "الفتح", "ayat": 29, "type": "Madinah"}, {"no": 49, "name": "Al-Hujurat", "arab": "الحجرٰت", "ayat": 18, "type": "Madinah"}, {"no": 50, "name": "Qaf", "arab": "ق", "ayat": 45, "type": "Mekah"}, {"no": 51, "name": "Az-Zariyat", "arab": "الذّٰريٰت", "ayat": 60, "type": "Mekah"}, {"no": 52, "name": "At-Tur", "arab": "الطور", "ayat": 49, "type": "Mekah"}, {"no": 53, "name": "An-Najm", "arab": "النجم", "ayat": 62, "type": "Mekah"}, {"no": 54, "name": "Al-Qamar", "arab": "القمر", "ayat": 55, "type": "Mekah"}, {"no": 55, "name": "Ar-Rahman", "arab": "الرحمن", "ayat": 78, "type": "Madinah"}, {"no": 56, "name": "Al-Waqi'ah", "arab": "الواقعة", "ayat": 96, "type": "Mekah"}, {"no": 57, "name": "Al-Hadid", "arab": "الحديد", "ayat": 29, "type": "Madinah"}, {"no": 58, "name": "Al-Mujadilah", "arab": "المجادلة", "ayat": 22, "type": "Madinah"}, {"no": 59, "name": "Al-Hasyr", "arab": "الحشر", "ayat": 24, "type": "Madinah"}, {"no": 60, "name": "Al-Mumtahanah", "arab": "الممتحنة", "ayat": 13, "type": "Madinah"}, {"no": 61, "name": "As-Saff", "arab": "الصّفّ", "ayat": 14, "type": "Madinah"}, {"no": 62, "name": "Al-Jumu'ah", "arab": "الجمعة", "ayat": 11, "type": "Madinah"}, {"no": 63, "name": "Al-Munafiqun", "arab": "المنٰفقون", "ayat": 11, "type": "Madinah"}, {"no": 64, "name": "At-Tagabun", "arab": "التغابن", "ayat": 18, "type": "Madinah"}, {"no": 65, "name": "At-Talaq", "arab": "الطلاق", "ayat": 12, "type": "Madinah"}, {"no": 66, "name": "At-Tahrim", "arab": "التحريم", "ayat": 12, "type": "Madinah"}, {"no": 67, "name": "Al-Mulk", "arab": "الملك", "ayat": 30, "type": "Mekah"}, {"no": 68, "name": "Al-Qalam", "arab": "القلم", "ayat": 52, "type": "Mekah"}, {"no": 69, "name": "Al-Haqqah", "arab": "الحاۤقّة", "ayat": 52, "type": "Mekah"}, {"no": 70, "name": "Al-Ma'arij", "arab": "المعارج", "ayat": 44, "type": "Mekah"}, {"no": 71, "name": "Nuh", "arab": "نوح", "ayat": 28, "type": "Mekah"}, {"no": 72, "name": "Al-Jinn", "arab": "الجن", "ayat": 28, "type": "Mekah"}, {"no": 73, "name": "Al-Muzzammil", "arab": "المزّمّل", "ayat": 20, "type": "Mekah"}, {"no": 74, "name": "Al-Muddassir", "arab": "المدّثّر", "ayat": 56, "type": "Mekah"}, {"no": 75, "name": "Al-Qiyamah", "arab": "القيٰمة", "ayat": 40, "type": "Mekah"}, {"no": 76, "name": "Al-Insan", "arab": "الانسان", "ayat": 31, "type": "Madinah"}, {"no": 77, "name": "Al-Mursalat", "arab": "المرسلٰت", "ayat": 50, "type": "Mekah"}, {"no": 78, "name": "An-Naba'", "arab": "النبأ", "ayat": 40, "type": "Mekah"}, {"no": 79, "name": "An-Nazi'at", "arab": "النّٰزعٰت", "ayat": 46, "type": "Mekah"}, {"no": 80, "name": "'Abasa", "arab": "عبس", "ayat": 42, "type": "Mekah"}, {"no": 81, "name": "At-Takwir", "arab": "التكوير", "ayat": 29, "type": "Mekah"}, {"no": 82, "name": "Al-Infitar", "arab": "الانفطار", "ayat": 19, "type": "Mekah"}, {"no": 83, "name": "Al-Mutaffifin", "arab": "المطفّفين", "ayat": 36, "type": "Mekah"}, {"no": 84, "name": "Al-Insyiqaq", "arab": "الانشقاق", "ayat": 25, "type": "Mekah"}, {"no": 85, "name": "Al-Buruj", "arab": "البروج", "ayat": 22, "type": "Mekah"}, {"no": 86, "name": "At-Tariq", "arab": "الطارق", "ayat": 17, "type": "Mekah"}, {"no": 87, "name": "Al-A'la", "arab": "الاعلى", "ayat": 19, "type": "Mekah"}, {"no": 88, "name": "Al-Gasyiyah", "arab": "الغاشية", "ayat": 26, "type": "Mekah"}, {"no": 89, "name": "Al-Fajr", "arab": "الفجر", "ayat": 30, "type": "Mekah"}, {"no": 90, "name": "Al-Balad", "arab": "البلد", "ayat": 20, "type": "Mekah"}, {"no": 91, "name": "Asy-Syams", "arab": "الشمس", "ayat": 15, "type": "Mekah"}, {"no": 92, "name": "Al-Lail", "arab": "الّيل", "ayat": 21, "type": "Mekah"}, {"no": 93, "name": "Ad-Duha", "arab": "الضحى", "ayat": 11, "type": "Mekah"}, {"no": 94, "name": "Al-Insyirah", "arab": "الشرح", "ayat": 8, "type": "Mekah"}, {"no": 95, "name": "At-Tin", "arab": "التين", "ayat": 8, "type": "Mekah"}, {"no": 96, "name": "Al-'Alaq", "arab": "العلق", "ayat": 19, "type": "Mekah"}, {"no": 97, "name": "Al-Qadr", "arab": "القدر", "ayat": 5, "type": "Mekah"}, {"no": 98, "name": "Al-Bayyinah", "arab": "البيّنة", "ayat": 8, "type": "Madinah"}, {"no": 99, "name": "Az-Zalzalah", "arab": "الزلزلة", "ayat": 8, "type": "Madinah"}, {"no": 100, "name": "Al-'Adiyat", "arab": "العٰديٰت", "ayat": 11, "type": "Mekah"}, {"no": 101, "name": "Al-Qari'ah", "arab": "القارعة", "ayat": 11, "type": "Mekah"}, {"no": 102, "name": "At-Takasur", "arab": "التكاثر", "ayat": 8, "type": "Mekah"}, {"no": 103, "name": "Al-'Asr", "arab": "العصر", "ayat": 3, "type": "Mekah"}, {"no": 104, "name": "Al-Humazah", "arab": "الهمزة", "ayat": 9, "type": "Mekah"}, {"no": 105, "name": "Al-Fil", "arab": "الفيل", "ayat": 5, "type": "Mekah"}, {"no": 106, "name": "Quraisy", "arab": "قريش", "ayat": 4, "type": "Mekah"}, {"no": 107, "name": "Al-Ma'un", "arab": "الماعون", "ayat": 7, "type": "Mekah"}, {"no": 108, "name": "Al-Kausar", "arab": "الكوثر", "ayat": 3, "type": "Mekah"}, {"no": 109, "name": "Al-Kafirun", "arab": "الكٰفرون", "ayat": 6, "type": "Mekah"}, {"no": 110, "name": "An-Nasr", "arab": "النصر", "ayat": 3, "type": "Madinah"}, {"no": 111, "name": "Al-Lahab", "arab": "اللهب", "ayat": 5, "type": "Mekah"}, {"no": 112, "name": "Al-Ikhlas", "arab": "الاخلاص", "ayat": 4, "type": "Mekah"}, {"no": 113, "name": "Al-Falaq", "arab": "الفلق", "ayat": 5, "type": "Madinah"}, {"no": 114, "name": "An-Nas", "arab": "الناس", "ayat": 6, "type": "Madinah"}];

        let verseThematicIndex = {};
        let currentSearchSurah = 2; // Default Al-Baqarah
        let currentSearchAyat = 255; // Default Ayat Kursi
        let surahApiCache = {};
        let activeMainMode = 'thematic';

        let allThematicUraianList = [];
        let allThematicVersesList = [];

        function buildVerseIndex() {
            verseThematicIndex = {};
            allThematicUraianList = [];
            if (!quranData) return;
            for (const [tema, pbs] of Object.entries(quranData)) {
                for (const [pb, spbs] of Object.entries(pbs)) {
                    for (const [spb, urs] of Object.entries(spbs)) {
                        for (const [ur, urData] of Object.entries(urs)) {
                            const vList = (urData && urData.verses) ? urData.verses : [];
                            allThematicUraianList.push({
                                tema: tema,
                                pokok: pb,
                                sub: spb,
                                uraian: ur,
                                verseCount: vList.length,
                                sampleVerses: vList.slice(0, 3)
                            });
                            if (vList.length > 0) {
                                vList.forEach(v => {
                                    const key = `${v.surah_num}:${v.ayat_num}`;
                                    if (!verseThematicIndex[key]) {
                                        verseThematicIndex[key] = {
                                            surah_name: v.surah_name,
                                            surah_num: v.surah_num,
                                            ayat_num: v.ayat_num,
                                            arab: v.arab,
                                            indo: v.indo,
                                            audio: v.audio,
                                            topics: []
                                        };
                                    }
                                    verseThematicIndex[key].topics.push({
                                        tema: tema,
                                        pokok: pb,
                                        sub: spb,
                                        uraian: ur
                                    });
                                });
                            }
                        }
                    }
                }
            }
            allThematicVersesList = Object.values(verseThematicIndex);
            console.log(`[VerseIndex] Indexed ${allThematicVersesList.length} unique verses and ${allThematicUraianList.length} thematic topics.`);
        }
"""

replacement_lines = clean_replacement_code.strip('\n').split('\n')

new_lines = lines[:5289] + replacement_lines + lines[5526:]

newline_char = '\r\n' if is_crlf else '\n'
new_content = newline_char.join(new_lines)

# Also ensure switchMainMode calls translatePageContent()
old_switch = """            } else if (mode === 'keyword') {
                if (tabKeyword) tabKeyword.classList.add('active');
                if (keywordNav) keywordNav.style.display = 'block';
                if (keywordView) keywordView.style.display = 'block';
                const kwInput = document.getElementById('keyword-search-input');
                if (kwInput && !kwInput.value.trim()) {
                    kwInput.focus();
                }
            }
        }"""

new_switch = """            } else if (mode === 'keyword') {
                if (tabKeyword) tabKeyword.classList.add('active');
                if (keywordNav) keywordNav.style.display = 'block';
                if (keywordView) keywordView.style.display = 'block';
                const kwInput = document.getElementById('keyword-search-input');
                if (kwInput && !kwInput.value.trim()) {
                    kwInput.focus();
                }
            }
            translatePageContent();
        }"""

if old_switch in new_content:
    new_content = new_content.replace(old_switch, new_switch)
    print("Added translatePageContent() to switchMainMode")
elif old_switch.replace('\n', '\r\n') in new_content:
    new_content = new_content.replace(old_switch.replace('\n', '\r\n'), new_switch.replace('\n', '\r\n'))
    print("Added translatePageContent() to switchMainMode (CRLF)")

# Ensure initData calls translatePageContent() before checkAutoNav()
old_init = """            populateSelect(elTema, naturalSort(Object.keys(data)), "Pilih Tema");
            translateDropdowns();
            updateTranslatorInfo();
            checkAutoNav();
            translatePageContent();"""

new_init = """            populateSelect(elTema, naturalSort(Object.keys(data)), "Pilih Tema");
            translateDropdowns();
            updateTranslatorInfo();
            translatePageContent();
            checkAutoNav();"""

if old_init in new_content:
    new_content = new_content.replace(old_init, new_init)
    print("Updated initData to call translatePageContent() before checkAutoNav")
elif old_init.replace('\n', '\r\n') in new_content:
    new_content = new_content.replace(old_init.replace('\n', '\r\n'), new_init.replace('\n', '\r\n'))
    print("Updated initData to call translatePageContent() before checkAutoNav (CRLF)")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully written repaired index.html!")
