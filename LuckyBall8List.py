import random

messages =['It is certain', 'It is decidedly so', 'Yes definetely', 'Reply hazy try again', 'Ask again later ', 'Concentrate and ask again', 'My replay is no', 'Outlook not so good', 'Very doubtful']
while True:
  print(messages[random.randint(0,len(messages) - 1)])
  print('Vrei sa incerci din nou? ')
  var0 = input()
  if var0 == "no" or var0 == "No" or var0 == 'NO':
      break
  elif var0 =='yes' or var0 =='Yes' or var0 =='YES':
      continue
  else:
      print('Acesta nu este un raspuns plauzibil, la revedere!')
      break
