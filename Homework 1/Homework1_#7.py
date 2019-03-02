hero = {}
hero['name'] = input('Enter Name: ')
hero['lastname'] = input('Enter Last Name: ')
hero['age'] = input('Enter Age: ')
hero['gender'] = input('Enter Gender: ')
hero['profession'] = input('Enter Profession: ')

print('\n')
for i in hero:
    print('{0:10}	{1}'.format(i, hero[i]))

hero['age'] = input('\nEnter new Age of {0} {1}: '.format(hero['name'], hero['lastname']))
hero['profession'] = input('Enter new Profession of {0} {1}: '.format(hero['name'], hero['lastname']))

print('\n')
for i in hero:
    print('{0:10}	{1}'.format(i, hero[i]))
