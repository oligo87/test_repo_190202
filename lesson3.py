a = int(input('Enter A: '))
b = int(input('Enter B: '))

def hipotenuse(x, y):
    global c
    c = (x**2 + y**2)**0.5
    return c
hipotenuse(a, b)
print('C = ', c)