lista = ''
for i in range(0,5):
    inp = input()
    lista += inp

lista = list(lista)
lista.sort()
lista = tuple(lista)
lista = str(lista)
print(lista, type(lista))
