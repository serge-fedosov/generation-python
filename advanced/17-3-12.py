with open('file.txt', encoding='utf-8') as file:
    lines = 0
    data = ''
    for line in file:
        lines += 1
        data += line

    data = data.split()
    words = len(data)
    letters = 0
    for word in data:
        for char in word:
            if char.isalpha():
                letters += 1

    print(f'Input file contains:\n{letters} letters\n{words} words\n{lines} lines')
