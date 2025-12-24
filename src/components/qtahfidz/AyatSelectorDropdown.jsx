import React, { useState, useRef, useEffect } from "react";

const AyatSelectorDropdown = ({
  availableAyats,
  selectedAyat,
  onSelectAyat,
  disabled,
}) => {
  const [isOpen, setIsOpen] = useState(false);
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

  const handleSelect = (val) => {
    onSelectAyat(val);
    setIsOpen(false);
  };

  const displayValue =
    selectedAyat === "all" ? "Semua Ayat" : `Ayat ${selectedAyat}`;

  return (
    <div className="relative" ref={dropdownRef}>
      <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
        Pilih Ayat
      </label>
      <button
        onClick={() => !disabled && setIsOpen(!isOpen)}
        disabled={disabled}
        className={`w-full flex items-center justify-between px-4 py-3 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl shadow-sm transition-all text-left ${
          disabled
            ? "bg-gray-50 dark:bg-gray-900 text-gray-400 dark:text-gray-600 cursor-not-allowed"
            : "hover:border-yellow-500 focus:outline-none focus:ring-2 focus:ring-yellow-500/20"
        }`}
      >
        <span className="block truncate font-medium text-gray-700 dark:text-gray-200">
          {disabled ? "Pilih Surah Dulu" : displayValue}
        </span>
        <svg
          className={`w-5 h-5 text-gray-400 transition-transform ${
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

      {isOpen && !disabled && (
        <div className="absolute z-50 w-full mt-2 bg-white dark:bg-gray-800 rounded-xl shadow-lg border border-gray-100 dark:border-gray-700 max-h-60 overflow-y-auto">
          <button
            onClick={() => handleSelect("all")}
            className={`w-full px-4 py-2 text-left hover:bg-yellow-50 dark:hover:bg-gray-700 transition-colors flex items-center justify-between ${
              selectedAyat === "all"
                ? "bg-yellow-50 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-300"
                : "text-gray-700 dark:text-gray-200"
            }`}
          >
            <span className="font-medium">Semua Ayat</span>
            {selectedAyat === "all" && (
              <svg
                className="w-4 h-4 text-yellow-600 dark:text-yellow-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M5 13l4 4L19 7"
                />
              </svg>
            )}
          </button>

          {availableAyats.map((num) => (
            <button
              key={num}
              onClick={() => handleSelect(num)}
              className={`w-full px-4 py-2 text-left hover:bg-yellow-50 dark:hover:bg-gray-700 transition-colors flex items-center justify-between ${
                selectedAyat === num
                  ? "bg-yellow-50 dark:bg-yellow-900 text-yellow-700 dark:text-yellow-300"
                  : "text-gray-700 dark:text-gray-200"
              }`}
            >
              <span>Ayat {num}</span>
              {selectedAyat === num && (
                <svg
                  className="w-4 h-4 text-yellow-600 dark:text-yellow-400"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M5 13l4 4L19 7"
                  />
                </svg>
              )}
            </button>
          ))}
        </div>
      )}
    </div>
  );
};

export default AyatSelectorDropdown;
