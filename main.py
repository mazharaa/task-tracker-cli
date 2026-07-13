from constants import Command
from constants import Status
from datetime import datetime, timezone
from pathlib import Path
import json
import sys
import re

task_path = Path("task_list.json")

def main():
  print("Welcome to Task Tracker CLI App")
  print("Here the command guide to use this app:")
  print("1. 'add' follows with task desc wrapped by double quote to add new task")
  print("2. 'update' follows with taskId and updated task desc wrapped by double quote to update existing task")
  print("3. 'delete' follows with taskId to delete existing task")
  print("4. 'mark-in-progress' follows with taskId to mark the task is in progress")
  print("5. 'mark-done' follows with taskId to mark the task is done")
  print("6. 'list' to list all tasks")
  print("7. 'list done' to list all done tasks")
  print("8. 'list todo' to list all todo tasks")
  print("9. 'list in-progress' to list all in-progress tasks")
  print("10. 'exit' to exit from Task Tracker CLI App")

  cli_input()

def cli_input():
  command = input("task-cli ")
  task_command = command.split()[0]

  if task_command == Command.ADD.value:
    task_desc = re.search(r'"(.*?)"', command)
    
    if task_desc:
      add_task(task_desc.group(1))

  elif task_command == Command.DELETE.value:
    delete_task(command.split()[1])
  elif task_command == Command.EXIT.value:
    exit_app()
  elif task_command == Command.UPDATE.value:
    task_desc = re.search(r'"(.*?)"', command)
    
    if task_desc:
      update_task(command.split()[1], task_desc.group())

def add_task(task_desc):
  task_id = 1
  status = Status.TODO.value
  now = datetime.now(timezone.utc).isoformat()

  task = {
    "id": task_id,
    "description": task_desc,
    "status": status,
    "createdAt": now,
    "updatedAt": None
  }

  # Auto-create if missing
  if not task_path.exists():
    task_path.write_text(json.dumps([task], indent=2))
  else:
    # Read
    data = json.loads(task_path.read_text())
    task["id"] = data[-1]["id"] + 1
    data.append(task)
    task_path.write_text(json.dumps(data, indent=2))

  cli_input()

def delete_task(id):
  id = int(id)
  if not task_path.exists():
    print("No task to delete, task is empty")
  else:
    # Read
    data = json.loads(task_path.read_text())
    task_by_id = {task["id"]: task for task in data}
    data.remove(task_by_id.get(id))
    task_path.write_text(json.dumps(data, indent=2))
    
  cli_input()

def exit_app():
  sys.exit()

def update_task(id, desc):
  id = int(id)

  if not task_path.exists():
    print("No task to update, task is empty")
  else:
    # Read
    data = json.loads(task_path.read_text())
    task_by_id = {task["id"]: task for task in data}
    task_by_id.get(id)["description"] = desc
    task_path.write_text(json.dumps(data, indent=2))

  cli_input()

if __name__ == "__main__":
  main()