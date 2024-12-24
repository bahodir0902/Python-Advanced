import typing
class University:
    def __init__(self, name):
        self.name = name
        self.students_numbers = []

    def __eq__(self, other: "University") -> bool:
        return len(self.students_numbers) == len(other.students_numbers)

    def __le__(self, other: "University") -> bool:
        return len(self.students_numbers) <= len(self.students_numbers)

    def __sub__(self, other: "University") -> int:
        return len(self.students_numbers) - len(other.students_numbers)

    def add_student(self, student: "Student") -> None:
        self.students_numbers.append(student)




class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades


u1 = University("TATU")
u2 = University("INHA")


s1 = Student("Student", 20, 3.4)
s2 = Student("Some student", 21, 4.2)
s3 = Student("ABC", 23, 2.5)

u2.add_student(s1)
print(u1 == u2)
print(u1 <= u2)
print(u2 - u1)
