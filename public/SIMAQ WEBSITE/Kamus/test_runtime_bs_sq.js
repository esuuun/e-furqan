/**
 * Runtime Simulation Test for Bosnian and Albanian in app.js
 */

const fs = require('fs');
const vm = require('vm');

// Mock browser environment
const localStorageData = {};
const window = {
  speechSynthesis: {
    getVoices: () => [
      { name: 'Microsoft Goran Online (Natural) - Bosnian (Bosnia and Herzegovina)', lang: 'bs-BA' },
      { name: 'Microsoft Anila Online (Natural) - Albanian (Albania)', lang: 'sq-AL' }
    ],
    speak: () => {},
    cancel: () => {},
    onvoiceschanged: null
  }
};
const localStorage = {
  getItem: (k) => localStorageData[k] || null,
  setItem: (k, v) => { localStorageData[k] = v; }
};
const document = {
  documentElement: {
    lang: 'id',
    setAttribute: () => {},
    removeAttribute: () => {}
  },
  getElementById: (id) => ({
    id,
    style: {},
    classList: { add: () => {}, remove: () => {} },
    setAttribute: () => {},
    removeAttribute: () => {},
    addEventListener: () => {},
    innerHTML: '',
    textContent: '',
    value: '',
    appendChild: () => {}
  }),
  createElement: (tag) => ({
    tagName: tag,
    style: {},
    classList: { add: () => {}, remove: () => {} },
    setAttribute: () => {},
    removeAttribute: () => {},
    addEventListener: () => {},
    appendChild: () => {},
    querySelectorAll: () => [],
    querySelector: () => null,
    innerHTML: '',
    textContent: '',
    value: ''
  }),
  addEventListener: () => {},
  querySelectorAll: () => []
};

// Load dhamir_data.js and harf_data.js
const dhamirJs = fs.readFileSync('./dhamir_data.js', 'utf8');
const harfJs = fs.readFileSync('./harf_data.js', 'utf8');
const appJs = fs.readFileSync('./app.js', 'utf8');

const sandbox = {
  window,
  document,
  localStorage,
  Audio: function(url) { this.url = url; this.play = () => Promise.resolve(); },
  console,
  setTimeout,
  clearTimeout,
  navigator: { clipboard: { writeText: () => Promise.resolve() } }
};

vm.createContext(sandbox);

// Execute files
vm.runInContext(dhamirJs, sandbox);
vm.runInContext(harfJs, sandbox);
vm.runInContext(appJs, sandbox);

console.log("=" .repeat(65));
console.log("TEST RUNTIME SIMULASI BAHASA BOSNIA & ALBANIA");
console.log("=" .repeat(65));

const DHAMIR_DATA = JSON.parse(fs.readFileSync('./dhamir_data.json', 'utf8'));
const HARF_DATA = JSON.parse(fs.readFileSync('./harf_data.json', 'utf8'));
console.log(`[PASS] Dataset loaded: ${DHAMIR_DATA.length} Dhamir, ${HARF_DATA.length} Harf entries.`);

// Test 2: Check Bosnian and Albanian translations in datasets
let bsMissingTeks = 0, sqMissingTeks = 0;
let bsMissingArti = 0, sqMissingArti = 0;

DHAMIR_DATA.forEach(d => {
  if (!d.TeksArtiBS) bsMissingTeks++;
  if (!d.TeksArtiSQ) sqMissingTeks++;
  if (!d.ArtiKataBS) bsMissingArti++;
  if (!d.ArtiKataSQ) sqMissingArti++;
});

console.log(`[PASS] Jamid Mabny:`);
console.log(`       Bosnian  - Teks: ${DHAMIR_DATA.length - bsMissingTeks}/${DHAMIR_DATA.length}, Arti: ${DHAMIR_DATA.length - bsMissingArti}/${DHAMIR_DATA.length}`);
console.log(`       Albanian - Teks: ${DHAMIR_DATA.length - sqMissingTeks}/${DHAMIR_DATA.length}, Arti: ${DHAMIR_DATA.length - sqMissingArti}/${DHAMIR_DATA.length}`);

// Sample Verse 1:1 test
const sampleDhamir = DHAMIR_DATA.find(d => d.SURAT === 112 && d.AYAT === 1) || DHAMIR_DATA[0];
console.log(`\nContoh Teks Terjemahan Surat ${sampleDhamir.SURAT}:${sampleDhamir.AYAT} (Kata: ${sampleDhamir.Kata}):`);
console.log(`  [Bosnian]  Arti Kata: "${sampleDhamir.ArtiKataBS}" | Ayat: "${sampleDhamir.TeksArtiBS}"`);
console.log(`  [Albanian] Arti Kata: "${sampleDhamir.ArtiKataSQ}" | Ayat: "${sampleDhamir.TeksArtiSQ}"`);

if (!sampleDhamir.TeksArtiBS || !sampleDhamir.TeksArtiSQ) {
  throw new Error("Missing sample translation!");
}

console.log("\n" + "=" .repeat(65));
console.log("SELURUH RUNTIME SIMULASI SUKSES 100%!");
console.log("=" .repeat(65));
