import statistics
from dataDictionary import *
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
  print ("Value", " "*(longestlength-len("value")+2), "Num Responses", "\t", "Percent of Responses")
  for key in keys:
    print (key, " "*(longestlength-len(key)+2), resultDistrib[key], "\t\t\t", round(100*resultDistrib[key]/sum(resultDistrib.values(), 2)), "%")

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
#  need to remove the missing, don't know, and refused responses
def univbyvar2 (data, var1, var2):
  ''' Create min, max, and mean for continous variables by state or sex'''
  var1values = {}
  for row in data:
    v = row[var1]
    if v not in var1values:
      var1values[v] = [row] # the first time encounter a specific value for var1 (state or sex), e.g., first time encounter '9' for state, create a new list of dictionaries for var1value = '9'
    else:
      var1values[v].append(row) # when see a value a second+ time, we append another dictionary to the list of dictionary - each of these dictionaries is a row of the data
  result = {}
  for k in var1values.keys():
    result[k] = univariate(var1values[k], var2) # create a dictionary for each level/response of var1
  return result
  
# Continuous variables in the dataset: poorhealth, sleptim1, avedrnk2
# univariate stats for poorhealth
#  need to remove the missing, don't know, and refused responses
def univariate (data, var):
  mean = createaverage(data, var)
  mode = createmode(data, var)
  valueslist = extractvalues (data, var)
  medianvalue = createmedian(valueslist)
  minvars = min(valueslist)
  maxvars = max(valueslist)
  result = {'average': mean, 'min': minvars, 'max': maxvars, 'mode': mode, 'median': medianvalue}
  return result

def extractvalues (data, var):
  ''' create a list of all values for a particular variable (var) in data '''
  valueslist = []
  for row in data:
    mapped = mapResponse(var, row[var])
    if mapped != 'refused' and mapped != "don't know" and mapped != 'missing' and row[var] != '':
      vars = int(row[var]) 
      valueslist.append(vars)
  return valueslist

def mapResponse (var, value):
  ''' function to assign response value mappings from dataDictionary to data'''
  newlabel=value
  if var in dataDictionary:
    if value in dataDictionary[var]:
      newlabel = dataDictionary[var][value] # remaps values from raw number to label, if number not mapped, actual value remains - because newlabel is set to value above
  return newlabel
  
def createmedian(valueslist):
  valueslist = sorted(valueslist)
  numvalues = len(valueslist)
  if numvalues % 2 == 1:
    medianvalue = valueslist[numvalues//2]
  else:
    medianvalue = (valueslist[numvalues//2 - 1] + valueslist[numvalues//2])/2
  return medianvalue
  
def createaverage (data, var):
  totalvars = 0
  countvars = 0
  for row in data:
    vars = row[var]
    if vars != '77' and vars != '88' and vars != '99' and vars != '':
      vars = int(vars) 
      totalvars += vars
      countvars += 1
  avevar = round(totalvars/countvars, 2)
  return avevar
  
def createmode (data, var):
  premode = distribution(data, var)
  mode = 0
  keymode = None
  for k,v in premode.items():
    if k != 'missing' and k != 'refused' and k != "don't know" :
      v=int(v)
      if v > mode:
        mode = v
        keymode = [k] # creates a new list with just k in it
      elif v == mode: # to accomodate condition that there are multiple modes in the list of values
        keymode.append(k)
  return keymode
  
