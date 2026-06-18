"""
Student Enrollment Manager
Week 2 Project - Supports add, query, and delete operations
"""

from datetime import date

# Dictionary to store students: {student_id: {name, email, join_date}}
students = {}
next_id = 1


def add_student():
    print("\n--- Add Student ---")
    name = input("Enter name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return

    email = input("Enter email: ").strip()
    if not email or "@" not in email:
        print("❌ Please enter a valid email address.")
        return

    # Check for duplicate email
    for s in students.values():
        if s["email"].lower() == email.lower():
            print(f"❌ A student with email '{email}' already exists.")
            return

    global next_id
    students[next_id] = {
        "name": name,
        "email": email,
        "join_date": str(date.today())
    }
    print(f"✅ Student added successfully! (ID: {next_id})")
    next_id += 1


def query_student():
    print("\n--- Query Student ---")
    if not students:
        print("No students enrolled yet.")
        return

    keyword = input("Enter name or email to search: ").strip().lower()
    if not keyword:
        print("❌ Search keyword cannot be empty.")
        return

    results = [
        (sid, s) for sid, s in students.items()
        if keyword in s["name"].lower() or keyword in s["email"].lower()
    ]

    if not results:
        print(f"No students found matching '{keyword}'.")
    else:
        print(f"\nFound {len(results)} result(s):")
        print(f"{'ID':<5} {'Name':<20} {'Email':<30} {'Join Date'}")
        print("-" * 65)
        for sid, s in results:
            print(f"{sid:<5} {s['name']:<20} {s['email']:<30} {s['join_date']}")


def list_all():
    print("\n--- All Students ---")
    if not students:
        print("No students enrolled yet.")
        return

    print(f"{'ID':<5} {'Name':<20} {'Email':<30} {'Join Date'}")
    print("-" * 65)
    for sid, s in students.items():
        print(f"{sid:<5} {s['name']:<20} {s['email']:<30} {s['join_date']}")
    print(f"\nTotal: {len(students)} student(s)")


def delete_student():
    print("\n--- Delete Student ---")
    if not students:
        print("No students enrolled yet.")
        return

    try:
        sid = int(input("Enter student ID to delete: ").strip())
    except ValueError:
        print("❌ Please enter a valid numeric ID.")
        return

    if sid not in students:
        print(f"❌ No student found with ID {sid}.")
        return

    name = students[sid]["name"]
    confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        del students[sid]
        print(f"✅ Student '{name}' deleted successfully.")
    else:
        print("Deletion cancelled.")


def main():
    print("=" * 40)
    print("  Student Enrollment Manager")
    print("=" * 40)

    menu = {
        "1": ("Add student", add_student),
        "2": ("Query student", query_student),
        "3": ("List all students", list_all),
        "4": ("Delete student", delete_student),
        "5": ("Exit", None),
    }

    while True:
        print("\nMenu:")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        elif choice in menu:
            _, action = menu[choice]
            action()
        else:
            print("❌ Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()
