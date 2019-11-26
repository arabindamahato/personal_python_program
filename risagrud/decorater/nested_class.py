def outer():
    print('Outer function started')
    def inner():
        print('Inner function executed')
    return inner
    print('Outer function execution complete')
f1 = outer
f1()

print('*'*30)

def m1(x):
    x()
    print('m1')
def m2():
    print('m2')
m1(m2)




