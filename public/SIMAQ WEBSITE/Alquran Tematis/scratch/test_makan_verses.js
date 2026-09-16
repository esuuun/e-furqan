const fs = require('fs');
const d = JSON.parse(fs.readFileSync('data.json', 'utf8'));

let verseThematicIndex = {};
for (const [tema, pbs] of Object.entries(d)) {
    for (const [pb, spbs] of Object.entries(pbs)) {
        for (const [spb, urs] of Object.entries(spbs)) {
            for (const [ur, urData] of Object.entries(urs)) {
                for (const v of (urData.verses || [])) {
                    const key = `${v.surah_num}:${v.ayat_num}`;
                    if (!verseThematicIndex[key]) {
                        verseThematicIndex[key] = v;
                    }
                }
            }
        }
    }
}
const allVerses = Object.values(verseThematicIndex);

function testWordMatch(text, term) {
    if (!text || !term) return false;
    term = term.trim().toLowerCase();
    
    // Check phrase if term contains space
    if (term.includes(' ')) {
        const regex = new RegExp('\\b' + term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\b', 'i');
        return regex.test(text);
    }

    const words = text.toLowerCase().split(/[^\w\u0600-\u06FF]+/);
    const prefixes = ['', 'me', 'mem', 'men', 'meng', 'meny', 'ber', 'di', 'ter', 'pe', 'pem', 'pen', 'peng', 'peny', 'se', 'ke'];
    const suffixes = ['', 'an', 'kan', 'i', 'lah', 'kah', 'pun', 'nya', 'ku', 'mu', 'annya', 'kanlah', 'kannya'];

    for (const w of words) {
        if (!w) continue;
        if (w === term) return true;
        if (term.length >= 3) {
            for (const p of prefixes) {
                for (const s of suffixes) {
                    if (!p && !s) continue;
                    if (p + term + s === w) return true;
                }
            }
        }
    }
    return false;
}

const vMatches = allVerses.filter(v => testWordMatch(v.indo, 'makan'));
console.log(`Verses matching "makan": ${vMatches.length}`);
vMatches.slice(0, 10).forEach(v => {
    console.log(` - QS ${v.surah_name} [${v.surah_num}:${v.ayat_num}]: ${v.indo.slice(0, 70)}...`);
});
