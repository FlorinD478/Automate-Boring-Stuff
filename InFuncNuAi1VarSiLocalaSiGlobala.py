def spam():
    print(eggs) # va da eroare
    eggs = 'spam local'

eggs = 'global'
spam()
