import requests
from bs4 import BeautifulSoup

# Function to input base URL and depth(To transverse multiple search pages)

def input():
    base_url = raw_input("Enter base url\n")
    n = int(raw_input("Enter the max depth of crawling\n"))
    return base_url, n

# Function stores source code as a bs4 object
# Programmed to extract anchor elements with attribute of sub = hover

def crawler(base_url, max_page):
    page = 1
    while page <= max_page:
        url = base_url
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)

        for links in soup.findAll('a', {'sub': 'hover'}):
            href = links.get('href')
            print links.string
            print url+href
            print "Cast"
            cast(url, url+href)

        page += 1

# Function to extract links to all "Cast" members for each movei link on baseurl

def cast(baseurl, web_page):
    url = web_page
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a', {'itemprop': 'url'}):
        #print link
        href = link.get('href')
        print baseurl+href

(base_url,n) = input()
crawler(base_url, n)

__author__ = 'vishket.shriwas'
