# Task Tracker CLI

This is a solution for the [Task Tracker](https://roadmap.sh/projects/task-tracker) project on roadmap.sh.

A simple command-line interface (CLI) application to track and manage your tasks. This tool helps you keep track of what you need to do, what you have done, and what you are currently working on.

## Features

The application allows you to:

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as in progress
- Mark tasks as done
- List all tasks

## Prerequisites

- Python 3.x installed on your system

## Installation

1. Clone this repository or download the files
2. Navigate to the project directory

```bash
cd Task-tracker
```

## Usage

You can run the task tracker using either of these methods:

### Method 1: Using Python directly
```bash
python task_cli.py <command> [arguments]
```

### Method 2: Using the batch file (Windows only)
```bash
task-cli <command> [arguments]
```

## Commands

### Adding a new task
```bash
python task_cli.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### Updating a task
```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
# Output: updated task succesfully
```

### Deleting a task
```bash
python task_cli.py delete 1
```

### Marking a task as in progress
```bash
python task_cli.py mark-in-progress 1
```

### Marking a task as done
```bash
python task_cli.py mark-done 1
```

### Listing all tasks
```bash
python task_cli.py list
# Output format: ID | status | description
# Example: 1 | todo | Buy groceries
```

## Task Properties

Each task has the following properties:

- **id**: A unique identifier for the task (auto-generated)
- **description**: A short description of the task
- **status**: The status of the task (`todo`, `in-progress`, or `done`)
- **createdAt**: The date and time when the task was created
- **updatedAt**: The date and time when the task was last updated

## Data Storage

Tasks are stored in a `tasks.json` file in the same directory as the script. This file is automatically created when you add your first task.

## Example Workflow

```bash
# Add some tasks
python task_cli.py add "Buy groceries"
python task_cli.py add "Read a book"
python task_cli.py add "Go for a walk"

# Mark a task as in progress
python task_cli.py mark-in-progress 1

# Mark a task as done
python task_cli.py mark-done 2

# Update a task description
python task_cli.py update 3 "Go for a 30-minute walk"

# List all tasks
python task_cli.py list

# Delete a task
python task_cli.py delete 1
```

## Project Structure

```
Task-tracker/
├── task_cli.py      # Main Python script
├── task-cli.bat     # Windows batch file wrapper
├── tasks.json       # JSON file storing tasks (auto-generated)
└── README.md        # This file
```

## Technical Details

- Built with Python 3
- Uses native `json` module for data storage
- Uses native `os` and `sys` modules for file operations
- No external dependencies required

## License

This project is part of the [roadmap.sh](https://roadmap.sh) backend development projects.

