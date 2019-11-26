def decor(arg):
    def inner(a,b):
        print('#'*30)
        print('The sum is :',end='')
        arg(10, 20) #this arg() function is alias name of add method. when add() function goes to the argument of decor() then it is replace by arg() function
        print('#'*30)

    return inner



@decor # if the @decor is activate then add() will not be executed, inner() will executed
#'''Here add execute first. it goes to the decor(arg) and replace with arg as alias name, means it holds only the obj address'''
def add(a,b):
    print(a+b)

add(10,20)

