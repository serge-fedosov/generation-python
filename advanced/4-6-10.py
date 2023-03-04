n, m = [int(s) for s in input().split()]

matrix = [[0] * m for _ in range(n)]

DIR_RIGHT = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_UP = 3
direction = DIR_RIGHT


def is_valid_move(matrix, n, m, row, col, direction):
    if direction == DIR_RIGHT:
        new_col = col + 1
        if new_col < m and matrix[row][new_col] == 0:
            return True
    elif direction == DIR_DOWN:
        new_row = row + 1
        if new_row < n and matrix[new_row][col] == 0:
            return True
    elif direction == DIR_LEFT:
        new_col = col - 1
        if new_col >= 0 and matrix[row][new_col] == 0:
            return True
    elif direction == DIR_UP:
        new_row = row - 1
        if new_row >= 0 and matrix[new_row][col] == 0:
            return True
    return False


count = 1
count2 = 0
row = 0
col = 0
correct = True
while count2 < 4:
    if correct:
        matrix[row][col] = count

    if is_valid_move(matrix, n, m, row, col, direction):
        if direction == DIR_RIGHT:
            col += 1
        elif direction == DIR_DOWN:
            row += 1
        elif direction == DIR_LEFT:
            col -= 1
        elif direction == DIR_UP:
            row -= 1

        correct = True
        count += 1
        count2 = 0
    else:
        direction = (direction + 1) % 4
        count2 += 1
        correct = False

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
