

import json
import os

file_name = "student_data.json"

def load_data():
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(file_name, "w") as f:
        json.dump(data, f)

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    class_name = input("Enter class: ")
    marks = input("Enter marks: ")
    students = load_data()
    students.append({"name": name, "roll": roll, "class": class_name, "marks": marks})
    save_data(students)
    print("Student added successfully.")

def display_students():
    students = load_data()
    if not students:
        print("No student records found.")
    else:
        for s in students:
            print(f"Name: {s['name']}, Roll: {s['roll']}, Class: {s['class']}, Marks: {s['marks']}")

def search_student():
    roll = input("Enter roll number to search: ")
    students = load_data()
    for s in students:
        if s['roll'] == roll:
            print(f"Found: Name: {s['name']}, Class: {s['class']}, Marks: {s['marks']}")
            return
    print("Student not found.")

def update_student():
    roll = input("Enter roll number to update: ")
    students = load_data()
    for s in students:
        if s['roll'] == roll:
            s['name'] = input("Enter new name: ")
            s['class'] = input("Enter new class: ")
            s['marks'] = input("Enter new marks: ")
            save_data(students)
            print("Student updated.")
            return
    print("Student not found.")

def delete_student():
    roll = input("Enter roll number to delete: ")
    students = load_data()
    new_list = [s for s in students if s['roll'] != roll]
    if len(new_list) == len(students):
        print("Student not found.")
    else:
        save_data(new_list)
        print("Student deleted.")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
