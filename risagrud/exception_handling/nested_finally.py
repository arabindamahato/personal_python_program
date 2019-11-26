try:
    print('outer try block')
except:
    print('outer except block')
finally:
    print('outer finally block')
    print(10 / 0)
    try:
        print('inner try block')
    except:
        print('inner except block')
    finally:
        print('inner finaly block')
