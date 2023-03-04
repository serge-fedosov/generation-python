n, m = [int(s) for s in input().split()]

matrix = [[0] * m for _ in range(n)]

for i in range(n):
    count = i % m
    for j in range(m):
        matrix[i][j] = count + 1
        count = (count + 1) % m

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
