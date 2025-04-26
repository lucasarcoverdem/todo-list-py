import time

TODO_LIST = []

def add_task(task):
    TODO_LIST.append(task) 

def remove_task(task):
    if task in TODO_LIST:
        TODO_LIST.remove(task)
        print(f"Task '{task}' removed from the list.")
        time.sleep(2)
    else:
        print(f"Task '{task}' not found in the list.")
        time.sleep(2)

def view_tasks():
    if TODO_LIST:
        print("TODO List:")
        for i, task in enumerate(TODO_LIST, start=1):
            print(f"{i}. {task}")
    else:
        print("TODO list is empty.")