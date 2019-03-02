a = int(input('Input a: '))
b = int(input('Input b: '))
c = int(input('Input c: '))

while not (a <= b <= c):
    if a > b:
        a, b = b, a
    elif b > c:
        b, c = c, b
else:
    print('Sorted: {0}, {1}, {2}'.format(a, b, c))
