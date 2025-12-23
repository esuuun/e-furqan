const fs = require('fs');
const path = 'd:/TAHFIDZ ANTIGRAVITY/quran-data.js';

// Mock splitArabicText function to test logic
function splitArabicText(text) {
    const cleanText = text.replace(/[\u200B-\u200D\uFEFF]/g, '').trim();
    return cleanText.split(/\s+/).filter(w => w.length > 0);
}

try {
    console.log('--- Checking quran-data.js ---');
    let content = fs.readFileSync(path, 'utf8');

    // Basic Syntax Check by mock eval
    // We wrap it in a function to avoid polluting global scope if we were in a browser, 
    // but here we just want to see if it parses.
    // We need to handle the 'const quranData =' part.
    const evalContent = content.replace('const quranData =', 'global.quranData =');

    eval(evalContent);

    if (Array.isArray(global.quranData)) {
        console.log(`✅ quranData loaded successfully. Total Surahs: ${global.quranData.length}`);
        if (global.quranData.length === 114) {
            console.log('✅ Full 114 Surahs found.');
        } else {
            console.warn(`⚠️ Warning: Expected 114 Surahs, found ${global.quranData.length}`);
        }

        // Check first and last
        console.log(`First Surah: ${global.quranData[0].name}`);
        console.log(`Last Surah: ${global.quranData[global.quranData.length - 1].name}`);

    } else {
        console.error('❌ quranData is not an array.');
    }

    console.log('\n--- Testing splitArabicText ---');
    const testString = "قُلْ أَعُوذُ بِرَبِّ النَّاسِ";
    const parts = splitArabicText(testString);
    console.log(`Original: ${testString}`);
    console.log(`Split (${parts.length} words):`, parts);

    if (parts.length === 4) {
        console.log('✅ Split logic looks correct for Al-Falaq/An-Naas sample.');
    } else {
        console.log('❌ Split logic might be off.');
    }

} catch (e) {
    console.error('❌ Error verifying data:', e.message);
}
