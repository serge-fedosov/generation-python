n = int(input())
matrix = [[int(s) for s in input().split()] for _ in range(n)]


def check_matrix(matrix, n):
    list1 = []
    diag_1 = 0
    diag_2 = 0
    total = sum(matrix[0])
    for i in range(n):
        diag_1 += matrix[i][i]
        diag_2 += matrix[i][n - i - 1]
        if sum(matrix[i]) != total:
            return False
        total_col = 0
        for j in range(n):
            list1.append(matrix[i][j])
            total_col += matrix[j][i]
        if total_col != total:
            return False
    if diag_1 != total or diag_2 != total:
        return False

    for i in range(1, n ** 2 + 1):
        if i not in list1:
            return False

    return True


print('YES') if check_matrix(matrix, n) else print('NO')
