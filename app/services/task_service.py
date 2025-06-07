from sqlalchemy.orm import Session
from app.models.task import Task
from app.schema.task import TaskCreate, TaskUpdate

def get_tasks(db: Session):
  return db.query(Task).all()

def get_tasks_by_id(db: Session, task_id: int):
  return db.query(Task).filter(Task.id == task_id).first()

def create_task(db: Session, task: TaskCreate):
  db_task = Task(**task.model_dump())
  db.add(db_task)
  db.commit()
  db.refresh()
  return db_task