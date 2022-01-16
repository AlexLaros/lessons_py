def the_longest_words(file):
    """
    Данная функция выводит самое длинное слово из текста,
    который храниться в файле. Функция закрывает файл.
    :return: str
    """
    longest_words_lst = []
    words = file.read()
    lst_words = words.split()
    max_len = len(max(lst_words, key=len))

    for i in range(len(lst_words)):
        if len(lst_words[i]) == max_len:
            longest_words_lst.append(lst_words[i])

    if len(longest_words_lst) == 1:
        for i in longest_words_lst:
            print(i)
    elif len(longest_words_lst) > 1:
        print(longest_words_lst)

    file.close()


if __name__ == "__main__":
    file1 = open("article.txt", encoding="utf_8")
    the_longest_words(file1)
