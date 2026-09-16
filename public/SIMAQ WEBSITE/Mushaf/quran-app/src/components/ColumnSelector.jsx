import React from 'react';

const columnsList = [
  { id: 'kataAkar', label: 'Kata/Akar' },
  { id: 'bentuk', label: 'Bentuk Kata' },
  { id: 'terjemah', label: 'Terjemah' },
];

function ColumnSelector({ visibleColumns, onToggle }) {
  return (
    <div className="selector-section glass">
      <h2 className="selector-title">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 3h7a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-7m0-18H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h7m0-18v18"/></svg>
        Tampilkan Kolom
      </h2>
      <div className="custom-select-wrapper">
        <details className="column-dropdown" style={{ width: '100%' }}>
          <summary className="custom-select" style={{ cursor: 'pointer', listStyle: 'none' }}>
            Pilih Kolom ▾
          </summary>
          <div className="dropdown-menu glass" style={{ width: '100%' }}>
            {columnsList.map(col => (
              <label key={col.id} className="dropdown-item">
                <input 
                  type="checkbox" 
                  checked={visibleColumns[col.id] || false} 
                  onChange={() => onToggle(col.id)} 
                />
                {col.label}
              </label>
            ))}
          </div>
        </details>
      </div>
    </div>
  );
}

export default ColumnSelector;
