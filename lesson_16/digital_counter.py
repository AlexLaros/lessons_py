class DigitalCounter:
    # параметр хранящий значение счетчика
    counter = 0

    def __init__(self, min, max):
        # границы
        self.min = min
        self.max = max
        # При вводе min счетчик автоматом будет равен ему
        self.counter = min

    def increase_and_show(self):
        # Увеличение на 1 тоько при условии,
        # если счетчик не равен max
        if self.counter < self.max:
            self.counter += 1
            return f"Counter increased to {self.counter}."
        else:
            return "---Counter value is out of range!---"
        pass

    def show_counter_value(self):
        return f"Counter value:\n{self.counter}"


    def reset_to_min(self):
        self.counter = self.min
        return "Counter value is minimized."

# Создаем экземпляр класса
c1 = DigitalCounter(1, 5)
# смотрим значение
print(c1.show_counter_value())
# проверка метода увеличения,
# чтобы значение счетчика не увеличивалось
# при достижении максимума
print(c1.increase_and_show())
print(c1.increase_and_show())
print(c1.increase_and_show())
print(c1.increase_and_show())
print(c1.increase_and_show())
print(c1.increase_and_show())
# Смотрим значение счетчика
print(c1.show_counter_value())
# Проверка метода сброса до минимума
c1.reset_to_min()
# Смотрим значение счетчика после сброса
print(c1.show_counter_value())
