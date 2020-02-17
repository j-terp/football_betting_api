import pandas as pd

data = pd.read_csv(r'football_data.csv') # All data
columns = pd.DataFrame(data, columns= ['HomeTeam','AwayTeam', 'FTHG','FTAG','HTHG','HTAG','HS','AS','HST','AST','HY','AY','HR','AR'])
print(columns)

'''
for x in range(380):
    for y in columns.loc[x,:]:
        print(y)
'''

row = columns.loc[0,:]
print(row[2])
print(row)
for y in (row):
    print(y)
