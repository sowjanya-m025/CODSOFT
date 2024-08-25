#A To-Do List application

import json
import os

FILE = 'tasktoenter.json'   #file created using json

def load_tasktoenter():
    if os.path.exists(FILE):
        with open(FILE, 'r') as file:
            return json.load(file)
    return []

def save_alltask(tasks):
    with open(FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def list_alltask(tasks):
    if not tasks:
        print("No task present.")
        return
    for i, task in enumerate(tasks):
        status = '✓' if task['completed'] else '✗'
        print(f"{i + 1}. {task['description']} [{status}]")

def add_alltask(description):
    tasks = load_tasktoenter()
    tasks.append({'description': description, 'completed': 0})
    save_alltask(tasks)

def update_alltask(i, completed):
    tasks = load_tasktoenter()
    if 0 <= i < len(tasks):
        tasks[i]['completed'] = completed
        save_alltask(tasks)
    else:
        print("Invalid task index i.")

def delete_task(i):
    tasks = load_tasktoenter()
    if 0 <= i < len(tasks):
        tasks.pop(i)
        save_alltask(tasks)
    else:
        print("Invalid task index i.")

def category_main():
    while True:
        print("\nTo-Do List application")
        print("1. List task")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. logout")
        choice = input("Choose any option Number: ")

        if choice == '1':
            list_alltask(load_tasktoenter())
        elif choice == '2':
            description = input("Enter task name/description: ")
            add_alltask(description)
        elif choice == '3':
            list_alltask(load_tasktoenter())
            i = int(input("Enter task number to update: ")) - 1
            completed = input("Mark as completed? (yes/No): ").lower() == 'yes'
            update_alltask(i, completed)
        elif choice == '4':
            list_alltask(load_tasktoenter())
            i= int(input("Enter task number to delete: ")) - 1
            delete_task(i)
        elif choice == '5':
            break
        else:
            print(" choice is invalid.")

if __name__ == "__main__":
    category_main()

