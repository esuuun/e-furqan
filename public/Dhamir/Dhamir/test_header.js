
const fs = require('fs');
let code = fs.readFileSync('app.js', 'utf8');

// Mock DOM
global.document = {
  documentElement: { setAttribute: () => {}, removeAttribute: () => {} },
  createElement: () => ({}),
  getElementById: (id) => ({ id: id, innerHTML: '', textContent: '', classList: { add: ()=>{}, remove: ()=>{} }, setAttribute: ()=>{} })
};
global.localStorage = { getItem: () => null, setItem: () => {} };

// Patch to prevent errors
code = code.replace('document.addEventListener', '//document.addEventListener');

// Evaluate app.js
eval(code);

// Run test
state.lang = 'fa';
state.activeDict = 'jamid';
updateHeaderTitles();
console.log('FA brandTitle:', elements.brandTitle.innerHTML);
console.log('FA brandSubtitle:', elements.brandSubtitle.textContent);

state.lang = 'ru';
updateHeaderTitles();
console.log('RU brandTitle:', elements.brandTitle.innerHTML);
