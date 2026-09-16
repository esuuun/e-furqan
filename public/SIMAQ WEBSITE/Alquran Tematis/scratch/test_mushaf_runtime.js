// scratch/test_mushaf_runtime.js
const fs = require('fs');
global.window = global;

// Load kamus lookup
const kamusCode = fs.readFileSync('Mushaf Per Kata/data_js/kamus_lookup.js', 'utf-8');
eval(kamusCode);

// Load surah 3
const surah3Code = fs.readFileSync('Mushaf Per Kata/data_js/surah_3.js', 'utf-8');
eval(surah3Code);

const words3_18 = window.__MUSHAF_SURAH_DATA[3]["18"];
console.log(`Surah 3 Ayat 18 total words: ${words3_18.length}`);

// Test word 1
const w1 = words3_18[0];
console.log('Word 1:', JSON.stringify(w1, null, 2));

// Test Kamus link logic
function cleanArabicWord(str) {
    if (!str) return '';
    str = String(str);
    str = str.replace(/\d+/g, '');
    str = str.replace(/\u0671/g, '\u0627');
    str = str.replace(/[\u064B-\u065F\u06E1\u06D6-\u06ED]/g, '');
    return str.replace(/\s+/g, ' ').trim();
}

function getKamusDeepLink(row, lang) {
    const lookup = window.__KAMUS_LOOKUP || {};
    const kataAkar = cleanArabicWord(row['Kata/Akar']);
    const kataAkarNoSpace = kataAkar.replace(/\s+/g, '');
    const lafdz = cleanArabicWord(row['Lafdz']);
    const s = row['SURAT_ID'] || row['SURAT'] || 3;
    const a = row['AYAT_ID'] || row['AYAT'] || 18;

    const musytaqMap = lookup.musytaq_roots || {};
    const mEntry = musytaqMap[kataAkar] || musytaqMap[kataAkarNoSpace];
    if (mEntry) {
        const akarId = mEntry.id || mEntry;
        return `Mushaf Per Kata/Kamus/index.html?dict=musytaq&akar=${akarId}&lang=${lang}`;
    }

    const jamidMap = lookup.jamid_words || {};
    const jEntry = jamidMap[kataAkar] || jamidMap[lafdz];
    if (jEntry) {
        const no = jEntry.no || jEntry;
        return `Mushaf Per Kata/Kamus/index.html?dict=jamid&no=${encodeURIComponent(no)}&lang=${lang}&surat=${s}&ayat=${a}`;
    }

    const harfAmilMap = lookup.harf_amil_words || {};
    const haEntry = harfAmilMap[kataAkar] || harfAmilMap[lafdz];
    if (haEntry) {
        const no = haEntry.no || haEntry;
        return `Mushaf Per Kata/Kamus/index.html?dict=harf_amil&no=${encodeURIComponent(no)}&lang=${lang}&surat=${s}&ayat=${a}`;
    }

    const harfMap = lookup.harf_words || {};
    const hEntry = harfMap[kataAkar] || harfMap[lafdz];
    if (hEntry) {
        const no = hEntry.no || hEntry;
        return `Mushaf Per Kata/Kamus/index.html?dict=harf&no=${encodeURIComponent(no)}&lang=${lang}&surat=${s}&ayat=${a}`;
    }

    return `Mushaf Per Kata/Kamus/index.html?lang=${lang}`;
}

words3_18.forEach((w, idx) => {
    const url = getKamusDeepLink(w, 'id');
    console.log(`Word ${idx + 1} [${w.Lafdz}] (${w['Kata/Akar']}) -> ${url}`);
});
