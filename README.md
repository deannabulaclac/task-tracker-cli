# 📝 Task Tracker CLI

A simple **Command Line Interface (CLI)** task tracker built with **Python**. This project helps you practice Python basics such as file handling, JSON, command-line arguments, and working with dates.

You can:

* Add tasks
* List tasks
* Update tasks
* Mark tasks as in-progress or done
* Delete tasks

---

## 📂 Project Structure

```
task-tracker-cli/
├── task-cli.py   # Main CLI application (run with: python task_cli.py)
├── .gitignore    # Tells Git to ignore your local tasks.json
├── LICENSE       # MIT License details
└── README.md     # Project documentation and usage guide
```

---

## ⚙️ Requirements

* Python **3.8+**
* No external libraries required (uses only Python standard library)

---

## 🚀 Getting Started

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd task-tracker
   ```

2. **Run the CLI**

   ```bash
   python task_cli.py
   ```

If no command is provided, the CLI will show usage instructions.

---

## 🧠 How It Works

* Tasks are stored in a `tasks.json` file
* Each task contains:

  * `id` (unique number)
  * `description`
  * `status` (`todo`, `in-progress`, `done`)
  * `createdAt`
  * `updatedAt`

The JSON file is automatically created when you add your first task.

---

## 📌 Commands & Usage

### ➕ Add a Task

```bash
python task_cli.py add "Buy groceries"
```

### 📋 List All Tasks

```bash
python task_cli.py list
```

### 🔍 List Tasks by Status

```bash
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done
```

### ✏️ Update a Task Description

```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

### 🔄 Mark Task as In Progress

```bash
python task_cli.py mark-in-progress 1
```

### ✅ Mark Task as Done

```bash
python task_cli.py mark-done 1
```

### 🗑️ Delete a Task

```bash
python task_cli.py delete 1
```

---

## ❗ Error Handling

* Handles missing or corrupted `tasks.json`
* Validates task IDs
* Displays helpful error messages for incorrect usage

---

## 🎯 Learning Goals

This project is great for beginners to learn:

* Python functions
* File I/O with JSON
* Command-line arguments (`sys.argv`)
* Basic error handling
* Simple project structure

---

## 🌱 Future Improvements (Optional)

* Add priority levels
* Add due dates
* Search tasks
* Use `argparse` for better CLI UX

---

## 📄 License

This project is open-source and free to use for learning purposes.

---

✨ *Built as a beginner-friendly Python project*
