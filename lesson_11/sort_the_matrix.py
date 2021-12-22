import random

# Ввод размера квадратной матрицы
m = int(input("Введите размер квадратной матрицы больше 5: "))
# генерация матрицы размера m из случайных чисел
matrix_lst = [[random.randint(1, 50) for i in range(m)] for j in range(m)]

# сумма элементов по столбцам
sum_lst = []
for i in range(m):
    summa = 0
    for j in range(m):
        summa += matrix_lst[j][i]
    sum_lst.append(summa)


def show_result(s):
    print()
    print(s)
    for i in range(m):
        for j in range(m):
            print(matrix_lst[i][j], end='  ')
        print()
    for i in sum_lst:
        print(i, end=' ')


def sort_the_matrix():
    # сортировка столбцов
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


while True:
    if m <= 5:
        m = int(input("Ошибка!\n Введите размер больше 5: "))
        continue
    else:
        show_result("До сортировки:")
        sort_the_matrix()
        show_result("После сортировки: ")
        break
