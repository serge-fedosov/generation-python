list1 = [s for s in input().split()]
n = int(input())

list2 = []
for _ in range(n):
    list2.append([])

for idx, val in enumerate(list1):
    list2[idx % n].append(val)

print(list2)
