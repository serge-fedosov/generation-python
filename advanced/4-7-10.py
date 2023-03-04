n1, m1 = [int(s) for s in input().split()]
matrix = [[int(s) for s in input().split()] for _ in range(n1)]
input()
n2, m2 = [int(s) for s in input().split()]
matrix2 = [[int(s) for s in input().split()] for _ in range(n2)]

result = [[0] * m2 for _ in range(n1)]

for i in range(n1):
    for j in range(m2):
        total = 0
        for k in range(m1):
            total += matrix[i][k] * matrix2[k][j]
        result[i][j] = total

for list1 in result:
    print(*list1)
