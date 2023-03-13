def read_csv():
    with open('data.csv', encoding='utf-8') as file:
        result = []
        header = file.readline().split(',')
        header[-1] = header[-1].rstrip()
        for line in file:
            info = line.split(',')
            info[-1] = info[-1].rstrip()
            result.append(dict(zip(header, info)))
        return result


print(read_csv())
