class Bank:
    bank_name    = 'Bank of Boroda'
    ifsc_code    = 'BARBAMUND'
    def __init__(self, name, age, ph_no, atm = False):
        self.name = name
        self.age = age
        self.ph_no = ph_no
        self.atm = atm


    def atminfo(self):
        if self.atm == True:
            print('Atm already issued')
        else:
            self.atm == True:




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