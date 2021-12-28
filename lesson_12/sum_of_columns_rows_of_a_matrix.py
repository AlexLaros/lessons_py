"""
Working with matrix elements.

--------------------------------------------------------------------------------
Available actions:
- Create an M x N Matrix from random numbers from 1 to 50 -
"create_the_matrix()";
- Formatted matrix output - "show_the_matrix()";
- Counting the sum of the elements of the rows of a matrix - "sum_of_rows()";
- Counting the sum of the elements of the columns of a matrix -
"sum_of_columns()".
--------------------------------------------------------------------------------
"""
from random import randint

__all__ = [
    "create_the_matrix",
    "show_the_matrix",
    "sum_of_columns",
    "sum_of_rows"
]


def create_the_matrix() -> list:
    """
    The function generates a matrix of random numbers from 1 to 50, size m by n,
    which are entered by the user. The function takes no arguments.
    :return: matrix
    """
    global m, n
    m = int(input("Enter the number of columns: "))
    n = int(input("Enter the number of rows: "))
    matrix = [[randint(1, 50) for j in range(n)] for i in range(m)]
    return matrix


def sum_of_columns(matrix) -> list:
    """
    This function calculates the sum of the elements of the columns of the
    matrix. The function takes one argument, a list.
    :param matrix: list
    :return: list
    """
    sum_lst = []
    for i in range(n):
        summa = 0
        for j in range(m):
            summa += matrix[j][i]
        sum_lst.append(summa)
    matrix.append('')
    matrix.append(sum_lst)
    return matrix


def sum_of_rows(matrix) -> list:
    """
    This function calculates the sum of the elements of the rows of the matrix.
    The function takes one argument, a list.
    :param matrix: list
    :return: list
    """
    sum_lst = []
    for i in range(m):
        summa = 0
        for j in range(n):
            summa += matrix[i][j]
        matrix[i].append('')
        matrix[i].append(summa)
    return matrix


def show_the_matrix(matrix) -> list:
    """
    This function print the matrix. The function takes one argument, a list.
     :param matrix: list
     :return: list
     """
    print()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('{:>3}'.format(matrix[i][j]), end=' ')
        print()
    return matrix


if __name__ == "__main__":
    # тест №1 подсчет сначала столбцов, затем строк.
    lst = create_the_matrix()
    show_the_matrix(lst)
    lst = sum_of_columns(lst)
    lst = sum_of_rows(lst)
    show_the_matrix(lst)
    # тест №2 подсчет сначала строк, затем столбцов.
    lst1 = create_the_matrix()
    show_the_matrix(lst1)
    lst1 = sum_of_rows(lst1)
    lst1 = sum_of_columns(lst1)
    show_the_matrix(lst1)
