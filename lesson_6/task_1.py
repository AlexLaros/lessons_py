import random

size = random.randint(3, 10)
lst = [random.randint(1, 50) for i in range(size)]

print(f"Создан список случайного размера от 3 до 10 и\nиз случайного набора чисел от 1 до 50:\n{lst}")
print("Элементы списка нумеруются начиная с НУЛЯ.")
k = int(input("Введите номер элемента, который хотите удалить:\n"))

# функция сдвига элемента под номер k  конец списка
def shift_and_del():
    count = 0
    global k
    while k < len(lst)-1:
        lst[k + 1], lst[k] = lst[k], lst[k + 1]
        k += 1
        count += 1
    print(f"Переносим элемент с номером {k-count} в конец списка:\n{lst}")
    lst.pop()
    print(f"После чего удаляем его.\nРезультат:\n{lst}")


# проверка местонахождения числа с индексом k
if k > len(lst)-1:
    print(f"ОШИБКА!\nЧисло с индексом {k} не найдено!")
elif k == len(lst) - 1:
    print(f"ОШИБКА!\nЧисло c индексом {k} находится в конце списка")
else:
    shift_and_del()

