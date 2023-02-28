import random

word_list = ['мама', 'рама', 'время']


def get_word():
    return random.choice(word_list).upper()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток

    word = word.upper()
    print('Давайте играть в угадайку слов!')

    while True:
        display_hangman(tries)
        print('Осталось попыток: ', tries)

        word_completion = ''
        for c in word:
            if c in guessed_letters:
                word_completion += c
            else:
                word_completion += '_'
        print(word_completion)

        if tries == 0:
            print('Вы не угадали слово', word)
            break

        s = input('Введите букву или слово целиком: ').upper()
        if not s.isalpha():
            print('Можно вводить только буквы!')
        elif len(s) == 1 and s in guessed_letters:
            print('Вы уже вводили эту букву!')
        elif len(s) > 1 and s in guessed_words:
            print('Вы уже вводили это слово!')
        else:
            if len(s) == 1:
                guessed_letters.append(s)
            else:
                guessed_words.append(s)

            if s == word:
                print(f'Поздравляем, вы угадали слово {word}! Вы победили!')
                break
            else:
                if s not in word:
                    tries -= 1

                found = True
                for c in word:
                    if c not in guessed_letters:
                        found = False
                        break
                if found:
                    print(f'Поздравляем, вы угадали последнюю букву и слово целиком {word}! Вы победили!')
                    break


while True:
    play(get_word())
    repeat = input('Сыграем ещё раз? (да/нет) ')
    if repeat == 'нет':
        break
