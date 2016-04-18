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

# To view the data...
# for v in data['smallbr2014.csv']:
#   print (v)


def distribution(data, whichVar):
  '''Create a dictionary of results for a specific variable, 
    where the key is each response value that is in the dataset and
    value is the number of times it occurs in the data'''
  result = {}
  keyLookup = None
  if whichVar in dataDictionary:
    keyLookup = dataDictionary[whichVar]
  for row in data:
    value = row[whichVar]
    if keyLookup is not None:
      value = keyLookup[value] # remaps values from raw number to label
    if value not in result:
      result[value] = 1
    else:
      result[value] += 1
  return result 

def table(resultDistrib):
  ''' Creates a frequency table of the variable of interest from the result
  of the function "distribution" '''
  keys = sorted(resultDistrib.keys(), key = lambda  key: resultDistrib[key], reverse= True)
  longestlength = 0
  for key in keys:
    if len(key) > longestlength:
      longestlength = len(key)
  for key in keys:
    print (key, " "*(longestlength-len(key)+2), resultDistrib[key], "\t", resultDistrib[key]/sum(resultDistrib.values()))

table(distribution(data['smallbr2014.csv'], 'SMOKE100'))

def histogram(resultDistrib):  
  ''' Creates a histogram of the variable of interest from the result
  of the function "distribution" '''
  keys = sorted(resultDistrib.keys(), key = lambda  key: resultDistrib[key], reverse= True)
  longestlength = 0
  for key in keys:
    if len(key) > longestlength:
      longestlength = len(key) 
  for key in keys:
    print (key, " "*(longestlength-len(key)+2), '*'*int(100*resultDistrib[key]/sum(resultDistrib.values())), '\t', int(100*resultDistrib[key]/sum(resultDistrib.values())), "%")

histogram (distribution(data['smallbr2014.csv'], 'SMOKE100'))