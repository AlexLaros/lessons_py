size_str = (input("Введите число от 3 до 9: "))


# функция построения треугольника(пирамиды) чисел
def nums_triangle():
    for i in range(1, size + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()


# Проверка введеного значения
if size_str.isdigit():
    size = int(size_str)
    if 3 <= size <= 9:
        nums_triangle()
    else:
        print("Число введено НЕ верно!")
else:
    print("Ошибка!")
