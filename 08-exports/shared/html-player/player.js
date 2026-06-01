(function () {
  const deck = window.LECTURE_DECK;
  let slideIndex = 0;

  const el = {
    module: document.querySelector('[data-module]'),
    lecture: document.querySelector('[data-lecture]'),
    slide: document.querySelector('[data-slide]'),
    audio: document.querySelector('[data-audio]'),
    transcript: document.querySelector('[data-transcript]'),
    sources: document.querySelector('[data-sources]'),
    progress: document.querySelector('[data-progress]'),
    prev: document.querySelector('[data-prev]'),
    next: document.querySelector('[data-next]'),
    replay: document.querySelector('[data-replay]')
  };

  function render({ autoplay = true } = {}) {
    const s = deck.slides[slideIndex];
    el.module.textContent = deck.module;
    el.lecture.textContent = deck.lecture;
    const listTag = s.ordered ? 'ol' : 'ul';
    const steps = s.steps.map((step) => `<li class="step visible">${escapeHtml(step.text)}</li>`).join('');
    el.slide.innerHTML = `
      <div class="slide-id">${escapeHtml(s.id)}</div>
      <h1>${escapeHtml(s.title)}</h1>
      <${listTag}>${steps}</${listTag}>
      <div class="visual"><strong>Visual placeholder:</strong> ${escapeHtml(s.visual.description)}</div>
    `;
    if (s.audio) {
      el.audio.src = s.audio;
      el.audio.parentElement.style.display = '';
      if (autoplay) {
        el.audio.currentTime = 0;
        const playPromise = el.audio.play();
        if (playPromise && typeof playPromise.catch === 'function') {
          playPromise.catch(() => {
            // Browsers may block autoplay until the first user interaction.
            // Controls remain visible, and subsequent slide changes after interaction usually play normally.
          });
        }
      }
    } else {
      el.audio.removeAttribute('src');
      el.audio.parentElement.style.display = 'none';
    }
    el.transcript.textContent = s.transcript || 'Transcript pending.';
    el.sources.textContent = s.sources && s.sources.length ? s.sources.join(', ') : 'Module synthesis / no single source required.';
    el.progress.textContent = `Slide ${slideIndex + 1} / ${deck.slides.length}`;
    el.prev.disabled = slideIndex === 0;
    el.next.disabled = slideIndex === deck.slides.length - 1;
  }

  function prevSlide() { if (slideIndex > 0) { slideIndex -= 1; render(); } }
  function nextSlide() { if (slideIndex < deck.slides.length - 1) { slideIndex += 1; render(); } }
  function replayAudio() { if (el.audio.src) { el.audio.currentTime = 0; el.audio.play().catch(() => {}); } }
  function escapeHtml(x) { return String(x).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }

  el.prev.addEventListener('click', prevSlide);
  el.next.addEventListener('click', nextSlide);
  el.replay.addEventListener('click', replayAudio);
  document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); nextSlide(); }
    if (e.key === 'ArrowLeft') { e.preventDefault(); prevSlide(); }
    if (e.key.toLowerCase() === 'r') replayAudio();
  });
  render({ autoplay: false });
})();
