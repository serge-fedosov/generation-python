list1 = [int(s) for s in input().split()]

count = 1
x_prev = list1[0]
for i in range(1, len(list1)):
    if list1[i] != x_prev:
        count += 1
    x_prev = list1[i]

print(count)
