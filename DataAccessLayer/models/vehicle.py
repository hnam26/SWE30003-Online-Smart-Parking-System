from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .booking import Booking
    from .user import User

Base = declarative_base()


class Vehicle(Base):
    __tablename__ = 'Vehicle'
    vehicle_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    license_plate = Column(String(20), unique=True, nullable=False)
    vehicle_type = Column(String(50), nullable=False)
    user = relationship('User', back_populates='vehicles')
    bookings = relationship('Booking', back_populates='vehicle')