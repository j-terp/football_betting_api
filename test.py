from get_data import pd, dataset_to_dictionary
fetched_dataframe = pd.read_csv(r'football_values.csv')
print(fetched_dataframe)
value_list = [["A","B","C","D","E","F"]]
for value in value_list:
    appended_dataframe = fetched_dataframe.append(pd.DataFrame([value], columns=fetched_dataframe.columns), ignore_index=True)
print(appended_dataframe)
export_csv = appended_dataframe.to_csv(r'football_values.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path