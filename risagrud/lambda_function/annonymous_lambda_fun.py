f = lambda x:x*x
for i in range(1,10+1):
    print('Square of {} is {}'.format(i,f(i)))


print('*'*50)
'''sum of two nos'''

s = lambda x,y:x+y
print(s(10,20))
print('the sum of x and y is',s(10,20))


print('*'*50)
'''Biggest of given numbers'''

g = lambda a,b,c:a if a>b and a>c  else b if  b>c else c
print('bigger is ',g(10,20,30))

