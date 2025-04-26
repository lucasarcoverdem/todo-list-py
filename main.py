TODO_LIST = []

def add_task(task):
    TODO_LIST.append(task) 

def remove_task(task):
    if task in TODO_LIST:
        TODO_LIST.remove(task)
    else:
        print(f"Task '{task}' not found in the list.")

def view_tasks():
    if TODO_LIST:
        print("TODO List:")
        for i, task in enumerate(TODO_LIST, start=1):
            print(f"{i}. {task}")
    else:
        print("TODO list is empty.")

def main():
    return

if __name__ == "__main__":
    main()
