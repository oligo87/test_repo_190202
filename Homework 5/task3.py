with open('source.txt') as source_file:
    text = source_file.read()

list_words = text.split()

sorted_list = list(set(list_words))
sorted_list.sort()

for i in sorted_list:
    counter = list_words.count(i)
    with open('sorted.txt', 'a') as new_file:
        new_file.write(f'{i} {str(counter)}\n')
