# The speciality of finally block is
# it will be executed always whether exception raised or not raised
# and whether exception handled or not handled.

#1
# try:
#     print('Risky Code')
# except:
#     print('Handling Code')
# finally:
#     print('Cleanup code')


#2

try:
    print(10/0)
    print('try block')
except:
    print('except block')
finally:
    print('finally block')


