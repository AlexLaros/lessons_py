def find_prime(x, y):
    """ Данная функция-генератор находит простые числа в указанном диапозоне
    от x до y не включительно"""
    lst_nums = []
    lst_div = []
    for j in range(x, y):
        lst_nums.append(j)

    for j in range(len(lst_nums)):
        lst_div.append([])

    for j in range(len(lst_div)):
        for k in range(1, lst_nums[j] + 1):
            if lst_nums[j] % k == 0:
                lst_div[j].append(k)

    for j in range(len(lst_div)):
        if len(lst_div[j]) == 2:
            yield lst_nums[j]


for i in find_prime(1, 100):
    print(i, end=' ')
