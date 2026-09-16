const fs = require('fs');

const elMap = {};
function makeEl(id) {
  return {
    id,
    textContent: '',
    innerHTML: '',
    value: '',
    style: {},
    classList: { add: ()=>{}, remove: ()=>{} },
    setAttribute: ()=>{},
    getAttribute: ()=> '',
    addEventListener: ()=>{},
    appendChild: ()=>{},
    querySelector: ()=> makeEl('child'),
    querySelectorAll: ()=> []
  };
}

const doc = {
  getElementById: (id) => {
    if (!elMap[id]) elMap[id] = makeEl(id);
    return elMap[id];
  },
  createElement: (tag) => makeEl(tag),
  documentElement: { setAttribute: ()=>{}, lang: 'id' },
  addEventListener: ()=>{}
};
global.document = doc;
global.localStorage = { getItem: ()=> 'es', setItem: ()=>{} };
global.window = { speechSynthesis: { speak: ()=>{}, cancel: ()=>{}, getVoices: ()=>[] } };
global.navigator = { clipboard: { writeText: ()=>Promise.resolve() } };

let dataCode = fs.readFileSync('dhamir_data.js', 'utf8');
dataCode = dataCode.replace('const DHAMIR_DATA =', 'global.DHAMIR_DATA =');
dataCode = dataCode.replace('const SURAH_DICT =', 'global.SURAH_DICT =');
dataCode = dataCode.replace('const GRAMMAR_INFO =', 'global.GRAMMAR_INFO =');
eval(dataCode);

let appCode = fs.readFileSync('app.js', 'utf8');
appCode = appCode.replace('function selectBentuk(', 'global.selectBentuk = function selectBentuk(');
appCode = appCode.replace('function selectNoKata(', 'global.selectNoKata = function selectNoKata(');
appCode = appCode.replace('function applyLanguage(', 'global.applyLanguage = function applyLanguage(');
appCode = appCode.replace('function updateSpotlightCard(', 'global.updateSpotlightCard = function updateSpotlightCard(');
appCode = appCode.replace('function renderAyatReferences(', 'global.renderAyatReferences = function renderAyatReferences(');
appCode = appCode.replace('function buildAiPrompt(', 'global.buildAiPrompt = function buildAiPrompt(');

eval(appCode);

console.log('=== 1. TESTING LANGUAGE SWITCH TO SPANISH (es) ===');
global.applyLanguage('es');
console.log('  Page Title          :', elMap['docTitle']?.textContent);
console.log('  Brand Subtitle      :', elMap['brandSubtitle']?.textContent);
console.log('  Translation Source  :', elMap['translationSourceText']?.textContent || elMap['translationSourceText']?.innerHTML);
console.log('  Label Lang Select   :', elMap['labelLangSelect']?.textContent);

console.log('\n=== 2. TESTING SPOTLIGHT CARD ACROSS ALL 7 CATEGORIES IN SPANISH ===');
const testCases = [
  { b: '1. Dhamir', nk: '1a', expectedKata: 'هُوَ' },
  { b: '2. Mawshul', nk: '1', expectedKata: 'مَا' },
  { b: '3. Istifham', nk: '1', expectedKata: 'مَا' },
  { b: '4. Syarath', nk: '3', expectedKata: 'كُلَّمَا' },
  { b: '5. Isyarah', nk: '1', expectedKata: 'ذَٰلِكَ / ذَا' },
  { b: "6. Isim Fi'il", nk: '1', expectedKata: 'سُبْحَانَ' },
  { b: "7. Fi'il Jamid", nk: '1', expectedKata: 'لَيْسَ' }
];

let failed = 0;
for (const tc of testCases) {
  global.selectBentuk(tc.b);
  global.selectNoKata(tc.nk);
  
  const bText = elMap['badgeBentukKata']?.textContent;
  const jText = elMap['badgeJenis']?.textContent;
  const word = elMap['arabicWordDisplay']?.textContent;
  const meaning = elMap['wordMeaningDisplay']?.textContent;
  const meaningSub = elMap['wordMeaningSub']?.textContent;
  
  console.log(`[Category: ${tc.b} | Word: ${tc.nk}]`);
  console.log(`  Badge Bentuk : ${bText}`);
  console.log(`  Badge Jenis  : ${jText}`);
  console.log(`  Lafaz Arab   : ${word}`);
  console.log(`  Arti Utama   : ${meaning}`);
  console.log(`  Sub-makna    : ${meaningSub}`);
  
  if (!bText || !jText || !word || !meaning) {
    console.error(`  --> FAILED on ${tc.b} ${tc.nk}!`);
    failed++;
  }
}

console.log('\n=== 3. TESTING AI PROMPT GENERATOR IN SPANISH ===');
const sampleGroup = global.DHAMIR_DATA.find(d => d['Bentuk Kata'] === '4. Syarath' && d['No kata'] === '3');
if (sampleGroup) {
  const occ = {
    surat: 2,
    ayat: 20,
    suratNama: 'Al-Baqarah',
    teksArab: sampleGroup.TeksArab,
    teksArtiES: sampleGroup.TeksArtiES
  };
  const gObj = {
    kata: sampleGroup.Kata,
    noKata: sampleGroup['No kata'],
    bentuk: sampleGroup['Bentuk Kata'],
    grammar: sampleGroup.Grammar || {}
  };
  const promptNahwu = global.buildAiPrompt(gObj, occ, 'nahwu');
  console.log('  Nahwu Prompt Preview (First 200 chars):');
  console.log('  ' + promptNahwu.replace(/\n/g, ' ').slice(0, 200) + '...');
}

if (failed === 0) {
  console.log('\n>>> ALL SPANISH INTEGRATION VERIFICATION TESTS PASSED SUCCESSFULLY! <<<');
} else {
  console.error(`\n>>> FAILED with ${failed} errors! <<<`);
  process.exit(1);
}
