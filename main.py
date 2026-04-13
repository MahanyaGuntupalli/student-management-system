FILE_NAME = "students.txt"

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(student + "\n")


students = load_students()


def add_student():
    name = input("Enter student name: ").strip().title()
    
    if name == "":
        print("Name cannot be empty!\n")
        return
    
    if name in students:
        print("Student already exists!\n")
    else:
        students.append(name)
        save_students(students)
        print(f"{name} added successfully!\n")


def view_students():
    if not students:
        print("No students found.\n")
    else:
        print("\n📋 Student List:")
        for i, student in enumerate(students, start=1):
            print(f"{i}. {student}")
        print()


def delete_student():
    name = input("Enter student name to delete: ").strip().title()
    
    if name in students:
        students.remove(name)
        save_students(students)
        print(f"{name} deleted successfully!\n")
    else:
        print("Student not found.\n")


def search_student():
    name = input("Enter student name to search: ").strip().title()
    
    if name in students:
        print(f"{name} found in records!\n")
    else:
        print("Student not found.\n")


def show_menu():
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        search_student()
    elif choice == "5":
        print("Thank you for using the system 🙌")
        break
    else:
        print("Invalid choice! Please enter 1-5.\n")