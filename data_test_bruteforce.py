from get_data import dataset_to_dictionary, fetch_data, single_match
from get_values import football_values
import time
start_time = time.time()

relevant_data = fetch_data("football_data.csv") # Hämtar data

match_list = dataset_to_dictionary(relevant_data) # Konverterar datan till dictionary
# match_list[index för matchens rad][target-data]

row = single_match(0)


"""
print(relevant_data)
print(match_list)
print(row)
"""


def HTG_compare(match, val):
    hometeam = match_list[match]['HTHG']
    awayteam = match_list[match]['HTAG']

    if hometeam > awayteam:
        return val, "H"
    
    elif hometeam == awayteam:
        return 0, "D"
    
    else:
        return -val, "A"


def S_compare(match, val):
    hometeam = match_list[match]['HS']
    awayteam = match_list[match]['AS']

    if hometeam > awayteam:
        return val, "H"
    
    elif hometeam == awayteam:
        return 0, "D"
    
    else:
        return -val, "A"

def ST_compare(match, val):
    hometeam = match_list[match]['HST']
    awayteam = match_list[match]['AST']

    if hometeam > awayteam:
        return val, "H"
    
    elif hometeam == awayteam:
        return 0, "D"
    
    else:
        return -val, "A"

def Y_compare(match, val):
    hometeam = match_list[match]['HY']
    awayteam = match_list[match]['AY']

    if hometeam > awayteam:
        return -val, "A"
    
    elif hometeam == awayteam:
        return 0, "D"
    
    else:
        return val, "H"


def R_compare(match, val):
    hometeam = match_list[match]['HR']
    awayteam = match_list[match]['AR']

    if hometeam > awayteam:
        return -val, "A"
    
    elif hometeam == awayteam:
        return 0, "D"
    
    else:
        return val, "H"




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


money_earned = 0
predictions = 0
good_variables = []

for x in range(1,21):
    print((21-x), "loops left")
    for z in range(1,21):
        for b in range(1,21):
            for i in range(1,21):
                for n in range(1,21):
                    predictions = 0
                    for y in match_list:
                        results = HTG_compare(y, x)[0]
                        function_return_id = HTG_compare(y, x)[1]
                        
                        results += ST_compare(y, z)[0]
                        function_return_id += ST_compare(y, z)[1]
                        
                        results += S_compare(y, b)[0]
                        function_return_id += S_compare(y, b)[1]
                       
                        results += Y_compare(y, i)[0]
                        function_return_id += S_compare(y, b)[1]
                        
                        results += R_compare(y, n)[0]
                        function_return_id += S_compare(y, b)[1]       
                        
                        match_predictions = winning_team(results)
                        predictions += check_predictions(y, match_predictions)

                    if round(((predictions / 380) * 100)) > 70:
                        print("Program predicted results in ", round(((predictions / 380) * 100)), "%", "of matches")
                        print("Variables were", x, z, b)
                        good_variables.append([y, x ,z]) 
print("Program finished")
print(good_variables)
                    



