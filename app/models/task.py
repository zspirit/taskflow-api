from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, default="")
    priority = Column(String, default="medium")  # low, medium, high
    status = Column(String, default="todo")  # todo, in_progress, done
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
