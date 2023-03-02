n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(s) for s in input().split()])

total = 0
for i in range(n):
    total += matrix[i][i]

print(total)
