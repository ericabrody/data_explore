from funct import *

def mainmenu():
  ''' Function that drives the user interface - first stage of user selection to start seeing data 
      user chooses data set of interest''' #syntax of options code borrowed from E. Hauser, class notes April 14, 2016
  options = """ 
Please select a dataset of interest:
  1 - 2013
  2 - 2014
  3 - your own data
  4 - help
  5 - quit"""
  going = True
  while going:
    print(options)
    choice = input("What year of data are you interested in? ")
    if choice == '1':
      rows = loaddata('smallbr2013.csv')
      choosetopic(rows)
    elif choice == '2':
      rows = loaddata('smallbr2014.csv')
      choosetopic(rows)
    elif choice == "3":
      bringyourown() # function that allows user to choose a dataset that they have loaded into Cloud 9
    elif choice == "4":
      helpscreen()
    elif choice == '5':
      quit()
    else: 
      print ('Please choose a number between 1 and 5')

def choosetopic(data):
  ''' User interface: stage two - selecting topic of interest
      user will see the univariate statistics for continuous variables in each topic
      and a frequency table and histogram for categorical variables in each topic'''
  options = '''
Please select a topic of interest:
  1 - General health
  2 - Exercise
  3 - Sleep
  4 - Tobacco
  5 - Alcohol 
  6 - Change dataset
  7 - help
  8 - quit '''
  going = True
  while going:
    print(options)
    choice = input ('What topic are you interested in? ')
    if choice == '1':
      printcateg (data, 'GENHLTH')
      printcontinuous (data, 'POORHLTH')
      nextstep = 'general health'
      bysexstate(data, nextstep)
      choosetopic(data)
    elif choice == '2':
      printcateg (data, 'EXERANY2')
      nextstep = 'exercise'
      bysexstate(data, nextstep)
      choosetopic(data)
    elif choice == '3':
      printcontinuous (data,'SLEPTIM1')
      nextstep = 'sleep'
      bysexstate(data, nextstep)
      choosetopic(data)
    elif choice == '4':
      printcateg (data, 'SMOKE100')
      printcateg (data, 'SMOKDAY2')
      nextstep = 'tobacco'
      bysexstate(data, nextstep)
      choosetopic(data)
    elif choice == '5':
      printcontinuous (data, 'AVEDRNK2')
      printcontinuous (data, 'MAXDRNKS')
      nextstep = 'alcohol'
      bysexstate(data, nextstep)
      choosetopic(data)
    elif choice == '6':
      mainmenu()
    elif choice == '7':
      helpscreen()
      return
    elif choice == '8':
      quit()
    else: 
      print ('Please choose a number between 1 and 8 ')
      
def bysexstate (data, nextstep):
  print ('''
Now you can see the survey results for these variables for sex (M/F) and state (CT/NC) ''')
  options = '''
  1 - Yes
  2 - No, I would like to select another topic
  3 - No, I would like to select another dataset
  4 - help
  5 - quit'''
  going = True
  while going:
    print(options)
    choice = input ('Would you like to see these variables by sex and state? ')
    if choice == '1' and nextstep == 'general health':
      printcategbysexstate (data, '_STATE', 'GENHLTH')
      printcategbysexstate (data, 'SEX', 'GENHLTH')
      printcontbysexstate (data, '_STATE', 'POORHLTH')
      printcontbysexstate (data, 'SEX', 'POORHLTH')
      barcategbystate (data, '_STATE', 'GENHLTH')
      barcategbystate (data, 'SEX', 'GENHLTH')
      going = False
    elif choice == '1' and nextstep == 'exercise':
      printcategbysexstate (data, '_STATE', 'EXERANY2')
      printcategbysexstate (data, 'SEX', 'EXERANY2')
      barcategbystate (data,'_STATE', 'EXERANY2')
      barcategbystate (data, 'SEX', 'EXERANY2')
      going = False
    elif choice == '1' and nextstep == 'sleep':
      printcontbysexstate (data, '_STATE', 'SLEPTIM1')
      printcontbysexstate (data, 'SEX', 'SLEPTIM1')
      going = False
    elif choice == '1' and nextstep == 'tobacco':
      printcategbysexstate (data, '_STATE', 'SMOKE100')
      printcategbysexstate (data, 'SEX', 'SMOKE100')
      printcategbysexstate (data, '_STATE', 'SMOKDAY2')
      printcategbysexstate (data, 'SEX', 'SMOKDAY2')
      barcategbystate (data, '_STATE', 'SMOKE100')
      barcategbystate (data, 'SEX', 'SMOKE100')
      barcategbystate (data, '_STATE', 'SMOKDAY2')
      barcategbystate (data, 'SEX', 'SMOKDAY2')
      going = False
    elif choice == '1' and nextstep == 'alcohol':
      printcontbysexstate (data, '_STATE', 'AVEDRNK2')
      printcontbysexstate (data, 'SEX', 'AVEDRNK2')
      printcontbysexstate (data, '_STATE', 'MAXDRNKS')
      printcontbysexstate (data, 'SEX', 'MAXDRNKS')
      going = False
    elif choice == '2':
      choosetopic(data)
      going = False
    elif choice == '3':
      mainmenu()
      going = False
    elif choice == '4':
      helpscreen()
    elif choice == '5':
      quit()
    else:
      print ('Please choose a number between 1 and 5')


def bringyourown():
  ''' functionality for users bringing their own data '''
  print ('''Instructions: )
  The data will need to be in a .csv file, in comma-separated format. 
  Variable names and response values are as follows:
  ''')
  print()
  displaydatadict()
  datafile = input('What is the name of your file?')
  print ("Please type the filename carefully in this format 'myfile.csv'")
  rows = loaddata(datafile) 
  if len(rows) == 0:
    mainmenu()
  else: 
    choosetopic(rows)

def displaydatadict():
  print ('Categorical variables')
  for item in categoricalVars:
    print ('\t', item)
    print ('\t\t', 'Value', '\t', 'Value Label')
    for k,v in dataDictionary[item].items():
      print ('\t\t', k, '\t', v)
  print ()
  print ('Continuous variables ')
  for item in continuousVars:
    print ('\t', item)
    print ('\t\t', 'Value', '\t', 'Value Label')
    for k,v in dataDictionary[item].items():
      print ('\t\t', k, '\t', v)
      
def helpscreen():
  print ('''
  To examine data using this program, you will be asked a series of questions 
  to let us know which data you would like to see in the following order:
  1 - Choose a dataset (each dataset represents a different year of data)
  2 - Choose a topic of interest (each topic has 1 to 3 variables)
   --> This will show you univariate statistics for continuous variables and, for 
       for categorical variables - a frequency table and histogram will be shown.
  3 - Then indicate if you would like to see the variables in this topic by sex 
      and state or if you would like to pick a new topic or a new dataset.
  
  If you brought your own data:
  The data  need to be in a .csv file, in comma-separated format. 
  Acceptable variable names and response values are shown below.
  Data analysis results will be shown with the value labels also listed below.
  ''')
  displaydatadict()
