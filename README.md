# Task Tracker CLI

A command-line task tracker built with Python. Tasks are stored in a JSON file.

## Features

- Add, update, delete, and list tasks
- Mark tasks as in-progress or done
- Persistent storage via JSON

## Usage

```bash
python main.py

# Then inside the app:
task-cli add "Buy groceries"
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1
task-cli mark-in-progress 1
task-cli mark-done 1
task-cli list
task-cli list done
task-cli list todo
task-cli list in-progress
task-cli exit
```

## Project Structure

- main.py - Entry point and CLI logic
- constants.py - Enums for commands and statuses
- task_list.json - Data storage (auto-generated)

## Requirements

- Python 3.x

## License

MIT
