from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/user/{user_id}")
async def get_user_id(user_id: int = Path(ge=1, le=100)) -> str:
	return f'You logged in as user № <{user_id}>'


@app.get("/user/{username}/{age}")
async def get_user_id(username: str = Path(min_length=5, max_length=20, description='Enter username'),
					  age: int = Path(ge=18, le=120, description='Enter age')) -> str:
	return f'Username: {username}, Age: {age}'





