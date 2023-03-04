n = int(input())
matrix = [[int(s) for s in input().split()] for _ in range(n)]


def check_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            if j + 1 not in matrix[i]:
                return False

            found = False
            for k in range(n):
                if j + 1 == matrix[k][i]:
                    found = True
                    break
            if not found:
                return False
    return True


print('YES') if check_matrix(matrix, n) else print('NO')
