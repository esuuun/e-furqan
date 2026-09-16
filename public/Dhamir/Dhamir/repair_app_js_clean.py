#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to build app.js with exact DOM element IDs and complete null-safety.
"""

import os
import sys

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'app.js'), 'r', encoding='utf-8') as f:
    orig_code = f.read()

# Extract the I18N block
idx_start = orig_code.find('  const I18N = {')
idx_end = orig_code.find('  };\n\n  // Helper for current i18n text')
if idx_end == -1:
    idx_end = orig_code.find('function t(')

i18n_block = orig_code[idx_start:idx_end + 4]

app_js_content = """/**
 * Aplikasi Eksplorasi Dhamir & Harf Al-Qur'an (16 Bahasa Dunia)
 * Logika Dropdown Bentuk Kata, Nomor Kata, Audio Tilawah Arab, Audio Terjemahan Multibahasa, & Transliterasi Latin
 */

(function () {
  'use strict';

  // State Management
  const state = {
    activeDict: localStorage.getItem('dhamir_active_dict') || 'jamid', // 'jamid' | 'harf'
    lang: ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa'].includes(localStorage.getItem('dhamir_lang')) ? localStorage.getItem('dhamir_lang') : 'id',
    selectedBentuk: '',
    selectedNoKata: '',
    currentAyatIndex: 0,
    searchQuery: '',
    theme: localStorage.getItem('dhamir_theme') || 'dark'
  };

""" + i18n_block + """

  // Helper for current i18n text
  function t(key, ...args) {
    const langDict = I18N[state.lang] || I18N.id;
    const val = langDict[key] !== undefined ? langDict[key] : (I18N.id[key] || key);
    if (typeof val === 'function') {
      return val(...args);
    }
    return val;
  }

  // DOM Elements Cache
  const elements = {
    docTitle: document.getElementById('docTitle'),
    brandTitle: document.getElementById('brandTitle'),
    brandSubtitle: document.getElementById('brandSubtitle'),
    labelLangSelect: document.getElementById('labelLangSelect'),
    langSelect: document.getElementById('langSelect'),
    translationSourceText: document.getElementById('translationSourceText'),
    themeToggleBtn: document.getElementById('themeToggleBtn'),
    themeIcon: document.getElementById('themeIcon'),
    
    // Tabs
    tabDictJamid: document.getElementById('tabDictJamid'),
    tabDictHarf: document.getElementById('tabDictHarf'),
    labelTabJamid: document.getElementById('labelTabJamid'),
    badgeTabJamid: document.getElementById('badgeTabJamid'),
    labelTabHarf: document.getElementById('labelTabHarf'),
    badgeTabHarf: document.getElementById('badgeTabHarf'),
    
    // Controls
    bentukKataSelect: document.getElementById('bentukKataSelect'),
    noKataSelect: document.getElementById('noKataSelect'),
    
    // Spotlight Card
    spotlightCard: document.getElementById('spotlightCard'),
    badgeBentukKata: document.getElementById('badgeBentukKata'),
    badgeNoKata: document.getElementById('badgeNoKata'),
    badgeJenis: document.getElementById('badgeJenis'),
    arabicWordDisplay: document.getElementById('arabicWordDisplay'),
    wordLatinDisplay: document.getElementById('wordLatinDisplay'),
    wordMeaningDisplay: document.getElementById('wordMeaningDisplay'),
    wordMeaningSub: document.getElementById('wordMeaningSub'),
    labelFreqTitle: document.getElementById('labelFreqTitle'),
    frekSubtitle: document.getElementById('frekSubtitle'),
    frekValueDisplay: document.getElementById('frekValueDisplay'),
    labelTotalAyatTitle: document.getElementById('labelTotalAyatTitle'),
    labelTotalAyatSub: document.getElementById('labelTotalAyatSub'),
    totalAyatBadge: document.getElementById('totalAyatBadge'),
    
    // Spotlight Actions
    btnAudioPlay: document.getElementById('btnAudioPlay'),
    labelAudioArab: document.getElementById('labelAudioArab'),
    btnAudioMeaning: document.getElementById('btnAudioMeaning'),
    labelAudioMeaning: document.getElementById('labelAudioMeaning'),
    btnCopyArabic: document.getElementById('btnCopyArabic'),
    btnCopyAll: document.getElementById('btnCopyAll'),
    
    // References Section
    referencesSection: document.getElementById('referencesSection'),
    ayatSectionTitle: document.getElementById('ayatSectionTitle'),
    ayatSearchInput: document.getElementById('ayatSearchInput'),
    btnExportCsv: document.getElementById('btnExportCsv'),
    labelExportCsv: document.getElementById('labelExportCsv'),
    ayatGridContainer: document.getElementById('ayatGridContainer'),
    emptyStateContainer: document.getElementById('emptyStateContainer'),
    emptyStateText: document.getElementById('emptyStateText'),
    
    // AI Modal
    aiModal: document.getElementById('aiModal'),
    aiModalTitle: document.getElementById('aiModalTitle'),
    aiModalSubtitle: document.getElementById('aiModalSubtitle'),
    aiModalCloseBtn: document.getElementById('aiModalCloseBtn'),
    aiModalArabicVerse: document.getElementById('aiModalArabicVerse'),
    aiModalTranslation: document.getElementById('aiModalTranslation'),
    labelAiTopic: document.getElementById('labelAiTopic'),
    aiTopicChips: document.getElementById('aiTopicChips'),
    labelPromptPreview: document.getElementById('labelPromptPreview'),
    aiPromptTextarea: document.getElementById('aiPromptTextarea'),
    btnOpenGemini: document.getElementById('btnOpenGemini'),
    labelOpenGemini: document.getElementById('labelOpenGemini'),
    btnOpenChatGpt: document.getElementById('btnOpenChatGpt'),
    labelOpenChatGpt: document.getElementById('labelOpenChatGpt'),
    btnCopyPrompt: document.getElementById('btnCopyPrompt'),
    labelCopyPrompt: document.getElementById('labelCopyPrompt'),
    
    // Toast
    toastNotification: document.getElementById('toastNotification')
  };

  // Preferred Sorting Orders for Jamid Mabny categories
  const PREFERRED_NO_KATA_ORDER = {
    '1. Dhamir': [
      '1a', '1b', '1c', '2a', '2b', '3a', '3b', '3c',
      '4a', '4b', '5a', '5b', '6a', '6b', '6c', '7a',
      '7b', '8a', '8b', '8c', '9a', '9b', '9c', '10a',
      '10b', '11a', '11b', '11c', '12a', '12b', '12c'
    ]
  };

  // Group Storage
  let groups = {};
  let availableBentukKatas = [];
  let noKatasByBentuk = {};

  // Audio Playback State
  let currentAudio = null;
  let currentAudioBtn = null;
  let activeUtterance = null;
  let currentPlayingAyatKey = null;

  // AI Modal Context
  let currentAiContext = {
    surat: 1,
    ayat: 1,
    kata: '',
    noKata: '',
    bentuk: '',
    suratNama: '',
    teksArab: '',
    teksArti: '',
    grammarDesc: '',
    topic: 'nahwu'
  };

  // Group key helper
  function getGroupKey(bentuk, noKata) {
    return `${bentuk}__${noKata}`;
  }

  function getGroup(bentuk, noKata) {
    return groups[getGroupKey(bentuk, noKata)] || null;
  }

  // Multi-language Property Helpers
  function getGroupArti(group, lang) {
    if (!group) return '';
    const l = lang || state.lang;
    return group['arti_' + l] || group.arti_id || group.arti || '';
  }

  function getGroupBentuk(group, lang) {
    if (!group) return '';
    const l = lang || state.lang;
    return group['bentuk_' + l] || group.bentuk_id || group.bentuk || '';
  }

  function getGroupDesc(group, lang) {
    if (!group) return '';
    const l = lang || state.lang;
    const g = group.grammar || {};
    return g['desc_' + l] || g.desc_id || g.keterangan || '';
  }

  function getGroupJenis(group, lang) {
    if (!group) return '';
    const l = lang || state.lang;
    const g = group.grammar || {};
    return g['jenis_' + l] || g.jenis_id || g.jenis || getDefaultJenis(group.bentuk, l);
  }

  function getOccSuratArti(occ, lang) {
    if (!occ) return '';
    const l = (lang || state.lang).toUpperCase();
    return occ['suratArti' + l] || occ['SuratArti' + l] || occ.suratArtiEN || occ.SuratArtiEN || occ.suratArtiID || occ.SuratArtiID || occ.suratArti || occ.SuratArti || '';
  }

  function getOccTeksArti(occ, lang) {
    if (!occ) return '';
    const l = (lang || state.lang).toUpperCase();
    return occ['teksArti' + l] || occ['TeksArti' + l] || occ.teksArtiEN || occ.TeksArtiEN || occ.teksArtiID || occ.TeksArtiID || occ.teksArti || occ.TeksArti || '';
  }

  // Switch Active Dictionary ('jamid' | 'harf')
  function switchDictionary(dictKey) {
    state.activeDict = dictKey;
    localStorage.setItem('dhamir_active_dict', dictKey);

    if (elements.tabDictJamid && elements.tabDictHarf) {
      if (dictKey === 'jamid') {
        elements.tabDictJamid.classList.add('active');
        elements.tabDictJamid.setAttribute('aria-selected', 'true');
        elements.tabDictHarf.classList.remove('active');
        elements.tabDictHarf.setAttribute('aria-selected', 'false');
      } else {
        elements.tabDictHarf.classList.add('active');
        elements.tabDictHarf.setAttribute('aria-selected', 'true');
        elements.tabDictJamid.classList.remove('active');
        elements.tabDictJamid.setAttribute('aria-selected', 'false');
      }
    }

    updateHeaderTitles();
    initData();
    populateBentukDropdown();
    
    if (availableBentukKatas.length > 0) {
      selectBentuk(availableBentukKatas[0]);
    } else {
      selectBentuk('');
    }
  }

  // Update Header Titles based on active dictionary
  function updateHeaderTitles() {
    if (!elements.brandTitle) return;
    
    if (state.activeDict === 'harf') {
      if (state.lang === 'fa') {
        elements.brandTitle.innerHTML = 'فرهنگ <span>حرف غیرعامل</span>';
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = 'لغت‌نامه تعاملی حروف غیرعامل قرآن کریم';
        if (elements.docTitle) elements.docTitle.textContent = 'فرهنگ حرف غیرعامل | مراجع تعاملی حروف قرآن';
      } else if (state.lang === 'sw') {
        elements.brandTitle.innerHTML = "Kamusi ya <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Kamusi Shirikishi ya Herufi Zisizo na Athari za Kisarufi";
        if (elements.docTitle) elements.docTitle.textContent = "Kamusi ya Harf Ghair 'Amil | Qur'ani Tukufu";
      } else if (state.lang === 'ha') {
        elements.brandTitle.innerHTML = "Ƙamus ɗin <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Ƙamus Mai Ma'amala don Haruffan da Ba Sa Canza Irabi";
        if (elements.docTitle) elements.docTitle.textContent = "Ƙamus ɗin Harf Ghair 'Amil | Al-Ƙur'ani";
      } else if (state.lang === 'pt') {
        elements.brandTitle.innerHTML = "Dicionário de <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Dicionário Interativo de Partículas Inoperantes do Alcorão";
        if (elements.docTitle) elements.docTitle.textContent = "Dicionário de Harf Ghair 'Amil | Alcorão";
      } else if (state.lang === 'tr') {
        elements.brandTitle.innerHTML = "Kur'an <span>Gayr-i Âmil Harfler</span> Sözlüğü";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "İnteraktif Gayr-i Âmil Harf ve Kelime Numarası Rehberi";
        if (elements.docTitle) elements.docTitle.textContent = "Gayr-i Âmil Harfler Sözlüğü | Kur'an-ı Kerim";
      } else if (state.lang === 'en') {
        elements.brandTitle.innerHTML = "Dictionary of <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Interactive Dictionary of Inoperative Quranic Particles";
        if (elements.docTitle) elements.docTitle.textContent = "Dictionary of Harf Ghair 'Amil | Quranic Particles";
      } else {
        elements.brandTitle.innerHTML = "Kamus <span>Harf Ghair 'Amil</span>";
        if (elements.brandSubtitle) elements.brandSubtitle.textContent = "Kamus Interaktif 17 Bentuk Harf & 52 Kata Al-Qur'an";
        if (elements.docTitle) elements.docTitle.textContent = "Kamus Harf Ghair 'Amil | Rujukan Ayat Interaktif Al-Qur'an";
      }
    } else {
      elements.brandTitle.innerHTML = t('brandTitle');
      if (elements.brandSubtitle) elements.brandSubtitle.textContent = t('brandSubtitle');
      if (elements.docTitle) elements.docTitle.textContent = t('pageTitle');
    }
  }

  // Parse Raw Dataset into Organized Groupings
  function initData() {
    let rawDataset = [];
    if (state.activeDict === 'harf' && typeof HARF_DATA !== 'undefined') {
      rawDataset = HARF_DATA;
    } else if (typeof DHAMIR_DATA !== 'undefined') {
      rawDataset = DHAMIR_DATA;
    }

    groups = {};
    availableBentukKatas = [];
    noKatasByBentuk = {};

    rawDataset.forEach(item => {
      const b = item['Bentuk Kata'] || item['BentukKata'] || '';
      const nk = item['No kata'] || item['NoKata'] || '';
      if (!b || !nk) return;

      const groupKey = getGroupKey(b, nk);

      if (!groups[groupKey]) {
        const grammar = item['Grammar'] || {};
        groups[groupKey] = {
          bentuk: b,
          noKata: nk,
          kata: item['Kata'] || '',
          latin: item['Latin'] || grammar.latin || item['Kata'] || '',
          frek: item['Frek kata'] || item['Frek'] || item['FrekKata'] || '',
          arti: item['Arti kata'] || item['Arti'] || '',
          grammar: grammar,
          
          // Multilingual Bentuk Kata
          bentuk_id: item['BentukKataID'] || b,
          bentuk_en: item['BentukKataEN'] || b,
          bentuk_ms: item['BentukKataMS'] || b,
          bentuk_fr: item['BentukKataFR'] || b,
          bentuk_de: item['BentukKataDE'] || b,
          bentuk_ur: item['BentukKataUR'] || b,
          bentuk_hi: item['BentukKataHI'] || b,
          bentuk_bn: item['BentukKataBN'] || b,
          bentuk_ru: item['BentukKataRU'] || b,
          bentuk_zh: item['BentukKataZH'] || b,
          bentuk_es: item['BentukKataES'] || b,
          bentuk_tr: item['BentukKataTR'] || b,
          bentuk_pt: item['BentukKataPT'] || b,
          bentuk_ha: item['BentukKataHA'] || b,
          bentuk_sw: item['BentukKataSW'] || b,
          bentuk_fa: item['BentukKataFA'] || b,
          
          // Multilingual Word Meanings
          arti_id: item['ArtiKataID'] || grammar.arti_id || item['Arti kata'] || '',
          arti_en: item['ArtiKataEN'] || grammar.arti_en || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_ms: item['ArtiKataMS'] || grammar.arti_ms || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_fr: item['ArtiKataFR'] || grammar.arti_fr || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_de: item['ArtiKataDE'] || grammar.arti_de || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_ur: item['ArtiKataUR'] || grammar.arti_ur || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_hi: item['ArtiKataHI'] || grammar.arti_hi || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_bn: item['ArtiKataBN'] || grammar.arti_bn || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_ru: item['ArtiKataRU'] || grammar.arti_ru || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_zh: item['ArtiKataZH'] || grammar.arti_zh || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_es: item['ArtiKataES'] || grammar.arti_es || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_tr: item['ArtiKataTR'] || grammar.arti_tr || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_pt: item['ArtiKataPT'] || grammar.arti_pt || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_ha: item['ArtiKataHA'] || grammar.arti_ha || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_sw: item['ArtiKataSW'] || grammar.arti_sw || item['ArtiKataID'] || item['Arti kata'] || '',
          arti_fa: item['ArtiKataFA'] || grammar.arti_fa || item['ArtiKataID'] || item['Arti kata'] || '',

          occurrences: []
        };

        if (!availableBentukKatas.includes(b)) {
          availableBentukKatas.push(b);
          noKatasByBentuk[b] = [];
        }
        if (!noKatasByBentuk[b].includes(nk)) {
          noKatasByBentuk[b].push(nk);
        }
      }

      groups[groupKey].occurrences.push({
        surat: parseInt(item['SURAT'] || item['Surat'] || 1, 10),
        ayat: parseInt(item['AYAT'] || item['Ayat'] || 1, 10),
        suratNama: item['SuratNama'] || `Surat ${item['SURAT']}`,
        suratArab: item['SuratArab'] || '',
        
        // Surat Meanings
        suratArtiID: item['SuratArtiID'] || item['SuratArti'] || '',
        suratArtiEN: item['SuratArtiEN'] || item['SuratArti'] || '',
        suratArtiMS: item['SuratArtiMS'] || item['SuratArti'] || '',
        suratArtiFR: item['SuratArtiFR'] || item['SuratArtiEN'] || '',
        suratArtiDE: item['SuratArtiDE'] || item['SuratArtiEN'] || '',
        suratArtiUR: item['SuratArtiUR'] || item['SuratArtiEN'] || '',
        suratArtiHI: item['SuratArtiHI'] || item['SuratArtiEN'] || '',
        suratArtiBN: item['SuratArtiBN'] || item['SuratArtiEN'] || '',
        suratArtiRU: item['SuratArtiRU'] || item['SuratArtiEN'] || '',
        suratArtiZH: item['SuratArtiZH'] || item['SuratArtiEN'] || '',
        suratArtiES: item['SuratArtiES'] || item['SuratArtiEN'] || '',
        suratArtiTR: item['SuratArtiTR'] || item['SuratArtiEN'] || '',
        suratArtiPT: item['SuratArtiPT'] || item['SuratArtiEN'] || '',
        suratArtiHA: item['SuratArtiHA'] || item['SuratArtiEN'] || '',
        suratArtiSW: item['SuratArtiSW'] || item['SuratArtiEN'] || '',
        suratArtiFA: item['SuratArtiFA'] || item['SuratArtiEN'] || '',

        teksArab: item['TeksArab'] || '',
        teksLatin: item['TeksLatin'] || '',
        
        // Verse Translations
        teksArtiID: item['TeksArtiID'] || item['TeksArti'] || '',
        teksArtiEN: item['TeksArtiEN'] || item['TeksArti'] || '',
        teksArtiMS: item['TeksArtiMS'] || item['TeksArti'] || '',
        teksArtiFR: item['TeksArtiFR'] || item['TeksArtiEN'] || '',
        teksArtiDE: item['TeksArtiDE'] || item['TeksArtiEN'] || '',
        teksArtiUR: item['TeksArtiUR'] || item['TeksArti'] || '',
        teksArtiHI: item['TeksArtiHI'] || item['TeksArti'] || '',
        teksArtiBN: item['TeksArtiBN'] || item['TeksArti'] || '',
        teksArtiRU: item['TeksArtiRU'] || item['TeksArti'] || '',
        teksArtiZH: item['TeksArtiZH'] || item['TeksArti'] || '',
        teksArtiES: item['TeksArtiES'] || item['TeksArti'] || '',
        teksArtiTR: item['TeksArtiTR'] || item['TeksArti'] || '',
        teksArtiPT: item['TeksArtiPT'] || item['TeksArti'] || '',
        teksArtiHA: item['TeksArtiHA'] || item['TeksArti'] || '',
        teksArtiSW: item['TeksArtiSW'] || item['TeksArti'] || '',
        teksArtiFA: item['TeksArtiFA'] || item['TeksArti'] || '',

        audioUrl: item['AudioUrl'] || getAyatAudioUrl(item['SURAT'], item['AYAT'])
      });
    });

    // Sort categories numerically
    availableBentukKatas.sort((a, bVal) => {
      const numA = parseInt(a.split('.')[0], 10) || 0;
      const numB = parseInt(bVal.split('.')[0], 10) || 0;
      if (numA !== numB) return numA - numB;
      return a.localeCompare(bVal);
    });

    // Sort No Katas in each category
    Object.keys(noKatasByBentuk).forEach(b => {
      const preferred = PREFERRED_NO_KATA_ORDER[b];
      if (preferred) {
        noKatasByBentuk[b].sort((a, bVal) => {
          const idxA = preferred.indexOf(a);
          const idxB = preferred.indexOf(bVal);
          if (idxA !== -1 && idxB !== -1) return idxA - idxB;
          if (idxA !== -1) return -1;
          if (idxB !== -1) return 1;
          return a.localeCompare(bVal, undefined, { numeric: true });
        });
      } else {
        noKatasByBentuk[b].sort((a, bVal) => {
          const intA = parseInt(a, 10);
          const intB = parseInt(bVal, 10);
          if (!isNaN(intA) && !isNaN(intB)) return intA - intB;
          return a.localeCompare(bVal, undefined, { numeric: true });
        });
      }
    });

    // Validate selected options
    if (state.selectedBentuk && !availableBentukKatas.includes(state.selectedBentuk)) {
      state.selectedBentuk = '';
    }
    const currentBentukList = noKatasByBentuk[state.selectedBentuk] || [];
    if (state.selectedNoKata && !currentBentukList.includes(state.selectedNoKata)) {
      state.selectedNoKata = '';
    }
  }

  // Populate Bentuk Kata Dropdown
  function populateBentukDropdown() {
    if (!elements.bentukKataSelect) return;
    elements.bentukKataSelect.innerHTML = '';

    const placeholderOption = document.createElement('option');
    placeholderOption.value = '';
    placeholderOption.textContent = t('step1Placeholder');
    if (!state.selectedBentuk) {
      placeholderOption.selected = true;
    }
    elements.bentukKataSelect.appendChild(placeholderOption);

    function getBentukLabelText(b) {
      if (state.activeDict === 'harf' && typeof HARF_BENTUK_LABELS !== 'undefined' && HARF_BENTUK_LABELS[b]) {
        return HARF_BENTUK_LABELS[b][state.lang] || HARF_BENTUK_LABELS[b]['id'] || b;
      }
      const map = {
        '1. Dhamir': 'step1OptionDhamir',
        '2. Mawshul': 'step1OptionMawshul',
        '3. Istifham': 'step1OptionIstifham',
        '4. Syarath': 'step1OptionSyarath',
        '5. Isyarah': 'step1OptionIsyarah',
        "6. Isim Fi'il": 'step1OptionIsimFiil',
        "7. Fi'il Jamid": 'step1OptionFiilJamid'
      };
      const key = map[b];
      if (key && I18N[state.lang] && I18N[state.lang][key]) {
        return I18N[state.lang][key];
      }
      return b;
    }

    availableBentukKatas.forEach(b => {
      const option = document.createElement('option');
      option.value = b;
      option.textContent = getBentukLabelText(b);
      if (state.selectedBentuk === b) {
        option.selected = true;
      }
      elements.bentukKataSelect.appendChild(option);
    });

    elements.bentukKataSelect.value = state.selectedBentuk || '';
  }

  // Populate No Kata Dropdown
  function populateNoKataDropdown() {
    if (!elements.noKataSelect) return;
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
      const localizedArti = getGroupArti(group, state.lang);
      
      option.textContent = `${nk} - ${group.kata} ${latinPart}(${localizedArti})`;
      if (state.selectedNoKata === nk) {
        option.selected = true;
      }
      elements.noKataSelect.appendChild(option);
    });

    elements.noKataSelect.value = state.selectedNoKata || '';
  }

  // Get Default Category Jenis (Fallback)
  function getDefaultJenis(bentuk, lang) {
    const defaultMap = {
      '1. Dhamir': {
        id: 'Munfashil', en: 'Munfashil', ms: 'Munfashil', fr: 'Munfashil', de: 'Munfashil',
        ur: 'منفصل', hi: 'मुन्फ़सिल', bn: 'মুনফাসিল', ru: 'Мунфасыль', zh: '独立代词', es: 'Munfashil (Independiente)', tr: 'Munfasıl (Ayrık Zamir)', pt: 'Munfashil (Independente)', ha: 'Munfashil (Mai Zaman Kansa)', sw: 'Munfashil (Kiwakilishi Huru)', fa: 'منفصل مرفوعی (ضمایر جدا)'
      },
      '2. Mawshul': {
        id: 'Isim Mawshul', en: 'Relative Pronoun', ms: 'Isim Mawshul', fr: 'Pronom Relatif', de: 'Relativpronomen',
        ur: 'اسم موصول', hi: 'संबंधवाचक सर्वनाम', bn: 'সম্বন্ধবাচক सर्वनाम', ru: 'Относительное местоимение', zh: '关系代词', es: 'Pronombre Relativo', tr: 'İsmi Mevsul (İlgi Zamiri)', pt: 'Pronome Relativo', ha: 'Isim Mawshul (Sunan Sadarwa)', sw: 'Isim Mawshul (Jina la Kuunganisha)', fa: 'اسم موصول'
      },
      '3. Istifham': {
        id: 'Isim Istifham', en: 'Interrogative', ms: 'Isim Istifham', fr: 'Mot Interrogatif', de: 'Fragewort',
        ur: 'اسم استفہام', hi: 'प्रश्नवाचक शब्द', bn: 'প্রশ্নবোধক शब्द', ru: 'Вопросительное слово', zh: '疑问代词', es: 'Interrogativo', tr: 'Soru Edatı (İstifham)', pt: 'Interrogativo', ha: 'Kalmar Tambaya (Istifham)', sw: 'Isim Istifham (Neno la Kuulizia)', fa: 'اسم استفهام (کلمات پرسشی)'
      },
      '4. Syarath': {
        id: 'Isim Syarat', en: 'Conditional', ms: 'Isim Syarat', fr: 'Mot Conditionnel', de: 'Konditionalwort',
        ur: 'اسم شرط', hi: 'शर्तवाचक शब्द', bn: 'শর্তমূলক शब्द', ru: 'Условное слово', zh: '条件代词', es: 'Condicional', tr: 'Şart Edatı', pt: 'Condicional', ha: 'Kalmar Sharaɗi (Syarath)', sw: 'Isim Syarat (Neno la Sharti)', fa: 'ادوات شرط'
      },
      '5. Isyarah': {
        id: 'Isim Isyarah', en: 'Demonstrative', ms: 'Isim Isyarah', fr: 'Pronom Démonstratif', de: 'Demonstrativpronomen',
        ur: 'اسم اشارہ', hi: 'संकेतवाचक सर्वनाम', bn: 'নির্দেশক सर्वनाम', ru: 'Указательное местоимение', zh: '指示代词', es: 'Demonstrativo', tr: 'İşaret Zamiri', pt: 'Demonstrativo', ha: 'Sunan Nuni (Isyarah)', sw: 'Isim Isyarah (Jina la Kuonyeshea)', fa: 'اسم اشاره'
      },
      "6. Isim Fi'il": {
        id: "Isim Fi'il", en: "Verbal Noun", ms: "Isim Fi'il", fr: "Nom Verbal", de: "Verbalnomen",
        ur: "اسم فعل", hi: "क्रियार्थک संज्ञा", bn: "ক্রিয়াভিত্তিক বিশেষ্য", ru: "Глагольное имя", zh: "动名词", es: "Nombre Verbal", tr: "İsim Fiil", pt: "Nome Verbal", ha: "Sunan Aiki (Isim Fi'il)", sw: "Isim Fi'il (Jina la Kitendo)", fa: "اسم فعل"
      },
      "7. Fi'il Jamid": {
        id: "Fi'il Jamid", en: "Inflexible Verb", ms: "Fi'il Jamid", fr: "Verbe Inflexible", de: "Inflexibles Verb",
        ur: "فعل جامد", hi: "रूढ़ क्रिया", bn: "অপরিবর্তনীয় ক্রিয়া", ru: "Неспрягаемый глагол", zh: "不变动词", es: "Verbo Inflexible", tr: "Câmid Fiil", pt: "Verbo Inflexível", ha: "Aiki Kafaffe (Fi'il Jamid)", sw: "Fi'il Jamid (Kitendo Kisichobadilika)", fa: "فعل جامد"
      }
    };
    const bMap = defaultMap[bentuk];
    if (bMap) {
      return bMap[lang] || bMap['id'] || bentuk;
    }
    return bentuk;
  }

  // Update Spotlight Card
  function updateSpotlightCard() {
    const group = getGroup(state.selectedBentuk, state.selectedNoKata);

    if (!group) {
      if (elements.spotlightCard) elements.spotlightCard.style.display = 'none';
      return;
    }

    if (elements.spotlightCard) elements.spotlightCard.style.display = 'block';

    // Badge texts
    if (elements.badgeBentukKata) elements.badgeBentukKata.textContent = getGroupBentuk(group, state.lang);
    if (elements.badgeNoKata) elements.badgeNoKata.textContent = `${t('wordNoBadgePrefix')} ${group.noKata}`;
    if (elements.badgeJenis) elements.badgeJenis.textContent = getGroupJenis(group, state.lang);

    // Displays
    if (elements.arabicWordDisplay) elements.arabicWordDisplay.textContent = group.kata;
    if (elements.wordLatinDisplay) elements.wordLatinDisplay.textContent = group.latin || group.kata;
    if (elements.wordMeaningDisplay) elements.wordMeaningDisplay.textContent = getGroupArti(group, state.lang);
    if (elements.wordMeaningSub) elements.wordMeaningSub.textContent = getGroupDesc(group, state.lang);

    // Frequency
    if (elements.labelFreqTitle) elements.labelFreqTitle.textContent = t('freqLabel');
    if (elements.frekValueDisplay) {
      if (group.frek) {
        elements.frekValueDisplay.textContent = `${group.frek} ×`;
        if (elements.frekSubtitle) elements.frekSubtitle.textContent = t('freqSub');
      } else {
        elements.frekValueDisplay.textContent = t('freqMuttashilVal');
        if (elements.frekSubtitle) elements.frekSubtitle.textContent = t('freqMuttashilSub');
      }
    }

    // Total Ayats
    const totalOccurrences = group.occurrences ? group.occurrences.length : 0;
    if (elements.labelTotalAyatTitle) elements.labelTotalAyatTitle.textContent = t('totalAyatLabel');
    if (elements.labelTotalAyatSub) elements.labelTotalAyatSub.textContent = t('totalAyatSub');
    if (elements.totalAyatBadge) elements.totalAyatBadge.textContent = `${totalOccurrences} Ayat`;
  }

  // Audio EveryAyah helper
  function getAyatAudioUrl(surat, ayat) {
    const s = String(surat).padStart(3, '0');
    const a = String(ayat).padStart(3, '0');
    return `https://everyayah.com/data/Alafasy_128kbps/${s}${a}.mp3`;
  }

  // Stop All Audio and TTS
  function stopAllSpeech() {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
    activeUtterance = null;
  }

  function stopVerseAudio() {
    if (currentAudio) {
      currentAudio.pause();
      currentAudio.currentTime = 0;
      currentAudio = null;
    }
    currentPlayingAyatKey = null;
  }

  function stopAllAudio() {
    stopAllSpeech();
    stopVerseAudio();
    updateAllAudioButtonStates();
  }

  // Update All Button States
  function updateAllAudioButtonStates() {
    document.querySelectorAll('.btn-play-tilawah').forEach(btn => {
      const icon = btn.querySelector('.audio-icon');
      const label = btn.querySelector('.audio-label');
      if (icon) icon.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>';
      if (label) label.textContent = t('playTilawahBtn');
      btn.classList.remove('playing');
    });

    document.querySelectorAll('.btn-play-translation').forEach(btn => {
      const icon = btn.querySelector('.audio-icon');
      const label = btn.querySelector('.audio-label');
      if (icon) icon.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>';
      if (label) label.textContent = t('playTranslationBtn');
      btn.classList.remove('playing');
    });
  }

  // Toggle Verse Tilawah Audio (Mishary Alafasy)
  function toggleVerseAudio(surat, ayat, audioUrl, buttonEl) {
    const ayatKey = `${surat}:${ayat}`;

    if (currentPlayingAyatKey === ayatKey && currentAudio && !currentAudio.paused) {
      stopVerseAudio();
      updateAllAudioButtonStates();
      showToast(t('toastTilawahPaused'));
      return;
    }

    stopAllAudio();

    currentAudio = new Audio(audioUrl);
    currentPlayingAyatKey = ayatKey;
    currentAudioBtn = buttonEl;

    const icon = buttonEl.querySelector('.audio-icon');
    const label = buttonEl.querySelector('.audio-label');
    if (icon) icon.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect></svg>';
    if (label) label.textContent = t('pauseTilawahBtn');
    buttonEl.classList.add('playing');

    showToast(t('toastTilawahPlaying', surat, ayat));

    currentAudio.play().catch(err => {
      console.error('Audio playback error:', err);
      stopVerseAudio();
      updateAllAudioButtonStates();
      showToast(t('toastAudioFailed'));
    });

    currentAudio.onended = () => {
      stopVerseAudio();
      updateAllAudioButtonStates();
      showToast(t('toastTilawahEnded'));
    };
  }

  // Speech Voice Selector Helper
  function getSpeechVoiceAndLang(langKey) {
    let speechLangCode = 'id-ID';
    let matchVoice = null;
    const voices = ('speechSynthesis' in window) ? window.speechSynthesis.getVoices() : [];

    if (langKey === 'ar') {
      speechLangCode = 'ar-SA';
      matchVoice = voices.find(v => v.lang.startsWith('ar') && (v.name.includes('Maged') || v.name.includes('Tariq') || v.name.includes('Arabic') || v.name.includes('Saudi') || v.name.includes('Google'))) || voices.find(v => v.lang.startsWith('ar'));
    } else if (langKey === 'en') {
      speechLangCode = 'en-US';
      matchVoice = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha') || v.name.includes('David') || v.name.includes('US'))) || voices.find(v => v.lang.startsWith('en'));
    } else if (langKey === 'ms') {
      speechLangCode = 'ms-MY';
      matchVoice = voices.find(v => v.lang.startsWith('ms') || v.name.toLowerCase().includes('malay')) || voices.find(v => v.lang.startsWith('id'));
    } else if (langKey === 'fr') {
      speechLangCode = 'fr-FR';
      matchVoice = voices.find(v => v.lang.startsWith('fr')) || voices.find(v => v.lang.startsWith('fr'));
    } else if (langKey === 'de') {
      speechLangCode = 'de-DE';
      matchVoice = voices.find(v => v.lang.startsWith('de')) || voices.find(v => v.lang.startsWith('de'));
    } else if (langKey === 'ur') {
      speechLangCode = 'ur-PK';
      matchVoice = voices.find(v => v.lang.startsWith('ur') || v.name.toLowerCase().includes('urdu') || v.name.toLowerCase().includes('pakistan')) || voices.find(v => v.lang.startsWith('hi'));
    } else if (langKey === 'hi') {
      speechLangCode = 'hi-IN';
      matchVoice = voices.find(v => v.lang.startsWith('hi') || v.name.toLowerCase().includes('hindi')) || voices.find(v => v.lang.startsWith('hi'));
    } else if (langKey === 'bn') {
      speechLangCode = 'bn-BD';
      matchVoice = voices.find(v => v.lang.startsWith('bn') || v.name.toLowerCase().includes('bangla') || v.name.toLowerCase().includes('bengali')) || voices.find(v => v.lang.startsWith('bn'));
    } else if (langKey === 'ru') {
      speechLangCode = 'ru-RU';
      matchVoice = voices.find(v => v.lang.startsWith('ru') || v.name.toLowerCase().includes('russian')) || voices.find(v => v.lang.startsWith('ru'));
    } else if (langKey === 'zh') {
      speechLangCode = 'zh-CN';
      matchVoice = voices.find(v => v.lang.startsWith('zh') || v.name.toLowerCase().includes('chinese')) || voices.find(v => v.lang.startsWith('zh'));
    } else if (langKey === 'es') {
      speechLangCode = 'es-ES';
      matchVoice = voices.find(v => v.lang.startsWith('es') || v.name.toLowerCase().includes('spanish')) || voices.find(v => v.lang.startsWith('es'));
    } else if (langKey === 'tr') {
      speechLangCode = 'tr-TR';
      matchVoice = voices.find(v => v.lang.startsWith('tr') || v.name.toLowerCase().includes('turkish')) || voices.find(v => v.lang.startsWith('tr'));
    } else if (langKey === 'pt') {
      speechLangCode = 'pt-PT';
      matchVoice = voices.find(v => v.lang.startsWith('pt') || v.name.toLowerCase().includes('portuguese')) || voices.find(v => v.lang.startsWith('pt'));
    } else if (langKey === 'ha') {
      speechLangCode = 'ha-NG';
      matchVoice = voices.find(v => v.lang.startsWith('ha') || v.name.toLowerCase().includes('hausa')) || voices.find(v => v.lang.startsWith('ha'));
    } else if (langKey === 'sw') {
      speechLangCode = 'sw-TZ';
      matchVoice = voices.find(v => v.lang.startsWith('sw') || v.name.toLowerCase().includes('swahili') || v.name.toLowerCase().includes('kiswahili')) || voices.find(v => v.lang.startsWith('sw'));
    } else if (langKey === 'fa') {
      speechLangCode = 'fa-IR';
      matchVoice = voices.find(v => v.lang.startsWith('fa') || v.name.toLowerCase().includes('persian') || v.name.toLowerCase().includes('farsi') || v.name.includes('فارسی')) || voices.find(v => v.lang.startsWith('fa'));
    } else {
      speechLangCode = 'id-ID';
      matchVoice = voices.find(v => v.lang.startsWith('id') || v.name.toLowerCase().includes('indonesian') || v.name.toLowerCase().includes('gadis')) || voices.find(v => v.lang.startsWith('id'));
    }

    return { speechLangCode, matchVoice };
  }

  // Speak Arabic Word
  function speakArabicWord(word) {
    if (!('speechSynthesis' in window)) {
      showToast(t('toastTtsNotSupported'));
      return;
    }
    stopAllAudio();

    const cleanWord = (word || '').replace(/\.\./g, '').replace(/\s*\d+$/, '');
    const { speechLangCode, matchVoice } = getSpeechVoiceAndLang('ar');

    const utterance = new SpeechSynthesisUtterance(cleanWord);
    utterance.lang = speechLangCode;
    utterance.rate = 0.85;
    if (matchVoice) utterance.voice = matchVoice;

    showToast(t('toastSpeakingArabic', cleanWord));
    window.speechSynthesis.speak(utterance);
  }

  // Speak Dhamir Meaning
  function speakDhamirMeaning(group) {
    if (!('speechSynthesis' in window)) {
      showToast(t('toastTtsNotSupported'));
      return;
    }
    if (!group) return;
    stopAllAudio();

    const langDict = I18N[state.lang] || I18N.id;
    const text = langDict.ttsMeaningSpeech ? langDict.ttsMeaningSpeech(group) : `${group.kata}, ${getGroupArti(group, state.lang)}`;
    const { speechLangCode, matchVoice } = getSpeechVoiceAndLang(state.lang);

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = speechLangCode;
    utterance.rate = 0.95;
    if (matchVoice) utterance.voice = matchVoice;

    showToast(t('toastSpeakingWordMeaning', getGroupArti(group, state.lang)));
    window.speechSynthesis.speak(utterance);
  }

  // Toggle Verse Translation Audio (TTS)
  function toggleVerseTranslationAudio(surat, ayat, text, buttonEl) {
    if (!('speechSynthesis' in window)) {
      showToast(t('toastTtsNotSupported'));
      return;
    }

    if (activeUtterance && window.speechSynthesis.speaking) {
      stopAllSpeech();
      updateAllAudioButtonStates();
      showToast(t('toastTranslationStopped'));
      return;
    }

    stopAllAudio();

    if (!text || text.trim() === '') {
      showToast(t('toastTranslationNotAvail'));
      return;
    }

    const { speechLangCode, matchVoice } = getSpeechVoiceAndLang(state.lang);
    const cleanText = text.replace(/<[^>]*>/g, '').replace(/[()"]/g, ' ');

    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.lang = speechLangCode;
    utterance.rate = 0.95;
    if (matchVoice) utterance.voice = matchVoice;

    activeUtterance = utterance;

    if (buttonEl) {
      buttonEl.classList.add('speaking');
      const icon = buttonEl.querySelector('.audio-icon-state');
      if (icon) icon.innerHTML = '<rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect>';
    }

    showToast(t('toastSpeakingMeaning', surat, ayat));

    utterance.onend = () => {
      activeUtterance = null;
      updateAllAudioButtonStates();
    };

    utterance.onerror = () => {
      activeUtterance = null;
      updateAllAudioButtonStates();
    };

    window.speechSynthesis.speak(utterance);
  }

  // Arabic Target Word Highlight
  function highlightArabicVerse(fullArabText, targetKata) {
    if (!fullArabText || !targetKata) return fullArabText || '';
    
    // Clean target kata diacritics for flexible matching
    const cleanTarget = targetKata.replace(/[\u064B-\u065F\u0670]/g, '').trim();
    if (!cleanTarget) return fullArabText;

    // Pattern matching Arabic word tokens
    const words = fullArabText.split(/\s+/);
    const highlightedWords = words.map(w => {
      const cleanW = w.replace(/[\u064B-\u065F\u0670]/g, '');
      if (cleanW.includes(cleanTarget) || cleanTarget.includes(cleanW)) {
        return `<span class="ayat-highlight-red">${w}</span>`;
      }
      return w;
    });

    return highlightedWords.join(' ');
  }

  // Render Ayat References in Grand Single-Ayat Screen Presentation
  function renderAyatReferences(groupOverride, queryOverride) {
    const group = groupOverride || getGroup(state.selectedBentuk, state.selectedNoKata);

    if (!elements.ayatGridContainer) return;
    elements.ayatGridContainer.innerHTML = '';

    if (!group || !group.occurrences || group.occurrences.length === 0) {
      if (elements.referencesSection) elements.referencesSection.style.display = 'none';
      return;
    }

    if (elements.referencesSection) elements.referencesSection.style.display = 'block';

    // Clean parentheses from word meaning
    const rawArti = getGroupArti(group, state.lang);
    const cleanArti = rawArti.replace(/^\((.*)\)$/, '$1');

    // Section title
    if (elements.ayatSectionTitle) {
      elements.ayatSectionTitle.innerHTML = `
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
          <polyline points="14 2 14 8 20 8"></polyline>
          <line x1="16" y1="13" x2="8" y2="13"></line>
          <line x1="16" y1="17" x2="8" y2="17"></line>
          <polyline points="10 9 9 9 8 9"></polyline>
        </svg>
        <span>${t('referencesTitlePrefix')} ${group.kata} (${cleanArti})</span>
      `;
    }

    // Filter occurrences by search query
    const q = (queryOverride !== undefined ? queryOverride : state.searchQuery).trim().toLowerCase();
    let filtered = group.occurrences;
    if (q) {
      filtered = group.occurrences.filter(occ => {
        const sNama = (occ.suratNama || '').toLowerCase();
        const sArti = getOccSuratArti(occ, state.lang).toLowerCase();
        const tArti = getOccTeksArti(occ, state.lang).toLowerCase();
        const sNum = String(occ.surat);
        const aNum = String(occ.ayat);
        return sNama.includes(q) || sArti.includes(q) || tArti.includes(q) || sNum === q || aNum === q || `${sNum}:${aNum}` === q;
      });
    }

    if (filtered.length === 0) {
      if (elements.emptyStateContainer) elements.emptyStateContainer.style.display = 'block';
      if (elements.emptyStateText) elements.emptyStateText.textContent = t('emptyStateText');
      return;
    } else {
      if (elements.emptyStateContainer) elements.emptyStateContainer.style.display = 'none';
    }

    const totalCount = filtered.length;
    if (state.currentAyatIndex >= totalCount) {
      state.currentAyatIndex = 0;
    }
    const currentIdx = state.currentAyatIndex;
    const occ = filtered[currentIdx];

    const singleScreenWrap = document.createElement('div');
    singleScreenWrap.className = 'single-ayat-screen animate-fade-in';

    // 1. Navigation Tabs & Arrows Toolbar
    const navBar = document.createElement('div');
    navBar.className = 'ayat-nav-toolbar';

    let tabsHtml = '';
    filtered.forEach((item, idx) => {
      const isActive = idx === currentIdx ? 'active' : '';
      tabsHtml += `
        <button type="button" class="ayat-select-tab ${isActive}" data-idx="${idx}" aria-label="Ayat ke-${idx + 1}">
          <span class="tab-number">${idx + 1}</span>
          <span>${item.suratNama} : ${item.ayat}</span>
        </button>
      `;
    });

    navBar.innerHTML = `
      <div class="ayat-nav-arrow-group">
        <button type="button" class="btn btn-outline btn-icon-nav btn-prev-ayat" ${currentIdx === 0 ? 'disabled' : ''} title="Ayat Sebelumnya (Arrow Left / k)">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polyline points="15 18 9 12 15 6"></polyline>
          </svg>
          <span>Prev</span>
        </button>
        <span class="ayat-page-counter">${currentIdx + 1} / ${totalCount}</span>
        <button type="button" class="btn btn-outline btn-icon-nav btn-next-ayat" ${currentIdx === totalCount - 1 ? 'disabled' : ''} title="Ayat Selanjutnya (Arrow Right / j)">
          <span>Next</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polyline points="9 18 15 12 9 6"></polyline>
          </svg>
        </button>
      </div>
      <div class="ayat-tab-group">
        ${tabsHtml}
      </div>
    `;

    // 2. Grand Unified Verse Card
    const cardWrapper = document.createElement('div');
    cardWrapper.className = 'single-ayat-card-wrapper';

    const activeSuratArti = getOccSuratArti(occ, state.lang);
    const activeTeksArti = getOccTeksArti(occ, state.lang);
    const highlightedArab = highlightArabicVerse(occ.teksArab, group.kata);

    cardWrapper.innerHTML = `
      <div class="single-ayat-unified-card animate-fade-in">
        <div class="ayat-top-row">
          <div class="surat-identity-badge">
            <div class="surat-number-circle surat-circle-gold">${occ.surat}</div>
            <div>
              <div class="surat-main-name">
                ${occ.suratNama} 
                <span class="surat-meaning-bracket">${activeSuratArti ? '(' + activeSuratArti + ')' : ''}</span>
              </div>
              ${occ.suratArab ? `<div class="surat-arabic-title font-arabic">${occ.suratArab}</div>` : ''}
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
              <span class="ai-sparkle-icon">✨</span>
              <span>${t('askAiBtn')}</span>
            </button>

            <span class="ayat-number-pill ayat-number-gold">${t('ayahPill', occ.ayat)}</span>
          </div>
        </div>

        <div class="ayat-body-content">
          <!-- 1. Teks Arab Penuh dengan Red Highlight -->
          <div class="arabic-verse-container notranslate" translate="no">
            <div class="single-ayat-arabic-text font-arabic notranslate" translate="no" dir="rtl">
              ${highlightedArab}
            </div>
          </div>

          <!-- 2. Terjemahan Ayat dengan Tombol Audio Suara -->
          <div class="verse-translation-box">
            <span class="content-pill-header tag-translation">${t('translationBoxHeader')}</span>
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

          <!-- 3. Bacaan Latin / Transliterasi jika ada -->
          ${occ.teksLatin ? `
          <div class="verse-latin-box notranslate" translate="no">
            <span class="content-pill-header tag-latin">${t('latinBoxHeader')}</span>
            <p class="verse-latin-text notranslate" translate="no">${occ.teksLatin}</p>
          </div>` : ''}
        </div>
      </div>
    `;

    // Audio Play Buttons inside card (Murottal Tilawah)
    cardWrapper.querySelectorAll('.btn-play-verse-audio').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const surat = btn.getAttribute('data-surat');
        const ayat = btn.getAttribute('data-ayat');
        const audioUrl = btn.getAttribute('data-audio');
        toggleVerseAudio(surat, ayat, audioUrl, btn);
      });
    });

    // Ask AI Button inside card
    cardWrapper.querySelectorAll('.btn-ask-ai').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        openAiModal(occ.surat, occ.ayat, group.kata, group.noKata, group.bentuk);
      });
    });

    // Audio Translation Buttons inside card
    cardWrapper.querySelectorAll('.btn-play-translation-audio').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        toggleVerseTranslationAudio(occ.surat, occ.ayat, activeTeksArti, btn);
      });
    });

    // Tab buttons event
    navBar.querySelectorAll('.ayat-select-tab').forEach(tab => {
      tab.addEventListener('click', (e) => {
        const targetIdx = parseInt(tab.getAttribute('data-idx'), 10);
        if (!isNaN(targetIdx) && targetIdx !== state.currentAyatIndex) {
          state.currentAyatIndex = targetIdx;
          stopAllAudio();
          renderAyatReferences(group, state.searchQuery);
        }
      });
    });

    // Prev / Next button events
    const prevBtn = navBar.querySelector('.btn-prev-ayat');
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (state.currentAyatIndex > 0) {
          state.currentAyatIndex--;
          stopAllAudio();
          renderAyatReferences(group, state.searchQuery);
        }
      });
    }

    const nextBtn = navBar.querySelector('.btn-next-ayat');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (state.currentAyatIndex < totalCount - 1) {
          state.currentAyatIndex++;
          stopAllAudio();
          renderAyatReferences(group, state.searchQuery);
        }
      });
    }

    // Assemble and mount
    singleScreenWrap.appendChild(navBar);
    singleScreenWrap.appendChild(cardWrapper);
    elements.ayatGridContainer.appendChild(singleScreenWrap);
  }

  // Select Bentuk Kata
  function selectBentuk(bentuk) {
    state.selectedBentuk = bentuk;
    if (elements.bentukKataSelect) {
      elements.bentukKataSelect.value = bentuk || '';
    }
    
    populateNoKataDropdown();

    const activeList = noKatasByBentuk[bentuk] || [];
    if (activeList.length > 0) {
      selectNoKata(activeList[0]);
    } else {
      selectNoKata('');
    }
  }

  // Select No Kata
  function selectNoKata(noKata) {
    state.selectedNoKata = noKata;
    if (elements.noKataSelect) {
      elements.noKataSelect.value = noKata || '';
    }
    state.searchQuery = '';
    if (elements.ayatSearchInput) elements.ayatSearchInput.value = '';

    stopAllAudio();
    updateSpotlightCard();
    renderAyatReferences();
  }

  // Apply Language Change across entire app
  function applyLanguage(lang) {
    state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn', 'ru', 'zh', 'es', 'tr', 'pt', 'ha', 'sw', 'fa'].includes(lang) ? lang : 'id';
    localStorage.setItem('dhamir_lang', state.lang);

    if (elements.langSelect) {
      elements.langSelect.value = state.lang;
    }

    // Set HTML lang and dir attribute
    document.documentElement.lang = state.lang;
    if (state.lang === 'ur' || state.lang === 'fa') {
      document.documentElement.setAttribute('dir', 'rtl');
    } else {
      document.documentElement.removeAttribute('dir');
    }

    // Update document & brand titles
    updateHeaderTitles();

    // Update Static UI Labels
    if (elements.labelLangSelect) elements.labelLangSelect.textContent = t('labelLangSelect');
    if (elements.translationSourceText) elements.translationSourceText.innerHTML = t('translationSourceHtml');
    if (elements.themeToggleBtn) elements.themeToggleBtn.setAttribute('title', t('themeToggleTitle'));

    if (elements.labelTabJamid) elements.labelTabJamid.textContent = t('brandTitle').replace(/<[^>]*>/g, '');
    if (elements.badgeTabJamid) elements.badgeTabJamid.textContent = '7 Bentuk Kata';
    if (elements.badgeTabHarf) elements.badgeTabHarf.textContent = '17 Bentuk Harf';

    // Spotlight buttons
    if (elements.labelAudioArab) elements.labelAudioArab.textContent = t('arabicVoiceBtn');
    if (elements.btnAudioPlay) elements.btnAudioPlay.setAttribute('title', t('arabicVoiceTooltip'));

    if (elements.labelAudioMeaning) elements.labelAudioMeaning.textContent = t('meaningVoiceBtn');
    if (elements.btnAudioMeaning) elements.btnAudioMeaning.setAttribute('title', t('meaningVoiceTooltip'));

    if (elements.btnCopyArabic) elements.btnCopyArabic.setAttribute('title', t('copyArabicTooltip'));
    if (elements.btnCopyAll) elements.btnCopyAll.setAttribute('title', t('copyInfoTooltip'));

    if (elements.labelExportCsv) elements.labelExportCsv.textContent = t('exportCsvBtn');
    if (elements.btnExportCsv) elements.btnExportCsv.setAttribute('title', t('exportCsvTooltip'));

    if (elements.ayatSearchInput) {
      elements.ayatSearchInput.setAttribute('placeholder', t('searchPlaceholder'));
    }

    // Re-populate dropdowns and re-render cards
    populateBentukDropdown();
    populateNoKataDropdown();
    updateSpotlightCard();
    renderAyatReferences();
  }

  // Apply Theme ('dark' | 'light')
  function applyTheme(theme) {
    state.theme = theme;
    localStorage.setItem('dhamir_theme', theme);
    document.documentElement.setAttribute('data-theme', theme);

    if (elements.themeIcon) {
      if (theme === 'light') {
        elements.themeIcon.innerHTML = `
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
          </svg>`;
      } else {
        elements.themeIcon.innerHTML = `
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="5"></circle>
            <line x1="12" y1="1" x2="12" y2="3"></line>
            <line x1="12" y1="21" x2="12" y2="23"></line>
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
            <line x1="1" y1="12" x2="3" y2="12"></line>
            <line x1="21" y1="12" x2="23" y2="12"></line>
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
          </svg>`;
      }
    }
  }

  // Toast Notification System
  let toastTimer = null;
  function showToast(msg) {
    if (!elements.toastNotification) return;
    elements.toastNotification.textContent = msg;
    elements.toastNotification.classList.add('show');

    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      elements.toastNotification.classList.remove('show');
    }, 3500);
  }

  // AI Prompt Builder with Clean Multilingual Dispatch
  function buildAiPrompt(topic, surat, ayat, kata, noKata, bentuk, teksArab, teksArti, grammarDesc) {
    const suratNama = currentAiContext.suratNama;

    switch (state.lang) {
      case 'fa':
        if (topic === 'nahwu') {
          return `لطفاً نکات صرفی، نحوی (قواعد زبان عربی) و اعراب کلمه «${kata}» (${noKata}, ${bentuk}) در سوره ${suratNama} (${surat})، آیه ${ayat} را به طور جامع تحلیل فرمایید:\\n\\nمتن عربی آیه: «${teksArab}»\\nترجمه فارسی آیه: «${teksArti}»\\n\\nلطفاً موارد زیر را بررسی نمایید:\\n۱. نقش نحوی، محل اعراب و کارکرد «${kata}» در این جمله (مرفوع / منصوب / مجرور).\\n۲. نوع کلمه (ضمیر / موصول / ادوات شرط و غیره) و ویژگی‌های ساختاری آن (منفصل / متصل).\\n۳. توضیحات تکمیلی نحوی: ${grammarDesc || "بر اساس قواعد بلاغی و ادبی قرآن کریم"}.`;
        } else if (topic === 'tafsir') {
          return `لطفاً تفسیر و شرحی پرمحتوا و مختصر درباره سوره ${suratNama} (${surat})، آیه ${ayat} ارائه فرمایید:\\n\\nمتن عربی آیه: «${teksArab}»\\nترجمه فارسی آیه: «${teksArti}»\\n\\nبا تمرکز بر مفهوم و کارکرد کلمه «${kata}»: چه حکمت، شأن نزول (در صورت وجود) و پیام‌های هدایت‌بخشی در این آیه برای زندگی مؤمنان نهفته است؟`;
        } else {
          return `لطفاً زیبایی‌های بلاغی و اعجاز ادبی قرآن کریم (فصاحت، ایجاز و صنایع ادبی) در خصوص انتخاب کلمه «${kata}» در سوره ${suratNama} (${surat})، آیه ${ayat} را تبیین فرمایید:\\n\\nمتن عربی آیه: «${teksArab}»\\nترجمه فارسی آیه: «${teksArti}»\\n\\nچرا این واژه یا ضمیر در این بافت خاص به کار رفته و چه عمق معنایی و ظرافتی به آیه بخشیده است؟`;
        }

      case 'sw':
        if (topic === 'nahwu') {
          return `Tafadhali fafanua kanuni za nahau (Nahwu/Sarf) na I'rabu kuhusu neno "${kata}" (${noKata}, ${bentuk}) katika Sura ${suratNama} (${surat}), Aya ${ayat}:\\n\\nMaandishi ya Kiarabu: "${teksArab}"\\nTafsiri ya Kiswahili: "${teksArti}"\\n\\nTafadhali chambua vipengele vifuatavyo:\\n1. Nafasi ya i'rabu na kazi ya "${kata}" katika sentensi hii (Marfu' / Manshub / Majrur).\\n2. Aina ya neno (Dhamir / Mawshul / nk.) na sifa zake (Munfashil / Muttashil).\\n3. Maelezo ya ziada ya kisarufi: ${grammarDesc || "Kulingana na kanuni za lugha ya Qur'ani"}.`;
        } else if (topic === 'tafsir') {
          return `Tafadhali toa muhtasari wa tafsiri yenye manufaa kuhusu Sura ${suratNama} (${surat}), Aya ${ayat}:\\n\\nMaandishi ya Kiarabu: "${teksArab}"\\nTafsiri ya Kiswahili: "${teksArti}"\\n\\nUkiwa na msisitizo maalum juu ya neno "${kata}": Je, kuna hekima gani, sababu ya kuteremka aya (asbabun nuzul ikiwa ipo), na mafunzo gani ambayo aya hii inatoa kwa maisha ya waumini?`;
        } else {
          return `Tafadhali fafanua uzuri wa lugha na balagha ya Qur'ani (I'jaz na ufasaha wa maneno) kuhusiana na uteuzi wa neno "${kata}" katika Sura ${suratNama} (${surat}), Aya ${ayat}:\\n\\nMaandishi ya Kiarabu: "${teksArab}"\\nTafsiri ya Kiswahili: "${teksArti}"\\n\\nKwa nini neno hili au kiwakilishi hiki kilitumika hapa? Je, kinaongeza kina gani cha maana na uzuri wa usemi katika muktadha wa aya hii?`;
        }

      case 'ha':
        if (topic === 'nahwu') {
          return `Da fatan za a yi cikakken bayanin ƙa'idojin nahawu (Nahwu/Sarf) da I'rabi game da kalmar "${kata}" (${noKata}, ${bentuk}) a cikin Surah ${suratNama} (${surat}), Aya ${ayat}:\\n\\nNassin Larabci: "${teksArab}"\\nFassarar Hausa: "${teksArti}"\\n\\nDa fatan a duba waɗannan abubuwan:\\n1. Matsayin i'rabi da aikin "${kata}" a cikin wannan jumla (Marfu' / Manshub / Majrur).\\n2. Nau'in kalmar (Dhamir / Mawshul / da sauransu) da siffofinta (Munfashil / Muttashil).\\n3. Ƙarin bayanin nahawu: ${grammarDesc || "Bisa ƙa'idar yaren Al-Ƙur'ani"}.`;
        } else if (topic === 'tafsir') {
          return `Da fatan a bayar da taƙaitaccen tafsiri mai fa'ida game da Surah ${suratNama} (${surat}), Aya ${ayat}:\\n\\nNassin Larabci: "${teksArab}"\\nFassarar Hausa: "${teksArti}"\\n\\nTare da mai da hankali kan ma'anar kalmar "${kata}": Wace hikima, asalin saukar aya (asbabun nuzul idan akwai), da koyarwar da wannan aya ke isarwa ga rayuwar muminai?`;
        } else {
          return `Da fatan a bayyana balagar Al-Ƙur'ani (I'jaz da adon magana) dangane da zaɓin kalmar "${kata}" a cikin Surah ${suratNama} (${surat}), Aya ${ayat}:\\n\\nNassin Larabci: "${teksArab}"\\nFassarar Hausa: "${teksArti}"\\n\\nMe ya sa aka yi amfani da wannan kalma ko damiri a nan? Wane zurfin ma'ana da kyawon lafazi take ƙarawa ga ayar?`;
        }

      case 'pt':
        if (topic === 'nahwu') {
          return `Por favor, faça uma análise gramatical árabe detalhada (Nahwu/Sarf) e I'rab sobre a palavra "${kata}" (${noKata}, ${bentuk}) na Surata ${suratNama} (${surat}), Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTradução em Português: "${teksArti}"\\n\\nPor favor, aborde os seguintes pontos:\\n1. Posição sintática (I'rab) e função de "${kata}" na oração (Marfu'/Manshub/Majrur).\\n2. Classificação morfológica (Dhamir / Mawshul / etc.) e propriedades (Munfashil / Muttashil).\\n3. Explicações gramaticais adicionais: ${grammarDesc || "De acordo com as regras gramaticais clássicas do Alcorão"}.`;
        } else if (topic === 'tafsir') {
          return `Por favor, forneça uma explicação contextual e Tafsir conciso sobre a Surata ${suratNama} (${surat}), Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTradução em Português: "${teksArti}"\\n\\nCom foco no significado da palavra "${kata}": Qual é a sabedoria, o contexto da revelação (asbab an-nuzul, se aplicável) e as lições práticas que este versículo transmite?`;
        } else {
          return `Por favor, elucide os aspectos de Balaghah (eloquência e recursos estilísticos corânicos) relacionados à escolha da palavra "${kata}" na Surata ${suratNama} (${surat}), Versículo ${ayat}:\\n\\nTexto Árabe: "${teksArab}"\\nTradução em Português: "${teksArti}"\\n\\nPor que esse termo ou pronome específico foi empregado aqui e que profundidade de significado ele confere ao versículo?`;
        }

      case 'en':
        if (topic === 'nahwu') {
          return `Please provide a detailed Arabic grammatical (Nahwu/Sarf) and I'rab analysis for the word "${kata}" (${noKata}, ${bentuk}) in Surah ${suratNama} (${surat}), Ayah ${ayat}:\\n\\nArabic Text: "${teksArab}"\\nEnglish Translation: "${teksArti}"\\n\\nPlease cover:\\n1. The grammatical role (I'rab position) of "${kata}" in this sentence (Marfu'/Manshub/Majrur).\\n2. Morphological type (Dhamir / Mawshul / etc.) and attributes (Munfashil / Muttashil).\\n3. Grammar notes: ${grammarDesc || "Based on Classical Quranic Arabic rules"}.`;
        } else if (topic === 'tafsir') {
          return `Please provide a concise and insightful Tafsir explanation for Surah ${suratNama} (${surat}), Ayah ${ayat}:\\n\\nArabic Text: "${teksArab}"\\nEnglish Translation: "${teksArti}"\\n\\nFocusing on the word "${kata}": What is the wisdom, context of revelation (asbab an-nuzul if any), and lessons conveyed for believers?`;
        } else {
          return `Please explain the Balaghah (eloquence, rhetorical beauty, and stylistic precision) regarding the choice of the word "${kata}" in Surah ${suratNama} (${surat}), Ayah ${ayat}:\\n\\nArabic Text: "${teksArab}"\\nEnglish Translation: "${teksArti}"\\n\\nWhy was this specific pronoun/word used in this context, and what subtle depth does it add to the Ayah?`;
        }

      default:
        // Indonesian (Default)
        if (topic === 'nahwu') {
          return `Tolong jelaskan analisis kaidah tata bahasa Arab (Nahwu/Shorof) dan I'rob secara mendalam mengenai kata "${kata}" (${noKata}, ${bentuk}) pada Surat ${suratNama} (${surat}) Ayat ${ayat}:\\n\\nTeks Arab: "${teksArab}"\\nTerjemahan: "${teksArti}"\\n\\nMohon sertakan:\\n1. Kedudukan i'rob kata "${kata}" dalam kalimat tersebut (Marfu'/Manshub/Majrur).\\n2. Jenis kata (Dhamir / Mawshul / dsb) dan statusnya (Munfashil / Muttashil).\\n3. Penjelasan kaidah: ${grammarDesc || "Sesuai kaidah bahasa Al-Qur'an"}.`;
        } else if (topic === 'tafsir') {
          return `Tolong berikan penjelasan tafsir ringkas dan kontekstual mengenai Surat ${suratNama} (${surat}) Ayat ${ayat}:\\n\\nTeks Arab: "${teksArab}"\\nTerjemahan: "${teksArti}"\\n\\nFokus pada kata "${kata}": Apa hikmah, asbabun nuzul (jika ada), dan pelajaran utama yang dapat diambil oleh seorang muslim dari ayat ini?`;
        } else {
          return `Tolong jelaskan keindahan balaghah (sastra dan uslub Al-Qur'an) terkait pemilihan kata "${kata}" pada Surat ${suratNama} (${surat}) Ayat ${ayat}:\\n\\nTeks Arab: "${teksArab}"\\nTerjemahan: "${teksArti}"\\n\\nMengapa kata/dhamir ini yang digunakan pada konteks ayat tersebut dan apa rahasia keindahan maknanya?`;
        }
    }
  }

  // Open AI Modal
  function openAiModal(surat, ayat, kata, noKata, bentuk) {
    const group = getGroup(state.selectedBentuk, state.selectedNoKata);
    const occ = group ? group.occurrences.find(o => o.surat === surat && o.ayat === ayat) : null;

    currentAiContext.surat = surat;
    currentAiContext.ayat = ayat;
    currentAiContext.kata = kata;
    currentAiContext.noKata = noKata;
    currentAiContext.bentuk = bentuk;
    currentAiContext.suratNama = occ ? occ.suratNama : `Surat ${surat}`;
    currentAiContext.teksArab = occ ? occ.teksArab : '';
    currentAiContext.teksArti = occ ? getOccTeksArti(occ, state.lang) : '';
    currentAiContext.grammarDesc = group ? getGroupDesc(group, state.lang) : '';
    currentAiContext.topic = 'nahwu';

    if (elements.aiModalTitle) elements.aiModalTitle.textContent = t('aiModalTitle');
    if (elements.aiModalSubtitle) elements.aiModalSubtitle.textContent = t('aiModalSubtitle', currentAiContext.suratNama, ayat, kata, noKata);
    if (elements.labelAiTopic) elements.labelAiTopic.textContent = t('aiTopicLabel');
    if (elements.labelPromptPreview) elements.labelPromptPreview.textContent = t('aiPromptPreviewLabel');
    if (elements.labelOpenGemini) elements.labelOpenGemini.textContent = t('aiOpenGemini');
    if (elements.labelOpenChatGpt) elements.labelOpenChatGpt.textContent = t('aiOpenChatGpt');
    if (elements.labelCopyPrompt) elements.labelCopyPrompt.textContent = t('aiCopyPrompt');

    if (elements.aiModalArabicVerse) elements.aiModalArabicVerse.textContent = currentAiContext.teksArab;
    if (elements.aiModalTranslation) elements.aiModalTranslation.textContent = currentAiContext.teksArti;

    const topicChips = elements.aiTopicChips ? elements.aiTopicChips.querySelectorAll('.ai-topic-chip') : [];
    topicChips.forEach(chip => {
      chip.classList.remove('active');
      const topicType = chip.getAttribute('data-topic');
      if (topicType === 'nahwu') chip.textContent = t('aiTopicNahwu');
      if (topicType === 'tafsir') chip.textContent = t('aiTopicTafsir');
      if (topicType === 'balaghah') chip.textContent = t('aiTopicBalaghah');
      if (topicType === 'nahwu') chip.classList.add('active');
    });

    updateAiModalPrompt();

    if (elements.aiModal) {
      elements.aiModal.classList.add('open');
      elements.aiModal.setAttribute('aria-hidden', 'false');
    }
  }

  // Close AI Modal
  function closeAiModal() {
    if (elements.aiModal) {
      elements.aiModal.classList.remove('open');
      elements.aiModal.setAttribute('aria-hidden', 'true');
    }
  }

  // Update AI Modal Prompt Preview
  function updateAiModalPrompt() {
    if (!elements.aiPromptTextarea) return;
    const prompt = buildAiPrompt(
      currentAiContext.topic,
      currentAiContext.surat,
      currentAiContext.ayat,
      currentAiContext.kata,
      currentAiContext.noKata,
      currentAiContext.bentuk,
      currentAiContext.teksArab,
      currentAiContext.teksArti,
      currentAiContext.grammarDesc
    );
    elements.aiPromptTextarea.value = prompt;
  }

  function openInGemini() {
    if (!elements.aiPromptTextarea) return;
    const prompt = elements.aiPromptTextarea.value;
    const url = `https://gemini.google.com/app?prompt=${encodeURIComponent(prompt)}`;
    window.open(url, '_blank');
  }

  function openInChatGpt() {
    if (!elements.aiPromptTextarea) return;
    const prompt = elements.aiPromptTextarea.value;
    const url = `https://chatgpt.com/?q=${encodeURIComponent(prompt)}`;
    window.open(url, '_blank');
  }

  function copyAiPrompt() {
    if (!elements.aiPromptTextarea) return;
    const prompt = elements.aiPromptTextarea.value;
    navigator.clipboard.writeText(prompt).then(() => {
      showToast(t('toastPromptCopied'));
    }).catch(() => {
      showToast('Gagal menyalin prompt.');
    });
  }

  // Export to CSV
  function exportToCsv() {
    const group = getGroup(state.selectedBentuk, state.selectedNoKata);
    if (!group || !group.occurrences || group.occurrences.length === 0) {
      showToast('Tidak ada data untuk diekspor.');
      return;
    }

    const headers = [
      'Surat', 'Nama Surat', 'Ayat', 'Kata Arab', 'No Kata', 'Bentuk Kata',
      'Arti (ID)', 'Arti (EN)', 'Arti (MS)', 'Arti (FR)', 'Arti (DE)',
      'Arti (UR)', 'Arti (HI)', 'Arti (BN)', 'Arti (RU)', 'Arti (ZH)',
      'Arti (ES)', 'Arti (TR)', 'Arti (PT)', 'Arti (HA)', 'Arti (SW)', 'Arti (FA)',
      'Frekuensi', 'Teks Arab', 'Teks Latin',
      'Terjemahan (ID)', 'Terjemahan (EN)', 'Terjemahan (MS)', 'Terjemahan (FR)', 'Terjemahan (DE)',
      'Terjemahan (UR)', 'Terjemahan (HI)', 'Terjemahan (BN)', 'Terjemahan (RU)', 'Terjemahan (ZH)',
      'Terjemahan (ES)', 'Terjemahan (TR)', 'Terjemahan (PT)', 'Terjemahan (HA)', 'Terjemahan (SW)', 'Terjemahan (FA)'
    ];

    const rows = group.occurrences.map(occ => {
      const cleanField = str => `"${(str || '').replace(/"/g, '""')}"`;
      return [
        occ.surat,
        cleanField(occ.suratNama),
        occ.ayat,
        cleanField(group.kata),
        cleanField(group.noKata),
        cleanField(group.bentuk),
        cleanField(group.arti_id),
        cleanField(group.arti_en),
        cleanField(group.arti_ms),
        cleanField(group.arti_fr),
        cleanField(group.arti_de),
        cleanField(group.arti_ur),
        cleanField(group.arti_hi),
        cleanField(group.arti_bn),
        cleanField(group.arti_ru),
        cleanField(group.arti_zh),
        cleanField(group.arti_es),
        cleanField(group.arti_tr),
        cleanField(group.arti_pt),
        cleanField(group.arti_ha),
        cleanField(group.arti_sw),
        cleanField(group.arti_fa),
        cleanField(group.frek ? `${group.frek}x` : 'Muttashil'),
        cleanField(occ.teksArab),
        cleanField(occ.teksLatin),
        cleanField(occ.teksArtiID),
        cleanField(occ.teksArtiEN),
        cleanField(occ.teksArtiMS),
        cleanField(occ.teksArtiFR),
        cleanField(occ.teksArtiDE),
        cleanField(occ.teksArtiUR),
        cleanField(occ.teksArtiHI),
        cleanField(occ.teksArtiBN),
        cleanField(occ.teksArtiRU),
        cleanField(occ.teksArtiZH),
        cleanField(occ.teksArtiES),
        cleanField(occ.teksArtiTR),
        cleanField(occ.teksArtiPT),
        cleanField(occ.teksArtiHA),
        cleanField(occ.teksArtiSW),
        cleanField(occ.teksArtiFA)
      ].join(',');
    });

    const csvContent = '\\uFEFF' + headers.join(',') + '\\n' + rows.join('\\n');
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.setAttribute('href', url);
    link.setAttribute('download', `Dhamir_${group.noKata}_${group.kata}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    showToast(t('toastCsvExported', group.noKata));
  }

  // Setup Event Listeners
  function setupEventListeners() {
    // Dropdown 1: Bentuk Kata
    if (elements.bentukKataSelect) {
      elements.bentukKataSelect.addEventListener('change', (e) => {
        selectBentuk(e.target.value);
      });
    }

    // Dropdown 2: No Kata
    if (elements.noKataSelect) {
      elements.noKataSelect.addEventListener('change', (e) => {
        selectNoKata(e.target.value);
      });
    }

    // Language Selector
    if (elements.langSelect) {
      elements.langSelect.addEventListener('change', (e) => {
        applyLanguage(e.target.value);
        showToast(t('toastLangChanged'));
      });
    }

    // Search Input in References
    if (elements.ayatSearchInput) {
      elements.ayatSearchInput.addEventListener('input', (e) => {
        state.searchQuery = e.target.value;
        renderAyatReferences();
      });
    }

    // Copy Arabic Word Button
    if (elements.btnCopyArabic) {
      elements.btnCopyArabic.addEventListener('click', () => {
        const group = getGroup(state.selectedBentuk, state.selectedNoKata);
        if (!group) return;
        navigator.clipboard.writeText(group.kata).then(() => {
          showToast(t('toastArabicCopied', group.kata));
        }).catch(() => {
          showToast('Gagal menyalin kata Arab.');
        });
      });
    }

    // Copy Summary Info Button
    if (elements.btnCopyAll) {
      elements.btnCopyAll.addEventListener('click', () => {
        const group = getGroup(state.selectedBentuk, state.selectedNoKata);
        if (!group) return;

        const activeArti = getGroupArti(group, state.lang);
        const activeDesc = getGroupDesc(group, state.lang);

        let titlePrefix = "Kamus Al-Qur'an";
        if (group.bentuk.includes('Mawshul')) {
          titlePrefix = "Isim Mawshul Al-Qur'an";
        } else if (group.bentuk.includes('Dhamir')) {
          titlePrefix = "Dhamir Al-Qur'an";
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

    // Dictionary Tab Switcher
    if (elements.tabDictJamid) {
      elements.tabDictJamid.addEventListener('click', () => {
        switchDictionary('jamid');
      });
    }
    if (elements.tabDictHarf) {
      elements.tabDictHarf.addEventListener('click', () => {
        switchDictionary('harf');
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
        const chip = e.target.closest('.ai-topic-chip');
        if (!chip) return;
        elements.aiTopicChips.querySelectorAll('.ai-topic-chip').forEach(c => c.classList.remove('active'));
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
    applyTheme(state.theme);
    setupEventListeners();
    switchDictionary(state.activeDict);
    applyLanguage(state.lang);
  }

  // Run on DOM Content Loaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
"""

with open(os.path.join(BASE_DIR, 'app.js'), 'w', encoding='utf-8') as f:
    f.write(app_js_content)

print(f"app.js successfully built with perfect element mappings! Total lines: {len(app_js_content.splitlines())}")
