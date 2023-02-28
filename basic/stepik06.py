strings = input().split()
result = []
for word in strings:
    k = len(word.strip(',."!'))
    new_word = ''
    for c in word:
        ord_c = ord(c)
        if ord('a') <= ord_c <= ord('z'):
            ord_v = (ord_c - ord('a') + k) % 26 + ord('a')
        elif ord('A') <= ord_c <= ord('Z'):
            ord_v = (ord_c - ord('A') + k) % 26 + ord('A')
        elif ord('а') <= ord_c <= ord('я'):
            ord_v = (ord_c - ord('а') + k) % 32 + ord('а')
        elif ord('А') <= ord_c <= ord('Я'):
            ord_v = (ord_c - ord('А') + k) % 32 + ord('А')
        else:
            ord_v = ord_c
        new_word += chr(ord_v)

    result.append(new_word)

print(' '.join(result))
