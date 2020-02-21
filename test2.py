from get_data import dataset_to_dictionary, fetch_data, single_match
from get_values import football_values


relevant_data = fetch_data() # Hämtar data

match_list = dataset_to_dictionary(relevant_data) # Konverterar datan till dictionary
# match_list[index för matchens rad][target-data]

row = single_match(0)

for y in range(5):
    print(football_values[y])