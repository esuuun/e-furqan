import React, { useState, useEffect, useRef } from "react";

const SurahSelector = ({ selectedSurah, onSelectSurah }) => {
  const [surahs, setSurahs] = useState([]);
  const [isOpen, setIsOpen] = useState(false);
  const [search, setSearch] = useState("");
  const dropdownRef = useRef(null);

  useEffect(() => {
    fetch("https://quran-api.santrikoding.com/api/surah")
      .then((res) => res.json())
      .then((data) => setSurahs(data))
      .catch((err) => console.error("Failed to fetch surahs", err));
  }, []);

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const filteredSurahs = surahs.filter(
    (surah) =>
      surah.nama_latin.toLowerCase().includes(search.toLowerCase()) ||
      surah.arti.toLowerCase().includes(search.toLowerCase())
  );

  const selectedSurahData = surahs.find((s) => s.nomor === selectedSurah);

  return (
    <div className="relative" ref={dropdownRef}>
      <label className="block text-sm font-medium text-gray-700 mb-2">
        Pilih Surah
      </label>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-full flex items-center justify-between px-4 py-3 bg-white border border-gray-200 rounded-xl shadow-sm hover:border-emerald-500 focus:outline-none focus:ring-2 focus:ring-emerald-500/20 transition-all text-left"
      >
        <span className="block truncate text-gray-700 font-medium">
          {selectedSurahData
            ? `${selectedSurahData.nomor}. ${selectedSurahData.nama_latin}`
            : "Pilih Surah..."}
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
        <div className="absolute z-50 w-full mt-2 bg-white border border-gray-100 rounded-xl shadow-xl max-h-80 overflow-hidden flex flex-col animate-in fade-in zoom-in-95 duration-200">
          <div className="p-3 border-b border-gray-100 bg-gray-50">
            <input
              type="text"
              placeholder="Cari surah..."
              className="w-full px-3 py-2 bg-white border border-gray-200 rounded-lg text-sm focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              autoFocus
            />
          </div>
          <div className="overflow-y-auto p-1">
            {filteredSurahs.length > 0 ? (
              filteredSurahs.map((surah) => (
                <button
                  key={surah.nomor}
                  onClick={() => {
                    onSelectSurah(surah.nomor);
                    setIsOpen(false);
                    setSearch("");
                  }}
                  className={`w-full flex items-center justify-between px-4 py-3 rounded-lg text-left transition-colors ${
                    selectedSurah === surah.nomor
                      ? "bg-emerald-50 text-emerald-700"
                      : "hover:bg-gray-50 text-gray-700"
                  }`}
                >
                  <div>
                    <span className="font-medium">{surah.nama_latin}</span>
                    <span className="text-xs text-gray-500 ml-2">
                      ({surah.arti})
                    </span>
                  </div>
                  <span className="text-xs font-arabic text-gray-400">
                    {surah.nama}
                  </span>
                </button>
              ))
            ) : (
              <div className="px-4 py-3 text-sm text-gray-500 text-center">
                Surah tidak ditemukan
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default SurahSelector;
