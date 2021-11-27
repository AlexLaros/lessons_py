import random
# формирование числа, которое должен угадать пользователь
comp_num = random.randrange(1, 101)
print("""Компьютер загадал число от 1 до 100 включительно.
Угадайте это число. Количество попыток неограничено! """)

# функция ввода пользователем числа
def guess_the_num():
    attempt = 1
    while comp_num >= 0:
        user_num_str = (input("Введите число: "))
        if user_num_str.isdigit():
            user_num = int(user_num_str)
            if user_num > comp_num:
                attempt += 1
                print(f"Ваше число {user_num} > ? .")
                continue
            elif user_num < comp_num:
                attempt += 1
                print(f"Ваше число {user_num} < ?.")
                continue
            elif user_num == comp_num:
                print(f"Поздравляю вы угадали число - '{comp_num}' c {attempt} попытки!")
        else:
            attempt += 1
            print("Ошибка!")
            continue


guess_the_num()
