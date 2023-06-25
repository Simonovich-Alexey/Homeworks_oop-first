class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades_from_students:
                lector.grades_from_students[course] += [grade]
            else:
                lector.grades_from_students[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __int__(self):
        self.grades_from_students = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python', 'Java']

print(some_lecturer.courses_attached)
print(some_student.courses_in_progress)
print(some_reviewer.courses_attached)
