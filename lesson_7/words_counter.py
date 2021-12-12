# Текстом является стихотворение И. Бродского "Письмо в Оазис"
text = """Не надо обо мне. Не надо ни о ком.
Заботься о себе, о всаднице матраца.
Я был не лишним ртом, но лишним языком,
подспудным грызуном словарного запаса. Теперь в твоих глазах амбарного кота,
хранившего зерно от порчи и урона,
читается печаль, дремавшая тогда,
когда за мной гналась секира фараона. С чего бы это вдруг? Серебряный висок?
Оскомина во рту от сладостей восточных?
Потусторонний звук? Но то шуршит песок,
пустыни талисман, в моих часах песочных. Помол его жесток, крупицы — тяжелы,
и кости в нем белей, чем просто перемыты.
Но лучше грызть его, чем губы от жары
облизывать тени осевшей пирамиды!"""

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
    print(words)


words_low = []
# функция приведения к нижнему регистру
def mk_low_reg():
    for i in range(len(words)):
        words_low.append(words[i].lower())

# функция подсчета слов
def count_words():
    amount = []
    
    for i in words_low:
        amount.append(words_low.count(i))
    max_cnt = max(amount)
    
    dic_text = dict(zip(words_low, amount))
    for k, v in dic_text.items():
        print(f'"{k}" - {v}')


del_punc_signs()
mk_low_reg()
count_words()
