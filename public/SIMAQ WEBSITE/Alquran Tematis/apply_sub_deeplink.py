# apply_sub_deeplink.py
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for .sub-copy-btn
target_css_1 = """.uraian-wa-btn:hover {
            background: rgba(37, 211, 102, 0.25);
            border-color: #25d366;
            color: #ffffff;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(37, 211, 102, 0.25);
        }"""

replacement_css_1 = """.uraian-wa-btn:hover {
            background: rgba(37, 211, 102, 0.25);
            border-color: #25d366;
            color: #ffffff;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(37, 211, 102, 0.25);
        }
        .sub-copy-btn {
            background: rgba(14, 165, 233, 0.12);
            color: #38bdf8;
            border-color: rgba(14, 165, 233, 0.3);
        }
        .sub-copy-btn:hover {
            background: rgba(14, 165, 233, 0.25);
            border-color: #38bdf8;
            color: #ffffff;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(14, 165, 233, 0.25);
        }
        .sub-copy-btn.copied {
            background: rgba(16, 185, 129, 0.25);
            color: #34d399;
            border-color: #34d399;
        }"""

assert target_css_1 in content, "target_css_1 not found"
content = content.replace(target_css_1, replacement_css_1, 1)

# 2. Add .sub-highlight-pulse and mobile responsive CSS
target_css_2 = """.uraian-highlight-pulse {
            animation: uraianGlow 3.5s ease;
        }
        @keyframes uraianGlow {
            0% { box-shadow: 0 0 0 0 rgba(20, 184, 166, 0.8); border-color: #2dd4bf; transform: scale(1); }
            25% { box-shadow: 0 0 35px 8px rgba(20, 184, 166, 0.6); border-color: #2dd4bf; transform: scale(1.008); }
            70% { box-shadow: 0 0 25px 4px rgba(20, 184, 166, 0.4); border-color: #2dd4bf; transform: scale(1); }
            100% { box-shadow: 0 0 0 0 rgba(20, 184, 166, 0); }
        }"""

replacement_css_2 = """.uraian-highlight-pulse {
            animation: uraianGlow 3.5s ease;
        }
        @keyframes uraianGlow {
            0% { box-shadow: 0 0 0 0 rgba(20, 184, 166, 0.8); border-color: #2dd4bf; transform: scale(1); }
            25% { box-shadow: 0 0 35px 8px rgba(20, 184, 166, 0.6); border-color: #2dd4bf; transform: scale(1.008); }
            70% { box-shadow: 0 0 25px 4px rgba(20, 184, 166, 0.4); border-color: #2dd4bf; transform: scale(1); }
            100% { box-shadow: 0 0 0 0 rgba(20, 184, 166, 0); }
        }
        .sub-highlight-pulse {
            animation: subGlow 3.5s ease;
        }
        @keyframes subGlow {
            0% { box-shadow: 0 0 0 0 rgba(14, 165, 233, 0.8); border-color: #38bdf8; transform: scale(1); }
            25% { box-shadow: 0 0 35px 8px rgba(14, 165, 233, 0.6); border-color: #38bdf8; transform: scale(1.008); }
            70% { box-shadow: 0 0 25px 4px rgba(14, 165, 233, 0.4); border-color: #38bdf8; transform: scale(1); }
            100% { box-shadow: 0 0 0 0 rgba(14, 165, 233, 0); }
        }"""

assert target_css_2 in content, "target_css_2 not found"
content = content.replace(target_css_2, replacement_css_2, 1)

target_css_3 = """.group-header-actions {
                width: 100%;
                justify-content: flex-end;
                margin-top: 0.5rem;
            }
        }"""

replacement_css_3 = """.group-header-actions {
                width: 100%;
                justify-content: flex-end;
                margin-top: 0.5rem;
            }
            .sub-header-banner-card {
                flex-direction: column;
                align-items: stretch;
            }
            .sub-header-actions {
                width: 100%;
                justify-content: flex-start;
                margin-top: 0.75rem;
                flex-wrap: wrap;
            }
        }"""

assert target_css_3 in content, "target_css_3 not found"
content = content.replace(target_css_3, replacement_css_3, 1)

# 3. Add translations in LANG_UI_MAP
target_lang_en = """'Salin Link': 'Copy Link',
                'Tersalin!': 'Copied!',"""
replacement_lang_en = """'Salin Link': 'Copy Link',
                'Salin Link Sub': 'Copy Sub-topic Link',
                'Tersalin!': 'Copied!',"""

assert target_lang_en in content, "target_lang_en not found"
content = content.replace(target_lang_en, replacement_lang_en, 1)

target_lang_ar = """'Salin Link': 'نسخ الرابط',
                'Tersalin!': 'تم النسخ!',"""
replacement_lang_ar = """'Salin Link': 'نسخ الرابط',
                'Salin Link Sub': 'نسخ رابط المحور الفرعي',
                'Tersalin!': 'تم النسخ!',"""

assert target_lang_ar in content, "target_lang_ar not found"
content = content.replace(target_lang_ar, replacement_lang_ar, 1)

target_lang_ms = """'Salin Link': 'Salin Pautan',
                'Tersalin!': 'Disalin!',"""
replacement_lang_ms = """'Salin Link': 'Salin Pautan',
                'Salin Link Sub': 'Salin Pautan Sub Pokok',
                'Tersalin!': 'Disalin!',"""

assert target_lang_ms in content, "target_lang_ms not found"
content = content.replace(target_lang_ms, replacement_lang_ms, 1)

# 4. Add allThematicSubList and populate in buildVerseIndex()
target_build_index = """        let allThematicUraianList = [];
        let allThematicVersesList = [];

        function buildVerseIndex() {
            verseThematicIndex = {};
            allThematicUraianList = [];
            if (!quranData) return;
            for (const [tema, pbs] of Object.entries(quranData)) {
                for (const [pb, spbs] of Object.entries(pbs)) {
                    for (const [spb, urs] of Object.entries(spbs)) {
                        for (const [ur, urData] of Object.entries(urs)) {
                            const vList = (urData && urData.verses) ? urData.verses : [];
                            allThematicUraianList.push({
                                tema: tema,
                                pokok: pb,
                                sub: spb,
                                uraian: ur,
                                verseCount: vList.length,
                                sampleVerses: vList.slice(0, 3)
                            });
                            if (vList.length > 0) {
                                vList.forEach(v => {
                                    const key = `${v.surah_num}:${v.ayat_num}`;
                                    if (!verseThematicIndex[key]) {
                                        verseThematicIndex[key] = {
                                            surah_name: v.surah_name,
                                            surah_num: v.surah_num,
                                            ayat_num: v.ayat_num,
                                            arab: v.arab,
                                            indo: v.indo,
                                            audio: v.audio,
                                            topics: []
                                        };
                                    }
                                    verseThematicIndex[key].topics.push({
                                        tema: tema,
                                        pokok: pb,
                                        sub: spb,
                                        uraian: ur
                                    });
                                });
                            }
                        }
                    }
                }
            }
            allThematicVersesList = Object.values(verseThematicIndex);
            console.log(`[VerseIndex] Indexed ${allThematicVersesList.length} unique verses and ${allThematicUraianList.length} thematic topics.`);
        }"""

replacement_build_index = """        let allThematicUraianList = [];
        let allThematicVersesList = [];
        let allThematicSubList = [];

        function buildVerseIndex() {
            verseThematicIndex = {};
            allThematicUraianList = [];
            allThematicSubList = [];
            if (!quranData) return;
            for (const [tema, pbs] of Object.entries(quranData)) {
                for (const [pb, spbs] of Object.entries(pbs)) {
                    for (const [spb, urs] of Object.entries(spbs)) {
                        let subVerseCount = 0;
                        for (const [ur, urData] of Object.entries(urs)) {
                            const vList = (urData && urData.verses) ? urData.verses : [];
                            subVerseCount += vList.length;
                            allThematicUraianList.push({
                                tema: tema,
                                pokok: pb,
                                sub: spb,
                                uraian: ur,
                                verseCount: vList.length,
                                sampleVerses: vList.slice(0, 3)
                            });
                            if (vList.length > 0) {
                                vList.forEach(v => {
                                    const key = `${v.surah_num}:${v.ayat_num}`;
                                    if (!verseThematicIndex[key]) {
                                        verseThematicIndex[key] = {
                                            surah_name: v.surah_name,
                                            surah_num: v.surah_num,
                                            ayat_num: v.ayat_num,
                                            arab: v.arab,
                                            indo: v.indo,
                                            audio: v.audio,
                                            topics: []
                                        };
                                    }
                                    verseThematicIndex[key].topics.push({
                                        tema: tema,
                                        pokok: pb,
                                        sub: spb,
                                        uraian: ur
                                    });
                                });
                            }
                        }
                        allThematicSubList.push({
                            tema: tema,
                            pokok: pb,
                            sub: spb,
                            uraianCount: Object.keys(urs).length,
                            verseCount: subVerseCount
                        });
                    }
                }
            }
            allThematicVersesList = Object.values(verseThematicIndex);
            console.log(`[VerseIndex] Indexed ${allThematicVersesList.length} unique verses, ${allThematicSubList.length} sub-topics, and ${allThematicUraianList.length} thematic topics.`);
        }"""

assert target_build_index in content, "target_build_index not found"
content = content.replace(target_build_index, replacement_build_index, 1)

# 5. Add Sub Pokok Bahasan helper functions and upgrade checkAutoNav
target_helpers = """        function shareUraianWhatsApp(event, encodedTitle) {
            if (event) event.stopPropagation();
            const uraianTitle = decodeURIComponent(encodedTitle);
            const found = findUraianPath(uraianTitle);
            const tema = found ? found.tema : (elTema ? elTema.value : '');
            const pokok = found ? found.pokok : (elPokok ? elPokok.value : '');
            const sub = found ? found.sub : (elSub ? elSub.value : '');
            const vCount = found ? found.verseCount : 0;
            const link = getUraianDeepLink(uraianTitle, tema, pokok, sub);

            const message = `*Al-Qur'an Tematis*\\n\\n` +
                `📖 *Uraian:* ${uraianTitle}\\n` +
                (tema ? `🏷️ *Tema:* ${tema}\\n` : '') +
                (pokok ? `📂 *Pokok:* ${pokok}\\n` : '') +
                (sub ? `📑 *Sub Pokok:* ${sub}\\n` : '') +
                (vCount > 0 ? `📊 *Jumlah Ayat:* ${vCount} ayat\\n\\n` : '\\n') +
                `Pelajari selengkapnya di tautan berikut:\\n${link}`;

            const waUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(message)}`;
            window.open(waUrl, '_blank');
        }

        function checkAutoNav() {
            if (!quranData || !Object.keys(quranData).length) return;

            const params = getParsedUrlParams();

            // 1. Check verse deep link (#surat=2&ayat=255)
            const s = parseInt(params.get('surat'));
            const a = parseInt(params.get('ayat'));
            if (s && a) {
                setTimeout(() => lookupVerseInSearch(s, a), 100);
                return;
            }

            // 2. Check Uraian deep link
            let paramUraian = params.get('uraian');
            const rawHash = (window.location.hash || '').replace(/^#/, '').trim();
            if (!paramUraian && rawHash && !rawHash.includes('=') && !rawHash.includes('&')) {
                paramUraian = decodeURIComponent(rawHash);
            }

            if (paramUraian) {
                let targetTema = params.get('tema');
                let targetPokok = params.get('pokok');
                let targetSub = params.get('sub');
                let targetUraian = decodeURIComponent(paramUraian);

                if (!targetTema || !targetPokok || !targetSub || !quranData[targetTema] || !quranData[targetTema][targetPokok] || !quranData[targetTema][targetPokok][targetSub]) {
                    const resolved = findUraianPath(targetUraian);
                    if (resolved) {
                        targetTema = resolved.tema;
                        targetPokok = resolved.pokok;
                        targetSub = resolved.sub;
                        targetUraian = resolved.uraian;
                    }
                }

                if (targetTema && targetPokok && targetSub && quranData[targetTema] && quranData[targetTema][targetPokok] && quranData[targetTema][targetPokok][targetSub]) {
                    setTimeout(() => {
                        navigateToThematicTopic(targetTema, targetPokok, targetSub, targetUraian);
                    }, 50);
                    return;
                }
            }

            // 3. Saved state from sessionStorage
            const savedTema = sessionStorage.getItem('active_tema');
            const savedPokok = sessionStorage.getItem('active_pokok');
            const savedSub = sessionStorage.getItem('active_sub');

            if (savedTema && quranData[savedTema]) {
                elTema.value = savedTema;
                populateSelect(elPokok, naturalSort(Object.keys(quranData[savedTema])), "Pilih Pokok Bahasan");
                if (savedPokok && quranData[savedTema][savedPokok]) {
                    elPokok.value = savedPokok;
                    populateSelect(elSub, naturalSort(Object.keys(quranData[savedTema][savedPokok])), "Pilih Sub Pokok Bahasan");
                    if (savedSub && quranData[savedTema][savedPokok][savedSub]) {
                        elSub.value = savedSub;
                        renderContentAll(savedTema, savedPokok, savedSub);
                        return;
                    }
                }
            }

            // 4. Default initial state
            const temaKeys = naturalSort(Object.keys(quranData));
            if (temaKeys.length > 0) {
                const firstTema = temaKeys[0];
                elTema.value = firstTema;
                const pokokKeys = naturalSort(Object.keys(quranData[firstTema] || {}));
                populateSelect(elPokok, pokokKeys, "Pilih Pokok Bahasan");
                if (pokokKeys.length > 0) {
                    const firstPokok = pokokKeys[0];
                    elPokok.value = firstPokok;
                    const subKeys = naturalSort(Object.keys(quranData[firstTema][firstPokok] || {}));
                    populateSelect(elSub, subKeys, "Pilih Sub Pokok Bahasan");
                    if (subKeys.length > 0) {
                        const firstSub = subKeys[0];
                        elSub.value = firstSub;
                        renderContentAll(firstTema, firstPokok, firstSub);
                    }
                }
            }
        }"""

replacement_helpers = """        function shareUraianWhatsApp(event, encodedTitle) {
            if (event) event.stopPropagation();
            const uraianTitle = decodeURIComponent(encodedTitle);
            const found = findUraianPath(uraianTitle);
            const tema = found ? found.tema : (elTema ? elTema.value : '');
            const pokok = found ? found.pokok : (elPokok ? elPokok.value : '');
            const sub = found ? found.sub : (elSub ? elSub.value : '');
            const vCount = found ? found.verseCount : 0;
            const link = getUraianDeepLink(uraianTitle, tema, pokok, sub);

            const message = `*Al-Qur'an Tematis*\\n\\n` +
                `📖 *Uraian:* ${uraianTitle}\\n` +
                (tema ? `🏷️ *Tema:* ${tema}\\n` : '') +
                (pokok ? `📂 *Pokok:* ${pokok}\\n` : '') +
                (sub ? `📑 *Sub Pokok:* ${sub}\\n` : '') +
                (vCount > 0 ? `📊 *Jumlah Ayat:* ${vCount} ayat\\n\\n` : '\\n') +
                `Pelajari selengkapnya di tautan berikut:\\n${link}`;

            const waUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(message)}`;
            window.open(waUrl, '_blank');
        }

        function findSubPath(subQuery) {
            if (!subQuery || !allThematicSubList || !allThematicSubList.length) return null;
            const cleanQ = decodeURIComponent(subQuery).trim().toLowerCase();
            if (!cleanQ) return null;

            // 1. Exact match
            let match = allThematicSubList.find(item => item.sub.toLowerCase() === cleanQ);
            if (match) return match;

            // 2. Starts with (e.g. "1.1.1" or "1.1.1." or code prefix)
            match = allThematicSubList.find(item => item.sub.toLowerCase().startsWith(cleanQ));
            if (match) return match;

            // 3. Substring match (e.g. "waris" or "tauhid")
            match = allThematicSubList.find(item => item.sub.toLowerCase().includes(cleanQ));
            if (match) return match;

            return null;
        }

        function getSubDeepLink(subTitle, tema, pokok) {
            if (!tema || !pokok) {
                const found = findSubPath(subTitle);
                if (found) {
                    tema = found.tema;
                    pokok = found.pokok;
                    subTitle = found.sub;
                }
            }
            const hash = `tema=${encodeURIComponent(tema || '')}&pokok=${encodeURIComponent(pokok || '')}&sub=${encodeURIComponent(subTitle)}`;
            const baseUrl = window.location.href.split('#')[0].split('?')[0];
            return `${baseUrl}#${hash}`;
        }

        function copySubLink(btn, event, encodedSubTitle) {
            if (event) event.stopPropagation();
            const subTitle = decodeURIComponent(encodedSubTitle);
            const link = getSubDeepLink(subTitle, elTema ? elTema.value : '', elPokok ? elPokok.value : '');

            const onCopiedSuccess = () => {
                showAIToast("Link Sub Pokok Bahasan berhasil disalin ke clipboard!");
                if (btn) {
                    const origHTML = btn.innerHTML;
                    btn.classList.add('copied');
                    btn.innerHTML = `
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span>Tersalin!</span>
                    `;
                    setTimeout(() => {
                        btn.classList.remove('copied');
                        btn.innerHTML = origHTML;
                    }, 2000);
                }
            };

            const fallbackCopy = (text) => {
                const ta = document.createElement('textarea');
                ta.value = text;
                ta.style.position = 'fixed';
                ta.style.left = '-9999px';
                document.body.appendChild(ta);
                ta.select();
                try {
                    document.execCommand('copy');
                    onCopiedSuccess();
                } catch(e) {
                    console.error("Fallback copy failed:", e);
                }
                document.body.removeChild(ta);
            };

            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(link).then(onCopiedSuccess).catch(() => fallbackCopy(link));
            } else {
                fallbackCopy(link);
            }
        }

        function shareSubWhatsApp(event, encodedSubTitle) {
            if (event) event.stopPropagation();
            const subTitle = decodeURIComponent(encodedSubTitle);
            const found = findSubPath(subTitle);
            const tema = found ? found.tema : (elTema ? elTema.value : '');
            const pokok = found ? found.pokok : (elPokok ? elPokok.value : '');
            const uCount = found ? found.uraianCount : (quranData[tema] && quranData[tema][pokok] && quranData[tema][pokok][subTitle] ? Object.keys(quranData[tema][pokok][subTitle]).length : 0);
            const vCount = found ? found.verseCount : 0;
            const link = getSubDeepLink(subTitle, tema, pokok);

            const message = `*Al-Qur'an Tematis*\\n\\n` +
                `📑 *Sub Pokok Bahasan:* ${subTitle}\\n` +
                (tema ? `🏷️ *Tema:* ${tema}\\n` : '') +
                (pokok ? `📂 *Pokok:* ${pokok}\\n` : '') +
                (uCount > 0 ? `📊 *Jumlah Uraian:* ${uCount} topik` + (vCount > 0 ? ` (${vCount} ayat)\\n\\n` : `\\n\\n`) : '\\n') +
                `Pelajari selengkapnya di tautan berikut:\\n${link}`;

            const waUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(message)}`;
            window.open(waUrl, '_blank');
        }

        function navigateToSubTopic(tema, pokok, sub) {
            stopTTS();
            switchMainMode('thematic');

            elTema.value = tema;
            resetSelect(elSub, "Pilih Sub Pokok Bahasan");
            if (quranData[tema]) {
                populateSelect(elPokok, naturalSort(Object.keys(quranData[tema])), "Pilih Pokok Bahasan");
                elPokok.value = pokok;
                if (quranData[tema][pokok]) {
                    populateSelect(elSub, naturalSort(Object.keys(quranData[tema][pokok])), "Pilih Sub Pokok Bahasan");
                    elSub.value = sub;
                    saveCurrentState();
                    renderContentAll(tema, pokok, sub);

                    setTimeout(() => {
                        const banner = document.querySelector('.sub-header-banner-card');
                        if (banner) {
                            banner.scrollIntoView({ behavior: 'smooth', block: 'center' });
                            banner.classList.add('sub-highlight-pulse');
                            setTimeout(() => banner.classList.remove('sub-highlight-pulse'), 3500);
                        }
                    }, 150);
                }
            }
        }

        function checkAutoNav() {
            if (!quranData || !Object.keys(quranData).length) return;

            const params = getParsedUrlParams();

            // 1. Check verse deep link (#surat=2&ayat=255)
            const s = parseInt(params.get('surat'));
            const a = parseInt(params.get('ayat'));
            if (s && a) {
                setTimeout(() => lookupVerseInSearch(s, a), 100);
                return;
            }

            // 2. Check Uraian deep link
            let paramUraian = params.get('uraian');
            let paramSub = params.get('sub');
            const rawHash = (window.location.hash || '').replace(/^#/, '').trim();
            if (!paramUraian && !paramSub && rawHash && !rawHash.includes('=') && !rawHash.includes('&')) {
                const uMatch = findUraianPath(rawHash);
                if (uMatch) {
                    paramUraian = decodeURIComponent(rawHash);
                } else {
                    const sMatch = findSubPath(rawHash);
                    if (sMatch) {
                        paramSub = decodeURIComponent(rawHash);
                    }
                }
            }

            if (paramUraian) {
                let targetTema = params.get('tema');
                let targetPokok = params.get('pokok');
                let targetSub = params.get('sub');
                let targetUraian = decodeURIComponent(paramUraian);

                if (!targetTema || !targetPokok || !targetSub || !quranData[targetTema] || !quranData[targetTema][targetPokok] || !quranData[targetTema][targetPokok][targetSub]) {
                    const resolved = findUraianPath(targetUraian);
                    if (resolved) {
                        targetTema = resolved.tema;
                        targetPokok = resolved.pokok;
                        targetSub = resolved.sub;
                        targetUraian = resolved.uraian;
                    }
                }

                if (targetTema && targetPokok && targetSub && quranData[targetTema] && quranData[targetTema][targetPokok] && quranData[targetTema][targetPokok][targetSub]) {
                    setTimeout(() => {
                        navigateToThematicTopic(targetTema, targetPokok, targetSub, targetUraian);
                    }, 50);
                    return;
                }
            }

            // 3. Check Sub Pokok Bahasan deep link
            if (paramSub) {
                let targetTema = params.get('tema');
                let targetPokok = params.get('pokok');
                let targetSub = decodeURIComponent(paramSub);

                if (!targetTema || !targetPokok || !quranData[targetTema] || !quranData[targetTema][targetPokok] || !quranData[targetTema][targetPokok][targetSub]) {
                    const resolved = findSubPath(targetSub);
                    if (resolved) {
                        targetTema = resolved.tema;
                        targetPokok = resolved.pokok;
                        targetSub = resolved.sub;
                    }
                }

                if (targetTema && targetPokok && targetSub && quranData[targetTema] && quranData[targetTema][targetPokok] && quranData[targetTema][targetPokok][targetSub]) {
                    setTimeout(() => {
                        navigateToSubTopic(targetTema, targetPokok, targetSub);
                    }, 50);
                    return;
                }
            }

            // 4. Saved state from sessionStorage
            const savedTema = sessionStorage.getItem('active_tema');
            const savedPokok = sessionStorage.getItem('active_pokok');
            const savedSub = sessionStorage.getItem('active_sub');

            if (savedTema && quranData[savedTema]) {
                elTema.value = savedTema;
                populateSelect(elPokok, naturalSort(Object.keys(quranData[savedTema])), "Pilih Pokok Bahasan");
                if (savedPokok && quranData[savedTema][savedPokok]) {
                    elPokok.value = savedPokok;
                    populateSelect(elSub, naturalSort(Object.keys(quranData[savedTema][savedPokok])), "Pilih Sub Pokok Bahasan");
                    if (savedSub && quranData[savedTema][savedPokok][savedSub]) {
                        elSub.value = savedSub;
                        renderContentAll(savedTema, savedPokok, savedSub);
                        return;
                    }
                }
            }

            // 5. Default initial state
            const temaKeys = naturalSort(Object.keys(quranData));
            if (temaKeys.length > 0) {
                const firstTema = temaKeys[0];
                elTema.value = firstTema;
                const pokokKeys = naturalSort(Object.keys(quranData[firstTema] || {}));
                populateSelect(elPokok, pokokKeys, "Pilih Pokok Bahasan");
                if (pokokKeys.length > 0) {
                    const firstPokok = pokokKeys[0];
                    elPokok.value = firstPokok;
                    const subKeys = naturalSort(Object.keys(quranData[firstTema][firstPokok] || {}));
                    populateSelect(elSub, subKeys, "Pilih Sub Pokok Bahasan");
                    if (subKeys.length > 0) {
                        const firstSub = subKeys[0];
                        elSub.value = firstSub;
                        renderContentAll(firstTema, firstPokok, firstSub);
                    }
                }
            }
        }"""

assert target_helpers in content, "target_helpers not found"
content = content.replace(target_helpers, replacement_helpers, 1)

# 6. Update elSub.addEventListener to sync URL hash
target_elsub = """            if (sub && quranData[tema] && quranData[tema][pokok] && quranData[tema][pokok][sub]) {
                saveCurrentState();
                renderContentAll(tema, pokok, sub);
            }"""

replacement_elsub = """            if (sub && quranData[tema] && quranData[tema][pokok] && quranData[tema][pokok][sub]) {
                saveCurrentState();
                renderContentAll(tema, pokok, sub);
                try {
                    const newUrl = getSubDeepLink(sub, tema, pokok);
                    history.replaceState(null, '', newUrl);
                } catch(e) {}
            }"""

assert target_elsub in content, "target_elsub not found"
content = content.replace(target_elsub, replacement_elsub, 1)

# 7. Update renderContentAll to include Salin Link Sub and WA buttons
target_render_sub = """                    <div class="sub-header-actions">
                        <button id="btn-toggle-all-groups" class="toggle-verses-btn" onclick="toggleAllGroups()">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="7 13 12 18 17 13"></polyline><polyline points="7 6 12 11 17 6"></polyline></svg>
                            <span id="toggle-all-text" data-i18n-orig="Buka Semua Uraian">Buka Semua Uraian</span>
                        </button>
                    </div>"""

replacement_render_sub = """                    <div class="sub-header-actions">
                        <button class="uraian-action-btn sub-copy-btn" onclick="copySubLink(this, event, '${encodeURIComponent(sub)}')" title="Salin Deep Link Sub Pokok Bahasan Ini">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
                            <span data-i18n-orig="Salin Link Sub">Salin Link Sub</span>
                        </button>
                        <button class="uraian-action-btn uraian-wa-btn" onclick="shareSubWhatsApp(event, '${encodeURIComponent(sub)}')" title="Bagikan ke WhatsApp">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                            <span>WA</span>
                        </button>
                        <button id="btn-toggle-all-groups" class="toggle-verses-btn" onclick="toggleAllGroups()">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="7 13 12 18 17 13"></polyline><polyline points="7 6 12 11 17 6"></polyline></svg>
                            <span id="toggle-all-text" data-i18n-orig="Buka Semua Uraian">Buka Semua Uraian</span>
                        </button>
                    </div>"""

assert target_render_sub in content, "target_render_sub not found"
content = content.replace(target_render_sub, replacement_render_sub, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("All Sub Pokok Bahasan deep link modifications applied successfully to index.html!")
