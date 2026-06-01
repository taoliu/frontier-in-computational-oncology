#!/usr/bin/env python3
"""Build a static HTML lecture from a JSON manifest."""
from __future__ import annotations
import argparse, json, shutil
from pathlib import Path

HTML = """<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{title}</title>
  <link rel=\"stylesheet\" href=\"../../../../shared/html-player/style.css\" />
</head>
<body>
  <div class=\"app\">
    <header>
      <div>
        <div class=\"brand\" data-module></div>
        <div class=\"meta\" data-lecture></div>
      </div>
      <div class=\"progress\" data-progress></div>
    </header>
    <main>
      <section class=\"slide\" data-slide></section>
      <aside>
        <div class=\"card\">
          <h2>Audio</h2>
          <audio data-audio controls preload=\"metadata\"></audio>
        </div>
        <div class=\"card\">
          <h2>Transcript</h2>
          <div class=\"transcript\" data-transcript></div>
        </div>
        <div class=\"card\">
          <h2>Sources</h2>
          <div class=\"sources\" data-sources></div>
        </div>
      </aside>
    </main>
    <footer>
      <div class=\"controls\">
        <button class=\"secondary\" data-prev>← Previous slide</button>
        <button data-reveal>Reveal next</button>
        <button class=\"secondary\" data-next>Next slide →</button>
        <button class=\"secondary\" data-reset>Reset slide</button>
      </div>
      <div class=\"meta\">Keyboard: ← / → / Space, R reset</div>
    </footer>
  </div>
  <script>window.LECTURE_DECK = {deck_json};</script>
  <script src=\"../../../../shared/html-player/player.js\"></script>
</body>
</html>
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--copy-audio", action="store_true")
    args = ap.parse_args()
    deck = json.loads(args.manifest.read_text())
    args.out_dir.mkdir(parents=True, exist_ok=True)
    if args.copy_audio:
        audio_dir = args.out_dir / "assets" / "audio"
        audio_dir.mkdir(parents=True, exist_ok=True)
        for slide in deck.get("slides", []):
            audio = slide.get("audio")
            if not audio:
                continue
            src = (args.manifest.parent / audio).resolve() if not Path(audio).is_absolute() else Path(audio)
            dest = audio_dir / src.name
            shutil.copy2(src, dest)
            slide["audio"] = f"assets/audio/{dest.name}"
    title = f"{deck.get('module', 'Lecture')} — {deck.get('lecture', '')}"
    (args.out_dir / "index.html").write_text(HTML.format(title=title, deck_json=json.dumps(deck, ensure_ascii=False)))

if __name__ == "__main__":
    main()
