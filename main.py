from get_url_SC import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import asyncio

# Software which navigates with Chrome
chrome_driver = ChromeDriverManager().install()
op = webdriver.ChromeOptions()
op.add_argument('headless')

# What we are going to use to give orders to Chrome
driver = webdriver.Chrome(options=op, service=Service(chrome_driver))

# Open browser at URL
url = asyncio.run((get_url_SC())) + 'browse/top10/'
driver.get(url)

top10 = []
show_covers = driver.find_elements(By.CLASS_NAME, "box-16x9")

for cover_img in show_covers:
    show = cover_img.find_element(By.TAG_NAME, "img").get_attribute("alt")
    top10.append(show)

# Close browser
driver.quit()

print(top10)