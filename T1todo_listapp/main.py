todo_list = []

def show_menu():
    print("\n----- To-Do List Application -----")
    print("1. Add New task")
    print("2. View all Tasks")
    print("3. Remove a Task")
    print("4. Mark task as done")
    print("5. Exit ")


def add_task():
    task = input("Enter the task: ")
    todo_list.append({"Task": task, "Status": "pending"})
    print(f"New Task added successfully!")


def view_tasks():
    if not todo_list:
        print(" No tasks found.")
    else:
        print("\nYour To-Do List Tasks:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}: {task["Task"]} - {task["Status"]}")


def remove_task():
    if len(todo_list) == 0:
        print("\n List is Empty")
    else:
        try: 
            search_index = int(input("Enter the Task number that you want to remove: ")) - 1
            if 0 <= search_index < len(todo_list):
                removed = todo_list.pop(search_index)
                print(f" Task '{removed}' removed!")
            else:
                print("Invalid Task Number")
        except (IndexError, ValueError):
            print(" Please Enter valid task number.")


def done_task():
    if len(todo_list) == 0:
        print("\n List is Empty")
    else:
        try: 
            search_index = int(input("Enter the Task number that you want to mark as done: ")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index] ['Status'] = 'done'
                print(f" Task {todo_list[search_index]['Task']} has been marked as done: ")
            else:
                print("Invalid Task Number")
        except (IndexError, ValueError):
            print(" Please Enter valid task number.")
    
    
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        done_task()
    elif choice == '5':
        print(" Exiting... Bye!")
        break
    else:
        print(" Invalid choice. Try again.")
