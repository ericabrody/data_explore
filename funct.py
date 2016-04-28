from dataDictionary import *
from funct import *
import csv

def loaddata (filename):
  ''' read in datafile for analysis, resulting file is a dictionary of dictionaries
      where each row of data is a dictionary, the key is the variable name from the top row of data'''
  with open(filename) as f:
    reader = csv.DictReader(f) # information obtained from https://docs.python.org/3/library/csv.html
    rows = []
    for row in reader: # creates a list of dictionaries where each case/row is a dictionary with a key-value pair for each variable
      rows.append(row)
    if sorted(reader.fieldnames) != sorted(dataDictionary.keys()): # check if contains variables with appropriate names and response value labesl
      print ('Your variable names are different than expected.')
      print ('Desired fieldnames: ' , ', '.join(sorted(dataDictionary.keys())))
      print ('Your fieldnames: ', ', '.join(sorted(reader.fieldnames)))
      return []
    else:
      return rows
      
def mapResponse (var, value):
  ''' function to assign response value mappings from dataDictionary to data'''
  newlabel=value
  if var in dataDictionary:
    if value in dataDictionary[var]:
      newlabel = dataDictionary[var][value] # remaps values from raw number to label, if number not mapped, actual value remains - because newlabel is set to value above
  return newlabel
      

def distribution(data, whichVar):
  '''Create a dictionary of results for a specific variable, 
    where the key is each response value that is in the dataset and
    value is the number of times it occurs in the data; best used for categorical variables'''
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
  ''' Creates a frequency table of the variable of interest from the dictionary result 
  from the function "distribution", best used for categorical variables '''
  keys = sorted(resultDistrib.keys(), key = lambda  key: resultDistrib[key], reverse= True) # code obtained from https://docs.python.org/3/howto/sorting.html
  longestlength = 0
  for key in keys:
    if len(key) > longestlength: # getting longest length of key (i.e., response value) to use, so printing of results lines up nicely
      longestlength = len(key)
  print ("Value", " "*(longestlength-len("value")+2), "Num Responses", "\t", "Percent of Responses")
  for key in keys:
    print (key, " "*(longestlength-len(key)+2), resultDistrib[key], "\t\t\t", round(100*resultDistrib[key]/sum(resultDistrib.values(), 2)), "%")

def histogram(resultDistrib):  
  ''' Creates a histogram of the variable of interest from the dictionary resulting
  from the function "distribution" - best for categorical variables '''
  keys = sorted(resultDistrib.keys(), key = lambda  key: resultDistrib[key], reverse= True)
  longestlength = 0
  for key in keys:
    if len(key) > longestlength: # getting longest length of key (i.e., response value) to use, so printing of results lines up nicely
      longestlength = len(key) 
  for key in keys:
    print (key, " "*(longestlength-len(key)+2), '*'*int(100*resultDistrib[key]/sum(resultDistrib.values())), '\t', round(100*resultDistrib[key]/sum(resultDistrib.values(), 2)), "%")

def barcategbystate (data, sexstate, var2):
  ''' Bar chart of a categorical variable by sex or state'''
  twovarresult = twovar (data, sexstate, var2)
  sexstatekeys = list(twovarresult.keys()) #keys of first level of dictionary (i.e., NC or CT; M or F)
  categvarkeys = twovarresult.values() # keys of second level of dictionary (e.g., Excellent, Very good, good, fair, poor)
  longestlength = 0
  print (varQuestion[var2])
  for k in sexstatekeys:
    print ((str(mapResponse (sexstate, k)) + ' ')*10)
    for categvar in sorted(twovarresult[k].keys()):
      print ('{:>10s} {:10d}% {:<100s}'.format (str(mapResponse(var2, categvar)), round(100*twovarresult[k][categvar]/sum(twovarresult[k].values(), 2)), '*'*int(100*twovarresult[k][categvar]/sum(twovarresult[k].values()))))

def twovar (data, var1, var2): 
  ''' Creates a dictionary of dictionaries that show for each level of var1, the frequency of each response of var 2
      - best used with categorical varilabes'''
  result = {}
  for row in data:
    value1=row[var1]
    value2=row[var2]
    if value1 not in result: # creating a dictionary for each level of state, the first time a row has a state that hasn't been seen yet in the for loop
      result[value1] = {}
    if value2 not in result[value1]: # once you have dict for state, add response values to it 
      result[value1][value2] = 1 # if response value new, i.e., new key in the state dict, then the value for that key is 1, after that the value for the key is x + 1
    else: 
      result[value1][value2] += 1
  return result      
  
def printcategbysexstate (data, sexstate, categvar):
  ''' Nice printout of a categorical variable by sex or state'''
  toprint= twovar(data, sexstate, categvar)
  catkeys = list(toprint.keys())
  if len(catkeys) != 2:
    print ('hm, there are more than two category one choices, we are not set up for this') # program is not set up for looking at a byvariable with more than 2 response values
    return
  print (categvar, varQuestion[categvar])
  print ('          {:>10s} {:>10s}'.format(mapResponse(sexstate,catkeys[0]), mapResponse(sexstate,catkeys[1])))
  for k in sorted(dataDictionary[categvar].keys()):
    v = dataDictionary[categvar][k]
    print ('{:>10s} {:10.2f}% {:10.2f}%'.format(v, round(100*toprint[catkeys[0]].get(k, 0)/sum(toprint[catkeys[0]].values()), 2), 
      round(100*toprint[catkeys[1]].get(k, 0)/sum(toprint[catkeys[1]].values()), 2)))
  
# For continuous variables in the dataset: poorhealth, sleptim1, avedrnk2
# Create min, max, mean, mode, and median for a single variable - 
# calculations for mode, median, and mean are in separate functions called in this function
def univariate (data, var):
  mean = createaverage(data, var)
  mode = createmode(data, var)
  valueslist = extractvalues (data, var)
  medianvalue = createmedian(valueslist)
  minvars = min(valueslist)
  maxvars = max(valueslist)
  result = {'average': mean, 'min': minvars, 'max': maxvars, 'mode': mode, 'median': medianvalue}
  return result
  
# Continuous variables in the dataset: poorhealth, sleptim1, avedrnk2
# Remove the missing, don't know, and refused responses
def univbyvar2 (data, var1, var2):
  ''' Create min, max, mean, mode, and median for continous variables by state or sex and store in a dictionary of dictionaries'''
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

def extractvalues (data, var):
  ''' create a list of all values for a particular variable (var) in data
      the list is used to find min, max, and median of variables'''
  valueslist = []
  for row in data:
    mapped = mapResponse(var, row[var])
    if mapped != 'refused' and mapped != "don't know" and mapped != 'missing' and row[var] != '':
      vars = int(row[var]) 
      valueslist.append(vars)
  return valueslist

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
        keymode = [k] # creates a new list with just k in it, k is the value with the most occurrences in the dataset, i.e., mode
      elif v == mode: # to accomodate condition that there are multiple modes in the list of values
        keymode.append(k)
  return keymode
  
def printcateg (data, catvar):
  ''' Nice printout of a single categorical variable'''
  print (catvar, varQuestion[catvar])
  thingtoprint = distribution(data, catvar)
  table (thingtoprint)
  print ()
  histogram (thingtoprint)
  print()

def printcontinuous (data, contvar):
  ''' Nice printout of a single continuous variable'''
  toprint = univariate(data, contvar)
  sep = ', '
  modeStrings = [] # accomodating the possibility of more than one mode in a distribution
  for v in toprint['mode']: # for each item in the list of integers representing modes, this loop turns each item into a string, so .join works
    modeStrings.append(str(v))
  print (contvar, varQuestion[contvar])
  print ('Minimum = ', toprint['min'])
  print ('Maximum = ', toprint['max'])
  print ('Mean    = ', toprint['average'])
  print ('Median  = ', toprint['median'])
  print ('Mode    = ', sep.join(modeStrings))

def printcontbysexstate (data, categvar, contvar):
  ''' Nice printout of a continuous variable by sex or state, which have only 2 levels/responses each'''
  toprint= univbyvar2(data, categvar, contvar)
  catkeys = list(toprint.keys())
  if len(catkeys) != 2:
    print ("hm, there are more than two category one choices, we aren't set up for this") # program is not set up for looking at a byvariable with more than 2 response values
    return
  print (contvar, varQuestion[contvar])
  # .format information obtained from http://www.python-course.eu/python3_formatted_output.php and https://pyformat.info
  # .format used so output would line up nicely 
  print ('          {:>10s} {:>10s}'.format(mapResponse(categvar,catkeys[0]), mapResponse(categvar,catkeys[1])))
  print ('Minimum = {:10.2f} {:10.2f}'.format(toprint[catkeys[0]]['min'], toprint[catkeys[1]]['min']))
  print ('Maximum = {:10.2f} {:10.2f}'.format(toprint[catkeys[0]]['max'], toprint[catkeys[1]]['max']))
  print ('Mean    = {:10.2f} {:10.2f}'.format(toprint[catkeys[0]]['average'], toprint[catkeys[1]]['average']))
  print ('Median  = {:10.2f} {:10.2f}'.format(toprint[catkeys[0]]['median'],toprint[catkeys[1]]['median']))
  print ('Mode    = {:>10s} {:>10s}'.format(modelisttostring(toprint[catkeys[0]]['mode']), modelisttostring(toprint[catkeys[1]]['mode'])))
  print ()

def modelisttostring (modevalues):
  ''' Convert list of modes to a string for printing'''
  sep = ', '
  modeStrings = []
  for v in modevalues: # for each item in the list of integers representing modes, this loop turns each item into a string, so .join works
    modeStrings.append(str(v))
  return sep.join(modeStrings)


