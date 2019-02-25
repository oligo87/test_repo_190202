# l = ['We are not what we should be!', 'We are not what we need to be.', 'But at least we are not what we used to be']
# x = 0
# for i in l:
#     if len(i) % 2 != 0:
#         x += 1
# print(x)

# d = {'name': 'ivan', 'lastname': 'ivanov', 'age': 30}
# for key in d:
#     print(key, ': ', d[key], sep='')
#     print(type(d[key]))

# def func(*args):
#     l = list(args)
#     l.sort()
#     return l[1]
#
# x = func(1, 6, 3, 7)
# print(x)

# def func(**kwargs):
#     return '{} is {}'.format(kwargs.get('name'), kwargs.get('job'))
#
# x = func(a=1, job='lazybum', name='Bob')
# print(x)

names = ['vasya', 'Sasha', 'olena', '123456', 'KOLYA']
names = [name.title() for name in names if name.isalpha()]
print(names)