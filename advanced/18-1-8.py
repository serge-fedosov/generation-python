# file_name = input()
file_name = 'test3.txt'

with open(file_name, encoding='utf-8') as file:
    prev_line = ''
    found = False
    for line in file:
        if line.startswith('def '):
            if not prev_line.startswith('#'):
                print(line[4:line.find('(')])
                found = True
        prev_line = line
    if not found:
        print('Best Programming Team')
