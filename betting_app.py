
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from get_values import football_values

service = Service(r'C:/webdrivers/chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url)
driver.implicitly_wait(15)

def HTG_compare(score):
    hometeam = int(score[0])
    awayteam = int(score[1])

    if hometeam > awayteam:
        if (hometeam - awayteam) == 1:
            return (football_values[0])
            
        elif (hometeam - awayteam) == 2:
            return (football_values[0] * 1.2)
            
        elif (hometeam - awayteam) == 3:
            return (football_values[0] * 1.5)
            
        else:
            return (football_values[0] * 2)      
    
    elif awayteam > hometeam:
        if (awayteam - hometeam) == 1:
            return -(football_values[0])
            
        elif (awayteam - hometeam) == 2:
            return -(football_values[0] * 1.2)
            
        elif (awayteam - hometeam) == 3:
            return -(football_values[0] * 1.5)
            
        else:
            return -(football_values[0] * 2)

    elif hometeam == awayteam:
        return 0
    
    else:
        print("Error")

def S_compare(value):
    hometeam = (int(value['Shots on Goal'][0]) + int(value["Shots off Goal"][0]))
    awayteam = (int(value['Shots on Goal'][1]) + int(value["Shots off Goal"][1]))

    if hometeam > awayteam:
        if (hometeam - awayteam) < 3:
            return (football_values[1])
            
        elif (hometeam - awayteam) < 5:
            return (football_values[1] * 1.2)
            
        elif (hometeam - awayteam) < 7:
            return (football_values[1] * 1.5)
            
        else:
            return (football_values[1])    
    
    elif awayteam > hometeam:
        if (awayteam - hometeam) < 3:
            return -(football_values[1])
            
        elif (awayteam - hometeam) < 5:
            return -(football_values[1] * 1.2)
            
        elif (awayteam - hometeam) < 7:
            return -(football_values[1] * 1.5)
            
        else:
            return -(football_values[1] * 2)

    elif hometeam == awayteam:
        return 0
    
    else:
        print("Error")

def ST_compare(value):
    hometeam = int(value['Shots on Goal'][0])
    awayteam = int(value['Shots on Goal'][1])

    if hometeam > awayteam:
        if (hometeam - awayteam) < 3:
            return (football_values[2])
            
        elif (hometeam - awayteam) < 5:
            return (football_values[2] * 1.2)
            
        elif (hometeam - awayteam) < 7:
            return (football_values[2] * 1.5)
            
        else:
            return (football_values[2] * 2)      
    
    elif awayteam > hometeam:
        if (awayteam - hometeam) < 3:
            return -(football_values[2])
            
        elif (awayteam - hometeam) < 5:
            return -(football_values[2] * 1.2)
            
        elif (awayteam - hometeam) < 7:
            return -(football_values[2] * 1.5)
            
        else:
            return -(football_values[2] * 2)

    elif hometeam == awayteam:
        return 0
    
    else:
        print("Error")

def Y_compare(value):
    hometeam = int(value['Yellow Cards'][0]) 
    awayteam = int(value['Yellow Cards'][1])


    if hometeam > awayteam:
        if (hometeam - awayteam) < 3:
            return -(football_values[3])
            
        elif (hometeam - awayteam) < 5:
            return -(football_values[3] * 1.2)
            
        elif (hometeam - awayteam) < 7:
            return -(football_values[3] * 1.5)
            
        else:
            return -(football_values[3])      
    
    elif awayteam > hometeam:
        if (awayteam - hometeam) < 3:
            return (football_values[3])
            
        elif (awayteam - hometeam) < 5:
            return (football_values[3] * 1.2)
            
        elif (awayteam - hometeam) < 7:
            return (football_values[3] * 1.5)
            
        else:
            return (football_values[3] * 2)

    elif hometeam == awayteam:
        return 0
    
    else:
        print("Error")
    


def R_compare(value):
    try:
        hometeam = int(value['Red Cards'][0]) 
    except:
        hometeam = 0
    
    try:
        awayteam = int(value['Red Cards'][0])
    except:
        awayteam = 0 


    if hometeam > awayteam:
        if (hometeam - awayteam) < 2:
            return -(football_values[4])
            
        elif (hometeam - awayteam) < 3:
            return -(football_values[4] * 1.2)
            
        elif (hometeam - awayteam) < 4:
            return -(football_values[4] * 1.5)
            
        else:
            return -(football_values[4] * 2)     
    
    elif awayteam > hometeam:
        if (awayteam - hometeam) < 2:
            return (football_values[4])
            
        elif (awayteam - hometeam) < 3:
            return (football_values[4] * 1.2)
            
        elif (awayteam - hometeam) < 4:
            return (football_values[4] * 1.5)
            
        else:
            return (football_values[4] * 2)

    elif hometeam == awayteam:
        return 0
    
    else:
        print("Error")
    
def winning_team(team_score):

    if team_score > 0:
        return "H"
    elif team_score < 0:
        return "A"
    else:
        return "D"

def get_stats(matches):
    info_stat = []
    
    for match in matches:
        match_url = "https://www.flashscore.com/match/" + match[4:] + "/#match-summary"
        print(match_url)
        driver.get(match_url)
        
        time.sleep(3)
        driver.find_element_by_xpath("""//*[@id="li-match-statistics"]""").click()
        time.sleep(1)
        
        info_raw = driver.find_elements_by_class_name("statText.statText")
        standings_raw = driver.find_elements_by_class_name("current-result").text
        print(standings_raw)
        info = []
        for element in info_raw:
            info.append(element.text)
        
        driver.implicitly_wait(3)
        info = remove_values_from_list(info, '')
        
        info_stat.append(info)
        time.sleep(2)
    driver.quit()
    return info_stat

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def get_matches():
    driver.get("https://www.flashscore.com/")
    
    driver.find_element_by_xpath("""//*[@id="live-table"]/div[1]/div/div[2]""").click()

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    matches_raw = soup.find_all('div', class_='event__match' )
    print(matches_raw)
    match_id = []
    for tag in matches_raw:
        match_id.append(tag.get("id"))

    return match_id


def get_stats1(match):
    
   
    
    match_url = "https://www.flashscore.com/match/" + match[4:] + "/#match-summary"
    driver.get(match_url)
        
        
    driver.find_element_by_xpath("""//*[@id="li-match-statistics"]""").click()
    

    standings_raw = driver.find_elements_by_class_name("current-result")    
    info_raw = driver.find_elements_by_class_name("statText.statText")
    
    standings = []
    for char in standings_raw:
        standings.append(char.text)
    info = []
    for element in info_raw:
        info.append(element.text)
        
    
    info = remove_values_from_list(info, '')
        
    
    return(info, standings)

def list_to_string(s):  
    
    str1 = ""  
       
    for ele in s:  
        str1 += ele   
       
    return str1  

if __name__ == "__main__":
    matches1 = ["eeeez7bKeorA", "eeeeU5iTgPCM", "eeeeSteCc7Dc", "eeeedGaGdRS3", "eeeeQywal3zp", "eeeeIVmPf5cG"]
    try:
        matches = get_matches()
        print(matches)
    
    except:
        matches = get_matches()
    
    finally:
        for match in matches1:
            stat_input, standings_unprocessed = get_stats1(match) #Should be matches once matches are live again
            
            standings = []
            standings_unprocessed = list_to_string(standings_unprocessed)
            print(standings_unprocessed)
            standings.append(standings_unprocessed[0])
            standings.append(standings_unprocessed[3])
            match_stat = {}
            for x in range(int(len(stat_input) / 3)):
                match_stat[stat_input[1]] = [stat_input[0], stat_input[2]]
                stat_input = stat_input[3:]
            print(match_stat)
            print(standings)
            team_performance_score = HTG_compare(standings)
            team_performance_score += ST_compare(match_stat)
            team_performance_score += S_compare(match_stat)
            team_performance_score += Y_compare(match_stat)
            team_performance_score += R_compare(match_stat)
            prediction = winning_team(team_performance_score)
            print(prediction)
            print("Match done")
            
        driver.quit()