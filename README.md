# Task Tracker CLI

Project Reference: https://roadmap.sh/projects/task-tracker

A simple **Command Line Interface (CLI)** task tracker built with **Python**. This project helps you practice Python basics such as file handling, JSON, command-line arguments, and working with dates.

You can:

* Add tasks
* List tasks
* Update tasks
* Mark tasks as in-progress or done
* Delete tasks

---

## Project Structure

```
task-tracker-cli/
├── task-cli.py   # Main CLI application (run with: python task_cli.py)
├── .gitignore    # Tells Git to ignore your local tasks.json
├── LICENSE       # MIT License details
└── README.md     # Project documentation and usage guide
```

---

## Requirements

* Python **3.8+**
* No external libraries required (uses only Python standard library)

---

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/deannabulaclac/task-tracker-cli.git
   cd task-tracker-cli
   ```

2. **Run the CLI**

   ```bash
   python task-cli.py
   ```

If no command is provided, the CLI will show usage instructions.

---

## How It Works

* Tasks are stored in a `tasks.json` file
* Each task contains:

  * `id` (unique number)
  * `description`
  * `status` (`todo`, `in-progress`, `done`)
  * `createdAt`
  * `updatedAt`

The JSON file is automatically created when you add your first task.

---

## Commands & Usage

### Add a Task

```bash
python task-cli.py add "Buy groceries"
```

### List All Tasks

```bash
python task-cli.py list
```

### List Tasks by Status

```bash
python task-cli.py list todo
python task-cli.py list in-progress
python task-cli.py list done
```

### Update a Task Description

```bash
python task-cli.py update 1 "Buy groceries and cook dinner"
```

### Mark Task as In Progress

```bash
python task-cli.py mark-in-progress 1
```

### Mark Task as Done

```bash
python task-cli.py mark-done 1
```

### Delete a Task

```bash
python task-cli.py delete 1
```

---


