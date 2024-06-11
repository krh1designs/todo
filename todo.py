tasks = []
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")

def view_tasks():
    if tasks:
        print("Tasks:")
        for task in tasks:
            print(f"- {task}")
    else:
        print("No tasks found.")

def show_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")
    
    if choice == '1':
        task = input("Enter a task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice, please try again.")

        import json

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def load_tasks():
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

        load_tasks()

while True:
    show_menu()
    choice = input("Choose an option: ")
    
    if choice == '1':
        task = input("Enter a task: ")
        add_task(task)
        save_tasks()
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
        save_tasks()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice, please try again.")