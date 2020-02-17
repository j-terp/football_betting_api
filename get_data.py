import pandas as pd

data = pd.read_csv(r'football_data.csv') # All data
columns = pd.DataFrame(data, columns= ['HomeTeam','AwayTeam','FTR','HTHG','HTAG','HS','AS','HST','AST','HY','AY','HR','AR'])
print(columns.loc[0,:])
