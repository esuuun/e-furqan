const fs = require('fs');
const txt = fs.readFileSync('index.html', 'utf8');
const lines = txt.split('\n');
lines.forEach((l, i) => {
    if (l.includes('tab-btn-keyword') || l.includes('keyword-nav-container') || l.includes('keyword-view-wrapper') || l.includes('keyword-input') || l.includes('keyword-popular-wrap')) {
        console.log(`${i+1}: ${l.trim()}`);
    }
});
