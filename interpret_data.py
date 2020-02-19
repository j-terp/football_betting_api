from get_data import dataset_to_dictionary, fetch_data, single_match


relevant_data = fetch_data() # Hämtar data

match_list = dataset_to_dictionary(relevant_data) # Konverterar datan till dictionary
# match_list[index för matchens rad][target-data]

row = single_match(0)

"""
print(relevant_data)
print(match_list)
print(row)
print(match_list[2])
print(match_list[2]["AY"])
"""
def HTG_compare(match):
    hometeam = match_list[match]['HTHG']
    awayteam = match_list[match]['HTAG']

    if hometeam > awayteam:
        return 1
    elif hometeam == awayteam:
        return 0
    else:
        return -1

def ST_compare(match):
    hometeam = match_list[match]['HST']
    awayteam = match_list[match]['AST']

    if hometeam > awayteam:
        return 0.5
    elif hometeam == awayteam:
        return 0
    else:
        return -0.5

def winning_team(team_score):
    print(team_score)
    if team_score > 0:
        print("Home team wins")
    elif team_score < 0:
        print("Away team wins")
    else:
        print("Draw")

for y in match_list:
    team_score = HTG_compare(y)
    team_score += ST_compare(y)
    winning_team(team_score)



