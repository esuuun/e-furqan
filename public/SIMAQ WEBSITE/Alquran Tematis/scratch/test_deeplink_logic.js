// scratch/test_deeplink_logic.js
const fs = require('fs');

const data = JSON.parse(fs.readFileSync('data.json', 'utf-8'));

// Build allThematicUraianList
let allThematicUraianList = [];
for (const [tema, pbs] of Object.entries(data)) {
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
            }
        }
    }
}

console.log('Total indexed Uraian topics:', allThematicUraianList.length);

// Replicate findUraianPath
function findUraianPath(uraianQuery) {
    if (!uraianQuery || !allThematicUraianList || !allThematicUraianList.length) return null;
    const cleanQ = decodeURIComponent(uraianQuery).trim().toLowerCase();
    if (!cleanQ) return null;

    // 1. Exact match
    let match = allThematicUraianList.find(item => item.uraian.toLowerCase() === cleanQ);
    if (match) return match;

    // 2. Starts with (e.g. "1.1.1.1" or "1.1.1.1." or code prefix)
    match = allThematicUraianList.find(item => item.uraian.toLowerCase().startsWith(cleanQ));
    if (match) return match;

    // 3. Substring match
    match = allThematicUraianList.find(item => item.uraian.toLowerCase().includes(cleanQ));
    if (match) return match;

    return null;
}

// Test cases
const tests = [
    { name: "Exact full title", input: "1.1.1.1.Tidak Ada Tuhan Selain Allah" },
    { name: "Code prefix with dot", input: "1.1.1.1." },
    { name: "Code prefix without dot", input: "1.1.1.1" },
    { name: "Title text only lowercase", input: "tidak ada tuhan selain allah" },
    { name: "Encoded URI component", input: encodeURIComponent("1.1.1.1.Tidak Ada Tuhan Selain Allah") },
    { name: "Another topic code", input: "4.5.10.2" },
    { name: "Subtopic query", input: "Hukum Waris" }
];

let allPassed = true;
tests.forEach(t => {
    const res = findUraianPath(t.input);
    if (res) {
        console.log(`[PASS] ${t.name}: "${t.input}" -> Found: "${res.uraian}"`);
        console.log(`       Path: [${res.tema}] > [${res.pokok}] > [${res.sub}] (${res.verseCount} verses)`);
    } else {
        console.error(`[FAIL] ${t.name}: "${t.input}" not found!`);
        allPassed = false;
    }
});

if (allPassed) {
    console.log("\nALL DEEP LINK RESOLUTION TESTS PASSED!");
} else {
    process.exit(1);
}
