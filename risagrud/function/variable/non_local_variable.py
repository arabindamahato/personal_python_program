def father():
    f_name = 'chunaram'
    c_name = 'pintu'
    c_name2 = 'sintu'
    print('I am the father of {} and {}'.format(c_name,c_name2))
    def child():
        c_name  = 'ramesh' # this is non local variable
        a_name2 = 'arabinda' # this is the non local variable
        print('these two are the son of ',f_name)
    child()
father()

