const fs = require('fs');
const d = JSON.parse(fs.readFileSync('data.json', 'utf8'));

// Build list of all Uraian
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

// Function to test if text matches term with word boundaries & valid affixes
function testWordMatch(text, term) {
    if (!text || !term) return false;
    term = term.trim().toLowerCase();
    
    // Split text into words
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

console.log('Testing "makan" on all Uraian:');
const matches = allUraian.filter(item => {
    // Check uraian and sub first, or pokok
    return testWordMatch(item.uraian, 'makan') || testWordMatch(item.sub, 'makan');
});

console.log(`Found ${matches.length} topics matching "makan" (in uraian/sub):`);
matches.forEach(m => console.log(` - [${m.tema}] ${m.uraian}`));
