string = input('Type: ')

print('\n1. All the characters are digits:', string.isdigit())

print('\n2. Spaces in the string:', string.count(' '))

print('\n3. Dots in the string:', string.count('.'))

h = 'Homework'
print('\n4. {0:_^100}'.format(h))

print('\n5. First letter in each word upper case:', string.title())
