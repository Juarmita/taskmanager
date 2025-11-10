import json
from pathlib import Path
import pytest
from TASKMANAGER.task_manager import TaskManager, Task

def test_load_tasks_file_not_found(tmp_path):
    filepath = tmp_path / "no_file.json"
    tm = TaskManager(filename=str(filepath))
    assert tm._tasks == []
    assert tm._next_id == 1

def test_load_tasks_with_data(tmp_path):
    filepath = tmp_path / "tasks.json"
    data = [
        {"id": 1, "description": "Tarea uno", "completed": False},
        {"id": 3, "description": "Tarea tres", "completed": True}
    ]
    filepath.write_text(json.dumps(data))
    tm = TaskManager(filename=str(filepath))
    assert len(tm._tasks) == 2
    assert isinstance(tm._tasks[0], Task)
    assert tm._tasks[0].id == 1
    assert tm._tasks[0].description == "Tarea uno"
    assert tm._tasks[0].completed is False
    assert tm._tasks[1].id == 3
    assert tm._tasks[1].description == "Tarea tres"
    assert tm._tasks[1].completed is True
    assert tm._next_id == 4

def test_load_tasks_empty_list(tmp_path):
    filepath = tmp_path / "empty.json"
    filepath.write_text(json.dumps([]))
    tm = TaskManager(filename=str(filepath))
    assert tm._tasks == []
    assert tm._next_id == 1

def test_load_tasks_invalid_json_raises(tmp_path):
    filepath = tmp_path / "bad.json"
    filepath.write_text("{ invalid json ")
    with pytest.raises(json.JSONDecodeError):
        TaskManager(filename=str(filepath))

def test_add_complete_delete_and_persistence(tmp_path):
    filepath = tmp_path / "persist.json"
    tm = TaskManager(filename=str(filepath))
    # Add two tasks
    tm.add_task("Alpha")
    tm.add_task("Beta")
    # Verify file written and contents
    saved = json.loads(Path(tm.FILENAME).read_text())
    assert len(saved) == 2
    assert saved[0]["id"] == 1 and saved[0]["description"] == "Alpha" and saved[0]["completed"] is False
    assert saved[1]["id"] == 2 and saved[1]["description"] == "Beta" and saved[1]["completed"] is False
    # Complete first task
    tm.complete_task(1)
    assert any(t.id == 1 and t.completed for t in tm._tasks)
    saved_after = json.loads(Path(tm.FILENAME).read_text())
    assert any(item["id"] == 1 and item["completed"] is True for item in saved_after)
    # Delete first task
    tm.delete_task(1)
    assert all(t.id != 1 for t in tm._tasks)
    saved_after_delete = json.loads(Path(tm.FILENAME).read_text())
    assert all(item["id"] != 1 for item in saved_after_delete)

def test_list_tasks_outputs(tmp_path, capsys):
    filepath = tmp_path / "list.json"
    tm = TaskManager(filename=str(filepath))
    tm.add_task("Item A")
    tm.add_task("Item B")
    tm.list_tasks()
    captured = capsys.readouterr()
    assert "Item A" in captured.out
    assert "Item B" in captured.out
    assert "#" in captured.out
    assert "[" in captured.out