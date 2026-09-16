const fs = require('fs');
const txt = fs.readFileSync('index.html', 'utf8');
const lines = txt.split('\n');
lines.forEach((l, i) => {
    if (l.includes('DOMContentLoaded') || l.includes('function init') || l.includes('window.onload') || l.includes('init()')) {
        console.log(`${i+1}: ${l}`);
    }
});
