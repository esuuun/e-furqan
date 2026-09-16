function highlightKeywordsInText(text, searchTerms) {
    if (!text || !searchTerms || !searchTerms.length) return text || '';
    
    // Normalize terms
    const terms = (Array.isArray(searchTerms) ? searchTerms : [searchTerms])
        .map(t => (t || '').trim().toLowerCase())
        .filter(t => t.length >= 2);
    if (!terms.length) return text;

    // Prefixes and suffixes for Indonesian morphology
    const prefixes = ['', 'me', 'mem', 'men', 'meng', 'meny', 'ber', 'di', 'ter', 'pe', 'pem', 'pen', 'peng', 'peny', 'se', 'ke'];
    const suffixes = ['', 'an', 'kan', 'i', 'lah', 'kah', 'pun', 'nya', 'ku', 'mu', 'annya', 'kanlah', 'kannya'];

    // Generate valid inflections for each single-word term
    const matchPatterns = [];

    for (const term of terms) {
        if (term.includes(' ')) {
            // Multi-word phrase: match with word boundaries
            const phraseWords = term.split(/\s+/).map(w => w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
            matchPatterns.push('\\b' + phraseWords.join('\\s+') + '\\b');
        } else {
            // Single word term: exact word and valid inflections
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

    // Sort by length descending
    const uniquePatterns = Array.from(new Set(matchPatterns)).sort((a, b) => b.length - a.length);
    const regex = new RegExp('(' + uniquePatterns.join('|') + ')', 'gi');
    return text.replace(regex, '<mark class="search-highlight">$1</mark>');
}

const sample1 = '5.13.5.2. Ketamakan Kerajaan Saba Untuk Melakukan Monopoli';
const sample2 = '13.1.1.1. Seluruh Makanan Yang Baik-baik Pada Dasarnya Halal';
const sample3 = '7.13.2.2. Etika Makan Bersama Ketika Bertamu';
const sample4 = '9.2.1.2. Cara Dan Hukum Memakan Harta Anak Yatim';

console.log('Sample 1 (Ketamakan):', highlightKeywordsInText(sample1, ['makan']));
console.log('Sample 2 (Makanan):', highlightKeywordsInText(sample2, ['makan']));
console.log('Sample 3 (Makan):', highlightKeywordsInText(sample3, ['makan']));
console.log('Sample 4 (Memakan):', highlightKeywordsInText(sample4, ['makan']));
