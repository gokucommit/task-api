from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
  title: str
  description: Optional[str] = None
  
class TaskCreate(TaskBase):
  pass

class TaskUpdate(BaseModel):
  title: Optional[str] = None
  description: Optional[str] = None
  is_done: Optional[bool] = None
  
class TaskInDB(TaskBase):
  id: int
  is_done: bool
  created_at: datetime
  
  class Config:
    orm_mode = True