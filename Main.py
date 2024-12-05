from datetime import datetime
from ProjectManagement import *
from TaskManagement import *

### Github Address for this Code https://github.com/seyedmahdirastialhosseini/Final_OOP_Project

def main():
    project_manager = ProjectManagement()
    task_manager = TaskManagement()

    while True:
        print("\nMenu:")
        print("1. Add Project")
        print("2. Edit Project")
        print("3. Delete Project")
        print("4. Add Task")
        print("5. Edit Task")
        print("6. Mark Task as Complete")
        print("7. Delete Task")
        print("8. Search Task")
        print("9. Display Projects and Tasks")
        print("10. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            project_name = input("Enter Project Name: ")
            project_manager.add_project(project_name)

        elif choice == "2":
            old_name = input("Enter the name of the project to edit: ")
            project_manager.edit_project(old_name)

        elif choice == "3":
            project_name = input("Enter the name of the project to delete: ")
            project_manager.delete_project(project_name)

        elif choice == "4":
            task_manager.add_task(project_manager)

        elif choice == "5":
            try:
                task_id = int(input("Enter Task ID to edit: "))
                task_manager.edit_task(task_id)
            except ValueError:
                print("Invalid Task ID.")

        elif choice == "6":
            try:
                task_id = int(input("Enter Task ID to mark as complete: "))
                task_manager.mark_as_done(task_id)
            except ValueError:
                print("Invalid Task ID.")

        elif choice == "7":
            try:
                task_id = int(input("Enter Task ID to delete: "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("Invalid Task ID.")

        elif choice == "8":
            try:
                task_id = int(input("Enter Task ID to search: "))
                task_manager.search_task(task_id)
            except ValueError:
                print("Invalid Task ID.")

        elif choice == "9":
            project_manager.display_projects()

        elif choice == "10":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
