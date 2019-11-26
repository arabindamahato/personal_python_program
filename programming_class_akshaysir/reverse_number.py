#To reverse the given no and print it

print('To reverse the given no')
n=(input('Enter your no : '))
o=n[::-1]
p=int(o)
print('After reversing {} is {}'.format(n,p))


'''another method'''

# n=int(input('Enter any number :'))
# rev=0
# while n!=0:
#     ld=n%10
#     n=n//10
#     rev=rev*10+ld
# print(rev)
