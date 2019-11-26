''' example of has-a relationship'''

class A:
    def m1(self):
        print('def m1')

class B(A):
    oa=A() #object created in child class
    def m2(self):
        print('def m2')

ob=B() # creating object for object B
ob.m2()
ob.oa.m1() # calling m1() function from object A inside object B
