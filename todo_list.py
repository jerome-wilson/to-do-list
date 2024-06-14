import json

class Task:
    def __init__(self, description, due_date=None, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"[{status}] {self.description} (Due: {self.due_date})" if self.due_date else f"[{status}] {self.description}"

    def to_dict(self):
        return {
            "description": self.description,
            "due_date": self.due_date,
            "completed": self.completed
        }

def add_task(tasks, description, due_date=None):
    task = Task(description, due_date)
    tasks.append(task)

def view_tasks(tasks):
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def update_task(tasks, index, description=None, due_date=None):
    if 0 <= index < len(tasks):
        if description:
            tasks[index].description = description
        if due_date:
            tasks[index].due_date = due_date

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index].completed = True

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        json.dump([task.to_dict() for task in tasks], file)

def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            tasks_data = json.load(file)
            return [Task(**data) for data in tasks_data]
    except FileNotFoundError:
            return []

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Complete Task")
        print("6. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            add_task(tasks, description, due_date)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            index = int(input("Enter task number to update: ")) - 1
            description = input("Enter new description (leave blank to keep unchanged): ")
            due_date = input("Enter new due date (leave blank to keep unchanged): ")
            update_task(tasks, index, description, due_date)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == '5':
            index = int(input("Enter task number to mark as completed: ")) - 1
            complete_task(tasks, index)
        elif choice == '6':
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
