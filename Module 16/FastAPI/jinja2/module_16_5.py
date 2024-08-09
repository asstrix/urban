from fastapi import FastAPI, HTTPException, Path, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    user_id: int = None
    username: str
    age: int = None


@app.get('/')
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/user/{user_id}')
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id - 1]})


@app.post('/user/{username}/{age}')
async def post_user(username: str = Path(min_length=5, max_length=20), age: int = Path(ge=18, le=120)):
    user_id = len(users) + 1
    new_user = User(user_id=user_id, username=username, age=age)
    users.append(new_user)
    return f'User <{new_user.user_id}> has been registered'


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: int = Path(ge=1, le=100),
                username: str = Path(min_length=5, max_length=20, description='Enter username'),
                age: int = Path(ge=18, le=120, description='Enter age')) -> str:
    User.username = username
    User.age = age
    User.user_id = user_id - 1
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