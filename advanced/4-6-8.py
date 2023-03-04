n, m = [int(s) for s in input().split()]

matrix = [[0] * m for _ in range(n)]

count = 1
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            matrix[i][j] = count
        else:
            matrix[i][m - j - 1] = count
        count += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
