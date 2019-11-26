


a=81
flag=0

for i in range(1,a):
    if i*i == a:
        flag=1
        break
if flag==1:
    print('perfect square')
else:
    print('not a perfect square')