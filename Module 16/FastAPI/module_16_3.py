from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Name: Example, Age: 18'}


@app.get('/users')
async def get_users() -> dict:
	return users


@app.post('/user/{username}/{age}')
async def add_user(username: str = Path(min_length=5, max_length=20, description='Enter username'),
				   age: int = Path(ge=18, le=120, description='Enter age')) -> str:
	id_ = str(int(max(users, key=int)) + 1)
	users[id_] = f"Name: {username}, Age: {age}"
	return f'User <{id_}> has been registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str = Path(min_length=1, max_length=100, description='Enter user id'),
					  username: str = Path(min_length=5, max_length=20, description='Enter username'),
					  age: int = Path(ge=18, le=120, description='Enter age')):
	users[user_id] = f'Name: {username}, Age: {age}'
	return f'The user <{user_id}> has been updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: str = Path(min_length=1, max_length=100)):
	users.pop(user_id)
	return f'The user <{user_id}> has been deleted'