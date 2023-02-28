n = int(input())
list1 = [int(input()) for _ in range(n)]
product = int(input())


def is_product(list1, product):
    for i in range(len(list1)):
        for j in range(len(list1)):
            if i != j and list1[i] * list1[j] == product:
                return True
    return False


if is_product(list1, product):
    print('ДА')
else:
    print('НЕТ')
