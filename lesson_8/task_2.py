import random
lst1 = [random.randrange(1, 10) for i in range(5)]
lst2 = [random.randrange(1, 10) for j in range(5)]
print(f"Даны два списка:\n{lst1}\n{lst2}\nНайдено "
      f"{len(set(lst1).intersection(set(lst2)))} общих элементов")
