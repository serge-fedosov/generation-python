with open('population.txt', encoding='utf-8') as file:
    for line in file:
        country, population = line.split('\t')
        population = int(population)
        if country[0] == 'G' and population > 500_000:
            print(country)
