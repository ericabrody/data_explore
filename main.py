#! /usr/bin/python3
import csv
from dataDictionary import *
from funct import *

# read in the datafiles as dictionary of list of dictionaries
datafiles = ['smallbr2013.csv','smallbr2014.csv']
data = {}
for file in datafiles:
  with open(file) as f:
    reader = csv.DictReader(f)
    rows = []
    for row in reader: # creates a list of dictionaries where each case/row is a dictionary with a key-value pair for each variable
      rows.append(row)
    data[file] =  rows # storing each file's list of rows in the dictionary called data, key of this dictionary is filename
    # and the values of this dictionary are the list of dictionaries
    print (file, reader.fieldnames) #fieldnames = property of dictreader
    print (file)

# # To view the variables names (i.e., keys)...from the first row, but could have been any row
# print (data['smallbr2014.csv'][4].keys())

# twovarfreq = twovar(data['smallbr2014.csv'], '_STATE', 'EXERANY2')
# print ('Two Var output: ', twovarfreq)

for variable in categoricalVars:
  print (variable, varQuestion[variable])
  thingtoprint = distribution(data['smallbr2014.csv'], variable)
  table (thingtoprint)
  print ()
  histogram (thingtoprint)
  print()

for variable in continousVars:
  toprint = univariate(data['smallbr2014.csv'], variable)
  sep = ', '
  modeStrings = []
  for v in toprint['mode']: # for each item in the list of integers representing modes, this loop turns each item into a string, so .join works
    modeStrings.append(str(v))
  print (variable, varQuestion[variable])
  print ('Minimum = ', toprint['min'])
  print ('Maximum = ', toprint['max'])
  print ('Mean    = ', toprint['average'])
  print ('Median  = ', toprint['median'])
  print ('Mode    = ', sep.join(modeStrings))
  print ()
  
#print (univbyvar2 (data['smallbr2014.csv'], '_STATE', 'POORHLTH'))

# whichVar = 0
# try:
#   while whichVar != '':
#     whichVar = input('Which variable are you interested in?')
#     table(distribution(data['smallbr2014.csv'], whichVar))
#     histogram (distribution(data['smallbr2014.csv'], whichVar))
# except:
#   print ('Thank you for using this program.')
