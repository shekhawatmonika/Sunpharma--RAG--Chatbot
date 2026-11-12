from urllib.request import Request, urlopen
from html.parser import HTMLParser
import os
import time


class PageTextParser(HTMLParser):
    IGNORED_TAGS = {"script", "style", "nav", "footer", "header"}

    def __init__(self):
        super().__init__()
        self.parts = []
        self.ignore_depth = 0

    def handle_starttag(self, tag, attrs):
        if self.ignore_depth or tag in self.IGNORED_TAGS:
            self.ignore_depth += 1

    def handle_endtag(self, tag):
        if self.ignore_depth:
            self.ignore_depth -= 1

    def handle_data(self, data):
        if not self.ignore_depth:
            self.parts.append(data)

# Sirf wahi URL jo 100% chalte hain - test kiye hue
URLS = {
    "about_us": "https://sunpharma.com/about-us/",
    "products": "https://sunpharma.com/products/",
    "careers": "https://sunpharma.com/careers/",
    "newsroom": "https://sunpharma.com/media/",
    "investors": "https://sunpharma.com/investors/",
    "sustainability": "https://sunpharma.com/sustainability/",
}

os.makedirs("data_sunpharma", exist_ok=True)
headers = {"User-Agent": "Mozilla/5.0 - Learning Project - Monika"}

for name, url in URLS.items():
    print(f"Le rahi hu: {name} -> {url}")
    try:
        request = Request(url, headers=headers)
        with urlopen(request, timeout=25) as response:
            status_code = response.status
            page = response.read().decode("utf-8", errors="replace")
        print(f"Status: {status_code}")

        
        if status_code != 200:
            print(f"❌ {name} - 404 ya 500 error, skip")
            continue

        parser = PageTextParser()
        parser.feed(page)
        text = "\n".join(parser.parts)
        clean = "\n".join([l.strip() for l in text.splitlines() if len(l.strip()) > 40])

        # Check if the cleaned text is too short
        if len(clean) < 2000:
            print(f"❌ {name} - Data bahut chhota hai ({len(clean)}), skip")
            continue

        with open(f"data_sunpharma/{name}.txt", "w", encoding="utf-8") as f:
            f.write(clean)
        print(f"✅ done ! {len(clean)} clean characters - SAVED!")
        time.sleep(2)
    except Exception as e:
        print(f"Problem {name} me: {e}")

print("all done! Sun Pharma data scrape complete. Check data_sunpharma folder.")