from get_data import dataset_to_dictionary, fetch_data, single_match


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
        return "H"
    elif hometeam == awayteam:
        return "D"
    else:
        return "A"

def ST_compare(match):
    hometeam = match_list[match]['HST']
    awayteam = match_list[match]['AST']

    if hometeam > awayteam:
        return "H"
    elif hometeam == awayteam:
        return "D"
    else:
        return "A"

def value(results, val):
    if results.count('H') > results.count('A'):
        return 1
    elif results.count('D') > results.count('A') and results.count('D') > results.count('H'):
        return 0
    else:
        return -1



def winning_team(team_score):
    print(team_score)
    if team_score > 0:
        print("Home team wins")
    elif team_score < 0:
        print("Away team wins")
    else:
        print("Draw")


for y, val in enumerate(match_list):
    results = HTG_compare(y)
    results += ST_compare(y)
    results_value = value(y, val)



