with open('nums.txt', encoding='utf-8') as file:
    data = file.read() + ' '
    total = 0
    num = ''
    digits_start = False
    for char in data:
        if char.isdigit() and digits_start:
            num += char
        elif char.isdigit() and not digits_start:
            num += char
            digits_start = True
        elif digits_start:
            total += int(num)
            num = ''
            digits_start = False

    print(total)










