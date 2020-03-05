from get_data import csv_fetch, csv_append, csv_return, csv_clean, df_from_dict, df_to_dict
import pandas as pd
base_dataframe = csv_fetch()
base_dictionary, dictionary_keys = df_to_dict(base_dataframe)
print(base_dictionary)