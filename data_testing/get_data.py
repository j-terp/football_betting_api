import pandas as pd


def fetch_data(file):
    data = pd.read_csv(file) # All data
    output = pd.DataFrame(data, columns= ['HomeTeam','AwayTeam', 'FTHG','FTAG','FTR','HTHG','HTAG','HS','AS','HST','AST','HY','AY','HR','AR','B365H','B365A','B365D'])
    return output # Sorted data

def dataset_to_dictionary(dataset):
    main_dictionary = dataset.to_dict('index')
    return main_dictionary

def single_match(index, file):
    data_set = fetch_data(file)
    single = data_set.loc[index,:] # Skapar en kolumn för en enskild match
    return single

def csv_fetch():
    fetched_dataframe = pd.read_csv(r'data_testing/dataframe.csv')
    return fetched_dataframe

def csv_append(value_list):
    base_dataframe = csv_fetch()
    for value in value_list:
        base_dataframe = base_dataframe.append(pd.DataFrame([value], columns=base_dataframe.columns), ignore_index=True)
    return base_dataframe

def csv_return(dataframe):
    export_csv = dataframe.to_csv(r'data_testing/dataframe.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path
    return export_csv

def csv_clean():
    base_dataframe = csv_fetch()
    export_csv = pd.DataFrame(columns=base_dataframe.columns).to_csv(r'data_testing/dataframe.csv', index = None, header=True)
    return export_csv

def df_to_dict(dataframe):
    fetched_dictionary = pd.DataFrame(dataframe).to_dict('index')
    dictionary_keys = dataframe.columns
    return fetched_dictionary, dictionary_keys

def df_from_dict(dictionary):
    export_dict = pd.DataFrame.from_dict(dictionary, orient='index')
    return export_dict