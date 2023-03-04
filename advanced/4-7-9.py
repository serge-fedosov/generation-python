n, m = [int(s) for s in input().split()]

matrix = [[int(s) for s in input().split()] for _ in range(n)]
input()
matrix2 = [[int(s) for s in input().split()] for _ in range(n)]

result = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        result[i][j] = matrix[i][j] + matrix2[i][j]

for list1 in result:
    print(*list1)
