list1 = [int(s) for s in input().split()]

n = len(list1) - len(list1) % 2
for i in range(0, n, 2):
    list1[i], list1[i + 1] = list1[i + 1], list1[i]

print(*list1)
