list1 = [int(s) for s in input().split()]

n = list1[-1]
# for i in range(len(list1) - 1, 0, -1):
for i in range(-1, -len(list1), -1):
    list1[i] = list1[i - 1]
list1[0] = n

print(*list1)
