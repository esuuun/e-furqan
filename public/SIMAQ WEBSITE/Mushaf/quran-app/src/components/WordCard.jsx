import React, { useState } from 'react';

const renderMixedText = (text, forceColor = null) => {
  if (!text) return '';
  const arabicRegex = /([\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+(?:[\s]+[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+)*)/g;
  const shouldHighlight = text.includes('-');
  
  let wordCount = 0;
  // User requested yellow and red colors
  const colors = ['#fde047', '#f87171']; // yellow and red

  return text.split(arabicRegex).map((part, index) => {
    // If it's an Arabic part
    if (part.match(/[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]/)) {
      const color = forceColor ? forceColor : (shouldHighlight ? colors[wordCount % colors.length] : undefined);
      if (shouldHighlight && !forceColor) wordCount++;
      return <span key={index} className="arabic-text-small" dir="rtl" style={color ? {color} : undefined}>{part}</span>;
    }
    
    // For non-Arabic parts, if we need to highlight hyphens
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

function WordCard({ data }) {
  const [showArtiTooltip, setShowArtiTooltip] = useState(false);
  const [showBentukTooltip, setShowBentukTooltip] = useState(false);
  const [showLafdzTooltip, setShowLafdzTooltip] = useState(false);
  // Extract fields with fallback to empty string
  const lafdz = data['Lafdz'] || '';
  const terjemah = data['Terjemah'] || '';
  const bentukKata = data['Bentuk Kata'] || '';
  const teoriIrabWazanIlal = data["Teori/i'rab/Wazan/I'lal"] || '';
  const arti = data['Arti '] || data['Arti'] || '';
  const akar = data['Kata/Akar'] || '';
  const dhamirHarfMuttashil = data['Dhamir Muttashil / Harf Muttashil'] || '';
  return (
    <div className="word-card glass">
      {lafdz && (
        <div 
          className="word-arabic arabic-text" 
          style={{color: 'white', cursor: dhamirHarfMuttashil.trim() ? 'pointer' : 'default', position: 'relative'}}
          onClick={() => {
            if (dhamirHarfMuttashil.trim()) {
              setShowLafdzTooltip(!showLafdzTooltip);
            }
          }}
          title={dhamirHarfMuttashil.trim() ? "Klik untuk melihat Dhamir/Harf Muttashil" : ""}
        >
          {lafdz}
          {!dhamirHarfMuttashil.trim() && <span style={{opacity: 0.3, fontSize: '0.6em', margin: '0 4px', verticalAlign: 'middle'}}>&bull;</span>}
          
          {showLafdzTooltip && dhamirHarfMuttashil && (
            <div className="glass" style={{
              position: 'absolute',
              top: '100%',
              left: '50%',
              transform: 'translateX(-50%)',
              marginTop: '0.25rem',
              padding: '0.5rem 0.75rem',
              borderRadius: '8px',
              zIndex: 20,
              border: '1px solid rgba(255,255,255,0.2)',
              boxShadow: '0 4px 12px rgba(0,0,0,0.5)',
              minWidth: '200px',
              textAlign: 'center'
            }}>
              <div style={{color: 'white', lineHeight: '1.4', fontSize: '1rem', fontFamily: 'system-ui, sans-serif'}} dir="rtl">
                <div style={{fontSize: '0.75rem', opacity: 0.7, marginBottom: '0.25rem', fontFamily: 'system-ui, sans-serif', textAlign: 'center'}}>Dhamir/Harf Muttashil:</div>
                {renderMixedText(dhamirHarfMuttashil, 'white')}
              </div>
            </div>
          )}
        </div>
      )}
      {terjemah && <div className="word-translation" style={{color: '#fde047'}}>{terjemah}</div>}
      
      <div className="word-details">
        {akar && (
          <div className="detail-row" 
               style={{ cursor: 'pointer', position: 'relative' }}
               onClick={() => setShowArtiTooltip(!showArtiTooltip)}
               title="Klik untuk melihat arti">
            <span className="detail-label">Akar Kata</span>
            <span className="detail-value arabic-text" style={{fontSize: '1.2rem', lineHeight: '1.5', color: '#fde047'}}>{renderMixedText(akar, '#fde047')}</span>
            
            {showArtiTooltip && arti && (
              <div className="glass" style={{
                position: 'absolute',
                top: '100%',
                right: '0',
                marginTop: '0.25rem',
                padding: '0.5rem 0.75rem',
                borderRadius: '8px',
                zIndex: 10,
                border: '1px solid rgba(255,255,255,0.2)',
                boxShadow: '0 4px 12px rgba(0,0,0,0.5)',
                minWidth: '150px',
                textAlign: 'right'
              }}>
                <div style={{color: '#fde047', lineHeight: '1.4'}}>{renderMixedText(arti, '#fde047')}</div>
              </div>
            )}
          </div>
        )}
        {bentukKata && (
          <div className="detail-row"
               style={{ cursor: 'pointer', position: 'relative' }}
               onClick={() => setShowBentukTooltip(!showBentukTooltip)}
               title="Klik untuk melihat Teori/I'rab/Wazan/I'lal">
            <span className="detail-label">Bentuk Kata</span>
            <span className="detail-value" style={{color: 'white'}}>{renderMixedText(bentukKata, 'white')}</span>
            
            {showBentukTooltip && teoriIrabWazanIlal && (
              <div className="glass" style={{
                position: 'absolute',
                top: '100%',
                right: '0',
                marginTop: '0.25rem',
                padding: '0.5rem 0.75rem',
                borderRadius: '8px',
                zIndex: 10,
                border: '1px solid rgba(255,255,255,0.2)',
                boxShadow: '0 4px 12px rgba(0,0,0,0.5)',
                minWidth: '200px',
                textAlign: 'right'
              }}>
                <div style={{color: 'white', lineHeight: '1.4'}}>{renderMixedText(teoriIrabWazanIlal, 'white')}</div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default WordCard;
