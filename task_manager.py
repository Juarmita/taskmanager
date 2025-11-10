import json

class Task:

    def __init__ (self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self): #Imprime el contetido de nuestra clse
        status = "✓" if self.completed else " " #Marca de verificación si la tarea está completada
        return f"[{status}] #{self.id}: {self.description}"     #Formato de cadena para representar la tarea
    
class TaskManager:

    FILENAME = "task.json"

    def __init__(self):
        self._tasks = []  #Lista para almacenar las tareas
        self._next_id = 1 #ID inicial para la primera tarea
        self.load_tasks

    def add_task(self, description): #Agregar una nueva tarea
        task = Task(self._next_id, description) #Crear una nueva tarea con el ID y la descripción proporcionada
        self._tasks.append(task) #Agregar la tarea a la lista
        self._next_id += 1 #Incrementar el ID para la próxima tarea
        print(f"Tarea agregada: {description}")
        self.save_tasks()

    def list_tasks(self): #Listar todas las tareas
        if not self._tasks:
            print("No hay tareas disponibles.")
        else:
           for task in self._tasks:
               print(task) 

    def complete_task(self, id):
        for task in self._tasks:
            if task.id == id:#Comprobamos si la tarea esta completada
                task.completed = True
                print(f"Tarea completada: {task}")
                self.save_tasks()
                return
        print (f"Tarea no encontrada: #{id}")


    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task) #Comprobamos el id y cuando lo encontremos lo borramos
                print(f"Tarea eliminada: #{id}")
                self.save_tasks()
                return
        print(f"Tarea no encontrada: #{id}")

    def load_tasks(self):
        try:
        
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
                self._tasks = [Task(item["id"], item["description"], item["completed"])for item in data]
                if self._tasks:
                    self._next_id = self._tasks[-1].id +1
                else:
                    self._next_id = 1
        except FileNotFoundError:
            self._tasks = []


    def save_tasks(self):
        with open(self.FILENAME, "w") as file:
            json.dump([{"id": task.id, "description": task.description, "completed": task.completed} for task in self._tasks], file, indent=4)