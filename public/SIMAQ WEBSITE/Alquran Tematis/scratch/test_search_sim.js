const fs = require('fs');

// Load data.json
const quranData = JSON.parse(fs.readFileSync('data.json', 'utf8'));

// Build index exactly like buildVerseIndex
let verseThematicIndex = {};
let allThematicUraianList = [];

for (const [tema, pbs] of Object.entries(quranData)) {
    for (const [pb, spbs] of Object.entries(pbs)) {
        for (const [spb, urs] of Object.entries(spbs)) {
            for (const [ur, urData] of Object.entries(urs)) {
                const vList = (urData && urData.verses) ? urData.verses : [];
                allThematicUraianList.push({
                    tema: tema,
                    pokok: pb,
                    sub: spb,
                    uraian: ur,
                    verseCount: vList.length,
                    sampleVerses: vList.slice(0, 3)
                });
                vList.forEach(v => {
                    const key = `${v.surah_num}:${v.ayat_num}`;
                    if (!verseThematicIndex[key]) {
                        verseThematicIndex[key] = {
                            surah_name: v.surah_name,
                            surah_num: v.surah_num,
                            ayat_num: v.ayat_num,
                            arab: v.arab,
                            indo: v.indo
                        };
                    }
                });
            }
        }
    }
}
const allThematicVersesList = Object.values(verseThematicIndex);

console.log(`Indexed ${allThematicUraianList.length} uraian and ${allThematicVersesList.length} verses.`);

// Test searching for 'drunk'
const searchTerms = ['drunk', 'mabuk', 'khamr', 'khamar', 'memabukkan'];

const matchedUraian = allThematicUraianList.filter(item => {
    const u = item.uraian.toLowerCase();
    const s = item.sub.toLowerCase();
    const p = item.pokok.toLowerCase();
    const t = item.tema.toLowerCase();
    return searchTerms.some(term => u.includes(term) || s.includes(term) || p.includes(term) || t.includes(term));
});

const matchedVerses = allThematicVersesList.filter(verse => {
    const indo = verse.indo ? verse.indo.toLowerCase() : '';
    const name = verse.surah_name ? verse.surah_name.toLowerCase() : '';
    const arab = verse.arab || '';
    return searchTerms.some(term => indo.includes(term) || name.includes(term) || arab.includes(term));
});

console.log(`\nSearch results for "drunk":`);
console.log(`Matched Uraian: ${matchedUraian.length}`);
matchedUraian.forEach(u => console.log(` - [${u.tema}] -> ${u.uraian}`));

console.log(`\nMatched Verses: ${matchedVerses.length}`);
matchedVerses.forEach(v => console.log(` - QS ${v.surah_name} [${v.surah_num}:${v.ayat_num}]`));
