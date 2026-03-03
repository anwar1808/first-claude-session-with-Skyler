# My First Claude Code Session with Skyler

**Date:** 3 March 2026
**Participants:** Annie & Skyler
**Tool:** [Claude Code](https://claude.com/claude-code)

---

## What We Did

### 1. Opened browsers from the terminal
- Launched Safari and Brave Browser using Claude Code CLI commands

### 2. Built a rainbow "HELLO WORLD" website
- Created `hello.html` — a page with a massive rainbow-gradient "HELLO WORLD" on a dark background
- Opened it directly in Brave

### 3. Tried to share it with Skyler on Google Meet
- Explored how to programmatically control a browser tab
- Set up **Playwright** (Python) to connect to Brave via Chrome DevTools Protocol
- Discovered the Meet call was in **Safari**, not Brave
- Switched to **AppleScript** to interact with Safari's Google Meet tab
- Hit Safari's sandboxed security restriction requiring manual "Allow JavaScript from Apple Events" setting

### 4. Saved this session and uploaded it to GitHub
- Documented everything in this README
- Pushed to GitHub as a memento of our first Claude Code experience

---

## Files

- [`hello.html`](hello.html) — The rainbow HELLO WORLD page
- [`meet_share.py`](meet_share.py) — Playwright script for sending messages in Google Meet chat

---

## Lessons Learned

- **Playwright** works great for Chromium-based browsers (Chrome, Brave) but not Safari
- **AppleScript** can control Safari tabs and run JavaScript in them, but requires a manual Safari setting
- macOS sandboxes Safari's preferences so they can't be changed from the terminal
- Browser automation from the CLI is powerful but each browser has its quirks

---

*Generated with Claude Code (Opus 4.6) — our first session together!*
