class Task:
    def __init__(self, id: int, description: str, completed:bool = False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "ok" if self.completed else "wait"
        return  f"id {self.id}, description {self.description}, completed {self.description}"

