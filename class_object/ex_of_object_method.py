class Bank:
    bank_name    = 'Bank of Boroda'
    ifsc_code    = 'BARBAMUND'
    def __init__(self, name, age, ph_no):
        self.name = name
        self.age = age
        self.ph_no = ph_no

    def disp(self):
        print('Bank Name :', self.bank_name)
        print('IFSC Code :', self.ifsc_code)
        print('Customer name :', self.name)
        print('Customer age :', self.age)
        print('Customer Ph_no :', self.ph_no)
        print('------------------------------')

    def modify(self):
        choice = input('Enter the member/paremeter name to be modified : ')
        if choice == 'age':
            self.age = int(input('enter the age : '))
        elif choice == 'name':
            self.name = input('Enter the name : ')
        elif choice == 'ph_no':
            self.ph_no = int(input('enter the ph_no : '))
        else:
            self.name = input('Enter the name : ')
            self.age = int(input('enter the age : '))
            self.ph_no = int(input('enter the ph_no : '))

oa=Bank('arabinda', '25', 123456)
 #oa1=Bank('Ramesh', '21', 321654)
# #calling the object by using class name
# Bank.disp(oa)
# #calling the object by using object name/ object variable
# oa.disp()

#-------modify-------
oa.disp()
oa.modify()
oa.disp()