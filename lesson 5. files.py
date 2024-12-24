# class CustomFileOpener:
#     def __init__(self, filename, mode):
#         self.file = open(filename, mode)
#         self.mode = mode
#
#     def __enter__(self):
#         print(f"Context manager is loaded.")
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Context manager is closed")
#         if self.file:
#             self.file.close()
#         if exc_type:
#             print(f"Error! {exc_type}")
#
#         return True
#
#
# with CustomFileOpener("temp.txt", "w") as temp:
#     data = temp.read()
#     print(data)
#
# print(f"{1}+{1}={1 + 1}")

import csv
import os

data = [
    {"First_name": "Bahodir", "Last_name": "Valijonov", "age": "19", "course": "2", "faculty": "Computer_engineering"},
    {"First_name": "Xusan", "Last_name": "Xasan", "age": "42", "course": "63", "faculty": "Logistics"},
    {"First_name": "Aziz", "Last_name": "Valiyev", "age": "12", "course": "6", "faculty": "School"},
    {"First_name": "Anvar", "Last_name": "Aliyev", "age": "23", "course": "4", "faculty": "Other"}

]
with open("data.csv", "w", newline="") as file:
    header = ["First_name", "Last_name", "age", "course", "faculty"]
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)

choices = ["Print average marks on all subjects", "Print marks on specific subject",
           "Print average age of all students", "Add student", "Exit"]




def display() -> None:
    for i, item in enumerate(choices, 1):
        print(f"{i}. {item}")

def write_to_csv(data: list[tuple]) -> None:
    file_exists = os.path.isfile("students.csv")
    with open("students.csv", "a", newline="") as file:
        header = ["First name", "Last name", "age", "English mark", "Math mark"]
        writer = csv.DictWriter(file, fieldnames=header)
        if not file_exists:
            writer.writeheader()

        for item in data:
            writer.writerow({
                "First name": item[0],
                "Last name": item[1],
                "age": item[2],
                "English mark": item[3],
                "Math mark": item[4]
            })


def add_student() -> None:
    try:
        name: str = input("Enter student name: ")
        last_name: str = input("Enter student last name: ")
        age: int = int(input("Enter student age: "))
        english_mark: float = float(input("Enter student's english subject mark: "))
        math_mark: float = float(input("Enter student's math subject mark: "))
    except (ValueError, TypeError) as e:
        print(f"Error! {e}")
        return

    students = []
    students.append((name, last_name, age, english_mark, math_mark))

    write_to_csv(students)

def read_from_csv():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            content = [row for row in reader if any(row)]
            del content[0]
        return content
    except Exception as e:
        print(f"Error! {e}")
        return


def average_age():
    students = read_from_csv()
    total = 0
    for student in students:
        total += int(student[2])
    average = total / len(students)

    print(f"Average age of all student: {average}")


def specific_subject():
    students = read_from_csv()
    for student in students:
        print(f"{student[0]} {student[1]} english mark: {student[3]}, math mark: {student[4]}")


def average_mark():
    students = read_from_csv()
    english_total = 0
    math_total = 0
    for student in students:
        english_total += float(student[3])
        math_total += float(student[4])

    average_english = english_total // len(students)
    average_math = math_total // len(students)
    print(f"Average english mark {average_english}, math mark: {average_math}")

def main() -> None:
    while True:
        display()
        while True:
            try:
                choice = int(input(f"Qaysi amalni bajarasiz (1-{len(choices)}): "))
                if choice <= 0 or choice > len(choices):
                    raise ValueError(f"Enter a valid range {len(choices)}!")
                break
            except (TypeError, ValueError) as e:
                print(f"Error! {e}")

        if choice == 1:
            average_mark()
        elif choice == 2:
            specific_subject()
        elif choice == 3:
            average_age()
        elif choice == 4:
            add_student()
        elif choice == 5:
            break
        else:
            continue


main()
