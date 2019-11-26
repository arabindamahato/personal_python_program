# Doing filtering without filter() function

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
newlist = []
for i in list1:
    if is_even(i) == True:
        newlist.append(i)
print(newlist)
print('*'*50)

'''''''''''''''''''''''''''''''with filter function'''''''''''''''''''''''''

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def iseven2(n):
    if n % 2 == 0:
        return True
    else:
        return False
s = list(filter(iseven2, l)) #list() is use for type casting. because filter() returns only object
print(s)
print('*'*50)

'''''''''''''''''''''''with lambda function'''''''''''''''''''''''''''''

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = list(filter(lambda n : n % 2 ==0 , l))
print(y)



print('*'*50)
'''''''''''''''''''filter the number whuch are devisible by 3 and odd number'''''''''

list2 = [1,2,3,4,5,6,7,8,9,10]
divby3odd = list(filter(lambda x: x%3 ==0 and x%2 !=0 ,list2 ))
print(divby3odd)


print('*'*50)
'''''''''''''''''''filter the name whose 1st letter is k '''''''''''''

heroines = ['katrina', 'sunnyleone', 'kareena kaif', 'kajal', 'anushka sharma']
startwithk = list(filter(lambda name: name[0] == 'k', heroines))
print(startwithk)


print('*'*50)
'''''''''''''''''''filter the names whose length devisible by 5 '''''''''''''
heroines = ['katrina', 'sunnyleone', 'kareena kaif', 'kajal', 'anushka sharma']
names_divisible_by_5 = list(filter(lambda name:len(name)%5 == 0, heroines ))
print(names_divisible_by_5)


print('*'*50)
'''''''''''''''''''filter the names whose name length is odd '''''''''''''
heroines = ['katrina', 'sunnyleone', 'kareena kaif', 'kajal', 'anushka sharma']
names_length_odd = list(filter(lambda name:len(name)%2 != 0, heroines ))
print(names_length_odd)