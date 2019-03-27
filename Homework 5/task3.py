import string

with open('source.txt') as source_file:
    text = source_file.read()

text = text.casefold()
text = text.translate(str.maketrans('', '', string.punctuation))
list_words = text.split()

sorted_list = list(set(list_words))
sorted_list.sort()

with open('sorted.txt', 'a') as new_file:
    for i in sorted_list:
        counter = list_words.count(i)
        new_file.write(f'{i} {str(counter)}\n')
