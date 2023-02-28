list1 = [int(s) for s in input().split()]

count = 0
for i in range(1, len(list1)):
    if list1[i] > list1[i - 1]:
        count += 1

print(count)
