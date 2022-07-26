import random
ran = random.randint(1,20)
print("Ma gandesc la un numar de la 1 la 20")
imp = 0
a = 0
while a <= 10:
    print('Ghiceste:')
    imp = int(input())
    a=a+1
    if ran < imp:
        print("Numarul tau este prea mare")
    elif ran > imp:
        print('Numarul tau este prea mic')
    else:
        break
if a == 11:
    print('Ai consumat toate incercarile. Numarul meu era ' + str(ran))
else:
    print('Bravo! Mi-a ghicit numarul din '+ str(a)+' incercari!')
