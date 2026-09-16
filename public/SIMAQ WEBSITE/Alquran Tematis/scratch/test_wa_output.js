const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf-8');

// Extract getWhatsAppTemplates and getDomOrCachedTranslation
const tplMatch = html.match(/function getWhatsAppTemplates[\s\S]*?return templates\[langCode\] \|\| templates\['en'\];\s*\}/);
const domMatch = html.match(/function getDomOrCachedTranslation[\s\S]*?return null;\s*\}/);

console.log('Found tpl:', !!tplMatch);
console.log('Found dom:', !!domMatch);

eval(tplMatch[0]);

const tplEn = getWhatsAppTemplates('en');
console.log('\n--- ENGLISH TEMPLATE ---');
console.log('appName:', tplEn.appName);
console.log('subHeader:', tplEn.subHeader);
console.log('tema:', tplEn.tema);
console.log('pokok:', tplEn.pokok);
console.log('subMeta:', tplEn.subMeta(4, 21));
console.log('learnMore:', tplEn.learnMore);

const tplId = getWhatsAppTemplates('id');
console.log('\n--- INDONESIAN TEMPLATE ---');
console.log('appName:', tplId.appName);
console.log('subHeader:', tplId.subHeader);
console.log('tema:', tplId.tema);
console.log('pokok:', tplId.pokok);
console.log('subMeta:', tplId.subMeta(4, 21));
console.log('learnMore:', tplId.learnMore);

// Simulate what message will look like in English:
const subTitle = "1.1.1. Testimony of Monotheism";
const tema = "1. Names and Attributes of Allah";
const pokok = "1.1. Traits 1-6";
const uCount = 4;
const vCount = 21;
const link = "https://...#tema=...&pokok=...&sub=...&lang=en-US";

const messageEn = `*${tplEn.appName}*\n\n` +
    `📑 *${tplEn.subHeader}:* ${subTitle}\n` +
    (tema ? `🏷️ *${tplEn.tema}:* ${tema}\n` : '') +
    (pokok ? `📂 *${tplEn.pokok}:* ${pokok}\n` : '') +
    (uCount > 0 ? `📊 *${tplEn.subMeta(uCount, vCount)}*\n\n` : '\n') +
    `${tplEn.learnMore}\n${link}`;

console.log('\n--- SIMULATED ENGLISH WA SHARE OUTPUT ---');
console.log(messageEn);
