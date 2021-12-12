# Создание текста
text = """Стоишь на берегу и чувствуешь соленый запах ветра, что веет с моря,
и веришь, что свободен ты и жизнь лишь началась, и губы жжет подруги поцелуй,
пропитанный слезой!"""
print(f"Дан текст:\n{text}")
# Разбиение строки на элементы списка
words = text.split()


# функция удаления знаков препинания
def del_punc_signs():
    punc_signs = [",", ".", "!", "?", ":", ";", "-", " ", "—"]
    for i in range(len(words) - 1):
        for s in range(len(punc_signs)):
            if words[i] == punc_signs[s]:
                words.pop(i)
    for i in range(len(words)):
        for s in range(len(punc_signs)):
            if words[i][-1] == punc_signs[s] or words[i][0] == punc_signs[s]:
                words[i] = words[i].replace(punc_signs[s], '')


words_low = []


# функция приведения к нижнему регистру
def mk_low_reg():
    for i in range(len(words)):
        words_low.append(words[i].lower())


# функция поиска самого повторяющегося (последнего, если их несколько) слова
def find_max_repeat_word():
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
        print(f'Слово "{k}" повторяется чаще всего.')


del_punc_signs()
mk_low_reg()
find_max_repeat_word()
