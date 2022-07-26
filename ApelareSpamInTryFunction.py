def spam(divideBy):
    return 42 / divideBy
try:
    print(spam(5))
    print(spam(3))
    print(spam(0))
    print(spam(2))
except ZeroDivisionError:
    print('Error: Invalid Argument')
