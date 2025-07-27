<div align="center">
  <img src="https://yourimageshare.com/ib/JUZqnD0xLu.png" alt="Professor Finder CLI Screenshot" width="800"/>
</div>

<h1 align="center">🎓 Professor Finder CLI</h1>
<p align="center">
  <strong>Lightweight CLI tool for academic profile discovery — API-free, privacy-conscious, and censorship-resilient.</strong>
</p>

<div align="center">
  <a href="https://github.com/shataragh/professor-finder/stargazers"><img src="https://img.shields.io/github/stars/shataragh/professor-finder?style=social" alt="GitHub Stars"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href="https://github.com/shataragh/professor-finder/commits/main"><img src="https://img.shields.io/github/last-commit/shataragh/professor-finder.svg" alt="Last Commit"></a>
</div>

---

## 🚀 About

Professor Finder is a terminal-based search utility that helps users locate academic websites or professional profiles using keyword queries.

It simulates human browsing behavior, avoids duplicate results, and gracefully falls back to DuckDuckGo if Google blocks scraping — all without browser automation or tracking.

---

## 🔧 Features

- 🔍 Simple keyword-based professor search (site:.edu, LinkedIn, etc.)
- ⏳ Human-like countdown between requests to avoid rate-limiting
- 🧠 Randomized suffixes for natural query phrasing
- 🔄 Automatic fallback to DuckDuckGo if Google fails
- ✅ Unique result enforcement
- 🎨 Emoji-enhanced, color-coded terminal output
- 🔐 Pure scraping — no API keys, cookies, or headless browsers

---

## ⚙️ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/shataragh/professor-finder.git
cd professor-finder
pip install -r requirements.txt
