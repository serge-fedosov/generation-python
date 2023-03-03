n = int(input())
matrix = [[int(s) for s in input().split()] for _ in range(n)]

for i in range(n):
    matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
