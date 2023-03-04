n = int(input())
matrix = [[int(s) for s in input().split()] for _ in range(n)]

max_val = matrix[n - 1][n - 1]
for i in range(n):
    for j in range(n):
        if (j >= i >= n - j - 1 or i >= j and i >= n - j - 1) and max_val < matrix[i][j]:
            max_val = matrix[i][j]

print(max_val)
