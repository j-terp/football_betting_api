from get_data import dataset_to_dictionary, fetch_data, single_match


relevant_data = fetch_data() # Hämtar data

match_list = dataset_to_dictionary(relevant_data) # Konverterar datan till dictionary
# match_list[index för matchens rad][target-data]

row = single_match(0)

print(relevant_data)
print(match_list)
print(row)