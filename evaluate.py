from get_data import csv_fetch, csv_append, csv_return, csv_clean, df_from_dict, df_to_dict
import pandas as pd
from get_values import football_values

def evalHTG(prediction, match):
    if prediction[match]["HTG"] == prediction[match]["FTR"]:
        return 0.000001
    else:
        return -0.000001

def evalS(prediction, match):
    if prediction[match]["S"] == prediction[match]["FTR"]:
        return 0.000001
    else:
        return -0.000001

def evalST(prediction, match):
    if prediction[match]["ST"] == prediction[match]["FTR"]:
        return 0.000001
    else:
        return -0.000001

def evalY(prediction, match):
    if prediction[match]["Y"] == prediction[match]["FTR"]:
        return 0.000001
    else:
        return -0.000001

def evalR(prediction, match):
    if prediction[match]["R"] == prediction[match]["FTR"]:
        return 0.000001
    else:
        return -0.000001



def main_eval():
    base_dataframe = csv_fetch()
    base_dictionary, _ = df_to_dict(base_dataframe)
    for match in range(4180):
        football_values[0] += evalHTG(base_dictionary, match)
        football_values[1] += evalS(base_dictionary, match)
        football_values[2] += evalST(base_dictionary, match)
        football_values[3] += evalY(base_dictionary, match)
        football_values[4] += evalR(base_dictionary, match)

    temp = str(football_values)
    temp = temp[1:-1]
    print(temp)
    file = open("football_values.txt","r+")
    file.truncate(0)
    file.write(temp)
    file.close()
    