import statistics
from helpers import *
from funct import *

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
      value = keyLookup.get(value, value) # remaps values from raw number to label, if number not mapped, actual value remains
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
    print (key, " "*(longestlength-len(key)+2), resultDistrib[key], "\t", round(100*resultDistrib[key]/sum(resultDistrib.values(), 2)), "%")

def histogram(resultDistrib):  
  ''' Creates a histogram of the variable of interest from the result
  of the function "distribution" '''
  keys = sorted(resultDistrib.keys(), key = lambda  key: resultDistrib[key], reverse= True)
  longestlength = 0
  for key in keys:
    if len(key) > longestlength:
      longestlength = len(key) 
  for key in keys:
    print (key, " "*(longestlength-len(key)+2), '*'*int(100*resultDistrib[key]/sum(resultDistrib.values())), '\t', round(100*resultDistrib[key]/sum(resultDistrib.values(), 2)), "%")

def twovar (data, var1, var2): 
  ''' Creates a dictionary of dictionaries that show for each level of var1, the frequency of each response of var 2'''
  result = {}
  for row in data:
    value1=row[var1]
    value2=row[var2]
    if value1 not in result: # create a dictionary for state, the first time a row has a state that hasn't been seen yet in the for loop
      result[value1] = {}
    if value2 not in result[value1]: # once you have dict for state, add response values to it 
      result[value1][value2] = 1 # if response value new, i.e., new key in the state dict, then the value for that key is 1, after that the value for the key is x + 1
    else: 
      result[value1][value2] += 1
  return result      
  
  # Continuous variables in the dataset: poorhealth, sleptim1, avedrnk2
# univariate stats for poorhealth
#  need to remove the missing responses
def univariate (data, var):
  totalvars = 0
  countvars = 0
  minvar = 500 
  maxvar = 0 
  for row in data:
    vars = row[var]
    if vars != '77' and vars != '88' and vars != '99' and vars != '':
      vars = int(vars) 
      totalvars += vars
      countvars += 1
      if vars < minvar:
        minvar = vars
      if vars > maxvar:
        maxvar = vars
  avevar = round(totalvars/countvars, 2)
  #calculate mode
  premode = distribution(data, var)
  maxv = 0
  for k,v in premode.items():
    if k != 'missing':
      if v > maxv:
        maxv = v
        maxk = k
  modevars = maxk
  # calculate median
  medianlist = []
  for row in data:
    vars = row[var]
    if vars != '77' and vars != '88' and vars != '99' and vars != '':
      vars = int(vars) 
      medianlist.append(vars)
  medianvars = statistics.median(medianlist)
  print ('Total: ', vars, 'Count: ', countvars, 'Average : ', avevar)
  print ('Min : ', minvar, 'Max : ', maxvar, 'Mode : ', modevars)
  print ('Median : ', medianvars)
  print (premode)