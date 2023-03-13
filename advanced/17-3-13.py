from random import sample

with open('first_names.txt', encoding='utf-8') as file, open('last_names.txt', encoding='utf-8') as file2:
    first_names = [s.rstrip() for s in file.readlines()]
    last_names = [s.rstrip() for s in file2.readlines()]
    for first_name, last_name in zip(sample(first_names, 3), sample(last_names, 3)):
        print(first_name, last_name)
