year = input('Input Year: ')
year = int(year)

if not (year % 400 == 0) and year % 100 == 0:
    s = 'NO'
elif year % 4 == 0:
    s = 'YES'
else:
    s = 'NO'

print('Leap Year: ', s)
