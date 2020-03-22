
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(r'C:/webdrivers/chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get("https://www.flashscore.com/")
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
"""
print(soup)
"""

driver.find_element_by_xpath("""//*[@id="live-table"]/div[1]/div/div[2]""").click()

titles_element = driver.find_elements_by_xpath("""/html/body/div[6]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div[2]/div/div/div[2]/div[6]""")
"""
print(titles_element)
"""
table = driver.find_elements_by_class_name("container__fsbody")
for thing in table:
    print(thing.text)
    print()
#print(table)
time.sleep(5)
driver.quit()


"""
for a in soup.findAll('a',href=True, attrs={'class':"container__liveTableWrapper sport_page"}):
    name = a.find('div', attrs={'class':'_3wU53n'})
    price = a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating = a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text) 

print(products)
"""

"""
time.sleep(5) # Let the user actually see something!
driver.quit()
"""


"""
url = "https://www.flashscore.se/"

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
teams = []
time = []
score = []
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    teams = a.find('div', attrs={'class':'_3wU53n'})
    time = a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    score = a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    teams.append(teams.text)
    time.append(time.text)
    score.append(score.text) 
"""