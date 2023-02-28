n, k = int(input()), int(input())

# n, k = 2, 1
# n, k = 5, 2
# n, k = 2, 1
# n, k = 50, 25
# n, k = 77, 28

# def convert_to(number, base, upper=False):
#     digits = '0123456789abcdefghijklmnopqrstuvwxyz'
#     if base > len(digits): return None
#     result = ''
#     while number > 0:
#         result = digits[number % base] + result
#         number //= base
#     return result.upper() if upper else result
#
#
# s = convert_to(n, k)
# s = s[1:] + s[0]
# print(s)
# print(int(s, k))

if k == 1:
    print(n)
else:
    list1 = [i for i in range(n)]
    i = 1
    while len(list1) > 1:
        i = (i + k - 1) % len(list1)
        del list1[i]

    print(list1[0])
