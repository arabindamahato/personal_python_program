
def decor(func):
    def inner(a,b):
        if b==0:
            print('hey ediot how can I devide by 0')
        else:
            func(a,b)
    return inner

@decor
def division(a,b):
    div=a/b
    print(div)
division(10,0)














































# def decor(func):
#         def inner(a):
#             l = ['Arabinda', 'Ramesh', 'Suresh']
#             print('#' * 35)
#             print('Congratulations {}'.format(l))
#             print('You are selected for our company with software engineer designation')
#             print('#' * 35)
#             func()
#
#         return inner
#
#
#
# @decor
# def job(name):
#     print('Congratulations {} you are selected for software engineer trainee'.format(name))
# job('Rohit')