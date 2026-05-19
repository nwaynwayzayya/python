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


def going_for_raw(file_in_repo):
    driver.get(file_in_repo)
    raw_button = driver.find_element(By.CSS_SELECTOR, 'a[data-testid="raw-button"]')
    raw_button.click()
    raw_code = driver.find_element(By.TAG_NAME, "body").text
    # print(raw_code)

    if "password" in raw_code:
        print("found password!")



def loop(repo_link):
    driver.get(repo_link)
    # repo_name = driver.find_elements(By.CLASS_NAME, "Link--primary")  -----this also prints other element names-----
    
    # [href*='blob'] means "find links where the URL contains 'blob'"
    # [href*='tree'] catches inner folders if they exist
    repo_names = driver.find_elements(By.CSS_SELECTOR, "a.Link--primary[href*='/blob/'], a.Link--primary[href*='/tree/']")
    for file_name in repo_names:
        # print(file_name.text)   
        pass 

    if "py" in file_name.text:
        file_in_repo = f"{repo_link}/blob/main/{file_name.text}"
        going_for_raw(file_in_repo)
        # print(file_in_repo)


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