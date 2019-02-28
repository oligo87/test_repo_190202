def func(*args):
    l = list(args)
    l.sort()
    s = list(set(l))
    return s[1]


x = func(1, 6, 3, 7, 1)
print(x)
