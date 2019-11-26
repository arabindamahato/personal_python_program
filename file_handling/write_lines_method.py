f=open('F:/abcde.txt', 'w')
# Writelines method accept string in the form of list
l=['Padmabati \n', 'Chunaram \n', 'Ramesh \n', 'Arabinda \n']
f.writelines(l)
f.close()
print('Written Successfully into the file')





#Explaination

# Writelines method also accept string in the form of tuple
#  t=('Padmabati \n', 'Chunaram \n', 'Ramesh \n', 'Arabinda \n')

# Writelines method also accept string in the form of set
# s={'Padmabati \n', 'Chunaram \n', 'Ramesh \n', 'Arabinda \n'}

# Writelines method also accept string in the form of dict but and only keys
# will be added and keys should be string type only otherwise we will get type
# error, Instead of keys if you want to add values then we have to write the
# code explicitely
# d=('P', 'Padmabati \n', 'C','Chunaram \n', 'R'Ramesh \n', 'A',Arabinda \n')
# f.writelines([d['P'],d['C'],d['R'],d['A']])    OR
# f.writelines(d.values())