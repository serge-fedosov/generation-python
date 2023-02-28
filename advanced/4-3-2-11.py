from math import factorial

n = int(input())


def pascal(n):
    result = []
    for m in range(n + 1):
        k = factorial(n) // (factorial(m) * factorial(n - m))
        result.append(k)
    return result


for i in range(n):
    print(*pascal(i))
