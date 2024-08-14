from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from models.task import Task
from models.user import User
from backend.db_depends import get_db
from schemes import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
	tasks = db.scalars(select(Task)).all()
	return tasks


@router.get('/task_id')
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
	task = db.scalars(select(Task).where(Task.id == task_id)).all()
	if len(task) == 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail='User was not found'
		)
	return task


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], c: CreateTask):
	user = db.scalars(select(User).where(User.id == c.user_id)).all()
	if len(user) == 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail='User was not found'
		)
	db.execute(insert(Task).values(
		title=c.title,
		content=c.content,
		user_id=c.user_id,
		slug=slugify(c.title)
	))
	db.commit()
	return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_task(user_id: int, db: Annotated[Session, Depends(get_db)], u: UpdateTask):
	user = db.scalars(select(User).where(User.id == user_id)).all()
	if len(user) == 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail='User was not found'
		)
	db.execute(update(Task).where(Task.user_id == user_id).values(
		title=u.title,
		content=u.content,
		user_id=user_id,
		slug=slugify(u.title)
	))
	db.commit()
	return {'status_code': status.HTTP_200_OK, 'transaction': 'User has been updated successfully!'}


@router.delete('/delete')
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
	user = db.scalars(select(Task).where(Task.id == task_id)).all()
	if len(user) == 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail='Task was not found'
		)
	db.execute(delete(Task).where(Task.id == task_id))
	db.commit()
	return {'status_code': status.HTTP_200_OK, 'transaction': 'task has been deleted successfully!'}