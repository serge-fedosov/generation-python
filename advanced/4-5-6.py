n = int(input())
matrix = [[int(s) for s in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(n // 2):
        matrix[j][i], matrix[n - j - 1][i] = matrix[n - j - 1][i], matrix[j][i]

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
