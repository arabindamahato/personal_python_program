#append is not a function it is mode...

def append():
    f = open('abc.txt','a')
    data = 'I want 10 lakh package'
    f.write(data)
    print('append  successfully')
    print('Is file closed :',f.closed)
    print('File is writable or not :',f.writable())
    f.close()
    print('Is file closed :',f.closed)
    print('The mode of file is :',f.mode)
    print('The name of file is :',f.name)
    print('File is readable or not :',f.readable())
   
append()