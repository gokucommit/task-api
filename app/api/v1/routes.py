from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schema import task as schema
from app.services import task_service

router = APIRouter()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
    
@router.get("/tasks", response_model=list[schema.TaskInDB])
def get_all_task(db: Session = Depends(get_db)):
  return task_service.get_tasks(db)

@router.get("/task/{task_id}", response_model=schema.TaskInDB)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
  task = task_service.get_tasks_by_id(db, task_id)
  if not task:
    raise HTTPException(status_code=404, detail="Task not found")
  return task

@router.post("/tasks", response_model=schema.TaskInDB)
def create_task(task: schema.TaskCreate, db: Session = Depends(get_db)):
  return task_service.create_task(db, task)

@router.put("/tasks/{task_id}", response_model=schema.TaskInDB)
def update_task(task: schema.TaskUpdate, task_id: int, db: Session = Depends(get_db)):
  return task_service.update_task(db, task_id, task)

@router.delete("/task/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
  deleted_task = task_service.get_tasks_by_id(db, task_id)
  if not deleted_task:
    raise HTTPException(status_code=404, detail="Task not found")
  task_service.delete_task(db, task_id)
  return {"detail": "Deleted successfully!"}
