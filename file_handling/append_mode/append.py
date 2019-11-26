#append is not a function it is mode...

def append():
    f = open('abc.txt','a')
    data = 'I want 10 lakh package'
    f.write(data)
    print('append  successfully')
    print(f.closed)
    f.close()
    print(f.closed)
append()