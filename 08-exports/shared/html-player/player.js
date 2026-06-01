(function () {
  const deck = window.LECTURE_DECK;
  let slideIndex = 0;
  let continuous = false;

  const el = {
    module: document.querySelector('[data-module]'),
    lecture: document.querySelector('[data-lecture]'),
    slide: document.querySelector('[data-slide]'),
    audio: document.querySelector('[data-audio]'),
    progress: document.querySelector('[data-progress]'),
    prev: document.querySelector('[data-prev]'),
    next: document.querySelector('[data-next]'),
    play: document.querySelector('[data-play]'),
    replay: document.querySelector('[data-replay]')
  };

  function render({ autoplay = true } = {}) {
    const s = deck.slides[slideIndex];
    el.module.textContent = deck.module;
    el.lecture.textContent = deck.lecture;
    const listTag = s.ordered ? 'ol' : 'ul';
    const steps = s.steps.map((step) => `<li class="step">${escapeHtml(step.text)}</li>`).join('');
    el.slide.innerHTML = `
      <div class="slide-id">${escapeHtml(s.id)}</div>
      <h1>${escapeHtml(s.title)}</h1>
      <${listTag}>${steps}</${listTag}>
      <div class="visual"><strong>Visual placeholder:</strong> ${escapeHtml(s.visual.description)}</div>
    `;
    if (s.audio) {
      el.audio.src = s.audio;
      if (autoplay) playAudio();
    } else {
      el.audio.removeAttribute('src');
    }
    el.progress.textContent = `Slide ${slideIndex + 1} / ${deck.slides.length}`;
    el.prev.disabled = slideIndex === 0;
    el.next.disabled = slideIndex === deck.slides.length - 1;
    el.play.textContent = continuous ? 'Pause continuous play' : 'Play continuously';
    el.play.classList.toggle('playing', continuous);
  }

  function playAudio() {
    if (!el.audio.src) return;
    el.audio.currentTime = 0;
    el.audio.play().catch(() => {
      // Browser autoplay policies may require the first user click.
    });
  }

  function prevSlide() {
    continuous = false;
    if (slideIndex > 0) { slideIndex -= 1; render(); }
    else render({ autoplay: false });
  }
  function nextSlide({ keepContinuous = false } = {}) {
    if (!keepContinuous) continuous = false;
    if (slideIndex < deck.slides.length - 1) { slideIndex += 1; render(); }
    else { continuous = false; render({ autoplay: false }); }
  }
  function replayAudio() { playAudio(); }
  function toggleContinuous() {
    continuous = !continuous;
    if (continuous) playAudio();
    render({ autoplay: continuous });
  }
  function escapeHtml(x) { return String(x).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }

  el.prev.addEventListener('click', prevSlide);
  el.next.addEventListener('click', () => nextSlide());
  el.replay.addEventListener('click', replayAudio);
  el.play.addEventListener('click', toggleContinuous);
  el.audio.addEventListener('ended', () => {
    if (continuous) nextSlide({ keepContinuous: true });
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); nextSlide(); }
    if (e.key === 'ArrowLeft') { e.preventDefault(); prevSlide(); }
    if (e.key.toLowerCase() === 'r') replayAudio();
    if (e.key.toLowerCase() === 'p') toggleContinuous();
  });
  render({ autoplay: false });
})();
