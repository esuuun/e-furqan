import React, { useState, useEffect } from 'react';
import SurahSelector from './components/SurahSelector';
import AyahSelector from './components/AyahSelector';
import ColumnSelector from './components/ColumnSelector';
import WordTable from './components/WordTable';

function App() {
  const [metadata, setMetadata] = useState(null);
  const [selectedSurah, setSelectedSurah] = useState(null);
  const [selectedAyah, setSelectedAyah] = useState(null);
  const [isAyahFlipped, setIsAyahFlipped] = useState(false);
  
  const [surahData, setSurahData] = useState(null);
  const [loadingSurah, setLoadingSurah] = useState(false);

  const [visibleColumns, setVisibleColumns] = useState({
    kataAkar: false,
    bentuk: false,
    terjemah: false
  });

  const handleToggleColumn = (colId) => {
    setVisibleColumns(prev => ({ ...prev, [colId]: !prev[colId] }));
  };

  // Fetch metadata on mount
  useEffect(() => {
    const baseUrl = import.meta.env.BASE_URL || './';
    fetch(`${baseUrl}data/metadata.json`)
      .then(res => res.json())
      .then(data => {
        setMetadata(data);
      })
      .catch(err => console.error("Error fetching metadata:", err));
  }, []);

  // Fetch surah data when selectedSurah changes
  useEffect(() => {
    if (selectedSurah) {
      setLoadingSurah(true);
      setSurahData(null);
      setSelectedAyah(null);
      setIsAyahFlipped(false);
      
      const baseUrl = import.meta.env.BASE_URL || './';
      fetch(`${baseUrl}data/surah_${selectedSurah}.json`)
        .then(res => res.json())
        .then(data => {
          setSurahData(data);
          setLoadingSurah(false);
          // auto-select first ayah if available
          const ayahs = Object.keys(data).sort((a,b) => parseInt(a) - parseInt(b));
          if (ayahs.length > 0) {
            setSelectedAyah(ayahs[0]);
          }
        })
        .catch(err => {
          console.error("Error fetching surah data:", err);
          setLoadingSurah(false);
        });
    }
  }, [selectedSurah]);

  const handleSelectSurah = (surahId) => {
    if (surahId !== selectedSurah) {
      setSelectedSurah(surahId);
    }
  };

  const handleSelectAyah = (ayahId) => {
    setSelectedAyah(ayahId);
    setIsAyahFlipped(false);
  };

  const availableSurahs = metadata ? Object.keys(metadata) : [];
  const availableAyahs = (metadata && selectedSurah) ? metadata[selectedSurah] : [];
  
  const currentAyahData = (surahData && selectedAyah) ? surahData[selectedAyah] : [];

  // Navigation Logic
  const ayahsList = surahData ? Object.keys(surahData).sort((a,b) => parseInt(a) - parseInt(b)) : [];
  const currentAyahIndex = ayahsList.indexOf(selectedAyah);
  const isFirstAyah = currentAyahIndex <= 0;
  const isLastAyah = currentAyahIndex >= ayahsList.length - 1 || currentAyahIndex === -1;

  const handleNextAyah = () => {
    if (!isLastAyah) {
      setSelectedAyah(ayahsList[currentAyahIndex + 1]);
      setIsAyahFlipped(false);
    }
  };

  const handlePrevAyah = () => {
    if (!isFirstAyah) {
      setSelectedAyah(ayahsList[currentAyahIndex - 1]);
      setIsAyahFlipped(false);
    }
  };

  return (
    <>
      <header className="app-header" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '1rem 1.5rem', maxWidth: '1200px', margin: '0 auto', width: '100%', flexWrap: 'wrap', gap: '1rem' }}>
        <a 
          href="../../../index.html" 
          className="portal-home-btn"
          title="Kembali ke Portal SIMAQ"
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '6px',
            background: 'rgba(255,255,255,0.08)',
            border: '1px solid rgba(255,255,255,0.15)',
            color: '#f8fafc',
            textDecoration: 'none',
            padding: '7px 14px',
            borderRadius: '8px',
            fontSize: '0.85rem',
            fontWeight: 600,
            transition: 'all 0.2s'
          }}
        >
          &larr; Portal SIMAQ
        </a>
        <h1 className="app-title" style={{ margin: 0, fontSize: '1.8rem', letterSpacing: '-0.02em' }}>Mushaf Per Kata</h1>
        <span style={{ fontSize: '0.85rem', color: '#94a3b8', fontWeight: 600, letterSpacing: '0.05em' }}>SIMAQ.CLOUD</span>
      </header>

      <main>
        <div className="controls-container">
          <SurahSelector 
            availableSurahs={availableSurahs}
            selectedSurah={selectedSurah}
            onSelectSurah={handleSelectSurah}
          />
          
          <AyahSelector 
            availableAyahs={availableAyahs}
            selectedAyah={selectedAyah}
            onSelectAyah={handleSelectAyah}
          />
          
          <ColumnSelector 
            visibleColumns={visibleColumns}
            onToggle={handleToggleColumn}
          />
        </div>

        <section className="results-section">
          {loadingSurah && <div className="loader"></div>}
          
          {!loadingSurah && selectedSurah && selectedAyah && (
            <div>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '1rem', marginBottom: '1.5rem' }}>
                <h3 style={{ margin: 0, fontSize: '1.5rem', color: 'var(--accent-color)' }}>
                  Surat {selectedSurah}, Ayat {selectedAyah}
                </h3>
                {selectedSurah && selectedAyah && (
                  <audio 
                    id="main-ayah-audio"
                    controls 
                    src={`https://everyayah.com/data/Alafasy_128kbps/${String(selectedSurah).padStart(3, '0')}${String(selectedAyah).padStart(3, '0')}.mp3`}
                    style={{ height: '36px' }}
                  >
                    Your browser does not support the audio element.
                  </audio>
                )}
              </div>
              
              {currentAyahData.length > 0 && (
                <div 
                  className={`flip-container ${isAyahFlipped ? 'flipped' : ''}`} 
                  onClick={() => setIsAyahFlipped(!isAyahFlipped)}
                  style={{ 
                    cursor: 'pointer', 
                    margin: '0 auto 2.5rem auto', 
                    maxWidth: '800px',
                    display: 'block'
                  }}
                  title="Klik untuk melihat terjemahan ayat"
                >
                  <div className="flip-inner" style={{ padding: '0', borderRadius: '12px' }}>
                    <div className="flip-front glass" style={{ padding: '1.5rem 2rem', color: 'white', fontSize: '2rem', lineHeight: '2.2', textAlign: 'center', fontFamily: '"Amiri Quran", serif' }} dir="rtl">
                      {currentAyahData.map(w => w['Lafdz']).join(' ')}
                    </div>
                    <div className="flip-back glass" style={{ padding: '1.5rem 2rem', color: '#fde047', fontSize: '1.15rem', lineHeight: '1.6', textAlign: 'center', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: '500' }}>
                      {currentAyahData
                        .map(w => String(w['Terjemah'] || '').replace(/\s*\[.*?\]\s*/g, ' ').trim())
                        .filter(t => t.length > 0)
                        .join(' ')
                        .replace(/\s+([,;.])/g, '$1')
                        .replace(/\s+/g, ' ')}
                    </div>
                  </div>
                </div>
              )}
              
              {currentAyahData.length === 0 ? (
                <p style={{ textAlign: 'center', color: 'var(--text-secondary)' }}>Tidak ada data untuk ayat ini.</p>
              ) : (
                <WordTable data={currentAyahData} visibleColumns={visibleColumns} />
              )}
              
              <div style={{ display: 'flex', justifyContent: 'center', gap: '1rem', marginTop: '1.5rem', marginBottom: '1.5rem' }}>
                <button 
                  onClick={handlePrevAyah} 
                  disabled={isFirstAyah}
                  className="nav-btn"
                  style={{
                    padding: '0.5rem 1rem',
                    background: isFirstAyah ? 'rgba(255,255,255,0.1)' : 'var(--accent-color)',
                    color: isFirstAyah ? 'var(--text-secondary)' : '#0f172a',
                    border: 'none',
                    borderRadius: '8px',
                    cursor: isFirstAyah ? 'not-allowed' : 'pointer',
                    fontWeight: '600',
                    transition: 'all 0.2s'
                  }}
                >
                  &laquo; Ayat Sebelumnya
                </button>
                <button 
                  onClick={handleNextAyah} 
                  disabled={isLastAyah}
                  className="nav-btn"
                  style={{
                    padding: '0.5rem 1rem',
                    background: isLastAyah ? 'rgba(255,255,255,0.1)' : 'var(--accent-color)',
                    color: isLastAyah ? 'var(--text-secondary)' : '#0f172a',
                    border: 'none',
                    borderRadius: '8px',
                    cursor: isLastAyah ? 'not-allowed' : 'pointer',
                    fontWeight: '600',
                    transition: 'all 0.2s'
                  }}
                >
                  Ayat Selanjutnya &raquo;
                </button>
              </div>
            </div>
          )}
        </section>
      </main>
    </>
  );
}

export default App;
