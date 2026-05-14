from selenium import webdriver
from selenium.webdriver.common.by import By
import time

on = True

while on: 
    def five_seconds():
        time.sleep(5)
        driver = webdriver.Chrome()

        driver.get("https://www.amazon.com/HV-F2056-15-6-17-Laptop-Cooler-Cooling/dp/B00NNMB3KS/ref=sr_1_20?dib=eyJ2IjoiMSJ9.2qqLtTgwGr9VyEgWhZH2Uex9sHqXlApnghFDwYHCTlqnLptsWpZhtiUjlj_YnMLV4SpJ2l6uG_0tFjJcy_46VdOG8F8wOsrkML5GvUk5BXsEAoOfZIIk7SQii8nU2b-zwtgERPRv9hQunCLNte1HUIT31h9VJ8-BTzdAeqaMWRAxipB3uKPMNh0Rh5UhFzTNzIuRYoglpl92eEVhGG-CxD4qk0-Iy_aM9tYqwuERmXEhh2tosfqIkA8CtHP6Rka_a45j-n4qfvUc8gAKD738i6Cdto6jgP9P51A7dqhBf18.IQw6VwTc6pVGWO0H1CTPmvjEkwTJiaWpRMYjq961nSA&dib_tag=se&qid=1778700205&s=computers-intl-ship&sr=1-20&th=1")
        price = driver.find_element(By.CLASS_NAME, "a-price-whole")
        print(price.text)
        driver.quit()

    five_seconds()