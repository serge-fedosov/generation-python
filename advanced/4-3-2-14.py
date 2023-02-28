list1 = input().split()

list2 = [[]]

for i in range(1, len(list1) + 1):
    for j in range(0, len(list1) - i + 1):
        list2.append(list1[j:j + i])

print(list2)
