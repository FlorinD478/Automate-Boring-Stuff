import random
ran = random.randint(1,20)
print("Ma gandesc la un numar de la 1 la 20")
for guess in range(1,15):
    print('Ghiceste:')
    inputGuess= int(input())
    if inputGuess == ran:
        break
    elif inputGuess > ran:
        print('Numarul tau este prea mare')
    else:
        print('Numarul tau este prea mic')
print('Bravo! Mi-ai ghicit numarul din '+ str(guess) +' incercari!')
