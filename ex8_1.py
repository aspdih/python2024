from selenium import webdriver #pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("https://www.naver.com/")
driver.implicitly_wait(0.5)
query_text="프리미어리그 득점순위"
search_box=driver.find_element(by=By.CSS_SELECTOR,value="#query")
search_box.send_keys(query_text)
search_button=driver.find_element(by=By.ID,value="search-btn")
search_button.click()
temp_div=driver.find_element(by=By.CSS_SELECTOR,value="#playerRankTabPanel_0 > div > div.scroll > table > tbody > tr:nth-child(1) > td.tl.tp > a")
print(temp_div.text)
print("20225 정진표")
time.sleep(10)
