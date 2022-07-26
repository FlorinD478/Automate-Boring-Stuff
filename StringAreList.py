name = 'Yggdrasil'

print(name[0],\
      '\n')
for i in name:
    print('***' + i + '***') #soo cool

newName= name[0:6] +'s' + name[6:9]
print(newName)




#daca vrei sa schimbi elementele unei liste
#ex. eg = [1,2,3] in eg = [4,5,6] trebuie sa stergi cu del fiecare element
#si sa adaugi apoi cu append (eg.append(4)..) elementele care le vrei
eg = [1,2,3]
del eg[2]
del eg[1]
del eg[0]
eg.append(4)
eg.append(5)
eg.append(6)
print(eg)
