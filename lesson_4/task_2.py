# Условие ввода
print("!ВАЖНОЕ УСЛОВИЕ!:\nЧисло N должно быть не больше 10 миллионов")

# Ввод
n = int(input("Введите число N: "))

# функция поиска и вывода автоморфного числа
def auto_morph():
    print("Автоморфные числа: ")
    for i in range(1, n):
        if i ** 2 % 10 == i:
            print(f"{i} * {i} = {i ** 2}")
        elif i ** 2 % 100 == i:
            print(f"{i} * {i} = {i ** 2}")
        elif i ** 2 % 1_000 == i:
            print(f"{i} * {i} = {i ** 2}")
        elif i ** 2 % 10_000 == i:
            print(f"{i} * {i} = {i ** 2}")
        elif i ** 2 % 100_000 == i:
            print(f"{i} * {i} = {i ** 2}")
        elif i ** 2 % 1_000_000 == i:
            print(f"{i} * {i} = {i ** 2}")


# проверка введенного числа
if n <= 10_000_000:
    auto_morph()
else:
    print("Число превышает 10 миллионов")
