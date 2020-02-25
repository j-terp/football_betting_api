import pandas as pd
file = "football_data.csv"

def fetch_data(file):
    data = pd.read_csv(file) # All data
    output = pd.DataFrame(data, columns= ['HomeTeam','AwayTeam', 'FTHG','FTAG','FTR','HTHG','HTAG','HS','AS','HST','AST','HY','AY','HR','AR','B365H','B365A','B365D'])
    return output # Sorted data

def dataset_to_dictionary(dataset):
    main_dictionary = dataset.to_dict('index')
    return main_dictionary

def single_match(index):
    data_set = fetch_data(file)
    single = data_set.loc[index,:] # Skapar en kolumn för en enskild match
    return single