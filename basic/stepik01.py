import random


def is_valid(value):
    return 1 <= int(value) <= 100


print('Добро пожаловать в числовую угадайку')
max_num = int(input('Введите максимальное целое число: '))
num = random.randint(1, max_num)

count = 0
is_exit = False
while not is_exit:
    value_str = input(f'Введите число от 1 до {max_num}: ')
    if is_valid(value_str):
        value = int(value_str)
        count += 1
        if value < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif value > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print('Количество попыток:', count)
            answer = input('Сыграем ещё раз (да, нет): ')
            if answer == 'да':
                num = random.randint(1, max_num)
                count = 0
            else:
                is_exit = True
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
