import sys


def display_menu():
    print("\nStudent Management System Menu:")
    print("1. View All Students")
    print("2. Add Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")


def view_students(students):
    if not students:
        print("\nNo students in the system.")
    else:
        print("\nList of Students:")
        for student_id, student_info in students.items():
            print(
                f"ID: {student_id}, Name: {student_info['name']}, Age: {student_info['age']}, Grade: {student_info['grade']}")


def add_student(students):
    student_id = input("\nEnter Student ID: ")
    if student_id in students:
        print("Student ID already exists.")
    else:
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        grade = input("Enter Student Grade: ")
        students[student_id] = {'name': name, 'age': age, 'grade': grade}
        print(f"Student {name} added successfully.")


def update_student(students):
    student_id = input("\nEnter Student ID to update: ")
    if student_id not in students:
        print("Student ID not found.")
    else:
        name = input("Enter new name (leave blank to keep current): ")
        age = input("Enter new age (leave blank to keep current): ")
        grade = input("Enter new grade (leave blank to keep current): ")

        if name:
            students[student_id]['name'] = name
        if age:
            students[student_id]['age'] = age
        if grade:
            students[student_id]['grade'] = grade

        print(f"Student ID {student_id} updated successfully.")


def delete_student(students):
    student_id = input("\nEnter Student ID to delete: ")
    if student_id not in students:
        print("Student ID not found.")
    else:
        del students[student_id]
        print(f"Student ID {student_id} deleted successfully.")


def main():
    students = {}

    while True:
        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == '1':
            view_students(students)
        elif choice == '2':
            add_student(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            print("Exiting the Student Management System. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
