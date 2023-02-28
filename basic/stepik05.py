# direction = input('направление: шифрование или дешифрование (ш/д) ')
# language = input('язык алфавита: русский или английский (ru/en) ')
string = 'Hawnj pk swhg xabkna ukq nqj.'
k = int(input('на сколько символов сдвигать?  '))


for k in range(-1, -25, -1):
    result = ''
    for c in string:
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
        result += chr(ord_v)

    print(f'k={k} string={result}')
