from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .booking import Booking
    from .parkingLot import ParkingLot


class ParkingSlot(Base):
    __tablename__ = 'ParkingSlot'
    parking_slot_id = Column(Integer, primary_key=True, autoincrement=True)
    parking_lot_id = Column(Integer, ForeignKey('ParkingLot.parking_lot_id'), nullable=False)
    slot_number = Column(String(10), nullable=False)
    is_available = Column(Boolean, nullable=False)
    parking_lot = relationship('ParkingLot', back_populates='slots')
    bookings = relationship('Booking', back_populates='parking_slot')
