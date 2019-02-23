l = [54, 23, 7, 64, 9, 25]
for i in range(len(l)):
    print(l)
    l.pop(0)

print('\n')

string = 'lorem ipsum'
for i in range(len(string)):
    print(string)
    string = string[1:]

print('\n')

l = [54, 23, 7, 64, 9, 25]
for i in range(len(l)):
    print(l)
    l.pop(l.index(min(l)))
