n = int(input())
m = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(s) for s in input().split()])

max_val = matrix[0][0]
max_row = 0
max_col = 0

for i in range(n):
    for j in range(m):
        if max_val < matrix[i][j]:
            max_val = matrix[i][j]
            max_row = i
            max_col = j

print(max_row, max_col)
