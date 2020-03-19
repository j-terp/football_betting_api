
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(r'C:/webdrivers/chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url)
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flashscore.se/")
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
for a in soup.findAll('a',href=True, attrs={'class':"container__liveTableWrapper sport_page"}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text) 



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