from utilities import log
from functions import *
from models import *
from time import sleep
from pony.orm import *
from bs4 import BeautifulSoup
import hashlib


@db_session
def get_urls():
    return select(u for u in Url if u.date_scraped is None).order_by(desc(Url.priority_scrape))


@db_session
def save_content(url_id, cleaned, raw, hashed):
    url = select(u for u in Url if u.id == url_id).get()
    raw_string = raw.decode('utf-8')
    content_object = Content(
        url=url,
        content=cleaned,
        content_raw=raw_string,
        content_raw_hash=hashed
    )
    commit()


def clean_me(html):  # clean the html, css and javascript tags
    soup = BeautifulSoup(html,
                         "html5lib")  # BeatuifulSoup library to clean it and use the html5lib parser to parse it
    for s in soup(['script', 'style']):  # select the tags that must removed
        s.decompose()
    return ' '.join(soup.stripped_strings)  # remove white spaces


def hash_content(content):
    hash_object = hashlib.sha256(content)
    hex_dig = hash_object.hexdigest()
    return (hex_dig)


def start_bee():
    while True:
        urls = get_urls()

        if len(urls) == 0:
            print("No URLs to be crawled, waiting for 60 seconds.")
            sleep(60)
            continue

        for url in urls:
            try:
                # url.url = encryption.hive_decrypt(url.url)
                data = content_crawler(url.url)

                hashed = hash_content(data)

                cleaned = clean_me(data)  # cleans the content

                #if cleaned is not None:
                save_content(url.id, cleaned, data, hashed)

            except(ValueError, NameError, TypeError) as error:
                log.error(str(error))