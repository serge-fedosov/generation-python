total = 0
for b in range(1, 300):
    for k in range(1, 300):
        for t in range(1, 300):
            if 10 * b + 5 * k + 0.5 * t == 100 and b + k + t == 100:
                total += 1
                print('b =', b, 'k =', k, 't =', t)
print('Общее количество натуральных решений =', total)
