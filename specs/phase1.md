# Phase I Specification: Evolution of Todo (Console Basics)

## 1. Overview & Scope
This phase focuses on the absolute fundamentals of the Todo application. It is a strictly **in-memory Python console application** designed for a **single user**.

**Strict Scope Limitations:**
*   **Persistence**: None (Data is lost when the app exits).
*   **Interface**: CLI / Console (Text-based menu).
*   **User Base**: Single User (No login/auth).
*   **Network**: Local only (No Web/API).

## 2. Data Model
The application manages a single entity: `Task`.

### `Task` Entity
| Field | Type | Required | Constraints | Description |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `int` | Yes | Unique, Auto-incrementing | Unique identifier for the task. |
| `title` | `str` | Yes | Non-empty, Max 100 chars | Short summary of the task. |
| `description` | `str` | No | Max 500 chars | Detailed explanation (optional). |
| `status` | `str` | Yes | "Pending" or "Completed" | Current state of the task (Default: "Pending"). |

## 3. User Stories & Functional Requirements

### 3.1 Add Task
*   **Story**: As a user, I want to create a new task so I can track what I need to do.
*   **Input**: Title (Required), Description (Optional).
*   **Process**: System assigns a new unique ID and default status "Pending".
*   **Output**: Confirmation message with the created Task ID.

### 3.2 View Task List
*   **Story**: As a user, I want to see all my tasks so I can prioritize my work.
*   **Input**: Selection from menu.
*   **Display**: Table or list format showing ID, Title, Status.
*   **Edge Case**: If list is empty, show "No tasks available."

### 3.3 Update Task
*   **Story**: As a user, I want to edit a task's details in case I made a mistake or requirements changed.
*   **Input**: Task ID. fields to update (Title, Description).
*   **Constraint**: Cannot change ID.
*   **Error**: If ID not found, display error.

### 3.4 Delete Task
*   **Story**: As a user, I want to remove a task that is no longer relevant.
*   **Input**: Task ID.
*   **Output**: Confirmation of deletion.
*   **Error**: If ID not found, display error.

### 3.5 Mark Task Complete / Incomplete
*   **Story**: As a user, I want to toggle a task's status to track progress.
*   **Input**: Task ID.
*   **Action**: Toggle status between "Pending" and "Completed".

## 4. CLI Interaction Flow
The application acts as a loop presenting a main menu until exit.

**Main Menu:**
```text
=== Todo App (Phase I) ===
1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Toggle Task Status
6. Exit
Select an option: 
```

**Interaction Patterns:**
*   **Prompts**: `Enter Task ID:`, `Enter Title: `
*   **Feedback**: `Task [ID] added successfully.`
*   **Errors**: `Error: Task with ID [ID] not found.`

## 5. Acceptance Criteria
1.  **App Start**: Application starts without errors and shows the main menu.
2.  **Add**: Can add a task; it appears in the list.
3.  **List**: Shows all added tasks with correct IDs and statuses.
4.  **Persistence Check**: Restarting the app clears all data (verifies in-memory only).
5.  **Validation**: prevents adding a task with empty title.
6.  **Error Handling**: Entering a non-existent ID for Update/Delete/Toggle shows a friendly error message, not a crash.

## 6. Technical Constraints
*   **Language**: Python 3.x
*   **Storage**: In-memory list or dictionary variables ONLY.
*   **Third-party libs**: Standard library only (no `pip install` required for core features).
*   **Structure**: standard python script or simple package.
*   **Code Quality**: Functions should be small and single-purpose.

## 7. Anti-Requirements (Phase Violation Checks)
*   **NO** Database (SQL, SQLite, JSON files).
*   **NO** Web Frameworks (Flask, Django, FastAPI).
*   **NO** Authentication logic.
*   **NO** Async functionality.
