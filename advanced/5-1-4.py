n = int(input())
matrix = [['.' for _ in range(n)] for _ in range(n)]

star = '*'

for i in range(n):
    matrix[i][i] = star
    matrix[i][n - i - 1] = star
    matrix[n // 2][i] = star
    matrix[i][n // 2] = star

for list1 in matrix:
    print(*list1)
