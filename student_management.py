students = []

def add_student():
    name = input("Enter student name: ")
    matric = input("Enter matric number: ")
    score = input("Enter score: ")

    student = {
        "name": name,
        "matric": matric,
        "score": score
    }

    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No records found.\n")
        return

    for student in students:
        print("Name:", student["name"])
        print("Matric:", student["matric"])
        print("Score:", student["score"])
        print("------------------")

def save_records():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"{student['name']}, {student['matric']}, {student['score']}\n")
    print("Records saved successfully.\n")

while True:
    print("STUDENT RECORD MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Students")
    print("3. Save Records")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        save_records()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.\n")


