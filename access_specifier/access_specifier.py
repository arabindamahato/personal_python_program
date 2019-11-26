class A:
    def __init__(self, screen,battery,processor):
        self.screen=screen
        self._battery=battery
        self.__processor=processor
    def disp(self):
        print('',self.screen)
        print('',self._battery)
        print('',self.__processor)

oa=A(5.5,'Leon','i3 processor')
oa.disp()
print('-'*15)
print(oa._A__processor)
print(oa._battery)
print(oa.screen)





