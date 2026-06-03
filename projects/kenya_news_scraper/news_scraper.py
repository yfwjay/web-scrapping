import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

RSS_URL = "https://bbci.co.uk"

KENYA_KEYWORDS = [
    'kenya', 'nairobi', 'mombasa', 'kisumu', 'nakuru', 'eldoret', 
    'nyeri', 'ruto', 'shilling', 'kes', 'kdf'
]

def get_secure_session():
    """Creates a requests session with browser headers and automatic retries."""
    session = requests.Session()
    
    # Modern browser headers to bypass basic bot blocks
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive"
    })
    
    # Retry logic if the server drops the connection temporarily
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))
    session.mount("http://", HTTPAdapter(max_retries=retries))
    return session

def scrape_full_article(session, url):
    if url == 'N/A':
        return 'N/A'
    try:
        time.sleep(1.5) 
        response = session.get(url, timeout=10)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"
            
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p', {'data-component': 'text-block'})
        
        if not paragraphs:
            article = soup.find('article')
            if article:
                paragraphs = article.find_all('p')
                
        text = " ".join([p.get_text(strip=True) for p in paragraphs])
        return text if text.strip() else "No text content found"
    except Exception as e:
        return f"Scraping failed: {str(e)}"

def scrape_bbc_africa_news():
    print("=" * 50)
    print(" ADVANCED KENYA BBC NEWS SCRAPER")
    print("=" * 50)
    
    session = get_secure_session()
    
    try:
        response = session.get(RSS_URL, timeout=15)
        if response.status_code != 200:
            print(f"❌ Server returned code: {response.status_code}")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Network Connection Refused!")
        print("💡 Solution: Check your internet connection or use a VPN if your ISP blocks foreign news feeds.")
        return
    except Exception as e:
        print(f"❌ Network error occurred: {e}")
        return

    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item')
    print(f"\n📰 Found {len(items)} total articles in the feed.\n")
    
    news = []
    for item in items:
        title = item.find('title')
        link = item.find('link')
        pub_date = item.find('pubDate')
        description = item.find('description')
        
        title_text = title.get_text(strip=True) if title else 'N/A'
        desc_text = description.get_text(strip=True) if description else 'N/A'
        url_text = link.get_text(strip=True) if link else 'N/A'
        
        combined_text = f"{title_text} {desc_text}".lower()
        is_kenya = 'No'
        if any(keyword in combined_text for keyword in KENYA_KEYWORDS):
            is_kenya = 'Yes'
            
        news.append({
            'headline': title_text,
            'url': url_text,
            'published': pub_date.get_text(strip=True) if pub_date else 'N/A',
            'summary': desc_text,
            'kenya_related': is_kenya,
            'source': 'BBC Africa',
            'date_scraped': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
    df = pd.DataFrame(news)
    kenya_news_df = df[df['kenya_related'] == 'Yes'].copy()
    
    if kenya_news_df.empty:
        print("🇰🇪 No Kenya-related articles found in this feed update.")
        return

    print(f"🇰🇪 Found {len(kenya_news_df)} Kenya-related articles. Fetching full body text...")
    
    full_texts = []
    for idx, row in kenya_news_df.iterrows():
        print(f"  → Scraping: {row['headline'][:40]}...")
        full_text = scrape_full_article(session, row['url'])
        full_texts.append(full_text)
        
    kenya_news_df['full_text'] = full_texts
    kenya_news_df.to_csv('kenya_news_detailed.csv', index=False)
    
    print(f"\n✅ Total feed articles scanned: {len(df)}")
    print(f"💾 Kenya specific data saved to: kenya_news_detailed.csv")
    
if __name__ == "__main__":
    scrape_bbc_africa_news()
