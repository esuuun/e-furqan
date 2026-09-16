#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full, flawless rewrite of renderAyatReferences and remaining functions in app.js
"""

import sys

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Cut code up to '// 2. Grand Unified Verse Card'
idx_cut = code.find('// 2. Grand Unified Verse Card')
assert idx_cut != -1, 'idx_cut not found'

new_tail = """// 2. Grand Unified Verse Card
    const cardWrapper = document.createElement('div');
    cardWrapper.className = 'single-ayat-card-wrapper';
    
    let activeSuratArti = occ.suratArtiID;
    let activeTeksArti = occ.teksArtiID || occ.teksArti;
    if (state.lang === 'en') {
      activeSuratArti = occ.suratArtiEN;
      activeTeksArti = occ.teksArtiEN || occ.teksArti;
    } else if (state.lang === 'ms') {
      activeSuratArti = occ.suratArtiMS;
      activeTeksArti = occ.teksArtiMS || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'fr') {
      activeSuratArti = occ.suratArtiFR;
      activeTeksArti = occ.teksArtiFR || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'de') {
      activeSuratArti = occ.suratArtiDE;
      activeTeksArti = occ.teksArtiDE || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'ur') {
      activeSuratArti = occ.suratArtiUR;
      activeTeksArti = occ.teksArtiUR || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'hi') {
      activeSuratArti = occ.suratArtiHI;
      activeTeksArti = occ.teksArtiHI || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'bn') {
      activeSuratArti = occ.suratArtiBN;
      activeTeksArti = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'ru') {
      activeSuratArti = occ.suratArtiRU;
      activeTeksArti = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'zh') {
      activeSuratArti = occ.suratArtiZH;
      activeTeksArti = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'es') {
      activeSuratArti = occ.suratArtiES || occ.suratArtiEN || '';
      activeTeksArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'tr') {
      activeSuratArti = occ.suratArtiTR || occ.suratArtiEN || '';
      activeTeksArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'pt') {
      activeSuratArti = occ.suratArtiPT || occ.suratArtiEN || '';
      activeTeksArti = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
    }

    cardWrapper.innerHTML = `
      <div class="single-ayat-unified-card animate-fade-in">
        <div class="ayat-top-row">
          <div class="surat-identity-badge">
            <div class="surat-number-circle surat-circle-gold">${occ.surat}</div>
            <div>
              <div class="surat-main-name">
                ${t('surahPrefix')} ${occ.suratNama} 
                <span class="surat-meaning-bracket">${activeSuratArti ? `(${activeSuratArti})` : ''}</span>
              </div>
              <div class="ayat-position-tag">${t('surahPositionTag', currentIdx + 1, occ.surat, occ.ayat)}</div>
            </div>
          </div>

          <div class="ayat-badge-actions">
            <!-- Audio Murottal Tilawah -->
            <button type="button" class="btn-play-verse-audio" data-surat="${occ.surat}" data-ayat="${occ.ayat}" data-audio="${occ.audioUrl || ''}" title="${t('playTilawahBtn')} (Mishary Alafasy)" aria-label="Putar Tilawah QS. ${occ.surat}:${occ.ayat}">
              <svg class="audio-icon-state" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <polygon points="5 3 19 12 5 21 5 3"></polygon>
              </svg>
            </button>

            <!-- Tombol Tanya AI -->
            <button type="button" class="btn-ask-ai" data-surat="${occ.surat}" data-ayat="${occ.ayat}" title="${t('askAiTooltip')}" aria-label="${t('askAiTooltip')}">
              <svg class="ai-sparkle-icon" width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2L14.4 7.6L20 10L14.4 12.4L12 18L9.6 12.4L4 10L9.6 7.6L12 2Z"/>
                <path d="M19 15L20.2 17.8L23 19L20.2 20.2L19 23L17.8 20.2L15 19L17.8 17.8L19 15Z"/>
              </svg>
              <span>${t('askAiBtn')}</span>
            </button>

            <span class="ayat-number-pill ayat-number-gold">${t('ayahPill', occ.ayat)}</span>
          </div>
        </div>

        <div class="ayat-body-content">
          <!-- 1. Teks Arab Penuh dengan Red Highlight -->
          <div class="arabic-verse-container">
            <div class="single-ayat-arabic-text font-arabic" dir="rtl">
              ${highlightArabicVerse(group, occ.teksArab || 'Teks Arab sedang dimuat...')}
            </div>
          </div>

          <!-- 2. Terjemahan Ayat dengan Tombol Audio Suara -->
          <div class="verse-translation-box">
            <div class="translation-content-row">
              <blockquote class="single-ayat-translation">
                "${activeTeksArti || 'Translation loading...'}"
              </blockquote>
              <button type="button" class="btn-play-translation-audio" data-surat="${occ.surat}" data-ayat="${occ.ayat}" title="${t('meaningVoiceTooltip')}" aria-label="${t('meaningVoiceTooltip')}">
                <svg class="audio-icon-state" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <polygon points="5 3 19 12 5 21 5 3"></polygon>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>
    `;

    // Explicit Flip Buttons inside the card
    cardWrapper.querySelectorAll('.flip-action-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        cardWrapper.classList.toggle('flipped');
      });
    });

    // Audio Play Buttons inside card (Murottal Tilawah)
    cardWrapper.querySelectorAll('.btn-play-verse-audio').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const surat = btn.getAttribute('data-surat');
        const ayat = btn.getAttribute('data-ayat');
        const audioUrl = btn.getAttribute('data-audio');
        toggleVerseAudio(surat, ayat, audioUrl);
      });
    });

    // Ask AI Button inside card
    cardWrapper.querySelectorAll('.btn-ask-ai').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        openAiModal(group, occ);
      });
    });

    // Audio Translation Buttons inside card
    cardWrapper.querySelectorAll('.btn-play-translation-audio').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const surat = btn.getAttribute('data-surat');
        const ayat = btn.getAttribute('data-ayat');
        toggleVerseTranslationAudio(occ.suratNama, surat, ayat, occ, btn);
      });
    });

    // Tab buttons event
    navBar.querySelectorAll('.ayat-select-tab').forEach(tab => {
      tab.addEventListener('click', (e) => {
        const targetIdx = parseInt(tab.getAttribute('data-idx'), 10);
        if (!isNaN(targetIdx) && targetIdx !== state.currentAyatIndex) {
          state.currentAyatIndex = targetIdx;
          renderAyatReferences(group, query);
        }
      });
    });

    // Prev / Next button events
    const prevBtn = navBar.querySelector('.btn-prev-ayat');
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (state.currentAyatIndex > 0) {
          state.currentAyatIndex--;
          renderAyatReferences(group, query);
        }
      });
    }

    const nextBtn = navBar.querySelector('.btn-next-ayat');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (state.currentAyatIndex < totalCount - 1) {
          state.currentAyatIndex++;
          renderAyatReferences(group, query);
        }
      });
    }

    // Assemble and mount
    singleScreenWrap.appendChild(navBar);
    singleScreenWrap.appendChild(cardWrapper);
    elements.ayatGridContainer.appendChild(singleScreenWrap);
  }

  // Update Visibility of Content Sections
  function updateViewVisibility() {
    const hasSelection = Boolean(state.selectedNoKata && getGroup(state.selectedBentuk, state.selectedNoKata));
    if (elements.spotlightCard) {
      elements.spotlightCard.style.display = hasSelection ? 'block' : 'none';
    }
    if (elements.referencesSection) {
      elements.referencesSection.style.display = hasSelection ? 'block' : 'none';
    }
  }

  // Bentuk Kata Selection Handler
  function selectBentuk(bentuk) {
    if (!bentuk) {
      state.selectedBentuk = '';
      state.selectedNoKata = '';
      elements.bentukKataSelect.value = '';
      populateNoKataDropdown();
      updateViewVisibility();
      return;
    }

    if (!availableBentukKatas.includes(bentuk)) return;

    state.selectedBentuk = bentuk;
    state.selectedNoKata = '';
    elements.bentukKataSelect.value = bentuk;
    populateNoKataDropdown();
    updateViewVisibility();
  }

  // Main Selection Handler
  function selectNoKata(noKata) {
    if (!noKata) {
      state.selectedNoKata = '';
      elements.noKataSelect.value = '';
      updateViewVisibility();
      return;
    }

    const currentGroup = getGroup(state.selectedBentuk, noKata);
    if (!currentGroup) return;

    state.selectedBentuk = currentGroup.bentuk;
    state.selectedNoKata = currentGroup.noKata;
    state.currentAyatIndex = 0;

    elements.bentukKataSelect.value = currentGroup.bentuk;
    elements.noKataSelect.value = currentGroup.noKata;

    updateViewVisibility();
    updateSpotlightCard(currentGroup);
    renderAyatReferences(currentGroup, elements.ayatSearchInput ? elements.ayatSearchInput.value : '');
  }

  // Language Switch Handler
  function applyLanguage(lang) {
    state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt'].includes(lang) ? lang : 'id';
    localStorage.setItem('dhamir_lang', state.lang);
    document.documentElement.lang = state.lang;

    // Update language select and translation badge
    if (elements.langSelect) {
      elements.langSelect.value = state.lang;
      elements.langSelect.setAttribute('aria-label', t('labelLangSelect'));
    }
    if (elements.labelLangSelect) elements.labelLangSelect.textContent = t('labelLangSelect');
    if (elements.translationSourceText) elements.translationSourceText.innerHTML = t('translationSourceHtml');

    // Update Static DOM text
    if (elements.docTitle) elements.docTitle.textContent = t('pageTitle');
    if (elements.brandTitle) elements.brandTitle.innerHTML = t('brandTitle');
    if (elements.brandSubtitle) elements.brandSubtitle.textContent = t('brandSubtitle');
    if (elements.themeToggleBtn) {
      elements.themeToggleBtn.setAttribute('title', t('themeToggleTitle'));
      elements.themeToggleBtn.setAttribute('aria-label', t('themeToggleTitle'));
    }
    
    if (elements.controlPanelTitle) elements.controlPanelTitle.textContent = t('controlPanelTitle');
    if (elements.step1Label) elements.step1Label.textContent = t('step1Label');
    if (elements.step2Label) elements.step2Label.textContent = t('step2Label');
    if (elements.bentukKataSelect) elements.bentukKataSelect.setAttribute('aria-label', t('step1Label'));
    if (elements.noKataSelect) elements.noKataSelect.setAttribute('aria-label', t('step2Label'));
    
    if (elements.labelAudioArab) elements.labelAudioArab.textContent = t('arabicVoiceBtn');
    if (elements.btnAudioPlay) elements.btnAudioPlay.setAttribute('title', t('arabicVoiceTooltip'));
    if (elements.labelAudioMeaning) elements.labelAudioMeaning.textContent = t('meaningVoiceBtn');
    if (elements.btnAudioMeaning) elements.btnAudioMeaning.setAttribute('title', t('meaningVoiceTooltip'));
    if (elements.btnCopyArabic) elements.btnCopyArabic.setAttribute('title', t('copyArabicTooltip'));
    if (elements.labelCopyInfo) elements.labelCopyInfo.textContent = t('copyInfoBtn');
    if (elements.btnCopyAll) elements.btnCopyAll.setAttribute('title', t('copyInfoTooltip'));
    
    if (elements.labelFreqTitle) elements.labelFreqTitle.textContent = t('freqLabel');
    if (elements.labelTotalAyatTitle) elements.labelTotalAyatTitle.textContent = t('totalAyatLabel');
    if (elements.labelTotalAyatSub) elements.labelTotalAyatSub.textContent = t('totalAyatSub');
    if (elements.labelExportCsv) elements.labelExportCsv.textContent = t('exportCsvBtn');
    if (elements.btnExportCsv) elements.btnExportCsv.setAttribute('title', t('exportCsvTooltip'));
    if (elements.ayatSearchInput) elements.ayatSearchInput.setAttribute('placeholder', t('searchPlaceholder'));
    if (elements.emptyStateText) elements.emptyStateText.textContent = t('emptyStateText');

    // AI Modal Text & Tooltips
    if (elements.aiModalTitle) elements.aiModalTitle.textContent = t('aiModalTitle');
    if (elements.aiModalCloseBtn) {
      elements.aiModalCloseBtn.setAttribute('title', t('closeBtn'));
      elements.aiModalCloseBtn.setAttribute('aria-label', t('closeBtn'));
    }
    if (elements.labelAiTopic) elements.labelAiTopic.textContent = t('aiTopicLabel');
    if (elements.labelPromptPreview) elements.labelPromptPreview.textContent = t('aiPromptPreviewLabel');
    if (elements.labelOpenGemini) elements.labelOpenGemini.textContent = t('aiOpenGemini');
    if (elements.btnOpenGemini) elements.btnOpenGemini.setAttribute('title', t('aiOpenGemini'));
    if (elements.labelOpenChatGpt) elements.labelOpenChatGpt.textContent = t('aiOpenChatGpt');
    if (elements.btnOpenChatGpt) elements.btnOpenChatGpt.setAttribute('title', t('aiOpenChatGpt'));
    if (elements.labelCopyPrompt) elements.labelCopyPrompt.textContent = t('aiCopyPrompt');
    if (elements.btnCopyPrompt) elements.btnCopyPrompt.setAttribute('title', t('aiCopyPrompt'));
    if (elements.aiTopicChips) {
      const chipNahwu = elements.aiTopicChips.querySelector('[data-topic="nahwu"]');
      const chipTafsir = elements.aiTopicChips.querySelector('[data-topic="tafsir"]');
      const chipBalaghah = elements.aiTopicChips.querySelector('[data-topic="balaghah"]');
      if (chipNahwu) chipNahwu.textContent = t('aiTopicNahwu');
      if (chipTafsir) chipTafsir.textContent = t('aiTopicTafsir');
      if (chipBalaghah) chipBalaghah.textContent = t('aiTopicBalaghah');
    }
    if (currentAiContext.group && currentAiContext.occ) {
      updateAiModalPrompt();
    }

    // Refresh Dropdowns
    populateBentukDropdown();
    populateNoKataDropdown();

    // Refresh Active Card & Verses or Welcome State
    const currentGroup = getGroup(state.selectedBentuk, state.selectedNoKata);
    if (currentGroup) {
      updateSpotlightCard(currentGroup);
      renderAyatReferences(currentGroup, elements.ayatSearchInput ? elements.ayatSearchInput.value : '');
    }
    updateViewVisibility();
  }

  // AI Assistant Modal State & Logic
  const currentAiContext = {
    group: null,
    occ: null,
    topic: 'nahwu'
  };

  function buildAiPrompt(group, occ, topic) {
    if (!group || !occ) return '';
    const suratNama = occ.suratNama;
    const surat = occ.surat;
    const ayat = occ.ayat;
    const kata = group.kata;
    const noKata = group.noKata;
    const bentuk = group.bentuk;
    const teksArab = occ.teksArab || '';
    let teksArti = occ.teksArtiID || occ.teksArti;
    let grammarDesc = (group.grammar && (group.grammar.desc_id || group.grammar.keterangan)) || '';
    if (state.lang === 'en') {
      teksArti = occ.teksArtiEN || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_en || group.grammar.keterangan)) || '';
    } else if (state.lang === 'ms') {
      teksArti = occ.teksArtiMS || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_ms || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'fr') {
      teksArti = occ.teksArtiFR || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_fr || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'de') {
      teksArti = occ.teksArtiDE || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_de || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'ur') {
      teksArti = occ.teksArtiUR || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_ur || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'hi') {
      teksArti = occ.teksArtiHI || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_hi || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'bn') {
      teksArti = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_bn || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'ru') {
      teksArti = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_ru || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'zh') {
      teksArti = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_zh || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'es') {
      teksArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_es || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'tr') {
      teksArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_tr || group.grammar.desc_id || group.grammar.keterangan)) || '';
    } else if (state.lang === 'pt') {
      teksArti = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_pt || group.grammar.desc_id || group.grammar.keterangan)) || '';
    }

    if (state.lang === 'en') {
      if (topic === 'nahwu') {
        return `Please explain in detail the Arabic grammar (Nahwu/Sarf) and I'rab for the word "${kata}" (${noKata}, ${bentuk}) in Quran Surah ${suratNama} (${surat}): Ayah ${ayat}:\\n\\nArabic: "${teksArab}"\\nTranslation: "${teksArti}"\\n\\nPlease cover:\\n1. Grammatical role / I'rab of "${kata}" in this sentence structure.\\n2. Morphological category (Dhamir/Mawshul type) and case (Marfu'/Manshub/Majrur).\\n3. Grammar notes: ${grammarDesc || "Standard Quranic usage"}.`;
      } else if (topic === 'tafsir') {
        return `Please provide a concise contextual Tafsir explanation for Quran Surah ${suratNama} (${surat}): Ayah ${ayat}:\\n\\nArabic: "${teksArab}"\\nTranslation: "${teksArti}"\\n\\nFocusing on the significance of the pronoun/word "${kata}", what is the core wisdom, context of revelation (asbabun nuzul if applicable), and theological message conveyed in this ayah?`;
      } else {
        return `Explain the Quranic Balaghah (Rhetorical Beauty & Stylistics) regarding the word choice "${kata}" in Surah ${suratNama} (${surat}) Ayah ${ayat}:\\n\\nArabic: "${teksArab}"\\nTranslation: "${teksArti}"\\n\\nWhy is this specific pronoun form used here? What subtle nuances, emphasis, or aesthetic eloquence does it add to the verse?`;
      }
    } else if (state.lang === 'ms') {
      if (topic === 'nahwu') {
        return `Mohon jelaskan secara terperinci kedudukan I'rab dan kaedah tatabahasa Nahwu/Saraf untuk kata "${kata}" (${noKata}, ${bentuk}) yang terdapat dalam Al-Qur'an Surah ${suratNama} (${surat}) ayat ${ayat}:\\n\\nTeks Arab: "${teksArab}"\\nTerjemahan: "${teksArti}"\\n\\nSila terangkan:\\n1. Kedudukan I'rab kata "${kata}" dalam susunan ayat ini.\\n2. Jenis kata (Dhamir Munfashil/Muttashil atau Isim Mawshul) berserta status kedudukannya (rafa'/nashab/jar).\\n3. Catatan kaedah: ${grammarDesc || "Kaedah piawai Al-Qur'an"}.`;
      } else if (topic === 'tafsir') {
        return `Mohon berikan penjelasan tafsir ringkas dan kontekstual berkenaan Surah ${suratNama} (${surat}) ayat ${ayat}:\\n\\nTeks Arab: "${teksArab}"\\nTerjemahan: "${teksArti}"\\n\\nDengan tumpuan kepada maksud kata "${kata}", apakah mesej utama, hikmah, serta konteks makna yang terkandung dalam ayat ini?`;
      } else {
        return `Jelaskan rahsia keindahan bahasa Al-Qur'an (Balaghah & Uslub) dalam pemilihan kata "${kata}" pada Surah ${suratNama} (${surat}) ayat ${ayat}:\\n\\nTeks Arab: "${teksArab}"\\nTerjemahan: "${teksArti}"\\n\\nMengapa Allah menggunakan bentuk kata ini dalam susunan ayat tersebut? Apakah rahsia keindahan sastera dan makna mendalamnya?`;
      }
    } else if (state.lang === 'fr') {
      if (topic === 'nahwu') {
        return `Veuillez expliquer en détail la grammaire arabe (Nahwu/Sarf) et l'I'rab pour le mot "${kata}" (${noKata}, ${bentuk}) dans le Coran, Sourate ${suratNama} (${surat}) : Verset ${ayat} :\\n\\nTexte Arabe : "${teksArab}"\\nTraduction : "${teksArti}"\\n\\nVeuillez détailler :\\n1. Le rôle grammatical / I'rab de "${kata}" dans cette structure de phrase.\\n2. La catégorie morphologique (type de Dhamir/Mawshul) et le cas (Marfu'/Manshub/Majrur).\\n3. Remarques grammaticales : ${grammarDesc || "Usage coranique standard"}.`;
      } else if (topic === 'tafsir') {
        return `Veuillez fournir une explication concise et contextuelle de Tafsir pour la Sourate ${suratNama} (${surat}) : Verset ${ayat} :\\n\\nTexte Arabe : "${teksArab}"\\nTraduction : "${teksArti}"\\n\\nEn mettant l'accent sur la portée du pronom / mot "${kata}", quelle est la sagesse fondamentale, le contexte de révélation (asbab an-nuzul le cas échéant) et le message théologique transmis dans ce verset ?`;
      } else {
        return `Expliquez la Balaghah coranique (Beauté rhétorique & stylistique) concernant le choix du mot "${kata}" dans la Sourate ${suratNama} (${surat}) Verset ${ayat} :\\n\\nTexte Arabe : "${teksArab}"\\nTraduction : "${teksArti}"\\n\\nPourquoi cette forme spécifique de pronom est-elle employée ici ? Quelles nuances subtiles, emphase ou éloquence esthétique apporte-t-elle au verset ?`;
      }
    } else if (state.lang === 'de') {
      if (topic === 'nahwu') {
        return `Bitte erklären Sie ausführlich die arabische Grammatik (Nahw/Sarf) und das I'rab für das Wort "${kata}" (${noKata}, ${bentuk}) im Koran, Sure ${suratNama} (${surat}) : Vers ${ayat}:\\n\\nArabischer Text: "${teksArab}"\\nÜbersetzung: "${teksArti}"\\n\\nBitte erläutern Sie:\\n1. Die grammatikalische Funktion / I'rab von "${kata}" in dieser Satzstruktur.\\n2. Die morphologische Kategorie (Art des Dhamir / Mawshul) und den Fall (Marfu'/Manshub/Majrur).\\n3. Grammatikalische Anmerkungen: ${grammarDesc || "Standardmäßiger koranischer Sprachgebrauch"}.`;
      } else if (topic === 'tafsir') {
        return `Bitte geben Sie eine prägnante und kontextbezogene Tafsir-Erklärung für Sure ${suratNama} (${surat}) : Vers ${ayat}:\\n\\nArabischer Text: "${teksArab}"\\nÜbersetzung: "${teksArti}"\\n\\nMit Fokus auf die Bedeutung des Pronomens / Wortes "${kata}": Was ist die wesentliche Weisheit, der Offenbarungsanlass (Asbab an-Nuzul, falls zutreffend) und die theologische Botschaft dieses Verses?`;
      } else {
        return `Erklären Sie die koranische Balagha (Rhetorische Schönheit & Stilistik) bezüglich der Wortwahl "${kata}" in Sure ${suratNama} (${surat}) Vers ${ayat}:\\n\\nArabischer Text: "${teksArab}"\\nÜbersetzung: "${teksArti}"\\n\\nWarum wird hier genau diese Pronomenform verwendet? Welche feinen Nuancen, Betonungen oder ästhetische Eloquenz verleiht sie dem Vers?`;
      }
    } else if (state.lang === 'ur') {
      if (topic === 'nahwu') {
        return `براہ کرم قرآن مجید کی سورۃ ${suratNama} (${surat}) آیت ${ayat} میں موجود لفظ "${kata}" (${noKata}، ${bentuk}) کے عربی قواعد و نحوی اعراب کی مفصل وضاحت کریں:\\n\\nعربی متن: "${teksArab}"\\nترجمہ: "${teksArti}"\\n\\nبراہ کرم درج ذیل نکات شامل کریں:\\n۱. اس جملے کی ترکیب میں "${kata}" کا نحوی کردار اور اعراب۔\\n۲. لفظ کی نوعیت (ضمیر منفصل/متصل یا اسم موصول) اور اس کی اعرابی حالت (مرفوع/منصوب/مجرور)۔\\n۳. نحوی نوٹس: ${grammarDesc || "قرآنی معیاری استعمال"}۔`;
      } else if (topic === 'tafsir') {
        return `براہ کرم سورۃ ${suratNama} (${surat}) آیت ${ayat} کی مختصر اور سیاق و سباق کے مطابق تفسیری وضاحت پیش کریں:\\n\\nعربی متن: "${teksArab}"\\nترجمہ: "${teksArti}"\\n\\nخاص طور پر لفظ/ضمیر "${kata}" کی اہمیت کو مدنظر رکھتے ہوئے، اس آیت میں کیا بنیادی حکمت، شان نزول اور الٰہی پیغام بیان کیا گیا ہے؟`;
      } else {
        return `سورۃ ${suratNama} (${surat}) آیت ${ayat} میں لفظ "${kata}" کے انتخاب کے حوالے سے قرآنی بلاغت اور اسلوب کی خوبصورتی بیان کریں:\\n\\nعربی متن: "${teksArab}"\\nترجمہ: "${teksArti}"\\n\\nیہاں پر ضمیر کی یہی مخصوص شکل کیوں استعمال ہوئی ہے؟ یہ آیت کے حسن اور معنوی گہرائی میں کیا نکھار پیدا کرتی ہے؟`;
      }
    } else if (state.lang === 'hi') {
      if (topic === 'nahwu') {
        return `कृपया क़ुरआन मजीद की सूरह ${suratNama} (${surat}) आयत ${ayat} में उपस्थित शब्द "${kata}" (${noKata}, ${bentuk}) के अरबी व्याकरण (नहव/सर्फ़) और ए'राब की विस्तृत व्याख्या करें:\\n\\nअरबी पाठ: "${teksArab}"\\nअनुवाद: "${teksArti}"\\n\\nकृपया निम्नलिखित बिंदुओं को शामिल करें:\\n१. इस वाक्य रचना में "${kata}" की व्याकरणिक भूमिका और ए'राब (I'rab)।\\n२. शब्द का रूप (ज़मीर मुन्फ़सिल/मुत्तसिल या इस्म मौसूल) और इसकी स्थिति (रफ़ा/नसब/जर)।\\n३. व्याकरणिक टिप्पणी: ${grammarDesc || "मानक क़ुरआनी प्रयोग"}।`;
      } else if (topic === 'tafsir') {
        return `कृपया सूरह ${suratNama} (${surat}) आयत ${ayat} की संक्षिप्त और संदर्भात्मक तफ़सीर (व्याख्या) प्रस्तुत करें:\\n\\nअरबी पाठ: "${teksArab}"\\nअनुवाद: "${teksArti}"\\n\\nविशेष रूप से शब्द/सर्वनाम "${kata}" के महत्व पर ध्यान केंद्रित करते हुए बताएं कि इस आयत में क्या मुख्य शिक्षा, अवतरण का संदर्भ और ईश्वरीय संदेश निहित है?`;
      } else {
        return `सूरह ${suratNama} (${surat}) आयत ${ayat} में शब्द "${kata}" के चयन के संबंध में क़ुरानी बलाग़त (अलंकारिक सौंदर्य व शैली) की व्याख्या करें:\\n\\nअरबी पाठ: "${teksArab}"\\nअनुवाद: "${teksArti}"\\n\\nयहाँ पर सर्वनाम का यही विशिष्ट रूप क्यों प्रयुक्त हुआ है? यह आयत के अर्थ की गहराई और साहित्यिक सौंदर्य में क्या वृद्धि करता है?`;
      }
    } else if (state.lang === 'bn') {
      if (topic === 'nahwu') {
        return `অনুগ্রহ করে পবিত্র কুরআনের সূরা ${suratNama} (${surat}) আয়াত ${ayat}-এ অবস্থিত শব্দ "${kata}" (${noKata}, ${bentuk})-এর আরবি ব্যাকরণ (নাহব/সরফ) ও ই'রাব বিস্তারিতভাবে ব্যাখ্যা করুন:\\n\\nআরবি পাঠ: "${teksArab}"\\nঅনুবাদ: "${teksArti}"\\n\\nঅনুগ্রহ করে নিম্নলিখিত বিষয়গুলো আলোচনা করুন:\\n১. এই বাক্যের গঠনে "${kata}"-এর ব্যাকরণগত ভূমিকা ও ই'রাব (I'rab)।\\n২. শব্দের রূপগত প্রকার (যমীর মুনফাসিল/মুত্তাসিল অথবা ইসম মাওসুল) এবং এর অবস্থা (মারফু'/মানসুব/মাজরুর)।\\n৩. ব্যাকরণগত নোট: ${grammarDesc || "প্রমিত কুরআনিক প্রয়োগ"}।`;
      } else if (topic === 'tafsir') {
        return `অনুগ্রহ করে সূরা ${suratNama} (${surat}) আয়াত ${ayat}-এর সংক্ষিপ্ত ও প্রাসঙ্গিক তাফসির (ব্যাখ্যা) উপস্থাপন করুন:\\n\\nআরবি পাঠ: "${teksArab}"\\nঅনুবাদ: "${teksArti}"\\n\\nবিশেষ করে শব্দ/সর্বনাম "${kata}"-এর তাৎপর্যের ওপর গুরুত্ব দিয়ে বলুন, এই আয়াতে কী মূল হেকমত, শানে নুযূল এবং ঐশী বার্তা নিহিত রয়েছে?`;
      } else {
        return `সূরা ${suratNama} (${surat}) আয়াত ${ayat}-এ শব্দ "${kata}" নির্বাচনের ক্ষেত্রে কুরআনিক বালাগাত (অলঙ্কারিক সৌন্দর্য ও রচনাশৈলী) ব্যাখ্যা করুন:\\n\\nআরবি পাঠ: "${teksArab}"\\nঅনুবাদ: "${teksArti}"\\n\\nএখানে সর্বনামের এই নির্দিষ্ট রূপটি কেন ব্যবহৃত হয়েছে? এটি আয়াতের অর্থ ও সাহিত্যের গভীরতায় কী সৌন্দর্য যোগ করে?`;
      }
    } else if (state.lang === 'ru') {
      if (topic === 'nahwu') {
        return `Пожалуйста, подробно объясните арабскую грамматику (нахву/сарф) и и'раб (синтаксический разбор) слова "${kata}" (${noKata}, ${bentuk}) в Суре ${suratNama} (${surat}), аят ${ayat}:\\n\\nАрабский текст: "${teksArab}"\\nПеревод: "${teksArti}"\\n\\nПожалуйста, включите следующие пункты:\\n1. Грамматическая роль "${kata}" в структуре этого предложения и его и'раб (падежное состояние: марфу'/мансуб/маджрур).\\n2. Морфологическая классификация (Дамир мунфасыль/муттасыль или Исм маусуль).\\n3. Грамматическое примечание: ${grammarDesc || "Классическое кораническое употребление"}.`;
      } else if (topic === 'tafsir') {
        return `Пожалуйста, представьте краткий и контекстуальный тафсир (толкование) Суры ${suratNama} (${surat}), аят ${ayat}:\\n\\nАрабский текст: "${teksArab}"\\nПеревод: "${teksArti}"\\n\\nУделив особое внимание значению слова/местоимения "${kata}", объясните, какой главный смысл, повод ниспослания (сабаб ан-нузуль) и духовное наставление заключены в этом аяте?`;
      } else {
        return `Объясните кораническую риторику и стилистику (баляга) в выборе слова "${kata}" в Суре ${suratNama} (${surat}), аят ${ayat}:\\n\\nАрабский текст: "${teksArab}"\\nПеревод: "${teksArti}"\\n\\nПочему здесь использована именно эта конкретная грамматическая форма? Какую смысловую глубину и красоту она придает аяту?`;
      }
    } else if (state.lang === 'zh') {
      if (topic === 'nahwu') {
        return `请详细解析古兰经苏拉 ${suratNama} (${surat}) 第 ${ayat} 节中词汇 "${kata}" (${noKata}, ${bentuk}) 的阿拉伯语语法 (Nahwu / Sarf) 及语法定位 (I'rab)：\\n\\n阿拉伯语原文: "${teksArab}"\\n中文译文: "${teksArti}"\\n\\n请包含以下要点：\\n1. "${kata}" 在该句子结构中的语法成分与格位状态 (主格/宾格/属格/断格)。\\n2. 词形形态分类 (独立人称代词/接尾人称代词/关系代词)。\\n3. 语法特别说明: ${grammarDesc || "标准古兰经语言用法"}。`;
      } else if (topic === 'tafsir') {
        return `请对苏拉 ${suratNama} (${surat}) 第 ${ayat} 节提供简明且结合语境的经注 (Tafsir) 与内涵阐释：\\n\\n阿拉伯语原文: "${teksArab}"\\n中文译文: "${teksArti}"\\n\\n请重点结合词汇/代词 "${kata}" 的用法，阐明本节经文所蕴含的核心教诲、启示背景 (Sabab al-Nuzul) 以及精神指导意义？`;
      } else {
        return `请赏析苏拉 ${suratNama} (${surat}) 第 ${ayat} 节中选用词汇 "${kata}" 的古兰经修辞美学 (Balaghah) 与文体风格：\\n\\n阿拉伯语原文: "${teksArab}"\\n中文译文: "${teksArti}"\\n\\n为什么此处使用了该特定词形？它为经文的意境深度与文学表现力增添了怎样的色彩？`;
      }
    } else if (state.lang === 'es') {
      if (topic === 'nahwu') {
        return `Por favor explique en detalle la gramática árabe (Nahw/Sarf) y el I'rab para la palabra "${kata}" (${noKata}, ${bentuk}) en el Corán, Sura ${suratNama} (${surat}): Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTraducción: "${teksArti}"\\n\\nPor favor detalle:\\n1. La función sintáctica / posición de I'rab de "${kata}" en la estructura de esta oración.\\n2. Categoría morfológica (tipo de Dhamir / Mawshul) y caso (Marfu'/Manshub/Mayrur).\\n3. Notas gramaticales: ${grammarDesc || "Uso estándar en el Corán"}.`;
      } else if (topic === 'tafsir') {
        return `Por favor proporcione una explicación concisa y contextual de Tafsir para la Sura ${suratNama} (${surat}): Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTraducción: "${teksArti}"\\n\\nCon enfoque en el significado y trascendencia del pronombre / palabra "${kata}", ¿cuál es la sabiduría principal, contexto de revelación (asbab an-nuzul si aplica) y mensaje teológico transmitido en este versículo?`;
      } else {
        return `Explique la Balaghah coránica (Belleza retórica y estilística) en cuanto a la elección de la palabra "${kata}" en la Sura ${suratNama} (${surat}) Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTraducción: "${teksArti}"\\n\\n¿Por qué se emplea esta forma específica de pronombre aquí? ¿Qué matices sutiles, énfasis o elocuencia estética aporta al versículo?`;
      }
    } else if (state.lang === 'tr') {
      if (topic === 'nahwu') {
        return `Lütfen Kur'an-ı Kerim ${suratNama} Suresi (${surat}), ${ayat}. Ayetinde geçen "${kata}" (${noKata}, ${bentuk}) kelimesinin Arapça Nahiv/Sarf kurallarını ve İ'rab analizini ayrıntılı olarak açıklayınız:\\n\\nArapça Metin: "${teksArab}"\\nTürkçe Meali: "${teksArti}"\\n\\nLütfen şu hususları detaylandırınız:\\n1. "${kata}" kelimesinin cümle içindeki sentaktik konumu ve İ'rab alameti (Merfû / Mansûb / Mecrûr).\\n2. Morfolojik kategorisi (Dhamir / Mevsul / Şart vb. türü) ve zamir özellikleri (Munfasıl / Muttasıl vb.).\\n3. Gramer notları: ${grammarDesc || "Kur'an'daki standart kullanımı"}.`;
      } else if (topic === 'tafsir') {
        return `Lütfen ${suratNama} Suresi (${surat}), ${ayat}. Ayeti için özlü ve bağlamsal bir Tefsir açıklaması sununuz:\\n\\nArapça Metin: "${teksArab}"\\nTürkçe Meali: "${teksArti}"\\n\\nÖzellikle seçilen "${kata}" kelimesine / zamirine odaklanarak; bu ayetin temel hikmeti, nüzul sebebi (varsa sebebi nüzul) ve içerdiği teolojik mesaj nedir?`;
      } else {
        return `Lütfen ${suratNama} Suresi (${surat}), ${ayat}. Ayetinde "${kata}" kelimesinin tercih edilmesindeki Kur'an Belâğatı ve edebî incelikleri açıklayınız:\\n\\nArapça Metin: "${teksArab}"\\nTürkçe Meali: "${teksArti}"\\n\\nNeden özellikle bu zamir / kelime formu tercih edilmiştir? Ayetin ahengine, anlamına ve vurgusuna ne gibi bir edebî derinlik katmaktadır?`;
      }
    } else if (state.lang === 'pt') {
      if (topic === 'nahwu') {
        return `Por favor, explique em detalhes a gramática árabe (Nahwu/Sarf) e a análise de I'rab para a palavra "${kata}" (${noKata}, ${bentuk}) na Surata ${suratNama} (${surat}): Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTradução: "${teksArti}"\\n\\nPor favor, aborde os seguintes pontos:\\n1. Função sintática e posição de I'rab de "${kata}" na estrutura desta oração (Marfu' / Manshub / Majrur).\\n2. Categoria morfológica (tipo de Dhamir / Mawshul / etc.) e propriedades do pronome (Munfashil / Muttashil).\\n3. Notas gramaticais: ${grammarDesc || "Uso alcorânico padrão"}.`;
      } else if (topic === 'tafsir') {
        return `Por favor, forneça uma explicação concisa e contextual de Tafsir para a Surata ${suratNama} (${surat}): Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTradução: "${teksArti}"\\n\\nCom foco especial no significado da palavra/pronome "${kata}": qual é a sabedoria principal, contexto de revelação (asbab an-nuzul, se aplicável) e a mensagem teológica transmitida neste versículo?`;
      } else {
        return `Explique a Balaghah alcorânica (Eloquência retórica e estilística) em relação à escolha da palavra "${kata}" na Surata ${suratNama} (${surat}) Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTradução: "${teksArti}"\\n\\nPor que essa forma específica de pronome foi utilizada aqui? Que nuances sutis, ênfase ou profundidade estética ela adiciona ao versículo?`;
      }
    } else {
      if (topic === 'nahwu') {
        return `Mohon jelaskan secara mendalam kedudukan I'rab dan kaidah tata bahasa Nahwu/Sharaf untuk kata "${kata}" (${noKata}, ${bentuk}) yang terdapat dalam Al-Qur'an Surat ${suratNama} (${surat}) ayat ${ayat}:\\n\\nTeks Arab: "${teksArab}"\\nTerjemahan: "${teksArti}"\\n\\nMohon jelaskan:\\n1. Kedudukan I'rab kata "${kata}" dalam susunan kalimat ini.\\n2. Jenis kata (Dhamir Munfashil/Muttashil atau Isim Mawshul) beserta status kedudukannya (rafa'/nashab/jar).\\n3. Catatan kaidah: ${grammarDesc || "Kaidah standar Al-Qur'an"}.`;
      } else if (topic === 'tafsir') {
        return `Mohon berikan penjelasan tafsir ringkas dan kontekstual mengenai Surat ${suratNama} (${surat}) ayat ${ayat}:\\n\\nTeks Arab: "${teksArab}"\\nTerjemahan: "${teksArti}"\\n\\nDengan fokus pada makna kata "${kata}", apa pesan utama, hikmah, serta konteks makna yang terkandung dalam ayat ini?`;
      } else {
        return `Jelaskan rahsia keindahan bahasa Al-Qur'an (Balaghah & Uslub) dalam pemilihan kata "${kata}" pada Surat ${suratNama} (${surat}) ayat ${ayat}:\\n\\nTeks Arab: "${teksArab}"\\nTerjemahan: "${teksArti}"\\n\\nMengapa Allah menggunakan bentuk kata ini dalam susunan ayat tersebut? Apa rahasia keindahan sastra dan makna mendalamnya?`;
      }
    }
  }

  function openAiModal(group, occ) {
    if (!group || !occ || !elements.aiModal) return;
    currentAiContext.group = group;
    currentAiContext.occ = occ;

    if (elements.aiModalArabicVerse) {
      elements.aiModalArabicVerse.innerHTML = highlightArabicVerse(group, occ.teksArab || '');
    }
    if (elements.aiModalTranslation) {
      let activeArti = occ.teksArtiID || occ.teksArti;
      if (state.lang === 'en') {
        activeArti = occ.teksArtiEN || occ.teksArti;
      } else if (state.lang === 'ms') {
        activeArti = occ.teksArtiMS || occ.teksArtiID || occ.teksArti;
      } else if (state.lang === 'fr') {
        activeArti = occ.teksArtiFR || occ.teksArtiID || occ.teksArti;
      } else if (state.lang === 'de') {
        activeArti = occ.teksArtiDE || occ.teksArtiID || occ.teksArti;
      } else if (state.lang === 'ur') {
        activeArti = occ.teksArtiUR || occ.teksArtiID || occ.teksArti;
      } else if (state.lang === 'hi') {
        activeArti = occ.teksArtiHI || occ.teksArtiID || occ.teksArti;
      } else if (state.lang === 'bn') {
        activeArti = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
      } else if (state.lang === 'ru') {
        activeArti = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
      } else if (state.lang === 'zh') {
        activeArti = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;
      } else if (state.lang === 'es') {
        activeArti = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
      } else if (state.lang === 'tr') {
        activeArti = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
      } else if (state.lang === 'pt') {
        activeArti = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
      }
      elements.aiModalTranslation.textContent = `"${activeArti || ''}"`;
    }
    if (elements.aiModalSubtitle) {
      elements.aiModalSubtitle.textContent = t('aiModalSubtitle', occ.suratNama, occ.ayat, group.kata, group.noKata);
    }

    updateAiModalPrompt();

    elements.aiModal.classList.add('open');
    elements.aiModal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function closeAiModal() {
    if (!elements.aiModal) return;
    elements.aiModal.classList.remove('open');
    elements.aiModal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  function updateAiModalPrompt() {
    if (!currentAiContext.group || !currentAiContext.occ) return;
    const prompt = buildAiPrompt(currentAiContext.group, currentAiContext.occ, currentAiContext.topic);
    if (elements.aiPromptTextarea) {
      elements.aiPromptTextarea.value = prompt;
    }
  }

  function openInGemini() {
    const prompt = elements.aiPromptTextarea ? elements.aiPromptTextarea.value : '';
    if (!prompt) return;
    if (navigator.clipboard) {
      navigator.clipboard.writeText(prompt).catch(() => {});
    }
    showToast(t('toastPromptCopied'));
    window.open('https://gemini.google.com/app', '_blank', 'noopener,noreferrer');
  }

  function openInChatGpt() {
    const prompt = elements.aiPromptTextarea ? elements.aiPromptTextarea.value : '';
    if (!prompt) return;
    if (navigator.clipboard) {
      navigator.clipboard.writeText(prompt).catch(() => {});
    }
    showToast(t('toastPromptCopied'));
    window.open(`https://chatgpt.com/?q=${encodeURIComponent(prompt)}`, '_blank', 'noopener,noreferrer');
  }

  function copyAiPrompt() {
    const prompt = elements.aiPromptTextarea ? elements.aiPromptTextarea.value : '';
    if (!prompt) return;
    if (navigator.clipboard) {
      navigator.clipboard.writeText(prompt).then(() => {
        showToast(t('toastPromptCopied'));
      }).catch(() => {
        showToast('Gagal menyalin prompt.');
      });
    }
  }

  // Toast Notification
  function showToast(message) {
    elements.toast.textContent = message;
    elements.toast.classList.add('show');
    setTimeout(() => {
      elements.toast.classList.remove('show');
    }, 2500);
  }

  // Export to CSV
  function exportToCsv() {
    const group = getGroup(state.selectedBentuk, state.selectedNoKata);
    if (!group) return;

    let csvContent = '\\uFEFF'; // UTF-8 BOM
    csvContent += 'Bentuk Kata,No Kata,Kata Arab,Transliterasi Latin,Arti Kata (ID),Meaning (EN),Maksud Kata (MS),Signification (FR),Bedeutung (DE),Mani (UR),Artha (HI),Orthobhed (BN),Znachenie (RU),Biaoda (ZH),Significado (ES),Meal (TR),Significado (PT),Frekuensi,Nomor Surat,Nama Surat,Ayat,Teks Arab Ayat,Transliterasi Latin Ayat,Terjemahan (ID),Translation (EN),Terjemahan (MS),Traduction (FR),Übersetzung (DE),Tarjuma (UR),Anuvad (HI),Onubad (BN),Perevod (RU),Fanyi (ZH),Traducción (ES),Meal (TR),Tradução (PT),Link Audio,Link QuranCom\\n';

    group.occurrences.forEach(occ => {
      const link = `https://quran.com/${occ.surat}/${occ.ayat}`;
      const cleanArab = (occ.teksArab || '').replace(/"/g, '""');
      const cleanLatin = (occ.teksLatin || '').replace(/"/g, '""');
      const cleanArtiID = (occ.teksArtiID || occ.teksArti || '').replace(/"/g, '""');
      const cleanArtiEN = (occ.teksArtiEN || '').replace(/"/g, '""');
      const cleanArtiMS = (occ.teksArtiMS || '').replace(/"/g, '""');
      const cleanArtiFR = (occ.teksArtiFR || '').replace(/"/g, '""');
      const cleanArtiDE = (occ.teksArtiDE || '').replace(/"/g, '""');
      const cleanArtiUR = (occ.teksArtiUR || '').replace(/"/g, '""');
      const cleanArtiHI = (occ.teksArtiHI || '').replace(/"/g, '""');
      const cleanArtiBN = (occ.teksArtiBN || '').replace(/"/g, '""');
      const cleanArtiRU = (occ.teksArtiRU || '').replace(/"/g, '""');
      const cleanArtiZH = (occ.teksArtiZH || '').replace(/"/g, '""');
      const cleanArtiES = (occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || '').replace(/"/g, '""');
      const cleanArtiTR = (occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || '').replace(/"/g, '""');
      const cleanArtiPT = (occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || '').replace(/"/g, '""');
      const audioLink = occ.audioUrl || '';
      csvContent += `"${group.bentuk}","${group.noKata}","${group.kata}","${group.latin || ''}","${group.arti_id || group.arti}","${group.arti_en || ''}","${group.arti_ms || ''}","${group.arti_fr || ''}","${group.arti_de || ''}","${group.arti_ur || ''}","${group.arti_hi || ''}","${group.arti_bn || ''}","${group.arti_ru || ''}","${group.arti_zh || ''}","${group.arti_es || ''}","${group.arti_tr || ''}","${group.arti_pt || ''}","${group.frek || 'Muttashil'}","${occ.surat}","${occ.suratNama}","${occ.ayat}","${cleanArab}","${cleanLatin}","${cleanArtiID}","${cleanArtiEN}","${cleanArtiMS}","${cleanArtiFR}","${cleanArtiDE}","${cleanArtiUR}","${cleanArtiHI}","${cleanArtiBN}","${cleanArtiRU}","${cleanArtiZH}","${cleanArtiES}","${cleanArtiTR}","${cleanArtiPT}","${audioLink}","${link}"\\n`;
    });

    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.setAttribute('href', url);
    link.setAttribute('download', `${group.bentuk.replace(/[^a-zA-Z0-9]/g, '_')}_${group.noKata}_${group.kata}_${state.lang.toUpperCase()}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);

    showToast(t('toastCsvExported', group.noKata));
  }

  // Theme Toggle
  function applyTheme(theme) {
    state.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('dhamir_theme', theme);

    if (theme === 'light') {
      elements.themeIcon.innerHTML = `
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
        </svg>
      `;
    } else {
      elements.themeIcon.innerHTML = `
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="5"></circle>
          <line x1="12" y1="1" x2="12" y2="3"></line>
          <line x1="12" y1="21" x2="12" y2="23"></line>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
          <line x1="1" y1="12" x2="3" y2="12"></line>
          <line x1="21" y1="12" x2="23" y2="12"></line>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
        </svg>
      `;
    }
  }

  // Setup Event Listeners
  function setupEventListeners() {
    // Language Switcher Dropdown
    if (elements.langSelect) {
      elements.langSelect.addEventListener('change', (e) => {
        applyLanguage(e.target.value);
        showToast(t('toastLangChanged'));
      });
    }

    // Bentuk Kata Select
    elements.bentukKataSelect.addEventListener('change', (e) => {
      selectBentuk(e.target.value);
    });

    // Nomor Kata Select
    elements.noKataSelect.addEventListener('change', (e) => {
      selectNoKata(e.target.value);
    });

    // Search Input inside Ayat
    elements.ayatSearchInput.addEventListener('input', (e) => {
      const group = getGroup(state.selectedBentuk, state.selectedNoKata);
      renderAyatReferences(group, e.target.value);
    });

    // Copy Arabic Word
    if (elements.btnCopyArabic) {
      elements.btnCopyArabic.addEventListener('click', () => {
        const group = getGroup(state.selectedBentuk, state.selectedNoKata);
        if (group && navigator.clipboard) {
          navigator.clipboard.writeText(group.kata).then(() => {
            showToast(t('toastArabicCopied', group.kata));
          }).catch(() => {
            showToast('Gagal menyalin kata.');
          });
        }
      });
    }

    // Copy Full Info Summary
    if (elements.btnCopyAll) {
      elements.btnCopyAll.addEventListener('click', () => {
        const group = getGroup(state.selectedBentuk, state.selectedNoKata);
        if (!group || !navigator.clipboard) return;

        let activeArti = group.arti_id || group.arti;
        if (state.lang === 'en') {
          activeArti = group.arti_en || group.arti;
        } else if (state.lang === 'ms') {
          activeArti = group.arti_ms || group.arti_id || group.arti;
        } else if (state.lang === 'fr') {
          activeArti = group.arti_fr || group.arti_id || group.arti;
        } else if (state.lang === 'de') {
          activeArti = group.arti_de || group.arti_id || group.arti;
        } else if (state.lang === 'ur') {
          activeArti = group.arti_ur || group.arti_id || group.arti;
        } else if (state.lang === 'hi') {
          activeArti = group.arti_hi || group.arti_id || group.arti;
        } else if (state.lang === 'bn') {
          activeArti = group.arti_bn || group.arti_id || group.arti;
        } else if (state.lang === 'ru') {
          activeArti = group.arti_ru || group.arti_id || group.arti;
        } else if (state.lang === 'zh') {
          activeArti = group.arti_zh || group.arti_id || group.arti;
        } else if (state.lang === 'es') {
          activeArti = group.arti_es || group.arti_id || group.arti;
        } else if (state.lang === 'tr') {
          activeArti = group.arti_tr || group.arti_id || group.arti;
        } else if (state.lang === 'pt') {
          activeArti = group.arti_pt || group.arti_id || group.arti;
        }

        const grammar = group.grammar || {};
        let activeDesc = grammar.desc_id || grammar.keterangan || '';
        if (state.lang === 'en') {
          activeDesc = grammar.desc_en || grammar.desc_id || grammar.keterangan || '';
        } else if (state.lang === 'ms') {
          activeDesc = grammar.desc_ms || grammar.desc_id || grammar.keterangan || '';
        } else if (state.lang === 'fr') {
          activeDesc = grammar.desc_fr || grammar.desc_id || grammar.keterangan || '';
        } else if (state.lang === 'de') {
          activeDesc = grammar.desc_de || grammar.desc_id || grammar.keterangan || '';
        } else if (state.lang === 'ur') {
          activeDesc = grammar.desc_ur || grammar.desc_id || grammar.keterangan || '';
        } else if (state.lang === 'hi') {
          activeDesc = grammar.desc_hi || grammar.desc_id || grammar.keterangan || '';
        } else if (state.lang === 'bn') {
          activeDesc = grammar.desc_bn || grammar.desc_id || grammar.keterangan || '';
        } else if (state.lang === 'ru') {
          activeDesc = grammar.desc_ru || grammar.desc_id || grammar.keterangan || '';
        } else if (state.lang === 'zh') {
          activeDesc = grammar.desc_zh || grammar.desc_id || grammar.keterangan || '';
        } else if (state.lang === 'es') {
          activeDesc = grammar.desc_es || grammar.desc_id || grammar.keterangan || '';
        } else if (state.lang === 'tr') {
          activeDesc = grammar.desc_tr || grammar.desc_id || grammar.keterangan || '';
        } else if (state.lang === 'pt') {
          activeDesc = grammar.desc_pt || grammar.desc_id || grammar.keterangan || '';
        }

        let titlePrefix = 'Dhamir Al-Qur\\'an';
        if (group.bentuk && group.bentuk.includes('Mawshul')) {
          titlePrefix = 'Isim Mawshul Al-Qur\\'an';
          if (state.lang === 'en') titlePrefix = 'Quranic Relative Pronoun (Mawshul)';
          else if (state.lang === 'ms') titlePrefix = 'Isim Mawshul Al-Qur\\'an';
          else if (state.lang === 'fr') titlePrefix = 'Pronom Relatif du Coran (Mawshul)';
          else if (state.lang === 'de') titlePrefix = 'Koranisches Relativpronomen (Mawshul)';
          else if (state.lang === 'ur') titlePrefix = 'قرآنی اسم موصول';
          else if (state.lang === 'hi') titlePrefix = 'क़ुरआनी संबंधवाचक सर्वनाम (मौसूल)';
          else if (state.lang === 'bn') titlePrefix = 'কুরআনিক সম্বন্ধবাচক সর্বনাম (মাওসুল)';
          else if (state.lang === 'ru') titlePrefix = 'Кораническое относительное местоимение (Маусуль)';
          else if (state.lang === 'zh') titlePrefix = '古兰经关系代词 (Mawshul)';
          else if (state.lang === 'es') titlePrefix = 'Pronombre Relativo del Corán (Mawshul)';
          else if (state.lang === 'tr') titlePrefix = 'Kur\\'an-ı Kerim İsmi Mevsul (Mawshul)';
          else if (state.lang === 'pt') titlePrefix = 'Pronome Relativo do Alcorão (Mawshul)';
        } else {
          if (state.lang === 'en') titlePrefix = 'Quranic Pronoun (Dhamir)';
          else if (state.lang === 'ms') titlePrefix = 'Dhamir Al-Qur\\'an';
          else if (state.lang === 'fr') titlePrefix = 'Pronom Coranique (Dhamir)';
          else if (state.lang === 'de') titlePrefix = 'Koranisches Pronomen (Dhamir)';
          else if (state.lang === 'ur') titlePrefix = 'قرآنی ضمیر';
          else if (state.lang === 'hi') titlePrefix = 'क़ुरआनी सर्वनाम (ज़मीर)';
          else if (state.lang === 'bn') titlePrefix = 'কুরআনিক সর্বনাম (যমীর)';
          else if (state.lang === 'ru') titlePrefix = 'Кораническое местоимение (Дамир)';
          else if (state.lang === 'zh') titlePrefix = '古兰经代词 (Dhamir)';
          else if (state.lang === 'es') titlePrefix = 'Pronombre del Corán (Dhamir)';
          else if (state.lang === 'tr') titlePrefix = 'Kur\\'an-ı Kerim Zamirleri (Dhamir)';
          else if (state.lang === 'pt') titlePrefix = 'Pronomes do Alcorão (Dhamir)';
        }

        const summary = `[${titlePrefix}]\\n${group.noKata} - ${group.kata} (${group.latin || '-'})\n${t('meaningPrefix')} ${activeArti}\\n${activeDesc ? t('wordFormBadge') + ': ' + activeDesc + '\\n' : ''}${t('freqLabel')}: ${group.frek ? group.frek + 'x' : t('freqMuttashilVal')}\\n${t('totalAyatLabel')}: ${group.occurrences.length} ${t('sampleAyatSuffix')}`;
        
        navigator.clipboard.writeText(summary).then(() => {
          showToast(t('toastSummaryCopied'));
        }).catch(() => {
          showToast('Gagal menyalin ringkasan.');
        });
      });
    }

    // Keyboard Navigation
    document.addEventListener('keydown', (e) => {
      if (elements.aiModal && elements.aiModal.classList.contains('open')) {
        if (e.key === 'Escape') closeAiModal();
        return;
      }

      if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') {
        if (e.key === 'Escape') e.target.blur();
        return;
      }

      const activeList = noKatasByBentuk[state.selectedBentuk] || [];
      if (activeList.length === 0) return;

      const currentNKIndex = activeList.indexOf(state.selectedNoKata);

      if (e.key === 'ArrowRight' || e.key === 'j') {
        if (currentNKIndex < activeList.length - 1) {
          selectNoKata(activeList[currentNKIndex + 1]);
        }
      } else if (e.key === 'ArrowLeft' || e.key === 'k') {
        if (currentNKIndex > 0) {
          selectNoKata(activeList[currentNKIndex - 1]);
        }
      } else if (e.key === ' ' || e.key === 'Spacebar') {
        e.preventDefault();
        const currentGroup = getGroup(state.selectedBentuk, state.selectedNoKata);
        if (currentGroup) speakDhamirMeaning(currentGroup);
      }
    });

    // Theme Switcher Button
    if (elements.themeToggleBtn) {
      elements.themeToggleBtn.addEventListener('click', () => {
        const nextTheme = state.theme === 'light' ? 'dark' : 'light';
        applyTheme(nextTheme);
      });
    }

    // Audio Play Button (Arabic Pronunciation)
    if (elements.btnAudioPlay) {
      elements.btnAudioPlay.addEventListener('click', () => {
        const group = getGroup(state.selectedBentuk, state.selectedNoKata);
        if (group) speakArabicWord(group.kata);
      });
    }

    // Audio Meaning Button
    if (elements.btnAudioMeaning) {
      elements.btnAudioMeaning.addEventListener('click', () => {
        const group = getGroup(state.selectedBentuk, state.selectedNoKata);
        if (group) speakDhamirMeaning(group);
      });
    }

    // Export CSV Button
    if (elements.btnExportCsv) {
      elements.btnExportCsv.addEventListener('click', () => {
        exportToCsv();
      });
    }

    // AI Modal Actions
    if (elements.aiModalCloseBtn) {
      elements.aiModalCloseBtn.addEventListener('click', closeAiModal);
    }
    if (elements.aiModal) {
      elements.aiModal.addEventListener('click', (e) => {
        if (e.target === elements.aiModal) closeAiModal();
      });
    }
    if (elements.aiTopicChips) {
      elements.aiTopicChips.addEventListener('click', (e) => {
        const chip = e.target.closest('.topic-chip');
        if (!chip) return;
        elements.aiTopicChips.querySelectorAll('.topic-chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        currentAiContext.topic = chip.getAttribute('data-topic');
        updateAiModalPrompt();
      });
    }
    if (elements.btnOpenGemini) {
      elements.btnOpenGemini.addEventListener('click', openInGemini);
    }
    if (elements.btnOpenChatGpt) {
      elements.btnOpenChatGpt.addEventListener('click', openInChatGpt);
    }
    if (elements.btnCopyPrompt) {
      elements.btnCopyPrompt.addEventListener('click', copyAiPrompt);
    }
  }

  // Initialize App
  function init() {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.onvoiceschanged = () => {
        window.speechSynthesis.getVoices();
      };
      window.speechSynthesis.getVoices();
    }
    initData();
    populateBentukDropdown();
    applyLanguage(state.lang);
    applyTheme(state.theme);
    setupEventListeners();

    // Default Selection on first load
    if (availableBentukKatas.length > 0) {
      const defaultBentuk = '1. Dhamir';
      selectBentuk(defaultBentuk);
      
      const list = noKatasByBentuk[defaultBentuk];
      if (list && list.length > 0) {
        selectNoKata('1a');
      }
    }
  }

  // Run on DOM Content Loaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
"""

code = code[:idx_cut] + new_tail

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Rewrote app.js successfully!")
