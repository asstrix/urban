from backend.db import Base
from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    password = Column(String)
    qrcodes = relationship("QRcodes", back_populates="customer")


class QRcodes(Base):
    __tablename__ = 'qrcodes'
    id = Column(Integer, primary_key=True, index=True)
    qrcode = Column(LargeBinary)
    user_id = Column(Integer, ForeignKey('customer.id'))
    q_name = Column(String)
    customer = relationship("Customer", back_populates="qrcodes")
