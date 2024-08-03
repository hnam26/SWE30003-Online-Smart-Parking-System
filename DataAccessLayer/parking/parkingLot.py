from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from .parkingSlot import ParkingSlot  # Use relative import for ParkingSlotTable
from typing import List

Base = declarative_base()


class ParkingLotTable(Base):
    __tablename__ = 'ParkingLot'
    parking_lot_id = Column(Integer, primary_key=True, autoincrement=True)
    location = Column(String(100), nullable=False)
    slots = relationship('ParkingSlotTable', back_populates='parking_lot')


class ParkingLot:
    def __init__(self, name: str, slots: List[ParkingSlot], location: str):
        self.__name = name
        self.__slots = slots
        self.__location = location

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getAllSlots(self) -> List[ParkingSlot]:
        return self.__slots

    def addSlot(self, slot: ParkingSlot):
        self.__slots.append(slot)

    def getLocation(self) -> str:
        return self.__location

    def setLocation(self, location: str):
        self.__location = location

    def getAllAvailableSlots(self) -> List[ParkingSlot]:
        return [slot for slot in self.__slots if slot.getIsAvailable()]
