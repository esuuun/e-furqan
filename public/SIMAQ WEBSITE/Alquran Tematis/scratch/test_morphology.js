function getIndonesianBaseWords(word) {
    if (!word || word.length < 5) return [word];
    const bases = new Set([word]);

    if (word.startsWith('peng') && word.endsWith('an') && word.length > 7) {
        bases.add(word.slice(4, -2));
    } else if (word.startsWith('per') && word.endsWith('an') && word.length > 6) {
        bases.add(word.slice(3, -2));
    } else if (word.startsWith('pe') && word.endsWith('an') && word.length > 5) {
        bases.add(word.slice(2, -2));
    } else if (word.startsWith('ke') && word.endsWith('an') && word.length > 5) {
        bases.add(word.slice(2, -2));
    }

    if (word.startsWith('me') && word.endsWith('kan') && word.length > 6) {
        bases.add(word.slice(2, -3));
    }
    if (word.startsWith('ber') && word.length > 5) {
        bases.add(word.slice(3));
    }
    if (word.startsWith('ter') && word.length > 5) {
        bases.add(word.slice(3));
    }

    return Array.from(bases).filter(b => b && b.length >= 3);
}

const words = ['kemabukan', 'pernikahan', 'keadilan', 'kesabaran', 'kematian', 'berjudi', 'memabukkan'];
for (const w of words) {
    console.log(w, '->', getIndonesianBaseWords(w));
}
