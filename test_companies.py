from urllib.request import Request, urlopen

COMPANIES = {
    "Mankind Pharma": "https://www.mankindpharma.com/about-us",
    "Torrent Pharma": "https://www.torrentpharma.com/about-us.php",
    "Zydus": "https://www.zyduslife.com/about-us",
    "Lupin": "https://www.lupin.com/about-us",
    "Sun Pharma": "https://sunpharma.com/about-us/",
    "Books Demo": "https://books.toscrape.com/catalogue/page-1.html"
}

headers = {"User-Agent": "Mozilla/5.0 - Learning Project - Monika"}

for name, url in COMPANIES.items():
    try:
        request = Request(url, headers=headers)
        with urlopen(request, timeout=15) as response:
            text = response.read().decode("utf-8", errors="replace")
            status = response.status
        # text recieved
        text_len = len(text)
        # check if the text contains relevant data
        has_data = "About" in text or "Pharma" in text or "book" in text.lower()
        print(f"{name} -> {text_len} characters | Data hai? {has_data} | Status: {status}")
    except Exception as e:
        print(f"{name} -> FAIL: {e}")

print("\n company data collected!")