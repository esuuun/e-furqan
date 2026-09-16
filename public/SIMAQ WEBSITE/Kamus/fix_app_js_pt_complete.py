#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flawless, comprehensive fix for Portuguese (pt) in app.js
"""

import sys
import re

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Normalize newlines
crlf = '\r\n' in code
code = code.replace('\r\n', '\n')

# 1. Clean populateNoKataDropdown
old_nokata_loop = """      let localizedArti = group.arti_id || group.arti;
      if (state.lang === 'en') {
        localizedArti = group.arti_en || group.arti;
      } else if (state.lang === 'ms') {
        localizedArti = group.arti_ms || group.arti_id || group.arti;
      } else if (state.lang === 'fr') {
        localizedArti = group.arti_fr || group.arti_id || group.arti;
      } else if (state.lang === 'de') {
        localizedArti = group.arti_de || group.arti_id || group.arti;
      } else if (state.lang === 'ur') {
        localizedArti = group.arti_ur || group.arti_id || group.arti;
      } else if (state.lang === 'hi') {
        localizedArti = group.arti_hi || group.arti_id || group.arti;
      } else if (state.lang === 'bn') {
        localizedArti = group.arti_bn || group.arti_id || group.arti;
      } else if (state.lang === 'ru') {
        localizedArti = group.arti_ru || group.arti_id || group.arti;
      } else if (state.lang === 'zh') {
        localizedArti = group.arti_zh || group.arti_id || group.arti;"""

# Replace in populateNoKataDropdown to ensure clean Portuguese assignment
idx_nokata = code.find('function populateNoKataDropdown()')
idx_nokata_end = code.find('function getDefaultJenis', idx_nokata)
nokata_section = code[idx_nokata:idx_nokata_end]

clean_nokata_section = """function populateNoKataDropdown() {
    elements.noKataSelect.innerHTML = '';

    const placeholderOption = document.createElement('option');
    placeholderOption.value = '';
    placeholderOption.textContent = t('step2Placeholder');
    if (!state.selectedNoKata) {
      placeholderOption.selected = true;
    }
    elements.noKataSelect.appendChild(placeholderOption);
    
    const activeList = noKatasByBentuk[state.selectedBentuk] || [];
    if (!state.selectedBentuk || activeList.length === 0) {
      elements.noKataSelect.disabled = true;
      elements.noKataSelect.value = '';
      return;
    }

    elements.noKataSelect.disabled = false;

    activeList.forEach(nk => {
      const group = getGroup(state.selectedBentuk, nk);
      if (!group) return;
      
      const option = document.createElement('option');
      option.value = nk;
      const latinPart = group.latin ? `[${group.latin}] ` : '';
      let localizedArti = group.arti_id || group.arti;
      if (state.lang === 'en') {
        localizedArti = group.arti_en || group.arti;
      } else if (state.lang === 'ms') {
        localizedArti = group.arti_ms || group.arti_id || group.arti;
      } else if (state.lang === 'fr') {
        localizedArti = group.arti_fr || group.arti_id || group.arti;
      } else if (state.lang === 'de') {
        localizedArti = group.arti_de || group.arti_id || group.arti;
      } else if (state.lang === 'ur') {
        localizedArti = group.arti_ur || group.arti_id || group.arti;
      } else if (state.lang === 'hi') {
        localizedArti = group.arti_hi || group.arti_id || group.arti;
      } else if (state.lang === 'bn') {
        localizedArti = group.arti_bn || group.arti_id || group.arti;
      } else if (state.lang === 'ru') {
        localizedArti = group.arti_ru || group.arti_id || group.arti;
      } else if (state.lang === 'zh') {
        localizedArti = group.arti_zh || group.arti_id || group.arti;
      } else if (state.lang === 'es') {
        localizedArti = group.arti_es || group.arti_id || group.arti;
      } else if (state.lang === 'tr') {
        localizedArti = group.arti_tr || group.arti_id || group.arti;
      } else if (state.lang === 'pt') {
        localizedArti = group.arti_pt || group.arti_id || group.arti;
      }
      option.textContent = `${nk} - ${group.kata} ${latinPart}(${localizedArti})`;
      if (state.selectedNoKata === nk) {
        option.selected = true;
      }
      elements.noKataSelect.appendChild(option);
    });

    elements.noKataSelect.value = state.selectedNoKata || '';
  }

  // Get Default Category Jenis (Fallback)
  """

code = code[:idx_nokata] + clean_nokata_section + code[idx_nokata_end:]

# 2. Clean updateSpotlightCard
idx_spotlight = code.find('function updateSpotlightCard(group)')
idx_spotlight_end = code.find('function stopAllSpeech()', idx_spotlight)
spotlight_section = code[idx_spotlight:idx_spotlight_end]

clean_spotlight_section = """function updateSpotlightCard(group) {
    if (!group) return;

    // Reset card state
    elements.spotlightCard.classList.remove('active');
    void elements.spotlightCard.offsetWidth; // Trigger reflow for animation
    elements.spotlightCard.classList.add('active');

    // Badge Bentuk
    if (state.lang === 'en') {
      elements.badgeBentukKata.textContent = group.bentuk_en || group.bentuk_id;
    } else if (state.lang === 'ms') {
      elements.badgeBentukKata.textContent = group.bentuk_ms || group.bentuk_id;
    } else if (state.lang === 'fr') {
      elements.badgeBentukKata.textContent = group.bentuk_fr || group.bentuk_id;
    } else if (state.lang === 'de') {
      elements.badgeBentukKata.textContent = group.bentuk_de || group.bentuk_id;
    } else if (state.lang === 'ur') {
      elements.badgeBentukKata.textContent = group.bentuk_ur || group.bentuk_id;
    } else if (state.lang === 'hi') {
      elements.badgeBentukKata.textContent = group.bentuk_hi || group.bentuk_id;
    } else if (state.lang === 'bn') {
      elements.badgeBentukKata.textContent = group.bentuk_bn || group.bentuk_id;
    } else if (state.lang === 'ru') {
      elements.badgeBentukKata.textContent = group.bentuk_ru || group.bentuk_id;
    } else if (state.lang === 'zh') {
      elements.badgeBentukKata.textContent = group.bentuk_zh || group.bentuk_id;
    } else if (state.lang === 'es') {
      elements.badgeBentukKata.textContent = group.bentuk_es || group.bentuk_id;
    } else if (state.lang === 'tr') {
      elements.badgeBentukKata.textContent = group.bentuk_tr || group.bentuk_id;
    } else if (state.lang === 'pt') {
      elements.badgeBentukKata.textContent = group.bentuk_pt || group.bentuk_id;
    } else {
      elements.badgeBentukKata.textContent = group.bentuk_id;
    }
    
    elements.badgeNoKata.textContent = `${t('wordNoBadgePrefix')} ${group.noKata}`;
    
    // Arabic Word & Transliteration
    elements.arabicWordText.textContent = group.kata;
    elements.latinWordText.textContent = group.latin || '-';

    // Jenis Tag & Grammar Info
    const grammar = group.grammar || {};
    let jenisText = grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, state.lang);
    if (state.lang === 'en') {
      jenisText = grammar.jenis_en || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'en');
    } else if (state.lang === 'ms') {
      jenisText = grammar.jenis_ms || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'ms');
    } else if (state.lang === 'fr') {
      jenisText = grammar.jenis_fr || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'fr');
    } else if (state.lang === 'de') {
      jenisText = grammar.jenis_de || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'de');
    } else if (state.lang === 'ur') {
      jenisText = grammar.jenis_ur || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'ur');
    } else if (state.lang === 'hi') {
      jenisText = grammar.jenis_hi || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'hi');
    } else if (state.lang === 'bn') {
      jenisText = grammar.jenis_bn || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'bn');
    } else if (state.lang === 'ru') {
      jenisText = grammar.jenis_ru || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'ru');
    } else if (state.lang === 'zh') {
      jenisText = grammar.jenis_zh || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'zh');
    } else if (state.lang === 'es') {
      jenisText = grammar.jenis_es || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'es');
    } else if (state.lang === 'tr') {
      jenisText = grammar.jenis_tr || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'tr');
    } else if (state.lang === 'pt') {
      jenisText = grammar.jenis_pt || grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'pt');
    } else {
      jenisText = grammar.jenis_id || grammar.jenis || getDefaultJenis(group.bentuk, 'id');
    }
    elements.jenisTag.textContent = jenisText;
    
    // Meaning
    let currentMeaning = group.arti_id || group.arti;
    if (state.lang === 'en') {
      currentMeaning = group.arti_en || group.arti;
    } else if (state.lang === 'ms') {
      currentMeaning = group.arti_ms || group.arti_id || group.arti;
    } else if (state.lang === 'fr') {
      currentMeaning = group.arti_fr || group.arti_id || group.arti;
    } else if (state.lang === 'de') {
      currentMeaning = group.arti_de || group.arti_id || group.arti;
    } else if (state.lang === 'ur') {
      currentMeaning = group.arti_ur || group.arti_id || group.arti;
    } else if (state.lang === 'hi') {
      currentMeaning = group.arti_hi || group.arti_id || group.arti;
    } else if (state.lang === 'bn') {
      currentMeaning = group.arti_bn || group.arti_id || group.arti;
    } else if (state.lang === 'ru') {
      currentMeaning = group.arti_ru || group.arti_id || group.arti;
    } else if (state.lang === 'zh') {
      currentMeaning = group.arti_zh || group.arti_id || group.arti;
    } else if (state.lang === 'es') {
      currentMeaning = group.arti_es || group.arti_id || group.arti;
    } else if (state.lang === 'tr') {
      currentMeaning = group.arti_tr || group.arti_id || group.arti;
    } else if (state.lang === 'pt') {
      currentMeaning = group.arti_pt || group.arti_id || group.arti;
    }
    elements.meaningText.textContent = currentMeaning;

    // Grammar Description
    let currentDesc = grammar.desc_id || grammar.keterangan || '';
    if (state.lang === 'en') {
      currentDesc = grammar.desc_en || grammar.desc_id || grammar.keterangan || '';
    } else if (state.lang === 'ms') {
      currentDesc = grammar.desc_ms || grammar.desc_id || grammar.keterangan || '';
    } else if (state.lang === 'fr') {
      currentDesc = grammar.desc_fr || grammar.desc_id || grammar.keterangan || '';
    } else if (state.lang === 'de') {
      currentDesc = grammar.desc_de || grammar.desc_id || grammar.keterangan || '';
    } else if (state.lang === 'ur') {
      currentDesc = grammar.desc_ur || grammar.desc_id || grammar.keterangan || '';
    } else if (state.lang === 'hi') {
      currentDesc = grammar.desc_hi || grammar.desc_id || grammar.keterangan || '';
    } else if (state.lang === 'bn') {
      currentDesc = grammar.desc_bn || grammar.desc_id || grammar.keterangan || '';
    } else if (state.lang === 'ru') {
      currentDesc = grammar.desc_ru || grammar.desc_id || grammar.keterangan || '';
    } else if (state.lang === 'zh') {
      currentDesc = grammar.desc_zh || grammar.desc_id || grammar.keterangan || '';
    } else if (state.lang === 'es') {
      currentDesc = grammar.desc_es || grammar.desc_id || grammar.keterangan || '';
    } else if (state.lang === 'tr') {
      currentDesc = grammar.desc_tr || grammar.desc_id || grammar.keterangan || '';
    } else if (state.lang === 'pt') {
      currentDesc = grammar.desc_pt || grammar.desc_id || grammar.keterangan || '';
    }
    elements.grammarDescText.textContent = currentDesc;

    // Freq Stats
    if (group.frek) {
      elements.freqValue.textContent = group.frek.toLocaleString('id-ID');
      elements.freqSubtitle.textContent = t('freqSub');
    } else {
      elements.freqValue.textContent = t('freqMuttashilVal');
      elements.freqSubtitle.textContent = t('freqMuttashilSub');
    }

    // Total Ayat Count
    elements.totalAyatValue.textContent = group.occurrences.length;
    elements.totalAyatSubtitle.textContent = t('totalAyatSub');
  }

  // Audio Controls & Synthesizer
  """

code = code[:idx_spotlight] + clean_spotlight_section + code[idx_spotlight_end:]

# 3. Clean toggleVerseTranslationAudio and speakDhamirMeaning
idx_stop = code.find('function stopAllSpeech()')
idx_arabic_pat = code.find('const ARABIC_WORD_PATTERNS =', idx_stop)

clean_audio_section = """function stopAllSpeech() {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
    if (currentTranslationAudio) {
      currentTranslationAudio.onended = null;
      currentTranslationAudio.onerror = null;
      currentTranslationAudio.pause();
      currentTranslationAudio.currentTime = 0;
      currentTranslationAudio = null;
    }
    isTranslationAudioPlaying = false;

    if (currentSpeakingBtn) {
      currentSpeakingBtn.classList.remove('speaking');
      currentSpeakingBtn.setAttribute('title', t('meaningVoiceTooltip'));
      const icon = currentSpeakingBtn.querySelector('.audio-icon-state');
      if (icon) {
        icon.innerHTML = `<polygon points="5 3 19 12 5 21 5 3"></polygon>`;
      }
      currentSpeakingBtn = null;
    }
    if (elements.btnAudioMeaning) {
      elements.btnAudioMeaning.style.color = '';
    }
    if (elements.btnAudioPlay) {
      elements.btnAudioPlay.style.color = '';
    }
    activeUtterance = null;
  }

  function stopVerseAudio() {
    if (currentVerseAudio) {
      currentVerseAudio.pause();
      currentVerseAudio.currentTime = 0;
      currentVerseAudio = null;
    }
    isVerseAudioPlaying = false;
    updateAllAudioButtonStates(false);
  }

  function stopAllAudio() {
    stopVerseAudio();
    stopAllSpeech();
  }

  function updateAllAudioButtonStates(playing) {
    const audioBtns = elements.ayatGridContainer.querySelectorAll('.btn-play-verse-audio');
    audioBtns.forEach(btn => {
      const icon = btn.querySelector('.audio-icon-state');
      if (playing) {
        btn.classList.add('playing');
        btn.setAttribute('title', t('pauseTilawahBtn'));
        if (icon) {
          icon.innerHTML = `<rect x="5" y="4" width="4" height="16" rx="1"></rect><rect x="15" y="4" width="4" height="16" rx="1"></rect>`;
        }
      } else {
        btn.classList.remove('playing');
        btn.setAttribute('title', `${t('playTilawahBtn')} (Mishary Alafasy)`);
        if (icon) {
          icon.innerHTML = `<polygon points="5 3 19 12 5 21 5 3"></polygon>`;
        }
      }
    });
  }

  function toggleVerseAudio(surat, ayat, directAudioUrl) {
    stopAllSpeech();

    const url = directAudioUrl || getAyatAudioUrl(surat, ayat);

    if (currentVerseAudio && currentVerseAudio.dataset.url === url) {
      if (isVerseAudioPlaying) {
        currentVerseAudio.pause();
        isVerseAudioPlaying = false;
        updateAllAudioButtonStates(false);
        showToast(t('toastTilawahPaused'));
      } else {
        currentVerseAudio.play();
        isVerseAudioPlaying = true;
        updateAllAudioButtonStates(true);
        showToast(t('toastTilawahPlaying', surat, ayat));
      }
      return;
    }

    stopVerseAudio();

    currentVerseAudio = new Audio(url);
    currentVerseAudio.dataset.url = url;
    isVerseAudioPlaying = true;
    updateAllAudioButtonStates(true);
    showToast(t('toastTilawahPlaying', surat, ayat));

    currentVerseAudio.onended = () => {
      isVerseAudioPlaying = false;
      updateAllAudioButtonStates(false);
      showToast(t('toastTilawahEnded'));
    };

    currentVerseAudio.onerror = () => {
      const fallbackUrl = getAyatAudioUrl(surat, ayat);
      if (url !== fallbackUrl) {
        currentVerseAudio.src = fallbackUrl;
        currentVerseAudio.dataset.url = fallbackUrl;
        currentVerseAudio.play().catch(() => {
          isVerseAudioPlaying = false;
          updateAllAudioButtonStates(false);
          showToast(t('toastAudioFailed'));
        });
      } else {
        isVerseAudioPlaying = false;
        updateAllAudioButtonStates(false);
        showToast(t('toastAudioFailed'));
      }
    };

    currentVerseAudio.play().catch(err => {
      console.warn('Audio playback error:', err);
      isVerseAudioPlaying = false;
      updateAllAudioButtonStates(false);
    });
  }

  // Helper to split long text into streamable chunks for TTS
  function splitTextForTts(text, maxLen = 170) {
    if (!text || text.length <= maxLen) return [text];
    const sentences = text.match(/[^.!?،,;؛\\n]+[.!?،,;؛\\n]*/g) || [text];
    const chunks = [];
    let current = '';
    for (const s of sentences) {
      if ((current + (current ? ' ' : '') + s).length <= maxLen) {
        current = current ? current + ' ' + s : s;
      } else {
        if (current.trim()) chunks.push(current.trim());
        if (s.length <= maxLen) {
          current = s;
        } else {
          const words = s.split(' ');
          current = '';
          for (const w of words) {
            if ((current + (current ? ' ' : '') + w).length <= maxLen) {
              current = current ? current + ' ' + w : w;
            } else {
              if (current.trim()) chunks.push(current.trim());
              current = w;
            }
          }
        }
      }
    }
    if (current.trim()) chunks.push(current.trim());
    return chunks.length ? chunks : [text.slice(0, maxLen)];
  }

  // Play audio stream via Google TTS with sequential chunking for long text
  function playGoogleTtsStream(text, langCode, onEnded, onError) {
    const chunks = splitTextForTts(text);
    let chunkIndex = 0;

    function playNextChunk() {
      if (chunkIndex >= chunks.length) {
        if (onEnded) onEnded();
        return;
      }

      const chunk = chunks[chunkIndex];
      chunkIndex++;
      const url = `https://translate.google.com/translate_tts?ie=UTF-8&tl=${encodeURIComponent(langCode)}&client=tw-ob&q=${encodeURIComponent(chunk)}`;
      currentTranslationAudio = new Audio(url);
      currentTranslationAudio.dataset.url = url;
      currentTranslationAudio.onended = () => {
        playNextChunk();
      };
      currentTranslationAudio.onerror = (err) => {
        console.warn(`TTS stream error for chunk ${chunkIndex} (${langCode}):`, err);
        if (onError) onError(err);
      };
      currentTranslationAudio.play().catch(err => {
        console.warn(`TTS playback error (${langCode}):`, err);
        if (onError) onError(err);
      });
    }

    playNextChunk();
  }

  // Multilingual Audio for Verse Translation (Urdu Shamshad Ali Khan MP3 / Web Speech ID/EN/MS/FR/DE/TR/PT/etc.)
  function toggleVerseTranslationAudio(suratNama, surat, ayat, occ, btn) {
    stopVerseAudio();

    if (currentSpeakingBtn === btn && (isTranslationAudioPlaying || (window.speechSynthesis && window.speechSynthesis.speaking))) {
      stopAllSpeech();
      showToast(t('toastTranslationStopped'));
      return;
    }

    stopAllSpeech();

    // 1. Specially for Urdu: Play authentic studio MP3 translation audio (Shamshad Ali Khan from EveryAyah)
    if (state.lang === 'ur') {
      const urduAudioUrl = getUrduVerseAudioUrl(surat, ayat);
      currentTranslationAudio = new Audio(urduAudioUrl);
      currentTranslationAudio.dataset.url = urduAudioUrl;
      isTranslationAudioPlaying = true;
      currentSpeakingBtn = btn;

      btn.classList.add('speaking');
      btn.setAttribute('title', t('stopTranslationBtn'));
      const icon = btn.querySelector('.audio-icon-state');
      if (icon) {
        icon.innerHTML = `<rect x="5" y="4" width="4" height="16" rx="1"></rect><rect x="15" y="4" width="4" height="16" rx="1"></rect>`;
      }

      showToast(t('toastSpeakingMeaning', suratNama, ayat));

      currentTranslationAudio.onended = () => {
        stopAllSpeech();
      };

      currentTranslationAudio.onerror = () => {
        // Fallback to Google TTS if MP3 fails
        const cleanUrdu = (occ.teksArtiUR || occ.teksArtiID || '').replace(/["“”]/g, '').trim();
        if (cleanUrdu) {
          playGoogleTtsStream(
            cleanUrdu,
            'ur',
            () => stopAllSpeech(),
            () => {
              stopAllSpeech();
              showToast(t('toastAudioFailed'));
            }
          );
        } else {
          stopAllSpeech();
          showToast(t('toastAudioFailed'));
        }
      };

      currentTranslationAudio.play().catch(err => {
        console.warn('Urdu translation playback error:', err);
        stopAllSpeech();
      });
      return;
    }

    // 2. For other languages: Use SpeechSynthesis with fallbacks
    let currentText = occ.teksArtiID || occ.teksArti;
    if (state.lang === 'en') {
      currentText = occ.teksArtiEN || occ.teksArti;
    } else if (state.lang === 'ms') {
      currentText = occ.teksArtiMS || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'fr') {
      currentText = occ.teksArtiFR || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'de') {
      currentText = occ.teksArtiDE || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'hi') {
      currentText = occ.teksArtiHI || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'bn') {
      currentText = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'ru') {
      currentText = occ.teksArtiRU || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'zh') {
      currentText = occ.teksArtiZH || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'es') {
      currentText = occ.teksArtiES || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'tr') {
      currentText = occ.teksArtiTR || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'pt') {
      currentText = occ.teksArtiPT || occ.teksArtiEN || occ.teksArtiID || occ.teksArti;
    }
    const cleanText = (currentText || '').replace(/["“”]/g, '').trim();
    if (!cleanText) {
      showToast(t('toastTranslationNotAvail'));
      return;
    }

    const voices = ('speechSynthesis' in window) ? window.speechSynthesis.getVoices() : [];
    let matchVoice = null;
    let speechLangCode = 'id-ID';

    if (state.lang === 'en') {
      speechLangCode = 'en-US';
      matchVoice = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('David') || v.name.includes('Zira'))) || voices.find(v => v.lang.startsWith('en'));
    } else if (state.lang === 'ms') {
      speechLangCode = 'ms-MY';
      matchVoice = voices.find(v => v.lang.startsWith('ms') || v.lang.startsWith('my')) || voices.find(v => v.lang.startsWith('id') || v.lang.startsWith('in'));
    } else if (state.lang === 'fr') {
      speechLangCode = 'fr-FR';
      matchVoice = voices.find(v => v.lang.startsWith('fr') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Paul') || v.name.includes('Julie') || v.name.includes('Hortense') || v.name.includes('Claude'))) || voices.find(v => v.lang.startsWith('fr'));
    } else if (state.lang === 'de') {
      speechLangCode = 'de-DE';
      matchVoice = voices.find(v => v.lang.startsWith('de') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Stefan') || v.name.includes('Hedda') || v.name.includes('Katja') || v.name.includes('Marlene') || v.name.includes('Hans'))) || voices.find(v => v.lang.startsWith('de'));
    } else if (state.lang === 'hi') {
      speechLangCode = 'hi-IN';
      matchVoice = voices.find(v => v.lang.startsWith('hi') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Hemant') || v.name.includes('Kalpana') || v.name.includes('Swara') || v.name.includes('Madhur'))) || voices.find(v => v.lang.startsWith('hi'));
    } else if (state.lang === 'bn') {
      speechLangCode = 'bn-BD';
      matchVoice = voices.find(v => v.lang.startsWith('bn') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Bashkar') || v.name.includes('Tanishaa'))) || voices.find(v => v.lang.startsWith('bn'));
    } else if (state.lang === 'ru') {
      speechLangCode = 'ru-RU';
      matchVoice = voices.find(v => v.lang.startsWith('ru') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Pavel') || v.name.includes('Irina') || v.name.includes('Yuri') || v.name.includes('Ekaterina') || v.name.includes('Dmitry'))) || voices.find(v => v.lang.startsWith('ru'));
    } else if (state.lang === 'zh') {
      speechLangCode = 'zh-CN';
      matchVoice = voices.find(v => v.lang.startsWith('zh') && (v.name.includes('Xiaoxiao') || v.name.includes('Yunxi') || v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Chinese') || v.name.includes('Huihui') || v.name.includes('Yaoyao') || v.name.includes('Kangkang'))) || voices.find(v => v.lang.startsWith('zh'));
    } else if (state.lang === 'tr') {
      speechLangCode = 'tr-TR';
      matchVoice = voices.find(v => v.lang.startsWith('tr') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Ahmet') || v.name.includes('Emel') || v.name.includes('Turkish') || v.name.includes('Filiz') || v.name.includes('Tolga'))) || voices.find(v => v.lang.startsWith('tr'));
    } else if (state.lang === 'pt') {
      speechLangCode = 'pt-PT';
      matchVoice = voices.find(v => v.lang.startsWith('pt') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Heloisa') || v.name.includes('Raquel') || v.name.includes('Portuguese') || v.name.includes('Francisca') || v.name.includes('Duarte') || v.name.includes('Luciana') || v.name.includes('Yara') || v.name.includes('Daniel'))) || voices.find(v => v.lang.startsWith('pt'));
    } else if (state.lang === 'es') {
      speechLangCode = 'es-ES';
      matchVoice = voices.find(v => v.lang.startsWith('es') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Helena') || v.name.includes('Laura') || v.name.includes('Pablo') || v.name.includes('Spanish') || v.name.includes('Sabina') || v.name.includes('Raul'))) || voices.find(v => v.lang.startsWith('es'));
    } else {
      speechLangCode = 'id-ID';
      matchVoice = voices.find(v => v.lang.startsWith('id') || v.lang.startsWith('in'));
    }

    // If Web Speech has no matching voice or is not supported in this browser, use Google TTS stream fallback
    if (!matchVoice || !('speechSynthesis' in window)) {
      isTranslationAudioPlaying = true;
      currentSpeakingBtn = btn;
      btn.classList.add('speaking');
      btn.setAttribute('title', t('stopTranslationBtn'));
      const icon = btn.querySelector('.audio-icon-state');
      if (icon) {
        icon.innerHTML = `<rect x="5" y="4" width="4" height="16" rx="1"></rect><rect x="15" y="4" width="4" height="16" rx="1"></rect>`;
      }
      showToast(t('toastSpeakingMeaning', suratNama, ayat));
      playGoogleTtsStream(
        cleanText,
        state.lang,
        () => stopAllSpeech(),
        () => {
          stopAllSpeech();
          showToast(t('toastAudioFailed'));
        }
      );
      return;
    }

    const speechText = t('ttsVerseSpeech', suratNama, ayat, cleanText);
    const utterance = new SpeechSynthesisUtterance(speechText);
    utterance.lang = speechLangCode;
    utterance.rate = (state.lang === 'hi' || state.lang === 'bn') ? 0.92 : 0.95;
    utterance.pitch = 1.0;
    if (matchVoice) utterance.voice = matchVoice;

    currentSpeakingBtn = btn;
    activeUtterance = utterance;

    btn.classList.add('speaking');
    btn.setAttribute('title', t('stopTranslationBtn'));
    const icon = btn.querySelector('.audio-icon-state');
    if (icon) {
      icon.innerHTML = `<rect x="5" y="4" width="4" height="16" rx="1"></rect><rect x="15" y="4" width="4" height="16" rx="1"></rect>`;
    }

    showToast(t('toastSpeakingMeaning', suratNama, ayat));

    utterance.onend = () => {
      stopAllSpeech();
    };

    utterance.onerror = (e) => {
      console.warn('TTS error, falling back to Google TTS stream:', e);
      playGoogleTtsStream(
        cleanText,
        state.lang,
        () => stopAllSpeech(),
        () => {
          stopAllSpeech();
          showToast(t('toastAudioFailed'));
        }
      );
    };

    window.speechSynthesis.speak(utterance);
  }

  // Text-To-Speech Pronunciation for Arabic Word
  function speakArabicWord(text) {
    stopAllAudio();

    const cleanWord = text.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '').trim();
    const voices = ('speechSynthesis' in window) ? window.speechSynthesis.getVoices() : [];
    const arabicVoice = voices.find(v => v.lang.startsWith('ar'));

    if (!arabicVoice || !('speechSynthesis' in window)) {
      if (elements.btnAudioPlay) elements.btnAudioPlay.style.color = 'var(--text-gold)';
      showToast(t('toastSpeakingArabic', cleanWord));
      playGoogleTtsStream(
        cleanWord,
        'ar',
        () => {
          if (elements.btnAudioPlay) elements.btnAudioPlay.style.color = '';
        },
        () => {
          if (elements.btnAudioPlay) elements.btnAudioPlay.style.color = '';
        }
      );
      return;
    }

    const utterance = new SpeechSynthesisUtterance(cleanWord);
    utterance.lang = 'ar-SA';
    utterance.rate = 0.82;
    utterance.voice = arabicVoice;

    utterance.onstart = () => {
      if (elements.btnAudioPlay) elements.btnAudioPlay.style.color = 'var(--text-gold)';
    };
    utterance.onend = () => {
      if (elements.btnAudioPlay) elements.btnAudioPlay.style.color = '';
    };
    utterance.onerror = () => {
      if (elements.btnAudioPlay) elements.btnAudioPlay.style.color = '';
      playGoogleTtsStream(
        cleanWord,
        'ar',
        () => {
          if (elements.btnAudioPlay) elements.btnAudioPlay.style.color = '';
        },
        () => {
          if (elements.btnAudioPlay) elements.btnAudioPlay.style.color = '';
        }
      );
    };

    window.speechSynthesis.speak(utterance);
    showToast(t('toastSpeakingArabic', cleanWord));
  }

  // Text-To-Speech for Dhamir Meaning (Multilingual)
  function speakDhamirMeaning(group) {
    stopAllAudio();

    const meaningText = t('ttsMeaningSpeech', group);
    let activeMeaning = group.arti_id || group.arti;
    if (state.lang === 'en') {
      activeMeaning = group.arti_en || group.arti;
    } else if (state.lang === 'ms') {
      activeMeaning = group.arti_ms || group.arti_id || group.arti;
    } else if (state.lang === 'fr') {
      activeMeaning = group.arti_fr || group.arti_id || group.arti;
    } else if (state.lang === 'de') {
      activeMeaning = group.arti_de || group.arti_id || group.arti;
    } else if (state.lang === 'ur') {
      activeMeaning = group.arti_ur || group.arti_id || group.arti;
    } else if (state.lang === 'hi') {
      activeMeaning = group.arti_hi || group.arti_id || group.arti;
    } else if (state.lang === 'bn') {
      activeMeaning = group.arti_bn || group.arti_id || group.arti;
    } else if (state.lang === 'ru') {
      activeMeaning = group.arti_ru || group.arti_id || group.arti;
    } else if (state.lang === 'zh') {
      activeMeaning = group.arti_zh || group.arti_id || group.arti;
    } else if (state.lang === 'es') {
      activeMeaning = group.arti_es || group.arti_id || group.arti;
    } else if (state.lang === 'tr') {
      activeMeaning = group.arti_tr || group.arti_id || group.arti;
    } else if (state.lang === 'pt') {
      activeMeaning = group.arti_pt || group.arti_id || group.arti;
    }

    const voices = ('speechSynthesis' in window) ? window.speechSynthesis.getVoices() : [];
    let matchVoice = null;
    let speechLangCode = 'id-ID';

    if (state.lang === 'en') {
      speechLangCode = 'en-US';
      matchVoice = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('David') || v.name.includes('Zira'))) || voices.find(v => v.lang.startsWith('en'));
    } else if (state.lang === 'ms') {
      speechLangCode = 'ms-MY';
      matchVoice = voices.find(v => v.lang.startsWith('ms') || v.lang.startsWith('my')) || voices.find(v => v.lang.startsWith('id') || v.lang.startsWith('in'));
    } else if (state.lang === 'fr') {
      speechLangCode = 'fr-FR';
      matchVoice = voices.find(v => v.lang.startsWith('fr') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Paul') || v.name.includes('Julie') || v.name.includes('Hortense') || v.name.includes('Claude'))) || voices.find(v => v.lang.startsWith('fr'));
    } else if (state.lang === 'de') {
      speechLangCode = 'de-DE';
      matchVoice = voices.find(v => v.lang.startsWith('de') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Stefan') || v.name.includes('Hedda') || v.name.includes('Katja') || v.name.includes('Marlene') || v.name.includes('Hans'))) || voices.find(v => v.lang.startsWith('de'));
    } else if (state.lang === 'ur') {
      speechLangCode = 'ur-PK';
      matchVoice = voices.find(v => v.lang.startsWith('ur') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Asad') || v.name.includes('Uzma'))) || voices.find(v => v.lang.startsWith('ur')) || voices.find(v => v.lang.startsWith('ar'));
    } else if (state.lang === 'hi') {
      speechLangCode = 'hi-IN';
      matchVoice = voices.find(v => v.lang.startsWith('hi') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Hemant') || v.name.includes('Kalpana') || v.name.includes('Swara') || v.name.includes('Madhur'))) || voices.find(v => v.lang.startsWith('hi'));
    } else if (state.lang === 'bn') {
      speechLangCode = 'bn-BD';
      matchVoice = voices.find(v => v.lang.startsWith('bn') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Bashkar') || v.name.includes('Tanishaa'))) || voices.find(v => v.lang.startsWith('bn'));
    } else if (state.lang === 'ru') {
      speechLangCode = 'ru-RU';
      matchVoice = voices.find(v => v.lang.startsWith('ru') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Pavel') || v.name.includes('Irina') || v.name.includes('Yuri') || v.name.includes('Ekaterina') || v.name.includes('Dmitry'))) || voices.find(v => v.lang.startsWith('ru'));
    } else if (state.lang === 'zh') {
      speechLangCode = 'zh-CN';
      matchVoice = voices.find(v => v.lang.startsWith('zh') && (v.name.includes('Xiaoxiao') || v.name.includes('Yunxi') || v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Chinese') || v.name.includes('Huihui') || v.name.includes('Yaoyao') || v.name.includes('Kangkang'))) || voices.find(v => v.lang.startsWith('zh'));
    } else if (state.lang === 'tr') {
      speechLangCode = 'tr-TR';
      matchVoice = voices.find(v => v.lang.startsWith('tr') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Ahmet') || v.name.includes('Emel') || v.name.includes('Turkish') || v.name.includes('Filiz') || v.name.includes('Tolga'))) || voices.find(v => v.lang.startsWith('tr'));
    } else if (state.lang === 'pt') {
      speechLangCode = 'pt-PT';
      matchVoice = voices.find(v => v.lang.startsWith('pt') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Heloisa') || v.name.includes('Raquel') || v.name.includes('Portuguese') || v.name.includes('Francisca') || v.name.includes('Duarte') || v.name.includes('Luciana') || v.name.includes('Yara') || v.name.includes('Daniel'))) || voices.find(v => v.lang.startsWith('pt'));
    } else if (state.lang === 'es') {
      speechLangCode = 'es-ES';
      matchVoice = voices.find(v => v.lang.startsWith('es') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Helena') || v.name.includes('Laura') || v.name.includes('Pablo') || v.name.includes('Spanish') || v.name.includes('Sabina') || v.name.includes('Raul'))) || voices.find(v => v.lang.startsWith('es'));
    } else {
      speechLangCode = 'id-ID';
      matchVoice = voices.find(v => v.lang.startsWith('id') || v.lang.startsWith('in'));
    }

    if (!matchVoice || !('speechSynthesis' in window)) {
      if (elements.btnAudioMeaning) elements.btnAudioMeaning.style.color = 'var(--primary-400)';
      showToast(t('toastSpeakingWordMeaning', activeMeaning));
      playGoogleTtsStream(
        meaningText,
        state.lang,
        () => {
          if (elements.btnAudioMeaning) elements.btnAudioMeaning.style.color = '';
        },
        () => {
          if (elements.btnAudioMeaning) elements.btnAudioMeaning.style.color = '';
        }
      );
      return;
    }

    const utterance = new SpeechSynthesisUtterance(meaningText);
    utterance.lang = speechLangCode;
    utterance.rate = (state.lang === 'ur' || state.lang === 'hi' || state.lang === 'bn') ? 0.92 : 0.95;
    if (matchVoice) utterance.voice = matchVoice;

    if (elements.btnAudioMeaning) {
      elements.btnAudioMeaning.style.color = 'var(--primary-400)';
    }

    utterance.onend = () => {
      if (elements.btnAudioMeaning) elements.btnAudioMeaning.style.color = '';
    };

    utterance.onerror = () => {
      if (elements.btnAudioMeaning) elements.btnAudioMeaning.style.color = '';
      playGoogleTtsStream(
        meaningText,
        state.lang,
        () => {
          if (elements.btnAudioMeaning) elements.btnAudioMeaning.style.color = '';
        },
        () => {
          if (elements.btnAudioMeaning) elements.btnAudioMeaning.style.color = '';
        }
      );
    };

    window.speechSynthesis.speak(utterance);
    showToast(t('toastSpeakingWordMeaning', activeMeaning));
  }

  """

code = code[:idx_stop] + clean_audio_section + code[idx_arabic_pat:]

# 4. Clean buildAiPrompt and openAiModal
idx_build_prompt = code.find('function buildAiPrompt(group, occ, topic)')
idx_close_modal = code.find('function closeAiModal()', idx_build_prompt)

clean_prompt_and_modal_section = """function buildAiPrompt(group, occ, topic) {
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
        return `Please explain in detail the Arabic grammar (Nahwu/Sarf) and I'rab for the word "${kata}" (${noKata}, ${bentuk}) in Quran Surah ${suratNama} (${surat}): Ayah ${ayat}:\\n\\nArabic: "${teksArab}"\\nTranslation: "${teksArti}"\\n\\nPlease cover:\\n1. Grammatical role / I'rab of "${kata}" in this sentence structure.\\n2. Morphological category (Dhamir/Mawshul type) and case (Marfu'/Manshub/Majrur).\\n3. Grammar notes: ${grammarDesc || 'Standard Quranic usage'}.`;
      } else if (topic === 'tafsir') {
        return `Please provide a concise contextual Tafsir explanation for Quran Surah ${suratNama} (${surat}): Ayah ${ayat}:\\n\\nArabic: "${teksArab}"\\nTranslation: "${teksArti}"\\n\\nFocusing on the significance of the pronoun/word "${kata}", what is the core wisdom, context of revelation (asbabun nuzul if applicable), and theological message conveyed in this ayah?`;
      } else {
        return `Explain the Quranic Balaghah (Rhetorical Beauty & Stylistics) regarding the word choice "${kata}" in Surah ${suratNama} (${surat}) Ayah ${ayat}:\\n\\nArabic: "${teksArab}"\\nTranslation: "${teksArti}"\\n\\nWhy is this specific pronoun form used here? What subtle nuances, emphasis, or aesthetic eloquence does it add to the verse?`;
      }
    } else if (state.lang === 'ms') {
      if (topic === 'nahwu') {
        return `Mohon jelaskan secara terperinci kedudukan I'rab dan kaedah tatabahasa Nahwu/Saraf untuk kata "${kata}" (${noKata}, ${bentuk}) yang terdapat dalam Al-Qur'an Surah ${suratNama} (${surat}) ayat ${ayat}:\\n\\nTeks Arab: "${teksArab}"\\nTerjemahan: "${teksArti}"\\n\\nSila terangkan:\\n1. Kedudukan I'rab kata "${kata}" dalam susunan ayat ini.\\n2. Jenis kata (Dhamir Munfashil/Muttashil atau Isim Mawshul) berserta status kedudukannya (rafa'/nashab/jar).\\n3. Catatan kaedah: ${grammarDesc || 'Kaedah piawai Al-Qur\'an'}.`;
      } else if (topic === 'tafsir') {
        return `Mohon berikan penjelasan tafsir ringkas dan kontekstual berkenaan Surah ${suratNama} (${surat}) ayat ${ayat}:\\n\\nTeks Arab: "${teksArab}"\\nTerjemahan: "${teksArti}"\\n\\nDengan tumpuan kepada maksud kata "${kata}", apakah mesej utama, hikmah, serta konteks makna yang terkandung dalam ayat ini?`;
      } else {
        return `Jelaskan rahsia keindahan bahasa Al-Qur'an (Balaghah & Uslub) dalam pemilihan kata "${kata}" pada Surah ${suratNama} (${surat}) ayat ${ayat}:\\n\\nTeks Arab: "${teksArab}"\\nTerjemahan: "${teksArti}"\\n\\nMengapa Allah menggunakan bentuk kata ini dalam susunan ayat tersebut? Apakah rahsia keindahan sastera dan makna mendalamnya?`;
      }
    } else if (state.lang === 'fr') {
      if (topic === 'nahwu') {
        return `Veuillez expliquer en détail la grammaire arabe (Nahwu/Sarf) et l'I'rab pour le mot "${kata}" (${noKata}, ${bentuk}) dans le Coran, Sourate ${suratNama} (${surat}) : Verset ${ayat} :\\n\\nTexte Arabe : "${teksArab}"\\nTraduction : "${teksArti}"\\n\\nVeuillez détailler :\\n1. Le rôle grammatical / I'rab de "${kata}" dans cette structure de phrase.\\n2. La catégorie morphologique (type de Dhamir/Mawshul) et le cas (Marfu'/Manshub/Majrur).\\n3. Remarques grammaticales : ${grammarDesc || 'Usage coranique standard'}.`;
      } else if (topic === 'tafsir') {
        return `Veuillez fournir une explication concise et contextuelle de Tafsir pour la Sourate ${suratNama} (${surat}) : Verset ${ayat} :\\n\\nTexte Arabe : "${teksArab}"\\nTraduction : "${teksArti}"\\n\\nEn mettant l'accent sur la portée du pronom / mot "${kata}", quelle est la sagesse fondamentale, le contexte de révélation (asbab an-nuzul le cas échéant) et le message théologique transmis dans ce verset ?`;
      } else {
        return `Expliquez la Balaghah coranique (Beauté rhétorique & stylistique) concernant le choix du mot "${kata}" dans la Sourate ${suratNama} (${surat}) Verset ${ayat} :\\n\\nTexte Arabe : "${teksArab}"\\nTraduction : "${teksArti}"\\n\\nPourquoi cette forme spécifique de pronom est-elle employée ici ? Quelles nuances subtiles, emphase ou éloquence esthétique apporte-t-elle au verset ?`;
      }
    } else if (state.lang === 'de') {
      if (topic === 'nahwu') {
        return `Bitte erklären Sie ausführlich die arabische Grammatik (Nahw/Sarf) und das I'rab für das Wort "${kata}" (${noKata}, ${bentuk}) im Koran, Sure ${suratNama} (${surat}) : Vers ${ayat}:\\n\\nArabischer Text: "${teksArab}"\\nÜbersetzung: "${teksArti}"\\n\\nBitte erläutern Sie:\\n1. Die grammatikalische Funktion / I'rab von "${kata}" in dieser Satzstruktur.\\n2. Die morphologische Kategorie (Art des Dhamir / Mawshul) und den Fall (Marfu'/Manshub/Majrur).\\n3. Grammatikalische Anmerkungen: ${grammarDesc || 'Standardmäßiger koranischer Sprachgebrauch'}.`;
      } else if (topic === 'tafsir') {
        return `Bitte geben Sie eine prägnante und kontextbezogene Tafsir-Erklärung für Sure ${suratNama} (${surat}) : Vers ${ayat}:\\n\\nArabischer Text: "${teksArab}"\\nÜbersetzung: "${teksArti}"\\n\\nMit Fokus auf die Bedeutung des Pronomens / Wortes "${kata}": Was ist die wesentliche Weisheit, der Offenbarungsanlass (Asbab an-Nuzul, falls zutreffend) und die theologische Botschaft dieses Verses?`;
      } else {
        return `Erklären Sie die koranische Balagha (Rhetorische Schönheit & Stilistik) bezüglich der Wortwahl "${kata}" in Sure ${suratNama} (${surat}) Vers ${ayat}:\\n\\nArabischer Text: "${teksArab}"\\nÜbersetzung: "${teksArti}"\\n\\nWarum wird hier genau diese Pronomenform verwendet? Welche feinen Nuancen, Betonungen oder ästhetische Eloquenz verleiht sie dem Vers?`;
      }
    } else if (state.lang === 'ur') {
      if (topic === 'nahwu') {
        return `براہ کرم قرآن مجید کی سورۃ ${suratNama} (${surat}) آیت ${ayat} میں موجود لفظ "${kata}" (${noKata}، ${bentuk}) کے عربی قواعد و نحوی اعراب کی مفصل وضاحت کریں:\\n\\nعربی متن: "${teksArab}"\\nترجمہ: "${teksArti}"\\n\\nبراہ کرم درج ذیل نکات شامل کریں:\\n۱. اس جملے کی ترکیب میں "${kata}" کا نحوی کردار اور اعراب۔\\n۲. لفظ کی نوعیت (ضمیر منفصل/متصل یا اسم موصول) اور اس کی اعرابی حالت (مرفوع/منصوب/مجرور)۔\\n۳. نحوی نوٹس: ${grammarDesc || 'قرآنی معیاری استعمال'}۔`;
      } else if (topic === 'tafsir') {
        return `براہ کرم سورۃ ${suratNama} (${surat}) آیت ${ayat} کی مختصر اور سیاق و سباق کے مطابق تفسیری وضاحت پیش کریں:\\n\\nعربی متن: "${teksArab}"\\nترجمہ: "${teksArti}"\\n\\nخاص طور پر لفظ/ضمیر "${kata}" کی اہمیت کو مدنظر رکھتے ہوئے، اس آیت میں کیا بنیادی حکمت، شان نزول اور الٰہی پیغام بیان کیا گیا ہے؟`;
      } else {
        return `سورۃ ${suratNama} (${surat}) آیت ${ayat} میں لفظ "${kata}" کے انتخاب کے حوالے سے قرآنی بلاغت اور اسلوب کی خوبصورتی بیان کریں:\\n\\nعربی متن: "${teksArab}"\\nترجمہ: "${teksArti}"\\n\\nیہاں پر ضمیر کی یہی مخصوص شکل کیوں استعمال ہوئی ہے؟ یہ آیت کے حسن اور معنوی گہرائی میں کیا نکھار پیدا کرتی ہے؟`;
      }
    } else if (state.lang === 'hi') {
      if (topic === 'nahwu') {
        return `कृपया क़ुरआन मजीद की सूरह ${suratNama} (${surat}) आयत ${ayat} में उपस्थित शब्द "${kata}" (${noKata}, ${bentuk}) के अरबी व्याकरण (नहव/सर्फ़) और ए'राब की विस्तृत व्याख्या करें:\\n\\nअरबी पाठ: "${teksArab}"\\nअनुवाद: "${teksArti}"\\n\\nकृपया निम्नलिखित बिंदुओं को शामिल करें:\\n१. इस वाक्य रचना में "${kata}" की व्याकरणिक भूमिका और ए'राब (I'rab)।\\n२. शब्द का रूप (ज़मीर मुन्फ़सिल/मुत्तसिल या इस्म मौसूल) और इसकी स्थिति (रफ़ा/नसब/जर)।\\n३. व्याकरणिक टिप्पणी: ${grammarDesc || 'मानक क़ुरआनी प्रयोग'}।`;
      } else if (topic === 'tafsir') {
        return `कृपया सूरह ${suratNama} (${surat}) आयत ${ayat} की संक्षिप्त और संदर्भात्मक तफ़सीर (व्याख्या) प्रस्तुत करें:\\n\\nअरबी पाठ: "${teksArab}"\\nअनुवाद: "${teksArti}"\\n\\nविशेष रूप से शब्द/सर्वनाम "${kata}" के महत्व पर ध्यान केंद्रित करते हुए बताएं कि इस आयत में क्या मुख्य शिक्षा, अवतरण का संदर्भ और ईश्वरीय संदेश निहित है?`;
      } else {
        return `सूरह ${suratNama} (${surat}) आयत ${ayat} में शब्द "${kata}" के चयन के संबंध में क़ुरानी बलाग़त (अलंकारिक सौंदर्य व शैली) की व्याख्या करें:\\n\\nअरबी पाठ: "${teksArab}"\\nअनुवाद: "${teksArti}"\\n\\nयहाँ पर सर्वनाम का यही विशिष्ट रूप क्यों प्रयुक्त हुआ है? यह आयत के अर्थ की गहराई और साहित्यिक सौंदर्य में क्या वृद्धि करता है?`;
      }
    } else if (state.lang === 'bn') {
      if (topic === 'nahwu') {
        return `অনুগ্রহ করে পবিত্র কুরআনের সূরা ${suratNama} (${surat}) আয়াত ${ayat}-এ অবস্থিত শব্দ "${kata}" (${noKata}, ${bentuk})-এর আরবি ব্যাকরণ (নাহব/সরফ) ও ই'রাব বিস্তারিতভাবে ব্যাখ্যা করুন:\\n\\nআরবি পাঠ: "${teksArab}"\\nঅনুবাদ: "${teksArti}"\\n\\nঅনুগ্রহ করে নিম্নলিখিত বিষয়গুলো আলোচনা করুন:\\n১. এই বাক্যের গঠনে "${kata}"-এর ব্যাকরণগত ভূমিকা ও ই'রাব (I'rab)।\\n২. শব্দের রূপগত প্রকার (যমীর মুনফাসিল/মুত্তাসিল অথবা ইসম মাওসুল) এবং এর অবস্থা (মারফু'/মানসুব/মাজরুর)।\\n৩. ব্যাকরণগত নোট: ${grammarDesc || 'প্রমিত কুরআনিক প্রয়োগ'}।`;
      } else if (topic === 'tafsir') {
        return `অনুগ্রহ করে সূরা ${suratNama} (${surat}) আয়াত ${ayat}-এর সংক্ষিপ্ত ও প্রাসঙ্গিক তাফসির (ব্যাখ্যা) উপস্থাপন করুন:\\n\\nআরবি পাঠ: "${teksArab}"\\nঅনুবাদ: "${teksArti}"\\n\\nবিশেষ করে শব্দ/সর্বনাম "${kata}"-এর তাৎপর্যের ওপর গুরুত্ব দিয়ে বলুন, এই আয়াতে কী মূল হেকমত, শানে নুযূল এবং ঐশী বার্তা নিহিত রয়েছে?`;
      } else {
        return `সূরা ${suratNama} (${surat}) আয়াত ${ayat}-এ শব্দ "${kata}" নির্বাচনের ক্ষেত্রে কুরআনিক বালাগাত (অলঙ্কারিক সৌন্দর্য ও রচনাশৈলী) ব্যাখ্যা করুন:\\n\\nআরবি পাঠ: "${teksArab}"\\nঅনুবাদ: "${teksArti}"\\n\\nএখানে সর্বনামের এই নির্দিষ্ট রূপটি কেন ব্যবহৃত হয়েছে? এটি আয়াতের অর্থ ও সাহিত্যের গভীরতায় কী সৌন্দর্য যোগ করে?`;
      }
    } else if (state.lang === 'ru') {
      if (topic === 'nahwu') {
        return `Пожалуйста, подробно объясните арабскую грамматику (нахву/сарф) и и'раб (синтаксический разбор) слова "${kata}" (${noKata}, ${bentuk}) в Суре ${suratNama} (${surat}), аят ${ayat}:\\n\\nАрабский текст: "${teksArab}"\\nПеревод: "${teksArti}"\\n\\nПожалуйста, включите следующие пункты:\\n1. Грамматическая роль "${kata}" в структуре этого предложения и его и'раб (падежное состояние: марфу'/мансуб/маджрур).\\n2. Морфологическая классификация (Дамир мунфасыль/муттасыль или Исм маусуль).\\n3. Грамматическое примечание: ${grammarDesc || 'Классическое кораническое употребление'}.`;
      } else if (topic === 'tafsir') {
        return `Пожалуйста, представьте краткий и контекстуальный тафсир (толкование) Суры ${suratNama} (${surat}), аят ${ayat}:\\n\\nАрабский текст: "${teksArab}"\\nПеревод: "${teksArti}"\\n\\nУделив особое внимание значению слова/местоимения "${kata}", объясните, какой главный смысл, повод ниспослания (сабаб ан-нузуль) и духовное наставление заключены в этом аяте?`;
      } else {
        return `Объясните кораническую риторику и стилистику (баляга) в выборе слова "${kata}" в Суре ${suratNama} (${surat}), аят ${ayat}:\\n\\nАрабский текст: "${teksArab}"\\nПеревод: "${teksArti}"\\n\\nПочему здесь использована именно эта конкретная грамматическая форма? Какую смысловую глубину и красоту она придает аяту?`;
      }
    } else if (state.lang === 'zh') {
      if (topic === 'nahwu') {
        return `请详细解析古兰经苏拉 ${suratNama} (${surat}) 第 ${ayat} 节中词汇 "${kata}" (${noKata}, ${bentuk}) 的阿拉伯语语法 (Nahwu / Sarf) 及语法定位 (I'rab)：\\n\\n阿拉伯语原文: "${teksArab}"\\n中文译文: "${teksArti}"\\n\\n请包含以下要点：\\n1. "${kata}" 在该句子结构中的语法成分与格位状态 (主格/宾格/属格/断格)。\\n2. 词形形态分类 (独立人称代词/接尾人称代词/关系代词)。\\n3. 语法特别说明: ${grammarDesc || '标准古兰经语言用法'}。`;
      } else if (topic === 'tafsir') {
        return `请对苏拉 ${suratNama} (${surat}) 第 ${ayat} 节提供简明且结合语境的经注 (Tafsir) 与内涵阐释：\\n\\n阿拉伯语原文: "${teksArab}"\\n中文译文: "${teksArti}"\\n\\n请重点结合词汇/代词 "${kata}" 的用法，阐明本节经文所蕴含的核心教诲、启示背景 (Sabab al-Nuzul) 以及精神指导意义？`;
      } else {
        return `请赏析苏拉 ${suratNama} (${surat}) 第 ${ayat} 节中选用词汇 "${kata}" 的古兰经修辞美学 (Balaghah) 与文体风格：\\n\\n阿拉伯语原文: "${teksArab}"\\n中文译文: "${teksArti}"\\n\\n为什么此处使用了该特定词形？它为经文的意境深度与文学表现力增添了怎样的色彩？`;
      }
    } else if (state.lang === 'es') {
      if (topic === 'nahwu') {
        return `Por favor explique en detalle la gramática árabe (Nahw/Sarf) y el I'rab para la palabra "${kata}" (${noKata}, ${bentuk}) en el Corán, Sura ${suratNama} (${surat}): Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTraducción: "${teksArti}"\\n\\nPor favor detalle:\\n1. La función sintáctica / posición de I'rab de "${kata}" en la estructura de esta oración.\\n2. Categoría morfológica (tipo de Dhamir / Mawshul) y caso (Marfu'/Manshub/Mayrur).\\n3. Notas gramaticales: ${grammarDesc || 'Uso estándar en el Corán'}.`;
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
        return `Mohon jelaskan secara mendalam kedudukan I'rab dan kaidah tata bahasa Nahwu/Sharaf untuk kata "${kata}" (${noKata}, ${bentuk}) yang terdapat dalam Al-Qur'an Surat ${suratNama} (${surat}) ayat ${ayat}:\\n\\nTeks Arab: "${teksArab}"\\nTerjemahan: "${teksArti}"\\n\\nMohon jelaskan:\\n1. Kedudukan I'rab kata "${kata}" dalam susunan kalimat ini.\\n2. Jenis kata (Dhamir Munfashil/Muttashil atau Isim Mawshul) beserta status kedudukannya (rafa'/nashab/jar).\\n3. Catatan kaidah: ${grammarDesc || 'Kaidah standar Al-Qur\'an'}.`;
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

  """

code = code[:idx_build_prompt] + clean_prompt_and_modal_section + code[idx_close_modal:]

# 5. Clean btnCopyAll
idx_btn_copy = code.find('elements.btnCopyAll.addEventListener(\'click\'')
idx_btn_copy_end = code.find('// Keyboard Navigation', idx_btn_copy)

clean_btn_copy = """elements.btnCopyAll.addEventListener('click', () => {
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

        const summary = `[${titlePrefix}]\n${group.noKata} - ${group.kata} (${group.latin || '-'})\n${t('meaningPrefix')} ${activeArti}\n${activeDesc ? t('wordFormBadge') + ': ' + activeDesc + '\n' : ''}${t('freqLabel')}: ${group.frek ? group.frek + 'x' : t('freqMuttashilVal')}\n${t('totalAyatLabel')}: ${group.occurrences.length} ${t('sampleAyatSuffix')}`;
        
        navigator.clipboard.writeText(summary).then(() => {
          showToast(t('toastSummaryCopied'));
        }).catch(() => {
          showToast('Gagal menyalin ringkasan.');
        });
      });
    }

    """

code = code[:idx_btn_copy] + clean_btn_copy + code[idx_btn_copy_end:]

if crlf:
    code = code.replace('\n', '\r\n')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("app.js completely and perfectly cleaned & updated!")
