class Person:
    def __init__(self):
        self.name='Arvind'
        self.dob=self.DOB()
    class DOB:
        def __init__(self):
            self.dd=15
            self.mm=12
            self.yyyy=1995

        def display(self):
            print('DOB={}/{}/{}'.format(self.dd,self.mm,self.yyyy))

oa=Person()
oa.DOB().display()



