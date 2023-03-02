n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(s) for s in input().split()])

max_val = matrix[0][0]
for i in range(n):
    for j in range(n):
        if (j <= i <= n - 1 - j or j >= i >= n - 1 - j) and matrix[i][j] > max_val:
            max_val = matrix[i][j]

print(max_val)
