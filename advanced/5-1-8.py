n = int(input())

matrix = [[0] * n for _ in range(n)]

for i in range(n):
    count = i
    for j in range(n):
        matrix[i][j] = count
        if j >= i:
            count += 1
        else:
            count -= 1

for list1 in matrix:
    print(*list1)
