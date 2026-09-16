# -*- coding: utf-8 -*-
"""
Updater script to add Bangla (bn) language support to app.js
"""
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app_js_path = os.path.join(BASE_DIR, 'app.js')

with open(app_js_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. State lang comment
code = code.replace(
    "lang: localStorage.getItem('dhamir_lang') || 'id', // 'id' | 'en' | 'ms' | 'fr' | 'de' | 'ur' | 'hi'",
    "lang: localStorage.getItem('dhamir_lang') || 'id', // 'id' | 'en' | 'ms' | 'fr' | 'de' | 'ur' | 'hi' | 'bn'"
)

# 2. Add 'bn' to I18N
bn_i18n = """    bn: {
      pageTitle: "জামেদ মাবনি অভিধান | ইন্টারেক্টিভ কুরআনিক শব্দ ও আয়াত রেফারেন্স",
      brandTitle: "জামেদ মাবনি <span>অভিধান</span>",
      brandSubtitle: "শব্দরূপ ও শব্দ নম্বরের ইন্টারেক্টিভ অভিধান",
      themeToggleTitle: "ডার্ক / লাইট থিম পরিবর্তন করুন",
      labelLangSelect: "অনুবাদ ও ভয়েস ভাষা:",
      translationSourceHtml: "অনুবাদ: <strong>মাওলানা মুহিউদ্দীন খান (Muhiuddin Khan)</strong>",
      
      // Control Card
      step1Label: "১. শব্দের রূপ নির্বাচন করুন",
      step1Placeholder: "শব্দের রূপ নির্বাচন করুন",
      step1OptionDhamir: "১. সর্বনাম (Dhamir - Pronouns)",
      step1OptionMawshul: "২. সম্বন্ধবাচক সর্বনাম (Mawshul - Relative Pronouns)",
      step1OptionIstifham: "৩. প্রশ্নবোধক শব্দ (Istifham - Interrogatives)",
      step1OptionSyarath: "৪. শর্তমূলক শব্দ (Syarath - Conditionals)",
      step1OptionIsyarah: "৫. নির্দেশক সর্বনাম (Isyarah - Demonstratives)",
      step1OptionIsimFiil: "৬. ক্রিয়াভিত্তিক বিশেষ্য (Isim Fi'il - Verbal Nouns)",
      step1OptionFiilJamid: "৭. অপরিবর্তনীয় ক্রিয়া (Fi'il Jamid - Inflexible Verbs)",
      step2Label: "২. শব্দ নম্বর নির্বাচন করুন",
      step2Placeholder: "শব্দ নম্বর নির্বাচন করুন",
      welcomeTitle: "অনুগ্রহ করে শব্দের রূপ ও নম্বর নির্বাচন করুন",
      welcomeSubtitle: "আরবি শব্দ, অর্থ, কুরআনে পুনরাবৃত্তি (ফ্রিকোয়েন্সি) ও আয়াত রেফারেন্স দেখতে উপরের মেনু থেকে শব্দরূপ নির্বাচন করুন।",
      
      // Spotlight Card
      wordFormBadge: "শব্দরূপ",
      wordNoBadgePrefix: "শব্দ নং:",
      arabicVoiceBtn: "আরবি ভয়েস",
      arabicVoiceTooltip: "আরবি উচ্চারণ শুনুন (TTS)",
      meaningVoiceBtn: "অর্থের ভয়েস",
      meaningVoiceTooltip: "বাংলা অর্থ / অনুবাদ শুনুন (বাংলা TTS)",
      copyArabicTooltip: "আরবি শব্দ কপি করুন",
      copyInfoBtn: "তথ্য কপি করুন",
      copyInfoTooltip: "সম্পূর্ণ সারাংশ কপি করুন",
      freqLabel: "পবিত্র কুরআনে পুনরাবৃত্তি (ফ্রিকোয়েন্সি)",
      freqSub: "উপস্থিতির সংখ্যা",
      freqMuttashilVal: "সংযুক্ত (Muttashil)",
      freqMuttashilSub: "সংযুক্ত রূপ (প্রত্যয় / Affix)",
      totalAyatLabel: "মোট রেফারেন্স আয়াত",
      totalAyatSub: "ডেটাবেজে উপলব্ধ",
      sampleAyatSuffix: "উদাহরণ আয়াত",
      transliterationPrefix: "উচ্চারণ (Transliteration):",
      meaningPrefix: "অর্থ:",
      
      // References Section
      referencesTitlePrefix: "কুরআনিক রেফারেন্স আয়াতসমূহ:",
      ayatCountBadgePattern: (cur, total) => `আয়াত ${cur} / ${total}`,
      ayatCountZero: "০ আয়াত",
      searchPlaceholder: "সূরার নাম / আয়াত নম্বর খুঁজুন...",
      exportCsvBtn: "CSV ডাউনলোড",
      exportCsvTooltip: "এই শব্দের সকল রেফারেন্স আয়াত CSV ফাইলে ডাউনলোড করুন",
      
      // Ayat Card
      surahPrefix: "সূরা",
      surahPositionTag: (cur, surahNo, ayatNo) => `সূরা #${surahNo} • আয়াত #${ayatNo}`,
      playTranslationBtn: "অনুবাদ শুনুন",
      stopTranslationBtn: "ভয়েস বন্ধ করুন",
      playTilawahBtn: "তিলাওয়াত শুনুন",
      pauseTilawahBtn: "তিলাওয়াত থামান",
      askAiBtn: "AI জিজ্ঞাসা করুন",
      askAiTooltip: "এই আয়াতের ব্যাকরণ ও তাফসির সম্পর্কে AI কে জিজ্ঞাসা করুন",
      aiModalTitle: "কুরআনিক AI সহকারী",
      aiModalSubtitle: (suratNama, ayat, kata, noKata) => `পর্যালোচনা: সূরা ${suratNama}:${ayat} • শব্দ "${kata}" (${noKata})`,
      aiTopicLabel: "AI বিশ্লেষণের বিষয় নির্বাচন করুন:",
      aiPromptPreviewLabel: "প্রস্তুতকৃত AI প্রম্পট:",
      aiTopicNahwu: "🔍 নাহব (ব্যাকরণ) ও ই'রাব",
      aiTopicTafsir: "📖 তাফসির ও আয়াতের মর্মার্থ",
      aiTopicBalaghah: "✨ অলঙ্কারশাস্ত্র (বালাগাত)",
      aiOpenGemini: "Google Gemini",
      aiOpenChatGpt: "ChatGPT",
      aiCopyPrompt: "প্রম্পট কপি করুন",
      toastPromptCopied: "AI প্রম্পট ক্লিপবোর্ডে কপি হয়েছে!",
      ayahPill: (n) => `আয়াত ${n}`,
      flipToArabicBtn: "আরবি পাঠ দেখুন",
      flipToTranslationBtn: "অনুবাদ দেখুন",
      translationBoxHeader: "আয়াতের অর্থ / অনুবাদ (বাংলা - মাওলানা মুহিউদ্দীন খান)",
      latinBoxHeader: "রোমান উচ্চারণ (TRANSLITERATION)",
      copyLatinBtn: "উচ্চারণ কপি করুন",
      arabicBoxHeader: "النص القرآني • সম্পূর্ণ আরবি আয়াত",
      latinBackHeader: "রোমান উচ্চারণ:",
      copyBtn: "কপি করুন",
      prevBtn: "পূর্ববর্তী",
      nextBtn: "পরবর্তী",
      emptyStateText: "আপনার অনুসন্ধানের সাথে মিলে এমন কোনো সূরা বা আয়াত পাওয়া যায়নি।",
      
      // Toasts & Speech
      toastLangChanged: "ভাষা সফলভাবে বাংলায় পরিবর্তিত হয়েছে 🇧🇩",
      toastTilawahPaused: "তিলাওয়াত স্থগিত করা হয়েছে।",
      toastTilawahPlaying: (s, a) => `সূরা ${s}:${a}-এর তিলাওয়াত চলছে (মিশারী রাশিদ আল-আফাসী)`,
      toastTilawahEnded: "তিলাওয়াত সমাপ্ত হয়েছে।",
      toastAudioFailed: "অডিও লোড করতে ব্যর্থ হয়েছে। ইন্টারনেট সংযোগ পরীক্ষা করুন।",
      toastTranslationStopped: "অনুবাদ ভয়েস বন্ধ করা হয়েছে।",
      toastTtsNotSupported: "আপনার ব্রাউজারে টেক্সট-টু-স্পিচ সমর্থিত নয়।",
      toastTranslationNotAvail: "অনুবাদ পাঠ্য উপলব্ধ নেই।",
      toastSpeakingMeaning: (suratNama, ayat) => `সূরা ${suratNama}:${ayat}-এর বাংলা অনুবাদ শোনানো হচ্ছে`,
      toastSpeakingArabic: (word) => `আরবি উচ্চারণ: ${word}`,
      toastSpeakingWordMeaning: (arti) => `অর্থ শোনানো হচ্ছে: ${arti}`,
      toastSpeakingLatin: (suratNama, ayat) => `সূরা ${suratNama}:${ayat}-এর রোমান উচ্চারণ শোনানো হচ্ছে`,
      toastArabicCopied: (word) => `আরবি শব্দ "${word}" কপি করা হয়েছে!`,
      toastLatinCopied: "রোমান উচ্চারণ কপি করা হয়েছে!",
      toastSummaryCopied: "সারাংশ সফলভাবে কপি করা হয়েছে!",
      toastCsvExported: (nk) => `শব্দ ${nk}-এর ডেটা সফলভাবে CSV-তে এক্সপোর্ট করা হয়েছে!`,
      
      // TTS Speech Format
      ttsMeaningSpeech: (group) => {
        const cleanWord = group.kata.replace(/\\.\\./g, '').replace(/\\s*\\d+$/, '');
        const latin = group.latin ? `${group.latin}, ` : '';
        const arti = group.arti_bn || group.arti_id || group.arti;
        const desc = (group.grammar && (group.grammar.desc_bn || group.grammar.desc_id || group.grammar.keterangan)) || '';
        const prefix = group.bentuk && group.bentuk.includes('Mawshul') ? 'সম্বন্ধবাচক সর্বনাম' : 'সর্বনাম';
        return `${prefix} ${cleanWord}, ${latin}অর্থ ${arti}। ${desc ? 'বিবরণ: ' + desc : ''}`;
      },
      ttsVerseSpeech: (suratNama, ayat, text) => text
    }"""

# Insert 'bn' at the end of I18N
# Find hi object end or last object end before "};" of I18N
hi_anchor = """      ttsVerseSpeech: (suratNama, ayat, text) => text
    }
  };"""

code = code.replace(hi_anchor, """      ttsVerseSpeech: (suratNama, ayat, text) => text
    },
""" + bn_i18n + """
  };""")

# 3. groupedData construction
old_group_data = """          bentuk_hi: item['BentukKataHI'] || (b === '1. Dhamir' ? '१. सर्वनाम (Dhamir)' : (b === '2. Mawshul' ? '२. संबंधवाचक सर्वनाम (Mawshul)' : b)),
          noKata: nk,"""
new_group_data = """          bentuk_hi: item['BentukKataHI'] || (b === '1. Dhamir' ? '१. सर्वनाम (Dhamir)' : (b === '2. Mawshul' ? '२. संबंधवाचक सर्वनाम (Mawshul)' : b)),
          bentuk_bn: item['BentukKataBN'] || (b === '1. Dhamir' ? '১. সর্বনাম (Dhamir)' : (b === '2. Mawshul' ? '২. সম্বন্ধবাচক সর্বনাম (Mawshul)' : b)),
          noKata: nk,"""
code = code.replace(old_group_data, new_group_data)

old_arti_hi = """          arti_hi: item['ArtiKataHI'] || grammar.arti_hi || item['ArtiKataID'] || item['Arti kata'],
          frek: item['Frek kata'],"""
new_arti_hi = """          arti_hi: item['ArtiKataHI'] || grammar.arti_hi || item['ArtiKataID'] || item['Arti kata'],
          arti_bn: item['ArtiKataBN'] || grammar.arti_bn || item['ArtiKataID'] || item['Arti kata'],
          frek: item['Frek kata'],"""
code = code.replace(old_arti_hi, new_arti_hi)

old_surat_arti = """        suratArtiHI: item['SuratArtiHI'] || item['SuratArti'] || '',
        teksArab: item['TeksArab'] || '',"""
new_surat_arti = """        suratArtiHI: item['SuratArtiHI'] || item['SuratArti'] || '',
        suratArtiBN: item['SuratArtiBN'] || item['SuratArti'] || '',
        teksArab: item['TeksArab'] || '',"""
code = code.replace(old_surat_arti, new_surat_arti)

old_teks_arti = """        teksArtiHI: item['TeksArtiHI'] || item['TeksArtiID'] || item['TeksArti'] || '',
        audioUrl: item['AudioUrl']"""
new_teks_arti = """        teksArtiHI: item['TeksArtiHI'] || item['TeksArtiID'] || item['TeksArti'] || '',
        teksArtiBN: item['TeksArtiBN'] || item['TeksArtiID'] || item['TeksArti'] || '',
        audioUrl: item['AudioUrl']"""
code = code.replace(old_teks_arti, new_teks_arti)

# 4. populateNoKataDropdown
old_no_kata = """      } else if (state.lang === 'hi') {
        localizedArti = group.arti_hi || group.arti_id || group.arti;
      }"""
new_no_kata = """      } else if (state.lang === 'hi') {
        localizedArti = group.arti_hi || group.arti_id || group.arti;
      } else if (state.lang === 'bn') {
        localizedArti = group.arti_bn || group.arti_id || group.arti;
      }"""
code = code.replace(old_no_kata, new_no_kata)

# 5. updateSpotlightCard
old_badge_bentuk = """    } else if (state.lang === 'hi') {
      elements.badgeBentukKata.textContent = group.bentuk_hi || group.bentuk_id;
    } else {"""
new_badge_bentuk = """    } else if (state.lang === 'hi') {
      elements.badgeBentukKata.textContent = group.bentuk_hi || group.bentuk_id;
    } else if (state.lang === 'bn') {
      elements.badgeBentukKata.textContent = group.bentuk_bn || group.bentuk_id;
    } else {"""
code = code.replace(old_badge_bentuk, new_badge_bentuk)

old_badge_jenis = """    } else if (state.lang === 'hi') {
      jenisText = grammar.jenis_hi || (group.bentuk.includes('Mawshul') ? 'संबंधवाचक सर्वनाम' : 'सर्वनाम');
    } else {"""
new_badge_jenis = """    } else if (state.lang === 'hi') {
      jenisText = grammar.jenis_hi || (group.bentuk.includes('Mawshul') ? 'संबंधवाचक सर्वनाम' : 'सर्वनाम');
    } else if (state.lang === 'bn') {
      jenisText = grammar.jenis_bn || (group.bentuk.includes('Mawshul') ? 'সম্বন্ধবাচক সর্বনাম' : 'সর্বনাম');
    } else {"""
code = code.replace(old_badge_jenis, new_badge_jenis)

old_meaning = """    } else if (state.lang === 'hi') {
      currentMeaning = group.arti_hi || group.arti;
    }"""
new_meaning = """    } else if (state.lang === 'hi') {
      currentMeaning = group.arti_hi || group.arti;
    } else if (state.lang === 'bn') {
      currentMeaning = group.arti_bn || group.arti;
    }"""
code = code.replace(old_meaning, new_meaning)

old_desc = """    } else if (state.lang === 'hi') {
      currentDesc = grammar.desc_hi || grammar.desc_id || grammar.keterangan || '';
    }"""
new_desc = """    } else if (state.lang === 'hi') {
      currentDesc = grammar.desc_hi || grammar.desc_id || grammar.keterangan || '';
    } else if (state.lang === 'bn') {
      currentDesc = grammar.desc_bn || grammar.desc_id || grammar.keterangan || '';
    }"""
code = code.replace(old_desc, new_desc)

# 6. Audio in toggleVerseTranslationAudio
old_play_trans_text = """    } else if (state.lang === 'hi') {
      currentText = occ.teksArtiHI || occ.teksArtiID || occ.teksArti;
    }"""
new_play_trans_text = """    } else if (state.lang === 'hi') {
      currentText = occ.teksArtiHI || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'bn') {
      currentText = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
    }"""
code = code.replace(old_play_trans_text, new_play_trans_text)

old_hi_fallback = """    // Special check for Hindi: if Web Speech has no Hindi voice, use audio streaming fallback
    if (state.lang === 'hi') {
      const voices = ('speechSynthesis' in window) ? window.speechSynthesis.getVoices() : [];
      const hiVoice = voices.find(v => v.lang.startsWith('hi'));
      if (!hiVoice || !('speechSynthesis' in window)) {
        const googleTtsUrl = `https://translate.google.com/translate_tts?ie=UTF-8&tl=hi&client=tw-ob&q=${encodeURIComponent(cleanText.slice(0, 200))}`;
        currentTranslationAudio = new Audio(googleTtsUrl);
        currentTranslationAudio.dataset.url = googleTtsUrl;
        isTranslationAudioPlaying = true;
        currentSpeakingBtn = btn;
        btn.classList.add('speaking');
        btn.setAttribute('title', t('stopTranslationBtn'));
        const icon = btn.querySelector('.audio-icon-state');
        if (icon) {
          icon.innerHTML = `<rect x="5" y="4" width="4" height="16" rx="1"></rect><rect x="15" y="4" width="4" height="16" rx="1"></rect>`;
        }
        showToast(t('toastSpeakingMeaning', suratNama, ayat));
        currentTranslationAudio.onended = () => stopAllSpeech();
        currentTranslationAudio.onerror = () => {
          stopAllSpeech();
          showToast(t('toastAudioFailed'));
        };
        currentTranslationAudio.play().catch(err => {
          console.warn('Hindi translation audio playback error:', err);
          stopAllSpeech();
        });
        return;
      }
    }"""

new_hi_bn_fallback = """    // Special check for Hindi & Bangla: if Web Speech has no native voice, use audio streaming fallback
    if (state.lang === 'hi' || state.lang === 'bn') {
      const langCode = state.lang;
      const voices = ('speechSynthesis' in window) ? window.speechSynthesis.getVoices() : [];
      const matchVoice = voices.find(v => v.lang.startsWith(langCode));
      if (!matchVoice || !('speechSynthesis' in window)) {
        const googleTtsUrl = `https://translate.google.com/translate_tts?ie=UTF-8&tl=${langCode}&client=tw-ob&q=${encodeURIComponent(cleanText.slice(0, 200))}`;
        currentTranslationAudio = new Audio(googleTtsUrl);
        currentTranslationAudio.dataset.url = googleTtsUrl;
        isTranslationAudioPlaying = true;
        currentSpeakingBtn = btn;
        btn.classList.add('speaking');
        btn.setAttribute('title', t('stopTranslationBtn'));
        const icon = btn.querySelector('.audio-icon-state');
        if (icon) {
          icon.innerHTML = `<rect x="5" y="4" width="4" height="16" rx="1"></rect><rect x="15" y="4" width="4" height="16" rx="1"></rect>`;
        }
        showToast(t('toastSpeakingMeaning', suratNama, ayat));
        currentTranslationAudio.onended = () => stopAllSpeech();
        currentTranslationAudio.onerror = () => {
          stopAllSpeech();
          showToast(t('toastAudioFailed'));
        };
        currentTranslationAudio.play().catch(err => {
          console.warn(`${langCode.toUpperCase()} translation audio playback error:`, err);
          stopAllSpeech();
        });
        return;
      }
    }"""
code = code.replace(old_hi_fallback, new_hi_bn_fallback)

old_play_trans_lang = """    } else if (state.lang === 'hi') {
      utterance.lang = 'hi-IN';
      utterance.rate = 0.92;
    } else {"""
new_play_trans_lang = """    } else if (state.lang === 'hi') {
      utterance.lang = 'hi-IN';
      utterance.rate = 0.92;
    } else if (state.lang === 'bn') {
      utterance.lang = 'bn-BD';
      utterance.rate = 0.92;
    } else {"""
code = code.replace(old_play_trans_lang, new_play_trans_lang)

old_play_trans_voice = """    } else if (state.lang === 'hi') {
      const hiVoice = voices.find(v => v.lang.startsWith('hi') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Hemant') || v.name.includes('Kalpana') || v.name.includes('Swara') || v.name.includes('Madhur'))) || voices.find(v => v.lang.startsWith('hi'));
      if (hiVoice) utterance.voice = hiVoice;
    } else {"""
new_play_trans_voice = """    } else if (state.lang === 'hi') {
      const hiVoice = voices.find(v => v.lang.startsWith('hi') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Hemant') || v.name.includes('Kalpana') || v.name.includes('Swara') || v.name.includes('Madhur'))) || voices.find(v => v.lang.startsWith('hi'));
      if (hiVoice) utterance.voice = hiVoice;
    } else if (state.lang === 'bn') {
      const bnVoice = voices.find(v => v.lang.startsWith('bn') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Bashkar') || v.name.includes('Tanishaa'))) || voices.find(v => v.lang.startsWith('bn'));
      if (bnVoice) utterance.voice = bnVoice;
    } else {"""
code = code.replace(old_play_trans_voice, new_play_trans_voice)

# 7. speakDhamirMeaning
old_speak_dhamir_lang = """    } else if (state.lang === 'hi') {
      activeMeaning = group.arti_hi || group.arti_id || group.arti;
    }"""
new_speak_dhamir_lang = """    } else if (state.lang === 'hi') {
      activeMeaning = group.arti_hi || group.arti_id || group.arti;
    } else if (state.lang === 'bn') {
      activeMeaning = group.arti_bn || group.arti_id || group.arti;
    }"""
code = code.replace(old_speak_dhamir_lang, new_speak_dhamir_lang)

old_ur_hi_tts = """    // Urdu & Hindi handling with Google TTS stream fallback if Web Speech has no native voice
    if (state.lang === 'ur' || state.lang === 'hi') {"""
new_ur_hi_bn_tts = """    // Urdu, Hindi & Bangla handling with Google TTS stream fallback if Web Speech has no native voice
    if (state.lang === 'ur' || state.lang === 'hi' || state.lang === 'bn') {"""
code = code.replace(old_ur_hi_tts, new_ur_hi_bn_tts)

old_speak_dhamir_utter = """    } else if (state.lang === 'hi') {
      utterance.lang = 'hi-IN';
      utterance.rate = 0.92;
    } else {"""
new_speak_dhamir_utter = """    } else if (state.lang === 'hi') {
      utterance.lang = 'hi-IN';
      utterance.rate = 0.92;
    } else if (state.lang === 'bn') {
      utterance.lang = 'bn-BD';
      utterance.rate = 0.92;
    } else {"""
code = code.replace(old_speak_dhamir_utter, new_speak_dhamir_utter)

old_speak_dhamir_voice = """    } else if (state.lang === 'hi') {
      const hiVoice = voices.find(v => v.lang.startsWith('hi') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Hemant') || v.name.includes('Kalpana') || v.name.includes('Swara') || v.name.includes('Madhur'))) || voices.find(v => v.lang.startsWith('hi'));
      if (hiVoice) utterance.voice = hiVoice;
    } else {"""
new_speak_dhamir_voice = """    } else if (state.lang === 'hi') {
      const hiVoice = voices.find(v => v.lang.startsWith('hi') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Hemant') || v.name.includes('Kalpana') || v.name.includes('Swara') || v.name.includes('Madhur'))) || voices.find(v => v.lang.startsWith('hi'));
      if (hiVoice) utterance.voice = hiVoice;
    } else if (state.lang === 'bn') {
      const bnVoice = voices.find(v => v.lang.startsWith('bn') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Bashkar') || v.name.includes('Tanishaa'))) || voices.find(v => v.lang.startsWith('bn'));
      if (bnVoice) utterance.voice = bnVoice;
    } else {"""
code = code.replace(old_speak_dhamir_voice, new_speak_dhamir_voice)

# 8. renderAyatReferences
old_search_filter = """        } else if (state.lang === 'hi') {
          sArti = occ.suratArtiHI;
          tArti = occ.teksArtiHI;
        }"""
new_search_filter = """        } else if (state.lang === 'hi') {
          sArti = occ.suratArtiHI;
          tArti = occ.teksArtiHI;
        } else if (state.lang === 'bn') {
          sArti = occ.suratArtiBN;
          tArti = occ.teksArtiBN;
        }"""
code = code.replace(old_search_filter, new_search_filter)

old_verse_card_arti = """    } else if (state.lang === 'hi') {
      activeSuratArti = occ.suratArtiHI;
      activeTeksArti = occ.teksArtiHI || occ.teksArtiID || occ.teksArti;
    }"""
new_verse_card_arti = """    } else if (state.lang === 'hi') {
      activeSuratArti = occ.suratArtiHI;
      activeTeksArti = occ.teksArtiHI || occ.teksArtiID || occ.teksArti;
    } else if (state.lang === 'bn') {
      activeSuratArti = occ.suratArtiBN;
      activeTeksArti = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
    }"""
code = code.replace(old_verse_card_arti, new_verse_card_arti)

# 9. applyLanguage
code = code.replace(
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi'].includes(lang) ? lang : 'id';",
    "state.lang = ['en', 'ms', 'fr', 'de', 'ur', 'hi', 'bn'].includes(lang) ? lang : 'id';"
)

# 10. buildAiPrompt
old_ai_vars = """    } else if (state.lang === 'hi') {
      teksArti = occ.teksArtiHI || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_hi || group.grammar.keterangan)) || '';
    }"""
new_ai_vars = """    } else if (state.lang === 'hi') {
      teksArti = occ.teksArtiHI || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_hi || group.grammar.keterangan)) || '';
    } else if (state.lang === 'bn') {
      teksArti = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
      grammarDesc = (group.grammar && (group.grammar.desc_bn || group.grammar.keterangan)) || '';
    }"""
code = code.replace(old_ai_vars, new_ai_vars)

old_ai_prompt_branches = """    } else if (state.lang === 'hi') {
      if (topic === 'nahwu') {
        return `कृपया क़ुरआन मजीद की सूरह ${suratNama} (${surat}) आयत ${ayat} में उपस्थित शब्द "${kata}" (${noKata}, ${bentuk}) के अरबी व्याकरण (नहव/सर्फ़) और ए'राब की विस्तृत व्याख्या करें:\\n\\nअरबी पाठ: "${teksArab}"\\nअनुवाद: "${teksArti}"\\n\\nकृपया निम्नलिखित बिंदुओं को शामिल करें:\\n१. इस वाक्य रचना में "${kata}" की व्याकरणिक भूमिका और ए'राब (I'rab)।\\n२. शब्द का रूप (ज़मीर मुन्फ़सिल/मुत्तसिल या इस्म मौसूल) और इसकी स्थिति (रफ़ा/नसब/जर)।\\n३. व्याकरणिक टिप्पणी: ${grammarDesc || 'मानक क़ुरआनी प्रयोग'}।`;
      } else if (topic === 'tafsir') {
        return `कृपया सूरह ${suratNama} (${surat}) आयत ${ayat} की संक्षिप्त और संदर्भात्मक तफ़सीर (व्याख्या) प्रस्तुत करें:\\n\\nअरबी पाठ: "${teksArab}"\\nअनुवाद: "${teksArti}"\\n\\nविशेष रूप से शब्द/सर्वनाम "${kata}" के महत्व पर ध्यान केंद्रित करते हुए बताएं कि इस आयत में क्या मुख्य शिक्षा, अवतरण का संदर्भ और ईश्वरीय संदेश निहित है?`;
      } else {
        return `सूरह ${suratNama} (${surat}) आयत ${ayat} में शब्द "${kata}" के चयन के संबंध में क़ुरआनी बलाग़त (अलंकारिक सौंदर्य व शैली) की व्याख्या करें:\\n\\nअरबी पाठ: "${teksArab}"\\nअनुवाद: "${teksArti}"\\n\\nयहाँ पर सर्वनाम का यही विशिष्ट रूप क्यों प्रयुक्त हुआ है? यह आयत के अर्थ की गहराई और साहित्यिक सौंदर्य में क्या वृद्धि करता है?`;
      }
    } else {"""

new_ai_prompt_branches = """    } else if (state.lang === 'hi') {
      if (topic === 'nahwu') {
        return `कृपया क़ुरआन मजीद की सूरह ${suratNama} (${surat}) आयत ${ayat} में उपस्थित शब्द "${kata}" (${noKata}, ${bentuk}) के अरबी व्याकरण (नहव/सर्फ़) और ए'राब की विस्तृत व्याख्या करें:\\n\\nअरबी पाठ: "${teksArab}"\\nअनुवाद: "${teksArti}"\\n\\nकृपया निम्नलिखित बिंदुओं को शामिल करें:\\n१. इस वाक्य रचना में "${kata}" की व्याकरणिक भूमिका और ए'राब (I'rab)।\\n२. शब्द का रूप (ज़मीर मुन्फ़सिल/मुत्तसिल या इस्म मौसूल) और इसकी स्थिति (रफ़ा/नसब/जर)।\\n३. व्याकरणिक टिप्पणी: ${grammarDesc || 'मानक क़ुरआनी प्रयोग'}।`;
      } else if (topic === 'tafsir') {
        return `कृपया सूरह ${suratNama} (${surat}) आयत ${ayat} की संक्षिप्त और संदर्भात्मक तफ़सीर (व्याख्या) प्रस्तुत करें:\\n\\nअरबी पाठ: "${teksArab}"\\nअनुवाद: "${teksArti}"\\n\\nविशेष रूप से शब्द/सर्वनाम "${kata}" के महत्व पर ध्यान केंद्रित करते हुए बताएं कि इस आयत में क्या मुख्य शिक्षा, अवतरण का संदर्भ और ईश्वरीय संदेश निहित है?`;
      } else {
        return `सूरह ${suratNama} (${surat}) आयत ${ayat} में शब्द "${kata}" के चयन के संबंध में क़ুরআनी बलाग़त (अलंकारिक सौंदर्य व शैली) की व्याख्या करें:\\n\\nअरबी पाठ: "${teksArab}"\\nअनुवाद: "${teksArti}"\\n\\nयहाँ पर सर्वनाम का यही विशिष्ट रूप क्यों प्रयुक्त हुआ है? यह आयत के अर्थ की गहराई और साहित्यिक सौंदर्य में क्या वृद्धि करता है?`;
      }
    } else if (state.lang === 'bn') {
      if (topic === 'nahwu') {
        return `অনুগ্রহ করে পবিত্র কুরআনের সূরা ${suratNama} (${surat}) আয়াত ${ayat}-এ অবস্থিত শব্দ "${kata}" (${noKata}, ${bentuk})-এর আরবি ব্যাকরণ (নাহব/সরফ) ও ই'রাব বিস্তারিতভাবে ব্যাখ্যা করুন:\\n\\nআরবি পাঠ: "${teksArab}"\\nঅনুবাদ: "${teksArti}"\\n\\nঅনুগ্রহ করে নিম্নলিখিত বিষয়গুলো আলোচনা করুন:\\n১. এই বাক্যের গঠনে "${kata}"-এর ব্যাকরণগত ভূমিকা ও ই'রাব (I'rab)।\\n২. শব্দের রূপগত প্রকার (যমীর মুনফাসিল/মুত্তাসিল অথবা ইসম মাওসুল) এবং এর অবস্থা (মারফু'/মানসুব/মাজরুর)।\\n৩. ব্যাকরণগত নোট: ${grammarDesc || 'প্রমিত কুরআনিক প্রয়োগ'}।`;
      } else if (topic === 'tafsir') {
        return `অনুগ্রহ করে সূরা ${suratNama} (${surat}) আয়াত ${ayat}-এর সংক্ষিপ্ত ও প্রাসঙ্গিক তাফসির (ব্যাখ্যা) উপস্থাপন করুন:\\n\\nআরবি পাঠ: "${teksArab}"\\nঅনুবাদ: "${teksArti}"\\n\\nবিশেষ করে শব্দ/সর্বনাম "${kata}"-এর তাৎপর্যের ওপর গুরুত্ব দিয়ে বলুন, এই আয়াতে কী মূল হেকমত, শানে নুযূল এবং ঐশী বার্তা নিহিত রয়েছে?`;
      } else {
        return `সূরা ${suratNama} (${surat}) আয়াত ${ayat}-এ শব্দ "${kata}" নির্বাচনের ক্ষেত্রে কুরআনিক বালাগাত (অলঙ্কারিক সৌন্দর্য ও রচনাশৈলী) ব্যাখ্যা করুন:\\n\\nআরবি পাঠ: "${teksArab}"\\nঅনুবাদ: "${teksArti}"\\n\\nএখানে সর্বনামের এই নির্দিষ্ট রূপটি কেন ব্যবহৃত হয়েছে? এটি আয়াতের অর্থ ও সাহিত্যের গভীরতায় কী সৌন্দর্য যোগ করে?`;
      }
    } else {"""
code = code.replace(old_ai_prompt_branches, new_ai_prompt_branches)

# 11. openAiModal
old_modal_arti = """      } else if (state.lang === 'hi') {
        activeArti = occ.teksArtiHI || occ.teksArtiID || occ.teksArti;
      }"""
new_modal_arti = """      } else if (state.lang === 'hi') {
        activeArti = occ.teksArtiHI || occ.teksArtiID || occ.teksArti;
      } else if (state.lang === 'bn') {
        activeArti = occ.teksArtiBN || occ.teksArtiID || occ.teksArti;
      }"""
code = code.replace(old_modal_arti, new_modal_arti)

# 12. CSV Export
old_csv_header = "Bedeutung (DE),Mani (UR),Artha (HI),Frekuensi"
new_csv_header = "Bedeutung (DE),Mani (UR),Artha (HI),Orthobhed (BN),Frekuensi"
code = code.replace(old_csv_header, new_csv_header)

old_csv_header2 = "Übersetzung (DE),Tarjuma (UR),Anuvad (HI),Link Audio"
new_csv_header2 = "Übersetzung (DE),Tarjuma (UR),Anuvad (HI),Onubad (BN),Link Audio"
code = code.replace(old_csv_header2, new_csv_header2)

old_csv_body1 = """      const cleanArtiHI = (occ.teksArtiHI || '').replace(/"/g, '""');
      const audioLink = occ.audioUrl || '';"""
new_csv_body1 = """      const cleanArtiHI = (occ.teksArtiHI || '').replace(/"/g, '""');
      const cleanArtiBN = (occ.teksArtiBN || '').replace(/"/g, '""');
      const audioLink = occ.audioUrl || '';"""
code = code.replace(old_csv_body1, new_csv_body1)

old_csv_row = """"${group.arti_de || ''}","${group.arti_ur || ''}","${group.arti_hi || ''}","${group.frek || 'Muttashil'}" """
new_csv_row = """"${group.arti_de || ''}","${group.arti_ur || ''}","${group.arti_hi || ''}","${group.arti_bn || ''}","${group.frek || 'Muttashil'}" """
# Let's check exact line in app.js for csv row
code = code.replace(
    '="${group.arti_hi || \'\'}","${group.frek || \'Muttashil\'}"',
    '="${group.arti_hi || \'\'}","${group.arti_bn || \'\'}","${group.frek || \'Muttashil\'}"'
)
code = code.replace(
    '"${cleanArtiHI}","${audioLink}"',
    '"${cleanArtiHI}","${cleanArtiBN}","${audioLink}"'
)

# 13. btnCopyAll
old_copy_arti = """        } else if (state.lang === 'hi') {
          activeArti = group.arti_hi || group.arti;
        }"""
new_copy_arti = """        } else if (state.lang === 'hi') {
          activeArti = group.arti_hi || group.arti;
        } else if (state.lang === 'bn') {
          activeArti = group.arti_bn || group.arti;
        }"""
code = code.replace(old_copy_arti, new_copy_arti)

old_copy_mawshul = """          else if (state.lang === 'hi') titlePrefix = 'क़ुरआनी संबंधवाचक सर्वनाम (Mawshul)';"""
new_copy_mawshul = """          else if (state.lang === 'hi') titlePrefix = 'क़ुरआनी संबंधवाचक सर्वनाम (Mawshul)';
          else if (state.lang === 'bn') titlePrefix = 'কুরআনিক সম্বন্ধবাচক সর্বনাম (Mawshul)';"""
code = code.replace(old_copy_mawshul, new_copy_mawshul)

old_copy_dhamir = """          else if (state.lang === 'hi') titlePrefix = 'क़ुरआनी सर्वनाम (Dhamir)';"""
new_copy_dhamir = """          else if (state.lang === 'hi') titlePrefix = 'क़ुरआनी सर्वनाम (Dhamir)';
          else if (state.lang === 'bn') titlePrefix = 'কুরআনিক সর্বনাম (Dhamir)';"""
code = code.replace(old_copy_dhamir, new_copy_dhamir)

with open(app_js_path, 'w', encoding='utf-8') as f:
    f.write(code)

print(f"[OK] Successfully updated {app_js_path} for Bangla (bn) language!")
