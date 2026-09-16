import re
import shutil

def main():
    html_file = 'index.html'
    backup_file = 'scratch/index.html.before_multilang_kw.bak'
    shutil.copy2(html_file, backup_file)
    print("Backup created at", backup_file)

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the old block to replace from index.html (lines 5188 to 5560 approx)
    old_start_marker = "        /* ==========================================================================\n           FITUR 2: Pencarian Kata Kunci (Uraian & Teks Ayat)\n           ========================================================================== */"
    old_end_marker = "            // If in non-Indonesian mode, translate dynamic titles and verses in results\n            if (targetLang !== 'id') {\n                translatePageContent();\n            }\n        }"

    start_idx = content.find(old_start_marker)
    if start_idx == -1:
        print("ERROR: old_start_marker not found!")
        return

    end_idx = content.find(old_end_marker, start_idx)
    if end_idx == -1:
        print("ERROR: old_end_marker not found!")
        return
    end_idx += len(old_end_marker)

    old_full_block = content[start_idx:end_idx]

    # Now let's create the comprehensive new block
    new_kw_block = '''        /* ==========================================================================
           FITUR 2: Pencarian Kata Kunci (Uraian & Teks Ayat) - Multilingual & Full-Text
           ========================================================================== */
        const KEYWORD_SYNONYMS = {
            // Intoxicants & Wine (e.g. drunk, wine, alcohol, khamr)
            'drunk': ['mabuk', 'khamr', 'khamar', 'memabukkan'],
            'drunkenness': ['mabuk', 'khamr', 'khamar', 'memabukkan'],
            'intoxicated': ['mabuk', 'khamr', 'khamar', 'memabukkan'],
            'intoxicant': ['mabuk', 'khamr', 'khamar', 'memabukkan'],
            'intoxicants': ['mabuk', 'khamr', 'khamar', 'memabukkan'],
            'wine': ['khamr', 'khamar', 'anggur', 'mabuk'],
            'alcohol': ['khamr', 'khamar', 'mabuk', 'alkohol'],
            'liquor': ['khamr', 'khamar', 'mabuk'],
            'mabuk': ['khamr', 'khamar', 'memabukkan'],
            'khamr': ['mabuk', 'khamar', 'memabukkan', 'arak'],
            'khamar': ['mabuk', 'khamr', 'memabukkan', 'arak'],

            // Core Virtues & Pillars
            'patience': ['sabar', 'kesabaran', 'tabah'],
            'patient': ['sabar', 'tabah'],
            'persevere': ['sabar', 'bertahan'],
            'perseverance': ['sabar', 'ketabahan'],
            'sabar': ['kesabaran', 'tabah'],
            'prayer': ['shalat', 'salat', 'doa'],
            'prayers': ['shalat', 'salat', 'doa'],
            'pray': ['shalat', 'salat', 'berdoa'],
            'shalat': ['salat', 'doa', 'sembahyang'],
            'salat': ['shalat', 'doa'],
            'worship': ['ibadah', 'menyembah'],
            'worshipping': ['ibadah', 'menyembah'],
            'ibadah': ['menyembah', 'penghambaan'],
            'usury': ['riba'],
            'interest': ['riba', 'bunga'],
            'riba': ['bunga uang', 'rente'],
            'repentance': ['taubat', 'tobat'],
            'repent': ['taubat', 'tobat', 'bertaubat'],
            'taubat': ['tobat', 'kembali'],
            'tobat': ['taubat'],
            'provision': ['rezeki', 'rejeki', 'penghidupan'],
            'sustenance': ['rezeki', 'rejeki', 'nafkah'],
            'livelihood': ['rezeki', 'nafkah', 'mata pencaharian'],
            'rezeki': ['rejeki', 'nafkah', 'anugerah'],
            'paradise': ['surga', 'jannah'],
            'heaven': ['surga', 'jannah', 'langit'],
            'heavens': ['surga', 'langit'],
            'jannah': ['surga'],
            'surga': ['jannah', 'kenikmatan'],
            'hell': ['neraka', 'jahannam', 'saqor'],
            'hellfire': ['neraka', 'jahannam', 'api neraka'],
            'fire': ['api', 'neraka'],
            'jahannam': ['neraka'],
            'neraka': ['jahannam', 'saqor'],
            'parents': ['orang tua', 'ibu bapak', 'ayah bunda'],
            'parent': ['orang tua'],
            'father': ['ayah', 'bapak'],
            'mother': ['ibu', 'bunda'],
            'children': ['anak', 'keturunan'],
            'child': ['anak'],
            'charity': ['sedekah', 'infaq', 'infak', 'zakat'],
            'alms': ['sedekah', 'zakat'],
            'almsgiving': ['sedekah', 'zakat'],
            'zakat': ['zakat', 'sedekah'],
            'sedekah': ['infak', 'zakat', 'derma'],
            'doomsday': ['kiamat', 'hari kiamat', 'hari akhir'],
            'judgment': ['kiamat', 'hari pembalasan', 'hisab'],
            'day of judgment': ['kiamat', 'hari kiamat', 'hari pembalasan'],
            'resurrection': ['kiamat', 'kebangkitan', 'hari berbangkit'],
            'kiamat': ['hari akhir', 'hari kiamat', 'kebangkitan'],
            'gratitude': ['syukur', 'bersyukur'],
            'grateful': ['syukur', 'bersyukur'],
            'thanks': ['syukur', 'terima kasih'],
            'thankfulness': ['syukur'],
            'syukur': ['bersyukur', 'berterima kasih'],
            'fasting': ['puasa', 'shaum'],
            'fast': ['puasa'],
            'puasa': ['shaum'],
            'pilgrimage': ['haji', 'umrah'],
            'hajj': ['haji'],
            'haji': ['umrah', 'baitullah'],
            'human': ['manusia', 'insan'],
            'humans': ['manusia', 'umat manusia'],
            'mankind': ['manusia', 'bani adam'],
            'people': ['manusia', 'kaum', 'orang-orang'],
            'manusia': ['insan', 'bani adam'],
            'creation': ['penciptaan', 'ciptaan', 'makhluk'],
            'creator': ['pencipta', 'khaliq'],

            // Faith & Theology
            'faith': ['iman', 'keimanan', 'percaya'],
            'belief': ['iman', 'keyakinan'],
            'believer': ['mukmin', 'orang beriman'],
            'believers': ['mukmin', 'orang-orang beriman'],
            'iman': ['keyakinan', 'mukmin'],
            'mukmin': ['orang beriman'],
            'disbelief': ['kafir', 'kekafiran', 'ingkar'],
            'disbeliever': ['kafir', 'orang kafir'],
            'disbelievers': ['kafir', 'orang-orang kafir'],
            'kafir': ['kekafiran', 'orang kafir'],
            'polytheism': ['syirik', 'menyekutukan'],
            'polytheist': ['musyrik'],
            'polytheists': ['musyrik', 'orang-orang musyrik'],
            'syirik': ['menyekutukan allah', 'musyrik'],
            'musyrik': ['orang musyrik'],
            'idol': ['berhala'],
            'idols': ['berhala'],
            'berhala': ['patung sembahan'],
            'god': ['allah', 'tuhan'],
            'lord': ['tuhan', 'rabb'],
            'allah': ['tuhan', 'allah swt'],
            'taqwa': ['takwa'],
            'piety': ['takwa', 'kesalehan'],
            'takwa': ['ketakwaan', 'takwa'],
            'righteous': ['saleh', 'kebaikan', 'amal saleh'],
            'saleh': ['amal saleh', 'kebaikan'],
            'prophet': ['nabi', 'rasul'],
            'prophets': ['nabi', 'rasul'],
            'nabi': ['rasul'],
            'messenger': ['rasul'],
            'messengers': ['rasul'],
            'rasul': ['nabi', 'utusan allah'],
            'angel': ['malaikat'],
            'angels': ['malaikat'],
            'malaikat': ['jibril', 'mikail', 'izrail', 'israfil'],
            'jinn': ['jin'],
            'jinns': ['jin'],
            'jin': ['bangsa jin'],
            'satan': ['setan', 'syaitan', 'iblis'],
            'devil': ['setan', 'syaitan', 'iblis'],
            'demon': ['setan'],
            'iblis': ['iblis', 'setan'],
            'setan': ['iblis', 'syaitan'],

            // Morals, Ethics & Law
            'justice': ['adil', 'keadilan'],
            'fair': ['adil'],
            'fairness': ['keadilan'],
            'adil': ['keadilan'],
            'keadilan': ['adil'],
            'truth': ['kebenaran', 'hak', 'benar'],
            'true': ['benar', 'hak'],
            'lie': ['dusta', 'bohong'],
            'lies': ['dusta', 'bohong'],
            'liar': ['pendusta'],
            'liars': ['pendusta'],
            'dusta': ['bohong', 'pendusta'],
            'hypocrite': ['munafik'],
            'hypocrites': ['munafik', 'orang-orang munafik'],
            'hypocrisy': ['kemunafikan', 'munafik'],
            'munafik': ['orang munafik', 'kemunafikan'],
            'oppress': ['zalim', 'menzalimi'],
            'oppression': ['zalim', 'kezaliman'],
            'oppressor': ['zalim', 'orang zalim'],
            'wrongdoer': ['zalim', 'orang-orang zalim'],
            'wrongdoers': ['zalim', 'orang-orang zalim'],
            'zalim': ['kezaliman', 'orang zalim'],
            'forgive': ['ampunan', 'mengampuni', 'memaafkan'],
            'forgiveness': ['ampunan', 'pengampunan', 'maaf'],
            'ampunan': ['pengampunan', 'maghfirah'],
            'mercy': ['rahmat', 'kasih sayang'],
            'merciful': ['maha penyayang', 'pengasih', 'rahmat'],
            'rahmat': ['kasih sayang', 'belas kasih'],
            'love': ['cinta', 'kasih'],
            'marriage': ['pernikahan', 'nikah', 'kawin'],
            'marry': ['menikah', 'nikah'],
            'nikah': ['pernikahan', 'kawin'],
            'divorce': ['cerai', 'talak'],
            'cerai': ['talak'],
            'orphan': ['yatim', 'anak yatim'],
            'orphans': ['yatim', 'anak-anak yatim'],
            'yatim': ['anak yatim'],
            'poor': ['miskin', 'fakir miskin'],
            'needy': ['fakir', 'miskin'],
            'miskin': ['fakir', 'dhuafa'],
            'debt': ['utang', 'piutang'],
            'utang': ['piutang'],
            'trade': ['dagang', 'perniagaan', 'jual beli'],
            'business': ['perniagaan', 'jual beli'],
            'dagang': ['jual beli', 'perniagaan'],
            'swine': ['babi'],
            'pork': ['babi'],
            'babi': ['daging babi'],
            'gambling': ['judi', 'berjudi', 'mengundi nasib'],
            'judi': ['berjudi', 'mengundi nasib', 'khamr'],
            'adultery': ['zina'],
            'zina': ['perzinaan'],
            'modesty': ['malu', 'kesucian', 'menjaga pandangan'],
            'arrogance': ['sombong', 'takabur', 'angkuh'],
            'arrogant': ['sombong', 'takabur', 'angkuh'],
            'sombong': ['takabur', 'angkuh'],
            'envy': ['hasad', 'dengki', 'iri'],
            'dengki': ['hasad', 'iri'],
            'backbiting': ['ghibah', 'menggunjing'],
            'ghibah': ['menggunjing'],
            'peace': ['damai', 'perdamaian', 'salam'],
            'damai': ['perdamaian', 'salam'],
            'war': ['perang'],
            'fight': ['perang', 'berperang'],
            'fighting': ['perang', 'berperang', 'jihad'],
            'jihad': ['jihad', 'berjuang', 'perang'],
            'perang': ['berperang', 'jihad'],
            'death': ['mati', 'kematian', 'ajal', 'wafat'],
            'die': ['mati', 'meninggal'],
            'mati': ['kematian', 'ajal', 'wafat'],
            'kematian': ['mati', 'ajal', 'wafat'],
            'grave': ['kubur', 'kuburan', 'alam barzakh'],
            'kubur': ['kuburan', 'alam barzakh'],
            'knowledge': ['ilmu', 'pengetahuan'],
            'ilmu': ['pengetahuan', 'hikmah'],
            'wisdom': ['hikmah', 'kebijaksanaan'],
            'hikmah': ['kebijaksanaan'],
            'guidance': ['petunjuk', 'hidayah'],
            'hidayah': ['petunjuk'],
            'sin': ['dosa', 'kesalahan', 'maksiat'],
            'sins': ['dosa', 'kesalahan', 'maksiat'],
            'dosa': ['maksiat', 'kesalahan'],
            'evil': ['kejahatan', 'buruk', 'keji'],
            'heart': ['hati', 'kalbu'],
            'hearts': ['hati', 'kalbu'],
            'hati': ['kalbu', 'jiwa'],
            'soul': ['jiwa', 'ruh'],
            'water': ['air'],
            'rain': ['hujan'],
            'air': ['hujan', 'sungai', 'laut'],
            'hujan': ['air hujan'],
            'sun': ['matahari'],
            'moon': ['bulan'],
            'stars': ['bintang'],
            'sky': ['langit'],
            'earth': ['bumi'],
            'mountain': ['gunung'],
            'animal': ['binatang', 'hewan'],
            'honey': ['madu'],
            'madu': ['lebah'],
            'bee': ['lebah'],
            'lebah': ['madu'],
            'ant': ['semut'],
            'iron': ['besi'],
            'gold': ['emas'],
            'silver': ['perak'],
            'tree': ['pohon']
        };

        function getIndonesianBaseWords(word) {
            if (!word || word.length < 5) return [word];
            const bases = new Set([word]);

            if (word.startsWith('peng') && word.endsWith('an') && word.length > 7) {
                bases.add(word.slice(4, -2));
            } else if (word.startsWith('per') && word.endsWith('an') && word.length > 6) {
                bases.add(word.slice(3, -2));
            } else if (word.startsWith('pe') && word.endsWith('an') && word.length > 5) {
                bases.add(word.slice(2, -2));
            } else if (word.startsWith('ke') && word.endsWith('an') && word.length > 5) {
                bases.add(word.slice(2, -2));
            }

            if (word.startsWith('me') && word.endsWith('kan') && word.length > 6) {
                bases.add(word.slice(2, -3));
            }
            if (word.startsWith('ber') && word.length > 5) {
                bases.add(word.slice(3));
            }
            if (word.startsWith('ter') && word.length > 5) {
                bases.add(word.slice(3));
            }

            return Array.from(bases).filter(b => b && b.length >= 3);
        }

        async function translateQueryToIndonesian(query, fromLang) {
            if (!query || typeof query !== 'string') return '';
            const cleanQ = query.trim().toLowerCase();
            if (cleanQ.length < 2) return '';

            // Check persistent translation cache
            const cacheKey = `q2id:${fromLang || 'auto'}:${cleanQ}`;
            if (translationCache[cacheKey]) {
                return translationCache[cacheKey];
            }

            // Provider 1: Google dict-chrome-ex
            try {
                const sl = (fromLang && fromLang !== 'id') ? fromLang : 'auto';
                const url = `https://translate.googleapis.com/translate_a/single?client=dict-chrome-ex&sl=${sl}&tl=id&dt=t&q=${encodeURIComponent(cleanQ)}`;
                const res = await fetch(url);
                const textResp = await res.text();
                if (textResp && textResp.startsWith('[')) {
                    const data = JSON.parse(textResp);
                    if (data && data[0] && Array.isArray(data[0])) {
                        const trans = data[0].map(item => item[0]).join('').trim().toLowerCase();
                        if (trans && trans !== cleanQ) {
                            translationCache[cacheKey] = trans;
                            saveTranslationCache();
                            return trans;
                        }
                    }
                }
            } catch (e) {
                console.warn("translateQueryToIndonesian Provider 1 failed:", e);
            }

            // Provider 2: MyMemory fallback
            try {
                const sl = (fromLang && fromLang !== 'id') ? fromLang : 'en';
                const myMemoryUrl = `https://api.mymemory.translated.net/get?q=${encodeURIComponent(cleanQ)}&langpair=${sl}|id`;
                const res = await fetch(myMemoryUrl);
                const data = await res.json();
                if (data && data.responseData && data.responseData.translatedText) {
                    let mmText = data.responseData.translatedText.trim().toLowerCase();
                    mmText = mmText.replace(/&#39;/g, "'").replace(/&quot;/g, '"').replace(/&amp;/g, '&');
                    if (mmText && !mmText.includes('quota exceeded') && mmText !== cleanQ) {
                        translationCache[cacheKey] = mmText;
                        saveTranslationCache();
                        return mmText;
                    }
                }
            } catch (err) {
                console.warn("translateQueryToIndonesian Provider 2 failed:", err);
            }

            return '';
        }

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

        let keywordFilterMode = 'all'; // 'all', 'uraian', 'ayat'
        let keywordDebounceTimer = null;
        let lastSearchedKeyword = "";
        window.lastActiveSearchTerms = [];

        function onKeywordInput(val) {
            const clearBtn = document.getElementById('btn-clear-keyword-search');
            if (clearBtn) clearBtn.style.display = val.trim() ? 'flex' : 'none';

            clearTimeout(keywordDebounceTimer);
            if (!val.trim()) {
                clearKeywordSearch();
                return;
            }

            keywordDebounceTimer = setTimeout(() => {
                executeKeywordSearch();
            }, 300);
        }

        function clearKeywordSearch() {
            const input = document.getElementById('keyword-search-input');
            const clearBtn = document.getElementById('btn-clear-keyword-search');
            const area = document.getElementById('keyword-content-area');

            if (input) {
                input.value = '';
                input.focus();
            }
            if (clearBtn) clearBtn.style.display = 'none';
            lastSearchedKeyword = "";
            window.lastActiveSearchTerms = [];

            if (area) {
                const emptyMsg = getI18nText("Ketik kata kunci di atas atau pilih salah satu kata populer untuk mencari uraian tematis dan ayat Al-Qur'an.");
                area.innerHTML = `
                    <div class="empty-state">
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="margin: 0 auto 1rem; display: block; color: var(--accent); opacity: 0.8;"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                        ${emptyMsg}
                    </div>
                `;
            }
        }

        function setKeywordFilter(filter) {
            keywordFilterMode = filter;
            ['all', 'uraian', 'ayat'].forEach(f => {
                const btn = document.getElementById(`filter-pill-${f}`);
                if (btn) {
                    if (f === filter) btn.classList.add('active');
                    else btn.classList.remove('active');
                }
            });

            if (lastSearchedKeyword) {
                executeKeywordSearch();
            }
        }

        function searchKeywordTag(tag) {
            switchMainMode('keyword');
            const input = document.getElementById('keyword-search-input');
            const langSelect = document.getElementById('tts-language');
            const lang = langSelect ? langSelect.value : 'id-ID';
            const cfg = LANG_CONFIG[lang] || LANG_CONFIG['id-ID'];
            const targetLang = cfg.code;

            let searchVal = tag;
            if (targetLang !== 'id') {
                const dict = LANG_UI_MAP[targetLang];
                const capTag = tag.charAt(0).toUpperCase() + tag.slice(1);
                if (dict && dict[capTag]) {
                    searchVal = dict[capTag].toLowerCase();
                }
            }

            if (input) input.value = searchVal;
            const clearBtn = document.getElementById('btn-clear-keyword-search');
            if (clearBtn) clearBtn.style.display = 'flex';
            executeKeywordSearch();
        }

        function highlightKeyword(text, keywords) {
            if (!text || !keywords) return text || '';
            const terms = (Array.isArray(keywords) ? keywords : [keywords])
                .map(t => (t || '').trim())
                .filter(t => t.length >= 2);
            if (!terms.length) return text;

            // Match longest terms first to prevent partial clashing
            terms.sort((a, b) => b.length - a.length);

            const safePatterns = terms.map(t => t.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&'));
            const regex = new RegExp(`(${safePatterns.join('|')})`, 'gi');
            return text.replace(regex, '<mark class="search-highlight">$1</mark>');
        }

        function escapeHtml(str) {
            if (!str) return '';
            return String(str)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        async function executeKeywordSearch() {
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

            const langSelect = document.getElementById('tts-language');
            const lang = langSelect ? langSelect.value : 'id-ID';
            const cfg = LANG_CONFIG[lang] || LANG_CONFIG['id-ID'];
            const targetLang = cfg.code;

            // Collect search terms (multilingual support)
            let searchTerms = [qLower];
            let translatedTerm = "";

            // 1. Check direct synonyms in dictionary
            if (KEYWORD_SYNONYMS[qLower]) {
                const syn = KEYWORD_SYNONYMS[qLower];
                if (Array.isArray(syn)) searchTerms.push(...syn);
                else if (typeof syn === 'string') searchTerms.push(syn);
            }

            // 2. If non-Indonesian mode or no direct synonym, auto-translate query to Indonesian
            const hasDirectSynonym = KEYWORD_SYNONYMS[qLower] !== undefined;
            if (targetLang !== 'id' || !hasDirectSynonym) {
                // Show slight loading indicator if translation might require network request
                const isCached = translationCache[`q2id:${targetLang}:${qLower}`] || translationCache[`q2id:auto:${qLower}`];
                if (!hasDirectSynonym && !isCached) {
                    const searchingMsg = getI18nText("Mencari topik & ayat...");
                    area.innerHTML = `
                        <div class="empty-state" style="padding: 2.5rem 1rem;">
                            <div class="spinner" style="width: 36px; height: 36px; border: 3px solid rgba(20, 184, 166, 0.2); border-top-color: var(--accent); border-radius: 50%; animation: spin 0.8s linear infinite; margin: 0 auto 1rem;"></div>
                            <div style="color: #94a3b8; font-size: 0.95rem;">${searchingMsg}</div>
                        </div>
                    `;
                }

                translatedTerm = await translateQueryToIndonesian(qLower, targetLang);
                if (translatedTerm && translatedTerm !== qLower) {
                    searchTerms.push(translatedTerm);
                    
                    // Add Indonesian base roots
                    const roots = getIndonesianBaseWords(translatedTerm);
                    roots.forEach(r => searchTerms.push(r));

                    // Check if translated term or roots have additional synonyms
                    roots.forEach(r => {
                        if (KEYWORD_SYNONYMS[r]) {
                            const synList = KEYWORD_SYNONYMS[r];
                            if (Array.isArray(synList)) searchTerms.push(...synList);
                            else if (typeof synList === 'string') searchTerms.push(synList);
                        }
                    });

                    // Add individual significant words if phrase
                    const words = translatedTerm.split(/\\s+/).filter(w => w.length >= 3 && !['dan', 'yang', 'dari', 'atau', 'pada', 'untuk', 'ke', 'di'].includes(w));
                    if (words.length > 1) {
                        words.forEach(w => {
                            searchTerms.push(w);
                            getIndonesianBaseWords(w).forEach(bw => searchTerms.push(bw));
                        });
                    }
                }
            }

            // Deduplicate and filter search terms
            searchTerms = Array.from(new Set(searchTerms.map(t => (t || '').trim().toLowerCase()).filter(t => t.length >= 2)));
            window.lastActiveSearchTerms = searchTerms;

            // 3. Search in all Uraian topics
            let matchedUraian = [];
            if (keywordFilterMode === 'all' || keywordFilterMode === 'uraian') {
                allThematicUraianList.forEach(item => {
                    const u = item.uraian.toLowerCase();
                    const s = item.sub.toLowerCase();
                    const p = item.pokok.toLowerCase();
                    const t = item.tema.toLowerCase();

                    const match = searchTerms.some(term => 
                        u.includes(term) || s.includes(term) || p.includes(term) || t.includes(term)
                    );

                    if (match) {
                        matchedUraian.push(item);
                    }
                });
            }

            // 4. Search in all Verses (Indonesian translation, Arabic, and Surah Name)
            let matchedVerses = [];
            if (keywordFilterMode === 'all' || keywordFilterMode === 'ayat') {
                allThematicVersesList.forEach(verse => {
                    const indo = verse.indo ? verse.indo.toLowerCase() : '';
                    const name = verse.surah_name ? verse.surah_name.toLowerCase() : '';
                    const arab = verse.arab || '';

                    const match = searchTerms.some(term => 
                        indo.includes(term) || name.includes(term) || arab.includes(term)
                    );

                    if (match) {
                        matchedVerses.push(verse);
                    }
                });
            }

            renderKeywordSearchResults(q, matchedUraian, matchedVerses, searchTerms, translatedTerm);
        }

        function renderKeywordSearchResults(keyword, matchedUraian, matchedVerses, searchTerms, translatedTerm) {
            const area = document.getElementById('keyword-content-area');
            if (!area) return;

            const langSelect = document.getElementById('tts-language');
            const lang = langSelect ? langSelect.value : 'id-ID';
            const cfg = LANG_CONFIG[lang] || LANG_CONFIG['id-ID'];
            const targetLang = cfg.code;

            const activeTerms = (searchTerms && searchTerms.length) ? searchTerms : [keyword.toLowerCase()];

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
                        ${notFoundText} "<strong>${escapeHtml(keyword)}</strong>"${(translatedTerm && translatedTerm.toLowerCase() !== keyword.toLowerCase()) ? ` (<em>${escapeHtml(translatedTerm)}</em>)` : ''}.
                        <div style="font-size: 0.88rem; color: #94a3b8; margin-top: 0.75rem;">
                            ${tipText}
                        </div>
                    </div>
                `;
                return;
            }

            let markup = `
                <div class="keyword-stats-banner">
                    <div class="keyword-stats-info" style="display: flex; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
                        <span>${lblSearchFor} <strong>"${escapeHtml(keyword)}"</strong></span>
                        ${(translatedTerm && translatedTerm.toLowerCase() !== keyword.toLowerCase()) ? `
                        <span style="display: inline-flex; align-items: center; gap: 0.35rem; font-size: 0.82rem; color: #5eead4; background: rgba(20, 184, 166, 0.15); border: 1px solid rgba(20, 184, 166, 0.3); padding: 0.2rem 0.65rem; border-radius: 999px;">
                            🔄 <em>${escapeHtml(translatedTerm)}</em>
                        </span>` : ''}
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
                                <div class="keyword-uraian-title" id="${uId}-title" data-original="${escapeHtml(u.uraian)}">${highlightKeyword(escapeHtml(u.uraian), activeTerms)}</div>
                                <span class="keyword-verse-count-badge">${u.verseCount} ${lblVersesBadge}</span>
                            </div>
                            <div class="keyword-uraian-path">
                                <div>🏷️ <strong>${lblTheme}</strong> <span id="${uId}-tema" data-original="${escapeHtml(u.tema)}">${highlightKeyword(escapeHtml(u.tema), activeTerms)}</span></div>
                                <div>📂 <strong>${lblSubject}</strong> <span id="${uId}-pokok" data-original="${escapeHtml(u.pokok)}">${highlightKeyword(escapeHtml(u.pokok), activeTerms)}</span></div>
                                <div>📑 <strong>${lblSubtopic}</strong> <span id="${uId}-sub" data-original="${escapeHtml(u.sub)}">${highlightKeyword(escapeHtml(u.sub), activeTerms)}</span></div>
                            </div>
                            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                                <button class="btn-jump-thematic" style="padding: 0.6rem 1.1rem; font-size: 0.88rem; flex: 1;" onclick="navigateToThematicTopic('${u.tema.replace(/'/g, "\\\\'")}', '${u.pokok.replace(/'/g, "\\\\'")}', '${u.sub.replace(/'/g, "\\\\'")}', '${u.uraian.replace(/'/g, "\\\\'")}', ${u.sampleVerses[0] ? u.sampleVerses[0].surah_num : 1}, ${u.sampleVerses[0] ? u.sampleVerses[0].ayat_num : 1})">
                                    <span>${lblOpenTopic}</span>
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                                </button>
                                <button class="uraian-action-btn uraian-copy-btn" style="padding: 0.6rem 0.9rem;" onclick="copyUraianLink(this, event, '${encodeURIComponent(u.uraian)}')" title="Salin Deep Link">
                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
                                    <span data-i18n-orig="Salin Link">Salin Link</span>
                                </button>
                            </div>
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
                                ${highlightKeyword(v.arab, activeTerms)} <span class="verse-end-sign">۝${toArabicDigits(v.ayat_num)}</span>
                            </div>

                            <div class="search-translation-box keyword-trans-box translation-text" style="margin-bottom: 1.25rem;" data-original="${escapeHtml(v.indo)}">
                                ${highlightKeyword(escapeHtml(v.indo), activeTerms)}
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
        }'''

    content = content[:start_idx] + new_kw_block + content[end_idx:]
    print("Replaced FITUR 2 keyword search block successfully.")

    # Also update translatePageContent() to preserve highlights on translated cards
    old_tp_uraian = """            // 5e. Terjemahkan kartu hasil pencarian kata kunci (Uraian, Path, dan Badge)
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
            });"""

    new_tp_uraian = """            // 5e. Terjemahkan kartu hasil pencarian kata kunci (Uraian, Path, dan Badge)
            const kwUraianElements = document.querySelectorAll('.keyword-uraian-title, .keyword-uraian-path span[data-original], .kw-topic-badge[data-original]');
            kwUraianElements.forEach(async el => {
                const orig = el.getAttribute('data-original');
                if (!orig) return;
                if (targetLangCode === 'id') {
                    el.innerHTML = (window.lastActiveSearchTerms && window.lastActiveSearchTerms.length)
                        ? highlightKeyword(escapeHtml(orig), window.lastActiveSearchTerms)
                        : escapeHtml(orig);
                } else {
                    const dict = LANG_UI_MAP[targetLangCode];
                    let trans = '';
                    if (dict && dict[orig]) {
                        trans = dict[orig];
                    } else {
                        trans = await translateTextFree(orig, targetLangCode);
                    }
                    el.innerHTML = (window.lastActiveSearchTerms && window.lastActiveSearchTerms.length)
                        ? highlightKeyword(escapeHtml(trans), window.lastActiveSearchTerms)
                        : escapeHtml(trans);
                }
            });"""

    if old_tp_uraian in content:
        content = content.replace(old_tp_uraian, new_tp_uraian, 1)
        print("Updated translatePageContent kwUraianElements successfully.")
    else:
        print("Warning: old_tp_uraian not found, skipping.")

    # Also update verse card translation to highlight in keyword-trans-box
    old_card_id_block = """            if (lang === 'id-ID') {
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
            }"""

    new_card_id_block = """            if (lang === 'id-ID') {
                cards.forEach(card => {
                    const origIndo = card.getAttribute('data-indo') ? decodeURIComponent(card.getAttribute('data-indo')) : '';
                    const textEl = card.querySelector('.translation-text');
                    const text = origIndo || (textEl ? textEl.getAttribute('data-original') || '' : '');
                    if (textEl && text) {
                        textEl.className = 'translation-text' + (textEl.classList.contains('keyword-trans-box') ? ' keyword-trans-box' : '');
                        if (textEl.classList.contains('keyword-trans-box') && window.lastActiveSearchTerms && window.lastActiveSearchTerms.length) {
                            textEl.innerHTML = highlightKeyword(escapeHtml(text), window.lastActiveSearchTerms);
                        } else {
                            textEl.textContent = text;
                        }
                    }
                    const playBtn = card.querySelector('.play-btn');
                    if (playBtn && text) playBtn.setAttribute('data-text', encodeURIComponent(text));
                });
                return;
            }"""

    if old_card_id_block in content:
        content = content.replace(old_card_id_block, new_card_id_block, 1)
        print("Updated translatePageContent card ID block successfully.")
    else:
        print("Warning: old_card_id_block not found, skipping.")

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully wrote updated content to index.html!")

if __name__ == '__main__':
    main()
