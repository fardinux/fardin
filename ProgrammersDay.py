# !/usr/bin/env/ python

__author__ = "66 61 72 64 69 6e 75 78" 

from datetime import datetime
import calendar

thisYear = datetime.now().year
thisMonth = datetime.now().month
today = datetime.now().day
leap = calendar.isleap(thisYear)

def message():
    print("Happy International Programmers' Day! :)\
  	\nDate:", today ,"/", thisMonth,"/", thisYear)
    
if leap == False and thisMonth == 9 and today == 13:
    message()

elif leap == True and thisMonth == 9 and today == 12:
    message()
    
else:
    print("It isn't International Programmers' Day :(")
    
