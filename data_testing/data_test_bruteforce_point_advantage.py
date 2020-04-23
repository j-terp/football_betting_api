from get_data import dataset_to_dictionary, fetch_data, single_match
from get_values import football_values
import time
start_time = time.time()

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
        return -(football_values[3]), "A"
    
    elif hometeam == awayteam:
        return 0, "D"
    
    else:
        return football_values[3], "H"


def R_compare(match):
    hometeam = match_list[match]['HR']
    awayteam = match_list[match]['AR']

    if hometeam > awayteam:
        return -(football_values[4]), "A"
    
    elif hometeam == awayteam:
        return 0, "D"
    
    else:
        return football_values[4], "H"


def winning_team(team_score):
    
    if team_score > 0:
        return "H"
    elif team_score < 0:
        return "A"
    else:
        return "D"

def check_predictions(match, results):
    if results == match_list[match]['FTR']:
        
        return 1
    else:
        
        return 0

def betting(match, results, points, value):
    money_bet = 100
    if points > (value/10) or points < (-value/10):
        if results == match_list[match]['FTR']:
            if results == "H":
                return money_bet * match_list[match]['B365H'] - 100, 1
            elif results == 'D':
                return money_bet * match_list[match]['B365D'] - 100, 1
            else:
                return money_bet * match_list[match]['B365A'] - 100, 1
        else:
            return -100, 1
    else: return 0, 0


file_list = ["imported_data/E0_2005.csv", "imported_data/E0_2006.csv", "imported_data/E0_2007.csv", "imported_data/E0_2008.csv", "imported_data/E0_2009.csv", "imported_data/E0_2010.csv", "imported_data/E0_2011.csv", "imported_data/E0_2012.csv", "imported_data/E0_2013.csv", "imported_data/E0_2014.csv", "imported_data/football_data.csv"]

for value in range(22):
    predictions_correct = 0
    money_earned = 0
    matches_bet = 0
    for file in file_list:
        relevant_data = fetch_data(file) # Hämtar data

        match_list = dataset_to_dictionary(relevant_data) # Konverterar datan till dictionary
        # match_list[index för matchens rad][target-data]

        row = single_match(0, file)

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
            predictions_correct += check_predictions(y, match_predictions)
            
            money_earned += betting(y, match_predictions, results, value)[0]
            matches_bet += betting(y, match_predictions, results, value)[1]
    print(money_earned, " kr earned")
    print((money_earned/matches_bet), " kr earned on average per match")
    print("Program bet on ", matches_bet, " matches")
    print("Limit was: ", value)




