string = input('Enter string: ')
try:
    print('\n1. The 3rd symbol:', string[2],
          '\n2. The second last symbol:', string[-2],
          '\n3. The first 5 symbols:', string[:5],
          '\n4. Without the last 2 symbols:', string[:-2],
          '\n5. Only even index symbols:', string[::2],
          '\n6. Only odd index symbols:', string[1::2],
          '\n7. Reverse:', string[::-1],
          '\n8. Reverse through one:', string[::-2],
          '\n9. Reverse without 1st and last:', string[-2:0:-1],
          '\n10. Length:', len(string))
except IndexError:
    print('Too short!')