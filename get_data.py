import pandas as pd

def fetch_data():
    data = pd.read_csv(r'football_data.csv') # All data
    output = pd.DataFrame(data, columns= ['HomeTeam','AwayTeam', 'FTHG','FTAG','FTR','HTHG','HTAG','HS','AS','HST','AST','HY','AY','HR','AR'])
    return output # Sorted data

def dataset_to_dictionary(dataset):
    main_dictionary = {}
    for i in range(380): # Möjligt att iterera alla matcher med loop, tillfälligt endast 3 (totala är 380)
        temp_dict = {}
        for j in range(14):
            temp_dict[dataset.columns[j]] = dataset.loc[i,:][j]
        main_dictionary[i] = temp_dict
    return main_dictionary

def single_match(index):
    data_set = fetch_data()
    single = data_set.loc[index,:] # Skapar en kolumn för en enskild match
    return single