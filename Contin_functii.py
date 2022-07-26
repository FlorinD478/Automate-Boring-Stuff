def spam():
    global eggs    #modifica variabila globala din functie!!! astfel rezultatul programului nu va fi global, va fi spam
    eggs ='spam' # this is glogal
def bacon():
    eggs = ' bacon' # this is local

def siesta():
    print(eggs) # this is global

eggs = 'global' # this is the global
spam()
print(eggs)
