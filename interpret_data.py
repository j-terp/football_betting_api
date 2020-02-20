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
        print("Home team wins")
    elif team_score < 0:
        print("Away team wins")
    else:
        print("Draw")



for y in match_list:
    results = HTG_compare(y)[0]
    function_return_id = HTG_compare(y)[1]
    results += ST_compare(y)[0]
    function_return_id += ST_compare(y)[1]
    winning_team(results)
    print(function_return_id)



