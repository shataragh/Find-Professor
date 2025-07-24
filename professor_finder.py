import time
import random
import requests
from bs4 import BeautifulSoup
from googlesearch import search as google_search
from colorama import init, Fore, Style

# Initialize terminal colors
init(autoreset=True)

# Query suffixes for variation
suffix_variants = ["", "research", "CV", "contact", "faculty", "publication", "bio"]

# DuckDuckGo headers to mimic a browser
duck_headers = {
    "User-Agent": "Mozilla/5.0",
}

# Countdown with human-like random pacing
def countdown(min_sec=4, max_sec=8):
    wait_time = random.randint(min_sec, max_sec)
    for remaining in range(wait_time, 0, -1):
        print(f"{Fore.YELLOW}⏳ Waiting {remaining}s to mimic human behavior...", end="\r")
        time.sleep(1)
    print(" " * 80, end="\r")

# Generate variable queries
def generate_query(base):
    suffix = random.choice(suffix_variants)
    return f"{base} {suffix} professor (site:.edu OR site:linkedin.com)"

# DuckDuckGo fallback search
def duckduckgo_search(query, max_results=10):
    print(f"\n{Fore.CYAN}🦆 Fallback activated: Searching DuckDuckGo...\n")
    url = f"https://html.duckduckgo.com/html/?q={requests.utils.quote(query)}"
    try:
        response = requests.get(url, headers=duck_headers, timeout=10)
        soup = BeautifulSoup(response.text, "lxml")
        links = []

        for a in soup.select("a.result__a"):
            href = a.get("href")
            if href and href.startswith("http"):
                links.append(href)
            if len(links) >= max_results:
                break
        return links
    except Exception as e:
        return [f"{Fore.RED}🐛 DuckDuckGo failed: {e}"]

# Unified search with Google + fallback
def search_professors(keywords, target_results=10):
    if not keywords.strip():
        return [f"{Fore.YELLOW}⚠️ Please enter valid keywords."]

    print(f"\n{Fore.CYAN}🔍 Searching for: {Style.BRIGHT}{keywords} (target: {target_results} unique results)\n")

    results = []
    seen = set()
    retries = 0
    max_attempts = target_results * 8
    fallback_triggered = False

    while len(results) < target_results and retries < max_attempts:
        countdown()
        query = generate_query(keywords)
        print(f"{Fore.CYAN}🌐 Attempting query [{retries+1}/{max_attempts}]...", end="\r")

        if not fallback_triggered:
            try:
                candidate = next(google_search(query, num_results=1), None)
            except Exception as e:
                print(f"\n{Fore.RED}🚫 Google blocked or failed. Switching to DuckDuckGo...")
                fallback_triggered = True
                continue
        else:
            candidates = duckduckgo_search(query, max_results=3)
            candidate = next((url for url in candidates if url not in seen), None)

        retries += 1

        if candidate and candidate not in seen:
            seen.add(candidate)
            results.append(f"{Fore.BLUE}{len(results)+1}. {Style.RESET_ALL}{candidate}")
            print(f"{Fore.GREEN}✅ Found: {candidate}")
        else:
            print(f"{Fore.YELLOW}🤔 Duplicate or empty. Trying again...", end="\r")
            time.sleep(1)

        if len(results) % 4 == 0 and len(results) < target_results:
            print(f"\n{Fore.CYAN}🧘‍♂️ Taking a moment to reflect before continuing...\n")
            countdown(min_sec=6, max_sec=12)

    print(" " * 80, end="\r")
    return results if results else [f"{Fore.RED}❌ No unique results found after {retries} attempts."]
    
# 🧪 Terminal entry point
if __name__ == "__main__":
    print(f"{Fore.MAGENTA}🎓 Professor Finder\n{Fore.MAGENTA}{'='*20}")

    keywords = input(f"{Fore.YELLOW}📝 Enter search keywords: ")
    try:
        target_results = int(input(f"{Fore.YELLOW}🔢 Number of unique results to find: "))
    except ValueError:
        print(f"{Fore.YELLOW}⚠️ Invalid input. Using default: 10 results.")
        target_results = 10

    links = search_professors(keywords, target_results)

    print(f"\n{Fore.GREEN}📄 Final Results:\n" + "-"*30)
    for line in links:
        print(line)
