#simple iterator class
# class MyIterator:
#     def __init__(self, start: int, end: int, step=1):
#         self.current = start
#         self.end = end
#           self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         if self.current >= self.end:
#             raise StopIteration("Sequence is end.")
#         if self.step == 1:
#             self.current += 1
#             return self.current - 1
#         else:
#             self.current += self.step
#             return self.current - self.step
#
#
#
# my_iter = MyIterator(0, 15)
#
# for i in my_iter:
#     print(i)

class MyInfinityIterator:
    def __init__(self, start: int, step=1):
        self.current = start
        self.step = step


    def __iter__(self):
        return self

    def __next__(self):
        if self.step == 1:
            self.current += 1
            return self.current - 1
        else:
            self.current += self.step
            return self.current - self.step

inf = MyInfinityIterator(1, 2)
# for i in inf:
#     print(i)

class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student: "Student"):
        if isinstance(student, Student):
            self.students.append(student)

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self) -> str:
        if self.current >= len(self.students):
            raise StopIteration("Iteration is end.")
        self.current += 1
        return self.students[self.current - 1].name


class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


student1 = Student("A", 32)
student2 = Student("B", 12)
student3 = Student("C", 54)
student4 = Student("D", 3)
student5 = Student("F", 43)

university = University("INHA")
university.add_student(student1)
university.add_student(student2)
university.add_student(student3)
university.add_student(student4)
university.add_student(student5)

for i in university:
    print(i)
print()
for i in university:
    print(i)

def test():
    pass

