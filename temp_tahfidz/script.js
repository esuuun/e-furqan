
let currentSurah = null;
let selectedAyahs = 'all'; // 'all' or array of numbers [1, 2, 5]

const surahSelect = document.getElementById('surahSelect');
const btnAyahSelector = document.getElementById('btnAyahSelector');
const ayahDropdown = document.getElementById('ayahDropdown');
const checkAll = document.getElementById('checkAll');
const ayahGrid = document.getElementById('ayahGrid');
const btnCloseAyahDropdown = document.getElementById('btnCloseAyahDropdown');
const btnLoadGame = document.getElementById('btnLoadGame');
const gameArea = document.getElementById('gameArea');

// --- Initialization ---
document.addEventListener('DOMContentLoaded', () => {
  // Debug Logging
  console.log('Initial Check - Type of quranData:', typeof quranData);
  if (typeof quranData !== 'undefined') {
    console.log('Is Array:', Array.isArray(quranData));
    console.log('Length:', Array.isArray(quranData) ? quranData.length : 'N/A');
  }

  if (typeof quranData !== 'undefined' && Array.isArray(quranData)) {
    populateSurahSelect();
  } else {
    console.error('Data Quran tidak ditemukan (Pastikan quran-data.js termuat).');
    surahSelect.innerHTML = '<option disabled>Gagal memuat data (Check script)</option>';
  }
});

function populateSurahSelect() {
  surahSelect.innerHTML = '<option value="" disabled selected>-- Pilih Surat --</option>';
  quranData.forEach((surah, index) => {
    const option = document.createElement('option');
    option.value = index;
    option.textContent = `${surah.id}. ${surah.name} (${surah.transliteration})`;
    surahSelect.appendChild(option);
  });
}

// --- Event Listeners ---

// 1. Surah Selection
surahSelect.addEventListener('change', (e) => {
  currentSurah = quranData[e.target.value];
  resetAyahSelection();
  renderAyahGrid();
});

// 2. Ayah Selector UI
btnAyahSelector.addEventListener('click', (e) => {
  e.stopPropagation();
  ayahDropdown.classList.toggle('hidden');
});

btnCloseAyahDropdown.addEventListener('click', () => {
  ayahDropdown.classList.add('hidden');
  updatebtnAyahSelectorLabel();
});

// Close dropdown if clicking outside
document.addEventListener('click', (e) => {
  if (!btnAyahSelector.contains(e.target) && !ayahDropdown.contains(e.target)) {
    ayahDropdown.classList.add('hidden');
    updatebtnAyahSelectorLabel();
  }
});

checkAll.addEventListener('change', (e) => {
  const checkboxes = ayahGrid.querySelectorAll('input[type="checkbox"]');
  checkboxes.forEach(cb => cb.checked = e.target.checked);
});

// 3. Start Game
btnLoadGame.addEventListener('click', () => {
  if (!currentSurah) {
    alert('Silakan pilih surat terlebih dahulu');
    return;
  }

  // Determine selected ayahs
  const checkboxes = Array.from(ayahGrid.querySelectorAll('input[type="checkbox"]:checked'));

  if (checkboxes.length === 0) {
    alert('Pilih minimal satu ayat');
    return;
  }

  // Map to 1-based index (value is index+1)
  const selectedIndices = checkboxes.map(cb => parseInt(cb.value));

  // Filter verses
  const versesToPlay = currentSurah.verses.filter(v => selectedIndices.includes(v.id));

  renderGame(versesToPlay);
});

// --- Ayah Grid Logic ---

function resetAyahSelection() {
  checkAll.checked = true;
  btnAyahSelector.textContent = 'Semua Ayat';
}

function renderAyahGrid() {
  ayahGrid.innerHTML = '';
  if (!currentSurah) return;

  currentSurah.verses.forEach(verse => {
    const label = document.createElement('label');
    const input = document.createElement('input');
    input.type = 'checkbox';
    input.value = verse.id;
    input.checked = true;

    // Update main Select All if one is unchecked
    input.addEventListener('change', () => {
      const allChecked = Array.from(ayahGrid.querySelectorAll('input[type="checkbox"]')).every(cb => cb.checked);
      checkAll.checked = allChecked;
    });

    label.appendChild(input);
    label.appendChild(document.createTextNode(verse.id));
    ayahGrid.appendChild(label);
  });
}

function updatebtnAyahSelectorLabel() {
  const checked = ayahGrid.querySelectorAll('input[type="checkbox"]:checked');
  const total = ayahGrid.querySelectorAll('input[type="checkbox"]').length;

  if (checked.length === total) {
    btnAyahSelector.textContent = 'Semua Ayat';
  } else if (checked.length === 0) {
    btnAyahSelector.textContent = 'Pilih Ayat';
  } else {
    btnAyahSelector.textContent = `${checked.length} Ayat Terpilih`;
  }
}

// --- Game Logic ---

function renderGame(verses) {
  gameArea.innerHTML = ''; // Clear

  verses.forEach(verse => {
    const words = splitArabicText(verse.text);

    if (words.length <= 15) {
      // Standard Card
      createAyatCard(verse);
    } else {
      // Split Card
      const chunkSize = 12; // 12 words per card
      let chunkIndex = 1;
      for (let i = 0; i < words.length; i += chunkSize) {
        const chunkText = words.slice(i, i + chunkSize).join(' ');
        const subVerse = {
          id: `${verse.id}.${chunkIndex}`,
          text: chunkText,
          originalId: verse.id // Keep original ID for audio
        };
        createAyatCard(subVerse);
        chunkIndex++;
      }
    }
  });
}

function createAyatCard(verse) {
  // Pad numbers for Audio URL (Use originalId if available for split cards)
  const targetId = verse.originalId || verse.id;
  const surahId = String(currentSurah.id).padStart(3, '0');
  const ayahId = String(targetId).padStart(3, '0');
  const audioUrl = `https://everyayah.com/data/Alafasy_64kbps/${surahId}${ayahId}.mp3`;

  const card = document.createElement('section');
  card.className = 'ayat-card';
  card.innerHTML = `
    <div class="header">
      <span class="badge">Ayat ${verse.id}</span>
      <div class="title">${currentSurah.name}</div>
    </div>
    <div class="ayatText" data-role="display">${verse.text}</div>
    <audio controls src="${audioUrl}" data-role="audio"></audio>
    <div class="controls">
      <button class="btn-replay" data-role="replay">🔁 Putar Ulang</button>
      <button class="btn-start" data-role="start">🎯 Mulai Latihan</button>
      <button class="btn-check" data-role="check">Cek Jawaban</button>
      <button class="btn-cancel" data-role="cancel">↩️ Lihat Ayat</button>
    </div>
    <div class="word-container" data-role="container"></div>
    <div class="result" data-role="result"></div>
  `;

  gameArea.appendChild(card);

  // Initialize Logic
  initCardLogic(card, verse.text);
}

// Helper to split Arabic text intelligently
function splitArabicText(text) {
  // Remove zero-width characters and extra spaces
  const cleanText = text.replace(/[\u200B-\u200D\uFEFF]/g, '').trim();
  // Split by whitespace
  return cleanText.split(/\s+/).filter(w => w.length > 0);
}

function initCardLogic(card, fullText) {
  const display = card.querySelector('[data-role="display"]');
  const audioEl = card.querySelector('[data-role="audio"]');
  const btnReplay = card.querySelector('[data-role="replay"]');
  const btnStart = card.querySelector('[data-role="start"]');
  const btnCheck = card.querySelector('[data-role="check"]');
  const btnCancel = card.querySelector('[data-role="cancel"]');
  const container = card.querySelector('[data-role="container"]');
  const result = card.querySelector('[data-role="result"]');

  // Logic Data
  const words = splitArabicText(fullText);

  // Audio Events
  audioEl.addEventListener('play', () => {
    display.style.opacity = '1';
  });

  audioEl.addEventListener('ended', () => {
    btnStart.classList.add('animate-bounce');
  });

  btnReplay.addEventListener('click', () => {
    audioEl.currentTime = 0;
    audioEl.play();
  });

  // Start Game / Next Level
  btnStart.addEventListener('click', () => {
    btnStart.classList.remove('animate-bounce');
    btnStart.style.display = 'none';
    display.style.display = 'none';
    btnCheck.style.display = 'inline-block';

    // Show Cancel Button
    if (btnCancel) {
      btnCancel.style.display = 'inline-block';
    }

    // Clear previous
    container.innerHTML = '';
    result.textContent = '';
    result.className = 'result';

    // Simple Shuffle
    const shuffled = shuffleArray([...words]);

    shuffled.forEach((word) => {
      const span = document.createElement('span');
      span.className = 'word';
      span.textContent = word;
      span.draggable = true;
      span.id = `w-${Math.random().toString(36).substr(2, 9)}`;

      // Drag Events
      span.addEventListener('dragstart', handleDragStart);
      span.addEventListener('dragover', handleDragOver);
      span.addEventListener('drop', handleDrop);
      // Touch Events
      span.addEventListener('touchstart', handleTouchStart, { passive: false });
      span.addEventListener('touchmove', handleTouchMove, { passive: false });
      span.addEventListener('touchend', handleTouchEnd);

      container.appendChild(span);
    });
  });

  // Cancel / Look at Verse
  if (btnCancel) {
    btnCancel.addEventListener('click', () => {
      container.innerHTML = '';
      result.textContent = '';
      display.style.display = 'block';
      btnStart.style.display = 'inline-block';
      btnCheck.style.display = 'none';
      btnCancel.style.display = 'none';
    });
  }

  btnCheck.addEventListener('click', () => {
    const currentOrder = Array.from(container.children).map(el => el.textContent).join(' ');

    // Verify
    const isCorrect = splitArabicText(currentOrder).join(' ') === words.join(' ');

    if (isCorrect) {
      result.textContent = '✅ Benar';
      result.className = 'result animate-fade-in text-green-600';
      display.style.display = 'block';
      container.innerHTML = '';

      btnStart.style.display = 'inline-block';
      btnStart.textContent = 'Main Lagi';
      btnCheck.style.display = 'none';
      btnCancel.style.display = 'none';
    } else {
      result.textContent = '❌ Masih belum tepat, ayo coba lagi.';
      result.className = 'result animate-fade-in text-red-600';
    }
  });
}

function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

// -- Drag and Drop Handlers --
let dragSrcEl = null;

function handleDragStart(e) {
  dragSrcEl = this;
  e.dataTransfer.effectAllowed = 'move';
  e.dataTransfer.setData('text/html', this.innerHTML);
  this.style.opacity = '0.4';
}

function handleDragOver(e) {
  if (e.preventDefault) e.preventDefault();
  e.dataTransfer.dropEffect = 'move';
  return false;
}

function handleDrop(e) {
  if (e.stopPropagation) e.stopPropagation();
  const target = e.target.closest('.word');

  if (dragSrcEl !== target && target) {
    // Swap logic
    const parent = target.parentNode;

    // Basic swap: insert dragSrc before target, or after if it was before
    // Easier: just swap content or swap DOM nodes.
    // Let's swap DOM nodes properly.

    // Get array of children
    const children = Array.from(parent.children);
    const idxSrc = children.indexOf(dragSrcEl);
    const idxTgt = children.indexOf(target);

    if (idxSrc < idxTgt) {
      parent.insertBefore(dragSrcEl, target.nextSibling);
    } else {
      parent.insertBefore(dragSrcEl, target);
    }
  }

  if (dragSrcEl) dragSrcEl.style.opacity = '1';
  return false;
}

// Touch support helpers (simple implementation)
let touchSrcEl = null;

function handleTouchStart(e) {
  touchSrcEl = this;
  this.style.opacity = '0.5';
}

function handleTouchMove(e) {
  e.preventDefault();
  // Needed to prevent scrolling while dragging
}

function handleTouchEnd(e) {
  if (touchSrcEl) touchSrcEl.style.opacity = '1';

  const touch = e.changedTouches[0];
  const target = document.elementFromPoint(touch.clientX, touch.clientY);
  const closestWord = target ? target.closest('.word') : null;

  if (closestWord && closestWord !== touchSrcEl && closestWord.parentNode === touchSrcEl.parentNode) {
    const parent = closestWord.parentNode;
    const children = Array.from(parent.children);
    const idxSrc = children.indexOf(touchSrcEl);
    const idxTgt = children.indexOf(closestWord);

    if (idxSrc < idxTgt) {
      parent.insertBefore(touchSrcEl, closestWord.nextSibling);
    } else {
      parent.insertBefore(touchSrcEl, closestWord);
    }
  }

  touchSrcEl = null;
}
