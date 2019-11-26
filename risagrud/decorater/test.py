def decorater(args):
    def after_mackup():
        print('Bride looks beautyfull')
        print('bride is well decorated ')
        print('Bride is ready for marriage')
    return after_mackup

@decorater
def before_mackup():
    print('Bride looks like simple')
    print('bride is not well decorated ')
    print('Bride is not ready for marriage')
before_mackup()
