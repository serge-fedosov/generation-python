n, m = int(input()), int(input())
matrix = [[int(s) for s in input().split()] for _ in range(n)]
i, j = [int(s) for s in input().split()]

for k in range(n):
    matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]

for i in range(n):
    for j in range(m):
        print(matrix[i][j], '',  end='')
    print()
