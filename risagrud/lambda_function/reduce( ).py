
from functools import *
list  = [1,2,3,4,5,6,7,8,9,10]
x = reduce(lambda x,y : x*y, list)
print(x)