# f = open('abc.txt','w')
# data = f.write('My aim is to be a good programmer')
# seek = f.seek(23)
# print(seek)
# data1 = f.write('engineer')
# print(data1)
# f.close()


# f = open('abc.txt','r')
# # data = f.write('My aim is to be a good programmer')
# seek = f.seek(23)
# # print(seek)
# # data1 = f.write('engineer')
# # print(data1)
# seekdata = f.read()
# print(seekdata)
# f.close()


f = open('abc.txt','w')
# data = f.write('My aim is to be a good programmer')
seek = f.seek(10)
# print(seek)
data1 = f.write('xxxxxxxxx')
print(data1)
# seekdata = f.write('ARABINDA')
# print(seekdata)
f.close()