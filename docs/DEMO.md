# DEMO — video in README the way that actually works (2026)

GitHub strips `<video>` tags in `README.md`. The four workarounds that work in 2026:

1. **Click-to-play poster (used here).** Upload `assets/demo.mp4` to the repo (or Releases), add a poster image that links to it:
   ```markdown
   [![Demo — 2 min proof](assets/preview.png)](assets/demo.mp4)
   ```
   `preview.html` embeds the real `<video>` player because Pages/HTML allows it; README links to it.
2. **Animated GIF.** `assets/demo.gif` autoplays in README. Keep under ~8MB, 15fps, 800px wide.
3. **Asciinema for terminal.** Lightweight `.cast`, shareable player link — ideal for `pytest` runs.
4. **YouTube + thumbnail.** For long walkthroughs; link thumbnail to YouTube.

## Record in 2 minutes

### Option A — VHS (beautiful terminal GIFs, recommended)
```bash
# install: https://github.com/charmbracelet/vhs
cat > demo.tape <<'TAPE'
Output assets/demo.gif
Set Shell "bash" FontSize 16 Width 900 Height 520
Type "python -m pytest -v" Enter Sleep 2s
Type "python -m src.experiments.exp01_bigo" Enter Sleep 2s
Type "python -m src.experiments.exp04_live_market" Enter Sleep 3s
TAPE
vhs demo.tape
ffmpeg -i assets/demo.gif -movflags faststart -pix_fmt yuv420p assets/demo.mp4
```

### Option B — asciinema
```bash
pip install asciinema
asciinema rec assets/demo.cast -c "bash -c 'python -m pytest -v; python -m src.benchmarks.run_all'"
# upload: asciinema upload assets/demo.cast  -> paste link in README
```

### Option C — Playwright (page video + screenshots)
```bash
# screenshots (used for assets/preview.png):
python -m http.server 8000 &
# then via Playwright: goto http://localhost:8000/preview.html, fullPage screenshot
# video: Playwright recordVideo context option, save to assets/demo.mp4
```

## Checklist before push
- [ ] `assets/preview.png` under ~1MB, 1280px wide
- [ ] `assets/demo.mp4` plays locally (`ffplay` / browser)
- [ ] `assets/demo.gif` under 8MB if added to README top
- [ ] Poster links to `assets/demo.mp4`, full player in `preview.html`
- [ ] No secrets in terminal output (our runs print only timings + AAPL quote)
