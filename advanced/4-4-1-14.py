n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(s) for s in input().split()])

total_up = 0
total_right = 0
total_down = 0
total_left = 0

for i in range(n):
    for j in range(n):
        if j < i < n - 1 - j:
            total_left += matrix[i][j]
        elif j > i > n - 1 - j:
            total_right += matrix[i][j]
        elif j > i and i < n - 1 - j:
            total_up += matrix[i][j]
        elif i > j and i > n - 1 - j:
            total_down += matrix[i][j]

print('Верхняя четверть:', total_up)
print('Правая четверть:', total_right)
print('Нижняя четверть:', total_down)
print('Левая четверть:', total_left)
