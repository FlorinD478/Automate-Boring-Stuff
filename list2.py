try:
 spam = [['cat', 'dog', 'elephant', 'duck', 'cow', 'tiger'], 34, 21, [33,12]]
 print(spam[1],'\n', spam[-1],'\n',spam[-1][1], ' \n', spam[0][1:4],\
       '\n', spam[0:2], '\n', spam[2:])
 # folosesti \ in print pentru a scrie pe randul urmator; ajuta
 #la aranjarea randurilor lungi
 print(len(spam))
 print(len(spam[1]))
except TypeError:
    print('asta nu e o lista')
