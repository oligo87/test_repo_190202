a = int(input('Input a: '))
b = int(input('Input b: '))
c = int(input('Input c: '))

i = 0
def count_match (x, y):
    global i
    if x == y:
        if i == 0:
            i += 2
        else:
            i += 1

count_match (a, b)
count_match (a, c)
if i != 3:
    count_match (b, c)

print (i)
