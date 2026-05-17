#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

BASE = "https://www.najpravo.sk"

FEEDS = {
    "rodinne-pravo": "https://www.najpravo.sk/pravna-poradna/rodinne-pravo/",
    "pracovne-pravo": "https://www.najpravo.sk/pravna-poradna/pracovne-pravo/",
    "obcianske-pravo": "https://www.najpravo.sk/pravna-poradna/obcianske-pravo/",
    "trestne-pravo": "https://www.najpravo.sk/pravna-poradna/trestne-pravo/",
    "spravne-pravo": "https://www.najpravo.sk/pravna-poradna/spravne-pravo/",
    "obchodne-pravo": "https://www.najpravo.sk/pravna-poradna/obchodne-pravo/",
    "ustavne-pravo": "https://www.najpravo.sk/pravna-poradna/ustavne-pravo/",
}
DEFAULT_FEEDS = list(FEEDS.keys())

RE_SEP = re.compile(r"-{5,}")
RE_AUTHOR_BLOCK = re.compile(r"\bNa otázku čitateľa odpovedal\b", re.IGNORECASE)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (dataset-scraper; +https://www.najpravo.sk/)"
}


def collapse_ws(s: str) -> str:
    return " ".join(s.replace("\xa0", " ").split())


def fetch(session: requests.Session, url: str, timeout: int = 30) -> str:
    response = session.get(url, headers=HEADERS, timeout=timeout)
    response.raise_for_status()
    if not response.encoding:
        response.encoding = "utf-8"
    return response.text


def extract_type_from_title(soup: BeautifulSoup) -> str:
    title = (soup.title.get_text(" ", strip=True) if soup.title else "").strip()
    parts = [part.strip() for part in title.split("|") if part.strip()]
    return parts[1] if len(parts) >= 2 else ""


def extract_section_text_between_headers(
    soup: BeautifulSoup,
    start_h2: str,
    end_h2: str | None,
) -> str:
    headers = soup.find_all(["h2", "h3"])

    start: Tag | None = None
    for header in headers:
        if header.get_text(" ", strip=True) == start_h2:
            start = header
            break
    if start is None:
        return ""

    end: Tag | None = None
    if end_h2 is not None:
        end = start.find_next(
            lambda tag: isinstance(tag, Tag)
            and tag.name in ("h2", "h3")
            and tag.get_text(" ", strip=True) == end_h2
        )

    chunks: list[str] = []
    for element in start.next_elements:
        if end is not None and element == end:
            break
        if not isinstance(element, Tag):
            continue
        if element.name in ("script", "style"):
            continue
        if element.name in ("p", "li"):
            text = element.get_text(" ", strip=True)
            if text:
                chunks.append(text)

    return "\n".join(chunks).strip()


def strip_trailing_author_block(answer: str) -> str:
    if not answer:
        return answer

    parts = RE_SEP.split(answer, maxsplit=1)
    answer2 = parts[0].strip() if parts else answer.strip()

    match = RE_AUTHOR_BLOCK.search(answer2)
    if match:
        answer2 = answer2[: match.start()].strip()

    return answer2


def parse_detail_page(session: requests.Session, url: str) -> dict | None:
    html = fetch(session, url)
    soup = BeautifulSoup(html, "html.parser")

    type_name = extract_type_from_title(soup)
    question = extract_section_text_between_headers(soup, "Otázka čitateľa", "Odpoveď")
    answer = extract_section_text_between_headers(soup, "Odpoveď", None)
    answer = strip_trailing_author_block(answer)

    question = collapse_ws(question)
    answer = collapse_ws(answer)
    if not question or not answer:
        return None

    return {
        "type": type_name,
        "question": question,
        "expected": answer,
        "url": url,
    }


def is_valid_article_url(url: str) -> bool:
    if not url:
        return False
    parsed = urlparse(url)
    return (
        parsed.netloc == urlparse(BASE).netloc
        and "/pravna-poradna/" in parsed.path
        and parsed.path.endswith(".html")
    )


def extract_article_links(list_page_html: str, list_url: str) -> list[str]:
    soup = BeautifulSoup(list_page_html, "html.parser")
    category_path = urlparse(list_url).path.rstrip("/")
    if not category_path.endswith("/"):
        category_path += "/"

    urls: list[str] = []
    selectors = [
        "h1 a[href]",
        "h2 a[href]",
        "h3 a[href]",
        "h4 a[href]",
        'a[href*="/pravna-poradna/"][href$=".html"]',
    ]

    for selector in selectors:
        for anchor in soup.select(selector):
            href = anchor.get("href", "")
            if not href:
                continue
            full = urljoin(list_url, href)
            if not is_valid_article_url(full):
                continue
            if not urlparse(full).path.startswith(category_path):
                continue
            urls.append(full)

    seen = set()
    out: list[str] = []
    for url in urls:
        if url not in seen:
            seen.add(url)
            out.append(url)
    return out


def find_next_page(list_page_html: str, list_url: str) -> str | None:
    soup = BeautifulSoup(list_page_html, "html.parser")

    anchor = soup.select_one('a[rel="next"][href]')
    if anchor:
        return urljoin(list_url, anchor["href"])

    for selector in ("li.next a[href]", "a.next[href]", "a[aria-label*='Next'][href]"):
        anchor = soup.select_one(selector)
        if anchor:
            return urljoin(list_url, anchor["href"])

    candidates = soup.find_all("a", href=True)
    for anchor in candidates:
        text = anchor.get_text(" ", strip=True)
        if text in ("Ďalej", "Ďalšia", "Ďalšie", "Next", "›", "»", ">"):
            next_url = urljoin(list_url, anchor["href"])
            if next_url != list_url:
                return next_url

    return None


def crawl_category(
    session: requests.Session,
    category_url: str,
    delay: float,
    max_pages: int,
) -> list[str]:
    base = category_url.split("?", 1)[0]
    if not base.endswith("/"):
        base += "/"

    found_all: list[str] = []
    seen_articles = set()

    page = 1
    while True:
        page_url = base if page == 1 else f"{base}?page={page}"
        html = fetch(session, page_url)
        links = extract_article_links(html, page_url)
        if not links:
            break

        for url in links:
            if url not in seen_articles:
                seen_articles.add(url)
                found_all.append(url)

        if max_pages > 0 and page >= max_pages:
            break

        page += 1
        if delay > 0:
            time.sleep(delay)

    return found_all


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="data/najpravo_pravna_poradna.json", help="output json path")
    parser.add_argument("--delay", type=float, default=0.25, help="delay between requests (seconds)")
    parser.add_argument("--max-pages-per-category", type=int, default=0, help="0 = no limit")
    parser.add_argument("--max-articles", type=int, default=0, help="0 = no limit")
    parser.add_argument(
        "--feeds",
        nargs="+",
        default=None,
        help=f"category slugs (default: all). Allowed: {', '.join(DEFAULT_FEEDS)}",
    )
    args = parser.parse_args()

    feeds = args.feeds if args.feeds else DEFAULT_FEEDS
    unknown = [slug for slug in feeds if slug not in FEEDS]
    if unknown:
        raise SystemExit(f"Unknown feed(s): {', '.join(unknown)}. Allowed: {', '.join(DEFAULT_FEEDS)}")

    category_urls = [FEEDS[slug] for slug in feeds]

    if args.out == "data/najpravo_pravna_poradna.json":
        if len(feeds) == 1:
            args.out = f"data/najpravo_{feeds[0]}.json"
        else:
            args.out = "data/najpravo_selected.json"

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    session = requests.Session()

    article_urls: list[str] = []
    for category_url in category_urls:
        urls = crawl_category(
            session,
            category_url,
            delay=args.delay,
            max_pages=args.max_pages_per_category,
        )
        article_urls.extend(urls)

    seen = set()
    unique_urls: list[str] = []
    for url in article_urls:
        if url not in seen:
            seen.add(url)
            unique_urls.append(url)

    if args.max_articles > 0:
        unique_urls = unique_urls[: args.max_articles]

    dataset: list[dict] = []
    for url in unique_urls:
        try:
            item = parse_detail_page(session, url)
            if item:
                dataset.append(item)
            else:
                print(f"[SKIP] no question/answer: {url}")
        except Exception as exc:
            print(f"[ERR] {url} -> {type(exc).__name__}: {exc}")

        if args.delay > 0:
            time.sleep(args.delay)

    with out_path.open("w", encoding="utf-8") as handle:
        json.dump(dataset, handle, ensure_ascii=False, indent=2)

    print(f"saved: {out_path} | items: {len(dataset)}")


if __name__ == "__main__":
    main()
