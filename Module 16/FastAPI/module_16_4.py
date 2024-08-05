from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List
app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int = None


@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def add_user(username: str = Path(min_length=5, max_length=20), age: int = Path(ge=18, le=120)):
    User.username = username
    User.age = age
    if not len(users):
        User.id = 1
    else:
        User.id = len(users) + 1
    users.append(User)
    return f'User <{User.id}> has been registered'


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: int = Path(ge=1, le=100),
                username: str = Path(min_length=5, max_length=20, description='Enter username'),
                age: int = Path(ge=18, le=120, description='Enter age')) -> str:
    User.username = username
    User.age = age
    User.id = user_id - 1
    try:
        users[User.id] = User
        return f'The user <{user_id}> has been updated.'
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=1, le=100)):
    try:
        users.pop(user_id - 1)
        return f'The user <{user_id}> has been deleted.'
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")