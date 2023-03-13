# file_name = input()
file_name = 'test.txt'

with open(file_name, encoding='utf-8') as file:
    lines = []
    for line in file:
        if len(lines) == 10:
            del lines[0]
        lines.append(line)
    print(*lines, sep='')
