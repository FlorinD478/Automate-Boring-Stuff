import math
name = input()
a = len(name) -1
for i in range(math.floor(len(name)/2)): #math.floor
    if name[i] != name[a]:        
        print('Numarul nu este')
        break
    a -= 1
print('PALINDROM')
