f = None
try:
    f = open('abc.txt','r')
except:
    print('some problem to getting file')
else:
    print('file read successfully')
    print('#' * 30)
    print(f.read())
    print('#' * 30)

finally:
    if f is not None:
        f.close()


