s = input()

n = 8
cell_free = '.'
cell_horse = 'N'
cell_go = '*'

l1 = '87654321'
l2 = 'abcdefgh'


def set_go(row, col, matrix, symbol):
    if 0 <= row <= 7 and 0 <= col <= 7:
        matrix[row][col] = symbol


matrix = [[cell_free for _ in range(n)] for _ in range(n)]

row = l1.index(s[1])
col = l2.index(s[0])
matrix[row][col] = cell_horse

set_go(row - 1, col - 2, matrix, cell_go)
set_go(row - 2, col - 1, matrix, cell_go)
set_go(row - 2, col + 1, matrix, cell_go)
set_go(row - 1, col + 2, matrix, cell_go)

set_go(row + 1, col - 2, matrix, cell_go)
set_go(row + 2, col - 1, matrix, cell_go)
set_go(row + 2, col + 1, matrix, cell_go)
set_go(row + 1, col + 2, matrix, cell_go)

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
