from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(r'C:/webdrivers/chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url)

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def get_matches():
    driver.get("https://www.flashscore.com/")
    time.sleep(3)
    driver.find_element_by_xpath("""//*[@id="live-table"]/div[1]/div/div[2]""").click()

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    matches_raw = soup.find_all('div', class_='event__match' )
    match_id = []
    for tag in matches_raw:
        match_id.append(tag.get("id"))

    return match_id

def get_stats1(match):
    
   
    driver.implicitly_wait(3)
    match_url = "https://www.flashscore.com/match/" + match[4:] + "/#match-summary"
    driver.get(match_url)
        
    time.sleep(3)
    driver.find_element_by_xpath("""//*[@id="li-match-statistics"]""").click()
    driver.implicitly_wait(3)
        
    info_raw = driver.find_elements_by_class_name("statText.statText")
    info = []
    for element in info_raw:
        info.append(element.text)
        
    driver.implicitly_wait(3)
    info = remove_values_from_list(info, '')
        
    time.sleep(1)
    return(info)


def get_stats(matches):
    info_stat = []
    
    for match in matches:
        match_url = "https://www.flashscore.com/match/" + match[4:] + "/#match-summary"
        print(match_url)
        driver.get(match_url)
        
        time.sleep(3)
        driver.find_element_by_xpath("""//*[@id="li-match-statistics"]""").click()
        driver.implicitly_wait(3)
        
        info_raw = driver.find_elements_by_class_name("statText.statText")
        info = []
        for element in info_raw:
            info.append(element.text)
        
        driver.implicitly_wait(3)
        info = remove_values_from_list(info, '')
        
        info_stat.append(info)
        driver.implicitly_wait(3)
    driver.quit()
    return info_stat


#matches = ["eeeez7bKeorA", "eeeeU5iTgPCM", "eeeeSteCc7Dc", "eeeedGaGdRS3", "eeeeQywal3zp", "eeeeIVmPf5cG"] #test list for get_stats

#matches = get_matches()
#print(matches)
#get_stats(matches)
