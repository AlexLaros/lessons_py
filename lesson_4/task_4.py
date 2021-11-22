# Ввод слов через пробел
words = input("Введите два слова через пробел:")

# функция разворота
def reverse():
    if point == 1:
        word1 = words_list[0]
        word2 = words_list[1]
        print(f"Дано:\n{word1 + ' ' + word2}")
        print(f"Вывод: \n{word1[::-1].title() + ' ' + word2[::-1].title()}")
    elif point == 2:
        word1 = no_spaces_words_list[0]
        word2 = no_spaces_words_list[1]
        print(f"Дано:\n{word1 +' '+ word2}")
        print(f"Вывод: \n{word1[::-1].title() + ' ' + word2[::-1].title()}")


# проверка наличия двух слов
while len(words) > 0:
    if words.count(" ") == 0:
        words = input("Попробуйте ещё раз: ")
        continue
    else:
        words_list = words.split(" ", maxsplit= -1)
        if words_list.count("") == 0:
            if len(words_list) == 2:
                if len(words_list[0]) == 1 and len(words_list[1]) == 1:
                    words = input("Попробуйте ещё раз: ")
                    continue
                else:
                    point = 1
                    reverse()
                    break
            else:
                words = input("Попробуйте ещё раз: ")
                continue
        else:
            no_spaces_words_list = []
            no_spaces_words_list = " ".join(words_list).split()
            if len(no_spaces_words_list) == 2:
                if len(no_spaces_words_list[0]) == 1 and len(no_spaces_words_list[1]) == 1:
                    words = input("Попробуйте ещё раз: ")
                    continue
                else:
                    point = 2
                    reverse()
                    break
            else:
                words = input("Попробуйте ещё раз: ")
                continue
    break
