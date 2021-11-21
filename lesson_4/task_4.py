# Ввод слов через пробел
words = input("Введите два слова через пробел:")

# проверка наличия пробела между слов
while len(words) > 0:
    if words.count(' ') == 0:
        words = input("Попробуйте ещё раз: ")
        continue
    else:
        break

# функция разварота слов
def reverse():
    words_list = words.split(" ")
    str1 = str(words_list[0])
    str2 = str(words_list[1])
    print(f"Дано:\n{str1.title() +' '+ str2.title()}")
    print(f"Вывод: \n{str1[::-1].title() + ' ' + str2[::-1].title()}")


reverse()
