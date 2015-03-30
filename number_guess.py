__author__ = 'fardin'
from random import randint

while True:
    a = randint(1, 100)
    try:
        while True:
            x = int(raw_input('Enter a number from 1 to 100: '))
            if x == a:
                print 'You win!'
                break
            elif x > a:
                print 'Try a smaller number!'
            elif x < a:
                print 'Try a bigger number!'
            if x>100:
                print 'Your number is too big!'
    except ValueError:
        print 'Enter a number!'
