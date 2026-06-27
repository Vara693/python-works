import json
import os

tasks = []
task_id = 1

def load_tasks():
    global tasks, task_id
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            if tasks:
                task_id = max(task["id"] for task in tasks) + 1
            else:
                task_id = 1
    except FileNotFoundError:
        tasks = []
        task_id = 1

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(name):
    global task_id
    task = {"id": task_id, "title": name, "done": False}
    tasks.append(task)
    task_id += 1
    save_tasks()
    return task  # return instead of print

def list_tasks():
    return tasks  # return list instead of print

def mark_done(id):
    for task in tasks:
        if task["id"] == id:
            task["done"] = True
            save_tasks()
            return task
    return None

def delete_task(id):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            save_tasks()
            return True
    return False

# Console menu (still works if run directly)
def menu():
    load_tasks()
    while True:
        print("\n--- TO-DO LIST APP ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
            print(f"Task added: {title}")
        elif choice == "2":
            if not tasks:
                print("No tasks found")
            else:
                for task in tasks:
                    status = "Done" if task["done"] else "Not done"
                    print(f"{task['id']}. {task['title']}: {status}")
        elif choice == "3":
            try:
                tid = int(input("Enter task ID to mark as done: "))
                if mark_done(tid):
                    print(f"{tid} task marked done")
                else:
                    print("Task not found")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                tid = int(input("Enter task ID to delete: "))
                if delete_task(tid):
                    print(f"{tid} task successfully deleted")
                else:
                    print("Task not found")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()

