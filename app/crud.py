from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


def create_task(db: Session, task_data: TaskCreate, owner_id: int):
    task = Task(**task_data.model_dump(), owner_id=owner_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(
    db: Session,
    owner_id: int,
    status: str | None = None,
    priority: str | None = None,
    skip: int = 0,
    limit: int = 20,
):
    query = db.query(Task).filter(Task.owner_id == owner_id)
    if status:
        query = query.filter(Task.status == status)
    if priority:
        query = query.filter(Task.priority == priority)
    return query.offset(skip).limit(limit).all()


def get_task(db: Session, task_id: int, owner_id: int):
    return db.query(Task).filter(Task.id == task_id, Task.owner_id == owner_id).first()


def update_task(db: Session, task_id: int, task_data: TaskUpdate, owner_id: int):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == owner_id).first()
    if not task:
        return None
    for key, value in task_data.model_dump(exclude_unset=True).items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int, owner_id: int):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == owner_id).first()
    if not task:
        return False
    db.delete(task)
    db.commit()
    return True
