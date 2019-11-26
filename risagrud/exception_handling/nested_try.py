try:
    print(10 / 0)
    print('outer try block')
    try:
        print('inner try block')
    except ValueError:
        print('inner except block')
    finally:
        print('inner finaly block')
except:
    print('outer except block')
finally:
    print('outer finally block')


'''until the try block is execute the finally block won't be executed (above example)'''



