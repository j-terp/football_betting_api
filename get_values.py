import pandas as pd 

data = pd.read_csv(r'football_values.csv') # All data
output = pd.DataFrame(data, columns= ['HTG','S', 'ST','Y','R'])
print(output["S"])
x = 0
x = x + output("S")
print(x)
#data = data.to_dict('records')