/**
 * Interactive QTajwid Level 1 - Main Script
 * Handles logic for all 4 modules.
 */

document.addEventListener("DOMContentLoaded", () => {
  // --- GLOBAL VARIABLES ---
  const audioPlayer = document.getElementById("global-audio");

  // --- LEVEL MANAGER ---
  window.selectLevel = function (level) {
    document.getElementById("level-selection").style.display = "none";
    document.getElementById("app-view").style.display = "block";

    // Filter Tabs
    const allTabs = document.querySelectorAll(".nav-btn");
    let firstVisibleTab = null;

    allTabs.forEach((tab) => {
      if (tab.classList.contains(`level-${level}`)) {
        tab.style.display = "flex";
        if (!firstVisibleTab) firstVisibleTab = tab;
      } else {
        tab.style.display = "none";
      }
    });

    // Update Header Info
    document.getElementById("level-subtitle").textContent = `Level ${level}`;

    // Click first tab
    if (firstVisibleTab) firstVisibleTab.click();
  };

  window.goHome = function () {
    document.getElementById("app-view").style.display = "none";
    document.getElementById("level-selection").style.display = "block";

    // Stop any active audio/game
    audioPlayer.pause();
  };

  // --- TAB NAVIGATION ---
  const tabs = document.querySelectorAll(".nav-btn");
  const contents = document.querySelectorAll(".tab-content");

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      // Remove active class from all
      tabs.forEach((t) => t.classList.remove("active"));
      contents.forEach((c) => c.classList.remove("active"));

      // Add active class to clicked
      tab.classList.add("active");
      const targetId = tab.dataset.tab;
      document.getElementById(targetId).classList.add("active");

      // Initialize module if needed (lazy load logic could go here)
      if (targetId === "module1") initModule1();
      if (targetId === "module2") initModule2();
      if (targetId === "module3") initModule3();
      if (targetId === "module4") initModule4();
      if (targetId === "module5") initModule5();
      if (targetId === "module6") initModule6();
      if (targetId === "module7") initModule7();
      if (targetId === "module8") initModule8();
      if (targetId === "module9") initModule9();
      if (targetId === "module10") initModule10();
      if (targetId === "module11") initModule11();
      if (targetId === "module12") initModule12();
      // Level 3
      if (targetId === "module13") initModule13();
      if (targetId === "module14") initModule14();
      if (targetId === "module15") initModule15();
      if (targetId === "module16") initModule16();
      if (targetId === "module17") initModule17();
      if (targetId === "module18") initModule18();
      if (targetId === "module19") initModule19();
      if (targetId === "module20") initModule20();
      if (targetId === "module21") initModule21();
    });
  });

  // ... (rest of audio helper, etc) ...

  // (After module 20 logic is actually where I should append, but I will append to end of file and update the initModule router in a separate small edit if needed, or I can just assume the router edit above is sufficient context)
  // Wait, I need to verify where the router logic is. It is around line 79.
  // I will append the NEW module logic at the end of the file, and then I might need another edit to update the router loop if I can't reach it easily.
  // Actually, I can just append the function `initModule21` at the end on line ~1320, but I MUST also update the router which is at line 79.
  // The previous edit to `index.html` added `data-tab="module21"`.
  // The `initModule` calls are inside `tabs.forEach`.

  // Strategy:
  // 1. Append `initModule21` function at the end of `script.js`.
  // 2. Update the router loop to call `initModule21`.

  // Let's do step 1 (Append function) first.

  // --- AUDIO HELPER ---
  function playSound(soundName, textFallback) {
    const audioPlayer = document.getElementById("global-audio");

    // 1. Stop any currently playing audio
    audioPlayer.pause();
    audioPlayer.currentTime = 0;

    // 2. Try Local Audio First
    const audioPath = `audio/${soundName}.mp3`;
    audioPlayer.src = audioPath;

    // Show "Loading" feedback immediately
    showAudioToast("Memuat...", "info");

    const playPromise = audioPlayer.play();

    if (playPromise !== undefined) {
      playPromise
        .then(() => {
          // Success local
          showAudioToast("Memutar", "success");
        })
        .catch((err) => {
          // Local failed, try TTS
          console.warn(`Local audio missing for: ${soundName}. Trying TTS...`);

          if (textFallback) {
            showAudioToast("Mengambil dari Google...", "warning");
            playTTS(textFallback, audioPlayer);
          } else {
            showAudioToast("Audio tidak ditemukan", "error");
          }
        });
    }
  }

  function playTTS(text, player) {
    const ttsUrl = `https://translate.google.com/translate_tts?ie=UTF-8&tl=ar&client=tw-ob&q=${encodeURIComponent(
      text
    )}`;
    player.src = ttsUrl;

    player
      .play()
      .then(() => {
        showAudioToast("Info: Menggunakan TTS (Online)", "success");
      })
      .catch((e) => {
        console.error("TTS Failed:", e);
        showAudioToast("Gagal memutar. Cek internet!", "error");
      });
  }

  // --- TOAST FEEDBACK ---
  function showAudioToast(msg, type) {
    let toast = document.getElementById("audio-toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "audio-toast";
      // Styling
      Object.assign(toast.style, {
        position: "fixed",
        bottom: "80px", // slightly higher to avoid mobile navs
        left: "50%",
        transform: "translateX(-50%)",
        backgroundColor: "rgba(30, 41, 59, 0.95)",
        color: "#fff",
        padding: "10px 20px",
        borderRadius: "50px",
        boxShadow: "0 4px 15px rgba(0,0,0,0.3)",
        zIndex: "10000",
        fontSize: "0.9rem",
        fontFamily: "sans-serif",
        transition: "all 0.3s ease",
        opacity: "0",
        pointerEvents: "none",
      });
      document.body.appendChild(toast);
    }

    // Color based on type
    if (type === "error") toast.style.backgroundColor = "#EF4444";
    else if (type === "warning") toast.style.backgroundColor = "#F59E0B";
    else toast.style.backgroundColor = "#EAB308"; // Default/Success Yellow

    toast.textContent = msg;
    toast.style.opacity = "1";
    toast.style.transform = "translateX(-50%) translateY(0)";

    // Clear previous timeout
    if (window.audioToastTimeout) clearTimeout(window.audioToastTimeout);

    // Hide after timer
    window.audioToastTimeout = setTimeout(() => {
      toast.style.opacity = "0";
      toast.style.transform = "translateX(-50%) translateY(10px)";
    }, 2000);
  }

  // ==========================================
  // MODULE 1: KLIK & DENGAR
  // ==========================================
  let module1Initialized = false;
  function initModule1() {
    if (module1Initialized) return;

    const grid = document.getElementById("letter-grid");
    grid.innerHTML = ""; // Clear existing

    hijaiyahSounds.forEach((item) => {
      const btn = document.createElement("div");
      btn.className = "letter-btn";
      btn.textContent = item.text;
      btn.title = item.name; // Tooltip

      btn.addEventListener("click", () => {
        // Visual feedback
        btn.style.borderColor = "var(--primary-color)";
        btn.style.backgroundColor = "#ECFDF5";
        setTimeout(() => {
          btn.style.borderColor = "";
          btn.style.backgroundColor = "";
        }, 500);

        playSound(item.sound, item.text);
      });

      grid.appendChild(btn);
    });

    module1Initialized = true;
  }

  // ==========================================
  // MODULE 2: TEBAK SUARA
  // ==========================================
  let quizScore = 0;
  let quizTotal = 0;
  let quizCurrentTarget = null;
  let quizIsProcessing = false;

  function initModule2() {
    startQuizRound();
  }

  function startQuizRound() {
    if (quizIsProcessing) return;

    const feedback = document.getElementById("quiz-feedback");
    feedback.textContent = "";
    feedback.className = "feedback-msg";

    // 1. Pick 3 random items
    const shuffled = [...hijaiyahSounds].sort(() => 0.5 - Math.random());
    const options = shuffled.slice(0, 3);

    // 2. Pick 1 winner
    quizCurrentTarget = options[Math.floor(Math.random() * options.length)];

    // 3. Render
    const container = document.getElementById("quiz-options");
    container.innerHTML = "";

    options.forEach((opt) => {
      const btn = document.createElement("div");
      btn.className = "quiz-option";
      btn.textContent = opt.text;

      btn.onclick = () => handleQuizAnswer(btn, opt);
      container.appendChild(btn);
    });

    // 4. Auto play sound
    setTimeout(
      () =>
        playSound(
          quizCurrentTarget.sound || quizCurrentTarget.soundAlt,
          quizCurrentTarget.text
        ),
      500
    );

    // Bind Play Button
    document.getElementById("quiz-play-btn").onclick = () => {
      if (quizCurrentTarget)
        playSound(
          quizCurrentTarget.sound || quizCurrentTarget.soundAlt,
          quizCurrentTarget.text
        );
    };
  }

  function handleQuizAnswer(btnElement, selection) {
    if (quizIsProcessing) return;

    const feedback = document.getElementById("quiz-feedback");
    const options = document.querySelectorAll(".quiz-option");

    quizTotal++;
    document.getElementById("quiz-total").textContent = quizTotal;

    if (selection.text === quizCurrentTarget.text) {
      // Correct
      quizScore++;
      document.getElementById("quiz-score").textContent = quizScore;

      btnElement.classList.add("correct");
      feedback.textContent = "Benar! Masha Allah 🌟";
      feedback.style.color = "var(--success)";

      quizIsProcessing = true;
      playSound("correct_sfx"); // Optional logic for SFX, or just nothing

      setTimeout(() => {
        quizIsProcessing = false;
        startQuizRound();
      }, 1000); // Wait 1.5s
    } else {
      // Wrong
      btnElement.classList.add("wrong");
      feedback.textContent = "Coba lagi...";
      feedback.style.color = "var(--error)";

      // Play sound again as hint
      setTimeout(
        () =>
          playSound(
            quizCurrentTarget.sound || quizCurrentTarget.soundAlt,
            quizCurrentTarget.text
          ),
        500
      );
    }
  }

  // ==========================================
  // MODULE 3: SUSUN KATA
  // ==========================================
  let puzzleCurrentIndex = 0;

  function initModule3() {
    loadPuzzle(puzzleCurrentIndex);

    document.getElementById("puzzle-reset-btn").onclick = () =>
      loadPuzzle(puzzleCurrentIndex);
    document.getElementById("puzzle-next-btn").onclick = () => {
      puzzleCurrentIndex = (puzzleCurrentIndex + 1) % wordList.length;
      loadPuzzle(puzzleCurrentIndex);
    };
  }

  function loadPuzzle(index) {
    const item = wordList[index];
    const nextBtn = document.getElementById("puzzle-next-btn");
    const feedback = document.getElementById("puzzle-feedback");

    nextBtn.disabled = true;
    feedback.textContent = "";

    // Update UI Info
    document.getElementById("word-current").textContent = index + 1;
    document.getElementById("word-total").textContent = wordList.length;
    document.getElementById("target-word-arabic").textContent = item.word;
    document.getElementById("target-word-meaning").textContent = item.meaning;

    // Setup Drop Area
    const dropArea = document.getElementById("drop-area");
    dropArea.innerHTML = "";
    item.pieces.forEach((piece, i) => {
      const slot = document.createElement("div");
      slot.className = "drop-slot";
      slot.dataset.correct = piece.value; // Store expected ID
      dropArea.appendChild(slot);
    });

    // Setup Pieces Area (Shuffled)
    const piecesArea = document.getElementById("pieces-area");
    piecesArea.innerHTML = "";

    const shuffledPieces = [...item.pieces].sort(() => 0.5 - Math.random());
    shuffledPieces.forEach((piece) => {
      const p = document.createElement("div");
      p.className = "puzzle-piece";
      p.textContent = piece.text;
      p.dataset.val = piece.value;
      p.draggable = true;

      // Drag Events
      p.addEventListener("dragstart", (e) => {
        e.dataTransfer.setData("text/plain", piece.value);
        e.dataTransfer.effectAllowed = "move";
        setTimeout(() => p.classList.add("hidden"), 0); // Hide original while dragging
      });

      p.addEventListener("dragend", () => {
        p.classList.remove("hidden");
      });

      piecesArea.appendChild(p);
    });

    setupDropZones();
  }

  function setupDropZones() {
    const slots = document.querySelectorAll(".drop-slot");
    const piecesArea = document.getElementById("pieces-area");

    // Allow dropping back to pieces area
    piecesArea.ondragover = (e) => e.preventDefault();
    piecesArea.ondrop = (e) => {
      e.preventDefault();
      const val = e.dataTransfer.getData("text/plain");
      const piece = document.querySelector(`.puzzle-piece[data-val="${val}"]`);
      if (piece) piecesArea.appendChild(piece);
      checkPuzzleCompletion();
    };

    slots.forEach((slot) => {
      slot.ondragover = (e) => {
        e.preventDefault();
        slot.style.background = "#D1FAE5"; // Highlight
      };

      slot.ondragleave = () => {
        slot.style.background = "";
      };

      slot.ondrop = (e) => {
        e.preventDefault();
        slot.style.background = "";

        // If slot already has something, move it back to pieces area
        if (slot.children.length > 0) {
          piecesArea.appendChild(slot.firstElementChild);
        }

        const val = e.dataTransfer.getData("text/plain");
        const piece = document.querySelector(
          `.puzzle-piece[data-val="${val}"]`
        );
        if (piece) slot.appendChild(piece);

        checkPuzzleCompletion();
      };
    });
  }

  function checkPuzzleCompletion() {
    const slots = document.querySelectorAll(".drop-slot");
    let isFull = true;
    let isCorrect = true;

    slots.forEach((slot) => {
      if (slot.children.length === 0) {
        isFull = false;
        return;
      }
      const piece = slot.firstElementChild;
      if (piece.dataset.val !== slot.dataset.correct) {
        isCorrect = false;
      }
    });

    if (isFull) {
      const feedback = document.getElementById("puzzle-feedback");
      const nextBtn = document.getElementById("puzzle-next-btn");

      if (isCorrect) {
        feedback.textContent = "Benar! Luar biasa!";
        feedback.style.color = "var(--success)";
        nextBtn.disabled = false;

        // Play success audio
        const currentIndex = puzzleCurrentIndex;
        const item = wordList[currentIndex];
        playSound(item.audio, item.word);
      } else {
        feedback.textContent = "Belum tepat, ayo coba lagi.";
        feedback.style.color = "var(--error)";
      }
    }
  }

  // ==========================================
  // MODULE 4: CEK UCAPAN
  // ==========================================
  let recognition;
  let speechTarget = null;

  function initModule4() {
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      document.getElementById("browser-warning").style.display = "block";
      return;
    }

    recognition = new SpeechRecognition();
    recognition.lang = "ar-SA";
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.onstart = () => {
      const card = document.getElementById("speech-card-trigger");
      card.style.borderColor = "#F87171"; // Red border when recording
      card.style.boxShadow = "0 0 0 4px rgba(248, 113, 113, 0.2)";
      document.getElementById("speech-feedback").textContent =
        "Mendengarkan...";
      document.getElementById("speech-feedback").style.color =
        "var(--text-muted)";
    };

    recognition.onend = () => {
      const card = document.getElementById("speech-card-trigger");
      card.style.borderColor = "";
      card.style.boxShadow = "";
    };

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      validateSpeech(transcript);
    };

    recognition.onerror = (e) => {
      document.getElementById("speech-feedback").textContent =
        "Error: " + e.error;
      document.getElementById("speech-feedback").style.color = "var(--error)";
    };

    // Buttons
    document.getElementById("speech-card-trigger").onclick = (e) => {
      // Prevent triggering if clicked on the play sample button which is inside
      if (e.target.id === "speech-play-sample") return;
      try {
        recognition.start();
      } catch (e) {}
    };

    document.getElementById("speech-next-btn").onclick = setupNewSpeechTarget;

    document.getElementById("speech-play-sample").onclick = () => {
      if (speechTarget)
        playSound(
          speechTarget.sound || speechTarget.soundAlt,
          speechTarget.text
        );
    };

    setupNewSpeechTarget();
  }

  function setupNewSpeechTarget() {
    // Pick random letter from database
    speechTarget =
      hijaiyahSounds[Math.floor(Math.random() * hijaiyahSounds.length)];

    document.getElementById("speech-target").textContent = speechTarget.text;
    document.getElementById("speech-feedback").textContent = "";
    document.getElementById("speech-feedback").style.color =
      "var(--text-muted)";
  }

  function validateSpeech(input) {
    // document.getElementById('speech-status').textContent = `Terdengar: "${input}"`;

    // Simple normalization
    const cleanInput = normalizeArabic(input);
    const cleanTarget = normalizeArabic(speechTarget.text);

    const feedback = document.getElementById("speech-feedback");

    if (cleanInput === cleanTarget) {
      feedback.textContent = "Masha Allah! Pengucapan Benar!";
      feedback.style.color = "var(--success)";
      playSound("correct_sfx"); // Optional
    } else {
      feedback.textContent = "Kurang pas, coba lagi ya.";
      feedback.style.color = "var(--error)";
    }
  }

  function normalizeArabic(text) {
    if (!text) return "";
    // Remove harakat
    let normalized = text.replace(/[\u064B-\u0652]/g, "");
    // Normalize Alif
    normalized = normalized.replace(/[أإآ]/g, "ا");
    return normalized.trim();
  }

  // --- INITIALIZE FIRST TAB ---
  initModule1(); // Default active tab

  // ==========================================
  // MODULE 5: MAD PANJANG
  // ==========================================
  function initModule5() {
    const container = document.getElementById("mad-container");
    if (container.children.length > 0) return; // Recently initialized

    // madPanjangWords is from data.js
    madPanjangWords.forEach((item) => {
      const row = document.createElement("div");
      row.className = "word-parts-container";

      // Reversing for visual display in LTR container if needed, but flex-direction: rtl handles it.
      // Data parts are ordered: [Part1, Part2] -> RTL displays Part1 (Right) then Part2 (Left).
      item.parts.forEach((part) => {
        const btn = document.createElement("div");
        btn.className = "word-part-btn";
        btn.textContent = part.text;

        btn.onclick = () => {
          if (part.isMad) {
            btn.classList.add("correct-mad");
            document.getElementById("mad-feedback").textContent =
              "Benar! Ini Mad Thabi'i (Panjang)";
            document.getElementById("mad-feedback").style.color =
              "var(--success)";
            playSound(null, item.transliteration); // Fallback to TTS whole word or part? TTS whole word is better.
          } else {
            btn.classList.add("wrong-mad");
            document.getElementById("mad-feedback").textContent =
              "Bukan, ini dibaca pendek.";
            document.getElementById("mad-feedback").style.color =
              "var(--error)";
            setTimeout(() => btn.classList.remove("wrong-mad"), 600);
          }
        };
        row.appendChild(btn);
      });

      // Translation label
      const label = document.createElement("div");
      label.className = "text-translation";
      label.textContent = item.translation;
      label.style.textAlign = "center";
      label.style.width = "100%";

      const wrapper = document.createElement("div");
      wrapper.style.marginBottom = "20px";
      wrapper.appendChild(row);
      wrapper.appendChild(label);

      container.appendChild(wrapper);
    });
  }

  // ==========================================
  // MODULE 6: TANWIN, SUKUN, TASYDID
  // ==========================================
  function initModule6() {
    const grid = document.getElementById("diacritic-grid");
    if (grid.children.length > 0) return;

    const btnTanwin = document.getElementById("btn-tanwin");
    const btnSukun = document.getElementById("btn-sukun");
    const btnTasydid = document.getElementById("btn-tasydid");
    const buttons = [btnTanwin, btnSukun, btnTasydid];

    function renderSet(dataset) {
      grid.innerHTML = "";
      dataset.forEach((item) => {
        const card = document.createElement("div");
        card.className = "sound-card";

        const text = document.createElement("span");
        text.className = "arabic-lg";
        text.textContent = item.text;

        const sub = document.createElement("span");
        sub.className = "text-transliteration";
        sub.textContent = item.sound; // name of sound e.g. 'ban'

        card.appendChild(text);
        card.appendChild(sub);

        card.onclick = () => {
          card.classList.add("playing");
          playSound(null, item.text); // Use TTS
          // Original used local files like 'ban.mp3', fallback handled by playSound
          setTimeout(() => card.classList.remove("playing"), 1000);
        };

        grid.appendChild(card);
      });
    }

    // Event Listeners
    btnTanwin.onclick = () => {
      setActiveBtn(btnTanwin);
      renderSet(tanwinData);
    };
    btnSukun.onclick = () => {
      setActiveBtn(btnSukun);
      renderSet(sukunData);
    };
    btnTasydid.onclick = () => {
      setActiveBtn(btnTasydid);
      renderSet(tasydidData);
    };

    function setActiveBtn(active) {
      buttons.forEach((b) => {
        b.classList.remove("btn-primary");
        b.classList.add("btn-secondary");
      });
      active.classList.remove("btn-secondary");
      active.classList.add("btn-primary");
    }

    // Default
    btnTanwin.click();
  }

  // ==========================================
  // MODULE 7: QALQALAH
  // ==========================================
  let qalqalahScore = 0;
  function initModule7() {
    const container = document.getElementById("qalqalah-container");
    if (container.children.length > 0) return;

    qalqalahWords.forEach((item) => {
      const wrapper = document.createElement("div");
      wrapper.style.marginBottom = "20px";
      wrapper.style.textAlign = "center";

      const row = document.createElement("div");
      row.className = "word-parts-container";

      item.parts.forEach((part) => {
        const btn = document.createElement("div");
        btn.className = "word-part-btn";
        btn.textContent = part.text;

        btn.onclick = () => {
          if (part.isQalqalah) {
            if (!btn.classList.contains("correct-mad")) {
              qalqalahScore += 10;
              document.getElementById("qalqalah-score").textContent =
                qalqalahScore;
            }
            btn.classList.add("correct-mad");
            playSound(null, item.arabicText);
          } else {
            btn.classList.add("wrong-mad");
            setTimeout(() => btn.classList.remove("wrong-mad"), 600);
          }
        };
        row.appendChild(btn);
      });

      const meaning = document.createElement("div");
      meaning.className = "text-transliteration";
      meaning.textContent = item.meaning + " (" + item.type + ")";

      wrapper.appendChild(row);
      wrapper.appendChild(meaning);
      container.appendChild(wrapper);
    });
  }

  // ==========================================
  // MODULE 8: GHUNNAH
  // ==========================================
  function initModule8() {
    const container = document.getElementById("ghunnah-container");
    if (container.children.length > 0) return;

    // Combine for display or separate? Let's show categorized.
    const categories = [
      { title: "Nun Tasydid", data: ghunnahData.nun },
      { title: "Mim Tasydid", data: ghunnahData.mim },
      { title: "Perbandingan (Bukan Ghunnah)", data: ghunnahData.comparison },
    ];

    categories.forEach((cat) => {
      const catBox = document.createElement("div");
      catBox.className = "aliflam-card"; // Reuse card style

      const title = document.createElement("h3");
      title.textContent = cat.title;
      title.style.color = "var(--primary-dark)";
      catBox.appendChild(title);

      const list = document.createElement("div");
      list.style.display = "flex";
      list.style.flexWrap = "wrap";
      list.style.gap = "10px";
      list.style.justifyContent = "center";

      cat.data.forEach((item) => {
        const btn = document.createElement("button");
        btn.className = "nav-btn"; // reuse
        btn.textContent = item.text;
        btn.onclick = () => playSound(null, item.text);

        const ref = document.createElement("span");
        ref.textContent = item.ref;
        ref.style.fontSize = "0.7em";
        ref.style.display = "block";
        ref.style.color = "#999";

        const wrapper = document.createElement("div");
        wrapper.appendChild(btn);
        wrapper.appendChild(ref);
        list.appendChild(wrapper);
      });

      catBox.appendChild(list);
      container.appendChild(catBox);
    });
  }

  // ==========================================
  // MODULE 9: ALIF LAM
  // ==========================================
  let alifLamIndex = 0;
  let alifLamScore = 0;
  function initModule9() {
    loadAlifLamQuestion();

    document.getElementById("btn-qamariyah").onclick = () =>
      checkAlifLam("Qamariyah");
    document.getElementById("btn-syamsiyah").onclick = () =>
      checkAlifLam("Syamsiyah");
  }

  function loadAlifLamQuestion() {
    const item = alifLamQuiz[alifLamIndex];
    document.getElementById("aliflam-arabic").textContent = item.example;
    document.getElementById("aliflam-latin").textContent = item.pronunciation;
    document.getElementById("aliflam-feedback").textContent = "";
  }

  function checkAlifLam(answer) {
    const item = alifLamQuiz[alifLamIndex];
    const feedback = document.getElementById("aliflam-feedback");

    if (item.answer === answer) {
      alifLamScore += 10;
      document.getElementById("aliflam-score").textContent = alifLamScore;
      feedback.textContent = "Benar! " + item.answer;
      feedback.style.color = "var(--success)";
      playSound(null, item.arabicText);

      setTimeout(() => {
        alifLamIndex = (alifLamIndex + 1) % alifLamQuiz.length;
        loadAlifLamQuestion();
      }, 1000);
    } else {
      feedback.textContent = "Salah... Coba lagi.";
      feedback.style.color = "var(--error)";
    }
  }

  // ==========================================
  // MODULE 10: WAQAF QUIZ
  // ==========================================
  let waqafQuizIndex = 0;
  let waqafScore = 0;
  let waqafTimer = 30;
  let waqafInterval;

  function initModule10() {
    startWaqafQuiz();
  }

  function startWaqafQuiz() {
    // Reset
    waqafScore = 0;
    waqafQuizIndex = 0;
    waqafTimer = 30;
    document.getElementById("waqaf-score").textContent = waqafScore;
    clearInterval(waqafInterval);

    loadWaqafQuestion();
    waqafInterval = setInterval(() => {
      waqafTimer--;
      document.getElementById("waqaf-timer").textContent = waqafTimer;
      if (waqafTimer <= 0) {
        clearInterval(waqafInterval);
        alert("Waktu Habis! Skor Akhir: " + waqafScore);
        startWaqafQuiz(); // Restart
      }
    }, 1000);
  }

  function loadWaqafQuestion() {
    const item = waqafQuiz[waqafQuizIndex];
    document.getElementById("waqaf-sign-display").textContent = item.sign;
    document.getElementById("waqaf-name-display").textContent = "???"; // Hide name

    const optionsContainer = document.getElementById("waqaf-options");
    optionsContainer.innerHTML = "";

    // Mix correct + incorrect
    const choices = [item.correctAnswer, ...item.incorrectAnswers].sort(
      () => 0.5 - Math.random()
    );

    choices.forEach((choice) => {
      const btn = document.createElement("div");
      btn.className = "quiz-option";
      btn.style.fontSize = "1rem"; // Smaller font for text choices
      btn.style.fontFamily = "var(--font-ui)";
      btn.textContent = choice;

      btn.onclick = () => {
        if (choice === item.correctAnswer) {
          btn.classList.add("correct");
          waqafScore += 10;
          document.getElementById("waqaf-score").textContent = waqafScore;
          document.getElementById("waqaf-name-display").textContent = item.name;
          playSound(null, item.explanationArab); // Play explanation

          setTimeout(() => {
            waqafQuizIndex = (waqafQuizIndex + 1) % waqafQuiz.length;
            loadWaqafQuestion();
          }, 1500);
        } else {
          btn.classList.add("wrong");
          waqafTimer -= 2; // Penalty
        }
      };
      optionsContainer.appendChild(btn);
    });
  }

  // ==========================================
  // MODULE 11: WAQAF LATIHAN
  // ==========================================
  function initModule11() {
    const grid = document.getElementById("waqaf-practice-grid");
    if (grid.children.length > 0) return;

    Object.keys(waqafPracticeData).forEach((key) => {
      const item = waqafPracticeData[key];

      const card = document.createElement("div");
      card.className = "sound-card";

      const text = document.createElement("span");
      text.className = "arabic-lg";
      text.textContent = item.text;

      const sub = document.createElement("span");
      sub.className = "text-transliteration";
      sub.textContent = "Klik untuk dengar";

      card.appendChild(text);
      card.appendChild(sub);

      card.onclick = () => {
        // Play normal then waqaf
        card.classList.add("playing");
        sub.textContent = "Normal: " + item.normal;
        playSound(null, item.arabic);

        setTimeout(() => {
          sub.textContent = "Waqaf: " + item.waqaf;
          // Heuristic TTS for waqaf: try to pronounce just the waqaf simplified text if possible,
          // but google TTS might pronounce harakat.
          // For now, re-play same but different prompt or just local file fallback
          // Original app used local files key.mp3
          playSound(key, item.waqaf);
          card.classList.remove("playing");
        }, 2500);
      };

      grid.appendChild(card);
    });
  }

  // ==========================================
  // MODULE 12: MUQATTA'AH
  // ==========================================
  function initModule12() {
    const grid = document.getElementById("muqattaah-grid");
    if (grid.children.length > 0) return;

    muqattaahData.forEach((item) => {
      const btn = document.createElement("div");
      btn.className = "letter-btn muqattaah-btn";

      const text = document.createElement("span");
      text.className = "muqattaah-text";
      text.textContent = item.text;

      const info = document.createElement("span");
      info.className = "surah-info";
      info.textContent = item.info;

      btn.appendChild(text);
      btn.appendChild(info);

      btn.onclick = () => {
        // Play individual letters names concatenated
        // Or try text. Original used: playSound('aliflammim') etc.
        // We'll try to construct a TTS query for letter names: "Alif Lam Mim"
        const prompt = item.transliteration;
        playSound(item.letters.replace(/ /g, ""), prompt);
      };

      grid.appendChild(btn);
    });
  }

  // ==========================================
  // MODULE 13: NUN SUKUN QUIZ
  // ==========================================
  let nunQuizIndex = 0;
  let nunQuizScore = 0;
  function initModule13() {
    // nunSukunQuiz from data.js (inside level3Data)
    if (typeof level3Data !== "undefined" && level3Data.nunSukunQuiz) {
      runGenericQuiz("nun", level3Data.nunSukunQuiz);
    } else {
      console.error("Data for Module 13 not found!");
    }
  }

  // ==========================================
  // MODULE 14: MIM SUKUN QUIZ
  // ==========================================
  let mimQuizIndex = 0;
  let mimQuizScore = 0;
  function initModule14() {
    if (typeof level3Data !== "undefined" && level3Data.mimSukunQuiz) {
      runGenericQuiz("mim", level3Data.mimSukunQuiz);
    } else {
      console.error("Data for Module 14 not found");
    }
  }

  // GENERIC QUIZ RUNNER (For Mod 13, 14, 17, 18)
  function runGenericQuiz(prefix, dataList) {
    const nextBtn = document.getElementById(`${prefix}-next-btn`);
    nextBtn.onclick = () => {
      if (prefix === "nun") {
        nunQuizIndex = (nunQuizIndex + 1) % dataList.length;
        loadNunQuestion(dataList);
      } else if (prefix === "mim") {
        mimQuizIndex = (mimQuizIndex + 1) % dataList.length;
        loadMimQuestion(dataList);
      } else if (prefix === "waqaf-adv") {
        waqafAdvIndex = (waqafAdvIndex + 1) % dataList.length;
        loadWaqafAdvQuestion(dataList);
      } else if (prefix === "mad-adv") {
        madAdvIndex = (madAdvIndex + 1) % dataList.length;
        loadMadAdvQuestion(dataList);
      }
    };

    if (prefix === "nun") loadNunQuestion(dataList);
    if (prefix === "mim") loadMimQuestion(dataList);
    if (prefix === "waqaf-adv") loadWaqafAdvQuestion(dataList);
    if (prefix === "mad-adv") loadMadAdvQuestion(dataList);
  }

  // --- NUN IMPLEMENTATION ---
  function loadNunQuestion(dataList) {
    // Fallback for previous impl calling without args
    const list =
      dataList ||
      (typeof level3Data !== "undefined" ? level3Data.nunSukunQuiz : []);
    if (!list || list.length === 0) return;

    const item = list[nunQuizIndex];
    document.getElementById("nun-example").textContent = item.arabicText; // fixed property name
    document.getElementById("nun-question").textContent =
      item.question || "Hukum bacaannya adalah?"; // fixed property

    const opts = document.getElementById("nun-options");
    opts.innerHTML = "";
    document.getElementById("nun-feedback").textContent = "";
    document.getElementById("nun-next-btn").style.display = "none";

    const allTypes = [
      "Izhar",
      "Idgham Bighunnah",
      "Idgham Bilaghunnah",
      "Iqlab",
      "Ikhfa",
    ]; // Matching data.js values
    const distractors = allTypes
      .filter((t) => t !== item.answer)
      .sort(() => 0.5 - Math.random())
      .slice(0, 3);
    const choices = [item.answer, ...distractors].sort(
      () => 0.5 - Math.random()
    );

    choices.forEach((c) => {
      const btn = document.createElement("div");
      btn.className = "quiz-option";
      btn.textContent = c;
      btn.onclick = () => {
        if (c === item.answer) {
          btn.classList.add("correct");
          nunQuizScore += 10;
          document.getElementById("nun-score").textContent = nunQuizScore;
          document.getElementById("nun-feedback").textContent = "Benar!";
          document.getElementById("nun-feedback").style.color =
            "var(--success)";
          playSound(null, item.arabicText);
          document.getElementById("nun-next-btn").style.display =
            "inline-block";
        } else {
          btn.classList.add("wrong");
          playSound("wrong_sfx");
        }
      };
      opts.appendChild(btn);
    });
  }

  // --- MIM IMPLEMENTATION ---
  function loadMimQuestion(dataList) {
    const list =
      dataList ||
      (typeof level3Data !== "undefined" ? level3Data.mimSukunQuiz : []);
    if (!list || list.length === 0) return;

    const item = list[mimQuizIndex];
    document.getElementById("mim-example").textContent = item.arabicText;
    document.getElementById("mim-question").textContent =
      item.question || "Hukum Mim Sukun ini?";

    const opts = document.getElementById("mim-options");
    opts.innerHTML = "";
    document.getElementById("mim-feedback").textContent = "";
    document.getElementById("mim-next-btn").style.display = "none";

    const allTypes = ["Ikhfa Syafawi", "Idgham Syafawi", "Izhar Syafawi"]; // Corrected values based on data.js
    const distractors = allTypes.filter((t) => t !== item.answer).slice(0, 2);
    const choices = [item.answer, ...distractors].sort(
      () => 0.5 - Math.random()
    );

    choices.forEach((c) => {
      const btn = document.createElement("div");
      btn.className = "quiz-option";
      btn.textContent = c;
      btn.onclick = () => {
        if (c === item.answer) {
          btn.classList.add("correct");
          mimQuizScore += 10;
          document.getElementById("mim-score").textContent = mimQuizScore;
          document.getElementById("mim-feedback").textContent = "Benar!";
          document.getElementById("mim-feedback").style.color =
            "var(--success)";
          playSound(null, item.arabicText);
          document.getElementById("mim-next-btn").style.display =
            "inline-block";
        } else {
          btn.classList.add("wrong");
        }
      };
      opts.appendChild(btn);
    });
  }

  // ==========================================
  // MODULE 15: RA TAFKHIM TARQIQ
  // ==========================================
  let raIndex = 0;
  function initModule15() {
    if (typeof level3Data === "undefined" || !level3Data.raTafkhimTarqiq)
      return;

    document.getElementById("btn-ra-tafkhim").onclick = () =>
      checkRa("Tafkhim");
    document.getElementById("btn-ra-tarqiq").onclick = () => checkRa("Tarqiq");
    document.getElementById("ra-next-btn").onclick = () => {
      raIndex = (raIndex + 1) % level3Data.raTafkhimTarqiq.length;
      loadRaQuestion();
    };
    loadRaQuestion();
  }

  function loadRaQuestion() {
    const item = level3Data.raTafkhimTarqiq[raIndex];
    document.getElementById("ra-example").textContent = item.arabicText;
    document.getElementById("ra-feedback").textContent = "";
    document.getElementById("ra-next-btn").style.display = "none";
    // Reset buttons style
    document.querySelectorAll("#module15 .choice-button").forEach((b) => {
      b.style.opacity = "1";
      b.style.transform = "none";
    });
  }

  function checkRa(ans) {
    const item = level3Data.raTafkhimTarqiq[raIndex];
    const feedback = document.getElementById("ra-feedback");

    if (ans === item.answer) {
      feedback.textContent = "Benar! " + (item.question || "");
      feedback.style.color = "var(--success)";
      playSound(null, item.arabicText);
      document.getElementById("ra-next-btn").style.display = "inline-block";
    } else {
      feedback.textContent = "Kurang tepat...";
      feedback.style.color = "var(--error)";
    }
  }

  // ==========================================
  // MODULE 16: LAM JALALAH
  // ==========================================
  let jalalahIndex = 0;
  function initModule16() {
    if (typeof level3Data === "undefined" || !level3Data.lamJalalah) return;

    document.getElementById("btn-jalalah-tafkhim").onclick = () =>
      checkJalalah("Tafkhim");
    document.getElementById("btn-jalalah-tarqiq").onclick = () =>
      checkJalalah("Tarqiq");
    document.getElementById("jalalah-next-btn").onclick = () => {
      jalalahIndex = (jalalahIndex + 1) % level3Data.lamJalalah.length;
      loadJalalahQuestion();
    };
    loadJalalahQuestion();
  }

  function loadJalalahQuestion() {
    const item = level3Data.lamJalalah[jalalahIndex];
    document.getElementById("jalalah-example").textContent = item.arabicText;
    document.getElementById("jalalah-question").textContent =
      item.question || "Bagaimana cara membaca Lam pada Lafaz Allah?"; // Use question from data
    document.getElementById("jalalah-feedback").textContent = "";
    document.getElementById("jalalah-next-btn").style.display = "none";
  }

  function checkJalalah(ans) {
    const item = level3Data.lamJalalah[jalalahIndex];
    const feedback = document.getElementById("jalalah-feedback");
    if (ans === item.answer) {
      feedback.textContent = "Benar!";
      feedback.style.color = "var(--success)";
      playSound(null, item.arabicText);
      document.getElementById("jalalah-next-btn").style.display =
        "inline-block";
    } else {
      feedback.textContent = "Salah... Perhatikan harakat sebelum Lafaz Allah.";
      feedback.style.color = "var(--error)";
    }
  }

  // ==========================================
  // MODULE 17: DRAG & DROP ARENA (Was 19)
  // ==========================================
  function initModule17() {
    if (typeof level3Data === "undefined" || !level3Data.tajwidDragDrop) return;
    const arena = document.getElementById("tajwid-drop-arena");
    const source = document.getElementById("tajwid-drag-source");

    // Reset
    if (arena) arena.innerHTML = "";
    if (source) source.innerHTML = "";
    document.getElementById("drag-feedback").textContent = "";
    document.getElementById("drag-reset-btn").onclick = initModule17;

    // Take 3 random items
    const subGame = level3Data.tajwidDragDrop
      .sort(() => 0.5 - Math.random())
      .slice(0, 3);
    const categories = [...new Set(subGame.map((x) => x.answer))];

    // Create Zones
    categories.forEach((cat) => {
      const zone = document.createElement("div");
      zone.className = "drop-zone";
      zone.dataset.cat = cat;

      const title = document.createElement("h4");
      title.textContent = cat;
      zone.appendChild(title);

      // Drop Events
      zone.ondragover = (e) => {
        e.preventDefault();
        zone.classList.add("highlight");
      };
      zone.ondragleave = () => zone.classList.remove("highlight");
      zone.ondrop = (e) => {
        e.preventDefault();
        zone.classList.remove("highlight");
        const id = e.dataTransfer.getData("text");
        const draggedEl = document.getElementById(id);
        if (draggedEl && draggedEl.dataset.cat === cat) {
          zone.classList.add("filled");
          zone.appendChild(draggedEl);
          draggedEl.draggable = false;
          draggedEl.style.cursor = "default";
          checkDragWin();
        } else {
          document.getElementById("drag-feedback").textContent =
            "Salah kamar... coba lagi!";
          document.getElementById("drag-feedback").style.color = "var(--error)";
          setTimeout(
            () => (document.getElementById("drag-feedback").textContent = ""),
            1500
          );
        }
      };
      arena.appendChild(zone);
    });

    // Create Draggables
    subGame.forEach((item, idx) => {
      const el = document.createElement("div");
      el.className = "drag-item";
      el.textContent = item.arabicText;
      el.id = "drag-item-" + idx;
      el.draggable = true;
      el.dataset.cat = item.answer;
      el.ondragstart = (e) => {
        e.dataTransfer.setData("text", el.id);
      };
      source.appendChild(el);
    });
  }

  function checkDragWin() {
    const source = document.getElementById("tajwid-drag-source");
    if (source.children.length === 0) {
      document.getElementById("drag-feedback").textContent =
        "Selamat! Semua benar!";
      document.getElementById("drag-feedback").style.color = "var(--success)";
      playSound("correct_sfx");
    }
  }

  // ==========================================
  // MODULE 18: SPEED QUIZ (Was 20)
  // ==========================================
  let speedTimer;
  let speedScore = 0;
  let speedLives = 3;
  let speedTimeLeft = 100;
  let speedGameActive = false;

  function initModule18() {
    document.getElementById("speed-start-btn").onclick = startSpeedGame;
  }

  function startSpeedGame() {
    if (typeof level3Data === "undefined" || !level3Data.tajwidSpeedQuiz)
      return;
    speedScore = 0;
    speedLives = 3;
    speedTimeLeft = 100;
    speedGameActive = true;

    document.getElementById("speed-start-screen").style.display = "none";
    document.getElementById("speed-game-area").style.display = "block";
    updateSpeedStats();

    // Timer Loop
    if (speedTimer) clearInterval(speedTimer);
    speedTimer = setInterval(() => {
      if (!speedGameActive) return;
      speedTimeLeft -= 0.2;
      document.getElementById("speed-timer-bar").style.width =
        speedTimeLeft + "%";
      if (speedTimeLeft < 30)
        document.getElementById("speed-timer-bar").classList.add("warning");
      else
        document.getElementById("speed-timer-bar").classList.remove("warning");
      if (speedTimeLeft <= 0) endGame("Waktu Habis!");
    }, 100);

    nextSpeedQuestion();
  }

  function nextSpeedQuestion() {
    if (!speedGameActive) return;
    const list = level3Data.tajwidSpeedQuiz;
    const q = list[Math.floor(Math.random() * list.length)];

    document.getElementById("speed-question").textContent = q.arabicText;
    const optsDiv = document.getElementById("speed-options");
    optsDiv.innerHTML = "";

    q.options.forEach((opt) => {
      const btn = document.createElement("div");
      btn.className = "quiz-option";
      btn.textContent = opt;
      btn.onclick = () => {
        if (opt === q.answer) {
          speedScore += 10;
          speedTimeLeft = Math.min(100, speedTimeLeft + 5);
          playSound(null, q.arabicText); // or correct_sfx
          nextSpeedQuestion();
        } else {
          speedLives--;
          document.getElementById("speed-game-area").classList.add("shake");
          setTimeout(
            () =>
              document
                .getElementById("speed-game-area")
                .classList.remove("shake"),
            300
          );
          if (speedLives <= 0) endGame("Game Over!");
          else nextSpeedQuestion();
        }
        updateSpeedStats();
      };
      optsDiv.appendChild(btn);
    });
  }

  function updateSpeedStats() {
    document.getElementById("speed-score").textContent = speedScore;
    document.getElementById("speed-lives").textContent = speedLives;
  }

  function endGame(msg) {
    speedGameActive = false;
    clearInterval(speedTimer);
    alert(msg + " Skor Akhir: " + speedScore);
    document.getElementById("speed-game-area").style.display = "none";
    document.getElementById("speed-start-screen").style.display = "block";
  }

  // ==========================================
  // MODULE 19: WAQAF ADVANCED (Was 17)
  // ==========================================
  let waqafAdvIndex = 0;
  function initModule19() {
    if (typeof level3Data !== "undefined" && level3Data.waqafQuizAdvanced) {
      runGenericQuiz("waqaf-adv", level3Data.waqafQuizAdvanced);
    }
  }
  // Helper: Waqaf Advanced Loader
  function loadWaqafAdvQuestion(dataList) {
    if (!dataList || dataList.length === 0) return;
    const item = dataList[waqafAdvIndex];

    document.getElementById("waqaf-adv-example").textContent = item.word;
    const opts = document.getElementById("waqaf-adv-options");
    opts.innerHTML = "";
    document.getElementById("waqaf-adv-feedback").textContent = "";
    document.getElementById("waqaf-adv-next-btn").style.display = "none";

    const choices = [item.stoppedWord, ...item.wrongOptions].sort(
      () => 0.5 - Math.random()
    );

    choices.forEach((c) => {
      const btn = document.createElement("div");
      btn.className = "quiz-option";
      btn.textContent = c;
      btn.onclick = () => {
        if (c === item.stoppedWord) {
          btn.classList.add("correct");
          document.getElementById("waqaf-adv-feedback").textContent = "Benar!";
          document.getElementById("waqaf-adv-feedback").style.color =
            "var(--success)";
          playSound(null, item.arabicText);
          document.getElementById("waqaf-adv-next-btn").style.display =
            "inline-block";
        } else {
          btn.classList.add("wrong");
        }
      };
      opts.appendChild(btn);
    });
  }

  // ==========================================
  // MODULE 20: MAD TAMBAHAN
  // ==========================================
  let madAdvIndex = 0;
  function initModule20() {
    if (typeof level3Data !== "undefined" && level3Data.madTambahanQuiz) {
      runGenericQuiz("mad-adv", level3Data.madTambahanQuiz);
    }
  }

  // Helper: Mad Tambahan Loader
  function loadMadAdvQuestion(dataList) {
    if (!dataList || dataList.length === 0) return;
    const item = dataList[madAdvIndex];

    document.getElementById("mad-adv-example").textContent = item.example;
    document.getElementById("mad-adv-note").textContent = item.note || "";

    const opts = document.getElementById("mad-adv-options");
    opts.innerHTML = "";
    document.getElementById("mad-adv-feedback").textContent = "";
    document.getElementById("mad-adv-next-btn").style.display = "none";

    // Collect all possible answers to make distractors
    const allAnswers = [...new Set(dataList.map((x) => x.answer))];
    const distractors = allAnswers
      .filter((a) => a !== item.answer)
      .sort(() => 0.5 - Math.random())
      .slice(0, 3);
    const choices = [item.answer, ...distractors].sort(
      () => 0.5 - Math.random()
    );

    choices.forEach((c) => {
      const btn = document.createElement("div");
      btn.className = "quiz-option";
      btn.textContent = c;
      btn.onclick = () => {
        if (c === item.answer) {
          btn.classList.add("correct");
          document.getElementById("mad-adv-feedback").textContent = "Benar!";
          document.getElementById("mad-adv-feedback").style.color =
            "var(--success)";
          playSound(null, item.arabicText);
          document.getElementById("mad-adv-next-btn").style.display =
            "inline-block";
        } else {
          btn.classList.add("wrong");
        }
      };
      opts.appendChild(btn);
    });
  }

  function updateSpeedStats() {
    document.getElementById("speed-lives").textContent = speedLives;
    document.getElementById("speed-score").textContent = speedScore;
  }

  function endGame(reason) {
    speedGameActive = false;
    clearInterval(speedTimer);
    alert(`Game Over: ${reason}\nSkor Akhir: ${speedScore}`);
    document.getElementById("speed-start-screen").style.display = "block";
    document.getElementById("speed-game-area").style.display = "none";
  }

  // ==========================================
  // MODULE 21: LEVEL 4 - SIMULASI MEMBACA (AN-NAAS)
  // ==========================================
  function initModule21() {
    // Dependencies
    const surah = [
      {
        text: "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
        audio: "basmalah",
        completed: false,
      },
      {
        text: "قُلْ أَعُوذُ بِرَبِّ النَّاسِ",
        audio: "an-naas-1",
        completed: false,
      },
      { text: "مَلِكِ النَّاسِ", audio: "an-naas-2", completed: false },
      { text: "إِلَٰهِ النَّاسِ", audio: "an-naas-3", completed: false },
      {
        text: "مِن شَرِّ الْوَسْوَاسِ الْخَنَّاسِ",
        audio: "an-naas-4",
        completed: false,
      },
      {
        text: "الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ",
        audio: "an-naas-5",
        completed: false,
      },
      {
        text: "مِنَ الْجِنَّةِ وَالنَّاسِ",
        audio: "an-naas-6",
        completed: false,
      },
    ];

    let currentVerseIndex = -1;
    let recognition = null;

    // Setup Elements
    const verseListEl = document.getElementById("verse-list");
    const verseNumEl = document.getElementById("current-verse-number");
    const verseTextEl = document.getElementById("current-verse-text");
    const statusMessageEl = document.getElementById("l4-status-message");
    const resultDisplayEl = document.getElementById("l4-result-display");
    const recordBtn = document.getElementById("l4-record-button");
    const listenBtn = document.getElementById("l4-listen-button");

    // Check Speech API
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      statusMessageEl.textContent =
        "Browser tidak mendukung fitur suara (Gunakan Chrome).";
      recordBtn.disabled = true;
      return;
    }

    try {
      recognition = new SpeechRecognition();
      recognition.lang = "ar-SA";
      recognition.interimResults = false;
      recognition.maxAlternatives = 1;
    } catch (e) {
      console.error("Speech API Error", e);
    }

    // --- Functions ---
    function buildVerseList() {
      verseListEl.innerHTML = "";
      surah.forEach((verse, index) => {
        const item = document.createElement("div");
        item.className = "verse-item";
        // Inline style for verse items since they are dynamically created
        item.style.padding = "10px";
        item.style.marginBottom = "5px";
        item.style.borderRadius = "8px";
        item.style.cursor = "pointer";
        item.style.background = "rgba(255,255,255,0.05)";
        item.style.textAlign = "right";
        item.style.fontFamily = "var(--font-arabic)";
        item.style.fontSize = "1.2rem";
        item.style.border = "1px solid transparent";

        item.textContent = `(${index + 1}) ${verse.text.substring(0, 30)}...`;

        if (verse.completed) {
          item.style.color = "var(--success)";
          item.style.borderColor = "var(--success)";
          item.style.textDecoration = "line-through";
        }
        if (index === currentVerseIndex) {
          item.style.background = "rgba(245, 158, 11, 0.2)";
          item.style.color = "var(--accent-color)";
          item.style.fontWeight = "bold";
          item.style.border = "1px solid var(--primary-color)";
        }

        item.onclick = () => setActiveVerse(index);
        verseListEl.appendChild(item);
      });
    }

    function setActiveVerse(index) {
      currentVerseIndex = index;
      const verse = surah[index];
      verseNumEl.textContent = `Ayat ${index + 1} dari ${surah.length}`;
      verseTextEl.textContent = verse.text;
      resultDisplayEl.textContent = "";
      statusMessageEl.textContent = "Klik tombol mikrofon untuk merekam...";

      buildVerseList();
    }

    function normalizeArabic(text) {
      if (!text) return "";
      let normalized = text.replace(/[\u064B-\u065F]/g, ""); // Harakat
      normalized = normalized.replace(/[\u0610-\u061A]/g, ""); // Signs
      normalized = normalized.replace(/[أإآ]/g, "ا"); // Alif
      normalized = normalized.replace(/ى/g, "ي"); // Ya
      normalized = normalized.replace(/ة/g, "ه"); // Ha
      return normalized.replace(/\s/g, ""); // Spaces
    }

    function checkReading(transcript) {
      const verse = surah[currentVerseIndex];
      const target = normalizeArabic(verse.text);
      const input = normalizeArabic(transcript);

      console.log("Target:", target);
      console.log("Input:", input);

      if (input.includes(target) || target.includes(input)) {
        resultDisplayEl.textContent = `✔️ Benar! (Terdengar: ${transcript})`;
        resultDisplayEl.style.color = "var(--success)";
        verse.completed = true;
        playSound("correct_sfx"); // Optional

        setTimeout(() => {
          if (currentVerseIndex < surah.length - 1)
            setActiveVerse(currentVerseIndex + 1);
          else
            statusMessageEl.textContent = "Alhamdulillah! Selesai semua ayat.";
        }, 1500);
      } else {
        resultDisplayEl.textContent = `❌ Coba lagi. (Terdengar: ${transcript})`;
        resultDisplayEl.style.color = "var(--error)";
      }
    }

    // --- Event Listeners ---
    // --- Media Recorder Variables ---
    let mediaRecorder = null;
    let audioChunks = [];
    let playbackUrl = null;

    // --- Functions ---
    // ... buildVerseList ...

    function setActiveVerse(index) {
      currentVerseIndex = index;
      const verse = surah[index];
      verseNumEl.textContent = `Ayat ${index + 1} dari ${surah.length}`;
      verseTextEl.textContent = verse.text;
      resultDisplayEl.textContent = "";
      statusMessageEl.textContent = "Klik tombol mikrofon untuk merekam...";

      // cleanup previous recording
      if (playbackUrl) {
        URL.revokeObjectURL(playbackUrl);
        playbackUrl = null;
      }
      // Remove audio player if exists
      const prevPlayer = document.getElementById("user-playback");
      if (prevPlayer) prevPlayer.remove();

      buildVerseList();
    }

    // ... normalizeArabic ...
    // ... checkReading ...

    // --- Recording Logic ---
    async function startRecording() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({
          audio: true,
        });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];

        mediaRecorder.ondataavailable = (event) => {
          audioChunks.push(event.data);
        };

        mediaRecorder.onstop = () => {
          const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
          playbackUrl = URL.createObjectURL(audioBlob);

          // Create Playback control
          let playerBtn = document.getElementById("user-play-btn");
          if (!playerBtn) {
            playerBtn = document.createElement("button");
            playerBtn.id = "user-play-btn";
            playerBtn.className = "btn-secondary";
            playerBtn.textContent = "▶️ Dengar Suara Saya";
            playerBtn.style.marginTop = "10px";
            playerBtn.onclick = () => {
              const audio = new Audio(playbackUrl);
              audio.play();
            };
            resultDisplayEl.parentNode.appendChild(playerBtn);
          } else {
            playerBtn.style.display = "inline-block";
          }
        };

        mediaRecorder.start();
        try {
          recognition.start();
        } catch (e) {}
      } catch (err) {
        console.error("Mic Error:", err);
        statusMessageEl.textContent = "Gagal akses mikrofon (MediaRecorder).";
      }
    }

    function stopRecording() {
      if (mediaRecorder && mediaRecorder.state !== "inactive") {
        mediaRecorder.stop();
      }
      if (recognition) recognition.stop();
    }

    // --- Event Listeners ---
    // REPLACE previous recordBtn.onclick
    recordBtn.onclick = () => {
      if (currentVerseIndex === -1) return;

      // Check if currently recording (using class flag)
      if (recordBtn.classList.contains("recording")) {
        stopRecording();
        statusMessageEl.textContent = "Berhenti...";
      } else {
        startRecording();
      }
    };

    listenBtn.onclick = () => {
      if (currentVerseIndex === -1) return;
      playSound(surah[currentVerseIndex].audio);
    };

    // Recognition Events
    if (recognition) {
      recognition.onstart = () => {
        statusMessageEl.textContent = "Mendengarkan...";
        recordBtn.style.background = "var(--success)";
        recordBtn.classList.add("recording");
      };

      recognition.onend = () => {
        statusMessageEl.textContent = "Memproses...";
        recordBtn.style.background = "";
        recordBtn.classList.remove("recording");
        stopRecording(); // Ensure media recorder also stops
      };

      recognition.onresult = (e) => {
        const transcript = e.results[0][0].transcript;
        checkReading(transcript); // Defined previously
      };

      recognition.onerror = (e) => {
        statusMessageEl.textContent = "Error: " + e.error;
        stopRecording();
      };
    }

    // Initialize Call
    if (verseListEl && verseListEl.children.length === 0) {
      buildVerseList();
      setActiveVerse(0);
    }
  }
});
