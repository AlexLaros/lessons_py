def add_vars():
    a = input("Введите 1-е любое значение(число, строка и т. д.):")
    b = input("Введите 2-е любое значение(число, строка и т. д.):")
    try:
        a, b = int(a), int(b)
        return f"Результат соединения: {a + b}"
    except ValueError:
        a, b = str(a), str(b)
        return f"Результат соединения: {a + b}"


if __name__ == "__main__":
    print(add_vars())
