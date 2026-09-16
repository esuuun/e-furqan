import React from 'react';

function AyahSelector({ availableAyahs, selectedAyah, onSelectAyah }) {
  if (!availableAyahs || availableAyahs.length === 0) {
    return (
      <div className="selector-section glass" style={{ opacity: 0.5 }}>
        <h2 className="selector-title">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
          Pilih Ayat
        </h2>
        <p style={{ color: 'var(--text-secondary)' }}>Silakan pilih surat terlebih dahulu.</p>
      </div>
    );
  }

  // Sort numerically
  const sortedAyahs = [...availableAyahs].sort((a, b) => parseInt(a) - parseInt(b));

  return (
    <div className="selector-section glass">
      <h2 className="selector-title">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
        Pilih Ayat
      </h2>
      <div className="custom-select-wrapper">
        <select
          className="custom-select"
          value={selectedAyah || ""}
          onChange={(e) => onSelectAyah(e.target.value)}
        >
          <option value="" disabled>-- Pilih Ayat --</option>
          {sortedAyahs.map((ayahId) => (
            <option key={ayahId} value={ayahId}>
              Ayat {ayahId}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
}

export default AyahSelector;
