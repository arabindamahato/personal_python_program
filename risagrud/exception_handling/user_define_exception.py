
'''Every exception is a class  '''

class TooOldException(Exception):
    def __init__(self, msg):
        self.msg = msg

class TooYoungException(Exception):
    def __init__(self, msg):
        self.msg = msg

age = int(input('Enter your age :'))
if age < 18:
    raise TooYoungException('Sorry Your age is too short wait for having age 18 .. you cant register.')
elif age > 80:
    raise TooOldException('Sorry Your age is too much.. you cant register.')
else:
    print('Thanks for register. we will give you matched details..')