# Program to grab information from the source

# https://en.wikipedia.org/wiki/Programmer

import requests
from bs4 import BeautifulSoup

def get_page(url):

    # Adding headers here is necessary because sometimes the requests get blocked if they detect a script without a proper User-Agent.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Give you the first anchor tag from the webpage
    # print(soup.a)   

    # Only grab the specific information
    # print(soup.title.string)

    # Give you all the anchor tags from the webpage
    # .find_all() -- finds all the information
    # .find() -- only find the first thing
    # print(soup.findAll("a"))

    # Only grab the href from all the links
    tag= soup.find_all("a")
    for t in tag:
        url2 = t.get("href")
        print(url2)



get_page(input("What url would you like to scrape? "))

