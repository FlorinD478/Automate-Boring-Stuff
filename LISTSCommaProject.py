
print("Cate elemente doriti sa adaugati in lista?")
nr = int(input())
lista = []
for i in range(0,nr):
    element = input()
    lista.append(element)
    
print(lista)

def commaPro(someList):
 for i in range(1,nr*2-1,2):
    if i == nr*2-3:
        someList.insert(i ,', and ')
    else:
        someList.insert(i  ,', ')
       
 legat = ''
 for i in range(0,nr*2-1):
    legat += lista[i]
 return legat
legat = commaPro(lista)
print(legat)
# nr = 3 ; acasa =0 , este = 1 , cald = 2 ; nr2*2-1 =5 ; nr*2-2 = 4
#i =1 ; range(0,5) bun lista[0] = acasa , lista[1] = ,  ; lista[2] = este, lista[3]= , , lista[4]=cald
#i =3 ;  
