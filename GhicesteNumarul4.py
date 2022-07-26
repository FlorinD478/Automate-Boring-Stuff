import random
ran = random.randint(1,20)
print("Ma gandesc la un numar de la 1 la 20")
imp = 0
a = 0
while True:
    print('Ghiceste:')
    try:
        imp = int(input())
    except ValueError:
        print('Ala nu e un numar! Ti-ai irosit o incercare degeaba')
        a=a+1
        continue
    a = a + 1
    if ran < imp:
        print("Numarul tau este prea mare")
    elif ran > imp:
        print('Numarul tau este prea mic')
    else:
        break

print('Bravo! Mi-a ghicit numarul din '+ str(a)+' incercari!')
