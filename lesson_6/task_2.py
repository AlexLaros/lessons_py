import random
size = random.randint(3, 10)
lst = [random.randint(1, 50) for i in range(size)]
print(f"Создан список случайного размера от 3 до 10 и\nиз случайного набора чисел от 1 до 50:\n{lst}")
print("Элементы списка нумеруются начиная с НУЛЯ.")
k = 1
c = 6
lst.append("что-то")
print(lst)
lst = lst[:k] + lst[-1:] + lst[k:-1]
lst[k] = c
print(lst)



