import json
import re

# Load surah list
with open('scratch/surah_list.js', 'r', encoding='utf-8') as f:
    surah_list_code = f.read().strip()

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Insert CSS before </style>
css_to_insert = """
        /* ==========================================================================
           Fitur Pilih Surat & Ayat (Pencarian Tematik Terbalik) Styling
           ========================================================================== */
        .mode-nav-tabs {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 2.2rem;
            flex-wrap: wrap;
        }
        .mode-tab-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.65rem;
            background: rgba(17, 24, 39, 0.9);
            color: #94a3b8;
            border: 1px solid var(--card-border);
            padding: 0.8rem 1.75rem;
            border-radius: 999px;
            font-family: 'Inter', sans-serif;
            font-size: 0.98rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
            user-select: none;
        }
        .mode-tab-btn:hover {
            border-color: #334155;
            color: #f8fafc;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);
        }
        .mode-tab-btn.active {
            background: linear-gradient(135deg, rgba(20, 184, 166, 0.22), rgba(13, 148, 136, 0.35));
            border-color: var(--accent);
            color: #5eead4;
            box-shadow: 0 0 25px rgba(20, 184, 166, 0.25), 0 4px 15px rgba(0, 0, 0, 0.3);
        }
        .mode-tab-btn svg {
            transition: transform 0.3s ease;
        }
        .mode-tab-btn.active svg {
            stroke: #2dd4bf;
            transform: scale(1.1);
        }

        /* Search Console Card */
        .search-nav-card {
            background: linear-gradient(145deg, rgba(17, 24, 39, 0.95), rgba(15, 23, 42, 0.95));
            border: 1px solid rgba(20, 184, 166, 0.35);
            border-radius: 18px;
            padding: 2rem;
            margin-bottom: 2.5rem;
            box-shadow: 0 12px 35px -5px rgba(0, 0, 0, 0.5), 0 0 25px rgba(20, 184, 166, 0.1);
            backdrop-filter: blur(12px);
            animation: fadeIn 0.4s ease;
        }
        .search-console-header {
            margin-bottom: 1.75rem;
            text-align: center;
        }
        .search-console-title {
            display: inline-flex;
            align-items: center;
            gap: 0.65rem;
            font-size: 1.35rem;
            font-weight: 700;
            color: #f8fafc;
            margin-bottom: 0.35rem;
        }
        .search-console-title svg {
            color: var(--accent);
        }
        .search-console-subtitle {
            font-size: 0.92rem;
            color: #94a3b8;
        }
        .search-controls-row {
            display: flex;
            gap: 1.25rem;
            align-items: flex-end;
            flex-wrap: wrap;
        }
        .search-field-group {
            display: flex;
            flex-direction: column;
            gap: 0.55rem;
            text-align: left;
        }
        .search-field-group label {
            font-size: 0.85rem;
            font-weight: 700;
            color: #5eead4;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        .search-field-group.surah-field {
            flex: 3;
            min-width: 280px;
        }
        .search-field-group.ayat-field {
            flex: 2;
            min-width: 220px;
        }
        .surah-filter-box {
            position: relative;
            margin-bottom: 0.5rem;
        }
        .surah-filter-input {
            width: 100%;
            box-sizing: border-box;
            background: #0f172a;
            color: #f8fafc;
            border: 1px solid #334155;
            padding: 0.65rem 1rem 0.65rem 2.25rem;
            border-radius: 8px;
            font-size: 0.88rem;
            font-family: 'Inter', sans-serif;
            transition: all 0.2s ease;
        }
        .surah-filter-input:focus {
            outline: none;
            border-color: var(--accent);
            box-shadow: 0 0 0 2px rgba(20, 184, 166, 0.2);
        }
        .surah-filter-icon {
            position: absolute;
            left: 0.75rem;
            top: 50%;
            transform: translateY(-50%);
            color: #64748b;
            pointer-events: none;
        }
        .ayat-picker-row {
            display: flex;
            gap: 0.5rem;
            align-items: center;
            width: 100%;
        }
        .ayat-stepper-btn {
            background: #1e293b;
            color: #94a3b8;
            border: 1px solid #334155;
            width: 44px;
            height: 44px;
            border-radius: 8px;
            font-size: 1.1rem;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
            flex-shrink: 0;
            user-select: none;
        }
        .ayat-stepper-btn:hover:not(:disabled) {
            background: var(--accent);
            color: #0b0f19;
            border-color: var(--accent);
            transform: scale(1.05);
        }
        .ayat-stepper-btn:disabled {
            opacity: 0.3;
            cursor: not-allowed;
        }

        /* Search Results & Verse Card */
        #search-view-wrapper {
            animation: fadeIn 0.4s ease;
        }
        .search-verse-card {
            background: linear-gradient(145deg, rgba(17, 24, 39, 0.85), rgba(15, 23, 42, 0.95));
            border: 1px solid var(--card-border);
            border-radius: 18px;
            padding: 2.2rem;
            margin-bottom: 2.5rem;
            box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.4);
            position: relative;
            overflow: hidden;
            text-align: left;
        }
        .search-verse-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #14b8a6, #3b82f6, #fbbf24);
        }
        .search-verse-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
            padding-bottom: 1.25rem;
            border-bottom: 1px solid rgba(30, 41, 59, 0.8);
            margin-bottom: 1.75rem;
        }
        .search-verse-title-wrap {
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
        }
        .search-verse-title {
            font-size: 1.45rem;
            font-weight: 700;
            color: #fbbf24;
            margin: 0;
            letter-spacing: -0.01em;
        }
        .search-verse-meta {
            font-size: 0.88rem;
            color: #94a3b8;
            font-weight: 500;
        }
        .search-verse-badges {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            flex-wrap: wrap;
        }
        .search-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            background: rgba(20, 184, 166, 0.12);
            border: 1px solid rgba(20, 184, 166, 0.3);
            color: #5eead4;
            padding: 0.35rem 0.85rem;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 600;
        }
        .search-badge.type-badge {
            background: rgba(59, 130, 246, 0.12);
            border-color: rgba(59, 130, 246, 0.35);
            color: #93c5fd;
        }
        .search-arabic-box {
            font-family: 'Amiri', serif;
            font-size: 2.2rem;
            line-height: 2.3;
            color: #f8fafc;
            direction: rtl;
            text-align: right;
            background: rgba(11, 15, 25, 0.55);
            padding: 1.75rem 2rem;
            border-radius: 14px;
            border: 1px solid rgba(30, 41, 59, 0.7);
            margin-bottom: 1.5rem;
            word-spacing: 0.15em;
        }
        .verse-end-sign {
            display: inline-block;
            font-size: 1.7rem;
            color: #fbbf24;
            margin-right: 0.4rem;
            font-weight: normal;
        }
        .search-translation-box {
            font-size: 1.12rem;
            line-height: 1.85;
            color: #cbd5e1;
            margin-bottom: 1.75rem;
            padding: 0 0.25rem;
        }
        .search-actions-bar {
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
            padding-top: 1.25rem;
            border-top: 1px solid rgba(30, 41, 59, 0.8);
        }
        .search-action-btns-left {
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
            align-items: center;
        }
        .search-action-btns-right {
            display: flex;
            gap: 0.5rem;
            align-items: center;
        }
        .copy-btn {
            background-color: #1e293b;
            color: #94a3b8;
            border: 1px solid #334155;
        }
        .copy-btn:hover {
            color: #f8fafc;
            border-color: #475569;
        }

        /* Thematic Classification Section */
        .thematic-results-section {
            margin-top: 2.5rem;
            text-align: left;
        }
        .thematic-results-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
            gap: 0.75rem;
            border-bottom: 2px solid rgba(30, 41, 59, 0.8);
            padding-bottom: 1rem;
        }
        .thematic-results-title {
            font-size: 1.35rem;
            font-weight: 700;
            color: #f8fafc;
            display: flex;
            align-items: center;
            gap: 0.65rem;
            margin: 0;
            text-align: left;
        }
        .thematic-count-badge {
            background: linear-gradient(135deg, rgba(20, 184, 166, 0.2), rgba(13, 148, 136, 0.3));
            color: #5eead4;
            border: 1px solid rgba(20, 184, 166, 0.4);
            padding: 0.4rem 1rem;
            border-radius: 999px;
            font-size: 0.88rem;
            font-weight: 700;
        }
        .thematic-match-card {
            background: linear-gradient(145deg, rgba(17, 24, 39, 0.8), rgba(15, 23, 42, 0.9));
            border: 1px solid rgba(30, 41, 59, 0.9);
            border-radius: 16px;
            padding: 1.75rem 2rem;
            margin-bottom: 1.5rem;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
        }
        .thematic-match-card:hover {
            border-color: rgba(20, 184, 166, 0.55);
            transform: translateY(-2px);
            box-shadow: 0 12px 30px -5px rgba(20, 184, 166, 0.18);
        }
        .thematic-match-top-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.25rem;
        }
        .thematic-match-badge {
            font-size: 0.82rem;
            font-weight: 700;
            color: #fbbf24;
            background: rgba(245, 158, 11, 0.12);
            border: 1px solid rgba(245, 158, 11, 0.3);
            padding: 0.25rem 0.75rem;
            border-radius: 999px;
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
        }
        .thematic-path {
            display: flex;
            flex-direction: column;
            gap: 0.8rem;
            margin-bottom: 1.5rem;
        }
        .thematic-step {
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
            font-size: 0.98rem;
            line-height: 1.5;
        }
        .thematic-step .step-label {
            font-weight: 600;
            color: #94a3b8;
            min-width: 155px;
            flex-shrink: 0;
        }
        .thematic-step .step-val {
            font-weight: 600;
            color: #f1f5f9;
        }
        .thematic-step.tema-step .step-val {
            color: #fbbf24;
            font-size: 1.05rem;
        }
        .thematic-step.pokok-step .step-val {
            color: #60a5fa;
        }
        .thematic-step.sub-step .step-val {
            color: #5eead4;
        }
        .thematic-step.uraian-step .step-val {
            color: #e2e8f0;
            font-style: italic;
        }
        .btn-jump-thematic {
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            background: linear-gradient(135deg, rgba(20, 184, 166, 0.22), rgba(13, 148, 136, 0.38));
            color: #5eead4;
            border: 1px solid rgba(20, 184, 166, 0.5);
            padding: 0.75rem 1.4rem;
            border-radius: 10px;
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .btn-jump-thematic:hover {
            background: linear-gradient(135deg, rgba(20, 184, 166, 0.45), rgba(13, 148, 136, 0.65));
            color: #ffffff;
            border-color: #2dd4bf;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(20, 184, 166, 0.3);
        }
        .btn-jump-thematic svg {
            transition: transform 0.2s ease;
        }
        .btn-jump-thematic:hover svg {
            transform: translateX(4px);
        }

        .thematic-empty-card {
            background: rgba(17, 24, 39, 0.6);
            border: 1px dashed #334155;
            border-radius: 16px;
            padding: 3rem 2rem;
            text-align: center;
            margin-top: 1rem;
        }
        .thematic-empty-card .empty-icon {
            font-size: 2.8rem;
            margin-bottom: 0.75rem;
        }
        .thematic-empty-card .empty-title {
            font-size: 1.25rem;
            font-weight: 700;
            color: #f8fafc;
            margin-bottom: 0.6rem;
        }
        .thematic-empty-card .empty-desc {
            font-size: 0.98rem;
            color: #94a3b8;
            max-width: 620px;
            margin: 0 auto;
            line-height: 1.7;
        }
        .verse-highlight-pulse {
            animation: highlightGlow 3.5s ease;
        }
        @keyframes highlightGlow {
            0% { box-shadow: 0 0 0 0 rgba(20, 184, 166, 0.8); border-color: #2dd4bf; }
            30% { box-shadow: 0 0 35px 8px rgba(20, 184, 166, 0.6); border-color: #2dd4bf; }
            70% { box-shadow: 0 0 25px 4px rgba(20, 184, 166, 0.4); border-color: #2dd4bf; }
            100% { box-shadow: 0 0 0 0 rgba(20, 184, 166, 0); }
        }

        @media (max-width: 768px) {
            .mode-nav-tabs {
                flex-direction: row;
                width: 100%;
            }
            .mode-tab-btn {
                flex: 1;
                justify-content: center;
                padding: 0.7rem 1rem;
                font-size: 0.9rem;
            }
            .search-controls-row {
                flex-direction: column;
                gap: 1rem;
            }
            .search-field-group.surah-field,
            .search-field-group.ayat-field {
                width: 100%;
            }
            .search-arabic-box {
                font-size: 1.7rem;
                padding: 1.25rem 1rem;
            }
            .thematic-step {
                flex-direction: column;
                gap: 0.2rem;
            }
            .thematic-step .step-label {
                min-width: unset;
            }
            .search-actions-bar {
                flex-direction: column;
                align-items: stretch;
                gap: 1rem;
            }
            .search-action-btns-left,
            .search-action-btns-right {
                justify-content: center;
            }
        }
"""

if '/* ==========================================================================\n           Fitur Pilih Surat & Ayat' not in html:
    html = html.replace('    </style>', css_to_insert + '    </style>')
    print("Inserted CSS successfully.")
else:
    print("CSS already present.")

# 2. Replace HTML navigation and content containers
old_nav_and_content = """        <div class="nav-container">
            <select id="select-tema" class="custom-select">
                <option value="">Pilih Tema</option>
            </select>
            
            <select id="select-pokok" class="custom-select" disabled>
                <option value="">Pilih Pokok Bahasan</option>
            </select>
            
            <select id="select-sub" class="custom-select" disabled>
                <option value="">Pilih Sub Pokok Bahasan</option>
            </select>
        </div>
        
        <div class="hint" id="hint-text">
            <span>✨</span> Klik pada kartu untuk membalik dan melihat teks Arabnya
        </div>

        <div id="content-area">
            <div class="empty-state">Silakan pilih kategori di atas untuk melihat ayat.</div>
        </div>

        <div id="bottom-nav-container" style="display: none; margin-top: 3rem;">
            <div style="display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center; align-items: center;">
                <button id="btn-prev-uraian" class="nav-action-btn secondary-btn" onclick="prevSub()">
                    ⬅️ Sub Bahasan Sebelum
                </button>
                <button id="btn-next-uraian" class="nav-action-btn next-btn" onclick="nextSub()">
                    Sub Bahasan Berikutnya ➡️
                </button>
            </div>
        </div>"""

new_nav_and_content = """        <!-- Mode Navigation Tabs -->
        <div class="mode-nav-tabs">
            <button id="tab-btn-thematic" class="mode-tab-btn active" onclick="switchMainMode('thematic')">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                <span>Jelajah Tematis</span>
            </button>
            <button id="tab-btn-search" class="mode-tab-btn" onclick="switchMainMode('search')">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                <span>Cari Surat & Ayat</span>
            </button>
        </div>

        <!-- Thematic Navigation (Mode 1) -->
        <div id="thematic-nav-container" class="nav-container">
            <select id="select-tema" class="custom-select">
                <option value="">Pilih Tema</option>
            </select>
            
            <select id="select-pokok" class="custom-select" disabled>
                <option value="">Pilih Pokok Bahasan</option>
            </select>
            
            <select id="select-sub" class="custom-select" disabled>
                <option value="">Pilih Sub Pokok Bahasan</option>
            </select>
        </div>

        <!-- Search Surah & Ayat Navigation (Mode 2) -->
        <div id="search-nav-container" class="search-nav-card" style="display: none;">
            <div class="search-console-header">
                <div class="search-console-title">
                    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                    <span>Pilih Surat & Nomor Ayat</span>
                </div>
                <div class="search-console-subtitle">Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan</div>
            </div>

            <div class="search-controls-row">
                <div class="search-field-group surah-field">
                    <label for="select-search-surah">Surat Al-Qur'an (1–114):</label>
                    <div class="surah-filter-box">
                        <svg class="surah-filter-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                        <input type="text" id="input-surah-filter" class="surah-filter-input" placeholder="Cari nama atau nomor surat (misal: Baqarah, 36, Yasin)..." oninput="filterSurahDropdown()">
                    </div>
                    <select id="select-search-surah" class="custom-select search-select" onchange="onSearchSurahChange()">
                        <option value="">-- Pilih Surat --</option>
                    </select>
                </div>

                <div class="search-field-group ayat-field">
                    <label for="select-search-ayat">Nomor Ayat:</label>
                    <div class="ayat-picker-row">
                        <button id="btn-ayat-prev" class="ayat-stepper-btn" onclick="stepAyat(-1)" title="Ayat Sebelumnya" disabled>◀</button>
                        <select id="select-search-ayat" class="custom-select search-select" onchange="onSearchAyatChange()" disabled>
                            <option value="">Pilih Ayat</option>
                        </select>
                        <button id="btn-ayat-next" class="ayat-stepper-btn" onclick="stepAyat(1)" title="Ayat Selanjutnya" disabled>▶</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Thematic Content View (Mode 1) -->
        <div id="thematic-view-wrapper">
            <div class="hint" id="hint-text">
                <span>✨</span> Klik pada kartu untuk membalik dan melihat teks Arabnya
            </div>

            <div id="content-area">
                <div class="empty-state">Silakan pilih kategori di atas untuk melihat ayat.</div>
            </div>

            <div id="bottom-nav-container" style="display: none; margin-top: 3rem;">
                <div style="display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center; align-items: center;">
                    <button id="btn-prev-uraian" class="nav-action-btn secondary-btn" onclick="prevSub()">
                        ⬅️ Sub Bahasan Sebelum
                    </button>
                    <button id="btn-next-uraian" class="nav-action-btn next-btn" onclick="nextSub()">
                        Sub Bahasan Berikutnya ➡️
                    </button>
                </div>
            </div>
        </div>

        <!-- Search Verse Content View (Mode 2) -->
        <div id="search-view-wrapper" style="display: none;">
            <div id="search-content-area">
                <div class="empty-state">Silakan pilih Surat dan Nomor Ayat di atas untuk melihat klasifikasi tematiknya.</div>
            </div>
        </div>"""

if old_nav_and_content in html:
    html = html.replace(old_nav_and_content, new_nav_and_content)
    print("Replaced navigation & content markup successfully.")
else:
    print("Navigation markup not found for direct replacement. Checking...")

# 3. Update initData to build index and init search
old_init_data = """        function initData(data) {
            quranData = data;
            const savedLang = localStorage.getItem('active_lang');
            const elTts = document.getElementById('tts-language');
            if (savedLang && elTts && elTts.querySelector(`option[value="${savedLang}"]`)) {
                elTts.value = savedLang;
            }
            populateSelect(elTema, naturalSort(Object.keys(data)), "Pilih Tema");
            translateDropdowns();
            updateTranslatorInfo();
            checkAutoNav();
        }"""

new_init_data = """        function initData(data) {
            quranData = data;
            buildVerseIndex();
            initSurahAyatSearch();
            const savedLang = localStorage.getItem('active_lang');
            const elTts = document.getElementById('tts-language');
            if (savedLang && elTts && elTts.querySelector(`option[value="${savedLang}"]`)) {
                elTts.value = savedLang;
            }
            populateSelect(elTema, naturalSort(Object.keys(data)), "Pilih Tema");
            translateDropdowns();
            updateTranslatorInfo();
            checkAutoNav();
        }"""

if old_init_data in html:
    html = html.replace(old_init_data, new_init_data)
    print("Updated initData successfully.")
else:
    print("initData pattern not found.")

# 4. Add "Cari Ayat" button inside flip cards in generateUraianGroupMarkup
old_flip_card_btns = """                                            <button class="tts-button ai-btn" style="color: #8b5cf6; border-color: #8b5cf6; background-color: rgba(139, 92, 246, 0.1);" onclick="tanyaAI(this, event, '${uraianTitle.replace(/'/g, "\\\\'")}')" title="Tanya AI tentang ayat ini">
                                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                                                Tanya AI
                                            </button>
                                        </div>"""

new_flip_card_btns = """                                            <button class="tts-button ai-btn" style="color: #8b5cf6; border-color: #8b5cf6; background-color: rgba(139, 92, 246, 0.1);" onclick="tanyaAI(this, event, '${uraianTitle.replace(/'/g, "\\\\'")}')" title="Tanya AI tentang ayat ini">
                                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                                                Tanya AI
                                            </button>
                                            <button class="tts-button" style="color: #38bdf8; border-color: #38bdf8; background-color: rgba(56, 189, 248, 0.1);" onclick="lookupVerseInSearch(${v.surah_num}, ${v.ayat_num}, event)" title="Lihat di Pencari Surat & Ayat">
                                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                                                Cari Ayat
                                            </button>
                                        </div>"""

if old_flip_card_btns in html:
    html = html.replace(old_flip_card_btns, new_flip_card_btns)
    print("Added Cari Ayat button to flip cards.")
else:
    print("Flip card buttons pattern not found.")

# 5. In translatePageContent, support .search-card-front
old_cards_selector = "const cards = document.querySelectorAll('.flip-card-front');"
new_cards_selector = "const cards = document.querySelectorAll('.flip-card-front, .search-card-front');"
if old_cards_selector in html:
    html = html.replace(old_cards_selector, new_cards_selector)
    print("Updated translatePageContent selector.")

# 6. Append full feature script before </script>
js_feature_code = f"""
        /* ==========================================================================
           FITUR PILIH SURAT & AYAT (PENCARIAN TEMATIK TERBALIK)
           ========================================================================== */
        {surah_list_code}

        let verseThematicIndex = {{}};
        let currentSearchSurah = 2; // Default Al-Baqarah
        let currentSearchAyat = 255; // Default Ayat Kursi
        let surahApiCache = {{}};
        let activeMainMode = 'thematic';

        function buildVerseIndex() {{
            verseThematicIndex = {{}};
            if (!quranData) return;
            for (const [tema, pbs] of Object.entries(quranData)) {{
                for (const [pb, spbs] of Object.entries(pbs)) {{
                    for (const [spb, urs] of Object.entries(spbs)) {{
                        for (const [ur, urData] of Object.entries(urs)) {{
                            if (urData && urData.verses) {{
                                urData.verses.forEach(v => {{
                                    const key = `${{v.surah_num}}:${{v.ayat_num}}`;
                                    if (!verseThematicIndex[key]) {{
                                        verseThematicIndex[key] = {{
                                            surah_name: v.surah_name,
                                            surah_num: v.surah_num,
                                            ayat_num: v.ayat_num,
                                            arab: v.arab,
                                            indo: v.indo,
                                            audio: v.audio,
                                            topics: []
                                        }};
                                    }}
                                    verseThematicIndex[key].topics.push({{
                                        tema: tema,
                                        pokok: pb,
                                        sub: spb,
                                        uraian: ur
                                    }});
                                }});
                            }}
                        }}
                    }}
                }}
            }}
            console.log(`[VerseIndex] Indexed ${{Object.keys(verseThematicIndex).length}} unique verses across all themes.`);
        }}

        function switchMainMode(mode) {{
            stopTTS();
            activeMainMode = mode;
            const tabThematic = document.getElementById('tab-btn-thematic');
            const tabSearch = document.getElementById('tab-btn-search');
            const thematicNav = document.getElementById('thematic-nav-container');
            const searchNav = document.getElementById('search-nav-container');
            const thematicView = document.getElementById('thematic-view-wrapper');
            const searchView = document.getElementById('search-view-wrapper');

            if (mode === 'thematic') {{
                if (tabThematic) tabThematic.classList.add('active');
                if (tabSearch) tabSearch.classList.remove('active');
                if (thematicNav) thematicNav.style.display = 'flex';
                if (searchNav) searchNav.style.display = 'none';
                if (thematicView) thematicView.style.display = 'block';
                if (searchView) searchView.style.display = 'none';
            }} else {{
                if (tabThematic) tabThematic.classList.remove('active');
                if (tabSearch) tabSearch.classList.add('active');
                if (thematicNav) thematicNav.style.display = 'none';
                if (searchNav) searchNav.style.display = 'block';
                if (thematicView) thematicView.style.display = 'none';
                if (searchView) searchView.style.display = 'block';

                // Render current search verse if not already rendered
                if (!document.getElementById('current-rendered-verse')) {{
                    renderSearchVerseResult(currentSearchSurah, currentSearchAyat);
                }}
            }}
        }}

        function initSurahAyatSearch() {{
            const selectSurah = document.getElementById('select-search-surah');
            if (!selectSurah) return;
            populateSurahDropdown(SURAH_LIST);

            // Set initial value
            selectSurah.value = currentSearchSurah;
            populateAyatDropdown(currentSearchSurah);
            const selectAyat = document.getElementById('select-search-ayat');
            if (selectAyat) selectAyat.value = currentSearchAyat;
            updateStepperButtons();
        }}

        function populateSurahDropdown(list) {{
            const selectSurah = document.getElementById('select-search-surah');
            if (!selectSurah) return;
            const currentVal = selectSurah.value;
            selectSurah.innerHTML = '<option value="">-- Pilih Surat (1-114) --</option>';
            list.forEach(s => {{
                const opt = document.createElement('option');
                opt.value = s.no;
                opt.textContent = `${{s.no}}. ${{s.name}} (${{s.arab}}) — ${{s.ayat}} Ayat [${{s.type}}]`;
                selectSurah.appendChild(opt);
            }});
            if (currentVal && list.some(s => s.no == currentVal)) {{
                selectSurah.value = currentVal;
            }}
        }}

        function filterSurahDropdown() {{
            const input = document.getElementById('input-surah-filter');
            if (!input) return;
            const query = input.value.trim().toLowerCase();
            if (!query) {{
                populateSurahDropdown(SURAH_LIST);
                return;
            }}
            const filtered = SURAH_LIST.filter(s => 
                s.name.toLowerCase().includes(query) ||
                String(s.no) === query ||
                s.arab.includes(query) ||
                s.type.toLowerCase().includes(query)
            );
            populateSurahDropdown(filtered);
            const selectSurah = document.getElementById('select-search-surah');
            if (filtered.length > 0 && selectSurah) {{
                selectSurah.value = filtered[0].no;
                onSearchSurahChange();
            }}
        }}

        function populateAyatDropdown(surahNum) {{
            const selectAyat = document.getElementById('select-search-ayat');
            if (!selectAyat) return;
            const surahInfo = SURAH_LIST.find(s => s.no == surahNum);
            if (!surahInfo) {{
                selectAyat.innerHTML = '<option value="">Pilih Ayat</option>';
                selectAyat.disabled = true;
                return;
            }}
            selectAyat.innerHTML = `<option value="">-- Pilih Ayat (1-${{surahInfo.ayat}}) --</option>`;
            for (let i = 1; i <= surahInfo.ayat; i++) {{
                const opt = document.createElement('option');
                opt.value = i;
                opt.textContent = `Ayat ${{i}}`;
                selectAyat.appendChild(opt);
            }}
            selectAyat.disabled = false;
        }}

        function onSearchSurahChange() {{
            stopTTS();
            const selectSurah = document.getElementById('select-search-surah');
            const selectAyat = document.getElementById('select-search-ayat');
            if (!selectSurah || !selectSurah.value) return;
            currentSearchSurah = parseInt(selectSurah.value);
            populateAyatDropdown(currentSearchSurah);
            currentSearchAyat = 1;
            if (selectAyat) selectAyat.value = 1;
            updateStepperButtons();
            renderSearchVerseResult(currentSearchSurah, currentSearchAyat);
        }}

        function onSearchAyatChange() {{
            stopTTS();
            const selectAyat = document.getElementById('select-search-ayat');
            if (!selectAyat || !selectAyat.value) return;
            currentSearchAyat = parseInt(selectAyat.value);
            updateStepperButtons();
            renderSearchVerseResult(currentSearchSurah, currentSearchAyat);
        }}

        function stepAyat(delta) {{
            stopTTS();
            const surahInfo = SURAH_LIST.find(s => s.no == currentSearchSurah);
            if (!surahInfo) return;
            let targetAyat = currentSearchAyat + delta;
            if (targetAyat < 1) targetAyat = 1;
            if (targetAyat > surahInfo.ayat) targetAyat = surahInfo.ayat;
            if (targetAyat === currentSearchAyat) return;

            currentSearchAyat = targetAyat;
            const selectAyat = document.getElementById('select-search-ayat');
            if (selectAyat) selectAyat.value = currentSearchAyat;
            updateStepperButtons();
            renderSearchVerseResult(currentSearchSurah, currentSearchAyat);
        }}

        function updateStepperButtons() {{
            const btnPrev = document.getElementById('btn-ayat-prev');
            const btnNext = document.getElementById('btn-ayat-next');
            const surahInfo = SURAH_LIST.find(s => s.no == currentSearchSurah);
            const totalAyat = surahInfo ? surahInfo.ayat : 1;

            if (btnPrev) btnPrev.disabled = (currentSearchAyat <= 1);
            if (btnNext) btnNext.disabled = (currentSearchAyat >= totalAyat);
        }}

        function toArabicDigits(num) {{
            const digits = ['٠','١','٢','٣','٤','٥','٦','٧','٨','٩'];
            return String(num).replace(/\\d/g, d => digits[d]);
        }}

        async function renderSearchVerseResult(surahNum, ayatNum) {{
            const searchArea = document.getElementById('search-content-area');
            if (!searchArea) return;

            const key = `${{surahNum}}:${{ayatNum}}`;
            const surahInfo = SURAH_LIST.find(s => s.no == surahNum) || {{ no: surahNum, name: `Surat ${{surahNum}}`, arab: '', ayat: 1, type: '' }};
            const indexedData = verseThematicIndex[key];

            let verseObj = null;

            if (indexedData) {{
                verseObj = {{
                    surah_num: indexedData.surah_num,
                    surah_name: indexedData.surah_name || surahInfo.name,
                    ayat_num: indexedData.ayat_num,
                    arab: indexedData.arab,
                    indo: indexedData.indo,
                    audio: indexedData.audio,
                    topics: indexedData.topics || []
                }};
            }} else {{
                // Fallback fetching for verses not in thematic excel
                searchArea.innerHTML = `
                    <div class="empty-state" style="padding: 3rem 2rem;">
                        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="animate-spin" style="margin: 0 auto 1rem auto; display: block; color: var(--accent);"><circle cx="12" cy="12" r="10" stroke-dasharray="32" stroke-dashoffset="10" stroke-opacity="0.3"></circle><path d="M12 2a10 10 0 0 1 10 10" stroke="currentColor"></path></svg>
                        Memuat data QS. ${{surahInfo.name}} [${{surahNum}}]: ${{ayatNum}}...
                    </div>
                `;
                verseObj = await fetchAyahFallback(surahNum, ayatNum, surahInfo);
            }}

            if (!verseObj) {{
                searchArea.innerHTML = `<div class="empty-state" style="color: #ef4444;">Gagal memuat ayat QS. ${{surahInfo.name}} [${{surahNum}}]: ${{ayatNum}}. Silakan periksa koneksi internet Anda.</div>`;
                return;
            }}

            const topics = (verseThematicIndex[key] && verseThematicIndex[key].topics) ? verseThematicIndex[key].topics : [];
            const topicsCount = topics.length;

            let markup = `
                <div id="current-rendered-verse" class="search-verse-card">
                    <div class="search-verse-header">
                        <div class="search-verse-title-wrap">
                            <h2 class="search-verse-title">QS. ${{surahInfo.name}} [${{surahNum}}] : Ayat ${{ayatNum}}</h2>
                            <div class="search-verse-meta">${{surahInfo.arab}} • ${{surahInfo.type}} • Total ${{surahInfo.ayat}} Ayat</div>
                        </div>
                        <div class="search-verse-badges">
                            <span class="search-badge">${{surahInfo.type}}</span>
                            ${{topicsCount > 0 ? `<span class="search-badge" style="background: rgba(245, 158, 11, 0.15); border-color: rgba(245, 158, 11, 0.4); color: #fbbf24;">📑 ${{topicsCount}} Tema Terkait</span>` : '<span class="search-badge" style="background: rgba(100, 116, 139, 0.15); border-color: rgba(100, 116, 139, 0.3); color: #94a3b8;">Belum diindeks</span>'}}
                            ${{verseObj.audio ? `
                            <audio controls style="height: 32px; border-radius: 999px; margin-left: 0.5rem;">
                                <source src="${{verseObj.audio}}" type="audio/mpeg">
                            </audio>
                            ` : ''}}
                        </div>
                    </div>

                    <div class="search-arabic-box">
                        ${{verseObj.arab}} <span class="verse-end-sign">۝${{toArabicDigits(ayatNum)}}</span>
                    </div>

                    <div class="search-card-front" data-surah="${{surahNum}}" data-ayat="${{ayatNum}}" data-indo="${{encodeURIComponent(verseObj.indo)}}">
                        <div class="search-translation-box translation-text">${{verseObj.indo}}</div>

                        <div class="search-actions-bar">
                            <div class="search-action-btns-left">
                                <button class="tts-button play-btn" data-text="${{encodeURIComponent(verseObj.indo)}}" onclick="playTTS(this, event)" title="Dengarkan Terjemahan Suara">
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path><path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path></svg>
                                    Dengarkan
                                </button>
                                <button class="tts-button ai-btn" style="color: #8b5cf6; border-color: #8b5cf6; background-color: rgba(139, 92, 246, 0.1);" onclick="tanyaAI(this, event, 'QS. ${{surahInfo.name}}: ${{ayatNum}}')" title="Tanya AI Tafsir Ayat Ini">
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                                    Tanya AI
                                </button>
                                <button class="tts-button copy-btn" onclick="copyAyatText(this, event, '${{surahInfo.name}}', ${{surahNum}}, ${{ayatNum}})" title="Salin Teks Arab & Terjemahan">
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                                    Salin Ayat
                                </button>
                            </div>
                            <div class="search-action-btns-right">
                                <button class="nav-action-btn secondary-btn" style="padding: 0.5rem 1rem; font-size: 0.88rem;" onclick="stepAyat(-1)" ${{ayatNum <= 1 ? 'disabled' : ''}}>
                                    ◀ Ayat ${{ayatNum - 1}}
                                </button>
                                <button class="nav-action-btn next-btn" style="padding: 0.5rem 1rem; font-size: 0.88rem;" onclick="stepAyat(1)" ${{ayatNum >= surahInfo.ayat ? 'disabled' : ''}}>
                                    Ayat ${{ayatNum + 1}} ▶
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Section Hasil Klasifikasi Tematis -->
                <div class="thematic-results-section">
                    <div class="thematic-results-header">
                        <h3 class="thematic-results-title">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--accent);"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                            Klasifikasi Al-Qur'an Tematis
                        </h3>
                        <span class="thematic-count-badge">
                            ${{topicsCount > 0 ? `Ditemukan dalam ${{topicsCount}} Pembahasan Tematis` : 'Tidak Ditemukan dalam Indeks Tematis'}}
                        </span>
                    </div>
            `;

            if (topicsCount === 0) {{
                markup += `
                    <div class="thematic-empty-card">
                        <div class="empty-icon">📖</div>
                        <div class="empty-title">Belum Ada Pengelompokan Tematik Khusus</div>
                        <div class="empty-desc">
                            Ayat ini belum diklasifikasikan ke dalam 17 tema Al-Qur'an Tematis saat ini. 
                            Anda tetap dapat membaca teks Arab, mendengarkan lantunan murottal, dan menelaah arti terjemahan serta tafsir AI di atas.
                        </div>
                    </div>
                `;
            }} else {{
                topics.forEach((t, idx) => {{
                    markup += `
                        <div class="thematic-match-card">
                            <div class="thematic-match-top-row">
                                <span class="thematic-match-badge">🏷️ Pembahasan Tematis #${{idx + 1}}</span>
                            </div>
                            <div class="thematic-path">
                                <div class="thematic-step tema-step">
                                    <span class="step-label">🏷️ Tema Besar:</span>
                                    <span class="step-val">${{t.tema}}</span>
                                </div>
                                <div class="thematic-step pokok-step">
                                    <span class="step-label">📂 Pokok Bahasan:</span>
                                    <span class="step-val">${{t.pokok}}</span>
                                </div>
                                <div class="thematic-step sub-step">
                                    <span class="step-label">📑 Sub Pokok Bahasan:</span>
                                    <span class="step-val">${{t.sub}}</span>
                                </div>
                                <div class="thematic-step uraian-step">
                                    <span class="step-label">📝 Uraian Khusus:</span>
                                    <span class="step-val">${{t.uraian}}</span>
                                </div>
                            </div>
                            <button class="btn-jump-thematic" onclick="navigateToThematicTopic('${{t.tema.replace(/'/g, "\\\\'") }}', '${{t.pokok.replace(/'/g, "\\\\'") }}', '${{t.sub.replace(/'/g, "\\\\'") }}', '${{t.uraian.replace(/'/g, "\\\\'") }}', ${{surahNum}}, ${{ayatNum}})">
                                <span>Buka di Halaman Tematik</span>
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                            </button>
                        </div>
                    `;
                }});
            }}

            markup += `</div>`;
            searchArea.innerHTML = markup;

            // Trigger translation if non-Indonesian language is selected
            translatePageContent();
        }}

        async function fetchAyahFallback(surahNum, ayatNum, surahInfo) {{
            if (surahApiCache[surahNum]) {{
                const sData = surahApiCache[surahNum];
                const aData = sData.ayat ? sData.ayat.find(a => a.nomorAyat == ayatNum) : null;
                if (aData) {{
                    return {{
                        surah_num: surahNum,
                        surah_name: surahInfo.name,
                        ayat_num: ayatNum,
                        arab: aData.teksArab,
                        indo: aData.teksIndonesia,
                        audio: aData.audio ? aData.audio['05'] || '' : '',
                        topics: []
                    }};
                }}
            }}

            // Fetch from API equran.id
            try {{
                const res = await fetch(`https://equran.id/api/v2/surat/${{surahNum}}`);
                const json = await res.json();
                if (json && json.data) {{
                    surahApiCache[surahNum] = json.data;
                    const aData = json.data.ayat ? json.data.ayat.find(a => a.nomorAyat == ayatNum) : null;
                    if (aData) {{
                        return {{
                            surah_num: surahNum,
                            surah_name: surahInfo.name,
                            ayat_num: ayatNum,
                            arab: aData.teksArab,
                            indo: aData.teksIndonesia,
                            audio: aData.audio ? aData.audio['05'] || '' : '',
                            topics: []
                        }};
                    }}
                }}
            }} catch (e) {{
                console.warn("Fallback equran.id fetch failed, trying alquran.cloud:", e);
            }}

            // Second fallback: api.alquran.cloud
            try {{
                const res = await fetch(`https://api.alquran.cloud/v1/ayah/${{surahNum}}:${{ayatNum}}/editions/quran-uthmani,id.indonesian,ar.alafasy`);
                const json = await res.json();
                if (json && json.data && json.data.length >= 2) {{
                    return {{
                        surah_num: surahNum,
                        surah_name: surahInfo.name,
                        ayat_num: ayatNum,
                        arab: json.data[0].text,
                        indo: json.data[1].text,
                        audio: json.data[2] ? json.data[2].audio : '',
                        topics: []
                    }};
                }}
            }} catch (err) {{
                console.error("All ayah fallbacks failed:", err);
            }}

            return null;
        }}

        function navigateToThematicTopic(tema, pokok, sub, uraian, surahNum, ayatNum) {{
            stopTTS();
            switchMainMode('thematic');

            // 1. Set Tema
            elTema.value = tema;
            resetSelect(elSub, "Pilih Sub Pokok Bahasan");
            if (quranData[tema]) {{
                populateSelect(elPokok, naturalSort(Object.keys(quranData[tema])), "Pilih Pokok Bahasan");
                elPokok.value = pokok;
                if (quranData[tema][pokok]) {{
                    populateSelect(elSub, naturalSort(Object.keys(quranData[tema][pokok])), "Pilih Sub Pokok Bahasan");
                    elSub.value = sub;
                    saveCurrentState();
                    renderContentAll(tema, pokok, sub);

                    // 2. Open group card & highlight verse
                    setTimeout(() => {{
                        const groupCards = document.querySelectorAll('.uraian-group-card');
                        let targetGroup = null;
                        groupCards.forEach(card => {{
                            const titleEl = card.querySelector('.group-title');
                            if (titleEl && titleEl.getAttribute('data-original') === uraian) {{
                                targetGroup = card;
                                card.classList.remove('is-collapsed');
                            }}
                        }});

                        setTimeout(() => {{
                            let targetVerse = null;
                            if (targetGroup) {{
                                const verseWrappers = targetGroup.querySelectorAll('.verse-item-wrapper');
                                verseWrappers.forEach(vw => {{
                                    const front = vw.querySelector('.flip-card-front');
                                    if (front && parseInt(front.getAttribute('data-surah')) === surahNum && parseInt(front.getAttribute('data-ayat')) === ayatNum) {{
                                        targetVerse = vw;
                                    }}
                                }});
                            }}

                            const elToScroll = targetVerse || targetGroup;
                            if (elToScroll) {{
                                elToScroll.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                                if (targetVerse) {{
                                    targetVerse.classList.add('verse-highlight-pulse');
                                    setTimeout(() => targetVerse.classList.remove('verse-highlight-pulse'), 3500);
                                }}
                            }}
                        }}, 200);
                    }}, 150);
                }}
            }}
        }}

        function lookupVerseInSearch(surahNum, ayatNum, event) {{
            if (event) event.stopPropagation();
            stopTTS();
            currentSearchSurah = surahNum;
            currentSearchAyat = ayatNum;

            switchMainMode('search');

            const selectSurah = document.getElementById('select-search-surah');
            const selectAyat = document.getElementById('select-search-ayat');

            if (selectSurah) selectSurah.value = surahNum;
            populateAyatDropdown(surahNum);
            if (selectAyat) selectAyat.value = ayatNum;
            updateStepperButtons();

            renderSearchVerseResult(surahNum, ayatNum);
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function copyAyatText(btn, event, surahName, surahNum, ayatNum) {{
            if (event) event.stopPropagation();
            const card = btn.closest('.search-verse-card');
            if (!card) return;
            const arabEl = card.querySelector('.search-arabic-box');
            const transEl = card.querySelector('.search-translation-box');
            const arab = arabEl ? arabEl.textContent.trim() : '';
            const trans = transEl ? transEl.textContent.trim() : '';

            const copyText = `QS. ${{surahName}} [${{surahNum}}]: ${{ayatNum}}\\n\\n${{arab}}\\n\\nArtinya:\\n"${{trans}}"`;
            navigator.clipboard.writeText(copyText).then(() => {{
                const origHtml = btn.innerHTML;
                btn.innerHTML = `
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color:#5eead4;"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    Tersalin!
                `;
                btn.style.borderColor = '#14b8a6';
                btn.style.color = '#5eead4';
                setTimeout(() => {{
                    btn.innerHTML = origHtml;
                    btn.style.borderColor = '';
                    btn.style.color = '';
                }}, 2000);
            }}).catch(err => {{
                console.error("Copy failed:", err);
            }});
        }}
"""

if '/* ==========================================================================\n           FITUR PILIH SURAT & AYAT' not in html:
    html = html.replace('    </script>\n</body>', js_feature_code + '    </script>\n</body>')
    print("Appended JS feature code successfully.")
else:
    print("JS feature code already present.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated index.html successfully!")
