with open('input.txt', encoding='utf-8') as file_input, open('output.txt', 'w') as file_output:
    count = 1
    for line in file_input:
        file_output.write(str(count) + ') ' + line)
        count += 1
