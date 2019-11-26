class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def talk(self):
        print('My name is:', self.name)
        print('My rollno is:', self.rollno)
        print('my marks is:', self.marks)
s=Student('RAMESH', 12, 95)
print(s.name)
print(s.rollno)
s.talk()
Student.talk(s)












