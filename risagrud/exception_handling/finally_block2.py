# there is only one situation , where the finally block won't work.
# If we close the execution of Python Virtual Machine. Before going to execution into the
# finally block. by using (os._exit(0)). The example is given below.....


'''Whenever we are using os._exit(0) function then Python Virtual Machine
 itself will be shutdown.In this particular case finally won't be executed. '''



import os
try:
    print('try block')
    os._exit(0)
except:
    print('except block')
finally:
    print('finally block')