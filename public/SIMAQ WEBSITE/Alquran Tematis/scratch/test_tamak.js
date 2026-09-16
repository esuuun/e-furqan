const testText = '5.13.5.2. Ketamakan Kerajaan Saba Untuk Melakukan Monopoli';

function highlightKeyword(text, searchTerms) {
    if (!text || !searchTerms || !searchTerms.length) return text || '';
    const terms = (Array.isArray(searchTerms) ? searchTerms : [searchTerms])
        .map(t => (t || '').trim().toLowerCase())
        .filter(t => t.length >= 2);
    if (!terms.length) return text;

    const prefixes = ['', 'me', 'mem', 'men', 'meng', 'meny', 'ber', 'di', 'ter', 'pe', 'pem', 'pen', 'peng', 'peny', 'se', 'ke'];
    const suffixes = ['', 'an', 'kan', 'i', 'lah', 'kah', 'pun', 'nya', 'ku', 'mu', 'annya', 'kanlah', 'kannya'];

    const matchPatterns = [];

    for (const term of terms) {
        if (/[\u0600-\u06FF]/.test(term)) {
            matchPatterns.push(term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
            continue;
        }

        if (term.includes(' ')) {
            const phraseWords = term.split(/\s+/).map(w => w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
            matchPatterns.push('\\b' + phraseWords.join('\\s+') + '\\b');
        } else {
            matchPatterns.push('\\b' + term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\b');
            if (term.length >= 3) {
                for (const p of prefixes) {
                    for (const s of suffixes) {
                        if (!p && !s) continue;
                        const inflected = p + term + s;
                        matchPatterns.push('\\b' + inflected.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\b');
                    }
                }
            }
        }
    }

    if (!matchPatterns.length) return text;

    const uniquePatterns = Array.from(new Set(matchPatterns)).sort((a, b) => b.length - a.length);
    const regex = new RegExp('(' + uniquePatterns.join('|') + ')', 'gi');
    return text.replace(regex, '<mark class="search-highlight">$1</mark>');
}

console.log('Searching "tamak":', highlightKeyword(testText, ['tamak']));
console.log('Searching "makan":', highlightKeyword(testText, ['makan']));
