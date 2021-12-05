import random

# Генерация списков
lst1 = [random.randint(1, 10) for i in range(5)]
lst2 = [random.randint(1, 10) for j in range(5)]
print(f"Даны два списка:\n{lst1}\n{lst2}.")
lst1 += lst2
# функция поиска и вывода уникальных элементов среди двух списков
print(f"Количество уникальных элементов:\n"
      f"{len([lst1.append(i) for i in range(len(lst1) + 1) if lst1.count(i) == 1])}"
      )
