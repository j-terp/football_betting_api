import requests
from bs4 import BeautifulSoup

URL = 'https://www.flashscore.se/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='live-table')

print(results.prettify())

job_elems = results.find_all('section', class_="container__fsbody")
print(job_elems)