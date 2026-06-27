import { useState, useEffect, useRef } from 'react';

function Flashcard({ word, surahId, ayatNumber, playAudioGlobal, rootWord }) {
  const [isFlipped, setIsFlipped] = useState(false);

  // If the word is the "end" marker (verse number), we don't necessarily need to flip it
  if (word.char_type_name === "end") {
    return (
      <div className="word-scene" style={{ width: '80px' }}>
         <div className="word-card">
           <div className="word-card-face word-card-front" style={{ border: 'none', background: 'transparent', boxShadow: 'none' }}>
             <div className="word-arabic-text" style={{ fontSize: '1.5rem', color: 'var(--text-dim)' }}>
               {word.text_uthmani}
             </div>
           </div>
         </div>
      </div>
    );
  }

  const handleCardClick = () => {
    setIsFlipped(!isFlipped);
    if (word.char_type_name === "word") {
      // Reconstruct audio URL manually to fix API offset bugs (like Surah 11 Ayat 4)
      const paddedSurah = String(surahId).padStart(3, '0');
      const paddedAyat = String(ayatNumber).padStart(3, '0');
      const paddedPos = String(word.position).padStart(3, '0');
      const constructedAudioUrl = `https://verses.quran.com/wbw/${paddedSurah}_${paddedAyat}_${paddedPos}.mp3`;
      
      playAudioGlobal(constructedAudioUrl, false);
    }
  };

  return (
    <div className="word-scene" onClick={handleCardClick}>
      <div className={`word-card ${isFlipped ? 'is-flipped' : ''}`}>
        <div className="word-card-face word-card-front">
          <div className="audio-indicator">🔊</div>
          <div className="word-arabic-text">{word.text_uthmani}</div>
        </div>
        <div className="word-card-face word-card-back">
          <div className="word-meaning-text">{word.translation?.text || ''}</div>
          {rootWord && (
            <div className="word-root-text">
              {rootWord}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

function App() {
  const [surahs, setSurahs] = useState([]);
  const [currentSurahId, setCurrentSurahId] = useState(1);
  const [ayatData, setAyatData] = useState([]);
  const [currentAyatIndex, setCurrentAyatIndex] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  const [rootDictionary, setRootDictionary] = useState({});
  
  const currentAudioRef = useRef(null);
  const [isPlayingVerse, setIsPlayingVerse] = useState(false);

  const stopAudio = () => {
    if (currentAudioRef.current) {
      currentAudioRef.current.pause();
      currentAudioRef.current.currentTime = 0;
    }
    setIsPlayingVerse(false);
  };

  const playAudioGlobal = (url, isVerse) => {
    stopAudio(); // Stop any currently playing audio
    const audio = new Audio(url);
    currentAudioRef.current = audio;
    if (isVerse) {
      setIsPlayingVerse(true);
    }
    audio.play().catch(e => {
      console.error("Audio error:", e);
      if (isVerse) setIsPlayingVerse(false);
    });
    audio.onended = () => {
      if (isVerse) setIsPlayingVerse(false);
    };
  };

  // Stop audio when changing verses or unmounting
  useEffect(() => {
    stopAudio();
    return () => stopAudio(); // Cleanup on unmount
  }, [currentAyatIndex, currentSurahId]);

  // Fetch all Surahs and roots on mount
  useEffect(() => {
    async function fetchAllSurahs() {
      try {
        const res = await fetch("https://api.quran.com/api/v4/chapters?language=id");
        const data = await res.json();
        setSurahs(data.chapters);
      } catch (error) {
        console.error("Error fetching chapters:", error);
      }
    }
    
    async function fetchRoots() {
      try {
        const res = await fetch("/roots.json");
        const data = await res.json();
        setRootDictionary(data);
      } catch (error) {
        console.error("Error fetching roots:", error);
      }
    }
    
    fetchAllSurahs();
    fetchRoots();
  }, []);

  // Fetch Ayats when Surah changes
  useEffect(() => {
    async function fetchSurah() {
      setIsLoading(true);
      try {
        let allVerses = [];
        let currentPage = 1;
        let totalPages = 1;
        
        do {
          const res = await fetch(`https://api.quran.com/api/v4/verses/by_chapter/${currentSurahId}?language=id&words=true&word_fields=text_uthmani&word_translation_language=id&audio=7&per_page=100&page=${currentPage}`);
          const data = await res.json();
          allVerses = [...allVerses, ...data.verses];
          totalPages = data.pagination.total_pages;
          currentPage++;
        } while (currentPage <= totalPages);
        
        // Transform the data
        const formattedData = allVerses.map(verse => ({
          ayatNumber: verse.verse_number,
          fullText: verse.words.map(w => w.text_uthmani).join(' '),
          words: verse.words,
          audioUrl: verse.audio?.url ? `https://verses.quran.com/${verse.audio.url}` : null
        }));
        
        setAyatData(formattedData);
        setCurrentAyatIndex(0); // Reset to first verse
      } catch (error) {
        console.error("Error fetching data:", error);
      }
      setIsLoading(false);
    }
    fetchSurah();
  }, [currentSurahId]);

  const handleNext = () => {
    setCurrentAyatIndex((prev) => (prev < ayatData.length - 1 ? prev + 1 : prev));
  };

  const handlePrev = () => {
    setCurrentAyatIndex((prev) => (prev > 0 ? prev - 1 : prev));
  };

  const currentAyat = ayatData[currentAyatIndex];

  return (
    <div className="app-container">
      <div className="header">
        <h1>Qur'an Flip Game</h1>
        <p>Belajar Terjemah Per Lafadz</p>
        
        <div className="selectors-container">
          <select 
            className="surah-selector" 
            value={currentSurahId} 
            onChange={(e) => setCurrentSurahId(Number(e.target.value))}
          >
            {surahs.map(surah => (
               <option key={surah.id} value={surah.id}>
                 Surah {surah.id} - {surah.name_simple}
               </option>
            ))}
          </select>

          {!isLoading && ayatData.length > 0 && (
            <select 
              className="ayat-selector" 
              value={currentAyatIndex} 
              onChange={(e) => setCurrentAyatIndex(Number(e.target.value))}
            >
              {ayatData.map((ayat, idx) => (
                <option key={ayat.ayatNumber} value={idx}>
                  Ayat {ayat.ayatNumber}
                </option>
              ))}
            </select>
          )}
        </div>
      </div>

      {isLoading ? (
        <div className="loading">Memuat Surah...</div>
      ) : (
        currentAyat && (
          <div className="ayat-container">
            <div className="ayat-header-container">
              <div className="ayat-full-text">{currentAyat.fullText}</div>
              {currentAyat.audioUrl && (
                <div className="ayat-audio-controls">
                  {isPlayingVerse ? (
                    <button 
                      className="play-ayat-btn stop" 
                      onClick={stopAudio}
                      title="Hentikan Audio"
                    >
                      ⏹ Hentikan
                    </button>
                  ) : (
                    <button 
                      className="play-ayat-btn play" 
                      onClick={() => playAudioGlobal(currentAyat.audioUrl, true)}
                      title="Dengarkan seluruh ayat"
                    >
                      🔊 Putar Ayat
                    </button>
                  )}
                </div>
              )}
            </div>
            
            <div className="words-grid">
              {currentAyat.words.map((word) => (
                <Flashcard 
                  key={word.id} 
                  word={word} 
                  surahId={currentSurahId} 
                  ayatNumber={currentAyat.ayatNumber} 
                  playAudioGlobal={playAudioGlobal}
                  rootWord={rootDictionary[`${currentSurahId}_${currentAyat.ayatNumber}_${word.position}`]}
                />
              ))}
            </div>
          </div>
        )
      )}

      {!isLoading && currentAyat && (
        <div className="controls">
          <button onClick={handlePrev} disabled={currentAyatIndex === 0}>
            Ayat Sebelumnya
          </button>
          <div className="verse-counter">
            Ayat {currentAyat.ayatNumber} / {ayatData.length}
          </div>
          <button onClick={handleNext} disabled={currentAyatIndex === ayatData.length - 1}>
            Ayat Selanjutnya
          </button>
        </div>
      )}
    </div>
  );
}

export default App;
