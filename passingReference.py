import copy

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1,2,3, 'Hello']
eggs(spam)
print(spam)

ches = spam # au aceeasi referinta la lista
ches[1] = 'Hy'
print(ches, spam)

ralf = copy.copy(spam) # copiaza lista la o referinta noua;
#deepcopy se foloseste cand vrei sa copiezi o lista cu liste in ea
ralf[2] = 'Ralf'
spam.remove('Hello')
print(ralf, spam)

print(spam[-1])

ar = [1,2,3]
ar *=2
pf = ['hi']
arpf = ar +pf
print(arpf)
