name = input()
if name == 'Mary':
    print('Hello '+name)
else:
    print('Is that you, Spartacus Aurelius Cezare al treilea?')

password = input()
if password == 'mustar':
    print('acces granted')
else:
    print('Wrong pass')

if len(name)<len(password):
    if len(name)+7<len(password):
        print('Asa ceva nu se poate')
    elif len(name)+4>len(password):
        print('asa si asa')
    else:
        print('No, ai pus-o')
else:
    print('Slanina nu e rea de loc')
