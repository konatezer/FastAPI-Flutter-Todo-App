from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text
from database import Base
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    status = Column(String, default="pending")
    created_date = Column(DateTime, default=datetime.now)
    completed_date = Column(DateTime, nullable=True, default=None)
   
class CreateTaskBase(BaseModel):
    title: str
    description: str = None
    status: str = "pending"
    created_date: datetime = datetime.now()

class TaskBase(BaseModel):
    title: str
    description: str = None
    status: str = "pending"
    created_date: datetime = datetime.now()
    completed_date: Optional[datetime] = None