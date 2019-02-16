hero = {}
hero['name'] = str(input('Enter Name: '))
hero['lastname'] = str(input('Enter Last Name: '))
hero['age'] = str(input('Enter Age: '))
hero['gender'] = str(input('Enter Gender: '))
hero['profession'] = str(input('Enter Profession: '))

print('\n')
for i in hero:
    print('{0:10}	{1}'.format(i, hero[i]))

hero['age'] = str(input('\nEnter new Age of {0} {1}: '.format(hero['name'],hero['lastname'])))
hero['profession'] = str(input('Enter new Profession of {0} {1}: '.format(hero['name'],hero['lastname'])))

print('\n')
for i in hero:
    print('{0:10}	{1}'.format(i, hero[i]))
