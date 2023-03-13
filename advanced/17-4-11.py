with open('class_scores.txt', encoding='utf-8') as file_input, open('new_scores.txt', 'w') as file_output:
    for line in file_input:
        name, score = line.split()
        new_score = str(min(100, int(score) + 5))
        new_line = name + ' ' + new_score + '\n'
        file_output.write(new_line)
