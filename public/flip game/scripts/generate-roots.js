import fs from 'fs';
import path from 'path';
import https from 'https';

const url = 'https://raw.githubusercontent.com/mustafa0x/quran-morphology/master/quran-morphology.txt';
const dest = path.resolve('public/roots.json');

console.log('Downloading Quranic Corpus Morphology data...');

https.get(url, (res) => {
  let data = '';

  res.on('data', (chunk) => {
    data += chunk;
  });

  res.on('end', () => {
    console.log('Download complete. Processing data...');
    
    const lines = data.split('\n');
    const rootDict = {};

    for (const line of lines) {
      if (!line.trim()) continue;
      
      const parts = line.split('\t');
      if (parts.length >= 4) {
        const id = parts[0]; // e.g. 1:1:1:1
        const features = parts[3]; // e.g. ROOT:حمد|LEM:حَمْد|M|NOM
        
        const idParts = id.split(':');
        if (idParts.length >= 3) {
          const surah = idParts[0];
          const ayah = idParts[1];
          const wordPos = idParts[2];
          const key = `${surah}_${ayah}_${wordPos}`;
          
          const rootMatch = features.match(/ROOT:([^\s|]+)/);
          if (rootMatch && rootMatch[1]) {
            const rootString = rootMatch[1];
            // Format to space-separated Arabic letters
            const formattedRoot = rootString.split('').join(' ');
            
            rootDict[key] = formattedRoot;
          }
        }
      }
    }

    fs.writeFileSync(dest, JSON.stringify(rootDict, null, 0));
    console.log(`Saved ${Object.keys(rootDict).length} unique word roots to public/roots.json`);
  });

}).on('error', (err) => {
  console.error('Error downloading:', err.message);
});
