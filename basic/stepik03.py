import random


def generate_password(length, chars):
    result = ''
    for _ in range(length):
        result += random.choice(chars)
    return result


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ignored_symbols = 'il1Lo0O'

passwords_count = int(input('Количество паролей для генерации? '))
password_length = int(input('Длина одного пароля? '))
ins_digits = input('Включать ли цифры 0123456789? (да/нет) ')
ins_big_letters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет) ')
ins_small_letters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет) ')
ins_special_sym = input('Включать ли символы !#$%&*+-=?@^_? (да/нет) ')
ignore_special_sym = input('Исключать ли неоднозначные символы il1Lo0O? (да/нет) ')

chars = ''
if ins_digits == 'да':
    for c in digits:
        if c not in chars and (ignore_special_sym != 'да' or c not in ignored_symbols):
            chars += c

if ins_big_letters == 'да':
    for c in uppercase_letters:
        if c not in chars and (ignore_special_sym != 'да' or c not in ignored_symbols):
            chars += c

if ins_small_letters == 'да':
    for c in lowercase_letters:
        if c not in chars and (ignore_special_sym != 'да' or c not in ignored_symbols):
            chars += c

if ins_special_sym == 'да':
    for c in punctuation:
        if c not in chars and (ignore_special_sym != 'да' or c not in ignored_symbols):
            chars += c

for _ in range(passwords_count):
    print(generate_password(password_length, chars))
