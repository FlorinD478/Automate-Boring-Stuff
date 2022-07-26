egg = ('Hello', 43.5, -5) # tuplele sunt liste scrise cu paranteze
print(egg[2])

abc = ('Halou',) #tupla cu un singur element
abcd = ('Halou') # string
print(type(abc))
print(type(abcd))
abcd = list(abcd) # lista
print(abcd)

egg[1] = 99 # tuplele la fel ca stringurile sunt nemodificabile,
#asa ca egg[1] = 99 va da eroare
#TypeError: 'tuple' object does not support item assignment
print(egg)
