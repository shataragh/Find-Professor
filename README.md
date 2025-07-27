<div align="center">
  <img src="https://yourimageshare.com/ib/JUZqnD0xLu.png" alt="Professor Finder CLI Screenshot" width="800"/>
</div>

<h1 align="center">🎓 Find-Professor CLI</h1>
<p align="center">
  <strong>Terminal-based academic profile discovery — API-free, stealth-friendly, and censorship-resilient.</strong>
</p>

<div align="center">
  <a href="https://github.com/shataragh/Find-Professor/stargazers"><img src="https://img.shields.io/github/stars/shataragh/Find-Professor?style=social" alt="GitHub Stars"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/shataragh/Find-Professor" alt="MIT License"></a>
  <a href="https://github.com/shataragh/Find-Professor/commits/main"><img src="https://img.shields.io/github/last-commit/shataragh/Find-Professor" alt="Last Commit"></a>
</div>

---

## 🧭 Overview

**Find-Professor** is a command-line tool that helps users discover academic profiles and professional pages using keyword-based search.  
It mimics human browsing behavior, rotates query phrasing, and gracefully falls back to DuckDuckGo if Google blocks scraping — all without browser automation or API keys.

---

## 🔧 Features

- 🔍 Keyword-based search with `.edu` and LinkedIn targeting
- 🧠 Randomized suffixes for natural query variation
- ⏳ Human-like countdown delays between requests
- 🔄 DuckDuckGo fallback if Google fails or blocks
- ✅ Unique result enforcement (no duplicates)
- 🎨 Color-coded terminal output with emoji feedback
- 🔐 No cookies, browser automation, or API keys required

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/shataragh/Find-Professor.git
cd Find-Professor
pip install -r requirements.txt
