from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .booking import Booking
    from .vehicle import Vehicle
    from .payment import Payment

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(10), nullable=False)
    dob = Column(Date, nullable=False)
    vehicles = relationship('Vehicle', back_populates='user')
    bookings = relationship('Booking', back_populates='user')
    payments = relationship('Payment', back_populates='user')