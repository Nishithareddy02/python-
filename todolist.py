import json

class TodoList:
    def __init__(self, filename='todolist.json'):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()
        print(f'Task added: "{task}"')

    def update_task(self, index, task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['task'] = task
            self.save_tasks()
            print(f'Task updated: "{task}"')
        else:
            print("Invalid task index.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            self.save_tasks()
            print(f'Task completed: "{self.tasks[index]["task"]}"')
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks):
                status = '✓' if task['completed'] else '✗'
                print(f"{index + 1}. [{status}] {task['task']}")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Complete Task")
        print("4. View Tasks")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task number to update: ")) - 1
            task = input("Enter the new task: ")
            todo_list.update_task(index, task)
        elif choice == '3':
            index = int(input("Enter the task number to complete: ")) - 1
            todo_list.complete_task(index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
