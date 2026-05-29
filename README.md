## BeautifulSoup & Web Scraping Notes

A deep dive into **BeautifulSoup 4**, web scraping fundamentals, parser behavior, navigation strategies, extraction techniques, and the engineering mindset behind reliable scrapers.

This repository focuses on:
- understanding how HTML is structured
- thinking in parse trees
- learning the tradeoffs of scraping tools
- avoiding beginner mistakes
- building resilient scraping workflows

---

# What You'll Learn

## Core BeautifulSoup Concepts
- Parsing HTML into a tree structure
- Understanding `Tag`, `NavigableString`, and document objects
- Navigating parents, children, and siblings
- Extracting text and attributes safely

## Searching & Selection
- `find()`
- `find_all()`
- CSS selectors with `.select()`

## Parser Differences
- `html.parser`
- `lxml`
- `html5lib`
- XML parsing

## Real Web Scraping Workflow
- Fetching HTML with `requests`
- Parsing with BeautifulSoup
- Extracting clean structured data
- Handling missing values safely

## Engineering Mindset
- Writing defensive scrapers
- Handling changing page structures
- Thinking beyond tutorials
- Building maintainable scraping systems


## Ethics & Responsible Scraping

Before scraping a website:

- Check robots.txt
- Respect rate limits
- Avoid overloading servers
- Read the site's terms of service
- Future Improvements

## Possible additions to this repo:

- pagination scraping
- exporting to CSV/JSON
- async scraping
- Playwright integration
- Selenium examples
- mini scraping projects
- data cleaning pipelines

---

# Repository Structure

```bash
.
├── job_market_analyzer
│   ├── README.md
│   ├── data
│   ├── main.py
│   ├── notebooks
│   ├── requirements.txt
│   └── scraper
└── kenya_news_scraper
    ├── books_data.csv
    ├── books_data_clean.csv
    ├── claener.py
    ├── cleaner.py
    ├── requirememnts.txt
    └── scraper.py

```
