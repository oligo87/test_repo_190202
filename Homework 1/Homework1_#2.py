a = 179
b = 971
n2 = 98
n3 = 765
n = 56.2
x = 4.321

c = (a**2 + b**2)**(0.5)
print('\n1. Hypotenuse: {0}'.format(c))

print('\n2. There are {0} tens in {1}'.format(n2 // 10, n2))

s3 = 0
for digit in str(n3):
    s3 += int(digit)
print('\n3. Sum of digits in {0} is {1}'.format(n3, s3))

import math
next_even = math.ceil(n / 2) * 2
if next_even == n:
    next_even += 2
print('\n4. The next even for {0} is {1}'.format(n, next_even))

s = str (x)
decimal = s.partition('.')[2]
print('\n5. Decimal part of {0} is {1}'.format(x, decimal))

print('\n6. First digit of {0} after . is {1}'.format(x, decimal[0]))
