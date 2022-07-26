spam = ['hello', 'hi', 'whatup', 'hello', 'heya']
print(spam.index('hello'), spam.index('whatup'))
#cand ai mai multe valori la fel o ia pe prima pe care o gaseste
spam.append('Hy')
spam.insert(1,'Hello beautiful')
print(spam.count('hello'))
spam.sort(key=str.lower, reverse = True)
# sort sorteaza folosind codul ASCII unde literele mari sunt inainte de literele mici
#daca vrei sa sortezi in ordine alfabetica: lista.sort(key=str.lower)
print(spam)
# returnul la spam.append, spam.insert este None asa ca nu pot fi incarcate intr-o variabila
#nu poate fi incarcata intr-o noua variabila, dar modifica permanent(pana schimbi tu) spam
spam.remove('hi')
print(spam)
# del este bun cand sti indexul , remove este bun cand sti valoarea!!!!
