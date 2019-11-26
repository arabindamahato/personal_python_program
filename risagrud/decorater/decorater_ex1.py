
def decorater(any_arg): # any arg is used for display() function at the time of decoration / execution
    def inner(): #argument of inner() and display() function must be same because these both are override when decoration
        print('done with beautiful mackup')
        print('Looking so cute')
    return inner


@decorater # Decorater function name @decorater name must be same
def display():#argument of inner() and display() function must be same because these both are override when decoration
    print('showing it as it is')

display()