from fastapi import APIRouter, HTTPException, status
from database import db_dependency
from models import TaskBase
import models

router = APIRouter()

# ==============     ENDPOINT       ====================
# Fetch all Tasks
@router.get("/task/", status_code=status.HTTP_200_OK)
async def get_all_task(db: db_dependency):
    tasks = db.query(models.Task).all()
    return tasks

# Create an task
@router.post("/task/", status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskBase, db: db_dependency):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


# Get task by id 
@router.get("/task/{task_id}", status_code=status.HTTP_200_OK)
async def get_task_by_number(task_id: str, db:db_dependency):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail=f"The task with {task_id} is not found")
    return task


# Delete task by id
@router.delete("/task/{task_id}", status_code=status.HTTP_200_OK)
async def delete_task(task_id: str, db:db_dependency):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail=f"The task with id {task_id} is not found")
    db.delete(task)
    db.commit()
    return f"Task with {task_id} has been deleted successfully "
# Update task
@router.put("/task/{task_id}")
def updated_task(task_id: int, task: TaskBase, db:db_dependency):
    task_to_update = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task_to_update is None:
        raise HTTPException(
            status_code=404,
            detail=f"The task with id {task_id} is not found"
        )

    task_to_update.title = task.title
    task_to_update.description = task.description
    task_to_update.status = task.status
    task_to_update.completed_date = task.completed_date
    db.add(task_to_update)
    db.commit()
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    return task

