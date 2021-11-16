# Задача 1
password_in = input("Введите пароль: ") # Ввод
# ожидаемые варианты пароля
password1 = "password123"
password2 = "пароль123"
# проверка пароля на совпадение
if password_in == password1 or password_in == password2 :
    print("Пароль совпал")
else:
    print("Пароль НЕ совпал")
