try:
    print('try block')
    print(10/'ten')
except ZeroDivisionError:
    print('zero division error')
except:
    print('default except block')
