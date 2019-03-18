# from lalala import song_gen
#
# filename = "file1.txt"
# file = open(filename, "w")
# file.write(song_gen(5, 6, 0))
#
#
# filename = "person.py"
# file = open(filename)
# print(file.read())

import requests
# import json
#
# p = {'spam': 'thjfgh'}
# r = requests.get('http://httpbin.org/get', headers={"Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7", "User-Agent": "potato"},
#                  params=p)
# print(r.text)
# d = r.json()
# print(d['headers']['Host'])

base_url = 'http://pulse-rest-testing.herokuapp.com'

# r = requests.post(base_url+'/books', data={'title': 'Trainspotting', 'author': 'Irwine Welsh'})
# books = r.json()
#
# print(books)

# r2 = requests.get(base_url+'/books')
# books = r2.json()

r3 = requests.delete(base_url+f'/books/')
# r2 = requests.get(base_url+'/books')
# books = r2.json()

# for book in books:
#     print(book['author'])

