import random
lst = [random.randrange(1, 50) for i in range(10)]
print(f"Дан список:\n{lst}\nНайдено {len(set(lst))} различных чисел, "
      f"а именно:\n{set(lst)}")
