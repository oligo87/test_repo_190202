year = input('Input Year: ')
year = int(year)

if year % 400 == 0 and not (year % 100 == 0):
    s = 'YES'
elif not (year % 400 == 0) and year % 100 == 0:
    s = 'NO'
elif year % 4 == 0:
    s = 'YES'
else:
    s = 'NO'

print ('Leap Year: ', s)