from get_data import pd, dataset_to_dictionary
dictionary_keys = []
for col in pd.read_csv(r'dataframe.csv').columns:
    dictionary_keys.append(col)
#export_dataframe = pd.DataFrame.from_dict(fetched_dictionary, orient='index')
export_csv = pd.DataFrame(columns=dictionary_keys).to_csv(r'dataframe.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path