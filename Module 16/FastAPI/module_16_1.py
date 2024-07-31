from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root() -> str:
	return 'Main Page'


@app.get("/user/admin")
async  def admin() -> str:
	return "Logged in as administrator"


@app.get("/user")
async def user(username: str, age: int) -> str:
	return f'User\'s information. Name: <{username}>, Age: <{age}>'


@app.get("/user/{user_id}")
async def user(user_id: int) -> str:
	return f'You logged in as user № <{user_id}>'



