n = int(input())
matrix = [[int(s) for s in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for list1 in matrix:
    print(*list1)
