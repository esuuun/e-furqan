const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');

// Extract the checkTextMatchesTerms and highlightKeyword functions from index.html
const fnMatch1 = content.match(/function checkTextMatchesTerms[\s\S]*?\n        \}/);
const fnMatch2 = content.match(/function highlightKeyword[\s\S]*?\n        \}/);

if (!fnMatch1 || !fnMatch2) {
    console.error('Could not extract functions!');
    process.exit(1);
}

eval(fnMatch1[0]);
eval(fnMatch2[0]);

const ketamakanText = '5.13.5.2. Ketamakan Kerajaan Saba Untuk Melakukan Monopoli';
const makananText = '13.1.1.1. Seluruh Makanan Yang Baik-baik Pada Dasarnya Halal';
const makanText = '7.13.2.2. Etika Makan Bersama Ketika Bertamu';

console.log('checkTextMatchesTerms results for "makan":');
console.log(' - Ketamakan:', checkTextMatchesTerms(ketamakanText, ['makan']));
console.log(' - Makanan:', checkTextMatchesTerms(makananText, ['makan']));
console.log(' - Makan:', checkTextMatchesTerms(makanText, ['makan']));

console.log('\nhighlightKeyword results for "makan":');
console.log(' - Ketamakan:', highlightKeyword(ketamakanText, ['makan']));
console.log(' - Makanan:', highlightKeyword(makananText, ['makan']));
console.log(' - Makan:', highlightKeyword(makanText, ['makan']));
