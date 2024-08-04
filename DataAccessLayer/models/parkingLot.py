from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .parkingSlot import ParkingSlot


class ParkingLot(Base):
    __tablename__ = 'ParkingLot'
    parking_lot_id = Column(Integer, primary_key=True, autoincrement=True)
    location = Column(String(100), nullable=False)
    slots = relationship('ParkingSlot', back_populates='parking_lot')
