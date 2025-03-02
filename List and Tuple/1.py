import csv
import os

students = []
filename = "students.csv"

def load_file():
    global students
    if os.path.exists(filename):
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            students = [tuple(row) for row in reader]
        print("\nFile loaded successfully!")
    else:
        print("\nFile not found!")

def save_file():
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(students)
    print("\nFile saved successfully!")

def save_as_file():
    new_filename = input("Enter new filename: ")
    with open(new_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(students)
    print("\nFile saved as", new_filename)

def show_all_records():
    if not students:
        print("\nNo student records available.")
        return
    print("\nAll Student Records:")
    for student in students:
        print(student)

def order_by_last_name():
    sorted_students = sorted(students, key=lambda x: x[1].split()[-1])
    print("\nStudents Ordered by Last Name:")
    for student in sorted_students:
        print(student)

def order_by_grade():
    sorted_students = sorted(students, key=lambda x: (0.6 * float(x[2]) + 0.4 * float(x[3])), reverse=True)
    print("\nStudents Ordered by Computed Grade (60% Class Standing + 40% Major Exam):")
    for student in sorted_students:
        print(student)

def show_student_record():
    search_id = input("Enter Student ID: ")
    for student in students:
        if student[0] == search_id:
            print("\nStudent Found:", student)
            return
    print("\nStudent not found!")

def add_record():
    student_id = input("Enter Student ID (6 digits): ")
    full_name = input("Enter Full Name (First Last): ")
    class_standing = input("Enter Class Standing Grade: ")
    major_exam = input("Enter Major Exam Grade: ")

    if not student_id.isdigit() or len(student_id) != 6:
        print("\nInvalid Student ID! Must be 6 digits.")
        return
    
    students.append((student_id, full_name, class_standing, major_exam))
    print("\nRecord added successfully!")

def edit_record():
    search_id = input("Enter Student ID to edit: ")
    for i, student in enumerate(students):
        if student[0] == search_id:
            print("\nEditing Record:", student)
            new_name = input("Enter New Full Name: ")
            new_class_standing = input("Enter New Class Standing Grade: ")
            new_major_exam = input("Enter New Major Exam Grade: ")

            students[i] = (search_id, new_name, new_class_standing, new_major_exam)
            print("\nRecord updated successfully!")
            return
    print("\nStudent not found!")

def delete_record():
    search_id = input("Enter Student ID to delete: ")
    global students
    students = [student for student in students if student[0] != search_id]
    print("\nRecord deleted successfully!")

def main():
    while True:
        print("\nStudent Record Management System")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            load_file()
        elif choice == "2":
            save_file()
        elif choice == "3":
            save_as_file()
        elif choice == "4":
            show_all_records()
        elif choice == "5":
            order_by_last_name()
        elif choice == "6":
            order_by_grade()
        elif choice == "7":
            show_student_record()
        elif choice == "8":
            add_record()
        elif choice == "9":
            edit_record()
        elif choice == "10":
            delete_record()
        elif choice == "11":
            print("\nExiting Program...")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
