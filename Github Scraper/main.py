from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# The account the youtuber created for testing this tool only 
# https://github.com/usernam121

driver = webdriver.Chrome()

driver.get("https://github.com/usernam121")
repo = "https://github.com/usernam121"

# time.sleep(2)
resources = driver.find_elements(By.CLASS_NAME, "repo")

links = []
repo_links = []


def loop(repo_link):
    driver.get(repo_link)
    # repo_name = driver.find_elements(By.CLASS_NAME, "Link--primary")  -----this also prints other element names-----
    
    # [href*='blob'] means "find links where the URL contains 'blob'"
    # [href*='tree'] catches inner folders if they exist
    repo_names = driver.find_elements(By.CSS_SELECTOR, "a.Link--primary[href*='/blob/'], a.Link--primary[href*='/tree/']")
    for i in repo_names:
        print(i.text)    


for i in resources:
    links.append(i.text)

# print(links)

for l in links: 
    repo_link = f"{repo}/{l}"
    repo_links.append(repo_link)
    loop(repo_link)

# print(repo_links)

time.sleep(2)
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
driver.quit()