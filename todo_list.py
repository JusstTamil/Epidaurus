tasks = []

def add_task(task, due_date):
    tasks.append({"task": task, "due_date": due_date, "completed": False})
    print(f"Task '{task}' with due date '{due_date}' has been added to the list.")

def view_all_tasks():
    print("\nAll Tasks:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['task']} (Due: {task['due_date']}), Completed: {'Yes' if task['completed'] else 'No'}")

def mark_as_completed(task_index):
    try:
        task = tasks[task_index - 1]
        task["completed"] = True
        print(f"Task '{task['task']}' has been marked as completed.")
    except IndexError:
        print(f"Invalid task index: {task_index}")

def remove_task(task_index):
    try:
        task = tasks.pop(task_index - 1)
        print(f"Task '{task['task']}' has been removed from the list.")
    except IndexError:
        print(f"Invalid task index: {task_index}")

while True:
    print("\nTo-Do List:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")

    user_input = input("Enter your choice: ")
    if user_input == "1":
        task = input("Enter task: ")
        due_date = input("Enter due date: ")
        add_task(task, due_date)
    elif user_input == "2":
        view_all_tasks()
    elif user_input == "3":
        task_index = int(input("Enter task index: "))
        mark_as_completed(task_index)
    elif user_input == "4":
        task_index = int(input("Enter task index: "))
        remove_task(task_index)
    elif user_input == "5":
        break
    else:
        print(f"Invalid choice: {user_input}")

print("Thank You!")
