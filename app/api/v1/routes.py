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
    
@router.post("/tasks", response_model=schema.TaskInDB)
def create_task(task: schema.TaskCreate, db: Session = Depends(get_db)):
  return task_service.create_task(db, task)