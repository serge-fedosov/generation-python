n = int(input())

matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i <= j and i <= n - j - 1 or i >= j and i >= n - j - 1:
            matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
