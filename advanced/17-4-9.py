from random import randint

with open('random.txt', 'w') as file:
    for _ in range(25):
        file.write(str(randint(111, 777)))
        file.write('\n')
