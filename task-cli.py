import sys
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

def load_tasks():
    # Load tasks from JSON file; return empty list if file is missing or corrupt
    if not os.path.exists(FILE_NAME):
        return[]
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return[]
    
def save_tasks(tasks):
    # Write current task list to JSON file with 4-space indentation
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent = 4)

def add_task(description):
    # Create a new task with unique ID and timestamps
    tasks = load_tasks()

    # Calculate next ID based on the highest existing ID
    new_id = max([t["id"] for t in tasks], default=0) + 1

    new_task = {
        "id": new_id,
        "description": description,
        "status":"todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def list_tasks(status_filter=None):
    # Print tasks to console, optionally filtered by status
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return
    
    if status_filter:
        tasks = [t for t in tasks if t["status"] == status_filter]
        if not tasks:
            print(f"No tasks found with status: {status_filter}")
            return
        
    for task in tasks:
        # Format ISO timestamp to a human-readable string
        dt = datetime.fromisoformat(task['createdAt'])
        readable_date = dt.strftime("%b %d, %I:%M %p")
        print(f"[{task['id']}] {task['description']} - {task['status']} (Created: {readable_date})")

def mark_task(task_id, status):
    # Updates the completion status of a task (e.g., 'to-do', 'in-progress', 'done')
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated.")
            return
    
    print(f"Error: Task with ID {task_id} not found.")

def delete_task(task_id):
    # Removes a task from the list based on its ID
    tasks = load_tasks()

    # Check if a task was actually removed
    new_tasks = [task for task in tasks if task["id"] != task_id]

    # 
    if len(tasks) == len(new_tasks):
        print("Task not found.")
        return
    
    save_tasks(new_tasks)
    print("Task deleted.")

def update_task(task_id, new_description):
    # Edits the description text of an existing task
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return

    print(f"Error: Task with ID {task_id} not found")

# CLI HANDLING
# Require at least one command argument
if len(sys.argv) < 2:
    print("Usage: python task_cli.py [add|list|update|delete|mark-done|mark-in-progress]")
    sys.exit() 

command = sys.argv[1].lower()

if command == "add":
    if len(sys.argv) < 3:
        print("Error: Please provide a task description.")
    else:
        add_task(sys.argv[2])
elif command == "list":
    if len(sys.argv) > 2:
        list_tasks(sys.argv[2])
    else:
        list_tasks()
elif command in ["mark-done", "mark-in-progress", "delete"]:
    if len(sys.argv) < 3:
        print(f"Error: Please provide a task ID for {command}.")
    else:
        try:
            # Ensure the ID argument is a valid integer
            task_id = int(sys.argv[2])
            if command == "mark-done":
                mark_task(task_id, "done")
            elif command == "mark-in-progress":
                mark_task(task_id, "in-progress")
            elif command == "delete":
                delete_task(task_id)
        except ValueError:
            print("Error: ID must be a number.")

elif command == "update":
    if len(sys.argv) < 4:
        print("Usage: update <ID> <description>")
    else:
        try:
            update_task(int(sys.argv[2]), sys.argv[3])
        except ValueError:
            print("Error: ID must be a number.")
else:
    print("Unknown command.")

