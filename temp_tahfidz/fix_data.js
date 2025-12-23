const fs = require('fs');
const path = 'd:/TAHFIDZ ANTIGRAVITY/quran-data.js';

try {
    let content = fs.readFileSync(path, 'utf8');
    console.log('Original length:', content.length);

    // Find properties of end
    // We look for the last occurrence of "}]}]"
    const marker = '"id":6,"text":"مِنَ ٱلۡجِنَّةِ وَٱلنَّاسِ"}]}]';
    const idx = content.lastIndexOf(marker);

    if (idx !== -1) {
        // Truncate everything after the marker
        const newContent = content.substring(0, idx + marker.length) + ';';
        fs.writeFileSync(path, newContent);
        console.log('Fixed content. New length:', newContent.length);
        console.log('End:', newContent.slice(-20));
    } else {
        console.error('Marker not found!');
    }

} catch (e) {
    console.error(e);
}
