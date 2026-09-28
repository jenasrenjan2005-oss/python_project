
import hashlib
import sqlite3
from pathlib import Path

DATABASE = Path(__file__).with_name("students.db")


def connect():
    """Connect to the database and turn on foreign-key checks."""
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    return db


def make_password(password):
    """Save a one-way digest instead of the original password."""
    return hashlib.sha256(password.encode()).hexdigest()


def setup_database():
    """Create the two related tables and a sample administrator."""
    with connect() as db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('admin', 'staff'))
            );
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL CHECK(age BETWEEN 5 AND 100),
                course TEXT NOT NULL,
                added_by INTEGER NOT NULL REFERENCES users(id)
            );
        """)
        if not db.execute("SELECT id FROM users WHERE username='admin'").fetchone():
            db.execute("INSERT INTO users(username,password,role) VALUES(?,?,?)",
                       ("admin", make_password("admin123"), "admin"))
        # Add example students only when the table is empty.
        if not db.execute("SELECT id FROM students LIMIT 1").fetchone():
            admin_id = db.execute("SELECT id FROM users WHERE username='admin'").fetchone()["id"]
            db.executemany("INSERT INTO students(name,age,course,added_by) VALUES(?,?,?,?)", [
                ("Asha Patel", 19, "Computer Science", admin_id),
                ("Ravi Kumar", 20, "Mathematics", admin_id),
            ])


def ask(prompt):
    """Keep asking until the user enters something."""
    while True:
        answer = input(prompt).strip()
        if answer:
            return answer
        print("Please enter a value.")


def ask_age(prompt, old_age=None):
    while True:
        text = input(prompt).strip()
        if not text and old_age is not None:
            return old_age
        try:
            age = int(text)
            if 5 <= age <= 100:
                return age
        except ValueError:
            pass
        print("Enter a whole number between 5 and 100.")


def register():
    print("\nCreate a staff account")
    username = ask("Choose a username: ")
    password = ask("Choose a password: ")
    try:
        with connect() as db:
            db.execute("INSERT INTO users(username,password,role) VALUES(?,?, 'staff')",
                       (username, make_password(password)))
        print("Staff account created. You can now log in.")
    except sqlite3.IntegrityError:
        print("That username is already used.")


def login():
    username = ask("Username: ")
    password = ask("Password: ")
    with connect() as db:
        return db.execute("SELECT * FROM users WHERE username=? AND password=?",
                           (username, make_password(password))).fetchone()


def list_students():
    with connect() as db:
        students = db.execute("SELECT id,name,age,course FROM students ORDER BY id").fetchall()
    print("\nID  NAME                 AGE  COURSE")
    print("-" * 50)
    if not students:
        print("No student records yet.")
    for student in students:
        print(f"{student['id']:<3} {student['name']:<20} {student['age']:<4} {student['course']}")


def add_student(user_id):
    name = ask("Student name: ")
    age = ask_age("Student age: ")
    course = ask("Course: ")
    with connect() as db:
        db.execute("INSERT INTO students(name,age,course,added_by) VALUES(?,?,?,?)",
                   (name, age, course, user_id))
    print("Student added.")


def update_student():
    list_students()
    try:
        student_id = int(ask("ID to edit: "))
    except ValueError:
        print("ID must be a number.")
        return
    with connect() as db:
        student = db.execute("SELECT * FROM students WHERE id=?", (student_id,)).fetchone()
        if not student:
            print("Student ID not found.")
            return
        name = input(f"Name [{student['name']}]: ").strip() or student["name"]
        age = ask_age(f"Age [{student['age']}]: ", student["age"])
        course = input(f"Course [{student['course']}]: ").strip() or student["course"]
        db.execute("UPDATE students SET name=?,age=?,course=? WHERE id=?",
                   (name, age, course, student_id))
    print("Student updated.")


def delete_student():
    list_students()
    try:
        student_id = int(ask("ID to delete: "))
    except ValueError:
        print("ID must be a number.")
        return
    with connect() as db:
        cursor = db.execute("DELETE FROM students WHERE id=?", (student_id,))
    if cursor.rowcount:
        print("Student deleted.")
    else:
        print("Student ID not found.")


def user_menu(user):
    while True:
        print(f"\n--- {user['role'].upper()} MENU ---")
        print("1. View students\n2. Add student\n3. Edit student")
        if user["role"] == "admin":
            print("4. Delete student")
        print("L. Log out\n0. Exit")
        choice = input("Choose: ").strip().lower()
        try:
            if choice == "1":
                list_students()
            elif choice == "2":
                add_student(user["id"])
            elif choice == "3":
                update_student()
            elif choice == "4" and user["role"] == "admin":
                delete_student()
            elif choice == "l":
                print("Logged out.")
                return True
            elif choice == "0":
                return False
            else:
                print("Choose one of the menu options.")
        except sqlite3.Error as error:
            print("Database problem:", error)


def main():
    setup_database()
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Log in\n2. Register as staff\n0. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            user = login()
            if user:
                print("Welcome!")
                if not user_menu(user):
                    break
            else:
                print("Username or password is incorrect.")
        elif choice == "2":
            register()
        elif choice == "0":
            break
        else:
            print("Please choose 1, 2, or 0.")
    print("Goodbye!")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
