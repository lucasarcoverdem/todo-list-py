import time
from storage import load_tasks, save_tasks

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added to the list.")

def remove_task(task):
    tasks = load_tasks()
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task '{task}' removed from the list.")
    else:
        print(f"Task '{task}' not found in the list.")
    time.sleep(2)

def view_tasks():
    tasks = load_tasks()
    if tasks:
        print("TODO List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("TODO list is empty.")