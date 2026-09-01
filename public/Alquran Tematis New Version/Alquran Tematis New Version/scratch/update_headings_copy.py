import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for .title-copy-btn in <style>
title_copy_css = """        .title-copy-btn {
            background-color: rgba(56, 189, 248, 0.1);
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.35);
            padding: 0.25rem 0.65rem;
            border-radius: 999px;
            font-family: 'Inter', sans-serif;
            font-size: 0.78rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.25s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            line-height: 1.2;
            vertical-align: middle;
            user-select: none;
        }
        .title-copy-btn:hover {
            background-color: #38bdf8;
            color: #0b1120;
            border-color: #38bdf8;
            box-shadow: 0 0 12px rgba(56, 189, 248, 0.45);
            transform: translateY(-1px);
        }
        .title-copy-btn.is-copied {
            background-color: rgba(16, 185, 129, 0.2) !important;
            color: #10b981 !important;
            border-color: #10b981 !important;
            box-shadow: 0 0 12px rgba(16, 185, 129, 0.35);
        }
"""

if ".title-copy-btn" not in content:
    target = ".tts-button.ai-btn:hover {"
    content = content.replace(".tts-button.ai-btn:hover {\n            background-color: #8b5cf6;\n            color: #ffffff;\n            box-shadow: 0 0 15px rgba(139, 92, 246, 0.4);\n        }", ".tts-button.ai-btn:hover {\n            background-color: #8b5cf6;\n            color: #ffffff;\n            box-shadow: 0 0 15px rgba(139, 92, 246, 0.4);\n        }\n" + title_copy_css)
    print("Added .title-copy-btn CSS")

# 2. Add copyHeadingText JS function
copy_heading_func = """        function copyHeadingText(button, event, targetSelector) {
            if (event) {
                event.stopPropagation();
                event.preventDefault();
            }
            
            let text = '';
            const container = button.closest('.sub-header-title-row, .group-title-row, .sub-header-info, .group-header-left');
            if (container && targetSelector) {
                const titleEl = container.querySelector(targetSelector);
                if (titleEl && titleEl.textContent) {
                    text = titleEl.textContent.trim();
                }
            }
            if (!text && targetSelector) {
                const parent = button.parentElement;
                if (parent) {
                    const titleEl = parent.querySelector(targetSelector);
                    if (titleEl && titleEl.textContent) text = titleEl.textContent.trim();
                }
            }
            if (!text) return;

            const langSelect = document.getElementById('tts-language');
            const selectedLang = langSelect ? langSelect.value : 'id-ID';
            const cfg = LANG_CONFIG[selectedLang] || LANG_CONFIG['id-ID'];

            const doCopy = (str) => {
                if (navigator.clipboard && window.isSecureContext) {
                    return navigator.clipboard.writeText(str);
                } else {
                    const textArea = document.createElement("textarea");
                    textArea.value = str;
                    textArea.style.position = "fixed";
                    textArea.style.left = "-999999px";
                    textArea.style.top = "-999999px";
                    document.body.appendChild(textArea);
                    textArea.focus();
                    textArea.select();
                    return new Promise((resolve, reject) => {
                        try {
                            document.execCommand('copy');
                            textArea.remove();
                            resolve();
                        } catch (err) {
                            textArea.remove();
                            reject(err);
                        }
                    });
                }
            };

            doCopy(text).then(() => {
                const checkSvg = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`;
                button.innerHTML = checkSvg + `<span>${cfg.copiedText ? cfg.copiedText.trim() : 'Tersalin!'}</span>`;
                button.classList.add('is-copied');

                clearTimeout(button._copyTimeout);
                button._copyTimeout = setTimeout(() => {
                    const copySvg = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>`;
                    button.innerHTML = copySvg + `<span>${cfg.copyText ? cfg.copyText.trim() : 'Salin Teks Ini'}</span>`;
                    button.classList.remove('is-copied');
                }, 2000);
            }).catch(err => {
                console.error("Gagal menyalin judul:", err);
            });
        }

"""

if "function copyHeadingText(" not in content:
    content = content.replace("        function copyText(button, event) {", copy_heading_func + "        function copyText(button, event) {")
    print("Added copyHeadingText function")

# 3. Update generateUraianGroupMarkup for group header
old_group_header = """                        <div class="group-header-left">
                            <h3 class="group-title" data-original="${uraianTitle}">${uraianTitle}</h3>
                            <div class="group-meta" data-count="${data && data.verses ? data.verses.length : 0}">
                                <span>📖 ${data && data.verses ? data.verses.length : 0} Ayat Al-Qur'an</span>
                            </div>
                        </div>"""

new_group_header = """                        <div class="group-header-left">
                            <div class="group-title-row" style="display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap; margin: 0.25rem 0 0.5rem 0;">
                                <h3 class="group-title" data-original="${uraianTitle}" style="margin: 0;">${uraianTitle}</h3>
                                <button class="title-copy-btn" onclick="copyHeadingText(this, event, '.group-title')" title="Salin Teks Ini">
                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                                    <span>Salin Teks Ini</span>
                                </button>
                            </div>
                            <div class="group-meta" data-count="${data && data.verses ? data.verses.length : 0}">
                                <span>📖 ${data && data.verses ? data.verses.length : 0} Ayat Al-Qur'an</span>
                            </div>
                        </div>"""

if old_group_header in content:
    content = content.replace(old_group_header, new_group_header)
    print("Updated group header markup")
else:
    print("Warning: old_group_header not found directly, checking regex")
    content = re.sub(
        r'<div class="group-header-left">\s*<h3 class="group-title" data-original="\$\{uraianTitle\}">\$\{uraianTitle\}</h3>\s*<div class="group-meta" data-count="\$\{data && data\.verses \? data\.verses\.length : 0\}">\s*<span>📖 \$\{data && data\.verses \? data\.verses\.length : 0\} Ayat Al-Qur\'an</span>\s*</div>\s*</div>',
        new_group_header,
        content
    )
    print("Replaced group header via regex")

# 4. Update renderContentAll for sub header banner
old_sub_header = """                <div class="sub-header-banner-card">
                    <div class="sub-header-info">
                        <h2 class="sub-header-title" data-original="${sub}">${sub}</h2>
                        <div class="sub-header-meta" data-count="${keys.length}">Menampilkan ${keys.length} Kelompok Uraian Flash Card</div>
                    </div>
                </div>"""

new_sub_header = """                <div class="sub-header-banner-card">
                    <div class="sub-header-info">
                        <div class="sub-header-title-row" style="display: flex; align-items: center; gap: 0.85rem; flex-wrap: wrap;">
                            <h2 class="sub-header-title" data-original="${sub}" style="margin: 0;">${sub}</h2>
                            <button class="title-copy-btn" onclick="copyHeadingText(this, event, '.sub-header-title')" title="Salin Teks Ini">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                                <span>Salin Teks Ini</span>
                            </button>
                        </div>
                        <div class="sub-header-meta" data-count="${keys.length}" style="margin-top: 0.4rem;">Menampilkan ${keys.length} Kelompok Uraian Flash Card</div>
                    </div>
                </div>"""

if old_sub_header in content:
    content = content.replace(old_sub_header, new_sub_header)
    print("Updated sub header banner markup")
else:
    print("Warning: old_sub_header not found directly, checking regex")
    content = re.sub(
        r'<div class="sub-header-banner-card">\s*<div class="sub-header-info">\s*<h2 class="sub-header-title" data-original="\$\{sub\}">\$\{sub\}</h2>\s*<div class="sub-header-meta" data-count="\$\{keys\.length\}">Menampilkan \$\{keys\.length\} Kelompok Uraian Flash Card</div>\s*</div>\s*</div>',
        new_sub_header,
        content
    )
    print("Replaced sub header via regex")

# 5. Update translatePageContent to also update title-copy-btn
old_trans_snippet = """            const copyBtns = document.querySelectorAll('.copy-btn');
            copyBtns.forEach(btn => {
                if (!btn.classList.contains('is-copied')) {
                    const copySvg = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>`;
                    btn.innerHTML = copySvg + (cfg.copyText || ' Salin Teks Ini');
                    btn.setAttribute('title', cfg.copyTitle || (cfg.copyText ? cfg.copyText.trim() : 'Salin Teks Ini'));
                }
            });"""

new_trans_snippet = """            const copyBtns = document.querySelectorAll('.copy-btn');
            copyBtns.forEach(btn => {
                if (!btn.classList.contains('is-copied')) {
                    const copySvg = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>`;
                    btn.innerHTML = copySvg + (cfg.copyText || ' Salin Teks Ini');
                    btn.setAttribute('title', cfg.copyTitle || (cfg.copyText ? cfg.copyText.trim() : 'Salin Teks Ini'));
                }
            });

            const titleCopyBtns = document.querySelectorAll('.title-copy-btn');
            titleCopyBtns.forEach(btn => {
                if (!btn.classList.contains('is-copied')) {
                    const copySvg = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>`;
                    btn.innerHTML = copySvg + `<span>${cfg.copyText ? cfg.copyText.trim() : 'Salin Teks Ini'}</span>`;
                    btn.setAttribute('title', cfg.copyTitle || (cfg.copyText ? cfg.copyText.trim() : 'Salin Teks Ini'));
                }
            });"""

if old_trans_snippet in content and "const titleCopyBtns = document.querySelectorAll('.title-copy-btn');" not in content:
    content = content.replace(old_trans_snippet, new_trans_snippet)
    print("Updated translatePageContent with title-copy-btn")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Finished updating index.html")
