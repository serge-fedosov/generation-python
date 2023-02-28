n = int(input())

string = 'anton'
list1 = []

for i in range(1, n + 1):
    s = input()
    j = 0
    for k in range(len(s)):
        if s[k] == string[j]:
            if j == len(string) - 1:
                list1.append(i)
                break  # нашли слово
            if j < len(string) - 1:
                j += 1
            else:
                break  # не нашли слово

print(*list1)
