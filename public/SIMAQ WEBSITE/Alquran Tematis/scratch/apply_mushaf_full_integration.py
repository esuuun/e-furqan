# scratch/apply_mushaf_full_integration.py
import re
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for Mushaf Per Kata
css_target = """        /* Deep Link & Action Buttons for Uraian */"""
css_replacement = """        /* ==========================================================================
           MUSHAF PER KATA & ANALISIS MORFOLOGI STYLES
           ========================================================================== */
        .mushaf-nav-card {
            background: rgba(17, 24, 39, 0.95);
            border: 1px solid rgba(56, 189, 248, 0.25);
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4), 0 0 20px rgba(56, 189, 248, 0.08);
            backdrop-filter: blur(12px);
        }
        .mushaf-controls-grid {
            display: grid;
            grid-template-columns: 1.2fr 1fr;
            gap: 1.25rem;
            margin-top: 1.25rem;
        }
        @media (max-width: 768px) {
            .mushaf-controls-grid {
                grid-template-columns: 1fr;
            }
        }
        .mushaf-lang-row {
            margin-top: 1.25rem;
            padding-top: 1rem;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            align-items: center;
            gap: 0.75rem;
            flex-wrap: wrap;
        }
        .mushaf-lang-label {
            font-size: 0.85rem;
            color: #94a3b8;
            font-weight: 600;
        }
        .mushaf-lang-pills {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }
        .mushaf-lang-btn {
            background: rgba(255, 255, 255, 0.05);
            color: #94a3b8;
            border: 1px solid rgba(255, 255, 255, 0.12);
            padding: 0.3rem 0.75rem;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .mushaf-lang-btn:hover {
            background: rgba(56, 189, 248, 0.15);
            color: #38bdf8;
            border-color: rgba(56, 189, 248, 0.3);
        }
        .mushaf-lang-btn.active {
            background: #fde047;
            color: #0f172a;
            border-color: #fde047;
            font-weight: 700;
            box-shadow: 0 2px 10px rgba(253, 224, 71, 0.3);
        }

        /* Mushaf Ayah Overview Card */
        .mushaf-ayah-overview {
            background: #111827;
            border: 1px solid #1e293b;
            border-radius: 16px;
            padding: 1.75rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
        }
        .mushaf-ayah-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }
        .mushaf-ayah-title {
            margin: 0;
            font-size: 1.35rem;
            font-weight: 700;
            color: #38bdf8;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .mushaf-ayah-meta {
            font-size: 0.85rem;
            color: #94a3b8;
            margin-top: 0.2rem;
        }

        /* Full Ayah Flip Card */
        .mushaf-full-flip-card {
            background-color: transparent;
            perspective: 1000px;
            cursor: pointer;
            margin-bottom: 0.75rem;
        }
        .mushaf-full-flip-inner {
            position: relative;
            width: 100%;
            text-align: center;
            transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            transform-style: preserve-3d;
            border-radius: 12px;
        }
        .mushaf-full-flip-card.flipped .mushaf-full-flip-inner {
            transform: rotateY(180deg);
        }
        .mushaf-full-front, .mushaf-full-back {
            width: 100%;
            backface-visibility: hidden;
            -webkit-backface-visibility: hidden;
            border-radius: 12px;
            padding: 1.5rem 1.75rem;
            box-sizing: border-box;
        }
        .mushaf-full-front {
            background: rgba(15, 23, 42, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #f8fafc;
            font-family: 'Amiri', serif;
            font-size: 2.1rem;
            line-height: 2.3;
            direction: rtl;
            text-align: right;
        }
        .mushaf-full-back {
            background: rgba(15, 23, 42, 0.95);
            border: 1px solid rgba(56, 189, 248, 0.3);
            color: #fde047;
            transform: rotateY(180deg);
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.15rem;
            line-height: 1.7;
            text-align: center;
            font-weight: 500;
        }
        .mushaf-flip-hint {
            text-align: center;
            font-size: 0.8rem;
            color: #64748b;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.35rem;
        }

        /* Word by Word Table */
        .mushaf-table-wrapper {
            overflow-x: auto;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            background: rgba(15, 23, 42, 0.6);
            margin-bottom: 2rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        }
        .mushaf-wbw-table {
            width: 100%;
            border-collapse: collapse;
            text-align: center;
        }
        .mushaf-wbw-table th {
            background: rgba(30, 41, 59, 0.9);
            color: #94a3b8;
            font-size: 0.82rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 0.85rem 1rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        .mushaf-wbw-table td {
            padding: 0.75rem 1rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            vertical-align: middle;
        }
        .mushaf-wbw-table tr:hover td {
            background: rgba(255, 255, 255, 0.02);
        }

        /* Lafdz Cell & Flip Effect */
        .mushaf-lafdz-card {
            perspective: 600px;
            cursor: pointer;
            min-height: 52px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .mushaf-lafdz-inner {
            position: relative;
            width: 100%;
            transition: transform 0.45s cubic-bezier(0.4, 0, 0.2, 1);
            transform-style: preserve-3d;
            border-radius: 8px;
            padding: 0.4rem 0.6rem;
        }
        .mushaf-lafdz-card.flipped .mushaf-lafdz-inner {
            transform: rotateY(180deg);
        }
        .mushaf-lafdz-front, .mushaf-lafdz-back {
            backface-visibility: hidden;
            -webkit-backface-visibility: hidden;
            width: 100%;
        }
        .mushaf-lafdz-front {
            font-family: 'Amiri', serif;
            font-size: 1.65rem;
            color: #ffffff;
            direction: rtl;
        }
        .mushaf-lafdz-back {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            transform: rotateY(180deg);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: rgba(30, 41, 59, 0.95);
            border-radius: 8px;
            padding: 0.3rem 0.5rem;
            font-size: 0.82rem;
            color: #38bdf8;
            direction: rtl;
        }
        .mushaf-muttashil-label {
            font-size: 0.68rem;
            color: #94a3b8;
            font-family: 'Inter', sans-serif;
            margin-bottom: 0.15rem;
        }
        .mushaf-muttashil-text {
            font-family: 'Amiri', serif;
            font-size: 1.15rem;
            color: #ffffff;
        }

        /* Root / Kata Akar Cell */
        .mushaf-root-cell {
            background: rgba(253, 224, 71, 0.08);
            border-left: 1px solid rgba(255, 255, 255, 0.05);
            border-right: 1px solid rgba(255, 255, 255, 0.05);
        }
        .mushaf-root-text {
            font-family: 'Amiri', serif;
            font-size: 1.35rem;
            color: #fde047;
            margin-bottom: 0.35rem;
        }
        .mushaf-kamus-btn {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 3px 8px;
            font-size: 0.72rem;
            font-weight: 600;
            color: #fde047;
            background: rgba(253, 224, 71, 0.12);
            border: 1px solid rgba(253, 224, 71, 0.35);
            border-radius: 6px;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.2s ease;
            font-family: 'Inter', sans-serif;
        }
        .mushaf-kamus-btn:hover {
            background: #fde047;
            color: #0f172a;
            transform: translateY(-1px);
            box-shadow: 0 2px 8px rgba(253, 224, 71, 0.25);
        }

        /* Meaning / Terjemahan Cell */
        .mushaf-meaning-cell {
            text-align: left;
            font-size: 0.95rem;
            color: #e2e8f0;
        }
        .mushaf-meaning-wrap {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.75rem;
        }
        .mushaf-word-audio-btn {
            background: transparent;
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #94a3b8;
            border-radius: 999px;
            width: 28px;
            height: 28px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            flex-shrink: 0;
            transition: all 0.2s ease;
        }
        .mushaf-word-audio-btn:hover {
            color: #38bdf8;
            border-color: #38bdf8;
            background: rgba(56, 189, 248, 0.1);
        }

        /* Stepper row at bottom of verse */
        .mushaf-bottom-stepper {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
            margin-top: 1.5rem;
            margin-bottom: 2.5rem;
        }
        .mushaf-step-btn {
            background: rgba(30, 41, 59, 0.9);
            color: #f8fafc;
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 0.6rem 1.25rem;
            border-radius: 10px;
            font-size: 0.9rem;
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.2s ease;
        }
        .mushaf-step-btn:hover:not(:disabled) {
            background: rgba(56, 189, 248, 0.15);
            border-color: #38bdf8;
            color: #38bdf8;
            transform: translateY(-1px);
        }
        .mushaf-step-btn:disabled {
            opacity: 0.4;
            cursor: not-allowed;
        }

        /* Deep Link & Action Buttons for Uraian */"""

assert css_target in content, "css_target not found"
content = content.replace(css_target, css_replacement, 1)
print("Step 1: Added Mushaf Per Kata CSS")

# 2. Replace #search-nav-container with the new Mushaf Per Kata console
html_nav_target = """        <!-- Search Surah & Ayat Navigation (Mode 2) -->
        <div id="search-nav-container" class="search-nav-card" style="display: none;">
            <div class="search-console-header">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem;">
                    <div class="search-console-title">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                        <span data-i18n-orig="Cari Surat & Nomor Ayat">Cari Surat & Nomor Ayat</span>
                    </div>
                    <button class="nav-action-btn secondary-btn" onclick="switchMainMode('thematic')" style="padding: 0.45rem 1rem; font-size: 0.88rem; display: inline-flex; align-items: center; gap: 0.4rem; border-radius: 999px;">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                        <span data-i18n-orig="Kembali ke Jelajah Tematis">Kembali ke Jelajah Tematis</span>
                    </button>
                </div>
                <div class="search-console-subtitle" data-i18n-orig="Ketahui Tema, Pokok Bahasan, dan Sub Pokok Bahasan ayat yang Anda pilih secara instan">Ketik nama surat & ayat langsung atau pilih dari daftar untuk melihat klasifikasi tematiknya secara instan</div>
            </div>

            <!-- Smart Direct Search Input Bar -->
            <div class="smart-search-box-wrap">
                <div class="smart-search-input-inner">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" class="search-icon"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                    <input type="text" id="smart-surah-ayat-input" class="smart-search-input" placeholder="Ketik nama surat & ayat (contoh: Al-Baqarah 255, 36:82, Yasin 82, Kahfi 10, An-Nas)..." data-i18n-placeholder="Ketik nama surat & ayat (contoh: Al-Baqarah 255, 36:82, Yasin 82, Kahfi 10, An-Nas)..." oninput="onSmartSearchInput(this.value)" onkeydown="onSmartSearchKeydown(event)" autocomplete="off">
                    <button id="btn-clear-smart-search" class="btn-clear-input" onclick="clearSmartSearch()" style="display: none;" title="Hapus pencarian">✕</button>
                </div>
                <div id="smart-search-suggestions" class="smart-suggestions-dropdown" style="display: none;"></div>
            </div>

            <!-- Quick Access Popular Verses -->
            <div class="popular-verses-row">
                <span class="popular-label">⚡ Akses Cepat:</span>
                <button class="popular-verse-chip" onclick="selectQuickVerse(2, 255)">Ayat Kursi (2:255)</button>
                <button class="popular-verse-chip" onclick="selectQuickVerse(1, 1)">Al-Fatihah (1:1)</button>
                <button class="popular-verse-chip" onclick="selectQuickVerse(18, 10)">Al-Kahfi (18:10)</button>
                <button class="popular-verse-chip" onclick="selectQuickVerse(36, 82)">Yasin (36:82)</button>
                <button class="popular-verse-chip" onclick="selectQuickVerse(67, 1)">Al-Mulk (67:1)</button>
                <button class="popular-verse-chip" onclick="selectQuickVerse(3, 190)">Ali 'Imran (3:190)</button>
                <button class="popular-verse-chip" onclick="selectQuickVerse(112, 1)">Al-Ikhlas (112:1)</button>
            </div>

            <div class="search-controls-row">
                <div class="search-field-group surah-field">
                    <label for="select-search-surah" data-i18n-orig="Surat Al-Qur'an (1–114):">Surat Al-Qur'an (1–114):</label>
                    <select id="select-search-surah" class="custom-select search-select" onchange="onSearchSurahChange()">
                        <option value="" data-i18n-orig="-- Pilih Surat --">-- Pilih Surat --</option>
                    </select>
                </div>

                <div class="search-field-group ayat-field">
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
                </div>
            </div>
        </div>"""

html_nav_replacement = """        <!-- Mushaf Per Kata Navigation (Mode 2) -->
        <div id="search-nav-container" class="mushaf-nav-card" style="display: none;">
            <div class="search-console-header">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem;">
                    <div class="search-console-title" style="display: flex; align-items: center; gap: 0.6rem;">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/></svg>
                        <span data-i18n-orig="Mushaf Per Kata">Mushaf Per Kata & Analisis Morfologi</span>
                    </div>
                    <div style="display: flex; gap: 0.6rem; align-items: center; flex-wrap: wrap;">
                        <a id="btn-portal-kamus" href="Mushaf Per Kata/Kamus/index.html?lang=id" target="_blank" rel="noopener noreferrer" class="nav-action-btn" style="background: rgba(253, 224, 71, 0.12); color: #fde047; border: 1px solid rgba(253, 224, 71, 0.4); padding: 0.45rem 1rem; font-size: 0.88rem; display: inline-flex; align-items: center; gap: 0.4rem; border-radius: 999px; text-decoration: none;" title="Buka Portal Kamus Al-Qur'an (39 Bahasa)">
                            <span>📖</span>
                            <span data-i18n-orig="Portal Kamus Al-Qur'an">Portal Kamus Al-Qur'an</span>
                        </a>
                        <button class="nav-action-btn secondary-btn" onclick="switchMainMode('thematic')" style="padding: 0.45rem 1rem; font-size: 0.88rem; display: inline-flex; align-items: center; gap: 0.4rem; border-radius: 999px;">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                            <span data-i18n-orig="Kembali ke Jelajah Tematis">Kembali ke Jelajah Tematis</span>
                        </button>
                    </div>
                </div>
                <div class="search-console-subtitle" data-i18n-orig="Telusuri setiap lafdz Al-Qur'an: Lafdz, Akar Kata, Dhamir/Harf Muttashil, Audio Per Kata, dan Terjemahan 7 Bahasa">
                    Telusuri setiap lafdz Al-Qur'an: Lafdz, Akar Kata, Dhamir/Harf Muttashil, Audio Per Kata, dan Terjemahan 7 Bahasa Dunia
                </div>
            </div>

            <div class="mushaf-controls-grid">
                <div class="search-field-group surah-field">
                    <label for="select-search-surah" data-i18n-orig="Pilih Surat:">Pilih Surat:</label>
                    <select id="select-search-surah" class="custom-select search-select" onchange="onSearchSurahChange()">
                        <option value="" data-i18n-orig="-- Pilih Surat --">-- Pilih Surat --</option>
                    </select>
                </div>

                <div class="search-field-group ayat-field">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <label for="select-search-ayat" data-i18n-orig="Pilih Ayat:">Pilih Ayat:</label>
                        <span id="ayat-range-hint" style="font-size: 0.8rem; color: #94a3b8; font-weight: 600;">(1–200)</span>
                    </div>
                    <div class="ayat-picker-row">
                        <button id="btn-ayat-prev" class="ayat-stepper-btn" onclick="stepAyat(-1)" title="Ayat Sebelumnya">◀</button>
                        <input type="number" id="input-search-ayat-num" class="custom-ayat-input" min="1" max="286" placeholder="No." onchange="onDirectAyatInput()" onkeydown="if(event.key==='Enter')onDirectAyatInput()" title="Ketik nomor ayat langsung">
                        <select id="select-search-ayat" class="custom-select search-select" onchange="onSearchAyatChange()">
                            <option value="">Pilih Ayat</option>
                        </select>
                        <button id="btn-ayat-next" class="ayat-stepper-btn" onclick="stepAyat(1)" title="Ayat Selanjutnya">▶</button>
                    </div>
                </div>
            </div>

            <div class="mushaf-lang-row">
                <span class="mushaf-lang-label" data-i18n-orig="Terjemahan Per Kata:">Terjemahan Per Kata:</span>
                <div class="mushaf-lang-pills">
                    <button class="mushaf-lang-btn active" data-lang="id" onclick="setMushafLanguage('id')">ID Indonesia</button>
                    <button class="mushaf-lang-btn" data-lang="en" onclick="setMushafLanguage('en')">EN English</button>
                    <button class="mushaf-lang-btn" data-lang="de" onclick="setMushafLanguage('de')">DE Deutsch</button>
                    <button class="mushaf-lang-btn" data-lang="ru" onclick="setMushafLanguage('ru')">RU Русский</button>
                    <button class="mushaf-lang-btn" data-lang="hi" onclick="setMushafLanguage('hi')">HI हिन्दी</button>
                    <button class="mushaf-lang-btn" data-lang="bn" onclick="setMushafLanguage('bn')">BN বাংলা</button>
                    <button class="mushaf-lang-btn" data-lang="tr" onclick="setMushafLanguage('tr')">TR Türkçe</button>
                </div>
            </div>
        </div>"""

assert html_nav_target in content, "html_nav_target not found"
content = content.replace(html_nav_target, html_nav_replacement, 1)
print("Step 2: Replaced search-nav-container with Mushaf Per Kata controls")

# 3. Update checkAutoNav to call openMushafPerKata
autonav_target = """                    if (s && a) {
                        setTimeout(() => lookupVerseInSearch(s, a), 100);
                        return;
                    }"""

autonav_replacement = """                    if (s && a) {
                        setTimeout(() => openMushafPerKata(s, a), 100);
                        return;
                    }"""

assert autonav_target in content, "autonav_target not found"
content = content.replace(autonav_target, autonav_replacement, 1)
print("Step 3: Updated checkAutoNav")

# 4. Update button in thematic cards from lookupVerseInSearch to openMushafPerKata
thematic_btn_target = """onclick="lookupVerseInSearch(${v.surah_num}, ${v.ayat_num}, event)" title="Lihat Mushaf Per Kata">"""
thematic_btn_replacement = """onclick="openMushafPerKata(${v.surah_num}, ${v.ayat_num}, event)" title="Lihat Mushaf Per Kata">"""

assert thematic_btn_target in content, "thematic_btn_target not found"
content = content.replace(thematic_btn_target, thematic_btn_replacement)
print("Step 4: Updated thematic card button onclick to openMushafPerKata")

# 5. Update keyword result card button from lookupVerseInSearch to openMushafPerKata
kw_btn_target = """onclick="lookupVerseInSearch(${v.surah_num}, ${v.ayat_num}, event)">
                                        ${lblOpenSearch}"""
kw_btn_replacement = """onclick="openMushafPerKata(${v.surah_num}, ${v.ayat_num}, event)">
                                        <span data-i18n-orig="Lihat Mushaf Per Kata">Lihat Mushaf Per Kata</span>"""

assert kw_btn_target in content, "kw_btn_target not found"
content = content.replace(kw_btn_target, kw_btn_replacement)
print("Step 5: Updated keyword card button onclick to openMushafPerKata")

# 6. Replace switchMainMode, lookupVerseInSearch, and renderSearchVerseResult with full Mushaf Per Kata engine
logic_target = """        function switchMainMode(mode) {
            stopTTS();
            activeMainMode = mode;
            const tabThematic = document.getElementById('tab-btn-thematic');
            const tabSearch = document.getElementById('tab-btn-search');
            const tabKeyword = document.getElementById('tab-btn-keyword');
            const thematicNav = document.getElementById('thematic-nav-container');
            const searchNav = document.getElementById('search-nav-container');
            const keywordNav = document.getElementById('keyword-nav-container');
            const thematicView = document.getElementById('thematic-view-wrapper');
            const searchView = document.getElementById('search-view-wrapper');
            const keywordView = document.getElementById('keyword-view-wrapper');

            // Reset all active states
            [tabThematic, tabSearch, tabKeyword].forEach(t => t && t.classList.remove('active'));
            [thematicNav, searchNav, keywordNav, thematicView, searchView, keywordView].forEach(el => el && (el.style.display = 'none'));

            if (mode === 'thematic') {
                if (tabThematic) tabThematic.classList.add('active');
                if (thematicNav) thematicNav.style.display = 'flex';
                if (thematicView) thematicView.style.display = 'block';
            } else if (mode === 'search') {
                if (tabSearch) tabSearch.classList.add('active');
                if (searchNav) searchNav.style.display = 'block';
                if (searchView) searchView.style.display = 'block';

                // Render current search verse if not already rendered
                if (!document.getElementById('current-rendered-verse')) {
                    renderSearchVerseResult(currentSearchSurah, currentSearchAyat);
                }
            } else if (mode === 'keyword') {
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

assert logic_target in content, "logic_target not found"

# Let's inspect what follows logic_target up to function lookupVerseInSearch
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Step 6 preparation complete!")
