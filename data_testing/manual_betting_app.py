from get_data import dataset_to_dictionary, fetch_data, single_match
from get_values import football_values
import time
start_time = time.time()
"""
print(relevant_data)
print(match_list)
print(row)
"""
def get_input():
    values = []
    values.append(input("Please enter goals of home team: "))
    values.append(input("Please enter goals of away team: "))
    values.append(input("Please enter shots of home team: "))
    values.append(input("Please enter shots of away team: "))
    values.append(input("Please enter shots on target of home team: "))
    values.append(input("Please enter shots on target of away team: "))
    values.append(input("Please enter yellow cards of home team: "))
    values.append(input("Please enter yellow cards of away team: "))
    values.append(input("Please enter red cards of home team: "))
    values.append(input("Please enter red cards away team: "))
    values.append(input("Please enter home team odds: "))
    values.append(input("Please enter away team odds: "))
    values.append(input("Please enter draw odds: "))
    return values
    
    



def HTG_compare(values):
    hometeam = int(values[0])
    awayteam = int(values[1])

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


def S_compare(values):
    hometeam = int(values[2])
    awayteam = int(values[3])

    if hometeam > awayteam:
        return football_values[1]
    
    elif hometeam == awayteam:
        return 0
    
    else:
        return -(football_values[1])

def ST_compare(values):
    hometeam = int(values[4])
    awayteam = int(values[5])

    if hometeam > awayteam:
        return football_values[2]
    
    elif hometeam == awayteam:
        return 0
    
    else:
        return -(football_values[2])

def Y_compare(values):
    hometeam = int(values[6])
    awayteam = int(values[7])

    if hometeam > awayteam:
        return -(football_values[3])
    
    elif hometeam == awayteam:
        return 0
    
    else:
        return football_values[3]


def R_compare(values):
    hometeam = int(values[8])
    awayteam = int(values[9])
    
    if hometeam > awayteam:
        return -(football_values[4])
    
    elif hometeam == awayteam:
        return 0
    
    else:
        return football_values[4]


def winning_team(team_score):
    print(team_score)
    if team_score > 0:
        return "H"
    elif team_score < 0:
        return "A"
    else:
        return "D"

def betting(prediction, values):
    if prediction == "H":
        if float(values[10]) > 1.1:
            print("You should bet for H")
        else:
            print("You should not bet")
    
    elif prediction == 'D':
        if float(values[12]) > 1.1:
            print("You should bet for D")
        else:
            print("You should not bet")
    
    else:
        if float(values[11]) > 1.1:
            print("You should bet for A")
        else:
            print("You should not bet")
    


if __name__ == "__main__":
    money_earned = 0
    predictions_correct = 0
    matches_bet = 0
    matches_bet_correct = 0
  
    values = get_input()

    results = HTG_compare(values)
            
    results += ST_compare(values)
            
    results += S_compare(values)

            
    results += Y_compare(values)

            
    results += R_compare(values)
           
    prediction = winning_team(results)

    betting(prediction, values)
