# apply_deeplink.py
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

orig_content = content

# 1. Add CSS for Uraian deep link & action buttons
target_css_1 = """.uraian-group-card.is-collapsed .group-cards-container {
            display: none;
        }"""

replacement_css_1 = """.uraian-group-card.is-collapsed .group-cards-container {
            display: none;
        }

        /* Deep Link & Action Buttons for Uraian */
        .group-header-actions {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            flex-shrink: 0;
            margin-top: 0.15rem;
        }
        .uraian-action-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.38rem 0.75rem;
            font-size: 0.78rem;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid transparent;
            user-select: none;
            line-height: 1;
            white-space: nowrap;
        }
        .uraian-copy-btn {
            background: rgba(20, 184, 166, 0.12);
            color: #2dd4bf;
            border-color: rgba(20, 184, 166, 0.3);
        }
        .uraian-copy-btn:hover {
            background: rgba(20, 184, 166, 0.25);
            border-color: #2dd4bf;
            color: #ffffff;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(20, 184, 166, 0.25);
        }
        .uraian-copy-btn.copied {
            background: rgba(16, 185, 129, 0.25);
            color: #34d399;
            border-color: #34d399;
        }
        .uraian-wa-btn {
            background: rgba(37, 211, 102, 0.12);
            color: #25d366;
            border-color: rgba(37, 211, 102, 0.3);
        }
        .uraian-wa-btn:hover {
            background: rgba(37, 211, 102, 0.25);
            border-color: #25d366;
            color: #ffffff;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(37, 211, 102, 0.25);
        }"""

assert target_css_1 in content, "target_css_1 not found"
content = content.replace(target_css_1, replacement_css_1, 1)

# 2. Add Uraian pulse animation CSS
target_css_2 = """.verse-highlight-pulse {
            animation: highlightGlow 3.5s ease;
        }
        @keyframes highlightGlow {
            0% { box-shadow: 0 0 0 0 rgba(20, 184, 166, 0.8); border-color: #2dd4bf; }
            30% { box-shadow: 0 0 35px 8px rgba(20, 184, 166, 0.6); border-color: #2dd4bf; }
            70% { box-shadow: 0 0 25px 4px rgba(20, 184, 166, 0.4); border-color: #2dd4bf; }
            100% { box-shadow: 0 0 0 0 rgba(20, 184, 166, 0); }
        }"""

replacement_css_2 = """.verse-highlight-pulse {
            animation: highlightGlow 3.5s ease;
        }
        @keyframes highlightGlow {
            0% { box-shadow: 0 0 0 0 rgba(20, 184, 166, 0.8); border-color: #2dd4bf; }
            30% { box-shadow: 0 0 35px 8px rgba(20, 184, 166, 0.6); border-color: #2dd4bf; }
            70% { box-shadow: 0 0 25px 4px rgba(20, 184, 166, 0.4); border-color: #2dd4bf; }
            100% { box-shadow: 0 0 0 0 rgba(20, 184, 166, 0); }
        }
        .uraian-highlight-pulse {
            animation: uraianGlow 3.5s ease;
        }
        @keyframes uraianGlow {
            0% { box-shadow: 0 0 0 0 rgba(20, 184, 166, 0.8); border-color: #2dd4bf; transform: scale(1); }
            25% { box-shadow: 0 0 35px 8px rgba(20, 184, 166, 0.6); border-color: #2dd4bf; transform: scale(1.008); }
            70% { box-shadow: 0 0 25px 4px rgba(20, 184, 166, 0.4); border-color: #2dd4bf; transform: scale(1); }
            100% { box-shadow: 0 0 0 0 rgba(20, 184, 166, 0); }
        }"""

assert target_css_2 in content, "target_css_2 not found"
content = content.replace(target_css_2, replacement_css_2, 1)

# 3. Add responsive styles for mobile
target_css_3 = """.search-action-btns-left,
            .search-action-btns-right {
                justify-content: center;
            }
        }"""

replacement_css_3 = """.search-action-btns-left,
            .search-action-btns-right {
                justify-content: center;
            }
            .group-header-banner {
                flex-wrap: wrap;
            }
            .group-header-actions {
                width: 100%;
                justify-content: flex-end;
                margin-top: 0.5rem;
            }
        }"""

assert target_css_3 in content, "target_css_3 not found"
content = content.replace(target_css_3, replacement_css_3, 1)

# 4. Update LANG_UI_MAP
target_lang_en = """'Bagikan': 'Share',
                'Bagikan ke WhatsApp': 'Share to WhatsApp',"""
replacement_lang_en = """'Bagikan': 'Share',
                'Salin Link': 'Copy Link',
                'Tersalin!': 'Copied!',
                'Bagikan ke WhatsApp': 'Share to WhatsApp',"""

assert target_lang_en in content, "target_lang_en not found"
content = content.replace(target_lang_en, replacement_lang_en, 1)

target_lang_ar = """'Bagikan': 'مشاركة',
                'Cari Ayat': 'بحث عن الآية',"""
replacement_lang_ar = """'Bagikan': 'مشاركة',
                'Salin Link': 'نسخ الرابط',
                'Tersalin!': 'تم النسخ!',
                'Bagikan ke WhatsApp': 'مشاركة عبر واتساب',
                'Cari Ayat': 'بحث عن الآية',"""

assert target_lang_ar in content, "target_lang_ar not found"
content = content.replace(target_lang_ar, replacement_lang_ar, 1)

target_lang_ms = """'Bagikan': 'Kongsi',
                'Cari Ayat': 'Cari Ayat',"""
replacement_lang_ms = """'Bagikan': 'Kongsi',
                'Salin Link': 'Salin Pautan',
                'Tersalin!': 'Disalin!',
                'Bagikan ke WhatsApp': 'Kongsi ke WhatsApp',
                'Cari Ayat': 'Cari Ayat',"""

assert target_lang_ms in content, "target_lang_ms not found"
content = content.replace(target_lang_ms, replacement_lang_ms, 1)

# 5. Add deep link helper functions & upgrade checkAutoNav
target_autonav = """        function checkAutoNav() {
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

            const savedTema = sessionStorage.getItem('active_tema');
            const savedPokok = sessionStorage.getItem('active_pokok');
            const savedSub = sessionStorage.getItem('active_sub');

            if (savedTema && quranData[savedTema]) {
                elTema.value = savedTema;
                populateSelect(elPokok, naturalSort(Object.keys(quranData[savedTema])), "Pilih Pokok Bahasan");
                if (savedPokok && quranData[savedTema][savedPokok]) {
                    elPokok.value = savedPokok;
                    populateSelect(elSub, naturalSort(Object.keys(quranData[savedTema][savedPokok])), "Pilih Sub Pokok Bahasan");
                    if (savedSub && quranData[savedTema][savedPokok][savedSub]) {
                        elSub.value = savedSub;
                        renderContentAll(savedTema, savedPokok, savedSub);
                        return;
                    }
                }
            }

            // Default initial state: open the first Tema, first Pokok, and first Sub
            const temaKeys = naturalSort(Object.keys(quranData));
            if (temaKeys.length > 0) {
                const firstTema = temaKeys[0];
                elTema.value = firstTema;
                const pokokKeys = naturalSort(Object.keys(quranData[firstTema] || {}));
                populateSelect(elPokok, pokokKeys, "Pilih Pokok Bahasan");
                if (pokokKeys.length > 0) {
                    const firstPokok = pokokKeys[0];
                    elPokok.value = firstPokok;
                    const subKeys = naturalSort(Object.keys(quranData[firstTema][firstPokok] || {}));
                    populateSelect(elSub, subKeys, "Pilih Sub Pokok Bahasan");
                    if (subKeys.length > 0) {
                        const firstSub = subKeys[0];
                        elSub.value = firstSub;
                        renderContentAll(firstTema, firstPokok, firstSub);
                    }
                }
            }
        }"""

replacement_autonav = """        function getParsedUrlParams() {
            let searchStr = window.location.search ? window.location.search.substring(1) : '';
            let hashStr = window.location.hash ? window.location.hash.substring(1) : '';
            if (hashStr.includes('?')) {
                const parts = hashStr.split('?');
                hashStr = parts[0] + '&' + parts[1];
            }
            return new URLSearchParams(searchStr + (searchStr && hashStr ? '&' : '') + hashStr);
        }

        function findUraianPath(uraianQuery) {
            if (!uraianQuery || !allThematicUraianList || !allThematicUraianList.length) return null;
            const cleanQ = decodeURIComponent(uraianQuery).trim().toLowerCase();
            if (!cleanQ) return null;

            // 1. Exact match
            let match = allThematicUraianList.find(item => item.uraian.toLowerCase() === cleanQ);
            if (match) return match;

            // 2. Starts with (e.g. "1.1.1.1" or "1.1.1.1." or code prefix)
            match = allThematicUraianList.find(item => item.uraian.toLowerCase().startsWith(cleanQ));
            if (match) return match;

            // 3. Substring match
            match = allThematicUraianList.find(item => item.uraian.toLowerCase().includes(cleanQ));
            if (match) return match;

            return null;
        }

        function getUraianDeepLink(uraianTitle, tema, pokok, sub) {
            if (!tema || !pokok || !sub) {
                const found = findUraianPath(uraianTitle);
                if (found) {
                    tema = found.tema;
                    pokok = found.pokok;
                    sub = found.sub;
                    uraianTitle = found.uraian;
                }
            }
            const hash = `tema=${encodeURIComponent(tema || '')}&pokok=${encodeURIComponent(pokok || '')}&sub=${encodeURIComponent(sub || '')}&uraian=${encodeURIComponent(uraianTitle)}`;
            const baseUrl = window.location.href.split('#')[0].split('?')[0];
            return `${baseUrl}#${hash}`;
        }

        function copyUraianLink(btn, event, encodedTitle) {
            if (event) event.stopPropagation();
            const uraianTitle = decodeURIComponent(encodedTitle);
            const link = getUraianDeepLink(uraianTitle, elTema ? elTema.value : '', elPokok ? elPokok.value : '', elSub ? elSub.value : '');

            const onCopiedSuccess = () => {
                showAIToast("Link Uraian berhasil disalin ke clipboard!");
                if (btn) {
                    const origHTML = btn.innerHTML;
                    btn.classList.add('copied');
                    btn.innerHTML = `
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span>Tersalin!</span>
                    `;
                    setTimeout(() => {
                        btn.classList.remove('copied');
                        btn.innerHTML = origHTML;
                    }, 2000);
                }
            };

            const fallbackCopy = (text) => {
                const ta = document.createElement('textarea');
                ta.value = text;
                ta.style.position = 'fixed';
                ta.style.left = '-9999px';
                document.body.appendChild(ta);
                ta.select();
                try {
                    document.execCommand('copy');
                    onCopiedSuccess();
                } catch(e) {
                    console.error("Fallback copy failed:", e);
                }
                document.body.removeChild(ta);
            };

            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(link).then(onCopiedSuccess).catch(() => fallbackCopy(link));
            } else {
                fallbackCopy(link);
            }
        }

        function shareUraianWhatsApp(event, encodedTitle) {
            if (event) event.stopPropagation();
            const uraianTitle = decodeURIComponent(encodedTitle);
            const found = findUraianPath(uraianTitle);
            const tema = found ? found.tema : (elTema ? elTema.value : '');
            const pokok = found ? found.pokok : (elPokok ? elPokok.value : '');
            const sub = found ? found.sub : (elSub ? elSub.value : '');
            const vCount = found ? found.verseCount : 0;
            const link = getUraianDeepLink(uraianTitle, tema, pokok, sub);

            const message = `*Al-Qur'an Tematis*\\n\\n` +
                `📖 *Uraian:* ${uraianTitle}\\n` +
                (tema ? `🏷️ *Tema:* ${tema}\\n` : '') +
                (pokok ? `📂 *Pokok:* ${pokok}\\n` : '') +
                (sub ? `📑 *Sub Pokok:* ${sub}\\n` : '') +
                (vCount > 0 ? `📊 *Jumlah Ayat:* ${vCount} ayat\\n\\n` : '\\n') +
                `Pelajari selengkapnya di tautan berikut:\\n${link}`;

            const waUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(message)}`;
            window.open(waUrl, '_blank');
        }

        function checkAutoNav() {
            if (!quranData || !Object.keys(quranData).length) return;

            const params = getParsedUrlParams();

            // 1. Check verse deep link (#surat=2&ayat=255)
            const s = parseInt(params.get('surat'));
            const a = parseInt(params.get('ayat'));
            if (s && a) {
                setTimeout(() => lookupVerseInSearch(s, a), 100);
                return;
            }

            // 2. Check Uraian deep link
            let paramUraian = params.get('uraian');
            const rawHash = (window.location.hash || '').replace(/^#/, '').trim();
            if (!paramUraian && rawHash && !rawHash.includes('=') && !rawHash.includes('&')) {
                paramUraian = decodeURIComponent(rawHash);
            }

            if (paramUraian) {
                let targetTema = params.get('tema');
                let targetPokok = params.get('pokok');
                let targetSub = params.get('sub');
                let targetUraian = decodeURIComponent(paramUraian);

                if (!targetTema || !targetPokok || !targetSub || !quranData[targetTema] || !quranData[targetTema][targetPokok] || !quranData[targetTema][targetPokok][targetSub]) {
                    const resolved = findUraianPath(targetUraian);
                    if (resolved) {
                        targetTema = resolved.tema;
                        targetPokok = resolved.pokok;
                        targetSub = resolved.sub;
                        targetUraian = resolved.uraian;
                    }
                }

                if (targetTema && targetPokok && targetSub && quranData[targetTema] && quranData[targetTema][targetPokok] && quranData[targetTema][targetPokok][targetSub]) {
                    setTimeout(() => {
                        navigateToThematicTopic(targetTema, targetPokok, targetSub, targetUraian);
                    }, 50);
                    return;
                }
            }

            // 3. Saved state from sessionStorage
            const savedTema = sessionStorage.getItem('active_tema');
            const savedPokok = sessionStorage.getItem('active_pokok');
            const savedSub = sessionStorage.getItem('active_sub');

            if (savedTema && quranData[savedTema]) {
                elTema.value = savedTema;
                populateSelect(elPokok, naturalSort(Object.keys(quranData[savedTema])), "Pilih Pokok Bahasan");
                if (savedPokok && quranData[savedTema][savedPokok]) {
                    elPokok.value = savedPokok;
                    populateSelect(elSub, naturalSort(Object.keys(quranData[savedTema][savedPokok])), "Pilih Sub Pokok Bahasan");
                    if (savedSub && quranData[savedTema][savedPokok][savedSub]) {
                        elSub.value = savedSub;
                        renderContentAll(savedTema, savedPokok, savedSub);
                        return;
                    }
                }
            }

            // 4. Default initial state
            const temaKeys = naturalSort(Object.keys(quranData));
            if (temaKeys.length > 0) {
                const firstTema = temaKeys[0];
                elTema.value = firstTema;
                const pokokKeys = naturalSort(Object.keys(quranData[firstTema] || {}));
                populateSelect(elPokok, pokokKeys, "Pilih Pokok Bahasan");
                if (pokokKeys.length > 0) {
                    const firstPokok = pokokKeys[0];
                    elPokok.value = firstPokok;
                    const subKeys = naturalSort(Object.keys(quranData[firstTema][firstPokok] || {}));
                    populateSelect(elSub, subKeys, "Pilih Sub Pokok Bahasan");
                    if (subKeys.length > 0) {
                        const firstSub = subKeys[0];
                        elSub.value = firstSub;
                        renderContentAll(firstTema, firstPokok, firstSub);
                    }
                }
            }
        }

        window.addEventListener('hashchange', checkAutoNav);"""

assert target_autonav in content, "target_autonav not found"
content = content.replace(target_autonav, replacement_autonav, 1)

# 6. Update toggleSingleGroup to sync URL hash
target_toggle = """            card.classList.toggle('is-collapsed');

            const groupCards = Array.from(document.querySelectorAll('.uraian-group-card'));"""

replacement_toggle = """            card.classList.toggle('is-collapsed');

            if (!card.classList.contains('is-collapsed')) {
                const titleEl = card.querySelector('.group-title');
                if (titleEl) {
                    const origTitle = titleEl.getAttribute('data-original') || titleEl.textContent.trim();
                    try {
                        const newUrl = getUraianDeepLink(origTitle, elTema ? elTema.value : '', elPokok ? elPokok.value : '', elSub ? elSub.value : '');
                        history.replaceState(null, '', newUrl);
                    } catch(e) {}
                }
            }

            const groupCards = Array.from(document.querySelectorAll('.uraian-group-card'));"""

assert target_toggle in content, "target_toggle not found"
content = content.replace(target_toggle, replacement_toggle, 1)

# 7. Update generateUraianGroupMarkup to include action buttons in header
target_markup = """                        <div class="group-header-left">
                            <h3 class="group-title" data-original="${uraianTitle}">${uraianTitle}</h3>
                            <div class="group-meta" data-count="${data && data.verses ? data.verses.length : 0}">
                                <span>📖 ${data && data.verses ? data.verses.length : 0} Ayat Al-Qur'an</span>
                            </div>
                        </div>
                        <div class="group-toggle-icon" title="Buka / Tutup Kelompok">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>"""

replacement_markup = """                        <div class="group-header-left">
                            <h3 class="group-title" data-original="${uraianTitle}">${uraianTitle}</h3>
                            <div class="group-meta" data-count="${data && data.verses ? data.verses.length : 0}">
                                <span>📖 ${data && data.verses ? data.verses.length : 0} Ayat Al-Qur'an</span>
                            </div>
                        </div>
                        <div class="group-header-actions">
                            <button class="uraian-action-btn uraian-copy-btn" onclick="copyUraianLink(this, event, '${encodeURIComponent(uraianTitle)}')" title="Salin Deep Link Uraian Ini">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
                                <span data-i18n-orig="Salin Link">Salin Link</span>
                            </button>
                            <button class="uraian-action-btn uraian-wa-btn" onclick="shareUraianWhatsApp(event, '${encodeURIComponent(uraianTitle)}')" title="Bagikan ke WhatsApp">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                                <span>WA</span>
                            </button>
                            <div class="group-toggle-icon" title="Buka / Tutup Kelompok">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                                    <polyline points="6 9 12 15 18 9"></polyline>
                                </svg>
                            </div>
                        </div>"""

assert target_markup in content, "target_markup not found"
content = content.replace(target_markup, replacement_markup, 1)

# 8. Update keyword search result card to include Salin Link
target_kw_btn = """                            <button class="btn-jump-thematic" style="padding: 0.6rem 1.1rem; font-size: 0.88rem;" onclick="navigateToThematicTopic('${u.tema.replace(/'/g, "\\\\'")}', '${u.pokok.replace(/'/g, "\\\\'")}', '${u.sub.replace(/'/g, "\\\\'")}', '${u.uraian.replace(/'/g, "\\\\'")}', ${u.sampleVerses[0] ? u.sampleVerses[0].surah_num : 1}, ${u.sampleVerses[0] ? u.sampleVerses[0].ayat_num : 1})">
                                <span>${lblOpenTopic}</span>
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                            </button>"""

replacement_kw_btn = """                            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                                <button class="btn-jump-thematic" style="padding: 0.6rem 1.1rem; font-size: 0.88rem; flex: 1;" onclick="navigateToThematicTopic('${u.tema.replace(/'/g, "\\\\'")}', '${u.pokok.replace(/'/g, "\\\\'")}', '${u.sub.replace(/'/g, "\\\\'")}', '${u.uraian.replace(/'/g, "\\\\'")}', ${u.sampleVerses[0] ? u.sampleVerses[0].surah_num : 1}, ${u.sampleVerses[0] ? u.sampleVerses[0].ayat_num : 1})">
                                    <span>${lblOpenTopic}</span>
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                </button>
                                <button class="uraian-action-btn uraian-copy-btn" style="padding: 0.6rem 0.9rem;" onclick="copyUraianLink(this, event, '${encodeURIComponent(u.uraian)}')" title="Salin Deep Link">
                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
                                    <span data-i18n-orig="Salin Link">Salin Link</span>
                                </button>
                            </div>"""

assert target_kw_btn in content, "target_kw_btn not found"
content = content.replace(target_kw_btn, replacement_kw_btn, 1)

# 9. Update verse search thematic match card to include Salin Link
target_verse_thematic_btn = """                            <button class="btn-jump-thematic" onclick="navigateToThematicTopic('${t.tema.replace(/'/g, "\\\\'") }', '${t.pokok.replace(/'/g, "\\\\'") }', '${t.sub.replace(/'/g, "\\\\'") }', '${t.uraian.replace(/'/g, "\\\\'") }', ${surahNum}, ${ayatNum})">
                                <span data-i18n-orig="Buka di Halaman Tematik">Buka di Halaman Tematik</span>
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                            </button>"""

replacement_verse_thematic_btn = """                            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                                <button class="btn-jump-thematic" style="flex: 1;" onclick="navigateToThematicTopic('${t.tema.replace(/'/g, "\\\\'") }', '${t.pokok.replace(/'/g, "\\\\'") }', '${t.sub.replace(/'/g, "\\\\'") }', '${t.uraian.replace(/'/g, "\\\\'") }', ${surahNum}, ${ayatNum})">
                                    <span data-i18n-orig="Buka di Halaman Tematik">Buka di Halaman Tematik</span>
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                </button>
                                <button class="uraian-action-btn uraian-copy-btn" onclick="copyUraianLink(this, event, '${encodeURIComponent(t.uraian)}')" title="Salin Deep Link">
                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
                                    <span data-i18n-orig="Salin Link">Salin Link</span>
                                </button>
                            </div>"""

assert target_verse_thematic_btn in content, "target_verse_thematic_btn not found"
content = content.replace(target_verse_thematic_btn, replacement_verse_thematic_btn, 1)

# 10. Update navigateToThematicTopic to scroll/pulse group and handle case-insensitivity
target_nav = """                        const groupCards = document.querySelectorAll('.uraian-group-card');
                        let targetGroup = null;
                        groupCards.forEach(card => {
                            const titleEl = card.querySelector('.group-title');
                            if (titleEl && titleEl.getAttribute('data-original') === uraian) {
                                targetGroup = card;
                                card.classList.remove('is-collapsed');
                            }
                        });

                        setTimeout(() => {
                            let targetVerse = null;
                            if (targetGroup) {
                                const verseWrappers = targetGroup.querySelectorAll('.verse-item-wrapper');
                                verseWrappers.forEach(vw => {
                                    const front = vw.querySelector('.flip-card-front');
                                    if (front && parseInt(front.getAttribute('data-surah')) === surahNum && parseInt(front.getAttribute('data-ayat')) === ayatNum) {
                                        targetVerse = vw;
                                    }
                                });
                            }

                            const elToScroll = targetVerse || targetGroup;
                            if (elToScroll) {
                                elToScroll.scrollIntoView({ behavior: 'smooth', block: 'center' });
                                if (targetVerse) {
                                    targetVerse.classList.add('verse-highlight-pulse');
                                    setTimeout(() => targetVerse.classList.remove('verse-highlight-pulse'), 3500);
                                }
                            }
                        }, 200);"""

replacement_nav = """                        const groupCards = document.querySelectorAll('.uraian-group-card');
                        let targetGroup = null;
                        groupCards.forEach(card => {
                            const titleEl = card.querySelector('.group-title');
                            if (titleEl) {
                                const orig = (titleEl.getAttribute('data-original') || titleEl.textContent || '').trim();
                                if (orig === uraian || orig.toLowerCase() === uraian.toLowerCase()) {
                                    targetGroup = card;
                                    card.classList.remove('is-collapsed');
                                }
                            }
                        });

                        setTimeout(() => {
                            let targetVerse = null;
                            if (targetGroup && surahNum && ayatNum) {
                                const verseWrappers = targetGroup.querySelectorAll('.verse-item-wrapper');
                                verseWrappers.forEach(vw => {
                                    const front = vw.querySelector('.flip-card-front');
                                    if (front && parseInt(front.getAttribute('data-surah')) === surahNum && parseInt(front.getAttribute('data-ayat')) === ayatNum) {
                                        targetVerse = vw;
                                    }
                                });
                            }

                            const elToScroll = targetVerse || targetGroup;
                            if (elToScroll) {
                                elToScroll.scrollIntoView({ behavior: 'smooth', block: 'center' });
                                if (targetVerse) {
                                    targetVerse.classList.add('verse-highlight-pulse');
                                    setTimeout(() => targetVerse.classList.remove('verse-highlight-pulse'), 3500);
                                } else if (targetGroup) {
                                    targetGroup.classList.add('uraian-highlight-pulse');
                                    setTimeout(() => targetGroup.classList.remove('uraian-highlight-pulse'), 3500);
                                }
                            }

                            if (targetGroup) {
                                const meta = targetGroup.querySelector('.group-meta');
                                const count = meta ? parseInt(meta.getAttribute('data-count') || '0') : 0;
                                if (count > 0 && elHint) {
                                    elHint.style.display = 'flex';
                                }
                            }
                        }, 200);"""

assert target_nav in content, "target_nav not found"
content = content.replace(target_nav, replacement_nav, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("All 10 deep link modifications successfully applied to index.html!")
