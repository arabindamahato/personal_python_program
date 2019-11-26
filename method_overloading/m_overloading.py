'''example'''
# def m1(a,b):
#     return a+b
# print(m1([10,20],[30,40,50]))

'''Questions :- How to have variable numbers of arguments in a method'''
'''Answer :- We can have variable numbers of method in two eays -----
            1. By assigning the default value to the arguments
            2. Using generic methods (*args, **keyword args) '''

'''Variable number of arguments'''

'''For number value'''
def add(a,b,c=0,d=0,e=0):
    return a+b+c+d+e
#if you give 2 or 3 or 4 or 5 argumets then it easily works
# you must have to give minimum 2 arguments
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))
print(add(10,20,30,40,50))


print('-'*50)

'''For string value'''
def add1(a,b,c='',d='',e='',f=''):
    return a+b+c+d+e+f
print(add1('A','r','v','i','n','d'))
print(add1('A','r','v','i','n'))

print('-'*50)

'''For tuple value'''
def add3(a,b,c=(),d=(),e=()):
    return a+b+c+d+e
print(add3((1,2),(3,4),(5,6),(7,8),(9,10)))
print(add3((1,2),(3,4),(5,6),(7,8)))
print(add3((1,2),(3,4),(5,6)))
print(add3((1,2),(3,4)))

print('-'*50)

'''For list value'''
def add3(a, b, c=[], d=[], e=[]):
    return a+b+c+d+e
print(add3([1, 2], [3, 4], [5, 6], [7, 8], [9, 10]))
print(add3([1, 2], [3, 4], [5, 6], [7, 8]))
print(add3([1, 2], [3, 4], [5, 6]))
print(add3([1, 2], [3, 4]))


print('-'*50, 'For generic value')


'''For generic value / Arguments'''


#def addGenericValue(a,b,c=None,d=None,e=None):
def addGenericValue(a=None, b=None, c=None, d=None, e=None):
    return a+b+c+d+e
print(addGenericValue(10, 20, 30, 40, 50), )
print(addGenericValue('R', 'a', 'm', 'e', 's'))
print(addGenericValue((1, 2), (3, 4), (5, 6), (7, 8), (9, 10)))
print(addGenericValue([1, 2], [3, 4], [5, 6], [7, 8], [9, 10]))
