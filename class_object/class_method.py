# Modify the manager name and address using @classmethod

class Bank:
    bank_name    = 'Bank of Boroda'
    ifsc_code    = 'BARBAMUND'

    def __init__(self, name, age, ph_no, manager_name):
        self.name = name
        self.age = age
        self.ph_no = ph_no
        self.manager_name = manager_name

    def disp(self):
        print('Bank Name :', self.bank_name)
        print('IFSC Code :', self.ifsc_code)
        print('Customer name :', self.name)
        print('Customer age :', self.age)
        print('Customer Ph_no :', self.ph_no)
        print('Customer Ph_no :', self.manager_name)
        print('------------------------------')

    @classmethod:
    def modify(cls, manager):








