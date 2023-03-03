n = int(input())
matrix = [[int(s) for s in input().split()] for _ in range(n)]


def is_simm(matrix, n):
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    else:
        return True


print('YES') if is_simm(matrix, n) else print('NO')
