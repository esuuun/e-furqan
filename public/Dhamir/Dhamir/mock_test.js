
const fs = require('fs');

// Mock browser objects
global.window = {
  speechSynthesis: {
    getVoices: () => [{ lang: 'pt-PT', name: 'Portuguese Natural Voice' }]
  },
  DHAMIR_DATA: JSON.parse(fs.readFileSync('dhamir_data.json', 'utf8'))
};
global.document = {
  documentElement: { setAttribute: () => {}, lang: '' },
  createElement: () => ({ appendChild: () => {}, classList: { add: () => {}, remove: () => {} }, setAttribute: () => {}, querySelectorAll: () => [] }),
  body: { appendChild: () => {}, removeChild: () => {}, style: {} },
  addEventListener: () => {}
};
global.localStorage = {
  getItem: () => 'pt',
  setItem: () => {}
};

console.log('Testing Node environment simulation of app logic...');
