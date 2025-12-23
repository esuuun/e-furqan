import React, { useState, useEffect } from "react";

const AyatGridSelector = ({ surah, selectedAyahs, onSelectionChange }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [search, setSearch] = useState("");

  // Helper to check if all are selected
  const isAllSelected = surah && selectedAyahs.length === surah.verses.length;

  const toggleOpen = () => setIsOpen(!isOpen);

  const filteredVerses = surah
    ? surah.verses.filter((verse) => verse.id.toString().includes(search))
    : [];

  const handleSelectAll = (e) => {
    if (e.target.checked) {
      onSelectionChange(surah.verses.map((v) => v.id));
    } else {
      onSelectionChange([]);
    }
  };

  const handleSelectOne = (id) => {
    if (selectedAyahs.includes(id)) {
      onSelectionChange(selectedAyahs.filter((aid) => aid !== id));
    } else {
      onSelectionChange([...selectedAyahs, id].sort((a, b) => a - b));
    }
  };

  // Close when clicking outside (simple implementation)
  useEffect(() => {
    const closeDropdown = (e) => {
      if (isOpen && !e.target.closest(".ayah-selector-container")) {
        setIsOpen(false);
      }
    };
    document.addEventListener("click", closeDropdown);
    return () => document.removeEventListener("click", closeDropdown);
  }, [isOpen]);

  if (!surah) return null;

  return (
    <div className="relative ayah-selector-container">
      <label className="block text-sm font-medium text-gray-700 mb-2">
        Pilih Ayat
      </label>
      <button
        onClick={toggleOpen}
        className="w-full flex items-center justify-between px-4 py-3 bg-white border border-gray-200 rounded-xl shadow-sm hover:border-emerald-500 focus:outline-none focus:ring-2 focus:ring-emerald-500/20 transition-all text-left"
      >
        <span className="block truncate text-gray-700 font-medium">
          {selectedAyahs.length === surah.verses.length
            ? "Semua Ayat"
            : selectedAyahs.length === 0
            ? "Pilih Ayat..."
            : `${selectedAyahs.length} Ayat Terpilih`}
        </span>
        <svg
          className={`w-5 h-5 text-gray-400 transition-transform ${
            isOpen ? "rotate-180" : ""
          }`}
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M19 9l-7 7-7-7"
          />
        </svg>
      </button>

      {isOpen && (
        <div className="absolute top-full left-0 right-0 mt-2 w-full bg-white rounded-xl shadow-lg border border-gray-100 z-50 overflow-hidden">
          <div className="p-3 border-b border-gray-100 bg-gray-50">
            <input
              type="text"
              placeholder="Cari ayat..."
              className="w-full px-3 py-2 bg-white border border-gray-200 rounded-lg text-sm focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              autoFocus
            />
          </div>

          <div className="p-4">
            <div className="flex items-center justify-between mb-4 pb-2 border-b border-gray-100">
              <label className="flex items-center gap-2 cursor-pointer select-none">
                <input
                  type="checkbox"
                  checked={isAllSelected}
                  onChange={handleSelectAll}
                  className="w-4 h-4 text-emerald-600 rounded focus:ring-emerald-500 border-gray-300"
                />
                <span className="text-sm font-medium text-gray-700">
                  Pilih Semua
                </span>
              </label>
              <button
                onClick={() => setIsOpen(false)}
                className="text-xs text-gray-500 hover:text-emerald-600 font-medium px-2 py-1 rounded hover:bg-gray-50"
              >
                Selesai
              </button>
            </div>

            <div className="grid grid-cols-5 gap-2 max-h-60 overflow-y-auto custom-scrollbar">
              {filteredVerses.map((verse) => (
                <label
                  key={verse.id}
                  className={`
                  flex items-center justify-center p-2 rounded-lg cursor-pointer text-sm font-medium transition-all
                  ${
                    selectedAyahs.includes(verse.id)
                      ? "bg-emerald-100 text-emerald-700 border border-emerald-200"
                      : "bg-gray-50 text-gray-600 border border-gray-100 hover:bg-gray-100"
                  }
                `}
                >
                  <input
                    type="checkbox"
                    className="hidden"
                    checked={selectedAyahs.includes(verse.id)}
                    onChange={() => handleSelectOne(verse.id)}
                  />
                  {verse.id}
                </label>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default AyatGridSelector;
