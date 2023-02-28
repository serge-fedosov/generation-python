timur = input()
ruslan = input()

stone = 'камень'
scissors = 'ножницы'
paper = 'бумага'

if timur == ruslan:
    print('ничья')
elif (timur == stone and ruslan == scissors or timur == scissors and ruslan == paper
      or timur == paper and ruslan == stone):
    print('Тимур')
else:
    print('Руслан')
