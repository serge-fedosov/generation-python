from fractions import Fraction

# n = int(input())
n = 23
max_val = Fraction(1, n - 1)
for numerator in range(2, n // 2 + 1):
    denominator = n - numerator
    num = Fraction(numerator, denominator)
    if num.numerator == numerator and num.denominator == denominator and max_val < num:
        max_val = num

print(max_val)
