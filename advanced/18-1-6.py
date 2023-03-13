# file_name = input()
file_name = 'test2.txt'

with open(file_name, encoding='utf-8') as file_text, open('forbidden_words.txt', encoding='utf-8') as file_forbidden_words:
    forbidden_words = file_forbidden_words.readline().rstrip().split()
    lines = []
    for line in file_text:
        lst = list(line.rstrip())
        i = 0
        while i < len(lst):
            found = False
            for f_word in forbidden_words:
                f_word_len = len(f_word)
                string = ''.join(lst[i:i + f_word_len]).lower()
                if string == f_word:
                    lst[i:i + f_word_len] = '*' * f_word_len
                    i += f_word_len
                    found = True
                    break
            if not found:
                i += 1
        print(''.join(lst))
