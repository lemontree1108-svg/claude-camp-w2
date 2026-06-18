"""
To-Do List Manager (with file saving)
Week 2 Project - Data persists to todos.json between sessions
"""

import json
import os

FILE = "todos.json"


# ---------- File I/O ----------

def load_todos():
    """Load todos from file. Returns empty list if file doesn't exist."""
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"⚠️  '{FILE}' was corrupted. Starting with an empty list.")
        return []


def save_todos(todos):
    """Save todos list to JSON file."""
    try:
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(todos, f, indent=2, ensure_ascii=False)
    except OSError as e:
        print(f"❌ Could not save to '{FILE}': {e}")


# ---------- Operations ----------

def add_todo(todos):
    print("\n--- Add Todo ---")
    task = input("Enter task: ").strip()
    if not task:
        print("❌ Task cannot be empty.")
        return

    todo = {"id": _next_id(todos), "task": task, "done": False}
    todos.append(todo)
    save_todos(todos)
    print(f"✅ Added: \"{task}\"")


def view_todos(todos):
    print("\n--- To-Do List ---")
    if not todos:
        print("No tasks yet. Add one!")
        return

    pending = [t for t in todos if not t["done"]]
    done    = [t for t in todos if t["done"]]

    if pending:
        print("\n📋 Pending:")
        for t in pending:
            print(f"  [{t['id']}] {t['task']}")

    if done:
        print("\n✅ Completed:")
        for t in done:
            print(f"  [{t['id']}] {t['task']}")

    print(f"\n{len(pending)} pending  |  {len(done)} completed  |  {len(todos)} total")


def complete_todo(todos):
    print("\n--- Complete Todo ---")
    pending = [t for t in todos if not t["done"]]
    if not pending:
        print("No pending tasks.")
        return

    print("Pending tasks:")
    for t in pending:
        print(f"  [{t['id']}] {t['task']}")

    try:
        tid = int(input("\nEnter task ID to mark complete: ").strip())
    except ValueError:
        print("❌ Please enter a valid numeric ID.")
        return

    for t in todos:
        if t["id"] == tid:
            if t["done"]:
                print(f"⚠️  Task [{tid}] is already completed.")
            else:
                t["done"] = True
                save_todos(todos)
                print(f"✅ Marked as done: \"{t['task']}\"")
            return

    print(f"❌ No task found with ID {tid}.")


def delete_todo(todos):
    print("\n--- Delete Todo ---")
    if not todos:
        print("No tasks to delete.")
        return

    view_todos(todos)

    try:
        tid = int(input("\nEnter task ID to delete: ").strip())
    except ValueError:
        print("❌ Please enter a valid numeric ID.")
        return

    for i, t in enumerate(todos):
        if t["id"] == tid:
            confirm = input(f"Delete \"{t['task']}\"? (yes/no): ").strip().lower()
            if confirm == "yes":
                todos.pop(i)
                save_todos(todos)
                print("✅ Task deleted.")
            else:
                print("Deletion cancelled.")
            return

    print(f"❌ No task found with ID {tid}.")


# ---------- Helper ----------

def _next_id(todos):
    return max((t["id"] for t in todos), default=0) + 1


# ---------- Main ----------

def main():
    print("=" * 40)
    print("      To-Do List Manager")
    print("=" * 40)

    todos = load_todos()
    if todos:
        print(f"📂 Loaded {len(todos)} task(s) from '{FILE}'.")
    else:
        print(f"📂 No saved data found — starting fresh.")

    menu = {
        "1": ("View list",         lambda: view_todos(todos)),
        "2": ("Add todo",          lambda: add_todo(todos)),
        "3": ("Complete todo",     lambda: complete_todo(todos)),
        "4": ("Delete todo",       lambda: delete_todo(todos)),
        "5": ("Exit",              None),
    }

    while True:
        print("\nMenu:")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")

        choice = input("\nChoose (1-5): ").strip()

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
