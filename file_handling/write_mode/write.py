# def write():
#     f = open('abc.txt','w')
#     data = 'I want to be a good software engineer'
#     f.write(data)
#     print('write successfully')
#     f.close()
# write()


def writelines():
    f = open('abc.txt','w')
    data = 'I want to be a good software engineer'
    f.writelines(data)
    print('write successfully')
    f.close()
writelines()

