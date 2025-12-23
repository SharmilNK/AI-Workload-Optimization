# scrape_pilot.py
# Minimal scraper for Wikipedia, arXiv abstracts, and Project Gutenberg
# Outputs scraped_docs.jsonl (gitignored)

import requests
import time
import json
import uuid
import re
from bs4 import BeautifulSoup
import feedparser

OUTFILE = "scraped_docs.jsonl"
HEADERS = {"User-Agent": "PilotBot/1.0 (learning-project)"}
RATE_LIMIT = 1.0

PII_PATTERNS = [
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",  # email
    r"\b\d{3}-\d{2}-\d{4}\b",  # SSN (naive)
]

def strip_pii(text):
    for p in PII_PATTERNS:
        text = re.sub(p, "[REDACTED]", text)
    return text

def save_record(record):
    with open(OUTFILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def scrape_wikipedia(count=50):
    url = "https://en.wikipedia.org/wiki/Special:Random"
    for _ in range(count):
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        title = soup.find("h1", id="firstHeading")
        paragraphs = soup.select("div.mw-parser-output > p")
        text = "\n".join(p.get_text() for p in paragraphs if p.get_text().strip())

        record = {
            "id": str(uuid.uuid4()),
            "source": "wikipedia",
            "url": r.url,
            "title": title.get_text() if title else "",
            "text": strip_pii(text),
        }

        save_record(record)
        time.sleep(RATE_LIMIT)

def scrape_arxiv(count=50):
    feed = feedparser.parse(
        f"http://export.arxiv.org/api/query?search_query=cat:cs.CL&max_results={count}"
    )

    for entry in feed.entries:
        record = {
            "id": str(uuid.uuid4()),
            "source": "arxiv",
            "url": entry.id,
            "title": entry.title,
            "text": strip_pii(entry.summary),
        }
        save_record(record)

def scrape_gutenberg():
    # Public-domain book example
    url = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
    r = requests.get(url, headers=HEADERS, timeout=10)

    record = {
        "id": str(uuid.uuid4()),
        "source": "gutenberg",
        "url": url,
        "title": "Pride and Prejudice (excerpt)",
        "text": strip_pii(r.text[:20000]),
    }

    save_record(record)

if __name__ == "__main__":
    scrape_wikipedia()
    scrape_arxiv()
    scrape_gutenberg()
