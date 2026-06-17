/**
 * Centralized Data for Interactive QTajwid Level 1
 * Contains:
 * 1. hijaiyahSounds: For "Klik & Dengar", "Tebak Suara", "Cek Ucapan"
 * 2. wordList: For "Susun Kata"
 */

// --- 1. LETTER DATABASE (HIJAIYAH) ---
// Used by: Module 1, Module 2, Module 4
export const hijaiyahSounds = [
    // Basic Alif-Ya
    { text: 'اَ', sound: 'a', name: 'Alif Fathah' },
    { text: 'اِ', sound: 'i', name: 'Alif Kasrah' },
    { text: 'اُ', sound: 'u', name: 'Alif Dhammah' },

    { text: 'بَ', sound: 'ba', name: 'Ba Fathah' },
    { text: 'بِ', sound: 'bi', name: 'Ba Kasrah' },
    { text: 'بُ', sound: 'bu', name: 'Ba Dhammah' },

    { text: 'تَ', sound: 'ta', name: 'Ta Fathah' },
    { text: 'تِ', sound: 'ti', name: 'Ta Kasrah' },
    { text: 'تُ', sound: 'tu', name: 'Ta Dhammah' },

    { text: 'ثَ', sound: 'tsa', soundAlt: 'tsa', name: 'Tsa Fathah' },
    { text: 'ثِ', sound: 'thi', soundAlt: 'tsi', name: 'Tsa Kasrah' },
    { text: 'ثُ', sound: 'thu', soundAlt: 'tsu', name: 'Tsa Dhammah' },

    { text: 'جَ', sound: 'ja', name: 'Jim Fathah' },
    { text: 'جِ', sound: 'ji', name: 'Jim Kasrah' },
    { text: 'جُ', sound: 'ju', name: 'Jim Dhammah' },

    { text: 'حَ', sound: 'ha_h', soundAlt: 'ha_h', name: 'Ha Fathah' },
    { text: 'حِ', sound: 'hi', name: 'Ha Kasrah' },
    { text: 'حُ', sound: 'hu', name: 'Ha Dhammah' },

    { text: 'خَ', sound: 'kho', soundAlt: 'kho', name: 'Kho Fathah' },
    { text: 'خِ', sound: 'khi', name: 'Kho Kasrah' },
    { text: 'خُ', sound: 'khu', name: 'Kho Dhammah' },

    { text: 'دَ', sound: 'da', name: 'Dal Fathah' },
    { text: 'دِ', sound: 'di', name: 'Dal Kasrah' },
    { text: 'دُ', sound: 'du', name: 'Dal Dhammah' },

    { text: 'ذَ', sound: 'dza', soundAlt: 'dho', name: 'Dzal Fathah' },
    { text: 'ذِ', sound: 'dzi', name: 'Dzal Kasrah' },
    { text: 'ذُ', sound: 'dzu', name: 'Dzal Dhammah' },

    { text: 'رَ', sound: 'ro', soundAlt: 'ro', name: 'Ra Fathah' },
    { text: 'رِ', sound: 'ri', name: 'Ra Kasrah' },
    { text: 'رُ', sound: 'ru', name: 'Ra Dhammah' },

    { text: 'زَ', sound: 'za', name: 'Zai Fathah' },
    { text: 'زِ', sound: 'zi', name: 'Zai Kasrah' },
    { text: 'زُ', sound: 'zu', name: 'Zai Dhammah' },

    { text: 'سَ', sound: 'sa', name: 'Sin Fathah' },
    { text: 'سِ', sound: 'si', name: 'Sin Kasrah' },
    { text: 'سُ', sound: 'su', name: 'Sin Dhammah' },

    { text: 'شَ', sound: 'sya', soundAlt: 'sho', name: 'Syin Fathah' },
    { text: 'شِ', sound: 'syi', name: 'Syin Kasrah' },
    { text: 'شُ', sound: 'syu', name: 'Syin Dhammah' },

    { text: 'صَ', sound: 'sho', soundAlt: 'sho', name: 'Shod Fathah' },
    { text: 'صِ', sound: 'shi', name: 'Shod Kasrah' },
    { text: 'صُ', sound: 'shu', name: 'Shod Dhammah' },

    { text: 'ضَ', sound: 'dho', soundAlt: 'dho', name: 'Dhod Fathah' },
    { text: 'ضِ', sound: 'dhi', name: 'Dhod Kasrah' },
    { text: 'ضُ', sound: 'dhu', name: 'Dhod Dhammah' },

    { text: 'طَ', sound: 'tho', soundAlt: 'tho', name: 'Tho Fathah' },
    { text: 'طِ', sound: 'thi2', name: 'Tho Kasrah' },
    { text: 'طُ', sound: 'thu2', name: 'Tho Dhammah' },

    { text: 'ظَ', sound: 'zho', soundAlt: 'zho', name: 'Zho Fathah' },
    { text: 'ظِ', sound: 'zhi', name: 'Zho Kasrah' },
    { text: 'ظُ', sound: 'zhu', name: 'Zho Dhammah' },

    { text: 'عَ', sound: 'ain', soundAlt: 'ain', name: 'Ain Fathah' },
    { text: 'عِ', sound: 'ii', name: 'Ain Kasrah' },
    { text: 'عُ', sound: 'uu', name: 'Ain Dhammah' },

    { text: 'غَ', sound: 'ghain', soundAlt: 'ghain', name: 'Ghain Fathah' },
    { text: 'غِ', sound: 'ghi', name: 'Ghain Kasrah' },
    { text: 'غُ', sound: 'ghu', name: 'Ghain Dhammah' },

    { text: 'فَ', sound: 'fa', name: 'Fa Fathah' },
    { text: 'فِ', sound: 'fi', name: 'Fa Kasrah' },
    { text: 'فُ', sound: 'fu', name: 'Fa Dhammah' },

    { text: 'قَ', sound: 'qof', soundAlt: 'qof', name: 'Qof Fathah' },
    { text: 'قِ', sound: 'qi', name: 'Qof Kasrah' },
    { text: 'قُ', sound: 'qu', name: 'Qof Dhammah' },

    { text: 'كَ', sound: 'kaf', soundAlt: 'kaf', name: 'Kaf Fathah' },
    { text: 'كِ', sound: 'ki', name: 'Kaf Kasrah' },
    { text: 'كُ', sound: 'ku', name: 'Kaf Dhammah' },

    { text: 'لَ', sound: 'lam', soundAlt: 'lam', name: 'Lam Fathah' },
    { text: 'لِ', sound: 'li', name: 'Lam Kasrah' },
    { text: 'لُ', sound: 'lu', name: 'Lam Dhammah' },

    { text: 'مَ', sound: 'mim', soundAlt: 'mim', name: 'Mim Fathah' },
    { text: 'مِ', sound: 'mi', name: 'Mim Kasrah' },
    { text: 'مُ', sound: 'mu', name: 'Mim Dhammah' },

    { text: 'نَ', sound: 'nun', soundAlt: 'nun', name: 'Nun Fathah' },
    { text: 'نِ', sound: 'ni', name: 'Nun Kasrah' },
    { text: 'نُ', sound: 'nu', name: 'Nun Dhammah' },

    { text: 'وَ', sound: 'waw', soundAlt: 'waw', name: 'Waw Fathah' },
    { text: 'وِ', sound: 'wi', name: 'Waw Kasrah' },
    { text: 'وُ', sound: 'wu', name: 'Waw Dhammah' },

    { text: 'هَ', sound: 'ha', soundAlt: 'ha', name: 'Ha Fathah' },
    { text: 'هِ', sound: 'hi2', name: 'Ha Kasrah' },
    { text: 'هُ', sound: 'hu2', name: 'Ha Dhammah' },

    { text: 'يَ', sound: 'ya', name: 'Ya Fathah' },
    { text: 'يِ', sound: 'yi', name: 'Ya Kasrah' },
    { text: 'يُ', sound: 'yu', name: 'Ya Dhammah' }
];

// --- 2. WORD DATABASE (VOCABULARY) ---
// Used by: Module 3
export const rawWords = [
    { word: 'أَمِنَ', root: 'ء م ن' },
    { word: 'عَلِمَ', root: 'ع ل م' },
    { word: 'كَفَرَ', root: 'ك ف ر' },
    { word: 'عَمِلَ', root: 'ع م ل' },
    { word: 'جَعَلَ', root: 'ج ع ل' },
    { word: 'رَحِمَ', root: 'ر ح م' },
    { word: 'كُتِبَ', root: 'ك ت ب' },
    { word: 'ظَلَمَ', root: 'ظ ل م' },
    { word: 'هُدِيَ', root: 'ه د ي' },
    { word: 'نَزَلَ', root: 'ن ز ل' },
    { word: 'كَذَبَ', root: 'ك ذ ب' },
    { word: 'عَبَدَ', root: 'ع ب د' },
    { word: 'ذُكِرَ', root: 'ذ ك ر' }
    // ... truncated for brevity, can add more later if needed
];

// Simplified meanings mapping
export const meanings = {
    'أَمِنَ': 'beriman', 'عَلِمَ': 'mengetahui', 'كَفَرَ': 'kafir', 'عَمِلَ': 'beramal',
    'جَعَلَ': 'menjadikan', 'رَحِمَ': 'merahmati', 'كُتِبَ': 'ditulis', 'ظَلَمَ': 'menganiaya',
    'هُدِيَ': 'diberi petunjuk', 'نَزَلَ': 'turun', 'كَذَبَ': 'berdusta', 'عَبَدَ': 'menyembah',
    'ذُكِرَ': 'diingat'
};

// --- HELPER FUNCTIONS FOR DATA ---

function removeTanwin(text) {
    return text.replace(/[ًٌٍ]/g, '');
}

function removeAllHarakat(text) {
    return text.replace(/[ًٌٍَُِّْ¹²]/g, '');
}

function createWordPieces(arabicWord) {
    let cleanWord = removeTanwin(arabicWord);
    const pieces = [];
    let i = 0;

    while (i < cleanWord.length) {
        let currentChar = cleanWord[i];

        // Skip purely harakat chars if they start a loop (safety check)
        if (/[ًٌٍَُِّْ]/.test(currentChar)) {
            i++;
            continue;
        }

        let piece = currentChar;

        // Append harakat to the base letter
        if (i + 1 < cleanWord.length && /[َُِّْ]/.test(cleanWord[i + 1])) {
            piece += cleanWord[i + 1];
            i++;
        }

        pieces.push({
            text: piece,
            value: `piece_${pieces.length}_${piece}`
        });

        i++;
    }
    return pieces;
}

// Prepare the ready-to-use word list
export const wordList = rawWords.map((item) => {
    const cleanWord = removeTanwin(item.word);

    // Construct audio filename: remove harakat, replace spaces with underscores
    // Note: Assuming audio files match this pattern based on original code
    const audioName = removeAllHarakat(cleanWord).split('').join('');

    return {
        word: cleanWord,
        meaning: meanings[item.word] || 'Terjemahan belum tersedia',
        // In the original, it tried to map root letters to audio.
        // For now we will use a generic placeholder or dynamic TTS if specific file missing.
        audio: audioName,
        pieces: createWordPieces(item.word)
    };
});

// ==========================================
// LEVEL 2 DATA (Centralized)
// ==========================================

// --- Module 5: Mad Panjang (Word List) ---
export const madPanjangWords = [
    // 10 MAD PANJANG A (Fathah + Alif)
    { transliteration: 'qāla', translation: 'dia (laki) berkata', parts: [{ text: 'قَا', isMad: true }, { text: 'لَ', isMad: false }] },
    { transliteration: 'kāna', translation: 'adalah / pernah', parts: [{ text: 'كَا', isMad: true }, { text: 'نَ', isMad: false }] },
    { transliteration: 'nasā', translation: 'dia lupa', parts: [{ text: 'نَ', isMad: false }, { text: 'سَا', isMad: true }] },
    { transliteration: 'jā\'a', translation: 'dia datang', parts: [{ text: 'جَا', isMad: true }, { text: 'ءَ', isMad: false }] },
    { transliteration: 'bā\'da', translation: 'setelah / sesudah', parts: [{ text: 'بَا', isMad: true }, { text: 'عَ', isMad: false }, { text: 'دَ', isMad: false }] },
    { transliteration: 'ṣalāh', translation: 'sholat', parts: [{ text: 'صَ', isMad: false }, { text: 'لَا', isMad: true }, { text: 'ةٌ', isMad: false }] },
    { transliteration: 'ṣābir', translation: 'sabar', parts: [{ text: 'صَا', isMad: true }, { text: 'بِ', isMad: false }, { text: 'رٍ', isMad: false }] },
    { transliteration: 'nāma', translation: 'dia tidur', parts: [{ text: 'نَا', isMad: true }, { text: 'مَ', isMad: false }] },
    { transliteration: 'māta', translation: 'dia mati', parts: [{ text: 'مَا', isMad: true }, { text: 'تَ', isMad: false }] },
    { transliteration: 'ḍālla', translation: 'sesat', parts: [{ text: 'ضَا', isMad: true }, { text: 'لَّ', isMad: false }] },
    // 10 MAD PANJANG I (Kasrah + Ya Sukun)
    { transliteration: 'qīla', translation: 'dikatakan', parts: [{ text: 'قِي', isMad: true }, { text: 'لَ', isMad: false }] },
    { transliteration: 'fīhi', translation: 'di dalamnya', parts: [{ text: 'فِي', isMad: true }, { text: 'هِ', isMad: false }] },
    { transliteration: 'dīn', translation: 'agama', parts: [{ text: 'دِي', isMad: true }, { text: 'نٌ', isMad: false }] },
    { transliteration: 'samīʿ', translation: 'pendengar', parts: [{ text: 'سَ', isMad: false }, { text: 'مِي', isMad: true }, { text: 'عٌ', isMad: false }] },
    { transliteration: 'baṣīr', translation: 'melihat', parts: [{ text: 'بَ', isMad: false }, { text: 'صِي', isMad: true }, { text: 'رٌ', isMad: false }] },
    { transliteration: 'ʿalīm', translation: 'mengetahui', parts: [{ text: 'عَ', isMad: false }, { text: 'لِي', isMad: true }, { text: 'مٌ', isMad: false }] },
    { transliteration: 'ḥakīm', translation: 'bijaksana', parts: [{ text: 'حَ', isMad: false }, { text: 'كِي', isMad: true }, { text: 'مٌ', isMad: false }] },
    { transliteration: 'karīm', translation: 'mulia', parts: [{ text: 'كَ', isMad: false }, { text: 'رِي', isMad: true }, { text: 'مٌ', isMad: false }] },
    { transliteration: 'qawīy', translation: 'kuat', parts: [{ text: 'قَ', isMad: false }, { text: 'وِيٌّ', isMad: true }] },
    { transliteration: 'naḍīr', translation: 'pemberi peringatan', parts: [{ text: 'نَ', isMad: false }, { text: 'ذِي', isMad: true }, { text: 'رٌ', isMad: false }] },
    // 10 MAD PANJANG U (Dhammah + Waw Sukun)
    { transliteration: 'yaqūlu', translation: 'dia mengatakan', parts: [{ text: 'يَ', isMad: false }, { text: 'قُو', isMad: true }, { text: 'لُ', isMad: false }] },
    { transliteration: 'nūr', translation: 'cahaya', parts: [{ text: 'نُو', isMad: true }, { text: 'رٌ', isMad: false }] },
    { transliteration: 'sujūd', translation: 'sujud', parts: [{ text: 'سُ', isMad: false }, { text: 'جُو', isMad: true }, { text: 'دٌ', isMad: false }] },
    { transliteration: 'ghafūr', translation: 'pengampun', parts: [{ text: 'غَ', isMad: false }, { text: 'فُو', isMad: true }, { text: 'رٌ', isMad: false }] },
    { transliteration: 'shakūr', translation: 'pembalas kebaikan', parts: [{ text: 'شَ', isMad: false }, { text: 'كُو', isMad: true }, { text: 'رٌ', isMad: false }] },
    { transliteration: 'quddūs', translation: 'maha suci', parts: [{ text: 'قُ', isMad: false }, { text: 'دُّو', isMad: true }, { text: 'سٌ', isMad: false }] },
    { transliteration: 'rasūl', translation: 'rasul / utusan', parts: [{ text: 'رَ', isMad: false }, { text: 'سُو', isMad: true }, { text: 'لٌ', isMad: false }] },
    { transliteration: 'ṣūr', translation: 'sangkakala', parts: [{ text: 'صُو', isMad: true }, { text: 'رٍ', isMad: false }] },
    { transliteration: 'nuzūl', translation: 'turun', parts: [{ text: 'نُ', isMad: false }, { text: 'زُو', isMad: true }, { text: 'لٌ', isMad: false }] },
    { transliteration: 'kafūr', translation: 'sangat kafir', parts: [{ text: 'كَ', isMad: false }, { text: 'فُو', isMad: true }, { text: 'رٌ', isMad: false }] }
];

// --- Module 6: Tanwin, Sukun, Tasydid ---
export const tanwinData = [
    { sound: 'ban', text: 'بًا' }, { sound: 'bin', text: 'بٍ' }, { sound: 'bun', text: 'بٌ' },
    { sound: 'tan', text: 'تًا' }, { sound: 'tin', text: 'تٍ' }, { sound: 'tun', text: 'تٌ' },
    { sound: 'tsan', text: 'ثًا' }, { sound: 'tsin', text: 'ثٍ' }, { sound: 'tsun', text: 'ثٌ' },
    { sound: 'jan', text: 'جًا' }, { sound: 'jin', text: 'جٍ' }, { sound: 'jun', text: 'جٌ' },
    { sound: 'han', text: 'حًا' }, { sound: 'hin', text: 'حٍ' }, { sound: 'hun', text: 'حٌ' },
    { sound: 'khan', text: 'خًا' }, { sound: 'khin', text: 'خٍ' }, { sound: 'khun', text: 'خٌ' },
    { sound: 'dan', text: 'دًا' }, { sound: 'din', text: 'دٍ' }, { sound: 'dun', text: 'دٌ' },
    { sound: 'dzan', text: 'ذًا' }, { sound: 'dzin', text: 'ذٍ' }, { sound: 'dzun', text: 'ذٌ' },
    { sound: 'ran', text: 'رًا' }, { sound: 'rin', text: 'رٍ' }, { sound: 'run', text: 'رٌ' },
    { sound: 'zan', text: 'زًا' }, { sound: 'zin', text: 'زٍ' }, { sound: 'zun', text: 'زٌ' },
    { sound: 'san', text: 'سًا' }, { sound: 'sin', text: 'سٍ' }, { sound: 'sun', text: 'سٌ' },
    { sound: 'syan', text: 'شًا' }, { sound: 'syin', text: 'شٍ' }, { sound: 'syun', text: 'شٌ' },
    { sound: 'shan', text: 'صًا' }, { sound: 'shin', text: 'صٍ' }, { sound: 'shun', text: 'صٌ' },
    { sound: 'dhan', text: 'ضًا' }, { sound: 'dhin', text: 'ضٍ' }, { sound: 'dhun', text: 'ضٌ' },
    { sound: 'than', text: 'طًا' }, { sound: 'thin', text: 'طٍ' }, { sound: 'thun', text: 'طٌ' },
    { sound: 'zhan', text: 'ظًا' }, { sound: 'zhin', text: 'ظٍ' }, { sound: 'zhun', text: 'ظٌ' },
    { sound: "'an", text: 'عًا' }, { sound: "'in", text: 'عٍ' }, { sound: "'un", text: 'عٌ' },
    { sound: 'ghan', text: 'غًا' }, { sound: 'ghin', text: 'غٍ' }, { sound: 'ghun', text: 'غٌ' },
    { sound: 'fan', text: 'فًا' }, { sound: 'fin', text: 'فٍ' }, { sound: 'fun', text: 'فٌ' },
    { sound: 'qan', text: 'قًا' }, { sound: 'qin', text: 'قٍ' }, { sound: 'qun', text: 'قٌ' },
    { sound: 'kan', text: 'كًا' }, { sound: 'kin', text: 'كٍ' }, { sound: 'kun', text: 'كٌ' },
    { sound: 'lan', text: 'لًا' }, { sound: 'lin', text: 'لٍ' }, { sound: 'lun', text: 'لٌ' },
    { sound: 'man', text: 'مًا' }, { sound: 'min', text: 'مٍ' }, { sound: 'mun', text: 'مٌ' },
    { sound: 'nan', text: 'نًا' }, { sound: 'nin', text: 'نٍ' }, { sound: 'nun', text: 'نٌ' },
    { sound: 'wan', text: 'وًا' }, { sound: 'win', text: 'وٍ' }, { sound: 'wun', text: 'وٌ' },
    { sound: 'han2', text: 'هًا' }, { sound: 'hin2', text: 'هٍ' }, { sound: 'hun2', text: 'هٌ' },
    { sound: 'laman', text: 'لاًا' }, { sound: 'lamin', text: 'لاٍ' }, { sound: 'lamun', text: 'لاٌ' },
    { sound: 'yan', text: 'يًا' }, { sound: 'yin', text: 'يٍ' }, { sound: 'yun', text: 'يٌ' }
];

export const sukunData = [
    { sound: 'ab', text: 'اَبْ' }, { sound: 'at', text: 'اَتْ' }, { sound: 'ats', text: 'اَثْ' },
    { sound: 'aj', text: 'اَجْ' }, { sound: 'ah', text: 'اَحْ' }, { sound: 'akh', text: 'اَخْ' },
    { sound: 'ad', text: 'اَدْ' }, { sound: 'adz', text: 'اَذْ' }, { sound: 'ar', text: 'اَرْ' },
    { sound: 'az', text: 'اَزْ' }, { sound: 'as', text: 'اَسْ' }, { sound: 'asy', text: 'اَشْ' },
    { sound: 'ash', text: 'اَصْ' }, { sound: 'adh', text: 'اَضْ' }, { sound: 'ath', text: 'اَطْ' },
    { sound: 'azh', text: 'اَظْ' }, { sound: "a'", text: 'اَعْ' }, { sound: 'agh', text: 'اَغْ' },
    { sound: 'af', text: 'اَفْ' }, { sound: 'aq', text: 'اَقْ' }, { sound: 'ak', text: 'اَكْ' },
    { sound: 'al', text: 'اَلْ' }, { sound: 'am', text: 'اَمْ' }, { sound: 'an2', text: 'اَنْ' },
    { sound: 'aw', text: 'اَوْ' }, { sound: 'ah2', text: 'اَهْ' }, { sound: 'ay', text: 'اَيْ' }
];

export const tasydidData = [
    { sound: 'abba', text: 'اَبَّ' }, { sound: 'atta', text: 'اَتَّ' }, { sound: 'atsa', text: 'اَثَّ' },
    { sound: 'ajja', text: 'اَجَّ' }, { sound: 'ahha', text: 'اَحَّ' }, { sound: 'akhkha', text: 'اَخَّ' },
    { sound: 'adda', text: 'اَدَّ' }, { sound: 'adzza', text: 'اَذَّ' }, { sound: 'arra', text: 'اَرَّ' },
    { sound: 'azza', text: 'اَزَّ' }, { sound: 'assa', text: 'اَسَّ' }, { sound: 'asyya', text: 'اَشَّ' },
    { sound: 'ashsha', text: 'اَصَّ' }, { sound: 'adhha', text: 'اَضَّ' }, { sound: 'aththa', text: 'اَطَّ' },
    { sound: 'azhzha', text: 'اَظَّ' }, { sound: "a''a", text: 'اَعَّ' }, { sound: 'aghgha', text: 'اَغَّ' },
    { sound: 'affa', text: 'اَفَّ' }, { sound: 'aqqa', text: 'اَقَّ' }, { sound: 'akka', text: 'اَكَّ' },
    { sound: 'alla', text: 'اَلَّ' }, { sound: 'amma', text: 'اَمَّ' }, { sound: 'anna', text: 'اَنَّ' },
    { sound: 'awwa', text: 'اَوَّ' }, { sound: 'ahha2', text: 'اَهَّ' }, { sound: 'ayya', text: 'اَيَّ' }
];

// --- Module 7: Qalqalah ---
export const qalqalahWords = [
    // JIM
    { arabicText: 'يَجْعَلُ', parts: [{ text: 'يَ', isQalqalah: false }, { text: 'جْ', isQalqalah: true, letter: 'ج' }, { text: 'عَ', isQalqalah: false }, { text: 'لُ', isQalqalah: false }], meaning: 'menjadikan', type: 'sughra' },
    { arabicText: 'نَجْمٌ', parts: [{ text: 'نَ', isQalqalah: false }, { text: 'جْ', isQalqalah: true, letter: 'ج' }, { text: 'مٌ', isQalqalah: false }], meaning: 'bintang', type: 'sughra' },
    { arabicText: 'أَجْرٌ', parts: [{ text: 'أَ', isQalqalah: false }, { text: 'جْ', isQalqalah: true, letter: 'ج' }, { text: 'رٌ', isQalqalah: false }], meaning: 'pahala', type: 'sughra' },
    { arabicText: 'رَجْعٌ', parts: [{ text: 'رَ', isQalqalah: false }, { text: 'جْ', isQalqalah: true, letter: 'ج' }, { text: 'عٌ', isQalqalah: false }], meaning: 'kembali', type: 'sughra' },
    { arabicText: 'يُخْرِجْ', parts: [{ text: 'يُ', isQalqalah: false }, { text: 'خْ', isQalqalah: false }, { text: 'رِ', isQalqalah: false }, { text: 'جْ', isQalqalah: true, letter: 'ج' }], meaning: 'mengeluarkan', type: 'kubra' },
    // QAF
    { arabicText: 'يَقْرَءُ', parts: [{ text: 'يَ', isQalqalah: false }, { text: 'قْ', isQalqalah: true, letter: 'ق' }, { text: 'رَ', isQalqalah: false }, { text: 'ءُ', isQalqalah: false }], meaning: 'membaca', type: 'sughra' },
    { arabicText: 'خَلَقْنَا', parts: [{ text: 'خَ', isQalqalah: false }, { text: 'لَ', isQalqalah: false }, { text: 'قْ', isQalqalah: true, letter: 'ق' }, { text: 'نَا', isQalqalah: false }], meaning: 'Kami ciptakan', type: 'sughra' },
    { arabicText: 'خَلَقْ', parts: [{ text: 'خَ', isQalqalah: false }, { text: 'لَ', isQalqalah: false }, { text: 'قْ', isQalqalah: true, letter: 'ق' }], meaning: 'menciptakan', type: 'kubra' },
    { arabicText: 'نَقْدِرُ', parts: [{ text: 'نَ', isQalqalah: false }, { text: 'قْ', isQalqalah: true, letter: 'ق' }, { text: 'دِ', isQalqalah: false }, { text: 'رُ', isQalqalah: false }], meaning: 'kami menentukan', type: 'sughra' },
    { arabicText: 'وَتَقْوَى', parts: [{ text: 'وَ', isQalqalah: false }, { text: 'تَ', isQalqalah: false }, { text: 'قْ', isQalqalah: true, letter: 'ق' }, { text: 'وَى', isQalqalah: false }], meaning: 'dan takwa', type: 'sughra' },
    // DAL
    { arabicText: 'يَدْخُلُونَ', parts: [{ text: 'يَ', isQalqalah: false }, { text: 'دْ', isQalqalah: true, letter: 'د' }, { text: 'خُ', isQalqalah: false }, { text: 'لُو', isQalqalah: false }, { text: 'نَ', isQalqalah: false }], meaning: 'mereka masuk', type: 'sughra' },
    { arabicText: 'أَحَدْ', parts: [{ text: 'أَ', isQalqalah: false }, { text: 'حَ', isQalqalah: false }, { text: 'دْ', isQalqalah: true, letter: 'د' }], meaning: 'satu/seorang', type: 'kubra' },
    { arabicText: 'قَدْ', parts: [{ text: 'قَ', isQalqalah: false }, { text: 'دْ', isQalqalah: true, letter: 'د' }], meaning: 'sungguh', type: 'kubra' },
    { arabicText: 'عَدْلٍ', parts: [{ text: 'عَ', isQalqalah: false }, { text: 'دْ', isQalqalah: true, letter: 'د' }, { text: 'لٍ', isQalqalah: false }], meaning: 'keadilan', type: 'sughra' },
    { arabicText: 'مَدْرَسَةٌ', parts: [{ text: 'مَ', isQalqalah: false }, { text: 'دْ', isQalqalah: true, letter: 'د' }, { text: 'رَ', isQalqalah: false }, { text: 'سَ', isQalqalah: false }, { text: 'ةٌ', isQalqalah: false }], meaning: 'sekolah', type: 'sughra' },
    // BA
    { arabicText: 'أَبْوَابًا', parts: [{ text: 'أَ', isQalqalah: false }, { text: 'بْ', isQalqalah: true, letter: 'ب' }, { text: 'وَا', isQalqalah: false }, { text: 'بًا', isQalqalah: false }], meaning: 'pintu-pintu', type: 'sughra' },
    { arabicText: 'أَقْرَبْ', parts: [{ text: 'أَ', isQalqalah: false }, { text: 'قْ', isQalqalah: false }, { text: 'رَ', isQalqalah: false }, { text: 'بْ', isQalqalah: true, letter: 'ب' }], meaning: 'lebih dekat', type: 'kubra' },
    { arabicText: 'يَبْسُطُ', parts: [{ text: 'يَ', isQalqalah: false }, { text: 'بْ', isQalqalah: true, letter: 'ب' }, { text: 'سُ', isQalqalah: false }, { text: 'طُ', isQalqalah: false }], meaning: 'meluaskan', type: 'sughra' },
    { arabicText: 'صَبْرًا', parts: [{ text: 'صَ', isQalqalah: false }, { text: 'بْ', isQalqalah: true, letter: 'ب' }, { text: 'رًا', isQalqalah: false }], meaning: 'kesabaran', type: 'sughra' },
    { arabicText: 'حِسَابْ', parts: [{ text: 'حِ', isQalqalah: false }, { text: 'سَا', isQalqalah: false }, { text: 'بْ', isQalqalah: true, letter: 'ب' }], meaning: 'perhitungan', type: 'kubra' },
    // THO
    { arabicText: 'يَطْمَعُ', parts: [{ text: 'يَ', isQalqalah: false }, { text: 'طْ', isQalqalah: true, letter: 'ط' }, { text: 'مَ', isQalqalah: false }, { text: 'عُ', isQalqalah: false }], meaning: 'mengharap', type: 'sughra' },
    { arabicText: 'قَطْرَةٌ', parts: [{ text: 'قَ', isQalqalah: false }, { text: 'طْ', isQalqalah: true, letter: 'ط' }, { text: 'رَ', isQalqalah: false }, { text: 'ةٌ', isQalqalah: false }], meaning: 'setetes', type: 'sughra' },
    { arabicText: 'فَرَّطْتُ', parts: [{ text: 'فَ', isQalqalah: false }, { text: 'رَّ', isQalqalah: false }, { text: 'طْ', isQalqalah: true, letter: 'ط' }, { text: 'تُ', isQalqalah: false }], meaning: 'aku lalai', type: 'sughra' },
    { arabicText: 'نَشَطْ', parts: [{ text: 'نَ', isQalqalah: false }, { text: 'شَ', isQalqalah: false }, { text: 'طْ', isQalqalah: true, letter: 'ط' }], meaning: 'bersemangat', type: 'kubra' },
    { arabicText: 'أَحَاطْ', parts: [{ text: 'أَ', isQalqalah: false }, { text: 'حَا', isQalqalah: false }, { text: 'طْ', isQalqalah: true, letter: 'ط' }], meaning: 'mengelilingi', type: 'kubra' }
];

// --- Module 8: Ghunnah ---
export const ghunnahData = {
    nun: [
        { text: 'إِنَّ', ref: 'Al-Fatiha: 6' },
        { text: 'إِنَّ', ref: 'Al-Baqarah: 165' },
        { text: 'جَنَّاتٍ', ref: 'Al-Baqarah: 25' },
        { text: 'النَّاسِ', ref: 'Al-Baqarah: 8' },
        { text: 'أَنَّهُ', ref: 'An-Najm: 42' },
        { text: 'إِنَّا', ref: 'Al-Baqarah: 156' }
    ],
    mim: [
        { text: 'ثُمَّ', ref: 'Al-Baqarah: 28' },
        { text: 'عَمَّ', ref: 'An-Naba: 1' },
        { text: 'عَمَّا', ref: 'An-Nahl: 1' },
        { text: 'مِمَّا', ref: 'Al-Baqarah: 61' },
        { text: 'هُمَزَةٍ', ref: 'Al-Humazah: 1' },
        { text: 'صُمٌّ', ref: 'Al-Baqarah: 18' }
    ],
    comparison: [
        { text: 'أَنْعَمْتَ', ref: 'Al-Fatiha: 7' },
        { text: 'مَنْ', ref: 'Al-Baqarah: 62' },
        { text: 'مِنْ', ref: 'Ibrahim: 26' },
        { text: 'خَيْرٍ', ref: 'Al-Baqarah: 110' }
    ]
};

// --- Module 9: Alif Lam Quiz ---
export const alifLamQuiz = [
    // Qamariyah
    { example: 'اَلْقَمَرُ', arabicText: 'القَمَر', pronunciation: 'al-qomaru', answer: 'Qamariyah' },
    { example: 'اَلْجَنَّةُ', arabicText: 'الجَنَّة', pronunciation: 'al-jannatu', answer: 'Qamariyah' },
    { example: 'اَلْفَجْرِ', arabicText: 'الفَجر', pronunciation: 'al-fajri', answer: 'Qamariyah' },
    { example: 'اَلْخَيْرُ', arabicText: 'الخَير', pronunciation: 'al-khoiru', answer: 'Qamariyah' },
    { example: 'اَلْكِتَابُ', arabicText: 'الكِتَاب', pronunciation: 'al-kitaabu', answer: 'Qamariyah' },
    // ... more Qamariyah
    { example: 'اَلْحَمْدُ', arabicText: 'الحَمد', pronunciation: 'al-hamdu', answer: 'Qamariyah' },
    { example: 'اَلْعَالَمِيْنَ', arabicText: 'العَالَمِين', pronunciation: 'al-ʿaalamiin', answer: 'Qamariyah' },
    { example: 'اَلْمَلِكُ', arabicText: 'المَلِك', pronunciation: 'al-maliku', answer: 'Qamariyah' },
    { example: 'اَلْغَفُوْرُ', arabicText: 'الغَفُور', pronunciation: 'al-ghofuuru', answer: 'Qamariyah' },
    { example: 'اَلْبَصِيْرُ', arabicText: 'البَصِير', pronunciation: 'al-bashiiru', answer: 'Qamariyah' },

    // Syamsiyah
    { example: 'اَلشَّمْسُ', arabicText: 'الشَّمس', pronunciation: 'ash-shamsu', answer: 'Syamsiyah' },
    { example: 'اَلرَّحْمٰنُ', arabicText: 'الرَّحمَن', pronunciation: 'ar-rahmaanu', answer: 'Syamsiyah' },
    { example: 'اَلنَّاسُ', arabicText: 'النَّاس', pronunciation: 'an-naasu', answer: 'Syamsiyah' },
    { example: 'اَلضُّحٰى', arabicText: 'الضُّحَى', pronunciation: 'ad-duhaa', answer: 'Syamsiyah' },
    { example: 'اَلتَّوَّابُ', arabicText: 'التَّوَّاب', pronunciation: 'at-tawwaabu', answer: 'Syamsiyah' },
    // ... more Syamsiyah
    { example: 'اَلذِّكْرُ', arabicText: 'الذِّكر', pronunciation: 'adh-dhikru', answer: 'Syamsiyah' },
    { example: 'اَلسَّلَامُ', arabicText: 'السَّلَام', pronunciation: 'as-salaamu', answer: 'Syamsiyah' },
    { example: 'اَلصَّمَدُ', arabicText: 'الصَّمَد', pronunciation: 'as-samadu', answer: 'Syamsiyah' },
    { example: 'اَلظَّالِمِيْنَ', arabicText: 'الظَّالِمِين', pronunciation: 'adh-dhaalimiin', answer: 'Syamsiyah' },
    { example: 'اَلطَّيِّبَاتُ', arabicText: 'الطَّيِّبَات', pronunciation: 'at-tayyibaatu', answer: 'Syamsiyah' }
];

// --- Module 10: Waqaf Quiz ---
export const waqafQuiz = [
    { sign: 'مـ', name: 'Mim - Waqaf Lazim', explanationArab: 'مِيمٌ. وَقْفٌ لَازِمٌ', correctAnswer: 'Wajib berhenti', incorrectAnswers: ['Boleh berhenti atau lanjut', 'Tidak boleh berhenti', 'Lebih baik lanjut'] },
    { sign: 'لا', name: 'La - Waqaf Mamnu', explanationArab: 'لَا تَقِفْ. لَا يَجُوزُ الْوَقْفُ', correctAnswer: 'Tidak boleh berhenti', incorrectAnswers: ['Wajib berhenti', 'Boleh berhenti atau lanjut', 'Lebih baik berhenti'] },
    { sign: 'ج', name: 'Jim - Waqaf Jaiz', explanationArab: 'جِيمٌ. وَقْفٌ جَائِزٌ', correctAnswer: 'Boleh berhenti atau lanjut, sama-sama', incorrectAnswers: ['Wajib berhenti', 'Tidak boleh berhenti', 'Lebih baik berhenti'] },
    { sign: 'صلى', name: 'Shola - Washlu Aula', explanationArab: 'صَلَّى. اَلْوَصْلُ أَوْلَى', correctAnswer: 'Lanjut lebih utama dari berhenti', incorrectAnswers: ['Wajib berhenti', 'Tidak boleh berhenti', 'Wajib lanjut'] },
    { sign: 'قلى', name: 'Qola - Waqfu Aula', explanationArab: 'قَلَى. اَلْوَقْفُ أَوْلَى', correctAnswer: 'Berhenti lebih utama dari lanjut', incorrectAnswers: ['Wajib berhenti', 'Tidak boleh berhenti', 'Wajib lanjut'] },
    { sign: 'قف', name: 'Qif - Waqaf Mustahab', explanationArab: 'قِفْ. يُسْتَحَبُّ الْوَقْفُ', correctAnswer: 'Disunnahkan berhenti', incorrectAnswers: ['Wajib berhenti', 'Tidak boleh berhenti', 'Wajib lanjut'] },
    { sign: 'صل', name: 'Shil - Washlu Mustahab', explanationArab: 'صِلْ. يُسْتَحَبُّ الْوَصْلُ', correctAnswer: 'Disunnahkan lanjut terus', incorrectAnswers: ['Wajib berhenti', 'Tidak boleh lanjut', 'Wajib lanjut'] },
    { sign: '۝', name: 'Tanda Akhir Ayat', explanationArab: 'رَقْمُ الْآيَةِ', correctAnswer: 'Tanda akhir ayat, disunnahkan berhenti', incorrectAnswers: ['Wajib berhenti', 'Tidak boleh berhenti', 'Tanda awal ayat'] },
    { sign: 'س', name: 'Sin - Saktah', explanationArab: 'سِينٌ. سَكْتَةٌ', correctAnswer: 'Diam sebentar tanpa napas lalu lanjut', incorrectAnswers: ['Berhenti dengan napas', 'Tidak boleh berhenti', 'Lanjut tanpa jeda'] },
    { sign: '⋮', name: 'Waqaf Muanaqah', explanationArab: 'وَقْفُ الْمُعَانَقَةِ', correctAnswer: 'Berhenti di salah satu, bukan keduanya', incorrectAnswers: ['Berhenti di keduanya', 'Tidak boleh berhenti', 'Lanjut semua'] }
];

// --- Module 11: Latihan Waqaf (Practice) ---
export const waqafPracticeData = {
    'alhamd': { text: 'ٱلْحَمْدُ', arabic: 'الحمد', normal: 'al-ḥamdu', waqaf: 'al-ḥamd', category: 'sukun' },
    'nastaiin': { text: 'نَسْتَعِينُ', arabic: 'نستعين', normal: "nasta'īnu", waqaf: "nasta'īn", category: 'sukun' },
    'aliimaa': { text: 'عَلِيمًا', arabic: 'عليما', normal: "'alīman", waqaf: "'alīmā", category: 'mad' },
    'hudaa': { text: 'هُدًى', arabic: 'هدى', normal: "hudan", waqaf: "hudā", category: 'mad' },
    'alqoriah': { text: 'ٱلْقَارِعَةُ', arabic: 'القارعة', normal: "al-qāri'atu", waqaf: "al-qāri'ah", category: 'marbutah' },
    'ahad': { text: 'أَحَدٌ', arabic: 'أحد', normal: "aḥadun", waqaf: "aḥad (qalqalah)", category: 'qalqalah' },
    'almudassir': { text: 'ٱلْمُدَّثِّرُ', arabic: 'المدثر', normal: "al-muddaṡṡiru", waqaf: "al-muddaṡṡir", category: 'qalqalah' },
    'arrohiim': { text: 'ٱلرَّحِيمِ', arabic: 'الرحيم', normal: "ar-raḥīmi", waqaf: "ar-raḥīm", category: 'mad_arid' },
    'khouf': { text: 'خَوْفٌ', arabic: 'خوف', normal: "khaufun", waqaf: "khauf", category: 'mad_layyin' },
    'bismillahir': { text: 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ', arabic: 'بسم الله الرحمن', normal: "Waqaf setelah Allah", waqaf: "Lanjut: ar-raḥmāni", category: 'hamzah_washal' }
};

// --- Module 12: Muqatta'ah ---
export const muqattaahData = [
    { letters: 'ا ل م', text: 'الم', transliteration: 'Alif Lām Mīm', info: '6 Surah' },
    { letters: 'ا ل م ص', text: 'المص', transliteration: 'Alif Lām Mīm Ṣād', info: '1 Surah' },
    { letters: 'ا ل ر', text: 'الر', transliteration: 'Alif Lām Rā', info: '5 Surah' },
    { letters: 'ا ل م ر', text: 'المر', transliteration: 'Alif Lām Mīm Rā', info: '1 Surah' },
    { letters: 'ك ه ي ع ص', text: 'كهيعص', transliteration: 'Kāf Hā Yā \'Ain Ṣād', info: '1 Surah' },
    { letters: 'ط ه', text: 'طه', transliteration: 'Ṭā Hā', info: '1 Surah' },
    { letters: 'ط س م', text: 'طسم', transliteration: 'Ṭā Sīn Mīm', info: '2 Surah' },
    { letters: 'ط س', text: 'طس', transliteration: 'Ṭā Sīn', info: '1 Surah' },
    { letters: 'ي س', text: 'يس', transliteration: 'Yā Sīn', info: '1 Surah' },
    { letters: 'ص', text: 'ص', transliteration: 'Ṣād', info: '1 Surah' },
    { letters: 'ح م', text: 'حم', transliteration: 'Ḥā Mīm', info: '7 Surah' },
    { letters: 'ح م ع س ق', text: 'حمعسق', transliteration: 'Ḥā Mīm \'Ain Sīn Qāf', info: '1 Surah' },
    { letters: 'ق', text: 'ق', transliteration: 'Qāf', info: '1 Surah' },
    { letters: 'ن', text: 'ن', transliteration: 'Nūn', info: '1 Surah' }
];

export const muqattaahPractice = {
    single: [
        { letters: 'ا', text: 'ا', name: 'Alif' }, { letters: 'ل', text: 'ل', name: 'Lām' },
        { letters: 'م', text: 'م', name: 'Mīm' }, { letters: 'ص', text: 'ص', name: 'Ṣād' },
        { letters: 'ر', text: 'ر', name: 'Rā' }, { letters: 'ك', text: 'ك', name: 'Kāf' },
        { letters: 'ه', text: 'ه', name: 'Hā' }, { letters: 'ي', text: 'ي', name: 'Yā' },
        { letters: 'ع', text: 'ع', name: '\'Ain' }, { letters: 'ط', text: 'ط', name: 'Ṭā' },
        { letters: 'س', text: 'س', name: 'Sīn' }, { letters: 'ح', text: 'ح', name: 'Ḥā' },
        { letters: 'ق', text: 'ق', name: 'Qāf' }, { letters: 'ن', text: 'ن', name: 'Nūn' }
    ]
};

export const level3Data = {
    // Module 13: Nun Sukun & Tanwin
    nunSukunQuiz: [
        { example: 'مِنْهُمْ', question: 'Nun Sukun (نْ) bertemu هـ (Ha)', arabicText: 'منهم', answer: 'Izhar' },
        { example: 'اَنْعَمْتَ', question: 'Nun Sukun (نْ) bertemu ع (Ain)', arabicText: 'أنعمت', answer: 'Izhar' },
        { example: 'مَنْ ءَامَنَ', question: 'Nun Sukun (نْ) bertemu ء (Hamzah)', arabicText: 'من آمن', answer: 'Izhar' },
        { example: 'مَنْ يَّعْمَلْ', question: 'Nun Sukun (نْ) bertemu ي (Ya)', arabicText: 'من يعمل', answer: 'Idgham Bighunnah' },
        { example: 'مِنْ وَّاقٍ', question: 'Nun Sukun (نْ) bertemu و (Waw)', arabicText: 'من واق', answer: 'Idgham Bighunnah' },
        { example: 'مِنْ مَّالٍ', question: 'Nun Sukun (نْ) bertemu م (Mim)', arabicText: 'من مال', answer: 'Idgham Bighunnah' },
        { example: 'مِنْ لَّدُنْهُ', question: 'Nun Sukun (نْ) bertemu ل (Lam)', arabicText: 'من لدنه', answer: 'Idgham Bilaghunnah' },
        { example: 'مِنْ رَّبِّهِمْ', question: 'Nun Sukun (نْ) bertemu ر (Ra)', arabicText: 'من ربهم', answer: 'Idgham Bilaghunnah' },
        { example: 'اَنْۢبِئْهُمْ', question: 'Nun Sukun (نْ) bertemu ب (Ba)', arabicText: 'أنبئهم', answer: 'Iqlab' },
        { example: 'مِنْۢ بَعْدِ', question: 'Nun Sukun (نْ) bertemu ب (Ba)', arabicText: 'من بعد', answer: 'Iqlab' },
        { example: 'اَنْ صَدُّوْكُمْ', question: 'Nun Sukun (نْ) bertemu ص (Shad)', arabicText: 'أن صدوكم', answer: 'Ikhfa' },
        { example: 'مَنْ ذَا', question: 'Nun Sukun (نْ) bertemu ذ (Dzal)', arabicText: 'من ذا', answer: 'Ikhfa' },
        { example: 'يَنْقَلِبُ', question: 'Nun Sukun (نْ) bertemu ق (Qaf)', arabicText: 'ينقلب', answer: 'Ikhfa' },
        { example: 'اَنْ تَزُوْلَا', question: 'Nun Sukun (نْ) bertemu ت (Ta)', arabicText: 'أن تزولا', answer: 'Ikhfa' },
        { example: 'مِنْ كُلِّ', question: 'Nun Sukun (نْ) bertemu ك (Kaf)', arabicText: 'من كل', answer: 'Ikhfa' }
    ],

    // Module 14: Mim Sukun
    mimSukunQuiz: [
        { example: 'تَرْمِيهِمْ بِحِجَارَةٍ', question: 'Mim Sukun (مْ) bertemu ب (Ba)', arabicText: 'ترميهم بحجارة', answer: 'Ikhfa Syafawi' },
        { example: 'وَمَا هُمْ بِمُؤْمِنِينَ', question: 'Mim Sukun (مْ) bertemu ب (Ba)', arabicText: 'وما هم بمؤمنين', answer: 'Ikhfa Syafawi' },
        { example: 'لَهُمْ مَّا يَشَاءُونَ', question: 'Mim Sukun (مْ) bertemu م (Mim)', arabicText: 'لهم ما يشاءون', answer: 'Idgham Syafawi' },
        { example: 'كَمْ مِّن فِئَةٍ', question: 'Mim Sukun (مْ) bertemu م (Mim)', arabicText: 'كم من فئة', answer: 'Idgham Syafawi' },
        { example: 'عَلَيْهِمْ وَلَا', question: 'Mim Sukun (مْ) bertemu و (Waw)', arabicText: 'عليهم ولا', answer: 'Izhar Syafawi' },
        { example: 'أَنْعَمْتَ عَلَيْهِمْ', question: 'Mim Sukun (مْ) bertemu ع (Ain)', arabicText: 'أنعمت عليهم', answer: 'Izhar Syafawi' },
        { example: 'هُمْ فِيهَا', question: 'Mim Sukun (مْ) bertemu ف (Fa)', arabicText: 'هم فيها', answer: 'Izhar Syafawi' }
    ],

    // Module 15: Ra Tafkhim & Tarqiq
    raTafkhimTarqiq: [
        { example: 'رَسُوْلٌ', arabicText: 'رسول', answer: 'Tafkhim' },
        { example: 'اَلرَّحْمٰنُ', arabicText: 'الرحمن', answer: 'Tafkhim' },
        { example: 'خَبِيْرًا', arabicText: 'خبيرا', answer: 'Tafkhim' },
        { example: 'رُزِقُوْا', arabicText: 'رزقوا', answer: 'Tafkhim' },
        { example: 'نَذِيْرًا', arabicText: 'نذيرا', answer: 'Tafkhim' },
        { example: 'غَفُوْرٌ', arabicText: 'غفور', answer: 'Tafkhim' },
        { example: 'رِجَالٌ', arabicText: 'رجال', answer: 'Tarqiq' },
        { example: 'قَدِيْرٌ', arabicText: 'قدير', answer: 'Tarqiq' },
        { example: 'فِرْعَوْنَ', arabicText: 'فرعون', answer: 'Tarqiq' },
        { example: 'خَبِيْرٌ', arabicText: 'خبير', answer: 'Tarqiq' },
        { example: 'بَصِيْرٌ', arabicText: 'بصير', answer: 'Tarqiq' },
        { example: 'الْفَقِيْرُ', arabicText: 'الفقير', answer: 'Tarqiq' }
    ],

    // Module 16: Lam Jalalah
    lamJalalah: [
        { example: 'هُوَ اللهُ', arabicText: 'هو الله', answer: 'Tafkhim', question: 'Huruf sebelum "الله" berharakat fathah' },
        { example: 'عَبْدُ اللهِ', arabicText: 'عبد الله', answer: 'Tafkhim', question: 'Huruf sebelum "الله" berharakat dhammah' },
        { example: 'قُلْ هُوَ اللهُ اَحَدٌ', arabicText: 'قل هو الله أحد', answer: 'Tafkhim', question: 'Huruf sebelum "الله" berharakat fathah' },
        { example: 'بِسْمِ اللهِ', arabicText: 'بسم الله', answer: 'Tarqiq', question: 'Huruf sebelum "الله" berharakat kasrah' },
        { example: 'لِلّٰهِ', arabicText: 'لله', answer: 'Tarqiq', question: 'Huruf sebelum "الله" berharakat kasrah' },
        { example: 'اَلْحَمْدُ لِلّٰهِ', arabicText: 'الحمد لله', answer: 'Tarqiq', question: 'Huruf sebelum "الله" berharakat kasrah' }
    ],

    // Module 19: Arena Tajwid (Drag & Drop)
    tajwidDragDrop: [
        { example: 'مِنْهُمْ', arabicText: 'منهم', answer: 'Izhar' },
        { example: 'اَنْعَمْتَ', arabicText: 'أنعمت', answer: 'Izhar' },
        { example: 'مِنْ قَبْلِ', arabicText: 'من قبل', answer: 'Ikhfa' },
        { example: 'اَنْتُمْ', arabicText: 'أنتم', answer: 'Ikhfa' },
        { example: 'مَنْ يَّعْمَلْ', arabicText: 'من يعمل', answer: 'Idgham' },
        { example: 'مِنْ لَّدُنْهُ', arabicText: 'من لدنه', answer: 'Idgham' },
        { example: 'مِنْۢ بَعْدِ', arabicText: 'من بعد', answer: 'Iqlab' },
        { example: 'سَمِيْعًا بَصِيْرًا', arabicText: 'سميعا بصيرا', answer: 'Iqlab' },
        { example: 'عَلِيْمٌ حَكِيْمٌ', arabicText: 'عليم حكيم', answer: 'Izhar' },
        { example: 'مِنْ شَرِّ', arabicText: 'من شر', answer: 'Ikhfa' },
        { example: 'مِنْ رَّبِّهِمْ', arabicText: 'من ربهم', answer: 'Idgham' },
        { example: 'بِرِيْحٍ صَرْصَرٍ', arabicText: 'بريح صرصر', answer: 'Ikhfa' },
        { example: 'ٱلْحَمْدُ', arabicText: 'الحمد', answer: 'Izhar' },
        { example: 'نَسْتَعِينُ', arabicText: 'نستعين', answer: 'Izhar' },
        { example: 'عَلِيمًا', arabicText: 'عليما', answer: 'Iqlab' },
        { example: 'هُدًى', arabicText: 'هدى', answer: 'Idgham' },
        { example: 'ٱلْقَارِعَةُ', arabicText: 'القارعة', answer: 'Ikhfa' },
        { example: 'جَنَّةٍ', arabicText: 'جنة', answer: 'Ikhfa' },
        { example: 'أَحَدٌ', arabicText: 'أحد', answer: 'Izhar' },
        { example: 'ٱلْفَلَقِ', arabicText: 'الفلق', answer: 'Ikhfa' }
    ],

    // Module 20: Tebak Cepat (Mega Quiz)
    tajwidSpeedQuiz: [
        { example: 'مِنْهُمْ', arabicText: 'منهم', answer: 'Izhar' },
        { example: 'اَنْعَمْتَ', arabicText: 'أنعمت', answer: 'Izhar' },
        { example: 'مِنْ قَبْلِ', arabicText: 'من قبل', answer: 'Ikhfa' },
        { example: 'اَنْتُمْ', arabicText: 'أنتم', answer: 'Ikhfa' },
        { example: 'مَنْ يَّعْمَلْ', arabicText: 'من يعمل', answer: 'Idgham' },
        { example: 'مِنْ لَّدُنْهُ', arabicText: 'من لدنه', answer: 'Idgham' },
        { example: 'مِنْۢ بَعْدِ', arabicText: 'من بعد', answer: 'Iqlab' },
        { example: 'تَرْمِيْهِمْ بِحِجَارَةٍ', arabicText: 'ترميهم بحجارة', answer: 'Ikhfa Syafawi' },
        { example: 'اَمْ مَنْ', arabicText: 'أم من', answer: 'Idgham Mitslain' },
        { example: 'لَهُمْ فِيْهَا', arabicText: 'لهم فيها', answer: 'Izhar Syafawi' },
        { example: 'قَالَ', arabicText: 'قال', answer: 'Mad Thabi\'i' },
        { example: 'يُؤْمِنُونَ', arabicText: 'يؤمنون', answer: 'Mad Wajib' },
        { example: 'مَآءً', arabicText: 'ماء', answer: 'Mad Jaiz' },
        { example: 'ءَامَنَّا', arabicText: 'آمنا', answer: 'Mad Lazim' },
        { example: 'اَحَدٌ', arabicText: 'أحد', answer: 'Qalqalah' },
        { example: 'يَكْتُبُونَ', arabicText: 'يكتبون', answer: 'Qalqalah' },
        { example: 'الشَّمْسُ', arabicText: 'الشمس', answer: 'Lam Syamsiyah' },
        { example: 'الْقَمَرُ', arabicText: 'القمر', answer: 'Lam Qomariyah' },
        { example: 'رَبِّ', arabicText: 'رب', answer: 'Ra Tafkhim' },
        { example: 'فِرْعَوْنَ', arabicText: 'فرعون', answer: 'Ra Tarqiq' }
    ],

    // Module 17: Waqaf Advanced
    waqafQuizAdvanced: [
        { word: 'ٱلْحَمْدُ', stoppedWord: 'ٱلْحَمْدْ', arabicText: 'الحمد', wrongOptions: ['ٱلْحَمْدَا', 'ٱلْحَمْدَهْ'] },
        { word: 'نَسْتَعِينُ', stoppedWord: 'نَسْتَعِينْ', arabicText: 'نستعين', wrongOptions: ['نَسْتَعِينَا', 'نَسْتَعِينَهْ'] },
        { word: 'عَلِيمًا', stoppedWord: 'عَلِيمَا', arabicText: 'عليما', wrongOptions: ['عَلِيمْ', 'عَلِيمَهْ'] },
        { word: 'هُدًى', stoppedWord: 'هُدَا', arabicText: 'هدى', wrongOptions: ['هُدْ', 'هُدَهْ'] },
        { word: 'ٱلْقَارِعَةُ', stoppedWord: 'ٱلْقَارِعَهْ', arabicText: 'القارعة', wrongOptions: ['ٱلْقَارِعَتْ', 'ٱلْقَارِعَا'] },
        { word: 'جَنَّةٍ', stoppedWord: 'جَنَّهْ', arabicText: 'جنة', wrongOptions: ['جَنَّتْ', 'جَنَّا'] },
        { word: 'أَحَدٌ', stoppedWord: 'أَحَدْ', arabicText: 'أحد', wrongOptions: ['أَحَدَا', 'أَحَدَهْ'] },
        { word: 'ٱلْفَلَقِ', stoppedWord: 'ٱلْفَلَقْ', arabicText: 'الفلق', wrongOptions: ['ٱلْفَلَقَا', 'ٱلْفَلَقَهْ'] },
        { word: 'ٱلرَّحِيمِ', stoppedWord: 'ٱلرَّحِيمْ', arabicText: 'الرحيم', wrongOptions: ['ٱلرَّحِيمَا', 'ٱلرَّحِيمَهْ'] },
        { word: 'يُؤْمِنُونَ', stoppedWord: 'يُؤْمِنُونْ', arabicText: 'يؤمنون', wrongOptions: ['يُؤْمِنُونَا', 'يُؤْمِنُونَهْ'] },
        { word: 'خَوْفٌ', stoppedWord: 'خَوْفْ', arabicText: 'خوف', wrongOptions: ['خَوْفَا', 'خَوْفَهْ'] },
        { word: 'ٱلْبَيْتِ', stoppedWord: 'ٱلْبَيْتْ', arabicText: 'البيت', wrongOptions: ['ٱلْبَيْتَا', 'ٱلْبَيْتَهْ'] }
    ],

    // Module 18: Mad Tambahan
    madTambahanQuiz: [
        { example: 'خَوْفٌ', note: '(saat waqaf)', arabicText: 'خوف', answer: 'Mad Layyin' },
        { example: 'قُرَيْشٍ', note: '(saat waqaf)', arabicText: 'قريش', answer: 'Mad Layyin' },
        { example: 'جَاءَ', note: '', arabicText: 'جاء', answer: 'Mad Wajib Muttasil' },
        { example: 'السَّمَاءِ', note: '', arabicText: 'السماء', answer: 'Mad Wajib Muttasil' },
        { example: 'يَا أَيُّهَا', note: '', arabicText: 'يا أيها', answer: 'Mad Jaiz Munfasil' },
        { example: 'قَالُوا آمَنَّا', note: '', arabicText: 'قالوا آمنا', answer: 'Mad Jaiz Munfasil' },
        { example: 'قَالَ', note: '', arabicText: 'قال', answer: 'Mad Thabi\'i' },
        { example: 'يَقُولُ', note: '', arabicText: 'يقول', answer: 'Mad Thabi\'i' }
    ]
};



// --- EXTRA JILID & LEVEL METADATA ---
export const JILID_META = {
  '1': { arabic:'اَ–خَ', title:'Jilid 1 — Alif s/d Kha', desc:'Huruf-huruf dasar hijaiyah pertama', levels:['1A','1B','1C'] },
  '2': { arabic:'حَ–ضَ', title:'Jilid 2 — Ha s/d Dhad',  desc:'Lanjutan pengenalan huruf hijaiyah',  levels:['2A','2B','2C'] },
  '3': { arabic:'طَ–مَ', title:'Jilid 3 — Tha s/d Mim',  desc:'Melengkapi seluruh huruf hijaiyah',   levels:['3A','3B','3C'] },
  '4': { arabic:'بَبِبُ', title:'Jilid 4 — Harakat',       desc:'Fathah, Kasrah dan Dhammah',         levels:['4A','4B','4C'] },
  '5': { arabic:'بًبْ',  title:'Jilid 5 — Tanwin & Sukun',desc:'Tanwin dan huruf bersukun',           levels:['5A','5B','5C'] },
  '6': { arabic:'بَّ آ', title:'Jilid 6 — Tasydid & Mad', desc:'Tasydid dan bacaan panjang (mad)',    levels:['6A','6B','6C'] },
};
export const CARD_META = {
  '1A':{ arabic:'اَ بَ',   name:'Ummi 1A', sub:'Alif & Ba',               jilid:'1', jclass:'j1' },
  '1B':{ arabic:'بَ تَ ثَ',name:'Ummi 1B', sub:'Ba, Ta & Tsa',            jilid:'1', jclass:'j1' },
  '1C':{ arabic:'ثَ جَ',   name:'Ummi 1C', sub:'Tsa & Ja',                jilid:'1', jclass:'j1' },
  '2A':{ arabic:'حَ دَ ذَ',name:'Ummi 2A', sub:'Ha, Dal & Dzal',          jilid:'2', jclass:'j2' },
  '2B':{ arabic:'رَ زَ سَ',name:'Ummi 2B', sub:'Ra, Zai & Sin',           jilid:'2', jclass:'j2' },
  '2C':{ arabic:'شَ صَ ضَ',name:'Ummi 2C', sub:'Syin, Shad & Dhad',      jilid:'2', jclass:'j2' },
  '3A':{ arabic:'طَ ظَ عَ',name:'Ummi 3A', sub:'Tha, Zha & Ain',         jilid:'3', jclass:'j3' },
  '3B':{ arabic:'غَ فَ قَ',name:'Ummi 3B', sub:'Ghain, Fa & Qaf',        jilid:'3', jclass:'j3' },
  '3C':{ arabic:'كَ لَ مَ',name:'Ummi 3C', sub:'Kaf, Lam & Mim',         jilid:'3', jclass:'j3' },
  '4A':{ arabic:'بَ بِ بُ',name:'Ummi 4A', sub:'Fathah, Kasrah & Dhammah',jilid:'4', jclass:'j4' },
  '4B':{ arabic:'نَ نِ نُ',name:'Ummi 4B', sub:'Nun dengan Harakat',      jilid:'4', jclass:'j4' },
  '4C':{ arabic:'لَ لِ لُ',name:'Ummi 4C', sub:'Lam dengan Harakat',      jilid:'4', jclass:'j4' },
  '5A':{ arabic:'بً بٍ بٌ',name:'Ummi 5A', sub:'Tanwin Fathah, Kasrah & Dhammah',jilid:'5',jclass:'j5'},
  '5B':{ arabic:'بْ دْ رْ',name:'Ummi 5B', sub:'Huruf Bersukun',          jilid:'5', jclass:'j5' },
  '5C':{ arabic:'مَنْ مِنْ',name:'Ummi 5C', sub:'Gabungan Sukun & Harakat',jilid:'5',jclass:'j5'},
  '6A':{ arabic:'بَّ دَّ', name:'Ummi 6A', sub:'Huruf Bertasydid',        jilid:'6', jclass:'j6' },
  '6B':{ arabic:'بَا دِي', name:'Ummi 6B', sub:"Mad Thabi'i (2 Harakat)", jilid:'6', jclass:'j6' },
  '6C':{ arabic:'آ ءَا',   name:'Ummi 6C', sub:"Mad Wajib & Lazim",       jilid:'6', jclass:'j6' },
};

export const LEVELS = {
  '1A':{ title:'Ummi 1A', sub:'Pengenalan Huruf: Alif & Ba (اَ , بَ)', next:'1B', prev:null,
    questions:[
      {arabic:'اَ',latin:'alif (a)',answer:'اَ',options:['اَ','بَ','تَ','ثَ','جَ','حَ']},
      {arabic:'بَ',latin:'ba (ba)',answer:'بَ',options:['اَ','بَ','تَ','ثَ','جَ','حَ']},
      {arabic:'اَ',latin:'alif (a)',answer:'اَ',options:['تَ','اَ','جَ','ثَ','حَ','بَ']},
      {arabic:'بَ',latin:'ba (ba)',answer:'بَ',options:['حَ','جَ','بَ','ثَ','تَ','اَ']},
      {arabic:'اَ',latin:'alif (a)',answer:'اَ',options:['جَ','حَ','ثَ','تَ','بَ','اَ']},
      {arabic:'بَ',latin:'ba (ba)',answer:'بَ',options:['اَ','بَ','حَ','جَ','ثَ','تَ']},
      {arabic:'اَ',latin:'alif (a)',answer:'اَ',options:['بَ','اَ','تَ','ثَ','جَ','حَ']},
      {arabic:'بَ',latin:'ba (ba)',answer:'بَ',options:['تَ','ثَ','جَ','حَ','اَ','بَ']},
      {arabic:'اَ',latin:'alif (a)',answer:'اَ',options:['حَ','جَ','ثَ','تَ','اَ','بَ']},
      {arabic:'بَ',latin:'ba (ba)',answer:'بَ',options:['اَ','تَ','ثَ','بَ','جَ','حَ']},
    ]},
  '1B':{ title:'Ummi 1B', sub:'Pengenalan Huruf: Ba, Ta & Tsa (بَ , تَ , ثَ)', next:'1C', prev:'1A',
    questions:[
      {arabic:'بَ',latin:'ba',answer:'بَ',options:['بَ','تَ','ثَ','جَ','حَ','خَ']},
      {arabic:'تَ',latin:'ta',answer:'تَ',options:['بَ','تَ','ثَ','جَ','حَ','خَ']},
      {arabic:'ثَ',latin:'tsa',answer:'ثَ',options:['بَ','تَ','ثَ','جَ','حَ','خَ']},
      {arabic:'تَ',latin:'ta',answer:'تَ',options:['خَ','حَ','جَ','ثَ','تَ','بَ']},
      {arabic:'بَ',latin:'ba',answer:'بَ',options:['ثَ','جَ','حَ','بَ','خَ','تَ']},
      {arabic:'ثَ',latin:'tsa',answer:'ثَ',options:['بَ','تَ','ثَ','خَ','حَ','جَ']},
      {arabic:'تَ',latin:'ta',answer:'تَ',options:['جَ','حَ','تَ','ثَ','بَ','خَ']},
      {arabic:'بَ',latin:'ba',answer:'بَ',options:['خَ','بَ','جَ','حَ','ثَ','تَ']},
      {arabic:'ثَ',latin:'tsa',answer:'ثَ',options:['تَ','بَ','ثَ','جَ','حَ','خَ']},
      {arabic:'تَ',latin:'ta',answer:'تَ',options:['بَ','جَ','حَ','خَ','تَ','ثَ']},
    ]},
  '1C':{ title:'Ummi 1C', sub:'Pengenalan Huruf: Tsa & Ja (ثَ , جَ)', next:'2A', prev:'1B',
    questions:[
      {arabic:'ثَ',latin:'tsa',answer:'ثَ',options:['ثَ','جَ','حَ','خَ','دَ','ذَ']},
      {arabic:'جَ',latin:'ja',answer:'جَ',options:['ثَ','جَ','حَ','خَ','دَ','ذَ']},
      {arabic:'ثَ',latin:'tsa',answer:'ثَ',options:['ذَ','دَ','خَ','حَ','جَ','ثَ']},
      {arabic:'جَ',latin:'ja',answer:'جَ',options:['حَ','ثَ','جَ','خَ','دَ','ذَ']},
      {arabic:'ثَ',latin:'tsa',answer:'ثَ',options:['جَ','حَ','ثَ','خَ','ذَ','دَ']},
      {arabic:'جَ',latin:'ja',answer:'جَ',options:['ثَ','دَ','خَ','جَ','حَ','ذَ']},
      {arabic:'ثَ',latin:'tsa',answer:'ثَ',options:['خَ','ثَ','جَ','حَ','دَ','ذَ']},
      {arabic:'جَ',latin:'ja',answer:'جَ',options:['دَ','ذَ','ثَ','جَ','حَ','خَ']},
      {arabic:'ثَ',latin:'tsa',answer:'ثَ',options:['جَ','ثَ','حَ','خَ','دَ','ذَ']},
      {arabic:'جَ',latin:'ja',answer:'جَ',options:['خَ','حَ','جَ','ثَ','ذَ','دَ']},
    ]},
  '2A':{ title:'Ummi 2A', sub:'Pengenalan Huruf: Ha, Dal & Dzal (حَ , دَ , ذَ)', next:'2B', prev:'1C',
    questions:[
      {arabic:'حَ',latin:'ha',answer:'حَ',options:['حَ','خَ','دَ','ذَ','رَ','زَ']},
      {arabic:'دَ',latin:'dal',answer:'دَ',options:['حَ','خَ','دَ','ذَ','رَ','زَ']},
      {arabic:'ذَ',latin:'dzal',answer:'ذَ',options:['حَ','خَ','دَ','ذَ','رَ','زَ']},
      {arabic:'حَ',latin:'ha',answer:'حَ',options:['زَ','رَ','ذَ','دَ','حَ','خَ']},
      {arabic:'دَ',latin:'dal',answer:'دَ',options:['خَ','حَ','ذَ','دَ','رَ','زَ']},
      {arabic:'ذَ',latin:'dzal',answer:'ذَ',options:['رَ','زَ','حَ','خَ','ذَ','دَ']},
      {arabic:'حَ',latin:'ha',answer:'حَ',options:['دَ','ذَ','حَ','خَ','رَ','زَ']},
      {arabic:'دَ',latin:'dal',answer:'دَ',options:['ذَ','رَ','زَ','دَ','حَ','خَ']},
      {arabic:'ذَ',latin:'dzal',answer:'ذَ',options:['خَ','حَ','رَ','زَ','دَ','ذَ']},
      {arabic:'حَ',latin:'ha',answer:'حَ',options:['دَ','زَ','ذَ','رَ','حَ','خَ']},
    ]},
  '2B':{ title:'Ummi 2B', sub:'Pengenalan Huruf: Ra, Zai & Sin (رَ , زَ , سَ)', next:'2C', prev:'2A',
    questions:[
      {arabic:'رَ',latin:'ra',answer:'رَ',options:['رَ','زَ','سَ','شَ','صَ','ضَ']},
      {arabic:'زَ',latin:'zai',answer:'زَ',options:['رَ','زَ','سَ','شَ','صَ','ضَ']},
      {arabic:'سَ',latin:'sin',answer:'سَ',options:['رَ','زَ','سَ','شَ','صَ','ضَ']},
      {arabic:'زَ',latin:'zai',answer:'زَ',options:['ضَ','صَ','شَ','سَ','زَ','رَ']},
      {arabic:'رَ',latin:'ra',answer:'رَ',options:['سَ','شَ','رَ','زَ','صَ','ضَ']},
      {arabic:'سَ',latin:'sin',answer:'سَ',options:['زَ','رَ','شَ','سَ','صَ','ضَ']},
      {arabic:'رَ',latin:'ra',answer:'رَ',options:['شَ','سَ','رَ','زَ','ضَ','صَ']},
      {arabic:'زَ',latin:'zai',answer:'زَ',options:['صَ','ضَ','زَ','رَ','سَ','شَ']},
      {arabic:'سَ',latin:'sin',answer:'سَ',options:['رَ','زَ','سَ','صَ','شَ','ضَ']},
      {arabic:'رَ',latin:'ra',answer:'رَ',options:['سَ','زَ','شَ','صَ','ضَ','رَ']},
    ]},
  '2C':{ title:'Ummi 2C', sub:'Pengenalan Huruf: Syin, Shad & Dhad (شَ , صَ , ضَ)', next:'3A', prev:'2B',
    questions:[
      {arabic:'شَ',latin:'syin',answer:'شَ',options:['شَ','صَ','ضَ','طَ','ظَ','عَ']},
      {arabic:'صَ',latin:'shad',answer:'صَ',options:['شَ','صَ','ضَ','طَ','ظَ','عَ']},
      {arabic:'ضَ',latin:'dhad',answer:'ضَ',options:['شَ','صَ','ضَ','طَ','ظَ','عَ']},
      {arabic:'صَ',latin:'shad',answer:'صَ',options:['عَ','ظَ','طَ','ضَ','صَ','شَ']},
      {arabic:'شَ',latin:'syin',answer:'شَ',options:['ضَ','صَ','شَ','طَ','ظَ','عَ']},
      {arabic:'ضَ',latin:'dhad',answer:'ضَ',options:['صَ','شَ','ضَ','عَ','ظَ','طَ']},
      {arabic:'شَ',latin:'syin',answer:'شَ',options:['طَ','ظَ','عَ','شَ','صَ','ضَ']},
      {arabic:'صَ',latin:'shad',answer:'صَ',options:['ضَ','طَ','صَ','شَ','ظَ','عَ']},
      {arabic:'ضَ',latin:'dhad',answer:'ضَ',options:['شَ','ضَ','صَ','عَ','طَ','ظَ']},
      {arabic:'شَ',latin:'syin',answer:'شَ',options:['صَ','ضَ','طَ','شَ','ظَ','عَ']},
    ]},
  '3A':{ title:'Ummi 3A', sub:'Pengenalan Huruf: Tha, Zha & Ain (طَ , ظَ , عَ)', next:'3B', prev:'2C',
    questions:[
      {arabic:'طَ',latin:'tha',answer:'طَ',options:['طَ','ظَ','عَ','غَ','فَ','قَ']},
      {arabic:'ظَ',latin:'zha',answer:'ظَ',options:['طَ','ظَ','عَ','غَ','فَ','قَ']},
      {arabic:'عَ',latin:'ain',answer:'عَ',options:['طَ','ظَ','عَ','غَ','فَ','قَ']},
      {arabic:'ظَ',latin:'zha',answer:'ظَ',options:['قَ','فَ','غَ','عَ','ظَ','طَ']},
      {arabic:'طَ',latin:'tha',answer:'طَ',options:['عَ','ظَ','طَ','غَ','فَ','قَ']},
      {arabic:'عَ',latin:'ain',answer:'عَ',options:['ظَ','طَ','غَ','عَ','فَ','قَ']},
      {arabic:'طَ',latin:'tha',answer:'طَ',options:['غَ','فَ','قَ','طَ','ظَ','عَ']},
      {arabic:'ظَ',latin:'zha',answer:'ظَ',options:['عَ','غَ','ظَ','طَ','فَ','قَ']},
      {arabic:'عَ',latin:'ain',answer:'عَ',options:['طَ','ظَ','عَ','قَ','فَ','غَ']},
      {arabic:'طَ',latin:'tha',answer:'طَ',options:['عَ','ظَ','غَ','فَ','قَ','طَ']},
    ]},
  '3B':{ title:'Ummi 3B', sub:'Pengenalan Huruf: Ghain, Fa & Qaf (غَ , فَ , قَ)', next:'3C', prev:'3A',
    questions:[
      {arabic:'غَ',latin:'ghain',answer:'غَ',options:['غَ','فَ','قَ','كَ','لَ','مَ']},
      {arabic:'فَ',latin:'fa',answer:'فَ',options:['غَ','فَ','قَ','كَ','لَ','مَ']},
      {arabic:'قَ',latin:'qaf',answer:'قَ',options:['غَ','فَ','قَ','كَ','لَ','مَ']},
      {arabic:'فَ',latin:'fa',answer:'فَ',options:['مَ','لَ','كَ','قَ','فَ','غَ']},
      {arabic:'غَ',latin:'ghain',answer:'غَ',options:['قَ','فَ','غَ','كَ','لَ','مَ']},
      {arabic:'قَ',latin:'qaf',answer:'قَ',options:['فَ','غَ','قَ','مَ','لَ','كَ']},
      {arabic:'غَ',latin:'ghain',answer:'غَ',options:['كَ','لَ','مَ','غَ','فَ','قَ']},
      {arabic:'فَ',latin:'fa',answer:'فَ',options:['قَ','كَ','فَ','غَ','لَ','مَ']},
      {arabic:'قَ',latin:'qaf',answer:'قَ',options:['غَ','فَ','قَ','مَ','كَ','لَ']},
      {arabic:'غَ',latin:'ghain',answer:'غَ',options:['فَ','قَ','كَ','غَ','مَ','لَ']},
    ]},
  '3C':{ title:'Ummi 3C', sub:'Pengenalan Huruf: Kaf, Lam & Mim (كَ , لَ , مَ)', next:'4A', prev:'3B',
    questions:[
      {arabic:'كَ',latin:'kaf',answer:'كَ',options:['كَ','لَ','مَ','نَ','وَ','هَ']},
      {arabic:'لَ',latin:'lam',answer:'لَ',options:['كَ','لَ','مَ','نَ','وَ','هَ']},
      {arabic:'مَ',latin:'mim',answer:'مَ',options:['كَ','لَ','مَ','نَ','وَ','هَ']},
      {arabic:'لَ',latin:'lam',answer:'لَ',options:['هَ','وَ','نَ','مَ','لَ','كَ']},
      {arabic:'كَ',latin:'kaf',answer:'كَ',options:['مَ','لَ','كَ','نَ','وَ','هَ']},
      {arabic:'مَ',latin:'mim',answer:'مَ',options:['لَ','كَ','مَ','هَ','وَ','نَ']},
      {arabic:'كَ',latin:'kaf',answer:'كَ',options:['نَ','وَ','هَ','كَ','لَ','مَ']},
      {arabic:'لَ',latin:'lam',answer:'لَ',options:['مَ','نَ','لَ','كَ','وَ','هَ']},
      {arabic:'مَ',latin:'mim',answer:'مَ',options:['كَ','لَ','مَ','هَ','نَ','وَ']},
      {arabic:'كَ',latin:'kaf',answer:'كَ',options:['لَ','مَ','نَ','كَ','هَ','وَ']},
    ]},
  '4A':{ title:'Ummi 4A', sub:'Harakat: Fathah, Kasrah & Dhammah (بَ بِ بُ)', next:'4B', prev:'3C',
    questions:[
      {arabic:'بَ',latin:'ba (fathah)',answer:'بَ',options:['بَ','بِ','بُ','تَ','تِ','تُ']},
      {arabic:'بِ',latin:'bi (kasrah)',answer:'بِ',options:['بَ','بِ','بُ','تَ','تِ','تُ']},
      {arabic:'بُ',latin:'bu (dhammah)',answer:'بُ',options:['بَ','بِ','بُ','تَ','تِ','تُ']},
      {arabic:'تَ',latin:'ta (fathah)',answer:'تَ',options:['تُ','تِ','تَ','بُ','بِ','بَ']},
      {arabic:'تِ',latin:'ti (kasrah)',answer:'تِ',options:['بَ','بِ','بُ','تَ','تِ','تُ']},
      {arabic:'تُ',latin:'tu (dhammah)',answer:'تُ',options:['تُ','تِ','تَ','بُ','بِ','بَ']},
      {arabic:'بَ',latin:'ba (fathah)',answer:'بَ',options:['تُ','تِ','تَ','بُ','بَ','بِ']},
      {arabic:'تِ',latin:'ti (kasrah)',answer:'تِ',options:['بَ','تِ','بِ','تَ','بُ','تُ']},
      {arabic:'بُ',latin:'bu (dhammah)',answer:'بُ',options:['تَ','تِ','بُ','تُ','بَ','بِ']},
      {arabic:'تَ',latin:'ta (fathah)',answer:'تَ',options:['بُ','بِ','تَ','تُ','تِ','بَ']},
    ]},
  '4B':{ title:'Ummi 4B', sub:'Nun dengan Harakat (نَ , نِ , نُ)', next:'4C', prev:'4A',
    questions:[
      {arabic:'نَ',latin:'na',answer:'نَ',options:['نَ','نِ','نُ','مَ','مِ','مُ']},
      {arabic:'نِ',latin:'ni',answer:'نِ',options:['نَ','نِ','نُ','مَ','مِ','مُ']},
      {arabic:'نُ',latin:'nu',answer:'نُ',options:['نَ','نِ','نُ','مَ','مِ','مُ']},
      {arabic:'مَ',latin:'ma',answer:'مَ',options:['مُ','مِ','مَ','نُ','نِ','نَ']},
      {arabic:'مِ',latin:'mi',answer:'مِ',options:['نَ','نِ','مَ','مِ','نُ','مُ']},
      {arabic:'مُ',latin:'mu',answer:'مُ',options:['مُ','مِ','مَ','نُ','نِ','نَ']},
      {arabic:'نَ',latin:'na',answer:'نَ',options:['مُ','مِ','مَ','نُ','نَ','نِ']},
      {arabic:'مِ',latin:'mi',answer:'مِ',options:['نَ','مِ','نِ','مَ','نُ','مُ']},
      {arabic:'نُ',latin:'nu',answer:'نُ',options:['مَ','مِ','نُ','مُ','نَ','نِ']},
      {arabic:'مَ',latin:'ma',answer:'مَ',options:['نُ','نِ','مَ','مُ','مِ','نَ']},
    ]},
  '4C':{ title:'Ummi 4C', sub:'Lam dengan Harakat (لَ , لِ , لُ)', next:'5A', prev:'4B',
    questions:[
      {arabic:'لَ',latin:'la',answer:'لَ',options:['لَ','لِ','لُ','كَ','كِ','كُ']},
      {arabic:'لِ',latin:'li',answer:'لِ',options:['لَ','لِ','لُ','كَ','كِ','كُ']},
      {arabic:'لُ',latin:'lu',answer:'لُ',options:['لَ','لِ','لُ','كَ','كِ','كُ']},
      {arabic:'كَ',latin:'ka',answer:'كَ',options:['كُ','كِ','كَ','لُ','لِ','لَ']},
      {arabic:'كِ',latin:'ki',answer:'كِ',options:['لَ','لِ','كَ','كِ','لُ','كُ']},
      {arabic:'كُ',latin:'ku',answer:'كُ',options:['كُ','كِ','كَ','لُ','لِ','لَ']},
      {arabic:'لَ',latin:'la',answer:'لَ',options:['كُ','كِ','كَ','لُ','لَ','لِ']},
      {arabic:'كِ',latin:'ki',answer:'كِ',options:['لَ','كِ','لِ','كَ','لُ','كُ']},
      {arabic:'لُ',latin:'lu',answer:'لُ',options:['كَ','كِ','لُ','كُ','لَ','لِ']},
      {arabic:'كَ',latin:'ka',answer:'كَ',options:['لُ','لِ','كَ','كُ','كِ','لَ']},
    ]},
  '5A':{ title:'Ummi 5A', sub:'Tanwin: Fathah, Kasrah & Dhammah (بً , بٍ , بٌ)', next:'5B', prev:'4C',
    questions:[
      {arabic:'بً',latin:'ban (tanwin fathah)',answer:'بً',options:['بً','بٍ','بٌ','تً','تٍ','تٌ']},
      {arabic:'بٍ',latin:'bin (tanwin kasrah)',answer:'بٍ',options:['بً','بٍ','بٌ','تً','تٍ','تٌ']},
      {arabic:'بٌ',latin:'bun (tanwin dhammah)',answer:'بٌ',options:['بً','بٍ','بٌ','تً','تٍ','تٌ']},
      {arabic:'تً',latin:'tan',answer:'تً',options:['تٌ','تٍ','تً','بٌ','بٍ','بً']},
      {arabic:'تٍ',latin:'tin',answer:'تٍ',options:['بً','بٍ','تً','تٍ','بٌ','تٌ']},
      {arabic:'تٌ',latin:'tun',answer:'تٌ',options:['تٌ','تٍ','تً','بٌ','بٍ','بً']},
      {arabic:'بً',latin:'ban',answer:'بً',options:['تٌ','تٍ','تً','بٌ','بً','بٍ']},
      {arabic:'تٍ',latin:'tin',answer:'تٍ',options:['بً','تٍ','بٍ','تً','بٌ','تٌ']},
      {arabic:'بٌ',latin:'bun',answer:'بٌ',options:['تً','تٍ','بٌ','تٌ','بً','بٍ']},
      {arabic:'تً',latin:'tan',answer:'تً',options:['بٌ','بٍ','تً','تٌ','تٍ','بً']},
    ]},
  '5B':{ title:'Ummi 5B', sub:'Huruf Bersukun (بْ , دْ , رْ)', next:'5C', prev:'5A',
    questions:[
      {arabic:'بْ',latin:'b (sukun)',answer:'بْ',options:['بْ','دْ','رْ','سْ','مْ','نْ']},
      {arabic:'دْ',latin:'d (sukun)',answer:'دْ',options:['بْ','دْ','رْ','سْ','مْ','نْ']},
      {arabic:'رْ',latin:'r (sukun)',answer:'رْ',options:['بْ','دْ','رْ','سْ','مْ','نْ']},
      {arabic:'سْ',latin:'s (sukun)',answer:'سْ',options:['نْ','مْ','سْ','رْ','دْ','بْ']},
      {arabic:'مْ',latin:'m (sukun)',answer:'مْ',options:['بْ','دْ','رْ','سْ','مْ','نْ']},
      {arabic:'نْ',latin:'n (sukun)',answer:'نْ',options:['نْ','مْ','سْ','رْ','دْ','بْ']},
      {arabic:'بْ',latin:'b (sukun)',answer:'بْ',options:['نْ','مْ','سْ','رْ','بْ','دْ']},
      {arabic:'مْ',latin:'m (sukun)',answer:'مْ',options:['بْ','مْ','دْ','رْ','سْ','نْ']},
      {arabic:'دْ',latin:'d (sukun)',answer:'دْ',options:['سْ','رْ','دْ','نْ','بْ','مْ']},
      {arabic:'نْ',latin:'n (sukun)',answer:'نْ',options:['مْ','سْ','رْ','نْ','دْ','بْ']},
    ]},
  '5C':{ title:'Ummi 5C', sub:'Gabungan Sukun & Harakat (مَنْ , مِنْ)', next:'6A', prev:'5B',
    questions:[
      {arabic:'مَنْ',latin:'man',answer:'مَنْ',options:['مَنْ','مِنْ','مُنْ','فَمْ','فِمْ','فُمْ']},
      {arabic:'مِنْ',latin:'min',answer:'مِنْ',options:['مَنْ','مِنْ','مُنْ','فَمْ','فِمْ','فُمْ']},
      {arabic:'مُنْ',latin:'mun',answer:'مُنْ',options:['مَنْ','مِنْ','مُنْ','فَمْ','فِمْ','فُمْ']},
      {arabic:'فَمْ',latin:'fam',answer:'فَمْ',options:['فُمْ','فِمْ','فَمْ','مُنْ','مِنْ','مَنْ']},
      {arabic:'فِمْ',latin:'fim',answer:'فِمْ',options:['مَنْ','مِنْ','فَمْ','فِمْ','مُنْ','فُمْ']},
      {arabic:'مَنْ',latin:'man',answer:'مَنْ',options:['فُمْ','فِمْ','فَمْ','مُنْ','مَنْ','مِنْ']},
      {arabic:'مُنْ',latin:'mun',answer:'مُنْ',options:['فَمْ','فِمْ','فُمْ','مُنْ','مِنْ','مَنْ']},
      {arabic:'فُمْ',latin:'fum',answer:'فُمْ',options:['مَنْ','مِنْ','فَمْ','فُمْ','مُنْ','فِمْ']},
      {arabic:'مِنْ',latin:'min',answer:'مِنْ',options:['فَمْ','فِمْ','مِنْ','فُمْ','مَنْ','مُنْ']},
      {arabic:'فَمْ',latin:'fam',answer:'فَمْ',options:['مُنْ','مِنْ','فَمْ','مَنْ','فُمْ','فِمْ']},
    ]},
  '6A':{ title:'Ummi 6A', sub:'Huruf Bertasydid (بَّ , دَّ)', next:'6B', prev:'5C',
    questions:[
      {arabic:'بَّ',latin:'bba (tasydid)',answer:'بَّ',options:['بَّ','دَّ','رَّ','سَّ','مَّ','نَّ']},
      {arabic:'دَّ',latin:'dda (tasydid)',answer:'دَّ',options:['بَّ','دَّ','رَّ','سَّ','مَّ','نَّ']},
      {arabic:'رَّ',latin:'rra (tasydid)',answer:'رَّ',options:['بَّ','دَّ','رَّ','سَّ','مَّ','نَّ']},
      {arabic:'سَّ',latin:'ssa (tasydid)',answer:'سَّ',options:['نَّ','مَّ','سَّ','رَّ','دَّ','بَّ']},
      {arabic:'مَّ',latin:'mma (tasydid)',answer:'مَّ',options:['بَّ','دَّ','رَّ','سَّ','مَّ','نَّ']},
      {arabic:'نَّ',latin:'nna (tasydid)',answer:'نَّ',options:['نَّ','مَّ','سَّ','رَّ','دَّ','بَّ']},
      {arabic:'بَّ',latin:'bba',answer:'بَّ',options:['نَّ','مَّ','سَّ','رَّ','بَّ','دَّ']},
      {arabic:'مَّ',latin:'mma',answer:'مَّ',options:['بَّ','مَّ','دَّ','رَّ','سَّ','نَّ']},
      {arabic:'دَّ',latin:'dda',answer:'دَّ',options:['سَّ','رَّ','دَّ','نَّ','بَّ','مَّ']},
      {arabic:'نَّ',latin:'nna',answer:'نَّ',options:['مَّ','سَّ','رَّ','نَّ','دَّ','بَّ']},
    ]},
  '6B':{ title:'Ummi 6B', sub:"Mad Thabi'i — Panjang 2 Harakat (بَا , دِي , بُو)", next:'6C', prev:'6A',
    questions:[
      {arabic:'بَا',latin:'baa (mad fathah)',answer:'بَا',options:['بَا','دِي','بُو','تَا','نِي','مُو']},
      {arabic:'دِي',latin:'dii (mad kasrah)',answer:'دِي',options:['بَا','دِي','بُو','تَا','نِي','مُو']},
      {arabic:'بُو',latin:'buu (mad dhammah)',answer:'بُو',options:['بَا','دِي','بُو','تَا','نِي','مُو']},
      {arabic:'تَا',latin:'taa',answer:'تَا',options:['مُو','نِي','تَا','بُو','دِي','بَا']},
      {arabic:'نِي',latin:'nii',answer:'نِي',options:['بَا','دِي','تَا','نِي','بُو','مُو']},
      {arabic:'مُو',latin:'muu',answer:'مُو',options:['مُو','نِي','تَا','بُو','دِي','بَا']},
      {arabic:'بَا',latin:'baa',answer:'بَا',options:['مُو','نِي','تَا','بُو','بَا','دِي']},
      {arabic:'نِي',latin:'nii',answer:'نِي',options:['بَا','نِي','دِي','تَا','بُو','مُو']},
      {arabic:'تَا',latin:'taa',answer:'تَا',options:['دِي','نِي','تَا','مُو','بَا','بُو']},
      {arabic:'مُو',latin:'muu',answer:'مُو',options:['نِي','تَا','مُو','دِي','بَا','بُو']},
    ]},
  '6C':{ title:'Ummi 6C', sub:"Mad Wajib & Lazim (آ , ءَا)", next:null, prev:'6B',
    questions:[
      {arabic:'آ',latin:'aa (mad lazim)',answer:'آ',options:['آ','ءَا','ءِي','ءُو','آنَ','ءَانَ']},
      {arabic:'ءَا',latin:"a'aa (mad wajib)",answer:'ءَا',options:['آ','ءَا','ءِي','ءُو','آنَ','ءَانَ']},
      {arabic:'آنَ',latin:'aana',answer:'آنَ',options:['آ','ءَا','ءِي','ءُو','آنَ','ءَانَ']},
      {arabic:'ءِي',latin:"i'ii",answer:'ءِي',options:['ءَانَ','آنَ','ءُو','ءِي','ءَا','آ']},
      {arabic:'ءُو',latin:"u'uu",answer:'ءُو',options:['آ','ءَا','ءِي','ءُو','آنَ','ءَانَ']},
      {arabic:'آ',latin:'aa',answer:'آ',options:['ءَانَ','آنَ','ءُو','ءِي','آ','ءَا']},
      {arabic:'ءَانَ',latin:"a'aana",answer:'ءَانَ',options:['آ','ءَا','ءِي','ءُو','آنَ','ءَانَ']},
      {arabic:'ءِي',latin:"i'ii",answer:'ءِي',options:['آ','ءِي','ءَا','آنَ','ءُو','ءَانَ']},
      {arabic:'آنَ',latin:'aana',answer:'آنَ',options:['ءَا','ءِي','آنَ','ءَانَ','آ','ءُو']},
      {arabic:'ءُو',latin:"u'uu",answer:'ءُو',options:['ءِي','ءَا','آ','ءُو','ءَانَ','آنَ']},
    ]},
};
