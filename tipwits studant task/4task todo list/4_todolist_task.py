
import json
import os

filename = "todo.json"

def load_tasks():
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(filename, "w") as f:
        json.dump(tasks, f)

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for i, t in enumerate(tasks):
        status = "✓" if t["done"] else "✗"
        print(f"{i+1}. {t['task']} [{status}]")

def mark_done(tasks):
    view_tasks(tasks)
    i = int(input("Task number to mark as done: ")) - 1
    if 0 <= i < len(tasks):
        tasks[i]["done"] = True
        print("Task marked as done.")

def delete_task(tasks):
    view_tasks(tasks)
    i = int(input("Task number to delete: ")) - 1
    if 0 <= i < len(tasks):
        tasks.pop(i)
        print("Task deleted.")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark as Done\n4. Delete Task\n5. Exit (Goodbye)")
        choice = input("Choose: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
        save_tasks(tasks)

if __name__ == "__main__":
    main()
