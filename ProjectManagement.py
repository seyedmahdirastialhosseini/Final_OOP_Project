class ProjectManagement:
    def __init__(self):
        self.projects = {}

    def add_project(self, name):
        if name in self.projects:
            print("Project already exists.")
        else:
            self.projects[name] = []
            print(f"Project '{name}' added successfully.")

    def edit_project(self, old_name):
        if old_name in self.projects:
            print(f"enter the new name for the project {old_name} : ")
            new_name = input()
            self.projects[new_name] = self.projects.pop(old_name)
            print(f"Project renamed from '{old_name}' to '{new_name}'.")
        else:
            print("Project does not exist.")

    def delete_project(self, name):
        if name in self.projects:
            del self.projects[name]
            print(f"Project '{name}' deleted successfully.")
        else:
            print("Project does not exist.")

    def display_projects(self):
        for p, tasks in self.projects.items():
            print(f"Project: {p}")
            print(f"Number of tasks: {len(tasks)}")
            for task in tasks:
                print(
                    f"  - Task ID: {task['id']}, Name: {task['name']}, "
                    f"Status: {'Completed' if task['status'] else 'Not Completed'}"
                )

    def add_task_to_project(self, project_name, task):
        if project_name in self.projects:
            self.projects[project_name].append(task)
            print(f"Task '{task['name']}' added to project '{project_name}'.")
        else:
            print(f"Project '{project_name}' does not exist.")