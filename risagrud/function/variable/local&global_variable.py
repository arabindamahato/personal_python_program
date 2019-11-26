l = 'london' #this is global variable
def india():
    global b # global keyword , its make global variable from local variable
    b='bangaluru'  #this is local variable
    print('Now I live in ',l)
def england():

    print('yesterday i was in',b)
india()
england()
print(l) # this print ststement execute because  i am printing here the global variable.


print('*'*50)
'''IF Global variable and local variable have same name then ?? '''

a=10
def m1():

    a=77
    print(a)
    print(globals()['a'])
m1()