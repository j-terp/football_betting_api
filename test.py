from get_data import pd, dataset_to_dictionary
fetched_dataframe = pd.read_csv(r'dataframe.csv')
print(fetched_dataframe)
fetched_dictionary = pd.DataFrame(fetched_dataframe).to_dict('index')
print(fetched_dictionary)
export_dictionary = pd.DataFrame.from_dict(fetched_dictionary)
print(export_dictionary)
export_csv = export_dictionary.to_csv(r'dataframe.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path