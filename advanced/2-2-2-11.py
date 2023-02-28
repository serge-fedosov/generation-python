s = input() + ' запретил букву'

for c in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
    if c in s:
        print(s, c)
        s = s.replace(c, '')
        s = s.replace('  ', ' ')
        s = s.strip()
        if len(s) == 0:
            break
