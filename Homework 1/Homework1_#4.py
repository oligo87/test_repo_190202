a = int(input('Input a: '))
b = int(input('Input b: '))
c = int(input('Input c: '))

if a + b > c and a + c > b and b + c > a :
    print ('YES')
else :
    print ('NO')