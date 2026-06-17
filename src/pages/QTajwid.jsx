import React, { useState, useCallback } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import {
  nunSukunQuiz,
  qalqalahWords,
  alifLamQuiz,
  waqafQuiz,
  hijaiyahLetters,
} from "../data/tajwidData";

// ─── Helpers ──────────────────────────────────────────────────────
function shuffle(arr) {
  return [...arr].sort(() => Math.random() - 0.5);
}

// ─── Game: Huruf Hijaiyah ─────────────────────────────────────────
function HijaiyahGame() {
  const [selected, setSelected] = useState(null);
  const [revealed, setRevealed] = useState(new Set());

  const handleSelect = (l) => {
    setSelected(l === selected ? null : l);
    setRevealed((prev) => new Set([...prev, l.name]));
  };

  return (
    <div>
      <p className="text-center text-gray-500 dark:text-gray-400 text-sm mb-2">
        Klik huruf untuk melihat nama dan makhraj-nya
      </p>
      <div className="flex items-center justify-center gap-2 mb-4">
        <div className="flex-1 max-w-xs bg-gray-200 dark:bg-gray-700 rounded-full h-1.5">
          <div
            className="bg-yellow-500 h-1.5 rounded-full transition-all duration-500"
            style={{ width: `${(revealed.size / hijaiyahLetters.length) * 100}%` }}
          />
        </div>
        <span className="text-xs text-gray-500 dark:text-gray-400">
          {revealed.size}/{hijaiyahLetters.length}
        </span>
      </div>

      <div className="grid grid-cols-6 sm:grid-cols-8 md:grid-cols-10 gap-2 mb-6">
        {hijaiyahLetters.map((letter) => (
          <button
            key={letter.name}
            onClick={() => handleSelect(letter)}
            className={`aspect-square rounded-xl flex items-center justify-center border-2 transition-all duration-200 text-2xl font-arabic relative ${
              selected?.name === letter.name
                ? "border-yellow-500 bg-yellow-50 dark:bg-yellow-900/20 scale-105 shadow-md"
                : revealed.has(letter.name)
                ? "border-yellow-300 dark:border-yellow-700 bg-yellow-50/50 dark:bg-yellow-900/10 text-gray-700 dark:text-gray-300"
                : "border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 text-gray-800 dark:text-gray-200 hover:border-yellow-400 hover:shadow-sm"
            }`}
          >
            {letter.text}
            {revealed.has(letter.name) && selected?.name !== letter.name && (
              <span className="absolute top-0.5 right-0.5 w-1.5 h-1.5 rounded-full bg-yellow-400" />
            )}
          </button>
        ))}
      </div>

      {selected && (
        <div className="bg-yellow-50 dark:bg-yellow-900/10 border border-yellow-200 dark:border-yellow-800 rounded-2xl p-6">
          <div className="flex items-start gap-5">
            <div className="text-7xl font-arabic text-gray-800 dark:text-white bg-white dark:bg-gray-800 rounded-xl w-20 h-20 flex items-center justify-center border border-yellow-200 dark:border-yellow-800 shadow-sm flex-shrink-0">
              {selected.text}
            </div>
            <div>
              <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-1">{selected.name}</h3>
              <p className="text-yellow-600 dark:text-yellow-400 font-mono mb-3">/{selected.romanization}/</p>
              <div className="bg-white dark:bg-gray-800 rounded-xl p-4 border border-gray-100 dark:border-gray-700">
                <p className="text-xs text-gray-400 uppercase tracking-wide mb-1">Makhraj</p>
                <p className="text-gray-700 dark:text-gray-300 text-sm">{selected.makhraj}</p>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

// ─── Generic Multiple-Choice Quiz ─────────────────────────────────
function QuizGame({ questions, accentBg = "bg-yellow-500" }) {
  const [qs] = useState(() => shuffle(questions).slice(0, 8));
  const [cur, setCur] = useState(0);
  const [chosen, setChosen] = useState(null);
  const [score, setScore] = useState(0);
  const [done, setDone] = useState(false);
  const [history, setHistory] = useState([]);

  const q = qs[cur];

  const handleChoose = (opt) => {
    if (chosen) return;
    const correct = opt === q.answer;
    setChosen(opt);
    if (correct) setScore((s) => s + 1);
    setHistory((h) => [...h, { ex: q.example || q.word || q.sign, answer: q.answer, chosen: opt, correct }]);
  };

  const next = () => {
    if (cur + 1 >= qs.length) setDone(true);
    else { setCur((c) => c + 1); setChosen(null); }
  };

  const restart = () => { setCur(0); setChosen(null); setScore(0); setDone(false); setHistory([]); };

  if (done) {
    const pct = Math.round((score / qs.length) * 100);
    return (
      <div className="text-center py-6">
        <div className={`text-6xl font-bold mb-3 ${pct >= 80 ? "text-emerald-600 dark:text-emerald-400" : pct >= 60 ? "text-yellow-600 dark:text-yellow-400" : "text-red-500"}`}>
          {pct}%
        </div>
        <p className="text-gray-900 dark:text-white font-bold text-lg mb-1">
          {pct >= 80 ? "🎉 Luar Biasa!" : pct >= 60 ? "👍 Bagus!" : "📚 Terus Berlatih!"}
        </p>
        <p className="text-gray-500 dark:text-gray-400 mb-6">{score} dari {qs.length} benar</p>
        <div className="space-y-2 mb-6 text-left max-h-40 overflow-y-auto">
          {history.map((h, i) => (
            <div key={i} className={`flex items-center gap-3 p-3 rounded-xl text-sm border ${h.correct ? "bg-emerald-50 dark:bg-emerald-900/10 border-emerald-200 dark:border-emerald-800" : "bg-red-50 dark:bg-red-900/10 border-red-200 dark:border-red-800"}`}>
              <span>{h.correct ? "✅" : "❌"}</span>
              <span className="font-arabic text-xl text-gray-800 dark:text-gray-200">{h.ex}</span>
              <span className="text-gray-500 dark:text-gray-400 text-xs">→ {h.answer}</span>
            </div>
          ))}
        </div>
        <button onClick={restart} className={`px-8 py-3 rounded-xl font-semibold text-white transition ${accentBg} hover:opacity-90`}>
          Ulangi
        </button>
      </div>
    );
  }

  const allOptions = q.options || shuffle([q.answer, ...(q.incorrectAnswers || [])]).slice(0, 4);

  return (
    <div>
      <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-3">
        <span>Soal {cur + 1}/{qs.length}</span>
        <span className="text-emerald-600 dark:text-emerald-400 font-semibold">{score} benar</span>
      </div>
      <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-1.5 mb-6">
        <div className={`h-1.5 rounded-full transition-all ${accentBg}`} style={{ width: `${(cur / qs.length) * 100}%` }} />
      </div>

      <div className="text-center mb-6">
        <div className="text-6xl font-arabic text-gray-900 dark:text-white bg-gray-50 dark:bg-gray-800 rounded-xl py-5 mb-3 border border-gray-100 dark:border-gray-700">
          {q.example || q.word || q.sign}
        </div>
        {q.romanization && <p className="text-gray-400 font-mono text-sm mb-2">/{q.romanization}/</p>}
        <p className="text-gray-700 dark:text-gray-200 font-semibold">{q.question || q.name || `Apa arti tanda "${q.sign}"?`}</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-4">
        {allOptions.map((opt) => {
          let cls = "border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:border-yellow-400 hover:bg-yellow-50 dark:hover:bg-yellow-900/10";
          if (chosen) {
            if (opt === q.answer) cls = "border-emerald-400 bg-emerald-50 dark:bg-emerald-900/20 text-emerald-700 dark:text-emerald-300";
            else if (opt === chosen) cls = "border-red-400 bg-red-50 dark:bg-red-900/20 text-red-700 dark:text-red-300";
            else cls = "border-gray-100 dark:border-gray-800 bg-gray-50 dark:bg-gray-900 text-gray-400 dark:text-gray-600";
          }
          return (
            <button
              key={opt}
              onClick={() => handleChoose(opt)}
              disabled={!!chosen}
              className={`p-4 rounded-xl border-2 text-left font-medium text-sm transition-all disabled:cursor-default ${cls}`}
            >
              {opt}
            </button>
          );
        })}
      </div>

      {chosen && q.explanation && (
        <div className="bg-blue-50 dark:bg-blue-900/10 border border-blue-200 dark:border-blue-800 rounded-xl p-4 mb-4 text-sm text-gray-600 dark:text-gray-300">
          💡 {q.explanation}
        </div>
      )}

      {chosen && (
        <button onClick={next} className={`w-full py-3 rounded-xl font-semibold text-white transition ${accentBg} hover:opacity-90`}>
          {cur + 1 >= qs.length ? "Lihat Hasil" : "Soal Berikutnya →"}
        </button>
      )}
    </div>
  );
}

// ─── Game: Qalqalah ───────────────────────────────────────────────
function QalqalahGame() {
  const [qs] = useState(() => shuffle(qalqalahWords));
  const [cur, setCur] = useState(0);
  const [result, setResult] = useState(null);
  const [score, setScore] = useState(0);
  const [done, setDone] = useState(false);

  const q = qs[cur];

  const handleClick = (part) => {
    if (result) return;
    if (part.isQalqalah) { setResult("correct"); setScore((s) => s + 1); }
    else setResult("wrong");
  };

  const next = () => {
    if (cur + 1 >= qs.length) setDone(true);
    else { setCur((c) => c + 1); setResult(null); }
  };

  const restart = () => { setCur(0); setResult(null); setScore(0); setDone(false); };

  if (done) {
    return (
      <div className="text-center py-6">
        <div className={`text-6xl font-bold mb-3 ${score >= qs.length * 0.8 ? "text-emerald-600" : "text-yellow-600"}`}>
          {Math.round((score / qs.length) * 100)}%
        </div>
        <p className="text-gray-900 dark:text-white font-bold mb-4">{score} dari {qs.length} benar</p>
        <div className="inline-flex gap-2 bg-gray-100 dark:bg-gray-800 rounded-xl p-3 mb-6 text-sm text-gray-600 dark:text-gray-300">
          Huruf Qalqalah: <span className="font-arabic text-lg font-bold text-yellow-600 dark:text-yellow-400">ق ط ب ج د</span>
        </div>
        <div><button onClick={restart} className="px-8 py-3 rounded-xl font-semibold text-white bg-yellow-500 hover:bg-yellow-400 transition">Ulangi</button></div>
      </div>
    );
  }

  return (
    <div>
      <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-3">
        <span>Soal {cur + 1}/{qs.length}</span>
        <span className="text-emerald-600 dark:text-emerald-400 font-semibold">{score} benar</span>
      </div>
      <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-1.5 mb-6">
        <div className="h-1.5 rounded-full bg-yellow-500 transition-all" style={{ width: `${(cur / qs.length) * 100}%` }} />
      </div>

      <p className="text-center text-gray-600 dark:text-gray-400 text-sm mb-5">
        Klik suku kata yang mengandung huruf <span className="font-bold text-gray-900 dark:text-white">Qalqalah</span> (ق ط ب ج د dalam keadaan sukun)
      </p>

      <div className="flex gap-3 justify-center mb-3 flex-wrap">
        {q.parts.map((part, i) => (
          <button
            key={i}
            onClick={() => handleClick(part)}
            disabled={!!result}
            className={`font-arabic text-5xl px-5 py-4 rounded-2xl border-2 transition-all disabled:cursor-default ${
              result && part.isQalqalah ? "border-emerald-400 bg-emerald-50 dark:bg-emerald-900/20 text-emerald-700 dark:text-emerald-300" :
              "border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 text-gray-900 dark:text-white hover:border-yellow-400 hover:bg-yellow-50 dark:hover:bg-yellow-900/10"
            }`}
          >
            {part.text}
          </button>
        ))}
      </div>

      <p className="text-center text-gray-500 dark:text-gray-400 text-sm mb-5">Arti: <span className="text-gray-700 dark:text-gray-300">{q.meaning}</span></p>

      {result && (
        <>
          <div className={`p-3 rounded-xl text-center text-sm mb-4 border ${result === "correct" ? "bg-emerald-50 dark:bg-emerald-900/10 border-emerald-200 dark:border-emerald-800 text-emerald-700 dark:text-emerald-300" : "bg-red-50 dark:bg-red-900/10 border-red-200 dark:border-red-800 text-red-700 dark:text-red-300"}`}>
            {result === "correct" ? "✅ Benar! Itu adalah huruf Qalqalah." : "❌ Bukan. Cari huruf dari ق ط ب ج د yang berharakat sukun."}
          </div>
          <button onClick={next} className="w-full py-3 rounded-xl font-semibold text-white bg-yellow-500 hover:bg-yellow-400 transition">
            {cur + 1 >= qs.length ? "Lihat Hasil" : "Soal Berikutnya →"}
          </button>
        </>
      )}
    </div>
  );
}

// ─── Game: Alif Lam ───────────────────────────────────────────────
function AlifLamGame() {
  const [qs] = useState(() => shuffle(alifLamQuiz));
  const [cur, setCur] = useState(0);
  const [chosen, setChosen] = useState(null);
  const [score, setScore] = useState(0);
  const [done, setDone] = useState(false);

  const q = qs[cur];
  const handleChoose = (a) => {
    if (chosen) return;
    setChosen(a);
    if (a === q.answer) setScore((s) => s + 1);
  };
  const next = () => {
    if (cur + 1 >= qs.length) setDone(true);
    else { setCur((c) => c + 1); setChosen(null); }
  };
  const restart = () => { setCur(0); setChosen(null); setScore(0); setDone(false); };

  if (done) {
    return (
      <div className="text-center py-6">
        <div className={`text-6xl font-bold mb-3 ${score >= qs.length * 0.8 ? "text-emerald-600" : "text-yellow-600"}`}>
          {Math.round((score / qs.length) * 100)}%
        </div>
        <p className="text-gray-900 dark:text-white font-bold mb-6">{score} dari {qs.length} benar</p>
        <button onClick={restart} className="px-8 py-3 rounded-xl font-semibold text-white bg-yellow-500 hover:bg-yellow-400 transition">Ulangi</button>
      </div>
    );
  }

  return (
    <div>
      <div className="flex items-center justify-between text-sm text-gray-500 dark:text-gray-400 mb-3">
        <span>Soal {cur + 1}/{qs.length}</span>
        <span className="text-emerald-600 font-semibold">{score} benar</span>
      </div>
      <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-1.5 mb-6">
        <div className="h-1.5 rounded-full bg-yellow-500 transition-all" style={{ width: `${(cur / qs.length) * 100}%` }} />
      </div>
      <div className="text-center mb-6">
        <div className="text-7xl font-arabic text-gray-900 dark:text-white bg-gray-50 dark:bg-gray-800 rounded-xl py-5 mb-3 border border-gray-100 dark:border-gray-700">{q.word}</div>
        <p className="text-gray-400 font-mono text-sm mb-1">/{q.pronunciation}/</p>
        <p className="text-gray-600 dark:text-gray-300">Arti: <span className="font-medium text-gray-900 dark:text-white">{q.meaning}</span></p>
      </div>

      <div className="grid grid-cols-2 gap-4 mb-4">
        {["Syamsiyah", "Qamariyah"].map((opt) => {
          let cls = "border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:border-yellow-400";
          if (chosen) {
            if (opt === q.answer) cls = "border-emerald-400 bg-emerald-50 dark:bg-emerald-900/20 text-emerald-700 dark:text-emerald-300";
            else if (opt === chosen) cls = "border-red-400 bg-red-50 dark:bg-red-900/20 text-red-700 dark:text-red-300";
            else cls = "border-gray-100 dark:border-gray-800 text-gray-400 dark:text-gray-600";
          }
          return (
            <button key={opt} onClick={() => handleChoose(opt)} disabled={!!chosen}
              className={`p-5 rounded-2xl border-2 font-bold text-lg transition-all disabled:cursor-default ${cls}`}>
              {opt === "Syamsiyah" ? "☀️" : "🌙"} {opt}
            </button>
          );
        })}
      </div>

      {chosen && (
        <div className={`p-4 rounded-xl text-sm mb-4 border ${chosen === q.answer ? "bg-emerald-50 dark:bg-emerald-900/10 border-emerald-200 dark:border-emerald-800 text-emerald-700 dark:text-emerald-300" : "bg-red-50 dark:bg-red-900/10 border-red-200 dark:border-red-800 text-red-700 dark:text-red-300"}`}>
          {chosen === q.answer ? `✅ Benar! ` : `❌ Jawaban benar: ${q.answer}. `}💡 {q.hint}
        </div>
      )}
      {chosen && (
        <button onClick={next} className="w-full py-3 rounded-xl font-semibold text-white bg-yellow-500 hover:bg-yellow-400 transition">
          {cur + 1 >= qs.length ? "Lihat Hasil" : "Soal Berikutnya →"}
        </button>
      )}
    </div>
  );
}

// ─── Games config ─────────────────────────────────────────────────
const GAMES = [
  {
    id: "hijaiyah",
    title: "Huruf Hijaiyah",
    subtitle: "Kenali 30 huruf Al-Qur'an beserta makhrajnya",
    icon: "🔤",
    level: "Pemula",
    component: <HijaiyahGame />,
  },
  {
    id: "nunSukun",
    title: "Nun Sukun & Tanwin",
    subtitle: "Izhar · Idgham · Iqlab · Ikhfa",
    icon: "📖",
    level: "Menengah",
    component: (
      <QuizGame
        questions={nunSukunQuiz}
        accentBg="bg-yellow-500"
      />
    ),
  },
  {
    id: "qalqalah",
    title: "Qalqalah",
    subtitle: "Temukan huruf yang memantul (ق ط ب ج د)",
    icon: "🔊",
    level: "Menengah",
    component: <QalqalahGame />,
  },
  {
    id: "alifLam",
    title: "Alif Lam (ال)",
    subtitle: "Syamsiyah vs Qamariyah",
    icon: "☀️",
    level: "Menengah",
    component: <AlifLamGame />,
  },
  {
    id: "waqaf",
    title: "Tanda Waqaf",
    subtitle: "Kapan harus berhenti saat membaca?",
    icon: "⏸️",
    level: "Lanjut",
    component: (
      <QuizGame
        questions={waqafQuiz.map((q) => ({
          ...q,
          question: `Apa arti tanda waqaf "${q.sign}" (${q.name})?`,
        }))}
        accentBg="bg-yellow-500"
      />
    ),
  },
];

const LEVEL_BADGE = {
  Pemula: "bg-emerald-100 dark:bg-emerald-900/30 text-emerald-700 dark:text-emerald-400",
  Menengah: "bg-yellow-100 dark:bg-yellow-900/30 text-yellow-700 dark:text-yellow-400",
  Lanjut: "bg-red-100 dark:bg-red-900/30 text-red-600 dark:text-red-400",
};

// ─── Main Page ────────────────────────────────────────────────────
const QTajwid = () => {
  const [activeTab, setActiveTab] = useState("tilawati"); // "tilawati" | game id
  const [activeGameKey, setActiveGameKey] = useState(0); // force remount on reselect

  const handleGameSelect = (id) => {
    if (activeTab === id) {
      setActiveGameKey((k) => k + 1); // restart game
    } else {
      setActiveTab(id);
    }
  };

  const activeGame = GAMES.find((g) => g.id === activeTab);

  return (
    <div className="min-h-screen flex flex-col bg-white dark:bg-gray-900 font-sans">
      <Navbar />

      {/* ── Hero ── */}
      <div className="relative bg-linear-to-br from-gray-50 via-white to-gray-100 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900 pt-32 pb-20 overflow-hidden">
        <div className="absolute top-0 right-0 -mr-20 -mt-20 w-96 h-96 bg-yellow-100 dark:bg-yellow-900/20 rounded-full blur-3xl opacity-50" />
        <div className="absolute bottom-0 left-0 -ml-20 -mb-20 w-80 h-80 bg-yellow-50 dark:bg-yellow-900/10 rounded-full blur-3xl opacity-50" />

        <div className="container mx-auto px-6 relative z-10 text-center">
          <div className="inline-block px-4 py-1.5 mb-6 bg-yellow-100 dark:bg-yellow-900/20 text-yellow-800 dark:text-yellow-200 rounded-full text-sm font-semibold tracking-wide">
            ✨ qTajwid — Metode Tilawati
          </div>
          <h1 className="text-4xl md:text-6xl font-bold text-gray-900 dark:text-white leading-tight mb-6">
            Belajar Tajwid Al-Qur'an <br />
            <span className="text-transparent bg-clip-text bg-linear-to-r from-yellow-500 to-yellow-600">
              Secara Interaktif
            </span>
          </h1>
          <p className="text-lg text-gray-600 dark:text-gray-300 mb-8 leading-relaxed max-w-2xl mx-auto">
            Pelajari tajwid Al-Qur'an dengan panduan Kitab Tilawati dan game interaktif — mulai dari huruf hijaiyah hingga hukum bacaan lanjut.
          </p>
          <div className="flex gap-3 justify-center flex-wrap">
            <button
              onClick={() => setActiveTab("tilawati")}
              className="px-6 py-3 bg-yellow-500 hover:bg-yellow-400 text-white font-bold rounded-full transition shadow-lg shadow-yellow-500/20"
            >
              📕 Buka Kitab Tilawati
            </button>
            <button
              onClick={() => setActiveTab("hijaiyah")}
              className="px-6 py-3 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 text-gray-700 dark:text-gray-200 font-semibold rounded-full hover:bg-gray-50 dark:hover:bg-gray-700 transition"
            >
              🎮 Mulai Game
            </button>
          </div>
        </div>
      </div>

      {/* ── Stats ── */}
      <section className="py-12 bg-white dark:bg-gray-900 border-b border-gray-100 dark:border-gray-800">
        <div className="container mx-auto px-6">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            {[
              { value: "30", label: "Huruf Hijaiyah" },
              { value: "5", label: "Game Interaktif" },
              { value: "50+", label: "Soal Latihan" },
              { value: "1", label: "Kitab Tilawati" },
            ].map((s) => (
              <div key={s.label}>
                <p className="text-4xl font-bold text-yellow-600 dark:text-yellow-400 mb-2">{s.value}</p>
                <p className="text-gray-500 dark:text-gray-400 font-medium">{s.label}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ── Main Content ── */}
      <section className="bg-gray-50 dark:bg-gray-800 py-24 flex-1">
        <div className="container mx-auto px-6">
          {/* Tab navigation */}
          <div className="flex flex-wrap gap-3 mb-10">
            {/* Tilawati PDF tab */}
            <button
              onClick={() => setActiveTab("tilawati")}
              className={`flex items-center gap-2 px-5 py-2.5 rounded-full font-semibold text-sm transition-all border ${
                activeTab === "tilawati"
                  ? "bg-yellow-500 border-yellow-500 text-white shadow-md shadow-yellow-500/20"
                  : "bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-400 hover:border-yellow-300"
              }`}
            >
              📕 Kitab Tilawati
            </button>

            {/* Game tabs */}
            {GAMES.map((g) => (
              <button
                key={g.id}
                onClick={() => handleGameSelect(g.id)}
                className={`flex items-center gap-2 px-5 py-2.5 rounded-full font-semibold text-sm transition-all border ${
                  activeTab === g.id
                    ? "bg-yellow-500 border-yellow-500 text-white shadow-md shadow-yellow-500/20"
                    : "bg-white dark:bg-gray-900 border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-400 hover:border-yellow-300"
                }`}
              >
                {g.icon} {g.title}
              </button>
            ))}
          </div>

          {/* ── PDF Viewer ── */}
          {activeTab === "tilawati" && (
            <div className="bg-white dark:bg-gray-900 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 overflow-hidden">
              <div className="flex items-center justify-between px-6 py-4 border-b border-gray-100 dark:border-gray-700">
                <div>
                  <h2 className="text-xl font-bold text-gray-900 dark:text-white">📕 Kitab Tilawati</h2>
                  <p className="text-sm text-gray-500 dark:text-gray-400">Panduan belajar tajwid metode Tilawati</p>
                </div>
                <a
                  href="/qtajwid/Tilawati.pdf"
                  download
                  className="flex items-center gap-2 px-4 py-2 rounded-lg bg-yellow-50 dark:bg-yellow-900/20 text-yellow-700 dark:text-yellow-400 border border-yellow-200 dark:border-yellow-800 text-sm font-semibold hover:bg-yellow-100 dark:hover:bg-yellow-900/30 transition"
                >
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                  </svg>
                  Download PDF
                </a>
              </div>
              <div style={{ height: "75vh" }}>
                <iframe
                  src="/qtajwid/Tilawati.pdf"
                  title="Kitab Tilawati"
                  className="w-full h-full"
                  style={{ border: "none" }}
                />
              </div>
            </div>
          )}

          {/* ── Game Panel ── */}
          {activeGame && (
            <div className="bg-white dark:bg-gray-900 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 overflow-hidden">
              <div className="flex items-center justify-between px-6 py-4 border-b border-gray-100 dark:border-gray-700">
                <div className="flex items-center gap-3">
                  <span className="text-2xl">{activeGame.icon}</span>
                  <div>
                    <h2 className="text-xl font-bold text-gray-900 dark:text-white">{activeGame.title}</h2>
                    <p className="text-sm text-gray-500 dark:text-gray-400">{activeGame.subtitle}</p>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <span className={`text-xs px-3 py-1 rounded-full font-semibold ${LEVEL_BADGE[activeGame.level]}`}>
                    {activeGame.level}
                  </span>
                  <button
                    onClick={() => handleGameSelect(activeGame.id)}
                    title="Mulai ulang"
                    className="p-2 rounded-lg text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 transition"
                  >
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                    </svg>
                  </button>
                </div>
              </div>
              <div className="p-6 md:p-8" key={activeGameKey}>
                {activeGame.component}
              </div>
            </div>
          )}
        </div>
      </section>

      {/* ── CTA ── */}
      <section className="py-20 bg-yellow-500 relative overflow-hidden">
        <div className="absolute top-0 left-0 w-full h-full overflow-hidden">
          <div className="absolute w-64 h-64 bg-white opacity-10 rounded-full -top-10 -left-10" />
          <div className="absolute w-96 h-96 bg-white opacity-10 rounded-full bottom-0 right-0" />
        </div>
        <div className="container mx-auto px-6 text-center relative z-10">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">
            Mulai Belajar Tajwid Sekarang
          </h2>
          <p className="text-white/90 text-lg mb-10 max-w-2xl mx-auto">
            Pelajari tajwid Al-Qur'an dengan panduan Kitab Tilawati dan game interaktif yang menyenangkan.
          </p>
          <button
            onClick={() => {
              setActiveTab("tilawati");
              document.querySelector("section.bg-gray-50")?.scrollIntoView({ behavior: "smooth" });
            }}
            className="bg-white text-yellow-600 px-8 py-4 rounded-full font-bold text-lg hover:bg-gray-100 transition shadow-xl"
          >
            Buka Kitab Tilawati
          </button>
        </div>
      </section>

      <Footer />
    </div>
  );
};

export default QTajwid;
