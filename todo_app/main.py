import sys
from .storage import Storage
from . import cli

def main():
    storage = Storage()
    
    while True:
        cli.show_menu()
        choice = cli.get_user_choice()
        
        if choice == 0:
            continue
            
        if choice == 1: # Add
            title, desc = cli.prompt_add_task()
            task = storage.add_task(title, desc)
            cli.show_success(f"Task {task.id} added successfully.")
            
        elif choice == 2: # List
            tasks = storage.get_all_tasks()
            cli.display_tasks(tasks)
            
        elif choice == 3: # Update
            task_id = cli.prompt_id("Update")
            if task_id:
                if storage.get_task(task_id):
                    title, desc = cli.prompt_update_fields()
                    if storage.update_task(task_id, title, desc):
                        cli.show_success(f"Task {task_id} updated.")
                    else:
                        cli.show_error(f"Failed to update Task {task_id}.")
                else:
                    cli.show_error(f"Task with ID {task_id} not found.")

        elif choice == 4: # Delete
            task_id = cli.prompt_id("Delete")
            if task_id:
                if storage.delete_task(task_id):
                    cli.show_success(f"Task {task_id} deleted.")
                else:
                    cli.show_error(f"Task with ID {task_id} not found.")
                    
        elif choice == 5: # Toggle
            task_id = cli.prompt_id("Toggle")
            if task_id:
                success, new_status = storage.toggle_status(task_id)
                if success:
                    cli.show_success(f"Task {task_id} is now {new_status}.")
                else:
                     cli.show_error(f"Task with ID {task_id} not found.")

        elif choice == 6: # Exit
            print("Exiting application. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()
