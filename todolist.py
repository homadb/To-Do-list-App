#To Do List App

class todolist:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Taks '{task}' removed successfully!")
        else:
            print("Task not found in the list.")

    def view_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}.{task}")
        else:
            print("Your To-Do List is empty.")
            
def main():
    todo_list = todolist()


    while True:
        print("\nMenu.")
        print("1.Add a task")
        print("2.Remove a task")
        print("3.View tasks")
        print("4.Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input(" Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    main()