import sqlite3
from models.task_model import Task

DB_NAME = "db.sqlite3"


class TaskDB:
    def __init__(self, db_path="db.sqlite3"):
        self.db_path = db_path
        self._init_db()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    completed INTEGER DEFAULT 0
                    )
            ''')
            conn.commit()

    def add_task(self, task: Task):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO tasks (description, completed) VALUES (?, ?)',
                           (task.description, int(task.completed)))
            conn.commit()

    def get_all_tasks(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tasks')
            rows = cursor.fetchall()
            return [Task(id=row(0), description=row(1), completed=bool(row[2])) for row in rows]


    def complete_task(self, task_id: int):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ? ', (task_id,))
            conn.commit()


    def delete_task(self, task_id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
            conn.commit()
