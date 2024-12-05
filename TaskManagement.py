from datetime import datetime

class TaskManagement:
    def __init__(self):
        self.tasks = {}

    def add_task(self, project_manager):
        try:
            id_ = int(input("Enter Task ID: "))
            if id_ in self.tasks:
                print("Task already exists.")
                return

            name = input("Enter Task Name: ")
            description = input("Enter Task Description: ")
            status = False
            start_date = self.input_for_date("Enter Start Date (YYYY-MM-DD HH:MM): ")
            end_date = None
            project_name = input("Enter the Project Name to associate with this task: ")

            if project_name not in project_manager.projects:
                print(f"Project '{project_name}' does not exist. Please create it first.")
                return

            task = {
                "id": id_,
                "name": name,
                "description": description,
                "status": status,
                "start_date": start_date,
                "end_date": end_date,
                "duration": None,
                "project": project_name,
            }

            self.tasks[id_] = task
            project_manager.add_task_to_project(project_name, task)
            print(f"Task '{name}' added successfully to project '{project_name}'.")
            print(f"Start Date: {start_date}")

        except ValueError:
            print("Invalid input. Please ensure numbers are entired correct.")

    def mark_as_done(self, id_):
        if id_ in self.tasks:
            task = self.tasks[id_]
            if not task["status"]:
                task["status"] = True
                end_date = self.input_for_date("Enter End Date (YYYY-MM-DD HH:MM): ")
                if end_date > task["start_date"]:
                    task["end_date"] = end_date
                    duration = task["end_date"] - task["start_date"]
                    task["duration"] = self.calculate_duration(duration)
                    print(f"Task '{task['name']}' marked as complete.")
                    print(f"End Date: {task['end_date']}")
                    print(f"Duration: {task['duration']}")
                else:
                    print("End Date should be greater than Start Date.")
            else:
                print("Task is already completed.")
        else:
            print("Task not found.")

    def input_for_date(self, prompt):
        while True:
            try:
                date_input = input(prompt)
                return datetime.strptime(date_input, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Invalid date format. Please enter in 'YYYY-MM-DD HH:MM' format.")

    def calculate_duration(self, duration):
        total_seconds = int(duration.total_seconds())
        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        months, days = divmod(days, 30)
        if months > 12:
            years, months = divmod(months, 12)
            return f"{years} years {months} months {days} days {hours} hours {minutes} minutes"
        else:
         return f"month {months} days {days} hour {hours} minute {minutes}"

    def edit_task(self, id_):
        if id_ in self.tasks:
            task = self.tasks[id_]
            print("Choose your option to edit:")
            print("1. Name")
            print("2. Description")
            print("3. Status")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                task["name"] = input("Enter new name: ")
            elif choice == 2:
                task["description"] = input("Enter new description: ")
            elif choice == 3:
                status_input = input("Is the task done? (yes/no): ").strip().lower()
                new_status = True if status_input in ["yes", "y"] else False
                if new_status and not task["status"]:
                    self.mark_as_done(id_)
                else:
                    task["status"] = new_status
                    print("Status updated.")
            else:
                print("Invalid option.")
        else:
            print("Task does not exist.")

    def delete_task(self, id_):
        if id_ in self.tasks:
            del self.tasks[id_]
            print(f"Task with ID {id_} deleted successfully.")
        else:
            print("Task does not exist.")

    def search_task(self, id_):
        if id_ in self.tasks:
            print("Task found:")
            task = self.tasks[id_]
            print(
                f"ID: {task['id']}, Name: {task['name']}, Status: {'Completed' if task['status'] else 'Not Completed'}, "
                f"Start Date: {task['start_date']}, End Date: {task['end_date']}, Duration: {task['duration']}, "
                f"Description: {task['description']}, Project: {task['project']}"
            )
        else:
            print("Task not found.")