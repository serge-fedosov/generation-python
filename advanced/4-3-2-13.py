list1 = input().split()
n = int(input())


def chunked(list1, n):
    result = []
    idx = -1
    for i in range(len(list1)):
        if i % n == 0:
            result.append([list1[i]])
            idx += 1
        else:
            result[idx].append(list1[i])
    return result


print(chunked(list1, n))
