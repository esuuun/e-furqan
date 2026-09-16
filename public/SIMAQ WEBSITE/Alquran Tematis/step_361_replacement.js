                                            <button class="tts-button" style="color: #38bdf8; border-color: #38bdf8; background-color: rgba(56, 189, 248, 0.1);" onclick="lookupVerseInSearch(${v.surah_num}, ${v.ayat_num}, event)" title="Lihat di Pencari Surat & Ayat">
                                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
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
                el.innerHTML = cfg.groupMeta(count);
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