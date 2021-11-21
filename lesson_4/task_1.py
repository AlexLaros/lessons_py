# Навание программы
print("Проверка числа на наличие одинаковых цифр")

# Ввод числа
number = int(input("Введите натуральное число:"))

# Вывод введнного числа
print(f"Ваше число: {number}")
# Преоброзование целочисленной переменной в строкковую
num_str = str(number)

# Проверка наличия одинаковых цифр с числе
i = 0
num = 0
while i < len(num_str):
    count = num_str.count(num_str[i], 0, len(num_str))
    if count > 1:
        num = count
    i += 1

# Вывод после проверки
print("Наличие одинаковых цифр:", end=" ")
if num > 1:
    print("Да.")
else:
    print("Нет.")
