// scratch/test_sub_deeplink_logic.js
const fs = require('fs');
const data = JSON.parse(fs.readFileSync('data.json', 'utf-8'));

let allThematicSubList = [];
let allThematicUraianList = [];

for (const [tema, pbs] of Object.entries(data)) {
    for (const [pb, spbs] of Object.entries(pbs)) {
        for (const [spb, urs] of Object.entries(spbs)) {
            let subVerseCount = 0;
            for (const [ur, urData] of Object.entries(urs)) {
                const vList = (urData && urData.verses) ? urData.verses : [];
                subVerseCount += vList.length;
                allThematicUraianList.push({
                    tema: tema,
                    pokok: pb,
                    sub: spb,
                    uraian: ur,
                    verseCount: vList.length,
                    sampleVerses: vList.slice(0, 3)
                });
            }
            allThematicSubList.push({
                tema: tema,
                pokok: pb,
                sub: spb,
                uraianCount: Object.keys(urs).length,
                verseCount: subVerseCount
            });
        }
    }
}

console.log(`Indexed ${allThematicSubList.length} sub-topics and ${allThematicUraianList.length} uraian topics.`);

function findSubPath(subQuery) {
    if (!subQuery || !allThematicSubList || !allThematicSubList.length) return null;
    const cleanQ = decodeURIComponent(subQuery).trim().toLowerCase();
    if (!cleanQ) return null;

    let match = allThematicSubList.find(item => item.sub.toLowerCase() === cleanQ);
    if (match) return match;

    match = allThematicSubList.find(item => item.sub.toLowerCase().startsWith(cleanQ));
    if (match) return match;

    match = allThematicSubList.find(item => item.sub.toLowerCase().includes(cleanQ));
    if (match) return match;

    return null;
}

function getSubDeepLink(subTitle, tema, pokok) {
    if (!tema || !pokok) {
        const found = findSubPath(subTitle);
        if (found) {
            tema = found.tema;
            pokok = found.pokok;
            subTitle = found.sub;
        }
    }
    const hash = `tema=${encodeURIComponent(tema || '')}&pokok=${encodeURIComponent(pokok || '')}&sub=${encodeURIComponent(subTitle)}`;
    return `http://localhost:8080/index.html#${hash}`;
}

const testCases = [
    { name: "Code prefix 1.1.1", input: "1.1.1" },
    { name: "Code prefix with dot 1.1.1.", input: "1.1.1." },
    { name: "Full title 1.1.1.Persaksian Tauhid", input: "1.1.1.Persaksian Tauhid" },
    { name: "Code prefix 9.5.2", input: "9.5.2" },
    { name: "Keyword Waris", input: "Waris" },
    { name: "Code prefix 4.5.10", input: "4.5.10" },
    { name: "Keyword Hudaibiyah", input: "Hudaibiyah" },
    { name: "URI encoded", input: encodeURIComponent("9.5.2. Waris") }
];

let allPassed = true;
testCases.forEach(tc => {
    const res = findSubPath(tc.input);
    if (res) {
        const link = getSubDeepLink(res.sub, res.tema, res.pokok);
        console.log(`[PASS] ${tc.name} ("${tc.input}") -> Found: "${res.sub}"`);
        console.log(`       Tema: [${res.tema}] | Pokok: [${res.pokok}]`);
        console.log(`       Generated link: ${link}`);
    } else {
        console.error(`[FAIL] ${tc.name} ("${tc.input}") NOT FOUND!`);
        allPassed = false;
    }
});

if (allPassed) {
    console.log("\nALL SUB-TOPIC DEEP LINK LOGIC TESTS PASSED SUCCESSFULLY!");
} else {
    process.exit(1);
}
