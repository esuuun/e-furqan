import React, { useState, useRef, useEffect } from "react";

const SurahSelectorLocal = ({ surahs, selectedSurahId, onSelectSurah }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [search, setSearch] = useState("");
  const dropdownRef = useRef(null);

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
      surah.transliteration.toLowerCase().includes(search.toLowerCase()) ||
      surah.name.includes(search)
  );

  const selectedSurah = surahs.find((s) => s.id === selectedSurahId);

  return (
    <div className="relative" ref={dropdownRef}>
      <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
        Pilih Surah
      </label>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-full flex items-center justify-between px-4 py-3 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl shadow-sm hover:border-yellow-500 dark:hover:border-yellow-500 focus:outline-none focus:ring-2 focus:ring-yellow-500/20 transition-all text-left"
      >
        <span className="block truncate text-gray-700 dark:text-gray-300 font-medium">
          {selectedSurah
            ? `${selectedSurah.id}. ${selectedSurah.transliteration} (${selectedSurah.name})`
            : "Pilih Surah..."}
        </span>
        <svg
          className={`w-5 h-5 text-gray-400 dark:text-gray-500 transition-transform ${
            isOpen ? "rotate-180" : ""
          }`}
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M19 9l-7 7-7-7"
          />
        </svg>
      </button>

      {isOpen && (
        <div className="absolute z-50 w-full mt-2 bg-white dark:bg-gray-800 rounded-xl shadow-lg border border-gray-100 dark:border-gray-700 max-h-96 overflow-hidden flex flex-col">
          <div className="p-3 border-b border-gray-100 dark:border-gray-700 bg-gray-50 dark:bg-gray-700">
            <div className="relative">
              <input
                type="text"
                className="w-full pl-10 pr-4 py-2 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-600 rounded-lg text-sm text-gray-900 dark:text-white focus:outline-none focus:border-yellow-500 focus:ring-1 focus:ring-yellow-500"
                placeholder="Cari surah..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                autoFocus
              />
              <svg
                className="absolute left-3 top-2.5 w-4 h-4 text-gray-400 dark:text-gray-500"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                />
              </svg>
            </div>
          </div>

          <div className="overflow-y-auto flex-1">
            {filteredSurahs.length > 0 ? (
              filteredSurahs.map((surah) => (
                <button
                  key={surah.id}
                  onClick={() => {
                    onSelectSurah(surah.id);
                    setIsOpen(false);
                    setSearch("");
                  }}
                  className={`w-full px-4 py-3 text-left hover:bg-yellow-50 dark:hover:bg-yellow-900/30 transition-colors flex items-center justify-between group ${
                    selectedSurahId === surah.id
                      ? "bg-yellow-50 dark:bg-yellow-900/30"
                      : ""
                  }`}
                >
                  <div className="flex items-center gap-3">
                    <span
                      className={`w-8 h-8 flex items-center justify-center rounded-full text-xs font-bold ${
                        selectedSurahId === surah.id
                          ? "bg-yellow-500 text-white"
                          : "bg-gray-100 dark:bg-gray-700 text-gray-500 dark:text-gray-400 group-hover:bg-yellow-200 dark:group-hover:bg-yellow-900/50 group-hover:text-yellow-700 dark:group-hover:text-yellow-300"
                      }`}
                    >
                      {surah.id}
                    </span>
                    <div>
                      <p
                        className={`font-medium ${
                          selectedSurahId === surah.id
                            ? "text-yellow-700 dark:text-yellow-400"
                            : "text-gray-700 dark:text-gray-300"
                        }`}
                      >
                        {surah.transliteration}
                      </p>
                      <p className="text-xs text-gray-500 dark:text-gray-400">
                        {surah.total_verses} Ayat • {surah.type}
                      </p>
                    </div>
                  </div>
                  <span className="font-arabic text-lg text-gray-400 dark:text-gray-500 group-hover:text-yellow-600 dark:group-hover:text-yellow-400">
                    {surah.name}
                  </span>
                </button>
              ))
            ) : (
              <div className="p-4 text-center text-gray-500 dark:text-gray-400 text-sm">
                Surah tidak ditemukan
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default SurahSelectorLocal;
