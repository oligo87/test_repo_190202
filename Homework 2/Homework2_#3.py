i = 0
while i <= 10:
    print(i)
    i += 1

x = 20
while x >= 0:
    print(x, end=' ')
    x -= 1

while True:
    number = input('\n\nEnter number: ')
    try:
        number = int(number)
        z = 0
        while number % 2 == 0:
            number /= 2
            z += 1
        print('Odd remainder: {0}. Iterations: {1}'.format(int(number), z))
        break
    except ValueError:
        print('Input integer!')