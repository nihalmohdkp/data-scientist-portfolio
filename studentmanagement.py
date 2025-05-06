class student :
    def __init__(self, student_id, name , age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def _init_(self):
        self.students = []

    def add_student(self):
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        student = student(student_id, name, age, grade)
        self.students.append(student)
        print("Student added successfully!\n")

    def display_students(self):
        if not self.students:
            print("No students found.\n")
        else:
            print("List of Students:")
            for student in self.students:
                print(student)
            print()
