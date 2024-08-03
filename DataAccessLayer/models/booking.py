from sqlalchemy import Column, Integer, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship, declarative_base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .vehicle import Vehicle
    from .parkingSlot import ParkingSlot
    from .payment import Payment

Base = declarative_base()


class Booking(Base):
    __tablename__ = 'Booking'
    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('Vehicle.vehicle_id'), nullable=False)
    parking_slot_id = Column(Integer, ForeignKey('ParkingSlot.parking_slot_id'), nullable=False)
    start_time = Column(DateTime, nullable=False)
    duration = Column(DECIMAL(2, 1), nullable=False)
    user = relationship('User', back_populates='bookings')
    vehicle = relationship('Vehicle', back_populates='bookings')
    parking_slot = relationship('ParkingSlot', back_populates='bookings')
    payment = relationship('Payment', uselist=False, back_populates='booking')