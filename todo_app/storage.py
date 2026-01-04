from typing import List, Optional, Tuple
from .models import Task

class Storage:
    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def add_task(self, title: str, description: str = "") -> Task:
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        # Return sorted by ID for consistent display
        return sorted(self._tasks.values(), key=lambda t: t.id)

    def get_task(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        task = self._tasks.get(task_id)
        if not task:
            return False
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        return True

    def delete_task(self, task_id: int) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def toggle_status(self, task_id: int) -> Tuple[bool, str]:
        task = self._tasks.get(task_id)
        if not task:
            return False, ""
        
        new_status = "Completed" if task.status == "Pending" else "Pending"
        task.status = new_status
        return True, new_status
