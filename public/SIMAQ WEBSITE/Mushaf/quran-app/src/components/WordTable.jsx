import React, { useState, useEffect } from 'react';

const renderMixedText = (text, forceColor = null) => {
  if (text == null || text === '') return '';
  const textStr = String(text);
  const arabicRegex = /([\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+(?:[\s]+[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+)*)/g;
  const shouldHighlight = textStr.includes('-');
  
  let wordCount = 0;
  // User requested yellow and red colors
  const colors = ['#fde047', '#f87171']; // yellow and red

  return textStr.split(arabicRegex).map((part, index) => {
    // If it's an Arabic part
    if (part.match(/[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]/)) {
      const color = forceColor ? forceColor : (shouldHighlight ? colors[wordCount % colors.length] : undefined);
      if (shouldHighlight && !forceColor) wordCount++;
      // Only shrink font size if it has a hyphen (shouldHighlight)
      return <span key={index} className="arabic-text-small" dir="rtl" style={{...(color ? {color} : {}), fontSize: shouldHighlight ? '1.1rem' : undefined}}>{part}</span>;
    }
    
    // For non-Arabic parts, highlight hyphens and apply colors to split parts
    if (shouldHighlight) {
      return (
        <span key={index}>
          {part.split(/(-)/).map((subPart, subIndex) => {
            if (subPart === '-') {
              return <span key={subIndex} style={{color: forceColor ? forceColor : 'rgba(255,255,255,0.4)', margin: '0 4px'}}>-</span>;
            } else if (subPart.trim().length > 0) {
              const color = forceColor ? forceColor : colors[wordCount % colors.length];
              if (!forceColor) wordCount++;
              return <span key={subIndex} style={{color}}>{subPart}</span>;
            } else {
              return <span key={subIndex}>{subPart}</span>;
            }
          })}
        </span>
      );
    }
    
    return <span key={index} style={forceColor ? {color: forceColor} : {}}>{part}</span>;
  });
};

const getMuttashilTitle = (text) => {
  if (!text) return 'Dhamir/Harf Muttashil';
  const trimmed = text.trim();
  // In RTL, starting with '..' means '..' is on the right (suffix/Dhamir)
  // Ending with '..' means '..' is on the left (prefix/Harf)
  const startsWithDots = trimmed.startsWith('..');
  const endsWithDots = trimmed.endsWith('..');
  
  if (startsWithDots && endsWithDots) {
    return 'Dhamir Muttashil / Harf Muttashil';
  } else if (startsWithDots) {
    return 'Dhamir Muttashil';
  } else if (endsWithDots) {
    return 'Harf Muttashil';
  }
  return 'Dhamir/Harf Muttashil';
};

const cleanArabicForTTS = (text) => {
  if (!text) return '';
  return text
    // Replace Uthmani Alif Wasla with normal Alif
    .replace(/\u0671/g, '\u0627')
    // Replace Dagger Alif with normal Alif
    .replace(/\u0670/g, '\u0627')
    // Replace Uthmani small sukoon with standard sukoon
    .replace(/\u06E1/g, '\u0652')
    // Remove waqf marks and other small Uthmani symbols
    .replace(/[\u06D6-\u06DC\u06DF-\u06E0\u06E2-\u06ED]/g, '')
    .trim();
};

let currentWordAudio = null;

const stopAllAudio = () => {
  const mainAudio = document.getElementById('main-ayah-audio');
  if (mainAudio && !mainAudio.paused) {
    mainAudio.pause();
  }
  
  if (currentWordAudio) {
    currentWordAudio.pause();
    currentWordAudio.currentTime = 0;
  }
  
  if (window.speechSynthesis) {
    window.speechSynthesis.cancel();
  }
};

const playAudio = (text, lang = 'ar') => {
  if (!text) return;
  
  // Clean Uthmani text so Google TTS can read it properly
  const ttsText = lang === 'ar' ? cleanArabicForTTS(text) : text;
  
  // Try using Google Translate TTS with multiple endpoints
  const urls = [
    `https://translate.google.com/translate_tts?ie=UTF-8&q=${encodeURIComponent(ttsText)}&tl=${lang}&client=tw-ob`,
    `https://translate.googleapis.com/translate_tts?ie=UTF-8&q=${encodeURIComponent(ttsText)}&tl=${lang}&client=gtx`
  ];

  const tryPlay = (index) => {
    if (index >= urls.length) {
      console.error("All TTS URLs failed, falling back to speech synthesis");
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = lang === 'ar' ? 'ar-SA' : 'id-ID'; 
      utterance.rate = 0.85;
      
      // Attempt to speak, and if it fails, alert the user
      utterance.onerror = (e) => {
        console.error("SpeechSynthesis error:", e);
        alert("Maaf, audio tidak dapat diputar. Peramban Anda mungkin tidak mendukung fitur ini atau butuh koneksi internet yang stabil.");
      };
      
      window.speechSynthesis.speak(utterance);
      return;
    }

    const audio = new Audio(urls[index]);
    currentWordAudio = audio;
    audio.play().catch(e => {
      console.warn(`TTS URL ${index} failed:`, e);
      tryPlay(index + 1);
    });
  };

  tryPlay(0);
};

const playQuranWord = (suratId, ayatId, wordIndex, fallbackText) => {
  stopAllAudio();
  
  if (!suratId || !ayatId || !wordIndex) {
    playAudio(fallbackText, 'ar');
    return;
  }
  
  const surahStr = String(suratId).padStart(3, '0');
  const ayahStr = String(ayatId).padStart(3, '0');
  const wordStr = String(wordIndex).padStart(3, '0');
  
  const url = `https://verses.quran.com/wbw/${surahStr}_${ayahStr}_${wordStr}.mp3`;
  
  const audio = new Audio(url);
  currentWordAudio = audio;
  audio.play().catch(e => {
    console.warn("Quran CDN failed, falling back to TTS:", e);
    playAudio(fallbackText, 'ar');
  });
};

const translationCache = new Map();

const fetchTranslation = async (text, lang) => {
  if (lang === 'id' || !text) return text;
  
  const cacheKey = `${lang}_${text}`;
  if (translationCache.has(cacheKey)) {
    return translationCache.get(cacheKey);
  }

  try {
    const response = await fetch(`https://translate.googleapis.com/translate_a/single?client=gtx&sl=id&tl=${lang}&dt=t&q=${encodeURIComponent(text)}`);
    const data = await response.json();
    const translatedText = data[0].map(item => item[0]).join('');
    translationCache.set(cacheKey, translatedText);
    return translatedText;
  } catch (error) {
    console.error("Translation error:", error);
    return text;
  }
};

const TranslatedText = ({ text, lang }) => {
  const [translated, setTranslated] = useState(lang === 'id' ? text : '...');
  
  useEffect(() => {
    if (lang === 'id') {
      setTranslated(text);
      return;
    }
    let isMounted = true;
    setTranslated('...');
    fetchTranslation(text, lang).then(res => {
      if (isMounted) setTranslated(res);
    });
    return () => { isMounted = false; };
  }, [text, lang]);

  return <span>{translated}</span>;
};

function WordTable({ data, visibleColumns }) {
  const [activeTooltipIndex, setActiveTooltipIndex] = useState(null);
  const [activeBentukTooltipIndex, setActiveBentukTooltipIndex] = useState(null);
  const [activeLafdzTooltipIndex, setActiveLafdzTooltipIndex] = useState(null);
  const [terjemahLang, setTerjemahLang] = useState('id');

  if (!data || data.length === 0) return null;

  const isAnyDetailVisible = Object.values(visibleColumns).some(v => v);

  return (
    <div>
      <div className="table-container glass">
        <table className={`word-table ${isAnyDetailVisible ? 'table-expanded' : 'table-compact'}`} dir="rtl">
          <thead>
            <tr>
              <th style={{color: 'white', backgroundColor: 'rgba(255, 255, 255, 0.08)', width: '20%'}}>Lafdz</th>
              {visibleColumns.kataAkar && <th style={{color: '#fde047', backgroundColor: 'rgba(253, 224, 71, 0.2)', width: '20%'}}>Kata/Akar</th>}
              {visibleColumns.bentuk && <th className="text-left" style={{color: 'white', backgroundColor: 'rgba(255, 255, 255, 0.08)', width: '20%'}}>Bentuk Kata</th>}
              {visibleColumns.terjemah && (
                <th className="text-left" style={{color: '#fde047', backgroundColor: 'rgba(253, 224, 71, 0.2)', width: '20%'}}>
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                    <span>Terjemah</span>
                    <div style={{ display: 'flex', gap: '4px' }}>
                      <button 
                        onClick={() => setTerjemahLang('id')}
                        style={{
                          background: terjemahLang === 'id' ? '#fde047' : 'transparent',
                          color: terjemahLang === 'id' ? '#0f172a' : '#fde047',
                          border: '1px solid #fde047',
                          borderRadius: '4px',
                          padding: '2px 6px',
                          fontSize: '0.75rem',
                          cursor: 'pointer'
                        }}
                      >ID</button>
                      <button 
                        onClick={() => setTerjemahLang('en')}
                        style={{
                          background: terjemahLang === 'en' ? '#fde047' : 'transparent',
                          color: terjemahLang === 'en' ? '#0f172a' : '#fde047',
                          border: '1px solid #fde047',
                          borderRadius: '4px',
                          padding: '2px 6px',
                          fontSize: '0.75rem',
                          cursor: 'pointer'
                        }}
                      >EN</button>
                    </div>
                  </div>
                </th>
              )}
            </tr>
          </thead>
          <tbody>
            {[...data].map((row, index) => {
              return (
                <tr key={index}>
                  <td 
                    style={{
                      padding: 0,
                      backgroundColor: 'rgba(255, 255, 255, 0.08)',
                      verticalAlign: 'middle'
                    }}
                  >
                    <div 
                      className={`flip-container ${activeLafdzTooltipIndex === index ? 'flipped' : ''}`}
                      onClick={() => {
                        if ((row['Dhamir Muttashil / Harf Muttashil'] || '').trim()) {
                          setActiveLafdzTooltipIndex(activeLafdzTooltipIndex === index ? null : index);
                        }
                      }}
                      title={(row['Dhamir Muttashil / Harf Muttashil'] || '').trim() ? "Klik untuk melihat Dhamir/Harf Muttashil" : ""}
                      style={{ cursor: (row['Dhamir Muttashil / Harf Muttashil'] || '').trim() ? 'pointer' : 'default' }}
                    >
                      <div className="flip-inner">
                        <div className="flip-front arabic-text-small" style={{ color: 'white' }}>
                          {row['Lafdz'] || ''}
                          {!(row['Dhamir Muttashil / Harf Muttashil'] || '').trim() && <span style={{opacity: 0.3, fontSize: '0.8em', margin: '0 4px'}}>&bull;</span>}
                        </div>
                        {row['Dhamir Muttashil / Harf Muttashil'] && (
                          <div className="flip-back">
                            <div style={{color: 'white', lineHeight: '1.4', fontSize: '1rem', fontFamily: 'system-ui, sans-serif'}} dir="rtl">
                              <div style={{fontSize: '0.75rem', opacity: 0.7, marginBottom: '0.25rem', fontFamily: 'system-ui, sans-serif', textAlign: 'center'}}>
                                {getMuttashilTitle(row['Dhamir Muttashil / Harf Muttashil'])}
                              </div>
                              {renderMixedText(row['Dhamir Muttashil / Harf Muttashil'], 'white')}
                            </div>
                          </div>
                        )}
                      </div>
                    </div>
                  </td>
                  {visibleColumns.kataAkar && (
                    <td 
                      style={{
                        padding: 0,
                        backgroundColor: 'rgba(253, 224, 71, 0.2)',
                        verticalAlign: 'middle'
                      }}
                    >
                      <div 
                        className={`flip-container ${activeTooltipIndex === index ? 'flipped' : ''}`}
                        onClick={() => setActiveTooltipIndex(activeTooltipIndex === index ? null : index)}
                        title="Klik untuk melihat arti"
                        style={{ cursor: 'pointer' }}
                      >
                        <div className="flip-inner">
                          <div className="flip-front arabic-text-small" style={{ color: '#fde047' }}>
                            {renderMixedText(row['Kata/Akar'] || '', '#fde047')}
                          </div>
                          {(row['Arti '] || row['Arti']) && (
                            <div className="flip-back">
                              <div style={{color: '#fde047', lineHeight: '1.4', fontSize: '0.9rem', fontFamily: 'system-ui, sans-serif'}} dir="ltr">
                                {renderMixedText(row['Arti '] || row['Arti'] || '', '#fde047')}
                              </div>
                            </div>
                          )}
                        </div>
                      </div>
                    </td>
                  )}
                  {visibleColumns.bentuk && (
                    <td 
                      style={{
                        padding: 0,
                        backgroundColor: 'rgba(255, 255, 255, 0.08)',
                        verticalAlign: 'middle'
                      }}
                    >
                      <div 
                        className={`flip-container ${activeBentukTooltipIndex === index ? 'flipped' : ''}`}
                        onClick={() => setActiveBentukTooltipIndex(activeBentukTooltipIndex === index ? null : index)}
                        title="Klik untuk melihat Teori/I'rab/Wazan/I'lal"
                        style={{ cursor: 'pointer' }}
                      >
                        <div className="flip-inner">
                          <div className="flip-front text-left" dir="ltr" style={{ color: 'white' }}>
                            {renderMixedText(row['Bentuk Kata'] || '', 'white')}
                          </div>
                          {row["Teori/i'rab/Wazan/I'lal"] && (
                            <div className="flip-back">
                              <div style={{color: 'white', lineHeight: '1.4', fontSize: '0.9rem', fontFamily: 'system-ui, sans-serif'}} dir="ltr">
                                {renderMixedText(row["Teori/i'rab/Wazan/I'lal"], 'white')}
                              </div>
                            </div>
                          )}
                        </div>
                      </div>
                    </td>
                  )}
                  {visibleColumns.terjemah && (
                    <td className="text-left" dir="ltr" style={{color: '#fde047', backgroundColor: 'rgba(253, 224, 71, 0.2)'}}>
                      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                        <TranslatedText text={String(row['Terjemah'] || '').replace(/\s*\[.*?\]\s*/g, ' ').trim()} lang={terjemahLang} />
                        <button 
                          onClick={(e) => {
                            e.stopPropagation();
                            playQuranWord(row['SURAT_ID'], row['AYAT_ID'], index + 1, row['Lafdz']);
                          }}
                          title="Putar Audio Lafdz"
                          style={{
                            background: 'transparent',
                            border: 'none',
                            cursor: 'pointer',
                            padding: '4px',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            color: '#fde047',
                            opacity: 0.7,
                            transition: 'opacity 0.2s',
                            marginLeft: '8px'
                          }}
                          onMouseEnter={(e) => e.currentTarget.style.opacity = '1'}
                          onMouseLeave={(e) => e.currentTarget.style.opacity = '0.7'}
                        >
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                            <path d="M11.536 14.01A8.47 8.47 0 0 0 14.026 8a8.47 8.47 0 0 0-2.49-6.01l-.708.707A7.48 7.48 0 0 1 13.025 8c0 2.071-.84 3.946-2.197 5.303z"/>
                            <path d="M10.121 12.596A6.48 6.48 0 0 0 12.025 8a6.48 6.48 0 0 0-1.904-4.596l-.707.707A5.48 5.48 0 0 1 11.025 8a5.48 5.48 0 0 1-1.61 3.89z"/>
                            <path d="M8.707 11.182A4.5 4.5 0 0 0 10.025 8a4.5 4.5 0 0 0-1.318-3.182L8 5.525A3.5 3.5 0 0 1 9.025 8 3.5 3.5 0 0 1 8 10.475zM6.717 3.55A.5.5 0 0 1 7 4v8a.5.5 0 0 1-.812.39L3.825 10.5H1.5A.5.5 0 0 1 1 10V6a.5.5 0 0 1 .5-.5h2.325l2.363-1.89a.5.5 0 0 1 .529-.06"/>
                          </svg>
                        </button>
                      </div>
                    </td>
                  )}
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default WordTable;
