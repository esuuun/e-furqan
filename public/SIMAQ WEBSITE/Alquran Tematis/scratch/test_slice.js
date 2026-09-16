const fs = require('fs');
const lines = fs.readFileSync('index.html', 'utf8').split(/\r?\n/);

console.log('Line 5289 (index 5288):', lines[5288]);
console.log('Line 5290 (index 5289):', lines[5289]);
console.log('Line 5526 (index 5525):', lines[5525]);
console.log('Line 5527 (index 5526):', lines[5526]);
