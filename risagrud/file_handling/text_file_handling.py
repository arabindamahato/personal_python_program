'''
r mode
w mode
a mode
x exclusive mode
r+
w+
a+
name variable
mode variable
read()
read(n)
readline()
readlines()
'''

# open function is is use to open the given file
'''
f=open('abc.txt','r')
print(f.read()) # read function is use to read the data from given file
print(f.name) # name is not a function. its a variable. it is use to get given file name
print(f.mode) # mode is not a function. its a variable. it is use to know the file mode (eg:read, write,append etc)
f.close()
'''

'''if the file is available then only it works otherwise it throws exception'''

# f1 = open('abc.txt', 'w+')
# data = 'Arabinda\n'
# data1 = 'Mahato\n'
# data2 = 'Kolkata\n'
# f1.write(data)
# f1.write(data1)
# f1.write(data2)
# print('Data written successfully')
# text = f1.read()
# print(text)
# f1.close()

# '''only read purpose'''
# f2 = open('abc.txt','r')
# print(f2.read())
# f2.close()
#
# '''only read(n) purpose'''
# f2 = open('abc.txt','r')
# print(f2.read(12))
# f2.close()

# '''only read single line purpose'''
# # f2 = open('abc.txt','r')
# # print(f2.readline(),end="")
# # print(f2.readline())
# # f2.close()

''' read multiple lines purpose'''
f2 = open('abc.txt','r')
list = f2.readlines()
for i in list: #I used for loop because of geting one by one data instead of list format.
    print(i, end="")


f2.close()



'''exclusive mode'''

# file = open('abcd.txt','x')
# text = 'Hello this is exclusive mode'
# data = file.write(text)
# file.close()

'''w+ mode'''
