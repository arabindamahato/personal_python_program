class Juice:
    def __init__(self, juice_name, juice_quantity, juice_color):
        self.juice_name     = juice_name
        self.juice_quantity = juice_quantity
        self.juice_color    = juice_color

#Creating object j
j = Juice('Mango_Juice', '1 liter', 'Yellow')
print(j.juice_name)
print(j.juice_quantity)

#Creating 2nd object j2
j2 = Juice('Apple_Juice', '2 liter', 'red')
print(j2.juice_name)
