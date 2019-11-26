try:
    print('outer try block')
    print(10 / 0)
except:
    print('outer except block')
    try:
        print(10 / 0)
        print('inner try block')
    except:
        print('inner except block')
    finally:
        print('inner finaly block')
finally:
    print('outer finally block')