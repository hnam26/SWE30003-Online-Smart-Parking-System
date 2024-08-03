from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .parkingSlot import ParkingSlot

Base = declarative_base()


class ParkingLot(Base):
    __tablename__ = 'ParkingLot'
    parking_lot_id = Column(Integer, primary_key=True, autoincrement=True)
    location = Column(String(100), nullable=False)
    slots = relationship('ParkingSlot', back_populates='parking_lot')
