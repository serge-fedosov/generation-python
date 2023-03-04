n, m = [int(s) for s in input().split()]

matrix = [[0] * m for _ in range(n)]

count = 1
for i in range(m):
    row = 0
    col = i
    while row < n and col >= 0:
        matrix[row][col] = count
        row += 1
        col -= 1
        count += 1

for i in range(1, n):
    row = i
    col = m - 1
    while row < n and col >= 0:
        matrix[row][col] = count
        row += 1
        col -= 1
        count += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
