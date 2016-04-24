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