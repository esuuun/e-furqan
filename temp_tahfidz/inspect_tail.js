const fs = require('fs');
const path = 'd:/TAHFIDZ ANTIGRAVITY/quran-data.js';

try {
    const stats = fs.statSync(path);
    const size = stats.size;
    const buffer = Buffer.alloc(200);
    const fd = fs.openSync(path, 'r');
    fs.readSync(fd, buffer, 0, 200, Math.max(0, size - 200));
    fs.closeSync(fd);

    console.log('--- Last 200 chars of quran-data.js ---');
    console.log(buffer.toString('utf8'));
    console.log('---------------------------------------');
} catch (e) {
    console.error(e);
}
