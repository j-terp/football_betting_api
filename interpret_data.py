from get_data import dataset_to_dictionary, fetch_data, single_match
from get_values import football_values


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

def ST_compare(match):
    hometeam = match_list[match]['HST']
    awayteam = match_list[match]['AST']

    if hometeam > awayteam:
        return football_values[1], "H"
    
    elif hometeam == awayteam:
        return 0, "D"
    
    else:
        return -(football_values[1]), "A"

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


predictions = 0
for y in match_list:
    results = HTG_compare(y)[0]
    function_return_id = HTG_compare(y)[1]
    results += ST_compare(y)[0]
    function_return_id += ST_compare(y)[1]
    match_predictions = winning_team(results)
    predictions += check_predictions(y, match_predictions)
print("Program predicted results in ", round(((predictions / 380) * 100)), "%", "of matches")




