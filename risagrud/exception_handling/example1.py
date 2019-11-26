# print('Arabinda Loves Python')
# print(10/0) #Risky code
# print('he is ediot')

'''For resolve the above problem, we must use exception handling'''

#Same code with exception handling

print('Arabinda Loves Python')
try:
    print(10/0) #Risky code
except ZeroDivisionError:
    print(10/2)
print('he is ediot')