from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .parkingSlot import ParkingSlot


class ParkingLot(Base):
    __tablename__ = 'ParkingLot'
    __parkingLotId = Column("parking_lot_id", Integer, primary_key=True, autoincrement=True)
    __name = Column("name", String(50), nullable=True)
    __location = Column("location", String(100), nullable=False)
    __slots = relationship('ParkingSlot', back_populates='parking_lot')

    @property
    def getName(self) -> str:
        return self.__name

    @property
    def getLocation(self) -> str:
        return self.__location

    @property
    def getAllSlots(self) -> list:
        return self.__slots
