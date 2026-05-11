import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Use a set to keep track of what we've already seen
visited_urls = set()

def spider_urls(url, keyword, max_depth=2):
    # Stop if we hit our depth limit or have already visited this site
    if max_depth == 0 or url in visited_urls:
        return
    
    visited_urls.add(url)
    
    # Adding headers here is necessary because sometimes the requests get blocked if they detect a script without a proper User-Agent.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        print(f"Searching: {url}")
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
    except Exception as e:
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    for tag in soup.find_all('a'):
        href = tag.get("href")
        if href:
            # Create the full URL immediately
            full_url = urljoin(url, href)
            
            # 1. Check if keyword matches
            # 2. Check if we've already BEEN to this specific full URL
            if keyword.lower() in full_url.lower() and full_url not in visited_urls:
                print(full_url)
                # Recurse with depth - 1
                spider_urls(full_url, keyword, max_depth - 1)

url = input("Enter the URL: ") 
keyword = input("Enter the keyword: ")

# Set max_depth to 2 so it doesn't crash the computer/get the programmer banned from a site
spider_urls(url, keyword, max_depth=2)

# https://en.wikipedia.org/wiki/Programmer
