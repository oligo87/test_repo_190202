string = input('Enter string: ')

if len(string) % 2 == 0:
    i = len(string) / 2 - 1

    x = string.partition(string[int(i)])
    part1 = x[0] + x[1]
    part2 = x[2]
    new_str = part2 + part1

    print(new_str)
else:
    i = len(string) // 2

    x = string.partition(string[int(i)])
    part1 = x[0] + x[1]
    part2 = x[2]
    new_str = part2 + part1

    print(new_str)