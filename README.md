<div align="center">
  <img src="https://yourimageshare.com/ib/JUZqnD0xLu.png" alt="Professor Finder Screenshot" width="800"/>
</div>


# 🎓 Professor Finder CLI

Professor Finder is a privacy-conscious, terminal-based search tool for discovering academic profiles. It uses search engine scraping (Google, DuckDuckGo) with no API keys, simulates human behavior, and ensures clean, unique result output.

Whether you're navigating censorship, building open-source research tools, or running remote queries in CLI-only environments, Professor Finder is fast, flexible, and stealth-friendly.

---

## 📦 Features

- 🔍 Keyword-based professor search
- ✅ Unique result enforcement (no duplicates)
- ⏳ Randomized human-like wait delays between queries
- 🔄 DuckDuckGo fallback if Google fails or blocks
- 🧠 Variable query phrasing to mimic curiosity
- 🎨 Color-coded terminal interface with emoji feedback
- 🔐 Pure scraping — no API keys, cookies, or browser dependencies
- 🌍 Compatible with WSL, VPNs, proxychains, and Tor

---

## ⚙️ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/shataragh/professor-finder.git
cd professor-finder
pip install -r requirements.txt
