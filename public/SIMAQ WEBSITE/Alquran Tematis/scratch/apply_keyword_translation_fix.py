import re
import shutil

def main():
    html_file = 'index.html'
    backup_file = 'scratch/index.html.before_kw_trans.bak'
    shutil.copy2(html_file, backup_file)
    print("Backup created at", backup_file)

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update HTML in #keyword-nav-container and #keyword-view-wrapper to include data-i18n-orig and data-i18n-placeholder
    old_keyword_nav = """        <!-- Keyword Search Navigation (Mode 3) -->
        <div id="keyword-nav-container" class="search-nav-card" style="display: none;">
            <div class="search-console-header">
                <div class="search-console-title">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    <span data-i18n-orig="Pencarian Kata: Uraian & Ayat">Pencarian Kata: Uraian & Ayat</span>
                </div>
                <div class="search-console-subtitle" data-i18n-orig="Cari topik uraian tematis dan teks terjemahan ayat secara instan">Cari topik bahasan/uraian tematis dan teks terjemahan ayat berdasarkan kata kunci secara instan</div>
            </div>

            <!-- Keyword Search Input -->
            <div class="smart-search-box-wrap">
                <div class="smart-search-input-inner">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" class="search-icon"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    <input type="text" id="keyword-search-input" class="smart-search-input" placeholder="Ketik kata pencarian (contoh: sabar, riba, shalat, taubat, rezeki, surga)..." oninput="onKeywordInput(this.value)" onkeydown="if(event.key==='Enter')executeKeywordSearch()" autocomplete="off">
                    <button id="btn-clear-keyword-search" class="btn-clear-input" onclick="clearKeywordSearch()" style="display: none;" title="Hapus pencarian">✕</button>
                    <button class="btn-keyword-submit" onclick="executeKeywordSearch()">Cari</button>
                </div>
            </div>

            <!-- Filter Chips -->
            <div class="keyword-filters-row">
                <span class="filter-label">Filter Hasil:</span>
                <button id="filter-pill-all" class="filter-pill-btn active" onclick="setKeywordFilter('all')">Semua Hasil</button>
                <button id="filter-pill-uraian" class="filter-pill-btn" onclick="setKeywordFilter('uraian')">Hanya Uraian Tematis</button>
                <button id="filter-pill-ayat" class="filter-pill-btn" onclick="setKeywordFilter('ayat')">Hanya Teks Terjemahan Ayat</button>
            </div>

            <!-- Popular Search Keywords -->
            <div class="popular-verses-row" style="margin-top: 1rem;">
                <span class="popular-label">💡 Kata Kunci Populer:</span>
                <button class="popular-verse-chip" onclick="searchKeywordTag('sabar')">Sabar</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('riba')">Riba</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('shalat')">Shalat</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('taubat')">Taubat</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('rezeki')">Rezeki</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('surga')">Surga</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('neraka')">Neraka</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('orang tua')">Orang Tua</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('sedekah')">Sedekah</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('kiamat')">Kiamat</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('syukur')">Syukur</button>
            </div>
        </div>

        <!-- Keyword Search Content View (Mode 3) -->
        <div id="keyword-view-wrapper" style="display: none;">
            <div id="keyword-content-area">
                <div class="empty-state">
                    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="margin: 0 auto 1rem; display: block; color: var(--accent); opacity: 0.8;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    Ketik kata kunci di atas atau pilih salah satu kata populer untuk mencari uraian tematis dan ayat Al-Qur'an.
                </div>
            </div>
        </div>"""

    new_keyword_nav = """        <!-- Keyword Search Navigation (Mode 3) -->
        <div id="keyword-nav-container" class="search-nav-card" style="display: none;">
            <div class="search-console-header">
                <div class="search-console-title">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    <span data-i18n-orig="Pencarian Kata: Uraian & Ayat">Pencarian Kata: Uraian & Ayat</span>
                </div>
                <div class="search-console-subtitle" data-i18n-orig="Cari topik uraian tematis dan teks terjemahan ayat secara instan">Cari topik bahasan/uraian tematis dan teks terjemahan ayat berdasarkan kata kunci secara instan</div>
            </div>

            <!-- Keyword Search Input -->
            <div class="smart-search-box-wrap">
                <div class="smart-search-input-inner">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" class="search-icon"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    <input type="text" id="keyword-search-input" class="smart-search-input" placeholder="Ketik kata pencarian (contoh: sabar, riba, shalat, taubat, rezeki, surga)..." data-i18n-placeholder="Ketik kata pencarian (contoh: sabar, riba, shalat, taubat, rezeki, surga)..." oninput="onKeywordInput(this.value)" onkeydown="if(event.key==='Enter')executeKeywordSearch()" autocomplete="off">
                    <button id="btn-clear-keyword-search" class="btn-clear-input" onclick="clearKeywordSearch()" style="display: none;" title="Hapus pencarian">✕</button>
                    <button class="btn-keyword-submit" onclick="executeKeywordSearch()" data-i18n-orig="Cari">Cari</button>
                </div>
            </div>

            <!-- Filter Chips -->
            <div class="keyword-filters-row">
                <span class="filter-label" data-i18n-orig="Filter Hasil:">Filter Hasil:</span>
                <button id="filter-pill-all" class="filter-pill-btn active" onclick="setKeywordFilter('all')" data-i18n-orig="Semua Hasil">Semua Hasil</button>
                <button id="filter-pill-uraian" class="filter-pill-btn" onclick="setKeywordFilter('uraian')" data-i18n-orig="Hanya Uraian Tematis">Hanya Uraian Tematis</button>
                <button id="filter-pill-ayat" class="filter-pill-btn" onclick="setKeywordFilter('ayat')" data-i18n-orig="Hanya Teks Terjemahan Ayat">Hanya Teks Terjemahan Ayat</button>
            </div>

            <!-- Popular Search Keywords -->
            <div class="popular-verses-row" style="margin-top: 1rem;">
                <span class="popular-label" data-i18n-orig="💡 Kata Kunci Populer:">💡 Kata Kunci Populer:</span>
                <button class="popular-verse-chip" onclick="searchKeywordTag('sabar')" data-i18n-orig="Sabar">Sabar</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('riba')" data-i18n-orig="Riba">Riba</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('shalat')" data-i18n-orig="Shalat">Shalat</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('taubat')" data-i18n-orig="Taubat">Taubat</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('rezeki')" data-i18n-orig="Rezeki">Rezeki</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('surga')" data-i18n-orig="Surga">Surga</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('neraka')" data-i18n-orig="Neraka">Neraka</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('orang tua')" data-i18n-orig="Orang Tua">Orang Tua</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('sedekah')" data-i18n-orig="Sedekah">Sedekah</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('kiamat')" data-i18n-orig="Kiamat">Kiamat</button>
                <button class="popular-verse-chip" onclick="searchKeywordTag('syukur')" data-i18n-orig="Syukur">Syukur</button>
            </div>
        </div>

        <!-- Keyword Search Content View (Mode 3) -->
        <div id="keyword-view-wrapper" style="display: none;">
            <div id="keyword-content-area">
                <div class="empty-state" data-i18n-orig="Ketik kata kunci di atas atau pilih salah satu kata populer untuk mencari uraian tematis dan ayat Al-Qur'an.">
                    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="margin: 0 auto 1rem; display: block; color: var(--accent); opacity: 0.8;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    <span data-i18n-orig="Ketik kata kunci di atas atau pilih salah satu kata populer untuk mencari uraian tematis dan ayat Al-Qur'an.">Ketik kata kunci di atas atau pilih salah satu kata populer untuk mencari uraian tematis dan ayat Al-Qur'an.</span>
                </div>
            </div>
        </div>"""

    if old_keyword_nav in content:
        content = content.replace(old_keyword_nav, new_keyword_nav, 1)
        print("Updated keyword nav markup with data-i18n-orig successfully.")
    else:
        print("ERROR: old_keyword_nav not found!")
        return

    # 2. Add Smart Search input placeholder data-i18n-placeholder
    old_smart_input = 'placeholder="Ketik nama surat & ayat (contoh: Al-Baqarah 255, 36:82, Yasin 82, Kahfi 10, An-Nas)..."'
    new_smart_input = 'placeholder="Ketik nama surat & ayat (contoh: Al-Baqarah 255, 36:82, Yasin 82, Kahfi 10, An-Nas)..." data-i18n-placeholder="Ketik nama surat & ayat (contoh: Al-Baqarah 255, 36:82, Yasin 82, Kahfi 10, An-Nas)..."'
    if old_smart_input in content:
        content = content.replace(old_smart_input, new_smart_input, 1)
        print("Updated smart search input with data-i18n-placeholder.")

    # 3. Add getI18nText helper and synonyms, and update executeKeywordSearch & renderKeywordSearchResults
    # Let's inspect where onKeywordInput starts
    old_kw_search_code_start = "        let keywordFilterMode = 'all'; // 'all', 'uraian', 'ayat'"
    
    new_kw_helpers = """        const KEYWORD_SYNONYMS = {
            'patience': 'sabar',
            'patient': 'sabar',
            'usury': 'riba',
            'interest': 'riba',
            'prayer': 'shalat',
            'prayers': 'shalat',
            'repentance': 'taubat',
            'provision': 'rezeki',
            'sustenance': 'rezeki',
            'paradise': 'surga',
            'heaven': 'surga',
            'hell': 'neraka',
            'hellfire': 'neraka',
            'parents': 'orang tua',
            'parent': 'orang tua',
            'father': 'orang tua',
            'mother': 'orang tua',
            'charity': 'sedekah',
            'alms': 'sedekah',
            'doomsday': 'kiamat',
            'judgment': 'kiamat',
            'resurrection': 'kiamat',
            'gratitude': 'syukur',
            'grateful': 'syukur',
            'fasting': 'puasa',
            'human': 'manusia',
            'creation': 'penciptaan'
        };

        function getI18nText(key) {
            const langSelect = document.getElementById('tts-language');
            const lang = langSelect ? langSelect.value : 'id-ID';
            const cfg = LANG_CONFIG[lang] || LANG_CONFIG['id-ID'];
            const targetLang = cfg.code;
            if (targetLang === 'id') return key;
            const dict = LANG_UI_MAP[targetLang];
            if (dict && dict[key]) return dict[key];
            return key;
        }

        let keywordFilterMode = 'all'; // 'all', 'uraian', 'ayat'"""

    if old_kw_search_code_start in content:
        content = content.replace(old_kw_search_code_start, new_kw_helpers, 1)
        print("Added getI18nText and KEYWORD_SYNONYMS successfully.")
    else:
        print("ERROR: old_kw_search_code_start not found!")
        return

    # 4. Enhance executeKeywordSearch to support multilingual query and synonyms
    old_execute_kw = """        function executeKeywordSearch() {
            stopTTS();
            const input = document.getElementById('keyword-search-input');
            const area = document.getElementById('keyword-content-area');
            if (!input || !area) return;

            const q = input.value.trim();
            if (!q || q.length < 2) {
                area.innerHTML = `<div class="empty-state">Silakan masukkan minimal 2 huruf untuk melakukan pencarian.</div>`;
                return;
            }

            lastSearchedKeyword = q;
            const qLower = q.toLowerCase();

            // 1. Search in all Uraian topics
            let matchedUraian = [];
            if (keywordFilterMode === 'all' || keywordFilterMode === 'uraian') {
                allThematicUraianList.forEach(item => {
                    const uMatch = item.uraian.toLowerCase().includes(qLower);
                    const sMatch = item.sub.toLowerCase().includes(qLower);
                    const pMatch = item.pokok.toLowerCase().includes(qLower);
                    const tMatch = item.tema.toLowerCase().includes(qLower);

                    if (uMatch || sMatch || pMatch || tMatch) {
                        matchedUraian.push(item);
                    }
                });
            }

            // 2. Search in all Verses (Indonesian translation and Arabic)
            let matchedVerses = [];
            if (keywordFilterMode === 'all' || keywordFilterMode === 'ayat') {
                allThematicVersesList.forEach(verse => {
                    const indoMatch = verse.indo && verse.indo.toLowerCase().includes(qLower);
                    const nameMatch = verse.surah_name && verse.surah_name.toLowerCase().includes(qLower);
                    const arabMatch = verse.arab && verse.arab.includes(q);

                    if (indoMatch || nameMatch || arabMatch) {
                        matchedVerses.push(verse);
                    }
                });
            }

            renderKeywordSearchResults(q, matchedUraian, matchedVerses);
        }"""

    new_execute_kw = """        function executeKeywordSearch() {
            stopTTS();
            const input = document.getElementById('keyword-search-input');
            const area = document.getElementById('keyword-content-area');
            if (!input || !area) return;

            const q = input.value.trim();
            if (!q || q.length < 2) {
                const minCharText = getI18nText("Silakan masukkan minimal 2 huruf untuk melakukan pencarian.");
                area.innerHTML = `<div class="empty-state">${minCharText}</div>`;
                return;
            }

            lastSearchedKeyword = q;
            const qLower = q.toLowerCase();
            const synonym = KEYWORD_SYNONYMS[qLower] || "";

            // 1. Search in all Uraian topics (matching query or synonym, plus cached translations)
            let matchedUraian = [];
            if (keywordFilterMode === 'all' || keywordFilterMode === 'uraian') {
                allThematicUraianList.forEach(item => {
                    const uMatch = item.uraian.toLowerCase().includes(qLower) || (synonym && item.uraian.toLowerCase().includes(synonym));
                    const sMatch = item.sub.toLowerCase().includes(qLower) || (synonym && item.sub.toLowerCase().includes(synonym));
                    const pMatch = item.pokok.toLowerCase().includes(qLower) || (synonym && item.pokok.toLowerCase().includes(synonym));
                    const tMatch = item.tema.toLowerCase().includes(qLower) || (synonym && item.tema.toLowerCase().includes(synonym));

                    if (uMatch || sMatch || pMatch || tMatch) {
                        matchedUraian.push(item);
                    }
                });
            }

            // 2. Search in all Verses (Indonesian translation, Arabic, and any cached verse translations)
            let matchedVerses = [];
            if (keywordFilterMode === 'all' || keywordFilterMode === 'ayat') {
                allThematicVersesList.forEach(verse => {
                    const indoMatch = (verse.indo && verse.indo.toLowerCase().includes(qLower)) || (synonym && verse.indo && verse.indo.toLowerCase().includes(synonym));
                    const nameMatch = verse.surah_name && verse.surah_name.toLowerCase().includes(qLower);
                    const arabMatch = verse.arab && verse.arab.includes(q);

                    if (indoMatch || nameMatch || arabMatch) {
                        matchedVerses.push(verse);
                    }
                });
            }

            renderKeywordSearchResults(q, matchedUraian, matchedVerses);
        }"""

    if old_execute_kw in content:
        content = content.replace(old_execute_kw, new_execute_kw, 1)
        print("Updated executeKeywordSearch with multilingual synonyms successfully.")
    else:
        print("ERROR: old_execute_kw not found!")
        return

    # 5. Update renderKeywordSearchResults to use getI18nText and translate dynamic results
    old_render_kw_pattern = re.compile(
        r'function renderKeywordSearchResults\(keyword, matchedUraian, matchedVerses\) \{[\s\S]*?area\.innerHTML = markup;\s*\}',
        re.MULTILINE
    )

    new_render_kw = """        function renderKeywordSearchResults(keyword, matchedUraian, matchedVerses) {
            const area = document.getElementById('keyword-content-area');
            if (!area) return;

            const langSelect = document.getElementById('tts-language');
            const lang = langSelect ? langSelect.value : 'id-ID';
            const cfg = LANG_CONFIG[lang] || LANG_CONFIG['id-ID'];
            const targetLang = cfg.code;

            const totalUraian = matchedUraian.length;
            const totalVerses = matchedVerses.length;
            const grandTotal = totalUraian + totalVerses;

            const lblSearchFor = getI18nText("🔍 Hasil pencarian untuk:");
            const lblUraianBadge = getI18nText("Uraian Tematis");
            const lblVersesBadge = getI18nText("Ayat Al-Qur'an");
            const lblSecTopics = getI18nText("📝 Topik & Uraian Tematis Terkait");
            const lblTopicsFound = getI18nText("Topik Ditemukan");
            const lblSecVerses = getI18nText("📖 Ayat-Ayat Al-Qur'an Terkait");
            const lblVersesFound = getI18nText("Ayat Ditemukan");
            const lblOpenTopic = getI18nText("Buka Topik Tematis Ini");
            const lblListen = getI18nText("Dengarkan");
            const lblAskAI = getI18nText("Tanya AI");
            const lblCopy = getI18nText("Salin");
            const lblShare = getI18nText("Bagikan");
            const lblOpenSearch = getI18nText("🔍 Buka di Pencarian Ayat");
            const lblOpenThematic = getI18nText("Buka Tematik ➡️");
            const lblTheme = getI18nText("Tema:");
            const lblSubject = getI18nText("Pokok:");
            const lblSubtopic = getI18nText("Sub Pokok:");

            if (grandTotal === 0) {
                const notFoundText = getI18nText("Tidak ditemukan hasil untuk kata kunci");
                const tipText = getI18nText("Saran: Periksa kembali ejaan kata, gunakan kata dasar (misal sabar, bukan bersabarlah), atau coba kata populer di atas.");
                area.innerHTML = `
                    <div class="empty-state" style="padding: 3rem 1.5rem;">
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="margin: 0 auto 1rem; display: block; color: #ef4444; opacity: 0.8;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
                        ${notFoundText} "<strong>${escapeHtml(keyword)}</strong>".
                        <div style="font-size: 0.88rem; color: #94a3b8; margin-top: 0.75rem;">
                            ${tipText}
                        </div>
                    </div>
                `;
                return;
            }

            let markup = `
                <div class="keyword-stats-banner">
                    <div class="keyword-stats-info">
                        <span>${lblSearchFor} <strong>"${escapeHtml(keyword)}"</strong></span>
                    </div>
                    <div class="keyword-stats-badges">
                        ${keywordFilterMode !== 'ayat' ? `<span class="thematic-match-badge" style="background: rgba(20, 184, 166, 0.15); border-color: rgba(20, 184, 166, 0.4); color: #5eead4;">📝 ${totalUraian} ${lblUraianBadge}</span>` : ''}
                        ${keywordFilterMode !== 'uraian' ? `<span class="thematic-match-badge" style="background: rgba(245, 158, 11, 0.15); border-color: rgba(245, 158, 11, 0.4); color: #fbbf24;">📖 ${totalVerses} ${lblVersesBadge}</span>` : ''}
                    </div>
                </div>
            `;

            // SECTION 1: Uraian Tematis
            if (keywordFilterMode !== 'ayat' && totalUraian > 0) {
                markup += `
                    <div class="keyword-section-title">
                        <span>${lblSecTopics}</span>
                        <span class="badge">${totalUraian} ${lblTopicsFound}</span>
                    </div>
                    <div class="keyword-uraian-grid">
                `;

                matchedUraian.slice(0, 40).forEach((u, uIdx) => {
                    const uId = `kw-u-${uIdx}`;
                    markup += `
                        <div class="keyword-uraian-card">
                            <div class="keyword-uraian-header">
                                <div class="keyword-uraian-title" id="${uId}-title" data-original="${escapeHtml(u.uraian)}">${highlightKeyword(escapeHtml(u.uraian), keyword)}</div>
                                <span class="keyword-verse-count-badge">${u.verseCount} ${lblVersesBadge}</span>
                            </div>
                            <div class="keyword-uraian-path">
                                <div>🏷️ <strong>${lblTheme}</strong> <span id="${uId}-tema" data-original="${escapeHtml(u.tema)}">${highlightKeyword(escapeHtml(u.tema), keyword)}</span></div>
                                <div>📂 <strong>${lblSubject}</strong> <span id="${uId}-pokok" data-original="${escapeHtml(u.pokok)}">${highlightKeyword(escapeHtml(u.pokok), keyword)}</span></div>
                                <div>📑 <strong>${lblSubtopic}</strong> <span id="${uId}-sub" data-original="${escapeHtml(u.sub)}">${highlightKeyword(escapeHtml(u.sub), keyword)}</span></div>
                            </div>
                            <button class="btn-jump-thematic" style="padding: 0.6rem 1.1rem; font-size: 0.88rem;" onclick="navigateToThematicTopic('${u.tema.replace(/'/g, "\\\\'")}', '${u.pokok.replace(/'/g, "\\\\'")}', '${u.sub.replace(/'/g, "\\\\'")}', '${u.uraian.replace(/'/g, "\\\\'")}', ${u.sampleVerses[0] ? u.sampleVerses[0].surah_num : 1}, ${u.sampleVerses[0] ? u.sampleVerses[0].ayat_num : 1})">
                                <span>${lblOpenTopic}</span>
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                            </button>
                        </div>
                    `;
                });

                if (totalUraian > 40) {
                    markup += `<div style="text-align: center; color: #94a3b8; font-size: 0.88rem; padding: 1rem;">Menampilkan 40 dari ${totalUraian} topik.</div>`;
                }

                markup += `</div>`;
            }

            // SECTION 2: Verses
            if (keywordFilterMode !== 'uraian' && totalVerses > 0) {
                markup += `
                    <div class="keyword-section-title" style="margin-top: 3.5rem;">
                        <span>${lblSecVerses}</span>
                        <span class="badge">${totalVerses} ${lblVersesFound}</span>
                    </div>
                `;

                matchedVerses.slice(0, 50).forEach((v, vIdx) => {
                    const topic = (v.topics && v.topics.length > 0) ? v.topics[0] : null;
                    const vCardId = `kw-v-${vIdx}`;

                    markup += `
                        <div class="keyword-verse-card" id="${vCardId}" data-surah="${v.surah_num}" data-ayat="${v.ayat_num}">
                            <div class="keyword-verse-header">
                                <div class="keyword-verse-title">QS. ${v.surah_name} [${v.surah_num}] : Ayat ${v.ayat_num}</div>
                                <div style="display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap;">
                                    ${topic ? `<span class="thematic-match-badge kw-topic-badge" style="font-size: 0.78rem;" data-original="${escapeHtml(topic.uraian)}">🏷️ ${escapeHtml(topic.uraian)}</span>` : ''}
                                    ${v.audio ? `
                                    <audio controls style="height: 30px; border-radius: 999px;">
                                        <source src="${v.audio}" type="audio/mpeg">
                                    </audio>
                                    ` : ''}
                                </div>
                            </div>

                            <div class="search-arabic-box keyword-arabic-box" style="font-size: 2rem; margin-bottom: 1.25rem;">
                                ${highlightKeyword(v.arab, keyword)} <span class="verse-end-sign">۝${toArabicDigits(v.ayat_num)}</span>
                            </div>

                            <div class="search-translation-box keyword-trans-box translation-text" style="margin-bottom: 1.25rem;" data-original="${escapeHtml(v.indo)}">
                                ${highlightKeyword(escapeHtml(v.indo), keyword)}
                            </div>

                            <div class="search-actions-bar">
                                <div class="search-action-btns-left">
                                    <button class="tts-button play-btn" data-text="${encodeURIComponent(v.indo)}" onclick="playTTS(this, event)" title="${lblListen}">
                                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path><path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path></svg>
                                        ${lblListen}
                                    </button>
                                    <button class="tts-button ai-btn" style="color: #8b5cf6; border-color: #8b5cf6; background-color: rgba(139, 92, 246, 0.1);" onclick="tanyaAI(this, event, 'QS. ${v.surah_name}: ${v.ayat_num}')" title="${lblAskAI}">
                                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                                        ${lblAskAI}
                                    </button>
                                    <button class="tts-button copy-btn" onclick="copyAyatText(this, event, '${v.surah_name}', ${v.surah_num}, ${v.ayat_num})" title="${lblCopy}">
                                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                                        ${lblCopy}
                                    </button>
                                    <button class="tts-button" style="color: #25d366; border-color: rgba(37, 211, 102, 0.4); background-color: rgba(37, 211, 102, 0.1);" onclick="shareAyatWhatsApp('${v.surah_name}', ${v.surah_num}, ${v.ayat_num})" title="${lblShare}">
                                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                                        ${lblShare}
                                    </button>
                                </div>
                                <div class="search-action-btns-right">
                                    <button class="nav-action-btn secondary-btn" style="padding: 0.5rem 1rem; font-size: 0.88rem;" onclick="lookupVerseInSearch(${v.surah_num}, ${v.ayat_num}, event)">
                                        ${lblOpenSearch}
                                    </button>
                                    ${topic ? `
                                    <button class="nav-action-btn next-btn" style="padding: 0.5rem 1rem; font-size: 0.88rem;" onclick="navigateToThematicTopic('${topic.tema.replace(/'/g, "\\\\'")}', '${topic.pokok.replace(/'/g, "\\\\'")}', '${topic.sub.replace(/'/g, "\\\\'")}', '${topic.uraian.replace(/'/g, "\\\\'")}', ${v.surah_num}, ${v.ayat_num})">
                                        ${lblOpenThematic}
                                    </button>
                                    ` : ''}
                                </div>
                            </div>
                        </div>
                    `;
                });

                if (totalVerses > 50) {
                    markup += `<div style="text-align: center; color: #94a3b8; font-size: 0.88rem; padding: 1rem;">Menampilkan 50 dari ${totalVerses} ayat.</div>`;
                }
            }

            area.innerHTML = markup;

            // If in non-Indonesian mode, translate dynamic titles and verses in results
            if (targetLang !== 'id') {
                translatePageContent();
            }
        }"""

    match_rk = old_render_kw_pattern.search(content)
    if match_rk:
        content = content[:match_rk.start()] + new_render_kw + content[match_rk.end():]
        print("Updated renderKeywordSearchResults with getI18nText successfully.")
    else:
        print("ERROR: old_render_kw_pattern not matched!")
        return

    # 6. Update translatePageContent to also translate [data-i18n-placeholder] and search results titles
    old_i18n_code = """            // 5b. Terjemahkan Mode Tabs & Elemen UI Lainnya (data-i18n-orig)
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
            });"""

    new_i18n_code = """            // 5b. Terjemahkan Mode Tabs & Elemen UI Lainnya (data-i18n-orig)
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
            });"""

    if old_i18n_code in content:
        content = content.replace(old_i18n_code, new_i18n_code, 1)
        print("Updated translatePageContent with placeholder translation successfully.")
    else:
        print("ERROR: old_i18n_code not found!")
        return

    # Write output
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: index.html fully updated with keyword search translation!")

if __name__ == '__main__':
    main()
