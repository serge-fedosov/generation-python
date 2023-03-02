n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(s) for s in input().split()])

for i in range(n):
    avg = sum(matrix[i]) / len(matrix[i])
    count = 0
    for val in matrix[i]:
        if val > avg:
            count += 1
    print(count)
