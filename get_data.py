import pandas as pd

data = pd.read_csv(r'football_data.csv') # All data
columns = pd.DataFrame(data, columns= ['HomeTeam','AwayTeam', 'FTHG','FTAG','HTHG','HTAG','HS','AS','HST','AST','HY','AY','HR','AR'])
print(columns)

lst_of_matches = {}
i = 0 # Möjligt att iterera alla matcher med loop
temp_dict = {}

for j in range(14):
    temp_dict[columns.columns[j]] = columns.loc[i,:][j]
lst_of_matches[i] = temp_dict

print(lst_of_matches)
print(lst_of_matches[0]["HomeTeam"]) # Möjligt att kalla på värden inom matcher

row = columns.loc[0,:] # Skapar en kolumn för en enskild match
print(row)