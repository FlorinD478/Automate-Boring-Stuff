catName = []
while True:
    print("Introduceti numele pisicii " + (str(len(catName)+1)) + ' (sau introduceti Stop cand nu mai aveti pisici de introdus)')
    name = input()
    if name == 'Stop':
        break
    catName = catName + [name]
if len(catName) == 0:
    print('Nu ai pisici')
else:
    print('Numele pisicilor tale sunt:')
    for name in catName:
        print(' ' + name)
