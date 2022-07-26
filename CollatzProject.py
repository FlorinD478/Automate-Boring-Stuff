def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number +1)
        return 3 * number +1


while True:
 print('Introduceti un numar:')
 try:
  number = int(input())
  r=str(number)
  if r.isnumeric():   #cu asta verific daca un string e numar sau nu
     break
 except ValueError:
  print('Trebuie sa introduceti un integer')
    
 
while number != 1:
     number = collatz(number)
    

     
