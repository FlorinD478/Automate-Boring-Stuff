import random

def getAnswer(number):
    if number == 1:
        return 'You got lucky'
    elif number == 2:
        return 'Ha ha, try again!'
    elif number == 3:
        print(' Nu am castigat,dar mesajul asta se scrie de doua ori!') #se pare ca nu se printeaza de doua ori;apare totusi un None dupa printare. cel mai probabil s-a facut printarea in functie, dar functia nu a returnat nimic ce poate fi stored intr-p variabila!
        #explicatie la pagina 65 din automatin boring stuff
        # daca vrei sa stochezi in vreo variabila valoarea obtinuta dintr-o functie, foloseste in functie return valoare
# urmatoarele 3 se pot scrie si ca print(getAnswer(random.randint(1,3)))
r = random.randint(1,3) 
fortune = getAnswer(r)
print(fortune)

spam = print('HEllo')
spam == None

# ajuta sa printezi lucruri pe acelasi rand cu print-uri deferite!!!
print('Good', end=' ')
print('Morning')
#cand sunt scrise ca mai jos se pune automat un spatiu intre ele
print('cats', 'dogs', 'mouse')
#schimba separare defaut printr-un spatiu in separare cu slash sau ce valoare vrei tu
print('cats', 'dogs', 'mouse', sep='/')
print('cats', 'dogs', 'mouse', sep='3')

#!!! Local variabiles cannot be used in a global scope

def spam():
    eggs = 322143
spam()
#print(eggs) nu va merge deoarece nu ai definit o astfel de varibila global
print(spam()) # va da None deoarece nu ai returnat nimic cu functia

#!!! Local Scopes cannot use variabiles in other local scopes
def spam():
    eggs=99
    bacon()
    print(eggs)

def bacon():
    ham=101
    eggs=0

spam()
# ce avem mai sus va returna 99, pentru a printa 0 vom modifica in felulu urmator:
def spam():
    eggs = 99
    eggs = bacon()
    print(eggs)

def bacon():
    ham=101
    eggs=0
    return eggs

spam()

# Global variables can be read from a local scope

spam = 'Richy'

def combi(name):
    print(spam + name)

combi('Alicia')

# in programul urmator , din cauza ca eggs este definit inaite de apelarea functiei, functia va returna valoarea lui eggs
def spam():
 print(eggs)
eggs = 42
spam()
print(eggs)

# Local and global variables with the same name

def spam():
 eggs=33   
 print(eggs)
eggs = 42
spam()
print(eggs)
# funtia de mai sus va folosi eggs local nu cel global
