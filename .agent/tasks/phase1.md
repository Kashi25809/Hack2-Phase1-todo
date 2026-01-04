---
description: tasks for Phase I implementation
---

# Phase I Implementation Tasks

This document breaks down the Phase I Implementation Plan into atomic, verifiable tasks. All work must reference these tasks explicitly.

## Task Legend
*   **ID**: P1-[Component]-[Number] (e.g., P1-CORE-01)
*   **P1**: Phase I

## 1. Core Structure & Data Model

### [P1-CORE-01] Initialize Project Structure & Models
*   **Description**: Create the project directory structure and define the `Task` data model.
*   **Prerequisites**: None.
*   **Input**: Plan Section 1 & 2.1.
*   **Steps**:
    1.  Create folder `todo_app/`.
    2.  Create empty `__init__.py`.
    3.  Create `todo_app/models.py`.
    4.  Implement `Task` dataclass (id, title, description, status).
*   **Artifacts**: `todo_app/models.py`.
*   **Success Criteria**: Python file exists, `Task` class can be imported and instantiated.

### [P1-CORE-02] Implement In-Memory Storage
*   **Description**: Implement the `Storage` class to manage tasks in memory (CRUD operations).
*   **Prerequisites**: P1-CORE-01.
*   **Input**: Plan Section 2.2 & 3.1.
*   **Steps**:
    1.  Create `todo_app/storage.py`.
    2.  Implement `add_task(title, description)`: auto-increment ID.
    3.  Implement `get_all_tasks()`: return list.
    4.  Implement `get_task(id)`: lookup by ID.
    5.  Implement `update_task(id, ...)`: updates fields if exists.
    6.  Implement `delete_task(id)`: removes from dict.
    7.  Implement `toggle_status(id)`: switches status logic.
*   **Artifacts**: `todo_app/storage.py`.
*   **Success Criteria**: All methods work logically in a standalone script (or REPL).

## 2. CLI Fundamentals

### [P1-CLI-01] Basic CLI Skeleton & Menu
*   **Description**: Create the CLI module with formatting helpers and the main menu display.
*   **Prerequisites**: P1-CORE-01.
*   **Input**: Plan Section 3.2.
*   **Steps**:
    1.  Create `todo_app/cli.py`.
    2.  Implement `show_menu()`: prints options 1-6.
    3.  Implement `get_user_choice()`: Validates input is int 1-6.
    4.  Implement `show_error(msg)` and `show_success(msg)` helpers.
*   **Artifacts**: `todo_app/cli.py`.
*   **Success Criteria**: Menu displays cleanly; invalid input is caught.

### [P1-CLI-02] Task Display & Inputs
*   **Description**: Add functions to `cli.py` for displaying tasks and collecting user input.
*   **Prerequisites**: P1-CLI-01.
*   **Input**: Spec Section 3.2, Plan 3.2.
*   **Steps**:
    1.  Implement `display_tasks(tasks)`: Table-like print format (ID | Title | Status).
    2.  Implement `prompt_add_task()`: Returns (title, desc). Checks title not empty.
    3.  Implement `prompt_id()`: Generic prompt for ID input.
*   **Artifacts**: `todo_app/cli.py`.
*   **Success Criteria**: Tasks print neatly; empty title input triggers re-prompt or error.

## 3. Application Application Flow

### [P1-APP-01] Main Controller & Loop
*   **Description**: Wire everything together in `main.py`.
*   **Prerequisites**: P1-CORE-02, P1-CLI-02.
*   **Input**: Plan Section 3.3.
*   **Steps**:
    1.  Create `todo_app/main.py`.
    2.  Instantiate `Storage`.
    3.  Create `while True` loop.
    4.  Connect Menu Choice 6 to `break` (Exit).
    5.  Connect Menu Choice 2 to `storage.get_all_tasks()` -> `cli.display_tasks()`.
*   **Artifacts**: `todo_app/main.py`.
*   **Success Criteria**: Can run app, view menu, view empty list, and exit.

### [P1-APP-02] Implement "Add Task" Workflow
*   **Description**: Connect the "Add" menu option.
*   **Prerequisites**: P1-APP-01.
*   **Steps**:
    1.  In `main.py` (Choice 1): Call `cli.prompt_add_task()`.
    2.  Pass data to `storage.add_task()`.
    3.  Show success message with new ID.
*   **Success Criteria**: Added task appears in the List view.

### [P1-APP-03] Implement "Update/Delete" Workflow
*   **Description**: Connect Update (3) and Delete (4) options.
*   **Prerequisites**: P1-APP-02.
*   **Steps**:
    1.  **Update**: Prompt ID -> Check exists -> Prompt Data -> Update -> Msg.
    2.  **Delete**: Prompt ID -> Confirm(optional) -> Delete -> Msg.
    3.  Handle "ID not found" errors gracefully using `cli.show_error`.
*   **Success Criteria**: Can edit and remove tasks; invalid IDs show error without crashing.

### [P1-APP-04] Implement "Toggle Status" Workflow
*   **Description**: Connect Toggle Status (5) option.
*   **Prerequisites**: P1-APP-03.
*   **Steps**:
    1.  Prompt ID.
    2.  Call `storage.toggle_status()`.
    3.  Show result (e.g., "Task 1 marked Completed").
*   **Success Criteria**: Status changes reflect in List view.

## 4. Final Polish

### [P1-FIN-01] Final Verification
*   **Description**: Walk through every user story in the Spec to ensure compliance.
*   **Prerequisites**: All P1-APP tasks.
*   **Steps**:
    1.  Run through the full CLI Interaction Flow defined in Spec.
    2.  Verify "Anti-Requirements" (No files created, etc.).
*   **Success Criteria**: All Acceptance Criteria passed.
