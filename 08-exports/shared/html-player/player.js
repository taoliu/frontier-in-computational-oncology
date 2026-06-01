(function () {
  const deck = window.LECTURE_DECK;
  let slideIndex = 0;
  let revealIndex = 0;

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
    reveal: document.querySelector('[data-reveal]'),
    reset: document.querySelector('[data-reset]')
  };

  function render() {
    const s = deck.slides[slideIndex];
    revealIndex = Math.min(revealIndex, s.steps.length);
    el.module.textContent = deck.module;
    el.lecture.textContent = deck.lecture;
    const listTag = s.ordered ? 'ol' : 'ul';
    const steps = s.steps.map((step, i) => `<li class="step ${i < revealIndex ? 'visible' : ''}">${escapeHtml(step.text)}</li>`).join('');
    el.slide.innerHTML = `
      <div class="slide-id">${escapeHtml(s.id)}</div>
      <h1>${escapeHtml(s.title)}</h1>
      <${listTag}>${steps}</${listTag}>
      <div class="visual"><strong>Visual placeholder:</strong> ${escapeHtml(s.visual.description)}</div>
    `;
    if (s.audio) {
      el.audio.src = s.audio;
      el.audio.parentElement.style.display = '';
    } else {
      el.audio.removeAttribute('src');
      el.audio.parentElement.style.display = 'none';
    }
    el.transcript.textContent = s.transcript || 'Transcript pending.';
    el.sources.textContent = s.sources && s.sources.length ? s.sources.join(', ') : 'Module synthesis / no single source required.';
    el.progress.textContent = `Slide ${slideIndex + 1} / ${deck.slides.length} · Reveal ${revealIndex} / ${s.steps.length}`;
    el.prev.disabled = slideIndex === 0;
    el.next.disabled = slideIndex === deck.slides.length - 1;
    el.reveal.disabled = revealIndex >= s.steps.length;
  }

  function revealNext() {
    const s = deck.slides[slideIndex];
    if (revealIndex < s.steps.length) {
      revealIndex += 1;
      render();
    } else if (slideIndex < deck.slides.length - 1) {
      slideIndex += 1;
      revealIndex = 0;
      render();
    }
  }
  function prevSlide() { if (slideIndex > 0) { slideIndex -= 1; revealIndex = 0; render(); } }
  function nextSlide() { if (slideIndex < deck.slides.length - 1) { slideIndex += 1; revealIndex = 0; render(); } }
  function resetSlide() { revealIndex = 0; render(); }
  function escapeHtml(x) { return String(x).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }

  el.prev.addEventListener('click', prevSlide);
  el.next.addEventListener('click', nextSlide);
  el.reveal.addEventListener('click', revealNext);
  el.reset.addEventListener('click', resetSlide);
  document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); revealNext(); }
    if (e.key === 'ArrowLeft') { e.preventDefault(); prevSlide(); }
    if (e.key.toLowerCase() === 'r') resetSlide();
  });
  render();
})();
