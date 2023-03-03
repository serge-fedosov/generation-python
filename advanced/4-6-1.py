n, m = [int(s) for s in input().split()]

sym_dot = '.'
sym_star = '*'
matrix = []

for i in range(n):
    list1 = []
    for j in range(m):
        if i % 2 == 0:
            list1.append(sym_dot if j % 2 == 0 else sym_star)
        else:
            list1.append(sym_star if j % 2 == 0 else sym_dot)
    matrix.append(list1)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
