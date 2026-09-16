with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = """                const cacheKey = `${edition}:${surah}:${ayat}`;
                if (ayahTranslationCache[cacheKey]) {
                    const translatedText = ayahTranslationCache[cacheKey];
                    if (textEl) textEl.textContent = translatedText;
                    if (playBtn) playBtn.setAttribute('data-text', encodeURIComponent(translatedText));
                    return;
                }
                
                if (textEl) textEl.textContent = cfg.loadingText;
                
                try {
                    const res = await fetch(`https://api.alquran.cloud/v1/ayah/${surah}:${ayat}/${edition}`);
                    const json = await res.json();
                    if (json && json.data && json.data.text) {
                        const translatedText = json.data.text;
                        ayahTranslationCache[cacheKey] = translatedText;
                        if (textEl) textEl.textContent = translatedText;
                        if (playBtn) playBtn.setAttribute('data-text', encodeURIComponent(translatedText));
                    } else {
                        if (textEl) textEl.textContent = cfg.errorText;
                    }
                } catch (e) {
                    console.error(e);
                    if (textEl) textEl.textContent = cfg.connErrorText;
                }"""

replacement = """                const cacheKey = `${edition}:${surah}:${ayat}`;
                if (ayahTranslationCache[cacheKey]) {
                    const translatedText = ayahTranslationCache[cacheKey];
                    if (textEl) {
                        if (textEl.classList.contains('keyword-trans-box') && window.lastActiveSearchTerms && window.lastActiveSearchTerms.length) {
                            textEl.innerHTML = highlightKeyword(escapeHtml(translatedText), window.lastActiveSearchTerms);
                        } else {
                            textEl.textContent = translatedText;
                        }
                    }
                    if (playBtn) playBtn.setAttribute('data-text', encodeURIComponent(translatedText));
                    return;
                }
                
                if (textEl) textEl.textContent = cfg.loadingText;
                
                try {
                    const res = await fetch(`https://api.alquran.cloud/v1/ayah/${surah}:${ayat}/${edition}`);
                    const json = await res.json();
                    if (json && json.data && json.data.text) {
                        const translatedText = json.data.text;
                        ayahTranslationCache[cacheKey] = translatedText;
                        if (textEl) {
                            if (textEl.classList.contains('keyword-trans-box') && window.lastActiveSearchTerms && window.lastActiveSearchTerms.length) {
                                textEl.innerHTML = highlightKeyword(escapeHtml(translatedText), window.lastActiveSearchTerms);
                            } else {
                                textEl.textContent = translatedText;
                            }
                        }
                        if (playBtn) playBtn.setAttribute('data-text', encodeURIComponent(translatedText));
                    } else {
                        if (textEl) textEl.textContent = cfg.errorText;
                    }
                } catch (e) {
                    console.error(e);
                    if (textEl) textEl.textContent = cfg.connErrorText;
                }"""

# Normalize line endings for replacement
if '\r\n' in c and '\r\n' not in target:
    target = target.replace('\n', '\r\n')
    replacement = replacement.replace('\n', '\r\n')

if target in c:
    c = c.replace(target, replacement, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Successfully updated ayah highlight in translatePageContent()!")
else:
    print("Target block not found, checking line endings...")
