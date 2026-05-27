import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime

# we identify the base url

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html" 
TOTAL_PAGES = 5 # URL HAS ALOT OF PAGES SO WE SELECT 5 FIRST
DELAY = 1 # this is the seconds to wait between requests


def scrap_page(page_number):

    url = BASE_URL.format(page_number)

    # we go ahead and fetch the html

    # we create a header so that the url doesnt see as a bot and not experience a 403 error

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
    }

    # we get our response

    response = requests.get(url , headers)


    # We go ahead and check if we got a 403 error in our response and how to overcome that

    if response.status_code != 200:
        print(f" Page {page_number} returned status code {response.status_code}. Skipping")
        return []
    

    # WE already have the html and taken care of the error. So we pass the html into a tree

    soup = BeautifulSoup(response.text , 'lxml')

    # we find all the book containers. Each book if we look at the url itrs wrapped in a container and artcle class product_pod tag

    books = soup.find_all('article' , class_ = 'product_pod')

    # we cover for incase the site structure that may have changed

    if not books:
        print(f"No books found on page {page_number}. The structure may have changed.")
        return []
    
    page_results = []

    # for each book we extract the titile , the price , and the rating

    # TITLE

    for book in books:
        # the title is in the a tag

        title_tag = book.find('h3')

        # if the title tag is there we extract the link and the title

        if title_tag:
            link_tag = title_tag.find('a')
            title = link_tag['title'] if link_tag else 'N/A'

            # BUILD THE FULL URL .combine relative and base url

            relative_url = link_tag.get('href' , '') if link_tag else ''
            base_url = "http://books.toscrape.com/catalogue/" + relative_url.replace("../" , '')

        else:
            title = 'N/A'
            full_url = 'N/A'

    # EXTRACT THE PRICE

    # PRICE IS IN THE P TAG
    price_tag = book.find('p' , class_ = 'price-color')
    price = price_tag.get_text(strip = True) if price_tag else 'N/A'

    # EXTRACT THE RATING
    
    # rating is in the p tag

    rating_tag = book.find('p' , class_ = 'star_rating')
    if rating_tag:
        classes = rating_tag.get('class' , [])
        rating = classes[1] if len(classes) > 1 else 'N/A'
    else:
        rating = 'N/A'

    # we extract availability

    # availability is in thte p tag

    availability_tag = book.find('p' , class_ = 'instock')
    availability = availability_tag.get_text(strip = True) if availability_tag else 'Out of stock'

    # NOW SINCE WE HAVE EVERYTHING WE APPEND IT IN OUR PAGE RESULTS LIST

    page_results.append({
        'title' : title , 
        'price' : price ,
        'rating' : rating , 
        'availability' : availability , 
        'url' : full_url ,
        'page_scraped' : page_number ,
        'date_scrrapped' : datetime.now().strfttime('%Y-%m-%d %H:%M:%S')
    }
    )

    return page_results
