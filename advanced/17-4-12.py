with open('goats.txt', encoding='utf-8') as file_input, open('answer.txt', 'w') as file_output:
    file_input.readline()
    colours = []
    line = file_input.readline().rstrip()
    while line != 'GOATS':
        colours.append(line)
        line = file_input.readline().rstrip()

    goats = {}
    count = 0
    line = file_input.readline().rstrip()
    while line != '':
        goats[line] = goats.get(line, 0) + 1
        count += 1
        line = file_input.readline().rstrip()

    for goat in sorted(goats):
        if goats[goat] / count > 0.07:
            file_output.write(goat)
            file_output.write('\n')
