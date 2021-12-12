import random
# генерация случайного списка
lst_int = [random.randrange(1, 15) for i in range(10)]
print("Случайно созданный список: ", lst_int)

# функция, которая выводит
# кортеж из уникальных чисел из списка
# в обратном пордке
def revers_unique_tuple():
    lst_unique = []
    for i in range(len(lst_int)):
        if lst_int.count(lst_int[i]) == 1:
            lst_unique.append(lst_int[i])
    lst_unique.sort()
    tpl = tuple(lst_unique[::-1])
    print(f"Результат:\n{tpl}")


revers_unique_tuple()
