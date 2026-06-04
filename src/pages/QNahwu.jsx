import React, { useState, useRef, useCallback } from "react";
import Navbar from "../components/Navbar";

/* ============================================================
   DATA SEMUA SUB-GAME JAMID MABNY
   ============================================================ */

const GAMES = [
  {
    id: "dhamir",
    title: "Dhamir",
    icon: "ض",
    color: "#6366f1",
    colorDark: "#4f46e5",
    colorLight: "#e0e7ff",
    columns: [
      { key: "type", label: "Jenis Dhomir" },
      { key: "gender", label: "Jenis Kelamin" },
      { key: "number", label: "Jumlah" },
    ],
    optionGroups: [
      [
        { value: "G", label: "G = Ghaib" },
        { value: "M", label: "M = Mukhatab" },
        { value: "T", label: "T = Takallum" },
      ],
      [
        { value: "L", label: "L = Laki" },
        { value: "P", label: "P = Perempuan" },
      ],
      [
        { value: "1", label: "1 = Mufrad" },
        { value: "2", label: "2 = Mutsanna" },
        { value: "3", label: "3 = Jamak" },
      ],
    ],
    questions: [
      {
        verse: `قُلْ <mark>هُوَ</mark> اللَّهُ أَحَدٌ`,
        translation: `Katakanlah: "Dialah Allah, Yang Maha Esa." (QS. Al-Ikhlas: 1)`,
        answers: { type: "G", gender: "L", number: "1" },
      },
      {
        verse: `أُولَٰئِكَ عَلَىٰ هُدًى مِنْ رَبِّهِمْ ۖ وَأُولَٰئِكَ <mark>هُمُ</mark> الْمُفْلِحُونَ`,
        translation: `Merekalah orang-orang yang beruntung. (QS. Al-Baqarah: 5)`,
        answers: { type: "G", gender: "L", number: "3" },
      },
      {
        verse: `قَالَ إِنَّكَ <mark>أَنْتَ</mark> الْعَلِيمُ الْحَكِيمُ`,
        translation: `Dia berfirman: "Sesungguhnya Engkaulah Yang Maha Mengetahui lagi Maha Bijaksana." (QS. Al-Baqarah: 32)`,
        answers: { type: "M", gender: "L", number: "1" },
      },
      {
        verse: `إِنَّا <mark>نَحْنُ</mark> نَزَّلْنَا الذِّكْرَ`,
        translation: `Sesungguhnya Kamilah yang menurunkan Al-Quran. (QS. Al-Hijr: 9)`,
        answers: { type: "T", gender: "L", number: "3" },
      },
      {
        verse: `<mark>إِيَّاكَ</mark> نَعْبُدُ وَ<mark>إِيَّاكَ</mark> نَسْتَعِينُ`,
        translation: `Hanya Engkaulah yang kami sembah dan hanya kepada Engkaulah kami mohon pertolongan. (QS. Al-Fatihah: 5)`,
        answers: { type: "M", gender: "L", number: "1" },
      },
    ],
  },
  {
    id: "fiil-jamid",
    title: "Fi'il Jamid",
    icon: "ف",
    color: "#f59e0b",
    colorDark: "#d97706",
    colorLight: "#fef3c7",
    columns: [
      { key: "zaman", label: "Zaman" },
      { key: "fungsi", label: "Fungsi" },
      { key: "irab", label: "I'rab" },
    ],
    optionGroups: [
      [
        { value: "MD", label: "MD = Madhi" },
        { value: "AM", label: "AM = Amar" },
      ],
      [
        { value: "MDH", label: "MDH = Madah" },
        { value: "RJA", label: "RJA = Raja'" },
        { value: "NFY", label: "NFY = Nafi" },
        { value: "TLB", label: "TLB = Thalab" },
      ],
      [{ value: "MBN", label: "MBN = Mabni" }],
    ],
    questions: [
      {
        verse: `<mark>نِعْمَ</mark> الْعَبْدُ ۖ إِنَّهُ أَوَّابٌ`,
        translation: `Dialah sebaik-baik hamba. Sesungguhnya dia amat taat kepada Tuhannya. (QS. Sad: 30)`,
        answers: { zaman: "MD", fungsi: "MDH", irab: "MBN" },
      },
      {
        verse: `<mark>بِئْسَ</mark> الِاسْمُ الْفُسُوقُ بَعْدَ الْإِيمَانِ`,
        translation: `Seburuk-buruk panggilan adalah (panggilan) yang buruk sesudah iman. (QS. Al-Hujurat: 11)`,
        answers: { zaman: "MD", fungsi: "MDH", irab: "MBN" },
      },
      {
        verse: `فَ<mark>عَسَى</mark> اللَّهُ أَنْ يَأْتِيَ بِالْفَتْحِ`,
        translation: `Maka mudah-mudahan Allah akan mendatangkan kemenangan kepadamu. (QS. Al-Ma'idah: 52)`,
        answers: { zaman: "MD", fungsi: "RJA", irab: "MBN" },
      },
      {
        verse: `<mark>لَيْسَ</mark> كَمِثْلِهِ شَيْءٌ`,
        translation: `Tidak ada sesuatupun yang serupa dengan Dia. (QS. Asy-Syura: 11)`,
        answers: { zaman: "MD", fungsi: "NFY", irab: "MBN" },
      },
      {
        verse: `رَبَّنَا <mark>هَبْ</mark> لَنَا مِنْ أَزْوَاجِنَا وَذُرِّيَّاتِنَا قُرَّةَ أَعْيُنٍ`,
        translation: `Ya Tuhan kami, anugerahkanlah kepada kami isteri-isteri kami dan keturunan kami sebagai penyenang hati. (QS. Al-Furqan: 74)`,
        answers: { zaman: "AM", fungsi: "TLB", irab: "MBN" },
      },
    ],
  },
  {
    id: "isim-fiil",
    title: "Isim Fi'il",
    icon: "ا",
    color: "#10b981",
    colorDark: "#059669",
    colorLight: "#d1fae5",
    columns: [
      { key: "zaman", label: "Zaman" },
      { key: "fungsi", label: "Fungsi" },
      { key: "irab", label: "I'rab" },
    ],
    optionGroups: [
      [
        { value: "MD", label: "MD = Madhi" },
        { value: "MDP", label: "MDP = Mudhari'" },
        { value: "AM", label: "AM = Amar" },
      ],
      [
        { value: "AJB", label: "AJB = Ta'ajub" },
        { value: "TLB", label: "TLB = Thalab" },
        { value: "NFY", label: "NFY = Nafi" },
        { value: "TRG", label: "TRG = Tarhib" },
      ],
      [{ value: "MBN", label: "MBN = Mabni" }],
    ],
    questions: [
      {
        verse: `<mark>هَيْهَاتَ</mark> هَيْهَاتَ لِمَا تُوعَدُونَ`,
        translation: `Jauh, jauh sekali (dari kebenaran) apa yang diancamkan kepada kamu itu. (QS. Al-Mu'minun: 36)`,
        answers: { zaman: "MD", fungsi: "NFY", irab: "MBN" },
      },
      {
        verse: `<mark>صَهٍ</mark> لَا تَقُلْ ذَٰلِكَ`,
        translation: `Diam! Jangan katakan itu.`,
        answers: { zaman: "AM", fungsi: "TLB", irab: "MBN" },
      },
      {
        verse: `<mark>أَوَّهْ</mark> مِمَّا أَنَا فِيهِ`,
        translation: `Aduh dari apa yang aku alami ini.`,
        answers: { zaman: "MDP", fungsi: "TRG", irab: "MBN" },
      },
      {
        verse: `<mark>شَتَّانَ</mark> مَا يَوْمِي بِيَوْمِ حَيَّانَ أَخِي`,
        translation: `Betapa jauh bedanya hariku dengan hari saudaraku Hayyan.`,
        answers: { zaman: "MD", fungsi: "AJB", irab: "MBN" },
      },
      {
        verse: `<mark>عَلَيْكُمْ</mark> أَنْفُسَكُمْ`,
        translation: `Jagalah dirimu masing-masing. (QS. Al-Ma'idah: 105)`,
        answers: { zaman: "AM", fungsi: "TLB", irab: "MBN" },
      },
    ],
  },
  {
    id: "istifham",
    title: "Istifham",
    icon: "؟",
    color: "#ef4444",
    colorDark: "#dc2626",
    colorLight: "#fee2e2",
    columns: [
      { key: "fungsi", label: "Fungsi" },
      { key: "irab", label: "I'rab" },
      { key: "jenis", label: "Jenis" },
    ],
    optionGroups: [
      [
        { value: "AQL", label: "AQL = Aqil" },
        { value: "GHA", label: "GHA = Ghair Aqil" },
        { value: "ZMN", label: "ZMN = Zaman" },
        { value: "MKN", label: "MKN = Makan" },
        { value: "HAL", label: "HAL = Hal" },
      ],
      [
        { value: "MBN", label: "MBN = Mabni" },
        { value: "MRB", label: "MRB = Mu'rab" },
      ],
      [
        { value: "I", label: "Isim" },
        { value: "H", label: "Harf" },
      ],
    ],
    questions: [
      {
        verse: `وَ<mark>مَنْ</mark> أَصْدَقُ مِنَ اللَّهِ حَدِيثًا`,
        translation: `Dan siapakah yang lebih benar perkataannya daripada Allah? (QS. An-Nisa: 87)`,
        answers: { fungsi: "AQL", irab: "MBN", jenis: "I" },
      },
      {
        verse: `قَالَ <mark>هَلْ</mark> عَلِمْتُمْ مَا فَعَلْتُمْ بِيُوسُفَ`,
        translation: `Dia berkata, "Apakah kamu mengetahui apa yang telah kamu perbuat terhadap Yusuf?" (QS. Yusuf: 89)`,
        answers: { fungsi: "AQL", irab: "MBN", jenis: "H" },
      },
      {
        verse: `وَيَقُولُونَ <mark>مَتَىٰ</mark> هَٰذَا الْوَعْدُ إِنْ كُنْتُمْ صَادِقِينَ`,
        translation: `Dan mereka berkata, "Kapankah datangnya janji ini, jika kamu orang-orang yang benar?" (QS. Yasin: 48)`,
        answers: { fungsi: "ZMN", irab: "MBN", jenis: "I" },
      },
      {
        verse: `فَ<mark>أَيْنَ</mark> تَذْهَبُونَ`,
        translation: `Maka ke manakah kamu akan pergi? (QS. At-Takwir: 26)`,
        answers: { fungsi: "MKN", irab: "MBN", jenis: "I" },
      },
      {
        verse: `فَبِ<mark>أَيِّ</mark> آلَاءِ رَبِّكُمَا تُكَذِّبَانِ`,
        translation: `Maka nikmat Tuhanmu yang manakah yang kamu dustakan? (QS. Ar-Rahman: 13)`,
        answers: { fungsi: "GHA", irab: "MRB", jenis: "I" },
      },
    ],
  },
  {
    id: "isyarah",
    title: "Isyarah",
    icon: "إ",
    color: "#8b5cf6",
    colorDark: "#7c3aed",
    colorLight: "#ede9fe",
    columns: [
      { key: "jarak", label: "Jarak" },
      { key: "gender", label: "Jenis Kelamin" },
      { key: "jumlah", label: "Jumlah" },
    ],
    optionGroups: [
      [
        { value: "Q", label: "Q = Qarib" },
        { value: "B", label: "B = Ba'id" },
      ],
      [
        { value: "L", label: "L = Mudzakkar" },
        { value: "P", label: "P = Muannats" },
      ],
      [
        { value: "1", label: "1 = Mufrad" },
        { value: "2", label: "2 = Mutsanna" },
        { value: "3", label: "3 = Jamak" },
      ],
    ],
    questions: [
      {
        verse: `<mark>هَٰذَا</mark> خَلْقُ اللَّهِ فَأَرُونِي مَاذَا خَلَقَ الَّذِينَ مِنْ دُونِهِ`,
        translation: `Inilah ciptaan Allah, maka perlihatkanlah olehmu kepadaku apa yang telah diciptakan oleh sembahan-sembahanmu selain Allah. (QS. Luqman: 11)`,
        answers: { jarak: "Q", gender: "L", jumlah: "1" },
      },
      {
        verse: `<mark>ذَٰلِكَ</mark> الْكِتَابُ لَا رَيْبَ فِيهِ`,
        translation: `Itulah Kitab (Al-Quran) yang tidak ada keraguan padanya. (QS. Al-Baqarah: 2)`,
        answers: { jarak: "B", gender: "L", jumlah: "1" },
      },
      {
        verse: `<mark>تِلْكَ</mark> آيَاتُ الْكِتَابِ الْحَكِيمِ`,
        translation: `Itulah ayat-ayat Al-Quran yang mengandung hikmah. (QS. Luqman: 2)`,
        answers: { jarak: "B", gender: "P", jumlah: "1" },
      },
      {
        verse: `قَالَ يَا قَوْمِ <mark>هَٰؤُلَاءِ</mark> بَنَاتِي هُنَّ أَطْهَرُ لَكُمْ`,
        translation: `Ia berkata: 'Hai kaumku, inilah puteri-puteriku, mereka lebih suci bagimu'. (QS. Hud: 78)`,
        answers: { jarak: "Q", gender: "P", jumlah: "3" },
      },
      {
        verse: `قَالُوا إِنْ <mark>هَٰذَانِ</mark> لَسَاحِرَانِ يُرِيدَانِ أَنْ يُخْرِجَاكُمْ`,
        translation: `Mereka berkata: 'Sesungguhnya dua orang ini adalah benar-benar ahli sihir yang hendak mengusir kamu'. (QS. Taha: 63)`,
        answers: { jarak: "Q", gender: "L", jumlah: "2" },
      },
    ],
  },
  {
    id: "mws",
    title: "Mws (Mausul)",
    icon: "م",
    color: "#0ea5e9",
    colorDark: "#0284c7",
    colorLight: "#e0f2fe",
    columns: [
      { key: "jenis", label: "Jenis" },
      { key: "gender", label: "Jenis Kelamin" },
      { key: "jumlah", label: "Jumlah" },
    ],
    optionGroups: [
      [
        { value: "I", label: "I = Isim" },
        { value: "H", label: "H = Harf" },
      ],
      [
        { value: "L", label: "L = Mudzakkar" },
        { value: "P", label: "P = Muannats" },
        { value: "U", label: "U = Umum" },
      ],
      [
        { value: "1", label: "1 = Mufrad" },
        { value: "2", label: "2 = Mutsanna" },
        { value: "3", label: "3 = Jamak" },
      ],
    ],
    questions: [
      {
        verse: `<mark>الَّذِي</mark> خَلَقَكَ فَسَوَّاكَ فَعَدَلَكَ`,
        translation: `Yang telah menciptakanmu lalu menyempurnakan kejadianmu dan menjadikan (susunan tubuh)mu seimbang. (QS. Al-Infitar: 7)`,
        answers: { jenis: "I", gender: "L", jumlah: "1" },
      },
      {
        verse: `<mark>الَّذِينَ</mark> يُؤْمِنُونَ بِالْغَيْبِ`,
        translation: `Orang-orang yang beriman kepada yang ghaib. (QS. Al-Baqarah: 3)`,
        answers: { jenis: "I", gender: "L", jumlah: "3" },
      },
      {
        verse: `وَالَّذِي جَاءَ بِالصِّدْقِ وَصَدَّقَ بِهِ أُولَٰئِكَ <mark>هُمُ</mark> الْمُتَّقُونَ`,
        translation: `Dan orang yang membawa kebenaran (Muhammad) dan yang membenarkannya, mereka itulah orang-orang yang bertakwa. (QS. Az-Zumar: 33)`,
        answers: { jenis: "I", gender: "L", jumlah: "3" },
      },
      {
        verse: `<mark>مَا</mark> عِندَكُمْ يَنفَدُ وَمَا عِندَ اللَّهِ بَاقٍ`,
        translation: `Apa yang di sisimu akan lenyap, dan apa yang ada di sisi Allah adalah kekal. (QS. An-Nahl: 96)`,
        answers: { jenis: "I", gender: "U", jumlah: "1" },
      },
      {
        verse: `<mark>مَنْ</mark> عَمِلَ صَالِحًا فَلِنَفْسِهِ`,
        translation: `Barangsiapa yang mengerjakan amal saleh maka (pahalanya) untuk dirinya sendiri. (QS. Fussilat: 46)`,
        answers: { jenis: "I", gender: "U", jumlah: "1" },
      },
    ],
  },
  {
    id: "syarath",
    title: "Syarath",
    icon: "ش",
    color: "#f97316",
    colorDark: "#ea580c",
    colorLight: "#ffedd5",
    columns: [
      { key: "jazm", label: "Jazm" },
      { key: "jenis", label: "Jenis" },
      { key: "fungsi", label: "Fungsi" },
    ],
    optionGroups: [
      [
        { value: "J", label: "J = Jazim" },
        { value: "GJ", label: "GJ = Ghairu Jazim" },
      ],
      [
        { value: "I", label: "Isim" },
        { value: "H", label: "Harf" },
      ],
      [
        { value: "AQL", label: "AQL = Aqil" },
        { value: "ZMN", label: "ZMN = Zaman" },
        { value: "MKN", label: "MKN = Makan" },
        { value: "RBT", label: "RBT = Rabth" },
      ],
    ],
    questions: [
      {
        verse: `<mark>إِنْ</mark> تَنْصُرُوا اللَّهَ يَنْصُرْكُمْ`,
        translation: `Jika kamu menolong (agama) Allah, niscaya Dia akan menolongmu. (QS. Muhammad: 7)`,
        answers: { jazm: "J", jenis: "H", fungsi: "RBT" },
      },
      {
        verse: `فَ<mark>مَنْ</mark> يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًا يَرَهُ`,
        translation: `Maka barangsiapa mengerjakan kebaikan seberat zarrah, niscaya dia akan melihat (balasan)nya. (QS. Az-Zalzalah: 7)`,
        answers: { jazm: "J", jenis: "I", fungsi: "AQL" },
      },
      {
        verse: `<mark>أَيْنَمَا</mark> تَكُونُوا يُدْرِكْكُمُ الْمَوْتُ`,
        translation: `Di mana saja kamu berada, kematian akan mendapatkan kamu. (QS. An-Nisa: 78)`,
        answers: { jazm: "J", jenis: "I", fungsi: "MKN" },
      },
      {
        verse: `<mark>إِذَا</mark> جَاءَ نَصْرُ اللَّهِ وَالْفَتْحُ`,
        translation: `Apabila telah datang pertolongan Allah dan kemenangan. (QS. An-Nasr: 1)`,
        answers: { jazm: "GJ", jenis: "I", fungsi: "ZMN" },
      },
      {
        verse: `<mark>لَوْ</mark> أَنْزَلْنَا هَٰذَا الْقُرْآنَ عَلَىٰ جَبَلٍ لَرَأَيْتَهُ خَاشِعًا`,
        translation: `Kalau sekiranya Kami turunkan Al-Quran ini kepada sebuah gunung, pasti kamu akan melihatnya tunduk terpecah belah. (QS. Al-Hasyr: 21)`,
        answers: { jazm: "GJ", jenis: "H", fungsi: "RBT" },
      },
    ],
  },
];

/* ============================================================
   KOMPONEN DRAG-AND-DROP CHIP
   ============================================================ */

function Chip({ label, value, color, isDragging, onDragStart, onDragEnd }) {
  return (
    <div
      draggable
      onDragStart={(e) => {
        e.dataTransfer.setData("text/plain", value);
        onDragStart(value);
      }}
      onDragEnd={onDragEnd}
      style={{
        background: isDragging
          ? "rgba(255,255,255,0.3)"
          : `linear-gradient(135deg, ${color}, ${color}cc)`,
        color: "white",
        padding: "6px 14px",
        borderRadius: "999px",
        cursor: "grab",
        fontWeight: 700,
        fontSize: "0.78rem",
        letterSpacing: "0.02em",
        boxShadow: isDragging
          ? "none"
          : "0 2px 8px rgba(0,0,0,0.25)",
        opacity: isDragging ? 0.4 : 1,
        transform: isDragging ? "scale(0.95)" : "scale(1)",
        transition: "all 0.15s ease",
        userSelect: "none",
        whiteSpace: "nowrap",
        border: "1.5px solid rgba(255,255,255,0.25)",
      }}
    >
      {label}
    </div>
  );
}

/* ============================================================
   KOMPONEN DROPZONE
   ============================================================ */

function DropZone({ category, label, state, droppedValue, droppedLabel, color, onDrop, onDragOver, onDragLeave }) {
  const getBg = () => {
    if (state === "correct") return "#d1fae5";
    if (state === "incorrect") return "#fee2e2";
    if (state === "hover") return `${color}22`;
    return "#f9fafb";
  };
  const getBorder = () => {
    if (state === "correct") return "#10b981";
    if (state === "incorrect") return "#ef4444";
    if (state === "hover") return color;
    return "#d1d5db";
  };
  const getChipBg = () => {
    if (state === "correct") return "#059669";
    if (state === "incorrect") return "#dc2626";
    return color;
  };

  return (
    <div style={{ flex: 1, textAlign: "center" }}>
      <div
        style={{
          fontSize: "0.7rem",
          fontWeight: 700,
          color: "#6b7280",
          textTransform: "uppercase",
          letterSpacing: "0.08em",
          marginBottom: "6px",
        }}
      >
        {label}
      </div>
      <div
        onDrop={onDrop}
        onDragOver={onDragOver}
        onDragLeave={onDragLeave}
        style={{
          minHeight: "52px",
          border: `2px dashed ${getBorder()}`,
          borderRadius: "10px",
          background: getBg(),
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          transition: "all 0.2s ease",
          cursor: "pointer",
          padding: "4px",
        }}
      >
        {droppedValue ? (
          <div
            style={{
              background: getChipBg(),
              color: "white",
              padding: "5px 12px",
              borderRadius: "999px",
              fontWeight: 700,
              fontSize: "0.78rem",
            }}
          >
            {droppedLabel}
          </div>
        ) : (
          <span style={{ color: "#9ca3af", fontSize: "0.75rem" }}>
            Taruh di sini
          </span>
        )}
      </div>
    </div>
  );
}

/* ============================================================
   KOMPONEN SATU GAME
   ============================================================ */

function GamePanel({ game }) {
  const totalQ = game.questions.length;
  const [qIndex, setQIndex] = useState(0);
  const [dropped, setDropped] = useState({}); // { colKey: value }
  const [dropState, setDropState] = useState({}); // { colKey: 'correct'|'incorrect'|'hover'|'' }
  const [feedback, setFeedback] = useState(null); // null | 'correct' | 'wrong'
  const [draggingValue, setDraggingValue] = useState(null);
  const [score, setScore] = useState(0);
  const [finished, setFinished] = useState(false);

  const q = game.questions[qIndex];
  const allColumns = game.columns.map((c) => c.key);

  // Build a flat map value → label
  const valueToLabel = {};
  game.optionGroups.forEach((grp) => {
    grp.forEach((opt) => {
      valueToLabel[opt.value] = opt.label.split(" = ")[0];
    });
  });

  const reset = useCallback(() => {
    setDropped({});
    setDropState({});
    setFeedback(null);
    setDraggingValue(null);
  }, []);

  const handleCheck = () => {
    if (feedback === "correct") {
      // Lanjut ke soal berikutnya
      if (qIndex + 1 >= totalQ) {
        setFinished(true);
      } else {
        setQIndex((i) => i + 1);
        reset();
      }
      return;
    }

    const newStates = {};
    let allCorrect = true;
    allColumns.forEach((key) => {
      const userVal = dropped[key];
      const correctVal = q.answers[key];
      if (userVal === correctVal) {
        newStates[key] = "correct";
      } else {
        newStates[key] = "incorrect";
        allCorrect = false;
      }
    });
    setDropState(newStates);
    if (allCorrect) {
      setFeedback("correct");
      setScore((s) => s + 1);
    } else {
      setFeedback("wrong");
    }
  };

  const handleRestart = () => {
    setQIndex(0);
    setScore(0);
    setFinished(false);
    reset();
  };

  // Render ayat dengan <mark> jadi highlight
  const renderVerse = (verse) => {
    const parts = verse.split(/(<mark>.*?<\/mark>)/g);
    return parts.map((part, i) => {
      if (part.startsWith("<mark>")) {
        const text = part.replace(/<\/?mark>/g, "");
        return (
          <span
            key={i}
            style={{ color: game.color, fontWeight: 800, textShadow: `0 0 20px ${game.color}44` }}
          >
            {text}
          </span>
        );
      }
      return <span key={i}>{part}</span>;
    });
  };

  if (finished) {
    const pct = Math.round((score / totalQ) * 100);
    return (
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          padding: "60px 20px",
          textAlign: "center",
        }}
      >
        <div style={{ fontSize: "5rem", marginBottom: "16px" }}>
          {pct >= 80 ? "🎉" : pct >= 60 ? "👍" : "💪"}
        </div>
        <h2 style={{ fontSize: "1.8rem", fontWeight: 800, color: "#1f2937", marginBottom: "8px" }}>
          Selesai!
        </h2>
        <p style={{ color: "#6b7280", marginBottom: "24px" }}>
          Kamu menjawab benar{" "}
          <strong style={{ color: game.color }}>
            {score} dari {totalQ}
          </strong>{" "}
          soal ({pct}%)
        </p>
        <div
          style={{
            width: "180px",
            height: "12px",
            background: "#e5e7eb",
            borderRadius: "999px",
            marginBottom: "32px",
            overflow: "hidden",
          }}
        >
          <div
            style={{
              width: `${pct}%`,
              height: "100%",
              background: `linear-gradient(90deg, ${game.color}, ${game.colorDark})`,
              borderRadius: "999px",
              transition: "width 1s ease",
            }}
          />
        </div>
        <button
          onClick={handleRestart}
          style={{
            background: `linear-gradient(135deg, ${game.color}, ${game.colorDark})`,
            color: "white",
            border: "none",
            padding: "12px 32px",
            borderRadius: "999px",
            fontSize: "1rem",
            fontWeight: 700,
            cursor: "pointer",
            boxShadow: `0 4px 20px ${game.color}55`,
          }}
        >
          Ulangi Latihan
        </button>
      </div>
    );
  }

  const allDropped = allColumns.every((k) => dropped[k]);

  return (
    <div style={{ padding: "0 4px" }}>
      {/* Progress */}
      <div style={{ marginBottom: "20px" }}>
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            marginBottom: "6px",
          }}
        >
          <span style={{ fontSize: "0.8rem", color: "#6b7280", fontWeight: 600 }}>
            Soal {qIndex + 1} / {totalQ}
          </span>
          <span
            style={{
              fontSize: "0.8rem",
              fontWeight: 700,
              color: game.color,
              background: game.colorLight,
              padding: "3px 12px",
              borderRadius: "999px",
            }}
          >
            ⭐ {score} poin
          </span>
        </div>
        <div
          style={{
            height: "6px",
            background: "#e5e7eb",
            borderRadius: "999px",
            overflow: "hidden",
          }}
        >
          <div
            style={{
              width: `${((qIndex + 1) / totalQ) * 100}%`,
              height: "100%",
              background: `linear-gradient(90deg, ${game.color}, ${game.colorDark})`,
              borderRadius: "999px",
              transition: "width 0.4s ease",
            }}
          />
        </div>
      </div>

      {/* Pilihan chip */}
      <div
        style={{
          background: "#f9fafb",
          border: "1px solid #e5e7eb",
          borderRadius: "14px",
          padding: "16px",
          marginBottom: "16px",
        }}
      >
        <p
          style={{
            fontSize: "0.7rem",
            color: "#9ca3af",
            fontWeight: 600,
            marginBottom: "12px",
            textTransform: "uppercase",
            letterSpacing: "0.1em",
          }}
        >
          Pilihan Jawaban — Seret ke kotak di bawah
        </p>
        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            gap: "12px",
            justifyContent: "center",
          }}
        >
          {game.optionGroups.map((grp, gi) => (
            <React.Fragment key={gi}>
              {grp.map((opt) => (
                <Chip
                  key={opt.value}
                  label={opt.label.split(" = ")[0]}
                  value={opt.value}
                  color={game.color}
                  isDragging={draggingValue === opt.value}
                  onDragStart={(v) => setDraggingValue(v)}
                  onDragEnd={() => setDraggingValue(null)}
                />
              ))}
              {gi < game.optionGroups.length - 1 && (
                <div
                  key={`sep-${gi}`}
                  style={{
                    width: "1px",
                    background: "#d1d5db",
                    margin: "0 4px",
                  }}
                />
              )}
            </React.Fragment>
          ))}
        </div>
      </div>

      {/* Drop zones */}
      <div
        style={{
          display: "flex",
          gap: "10px",
          marginBottom: "20px",
        }}
      >
        {game.columns.map((col) => (
          <DropZone
            key={col.key}
            category={col.key}
            label={col.label}
            state={dropState[col.key] || ""}
            droppedValue={dropped[col.key] || null}
            droppedLabel={dropped[col.key] ? valueToLabel[dropped[col.key]] : null}
            color={game.color}
            onDrop={(e) => {
              e.preventDefault();
              const val = e.dataTransfer.getData("text/plain") || draggingValue;
              if (val) {
                setDropped((prev) => ({ ...prev, [col.key]: val }));
                setDropState((prev) => ({ ...prev, [col.key]: "" }));
                setFeedback(null);
              }
            }}
            onDragOver={(e) => {
              e.preventDefault();
              setDropState((prev) => ({ ...prev, [col.key]: "hover" }));
            }}
            onDragLeave={() => {
              setDropState((prev) => {
                const s = { ...prev };
                if (s[col.key] === "hover") s[col.key] = "";
                return s;
              });
            }}
          />
        ))}
      </div>

      {/* Feedback */}
      {feedback && (
        <div
          style={{
            textAlign: "center",
            padding: "10px",
            borderRadius: "10px",
            marginBottom: "16px",
            fontWeight: 700,
            fontSize: "0.9rem",
            background: feedback === "correct" ? "#d1fae5" : "#fee2e2",
            color: feedback === "correct" ? "#065f46" : "#991b1b",
            border: `1.5px solid ${feedback === "correct" ? "#a7f3d0" : "#fca5a5"}`,
          }}
        >
          {feedback === "correct"
            ? "✅ Jawaban benar! Lanjut ke soal berikutnya."
            : "❌ Masih ada yang kurang tepat, coba lagi!"}
        </div>
      )}

      {/* Ayat */}
      <div
        style={{
          fontFamily: "'Noto Naskh Arabic', serif",
          fontSize: "2rem",
          direction: "rtl",
          textAlign: "center",
          lineHeight: 1.9,
          background: "linear-gradient(135deg, #fafafa, #f3f4f6)",
          border: "1px solid #e5e7eb",
          borderRadius: "14px",
          padding: "20px 24px",
          marginBottom: "12px",
          boxShadow: "inset 0 2px 8px rgba(0,0,0,0.04)",
        }}
      >
        {renderVerse(q.verse)}
      </div>

      {/* Terjemahan */}
      <div
        style={{
          background: "#f9fafb",
          borderRadius: "10px",
          padding: "12px 16px",
          marginBottom: "20px",
          color: "#4b5563",
          fontSize: "0.85rem",
          fontStyle: "italic",
          textAlign: "center",
          lineHeight: 1.7,
          border: "1px solid #f3f4f6",
        }}
      >
        {q.translation}
      </div>

      {/* Tombol */}
      <div style={{ textAlign: "center" }}>
        <button
          onClick={handleCheck}
          disabled={!allDropped && feedback !== "correct"}
          style={{
            background:
              !allDropped && feedback !== "correct"
                ? "#d1d5db"
                : feedback === "correct"
                ? `linear-gradient(135deg, #10b981, #059669)`
                : `linear-gradient(135deg, ${game.color}, ${game.colorDark})`,
            color: "white",
            border: "none",
            padding: "12px 36px",
            borderRadius: "999px",
            fontSize: "1rem",
            fontWeight: 700,
            cursor: !allDropped && feedback !== "correct" ? "not-allowed" : "pointer",
            boxShadow:
              !allDropped && feedback !== "correct"
                ? "none"
                : `0 4px 20px ${game.color}55`,
            transition: "all 0.2s ease",
          }}
        >
          {feedback === "correct"
            ? qIndex + 1 >= totalQ
              ? "Lihat Hasil 🎉"
              : "Soal Berikutnya →"
            : "Periksa Jawaban"}
        </button>
      </div>
    </div>
  );
}

/* ============================================================
   KOMPONEN UTAMA QNahwu
   ============================================================ */

const QNahwu = () => {
  const [activeGame, setActiveGame] = useState(GAMES[0].id);
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  const currentGame = GAMES.find((g) => g.id === activeGame) || GAMES[0];

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%)",
      }}
    >
      <Navbar />
      <div
        style={{
          display: "flex",
          height: "100vh",
          paddingTop: "72px",
          fontFamily: "'Inter', 'Segoe UI', sans-serif",
        }}
      >
        {/* ── Sidebar ── */}
        <aside
          style={{
            width: isSidebarOpen ? "260px" : "0",
            minWidth: isSidebarOpen ? "260px" : "0",
            overflow: "hidden",
            background: "linear-gradient(180deg, #1e293b 0%, #0f172a 100%)",
            borderRight: "1px solid rgba(255,255,255,0.06)",
            display: "flex",
            flexDirection: "column",
            transition: "min-width 0.3s ease, width 0.3s ease",
          }}
        >
          {/* Header sidebar */}
          <div
            style={{
              padding: "24px 20px 16px",
              borderBottom: "1px solid rgba(255,255,255,0.08)",
            }}
          >
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: "10px",
                marginBottom: "4px",
              }}
            >
              <span style={{ fontSize: "1.4rem" }}>📖</span>
              <span
                style={{
                  fontWeight: 800,
                  fontSize: "1.05rem",
                  color: "#f8fafc",
                  letterSpacing: "-0.01em",
                }}
              >
                Jamid Mabny
              </span>
            </div>
            <p
              style={{
                color: "#64748b",
                fontSize: "0.72rem",
                margin: 0,
              }}
            >
              Game Drag & Drop Interaktif
            </p>
          </div>

          {/* Menu items */}
          <nav style={{ padding: "12px 10px", flex: 1, overflowY: "auto" }}>
            {GAMES.map((game) => {
              const isActive = activeGame === game.id;
              return (
                <button
                  key={game.id}
                  onClick={() => setActiveGame(game.id)}
                  style={{
                    width: "100%",
                    display: "flex",
                    alignItems: "center",
                    gap: "12px",
                    padding: "10px 14px",
                    borderRadius: "10px",
                    border: "none",
                    cursor: "pointer",
                    marginBottom: "4px",
                    background: isActive
                      ? `linear-gradient(135deg, ${game.color}33, ${game.color}18)`
                      : "transparent",
                    borderLeft: isActive
                      ? `3px solid ${game.color}`
                      : "3px solid transparent",
                    transition: "all 0.18s ease",
                  }}
                >
                  <span
                    style={{
                      width: "32px",
                      height: "32px",
                      borderRadius: "8px",
                      background: isActive
                        ? `linear-gradient(135deg, ${game.color}, ${game.colorDark})`
                        : "rgba(255,255,255,0.07)",
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                      fontSize: "1rem",
                      fontFamily: "'Noto Naskh Arabic', serif",
                      color: isActive ? "white" : "#94a3b8",
                      flexShrink: 0,
                      transition: "all 0.18s ease",
                    }}
                  >
                    {game.icon}
                  </span>
                  <span
                    style={{
                      fontWeight: isActive ? 700 : 500,
                      fontSize: "0.88rem",
                      color: isActive ? "#f1f5f9" : "#94a3b8",
                      transition: "color 0.18s ease",
                    }}
                  >
                    {game.title}
                  </span>
                  {isActive && (
                    <span
                      style={{
                        marginLeft: "auto",
                        fontSize: "0.65rem",
                        background: game.color,
                        color: "white",
                        padding: "2px 7px",
                        borderRadius: "999px",
                        fontWeight: 700,
                      }}
                    >
                      {game.questions.length}Q
                    </span>
                  )}
                </button>
              );
            })}
          </nav>

          {/* Footer info */}
          <div
            style={{
              padding: "16px 20px",
              borderTop: "1px solid rgba(255,255,255,0.06)",
            }}
          >
            <p
              style={{
                color: "#475569",
                fontSize: "0.7rem",
                margin: 0,
                lineHeight: 1.6,
              }}
            >
              Seret chip jawaban ke kotak yang sesuai, lalu tekan <em>Periksa Jawaban</em>.
            </p>
          </div>
        </aside>

        {/* ── Toggle sidebar button ── */}
        <button
          onClick={() => setIsSidebarOpen((v) => !v)}
          style={{
            position: "fixed",
            left: isSidebarOpen ? "260px" : "0",
            top: "50%",
            transform: "translateY(-50%)",
            zIndex: 50,
            background: currentGame.color,
            color: "white",
            border: "none",
            width: "22px",
            height: "48px",
            borderRadius: isSidebarOpen ? "0 8px 8px 0" : "0 8px 8px 0",
            cursor: "pointer",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            fontSize: "0.6rem",
            boxShadow: "2px 0 12px rgba(0,0,0,0.15)",
            transition: "left 0.3s ease",
          }}
        >
          {isSidebarOpen ? "◀" : "▶"}
        </button>

        {/* ── Main Content ── */}
        <main
          style={{
            flex: 1,
            overflowY: "auto",
            padding: "32px clamp(16px, 4vw, 48px)",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <div style={{ width: "100%", maxWidth: "680px" }}>
            {/* Header game */}
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: "14px",
                marginBottom: "28px",
              }}
            >
              <div
                style={{
                  width: "48px",
                  height: "48px",
                  borderRadius: "14px",
                  background: `linear-gradient(135deg, ${currentGame.color}, ${currentGame.colorDark})`,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  fontSize: "1.5rem",
                  fontFamily: "'Noto Naskh Arabic', serif",
                  color: "white",
                  boxShadow: `0 4px 16px ${currentGame.color}66`,
                  flexShrink: 0,
                }}
              >
                {currentGame.icon}
              </div>
              <div>
                <h1
                  style={{
                    margin: 0,
                    fontSize: "1.4rem",
                    fontWeight: 800,
                    color: "#1e293b",
                    letterSpacing: "-0.02em",
                  }}
                >
                  Latihan {currentGame.title}
                </h1>
                <p
                  style={{
                    margin: 0,
                    fontSize: "0.8rem",
                    color: "#64748b",
                  }}
                >
                  Identifikasi sifat kata yang disorot dalam ayat Al-Quran
                </p>
              </div>
            </div>

            {/* Card game */}
            <div
              style={{
                background: "white",
                borderRadius: "20px",
                padding: "28px",
                boxShadow:
                  "0 4px 6px rgba(0,0,0,0.04), 0 10px 40px rgba(0,0,0,0.08)",
                border: "1px solid rgba(0,0,0,0.04)",
              }}
            >
              <GamePanel key={activeGame} game={currentGame} />
            </div>

            {/* Legend */}
            <div
              style={{
                marginTop: "20px",
                padding: "14px 18px",
                background: `${currentGame.colorLight}`,
                borderRadius: "12px",
                border: `1px solid ${currentGame.color}33`,
              }}
            >
              <p
                style={{
                  margin: "0 0 8px",
                  fontWeight: 700,
                  fontSize: "0.75rem",
                  color: currentGame.colorDark,
                  textTransform: "uppercase",
                  letterSpacing: "0.08em",
                }}
              >
                Legenda Pilihan
              </p>
              <div
                style={{
                  display: "flex",
                  flexWrap: "wrap",
                  gap: "6px",
                }}
              >
                {currentGame.optionGroups.flat().map((opt) => (
                  <span
                    key={opt.value}
                    style={{
                      fontSize: "0.72rem",
                      color: "#374151",
                      background: "white",
                      padding: "3px 10px",
                      borderRadius: "999px",
                      border: "1px solid #e5e7eb",
                    }}
                  >
                    {opt.label}
                  </span>
                ))}
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
};

export default QNahwu;
