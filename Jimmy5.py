print('My name is ')
for i in range(5):
    print('my name is Jimmy (' + str(i) + ')')

total = 0
for num in range(101):
    total=total + num
print(total)

total = 0
num = 1
while num<101:
    total = total + num
    num = num + 1
print(total)

# About range(a,b,c)
for e in range(1,10,2):  #numara din 2 in 2
    print(e)

for r in range(2,27,3):   # numara din 3 in 3
    print(r)

#modulul random
for f in range(5,-3,-1): #numara descrescator
    print(f)
import math, random, sys, os

for i in range(5):
    print(random.randint(1, 10))
    print(random.lognormvariate(3, 5))

#modulul sys functia exit
#while True:
 #   print('Type exit to exit/')
  #  response = input()
   # if response == 'exit':
    #    sys.exit()      #toata treaba asta mergea facuta cu functia continue dar in fine poate e mai folositoare finctia asta in unele situatii
    #print('You typed ' +response + '.') # se pare ca nu o sa se ruleze niciodata linia asta de cod


print('Scrie valoarea spam')

i=1
while i<=3:
 spam= input()
 if spam == '1':
    print('Hello')
 elif spam =='2':
    print('Howdy')
 else:
    print('Greetings!')
 i=i+1       
