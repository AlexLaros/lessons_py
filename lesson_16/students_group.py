class Student:
    name = ''
    age = 0
    sex = ''
    semester = 0
    grades = []


class Group:
    # Создание студентов
    s1 = Student()
    s1.name = "Ivan"
    s1.age = 23
    s1.sex = 'male'
    s1.semester = 3
    s1.grades = [4, 4, 5, 5]

    s2 = Student()
    s2.name = "Margaret"
    s2.age = 22
    s2.sex = 'female'
    s2.semester = 3
    s2.grades = [3, 4, 5, 2]

    s3 = Student()
    s3.name = "Peter"
    s3.age = 21
    s3.sex = 'male'
    s3.semester = 3
    s3.grades = [2, 3, 3, 2]

    s4 = Student()
    s4.name = "Jessica"
    s4.age = 22
    s4.sex = "female"
    s4.semester = 3
    s4.grades = [5, 5, 5, 5]
    # Заносим их в список
    students = [s1, s2, s3, s4]
    num_of_students = len(students)

    def __init__(self, group_name):
        self.group_name = group_name

    def show_names_and_marks(self, group):
        print(f"Группе {self.group_name} (Численность:"
              f" {self.num_of_students}):")
        for i in range(len(group)):
            if group[i].sex == 'male':
                print(f"Оценки студента {group[i].name}: {group[i].grades}")
            else:
                print(f"Оценки студентки {group[i].name}: {group[i].grades}")


g1 = Group('A1')
g1.show_names_and_marks(g1.students)
