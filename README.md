# TASKMANAGER

Proyecto sencillo para gestionar tareas en memoria con persistencia en JSON. Incluye una clase `Task` y un `TaskManager` con operaciones básicas (añadir, listar, completar, borrar) y soporte para cargar/guardar desde un fichero JSON.

## Características
- ✅ Añadir tareas (con id incremental automático)
- 📋 Listar tareas con representación legible
- ✔️ Marcar tareas como completadas
- ❌ Eliminar tareas
- 💾 Persistencia automática en fichero JSON
- 🧪 Constructor de `TaskManager` acepta un `filename` para tests y uso aislado
- 🔬 Tests automatizados con `pytest`

## Requisitos
- Python 3.8+
- pytest (para ejecutar tests)

## Estructura del proyecto
```
TASKMANAGER/
├── task_manager.py        # Implementación de Task y TaskManager
├── test_task_manager.py   # Tests con pytest
├── __init__.py           # Archivo vacío para hacer el directorio un paquete Python
└── README.md             # Este archivo
```

## Instalación

### Windows / PowerShell
1. Abrir la terminal integrada de VS Code o PowerShell
2. Navegar al directorio del proyecto:
   ```powershell
   cd "c:\Users\juanm\Desktop\Programacion + IA Brais\Máster IA\Modulo 0\10. Proyecto práctico inicial"
   ```
3. (Opcional) Crear y activar un entorno virtual:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
4. Instalar pytest para ejecutar tests:
   ```powershell
   pip install pytest
   ```

## Uso básico

### Desde Python (script o REPL)
```python
from TASKMANAGER.task_manager import TaskManager

# Crear TaskManager con archivo por defecto (task.json)
tm = TaskManager()

# O crear con archivo específico
tm = TaskManager(filename="mis_tareas.json")

# Añadir tareas
tm.add_task("Comprar leche")
tm.add_task("Preparar presentación")
tm.add_task("Estudiar Python")

# Listar todas las tareas
tm.list_tasks()
# Salida:
# [ ] #1: Comprar leche
# [ ] #2: Preparar presentación
# [ ] #3: Estudiar Python

# Marcar tarea como completada
tm.complete_task(1)

# Listar tareas después de completar
tm.list_tasks()
# Salida:
# [✓] #1: Comprar leche
# [ ] #2: Preparar presentación
# [ ] #3: Estudiar Python

# Eliminar una tarea
tm.delete_task(2)

# Listar tareas finales
tm.list_tasks()
# Salida:
# [✓] #1: Comprar leche
# [ ] #3: Estudiar Python
```

### Formato del archivo JSON
El archivo de persistencia tiene la siguiente estructura:
```json
[
    {
        "id": 1,
        "description": "Comprar leche",
        "completed": true
    },
    {
        "id": 3,
        "description": "Estudiar Python",
        "completed": false
    }
]
```

## Ejecutar tests

Desde la raíz del proyecto ejecutar:

```powershell
# Ejecutar solo el archivo de tests (recomendado)
python -m pytest TASKMANAGER/test_task_manager.py -q

# Ejecutar con más detalle
python -m pytest TASKMANAGER/test_task_manager.py -v

# Ejecutar todos los tests del proyecto
python -m pytest -q
```

### Tests incluidos
- `test_load_tasks_file_not_found`: Verifica comportamiento cuando el archivo no existe
- `test_load_tasks_with_data`: Carga datos existentes correctamente
- `test_load_tasks_empty_list`: Maneja archivos con listas vacías
- `test_load_tasks_invalid_json_raises`: Controla archivos JSON malformados
- `test_add_complete_delete_and_persistence`: Prueba operaciones completas con persistencia
- `test_list_tasks_outputs`: Verifica la salida del listado de tareas

## API de clases

### Clase `Task`
```python
class Task:
    def __init__(self, id, description, completed=False)
    def __str__(self)  # Retorna formato "[✓] #1: Descripción"
```

### Clase `TaskManager`
```python
class TaskManager:
    def __init__(self, filename=None)      # Crea instancia y carga tareas
    def add_task(self, description)        # Añade nueva tarea
    def list_tasks(self)                   # Imprime todas las tareas
    def complete_task(self, id)            # Marca tarea como completada
    def delete_task(self, id)              # Elimina tarea por ID
    def load_tasks(self)                   # Carga tareas desde JSON
    def save_tasks(self)                   # Guarda tareas a JSON
```

## Solución de problemas

### Error: `ModuleNotFoundError: No module named 'TASKMANAGER'`
**Causa**: pytest no encuentra el paquete TASKMANAGER
**Solución**:
1. Ejecutar pytest desde la raíz del proyecto (no desde dentro de TASKMANAGER/)
2. Crear archivo `TASKMANAGER/__init__.py` vacío si no existe:
   ```powershell
   New-Item -Path "TASKMANAGER\__init__.py" -ItemType File
   ```

### Error: `TypeError: TaskManager.__init__() got an unexpected keyword argument 'filename'`
**Causa**: La clase TaskManager no acepta el parámetro filename
**Solución**: Verificar que task_manager.py tiene el constructor actualizado con `filename=None`

### Tests fallan por IDs incorrectos
**Causa**: TaskManager carga tareas existentes del archivo task.json por defecto
**Solución**: Los tests usan `tmp_path` fixture para crear archivos temporales aislados

### Problemas de encoding en Windows
**Causa**: Caracteres especiales en descripciones de tareas
**Solución**: Los métodos usan `encoding="utf-8"` y `ensure_ascii=False`

## Características técnicas

- **Persistencia automática**: Cada operación (add, complete, delete) guarda automáticamente
- **ID incremental**: Los IDs se asignan automáticamente y se mantienen únicos
- **Manejo de errores**: FileNotFoundError se maneja graciosamente
- **Encoding UTF-8**: Soporte completo para caracteres especiales
- **Aislamiento en tests**: Cada test usa archivos temporales independientes

## Mejoras futuras

- [ ] Interfaz de línea de comandos (CLI)
- [ ] Filtros por estado (completadas/pendientes)
- [ ] Fechas de creación y vencimiento
- [ ] Prioridades de tareas
- [ ] Categorías o etiquetas
- [ ] Búsqueda por texto
- [ ] Interfaz web con Flask/FastAPI

## Contribuir

1. Fork del repositorio
2. Crear rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Añadir tests para nuevas funcionalidades
4. Verificar que todos los tests pasan
5. Commit cambios (`git commit -am 'Añadir nueva funcionalidad'`)
6. Push a la rama (`git push origin feature/nueva-funcionalidad`)
7. Crear Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

## Contacto

- Abrir un issue en GitHub para reportar errores
- Proponer mejoras mediante Pull Requests
- Documentar claramente cualquier cambio en funcionalidad