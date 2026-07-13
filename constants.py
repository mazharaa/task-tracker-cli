from enum import Enum

class Command(Enum):
  ADD = "add"
  UPDATE = "update"
  DELETE = "delete"
  MARK_IN_PROGRESS = "mark-in-progress"
  MARK_DONE = "mark-done"
  LIST = "list"
  LIST_DONE = "list done"
  LIST_TODO = "list todo"
  LIST_IN_PROGRESS = "list in-progress"
  EXIT = "exit"

class Status(Enum):
  TODO = "todo"
  IN_PROGRESS = "in progress"
  DONE = "done"