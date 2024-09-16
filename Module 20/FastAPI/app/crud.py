from sqlalchemy.orm import Session
from models import Customer, QRcodes
from schemas import CreateCustomer
from fastapi import HTTPException
import bcrypt


def get_customer(db: Session, email: str):
	return db.query(Customer).filter(Customer.email == email).first()


def get_customer_id(db: Session, email: str):
	return db.query(Customer).filter(Customer.email == email).first()


def create_customer(db: Session, customer: CreateCustomer):
	existing_customer = get_customer(db, customer.email)
	if existing_customer:
		raise HTTPException(status_code=400, detail="User already exists")
	new_customer = Customer(
		email=customer.email,
		name=customer.name,
		password=bcrypt.hashpw(customer.password.encode('utf-8'), bcrypt.gensalt())
	)
	db.add(new_customer)
	db.commit()
	db.refresh(new_customer)
	return new_customer


def create_qrcode(db: Session, user_id: int, qrcode_data: bytes, q_name: str):
	new_qrcode = QRcodes(qrcode=qrcode_data, user_id=user_id, q_name=q_name)
	db.add(new_qrcode)
	db.commit()
	db.refresh(new_qrcode)
	return new_qrcode


def get_qrcodes_by_user(db: Session, user_id: int):
	return db.query(QRcodes).filter(QRcodes.user_id == user_id).all()


def delete_qrcode(db: Session, code_id: int, user_id: int):
	code = db.query(QRcodes).filter(QRcodes.id == code_id, QRcodes.user_id == user_id).first()
	if not code:
		raise HTTPException(status_code=404, detail="QR code not found")
	db.delete(code)
	db.commit()


def get_qrcode_by_id(db: Session, code_id: int, user_id: int):
	code = db.query(QRcodes).filter(QRcodes.id == code_id, QRcodes.user_id == user_id).first()
	if not code:
		raise HTTPException(status_code=404, detail="QR code not found")
	return code
