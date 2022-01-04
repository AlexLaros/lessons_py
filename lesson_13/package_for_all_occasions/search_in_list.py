"""Search for what you need in the list
--------------------------------------------------------------------------------
Currently available search methods:
    - find_sum();
    - find_prime();
    - find_max_repeat_word().
--------------------------------------------------------------------------------
"""


def find_sum(lst: list, a: int) -> bool:
    """
    This function checks for the presence of a pair of numbers
    from the list 'lst', whose sum is equal to the number 'a'.
    """
    summa = []
    for i in lst:
        for j in lst:
            if j <= i:
                continue
            else:
                summa.append(i + j)
    for i in range(len(set(summa))):
        if a in summa:
            return True
        else:
            return False


def find_prime(a: int, b: int):
    """
    This generator function finds prime numbers in the specified range
     from 'a' to 'b'(not inclusive).
    """
    lst_nums = []
    lst_div = []
    # заполнение списка числами от a до b
    for j in range(a, b):
        lst_nums.append(j)
    # заполнение списка lst_div списками делителей каждого элемента lst_nums
    for j in range(len(lst_nums)):
        lst_div.append([])
    # нахождение длинны элементов списка lst_div
    for j in range(len(lst_div)):
        for k in range(1, lst_nums[j] + 1):
            if lst_nums[j] % k == 0:
                lst_div[j].append(k)
    # если длинна равна двум - число из списка lst_nums простое
    for j in range(len(lst_div)):
        if len(lst_div[j]) == 2:
            yield lst_nums[j]


def find_max_repeat_word(text: str):
    """
    This function can take large strings and as a result outputs the word
    that was most often repeated in this sentence.
    """
    print(f"Дан текст:\n{text}")
    # Разбиение строки на элементы списка
    words = text.split()
    # удаление знаков препинаний
    punc_signs = [",", ".", "!", "?", ":", ";", "-", " ", "—"]
    for i in range(len(words) - 1):
        for s in range(len(punc_signs)):
            if words[i] == punc_signs[s]:
                words.pop(i)
    for i in range(len(words)):
        for s in range(len(punc_signs)):
            if words[i][-1] == punc_signs[s] or words[i][0] == punc_signs[s]:
                words[i] = words[i].replace(punc_signs[s], '')

    # список, который будет хранит все элементы списка(т. е. слова)
    # в нижнем регистре
    words_low = []
    # приведенеие слов к нижнему регистру
    for i in range(len(words)):
        words_low.append(words[i].lower())

    # реализация заключительного функционала: поиска самого повторяющегося
    # (последнего, если их несколько) слова
    amount = []
    index = []

    # формирование переменной, хранящей максимальное кол-во повторений
    for i in words_low:
        amount.append(words_low.count(i))
    max_cnt = max(amount)

    # формирование переменной, хранящей индекс последнего максимального
    for i in range(len(words_low)):
        if words_low.count(words_low[i]) == max_cnt:
            index.append(i)
    max_ind = max(index)

    # формирования словаря, хранящего самое повторяющееся последнее слово
    dic_text = {}
    for k in range(len(words_low)):
        for v in range(len(amount)):
            if k == max_ind and v == max_cnt:
                dic_text[words_low[k]] = amount[v]
    for k in dic_text.keys():
        return f'Слово "{k}" повторяется чаще всего.'


if __name__ == "__main__":
    pass
