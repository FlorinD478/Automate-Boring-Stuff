import random

ran = random.randint(1,20)
print("Ma gandesc la un numar de la 1 la 20")
imp = 0
a = 0
while imp != ran:
    print('Ghiceste:')
    imp = int(input())
    a=a+1
    if ran < imp:
        print("Numarul tau este prea mare")
    elif ran > imp:
        print('Numarul tau este prea mic')

print('Bravo! Mi-a ghicit numarul din '+ str(a)+' incercari!')
    
# incearca sa faci unu =l in care sa folosesti functia continue
