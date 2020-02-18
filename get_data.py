import pandas as pd

data = pd.read_csv(r'football_data.csv') # All data
relevant_data = pd.DataFrame(data, columns= ['HomeTeam','AwayTeam', 'FTHG','FTAG','HTHG','HTAG','HS','AS','HST','AST','HY','AY','HR','AR'])
print(relevant_data)

list_of_matches = {}
i = 0 # Möjligt att iterera alla matcher med loop
temp_dict = {}

for j in range(14):
    temp_dict[relevant_data.columns[j]] = relevant_data.loc[i,:][j]
list_of_matches[i] = temp_dict

print(list_of_matches)
print(list_of_matches[0]["HomeTeam"]) # Möjligt att kalla på specifika värden inom matcher
# lst_ofmatches[index för matchens rad][target-data]

row = relevant_data.loc[0,:] # Skapar en kolumn för en enskild match
print(row)