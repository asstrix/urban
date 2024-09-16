from fastapi import Request, APIRouter, Depends, HTTPException, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import schemas, crud, bcrypt
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from urllib.parse import urlencode


router = APIRouter(prefix="/customer", tags=["customer"])
templates = Jinja2Templates(directory="templates")


@router.get("/main", response_class=HTMLResponse)
async def main_page(request: Request):
    user = request.session.get('user')  # Получаем имя пользователя из сессии
    return templates.TemplateResponse("main.html", {"request": request, "user": user})


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/customer/login", status_code=303)


@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/login")
async def login_user(request: Request, db: Session = Depends(get_db), email: str = Form(...), password: str = Form(...)):
    user = crud.get_customer(db=db, email=email)
    if not user:
        query_params = urlencode({"message": "User does not exist."})
        return RedirectResponse(url=f"/customer/login?{query_params}", status_code=status.HTTP_303_SEE_OTHER)
    if not bcrypt.checkpw(password.encode('utf-8'), user.password):
        query_params = urlencode({"message": "Incorrect password."})
        return RedirectResponse(url=f"/customer/login?{query_params}", status_code=status.HTTP_303_SEE_OTHER)
    request.session['user'] = user.name
    return RedirectResponse(url="/customer/main", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/register")
def register_user(name: str = Form(...), email: str = Form(...), password: str = Form(...), password2: str = Form(...), db: Session = Depends(get_db)):
    if password != password2:
        query_params = urlencode({"message": "Passwords do not match."})
        return RedirectResponse(url=f"/customer/register?{query_params}", status_code=303)
    customer_data = schemas.CreateCustomer(name=name, email=email, password=password)
    try:
        crud.create_customer(db=db, customer=customer_data)
        query_params = urlencode({"message": "User has been successfully registered."})
        return RedirectResponse(url=f"/customer/login?{query_params}", status_code=303)
    except HTTPException as e:
        query_params = urlencode({"message": e.detail})
        return RedirectResponse(url=f"/customer/register?{query_params}", status_code=303)