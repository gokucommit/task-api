from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.db.session import Base

class Task(Base):
  __tablename__ = "tasks"
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True, nullable=False)
  description = Column(String, nullable=True)
  is_done = Column(Boolean, default=False)
  created_at = Column(DateTime, default=datetime.now)
  