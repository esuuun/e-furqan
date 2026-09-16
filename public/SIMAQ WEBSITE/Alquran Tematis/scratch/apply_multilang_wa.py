# scratch/apply_multilang_wa.py
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update getUraianDeepLink to include &lang=...
target_uraian_link = """        function getUraianDeepLink(uraianTitle, tema, pokok, sub) {
            if (!tema || !pokok || !sub) {
                const found = findUraianPath(uraianTitle);
                if (found) {
                    tema = found.tema;
                    pokok = found.pokok;
                    sub = found.sub;
                    uraianTitle = found.uraian;
                }
            }
            const hash = `tema=${encodeURIComponent(tema || '')}&pokok=${encodeURIComponent(pokok || '')}&sub=${encodeURIComponent(sub || '')}&uraian=${encodeURIComponent(uraianTitle)}`;
            const baseUrl = window.location.href.split('#')[0].split('?')[0];
            return `${baseUrl}#${hash}`;
        }"""

replacement_uraian_link = """        function getUraianDeepLink(uraianTitle, tema, pokok, sub) {
            if (!tema || !pokok || !sub) {
                const found = findUraianPath(uraianTitle);
                if (found) {
                    tema = found.tema;
                    pokok = found.pokok;
                    sub = found.sub;
                    uraianTitle = found.uraian;
                }
            }
            let hash = `tema=${encodeURIComponent(tema || '')}&pokok=${encodeURIComponent(pokok || '')}&sub=${encodeURIComponent(sub || '')}&uraian=${encodeURIComponent(uraianTitle)}`;
            const langSelect = document.getElementById('tts-language');
            if (langSelect && langSelect.value && langSelect.value !== 'id-ID') {
                hash += `&lang=${encodeURIComponent(langSelect.value)}`;
            }
            const baseUrl = window.location.href.split('#')[0].split('?')[0];
            return `${baseUrl}#${hash}`;
        }"""

assert target_uraian_link in content, "target_uraian_link not found"
content = content.replace(target_uraian_link, replacement_uraian_link, 1)

# 2. Add getWhatsAppTemplates and getDomOrCachedTranslation helper functions,
# and upgrade shareUraianWhatsApp, getSubDeepLink, shareSubWhatsApp
target_share_block = """        function shareUraianWhatsApp(event, encodedTitle) {
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
        }"""

replacement_share_block = """        function getWhatsAppTemplates(langCode) {
            const templates = {
                'id': {
                    appName: "Al-Qur'an Tematis",
                    subHeader: "Sub Pokok Bahasan",
                    tema: "Tema",
                    pokok: "Pokok",
                    sub: "Sub Pokok",
                    uraian: "Uraian",
                    subMeta: (uCount, vCount) => `Jumlah Uraian: ${uCount} topik` + (vCount > 0 ? ` (${vCount} ayat)` : ''),
                    uraianMeta: vCount => `Jumlah Ayat: ${vCount} ayat`,
                    learnMore: "Pelajari selengkapnya di tautan berikut:",
                    quranPrefix: "QS.",
                    ayahLabel: "Ayat",
                    meaningLabel: "Artinya"
                },
                'en': {
                    appName: "Thematic Quran",
                    subHeader: "Sub-topic",
                    tema: "Theme",
                    pokok: "Topic",
                    sub: "Sub-topic",
                    uraian: "Topic Details",
                    subMeta: (uCount, vCount) => `Total Topics: ${uCount} topics` + (vCount > 0 ? ` (${vCount} verses)` : ''),
                    uraianMeta: vCount => `Total Verses: ${vCount} verses`,
                    learnMore: "Learn more at the following link:",
                    quranPrefix: "Quran",
                    ayahLabel: "Verse",
                    meaningLabel: "Translation"
                },
                'ms': {
                    appName: "Al-Quran Tematik",
                    subHeader: "Sub Pokok Bahasan",
                    tema: "Tema",
                    pokok: "Pokok",
                    sub: "Sub Pokok",
                    uraian: "Huraian",
                    subMeta: (uCount, vCount) => `Jumlah Huraian: ${uCount} topik` + (vCount > 0 ? ` (${vCount} ayat)` : ''),
                    uraianMeta: vCount => `Jumlah Ayat: ${vCount} ayat`,
                    learnMore: "Ketahui lebih lanjut di pautan berikut:",
                    quranPrefix: "QS.",
                    ayahLabel: "Ayat",
                    meaningLabel: "Maksudnya"
                },
                'ar': {
                    appName: "القرآن الكريم الموضوعي",
                    subHeader: "الموضوع الفرعي",
                    tema: "الموضوع الرئيسي",
                    pokok: "الموضوع",
                    sub: "الموضوع الفرعي",
                    uraian: "التفصيل الموضوعي",
                    subMeta: (uCount, vCount) => `عدد المواضيع: ${uCount} موضوع` + (vCount > 0 ? ` (${vCount} آية)` : ''),
                    uraianMeta: vCount => `عدد الآيات: ${vCount} آية`,
                    learnMore: "اقرأ المزيد عبر الرابط التالي:",
                    quranPrefix: "سورة",
                    ayahLabel: "آية",
                    meaningLabel: "الترجمة"
                },
                'ur': {
                    appName: "موضوعاتی قرآن",
                    subHeader: "ذیلی موضوع",
                    tema: "مرکزی موضوع",
                    pokok: "بنیادی موضوع",
                    sub: "ذیلی موضوع",
                    uraian: "موضوعاتی تفصیل",
                    subMeta: (uCount, vCount) => `کل موضوعات: ${uCount} موضوعات` + (vCount > 0 ? ` (${vCount} آیات)` : ''),
                    uraianMeta: vCount => `کل آیات: ${vCount} آیات`,
                    learnMore: "مندرجہ ذیل لنک پر مزید ملاحظہ فرمائیں:",
                    quranPrefix: "قرآن",
                    ayahLabel: "آیت",
                    meaningLabel: "ترجمہ"
                },
                'fr': {
                    appName: "Coran Thématique",
                    subHeader: "Sous-sujet",
                    tema: "Thème",
                    pokok: "Sujet principal",
                    sub: "Sous-sujet",
                    uraian: "Détails du sujet",
                    subMeta: (uCount, vCount) => `Total des sujets: ${uCount} sujets` + (vCount > 0 ? ` (${vCount} versets)` : ''),
                    uraianMeta: vCount => `Total des versets: ${vCount} versets`,
                    learnMore: "En savoir plus sur le lien suivant :",
                    quranPrefix: "Coran",
                    ayahLabel: "Verset",
                    meaningLabel: "Traduction"
                },
                'es': {
                    appName: "Corán Temático",
                    subHeader: "Subtema",
                    tema: "Tema",
                    pokok: "Tema principal",
                    sub: "Subtema",
                    uraian: "Detalles del tema",
                    subMeta: (uCount, vCount) => `Total de temas: ${uCount} temas` + (vCount > 0 ? ` (${vCount} versículos)` : ''),
                    uraianMeta: vCount => `Total de versículos: ${vCount} versículos`,
                    learnMore: "Obtenga más información en el siguiente enlace:",
                    quranPrefix: "Corán",
                    ayahLabel: "Versículo",
                    meaningLabel: "Traducción"
                },
                'tr': {
                    appName: "Tematik Kuran",
                    subHeader: "Alt Konu",
                    tema: "Tema",
                    pokok: "Ana Konu",
                    sub: "Alt Konu",
                    uraian: "Konu Detayı",
                    subMeta: (uCount, vCount) => `Toplam Konu: ${uCount} konu` + (vCount > 0 ? ` (${vCount} ayet)` : ''),
                    uraianMeta: vCount => `Toplam Ayet: ${vCount} ayet`,
                    learnMore: "Aşağıdaki bağlantıdan daha fazlasını öğrenin:",
                    quranPrefix: "Kuran",
                    ayahLabel: "Ayet",
                    meaningLabel: "Anlamı"
                },
                'de': {
                    appName: "Thematischer Koran",
                    subHeader: "Unterthema",
                    tema: "Thema",
                    pokok: "Hauptthema",
                    sub: "Unterthema",
                    uraian: "Themendetail",
                    subMeta: (uCount, vCount) => `Gesamte Themen: ${uCount} Themen` + (vCount > 0 ? ` (${vCount} Verse)` : ''),
                    uraianMeta: vCount => `Gesamte Verse: ${vCount} Verse`,
                    learnMore: "Erfahren Sie mehr unter folgendem Link:",
                    quranPrefix: "Koran",
                    ayahLabel: "Vers",
                    meaningLabel: "Übersetzung"
                },
                'ru': {
                    appName: "Тематический Коран",
                    subHeader: "Подтема",
                    tema: "Тема",
                    pokok: "Основная тема",
                    sub: "Подтема",
                    uraian: "Описание темы",
                    subMeta: (uCount, vCount) => `Всего тем: ${uCount}` + (vCount > 0 ? ` (${vCount} аятов)` : ''),
                    uraianMeta: vCount => `Всего аятов: ${vCount} аятов`,
                    learnMore: "Узнайте больше по следующей ссылке:",
                    quranPrefix: "Коран",
                    ayahLabel: "Аят",
                    meaningLabel: "Перевод"
                },
                'zh': {
                    appName: "专题古兰经",
                    subHeader: "子主题",
                    tema: "主题",
                    pokok: "主干",
                    sub: "子主题",
                    uraian: "专题详解",
                    subMeta: (uCount, vCount) => `主题总数: ${uCount} 个` + (vCount > 0 ? ` (${vCount} 节经文)` : ''),
                    uraianMeta: vCount => `经文总数: ${vCount} 节`,
                    learnMore: "点击下方链接了解更多：",
                    quranPrefix: "古兰经",
                    ayahLabel: "节",
                    meaningLabel: "译文"
                }
            };
            return templates[langCode] || templates['en'];
        }

        function getDomOrCachedTranslation(origText, targetLangCode, domSelectorOrEl) {
            if (!origText || targetLangCode === 'id') return origText;

            // 1. From DOM element (if it has already been translated and rendered)
            if (domSelectorOrEl) {
                const el = (typeof domSelectorOrEl === 'string') ? document.querySelector(domSelectorOrEl) : domSelectorOrEl;
                if (el) {
                    const text = el.textContent ? el.textContent.trim() : '';
                    if (text && text !== origText) {
                        return text;
                    }
                }
            }

            // 2. From persistent cache
            const cacheKey = `${targetLangCode}:${origText.trim()}`;
            if (translationCache && translationCache[cacheKey]) {
                return translationCache[cacheKey];
            }

            // 3. From static dictionary
            const dict = LANG_UI_MAP && LANG_UI_MAP[targetLangCode];
            if (dict && dict[origText.trim()]) {
                return dict[origText.trim()];
            }

            return null;
        }

        async function shareUraianWhatsApp(event, encodedTitle) {
            if (event) event.stopPropagation();
            const uraianTitle = decodeURIComponent(encodedTitle);
            const found = findUraianPath(uraianTitle);
            const tema = found ? found.tema : (elTema ? elTema.value : '');
            const pokok = found ? found.pokok : (elPokok ? elPokok.value : '');
            const sub = found ? found.sub : (elSub ? elSub.value : '');
            const vCount = found ? found.verseCount : 0;
            const link = getUraianDeepLink(uraianTitle, tema, pokok, sub);

            const langSelect = document.getElementById('tts-language');
            const langKey = langSelect ? langSelect.value : 'id-ID';
            const cfg = LANG_CONFIG[langKey] || LANG_CONFIG['id-ID'];
            const targetLangCode = cfg.code;
            const t = getWhatsAppTemplates(targetLangCode);

            let displayUraian = uraianTitle;
            let displayTema = tema;
            let displayPokok = pokok;
            let displaySub = sub;

            if (targetLangCode !== 'id') {
                let cardEl = null;
                if (event && event.target) {
                    cardEl = event.target.closest('.uraian-group-card');
                }
                const groupTitleEl = cardEl ? cardEl.querySelector('.group-title') : null;

                displayUraian = getDomOrCachedTranslation(uraianTitle, targetLangCode, groupTitleEl);
                if (!displayUraian) {
                    try { displayUraian = await translateTextFree(uraianTitle, targetLangCode); } catch(e) {}
                }
                displayUraian = displayUraian || uraianTitle;

                const temaOpt = elTema && elTema.value === tema ? elTema.options[elTema.selectedIndex] : null;
                displayTema = getDomOrCachedTranslation(tema, targetLangCode, temaOpt);
                if (!displayTema && tema) {
                    try { displayTema = await translateTextFree(tema, targetLangCode); } catch(e) {}
                }
                displayTema = displayTema || tema;

                const pokokOpt = elPokok && elPokok.value === pokok ? elPokok.options[elPokok.selectedIndex] : null;
                displayPokok = getDomOrCachedTranslation(pokok, targetLangCode, pokokOpt);
                if (!displayPokok && pokok) {
                    try { displayPokok = await translateTextFree(pokok, targetLangCode); } catch(e) {}
                }
                displayPokok = displayPokok || pokok;

                const subEl = document.querySelector('.sub-header-title');
                displaySub = getDomOrCachedTranslation(sub, targetLangCode, subEl);
                if (!displaySub && sub) {
                    try { displaySub = await translateTextFree(sub, targetLangCode); } catch(e) {}
                }
                displaySub = displaySub || sub;
            }

            const message = `*${t.appName}*\\n\\n` +
                `📖 *${t.uraian}:* ${displayUraian}\\n` +
                (displayTema ? `🏷️ *${t.tema}:* ${displayTema}\\n` : '') +
                (displayPokok ? `📂 *${t.pokok}:* ${displayPokok}\\n` : '') +
                (displaySub ? `📑 *${t.sub}:* ${displaySub}\\n` : '') +
                (vCount > 0 ? `📊 *${t.uraianMeta(vCount)}*\\n\\n` : '\\n') +
                `${t.learnMore}\\n${link}`;

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
            let hash = `tema=${encodeURIComponent(tema || '')}&pokok=${encodeURIComponent(pokok || '')}&sub=${encodeURIComponent(subTitle)}`;
            const langSelect = document.getElementById('tts-language');
            if (langSelect && langSelect.value && langSelect.value !== 'id-ID') {
                hash += `&lang=${encodeURIComponent(langSelect.value)}`;
            }
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

        async function shareSubWhatsApp(event, encodedSubTitle) {
            if (event) event.stopPropagation();
            const subTitle = decodeURIComponent(encodedSubTitle);
            const found = findSubPath(subTitle);
            const tema = found ? found.tema : (elTema ? elTema.value : '');
            const pokok = found ? found.pokok : (elPokok ? elPokok.value : '');
            const uCount = found ? found.uraianCount : (quranData[tema] && quranData[tema][pokok] && quranData[tema][pokok][subTitle] ? Object.keys(quranData[tema][pokok][subTitle]).length : 0);
            const vCount = found ? found.verseCount : 0;
            const link = getSubDeepLink(subTitle, tema, pokok);

            const langSelect = document.getElementById('tts-language');
            const langKey = langSelect ? langSelect.value : 'id-ID';
            const cfg = LANG_CONFIG[langKey] || LANG_CONFIG['id-ID'];
            const targetLangCode = cfg.code;
            const t = getWhatsAppTemplates(targetLangCode);

            let displaySub = subTitle;
            let displayTema = tema;
            let displayPokok = pokok;

            if (targetLangCode !== 'id') {
                const subEl = document.querySelector('.sub-header-title');
                displaySub = getDomOrCachedTranslation(subTitle, targetLangCode, subEl);
                if (!displaySub) {
                    try { displaySub = await translateTextFree(subTitle, targetLangCode); } catch(e) {}
                }
                displaySub = displaySub || subTitle;

                const temaOpt = elTema && elTema.value === tema ? elTema.options[elTema.selectedIndex] : null;
                displayTema = getDomOrCachedTranslation(tema, targetLangCode, temaOpt);
                if (!displayTema && tema) {
                    try { displayTema = await translateTextFree(tema, targetLangCode); } catch(e) {}
                }
                displayTema = displayTema || tema;

                const pokokOpt = elPokok && elPokok.value === pokok ? elPokok.options[elPokok.selectedIndex] : null;
                displayPokok = getDomOrCachedTranslation(pokok, targetLangCode, pokokOpt);
                if (!displayPokok && pokok) {
                    try { displayPokok = await translateTextFree(pokok, targetLangCode); } catch(e) {}
                }
                displayPokok = displayPokok || pokok;
            }

            const message = `*${t.appName}*\\n\\n` +
                `📑 *${t.subHeader}:* ${displaySub}\\n` +
                (displayTema ? `🏷️ *${t.tema}:* ${displayTema}\\n` : '') +
                (displayPokok ? `📂 *${t.pokok}:* ${displayPokok}\\n` : '') +
                (uCount > 0 ? `📊 *${t.subMeta(uCount, vCount)}*\\n\\n` : '\\n') +
                `${t.learnMore}\\n${link}`;

            const waUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(message)}`;
            window.open(waUrl, '_blank');
        }"""

assert target_share_block in content, "target_share_block not found"
content = content.replace(target_share_block, replacement_share_block, 1)

# 3. Update checkAutoNav to sync language if &lang=... is in URL
target_autonav = """        function checkAutoNav() {
            if (!quranData || !Object.keys(quranData).length) return;

            const params = getParsedUrlParams();"""

replacement_autonav = """        function checkAutoNav() {
            if (!quranData || !Object.keys(quranData).length) return;

            const params = getParsedUrlParams();

            // Language sync from deep link (#...&lang=en-US)
            const paramLang = params.get('lang');
            if (paramLang && elTtsLanguage && elTtsLanguage.value !== paramLang) {
                elTtsLanguage.value = paramLang;
                elTtsLanguage.dispatchEvent(new Event('change'));
            }"""

assert target_autonav in content, "target_autonav not found"
content = content.replace(target_autonav, replacement_autonav, 1)

# 4. Update shareAyatWhatsApp to be multilingual and accept event
target_ayat_share = """        function shareAyatWhatsApp(surahName, surahNum, ayatNum) {
            const card = document.getElementById('current-rendered-verse');
            if (!card) return;
            const arabEl = card.querySelector('.search-arabic-box');
            const transEl = card.querySelector('.search-translation-box');
            const arab = arabEl ? arabEl.textContent.trim() : '';
            const trans = transEl ? transEl.textContent.trim() : '';
            const pageUrl = window.location.origin + window.location.pathname + `#surat=${surahNum}&ayat=${ayatNum}`;
            
            const msg = `📖 *QS. ${surahName} [${surahNum}] : Ayat ${ayatNum}*\\n\\n${arab}\\n\\n*Artinya:*\\n"${trans}"\\n\\n🔗 *Al-Qur'an Tematis:*\\n${pageUrl}`;
            const waUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(msg)}`;
            window.open(waUrl, '_blank');
        }"""

replacement_ayat_share = """        function shareAyatWhatsApp(surahName, surahNum, ayatNum, event) {
            if (event) event.stopPropagation();
            let card = null;
            if (event && event.target) {
                card = event.target.closest('.search-verse-card') || event.target.closest('.verse-item-wrapper');
            }
            if (!card) {
                card = document.getElementById('current-rendered-verse');
            }
            if (!card) return;

            const arabEl = card.querySelector('.search-arabic-box') || card.querySelector('.flip-card-back');
            const transEl = card.querySelector('.search-translation-box') || card.querySelector('.translation-text');
            const arab = arabEl ? arabEl.textContent.trim() : '';
            const trans = transEl ? transEl.textContent.trim() : '';

            const langSelect = document.getElementById('tts-language');
            const langKey = langSelect ? langSelect.value : 'id-ID';
            const cfg = LANG_CONFIG[langKey] || LANG_CONFIG['id-ID'];
            const targetLangCode = cfg.code;
            const t = getWhatsAppTemplates(targetLangCode);

            let pageUrl = window.location.origin + window.location.pathname + `#surat=${surahNum}&ayat=${ayatNum}`;
            if (langKey && langKey !== 'id-ID') {
                pageUrl += `&lang=${encodeURIComponent(langKey)}`;
            }

            const msg = `📖 *${t.quranPrefix} ${surahName} [${surahNum}] : ${t.ayahLabel} ${ayatNum}*\\n\\n${arab}\\n\\n*${t.meaningLabel}:*\\n"${trans}"\\n\\n🔗 *${t.appName}:*\\n${pageUrl}`;
            const waUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(msg)}`;
            window.open(waUrl, '_blank');
        }"""

assert target_ayat_share in content, "target_ayat_share not found"
content = content.replace(target_ayat_share, replacement_ayat_share, 1)

# 5. Pass event to shareAyatWhatsApp in search results
content = content.replace("shareAyatWhatsApp('${surahInfo.name}', ${surahNum}, ${ayatNum})", "shareAyatWhatsApp('${surahInfo.name}', ${surahNum}, ${ayatNum}, event)")
content = content.replace("shareAyatWhatsApp('${v.surah_name}', ${v.surah_num}, ${v.ayat_num})", "shareAyatWhatsApp('${v.surah_name}', ${v.surah_num}, ${v.ayat_num}, event)")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully applied multilingual WhatsApp share features to index.html!")
