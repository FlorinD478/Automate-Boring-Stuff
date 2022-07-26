grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
def rasturnare(someList):    
 for y in range(0,len(someList[0])):
    for x in range(0,len(someList)):
        print(someList[x][y], end = ' ')
    print()

rasturnare(grid)


print('Doriti sa creati un grid? (yes/no)')
raspuns = input()
if raspuns =='yes':
    #Dimensiunile gridului
    print("Cate randuri doriti in grid? x = ", end= '')
    A = int(input())
    print('Cate coloane doriti in grid? y = ', end= '')
    B = int(input())
    # Masca de afisare
    gridul = []
    for x in range(0,A):
        for y in range(0,B):
            print('grid[',x,']','[',y,'] = ' ,end = '')
            gridul[x][y] = int(input())
        print()

    print(gridul)

else:
    print("La revedere!")
