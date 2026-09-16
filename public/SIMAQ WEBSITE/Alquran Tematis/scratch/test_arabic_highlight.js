function highlightArabic(text, term) {
    // Unicode-aware regex for Arabic terms
    const safeTerm = term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const regex = new RegExp(`(^|[\\s\\p{P}])(${safeTerm})($|[\\s\\p{P}])`, 'gu');
    return text.replace(regex, '$1<mark class="search-highlight">$2</mark>$3');
}

const arabicText = 'يَسْـَٔلُونَكَ عَنِ ٱلْخَمْرِ وَٱلْمَيْسِرِ';
console.log('Highlighting خمر:');
// Notice in Quranic text, diacritics / harakat might be present or absent.
// If direct match:
console.log(highlightArabic('يسألونك عن الخمر والميسر', 'الخمر'));
