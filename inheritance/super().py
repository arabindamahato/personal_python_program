# class A:
#     a=10
#     def m1(self):
#         print('def m1')
# class B(A):
#     b=20
#     def m2(self):
#         print(' def m2')
#
# ob=B()
# super(B,ob).m2()

#----------------------------------------------

class A:
    a=10
    def __init__(self,a):
        self.a = a
        print(a)
        print('init in parent')
class B(A):
    b=20
    def __init__(self,a ,b):
        self.b=b
        print('init in child')
        #A.__init__(self,b)
        # super().__init__(b)
class C(B):
    c=30
    def __init__(self,a,b,c):
        self.c=c
        print('init in sub-child')
        #super().__init__(b,c)
        B.__init__(self,b,c)
oc=C(1,2,3)


print('-'*20)


class Parent:
    def f1(self):
        print('Money, Property, Land, Gold')
    def merry(self):
        print('Katrina')
class Child(Parent):
    def merry(self):
        print('Deepika')
        super().merry()

oa = Child()
oa.merry()

