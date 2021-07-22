'''
find_duplicates.py
Duplicate Detector v1.0
Built with Python, TKinter, FuzzyWuzzy, and Pandas
Abdul Ali Khan
'''

import pandas as pd
from fuzzywuzzy import process, fuzz


def fetchKeyByValue(dict, value):
    return [key for key in dict if (dict[key] == value)]


def findDuplicates(filePath, description):
    df = pd.read_csv(filePath)
    descriptions = []
    descIdPairs = {}
    for index, row in df.iterrows():
        descriptions.append(row['description'])
        descIdPairs[row['record_id']] = row['description']
    Ratios = process.extract(description, descriptions,
                             processor=None, scorer=fuzz.token_set_ratio)
    possibleDuplicates = []
    for record in Ratios:
        recordID = fetchKeyByValue(descIdPairs, record[0])
        thisRecord = [record[0], record[1], recordID[0]]
        possibleDuplicates.append(thisRecord)
    return possibleDuplicates
