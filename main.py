tasks = []

# A function to show the menu
def show_menu():
    print("\n=== To-Do List ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark task as Done")
    print("4. Delete Task")
    print("5. Exit")
     
# A function to add task    
def add_task():
    task_name = input("Enter task: ")
    task = {"task": task_name, "done": False}
    tasks.append(task)
    print("Task added!")

# A function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
        return    
for i, task in enumerate (tasks):
    status = "✅" if task["done"] else "❌"
    print(f"{i + 1}. {task["task"]} [{status}]")
    
# A function to mark the task as done
def mark_done():
    view_tasks()
    try:
        task_no = int(input("Enter a task number to mark as done")) - 1
        if 0 <= task_no < len(tasks):
            tasks[task_no]["done"] = True
            print("Task marked as done!")
        else:
            print("invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
        
#A function to delete the task 
def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_no < len(tasks):
            deleted = tasks.pop(task_no)
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
        
# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("bye!")
        break
    else:
        print("Invalid choice. Try again")
        