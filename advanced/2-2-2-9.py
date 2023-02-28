string = input()

max_count = 0
count = 0
prev = 'О'

for c in string:
    if c == 'Р':
        count += 1
        if max_count < count:
            max_count = count
    else:
        count = 0
    prev = c

print(max_count)
