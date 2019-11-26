''' In default argument the function contain already a arguments. if we give any veriable
at the time of function calling then it takes explicitely . If we dont give any arguments then
the function receives the default arguments'''

'''Sometimes we can provide default values for our positional arguments. '''

def wish(name='Guest'):
    print('hello {}'.format(name))
    print('hello {}'.format(name))
wish('Arabinda')

''' This below code is not right because 
" After default arguments we should not take non default arguments"'''

# def wish(name='Guest', ph_no):
#     print('hello {} {}'.format(name, ph_no))
#     print('hello {} {}'.format(name, ph_no))
# wish('Arabinda','ph_no')