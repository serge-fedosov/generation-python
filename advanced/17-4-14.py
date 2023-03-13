def minutes(time1, time2):
    t1 = time1.split(':')
    t2 = time2.split(':')
    return int(t2[0]) * 60 + int(t2[1]) - int(t1[0]) * 60 - int(t1[1])


with open('logfile.txt', encoding='utf-8') as file_input, open('output.txt', 'w') as file_output:
    for line in file_input:
        name, time1, time2 = line.rstrip().split(', ')
        if minutes(time1, time2) >= 60:
            file_output.write(name)
            file_output.write('\n')

