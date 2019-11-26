# multiple except block.
# Flow :- It works top to bottom until matched except identified
try:
    a=int(input('Enter any number :'))
    b=int(input('Enter any number :'))
    print(a/b)
except ZeroDivisionError:
    print('You cannot devide  by zero')

except ValueError:
    print('Please provide int value')

