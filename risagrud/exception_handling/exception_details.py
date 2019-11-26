print('Arabinda Loves Python')
try:
    a=int(input('Enter any number :'))
    b=int(input('Enter any number :'))
    print(a/b)
except Exception as msg: # 'Exception'? Remember the exception hirerchy
    print('Description of exception :',msg)
    print('Description of exception class :',msg.__class__)
    print('Description of exception name :',msg.__class__.__name__)
    print('Description of exception type :',type(msg))

print('he is ediot')