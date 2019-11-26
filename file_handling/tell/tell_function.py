#tell function : it tells the cursor position in the file
f = open('abc.txt','r')
position = f.tell()
print(position)
data = f.read(10)
print(data)
position = f.tell()
print(position)
f.close()





