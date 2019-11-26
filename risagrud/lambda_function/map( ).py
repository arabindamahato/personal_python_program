# if it takes 5 inputs then the output will be must be 5.
# if not match the list items then extra items will be ignored..
# all of others are are filter method..

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

list3 = list(map(lambda m,n:m*n,list1, list2))
print(list3)