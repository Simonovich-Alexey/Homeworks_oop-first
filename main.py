class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress \
                and 0 <= grade <= 10:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            raise TypeError('Ошибка ввода данных!')

    @classmethod
    def __calc_average(cls, grades):
        count = []
        for value in grades.values():
            for i in value:
                count.append(i)
        count = sum(count) / len(count)
        return round(count, 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Сравнивать друг с другом, можно только студентов!')
        return self.__calc_average(self.grades) < other.__calc_average(other.grades)

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\n" \
              f"Средняя оценка за домашние задания: {self.__calc_average(self.grades)}\n" \
              f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
              f"Завершенные курсы: {', '.join(self.finished_courses)}\n"
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    @classmethod
    def __calc_average(cls, grades):
        count = []
        for value in grades.values():
            for i in value:
                count.append(i)
        count = sum(count) / len(count)
        return round(count, 1)

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за лекции: {self.__calc_average(self.grades)}\n"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Сравнивать друг с другом, можно только лекторов!')

        return self.__calc_average(self.grades) < other.__calc_average(other.grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            raise TypeError('Ошибка ввода данных!')

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n"
        return res


some_lecturer_1 = Lecturer('Some', 'Buddy')
some_lecturer_1.courses_attached += ['Python']
some_lecturer_2 = Lecturer('Some_2', 'Buddy_2')
some_lecturer_2.courses_attached += ['Python']

some_student_1 = Student('Bill', 'Gates')
some_student_1.courses_in_progress += ['Python']
some_student_1.finished_courses += ['Введение в программирование']
some_student_1.rate_lecture(some_lecturer_1, 'Python', 9.5)
some_student_1.rate_lecture(some_lecturer_1, 'Python', 10)
some_student_1.rate_lecture(some_lecturer_1, 'Python', 8)
some_student_2 = Student('Steve', 'Jobs')
some_student_2.courses_in_progress += ['Python']
some_student_2.finished_courses += ['Введение в программирование', 'Git']
some_student_2.rate_lecture(some_lecturer_2, 'Python', 10)
some_student_2.rate_lecture(some_lecturer_2, 'Python', 5)
some_student_2.rate_lecture(some_lecturer_2, 'Python', 9)

some_reviewer_1 = Reviewer('Some', 'Buddy')
some_reviewer_1.courses_attached += ['Python']
some_reviewer_1.rate_hw(some_student_1, 'Python', 10)
some_reviewer_1.rate_hw(some_student_1, 'Python', 8)
some_reviewer_1.rate_hw(some_student_1, 'Python', 7)
some_reviewer_2 = Reviewer('Some_2', 'Buddy_2')
some_reviewer_2.courses_attached += ['Python']
some_reviewer_2.rate_hw(some_student_2, 'Python', 8)
some_reviewer_2.rate_hw(some_student_2, 'Python', 7)
some_reviewer_2.rate_hw(some_student_2, 'Python', 9)


print(some_lecturer_1)
print(some_lecturer_2)
print(some_student_1)
print(some_student_2)
print(some_lecturer_1 > some_lecturer_2)
print(some_student_1 < some_student_2)


def calculating_average_score(list_st, courses):
    all_grades = []
    for i in list_st:
        if i.grades.get(courses):
            for value in i.grades[courses]:
                all_grades.append(value)
        else:
            continue

    if len(all_grades) != 0:
        aver_sc_course = sum(all_grades) / len(all_grades)
        return round(aver_sc_course, 1)
    else:
        return f'Нет оценок по этому курсу'


students = [some_student_1, some_student_2]
lecturer = [some_lecturer_1, some_lecturer_2]

print(calculating_average_score(students, 'Java'))
print(calculating_average_score(lecturer, 'Python'))
