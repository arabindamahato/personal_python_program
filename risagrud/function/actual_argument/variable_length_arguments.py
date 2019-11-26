
'''Sometimes we can pass variable number of arguments to our function,
 such type of arguments are called variable length arguments'''

'''We can call this function by passing any number of arguments including zero number.
 Internally all these values represented in the form of tuple. '''

# def var_len_arg(*a):
#     for i in a:
#         print(i)
# var_len_arg(10,20,30,40,50)

'''Note: We can declare key word variable length arguments also. '''
'''We can call this function by passing any number of keyword arguments.
 Internally these keyword arguments will be stored inside a dictionary. 
1'''
def var_len_arg(**a):
    for i,j in a.items():
        print(i,'=',j)
var_len_arg(a=10,b=20,c=30,d=40)
