import json

class Task:

    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"
    
class TaskManager:

    FILENAME = "task.json"

    def __init__(self, filename=None):
        # Si se pasa filename, usarlo para esta instancia
        if filename:
            self.FILENAME = filename
        self._tasks = []
        self._next_id = 1
        self.load_tasks()

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Tarea agregada: {description}")
        self.save_tasks()

    def list_tasks(self):
        if not self._tasks:
            print("No hay tareas disponibles.")
        else:
           for task in self._tasks:
               print(task)

    def complete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"Tarea completada: {task}")
                self.save_tasks()
                return
        print(f"Tarea no encontrada: #{id}")

    def delete_task(self, id):
        for task in list(self._tasks):
            if task.id == id:
                self._tasks.remove(task)
                print(f"Tarea eliminada: #{id}")
                self.save_tasks()
                return
        print(f"Tarea no encontrada: #{id}")

    def load_tasks(self):
        try:
            with open(self.FILENAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                self._tasks = [Task(item["id"], item["description"], item.get("completed", False)) for item in data]
                if self._tasks:
                    max_id = max(t.id for t in self._tasks)
                    self._next_id = max_id + 1
                else:
                    self._next_id = 1
        except FileNotFoundError:
            self._tasks = []
            self._next_id = 1

    def save_tasks(self):
        with open(self.FILENAME, "w", encoding="utf-8") as file:
            json.dump([{"id": task.id, "description": task.description, "completed": task.completed} for task in self._tasks], file, indent=4, ensure_ascii=False)