
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

service = Service(r'C:/webdrivers/chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url)

match_url = "https://www.flashscore.com/match/APnv8Zkc/#match-summary"
driver.get(match_url)
time.sleep(2)

driver.find_element_by_xpath("""//*[@id="li-match-statistics"]""").click()
content = driver.page_source
#soup = BeautifulSoup(content, features="html.parser")
#stats = soup.find_all('div', class_='statText.statText')

#info = driver.find_elements_by_class_name('statTextGroup')
time.sleep(1)
info_raw = driver.find_elements_by_class_name("statText.statText")
info = []
for element in info_raw:
    info.append(element.text)
time.sleep(1)
info = remove_values_from_list(info, '')
print(info)
time.sleep(2)
driver.quit()
