class TriangleChecker:

    def __init__(self, num1, num2, num3):
        self.n1 = num1
        self.n2 = num2
        self.n3 = num3

    def is_triangle(self):
        if type(self.n1) is bool or type(self.n2) is bool or type(self.n3) is \
                bool:
            print("Нужно вводить только числа!")
        else:
            try:
                if self.n1 < 0 or self.n2 < 0 or self.n3 < 0:
                    print("С отрицательными числами ничего не выйдет!")
                elif self.n1 + self.n2 > self.n3 and self.n1 + self.n3 > self.n2 \
                        and self.n2 + self.n3 > self.n1:
                    print("Ура, можно построить треугольник!")
                else:
                    print("Жаль, но из этого треугольник не построить.")
            except TypeError:
                print("Нужно вводить только числа!")


triangle1 = TriangleChecker(3, 3, 4)
triangle1.is_triangle()
