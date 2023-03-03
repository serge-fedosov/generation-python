n = int(input())
matrix = [[int(s) for s in input().split()] for _ in range(n)]
matrix2 = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix2[n - j - 1][n - i - 1] = matrix[i][n - j - 1]

for i in range(n):
    for j in range(n):
        print(matrix2[i][j], end=' ')
    print()
