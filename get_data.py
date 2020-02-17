import pandas as pd

data = pd.read_csv(r'football_data.csv') # All data
columns = pd.DataFrame(data, columns= ['HomeTeam','AwayTeam', 'FTHG','FTAG','HTHG','HTAG','HS','AS','HST','AST','HY','AY','HR','AR'])
print(columns)
row0 = columns.loc[0,:]
print(row0[2])
