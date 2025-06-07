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
  db.refresh(db_task)
  return db_task

def update_task(db: Session, task_id: int, task_data: TaskUpdate):
  task = get_tasks_by_id(db, task_id)
  if task:
    for field, value in task_data.model_dump(exclude_unset=True).items():
      setattr(task, field, value)
    db.commit()
    db.refresh(task)
  return task

def delete_task(db: Session, task_id: int):
  task = get_tasks_by_id(task_id)
  if task:
    db.delete(task)
    db.commit()
  return task