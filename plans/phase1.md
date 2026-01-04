# Phase I Implementation Plan: In-Memory Python Console App

This plan outlines the technical approach to implement the Phase I Specification for the "Evolution of Todo" project. It adheres strictly to the Global Constitution and Phase I strict constraints (In-memory, CLI only, No DB/Files).

## 1. High-Level Architecture
The application will be structured as a modular Python application to ensure Separation of Concerns (Constitution Quality Principle).

**Structure:**
```text
todo_app/
├── __init__.py
├── main.py          # Entry point, orchestrates the application loop
├── models.py        # Data definitions (Task class)
├── storage.py       # In-memory data management (CRUD logic)
└── cli.py           # User Interface (Menu, Input parsing, Output formatting)
```

## 2. Data Design (In-Memory)
Since there is no persistence, data will exist only in Python variables during runtime.

### 2.1 Data Model (`models.py`)
We will use a Python `dataclass` for the Task entity to enforce structure.
```python
@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    status: str = "Pending"  # Enums can be used, but keeping simple string per spec
```

### 2.2 Storage Mechanism (`storage.py`)
*   **Primary Storage**: A private list `_tasks = []` or dictionary `_tasks = {}`. Using a dictionary keyed by ID (`{id: Task}`) provides O(1) lookup for updates/deletes.
*   **ID Generation**: A simple integer counter `_next_id` starting at 1.

## 3. Component Details

### 3.1 Storage Manager (`storage.py`)
Responsible for all data manipulation.
*   `add_task(title, description) -> Task`: Increments ID, creates object, stores it.
*   `get_to_tasks() -> List[Task]`: Returns list of all tasks.
*   `get_task(id) -> Task`: Returns specific task or `None`.
*   `update_task(id, title, description) -> bool`: Updates fields if ID exists.
*   `delete_task(id) -> bool`: Removes task if ID exists.
*   `toggle_status(id) -> tuple[bool, str]`: Switches status, returns success + new status.

### 3.2 CLI Interface (`cli.py`)
Responsible for all user interaction (Input/Output). **Logic-free**.
*   `show_menu()`: Prints the 6 menu options.
*   `get_user_choice() -> int`: specific input validation for menu selection.
*   `prompt_add_task()`: Asks for title/desc.
*   `display_tasks(tasks)`: Formats the task list into a readable table.
*   `show_error(message)`: Standardized error formatting.
*   `show_success(message)`: Standardized success message.

### 3.3 Main Controller (`main.py`)
The "Glue" code.
1.  Initialize `Storage`.
2.  Start `while True` loop.
3.  Call `cli.show_menu()`.
4.  Get choice.
5.  Route choice to appropriate logic:
    *   *If Add*: Call CLI input -> Call Storage Add -> Call CLI Success.
    *   *If List*: Call Storage List -> Call CLI Display.
    *   etc.
6.  Handle Exit.

## 4. Control Flow & User Experience

### Menu Loop
```text
INITIALIZE Storage
LOOP
    DISPLAY Menu
    GET Choice
    MATCH Choice
        CASE 1 (Add): PROMPT data -> STORE -> CONFIRM
        CASE 2 (List): FETCH data -> DISPLAY
        CASE 3 (Update): PROMPT ID -> VALIDATE -> PROMPT data -> UPDATE -> CONFIRM
        CASE 4 (Delete): PROMPT ID -> DELETE -> CONFIRM
        CASE 5 (Toggle): PROMPT ID -> TOGGLE -> CONFIRM/SHOW STATUS
        CASE 6 (Exit): BREAK LOOP
    END MATCH
    HANDLE Invalid Input (Catch ValueError)
END LOOP
```

## 5. Error Handling Strategy
*   **Input Validation**: CLI layer ensures non-empty titles.
*   **ID Lookup**: Storage layer returns `None` or `False` if ID doesn't exist. Controller checks this and instructs CLI to show "Task not found" error.
*   **Type Safety**: `try/except ValueError` used when parsing integer IDs from user input.

## 6. Implementation Steps
1.  **Setup**: Create directory structure and empty files.
2.  **Models**: Define `Task` dataclass.
3.  **Storage**: Implement CRUD methods with unit tests (manual verification).
4.  **CLI**: Implement input prompts and menu display.
5.  **Integration**: logical routing in `main.py`.
6.  **Verification**: multiple manual test passes against User Stories.
