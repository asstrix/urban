from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root_page() -> str:
	return 'Main Page'


@app.get("/user/admin")
async def login_admin() -> str:
	return "Logged in as administrator"


@app.get("/user")
async def get_user_info(username: str, age: int) -> str:
	return f'User\'s information. Name: <{username}>, Age: <{age}>'


@app.get("/user/{user_id}")
async def get_user_id(user_id: int) -> str:
	return f'You logged in as user № <{user_id}>'



