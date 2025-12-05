import React, { useState, useEffect, useRef } from "react";

const AyatCard = ({ surahNumber, ayatNumber, ayatText, surahName }) => {
  const [mode, setMode] = useState("display"); // 'display', 'quiz', 'success'
  const [segments, setSegments] = useState([]);
  const [currentSegmentIndex, setCurrentSegmentIndex] = useState(0);
  const [shuffledWords, setShuffledWords] = useState([]);
  const [containerWords, setContainerWords] = useState([]);
  const [feedback, setFeedback] = useState(null); // { type: 'success' | 'error', message: '' }
  const audioRef = useRef(null);

  const surahNoPadded = String(surahNumber).padStart(3, "0");
  const ayatNoPadded = String(ayatNumber).padStart(3, "0");
  const audioSrc = `https://everyayah.com/data/Alafasy_64kbps/${surahNoPadded}${ayatNoPadded}.mp3`;

  // Reload audio when source changes
  useEffect(() => {
    if (audioRef.current) {
      audioRef.current.load();
    }
  }, [audioSrc]);

  const handlePlayAudio = () => {
    if (audioRef.current) {
      audioRef.current.currentTime = 0;
      audioRef.current.play();
    }
  };

  const handleStartQuiz = () => {
    // Tokenize logic
    const rawTokens = ayatText
      .split(/[\s\u0020\u00A0\u1680\u2000-\u200B\u202F\u205F\u3000]+/)
      .filter((word) => word.trim().length > 0);

    const normalizeTokens = (tokens) => {
      const out = [];
      const getCleanLength = (text) => {
        return text.replace(/[\u064B-\u065F\u0670]/g, "").length;
      };

      for (let i = 0; i < tokens.length; i++) {
        let t = tokens[i];
        const cleanLen = getCleanLength(t);
        if (cleanLen === 1 && i + 1 < tokens.length) {
          tokens[i + 1] = t + " " + tokens[i + 1];
        } else {
          out.push(t);
        }
      }
      return out;
    };

    const tokens = normalizeTokens(rawTokens);

    let newSegments = [];
    if (tokens.length > 15) {
      const mid = Math.ceil(tokens.length / 2);
      newSegments = [tokens.slice(0, mid), tokens.slice(mid)];
    } else {
      newSegments = [tokens];
    }

    setSegments(newSegments);
    setCurrentSegmentIndex(0);
    setMode("quiz");
    prepareSegment(newSegments[0]);
  };

  const prepareSegment = (segmentTokens) => {
    const shuffled = shuffleArray([...segmentTokens]);
    setShuffledWords(
      shuffled.map((word, idx) => ({ id: `word-${idx}`, text: word }))
    );
    setContainerWords([]);
    setFeedback(null);
  };

  const shuffleArray = (array) => {
    const newArray = [...array];
    for (let i = newArray.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
    }
    return newArray;
  };

  // Drag and Drop Handlers
  const handleDragStart = (e, word, source, index) => {
    e.dataTransfer.setData(
      "text/plain",
      JSON.stringify({ word, source, index })
    );
    e.dataTransfer.effectAllowed = "move";
  };

  const handleDrop = (e, targetSource, targetIndex = null) => {
    e.preventDefault();
    e.stopPropagation();
    const data = e.dataTransfer.getData("text/plain");
    if (!data) return;

    const { word, source, index: sourceIndex } = JSON.parse(data);

    if (source === targetSource && source === "pool") return;

    if (source === "pool" && targetSource === "container") {
      setShuffledWords((prev) => prev.filter((w) => w.id !== word.id));
      setContainerWords((prev) => {
        const newWords = [...prev];
        if (targetIndex !== null && targetIndex !== undefined) {
          newWords.splice(targetIndex, 0, word);
        } else {
          newWords.push(word);
        }
        return newWords;
      });
    } else if (source === "container" && targetSource === "pool") {
      setContainerWords((prev) => prev.filter((w) => w.id !== word.id));
      setShuffledWords((prev) => [...prev, word]);
    } else if (source === "container" && targetSource === "container") {
      if (sourceIndex === targetIndex) return;

      setContainerWords((prev) => {
        const newWords = [...prev];
        const [movedWord] = newWords.splice(sourceIndex, 1);

        if (targetIndex === null || targetIndex === undefined) {
          newWords.push(movedWord);
        } else {
          let insertPos = targetIndex;
          if (sourceIndex < targetIndex) {
            insertPos -= 1;
          }
          newWords.splice(insertPos, 0, movedWord);
        }
        return newWords;
      });
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleCheckAnswer = () => {
    const currentSegment = segments[currentSegmentIndex];
    const currentAnswer = currentSegment.join(" ");
    const userAnswer = containerWords.map((w) => w.text).join(" ");

    if (userAnswer === currentAnswer) {
      setFeedback({ type: "success", message: "Benar!" });

      if (currentSegmentIndex < segments.length - 1) {
        // Next segment
        setTimeout(() => {
          setCurrentSegmentIndex((prev) => prev + 1);
          prepareSegment(segments[currentSegmentIndex + 1]);
        }, 1500);
      } else {
        // Finished
        setMode("success");
      }
    } else {
      setFeedback({ type: "error", message: "Coba lagi ya" });
    }
  };

  const handleRetry = () => {
    const currentSegment = segments[currentSegmentIndex];
    prepareSegment(currentSegment);
  };

  const handleReset = () => {
    setMode("display");
    setSegments([]);
    setCurrentSegmentIndex(0);
    setShuffledWords([]);
    setContainerWords([]);
    setFeedback(null);
  };

  return (
    <div className="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-md transition-shadow duration-300">
      {/* Header */}
      <div className="bg-gray-50 px-6 py-4 border-b border-gray-100 flex justify-between items-center">
        <div className="flex items-center gap-3">
          <span className="bg-emerald-100 text-emerald-700 text-xs font-bold px-3 py-1 rounded-full">
            Ayat {ayatNumber}
          </span>
          <span className="text-gray-500 text-sm font-medium">{surahName}</span>
        </div>
      </div>

      <div className="p-8">
        <audio ref={audioRef} src={audioSrc} className="hidden" />

        {/* Display Mode */}
        {mode === "display" && (
          <div className="text-center">
            <div
              className="text-4xl leading-loose font-arabic mb-8 text-gray-800"
              dir="rtl"
            >
              {ayatText}
            </div>

            <div className="flex justify-center gap-4">
              <button
                onClick={handlePlayAudio}
                className="flex items-center px-6 py-2.5 bg-white border border-gray-200 text-gray-700 rounded-full font-medium hover:bg-gray-50 transition shadow-sm"
              >
                <span className="mr-2">🔊</span> Dengarkan
              </button>
              <button
                onClick={handleStartQuiz}
                className="flex items-center px-6 py-2.5 bg-emerald-600 text-white rounded-full font-medium hover:bg-emerald-700 transition shadow-lg shadow-emerald-600/20"
              >
                <span className="mr-2">🎯</span> Mulai Latihan
              </button>
            </div>
          </div>
        )}

        {/* Quiz Mode */}
        {mode === "quiz" && (
          <div>
            <div className="text-center mb-6">
              <span className="inline-block px-3 py-1 bg-blue-50 text-blue-600 rounded-full text-xs font-semibold mb-2">
                Bagian {currentSegmentIndex + 1} dari {segments.length}
              </span>
              <p className="text-gray-600 text-sm">
                Susun kata-kata di bawah ini sesuai urutan ayat.
              </p>
              <button
                onClick={handlePlayAudio}
                className="mt-3 inline-flex items-center px-4 py-1.5 bg-emerald-50 text-emerald-700 rounded-full text-sm font-medium hover:bg-emerald-100 transition"
              >
                <span className="mr-1.5">🔊</span> Dengarkan
              </button>
            </div>

            {/* Drop Zone */}
            <div
              onDrop={(e) => handleDrop(e, "container")}
              onDragOver={handleDragOver}
              className="min-h-[120px] bg-gray-50 border-2 border-dashed border-gray-300 rounded-xl p-6 mb-8 flex flex-wrap gap-3 justify-center items-center transition-colors hover:border-emerald-400 hover:bg-emerald-50/30"
              dir="rtl"
            >
              {containerWords.length === 0 && (
                <span className="text-gray-400 text-sm pointer-events-none">
                  Tarik kata ke sini
                </span>
              )}
              {containerWords.map((word, index) => (
                <div
                  key={word.id}
                  draggable
                  onDragStart={(e) =>
                    handleDragStart(e, word, "container", index)
                  }
                  onDrop={(e) => handleDrop(e, "container", index)}
                  onDragOver={(e) => e.preventDefault()}
                  className="bg-white border border-gray-200 shadow-sm px-4 py-2 rounded-lg text-xl font-arabic cursor-grab active:cursor-grabbing hover:border-emerald-500 transition-colors"
                >
                  {word.text}
                </div>
              ))}
            </div>

            {/* Word Pool */}
            <div
              onDrop={(e) => handleDrop(e, "pool")}
              onDragOver={handleDragOver}
              className="flex flex-wrap gap-3 justify-center mb-8"
              dir="rtl"
            >
              {shuffledWords.map((word, index) => (
                <div
                  key={word.id}
                  draggable
                  onDragStart={(e) => handleDragStart(e, word, "pool", index)}
                  className="bg-white border border-gray-200 shadow-sm px-4 py-2 rounded-lg text-xl font-arabic cursor-grab active:cursor-grabbing hover:border-emerald-500 transition-colors"
                >
                  {word.text}
                </div>
              ))}
            </div>

            {/* Controls */}
            <div className="flex flex-col items-center gap-4">
              {feedback && (
                <div
                  className={`text-lg font-bold ${
                    feedback.type === "success"
                      ? "text-emerald-600"
                      : "text-red-500"
                  }`}
                >
                  {feedback.message}
                </div>
              )}

              <div className="flex gap-3">
                <button
                  onClick={handleReset}
                  className="px-6 py-2.5 text-gray-500 hover:text-gray-700 font-medium transition"
                >
                  Batal
                </button>

                {feedback?.type === "error" && (
                  <button
                    onClick={handleRetry}
                    className="px-6 py-2.5 bg-yellow-500 text-white rounded-full font-bold hover:bg-yellow-600 transition shadow-lg shadow-yellow-500/20"
                  >
                    Ulangi
                  </button>
                )}
                <button
                  onClick={handleCheckAnswer}
                  className="px-8 py-2.5 bg-emerald-600 text-white rounded-full font-bold hover:bg-emerald-700 transition shadow-lg shadow-emerald-600/20"
                >
                  Cek Jawaban
                </button>
              </div>
            </div>
          </div>
        )}

        {/* Success Mode */}
        {mode === "success" && (
          <div className="text-center py-8">
            <div className="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto mb-4 text-3xl">
              🎉
            </div>
            <h3 className="text-2xl font-bold text-gray-900 mb-2">Benar!</h3>
            <p className="text-gray-600 mb-8">
              Kamu berhasil menyusun ayat ini dengan benar.
            </p>

            <div
              className="text-3xl leading-loose font-arabic mb-8 text-emerald-800"
              dir="rtl"
            >
              {ayatText}
            </div>

            <button
              onClick={handleReset}
              className="px-8 py-3 bg-emerald-600 text-white rounded-full font-bold hover:bg-emerald-700 transition shadow-lg shadow-emerald-600/20"
            >
              Ulangi Latihan
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default AyatCard;
