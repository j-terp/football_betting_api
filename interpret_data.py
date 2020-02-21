from get_data import dataset_to_dictionary, fetch_data, single_match
from get_values import football_values
import time
start_time = time.time()

relevant_data = fetch_data() # Hämtar data

match_list = dataset_to_dictionary(relevant_data) # Konverterar datan till dictionary
# match_list[index för matchens rad][target-data]

row = single_match(0)


"""
print(relevant_data)
print(match_list)
print(row)
"""


def HTG_compare(match):
    hometeam = match_list[match]['HTHG']
    awayteam = match_list[match]['HTAG']

    if hometeam > awayteam:
        return football_values[0], "H"
    
    elif hometeam == awayteam:
        return 0, "D"
    
    else:
        return -(football_values[0]), "A"


def S_compare(match):
    hometeam = match_list[match]['HS']
    awayteam = match_list[match]['AS']

    if hometeam > awayteam:
        return football_values[1], "H"
    
    elif hometeam == awayteam:
        return 0, "D"
    
    else:
        return -(football_values[1]), "A"

def ST_compare(match):
    hometeam = match_list[match]['HST']
    awayteam = match_list[match]['AST']

    if hometeam > awayteam:
        return football_values[2], "H"
    
    elif hometeam == awayteam:
        return 0, "D"
    
    else:
        return -(football_values[2]), "A"

def Y_compare(match):
    hometeam = match_list[match]['HY']
    awayteam = match_list[match]['AY']

    if hometeam > awayteam:
        return football_values[3], "H"
    
    elif hometeam == awayteam:
        return 0, "D"
    
    else:
        return -(football_values[3]), "A"


def R_compare(match):
    hometeam = match_list[match]['HR']
    awayteam = match_list[match]['AR']

    if hometeam > awayteam:
        return football_values[4], "H"
    
    elif hometeam == awayteam:
        return 0, "D"
    
    else:
        return -(football_values[4]), "A"


def winning_team(team_score):
    print(team_score)
    if team_score > 0:
        return "H"
    elif team_score < 0:
        return "A"
    else:
        return "D"

def check_predictions(match, results):
    if results == match_list[match]['FTR']:
        print("Program was correct")
        return 1
    else:
        print("Program was incorrect")
        return 0

def betting(match, results):
    money_bet = 100
    if results == match_list[match]['FTR']:
        if results == "H":
            return money_bet * match_list[match]['B365H']
        elif results == 'D':
            return money_bet * match_list[match]['B365D']
        else:
            return money_bet * match_list[match]['B365A']
    else:
        return -100

money_earned = 0
predictions = 0
for y in match_list:
    results = HTG_compare(y)[0]
    function_return_id = HTG_compare(y)[1]
    
    results += ST_compare(y)[0]
    function_return_id += ST_compare(y)[1]
    
    results += S_compare(y)[0]
    function_return_id += S_compare(y)[1]
    
    results += Y_compare(y)[0]
    function_return_id += Y_compare(y)[1]
    
    results += R_compare(y)[0]
    function_return_id += R_compare(y)[1]
    
    match_predictions = winning_team(results)
    predictions += check_predictions(y, match_predictions)
    money_earned += betting(y, match_predictions)
print(money_earned, " kr earned")
print((money_earned/380), " kr earned on average per match")
print("Program predicted results in ", round(((predictions / 380) * 100)), "%", "of matches")
print("--- %s seconds ---" % (time.time() - start_time))




