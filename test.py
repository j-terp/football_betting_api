from get_data import pd, dataset_to_dictionary
fetched_dataframe = pd.read_csv(r'dataframe.csv')

dictionary_keys = []
for col in fetched_dataframe.columns:
    dictionary_keys.append(col)
print(dictionary_keys)

fetched_dictionary = pd.DataFrame(fetched_dataframe).to_dict('index')
print(fetched_dictionary)

values = [["Volvo V70", 69420],["Saab", 39900]]
addition_point = len(fetched_dictionary)
for x in values:
    temp_dict = {}
    for key in dictionary_keys:
        temp_dict[key] = x[dictionary_keys.index(key)]
    fetched_dictionary[addition_point + values.index(x)] = temp_dict
    print(fetched_dictionary)


export_dictionary = pd.DataFrame.from_dict(fetched_dictionary, orient='index')
export_csv = export_dictionary.to_csv(r'dataframe.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path