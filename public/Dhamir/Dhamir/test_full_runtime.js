const fs = require('fs');
const vm = require('vm');

const context = {
  console,
  localStorage: {
    getItem: () => null,
    setItem: () => null
  },
  document: {
    documentElement: {
      setAttribute: () => {},
      removeAttribute: () => {},
      getAttribute: () => 'dark'
    },
    createElement: (tag) => ({
      tagName: tag,
      appendChild: () => {},
      setAttribute: () => {},
      querySelectorAll: () => [],
      classList: { add: () => {}, remove: () => {} }
    }),
    querySelector: () => null,
    querySelectorAll: () => [],
    getElementById: (id) => ({
      id,
      innerHTML: '',
      textContent: '',
      style: {},
      appendChild: () => {},
      addEventListener: () => {},
      classList: { add: () => {}, remove: () => {} },
      setAttribute: () => {},
      querySelectorAll: () => []
    }),
    addEventListener: () => {}
  },
  window: {}
};
vm.createContext(context);

['dhamir_data.js', 'harf_data.js', 'harf_amil_data.js', 'musytaq_data.js', 'app.js'].forEach(f => {
  const code = fs.readFileSync(f, 'utf8');
  vm.runInContext(code, context);
  console.log(`[OK] Evaluated ${f} without errors!`);
});

const stats = vm.runInContext(`({
  jamidLen: typeof DHAMIR_DATA !== 'undefined' ? DHAMIR_DATA.length : 0,
  harfLen: typeof HARF_DATA !== 'undefined' ? HARF_DATA.length : 0,
  harfAmilLen: typeof HARF_AMIL_DATA !== 'undefined' ? HARF_AMIL_DATA.length : 0,
  harfAmilCats: typeof HARF_AMIL_BENTUK_LABELS !== 'undefined' ? Object.keys(HARF_AMIL_BENTUK_LABELS).length : 0,
  harfAmilGrammar: typeof HARF_AMIL_GRAMMAR_INFO !== 'undefined' ? Object.keys(HARF_AMIL_GRAMMAR_INFO).length : 0
})`, context);

console.log('\n=== RUNTIME DATA SUMMARY ===');
console.log('Total Jamid Mabny Entries:', stats.jamidLen);
console.log('Total Harf Ghair Amil Entries:', stats.harfLen);
console.log('Total Harf Amil Entries:', stats.harfAmilLen);
console.log('Total Harf Amil Categories:', stats.harfAmilCats);
console.log('Total Harf Amil Grammar Metadata:', stats.harfAmilGrammar);
console.log('\n[SUCCESS] ALL DATASETS & APPLICATION JS EVALUATED CLEANLY AND FLAWLESSLY!');
