fibo1 = 0
fibo2 = 1
fibo = int(input('Enter any number :'))
original_no=fibo
if fibo == 1:
    print(fibo1)
elif fibo == 2:
    print(fibo2)
else:
    for i in range(3,fibo+1):
        fibo = fibo1 + fibo2
        fibo1=fibo2
        fibo2=fibo
    print('The fibonacci number of {} is {}'.format(original_no,fibo))
