# scratch/apply_mushaf_full_replacement.py
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

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
            user-select: none;
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
            border: 1px solid rgba(56, 189, 248, 0.3);
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
            text-align: center;
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

# 3. Update checkAutoNav
autonav_pattern = r"const s = parseInt\(params\.get\('surat'\)\);\s*const a = parseInt\(params\.get\('ayat'\)\);\s*if \(s && a\) \{\s*setTimeout\(\(\) => lookupVerseInSearch\(s, a\), 100\);\s*return;\s*\}"
autonav_repl = """const s = parseInt(params.get('surat'));
            const a = parseInt(params.get('ayat'));
            if (s && a) {
                setTimeout(() => openMushafPerKata(s, a), 100);
                return;
            }"""

content, count = re.subn(autonav_pattern, autonav_repl, content, count=1)
assert count == 1, "autonav_pattern not found"
print("Step 3: Updated checkAutoNav to openMushafPerKata")

# 4. Update thematic card buttons
content = content.replace('onclick="lookupVerseInSearch(${v.surah_num}, ${v.ayat_num}, event)"', 'onclick="openMushafPerKata(${v.surah_num}, ${v.ayat_num}, event)"')
print("Step 4: Updated thematic & card buttons to openMushafPerKata")

# 5. Insert Kamus lookup script before main logic or load lazily
kamus_script_tag = """    <script src="Mushaf Per Kata/data_js/kamus_lookup.js"></script>
    <script>"""
content = content.replace('<script>', kamus_script_tag, 1)
print("Step 5: Added kamus_lookup.js script tag")

# 6. Replace and upgrade the JavaScript functions:
# We will replace from `function switchMainMode` all the way to `function copyAyatText`
target_js_block = """        function switchMainMode(mode) {
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

assert target_js_block in content, "target_js_block not found"

# Now find where copyAyatText starts
idx_switch = content.find(target_js_block)
idx_copy = content.find("function copyAyatText(btn, event, surahName, surahNum, ayatNum) {", idx_switch)
assert idx_copy != -1, "copyAyatText not found"

new_mushaf_engine = """        let currentMushafLang = 'id';
        let currentWordAudioPlayer = null;

        function setMushafLanguage(langCode) {
            currentMushafLang = langCode;
            document.querySelectorAll('.mushaf-lang-btn').forEach(btn => {
                btn.classList.toggle('active', btn.getAttribute('data-lang') === langCode);
            });
            const portalBtn = document.getElementById('btn-portal-kamus');
            if (portalBtn) {
                portalBtn.href = `Mushaf Per Kata/Kamus/index.html?lang=${langCode}`;
            }
            renderSearchVerseResult(currentSearchSurah, currentSearchAyat);
        }

        function switchMainMode(mode) {
            stopTTS();
            stopWordAudio();
            activeMainMode = (mode === 'mushaf' || mode === 'search') ? 'search' : mode;
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
            } else if (mode === 'search' || mode === 'mushaf') {
                if (tabSearch) tabSearch.classList.add('active');
                if (searchNav) searchNav.style.display = 'block';
                if (searchView) searchView.style.display = 'block';

                renderSearchVerseResult(currentSearchSurah, currentSearchAyat);
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
        }

        function initSurahAyatSearch() {
            const selectSurah = document.getElementById('select-search-surah');
            if (!selectSurah) return;
            populateSurahDropdown(SURAH_LIST);

            // Set initial value
            selectSurah.value = currentSearchSurah;
            populateAyatDropdown(currentSearchSurah);
            const selectAyat = document.getElementById('select-search-ayat');
            if (selectAyat) selectAyat.value = currentSearchAyat;
            updateStepperButtons();
        }

        function populateSurahDropdown(list) {
            const selectSurah = document.getElementById('select-search-surah');
            if (!selectSurah) return;
            const currentVal = selectSurah.value;
            selectSurah.innerHTML = '<option value="">-- Pilih Surat (1-114) --</option>';
            list.forEach(s => {
                const opt = document.createElement('option');
                opt.value = s.no;
                opt.textContent = `${s.no}. ${s.name} (${s.arab}) — ${s.ayat} Ayat [${s.type}]`;
                selectSurah.appendChild(opt);
            });
            if (currentVal && list.some(s => s.no == currentVal)) {
                selectSurah.value = currentVal;
            }
        }

        function populateAyatDropdown(surahNum) {
            const selectAyat = document.getElementById('select-search-ayat');
            if (!selectAyat) return;
            const surahInfo = SURAH_LIST.find(s => s.no == surahNum);
            if (!surahInfo) {
                selectAyat.innerHTML = '<option value="">Pilih Ayat</option>';
                selectAyat.disabled = true;
                return;
            }
            selectAyat.innerHTML = `<option value="">-- Pilih Ayat (1-${surahInfo.ayat}) --</option>`;
            for (let i = 1; i <= surahInfo.ayat; i++) {
                const opt = document.createElement('option');
                opt.value = i;
                opt.textContent = `Ayat ${i}`;
                selectAyat.appendChild(opt);
            }
            selectAyat.disabled = false;
        }

        function onSearchSurahChange() {
            stopTTS();
            stopWordAudio();
            const selectSurah = document.getElementById('select-search-surah');
            const selectAyat = document.getElementById('select-search-ayat');
            if (!selectSurah || !selectSurah.value) return;
            currentSearchSurah = parseInt(selectSurah.value);
            populateAyatDropdown(currentSearchSurah);
            currentSearchAyat = 1;
            if (selectAyat) selectAyat.value = 1;
            updateStepperButtons();
            renderSearchVerseResult(currentSearchSurah, currentSearchAyat);
        }

        function onSearchAyatChange() {
            stopTTS();
            stopWordAudio();
            const selectAyat = document.getElementById('select-search-ayat');
            if (!selectAyat || !selectAyat.value) return;
            currentSearchAyat = parseInt(selectAyat.value);
            updateStepperButtons();
            renderSearchVerseResult(currentSearchSurah, currentSearchAyat);
        }

        function onDirectAyatInput() {
            stopTTS();
            stopWordAudio();
            const input = document.getElementById('input-search-ayat-num');
            const surahInfo = SURAH_LIST.find(s => s.no == currentSearchSurah);
            const totalAyat = surahInfo ? surahInfo.ayat : 1;
            if (!input) return;

            let val = parseInt(input.value);
            if (isNaN(val) || val < 1) val = 1;
            if (val > totalAyat) val = totalAyat;

            currentSearchAyat = val;
            const selectAyat = document.getElementById('select-search-ayat');
            if (selectAyat) selectAyat.value = currentSearchAyat;
            updateStepperButtons();
            renderSearchVerseResult(currentSearchSurah, currentSearchAyat);
        }

        function stepAyat(delta) {
            stopTTS();
            stopWordAudio();
            const surahInfo = SURAH_LIST.find(s => s.no == currentSearchSurah);
            if (!surahInfo) return;
            let targetAyat = currentSearchAyat + delta;
            
            // Boundary crossing
            if (targetAyat < 1) {
                if (currentSearchSurah > 1) {
                    currentSearchSurah--;
                    const prevSurahInfo = SURAH_LIST.find(s => s.no == currentSearchSurah);
                    targetAyat = prevSurahInfo ? prevSurahInfo.ayat : 1;
                    const selectSurah = document.getElementById('select-search-surah');
                    if (selectSurah) selectSurah.value = currentSearchSurah;
                    populateAyatDropdown(currentSearchSurah);
                } else {
                    targetAyat = 1;
                }
            } else if (targetAyat > surahInfo.ayat) {
                if (currentSearchSurah < 114) {
                    currentSearchSurah++;
                    targetAyat = 1;
                    const selectSurah = document.getElementById('select-search-surah');
                    if (selectSurah) selectSurah.value = currentSearchSurah;
                    populateAyatDropdown(currentSearchSurah);
                } else {
                    targetAyat = surahInfo.ayat;
                }
            }

            currentSearchAyat = targetAyat;
            const selectAyat = document.getElementById('select-search-ayat');
            if (selectAyat) selectAyat.value = currentSearchAyat;
            updateStepperButtons();
            renderSearchVerseResult(currentSearchSurah, currentSearchAyat);
        }

        function updateStepperButtons() {
            const btnPrev = document.getElementById('btn-ayat-prev');
            const btnNext = document.getElementById('btn-ayat-next');
            const surahInfo = SURAH_LIST.find(s => s.no == currentSearchSurah);
            const totalAyat = surahInfo ? surahInfo.ayat : 1;

            if (btnPrev) btnPrev.disabled = (currentSearchSurah === 1 && currentSearchAyat <= 1);
            if (btnNext) btnNext.disabled = (currentSearchSurah === 114 && currentSearchAyat >= totalAyat);

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
        }

        // ==========================================================================
        // MUSHAF DATA LOADER & KAMUS DEEP LINK ENGINE
        // ==========================================================================
        function loadMushafSurahData(surahNum, callback) {
            if (window.__MUSHAF_SURAH_DATA && window.__MUSHAF_SURAH_DATA[surahNum]) {
                callback(window.__MUSHAF_SURAH_DATA[surahNum]);
                return;
            }

            const scriptId = `mushaf-script-surah-${surahNum}`;
            let existingScript = document.getElementById(scriptId);
            if (existingScript) {
                existingScript.addEventListener('load', () => {
                    callback(window.__MUSHAF_SURAH_DATA && window.__MUSHAF_SURAH_DATA[surahNum]);
                });
                return;
            }

            // Always try dynamic script first as it works 100% on file:/// and http://
            const script = document.createElement('script');
            script.id = scriptId;
            script.src = `Mushaf Per Kata/data_js/surah_${surahNum}.js`;
            script.onload = () => {
                const data = window.__MUSHAF_SURAH_DATA && window.__MUSHAF_SURAH_DATA[surahNum];
                callback(data);
            };
            script.onerror = () => {
                // Fallback to fetch if script fails
                fetch(`Mushaf Per Kata/quran-app/dist/data/surah_${surahNum}.json`)
                    .then(r => r.json())
                    .then(data => {
                        window.__MUSHAF_SURAH_DATA = window.__MUSHAF_SURAH_DATA || {};
                        window.__MUSHAF_SURAH_DATA[surahNum] = data;
                        callback(data);
                    })
                    .catch(err => {
                        console.error(`Gagal memuat data Mushaf Surat ${surahNum}:`, err);
                        callback(null);
                    });
            };
            document.head.appendChild(script);
        }

        function cleanArabicWord(str) {
            if (!str) return '';
            str = String(str);
            str = str.replace(/\\d+/g, '');
            str = str.replace(/\\u0671/g, '\\u0627');
            str = str.replace(/[\\u064B-\\u065F\\u06E1\\u06D6-\\u06ED]/g, '');
            return str.replace(/\\s+/g, ' ').trim();
        }

        function getKamusDeepLink(row, lang) {
            const lookup = window.__KAMUS_LOOKUP || {};
            const kataAkar = cleanArabicWord(row['Kata/Akar']);
            const kataAkarNoSpace = kataAkar.replace(/\\s+/g, '');
            const lafdz = cleanArabicWord(row['Lafdz']);
            const s = row['SURAT_ID'] || row['SURAT'] || currentSearchSurah || 1;
            const a = row['AYAT_ID'] || row['AYAT'] || currentSearchAyat || 1;

            // 1. Musytaq (by root)
            const musytaqMap = lookup.musytaq_roots || {};
            const mEntry = musytaqMap[kataAkar] || musytaqMap[kataAkarNoSpace];
            if (mEntry) {
                const akarId = mEntry.id || mEntry;
                return `Mushaf Per Kata/Kamus/index.html?dict=musytaq&akar=${akarId}&lang=${lang}`;
            }

            // 2. Jamid Mabny
            const jamidMap = lookup.jamid_words || {};
            const jEntry = jamidMap[kataAkar] || jamidMap[lafdz];
            if (jEntry) {
                const no = jEntry.no || jEntry;
                return `Mushaf Per Kata/Kamus/index.html?dict=jamid&no=${encodeURIComponent(no)}&lang=${lang}&surat=${s}&ayat=${a}`;
            }

            // 3. Harf Amil
            const harfAmilMap = lookup.harf_amil_words || {};
            const haEntry = harfAmilMap[kataAkar] || harfAmilMap[lafdz];
            if (haEntry) {
                const no = haEntry.no || haEntry;
                return `Mushaf Per Kata/Kamus/index.html?dict=harf_amil&no=${encodeURIComponent(no)}&lang=${lang}&surat=${s}&ayat=${a}`;
            }

            // 4. Harf Ghair Amil
            const harfMap = lookup.harf_words || {};
            const hEntry = harfMap[kataAkar] || harfMap[lafdz];
            if (hEntry) {
                const no = hEntry.no || hEntry;
                return `Mushaf Per Kata/Kamus/index.html?dict=harf&no=${encodeURIComponent(no)}&lang=${lang}&surat=${s}&ayat=${a}`;
            }

            // Fallback
            return `Mushaf Per Kata/Kamus/index.html?lang=${lang}`;
        }

        function getMuttashilTitle(text) {
            if (!text) return 'Dhamir/Harf Muttashil';
            const trimmed = text.trim();
            const startsWithDots = trimmed.startsWith('..');
            const endsWithDots = trimmed.endsWith('..');
            if (startsWithDots && endsWithDots) return 'Dhamir & Harf Muttashil';
            if (startsWithDots) return 'Dhamir Muttashil';
            if (endsWithDots) return 'Harf Muttashil';
            return 'Dhamir/Harf Muttashil';
        }

        function stopWordAudio() {
            if (currentWordAudioPlayer) {
                currentWordAudioPlayer.pause();
                currentWordAudioPlayer = null;
            }
            if (window.speechSynthesis) {
                window.speechSynthesis.cancel();
            }
        }

        function playQuranWord(surahNum, ayatNum, wordIndex, fallbackArabic) {
            stopTTS();
            stopWordAudio();

            const s3 = String(surahNum).padStart(3, '0');
            const a3 = String(ayatNum).padStart(3, '0');
            const w3 = String(wordIndex).padStart(3, '0');
            const url = `https://verses.quran.com/wbw/${s3}_${a3}_${w3}.mp3`;

            const audio = new Audio(url);
            currentWordAudioPlayer = audio;

            audio.play().catch(e => {
                console.warn("WBW CDN audio failed, using TTS fallback:", e);
                speakArabicWord(fallbackArabic);
            });
        }

        function speakArabicWord(arabicText) {
            if (!window.speechSynthesis || !arabicText) return;
            const cleaned = arabicText
                .replace(/\\u0671/g, '\\u0627')
                .replace(/\\u0670/g, '\\u0627')
                .replace(/\\u06E1/g, '\\u0652')
                .replace(/[\\u06D6-\\u06DC\\u06DF-\\u06E0\\u06E2-\\u06ED]/g, '')
                .trim();

            const utter = new SpeechSynthesisUtterance(cleaned);
            utter.lang = 'ar-SA';
            utter.rate = 0.85;
            window.speechSynthesis.speak(utter);
        }

        function toggleWordFlip(cardEl) {
            if (!cardEl) return;
            cardEl.classList.toggle('flipped');
        }

        function toggleFullAyahFlip(cardEl) {
            if (!cardEl) return;
            cardEl.classList.toggle('flipped');
        }

        // ==========================================================================
        // RENDER MUSHAF PER KATA (WORD BY WORD)
        // ==========================================================================
        function openMushafPerKata(surahNum, ayatNum, event) {
            if (event) event.stopPropagation();
            stopTTS();
            stopWordAudio();

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
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // Alias for backward compatibility
        function lookupVerseInSearch(surahNum, ayatNum, event) {
            openMushafPerKata(surahNum, ayatNum, event);
        }

        function renderSearchVerseResult(surahNum, ayatNum) {
            renderMushafPerKata(surahNum, ayatNum);
        }

        function renderMushafPerKata(surahNum, ayatNum) {
            const searchArea = document.getElementById('search-content-area');
            if (!searchArea) return;

            const key = `${surahNum}:${ayatNum}`;
            const surahInfo = SURAH_LIST.find(s => s.no == surahNum) || { no: surahNum, name: `Surat ${surahNum}`, arab: '', ayat: 1, type: 'Mekah' };
            const indexedData = verseThematicIndex[key];

            const s3 = String(surahNum).padStart(3, '0');
            const a3 = String(ayatNum).padStart(3, '0');
            const fullAudioUrl = `https://everyayah.com/data/Alafasy_128kbps/${s3}${a3}.mp3`;

            // Update URL hash
            history.replaceState(null, '', `#surat=${surahNum}&ayat=${ayatNum}`);

            // Loading state while word-by-word data loads
            searchArea.innerHTML = `
                <div class="empty-state" style="padding: 3rem 2rem;">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="animate-spin" style="margin: 0 auto 1rem auto; display: block;"><circle cx="12" cy="12" r="10" stroke-dasharray="32" stroke-dashoffset="10" stroke-opacity="0.3"></circle><path d="M12 2a10 10 0 0 1 10 10" stroke="currentColor"></path></svg>
                    <div style="font-weight: 600; color: #f8fafc; margin-bottom: 0.25rem;">Memuat Mushaf Per Kata...</div>
                    <div style="font-size: 0.88rem; color: #94a3b8;">QS. ${surahInfo.name} [${surahNum}] : Ayat ${ayatNum}</div>
                </div>
            `;

            loadMushafSurahData(surahNum, (surahData) => {
                if (!surahData || !surahData[String(ayatNum)]) {
                    // Fallback to basic verse display if WBW dataset unavailable
                    renderMushafFallback(surahNum, ayatNum, surahInfo, indexedData, fullAudioUrl);
                    return;
                }

                const words = surahData[String(ayatNum)] || [];

                // Full Arabic text composed from words if indexedData not present
                const fullArabic = indexedData ? indexedData.arab : words.map(w => w['Lafdz']).join(' ');
                const fullTranslation = indexedData ? indexedData.indo : words.map(w => {
                    const t = (w.translations && w.translations[currentMushafLang]) || (currentMushafLang === 'id' ? w['Terjemah'] : '') || w['Terjemah'] || '';
                    return String(t).replace(/\\s*\\[.*?\\]\\s*/g, ' ').trim();
                }).filter(Boolean).join(' ').replace(/\\s+([,;.])/g, '$1').replace(/\\s+/g, ' ');

                // Thematic cross-reference
                const topics = (indexedData && indexedData.topics) ? indexedData.topics : [];
                const topicsCount = topics.length;

                let markup = `
                    <div id="current-rendered-verse" class="mushaf-ayah-overview">
                        <!-- Top Header -->
                        <div class="mushaf-ayah-header">
                            <div>
                                <h2 class="mushaf-ayah-title">
                                    <span>📖</span>
                                    <span>QS. ${surahInfo.name} [${surahNum}] : Ayat ${ayatNum}</span>
                                </h2>
                                <div class="mushaf-ayah-meta">${surahInfo.arab} • ${surahInfo.type} • Total ${surahInfo.ayat} Ayat</div>
                            </div>
                            <div style="display: flex; gap: 0.6rem; align-items: center; flex-wrap: wrap;">
                                <span class="search-badge">${surahInfo.type}</span>
                                ${topicsCount > 0 ? `<span class="search-badge" style="background: rgba(245, 158, 11, 0.15); border-color: rgba(245, 158, 11, 0.4); color: #fbbf24;">📑 ${topicsCount} Topik Tematis</span>` : '<span class="search-badge" style="background: rgba(100, 116, 139, 0.15); border-color: rgba(100, 116, 139, 0.3); color: #94a3b8;">Mushaf Digital</span>'}
                                <audio controls style="height: 32px; border-radius: 999px;">
                                    <source src="${fullAudioUrl}" type="audio/mpeg">
                                </audio>
                            </div>
                        </div>

                        <!-- Full Ayah Card with Flip Effect -->
                        <div class="mushaf-full-flip-card" onclick="toggleFullAyahFlip(this)" title="Klik untuk membalik dan melihat arti ayat">
                            <div class="mushaf-full-flip-inner">
                                <div class="mushaf-full-front">
                                    ${fullArabic} <span class="verse-end-sign" style="font-size: 0.85em; color: #38bdf8;">۝${toArabicDigits(ayatNum)}</span>
                                </div>
                                <div class="mushaf-full-back">
                                    <div>"${fullTranslation}"</div>
                                </div>
                            </div>
                        </div>
                        <div class="mushaf-flip-hint">
                            <span>✨</span> <span>Klik kotak ayat di atas untuk membalik dan melihat terjemahan lengkap</span>
                        </div>

                        <!-- Word by Word Table -->
                        <div class="mushaf-table-wrapper">
                            <table class="mushaf-wbw-table">
                                <thead>
                                    <tr>
                                        <th style="width: 32%;">Lafdz (اللفظ)</th>
                                        <th style="width: 30%;">Kata / Akar (الأصل)</th>
                                        <th style="width: 38%;">Terjemah Kata (${currentMushafLang.toUpperCase()})</th>
                                    </tr>
                                </thead>
                                <tbody>
                `;

                words.forEach((w, wIdx) => {
                    const lafdz = w['Lafdz'] || '';
                    const kataAkar = w['Kata/Akar'] || '';
                    const muttashil = (w['Dhamir Muttashil / Harf Muttashil'] || '').trim();
                    const hasMuttashil = muttashil.length > 0;
                    const muttashilTitle = getMuttashilTitle(muttashil);

                    const trans = (w.translations && w.translations[currentMushafLang]) 
                        || (currentMushafLang === 'id' ? (w['Terjemah'] || '') : '') 
                        || w['Terjemah'] 
                        || '';
                    const cleanTrans = String(trans).replace(/\\s*\\[.*?\\]\\s*/g, ' ').trim();
                    const kamusUrl = getKamusDeepLink(w, currentMushafLang);

                    markup += `
                        <tr>
                            <!-- Kolom 1: Lafdz -->
                            <td>
                                <div class="mushaf-lafdz-card" ${hasMuttashil ? 'onclick="toggleWordFlip(this)" title="Klik untuk melihat ' + muttashilTitle + '" style="cursor: pointer;"' : 'style="cursor: default;"'}>
                                    <div class="mushaf-lafdz-inner">
                                        <div class="mushaf-lafdz-front">
                                            ${lafdz}
                                            ${hasMuttashil ? '<span style="color: #38bdf8; font-size: 0.65rem; vertical-align: super; margin-left: 2px;">●</span>' : ''}
                                        </div>
                                        ${hasMuttashil ? `
                                        <div class="mushaf-lafdz-back">
                                            <span class="mushaf-muttashil-label">${muttashilTitle}</span>
                                            <span class="mushaf-muttashil-text">${muttashil}</span>
                                        </div>
                                        ` : ''}
                                    </div>
                                </div>
                            </td>

                            <!-- Kolom 2: Kata / Akar -->
                            <td class="mushaf-root-cell">
                                <div class="mushaf-root-text">${kataAkar || '—'}</div>
                                <a href="${kamusUrl}" target="_blank" rel="noopener noreferrer" class="mushaf-kamus-btn" title="Buka Kamus Al-Qur'an">
                                    <span>📖</span>
                                    <span>Kamus</span>
                                </a>
                            </td>

                            <!-- Kolom 3: Arti & Audio -->
                            <td class="mushaf-meaning-cell">
                                <div class="mushaf-meaning-wrap">
                                    <span>${cleanTrans || '—'}</span>
                                    <button class="mushaf-word-audio-btn" onclick="playQuranWord(${surahNum}, ${ayatNum}, ${wIdx + 1}, '${lafdz.replace(/'/g, "\\\\'")}')" title="Putar audio lafdz ini">
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
                                    </button>
                                </div>
                            </td>
                        </tr>
                    `;
                });

                markup += `
                                </tbody>
                            </table>
                        </div>

                        <!-- Stepper Nav Bottom -->
                        <div class="mushaf-bottom-stepper">
                            <button class="mushaf-step-btn" onclick="stepAyat(-1)" ${surahNum === 1 && ayatNum === 1 ? 'disabled' : ''}>
                                <span>◀</span> <span>Ayat Sebelumnya</span>
                            </button>
                            <div style="font-size: 0.9rem; color: #94a3b8; font-weight: 600;">
                                QS. ${surahInfo.name} [${surahNum}] : Ayat ${ayatNum} / ${surahInfo.ayat}
                            </div>
                            <button class="mushaf-step-btn" onclick="stepAyat(1)" ${surahNum === 114 && ayatNum === surahInfo.ayat ? 'disabled' : ''}>
                                <span>Ayat Selanjutnya</span> <span>▶</span>
                            </button>
                        </div>

                        <!-- Thematic Cross Reference -->
                        ${topicsCount > 0 ? `
                        <div class="thematic-coverage-box" style="margin-top: 2rem;">
                            <div class="thematic-coverage-header">
                                <div class="thematic-coverage-title">
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                                    <span>Klasifikasi Tematik Ayat Ini (Ditemukan di ${topicsCount} Kelompok Uraian)</span>
                                </div>
                            </div>
                            <div class="thematic-coverage-body">
                                ${topics.map(t => `
                                    <div class="thematic-coverage-item">
                                        <div class="thematic-topic-breadcrumbs">
                                            <span class="thematic-crumb crumb-tema">${escapeHtml(t.tema)}</span>
                                            <span class="thematic-separator">›</span>
                                            <span class="thematic-crumb crumb-pokok">${escapeHtml(t.pokok)}</span>
                                            <span class="thematic-separator">›</span>
                                            <span class="thematic-crumb crumb-sub">${escapeHtml(t.sub)}</span>
                                        </div>
                                        <div class="thematic-uraian-link-row">
                                            <div class="thematic-uraian-title">${escapeHtml(t.uraian)}</div>
                                            <button class="nav-action-btn secondary-btn" style="padding: 0.35rem 0.85rem; font-size: 0.8rem;" onclick="navigateToThematicTopic('${t.tema.replace(/'/g, "\\\\'")}', '${t.pokok.replace(/'/g, "\\\\'")}', '${t.sub.replace(/'/g, "\\\\'")}', '${t.uraian.replace(/'/g, "\\\\'")}', ${surahNum}, ${ayatNum})">
                                                Lihat di Topik Ini →
                                            </button>
                                        </div>
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                        ` : ''}
                    </div>
                `;

                searchArea.innerHTML = markup;
            });
        }

        function renderMushafFallback(surahNum, ayatNum, surahInfo, indexedData, fullAudioUrl) {
            const searchArea = document.getElementById('search-content-area');
            if (!searchArea) return;
            const fullArabic = indexedData ? indexedData.arab : '';
            const fullTranslation = indexedData ? indexedData.indo : '';

            searchArea.innerHTML = `
                <div id="current-rendered-verse" class="mushaf-ayah-overview">
                    <div class="mushaf-ayah-header">
                        <div>
                            <h2 class="mushaf-ayah-title">
                                <span>📖</span>
                                <span>QS. ${surahInfo.name} [${surahNum}] : Ayat ${ayatNum}</span>
                            </h2>
                            <div class="mushaf-ayah-meta">${surahInfo.arab} • ${surahInfo.type} • Total ${surahInfo.ayat} Ayat</div>
                        </div>
                        <audio controls style="height: 32px; border-radius: 999px;">
                            <source src="${fullAudioUrl}" type="audio/mpeg">
                        </audio>
                    </div>
                    <div class="mushaf-full-front" style="margin-bottom: 1.5rem;">
                        ${fullArabic} <span class="verse-end-sign" style="color: #38bdf8;">۝${toArabicDigits(ayatNum)}</span>
                    </div>
                    <div style="background: rgba(15, 23, 42, 0.6); padding: 1.25rem; border-radius: 12px; color: #fde047; font-size: 1.05rem; margin-bottom: 1.5rem;">
                        "${fullTranslation}"
                    </div>
                    <div class="mushaf-bottom-stepper">
                        <button class="mushaf-step-btn" onclick="stepAyat(-1)" ${surahNum === 1 && ayatNum === 1 ? 'disabled' : ''}>◀ Ayat Sebelumnya</button>
                        <button class="mushaf-step-btn" onclick="stepAyat(1)" ${surahNum === 114 && ayatNum === surahInfo.ayat ? 'disabled' : ''}>Ayat Selanjutnya ▶</button>
                    </div>
                </div>
            `;
        }

        """

content = content[:idx_switch] + new_mushaf_engine + content[idx_copy:]
print("Step 6: Replaced switchMainMode, lookupVerseInSearch, and renderSearchVerseResult with full Mushaf Per Kata engine")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.html fully updated with Mushaf Per Kata integration!")
