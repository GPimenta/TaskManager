from controllers.task_controller import TaskController
from services.db_service import  TaskDB


def print_menu():
    print("\n=== Task Tracker ===")
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")



def main():
    db = TaskDB()
    controller = TaskController(db)

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            desc = input("Enter task description: ").strip()
            controller.add_task(desc)
            print("Task added.")
        elif choice == "2":
            tasks = controller.list_tasks()
            if not tasks:
                print("No tasks yet.")
            for task in tasks:
                print(task)
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))
                controller.complete_task(task_id)
                print("✅ Task marked as complete.")
            except ValueError:
                print("Invalid ID.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                controller.delete_task(task_id)
                print("🗑️ Task deleted.")
            except ValueError:
                print("❌ Invalid ID.")
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
