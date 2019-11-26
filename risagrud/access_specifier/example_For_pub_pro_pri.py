class Laptop:
    laptop_color = 'black'
    laptop_brand = 'HP'
    def __init__(self, keyboard, screen, pwd):
        self.laptop_keyboard = keyboard
        self._laptop_screen = screen
        self.__laptop_password = pwd


    def display(self):
        print(self.laptop_keyboard)
        print(self._laptop_screen)
        print(self.__laptop_password)




oa = Laptop('hp keyboard', 'lcd screen', '12345')
oa.display()
print(oa.laptop_keyboard, oa._laptop_screen, oa.__laptop_password)

