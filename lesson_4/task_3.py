# Навание программы
print("Проверка числа на наличие соседних одинаковых цифр")

# Ввод числа
number = int(input("Введите натуральное число:"))
num_str = str(number)  # Преоброзование целочисленную переменную в строковую

# Вывод числа
print(f"Ваше число: {num_str}")

# Проверка "соседей" на равенство
i = 0
neighbor_count = 0
while len(num_str):
    if i == len(num_str)-1:
        break
    else:
        if num_str[i] == num_str[i+1]:
            neighbor_count += 1
    i += 1

# Вывод после проверки
print("Наличие одинаковых соседей: ", end=" ")
if neighbor_count > 1:
    print("Да.")
else:
    print("Нет.")
