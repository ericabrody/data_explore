from funct import *

def mainmenu():
  ''' Function that drives the user interface - first stage of user selection to start seeing data 
      user chooses data set of interest'''
  options = """ #syntax of options code borrowed from E. Hauser, class notes April 14, 2016
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
      going = False
    else: 
      print ('Please choose a number between 1 and 5')

def choosetopic(data):
  ''' User interface: stage two - selecting topic of interest
      user will see the univariate statistics for continuous variables in each topic
      and a frequency table and histogram for categorical variables in each topic'''
  options = '''
  1 - General health
  2 - Exercise
  3 - Sleep
  4 - Tobacco
  5 - Alcohol 
  6 - Change dataset
  7 - help'''
  going = True
  while going:
    print(options)
    choice = input ('What topic are you interested in?')
    if choice == '1':
      printcateg (data, 'GENHLTH')
      printcontinuous (data, 'POORHLTH')
    elif choice == '2':
      printcateg (data, 'EXERANY2')
    elif choice == '3':
      printcontinuous (data,'SLEPTIM1')
    elif choice == '4':
      printcateg (data, 'SMOKE100')
      printcateg (data, 'SMOKDAY2')
    elif choice == '5':
      printcontinuous (data, 'AVEDRNK2')
      printcontinuous (data, 'MAXDRNKS')
    elif choice == '6':
      return
    else: 
      print ('Please choose a number between 1 and 7')
  

def bringyourown():
  ''' functionality for users bringing their own data '''
  print ('Instructions - need to load into Cloud 9 yourself')
  datafile = input('What is the name of your file?')
  rows = loaddata(datafile) 
  if len(rows) == 0:
    mainmenu()
  else: 
    choosetopic(rows)
  



