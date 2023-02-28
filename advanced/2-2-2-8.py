timur = input()
ruslan = input()

stone = 'камень'
scissors = 'ножницы'
paper = 'бумага'
lizard = 'ящерица'
spok = 'Спок'

if timur == ruslan:
    print('ничья')
elif (timur == scissors and ruslan == paper or timur == paper and ruslan == stone
      or timur == stone and ruslan == lizard or timur == lizard and ruslan == spok
      or timur == spok and ruslan == scissors or timur == scissors and ruslan == lizard
      or timur == lizard and ruslan == paper or timur == paper and ruslan == spok
      or timur == spok and ruslan == stone or timur == stone and ruslan == scissors):
    print('Тимур')
else:
    print('Руслан')
