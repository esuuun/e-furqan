import React from "react";

const AyatSelector = ({ totalAyat, selectedAyat, onSelectAyat, disabled }) => {
  return (
    <div>
      <label className="block text-sm font-medium text-gray-700 mb-2">
        Pilih Ayat
      </label>
      <select
        value={selectedAyat || ""}
        onChange={(e) =>
          onSelectAyat(e.target.value ? Number(e.target.value) : null)
        }
        disabled={disabled}
        className="w-full px-4 py-3 bg-white border border-gray-200 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition-all disabled:bg-gray-50 disabled:text-gray-400 appearance-none cursor-pointer"
        style={{
          backgroundImage: `url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%236b7280' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3e%3c/svg%3e")`,
          backgroundPosition: "right 0.75rem center",
          backgroundRepeat: "no-repeat",
          backgroundSize: "1.5em 1.5em",
          paddingRight: "2.5rem",
        }}
      >
        <option value="">Semua Ayat</option>
        {Array.from({ length: totalAyat }, (_, i) => i + 1).map((num) => (
          <option key={num} value={num}>
            Ayat {num}
          </option>
        ))}
      </select>
    </div>
  );
};

export default AyatSelector;
