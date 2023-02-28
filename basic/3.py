for a in range(1, 61):
    for b in range(1, 65):
        for c in range(1, 70):
            for d in range(1, 151):
                for e in range(1, 151):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print(f'a={a}, b={b}, c={c}, d={d}, e={e}, sum={a + b + c + d + e}')
                        break
