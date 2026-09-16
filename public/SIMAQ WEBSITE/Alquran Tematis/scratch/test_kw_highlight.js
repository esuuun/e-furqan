function highlightKeyword(text, keywords) {
    if (!text || !keywords) return text || '';
    const terms = (Array.isArray(keywords) ? keywords : [keywords])
        .map(t => (t || '').trim())
        .filter(t => t.length >= 2);
    if (!terms.length) return text;
    terms.sort((a, b) => b.length - a.length);
    const safePatterns = terms.map(t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
    const regex = new RegExp('(' + safePatterns.join('|') + ')', 'gi');
    return text.replace(regex, '<mark class="search-highlight">$1</mark>');
}

const sample = 'Wahai orang-orang yang beriman, janganlah mendekati salat, sedangkan kamu dalam keadaan mabuk';
console.log(highlightKeyword(sample, ['drunk', 'mabuk', 'memabukkan']));
