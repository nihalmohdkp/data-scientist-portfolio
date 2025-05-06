class Student:
    def _init_(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

        def _str_(self):
            return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentManagementSystem:
    def _init_(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        student = Student(student_id, name, age, grade)
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

    def edit_student(self):
        student_id = input("Enter student ID to edit: ")
        for student in self.students:
            if student.student_id == student_id:
                print("Editing student details...")
                student.name = input("Enter new name: ")
                student.age = input("Enter new age: ")
                student.grade = input("Enter new grade: ")
                print("Student details updated successfully!\n")
                return
        print("Student not found!\n")
    def delete_student(self):
        student_id = input("Enter student ID to delete: ")
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student deleted successfully!\n")
                return
        print("Student not found!\n")

    def run(self):
        while True:
            print("1. Add Student")
            print("2. Display All Students")
            print("3. Edit Student")
            print("4. Delete Student")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.display_students()
            elif choice == "3":
                self.edit_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.\n")


# Main program execution
if name == "_main_":
    system = StudentManagementSystem()
system.run()