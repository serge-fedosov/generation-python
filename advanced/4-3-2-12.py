list1 = input().split()

list2 = []
pred = ''
pos = -1

for c in list1:
    if c != pred:
        list2.append([c])
        pos += 1
        pred = c
    else:
        list2[pos].append(c)

print(list2)
