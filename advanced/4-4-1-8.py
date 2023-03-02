n = int(input())
m = int(input())

matrix = []

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(input())

for i in range(n):
    for j in range(m):
        print(matrix[i][j], '', end='')
    print()
