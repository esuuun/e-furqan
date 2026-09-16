import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS for enhancements
css_enhancements = """
        /* ==========================================================================
           UI Polish Enhancements: Font Scaler, Direct Ayat Input, Back to Top
           ========================================================================== */
        :root {
            --arabic-font-size: 2.2rem;
        }

        .flip-card-back {
            font-size: var(--arabic-font-size, 2.2rem) !important;
        }
        .search-arabic-box {
            font-size: var(--arabic-font-size, 2.2rem) !important;
        }

        .font-size-toolbar {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            background: rgba(17, 24, 39, 0.85);
            border: 1px solid var(--card-border);
            padding: 0.25rem 0.65rem;
            border-radius: 999px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        }
        .font-toolbar-label {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            color: #94a3b8;
            font-size: 0.82rem;
            font-weight: 600;
            margin-right: 0.25rem;
            user-select: none;
        }
        .font-toolbar-label svg {
            color: var(--accent);
        }
        .font-size-btn {
            background: #1e293b;
            color: #cbd5e1;
            border: 1px solid #334155;
            width: 30px;
            height: 28px;
            border-radius: 6px;
            font-size: 0.82rem;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
            user-select: none;
        }
        .font-size-btn:hover {
            background: var(--accent);
            color: #0b0f19;
            border-color: var(--accent);
            transform: scale(1.06);
        }
        .font-reset-btn {
            font-weight: 500;
            color: #94a3b8;
        }

        .custom-ayat-input {
            width: 65px;
            height: 44px;
            box-sizing: border-box;
            background: #0f172a;
            color: #5eead4;
            border: 1px solid #334155;
            border-radius: 8px;
            text-align: center;
            font-family: 'Inter', sans-serif;
            font-size: 0.98rem;
            font-weight: 700;
            transition: all 0.2s ease;
            -moz-appearance: textfield;
            flex-shrink: 0;
        }
        .custom-ayat-input::-webkit-outer-spin-button,
        .custom-ayat-input::-webkit-inner-spin-button {
            -webkit-appearance: none;
            margin: 0;
        }
        .custom-ayat-input:focus {
            outline: none;
            border-color: var(--accent);
            box-shadow: 0 0 0 2px rgba(20, 184, 166, 0.25);
        }

        .floating-back-to-top {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            width: 46px;
            height: 46px;
            border-radius: 50%;
            background: linear-gradient(135deg, rgba(20, 184, 166, 0.9), rgba(13, 148, 136, 0.95));
            color: #0b0f19;
            border: 1px solid rgba(94, 234, 212, 0.5);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5), 0 0 20px rgba(20, 184, 166, 0.4);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 999;
            opacity: 0;
            visibility: hidden;
            transform: translateY(15px);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .floating-back-to-top.show {
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }
        .floating-back-to-top:hover {
            background: linear-gradient(135deg, #2dd4bf, #14b8a6);
            transform: translateY(-3px) scale(1.08);
            box-shadow: 0 8px 25px rgba(20, 184, 166, 0.6);
        }
"""

if '/* ==========================================================================\n           UI Polish Enhancements' not in html:
    html = html.replace('    </style>', css_enhancements + '    </style>')
    print("Inserted enhancement CSS.")

# 2. Add Font Size Toolbar in Header
old_header_box = """        <div style="text-align: center; margin-bottom: 2rem; margin-top: -1rem;">
            <div style="display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; flex-wrap: wrap;">
                <label for="tts-language" style="color: #94a3b8; margin-right: 0.5rem; font-size: 0.95rem; font-weight: 500;">Bahasa Terjemahan & Suara:</label>
                <select id="tts-language" class="custom-select" style="min-width: 190px; padding: 0.5rem 2.5rem 0.5rem 1rem; font-size: 0.9rem;">"""

new_header_box = """        <div style="text-align: center; margin-bottom: 2rem; margin-top: -1rem;">
            <div style="display: inline-flex; align-items: center; justify-content: center; gap: 0.85rem; flex-wrap: wrap;">
                <div style="display: inline-flex; align-items: center; gap: 0.5rem; flex-wrap: wrap;">
                    <label for="tts-language" style="color: #94a3b8; margin-right: 0.5rem; font-size: 0.95rem; font-weight: 500;">Bahasa Terjemahan & Suara:</label>
                    <select id="tts-language" class="custom-select" style="min-width: 190px; padding: 0.5rem 2.5rem 0.5rem 1rem; font-size: 0.9rem;">"""

if old_header_box in html:
    html = html.replace(old_header_box, new_header_box)
    
old_select_close = """                    <option value="ku-IQ">☀️ کوردی (Kurdish)</option>
                </select>
            </div>
            <div style="display: flex; justify-content: center; width: 100%;">"""

new_select_close = """                    <option value="ku-IQ">☀️ کوردی (Kurdish)</option>
                </select>
                </div>

                <!-- Font Size Scaler Widget -->
                <div class="font-size-toolbar" title="Atur Ukuran Huruf Kaligrafi Arab">
                    <span class="font-toolbar-label">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 7 4 4 20 4 20 7"></polyline><line x1="9" y1="20" x2="15" y2="20"></line><line x1="12" y1="4" x2="12" y2="20"></line></svg>
                        <span data-i18n-orig="Huruf Arab:">Huruf Arab:</span>
                    </span>
                    <button class="font-size-btn" onclick="changeFontSize(-1)" title="Perkecil Ukuran Huruf Arab">A-</button>
                    <button class="font-size-btn font-reset-btn" onclick="resetFontSize()" title="Reset Ukuran Bawaan">A</button>
                    <button class="font-size-btn" onclick="changeFontSize(1)" title="Perbesar Ukuran Huruf Arab">A+</button>
                </div>
            </div>
            <div style="display: flex; justify-content: center; width: 100%;">"""

if old_select_close in html:
    html = html.replace(old_select_close, new_select_close)
    print("Inserted Font Size Toolbar into Header.")

# 3. Add Direct Ayat Input in Search Console
old_ayat_field = """                <div class="search-field-group ayat-field">
                    <label for="select-search-ayat" data-i18n-orig="Nomor Ayat:">Nomor Ayat:</label>
                    <div class="ayat-picker-row">
                        <button id="btn-ayat-prev" class="ayat-stepper-btn" onclick="stepAyat(-1)" title="Ayat Sebelumnya" disabled>◀</button>
                        <select id="select-search-ayat" class="custom-select search-select" onchange="onSearchAyatChange()" disabled>
                            <option value="">Pilih Ayat</option>
                        </select>
                        <button id="btn-ayat-next" class="ayat-stepper-btn" onclick="stepAyat(1)" title="Ayat Selanjutnya" disabled>▶</button>
                    </div>
                </div>"""

new_ayat_field = """                <div class="search-field-group ayat-field">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <label for="select-search-ayat" data-i18n-orig="Nomor Ayat:">Nomor Ayat:</label>
                        <span id="ayat-range-hint" style="font-size: 0.8rem; color: #94a3b8; font-weight: 600;">(1–286)</span>
                    </div>
                    <div class="ayat-picker-row">
                        <button id="btn-ayat-prev" class="ayat-stepper-btn" onclick="stepAyat(-1)" title="Ayat Sebelumnya" disabled>◀</button>
                        <input type="number" id="input-search-ayat-num" class="custom-ayat-input" min="1" max="286" placeholder="No." onchange="onDirectAyatInput()" onkeydown="if(event.key==='Enter')onDirectAyatInput()" title="Ketik nomor ayat langsung">
                        <select id="select-search-ayat" class="custom-select search-select" onchange="onSearchAyatChange()" disabled>
                            <option value="">Pilih Ayat</option>
                        </select>
                        <button id="btn-ayat-next" class="ayat-stepper-btn" onclick="stepAyat(1)" title="Ayat Selanjutnya" disabled>▶</button>
                    </div>
                </div>"""

if old_ayat_field in html:
    html = html.replace(old_ayat_field, new_ayat_field)
    print("Updated Ayat controls with Direct Number Input.")
else:
    print("old_ayat_field not matched directly.")

# 4. Add "Buka Semua / Tutup Semua" in renderContentAll
old_render_all_header = """            let html = `
                <div class="sub-header-banner-card">
                    <div class="sub-header-info">
                        <h2 class="sub-header-title" data-original="${sub}">${sub}</h2>
                        <div class="sub-header-meta" data-count="${keys.length}">Menampilkan ${keys.length} Kelompok Uraian Flash Card</div>
                    </div>
                </div>
            `;"""

new_render_all_header = """            let html = `
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
            `;"""

if old_render_all_header in html:
    html = html.replace(old_render_all_header, new_render_all_header)
    print("Updated renderContentAll with Expand/Collapse All button.")
else:
    print("old_render_all_header not found directly.")

# 5. Add WhatsApp Share Button in renderSearchVerseResult
old_actions_bar = """                                <button class="tts-button copy-btn" onclick="copyAyatText(this, event, '${surahInfo.name}', ${surahNum}, ${ayatNum})" title="Salin Teks Arab & Terjemahan">
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                                    <span data-i18n-orig="Salin Ayat">Salin Ayat</span>
                                </button>
                            </div>"""

new_actions_bar = """                                <button class="tts-button copy-btn" onclick="copyAyatText(this, event, '${surahInfo.name}', ${surahNum}, ${ayatNum})" title="Salin Teks Arab & Terjemahan">
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                                    <span data-i18n-orig="Salin Ayat">Salin Ayat</span>
                                </button>
                                <button class="tts-button" style="color: #25d366; border-color: rgba(37, 211, 102, 0.4); background-color: rgba(37, 211, 102, 0.1);" onclick="shareAyatWhatsApp('${surahInfo.name}', ${surahNum}, ${ayatNum})" title="Bagikan Ayat ke WhatsApp">
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                                    <span data-i18n-orig="Bagikan">Bagikan</span>
                                </button>
                            </div>"""

if old_actions_bar in html:
    html = html.replace(old_actions_bar, new_actions_bar)
    print("Added WhatsApp Share Button in search view.")

# 6. Add Floating Back-to-Top button before </body>
back_to_top_html = """    <!-- Floating Back to Top Button -->
    <button id="btn-back-to-top" class="floating-back-to-top" onclick="window.scrollTo({ top: 0, behavior: 'smooth' })" title="Kembali ke Atas">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
    </button>
"""

if 'id="btn-back-to-top"' not in html:
    html = html.replace('</body>', back_to_top_html + '</body>')
    print("Added Floating Back-to-Top Button.")

# 7. Add JavaScript functions for Font Scaler, Direct Input, Toggle All, Share, and URL Sync
js_functions = """
        /* ==========================================================================
           JavaScript Helpers: Font Scaler, Direct Ayat Input, Toggle All, Share
           ========================================================================== */
        const FONT_SCALES = ['1.7rem', '1.95rem', '2.2rem', '2.55rem', '3.0rem'];
        let currentFontScaleIdx = 2; // Default 2.2rem

        function initFontScale() {
            const saved = localStorage.getItem('arabic_font_scale_idx');
            if (saved !== null) {
                const idx = parseInt(saved);
                if (idx >= 0 && idx < FONT_SCALES.length) {
                    currentFontScaleIdx = idx;
                    applyFontScale();
                }
            }
        }

        function applyFontScale() {
            const size = FONT_SCALES[currentFontScaleIdx];
            document.documentElement.style.setProperty('--arabic-font-size', size);
            localStorage.setItem('arabic_font_scale_idx', currentFontScaleIdx);
        }

        function changeFontSize(delta) {
            let next = currentFontScaleIdx + delta;
            if (next < 0) next = 0;
            if (next >= FONT_SCALES.length) next = FONT_SCALES.length - 1;
            currentFontScaleIdx = next;
            applyFontScale();
        }

        function resetFontSize() {
            currentFontScaleIdx = 2;
            applyFontScale();
        }

        function onDirectAyatInput() {
            const input = document.getElementById('input-search-ayat-num');
            if (!input) return;
            const surahInfo = SURAH_LIST.find(s => s.no == currentSearchSurah);
            const maxAyat = surahInfo ? surahInfo.ayat : 286;
            let val = parseInt(input.value);
            if (isNaN(val) || val < 1) val = 1;
            if (val > maxAyat) val = maxAyat;

            input.value = val;
            currentSearchAyat = val;

            const selectAyat = document.getElementById('select-search-ayat');
            if (selectAyat) selectAyat.value = val;
            updateStepperButtons();
            renderSearchVerseResult(currentSearchSurah, currentSearchAyat);
        }

        function toggleAllGroups() {
            const groupCards = document.querySelectorAll('.uraian-group-card');
            const toggleBtn = document.getElementById('btn-toggle-all-groups');
            if (!groupCards.length) return;

            const anyCollapsed = Array.from(groupCards).some(c => c.classList.contains('is-collapsed'));

            groupCards.forEach(c => {
                if (anyCollapsed) {
                    c.classList.remove('is-collapsed');
                } else {
                    c.classList.add('is-collapsed');
                }
            });

            if (toggleBtn) {
                const langSelect = document.getElementById('tts-language');
                const lang = langSelect ? langSelect.value : 'id-ID';
                const cfg = LANG_CONFIG[lang] || LANG_CONFIG['id-ID'];
                const targetLangCode = cfg.code;

                if (anyCollapsed) {
                    toggleBtn.classList.add('collapsed-mode');
                    const text = (targetLangCode === 'id') ? 'Tutup Semua Uraian' : (targetLangCode === 'en' ? 'Collapse All' : 'Tutup Semua Uraian');
                    toggleBtn.innerHTML = `
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="17 11 12 6 7 11"></polyline><polyline points="17 18 12 13 7 18"></polyline></svg>
                        <span id="toggle-all-text" data-i18n-orig="Tutup Semua Uraian">${text}</span>
                    `;
                } else {
                    toggleBtn.classList.remove('collapsed-mode');
                    const text = (targetLangCode === 'id') ? 'Buka Semua Uraian' : (targetLangCode === 'en' ? 'Expand All' : 'Buka Semua Uraian');
                    toggleBtn.innerHTML = `
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="7 13 12 18 17 13"></polyline><polyline points="7 6 12 11 17 6"></polyline></svg>
                        <span id="toggle-all-text" data-i18n-orig="Buka Semua Uraian">${text}</span>
                    `;
                }
            }

            const elHint = document.getElementById('hint-text');
            if (elHint) {
                elHint.style.display = anyCollapsed ? 'flex' : 'none';
            }
        }

        function shareAyatWhatsApp(surahName, surahNum, ayatNum) {
            const card = document.getElementById('current-rendered-verse');
            if (!card) return;
            const arabEl = card.querySelector('.search-arabic-box');
            const transEl = card.querySelector('.search-translation-box');
            const arab = arabEl ? arabEl.textContent.trim() : '';
            const trans = transEl ? transEl.textContent.trim() : '';
            const pageUrl = window.location.origin + window.location.pathname + `#surat=${surahNum}&ayat=${ayatNum}`;
            
            const msg = `📖 *QS. ${surahName} [${surahNum}] : Ayat ${ayatNum}*\\n\\n${arab}\\n\\n*Artinya:*\\n"${trans}"\\n\\n🔗 *Al-Qur'an Tematis:*\\n${pageUrl}`;
            const waUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(msg)}`;
            window.open(waUrl, '_blank');
        }

        window.addEventListener('scroll', () => {
            const btn = document.getElementById('btn-back-to-top');
            if (btn) {
                if (window.scrollY > 350) {
                    btn.classList.add('show');
                } else {
                    btn.classList.remove('show');
                }
            }
        });

        // Initialize font scale on startup
        initFontScale();
"""

if 'function initFontScale' not in html:
    html = html.replace('    </script>', js_functions + '\n    </script>')
    print("Added helper JavaScript functions.")

# 8. Synchronize direct ayat input in onSearchSurahChange and onSearchAyatChange and stepAyat
old_update_stepper = """        function updateStepperButtons() {
            const btnPrev = document.getElementById('btn-ayat-prev');
            const btnNext = document.getElementById('btn-ayat-next');
            const surahInfo = SURAH_LIST.find(s => s.no == currentSearchSurah);
            const totalAyat = surahInfo ? surahInfo.ayat : 1;

            if (btnPrev) btnPrev.disabled = (currentSearchAyat <= 1);
            if (btnNext) btnNext.disabled = (currentSearchAyat >= totalAyat);
        }"""

new_update_stepper = """        function updateStepperButtons() {
            const btnPrev = document.getElementById('btn-ayat-prev');
            const btnNext = document.getElementById('btn-ayat-next');
            const surahInfo = SURAH_LIST.find(s => s.no == currentSearchSurah);
            const totalAyat = surahInfo ? surahInfo.ayat : 1;

            if (btnPrev) btnPrev.disabled = (currentSearchAyat <= 1);
            if (btnNext) btnNext.disabled = (currentSearchAyat >= totalAyat);

            // Sync direct input box and hint
            const inputDirect = document.getElementById('input-search-ayat-num');
            if (inputDirect) {
                inputDirect.max = totalAyat;
                inputDirect.value = currentSearchAyat;
            }
            const hint = document.getElementById('ayat-range-hint');
            if (hint) {
                hint.textContent = `(1–${totalAyat})`;
            }

            // Sync URL hash
            if (activeMainMode === 'search') {
                history.replaceState(null, '', `#surat=${currentSearchSurah}&ayat=${currentSearchAyat}`);
            }
        }"""

if old_update_stepper in html:
    html = html.replace(old_update_stepper, new_update_stepper)
    print("Updated updateStepperButtons with direct input sync and URL hash.")

# 9. Handle hash in checkAutoNav
old_check_auto_nav = """        function checkAutoNav() {
            const savedTema = sessionStorage.getItem('active_tema');"""

new_check_auto_nav = """        function checkAutoNav() {
            // Check URL hash first for deep linking (#surat=2&ayat=255)
            const hash = window.location.hash;
            if (hash && hash.includes('surat=')) {
                try {
                    const params = new URLSearchParams(hash.replace('#', ''));
                    const s = parseInt(params.get('surat'));
                    const a = parseInt(params.get('ayat'));
                    if (s && a) {
                        setTimeout(() => lookupVerseInSearch(s, a), 100);
                        return;
                    }
                } catch(e) {
                    console.warn("Error parsing URL hash:", e);
                }
            }

            const savedTema = sessionStorage.getItem('active_tema');"""

if old_check_auto_nav in html:
    html = html.replace(old_check_auto_nav, new_check_auto_nav)
    print("Updated checkAutoNav with URL hash deep linking.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved all enhancements to index.html successfully!")
