#! /usr/bin/python3
import csv
from dataDictionary import *
from funct import *
from interface import *

print (''' 
Welcome to the fabulous world of health data.
You can use this program to review results of the Behavioral Risk Factor Surveillance Survey. 
You will be able to review results of the survey for Connecticut and North Carolina for the following topics:  
General health, Exercise, Sleep, Tobacco, and Alcohol. 

Data from the 2013 and 2014 surveys are provided or you can upload your own data file. (more about this below)

The system is driven by menus, so you will always be prompted to select an item from a numbered list.
First, you will select the year of data that you are interested in, 
then the health topic of interest. Then, you will have the option of seeing the variables for that health topic
reported by state and sex.

Please access the "help" screen for additional information about bringing your own data. ''')


mainmenu()


