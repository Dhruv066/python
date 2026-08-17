import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

# Functions
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                   (name, age, course))
    conn.commit()
    print("✅ Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if len(records) == 0:
        print("No records found!")
    else:
        print("\nID | Name | Age | Course")
        print("-" * 30)
        for row in records:
            print(row)

def update_student():
    student_id = int(input("Enter student ID to update: "))

    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")

    cursor.execute("""
    UPDATE students
    SET name=?, age=?, course=?
    WHERE id=?
    """, (name, age, course, student_id))

    conn.commit()
    print("✅ Student updated!")

def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

    print("✅ Student deleted!")

# Menu-driven program
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("❌ Invalid choice!")

# Close connection
conn.close()