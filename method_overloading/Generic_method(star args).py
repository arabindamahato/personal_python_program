#generic method
'''method(*args)'''

print('-'*50, 'method(*args)')

def m1(*args):
    print(args)
    print(*args)
    print(type(args))


m1('I', 'love', 'Python')

print('-'*50)

m1(10,20,30,40,50,60,70,80,90)

print('-'*50)

m1([10, 20], [30, 40])

print('-'*50, 'Packing')


'''Packing'''

def m1(*args):
    print(*args)
    print(args)
    print(type(args))
def packing():
    a,b,c,d=10,20,30,40
    m1(a,b,c,d)
packing()





