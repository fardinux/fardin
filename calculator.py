#!/usr/bin/env python
__author__ = 'fardin'

"""A very basic calculator program with \
 addition, subtraction, multiplication, division and modulo operations written in python 2."""

while True:
    option = int(raw_input(
        'Welcome to calculator program.\n1)Add\n2)Subtract\n3)Multiply\n4)Divide\n5)Modulo\nChoose\
         one of the options above: '))  # menu
    num1 = float(raw_input('Enter first number: '))  # first number
    num2 = float(raw_input('Enter second number: '))  # second number
    if option == 1:
        print num1, '+', num2, '=', num1 + num2  # addition
    elif option == 2:
        print num1, '-', num2, '=', num1 - num2  # subtraction
    elif option == 3:
        print num1, '*', num2, '=', num1 * num2  # multiplication
    elif option == 4:
        print num1, '/', num2, '=', num1 / num2  # division
    elif option == 5:
        print num1, '%', num2, '=', num1 % num2  # modulo
    else:
        print 'Invalid input' 
