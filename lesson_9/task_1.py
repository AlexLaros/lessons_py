def find_sum_of(lst, a):
     """Данная функция проверяет наличие пары чисел из списка lst, чья сумма 
    равна числу a """
    summa = []
    for i in lst:
        for j in lst:
            if j <= i:
                continue
            else:
                summa.append(i + j)
    for i in range(len(set(summa))):
        if a in summa:
            return True
        else:
            return False


print(find_sum_of([1, 2, 3, 4], 8))
print(find_sum_of([1, 22, 11, 2, 14, 12, 10, 3], 33))
