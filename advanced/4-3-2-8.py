n = int(input())

my_list = [[i for i in range(1, n + 1)] for _ in range(1, n + 1)]

print(*my_list, sep='\n')
