from user import User
from task_manager import TaskManager
import sensitive_data


if __name__ == "__main__":
    dbname = sensitive_data.dbname
    user = sensitive_data.user
    password = sensitive_data.password
    host = sensitive_data.host
    port = sensitive_data.port

    task_manager = TaskManager(dbname, user, password, host, port)
    user_manager = User(dbname, user, password, host, port)
    user_manager.create_table()
    task_manager.create_table()

    while True:
        print("1. Add user")
        print("2. Add a task")
        print("3. Update task")
        print("4. Delete task")
        print("5. View user tasks")
        print("6. View users")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter a username: ")
            user_manager.add_user(name)
            print("User added.")
        elif choice == "2":
            user_id = input("Enter user ID: ")
            name = input("Enter the name of the task: ")
            description = input("Enter job description: ")
            deadline = input("Enter the due date (in the format YYYY-MM-DD): ")
            status = input("Enter the status of the task (1 - to be done, 2 - in progress, 3 - done) ")
            task_manager.add_task(user_id, name, description, deadline, status)
            print("Task added.")
        elif choice == "3":
            task_id = input("Enter task ID: ")
            name = input("Enter a new task name (if you don't want to change it, leave it blank): ")
            description = input("Enter a new job description (if you don't want to change it, leave it blank): ")
            deadline = input(
                "Enter a new due date (in the format YYYY-MM-DD) (if you do not want to change it, leave it blank): ")
            status = input(
                "Enter the new status of the task (1 - to be done, 2 - in progress, 3 - done) (if you "
                "do not want to change, leave blank): ")
            task_manager.update_task(task_id, name, description, deadline, status)
            print("Task updated.")
        elif choice == "4":
            task_id = input("Enter task ID: ")
            task_manager.delete_task(task_id)
            print("Job deleted.")
        elif choice == "5":
            user_id = input("Enter user ID: ")
            tasks = task_manager.get_tasks(user_id)
            print(f"User Tasks {user_id}:")
            for task in tasks:
                print(f"- {task[2]} ({task[4]})")
        elif choice == "6":
            users = user_manager.get_users()
            print("Users:")
            for user in users:
                print(f"- {user[1]}")
        elif choice == "0":
            break
        else:
            print("Invalid option.")
