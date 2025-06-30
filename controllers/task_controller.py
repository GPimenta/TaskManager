from services.db_service import TaskDB
from models.task_model import Task


class TaskController:
    def __init__(self, db: TaskDB):
        self.db = db

    def add_task(self, description: str):
        task = Task(id=None, description=description)
        self.db.add_task(task)

    def list_tasks(self):
        return self.db.get_all_tasks()

    def complete_task(self, task_id):
        self.db.complete_task(task_id)

    def delete_task(self, task_id):
        self.db.delete_task(task_id)
