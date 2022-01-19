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
        # Увеличение на 1 только при условии,
        # если счетчик не равен max
        if self.counter < self.max:
            self.counter += 1
            print(f"Counter increased to {self.counter}.")
        else:
            print("---Counter value is out of range!---")
        pass

    def show_counter_value(self):
        print(f"Counter value:\n{self.counter}")


    def reset_to_min(self):
        self.counter = self.min
        print("Counter value is minimized.")

# Создаем экземпляр класса
c1 = DigitalCounter(1, 5)
# смотрим значение
c1.show_counter_value()
# проверка метода увеличения,
# чтобы значение счетчика не увеличивалось
# при достижении максимума
c1.increase_and_show()
c1.increase_and_show()
c1.increase_and_show()
c1.increase_and_show()
c1.increase_and_show()
c1.increase_and_show()
# Смотрим значение счетчика
c1.show_counter_value()
# Проверка метода сброса до минимума
c1.reset_to_min()
# Смотрим значение счетчика после сброса
c1.show_counter_value()
