n = int(input())

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for _ in range(n):
    x, y = [int(s) for s in input().split()]
    if x > 0 and y > 0:
        q1 += 1
    elif x < 0 and y > 0:
        q2 += 1
    elif x < 0 and y < 0:
        q3 += 1
    elif x > 0 and y < 0:
        q4 += 1

print('Первая четверть:', q1)
print('Вторая четверть:', q2)
print('Третья четверть:', q3)
print('Четвертая четверть:', q4)
