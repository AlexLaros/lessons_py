from random import randrange

# Декоратор 
def count_time(func):
    import time

    def inner(s, f):
        start = time.time()
        value = func(s, f)
        end = time.time()
        do_time = round((end - start), 4)
        print('Время выполнения:', do_time)
        return value

    return inner

# функция линейного поиска №1
@count_time
def line_search_1(sequence, look_for):
    for i in range(len(sequence)):
        if sequence[i] == look_for:
            return f'Номер элемента "{look_for}" в списке - {i}'
    return 'Ничего не найдено.'

# функция линейного поиска №2
@count_time
def line_search_2(sequence, look_for):
    sequence.append(look_for)
    i = 0
    while sequence[i] != look_for:
        i += 1
    sequence.pop()
    if i != len(sequence):
        return f'Номер элемента "{look_for}" в списке - {i}'
    return 'Ничего не найдено.'


lst = [randrange(50) for i in range(10_000_000)]
print(line_search_1(lst, 51))
print(line_search_2(lst, 51))
