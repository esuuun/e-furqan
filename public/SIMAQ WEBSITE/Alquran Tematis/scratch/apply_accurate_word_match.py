import shutil

def main():
    html_file = 'index.html'
    backup_file = 'scratch/index.html.before_word_boundary_fix.bak'
    shutil.copy2(html_file, backup_file)
    print("Backup created at", backup_file)

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Target block: from function highlightKeyword to end of executeKeywordSearch
    old_block_start = "        function highlightKeyword(text, keywords) {"
    old_block_end = "            renderKeywordSearchResults(q, matchedUraian, matchedVerses, searchTerms, translatedTerm);\n        }"

    start_idx = content.find(old_block_start)
    if start_idx == -1:
        print("ERROR: old_block_start not found!")
        return

    end_idx = content.find(old_block_end, start_idx)
    if end_idx == -1:
        print("ERROR: old_block_end not found!")
        return
    end_idx += len(old_block_end)

    new_block = """        function checkTextMatchesTerms(text, searchTerms) {
            if (!text || !searchTerms || !searchTerms.length) return false;

            const prefixes = ['', 'me', 'mem', 'men', 'meng', 'meny', 'ber', 'di', 'ter', 'pe', 'pem', 'pen', 'peng', 'peny', 'se', 'ke'];
            const suffixes = ['', 'an', 'kan', 'i', 'lah', 'kah', 'pun', 'nya', 'ku', 'mu', 'annya', 'kanlah', 'kannya'];

            const lowerText = text.toLowerCase();
            const rawTokens = lowerText.split(/[^\\w\\u0600-\\u06FF\\-]+/);
            const tokens = [];
            rawTokens.forEach(t => {
                if (!t) return;
                tokens.push(t);
                if (t.includes('-')) {
                    t.split('-').forEach(part => { if (part) tokens.push(part); });
                }
            });

            for (const term of searchTerms) {
                if (!term) continue;
                const cleanTerm = term.trim().toLowerCase();
                if (!cleanTerm) continue;

                // If Arabic text, use direct inclusion
                if (/[\\u0600-\\u06FF]/.test(cleanTerm)) {
                    if (lowerText.includes(cleanTerm)) return true;
                    continue;
                }

                // Multi-word phrase: match with word boundaries
                if (cleanTerm.includes(' ')) {
                    const phrasePattern = cleanTerm.split(/\\s+/).map(w => w.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&')).join('\\\\s+');
                    const phraseRegex = new RegExp('\\\\b' + phrasePattern + '\\\\b', 'i');
                    if (phraseRegex.test(lowerText)) return true;
                    continue;
                }

                // Single word: test against word tokens with valid prefixes/suffixes
                for (const w of tokens) {
                    if (w === cleanTerm) return true;
                    if (cleanTerm.length >= 3) {
                        for (const p of prefixes) {
                            for (const s of suffixes) {
                                if (!p && !s) continue;
                                if (p + cleanTerm + s === w) return true;
                            }
                        }
                    }
                }
            }

            return false;
        }

        function highlightKeyword(text, keywords) {
            if (!text || !keywords) return text || '';
            const terms = (Array.isArray(keywords) ? keywords : [keywords])
                .map(t => (t || '').trim().toLowerCase())
                .filter(t => t.length >= 2);
            if (!terms.length) return text;

            const prefixes = ['', 'me', 'mem', 'men', 'meng', 'meny', 'ber', 'di', 'ter', 'pe', 'pem', 'pen', 'peng', 'peny', 'se', 'ke'];
            const suffixes = ['', 'an', 'kan', 'i', 'lah', 'kah', 'pun', 'nya', 'ku', 'mu', 'annya', 'kanlah', 'kannya'];

            const matchPatterns = [];

            for (const term of terms) {
                if (/[\\u0600-\\u06FF]/.test(term)) {
                    // Match Arabic word boundaries with unicode
                    matchPatterns.push(term.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&'));
                    continue;
                }

                if (term.includes(' ')) {
                    const phraseWords = term.split(/\\s+/).map(w => w.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&'));
                    matchPatterns.push('\\\\b' + phraseWords.join('\\\\s+') + '\\\\b');
                } else {
                    // Match exact word and valid inflected words
                    matchPatterns.push('\\\\b' + term.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&') + '\\\\b');
                    if (term.length >= 3) {
                        for (const p of prefixes) {
                            for (const s of suffixes) {
                                if (!p && !s) continue;
                                const inflected = p + term + s;
                                matchPatterns.push('\\\\b' + inflected.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&') + '\\\\b');
                            }
                        }
                    }
                }
            }

            if (!matchPatterns.length) return text;

            // Sort by length descending to match longest full word first
            const uniquePatterns = Array.from(new Set(matchPatterns)).sort((a, b) => b.length - a.length);
            const regex = new RegExp(`(${uniquePatterns.join('|')})`, 'gi');
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

            // 3. Search in all Uraian topics (strict word & affix matching on uraian, sub, pokok)
            let matchedUraian = [];
            if (keywordFilterMode === 'all' || keywordFilterMode === 'uraian') {
                allThematicUraianList.forEach(item => {
                    const uMatch = checkTextMatchesTerms(item.uraian, searchTerms);
                    const sMatch = checkTextMatchesTerms(item.sub, searchTerms);
                    const pMatch = checkTextMatchesTerms(item.pokok, searchTerms);

                    if (uMatch || sMatch || pMatch) {
                        matchedUraian.push(item);
                    }
                });
            }

            // 4. Search in all Verses (strict word & affix matching on Indonesian translation and Arabic)
            let matchedVerses = [];
            if (keywordFilterMode === 'all' || keywordFilterMode === 'ayat') {
                allThematicVersesList.forEach(verse => {
                    const indoMatch = checkTextMatchesTerms(verse.indo, searchTerms);
                    const nameMatch = checkTextMatchesTerms(verse.surah_name, searchTerms);
                    const arabMatch = verse.arab && searchTerms.some(t => /[\\u0600-\\u06FF]/.test(t) && verse.arab.includes(t));

                    if (indoMatch || nameMatch || arabMatch) {
                        matchedVerses.push(verse);
                    }
                });
            }

            renderKeywordSearchResults(q, matchedUraian, matchedVerses, searchTerms, translatedTerm);
        }"""

    content = content[:start_idx] + new_block + content[end_idx:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated index.html with accurate word boundary matching and highlighting!")

if __name__ == '__main__':
    main()
