from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from models.user import User
from backend.db_depends import get_db
from schemes import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
	users = db.scalars(select(User)).all()
	return users


@router.get('/user_id')
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
	user = db.scalars(select(User).where(User.id == user_id)).all()
	if len(user) == 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail='User was not found'
		)
	return user


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], c: CreateUser):
	db.execute(insert(User).values(
		username=c.username,
		firstname=c.firstname,
		lastname=c.lastname,
		age=c.age,
		slug=slugify(c.username)
	))
	db.commit()
	return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_user(user_id: int, db: Annotated[Session, Depends(get_db)], u: UpdateUser):
	user = db.scalars(select(User).where(User.id == user_id)).all()
	if len(user) == 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail='User was not found'
		)
	db.execute(update(User).where(User.id == user_id).values(
		username=u.username,
		firstname=u.firstname,
		lastname=u.lastname,
		age=u.age,
		slug=slugify(u.username)
	))
	db.commit()
	return {'status_code': status.HTTP_200_OK, 'transaction': 'User has been updated successfully!'}


@router.delete('/delete')
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
	user = db.scalars(select(User).where(User.id == user_id)).all()
	if len(user) == 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail='User was not found'
		)
	db.execute(delete(User).where(User.id == user_id))
	db.commit()
	return {'status_code': status.HTTP_200_OK, 'transaction': 'User has been deleted successfully!'}