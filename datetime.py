#!/usr/bin/env python

# A simple programs which "tells" current date and time
# Written in Python2

from datetime import datetime
now=datetime.now()

print 'Today is: %s/%s/%s' %(now.day, now.month, now.year)
print 'Current time is: %s:%s:%s' %(now.hour, now.minute, now.second)
