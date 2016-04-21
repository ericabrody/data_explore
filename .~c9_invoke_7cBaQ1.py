#! /usr/bin/python3

import csv

dataDictionary = {
  'SMOKE100': {
    '': 'missing',
    '1': 'smoker',
    '2': 'never smoked',
    '7': "don't know",
    '9': 'refused'
  }
}

datafiles = ['smallbr2013.csv','smallbr2014.csv']
data = {}
for name in datafiles:
  with open(name) as f:
    rows = []
    for row in csv.DictReader(f):
      rows.append(row)
    data[name] =  rows


# for v in data['smallbr2014.csv']:
#   print (v)


def distributionSmall(data, whichVar):
  result = {}
  for row in data:
    value = row[whichVar]
    result[value] = result.get(value, 0) + 1
  return result

def distribution(data, whichVar):
  result = {}
  keyLookup = dataDictionary.get(whichVar)
  for row in data:
    value = row[whichVar]
    if keyLookup is not None:
      value = keyLookup[value]
    if value not in result:
      result[value] = 1
    else:
      result[value] += 1
  return result

def histogram(resultDistrib):
  biggest = max(resultDistrib.values())
  keys = list(resultDistrib.keys())
  keys.sort()
  for key in keys:
    print (key, "\t", resultDistrib[key], resultDistrib[key]/biggest)


histogram(distribution(data['smallbr2014.csv'], 'SMOKE100'))


