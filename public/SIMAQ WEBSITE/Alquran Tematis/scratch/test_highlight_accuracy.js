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

const inputs = [
    '5.13.5.2. Ketamakan Kerajaan Saba Untuk Melakukan Monopoli',
    '7.13.2.2. Etika Makan Bersama Ketika Bertamu',
    '9.2.1.2. Cara Dan Hukum Memakan Harta Anak Yatim',
    '13.1.1.1. Seluruh Makanan Yang Baik-baik Pada Dasarnya Halal',
    '13.1.3.2. ...Yang Dimakan Binatang Buas',
    'Tetapi janganlah kamu mendekati api'
];

inputs.forEach(inp => {
    console.log(highlightKeyword(inp, ['makan']));
});

console.log('\nTesting "api":');
console.log(highlightKeyword('Tetapi janganlah kamu mendekati api yang berapi-api', ['api']));

console.log('\nTesting "hak":');
console.log(highlightKeyword('Bahkan setiap pihak berhak atas akhlak yang baik', ['hak']));
