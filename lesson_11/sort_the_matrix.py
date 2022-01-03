import random

# Ввод размера квадратной матрицы
m = int(input("Введите размер квадратной матрицы больше 5: "))


# Функция сортировки матрицы
def sort_the_matrix():
    # сортировка столбоцов по сумме их элементов, по возрастанию
    for i in range(len(matrix_lst)):
        for j in range(1, m):
            if matrix_lst[-1][j - 1] > matrix_lst[-1][j]:
                for k in range(len(matrix_lst)):
                    matrix_lst[k][j], matrix_lst[k][j - 1] = matrix_lst[k][j - 1
                                                                           ], \
                                                             matrix_lst[k][j]
        # сортировка  самих столбцов
    for run in range(m - 1):
        for i in range(m):
            for j in range(m - 1):
                if i % 2 != 0:
                    if matrix_lst[j][i] > matrix_lst[j + 1][i]:
                        matrix_lst[j][i], matrix_lst[j + 1][i] = \
                            matrix_lst[j + 1][
                                i], matrix_lst[
                                j][i]
                else:
                    if matrix_lst[j][i] < matrix_lst[j + 1][i]:
                        matrix_lst[j][i], matrix_lst[j + 1][i] = \
                            matrix_lst[j + 1][
                                i], matrix_lst[
                                j][i]

# функция вывода матрицы
def show_result(s):
    print(s)
    for i in range(len(matrix_lst)):
        for j in range(m):
            print("%4d" % matrix_lst[i][j], end='')
        print()

# проверка значения числа m
while True:
    if m > 5:
        matrix_lst = [[random.randint(1, 50) for i in range(m)] for j in
                      range(m)]
        sum_lst = []
        matrix_lst.append(sum_lst)
        # подсчет суммы элементов каждого из столбца и занесение их в список
        for i in range(m):
            summa = 0
            for j in range(m):
                summa += matrix_lst[j][i]
            matrix_lst[-1].append(summa)
        show_result("До сортировки:")
        sort_the_matrix()
        show_result("После сортировки: ")
        break
    else:
        print("Ошибка!")
        m = int(input("Введите размер квадратной матрицы больше 5: "))
        continue
