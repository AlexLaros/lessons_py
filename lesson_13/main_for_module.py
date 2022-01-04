from random import randrange
import sorting as sort
lst = [randrange(30) for i in range(10)]
print(lst)
print(sort.bubble(lst))
print(sort.choice(lst))
print(sort.insert(lst))
print(sort.quick(lst))
