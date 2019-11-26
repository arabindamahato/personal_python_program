def decor(func):
    def inner(name):
        if name == 'Krishna':
            print('#'*30)
            print(name,'You are very important to me')
            print('Very Very Good Morning :', name)
            print('#' * 30)
        else:
            func(name) #this func() function is alias name of wish method. when wish() function goes to the argument of decor() then it is replace by func() function

    return inner



@decor # if the @decor is activate then add() will not be executed, inner() will executed
#'''Here wish() execute first. it goes to the decor() and replace with func as alies name, means it holds only the obj address'''
def wish(name):
    print('Good morning :',name)

# wish('Arabinda')
wish('Krishna')


