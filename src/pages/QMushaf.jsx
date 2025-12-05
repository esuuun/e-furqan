import React, { useState, useEffect, useMemo } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import SurahSelector from "../components/qtahfidz/SurahSelector";
import AyatSelector from "../components/qtahfidz/AyatSelector";

const QMushaf = () => {
  const [csvData, setCsvData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedSurah, setSelectedSurah] = useState(1);
  const [selectedAyat, setSelectedAyat] = useState(null);
  const [surahInfo, setSurahInfo] = useState(null);

  // Fetch and parse CSV
  useEffect(() => {
    fetch("/Master Mushaf.csv")
      .then((response) => response.text())
      .then((text) => {
        const rows = text.split("\n").slice(1); // Skip header
        const parsedData = rows
          .map((row) => {
            // Regex to split by comma ignoring quotes
            const cols = row.split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/);
            if (cols.length < 12) return null;
            return {
              arti: cols[1]?.replace(/^"|"$/g, ""),
              ilal: cols[2],
              bentuk_kata: cols[3],
              irab: cols[4]?.replace(/^"|"$/g, ""),
              pola_irab: cols[5],
              arti_akar: cols[6],
              akar: cols[7],
              akhiran: cols[8],
              awalan: cols[9],
              mushaf: cols[10],
              surat: parseInt(cols[11]),
              ayat: parseInt(cols[12]),
            };
          })
          .filter((row) => row && row.surat);
        setCsvData(parsedData);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error loading CSV:", err);
        setLoading(false);
      });
  }, []);

  // Fetch Surah Info (for name, etc)
  useEffect(() => {
    if (selectedSurah) {
      fetch(`https://quran-api.santrikoding.com/api/surah/${selectedSurah}`)
        .then((res) => res.json())
        .then((data) => setSurahInfo(data));
    }
  }, [selectedSurah]);

  const filteredData = useMemo(() => {
    if (!csvData.length) return {};

    const surahWords = csvData.filter(
      (row) =>
        row.surat === selectedSurah &&
        !/^\d+$/.test(row.arti) && // Filter out verse numbers in meaning
        !/^\d+$/.test(row.mushaf) // Filter out verse numbers in arabic text
    );

    // Group by Ayat
    const verses = {};
    surahWords.forEach((word) => {
      if (!verses[word.ayat]) verses[word.ayat] = [];
      verses[word.ayat].push(word);
    });

    return verses;
  }, [csvData, selectedSurah]);

  const handleSelectSurah = (id) => {
    setSelectedSurah(id);
    setSelectedAyat(null);
  };

  return (
    <div className="min-h-screen flex flex-col bg-white font-sans">
      <Navbar />

      {/* Hero / Header */}
      <div className="relative bg-linear-to-br from-emerald-50 via-white to-teal-50 pt-32 pb-12">
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          <div className="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-emerald-100 rounded-full blur-3xl opacity-50"></div>
          <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-80 h-80 bg-teal-100 rounded-full blur-3xl opacity-50"></div>
        </div>

        <div className="container mx-auto px-6 relative z-10 text-center">
          <div className="inline-block px-4 py-1.5 mb-6 bg-emerald-100 text-emerald-700 rounded-full text-sm font-semibold tracking-wide">
            📖 qMushaf Digital
          </div>
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 leading-tight mb-6">
            Analisis Kata per Kata <br />
            <span className="text-transparent bg-clip-text bg-linear-to-r from-emerald-600 to-teal-600">
              Al-Qur'an
            </span>
          </h1>
          <p className="text-lg text-gray-600 mb-8 leading-relaxed max-w-2xl mx-auto">
            Pelajari struktur bahasa, akar kata, dan terjemahan setiap lafadz
            dalam Al-Qur'an secara mendalam.
          </p>

          <div className="bg-white p-4 rounded-2xl shadow-xl border border-gray-100 max-w-3xl mx-auto flex flex-col md:flex-row gap-4">
            <div className="flex-1">
              <SurahSelector
                selectedSurah={selectedSurah}
                onSelectSurah={handleSelectSurah}
              />
            </div>
            <div className="w-full md:w-48">
              <AyatSelector
                totalAyat={surahInfo ? surahInfo.jumlah_ayat : 0}
                selectedAyat={selectedAyat}
                onSelectAyat={setSelectedAyat}
                disabled={!surahInfo}
              />
            </div>
          </div>
        </div>
      </div>

      <main className="grow container mx-auto px-6 py-12">
        {loading ? (
          <div className="text-center py-20">
            <div className="inline-block animate-spin rounded-full h-8 w-8 border-4 border-emerald-500 border-t-transparent"></div>
            <p className="mt-4 text-gray-500">Memuat data Mushaf...</p>
            <p className="text-xs text-gray-400 mt-2">
              (Proses ini mungkin memakan waktu beberapa detik karena memuat
              database kata)
            </p>
          </div>
        ) : (
          <div className="space-y-12 max-w-5xl mx-auto">
            {Object.entries(filteredData).map(([ayatNum, words]) => {
              if (selectedAyat && parseInt(ayatNum) !== selectedAyat)
                return null;

              return (
                <div
                  key={ayatNum}
                  className="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden"
                >
                  <div className="bg-gray-50 px-6 py-4 border-b border-gray-100 flex items-center gap-3">
                    <span className="bg-emerald-100 text-emerald-700 text-xs font-bold px-3 py-1 rounded-full">
                      Ayat {ayatNum}
                    </span>
                    <span className="text-gray-500 text-sm font-medium">
                      {surahInfo?.nama_latin}
                    </span>
                  </div>

                  <div className="p-8">
                    {/* Arabic Text Full */}
                    <div className="text-right mb-10" dir="rtl">
                      <p className="text-4xl font-arabic leading-loose text-gray-800">
                        {words.map((w) => w.mushaf).join(" ")}
                      </p>
                    </div>

                    {/* Word Analysis Grid */}
                    <div
                      className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6"
                      dir="rtl"
                    >
                      {words.map((word, idx) => (
                        <div
                          key={idx}
                          className="bg-white border border-gray-200 rounded-2xl p-6 hover:border-emerald-400 hover:shadow-lg transition-all group"
                        >
                          {/* Card Header */}
                          <div className="flex justify-between items-center mb-6 border-b border-gray-100 pb-4">
                            <span className="bg-emerald-600 text-white text-sm font-bold px-3 py-1 rounded-lg shadow-sm shadow-emerald-200">
                              #{idx + 1}
                            </span>
                            <span className="text-sm text-emerald-600 font-bold">
                              Surah {word.surat}, Ayat {word.ayat}
                            </span>
                          </div>

                          {/* Arabic Word */}
                          <div className="text-center mb-8">
                            <p className="text-5xl font-arabic text-gray-800 leading-relaxed group-hover:text-emerald-600 transition-colors drop-shadow-sm">
                              {word.mushaf}
                            </p>
                          </div>

                          {/* Details Grid */}
                          <div className="grid grid-cols-2 gap-3">
                            <div className="bg-gray-50 p-3 rounded-xl">
                              <p className="text-[10px] text-gray-400 uppercase font-bold tracking-wider mb-1">
                                Awalan
                              </p>
                              <p className="text-gray-800 font-medium text-sm font-arabic">
                                {word.awalan === "*" ? "-" : word.awalan}
                              </p>
                            </div>
                            <div className="bg-gray-50 p-3 rounded-xl">
                              <p className="text-[10px] text-gray-400 uppercase font-bold tracking-wider mb-1">
                                Akhiran
                              </p>
                              <p className="text-gray-800 font-medium text-sm font-arabic">
                                {word.akhiran === "*" ? "-" : word.akhiran}
                              </p>
                            </div>

                            <div className="bg-gray-50 p-3 rounded-xl">
                              <p className="text-[10px] text-gray-400 uppercase font-bold tracking-wider mb-1">
                                Akar Kata
                              </p>
                              <p className="text-gray-800 font-medium text-lg font-arabic">
                                {word.akar === "*" ? "-" : word.akar}
                              </p>
                            </div>
                            <div className="bg-gray-50 p-3 rounded-xl">
                              <p className="text-[10px] text-gray-400 uppercase font-bold tracking-wider mb-1">
                                Arti Akar
                              </p>
                              <p className="text-gray-800 font-medium text-sm wrap-break-word">
                                {word.arti_akar || "-"}
                              </p>
                            </div>

                            <div className="bg-gray-50 p-3 rounded-xl">
                              <p className="text-[10px] text-gray-400 uppercase font-bold tracking-wider mb-1">
                                Pola I'rab
                              </p>
                              <p className="text-gray-800 font-medium text-lg font-arabic wrap-break-word">
                                {word.pola_irab || "-"}
                              </p>
                            </div>
                            <div className="bg-gray-50 p-3 rounded-xl">
                              <p className="text-[10px] text-gray-400 uppercase font-bold tracking-wider mb-1">
                                I'rab
                              </p>
                              <p className="text-gray-800 font-medium text-sm wrap-break-word">
                                {word.irab || "-"}
                              </p>
                            </div>

                            <div className="bg-gray-50 p-3 rounded-xl">
                              <p className="text-[10px] text-gray-400 uppercase font-bold tracking-wider mb-1">
                                Bentuk Kata
                              </p>
                              <p className="text-gray-800 font-medium text-sm wrap-break-word">
                                {word.bentuk_kata || "-"}
                              </p>
                            </div>
                            <div className="bg-gray-50 p-3 rounded-xl">
                              <p className="text-[10px] text-gray-400 uppercase font-bold tracking-wider mb-1">
                                I'lal
                              </p>
                              <p className="text-gray-800 font-medium text-sm wrap-break-word">
                                {word.ilal || "-"}
                              </p>
                            </div>

                            <div className="col-span-2 bg-emerald-50 p-4 rounded-xl border border-emerald-100">
                              <p className="text-[10px] text-emerald-600 uppercase font-bold tracking-wider mb-1">
                                Arti Kata
                              </p>
                              <p className="text-gray-900 font-bold text-base">
                                {word.arti}
                              </p>
                            </div>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </main>
      <Footer />
    </div>
  );
};

export default QMushaf;
