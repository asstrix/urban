from fastapi import FastAPI, Request, Depends, HTTPException, Form, status, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse
from starlette.middleware.sessions import SessionMiddleware
from sqlalchemy.orm import Session
from backend.db_depends import get_db
import schemas, crud, bcrypt, qrcode, base64, uvicorn
from urllib.parse import urlencode
from io import BytesIO
from PIL import Image

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="@S7twGRuagfEw#VX")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
	user_id = request.session.get('user_id')
	if user_id:
		return RedirectResponse(url="/main")
	return RedirectResponse(url="/login")


@app.get("/main", response_class=HTMLResponse)
async def main_page(request: Request):
	user = request.session.get('user')
	return templates.TemplateResponse("main.html", {
		"request": request,
		"user": user

	})


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
	return templates.TemplateResponse("login.html", {"request": request})


@app.get("/logout")
async def logout(request: Request):
	request.session.clear()
	return RedirectResponse(url="/login", status_code=303)


@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
	return templates.TemplateResponse("register.html", {"request": request})


@app.post("/login")
async def login_user(
    request: Request,
    db: Session = Depends(get_db),
    email: str = Form(...),
    password: str = Form(...),
):
	user = crud.get_customer(db=db, email=email)
	if not user:
		query_params = urlencode({"message": "User does not exist."})
		return RedirectResponse(url=f"/login?{query_params}", status_code=status.HTTP_303_SEE_OTHER)
	if not bcrypt.checkpw(password.encode('utf-8'), user.password):
		query_params = urlencode({"message": "Incorrect password."})
		return RedirectResponse(url=f"/login?{query_params}", status_code=status.HTTP_303_SEE_OTHER)
	request.session['user'] = user.name
	request.session['user_id'] = user.id
	return RedirectResponse(url="/main", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/register")
async def register_user(
		name: str = Form(...),
		email: str = Form(...),
		password: str = Form(...),
		password2: str = Form(...),
		db: Session = Depends(get_db),
):
	if password != password2:
		query_params = urlencode({"message": "Passwords do not match."})
		return RedirectResponse(url=f"/register?{query_params}", status_code=303)
	password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
	customer_data = schemas.CreateCustomer(name=name, email=email, password=password)
	try:
		crud.create_customer(db=db, customer=customer_data)
		query_params = urlencode({"message": "User has been successfully registered."})
		return RedirectResponse(url=f"/login?{query_params}", status_code=303)
	except HTTPException as e:
		query_params = urlencode({"message": e.detail})
		return RedirectResponse(url=f"/register?{query_params}", status_code=303)


@app.post("/create")
async def create_qr_code(
		request: Request,
		db: Session = Depends(get_db),
		data: str = Form(...),
		size: int = Form(...),
		transparent: bool = Form(False),
		background: UploadFile = File(None),
		logo: UploadFile = File(None),
		color: str = Form(...)
):
	try:
		qr = qrcode.QRCode(
			version=size,
			error_correction=qrcode.constants.ERROR_CORRECT_L,
			box_size=10,
			border=4,
		)
		qr.add_data(data)
		qr.make(fit=True)
		if background.filename:
			back_color = "transparent"
		else:
			if transparent:
				back_color = "transparent"
			else:
				back_color = "black" if color == "#ffffff" else "white"
		img = qr.make_image(
			fill_color=color,
			back_color=back_color
		).convert("RGBA")
		if background.filename:
			background_image = Image.open(BytesIO(await background.read())).convert("RGBA")
			background_image = background_image.resize(img.size)
			img = Image.alpha_composite(background_image, img)
		if logo.filename:
			logo_image = Image.open(BytesIO(await logo.read())).convert("RGBA")
			qr_width, qr_height = img.size
			logo_size = int(min(qr_width, qr_height) * 0.2)
			logo_image = logo_image.resize((logo_size, logo_size), Image.LANCZOS)
			logo_image.putalpha(200)
			logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
			img.paste(logo_image, logo_position, logo_image)
		buffer = BytesIO()
		img.save(buffer, format="PNG")
		buffer.seek(0)
		qr_code_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
		qr_code_data = f"data:image/png;base64,{qr_code_base64}"
		user_id = request.session.get('user_id')
		user = request.session.get('user')
		crud.create_qrcode(db=db, user_id=user_id, qrcode_data=buffer.getvalue(), q_name=f"{data}")
		return templates.TemplateResponse("main.html", {"request": request, "qr_code": qr_code_data, "user": user})
	except Exception as e:
		return templates.TemplateResponse("main.html", {"request": request, "error": f"Error generating QR code: {e}"}, status_code=500)


@app.get("/qrcodes")
async def my_qrcodes(request: Request, db: Session = Depends(get_db)):
	user_id = request.session.get('user_id')
	qrcodes = crud.get_qrcodes_by_user(db=db, user_id=user_id)
	user = request.session.get('user')
	return templates.TemplateResponse("qrcodes.html", {"request": request, "codes": qrcodes, "user": user})


@app.get("/qrcodes/{code_id}/delete")
async def delete_qrcode(
		request: Request,
		code_id: int,
		db: Session = Depends(get_db),
	):
	user_id = request.session.get('user_id')
	try:
		crud.delete_qrcode(db=db, code_id=code_id, user_id=user_id)
	except HTTPException as e:
		return RedirectResponse(url="/qrcodes", status_code=404)
	return RedirectResponse(url="/qrcodes", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/qrcodes/{code_id}/download")
async def download_qrcode(request: Request, code_id: int, db: Session = Depends(get_db)):
	user_id = request.session.get('user_id')
	if not user_id:
		raise HTTPException(status_code=401, detail="User not authenticated")
	code = crud.get_qrcode_by_id(db=db, code_id=code_id, user_id=user_id)
	buffer = BytesIO(code.qrcode)
	buffer.seek(0)
	file_name = code.q_name.replace('https://', '') + ".png"
	return StreamingResponse(buffer, media_type="image/png", headers={
		"Content-Disposition": f"attachment; filename={file_name}"
	})


if __name__ == "__main__":
	uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)
