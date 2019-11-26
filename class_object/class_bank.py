class Bank:
    bank_name    = 'Bank of Boroda'
    manager_name = 'Arabinda'
    ifsc_code    = 'BARBAMUND'
    def __init__(self, name, age, ph_no, mail):
        self.name = name
        self.age = age
        self.ph_no = ph_no
        self.mail = mail
        print('Bank Name :', Bank.bank_name)
        print('Manager Name :', Bank.manager_name)
        print('IFSC Code :', Bank.ifsc_code)

    def info(self):
        print('Customer Name :',self.name)
        print('age is :',self.age)
        print('Contact is :',self.ph_no)
        print('Email is :',self.mail)

s1=Bank('Arabinda', 23, 1234657895, 'abc@gmail.com')
s1.info()

s2=Bank('Rohit', 24, 1234655495, 'rohit@gmail.com')
s2.info()

s2=Bank('Avinash', 20, 894568745, 'avinash@gmail.com')
s2.info()

s2=Bank('Ramesh', 21, 9934655495, 'ramesh@gmail.com')
s2.info()

s2=Bank('Suresh', 22, 9901655495, 'suresh@gmail.com')
s2.info()
















