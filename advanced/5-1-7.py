s = input()

n = 8
cell_free = '.'
cell_ferz = 'Q'
cell_go = '*'

l1 = '87654321'
l2 = 'abcdefgh'
matrix = [[cell_free for _ in range(n)] for _ in range(n)]

row = l1.index(s[1])
col = l2.index(s[0])

for row1 in range(n):
    for col1 in range(n):
        if abs(row - row1) == abs(col - col1) or row == row1 or col == col1:
            matrix[row1][col1] = cell_go

matrix[row][col] = cell_ferz

for list1 in matrix:
    print(*list1)
