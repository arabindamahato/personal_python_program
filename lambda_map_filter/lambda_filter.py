# Lambda function is anonymas( no name ) function
#filter function always takes two arguments:
    # 1. function address
    # 2. collection (from which collection we want to filter)
# output will always "less or equal"  input collection


# Find even no from the list using lambda and filter function

# iseven = lambda a:a%2==0
# l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# y = filter(iseven, l)
# print(list(y))



# prime number using filter function

def isprime(n):
    if n == 1:
        return False
    for i in range(2,n):
         if n%i == 0:
             return False
    return True
primes = filter(isprime, range(1,100))
print(list(primes))

