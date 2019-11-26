# class A:
#     a=10
#     b=20
# x=A()
# print(x.a)
#-------------------------------

# class B:
#     a=10
#     b=20
# x1=B()
# print(x1.a)
# x2=B()
# print(x2.b)
#---------------------------------

# class B:
#     a=10
#     b=20
#     def __init__(self,b):
#         self.b=b
# x=B(50)
# print(x.b)

#------------------------------------------------------------------------------
#
# class Bank:
#     bank_name = 'BOB'
#     manager_name = 'Ramesh'
#     def __init__(self, cname, caddress, cph_no):
#         self.cname = cname
#         self.caddress = caddress
#         self.cph_no = cph_no
#     def display(self):
#         print('Customer name',self.cname)
#         print('Customer address',self.caddress)
#         print('Customer phone no',self.cph_no)
#
# # Object creation
# o1 = Bank('Arabinda', 'Manpur', 7602125658)
# print(Bank.bank_name)
# print(Bank.manager_name)
# print(o1.cname)
# print(o1.caddress)
# print(o1.cph_no)
# Bank.display(o1)
#
# print(Bank.bank_name, Bank.manager_name)
# print(Bank.bank_name, Bank.manager_name, o1.cname, o1.cph_no, o1.caddress)


#---------------------------------------------------------------------------------

# class A:
#     a=10
#     b=20
#     def __init__(self):
#         print('init is invoked')
#         print('Address of self is :', self)
# oa=A()
# print('Address of oa is :',oa)
# print('Address of A() is :',A())
# oa1=A()
# print('Address of oa1 is :',oa1)

#--------------------------------------------------------------------------------

# class Bank:
#     bank_name = 'sbi'
#     manager_name = 'rama'
#     ifsc = 'sbi486512'
#     def __init__(self, name, age, ph_no, adhar_no):
#         self.name = name
#         self.age = age
#         self.ph_no = ph_no
#         self.adhar_no = adhar_no
#     def abc(self):
#         print(self.name)
#         print(self.age)
#         print(self.ph_no)
#         print(self.adhar_no)
#     def def1(self):
#         print(self.name)
#         print(self.age)
#         print(self.ph_no)
#         print(self.adhar_no)
# oa = Bank('abm', '21','1234567890', '12345678' )
# #print(Bank.bank_name)
# #print(Bank.abc(oa))
# print(Bank.def1(oa))

#---------------------------------------------------------------



class A:
    a=10
    b=20
    def __init__(self, name):
        self.name = name
    def abc(self):
        print('My name is :', self.name)
oa = A('Arvind')
#print(oa.abc())
#A.abc('a','n')
oa.abc()










