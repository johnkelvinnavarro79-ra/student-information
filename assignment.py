import csv

students = {}
FILENAME = "students.csv"

# Function
def input_grades():
    """Loop asking for grades until 'done' is entered."""
    grades = []
    while True:
        g = input("Enter grade (or 'done' to finish): ").strip()
        if g.lower() == "done":
            break
        if g.isdigit():
            grades.append(int(g))
        else:
            print("Invalid input. Enter a number or 'done'.")
    return grades

def add_student(sid, name, age, grades):
    students[sid] = {"name": name, "age": age, "grades": grades}
    print(f" Added student: ({sid}, {name})")

def update_student(sid, name=None, age=None, grades=None):
    if sid in students:
        if name: students[sid]["name"] = name
        if age: students[sid]["age"] = age
        if grades is not None: students[sid]["grades"] = grades
        print(f" Updated {sid}")
    else:
        print(" Student not found.")

def delete_student(sid):
    if sid in students:
        del students[sid]
        print(f" Deleted {sid}")
    else:
        print(" Student not found.")

def display_students(from_file=False):
    data = students if not from_file else load_from_file(True)
    if not data:
        print("⚠ No students found.")
        return
    for sid, info in data.items():
        print(f"\nID: {sid}")
        print(f"Name: {info['name']}")
        print(f"Age: {info['age']}")
        print("Grades:", ", ".join(map(str, info['grades'])))

def save_to_file():
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        for sid, info in students.items():
            row = [sid, info["name"], info["age"]] + info["grades"]
            writer.writerow(row)
    print(" Data saved to file.")

def load_from_file(return_data=False):
    data = {}
    try:
        with open(FILENAME, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                sid, name, age, *grades = row
                data[sid] = {"name": name, "age": int(age), "grades": [int(g) for g in grades]}
        if not return_data:
            global students
            students = data
        print(" Data loaded from file.")
    except FileNotFoundError:
        print(" No file found.")
    return data

# main menu
def menu():
    while True:
        print("\n--- STUDENT MANAGEMENT ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Save to File")
        print("6. Load from File")
        print("0. Exit")

        choice = input("Choice: ").strip()

        if choice == "1":
            sid = input("ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            print("Enter grades one by one. Type 'done' when finished:")
            grades = input_grades()
            add_student(sid, name, age, grades)

        elif choice == "2":
            opt = input("Display from (M)emory or (F)ile? ").strip().lower()
            if opt == "m":
                display_students()
            elif opt == "f":
                display_students(True)

        elif choice == "3":
            sid = input("Student ID: ")
            name = input("New Name (Enter to skip): ") or None
            age_inp = input("New Age (Enter to skip): ")
            age = int(age_inp) if age_inp else None
            print("Enter new grades (or type 'done' immediately to skip):")
            grades = input_grades()
            grades = grades if grades else None
            update_student(sid, name, age, grades)

        elif choice == "4":
            delete_student(input("Student ID: "))

        elif choice == "5":
            save_to_file()

        elif choice == "6":
            load_from_file()

        elif choice == "0":
            print(" Goodbye!")
            break
        else:
            print("⚠ Invalid choice.")

# ---------------- RUN ---------------- #
if __name__ == "__main__":
    menu()
