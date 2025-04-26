import os
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

def main():
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n=== M Y - T O - D O ===\n")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. View Tasks")
            print("0. Exit")
            choice = int(input("Choose an option: "))
            if choice not in [0, 1, 2, 3]:
                print("Invalid choice. Please try again.")
                time.sleep(2)
                continue

            else:
                if choice == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\n=== M Y - T O - D O ===\n")
                    task = input("Enter the task to add: ")
                    add_task(task)
                    print(f"Task '{task}' added to the list.")
                    time.sleep(2)

                elif choice == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\n=== M Y - T O - D O ===\n")
                    task = input("Enter the task to remove: ")
                    remove_task(task)
                    time.sleep(2)

                elif choice == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\n=== M Y - T O - D O ===\n")
                    view_tasks()
                    input("\nPress Enter to continue...")

                elif choice == 0:
                    print("Exiting the program.")
                    break
        
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        except KeyboardInterrupt:
            print("\nExiting the program.")
            break

if __name__ == "__main__":
    main()
