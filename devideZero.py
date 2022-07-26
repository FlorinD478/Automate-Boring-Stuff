#def spam(divideBy):
#    return 42/ divideBy
#print(spam(3))
#print(spam(5))
#print(spam(0)) # o sa dea eroare
#print(spam(6))

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')
print(spam(3))
print(spam(5))
print(spam(0))
print(spam(6))
