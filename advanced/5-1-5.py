n = int(input())
matrix = [[int(s) for s in input().split()] for _ in range(n)]


def check_symm(matrix, n):
    for i in range(n):
        row1 = i
        col1 = n - i - 1
        row2 = i
        col2 = n - i - 1
        while 0 <= row1 < n and col1 >= 0:
            if matrix[row1][col1] != matrix[row2][col2]:
                return False
            row1 -= 1
            col2 += 1
    return True


print('YES') if check_symm(matrix, n) else print('NO')
