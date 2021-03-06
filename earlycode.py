# code used to develop other code

######
#### CODE for twovar using two variables before created function
# result = {}
# for row in data['smallbr2014.csv']:
#   state=row['_STATE']
#   smokever=row['SMOKE100']
#   if state not in result: # create a dictionary for state, the first time a row has a state that hasn't been seen yet in the for loop
#     result[state] = {}
#   if smokever not in result[state]: # once you have dict for state, add response values to it 
#     result[state][smokever] = 1 # if response value new, i.e., new key in the state dict, then the value for that key is 1, after that the value for the key is x + 1
#   else: 
#     result[state][smokever] += 1

#########
###CODE For univariate statistics with one variable 


# Continuous variables in the dataset: poorhealth, sleptim1, smokday2, alcday5, maxdrnk5
# univariate stats for poorhealth
#  need to remove the missing responses
# totalbaddays = 0
# countbaddays = 0
# minbaddays = 500 
# maxbaddays = 0 
# for row in data['smallbr2014.csv']:
#   baddays = row['POORHLTH']
#   if baddays != '77' and baddays != '88' and baddays != '99' and baddays != '':
#     baddays = int(baddays) 
#     totalbaddays += baddays
#     countbaddays += 1
#     if baddays < minbaddays:
#       minbaddays = baddays
#     if baddays > maxbaddays:
#       maxbaddays = baddays
# avebaddays = round(totalbaddays/countbaddays, 2)
# #calculate mode
# premode = distribution(data['smallbr2014.csv'], 'POORHLTH')
# maxv = 0
# for k,v in premode.items():
#   if k != 'missing':
#     if v > maxv:
#       maxv = v
#       maxk = k
# modebaddays = maxk
# # calculate median
# medianlist = []
# for row in data['smallbr2014.csv']:
#   baddays = row['POORHLTH']
#   if baddays != '77' and baddays != '88' and baddays != '99' and baddays != '':
#     baddays = int(baddays) 
#     medianlist.append(baddays)
# medianbaddays = statistics.median(medianlist)

  
# print ('Totalbaddays: ', totalbaddays, 'Count: ', countbaddays, 'Average baddays: ', avebaddays)
# print ('Min baddays: ', minbaddays, 'Max baddays: ', maxbaddays, 'Mode baddays: ', modebaddays)
# print ('Median baddays: ', medianbaddays)
# print (premode)

#### Initial code to print continuous variables in a nice format - which was turned into function called printcontinuous
# for variable in continousVars:
#   toprint = univariate(data['smallbr2014.csv'], variable)
#   sep = ', '
#   modeStrings = []
#   for v in toprint['mode']: # for each item in the list of integers representing modes, this loop turns each item into a string, so .join works
#     modeStrings.append(str(v))
#   print (variable, varQuestion[variable])
#   print ('Minimum = ', toprint['min'])
#   print ('Maximum = ', toprint['max'])
#   print ('Mean    = ', toprint['average'])
#   print ('Median  = ', toprint['median'])
#   print ('Mode    = ', sep.join(modeStrings))
#   print ()

#### Initial code to print categorical variables in a nice format - which was turned into function called printcateg
# for variable in categoricalVars:
#   print (variable, varQuestion[variable])
#   thingtoprint = distribution(data['smallbr2014.csv'], variable)
#   table (thingtoprint)
#   print ()
#   histogram (thingtoprint)
#   print()

### initial code to read in data
# read in the datafiles as dictionary of list of dictionaries
# datafiles = ['smallbr2013.csv','smallbr2014.csv']
# data = {}
# for file in datafiles:
#   with open(file) as f:
#     reader = csv.DictReader(f)
#     rows = []
#     for row in reader: # creates a list of dictionaries where each case/row is a dictionary with a key-value pair for each variable
#       rows.append(row)
#     data[file] =  rows # storing each file's list of rows in the dictionary called data, key of this dictionary is filename
#     # and the values of this dictionary are the list of dictionaries
#     print (file, reader.fieldnames) #fieldnames = property of dictreader
#     print (file)


### Code to test each function
# whichVar = 0
# try:
#   while whichVar != '':
#     whichVar = input('Which variable are you interested in?')
#     table(distribution(data['smallbr2014.csv'], whichVar))
#     histogram (distribution(data['smallbr2014.csv'], whichVar))
# except:
#   print ('Thank you for using this program.')

# # To view the variables names (i.e., keys)...from the first row, but could have been any row
# print (data['smallbr2014.csv'][4].keys())

# twovarfreq = twovar(data['smallbr2014.csv'], '_STATE', 'EXERANY2')
# print ('Two Var output: ', twovarfreq)

# for catevar in ('_STATE', 'SEX'):
#   for contvar in continousVars:
#     printcontbysexstate (data['smallbr2014.csv'], catevar, contvar)

#printcateg (data['smallbr2014.csv'], 'EXERANY2')
#printcategbysexstate (data['smallbr2014.csv'], '_STATE', 'GENHLTH')
# #printcontinuous (data['smallbr2014.csv'], 'MAXDRNKS')

# print (univbyvar2 (data['smallbr2014.csv'], '_STATE', 'POORHLTH'))