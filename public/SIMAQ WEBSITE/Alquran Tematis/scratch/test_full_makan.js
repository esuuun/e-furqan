const fs = require('fs');
const d = JSON.parse(fs.readFileSync('data.json', 'utf8'));

const allUraian = [];
for (const [tema, pbs] of Object.entries(d)) {
    for (const [pb, spbs] of Object.entries(pbs)) {
        for (const [spb, urs] of Object.entries(spbs)) {
            for (const [ur, urData] of Object.entries(urs)) {
                allUraian.push({
                    tema: tema,
                    pokok: pb,
                    sub: spb,
                    uraian: ur
                });
            }
        }
    }
}

function checkTextMatchesTerms(text, searchTerms) {
    if (!text || !searchTerms || !searchTerms.length) return false;

    const prefixes = ['', 'me', 'mem', 'men', 'meng', 'meny', 'ber', 'di', 'ter', 'pe', 'pem', 'pen', 'peng', 'peny', 'se', 'ke'];
    const suffixes = ['', 'an', 'kan', 'i', 'lah', 'kah', 'pun', 'nya', 'ku', 'mu', 'annya', 'kanlah', 'kannya'];

    const lowerText = text.toLowerCase();
    const rawTokens = lowerText.split(/[^\w\u0600-\u06FF\-]+/);
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

        if (/[\u0600-\u06FF]/.test(cleanTerm)) {
            if (lowerText.includes(cleanTerm)) return true;
            continue;
        }

        if (cleanTerm.includes(' ')) {
            const phrasePattern = cleanTerm.split(/\s+/).map(w => w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('\\s+');
            const phraseRegex = new RegExp('\\b' + phrasePattern + '\\b', 'i');
            if (phraseRegex.test(lowerText)) return true;
            continue;
        }

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

const terms = ['makan'];
const matched = allUraian.filter(item => {
    return checkTextMatchesTerms(item.uraian, terms) ||
           checkTextMatchesTerms(item.sub, terms) ||
           checkTextMatchesTerms(item.pokok, terms);
});

console.log(`Matched Uraian count: ${matched.length}`);
matched.forEach(m => console.log(' - ' + m.uraian));
