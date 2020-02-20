import pandas as pd

def fetch_data():
    data = pd.read_csv(r'football_data.csv') # All data
    output = pd.DataFrame(data, columns= ['HomeTeam','AwayTeam', 'FTHG','FTAG','FTR','HTHG','HTAG','HS','AS','HST','AST','HY','AY','HR','AR'])
    return output # Sorted data

def dataset_to_dictionary(dataset):
    main_dictionary = dataset.to_dict('index')
    return main_dictionary

def single_match(index):
    data_set = fetch_data()
    single = data_set.loc[index,:] # Skapar en kolumn för en enskild match
    return single