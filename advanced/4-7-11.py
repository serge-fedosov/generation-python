n = int(input())
matrix = [[int(s) for s in input().split()] for _ in range(n)]
m = int(input())


def matrix_product(matrix1, matrix2, n):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            total = 0
            for k in range(n):
                total += matrix1[i][k] * matrix2[k][j]
            result[i][j] = total
    return result


result = matrix.copy()
for i in range(m - 1):
    result = matrix_product(result, matrix, n)

for list1 in result:
    print(*list1)
