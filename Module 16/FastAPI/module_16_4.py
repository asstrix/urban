from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List
app = FastAPI()

users = []


class User(BaseModel):
    id: int = Path(ge=1, le=100)
    username: str = Path(min_length=5, max_length=20)
    age: int = Path(ge=18, le=120)


@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def add_user(user: User):
    if not len(users):
        User.id = 1
    else:
        User.id = str(len(users) + 1)
    users.append(user)
    return f'User <{user.id}> has been registered'


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user: User) -> str:
    try:
        users[user.id] = user
        return f'The user <{user.id}> has been updated.'
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=1, le=100)):
    try:
        users.pop(user_id)
        return f'The user <{user_id}> has been deleted.'
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")