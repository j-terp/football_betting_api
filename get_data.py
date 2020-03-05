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

def csv_fetch():
    fetched_dataframe = pd.read_csv(r'dataframe.csv')
    dictionary_keys = []
    for col in fetched_dataframe.columns:
        dictionary_keys.append(col)
    fetched_dictionary = pd.DataFrame(fetched_dataframe).to_dict('index')
    return fetched_dictionary, dictionary_keys

def csv_append(value_list):
    base_dictionary, base_keys = csv_fetch()
    #value_list = [["Volvo V70", 69420],["Saab", 39900]]
    addition_point = len(base_dictionary)
    for x in value_list:
        temp_dict = {}
        for key in base_keys:
            temp_dict[key] = x[base_keys.index(key)]
        base_dictionary[addition_point + value_list.index(x)] = temp_dict
    return base_dictionary

def csv_return(dictionary):
    export_csv = pd.DataFrame.from_dict(dictionary, orient='index').to_csv(r'dataframe.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path
    return export_csv

def csv_clean():
    dictionary_keys = []
    for col in pd.read_csv(r'dataframe.csv').columns:
        dictionary_keys.append(col)
    export_csv = pd.DataFrame(columns=dictionary_keys).to_csv(r'dataframe.csv', index = None, header=True)
    return export_csv