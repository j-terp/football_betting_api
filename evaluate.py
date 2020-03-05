from get_data import csv_fetch, csv_clean
import pandas as pd
csv_clean()
csv, keys = csv_fetch()
print(csv[0])