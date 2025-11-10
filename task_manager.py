class Task:

    def __init__ (self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self): #Imprime el contetido de nuestra clse
        status = "✓" if self.completed else " " #Marca de verificación si la tarea está completada
        return f"[{status}] #{self.id}: {self.description}"     #Formato de cadena para representar la tarea
    
class TaskManager:

    def __init__(self):
        self._tasks = []  #Lista para almacenar las tareas
        self._next_id = 1 #ID inicial para la primera tarea

    def add_task(self, description): #Agregar una nueva tarea
        task = Task(self._next_id, description) #Crear una nueva tarea con el ID y la descripción proporcionada
        self._tasks.append(task) #Agregar la tarea a la lista
        self._next_id += 1 #Incrementar el ID para la próxima tarea
        print(f"Tarea agregada: {description}")

    def list_tasks(self): #Listar todas las tareas
        if not self._tasks:
            print("No hay tareas disponibles.")
        else:
           for task in self._tasks:
               print(task) 

    def complete_task(self):
        for task in self._tasks:
            if task.id == id:#Comprobamos si la tarea esta completada
                task.completed = True
                print(f"Tarea completada: {task}")
                return
        print (f"Tarea no encontrada: #{id}")


    def delete_task(self, id):
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task) #Comprobamos el id y cuando lo encontremos lo borramos
                print(f"Tarea eliminada: #{id}")
                return
        print(f"Tarea no encontrada: #{id}")