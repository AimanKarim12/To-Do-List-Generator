tasks = []

def display_todo_list(tasks):
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['name']}")

def print_list_names(tasks):
    for task in tasks:
        print(task["name"])

def search_task(tasks, task_name):
    for task in tasks:
        if task["name"] == task_name:
            print(f"Name: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Due date: {task['due_date']}")
            print(f"Priority: {task['priority']}")
            return
    print("Task not found.")

def edit_task(tasks, task_name):
    for task in tasks:
        if task["name"] == task_name:
            task["name"] = input("Enter new task name: ")
            task["description"] = input("Enter new task description: ")
            task["due_date"] = input("Enter new task due date: ")
            task["priority"] = input("Enter new task priority: ")
            return
    print("Task not found.")

def new_task():
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    due_date = input("Enter task due date: ")
    priority = input("Enter task priority: ")
    tasks.append({"name": name, "description": description, "due_date": due_date, "priority": priority})

def remove_task(tasks, task_name):
    for i, task in enumerate(tasks):
        if task["name"] == task_name:
            del tasks[i]
            return
    print("Task not found.")

while True:
    print("1. Display to-do list")
    print("2. Print out all list names")
    print("3. Search for task")
    print("4. Edit task")
    print("5. New task")
    print("6. Remove task")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        display_todo_list(tasks)
    elif choice == "2":
        print_list_names(tasks)
    elif choice == "3":
        task_name = input("Enter task name: ")
        search_task(tasks, task_name)
    elif choice == "4":
        task_name = input("Enter task name: ")
        edit_task(tasks, task_name)
    elif choice == "5":
        new_task()
    elif choice == "6":
        task_name = input("Enter task name: ")
        remove_task(tasks, task_name)
    elif choice == "7":
        break
    else:
        print("Invalid choice.")
