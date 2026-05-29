import json

students = []


# Load data from file
def load_from_file():
    global students

    try:
        with open("students.json", "r") as f:
            students = json.load(f)

    except:
        students = []


# Save data to file
def save_to_file():
    with open("students.json", "w") as f:
        json.dump(students, f)


# Add student
def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)

    save_to_file()

    print("Student added successfully!\n")


# View students
def view_students():

    if not students:
        print("No records found.\n")

    else:
        print("\n----- STUDENT RECORDS -----")

        for s in students:
            print("Name :", s["name"])
            print("Roll :", s["roll"])
            print("Marks:", s["marks"])
            print("---------------------------")

        print()


# Search student
def search_student():

    roll = input("Enter roll number: ")

    for s in students:

        if s["roll"] == roll:

            print("\nStudent Found")
            print("Name :", s["name"])
            print("Roll :", s["roll"])
            print("Marks:", s["marks"])
            print()

            return

    print("Student not found.\n")


# Delete student
def delete_student():

    roll = input("Enter roll number: ")

    for s in students:

        if s["roll"] == roll:

            students.remove(s)

            save_to_file()

            print("Student deleted successfully!\n")

            return

    print("Student not found.\n")


# Load existing data
load_from_file()


# Menu-driven program
while True:

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!\n")