str1 = input("Введите строку(Минимум 3 символа): ")

# проверка минимального ввода: от 3 символов
while len(str1) >= 0:
    if len(str1) >= 3 and len(str1) != 0:
        break
    else:
        str1 = input("Введите строку из 3 и больше символов:")
        continue

char = input("Введите один символ:")

# проверка ввода только одного символа
while len(char) >= 0:
    if len(char) != 1:
        char = input("Введите только один символ:")
        continue
    else:
        break

# функция поиска введнного символа в введенной строке
count = 0
start = -1
while len(str1) > 0:
    start = str1.find(char, start+1)
    if start == -1:
        break
    count += 1

print("Количество найденных символов:", count)
