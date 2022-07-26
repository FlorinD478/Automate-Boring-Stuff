for i in range(4):
    print(i)
for i in [0,1,2,3]:
    print(i)
    
suplies = ['pens', 'rockets', 'M4-A1', 'AK-47','MP5']
for i in range(len(suplies)):
    print('La indexul ' + str(i) + ' avem in suplies: ' + suplies[i])

myPets = ['Richal', 'Savana', 'LeRoy', 'Ricardo']
name = input()
if name not in myPets:  # pur si simplu schimba blocurile  if si else intre ele;cred ca poate fi folositor cand ai elif
    print('Nu am o pisica cu numele asta')
else:
    print('Asta este pisica mea')
