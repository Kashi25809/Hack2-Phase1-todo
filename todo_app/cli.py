from typing import List, Tuple, Optional
from .models import Task

def show_menu():
    print("\n=== Todo App (Phase I) ===")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Toggle Task Status")
    print("6. Exit")

def get_user_choice() -> int:
    try:
        user_input = input("Select an option: ").strip()
        if not user_input:
            return 0
        choice = int(user_input)
        if 1 <= choice <= 6:
            return choice
        else:
            print("Invalid option. Please choose between 1 and 6.")
            return 0
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0

def show_error(msg: str):
    print(f"Error: {msg}")

def show_success(msg: str):
    print(f"Success: {msg}")

def display_tasks(tasks: List[Task]):
    if not tasks:
        print("No tasks available.")
        return

    print(f"\n{'ID':<5} | {'Status':<12} | {'Title'}")
    print("-" * 50)
    for task in tasks:
        print(f"{task.id:<5} | {task.status:<12} | {task.title}")
    print("-" * 50)

def prompt_add_task() -> Tuple[str, str]:
    while True:
        title = input("Enter Title: ").strip()
        if title:
            break
        print("Title cannot be empty.")
    
    desc = input("Enter Description (optional): ").strip()
    return title, desc

def prompt_id(action_name: str) -> Optional[int]:
    try:
        val = input(f"Enter Task ID to {action_name}: ").strip()
        return int(val)
    except ValueError:
        print("Invalid ID format.")
        return None

def prompt_update_fields() -> Tuple[Optional[str], Optional[str]]:
    print("Leave blank to keep current value.")
    title = input("New Title: ").strip()
    desc = input("New Description: ").strip()
    
    return (title if title else None, desc if desc else None)
