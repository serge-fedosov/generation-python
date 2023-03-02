n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(s) for s in input().split()])

max_val = matrix[0][0]
for i in range(n):
    for j in range(i + 1):
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]

print(max_val)
