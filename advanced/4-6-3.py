n, m = [int(s) for s in input().split()]

matrix = [[0] * m for _ in range(n)]

count = 1
for i in range(n):
    for j in range(m):
        matrix[i][j] = count
        count += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
