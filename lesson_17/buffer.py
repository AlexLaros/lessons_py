import numpy as np


class Buffer:
    def __init__(self, sequences: list):
        self.sequences = sequences

    def _get_sum_of_five(self, lst):
        if len(lst) < 5:
            pass
        else:
            if len(lst) % 5 == 0:
                # подсчет суммы пяторк происходит с помощью методов модуля numpy
                # вкратце, разделение по индексам и подсчет
                a = np.add.reduceat(lst, np.arange(0, len(lst), 5))
                a = list(a)
                print('Cуммы группы "пятерок":')
                for i in a:
                    print(f"({i})", end=' ')
                print()
                lst.clear()
            else:
                a = np.add.reduceat(lst, np.arange(0, len(lst), 5))
                a = list(a)
                a.pop()
                length_a = len(a)
                del self.sequences[0:length_a * 5]
                print('Cуммы групп "пятерок":')
                for i in a:
                    print(f"({i})", end=' ')
                print()

    def add(self, *args: int):
        l = [*args]
        for i in range(len(l)):
            self.sequences.append(l[i])
        self._get_sum_of_five(self.sequences)

    def get_current_part(self, lst: list) -> str:
        if lst != []:
            return f"Cохраняемые в данный момент элементы " \
                   f"последовательностей:\n{self.sequences}"
        else:
            return "Cохраняемые в данный момент элементы " \
                   "последовательностей ОТСУТСТВУЮТ."


if __name__ == "__main__":
    s1 = Buffer([])
    s1.add(1, 2, 3)
    print(s1.get_current_part(s1.sequences))
    s1.add(4, 5, 6, 7, 8, 9, 10)
    print(s1.get_current_part(s1.sequences))
    s1.add(11, 12)
    print(s1.get_current_part(s1.sequences))
    s1.add(13, 14, 15)
    print(s1.get_current_part(s1.sequences))
