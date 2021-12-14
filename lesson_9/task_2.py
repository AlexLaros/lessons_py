# ввод количесвта в будущем обрабатываемых элементов
while 1 > 0:
    size = input("Введите количество обрабатываемых элементов: ")
    if size.isdigit():
        size = int(size)
        break
    else:
        print("Ошибка!")
        continue

lst1 = []
i = 0
# генерация списка пользователем в консоли
while size >= 0:
    k = input(f"Введите элемент №{i}: ")
    if k.isdigit():
        lst1.append(int(k))
        if len(lst1) == size:
            break
    else:
        print("Попробуйте ещё раз:")
        continue
    i += 1

print(f"Полученый список элементов:\n{lst1}")

# обработка элементов списка анонимной функцией
pov = list(map(lambda x, y=2: x ** y, lst1))
print(f"Результат обработки анонимной функцией:\n{pov}")
